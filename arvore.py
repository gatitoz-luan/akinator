
class Arvore():
    def __init__(self):
        self.root =  {  'left' : {},
                        'right' : {},
                        'value' : None,
                        'tipo' : None   }



    def set_node_leaf(self, valor, history):
        posicao = self.root
        for a in range(len(history)):
            if history[a] == 0:
                posicao = posicao['left']
            elif history[a] == 1:
                posicao = posicao['right']
        posicao['value'] = valor
