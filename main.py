from classes import *
from random import randint


print(TEXT.THE, "\n",TEXT.RESISTENCE)
input(TEXT.WELCOME)
numero_players=input( TEXT.CONFIG)
positive_awnser = ["sim", "ok", "s", "y"]
negative_awnser = ["não", "nao", "n", "nop"]

jogo1 = jogo(numero_players)
same_game = True
jogo1.show_functions()


while same_game:

    print(TEXT.GAME_START)
    input("(Aperte Enter)")
    round_aux = 1
    max = int(numero_players) - 1
    time_player = randint(0, max)
    keep_playing = True
    rejections = 0
    resistence_points = 0
    spy_points = 0
    while keep_playing:
        jogadores_selecionados = jogo1.leader_order(time_player, round_aux)
        result = jogo1.mission_aproval()
        if result:
            incursion_result = jogo1.incursion_success(jogadores_selecionados, round_aux)
            round_aux +=1
            if incursion_result:
               resistence_points += 1
               print("A missão foi um sucesso!")
               sleep(1)
            else:
                spy_points += 1
                sleep(1)
                print("A missão foi sabotada!")
        else:
            rejections += 1
        if (rejections == 6) or (spy_points == 3):
            print("Os espiões ganharam o jogo!")
            break
        if (resistence_points == 3):
            print("A resitência ganhou o jogo")
            break
        if time_player == (int(numero_players) - 1):
            time_player = 0
        else:
            time_player += 1
    print("Você deseja continuar jogando com as mesmas pesoas?")
    if input() in positive_awnser:
        continue
    if input in negative_awnser:
        break
