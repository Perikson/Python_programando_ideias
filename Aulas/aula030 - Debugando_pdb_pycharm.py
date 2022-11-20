"""
Debugando com Pdb e Pycharm
"""
"""
O que é Debug?
 - Debug é uma forma de voce limpar e analisar todos os problemas ocorridos no seu código.

Obs: A prática de utilizar print() para tratar erros apresentando aos poucos os dados ao longo do programa
     é uma prática ruim.
Ex:
def boas_vindas(nome):
    print(nome) #Apenas para verificar se a variavel está certa
    print(f'Seja Bem vindo/a {nome}')

boas_vindas('Carlos')

#Forma profisional/Pythonica de corrigir erros de codificação:
a) PDB: Python Debugger
 - Para usar utiliza-lo devemos importar uma biblioteca chamada pdb e assim utilizar a função
   set_trace()
Há alguns comandos básicos a serem usados no pdb:
1)l(list): Apresenta onde voce está no código
2)n(next):Pular para a próxima linha
3)p(print): Imprime uma variavel
4)c(continue): Continua a execução do código até o final do programa ou até o proximo set_trace()
Ex:
 - Cuidado para não usar letras em seu código que se confundem com os comandos l,n,p,c
 - Recomenda-se chamar o import pdb perto do local que você deseja utiliza-lo.
x = 2
y = 3
import pdb
pdb.set_trace()
z = x * y
nome = 'Clara'
frase = nome * z
print(frase)

 - A partir da versão 3.7 do python não precisa importar pdb, ela foi incorporada aos Built-in com o nome
   breakpoint().
 - breakpoint() mantem os comandos básicos em pdb (l,n,p,c) e todas as outras funcionalidades. 
Ex:
x = 2
y = 3
breakpoint()
z = x * y
nome = 'Clara'
breakpoint()
frase = nome * z
print(frase)

b)Utilizando o Debugger do Pycharm:
Ex:
x = 2
y = 3
x = x + y
z = x * y
nome = 'Clara'
frase = nome * z
print(frase)
"""
