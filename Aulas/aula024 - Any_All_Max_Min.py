""""""
"""
Any, All, Max e Min

- Any: Retorna True se QUALQUER elemento do iterável for True
#Obs.: Neste caso, um iterável vazio retorna False.

#Exemplos de Any:

print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #True
print(any('Programando Ideias')) #True
print(any([0, False, {}, [], ()])) #False
print(any([0, False, {}, [], (), 89437])) #True
print(any([])) #False

numeros = [1, 2, 3, 4, 5, 6]
print(list(num % 5 == 0 for num in numeros))
print(any(num % 5 == 0 for num in numeros))

- All: Retorna True se TODOS os elementos do iterável forem True
#Obs.: Neste caso, um iterável vazio retorna True.

#Exemplos de All:

print(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #True
print(all('Programando Ideias')) #True
print(all([0, False, {}, [], ()])) #False
print(all([0, False, {}, [], (), 89437])) #False
print(all([])) #True

numeros = [2, 4, 6, 8, 10, 11]
print(list(num % 2 == 0 for num in numeros))
print(all(num % 2 == 0 for num in numeros))

- Max: Retorna o elemento de maior valor de um iterável ou dos elementos passados como 
# argumentos

# Exemplos de Max:
numeros = [31, 12, 343, 43, 11, 242, 15]
print(max(numeros))
print(max(31, 12, 343, 43, 11, 242, 15))

cores = {'azul':2, 'vermelho':5, 'verde':3}
print(max(cores.values()))
print(max(cores))

- Min: Retorna o elemento de menor valor de um iterável ou dos elementos passados como
# argumentos

#Exemplos de Min:
numeros = [31, 12, 343, 43, 11, 242, 15]
print(min(numeros))
print(min(31, 12, 343, 43, 11, 242, 15))

cores = {'azul':2, 'vermelho':5, 'verde':3}
print(min(cores.values()))
print(min(cores))

# Exemplo com max e min

alunos = ['Pedro', 'Isadora', 'Lucas', 'Camila', 'Samuel']
print(max(alunos)) #Samuel
print(min(alunos)) #Camila

print(max(alunos, key=lambda aluno: len(aluno))) #Isadora
print(min(alunos, key=lambda aluno: len(aluno))) #Pedro

"""
