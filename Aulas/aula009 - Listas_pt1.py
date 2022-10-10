""""""
"""
Listas - Coleção de dados muito poderosa e importante, diferente de tudo que voce já viu.

C - Vetores e Matrizes: Apenas um tipo de dado, tamanho único.

Listas - São dinâmicas: podem receber qualquer tipo de dado,
         tamanho limitado à memória disponível do seu PC.
         
Sintaxe: [elemento1, elemento2, ..., elementoN]

# Exemplos de declaração de listas:
lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898')
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

cor = 'azul'
animal = 'pavão'
numero = 42
lista8 = [cor, animal, numero]

# Adicionar valores em uma lista - Append: Adiciona apenas 1 elementos por vez
# Obs.: Adiciona o objeto
print(lista2)
lista2.append(6)
print(lista2)

lista2.append(10)
lista2.append('Maria Joaquina')
lista2.append('Molho de alho')
lista2.append(True)
lista2.append([2, 4, 6, 8])
print(lista2)

# Adicionar valores em uma lista - Extend: Adiciona multiplos elementos
lista5.extend(['abacaxi', 1.98, 'Kg'])
print(lista5)

#lista5.extend(12) #TypeError

# Obs.: Recebe apenas iteráveis e adiciona os elementos dos mesmos

#lista5.extend([1, True], [0, False]) #TypeError

# Obs.: Recebe apenas um iterável por vez

# Adionar valores em uma lista - Insert: Adiciona um valor em um determinado indice de uma lista
# Obs.: Este comando nao substitui o valor original, apenas desloca-o para a direita
lista4.insert(1, 'Aqui')
print(lista4)

# Concatenar duas (ou mais) listas
listaSomada = lista2 + lista4
print(listaSomada)

lista2 = lista2 + lista4
print(lista2)
#lista2.extend(lista4)

# Converter strings em listas - Split: Cria uma lista separando uma string
#                                      por seus espaços (' ') (padrão)
frase = 'Hoje é um novo dia, de um novo tempo, que começou'

lista9 = frase.split()
print(lista9)

# Obs.: É possível indicar o parâmetro de separação
lista9 = frase.split(',')
print(lista9)

lista9 = frase.split('novo')
print(lista9)

# Converter listas em strings - Join: Cria uma string juntando os elementos de uma lista
lista10 = ['Silvio', 'Santos', 'vem', 'aí']

frase = ' '.join(lista10)
print(frase)

frase = '@'.join(lista10)
print(frase)

# Contar a quantidade de elementos de uma lista
print(len(lista7))
    
# Verificar se determinado valor está em uma lista
if [1, 3, 5, 7] in lista7:
    print('Está na lista')
else:
    print('Não está na lista')

print(40 in lista7)

# Obter a quantidade de vezes que um valor se repete em uma lista - Count
print(lista6)
quantidade = lista6.count('S')
print(f'Eu encontrei {quantidade} vez/vezes')

# Ordenar uma lista - Sort
listaMaluca = [21, 232, 123, 434, 1, 2, 42, 6, 10, 83, 567]
print(listaMaluca)

listaMaluca.sort()
print(listaMaluca)

listaDoida = ['v', 'uy', 'a', 'peixe']
print(listaDoida)
listaDoida.sort()
print(listaDoida)

# inverter uma lista
print(lista7)
lista7.reverse()
print(lista7)

print(lista7[::-1]) #slicing

# Obs.: lista[inicio:fim:passo]
print(lista7)
print(lista7[2:]) #Do índice 2 ao final
print(lista7[2:6]) #Do indice 2 ao 6
print(lista7[2:7:2]) #Do indice 2 ao 7, de dois em dois elementos

# Acessar elementos de uma lista
print(lista7[2])
print(lista7[4])
print(lista7[-2])
print(lista7[-4])
print(lista7[5])

#print(lista7[15]) #IndexError
#print(lista7[-15]) #IndexError

for ind in range(0, 10):
    print(f'Índice: {ind}, valor: {lista7[ind]}')
    
# Substituir elementos de uma lista
print(lista7)
lista7[1] = False
lista7[4] = 'Vodka'
print(lista7)

# Remover elementos de uma lista - Pop: Remove e retorna o ultimo elemento de uma lista (padrão)
print(lista2)
print(lista2.pop())
print(lista2)

# Obs.: É possível indicar o índice do valor a ser removido
print(lista7)
lista7.pop(5)
print(lista7)

# Obs.: Os valores à direita são deslocados para esquerda.

# Repetir elementos de uma lista
print(lista4)
lista4 = 5 * lista4
print(lista4)

# Limpar uma lista
print(lista7)
lista7.clear()
print(lista7)

"""