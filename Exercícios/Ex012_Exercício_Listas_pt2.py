""""""
"""
1 - Criar um sistema de comando de uma loja de jogos. O programa deve conter pelo menos 6 listas: uma 
indicando quais jogos estão disponíveis para venda, uma para mostrar o preço de cada jogo, uma para
mostrar a quantidade de jogos disponíveis na loja para venda, uma informando o preço de fábrica dos 
jogos para aumentar o estoque, uma para registrar as vendas e uma para registrar as compras de estoque. 
Todas as informações de um jogo devem estar no mesmo índice nas listas. Criar um menu interativo 
com as seguintes opções para o usuário: Registrar venda, Compra de estoque, Resumo da loja, Sair. 
Ao sair indicar que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando 
as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade. 

# 1

jogos = ['GoW', 'Minecraft', 'GTA', 'Sonic', 'FIFA'] #Jogos disponíveis para venda
precosVenda = [210.00, 2.99, 150.00, 1.80, 125.00] #Preços de venda
precosCompraEstoque = [105.00, 1.50, 75.00, 0.90, 62.50] #Preços para o dono da loja comprar da fábrica
quantidade = [3, 0, 2, 5, 1] #Quantidade de jogos disponíveis
vendas = [] #Vendas registradas
compraDeEstoque = [] #Compras de estoque registradas

op = 0

while op != 4:
    print('1 - Registrar venda\n2 - Compra de estoque\n3 - Resumo da loja\n4 - Sair')
    op = int(input('Opção: '))

    if op == 1:
        jogoVendido = input('Jogo vendido: ')
        quantidadeVendida = int(input('Quantidade vendida: '))
        if quantidadeVendida <= quantidade[jogos.index(jogoVendido)]: #Testa se a quantidade que o
    # cliente deseja está disponível em estoque. jogos.index(jogoVendido) retorna o índice do jogo
    # escolhido na lista 'jogos' para verificar seu preço na lista 'precosVenda'.
            print(f'\n{jogoVendido} Vendido!\n')
            quantidade[jogos.index(jogoVendido)] -= quantidadeVendida #Remove do estoque a quantidade
    # vendida
            vendas.append(precosVenda[jogos.index(jogoVendido)] * quantidadeVendida) #Adiciona na lista
    # vendas o valor do jogo vendido, encontrado em precosVenda[jogos.index(jogoVendido)].
        else:
            print('\nNão há essa quantidade disponível em estoque\n') #Caso não houver a quantidade
            # disponível

    elif op == 2:
        jogoComprado = input('Jogo comprado: ')
        quantidadeComprada = int(input('Quantidade comprada: '))
        print(f'\n{jogoComprado} comprado!')
        quantidade[jogos.index(jogoComprado)] += quantidadeComprada #Adiciona ao estoque a
        # quantidade comprada na fábrica
        compraDeEstoque.append(precosCompraEstoque[jogos.index(jogoComprado)] * quantidadeComprada)
        # Adiciona na lista o valor do jogo comprado

    elif op == 3:
        print('\n\nQuantidade de jogos em estoque: ')
        for jogo in jogos:
            print(f'{jogo}: {quantidade[jogos.index(jogo)]}') #Apresenta a lista de jogos e a
            # quantidade disponivel

        print(f'Lucros: R${sum(vendas)}') #Soma dos valores da lista 'vendas'
        print(f'Despesas: R${sum(compraDeEstoque)}') #Soma dos valores da lista 'compraDeEstoque'
        print(f'Caixa: R${sum(vendas) - sum(compraDeEstoque)}\n') #Determina a receita total da loja pela
        # subtração dos lucros pelas despesas

print('\n\nCaixa Fechado!')

"""