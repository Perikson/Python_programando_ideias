"""
Faça uma função que calcule a diferença entre dois números, decore-a com outra função adicionando as Mensagens:
‘Inicio do Programa’ e ‘Decorando a funcao’. Após isso faça com que o decorador permita que apenas
seja calculada a diferença positiva entre os dois números, independente da ordem de entrada. Imprima o resultado.
"""


def completa(funcao): #Função decoradora
    def decora(x,y): #Função interna que recebe os dois numeros
        print('------Inicio do Programa------') #Decoração
        print('------Decorando a Funcao------') #Decoração
        #O bloco condicional a seguir faz com que sempre calcule a diferença positiva entre os numeros
        if x > y:
            funcao(x,y)
        else:
            funcao(y,x)
    return decora #Retorna a própria função decora, não sua execução


@completa #Decorador
def diminui(num1,num2):
    print(f'O resultado desejado: {num1 - num2}')

diminui(7,1) #Chama para a função ser executada
diminui(1,7) #Mesmo invertendo sempre dará diferença positiva
