import sys

import pygame

def check_events(nave):
    """Responde a eventos do mouse e do teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave)
                
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, nave)
        
def update_screen(configuracoes, screen, nave):
    """Atualiza as imagens na tela e faz o flip na tela"""
    #Preenche a tela com uma cor
    screen.fill(configuracoes.bg_color)
    
    #Desenha a nave
    nave.atualizar()
                
    #Apaga a tela antiga e desenha a nova tela
    pygame.display.flip()


def define_FPS(clock, fps):
    clock.tick(fps)

def check_keydown_events(event, nave):
    if event.key == pygame.K_RIGHT:
        #Move a nava para a direita
        nave.movimentando_direita = True
    elif event.key == pygame.K_LEFT:
        #Move a nave para a esquerda
        nave.movimentando_esquerda = True
                
def check_keyup_events(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movimentando_direita = False
    elif event.key == pygame.K_LEFT:
        nave.movimentando_esquerda = False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
