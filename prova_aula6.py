# Desenvolva um programa em Python que funcione como um sistema de gerenciamento de uma biblioteca.
# O programa deverá permitir que os usuários realizem as seguintes operações:

# Funcionalidades:
# Adicionar Livros à Biblioteca:

# O programa deve permitir que o usuário adicione novos livros à biblioteca. Para cada livro, o sistema deve armazenar:
# Título do livro
# Autor do livro
# Número de cópias disponíveis
# Listar Todos os Livros Disponíveis:

# O programa deve exibir uma lista de todos os livros disponíveis na biblioteca, incluindo o título, autor e o número de cópias disponíveis.
# Empréstimo de Livros:

# O programa deve permitir que os usuários façam o empréstimo de um livro, o que reduzirá o número de cópias disponíveis para aquele livro.
# Se não houver cópias disponíveis, o programa deve informar ao usuário que o livro não pode ser emprestado.
# Devolução de Livros:

# O programa deve permitir que os usuários devolvam livros, aumentando o número de cópias disponíveis.
# Verificar Disponibilidade de um Livro:

# O programa deve permitir que o usuário consulte se um livro específico está disponível na biblioteca, verificando o número de cópias.
# Mostrar Livros Emprestados a um Usuário Específico:

# O programa deve permitir que o usuário visualize a lista de todos os livros que ele já pegou emprestado.

###DICIONÁRIOS:

biblioteca = {'livro': {}}



###VARIÁVEIS:

n = 1 #operador para adicionar a prdem do livro na biblioteca

##FUNÇÕES:

def add_livro (titulo , autor , nu_copias_disp):
    global n
    novo_livro = {'Titulo': titulo , 'Autor' : autor , 'Número de Cópias' : nu_copias_disp}
    biblioteca['livro'][n] = novo_livro
    n += 1
    return biblioteca

def exibir_biblioteca (biblioteca):
    print('Lista de livros:')
    for identificador , livro in biblioteca['livro'].items():
        print(f'ID: {identificador}')
        print(f" - Título: {livro['Titulo']}")
        print(f" - Autor: {livro['Autor']}")
        print(f" - Números de Cópias: {livro['Número de Cópias']}")
        
def aluguel (biblioteca , titulo):
    for identificador , livro in biblioteca['livro'].items():
        if livro['Titulo'] == titulo:
            if livro['Número de Cópias'] > 0:
                livro['Número de Cópias'] -= 1
                return
            else:
                print(f"O livro '{livro['Titulo']}' não possui cópia disponível!")
                return

    print(f"Livro '{titulo}' não encontrado")

def devolucao (biblioteca , titulo):
    for identificador , livro in biblioteca['livro'].items():
        if livro['Titulo'] == titulo:
            livro['Número de Cópias'] += 1
            return   
    print(f"Livro '{titulo}' não encontrado")

def verificacao_disponibilidade (biblioteca , titulo):
    for identificador , livro in biblioteca['livro'].items():
        if livro['Titulo'] == titulo:
            print(f"A disponibilidade do Livro {titulo} é: {livro['Número de Cópias']}")
            return
    print(f"Livro '{titulo}' não encontrado")


####FUNÇÃO PRINCIPAL:
print('====='*10)
print('\n\n')
print('Biblioteca Infinity\n\nBem Vindo!')
print('\n\n')

