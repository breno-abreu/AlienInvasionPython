import sys
import pygame

from settings import Settings
from nave import Nave
import game_functions as gf

def rodar_jogo():
    """Inicializa o jogo e cria uma janela"""
    pygame.init()
    configuracoes = Settings()
    screen = pygame.display.set_mode(
        (configuracoes.screen_width, configuracoes.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #clock = pygame.time.Clock()
    
    #Cria uma nave
    nave = Nave(screen)
    
    """Inicia o loop principal do jogo"""
    while True:
        """Aguarda eventos de entrada do mouse e do teclado"""
        gf.check_events(nave)
                
        """Atualiza as imagens na tela"""
        gf.update_screen(configuracoes, screen, nave)
        
        """Mantem o FPS do jogo estável"""
        #gf.define_FPS(clock, 80)
        
if __name__ == '__main__':
    rodar_jogo()
