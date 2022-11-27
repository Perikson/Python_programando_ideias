""""""
"""
1 - Utilize o módulo random e suas funções para realizar os seguintes procedimentos da 
tabela abaixo:
 __________________________________________________________________________________________________
 |  nº | função    | procedimento                                                                  |
 |_________________________________________________________________________________________________|
 |  1  | random()  | Obter um número aleatório inteiro entre 1 e 10 e armazenar em uma variável X  | 
 |  2  | randint() | Obter X números aleatórios inteiros entre 0 e 100 e armazená-los em uma lista |
 |  3  | shuffle() | Embaralhar a lista                                                            | 
 |  4  | choice()  | Selecionar um elemento aleatório da lista                                     |
 |  5  | loop      | Imprimir os números da lista que são maiores que o número selecionado         |
 |_________________________________________________________________________________________________|   
    

# 1

#Importando várias funções do módulo random
from random import (
    random as rd,
    randint as ri,
    shuffle as sh,
    choice as ch
)

listaAle = []
x = round(rd() * 10) #Número aleatório multiplicado por 10 e arredondado
print(x)
for i in range(x):
    listaAle.append(ri(0, 100))

#O preenchimento poderia ser feito utilizando comprehension:
#listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

sh(listaAle) #Embaralha a lista
print(listaAle)

escolhido = ch(listaAle) #Escholhe um elemento aleatório da lista
print(f'Numero Escolhido: {escolhido}')

print('Numeros maiores que o escolhido: ', end=' ')
for i in listaAle:
    if i > escolhido:
        print(i, end=' ')

#É possível encontrar os numeros maiores utilizando filter
# maiores = filter(lambda  x: x > escolhido, listaAle)
# print(list(maiores), end=' ')
"""