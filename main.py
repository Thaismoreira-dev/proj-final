from notificacoes import (
    horario_indisponivel,
    data_invalida,
    domingo_indisponivel,
    local_reservado,
    reserva_realizada,
    reserva_cancelada,
    opcao_invalida
)

from espacos import espacos, retornar_espacos_disponiveis


def listar_espacos_disponiveis():
    print("=== ESPAÇOS DISPONÍVEIS ===")

    for espaco in retornar_espacos_disponiveis():
        print(f"{espaco['codigo']} - {espaco['nome']} ({espaco['tipo']})")

#A parte que ficou comigo Gabriel Cavalcante
import reservas
codigo = input("Código do espaço: ")
responsavel = input("Responsável: ")
reservas.criar_reserva(codigo, responsavel)
reservas.listar_reservas()
resultado = reservas.consultar_reserva(codigo)
if resultado:
    print("Reserva encontrada!")
else:
    print("Reserva não encontrada!")