while True:
    print('====='*10)
    print('\n\n')
    print('Menu principal:\n\n [AM] - Aministrador\n [US] - Usuário\n [SR] - Sair')
    op_principal = input('\nQual é o seu acesso: ')
    op_principal_min = op_principal.lower()
    print('\n\n')
    print('====='*10)
    if op_principal_min == 'am':
        while True:
            print('\n\n')
            print('Menu do Administrador:\n\n [AD] - Adicionar Livro\n [EB] - Exibir lista de Livros\n [VD] - Verificar Disponibilidade\n [RT] - Retornar ao Menu Principal ')
            op_admin = input('\nQual é a opção desejada: ')
            op_admin_min = op_admin.lower()
            print('\n\n')
            print('====='*10)
            if op_admin_min == 'ad':
                print('\n\n')
                titulo = input('Qual é Título do Livro: ')
                autor = input('Qual é o nome do autor do Livro: ')
                nu_copias_disp = int(input('Quantas cópias deste Livro temos disponível: '))
                add_livro(titulo , autor , nu_copias_disp)
                print('\n')
                print(f'O Livro {titulo} foi adicionado a Biblioteca!')
                print('\n\n')
                print('====='*10)
                continue
            elif op_admin_min == 'eb':
                print('\n\n')
                exibir_biblioteca(biblioteca)
                print('\n\n')
                print('====='*10)
                continue
            elif op_admin_min == 'vd':
                print('\n\n')
                titulo = input('Qual o nome do Livro que deseja verificar a disponibilidade: ')
                print('\n')
                verificacao_disponibilidade(biblioteca , titulo)
                print('\n\n')
                print('====='*10)
                continue
            elif op_admin_min == 'rt':
                print('\n\n')
                print('Retornando ao Menu Principal...')
                print('\n\n')
                break
            else:
                print('\n\n')
                print('Opção Inválida!\nTente Novamente!')
                print('\n\n')
                print('====='*10)
                continue
        continue
    elif op_principal_min == 'us':
        print('\n\n')
        usuario = input('Qual é o nome do usuário: ')
        n_usu = usuario
        n_usu = []
        print('\n\n')
        print('====='*10)
        print('\n\n')
        print(f'Bem Vindo {usuario}!')
        print('\n\n')
        while True:
            print('====='*10)
            print('\n\n')
            print(f'Menu do Usuário:\n\n [AL] - Alugar Livro\n [DV] - Devolver Livro\n [LU] - Exibir Lista de Livros Alugados pelo Usuário {usuario}\n [EB] - Exibir lista de Livros\n [VD] - Verificar Disponibilidade\n [RT] - Retornar ao Menu Principal ')
            op_usu = input('\nQual é a opção desejada: ')
            op_usu_min = op_usu.lower()
            print('\n\n')
            print('====='*10)
            if op_usu_min == 'al':
                print('\n\n')
                titulo = input('Qual é Título do Livro que deseja Alugar: ')
                aluguel(biblioteca , titulo)
                print(f'O Livro {titulo} foi aludado pelo usuário {usuario}')
                n_usu.append(titulo)
                print('\n\n')
                continue
            elif op_usu_min == 'dv':
                print('\n\n')
                titulo = input('Qual é Título do Livro que deseja Devolver: ')
                devolucao(biblioteca , titulo)
                print(f'O Livro {titulo} foi devolvido pelo usuário {usuario}')
                print('\n\n')
                continue
            elif op_usu_min == 'lu':
                print('\n\n')
                print(f'Lista de Livros alugados pelo usuário {usuario} ')
                print('\n')
                for i in n_usu:
                    print(f'- {i}')
                print('\n\n')
                continue
            elif op_usu_min == 'eb':
                print('\n\n')
                exibir_biblioteca(biblioteca)
                print('\n\n')
                print('====='*10)
                continue
            elif op_usu_min == 'vd':
                print('\n\n')
                titulo = input('Qual o nome do Livro que deseja verificar a disponibilidade: ')
                print('\n')
                verificacao_disponibilidade(biblioteca , titulo)
                print('\n\n')
                print('====='*10)
                continue
            elif op_usu_min == 'rt':
                print('\n\n')
                print('Retornando ao Menu Principal...')
                print('\n\n')
                break
            else:
                print('\n\n')
                print('Opção Inválida!\nTente Novamente!')
                print('\n\n')
                continue
        continue
    elif op_principal_min == 'sr':
        print('\n\n')
        print('Saindo...')
        print('\n\n')
        print('====='*10)
        break
    else:
        print('\n\n')
        print('Opção Inválida!\nTente Novamente!')
        print('\n\n')
        continue






