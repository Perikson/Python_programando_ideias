"""
Um estudante do Curso Programando Ideias acabou de assistir a aula de diferença entre iteráveis e iteradores,
para praticar mais, criou um programa que realiza o processo de um for, porém sem utilizar a ferramenta for
diretamente, segue o código desenvolvido:

O estudante percebeu que o código estava apresentando o seguinte erro:
                         TypeError: 'list' object is not an iterator

Porém, não sabe como corrigir. Altere o programa do estudante para fazer funcionar corretamente e explique
o que aconteceu.

"""

def desmembra_iteravel(iteravel): #Função que realiza a operação for
    iterador = iter(iteravel) #Transforma iteravel em iterador
    while True: #Loop infinito
        try:
            print(next(iterador)) #Imprime cada dado desmembrado do
                                  #iterador
        except StopIteration: #Caso chegue ao final do iterador faça:
            print('Chegamos ao ultimo elemento') #Aviso
            break #Quebra o loop infinito

desmembra_iteravel([1,2,3,4,5,6,7,8]) #Chamada de função com iterável

