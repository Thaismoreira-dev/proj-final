espacos = [
    {"codigo": "S01", "tipo": "Sala", "nome": "Sala de Aula 01", "disponivel": True},
    {"codigo": "S02", "tipo": "Sala", "nome": "Sala de Aula 02", "disponivel": True},
    {"codigo": "S03", "tipo": "Sala", "nome": "Sala de Aula 03", "disponivel": True},
    {"codigo": "S04", "tipo": "Sala", "nome": "Sala de Aula 04", "disponivel": True},
    {"codigo": "L01", "tipo": "Laboratório", "nome": "Laboratório de Informática 01", "disponivel": True},
    {"codigo": "L02", "tipo": "Laboratório", "nome": "Laboratório de Informática 02", "disponivel": True},
    {"codigo": "L03", "tipo": "Laboratório", "nome": "Laboratório de Redes", "disponivel": True},
    {"codigo": "A01", "tipo": "Auditório", "nome": "Auditório Principal", "disponivel": True}
]

reservas = []


def listar_espacos():
    print("Espaços")
    for espaco in espacos:
        status = "Disponível" if espaco["disponivel"] else "Reservado"
        print(f"{espaco['codigo']} - {espaco['nome']} ({status})")


def reservar_espaco():
    codigo = input("Digite o código do espaço: ").upper()

    for espaco in espacos:
        if espaco["codigo"] == codigo:
            if espaco["disponivel"]:
                nome_usuario = input("Nome do responsável: ")

                espaco["disponivel"] = False

                reservas.append({
                    "responsavel": nome_usuario,
                    "codigo": codigo,
                    "nome_espaco": espaco["nome"]
                })

                print("Reserva realizada com sucesso!")
            else:
                print("Espaço já está reservado!")
            return

    print("Código não encontrado!")


def listar_reservas():
    if not reservas:
        print("Nenhuma reserva cadastrada.")
        return

    print("\n=== RESERVAS ===")
    for reserva in reservas:
        print(
            f"Responsável: {reserva['responsavel']} | "
            f"Espaço: {reserva['codigo']} - {reserva['nome_espaco']}"
        )
while True:
    print("Sistemas de reserva de espaços: ")
    print("1 - Listar espaços")
    print("2 - Reservar espaço")
    print("3 - Listar reservas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_espacos()
    elif opcao == "2":
        reservar_espaco()
    elif opcao == "3":
        listar_reservas()
    elif opcao == "4":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")
