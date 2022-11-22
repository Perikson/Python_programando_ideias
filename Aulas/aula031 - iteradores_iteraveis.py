"""
Iteradores e iteraveis
"""
"""
Definição:
O que é um Iterador?
 - É um objeto que pode ser iterado e retorna um dado quando utiliza-se a função next()
O que é um iteravel?
 - É um objeto que retorna um iterador quando usa-se a função iter()
 
Ex:
nome = 'Programando Ideias' #Strings são iteráveis como já vimos
lista = [1,'oi',True] #Listas são iteráveis

prim_iterador = iter(nome) #Transformação de iterável para iterador
seg_iterador = iter(lista)
print(prim_iterador) #Retorna uma string iteradora
print(seg_iterador) #Retorna uma lista iteradora
print(type(prim_iterador))

Obs:Geração de erro:
print(next(prim_iterador)) #retorna um dado, 'P'
print(next(prim_iterador)) #retorna um dado, 'r'
print(next(prim_iterador)) #retorna um dado, 'o'
print(next(prim_iterador)) #retorna um dado, 'g'
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador))
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) 
print(next(prim_iterador)) #Acusa StopIteration pois voce já obteve todos os dados desmembrados da sequencia

- O loop for trabalha exatamente assim, ele pega um iteravel, aplica iter() e assim desmembra a sequencia com varios next()
Ex:
lista = [1,'oi',True] #Listas são iteráveis

seg_iterador = iter(lista)
iteradorfinal = iter(seg_iterador) #Comprovando que ao aplicar iter() em um iterador ele se mantem iterador

print(iteradorfinal) #Retorna uma lista iteradora
for item in seg_iterador: #O loop continua a funcionar pois ao aplicar o método iter() em um iterador, ele se mantem 
                          #iterador
    print(item)
    
 - Sabendo como funciona iteradores e iteraveis, nós podemos criar o nosso próprio loop for.
Ex:
iteravel = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(iteravel)

while True: #Loop infinito
    try:
        elemento = next(iterador) #Elemento recebe cada caracter de iterável que foi transformada em iterador
        print(elemento)
    except StopIteration:
        break #Parar o loop infinito

print('------------------------------------')
#O modo acima é equivalente a:
iteravel = [1,2,3,4,5,6,7,8,9,10]

for elemento in iteravel:
    print(elemento)
"""
