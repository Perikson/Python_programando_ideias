""""""
"""
Módulos Customizados e Externos

# Importar módulo criado por nós (customizado)
import moduloTeste

moduloTeste.imparPar(80)
moduloTeste.imparPar(81)

print(moduloTeste.lista)
for num in moduloTeste.lista:
    print(num * 10)

#Módulos Externos
#Obs.: Deixam o cógio mais visível, organizado e acessível.

#Todos os módulos oficiais externos podem ser encontrados em: https://pypi.org/

#Colorama
from colorama import init
init()

from colorama import Fore, Back
print(Fore.RED + 'Sou o deadpool')
print(Fore.BLACK + ' ')
print(Back.GREEN + 'Sou o Hulk')

"""