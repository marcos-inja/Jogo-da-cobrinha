import pygame
import sys

from cobrinha import Cobra
from comida import Comida

# Inicia o pygame
pygame.init()
TAM_TELA = (300,400)
tela = pygame.display.set_mode(TAM_TELA)

cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao

# Para ficar atualizando a tela
while True:

    # Muda a cor da tela, usando o rgb
    tela.fill((25, 0, 34))

    for event in pygame.event.get():
        # escuta - mouse ou teclado, for igual a sair
        if event.type == pygame.QUIT:
            # Interrompe o jogo
            pygame.quit()
            print('falou')
            # Fecha a janela
            sys.exit()  
    
    # Desenha a cobra na tela
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(67,145,0),
                                pygame.Rect(pos[0], pos[1], 10, 10))

    # Desenha a comida na tela
    pygame.draw.rect(tela, pygame.Color(150, 200, 100),
                            pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10))

    # Atualiza a tela a cada frame
    pygame.display.update() 

