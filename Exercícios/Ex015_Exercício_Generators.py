""""""
"""
1 - A partir da lista apresentada, criar um Generator contendo apenas animais que comecem com 
'C' ou 'A' e que o tamanho de seu nome seja maior que 5. Por fim, itere e imprima o Generator.

listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha', 
'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

# 1
listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha',
'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

GenAnimais = (animal for animal in listaAnimais if (animal[0] == 'C' or animal[0] == 'A') and
              len(animal) > 5)

#O generator executa o seguinte: para cada animal na lista 'listaAnimais', se o nome do animal começar
#com 'C' ou 'A', e o nome do animal ter mais de 5 letras, armazene o nome em GenAnimais.

print(GenAnimais)
for animal in GenAnimais:
    print(animal, end=' ')

"""