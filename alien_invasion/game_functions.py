import sys
import pygame

from projetil import Projetil
from estrela import Estrela

def check_events(nave, screen, projeteis):
    """Responde a eventos do mouse e do teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave, projeteis, screen)
                
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, nave)
        
def update_screen(configuracoes, screen, nave, projeteis, estrelas):
    """Atualiza as imagens na tela e faz o flip na tela"""
    #Preenche a tela com uma cor
    screen.fill(configuracoes.bg_color)
    
    #Desenha as estrelas no background
    for estrela in estrelas:
        estrela.atualizar()
    
    #Desenha os projeteis de uma nave
    for projetil in projeteis:
        projetil.atualizar()
        
    #Deleta projeteis que estão fora da tela
    for projetil in projeteis.copy():
        if projetil.na_tela == False:
            projeteis.remove(projetil)
    
    #Desenha a nave
    nave.atualizar()
                
    #Apaga a tela antiga e desenha a nova tela
    pygame.display.flip()


def define_FPS(clock, fps):
    clock.tick(fps)

def check_keydown_events(event, nave, projeteis, screen):
    """Checa se alguma tecla está pressionada"""
    if event.key == pygame.K_RIGHT:
        #Move a nava para a direita
        nave.movimentando_direita = True
    elif event.key == pygame.K_LEFT:
        #Move a nave para a esquerda
        nave.movimentando_esquerda = True
    elif event.key == pygame.K_SPACE:
        #Cria um tiro de nave
        criar_tiro(projeteis, screen, nave)
                
def check_keyup_events(event, nave):
    """Checa se uma telca parou de ser pressionada"""
    if event.key == pygame.K_RIGHT:
        nave.movimentando_direita = False
    elif event.key == pygame.K_LEFT:
        nave.movimentando_esquerda = False
        
def criar_tiro(projeteis, screen, nave):
    """Cria um novo projétil e o coloca na lista de projeteis"""
    novo_projetil = Projetil(screen, nave)
    projeteis.append(novo_projetil)
    
def criar_estrelas(screen, estrelas):
    """Cria n novas estrelas"""
    n = 50
    for i in range(n):
        nova_estrela = Estrela(screen)
        estrelas.append(nova_estrela)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
