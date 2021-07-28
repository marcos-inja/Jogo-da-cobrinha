class Cobra:
    def __init__(self, tam_tela = (300, 400), 
                        posicao = [100,50], # esquerda, cima
                        corpo = [[90, 50],[80, 50],[70,50]],
                        direcao = 'DIREITA'):
        self.tam_tela = tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao


    def muda_direcao(self, nova_direcao):
        pass


    def move(self, posicao_comida):
        pass


    def colisao(self):
        pass