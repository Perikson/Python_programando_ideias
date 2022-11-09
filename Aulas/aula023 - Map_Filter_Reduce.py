""""""
"""
Map, Filter e Reduce

- Funções predefinidas integradas à linguagem

- Map: Aplica um iterável em uma função, gerando um resultado para cada elemento do iterável.

Sintaxe: map(função, iterável)

#Exemplos de map

def maiorq10(num):
    if num > 10:
        print('Maior')
    else:
        print('Menor')

#maiorq10(27)
#maiorq10(8)

numeros = [4, 6, 5, 91, 8, 7, 14, 16, 98, 4, 1.3, 75.4, 3]

result = map(maiorq10, numeros)
print(result) #Retorna um map object
print(type(result))

print(list(result))
#print(list(result)) #Os valores se perdem após sua utilização

# Map com lambda
nascimento = lambda dado: f'Ano de nascimento: {dado[0] - dado[1]}'

dados = [(1998, 22), (1815, 88), (2027, 3)]

print(list(map(nascimento, dados)))

- Filter: Filtra dados originados de uma função ou coleção de dados.

Sintaxe: filter(função, iterável)

# Exemplos de filter
import math
numeros = [1, 4, 1, 3, 5, 6, 3, 2, 9, 7, 4, 6, 9]
result = filter(lambda num: num > math.pi, numeros)

print(result) #Retorna um filter object
print(type(result))

print(list(result)) #Os valores se perdem após sua utilização
print(list(result))

'''
def qualquer(*args):
    for num in args:
        if num > math.pi:
            return True
        else:
            return False
'''

# Filter com map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#POR PARTES:
#filter(lambda num: num % 2 == 0, numeros)

#map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros))

result = list(map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros)))
print(result)

- Reduce: Relaciona dados posteriores de uma coleção com o resultado da relação de 
dados anteriores

Sintaxe: reduce(função, iterável)

#Obs.: A partir do Python3+ a função reduce() não é mais integrada (built-in). Agora temos 
que importar e utilizar essa função a partir do módulo 'functools'

#Exemplos de reduce
from functools import reduce

numeros = [2, 1, 2, 3]

result = reduce(lambda x, y: x ** y, numeros)
print(result)

#Obs.: Utilize reduce apenas se realmente for necessário, usar um loop for é 
# mais legível em 99% das vezes - Guido Van Rossum
"""