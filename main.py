times = []

while True:
    print("\n=== CAMPEONATO BRASILEIRO ===")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        nome = input("Nome do time: ")
        times.append(nome)
        print("Time cadastrado com sucesso!")

    elif op == "2":
        print("Funcionalidade em desenvolvimento")

    elif op == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")