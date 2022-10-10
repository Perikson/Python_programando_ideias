""""""
"""
1 - Crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra 
para os preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, 
recebendo estes dados do usuário (input). Por fim, some os preços, imprima o valor total e os
produtos do carrinho.

# 1
listaCarrinho = [] #Criando a lista que vai receber os produtos
listaPrecos = [] #Criando a lista que vai receber os preços
contProdutos = 0 #Criação de variáveis
valorTotal = 0
produto = ''

while contProdutos < 5: #Loop para acrescentar 5 itens nas listas
    produto = input('Produto: ')
    listaCarrinho.append(produto) #Adicionando elemento à lista
    preco = float(input('Preço: '))
    listaPrecos.append(preco)
    contProdutos += 1

for id in range(0, 5): # 0, 1, 2, 3, 4
    valorTotal += listaPrecos[id] #Somando todos os elementos da lista

#Obs.: O acesso aos elementos está sendo feito via índice. A variável id terá os valores
#0, 1, 2, 3, 4 de acoro com o range(0, 5).
#Portanto, por baixo dos panos, o loop for está realizando o seguinte:
#listaPrecos[0] + listaPrecos[1] + listaPrecos[2] + listaPrecos[3] + listaPrecos[4]

print(f'Produtos comprados: {listaCarrinho}')
print(f'Valor total: R${valorTotal}')

"""