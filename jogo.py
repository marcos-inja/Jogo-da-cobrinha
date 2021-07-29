import pygame
import sys

from cobrinha import Cobra
from comida import Comida

# Inicia o pygame
pygame.init()
TAM_TELA = (300,400)
tela = pygame.display.set_mode(TAM_TELA)

# Cronômetro
tempo = pygame.time.Clock()

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cobra.muda_direcao('DIREITA')   
            if event.key == pygame.K_UP:
                cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_LEFT:
                cobra.muda_direcao('ESQUERDA')
    
    cobra.move(posicao_comida)
    
    # Desenha a cobra na tela
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(67,145,0),
                                pygame.Rect(pos[0], pos[1], 10, 10))

    # Desenha a comida na tela
    pygame.draw.rect(tela, pygame.Color(150, 200, 100),
                            pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10))

    # Atualiza a tela a cada frame
    pygame.display.update() 

    # Define os frames do jogo
    tempo.tick(22)
