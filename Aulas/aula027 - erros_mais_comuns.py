"""
Tipos de erros mais comuns em Python
"""
"""
- Para tratar erros é muito bom prestar atenção na mensagem apresentada no console.

Erros mais comuns:
a) AttributeError : Ocorre quando há falha de atribuição.
Ex:
dicionario = {'SP':'Sao Paulo','RJ':'Rio de Janeiro'}
dicionario.add('ES')
print(dicionario)
#Ocorrerá AttributeError pois o comando add() não existe para dicionarios

b)IndexError : Ocorre quando não existe o indice de acesso dentro da variavel
Ex:
lista = [1,2,3,4,5]
print(lista[3])
print(lista[6]) #Esse indice não existe na lista, logo dará IndexError

c) KeyError: Aconte quando uma chave não é encontrada dentro do dicionario.
Ex:
dicionario = {'SP':'Sao Paulo','RJ':'Rio de Janeiro'}
print(dicionario['SP'])
print(dicionario['MG']) #Acusa KeyError, pois a chave 'MG' não existe no dicionario

d) NameError: Ocorre quando uma variavel ou função não é encontrada no código
Ex:
print(programandoideias) #Acusa NameError pois não houve declaração da variavel
programandoideias = 'Top'

x() #Acusa NameError, pois a função x não está definida

e) SyntaxError: Surge quando há um erro de sintaxe:
Ex:
variavel = 
10

break 100

def variavel = 5
#Todos os três exemplos acusam SyntaxError

f) IndentationError: Ocorre quando há um erro de indentação no código
Ex:
x = 10
if x == 10:
x = 5 #Acusa IndentationError, pois não está indentado (4 espaços)

g) TypeError: Ocorre quando há uma operação com tipos incorretos
Ex:
nome = 'Marcelo'
numero = 10
nome_numero = nome + numero #Acusa TypeError pois não é possivel concatenar str com int
print(nome_numero)

h) ValueError: Acontece quando uma função recebe um parametro de tipo certo, mas valor errado
Ex:
valor = int(input('Digite um numero de 1 a 10: ')) #Se escrever uma letra ou palavra dará erro
print(valor)
#Ocorre erro, pois a função int() está recebendo um parametro de tipo certo (str), porem, o valor dentro dela não, pois
 deve ser um numero e não letra.
"""
