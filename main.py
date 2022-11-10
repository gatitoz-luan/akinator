# -*- coding: utf-8 -*-
import arvore as tree
import time
import json
# Entre as dependências temos:
########## O arquivo com a classe arvore, que foi usado na criação da arvore e atualmente atua criando novas folhas
########## Lib time, módulo nativo da linguagem, foi usado no projeto para gerar pausas que facilitam a leitura e interação com o usuário
########## json é um tambem nativa da linguagem, usado no projeto para comunicar com o arquivo "dados.json"    

class Main():                   #Classe para a origem do game
    def __init__(self):
        # Abrir o arquivo de dados e guardar seu conteúdo em um objeto
        with open("dados.json") as file:
            self.dados = json.load(file)
        self.cursor = self.dados
        self.root_fixa = self.dados
        self.cursor_history = []    #historico de passos percorridos na árvore
        self.move_cursor()          #função que desloca o cursor percorrendo e armazenando o histórico


    def move_cursor(self, tipo=0):
        if tipo == 0:           #não move o cursor
            pass
        elif tipo ==1:          #caso resposta negativa
            self.cursor = self.cursor['left']
            self.cursor_history.append('0')
        elif tipo ==2:          #caso resposta positiva
            self.cursor = self.cursor['right']
            self.cursor_history.append('1')
        if self.cursor['tipo'] == 1:       #cursor tipo define se é pergunta ou resposta (ramo ou folha)
            self.chute(self.cursor['value'])
        else: 
            self.perguta(self.cursor['value'])          #cursor value é a string com a caracteristica ou animal

    def chute(self,animal):             #quando cursor chega a uma folha o progama interage com o usuário para verificar se a folha condiz com o que o usuário espera, caso contrário armazena um novo animal e sua diferença
        while True:
            resposta = input("O animal que você pensou é um "+animal+'? [s/n]  ')
            time.sleep(2)
            if resposta.lower() == 's':
                self.finaliza(1)
            elif resposta.lower() == 'n':
                bicho = input('Errei! Qual era seu animal?  ')
                time.sleep(2)
                diferenca = input('em que seu animal se diferencia?  ')
                time.sleep(2)
                posicao = self.cursor

                posicao.update({"left" : {"left" : {}, "right": {}, "value": bicho, "tipo" : 1}, "right": {"left" : {}, "right": {}, "value": animal, "tipo" : 1}, "value": diferenca, "tipo" : 0})
                self.finaliza(0)


    def perguta(self,caracteristica):            #quando cursor chega a uma ramificação o progama interage com o usuário para verificar atrávez se uma pergunta, qual caminho seguir
        while True:
            resposta = input("O animal que você pensou "+caracteristica+'? [s/n]  ')
            if resposta.lower() == 's':
                self.move_cursor(1)
            elif resposta.lower() == 'n':
                self.move_cursor(2)

    def finaliza(self, seletor):            #método para encerrar o programa, observe que o arquivo "dados.json" só recebe alteração após o encerramento correto do programa
        if seletor == 1:
            print('Obrigado! Eu sei que sou o melhor do mundo!')
            time.sleep(2)
            print('##################################')
            time.sleep(2)
        else:
            print('Espero que você não tenha mentido!')
        time.sleep(1)

        while True:
            novamente = input('Deseja jogar novamente? [s/n]  ')
            time.sleep(1)
            if novamente.lower() == 's':
                self.cursor =    self.root_fixa
                self.cursor_history.clear()
                self.move_cursor()
            elif novamente.lower() == 'n':
                with open("dados.json", 'w') as file:
                    time.sleep(1)
                    print('---------------SALVANDO DADOS-------------')
                    json.dump(self.dados, file, indent=4 )
                    time.sleep(1)
                    print('################ END GAME ##################')




print('---------------BEM VINDO AO AKINATOR-------------')
time.sleep(1)
print('Aqui consigo descobrir o animal que você estiver pensando')
time.sleep(2)
print('Bora lá!!!')
time.sleep(1)
print('Pense em um animal e não conte para ninguem')
time.sleep(3)
Main()


#falta: tratar erros no {s/n}; documentar; 