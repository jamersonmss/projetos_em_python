# Projetos em Python

Repositório com exercícios e projetos desenvolvidos durante meus estudos de **Python**. Aqui reúno exemplos de lógica de programação, automação simples, interfaces gráficas, consumo de APIs e análise de dados.

> Projeto de aprendizado em evolução. As aplicações têm finalidade educacional.

## Projetos

### Aplicações e exercícios

| Projeto | Descrição | Tecnologias |
|---|---|---|
| [Calculadora MEI](calculadora-mei/) | Interface para simular cálculos a partir de valores informados pelo usuário. | Python, Tkinter |
| [Calculadora de IMC](calculo-imc/) | Calcula o IMC e apresenta uma classificação conforme as regras implementadas no exercício. | Python |
| [Descubra sua idade](descubra-sua-idade/) | Calcula idade em anos, meses e dias a partir da data de nascimento. | Python, `datetime` |
| [Tempo de digitação](tempo-digitacao/) | Cronometra tentativas de digitação e exibe os tempos em um gráfico. | Python, Matplotlib |
| [Média do aluno](nota/) | Calcula média, assiduidade e resultado com base nas notas e faltas informadas. | Python |
| [Weather App](weather_app/) | Consulta condições atuais e previsão do tempo para uma localização. | Python, Requests, AccuWeather, Mapbox |
| [Fatura de produtos](Fatura.py) | Registra produtos e preços e calcula o total da fatura. | Python |
| [Exercício introdutório](curso-python/aula1.py) | Exercício inicial com saída de mensagens no terminal. | Python |

### Estudos de Machine Learning

| Conteúdo | Descrição | Tecnologias |
|---|---|---|
| [Notebooks de Machine Learning](curso_machine_learning/) | Exercícios e experimentos com conjuntos de dados Iris e Digits, além de regressão linear e publicidade. | Jupyter Notebook, Python, scikit-learn |

## Como executar

Clone o repositório e acesse a pasta do projeto que deseja executar:

```bash
git clone https://github.com/jamersonmss/projetos_em_python.git
cd projetos_em_python
```

Os exercícios de terminal podem ser iniciados com `python` e o caminho do arquivo. Por exemplo:

```bash
python calculo-imc/IMC.py
```

Para o projeto de tempo de digitação, instale a dependência antes:

```bash
python -m pip install matplotlib
python tempo-digitacao/tempo_digitacao.py
```

O **Weather App** requer as bibliotecas e credenciais descritas em [weather_app/README.md](weather_app/README.md). A **Calculadora MEI** abre uma janela gráfica com Tkinter; confira os requisitos e o aviso educacional no [README do projeto](calculadora-mei/calculadora-mei/README.md).

Os notebooks podem ser abertos no Jupyter Notebook ou JupyterLab. Dependendo do notebook, pode ser necessário instalar bibliotecas como `pandas`, `matplotlib` e `scikit-learn`.

## Objetivos de aprendizado

- Praticar variáveis, condicionais, laços e funções;
- Trabalhar com entrada e validação de dados;
- Explorar bibliotecas e APIs externas;
- Criar gráficos, interfaces gráficas e notebooks;
- Aprender a organizar projetos e versionar código com Git e GitHub.

## Observação

Este repositório reúne exercícios de estudo e pode conter projetos em diferentes estágios de desenvolvimento. Os resultados devem ser entendidos dentro do contexto educacional de cada projeto.
