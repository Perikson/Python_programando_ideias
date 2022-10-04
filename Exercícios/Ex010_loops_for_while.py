"""
Média dos 5 primeiros números primos da Sequência Fibonacci
"""
"""
- O que é a Sequencia de Fibonacci?
 1,1,2,3,5,8,13,21,34,55,...
 
Agora aplicando a condição de ser numero primo:
 - Condição:
a) Numeros primos devem ser maiores do que 1.
b) Numeros primos são apenas divisiveis por ele mesmo e o numero 1.

"""

anterior = 0 #Numero antecessor da sequencia
proximo = 1 #Numero posterior da sequencia
parada = 1 #Variavel de parada para impressao dos 5 numeros
soma = 0 #Variavel que armazena a soma para realizar a média
while parada <= 5: #Enquanto parada for menor ou igual a 5 faça:
    proximo = proximo + anterior #Proximo recebe ele mesmo e anterior para atualizar o numero posterior
    anterior = proximo - anterior #Anterior recebe proximo menos anterior para atualizar
    divisor = 1 #Variavel que será o divisor
    num_divisores_inteiros = 0 #Contagem de numero de divisores
    while divisor <= proximo: #Loop para realizar as divisões de proximo por todos os divisores começando de 1 até proximo
        if proximo % divisor == 0: #Caso a divisão tenha resto zero
            num_divisores_inteiros += 1 #incrementa o contador de divisores
        divisor += 1 #Incrementa divisor para realizar outro loop
    if num_divisores_inteiros == 2: #Caso tenha apenas dois divisores, é um numero primo
        soma = soma + proximo #Atualiza soma com o numero primo proximo
        print(proximo) #Apenas imprime o numero primo para verificação
        parada += 1 #Incrementa a variavel parada para achar o proximo numero primo

print(soma/5) #Imprime a media


# tambem pode-se realizar o exercício da seguinte forma(com 3 variáveis):

n1 = 0
n2 = 1
stop = 0
soma = 0

while stop != 5:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    divisor = 1
    num_divisores = 0

    while divisor <= n3:

        if n3 % divisor == 0:
            num_divisores += 1
        divisor += 1

    if num_divisores == 2:
        soma += n3
        print(n3, end=' ')
        stop += 1

print('\n')
print(f'A media dos 5 primeiros números primos da sequencia de fibonatti é {soma / 5}.')

