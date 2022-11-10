####### A árvore usada para armazenar os dados é uma estrutura de chave:valor onde os valores podem ser strings ou conjuntos de chaves:valores
class Arvore():
    def __init__(self):
        self.root =  {  'left' : {},
                        'right' : {},
                        'value' : None,
                        'tipo' : None   }

#metodo para criação de novas folhas na árvore, usando o endereço por meio do histórico de passos

    def set_node_leaf(self, valor, history):
        posicao = self.root
        for a in range(len(history)):
            if history[a] == 0:
                posicao = posicao['left']
            elif history[a] == 1:
                posicao = posicao['right']
        posicao['value'] = valor
