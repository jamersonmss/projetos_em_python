# Solicita ao usuário as informações do aluno
nome = input('Digite o nome do aluno: ')

valid_nota = False
while valid_nota == False:
    nota1 = input('Digite a nota da prova 1: ')
    try:
        nota1 = float (nota1)
        if nota1 < 0 or nota1 > 10:
            print ('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True                
    except:
        print ('Nota inválida. Use apenas números e separe os decimais com ponto. (Ex. 9.5) ')

valid_nota = False
while valid_nota == False:
    nota2 = input('Digite a nota da prova 2: ')
    try:
        nota2 = float (nota2)
        if nota2 < 0 or nota2 > 10:
            print ('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True                
    except:
        print ('Nota inválida. Use apenas números e separe os decimais com ponto. (Ex. 9.5) ')

        
valid_faltas = False
while valid_faltas == False:
    faltas = input('Digite o total de faltas: ')
    try:
        faltas = float (faltas)
        if faltas < 0 or faltas > 20:
            print ('Total de faltas inválido. Valor deve ser entre 0 e 20.')
        else:
            valid_faltas = True                
    except:
        print ('Total de faltas inválido. Use apenas números e separe os decimais com ponto. (Ex. 15.5) ')
    

# Calcula a média do aluno
media = (nota1 + nota2) / 2

# Calcula o percentual de presença do aluno
assid = (20 - faltas)  /  20 

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'
elif media < 6 and assid < 0.7:
    resultado = 'Reprovado por média e por faltas'
elif media < 6:
    resultado = 'Reprovado por média'
elif assid < 0.7:
    resultado = 'Reprovado por faltas'
else:
    print ('Erro')

# Imprime o resultado para o usuário
print('Nome do aluno:', nome)
print('Média:', media)
print('Assiduidade:', str(assid*100)+'%')
print('Resultado:', resultado)
