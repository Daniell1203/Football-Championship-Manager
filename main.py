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
        print("\n=== TIMES CADASTRADOS ===")

        if len(times) == 0:
            print("Nenhum time cadastrado.")

        else:
            for i, time in enumerate(times, start=1):
                print(f"{i} - {time}")

    elif op == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")