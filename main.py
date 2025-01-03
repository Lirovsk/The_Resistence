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
            return chosed

        elif round == 2:
            leader_choice = 3
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)
            return chosed

        elif round == 3:
            list_restricted = []
            leader_choice = 3
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)
            return chosed

        elif round == 4:
            leader_choice = 4
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)
            return chosed

        elif round == 5:
            leader_choice = 4
            list_restricted = []
            chosed = []
            for i in range(0, leader_choice):
                self.print_and_save_options(leader, self.list_options, list_restricted, chosed)
            print ( "Os selecionados para a missão foram: ",  chosed)
            return chosed

    
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

    def incursion_success (self, list_of_players, round):
        List_result = []
        positive = 0
        negative = 0
        positive_awnser = ["sim", "ok", "s", "y"]
        negative_awnser = ["não", "nao", "n", "nop"]
        if round in [1,2,3,5]:
            for i in list_of_players:
                print(f"{list_of_players[i]}, deseja sabotar essa missão?")
                result_incurssoin = input()
                if result_incurssoin in positive_awnser:
                    List_result.extend(1)
                elif result_incurssoin in negative_awnser:
                    List_result.extend(0)
                for i in List_result:
                    if List_result[i] == 1:
                        positive += 1
                    else:
                        negative += 1
                if negative > 0:
                    return False
                else:
                    return True
        else:
            for i in list_of_players:
                print(f"{list_of_players[i]}, deseja sabotar essa missão?")
                result_incurssoin = input()
                if result_incurssoin in positive_awnser:
                    List_result.extend(1)
                elif result_incurssoin in negative_awnser:
                    List_result.extend(0)
                for i in List_result:
                    if List_result[i] == 1:
                        positive += 1
                    else:
                        negative += 1
                if negative >= 2:
                    return False
                else:
                    return True



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
TEXTO_5 = """O jogo está prestes a começar, atenção aos seu arredores! A pessoa ao seu lado pode ser um espião"""
print(TEXTO_1, "\n", TEXTO_2)
input(TEXTO_3)
numero_players=input(TEXTO_4)
positive_awnser = ["sim", "ok", "s", "y"]
negative_awnser = ["não", "nao", "n", "nop"]

jogo1 = jogo(numero_players)
same_game = True

while same_game:
    print(TEXTO_5)
    input("(Aperte Enter)")
    round_aux = 1
    time_player = randint(0,6)
    keep_playing = True
    rejections = 0
    resistence_points = 0
    spy_points = 0
    jogo1.show_function()
    while keep_playing:
        jogadores_selecionados = jogo1.leader_order(time_player, round_aux)
        result = jogo1.mission_aproval()
        if result:
            incursion_result = jogo1.incursion_success(result, round_aux)
            round_aux +=1
            if incursion_result:
               resistence_points += 1
            else:
                spy_points += 1
        else:
            rejections += 1
        if (rejections == 6) or (spy_points == 3):
            print("Os espiões ganharam o jogo!")
            break
        if (resistence_points == 3):
            print("A resitência ganhou o jogo")
            break
    print("Você deseja continuar jogando com as mesmas pesoas?")
    if input() in positive_awnser:
        continue
    if input in negative_awnser:
        break
    