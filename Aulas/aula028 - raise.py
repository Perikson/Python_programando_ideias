"""
Raise
"""
"""
- A palavra Raise significa levantar, em programação é utilizada para apresentar/levantar erros no código que
  nós mesmos identificamos.
- A palavra raise é reservada assim como return,def,break,...
- Caso você utilize o raise dentro de uma função, assim que o programa o reconhecer irá acusar o erro e sair da função.

Como declarar?
raise tipo_do_erro('Mensagem que voce desejar que apareça')

Ex:
a)
#Cadastramentro em site:
#Adaptar de maneira que login aceite apenas strings e senha inteiros
def cadastrar(login,senha):
    if type(login) is not str: #Não utilizei == pois estou fazendo uma comparação de tipos, não de valores
        raise TypeError('Login deve ser string')
    if type(senha) is not int:
        raise TypeError('Senha deve ser inteiro')
    print(f'Login:{login} e Senha{senha}')

cadastrar('123','123')

b)
def divisao(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError('Numero 2 não pode ser zero, pois e denominador')
    divisao = num1/num2
    print(f'{divisao}')

divisao(1,2)
"""
