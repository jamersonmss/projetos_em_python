# Solicita ao usuário as informações do aluno
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
faltas = int(input("Digite o total de faltas: "))

# Calcula a média do aluno
media = (nota1 + nota2) / 2

# Calcula o percentual de presença do aluno
assid = (20 - faltas)  /  20 

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6 and assid >= 0.7:
    resultado = "Aprovado"
elif media < 6 and assid < 0.7:
    resultado = "Reprovado por média e por faltas"
elif media < 6:
    resultado = "Reprovado por média"
elif assid < 0.7:
    resultado = "Reprovado por faltas"
else:
    print ("Erro")

# Imprime o resultado para o usuário
print("Nome do aluno:", nome)
print("Média:", media)
print("Assiduidade:", str(assid*100)+"%")
print("Resultado:", resultado)
