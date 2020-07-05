import sys
import pygame

from settings import Settings
from nave import Nave
import game_functions as gf
from alien_amarelo import AlienAmarelo

def rodar_jogo():
    """Inicializa o jogo e cria uma janela"""
    pygame.init()
    configuracoes = Settings()
    screen = pygame.display.set_mode(
        (configuracoes.screen_width, configuracoes.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    clock = pygame.time.Clock()
    
    #Cria as estrelas no background
    estrelas = []
    aliens_amarelos = []
    explosoes = []
    contador = [0]
    gf.criar_estrelas(screen, estrelas)
    
    #Cria uma nave
    nave = Nave(screen)
    
    #Cria uma lista de projeteis 
    projeteis = []
    
    """Inicia o loop principal do jogo"""
    while True:
        """Aguarda eventos de entrada do mouse e do teclado"""
        gf.check_events(nave, screen, projeteis)
        
        """Atualiza as imagens na tela"""
        gf.update_screen(
            contador, configuracoes, screen, nave, projeteis, estrelas,
            aliens_amarelos, explosoes)
        
        """Mantem o FPS do jogo estável"""
        clock.tick(100)
        
if __name__ == '__main__':
    rodar_jogo()
