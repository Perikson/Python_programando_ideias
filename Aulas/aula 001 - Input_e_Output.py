""""""
"""
Input e Output

Output - print(): Apresenta dados para o usuário

Input - input(): Recebe dados do usuário

# Obs.: Os dados recebidos são do tipo String.

#print('Digite uma cor: ')
#cor = input()

# Versões 2.x
#print('Voce escolheu a cor %s' % cor)

# versões 3.x até 3.7
#print('Voce escolheu a cor {0}'.format(cor))

# Versões a partir da 3.7
#print(f'Voce escolheu a cor {cor}')

cor = input('Digite uma cor: ')

num = input('Digite um numero: ')

# Versões 2.x
#print('Voce escolheu a cor %s e o numero %s' % (cor, num))

# versões 3.x até 3.7
#print('Voce escolheu a cor {0} e o numero {1}'.format(cor, num))

# Versões a partir da 3.7
#print(f'Voce escolheu a cor {cor} e o numero {num}')

# Print sem pular linha
print('tomate')
print('tomate')
print('tomate')

print('tomate', end=' ')
print('tomate', end=' ')
print('tomate', end=' ')

# Realizar operações nas saídas (print)
num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

#print(f'A soma é: {num1 + num2}') # Erro # Concatenação

print(f'A soma é: {int(num1) + int(num2)}')

# Obs.: Casting - conversão de um tipo de dado para outro
"""