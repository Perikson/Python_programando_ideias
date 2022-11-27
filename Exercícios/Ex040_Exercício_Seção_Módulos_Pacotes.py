""""""
"""
1 - Maria e Joao estão jogando bingo em família. Cada um possui uma cartela e cada cartela 
possui 7 números entre 1 e 30, que serão sorteados por uma função, utilizando choice(), contida em 
um módulo customizado, sendo acessada apenas se o módulo for importado. Os números 
das cartelas devem ser definidos utilizando comprehensions e choice() no programa principal. O 
primeiro a ter seus 7 números chamados vence. Crie um sistema para representar o jogo, como os 
numeros sorteados e a conferência das cartelas. No final apresente o vencedor, os números da 
cartela do vencedor e os números sorteados.


# 1

from random import choice as ch
from Exercícios.Módulo_Exercício_Bingo import sorteio

numeros = 7 #Quantidade de numeros de cada cartela
max = 30 #Limite dos numeros para sorteio (1 até max)

sorteador = list(range(1, max + 1))
cartelaMaria = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

sorteador = list(range(1, max + 1))
cartelaJoao = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]
#Escolhe um numero da lista 'sorteador'. O numero escolhido é depois removido da lista para não
# haver repetição dos numeros sorteados. Como o pop() retorna o numero removido, ele é armazenado
# no comprehension (cartelaJoao)
print(f'Cartela João: {cartelaJoao}')
print(f'Cartela Maria: {cartelaMaria}')

sorteio(cartelaJoao, cartelaMaria, max)
"""