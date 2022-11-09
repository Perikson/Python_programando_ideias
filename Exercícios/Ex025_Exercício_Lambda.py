""""""
"""
1 - Criar duas listas de mesmo tamanho preenchidas com números inteiros e retornar outra lista com 
a soma das duas listas sendo uma delas invertida (indice 0 com indice 9 para uma lista de tamanho 10, 
por exemplo), utilizando lambda e comprehensions para iterar em ambas.


# 1

lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [160, 11, 50, 22, 43, 24, -12, 24, 542, 217]
lista3 = []

lista2.reverse() #Inverte os valores da lista2
soma = lambda lista1, lista2: [lista1[ind] + lista2[ind] for ind in range(0, 10)] #Soma os elementos
#correspondentes das listas. Ex: Elemento 0 (10) + Elemento 0 (217) ...
result = soma(lista1, lista2)
lista3.append(result)
print(lista3)


# 2 - Fazendo de forma mais direta:

lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [160, 11, 50, 22, 43, 24, -12, 24, 542, 217]
lista2.reverse()

lista_3 = lambda x, y: [x[ind] + y[ind] for ind in range(len(lista1))]

print(lista_3(lista1, lista2))
"""