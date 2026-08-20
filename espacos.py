espacos = []

def cadastrar_espaco():
    id_espaco = input("ID do espaço: ")
    nome = input("Nome do espaço: ")
    capacidade = int(input("Capacidade: "))
    projetor = input("Possui projetor? (s/n): ")
    tem_projetor = projetor == "s"

    espacos.append({"id_espaco": id_espaco, "nome": nome, "capacidade": capacidade, "tem_projetor": tem_projetor})
    print("Espaço cadastrado com sucesso!")


def listar_espacos():
    if not espacos:
        print("Não tem nenhum espaço cadastrado")
        return

    print("Espaçõses cadastrados: ")
    for espaco in espacos:
        print(f"ID: {espaco['id_espaco']}",
              f"Nome: {espaco['nome']}",
              f"Capacidade: {espaco['capacidade']}",
              f"Projetor: {espaco['tem_projetor']}")

import escopo

while True:
    print("1 - Cadastrar espaço")
    print("2 - Listar espaços")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        escopo.cadastrar_espaco()
    elif opcao == "2":
        escopo.listar_espacos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")


espacos = [
    {
        "codigo": "S01",
        "tipo": "Sala",
        "nome": "Sala de Aula 01",
        "disponivel": True
    },
    {
        "codigo": "S02",
        "tipo": "Sala",
        "nome": "Sala de Aula 02",
        "disponivel": True
    },
    {
        "codigo": "S03",
        "tipo": "Sala",
        "nome": "Sala de Aula 03",
        "disponivel": True
    },
    {
        "codigo": "S04",
        "tipo": "Sala",
        "nome": "Sala de Aula 04",
        "disponivel": True
    },
    {
        "codigo": "L01",
        "tipo": "Laboratório",
        "nome": "Laboratório de Informática 01",
        "disponivel": True
    },
    {
        "codigo": "L02",
        "tipo": "Laboratório",
        "nome": "Laboratório de Informática 02",
        "disponivel": True
    },
    {
        "codigo": "L03",
        "tipo": "Laboratório",
        "nome": "Laboratório de Redes",
        "disponivel": True
    },
    {
        "codigo": "A01",
        "tipo": "Auditório",
        "nome": "Auditório Principal",
        "disponivel": True
    }
]
