"""
Geradores
"""
"""
- Geradores são iteradores, basicamente são objetos que voce pode percorrer como listas porem eles nao armazenam
  na memoria.
  
- Só podemos iterar(loops/funções) apenas uma vez geradores.

- As funções que geram geradores são chamadas de funções geradoras.

- Para retornar o conteudo presente em uma função geradora usa-se ao invés da palavra return, yield.

- Sendo que funções geradores retornam um elemento por vez.

- Geradores trazem performace tanto em memoria quanto velocidade no código, pois só podem ser usados uma vez.
Ex:
def funcao_geradora():
    while True: #Loop infinito
        palavra = input('Fale: ')
        yield palavra

resultado = funcao_geradora()
print(resultado)
#Ele irá gerar loops de acordo com a quantidade de next()
print(next(resultado))
print(next(resultado))
print(next(resultado))

Obs: Caso use um loop for, cuidado para nao cair em um loop infinito:
#Utilize um contador para parar o loop while.
def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5:
        auxiliar += 1
        palavra = input('Fale: ')
        yield palavra

resultado = funcao_geradora()
print(resultado)

for item in resultado:
    print(item)

Observação:
print(set(resultado)) #Podemos manipular geradores e transforma-los no que quisermos(set,list,tuple,dict)

 - Teste de iteração unica em geradores:
 def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5:
        auxiliar += 1
        palavra = input('Fale: ')
        yield palavra

resultado = funcao_geradora()
print(resultado)
for item in resultado:
    print(item)
#Não será executado a próxima iteração pois geradores só podem ser iterados uma vez
for x in resultado:
    print(x)
    
    
#Teste de Velocidade:
import time #Importando toda biblioteca

#List comprehension
tinicio_lista = time.time()
print(sum([valor ** 2 for valor in range(100000000)]))
tfinal_lista = time.time() - tinicio_lista

#Generator comprehension
tinicio_gen = time.time()
print(sum((valor ** 2 for valor in range(100000000))))
tfinal_gen = time.time() - tinicio_gen

print(f'Lista levou {tfinal_lista}')
print(f'Generator levou {tfinal_gen}')
#Lista levou 47.273388147354126
#Generator levou 38.0003924369812

#Teste de Memória
 - Para esse exemplo iremos utilizar a geração de 100000 numeros da sequencia fibonacci.
 - Para quem nao lembra: 1,1,2,3,5,8,13,21,...
# a) Lista:
def fibonacci(max):
    sequencia = []
    x,y = 0,1
    while len(sequencia) < max:
        sequencia.append(y)
        x,y = y, x+y
    return sequencia

for x in fibonacci(100000):
    print(x)

# b) Gerador:
def fibonacci(max):
    x,y,contador = 0,1,0
    while contador < max:
        x,y = y, x+y
        yield x
        contador = contador + 1

for x in fibonacci(100000):
    print(x)
"""
