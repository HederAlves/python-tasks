# EXIGÊNCIA DE CÓDIGO E CONSOLE 1
# Mensagem de boas-vindas com meu nome
print("Bem-vindo(a) ao sistema de gerenciamento de livros! Desenvolvido por Heder Alves")

# EXIGÊNCIA DE CÓDIGO 2 e 7
# Lista de livros e ID global
lista_livro = []  # <- Aqui é a lista que irá conter os dicionários
id_global = 0

# EXIGÊNCIA DE CÓDIGO 3
# Função para cadastrar um livro
def cadastrar_livro(id):
    print("\n----------------------------------------------")
    print("------------ Menu Cadastrar Livro ------------")
    print(f"Id do Livro: {id}")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    # Dicionário
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}

    # Adiciona dicionário à lista de livros
    lista_livro.append(livro)
    print("----------------------------------------------")
    print("Livro cadastrado com sucesso!")
    print("----------------------------------------------\n")

# EXIGÊNCIA DE CÓDIGO 4
# Função para consultar livros
def consultar_livro():
    while True:
        print("\n----------------------------------------------")
        print("------------ Menu Consultar Livro -------------")
        print("Escolha a opção desejada:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input(">>")
        print()

        if opcao == "1":
            print("====== Lista de Todos os Livros ======")
            for livro in lista_livro:
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print()
        elif opcao == "2":
            try:
                id_pesquisa = int(input("Digite o ID do livro: "))
                print("-----------------------------------------")
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_pesquisa:
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print()
                        encontrado = True
                if not encontrado:
                    print("Livro com este ID não encontrado.")
            except ValueError:
                print("ID inválido.")
        elif opcao == "3":
            autor_pesquisa = input("Digite o nome do autor: ")
            print("-----------------------------------------")
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_pesquisa.lower()]
            if encontrados:
                for livro in encontrados:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print()
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

# EXIGÊNCIA DE CÓDIGO 5
# Função para remover um livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("\n Digite o ID do livro a ser removido: "))
            print("-----------------------------------------")
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print("----------------------------------------------")
                    print("Livro removido com sucesso!")
                    print("----------------------------------------------\n")
                    return
            print("Id inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# EXIGÊNCIA DE CÓDIGO 6
# Menu principal
while True:
    print("\n---------------------------------------------")
    print("------------- Menu Principal ----------------")
    print("Escolha a opção desejada:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro(s)")
    print("3. Remover Livro")
    print("4. Sair")
    escolha = input(">>")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha == "2":
        consultar_livro()
    elif escolha == "3":
        remover_livro()
    elif escolha == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.\n")
