""""""
"""
1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de
Fibonacci em uma lista. N é definido pelo usuário. Ao encontrar os termos, imprimir a lista 
e finalizar a função.

2 - Criar 5 funções: uma para um cadastro, outra para realizar o login, outra para mudar a senha, 
outra para realizar logout e ainda uma para definir qual opção o usuário deseja escolher.
Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a opção 'sair').
Atente-se às regras:
    - Só é possível realizar um cadastro se não houver nenhum anterior.
    - Só é possível realizar login se houver um cadastro.
    - Só é possível realizar login se o usuário informar corretamente username e senha.
    - Só é possível alterar a senha se o usuário estiver logado.
    - Só é possível alterar a senha se o usuário informar corretamente a senha atual.
    - Só é possível realizar logout se o usuário estiver logado.

# 1

listaSF = []
stop = 0

def fibonacci(stop, a, b, aux): #1, 1, 2, 3, 5, 8, 13, 21, 34...
    global listaSF #Utiliza uma variável global dentro de uma função
    listaSF.append(a) #Adiciona os valores na lista 'listaSF'
    a, b = b, a + b #Acumula os valores para determinar os proximos numeros da sequencia.
#Essa é a logica da sequencia de fibonacci, o proximo termo é sempre a soma dos dois
# termos anteriores
    aux += 1
    if stop == aux:
        print(listaSF)
        return 0
    else:
        return fibonacci(stop, a, b, aux) #Chama a própra função até que stop == aux.

while stop < 1:
    stop = int(input('Digite a quantidade de termos: '))

fibonacci(stop, a=1, b=1, aux=0)

# 2

login = False
cadastroFeito = False
op = 0
username = ' '
senha = ' '

def intro():
    global op
    global cadastroFeito
    global login
    while op != 5:
        print('1 - Cadastro\n2 - Login\n3 - Mudar senha\n4 - Logout\n5 - Sair')
        op = int(input('______Opção: '))

        if op == 1:
            if not cadastroFeito: #Se não exitir nenhum cadastro anteriror
                cadastro()
            else: #Caso já foi feito um cadastro antes:
                print('__________Cadastro já feito anteriormente_________')

        elif op == 2:
            if cadastroFeito:
                loginSistema()
            else:
                print('__________Faça o cadastro antes de fazer login__________')

        elif op == 3:
            if cadastroFeito:
                mudarSenha()
            else:
                print('__________Faça o cadastro antes de alterar a senha_________')

        elif op == 4:
            if login:
                logout()
            else:
                print('__________Para dar logout primeiro tem que fazer login né')

        elif op == 5:
            return 0

def cadastro():
    global username
    global senha
    global cadastroFeito
    username = input('__________Digite seu nome de usuário: ')
    senha = input('__________Digite sua senha: ')
    cadastroFeito = True
    return intro() #Chama a função intro() de novo

def loginSistema():
    global username
    global senha
    global login
    if not login:
        testeUsuario = input('__________Username: ')
        testeSenha = input('__________Senha: ')

        if testeUsuario == username and testeSenha == senha: #Teste se usuario e senha
    # estão corretos
            login = True

    if login:
        print('_________Você está logado!__________')
    else:
        print('__________Username ou senha incorretos__________')

    return intro()

def mudarSenha():
    global login
    global senha
    if login:
        testeSenha = input('__________Senha atual: ')
        if testeSenha == senha:
            senha = input('__________Digite sua nova senha: ')
        else:
            print('__________Senha atual incorreta__________')
    else:
        print('___________Faça login antes__________')

    return intro()

def logout():
    global login
    login = False
    print('__________Deslogado!__________')
    return intro()

intro() #Chama a função intro() pela primeira vez, iniciando o sistema.

"""