# -*- coding: utf-8 -*-
import arvore as tree
import time

class Main():
    def __init__(self):
        self.init = tree.Arvore()
        self.cursor = self.init.root
        self.root_fixa = self.cursor
        self.cursor_history = []
        if self.cursor['value'] == None:
            self.cursor['value'] = 'cachorro'
            self.cursor['tipo'] = 1
        self.move_cursor()


    def move_cursor(self, tipo=0):
        if tipo == 0:           #não move
            pass
        elif tipo ==1:          #resposta negativa
            self.cursor = self.cursor['left']
            self.cursor_history.append('0')
        elif tipo ==2:          #resposta positiva
            self.cursor = self.cursor['right']
            self.cursor_history.append('1')
        if self.cursor['tipo'] == 1:       #cursor tipo define se é pergunta ou resposta
            self.chute(self.cursor['value'])
        else: 
            self.perguta(self.cursor['value'])          #cursor value é a string com a caracteristica ou animal

    def chute(self,animal):
        resposta = input("O animal que você pensou é um "+animal+'? [s/n]  ')
        time.sleep(2)
        if resposta.lower() == 's':
            self.finaliza(1)
        else:
            bicho = input('Errei! Qual era seu animal?  ')
            time.sleep(2)
            diferenca = input('em que seu animal se diferencia?  ')
            time.sleep(2)
            posicao = self.cursor

            posicao.update({'left' : {'left' : {}, 'right': {}, 'value': bicho, 'tipo' : 1}, 'right': {'left' : {}, 'right': {}, 'value': animal, 'tipo' : 1}, 'value': diferenca, 'tipo' : 0})
            self.finaliza(0)


    def perguta(self,caracteristica):
        resposta = input("O animal que você pensou "+caracteristica+'? [s/n]')
        if resposta.lower() == 's':
            self.move_cursor(1)
        else:
            self.move_cursor(2)

    def finaliza(self, seletor):
        if seletor == 1:
            print('Obrigado! Eu sei que sou o melhor do mundo!')
            time.sleep(2)
            print('##################################')
            time.sleep(2)
        else:
            print('Espero que você não tenha mentido!')
        time.sleep(1)
        print('jogue novamente')

        self.cursor =    self.root_fixa
        self.cursor_history.clear()
        self.move_cursor()


print('---------------BEM VINDO AO AKINATOR-------------')
time.sleep(1)
print('Aqui consigo advinhar o animal quevocê estiver pensando')
time.sleep(2)
print('Bora lá!!!')
time.sleep(1)
print('Pense em um animal e não conte para ninguem')
time.sleep(3)
Main()