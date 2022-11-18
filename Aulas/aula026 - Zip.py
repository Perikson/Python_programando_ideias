""""""
"""
Zip

- Retorna um objeto zip com elementos dos iteráveis passados como parâmetros.

- Pode receber qualquer tipo de iterável.

- O tamanho do menor iterável predomina.

# Exemplo 1 de zip
alunos = ['Bianca', 'Vitor', 'Ariel']
notas = (10, 6, 8)

juntarTudo = zip(alunos, notas)
print(juntarTudo)
print(type(juntarTudo))

#print(list(juntarTudo))
print(dict(juntarTudo))
print(tuple(juntarTudo)) # Os valores se perdem após sua utilização

# Exemplo 2 de zip
nome = ['Bianca', 'Vitor', 'Ariel', 'José']
idade = (18, 82, 71, 9, 12)
cidade = {'São Paulo', 'Vitória', 'São Luís'}
estado = {1:'RS', 2:'PR', 3:'ES', 4:'AM'}

print(list(zip(nome, idade, cidade, estado.values())))

#Exemplo 3 de zip
lugares = [('RS', 'São Paulo'), ('PR', 'Vitória'), ('AM', 'São Luís')]

#*lugares -> ('RS', 'São Paulo') ; ('PR', 'Vitória') ; ('AM', 'São Luís')
#zip ->  RS, PR, AM

print(list(zip(*lugares)))
"""