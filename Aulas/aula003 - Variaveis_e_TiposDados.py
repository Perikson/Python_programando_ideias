"""
Variaveis e Tipos de Dados
"""
"""
O que são Variaveis?
 - São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.
O que são Dados?
 - São todas as informações que serão utilizadas ao longo do seu código. Podendo ser 
   números, palavras, frases, textos, dentre outros.
   
Existem 2 tipos de variaveis:
1) Variavel Global: São variaveis que podem ser manipuladas ao longo de todo código.
2) Variavel Local: São variaveis que podem ser manipuladas apenas em uma determinada parte
                   do programa.

Como declarar variaveis?
nome = dado
 - Sempre dê nomes intuitivos a suas variaveis para facilitar o entendimento.
 Ex:
 idadeSilvioSantos = 85
 a = 85

É necessario algumas regras para nomear suas variaveis:
a) Em nomes compostos devemos separar por underline ou letra maiusculas.
Ex:
Modo Certo (Pythonico):
idadeJoao = 17
idade_joao = 17
IDADE_JOAO = 17
Modo Errado:
idadejoao = 17
b) Variaveis não devem possuir nenhum tipo de caracter especial (%,acentos, ç, dentre outros).
Ex:
Modo certo:
fracao = 100
Modo Errado:
fração = 100
c) Variaveis não devem possuir apenas numeros em seu nome.
Ex:
Modo errado:
123 = 17 # Irá acusar erro
Modo Certo:
a123 = 17
OBS: Ao utilizar numeros na nomeclatura de variaveis devem sempre vir no minimo uma letra antes dos numeros.

Tipos de Dados:
a) Inteiros: Número que não possui casas decimais. 
Ex: 
idadeJoao = 17
print(type(idadeJoao)) # Para utilizar a função type faça: type(nome da variavel).
b) Flutuantes (float):Números que possuem casas decimais.
 - Utiliza-se ponto para separar os numeros, NÃO VÍRGULA.
 - Não utiliza espaços em volta do ponto.
 - Apresenta maior precisão e riqueza de dados.
Ex:
precoBanana = 5.59
print(type(precoBanana))
c) Complexo:
 - Se um dado possuir a letra j é um numero complexo, lembrando que precisa de haver um numero junto a ele.
Ex:
num_complexo = 1j
print(type(num_complexo))
d) Booleana:
 - O valor 1 representa True (Verdadeiro), enquanto o valor 0 representa False (Falso).
Ex: 
var_bool = True
print(type(var_bool))
e) String:
 - Todos os dados que estão entre aspas simples, aspas duplas ou aspas simples triplas.
 - Podem conter numeros e letras dentro dela.
 - Para inverter o conteudo presente na string basta adicionar [::-1]
Ex:
var_string = '12345'
print(type(var_string))
var_string = "Tom cruise"
print(type(var_string))
var_string = '''Tom cruise'''
print(type(var_string))
var_string = 'Tom cruise'
print(var_string[::-1])
# Tom Cruise
# 0123456789
var_string = 'Tom cruise'
print(var_string[4:10]) # Estou pegando a posição 4(c) até a posição 9(e)
var_String = "turquia god of war"
print(var_String[6:13]) # Estou pegando a posição 6(a) até a posição 12(o)

Por fim, é possível declarar varias variaveis dentro de uma mesma linha.
Ex:
a1,a2,a3,a4,a5 = 1,2.5,True,2j,'sim'
 - Caso haja mais dados ou variaveis em algum dos lados irá dar erro.
"""
