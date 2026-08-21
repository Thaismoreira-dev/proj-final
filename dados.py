from datetime import date, timedelta


# =========================
# ESPAÇOS
# =========================

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


# =========================
# RESPONSÁVEIS
# =========================

responsaveis = [
    "Maria Eduarda",
    "Thais Moreira",
    "Gabriel Cavalcante",
    "Carlos Emanuel",
    "João Marcos",
    "Alexandre",
    "Adriana",
    "Sávio",
    "Amerilton",
    "Zayra"
]


# =========================
# HORÁRIOS
# =========================

horarios = [
    "[1] 07:30 às 08:30",
    "[2] 08:30 às 09:20",
    "[3] 09:50 às 10:40",
    "[4] 10:40 às 11:30",
    "[5] 13:00 às 13:50",
    "[6] 13:50 às 14:40",
    "[7] 15:00 às 15:50",
    "[8] 15:50 às 16:40",
    "[9] 18:30 às 19:20",
    "[10] 19:20 às 20:10",
    "[11] 20:30 às 21:20",
    "[12] 21:20 às 22:10",
    "[13] 22:10 às 23:00"
]


# =========================
# DATAS
# =========================

data_atual = date.today()

datas = [
    (data_atual + timedelta(days=i)).strftime("%d/%m/%Y")
    for i in range(30)
]
