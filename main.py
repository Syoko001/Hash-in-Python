import os

jogadas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def cls():
    return os.system("cls")
    

def table(j):
    p1 = j[0]
    p2 = j[1]
    p3 = j[2]
    p4 = j[3]
    p5 = j[4]
    p6 = j[5]
    p7 = j[6]
    p8 = j[7]
    p9 = j[8]

    print(f"{p1} | {p2} | {p3}")
    print(f"{p4} | {p5} | {p6}")
    print(f"{p7} | {p8} | {p9}")


def title():
    titulo = "\033[1;32mJogo da velha\033[m"
    print("="*30)
    print(f"{titulo:^40}")
    print("="*30)


def menu():
    print("[ 1 ] - \033[33mTutorial\033[m")
    print("[ 2 ] - \033[33mInciar\033[m")
    print("[ 3 ] - \033[33mSair\033[m")


def tutorial():
    cls()
    print("Cada casa do tabuleiro é representada por um número:\n")
    for c in range(0,9):
        jogadas[c] = c+1
    table(jogadas)
    print()
    print("Então, para fazer sua jogada, basta apenas escolher o número que corresponde a casa.")
    print("Divirta-se")
    for c in range(0,9):
        jogadas[c] = " "
    print("Aperte ENTER para continuar!")
    input()



def game():
    total_jogadas = 0
    cls()
    print(f"Começaremos pelo X:")

    while total_jogadas != 9:
        print("1 | 2 | 3 ")
        print("4 | 5 | 6 ")
        print("7 | 8 | 9 \n")
        table(jogadas)

        jogada = int(input("Digite a sua jogada > "))

        if total_jogadas % 2 == 0:
            jogada_valida = True
            while jogada_valida:
                if jogadas[jogada-1] not in "XO":
                    jogadas[jogada-1] = "X"
                    win("X")
                    jogada_valida = False
                else:
                    print("Jogada inválida, tente novamente!")
                    jogada = int(input("Digite a sua jogada > "))
        else:
            jogada_valida = True
            while jogada_valida:
                if jogadas[jogada-1] not in "XO":
                    jogadas[jogada-1] = "O"
                    win("O")
                    jogada_valida = False
                else:
                    print("Jogada inválida, tente novamente!")
                    jogada = int(input("Digite a sua jogada > "))
        total_jogadas += 1
        
        if winOrLose:
            break

        cls()
        

def win(jogador):
    global winOrLose
    global ganhou
    winOrLose = False

    ganhou = f"O jogador {jogador} ganhou!!! Parabéns"

    #jogadas horizontais possiveis
    if jogadas[0] == jogador and jogadas[1] == jogador and jogadas[2] == jogador:
        winOrLose = True
    elif jogadas[3] == jogador and jogadas[4] == jogador and jogadas[5] == jogador:
        winOrLose = True
    elif jogadas[6] == jogador and jogadas[7] == jogador and jogadas[8] == jogador:
        winOrLose = True
    #jogadas verticais possiveis
    elif jogadas[0] == jogador and jogadas[3] == jogador and jogadas[6] == jogador:
        winOrLose = True
    elif jogadas[1] == jogador and jogadas[4] == jogador and jogadas[7] == jogador:
        winOrLose = True
    elif jogadas[2] == jogador and jogadas[5] == jogador and jogadas[8] == jogador:
        winOrLose = True
    #jogadas diagonais possiveis
    elif jogadas[0] == jogador and jogadas[4] == jogador and jogadas[8] == jogador:
        winOrLose = True
    elif jogadas[6] == jogador and jogadas[4] == jogador and jogadas[2] == jogador:
        winOrLose = True

    # 0 | 1 | 2
    # 3 | 4 | 5
    # 6 | 7 | 8


while True:
    cls()
    title()
    menu()
    option = int(input("Digite a opção desejada > \033[33m"))
    print("\033[m", end="")

    if option == 1:
        tutorial()
    elif option == 2:
        game()
        cls()
        table(jogadas)
        print(ganhou)
        print("Aperte ENTER para jogar novamente!")
        input()
        for c in range(0,9):
            jogadas[c] = " "
        cls()

    elif option == 3:
        break
    else:
        cls()
        print("Erro, opção inválida, tente novamente!")