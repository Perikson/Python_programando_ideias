""""""
"""
1 - Realizar a média das notas de 4 alunos. 

2 - Converter uma temperatura de graus °C para ºF e para K.
Dados: ºF = ºC * 1.8 + 32, K = ºC + 273.15


# 1
notaPedro = int(input('Digite a nota de Pedro: ')) #Recebendo a nota dos alunos
notaPaula = int(input('Digite a nota de Paula: '))
notaPatricia = int(input('Digite a nota de Patricia: '))
notaPablo = int(input('Digite a nota de Pablo: '))

media = (notaPedro + notaPaula + notaPatricia + notaPablo) / 4 #Obtendo a média
print(f'Média das notas: {media}')

# 2
# ºF = ºC * 1.8 + 32
tempC = float(input('Temperatura em ºC: '))
tempF = tempC * 1.8 + 32 #Convertendo a temperatura
print(f'A temperatura em ºF é: {tempF}ºF\n')

# K = ºC + 273.15
#tempC = float(input('Temperatura em ºC: '))
tempK = tempC + 273.15 #Convertendo a temperaura
print(f'A temperatura em K é: {tempK}K')
"""
