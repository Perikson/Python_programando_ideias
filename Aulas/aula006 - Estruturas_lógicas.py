""""""
"""
Estruturas lógicas

and (e): True apenas se todas as condições forem True

Or (ou): True quando pelo menos uma condição for True

is (é): Comparação entre valores, similar ao ==

not (não): Inversão do valor booleano (True -> False, False -> True)

#and
#Exemplo 1
sensor = 875 #range de segurança do sensor: 60 a 75

if sensor >= 60 and sensor <= 75:
    print('Tudo OK!')
else:
    print('Corre!')

# Exemplo 2
agua = True
comida = False

if agua and comida:
    print('Cachorro feliz!')
else:
    print('Cachorro triste!')

# Or
# Exemplo 1
pizza = False
lasanha = False

if pizza or lasanha:
    print('Preciso comer mais salada')
else:
    print('Estou com fome')
    
# Exemplo 2
num = 23

if num % 2 == 0 or num < 10:
    print('É par ou menor que 10')
else:
    print('É ímpar e maior ou igual a 10')
    
#is
login = False
#print(login is True) #login é True? R: NÃO (False)
#print(login is False) #login é False? R: SIM (True)

if login is True:
    print('logado')
else:
    print('deslogado')
    
# not
login = True

if not login: # não False: True
    print('deslogado')
else:
    print('logado')
"""