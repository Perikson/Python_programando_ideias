""""""
"""
1 - Crie um sistema de cadastro e login de um site, utilizando um username e senha informados pelo usuário.

# 1
login = False
print('Bem-vindo(a) ao cadastro do site!')
user = input('Crie seu nome de usuário: ')
senha = input('Crie sua senha: ')

print('\n__________LOGIN__________')
if input('Usuário: ') == user and input('Senha: ') == senha: #Testando as duas condições com o 'and'
    login = True


if login: #if login == True
    print(f'\nBem-vindo(a) {user}')
else:
    print('\nTente novamente!')


#Obs: É possível desenvolver o teste de login de outros modos
#e utilizando outros operadores, por exemplo:

'''
if not login: #Utilizando o 'not' e trocando os prints
    print('\nTente novamente!')
else:
    print(f'\nBem-vindo(a) {user}')
'''
'''
if login is True: #Utilizando o 'is'
    print(f'\nBem-vindo(a) {user}')
else:
    print('\nTente novamente!')
'''

"""
