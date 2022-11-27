""""""
"""
1 - Crie uma pasta, uma subpasta e em seguida um módulo na subpasta contendo uma função qualquer. 
Acesse o módulo no programa principal e execute a função.

Obs.: No módulo criado, estabeleça uma condição para a função ser acessada apenas se o módulo for 
importado e executado em outro. Ou seja, quando o módulo em questão não é o principal (main).


# 1

from PacoteFora.PacoteDentro.ModuloDentro import preverFuturo
from random import choice as ch

idades = [12, 65, 87, 14, 52, 42, 4, 84, 14, 73, 16, 61, 34, 28, 35, 22]
formacao = ['filosofia', 'engenharia', 'medicina', 'artes', 'letras', 'biologia']
trabalho = ['bartender', 'político(a)', 'administrador(a)', 'professor(a)', 'carpinteiro(a)']
pais = ['França', 'Angola', 'Escócia', 'Espanha', 'Turquia']
animal = ['crocodilo', 'urso', 'sapo', 'elefante', 'tubarão', 'golfinho']
nome = input('Digite um nome: ')

preverFuturo(nome, ch(idades), ch(formacao), ch(trabalho), ch(pais), ch(animal))
"""