from time import *
from random import *
class jogo:
    def __init__(self, numero_jogadores):
        self.numero_jogadores = numero_jogadores
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
    
    def show_function(self):
        for i in range(0, self.numero_jogadores):
            input(self.nome_jogadores[i][0], " aperte enter para ver sua função")
            input(self.nome_jogadores[i][0], " você é: ", self.nome_jogadores[i][1], end='\r')
            input()
    
    def leader_order(self, leader, round):
        #this function must be completed later
        print(" O lider da rodada é: ", self.nome_jogadores[leader],[0])
        if round == 1:
            leader_choice = 2
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)

        elif round == 2:
            leader_choice = 3
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)

        elif round == 3:
            list_restricted = []
            leader_choice = 3
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)

        elif round == 4:
            leader_choice = 4
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)

        elif round == 5:
            leader_choice = 4
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)

    
    def list_options(self):
        list = []
        for i in range(0, self.nome_jogadores):
            list.extend(self.nome_jogadores[i][0])
        list = [item.center(15, " ") for item in list]
        list = "|".join(list)
        return list
    
    def print_and_save_options(self, leader, list, restrictions, chosen_list):
        print (self.nome_jogadores[leader][0], "suas opções de escolha são: \n")
        for i in list:
            if list.index(list) not in restrictions:
                print(list(i), end="")
        chosen = input("Quem voce chamará para a missão?")
        restrictions.extend(list.index(chosen))
        chosen_list.extend(chosen)

        

    def mission_aproval(self):
        aproving_votes = 0
        rejecting_votes = 0

        types_of_aproval = ["aprovo", "sim", "aceito", "ok"]
        for i in range(0, self.numero_jogadores):
            vote = input(f"{self.nome_jogadores[i][0]}, você aprova a missão? ")
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

#Begining of the code/game
TEXTO_1 = """"
                .___________. __    __   _______ 
                |           ||  |  |  | |   ____|
                `---|  |----`|  |__|  | |  |__   
                    |  |     |   __   | |   __|  
                    |  |     |  |  |  | |  |____ 
                    |__|     |__|  |__| |_______| """
TEXTO_2 = """
██████╗ ███████╗███████╗██╗███████╗████████╗███████╗███╗   ██╗ ██████╗███████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔════╝
██████╔╝█████╗  ███████╗██║███████╗   ██║   █████╗  ██╔██╗ ██║██║     █████╗  
██╔══██╗██╔══╝  ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╗██║██║     ██╔══╝  
██║  ██║███████╗███████║██║███████║   ██║   ███████╗██║ ╚████║╚██████╗███████╗
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                                                              """
TEXTO_3 = """Bem vindo ao jogo de estratégia e espioangem para ser jogado em grupo!
                         Aperte qualquer tecla para continuar"""
TEXTO_4 = "Insira o núnero de jogadores da partida: "

print(TEXTO_1, "\n", TEXTO_2)
input(TEXTO_3)
numero_players=input(TEXTO_4)

jogo1 = jogo(numero_players)
round_aux = 0
time_player = randint(0,6)
keep_playing = True
jogo1.show_function
rejections = 0
while keep_playing:
    jogo1.leader_order(time_player, round_aux)
    result = jogo1.mission_aproval()
    if result:
        round_aux +=1
        #função de missão
    else:
        rejections += 1
    
    