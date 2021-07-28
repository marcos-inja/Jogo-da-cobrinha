import pygame
import sys
from cobrinha import Cobra

# Inicia o pygame
pygame.init()
TAM_TELA = (300,400)
tela = pygame.display.set_mode(TAM_TELA)
cobra = Cobra()

# Para ficar atualizando a tela
while True:

    # Escuta os eventos
    for event in pygame.event.get():
        # Se a tecla precionada for igual a sair, ele sai
        if event.type == pygame.QUIT:
            # Sai do jogo
            pygame.quit()
            # Fecha a janela
            sys.exit()  


