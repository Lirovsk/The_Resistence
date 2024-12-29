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
    
    def leader_order(self, leader, round):
        #this function must be completed later
        print("O líder da missão é o(a) ", self.nome_jogadores[leader], "\n")
        input("Pressione enter para escolher as pessoa para a sua missão")

        if round == 1:
            leader_choice = 2
            list_restrict = []
            self.show_leader_options(self.leader_option(leader), list_restrict)
            for i in range(0, leader_choice):
                pass
        elif round == 2:
            leader_choice = 3
            for i in range(0, leader_choice):
                pass
        elif round == 3:
            leader_choice = 3
            for i in range(0, leader_choice):
                pass
        elif round == 4:
            leader_choice = 4
            for i in range(0, leader_choice):
                pass
        elif round == 5:
            leader_choice = 4
            for i in range(0, leader_choice):
                pass
    
    def leader_option(self, leader):
        showing_options = []
        for i in range (0, self.nome_jogadores):
            showing_options.extend(self.nome_jogadores[i][0])
        for item in showing_options:
            showing_options = item.center(15, " ")
        showing_options = "|".join(showing_options)
        print("O líder da missão é: ", self.nome_jogadores[leader][0])
        return showing_options
    
    def show_leader_options(self, list, list_restriction):
        print("Suas opções de escolha são: \n")
        for i in list:
            if list.index(i) not in list_restriction:
                print(i, end= "")
            


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