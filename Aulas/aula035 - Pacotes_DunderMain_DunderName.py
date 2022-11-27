""""""
"""
Pacotes, Dunder Main e Dunder Name

- Pacotes são conjuntos de módulos

#Obs.: O módulo __init__.py é criado automaticamente, e por convenção e compatibilidade, não é utilizado.

#Importar um módulo
from PACOTE1 import ARQUIVO1
ARQUIVO1.intro()

from PACOTE1.PACOTE2 import ARQUIVO2
ARQUIVO2.soma(10, 18)

#Importar uma função
from PACOTE1.ARQUIVO1 import intro
intro()

from PACOTE1.PACOTE2.ARQUIVO2 import soma
soma(10, 5)

#Dunder Main e Dunder Name
- Dunder( __ ): Double Under
- Dunder Main: __main__
- Dunder Name: __name__

#C:
int main(){
    #TUDO AQUI
}

#Python: Atrubui o valor __main__ para a variável __name__

#print(__name__)

from PACOTE1 import ARQUIVO1
ARQUIVO1.intro()

"""

"""

class Personagem:

    def __pular(self):
        print('PULOU')

    def apertou_w(self, personagem):
        personagem.__pular()

    def __abaixar(self):
        print('ABAIXOU')

    def apertou_s(self, personagem):
        personagem.__abaixar()

    def __desviar_esquerda(self):
        print('DESVIOU PARA ESQUERDA')

    def apertou_a(self, personagem):
        personagem.__desviar_esquerda()

    def __desviar_direita(self):
        print('DESVIOU PARA DIREITA')

    def apertou_d(self, personagem):
        personagem.__desviar_direita()


class Teclado:

    def tecla_w(self, personagem):
        personagem.apertou_w(personagem)

    def tecla_s(self, personagem):
        personagem.apertou_s(personagem)

    def tecla_a(self, personagem):
        personagem.apertou_a(personagem)

    def tecla_d(self, personagem):
        personagem.apertou_d(personagem)


from random import choice as ch
import time

vivo = True
obstaculos = ['Cima', 'Baixo', 'Esquerda', 'Direita']
pontos = -1
tempo = 2

teclado = Teclado()
bob = Personagem()

while vivo:
    passou = False
    pontos += 1
    time.sleep(tempo - pontos / 10)
    print('\n')
    obstaculo = ch(obstaculos)
    print(f'Obstáculo: {obstaculo}')
    comando = input('Comando: ')
    if comando == 'w' and obstaculo == 'Baixo':
        teclado.tecla_w(bob)
        passou = True
    elif comando == 's' and obstaculo == 'Cima':
        teclado.tecla_s(bob)
        passou = True
    elif comando == 'a' and obstaculo == 'Direita':
        teclado.tecla_a(bob)
        passou = True
    elif comando == 'd' and obstaculo == 'Esquerda':
        teclado.tecla_d(bob)
        passou = True
    else:
        vivo = False

print('\n')
print('GAME OVER!')
print('Obrigado por jogar...')
print(f'Pontuação: {pontos}')

"""
