"""
Try,Except,else,finally
"""
"""
Como declarar?
try: #Tente fazer isso:
    #Processo
except: #Exceto apresente algum erro faça:
    #Processo
else: #Se não
    #Processo
finally: #Finalmente faça:
    #Processo
Obs.1: O bloco else e finally são opcionais, enquanto o try/except é obrigatório.
Obs.2: O bloco else só é executado caso o try funcione
Obs.3: O bloco finally sempre é executado
Ex:
#Calculadora
a) Tratando com try/except:
#Tratando de forma generica:
try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except:
    print('Deu algum erro')
#Tratando de forma especifica(Recomendada):
Sintaxe:
try:
    #Processo
except (opcional: tipo_do_erro):
    #Processo
Ex:
try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError as erro:
    print(f'Deu {erro}') #variavel erro traz a mensagem do motivo do erro

- Nós podemos usar varios excepts depois do try.
Ex:
try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except TypeError:
    print('Deu TypeError')
except ValueError:
    print('Deu ValueError')
except: #Deve sempre finalizar como um default
    print('Nao sei qual erro deu')

b) try/except/else:
Ex:
try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}')
    elif operacao == 3:
        print(f'Resultado: {mul(num1, num2)}')
    elif operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}')

c)Try/except/else/finally:
#Finally é muito utilizado para finalizar processos
Ex:
try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}')
    elif operacao == 3:
        print(f'Resultado: {mul(num1, num2)}')
    elif operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}')
finally:
    print('terminou o processo')
    
Programa completamente tratado de erros:
def soma(x,y):
    op = x + y
    return op

def subtracao(x,y):
    op = x - y
    return op

def mul(x,y):
    op = x * y
    return op

def divisao(x,y):
    try:
        op = x / y
    except ZeroDivisionError:
        print('O denominador nao pode ser zero')
        return 'Infinito'
    else:
        return op

try:
    operacao = int(input('Escolha a operacao de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    try:
        num1 = int(input('Digite o primeiro numero: '))
    except ValueError:
        print('Deve ser um numero inteiro')
    else:
        try:
            num2 = int(input('Digite o segundo numero: '))
        except ValueError:
            print('Digite um numero inteiro')
        else:
            if operacao == 1:
                print(f'Resultado: {soma(num1,num2)}')
            elif operacao == 2:
                print(f'Resultado: {subtracao(num1, num2)}')
            elif operacao == 3:
                print(f'Resultado: {mul(num1, num2)}')
            elif operacao == 4:
                print(f'Resultado: {divisao(num1, num2)}')
finally:
    print('Terminou o processo')
"""
