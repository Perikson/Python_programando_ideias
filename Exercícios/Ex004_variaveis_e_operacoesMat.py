"""
1)a)
nome = 'Mark'
print(int(nome)) #Não é possível transformar letras em inteiros

b)
frase = 'Eu sou seu pai'
print(frase[-1::]) #Sintaxe incorreta, o certo é utilizar [::-1]

c)
filme = 'Avatar'
print('A maior bilheteria de 2009 foi {filme}') #Falta acrescentar a letra f antes do primeiro aspas

d)
numero1 = 10
dado = int(input(Digite o numero que deseja: )) #Faltou o uso de aspas em volta do texto em input()
print(numero1 * dado)

2) Criação de personagem de mundo de ficção, apresentando opcoes de acordo com os tipos das variaveis:
 - Cor de Cabelo(string)
 - Cor de pele(string)
 - Classe: Guerreiro, Mago, Arqueiro(string)
 - Idade(int)
 - Altura(float)
 - Habilidade Específica(string)
Imprima para o usuário o personagem completo.

Resolução:
print('----------Bem Vindo a um novo universo----------')
print('--------------Crie seu personagem---------------')
cor_cabelo = input('Digite a cor do cabelo: ')
cor_pele = input('Digite a cor da pele: ')
classe = input('Digite a sua classe dentre: 1- Guerreiro\n2 - Mago\n3 - Arqueiro\nOpcao: ')
idade = int(input('Digite sua idade em anos: '))
altura = float(input('Digite sua altura em metros: '))
habilidade_especifica = input('Digite sua habilidade: ')
print('---------------Personagem Criado----------------')
print(f'Seu personagem tem: \n'
      f'Cabelo de cor: {cor_cabelo}\n'
      f'Pele de cor {cor_pele}\n'
      f'Classe {classe}\n'
      f'Idade de {idade}\n'
      f'Altura de {altura}\n'
      f'Habilidade de {habilidade_especifica}')
"""
