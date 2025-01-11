from time import *
from random import *
import os
from colorama import Cursor, init
class jogo:
    def __init__(self, numero_jogadores):
        self.numero_jogadores = int(numero_jogadores)
        self.numero_espioes= 0
        self.nome_jogadores = []

        if self.numero_jogadores % 2 == 0:
            self.numero_espioes = (self.numero_jogadores // 2) - 1
        else:
            self.numero_espioes = (self.numero_jogadores -1) // 2
        
        for i in range(1, self.numero_jogadores + 1):
            self.add_jogador(i)

        self.create_spys()
        
    def add_jogador(self, numero):
        nome = input(f"Digite o nome do jogador {numero}: ")
        self.nome_jogadores.append([nome])
    
    def create_spys(self):
        created_spys = 0
        for i in range (0, self.numero_jogadores):
            if created_spys < self.numero_espioes:
                if randint(0, 1) == 1:
                    self.nome_jogadores[i].append("espião")
                    created_spys += 1
                else:
                    self.nome_jogadores[i].append("resistencia")
            
            else:
                self.nome_jogadores[i].append("resistencia")
    
    def show_functions(self):
        os.system('cls')
        for i in range(0, self.numero_jogadores):
            print(TEXT.THE, TEXT.RESISTENCE)
            print(self.nome_jogadores[i][0], end=' ')
            input( "aperte enter para ver sua função")
            print(self.nome_jogadores[i][0], "você é:", self.nome_jogadores[i][1])
            input("Aperte qualquer tecla para esconder sua identidade antes de passaar o aparelho para o próximo jogador")
            os.system('cls')
    
    def leader_order(self, leader, round):
        #this function must be completed later
        print("\n \nO lider da rodada é: ", self.nome_jogadores[leader][0])
        sleep(1)
        print("\n")
        round_local = int(round)
        if round_local == 1:
            leader_choice = 2
            list_restricted = []
            chosed = []
            lista = self.list_options()
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, lista, list_restricted, chosed)
            print ( "\n \nOs selecionados para a missão foram: ",  chosed)
            return chosed

        elif round_local == 2:
            leader_choice = 3
            list_restricted = []
            chosed = []
            lista = self.list_options()
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, lista, list_restricted, chosed)
            print ( "\n \nOs selecionados para a missão foram: ",  chosed)
            return chosed

        elif round_local == 3:
            list_restricted = []
            leader_choice = 3
            chosed = []
            lista = self.list_options()
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, lista, list_restricted, chosed)
            print ( "\n \nOs selecionados para a missão foram: ",  chosed)
            return chosed

        elif round_local == 4:
            leader_choice = 4
            list_restricted = []
            chosed = []
            lista = self.list_options()
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, lista, list_restricted, chosed)
            print ( "\n \nOs selecionados para a missão foram: ",  chosed)
            return chosed

        elif round_local == 5:
            leader_choice = 4
            list_restricted = []
            chosed = []
            lista = self.list_options()
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, lista, list_restricted, chosed)
            print ( "\n \nOs selecionados para a missão foram: ",  chosed)
            return chosed

    
    def list_options(self):
        list = []
        for i in range(0, self.numero_jogadores):
            list.append(self.nome_jogadores[i][0])
            #print(list)
        return list
    
    def print_and_save_options(self, leader, list_aux, restrictions, chosen_list):
        #print (list_aux)
        print ("\n\n", self.nome_jogadores[leader][0], "suas opções de escolha são:")
        for i in range(0, len(list_aux)):
            if list_aux.index(list_aux[i]) not in restrictions:
                print(list_aux[i], end=" ")
        chosen = input("\n \nQuem voce chamará para a missão?\n")
        restrictions.append(list_aux.index(chosen))
        chosen_list.append(chosen)

        

    def mission_aproval(self):
        aproving_votes = 0
        rejecting_votes = 0

        types_of_aproval = ["aprovo", "sim", "aceito", "ok"]
        for i in range(0, self.numero_jogadores):
            vote = input(f"{self.nome_jogadores[i][0]}, você aprova a missão? ")
            print(Cursor.UP(1), " "*50, Cursor.UP(1))
            if vote.lower() in types_of_aproval:
                aproving_votes += 1
            else:
                rejecting_votes += 1
        if aproving_votes > rejecting_votes:
            print("Missão Aprovada!")
            print(f"A missão obeteve {aproving_votes} votos a favor e {rejecting_votes} votos contra.")
            final_aproval = True
        elif aproving_votes == rejecting_votes:
            print("Missão Reprovada!")
            print("A missão obeteve a mesma quantidade de votos a favor e contra.")
            final_aproval =False
        else:
            print("Missão Reprovada!")
            print(f"A missão obeteve {aproving_votes} votos a favor e {rejecting_votes} votos contra.")
            final_aproval = False
        return final_aproval

    def incursion_success (self, list_of_players, round):
        List_result = []
        positive = 0
        round_local = int(round)
        negative = 0
        positive_awnser = ["sim", "ok", "s", "y"]
        negative_awnser = ["não", "nao", "n", "nop"]
        if round_local in [1,2,3,5]:
            #print("controle: ", list_of_players)
            for i in range(0, len(list_of_players)):
                #print (i)
                print(f"{list_of_players[i]}, deseja sabotar essa missão?")
                result_incurssoin = input()
                print(Cursor.UP(1), " "*70, Cursor.UP(2))
                if result_incurssoin in positive_awnser:
                    List_result.append(1)
                elif result_incurssoin in negative_awnser:
                    List_result.append(0)
            for a in range(0,len(List_result)):
                #print(a)
                #print(List_result)
                if List_result[a] == 0:
                    positive += 1
                else:
                    negative += 1
                #print(List_result)
            if negative > 0:
                return False
            else:
                return True
        else:
            #print("controle: ", list_of_players)
            for i in range(0, len(list_of_players)):
                #print (i)
                print(f"{list_of_players[i]}, deseja sabotar essa missão?")
                result_incurssoin = input()
                print(Cursor.UP(1), " "*50, Cursor.UP(1))
                if result_incurssoin in positive_awnser:
                    List_result.append(1)
                elif result_incurssoin in negative_awnser:
                    List_result.append(0)
            for a in range(0,len(List_result)):
                #print(a)
                #print(List_result)
                if List_result[a] == 0:
                    positive += 1
                else:
                    negative += 1
                #print(List_result)
            if negative > 1:
                return False
            else:
                return True


