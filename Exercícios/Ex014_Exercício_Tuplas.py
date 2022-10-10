""""""
"""
1 - Kiko precisa invadir uma prisão de segurança extremamente alta para resgatar Jaiminho. Porém, 
existem 3 portões protegidos por senhas do TIPO TUPLA. Cada portão oferece uma dica para 
descobrir a senha. A dica é composta por uma tupla contendo algumas dezenas, e uma frase indicando 
o processo a ser realizado. Kiko deve criar um programa que imprima na tela as três senhas no 
seguinte formato: print(f'Portão X: {senha_do_portão_X}').

# Dicas
Portao 1 = (29, 54, 45) [Alterar todas as dezenas para 0]

Portao 2 = (12, 28, 37, 54) [A soma dos elementos 2 e 3 é o primeiro elemento da senha, a soma 
dos elementos 1 e 4 é o segundo elemento da senha]

Portao 3 = (16, 86, 78, 32, 85, 12) [O valor mínimo é o primeiro elemento da senha, o valor 
máximo é o segundo elemento da senha]

# 1
portao1 = (29, 54, 45)
portao2 = (12, 28, 37, 54)
portao3 = (16, 86, 78, 32, 85, 12)

#Portão 1
senha1 = list(portao1)
for id in range(0, 3): #0, 1, 2
    senha1[id] = 0

portao1 = tuple(senha1)
print(f'Portão 1: {portao1}')

#A tupla 'portao1' é convertida para a lista 'senha1'. Assim, é possível editar
# seus dados, substituindo todos por 0. Em seguida, senha1 é convertida para a tupla 'portao1' e
# é impressa, abrindo o Portão 1.

#Portão 2
portao2 = (portao2[1] + portao2[2], portao2[0] + portao2[3])
print(f'Portão 2: {portao2}')

#São somados os elementos 2 e 3 da tupla 'portao2', em seguida os elementos 1 e 4 tambem sao somados.
#A tupla 'portao2' é recriada, com os novos valores, e é impressa, abrindo o Portão 2.

#Portão 3
portao3 = (min(portao3), max(portao3))
print(f'Portão 3: {portao3}')

#A tupla 'portao3' é recriada com os elementos min e max da tupla 'portao3' original. Em seguida,
# é impressa, abrindo o Portão 3.

"""