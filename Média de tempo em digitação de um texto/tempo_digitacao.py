## importação de métodos
import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repet = 5

## Explicação do programa:
print ('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitá-la ' + str (repet) + ' vezes')
input ('Aperte enter para começar. ')

while vez <= repet:
    inicio = t.time()
    input ('Digite a palavra: ')
    fim = t.time()
    tempo = round (fim-inicio, 2)
    tempos.append (tempo)
    vezes.append(vez)
    vezstr = str (vez) + 'a vez'
    legenda.append (vezstr)
    vez += 1

plt.xticks (vezes, legenda)
plt.plot (vezes, tempos)
plt.show()





    
