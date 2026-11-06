import tkinter as tk
from tkinter import messagebox


def converter_valor(texto):
    """
    Converte valores digitados nos formatos:
    1500
    1500,00
    1.500,00
    1500.00
    R$ 1.500,00
    """
    texto = texto.strip()

    if texto == "":
        return 0.0

    texto = texto.replace("R$", "").replace(" ", "")

    # Formato brasileiro: 1.500,00
    if "," in texto:
        texto = texto.replace(".", "")
        texto = texto.replace(",", ".")

    try:
        valor = float(texto)

        if valor < 0:
            raise ValueError

        return valor
    except ValueError:
        raise ValueError(f"Valor inválido: {texto}")


def moeda(valor):
    """
    Formata número como moeda brasileira.
    1500.5 -> R$ 1.500,50
    """
    numero = f"{valor:,.2f}"
    numero = numero.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {numero}"


def calcular():
    campos = {
        "Receita Bruta": entry_receita,
        "Despesas da Empresa": entry_despesas,
        "Dependentes": entry_dependentes,
        "Educação": entry_educacao,
        "Saúde": entry_saude,
        "Outros": entry_outros,
    }

    valores = {}

    # Volta todos os campos para a cor normal
    for entry in campos.values():
        entry.config(bg="white")

    # Valida cada campo individualmente
    for nome, entry in campos.items():
        try:
            valores[nome] = converter_valor(entry.get())
        except ValueError:
            entry.config(bg="#ffd6d6")
            entry.focus_set()

            messagebox.showerror(
                "Valor inválido",
                f'O campo "{nome}" contém um valor inválido.\n\n'
                "Use um dos formatos abaixo:\n"
                "1500\n"
                "1500,00\n"
                "1.500,00\n\n"
                "Não é necessário digitar R$."
            )
            return

    receita_bruta = valores["Receita Bruta"]
    despesas_empresa = valores["Despesas da Empresa"]
    dependentes = valores["Dependentes"]
    educacao = valores["Educação"]
    saude = valores["Saúde"]
    outros = valores["Outros"]

    if receita_bruta <= 0:
        entry_receita.config(bg="#ffd6d6")
        entry_receita.focus_set()

        messagebox.showwarning(
            "Receita necessária",
            "Informe uma Receita Bruta maior que zero."
        )
        return

    # ===============================
    # CÁLCULOS ORIGINAIS
    # ===============================

    receita_liquida = receita_bruta - despesas_empresa
    parcela_isenta = receita_bruta * 0.32

    deducoes_totais = (
        dependentes
        + educacao
        + saude
        + outros
    )

    base_ir = (
        receita_liquida
        - deducoes_totais
        - parcela_isenta
    )

    if base_ir < 0:
        base_ir = 0

 
    # Faixas mantidas apenas para fins de demonstração.
    # Validar valores e regras tributárias antes do uso fiscal.
    if base_ir <= 2112:
        imposto = 0
    elif base_ir <= 2826.65:
        imposto = base_ir * 0.075 - 158.40
    elif base_ir <= 3751.05:
        imposto = base_ir * 0.15 - 370.40
    elif base_ir <= 4664.68:
        imposto = base_ir * 0.225 - 651.73
    else:
        imposto = base_ir * 0.275 - 884.96

    if imposto < 0:
        imposto = 0

    # ===============================
    # RESULTADO NA PRÓPRIA JANELA
    # ===============================

    resultado_texto.set(
        f"Receita líquida:              {moeda(receita_liquida)}\n"
        f"Parcela isenta (32%):         {moeda(parcela_isenta)}\n"
        f"Deduções informadas:          {moeda(deducoes_totais)}\n"
        f"Base de cálculo estimada:     {moeda(base_ir)}\n"
        f"\nImposto estimado:             {moeda(imposto)}"
    )


def limpar():
    for entry in entries:
        entry.delete(0, tk.END)
        entry.config(bg="white")

    entry_outros.insert(0, "0,00")
    resultado_texto.set("")
    entry_receita.focus_set()


# =====================================
# INTERFACE
# =====================================

root = tk.Tk()

root.title("Calculadora MEI de Serviços")
root.geometry("620x620")
root.resizable(False, False)

# Título
titulo = tk.Label(
    root,
    text="Calculadora MEI de Serviços",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=(20, 5))


# Orientação
orientacao = tk.Label(
    root,
    text=(
        "Como preencher\n\n"
        "Informe os valores em reais usando números.\n"
        "Exemplos aceitos: 1500 | 1500,00 | 1.500,00\n"
        "Campos sem valor serão considerados R$ 0,00."
    ),
    justify="center",
    fg="#444444"
)

orientacao.pack(pady=(0, 15))


# Formulário
frame = tk.Frame(root)
frame.pack(padx=30)


def criar_campo(texto, linha):
    label = tk.Label(
        frame,
        text=texto,
        anchor="w",
        width=25
    )

    label.grid(
        row=linha,
        column=0,
        padx=5,
        pady=6,
        sticky="w"
    )

    entry = tk.Entry(
        frame,
        width=25,
        font=("Arial", 11)
    )

    entry.grid(
        row=linha,
        column=1,
        padx=5,
        pady=6
    )

    return entry


entry_receita = criar_campo(
    "Receita Bruta (R$):",
    0
)

entry_despesas = criar_campo(
    "Despesas da Empresa (R$):",
    1
)

entry_dependentes = criar_campo(
    "Dependentes (R$):",
    2
)

entry_educacao = criar_campo(
    "Educação (R$):",
    3
)

entry_saude = criar_campo(
    "Saúde (R$):",
    4
)

entry_outros = criar_campo(
    "Outros (R$):",
    5
)


entries = [
    entry_receita,
    entry_despesas,
    entry_dependentes,
    entry_educacao,
    entry_saude,
    entry_outros
]


# Valores iniciais
for entry in entries:
    entry.insert(0, "0,00")

# Receita começa selecionada
entry_receita.selection_range(0, tk.END)
entry_receita.focus_set()


# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=15)


btn_calcular = tk.Button(
    frame_botoes,
    text="Calcular",
    command=calcular,
    width=15,
    font=("Arial", 10, "bold")
)

btn_calcular.grid(
    row=0,
    column=0,
    padx=5
)


btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar,
    width=15
)

btn_limpar.grid(
    row=0,
    column=1,
    padx=5
)


# Resultado

resultado_frame = tk.LabelFrame(
    root,
    text="Resultado estimado",
    padx=20,
    pady=15
)

resultado_frame.pack(
    padx=30,
    pady=10,
    fill="both"
)


resultado_texto = tk.StringVar()


resultado_label = tk.Label(
    resultado_frame,
    textvariable=resultado_texto,
    justify="left",
    anchor="w",
    font=("Courier", 11)
)

resultado_label.pack(
    fill="both"
)


# Aviso
aviso = tk.Label(
    root,
    text=(
        "Atenção: ferramenta de simulação.\n"
        "As regras tributárias devem ser validadas antes do uso fiscal."
    ),
    fg="#8a5a00",
    justify="center",
    font=("Arial", 9)
)

aviso.pack(pady=10)


# Enter calcula
root.bind("<Return>", lambda event: calcular())

# Esc limpa
root.bind("<Escape>", lambda event: limpar())


root.mainloop()