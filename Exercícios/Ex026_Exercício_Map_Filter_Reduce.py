""""""
"""
1 - Calcule o fatorial de n utilizando loop for, e depois utilizando reduce. O resultado é o mesmo? 

2 - Realizar o calculo do IMC através de uma função utilizando map com os dados fornecidos abaixo 
sobre peso e altura, e salvar os resultados em outra lista. Apó isso, aplicar o filter para separar 
pessoas obesas (IMC > 25).

Dados:
índice 0 das tuplas: peso (kg)
índice 1 das tuplas: altura (m)
listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112, 1.63), (98, 1.59)]



# 1

#Utilizando loop for
n = int(input('Fatorial de: '))
fat = 1

for i in range(1, n+1): #O range deve começar em 1, pois se houvesse uma multiplicação por 0, o
#resultado seria 0. E deve terminar em n+1 para o valor de n ser incluído na multiplicação.
    fat *= i #Multiplica todos os termos do range

print(f'Fatorial loop for: {fat}')
'''
Ex.: n = 4
range(1, 5) = 1, 2, 3, 4
(1) fat = fat * 1 = 1
(2) fat = fat * 2 = 2
(3) fat = fat * 3 = 6
(4) fat = fat * 4 = 24
'''

#Utilizando reduce
from functools import reduce #Importando a função reduce()

lista = [1] #Colcoando o valor 1 como primeiro elemento da lista, para não haver
# problema caso o usuário escolha n == 0.

lista.extend(range(1, n+1))

fat = reduce(lambda x, y: x * y, lista)
print(f'Fatorial reduce: {fat}')


# 2

#Map
listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112, 1.63), (98, 1.59)]

def calculoIMC(amostra):
    imc = amostra[0] / (amostra[1] ** 2)
    return imc #Retorna o valor do imc calculado

imc = map(calculoIMC, listaAmostras)
# Pode-se substituir a função com uma função lambda.: imc = map(lambda x: x[0] / (x[1] ** 2), listaAmostras) 

resultadoIMC = list(imc)
resultIMC = []

for num in resultadoIMC:
    resultIMC.append(round(num)) #Arredonda os valores da lista 'resultadoIMC' e adiciona cada um
# na lista 'resultIMC'.

print(resultIMC)

#Filter
#IMC > 25 -> Sobrepeso
sobrepeso = filter(lambda imc: imc > 25, resultIMC) #Testa se os valores da lista 'resultIMC' são
#maiores do que 25
print(f'IMCs acima do peso: {list(sobrepeso)}')




"""