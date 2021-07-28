import random

class Comida:
    def __init__(self, tam_tela = (300,400)):
        self.tam_tela = tam_tela
        self.posicao = [random.randrange(10, self.tam_tela[0], 10), 
                        random.randrange(10, self.tam_tela[1], 10)]
        self.devorada = False        