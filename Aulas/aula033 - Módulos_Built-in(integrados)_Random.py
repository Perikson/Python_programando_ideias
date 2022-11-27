""""""
"""
Módulos Integrados e Módulo Random

- Módulos são arquivos Python que podem ser importados para o arquivo principal, 
geralmente contendo funções.

-  Módulo Random: possui funções que retornam valores pseudo-aleatórios. 
Porém, consideremos aleatorios.

#Modo 1 de importação
import random

#Obs.: Neste modo, TODO o módulo é importado, ou seja,
# todas as classes, funções e atributos ficarão disponiveis na memória.

#Função random: Retorna um número real aleatório entre 0 e 1(exclusivo)
print(random.random())

#Modo 2 de importação
from random import randint

#Obs.: Neste modo APENAS a função é importada

# Função Randint: Retorna um numero inteiro aleatória entre os valores dos parâmetros
print(randint(1, 60))

# Função uniform: Retorna um numero real aleatório entre os valores dos parâmetros
from random import uniform
print(uniform(1, 60))

# Função Choice: Retorna um valor aletório de um iterável
from random import choice
premios = ['Playstation 2', 'Peixe', 'Chinelo', 'Lápis']
print(f'Mario ganhou um {choice(premios)}')

# Função Shuffle: Retorna o iterável com os elementos embaralhados
from random import shuffle
cores = ['Azul', 'Preto', 'Amarelo', 'Verde', 'Vermelho', 'Magenta', 'Cinza']
print(cores)
shuffle(cores)

#Obs.: Todos os módulos oficiais podem ser encontrados em:https:
# //docs.python.org/3/py-modindex.html

#Módulo Statistics
import statistics
numeros = [1, 2, 3, 4, 5]
media = statistics.mean(numeros)
print(media)

# Outros modos de importação
# Utilizando alias (as): Apelida um módulo ou uma função
import random as rd
print(rd.random())

from random import choice as ch
lista = ['Navio', 'Batata', 'Acre']
print(ch(lista))


# Utilizando *: Importa TODAS as funções do módulo
from random import *
print(random())

# Importar multiplas funções de um mesmo modulo
from random import shuffle as sh, randint as ri
lista = ['Navio', 'Batata', 'Acre']
sh(lista)
print(lista)
print(ri(1, 11))

# Modo mais utilizado
from random import(
    random,
    randint,
    uniform,
    choice,
    shuffle
)

print(random())
print(randint(1, 11))
print(uniform(1, 11))
print(choice('Programando Ideias'))
nomes = ['Rebeca', 'Roberta', 'Rúbia']
shuffle(nomes)
print(nomes)
"""