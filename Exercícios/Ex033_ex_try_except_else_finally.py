"""
Aplique o procedimento Try/Except/Else/Finally no seguinte código que realiza um cadastro de formulário
para uma pessoa realizar uma viagem:
"""


opcoes_viagem = {1:'EUA',2:'Franca',3:'Japao',4:'Brasil'}
try:
    nome = input('Digite seu nome: ')
# Caso for possível fazer a transformação quer dizer que o usuario colocou um numero ao inves de letra

    teste = int(nome)
except ValueError: #Caso dê erro quer dizer que nome contem letras
    try:
        idade = int(input('Digite sua idade:'))
    except ValueError: #Caso idade receba letras faça:
        print('Idade deve conter apenas numeros')
    else:
        try:
            lugar = int(input('Digite o numero para escolha do lugar: \n '
                              '1 - EUA \n '
                              '2 - Franca \n '
                              '3 - Japao \n '
                              '4 - Brasil \n'))
        except ValueError: # Caso a opcao de lugar seja uma letra faça:
            print('Voce deve escolher um numero de 1 a 4')
        else:
            try:
                pais = opcoes_viagem[lugar]
# Caso o usuario digite um numero,mas está fora do intervalo de 1 a 4 faça:
            except KeyError:
                print('Voce digitou um numero fora do intervalo de 1 a 4')
else: #Caso digite numero em nome faça:
    print('AVISO! Nome deve ser escrito com letras apenas.')
finally: #Sempre executado:
    print('Cadastro finalizado!')

