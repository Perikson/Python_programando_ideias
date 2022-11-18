""""""
"""
Sorted e Reversed

- Sorted: Semelhante ao sort. Porém, sort é utilizado apenas em listas e sorted em 
qualquer iterável

- Retorna uma lista com os elementos de um iterável ordenados

# Exemplos de sorted
notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
print(sorted(notasL))

notasT = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
print(sorted(notasT))

notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
print(sorted(notasC))

#Inverter o sorted
print(sorted(notasT, reverse=True))

- Reversed: Semelhante ao reverse. Porém, reverse é utilizado apenas em listas e 
reversed em qualquer iterável

- Retorna um objeto do tipo list_reverseiterator com os elementos de um iterável invertidos

#Exemplos de Reversed
notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
print(reversed(notasL))
print(list(reversed(notasL)))

notasT = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
print(list(reversed(notasT)))

notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
#print(list(reversed(notasC))) #TypeError

#Iterar sobre o reversed
notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
for nota in reversed(notasL):
    print(nota, end=' ')
"""