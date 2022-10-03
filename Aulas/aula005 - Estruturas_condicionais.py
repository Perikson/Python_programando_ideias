""""""
"""
Estruturas condicionais

if(se), elif(senão se), else(senão)

# Testar altura para brinquedo do parque
altura = float(input('Digite sua altura: '))

if altura < 1.6:
    print('Saia daqui')
else:
    print('Voce pode brincar!')
    
# Consultar média final para aprovação
nota = float(input('Digite a sua nota: '))
'
if nota > 6:
    print('Pode curtir suas férias')
elif nota == 6:
    print('Pode curtir suas férias')
else:
    print('Te vejo ano que vem outra vez')
'

if nota >= 6:
    print('Pode curtir sua ferias')
else:
    print('te vejo ano que vem outra vez')
    
# Determinar se um numero é par ou ímpar
num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')

if num % 2 == 1:
    print(f'{num} é ímpar')
else:
    print(f'{num} é par')


# Utilizando outros tipo de dados
# Strings

pais = input('Digite um pais que voce deseja visitar: ')

if pais == 'Noruega':
    print('Ah nao, muito frio!')
elif pais == 'China':
    print('Ah nao, muito longe!')
elif pais == 'Austrália':
    print('Ah nao, muito canguru!')
else:
    print('Vamos!')
    
# Boolean
login = False
senha = 'Caneta1'

key = input('Digite sua senha: ')

if key == senha:
    login = True
else:
    print('Senha incorreta!')

if login == True:
    print('Bem-vindo admin!')
else:
    print('Tente novamente!')
"""

# Cuidado com as variaveis locais e globais

login = False # Variável global
senha = 'Caneta1'
key = 'Canet'

if key == senha:
    login = True # Variável local
else:
    print('Senha incorreta')

#if login == True:
if login:
    print('Bem-vindo admin!')
else:
    print('Tente novamente!')

"""
# Lista de operadores

> - maior
< - menor
>= - maior ou igual
<= - menor ou igual
== - igual
!= - diferente
% - resto da divisão
"""