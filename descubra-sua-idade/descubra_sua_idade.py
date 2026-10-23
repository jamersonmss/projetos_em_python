from datetime import date

# Solicita a data de nascimento do usuário
data_nasc = input('Digite a data de nascimento no formato dd/mm/aaaa: ')

# Converte a data de nascimento para o tipo Date
data_nasc = date.fromisoformat(data_nasc.split("/")[2] + "-" + data_nasc.split("/")[1] + "-" + data_nasc.split("/")[0])

# Calcula a idade em anos, meses e dias
hoje = date.today()
idade = hoje.year - data_nasc.year
meses = hoje.month - data_nasc.month
dias = hoje.day - data_nasc.day

# Ajusta a idade para considerar os meses e dias
if meses < 0 or (meses == 0 and dias < 0):
    idade -= 1
    meses = 12 + meses
    dias = 30 + dias

if dias < 0:
    meses -= 1
    dias = 30 + dias

# Exibe a idade em anos, meses e dias
print('Você tem', idade, 'anos,', meses, 'meses e', dias, 'dias.')
