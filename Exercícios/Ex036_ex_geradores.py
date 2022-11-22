"""
Crie uma lista que armazene inteiros de um usuário em um loop até que o usuário não deseje mais adicionar,
trate o erro com try/except caso o usuário digite uma letra ao invés de um numero. Passe essa lista para
uma função geradora que reconhecerá quais são os números primos dentro da lista passada inicialmente.
Caso seja um numero primo, retorne pelo método yield, caso contrário passe para o próximo numero.
Ao final, imprima os valores retornados pelo yield em forma de tupla.
"""


def primos_list(lista): #Função que reconhece numeros primos
    for item in lista: #Para cada item dentro de lista faça:
        divisor = 1 #Variavel auxiliar para parada do while
        numero_divisores = 0 #Quantidade de divisores do item na lista
        while divisor <= item:
            if item % divisor == 0: #Se o resto da divisão de item por aux
                                #for zero faça:
                numero_divisores += 1 #Adiciona na variavel numero de
                                      #divisor
                divisor += 1 #Incrementa o auxiliar
            else:
                divisor += 1 #Incrementa o auxiliar
        # Se numero_divisores for igual a 2, temos um numero primo divisivel apenas por 1 e ele mesmo.
        if numero_divisores == 2:
            yield item #Retorna cada item

lista = [] #Declaração da lista a ser entrada pelo usuario
sair = '' #Declaração da condição de parada do while
while sair != 'sim':
    # Tente
    try:
        # Adiciona o numero que o usuario desejar convertendo para int
        lista.append(int(input('Numero: ')))
    #Caso o usuario digite um numero e não tem como converter para int gera ValueError
    except ValueError:

        print('Deve ser um numero') #Aviso
    sair = input('Deseja parar? ') #Se digitar sim o loop irá parar

#Criação uma tupla com cada elemento retornado pelo yield
tuple_primos = tuple(primos_list(lista))
#Impressão da resposta
print(f'Tupla contendo todos primos: {tuple_primos}')

