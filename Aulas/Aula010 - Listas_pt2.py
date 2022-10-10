""""""
"""
# Exemplos de declaração de listas:
lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

# Obs.: Listas são ordenadas, ou seja, seus índices são importantes.

listaNova = []
for numero in range(1, 11):
    listaNova.append(numero)

print(listaNova)

listaNova2 = list(range(1, 11))
print(listaNova2)

# Percorrer listas (iterar)

# For
for elemento in lista2:
    print(elemento, end=' ')

total = 0
for elemento in lista2:
    total = total + elemento
print(f'\n{total/len(lista2)}')

# While

total = 0
cont = 0
while len(lista2) != 0:
    total = total + lista2.pop()
    cont = cont + 1
print(total/cont)

# Obter indices da lista
jogos = ['Sonic', 'Super Mario', 'GTA', 'GoW', 'PES']
for indice, jogo in enumerate(jogos):
    print(indice, jogo)
    
print(lista2.index(2))

print(lista2.index(8)) # Primeiro 8 encontrado
#print(lista2.index(80)) #ValueError

print(lista2.index(5, 4)) #Busca A PARTIR do índice 4
#print(lista2.index(5, 20)) #ValueError

print(lista2.index(5, 3, 6)) # Busca ENTRE os índices 3 e 6

# Descompactar listas

animal, cor, letra = lista5
print(animal)
print(cor)
print(letra)

#animal, cor, letra, outraCoisa = lista5 #ValueError

lista5.append('Peppa Pig')
print(lista5)
animal, cor, letra = lista5 #ValueError

# Funções úteis para trabalhar com listas
# Obs.: Apenas para inteiros ou floats
print(sum(lista2)) # Retorna a soma dos elementos
print(max(lista2)) # Retorna o maior valor
print(min(lista2)) # Retorna o menor valor

# Arredondar os valores da lista
listaPlana = [1.22, 2.984367, 9.23184832, 4.51]

for elemento in listaPlana:
    print(round(elemento))
    
# Obter o módulo de uma lista
listaPessimista = [-1, -2, -5, -10, 1000]

for numero in listaPessimista:
    print(abs(numero))

# Copiar uma lista - Deep Copy
print(lista2)
lista1 = lista2.copy()
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

# Obs.: A deep copy copia as listas e as torna independentes entre si, ou seja,
# quaqluer modificação em uma NÃO afeta a outra.

# Copiar uma lista - Shallow Copy
print(lista2)
lista1 = lista2
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

# Obs.: A shallow copy copia as listas e as conecta, ou seja,
# qualquer modificação em uma AFETA a outra.

# Matrizes

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

# Obs.: Cada lista interna é uma linha da matriz

#print(matriz[0])
#print(matriz[1])
#print(matriz[2])

#for linha in matriz:
#    print(linha)

#print(matriz[0][2]) #3
#print(matriz[2][2]) #9
#print(matriz[1][0]) #4

#for linha in matriz:
#    for numero in linha:
#        print(numero)

# Jogo de Velha com matriz

matriz = [[' ', ' ', ' '], [' ', 'O', 'X'], [' ', ' ', ' ']] #Matriz 3x3

print(matriz[0])
print(matriz[1])
print(matriz[2])

LP1 = int(input('Escolha a linha: '))
CP1 = int(input('Escolha a coluna: '))
matriz[LP1][CP1] = 'X'

LP2 = int(input('Escolha a linha: '))
CP2 = int(input('Escolha a coluna: '))
matriz[LP2][CP2] = 'O'

for linha in matriz:
    print(linha)
"""