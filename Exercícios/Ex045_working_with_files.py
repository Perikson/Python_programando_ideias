def inserir():
    with open('Notas_escolas.txt', 'a') as NE:  # Abertura no modo append.
        NE.write('Aluno(a): ' + input('Aluno(a): ') + ' ' + 'Nota: ' + input('Nota: ') + '\n')
        print('\nDados Inseridos.\n')


def exibir():
    with open('Notas_escolas.txt') as NE:  # O modo de abertura padrão é o leitura.
        print(NE.read())
        print('\nDados Apresentados.')


def situacao():
    with open('Notas_escolas.txt') as NE:  # O modo de abertura padrão é o leitura.
        lista_linhas = NE.readlines()
        for dado in lista_linhas:
            id_1 = dado.index(':')  # Retorna o indice do primeiro ':'.
            id_2 = dado.index('Nota')  # Retorna o indice da primeira letra da palavra Nota.
            nome = dado[id_1 + 1:id_2 - 1]  # Slice para retorno do nome. Os números são para a remoção dos espaços
# Em branco.

            id_3 = dado.index(':', 9)  # Busca a partir do índice 9 a string ':'.
            nota = float(dado[id_3 + 1:])

            if nota >= 7:
                print(f'{nome} com nota {nota} está APROVADO.')
            else:
                print(f'{nome} com nota {nota} está REPROVADO.')


while True:

    print('\nMenu:\n'
          '1 - Inserir aluno(a) e nota.\n'
          '2 - Exibir aluno(a) e notas.\n'
          '3 - Exibir alunos aprovados e reprovados.\n'
          '4 - Sair\n')

    op = int(input('Qual opeção você deseja: '))

    if op == 1:
        print()
        inserir()

    elif op == 2:
        print()
        exibir()

    elif op == 3:
        print()
        situacao()

    elif op == 4:
        print('Programa Encerrado.')
        break

    else:
        print('Informe uma opção possível.')
