""""""
"""
Tuplas

Parecem listas, mas possuem duas diferenças:

Obs.: Não é possível remover ou adicionar elementos, apenas sobrescrevê-las.

Sintaxe: (elemento1, elemento2, ..., elementoN) ou elemento1, elemento2, ..., elementoN

#Obs.: A vírgula é obrigatória!

Vantagens: Dados são mais seguros. Tuplas são mais rápidas. Não há o efeito shallow copy (tuplas 
                                                            são sempre independentes)
                                                            
# Obs.: Assim como listas, tuplas também são ordenadas.

Quando usar? 
Usar quando não forem necessárias modificações nos dados.
Exemplo: Meses do ano, dias da semana.

# Exemplos de declaração de tuplas

tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)

#print(type(tupla1), type(tupla2), type(tupla3), type(tupla4))

# Forma errada
tupla1 = 1
tupla2 = (1)
tupla3 = ('peixe')

#print(type(tupla1), type(tupla2), type(tupla3))

# Exemplos de declaração de tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)
tupla5 = ('futebol', 'moto', 'França')
tupla6 = ('pizza', True, 18, 5j, 0.43, 'x', True)
tupla7 = tuple(range(11))
tupla8 = tuple(['azul', True, 'x', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])

# Concatenar duas (ou mais) tuplas
tuplaNova = tupla1 + tupla5
print(tuplaNova)

tupla1 = tupla1 + tupla5
print(tupla1)

# Obs.: A primeira tupla1 foi apagada, e assim foi criada uma nova no momento da concatenação.

# Verificar se determinado valor está em uma tupla
print(tupla8)
print(10 in tupla8)
print(False in tupla8)

# Obter a quantidade de vezes que um valor se repete em uma tupla
cores = ('branco', 'azul', 'preto', 'verde', 'amarelo', 'verde')

print(cores.count('verde'))
print(cores.count('amarelo'))

# Acessar elementos de uma tupla
print(tupla8)
print(tupla8[2])
print(tupla8[4])
print(tupla8[-2])
print(tupla8[-4])

#print(tupla8[15]) #IndexError
#print(tupla8[-15]) #IndexError

for indice in range(0, 3): #0, 1, 2
    print(f'indice: {indice}, valor: {tupla6[indice]}')

# Slicing
print(tupla6)
print(tupla6[2:]) #Do índice 2 ao final
print(tupla6[2:6]) #Do índice 2 ao 6
print(tupla6[2:7:2]) #Do índice 2 ao 7, de dois em dois

# Percorer tuplas (iterar)
# For

for elemento in tupla1:
    print(elemento, end=' ')

total = 0
for elemento in tupla1:
    total = total + elemento
print(f'\n{total/len(tupla1)}')

# While

total = 0
cont = 0
while cont < len(tupla1):
    total += tupla1[cont] #total = total + tupla1[cont]
    cont += 1 #cont = cont + 1
print(total/cont)

# Obter indice da tupla
cores = ('branco', 'azul', 'preto', 'verde', 'amarelo', 'verde')

#for indice, cor in enumerate(cores):
#    print(f'{indice}: {cor}')

print(cores.index('azul'))
print(cores.index('verde')) # Retorna o índice do primeiro valor encontrado
#print(cores.index('vermelho')) #ValueError

print(cores.index('verde', 4)) #Busca A PARTIR do indice 4
#print(cores.index('verde', 20)) #ValueError

print(cores.index('verde', 2, 4)) #Busca ENTRE os índices 2 e 4

# Desempacotar tuplas

esporte, meioTrans, pais = tupla5
print(esporte)
print(meioTrans)
print(pais)

#esporte, meioTrans, pais, outraCoisa = tupla5 #ValueError
#esporte, meioTrans = tupla5 #ValueError

# Funções úteis para trabalhar com tuplas

#Obs.: Apenas para inteiros ou floats
print(sum(tupla1)) #Retorna a soma dos elementos
print(max(tupla1)) #Retorna o maior elemento
print(min(tupla1)) #Retorna o menor elemento

#Obs.: Para qualquer tipo de dado
print(len(tupla1))

#Copiar uma tupla
#Obs.: Não há o efeito shallow copy. Porém, a declaração (sintaxe) é a mesma.

tuplaNova = tupla1
print(tuplaNova)
print(tupla1)

tuplaNova = tuplaNova + tupla5
print(tuplaNova)
print(tupla1)

"""