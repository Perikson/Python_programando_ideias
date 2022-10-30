"""
Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes incluindo:
nome, sexo, esporte favorito (Natação, Futebol, Volêi, Tênis) e idade. Com esses dados faça:
- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
- Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam de natação chame uma função e
  imprima um aviso de que não há homens que gostam de natação.
"""

def cadastro(): #Função que realiza a criação da lista com os dados
    list = []
    for i in range(4):
        #Criação de um dicionario para cada pessoa, facilitando
        #localizar elementos
        dicionario = dict(nome = input('Digite seu nome: '),
                          sexo = input('Digite M para masculino e F para feminino: '),
                          esporte = input('Escolha seu esporte favorito entre natacao, futebol, volei, tenis: '),
                          idade = int(input('Digite sua idade: ')))
        list.append(dicionario) #Adiciona o dicionario na lista
    return list #retorna a lista


def aviso(): #Mensagem de que não existem homens que gostam de natacao
    print('Nao tem homens que gostam de natacao')

lista = cadastro()
cont = 0 #Contar quantos homens gostam de natação
soma = 0 #Fazer a soma do numerador para calcular a media

for i in range(4):
    # Pego em cada loop uma pessoa e o dado especifico dela.
    # Ex:lista[i]['esporte'] estou pegando a pessoa do indice i da lista e dentro dela usando a chave 'esporte' para acessar
    # o elemento
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'natacao':
        soma = soma + lista[i]['idade'] #Somar a idade de todos os
                                        #homens que gostam de natacao
        cont += 1
if cont == 0: #Caso não há homens que gostam de natação faça:
    aviso()
else:
    media = soma / cont #Calcula a media
    print(f'A idade media de homens que fazem natacao é {media}') #Imprime a media de idade

