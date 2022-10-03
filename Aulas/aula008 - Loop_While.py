"""
Loop While
"""
"""
Como declarar?
while condição: #Enquanto essa condição for True faça:
    #Processo
Ex:
a)
x = True
while x:
    print('Estou rodando')
    x = False
b)
pedido = ''

while pedido != 'quero sair':
    pedido = input('voce nao vai sair: ')

O loop While, diferente do loop for, precisa de uma condição de parada definida pelo programador.
A palavra break executa a finalização do loop while.
Ex:
contador = 0

while contador < 9:
    print(contador,end = ' ')
    contador = contador + 1
    if contador == 5:
        break #Ira sair loop imediatamente
Dicas de ouro:
1) Podemos escrever um loop while em uma mesma linha caso a codificação seja simples.
Para isso, separe prints, operações matematicas com ponto e vírgula.
Ex:
contador = 0

while contador < 9: print(contador,end = ' '); contador = contador + 1
2) Palavra continue(Prosseguir):
 - Caso você tenha uma condição que precise apenas de mandar o loop se repetir escreva continue.
Ex:
contador = 0

while contador < 9:
    print(contador, end = ' ')
    contador += 1
    if contador == 5:
        continue # Prosseguir com o loop imediatamente
for                                                       x                   while
Numero de iterações dependente da sua sequencia.                       Numero de iterações ilimitados.
Utiliza um contador que automaticamente se incrementa.                 Pode utilizar um contador, porém é necessário que você declare ele por fora e o incremente por dentro

Qual dos dois é melhor?
 - Ambos são permutaveis, logo você pode decidir qual queira em determinada situação.
"""
