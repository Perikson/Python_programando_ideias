"""
1) Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário.
Ex: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18
Solução:
soma = 0 # Inicializa variavel soma
numero = int(input('Digite o numero: ')) #Pede o numero para o usuario
for num in range(1,numero+1): #Para cada num dentro do intervalo 1 e numero+1 faça:
    if numero % num == 0: #Se o resto da divisão de numero por num for zero faça:
        soma = soma + num #atualiza soma com num
print(soma) #Imprime a soma final


2) Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuário.
Ex: Se o usuário escolheu n=3, será impresso 5,10,15.
Solução:
numero = int(input('Digite o numero de multiplos de 5 que deseja: ')) #Recebe numero como inteiro para entrar no range()
for num in range(1,numero+1): #Para cada num no intervalo de 1 a numero+1 faça:
    print(f'{5 * num}') #Imprime 5 vezes num

"""
