"""
Exercicios de Seção
"""
"""
Faça uma função que receba um número inteiro maior que zero e retorne a soma de todos os algarismos.
Caso o valor seja negativo retorne 'Numero invalido'
Exemplo:
251 = 2 + 5 + 1 = 8
"""

def soma_algarismo(numero): #100 - 3 algarismos
    divisor = 1
    num_algarismo = 0
    while True: #Loop que descobre a quantidade de algarismos.
        if (numero // divisor) == 0: # 25 // 1 = 25; 25 // 10 = 2; 25 // 100 = 0
            break
        else:
            num_algarismo = num_algarismo + 1
            divisor *= 10
    soma = 0
    for valor in range(num_algarismo):
        soma = soma + ((numero // (10 ** valor)) % 10)
    return soma

#Ex: Como separar os digitos?
#251 = 2 * 10^2 + 5 * 10^1 + 1 * 10^0
#251 // 100 = 2
#251 // 10 = 25 % 10 = 5
#251 // 1 = 251 % 10 = 1

numero = int(input('Digite um numero: '))
if numero >= 0:
    print(soma_algarismo(numero))
else:
    print('Numero Invalido')
