times = []

while True:
    print("\n=== CAMPEONATO BRASILEIRO ===")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        nome = input("Nome do time: ")

        time = {
            "nome": nome,
            "pontos": 0,
            "vitorias": 0,
            "empates": 0,
            "derrotas": 0
        }

        times.append(time)

        print("Time cadastrado com sucesso!")

    elif op == "2":

        print("\n=== TIMES CADASTRADOS ===")

        if len(times) == 0:
            print("Nenhum time cadastrado.")

        else:
            for t in times:
                print(
                    f"{t['nome']} | "
                    f"{t['pontos']} pts | "
                    f"V:{t['vitorias']} "
                    f"E:{t['empates']} "
                    f"D:{t['derrotas']}"
                )

    elif op == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")