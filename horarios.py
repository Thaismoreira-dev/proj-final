NOMES = [
    'Saulo', 'JM', 'Ronald'
]

def menu_inicial():
    print('Bem-vindo, usuário')
    print('Esse é o menu inicial')

    nome = input('Digite o seu nome: ')
    return nome.upper()


def quatro_op(a, b):
    soma = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return soma, sub, mul, div


def i18n(nome):
    inicial = nome[0]
    final = nome[-1]
    contar_interna = len(nome) - 2

    return f'{inicial}{contar_interna}{final}'
    return inicial + str(contar_interna) + final


def contar_cv(texto):

#     n_vogais = len([letra for letra in texto if letra in 'aeiou'])
#     n_consoantes = len([letra for letra in texto if letra not in 'aeiou '])
# ####
    n_vogais = 0
    for letra in texto:
        if letra in 'aeiou':
            n_vogais += 1

    n_consoantes = 0
    for letra in texto:
        if letra not in 'aeiou ':
            n_consoantes += 1

    return f'{n_vogais}V{n_consoantes}C'
