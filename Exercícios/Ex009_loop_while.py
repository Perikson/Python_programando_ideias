"""
1) Faça um programa que calcule o maior palíndromo resultado do produto de dois números de 3 dígitos.
 - Palíndromo são números que lendo da esquerda para a direita resulta no mesmo número caso leia da direita para esquerda.
  Ex: 52625
- Ex: O maior palíndromo resultado do produto de dois números é 91*99 = 9009

"""

n1 = 999 #Inicializa o primeiro numero
res = 0 #Inicializa resultado
while n1 != 99: #Enquanto o primeiro numero for diferente de 99 faça:
    n2 = n1 #Inicializa o segundo numero para fazer n1 * n2
#Esse loop realiza 999*n2,998*n2,997*n2,...
    while n2 != 99: #Enquanto o segundo numero for diferente de 99 faça:
# Esse loop realiza operações n1*999, n1*998, n1*997,... até n2 = 100
        numero = str(n1 * n2) #Transforma para string o produto entre n1 e n2 para realizar o comando [::-1]
        inverte_numero=numero[::-1] #Inverte o produto de n1 e n2
        if inverte_numero == numero: #Se numero for igual ao inverso de numero
            num = int(numero) #Volta numero para inteiro
            if res < num: #Se resultado for menor que num faça:
                res=num #Armazena num em res pois num é maior
                n2 -= 1 #Diminui n2 em 1
            else:
                n2 -= 1 #Diminui n2 em 1
        else: #Caso o inverso de numero não seja igual a numero faça:
            n2 -= 1 #Diminui n2 em 1
    n1 -= 1 #Diminui n1 em 1
print(res) #Imprime res