class TEXT:
    #class designed to store all the TEXT that will be used in the game
    THE = """
                .___________. __    __   _______ 
                |           ||  |  |  | |   ____|
                `---|  |----`|  |__|  | |  |__   
                    |  |     |   __   | |   __|  
                    |  |     |  |  |  | |  |____ 
                    |__|     |__|  |__| |_______| """
    RESISTENCE =  """
██████╗ ███████╗███████╗██╗███████╗████████╗███████╗███╗   ██╗ ██████╗███████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔════╝
██████╔╝█████╗  ███████╗██║███████╗   ██║   █████╗  ██╔██╗ ██║██║     █████╗  
██╔══██╗██╔══╝  ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╗██║██║     ██╔══╝  
██║  ██║███████╗███████║██║███████║   ██║   ███████╗██║ ╚████║╚██████╗███████╗
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                                                              """
    WELCOME = """Bem vindo ao jogo de estratégia e espioangem para ser jogado em grupo!
                        Aperte qualquer tecla para continuar"""
    CONFIG = "Insira o núnero de jogadores da partida: "
    GAME_START = """O jogo está prestes a começar, atenção aos seu arredores! A pessoa ao seu lado pode ser um espião"""

class cmd_config: 
    CLEAR = 'cls'
    
    COLOR = 'color'
    PRETO = '0'
    AZUL = '1'
    VERDE = '2'
    VERDE_AGUA = '3'
    VERMELHO = '4'
    ROXO = '5'
    AMARELO = '6'
    BRANCO = '7'
    CINZA = '8'
    AZUL_CLARO = '9'
    VERDE_CLARO = 'A'
    VERDE_AGUA_CLARO = 'B'
    VERMELHO_CLARO = 'C'
    LILAS = 'D'
    AMARELO_CLARO = 'E'
    BRANCO_CLARO = 'F'

    pass