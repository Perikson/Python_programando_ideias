""""""
"""
1 - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência).
Peça a operação desejada e depois os dois números ao usuário.


# 1
print('1 - Soma\n2 - Multiplicacao\n3 - Divisao Inteira\n4 - Potencia')
op = int(input('Escolha uma operação: '))
num1 = float(input('Primeiro numero: ')) #Convertendo o numero para float
num2 = float(input('Segundo numero: '))

if op == 1: #Testando o valor de 'op' para determinar o operador
    print(f'Soma: {num1 + num2}')
elif op == 2:
    print(f'Multiplicacao: {num1 * num2}')
elif op == 3:
    print(f'Divisao Inteira: {num1 // num2}')
elif op == 4:
    print(f'Potencia: {num1 ** num2}')
else:
    print('Digite uma opcao valida!')
"""
