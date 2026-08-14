responsaveis = [
'Maria Eduarda',
'Thais Moreira',
'Gabriel Cavalcante',
'Carlos Emanuel',
'João Marcos',
'Alexandre',
'Adriana',
'Sávio',
'Amerilton',
'Zayra'
]

while True:

    print("=" * 70)
    print("          SISTEMA DE CADASTRO DE RESPONSÁVEIS")
    print("=" * 70)
    print("[1] Cadastrar Responsável")
    print("[2] Listar Responsáveis")
    print("[3] Consultar Responsável")
    print("[4] Excluir Responsável")
    print("[0] Encerramento")

    print("=" * 70)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRAR RESPONSÁVEL ---")

        nome = input("Digite o nome do responsável: ")

        responsaveis.append(nome)

        print("Responsável cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE RESPONSÁVEIS ---")

        for i in range(len(responsaveis)):
            print(f"[{i + 1}] {responsaveis[i]}")

    elif opcao == "3":
        print("\n--- CONSULTAR RESPONSÁVEL ---")

        nome = input("Digite o nome: ")

        if nome in responsaveis:
            print("Responsável encontrado!")
        else:
            print("Responsável não encontrado!")

    elif opcao == "4":
        print("\n--- EXCLUIR RESPONSÁVEL ---")

        nome = input("Digite o nome: ")

        if nome in responsaveis:
            responsaveis.remove(nome)
            print("Responsável excluído com sucesso!")
        else:
            print("Responsável não encontrado!")

    elif opcao == "0":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida!")

    input("\nPressione ENTER para continuar...")
