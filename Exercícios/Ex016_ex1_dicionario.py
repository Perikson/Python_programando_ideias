"""
1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
- Crie um dicionário chamado herói com chave sendo o nome do personagem e o elemento o nível de poder
  do personagem entre 1 a 100. Ex: herói = {‘Flash’:85}.
- Crie outro dicionário que serão as armas que podem ser usadas pelo herói, sendo a chave o nome da arma
  e o elemento o nível de poder de 0 a 100. Ex: arma = {‘Escudo do Capitão América’:60}
- Crie um último dicionário representado os vilões sendo a chave o nome e o elemento o nível de poder de 0 a 200.
  Ex: vilao={‘Thanos’:175}
Após isso o usuário poderá escolher um herói, uma arma soma os pontos de poder e escolher um vilao para lutar,
apresente quem foi o vencedor, caso for o herói imprima a arma usada. Caso resulte em empate informe na saída.
Observação: Pode definir qualquer herói,vilao e arma que quiser.
"""


#Declaração dos dicionários
herois ={'Homem aranha':85,'Goku':100,'Flash':90}
armas = {'Martelo do Thor':90,'Pistola da viuva negra':55,'Roupa do Pantera Negra':80}
viloes = {'Thanos':180,'Venom':145,'Ultron':160}

#Escolha do usuario
heroi_escolhido = input('Digite o heroi escolhido: ')
arma_escolhida = input('Digite a arma escolhida: ')
vilao_escolhido = input('Digite o vilao escolhido: ')

#Soma do nivel de poder heroi e arma
nivel_poder_heroi_arma=herois[heroi_escolhido] + armas[arma_escolhida]

#Se o nivel de poder do heroi e arma é maior que vilao faça:
if nivel_poder_heroi_arma > viloes[vilao_escolhido]:
    print(f'O vencedor é {heroi_escolhido} com {arma_escolhida}')
#Se não se nivel de poder do heroi e arma é igual a vilao faça:
elif nivel_poder_heroi_arma == viloes[vilao_escolhido]:
    print(f'Deu empate')
else: #Senão faça:
    print(f'O vencedor é {vilao_escolhido}! Terra em Perigo')

