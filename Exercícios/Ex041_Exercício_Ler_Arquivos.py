""""""
"""
1 - Crie um arquivo de texto na pasta onde está seu programa Python. O arquivo deve conter 
alguns números de 4 dígitos separados por linha, representando números de uma rifa. Após isso, 
itere no arquivo para colocar os valores em uma lista. Por fim, utilize a função choice() para 
determinar o ganhador.

# 1

from random import choice as ch

numerosRifa = []
with open('Rifa.txt') as rifa:
    for num in rifa: #Itera em cada linha do arquivo
        numerosRifa.append(int(num)) #int(num) para remover o '\n'

print(f'Número vencedor: {ch(numerosRifa)}. Parabéns!')
"""