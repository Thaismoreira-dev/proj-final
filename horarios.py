
horario=[
 "[1] Manhã",                                                  
 "[2] Tarde",                                                  
 "[3] Noite",                                                  
 ]       
                                           
opcao=int(input('''
╔═════════════════════════════════════════════════════════════════════╗
║           SISTEMA DE RESERVA DE ESPAÇOS FÍSICOS - CAMPUS            ║
║                                                                     ║
╠═════════════════════════════════════════════════════════════════════╣
║ [1] Manhã                                                           ║
║ [2] Tarde                                                           ║
║ [3] Noite                                                           ║
╚═════════════════════════════════════════════════════════════════════╝
Digite o número referente ao horário que deseja reservar:'''))

import os
os.system('cls' if os.name == 'nt' else 'clear')



def reservar_horario (opcao):
    if opcao >=1 and opcao<=3:
        escolha = opcao - 1
        print("Seu horário foi reservado com sucesso!")
        print(horario[escolha])

        arquivo=open ("reserva.txt", "a", encoding='utf-8')
        arquivo

    else:
        print("Opção Inválida")


reservar_horario(opcao)

