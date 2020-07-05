import sys
import pygame

from projetil import Projetil
from estrela import Estrela
from alien_amarelo import AlienAmarelo
from explosao import Explosao

def check_events(nave, screen, projeteis):
    """Responde a eventos do mouse e do teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave, projeteis, screen)
                
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, nave)
        
def update_screen(configuracoes, screen, nave, projeteis, estrelas, 
     aliens_amarelos, explosoes):
    """Atualiza as imagens na tela e faz o flip na tela"""
    #Preenche a tela com uma cor
    screen.fill(configuracoes.bg_color)
    
    #Testa a colisao entre projeteis e aliens amarelos
    for projetil in projeteis:
        for alien in aliens_amarelos:
            if testar_colisao(projetil, alien):
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.na_tela = False
                projetil.na_tela = False
                
    
    #Desenha as estrelas no background
    for estrela in estrelas:
        estrela.atualizar()
    
    #Desenha os projeteis de uma nave
    for projetil in projeteis:
        projetil.atualizar()
        
    #Atualiza os alienigenas amarelos
    for alien in aliens_amarelos:
        alien.atualizar()
        
    #Deleta um projetil
    for projetil in projeteis.copy():
        if projetil.na_tela == False:
            projeteis.remove(projetil)
    
    #Deleta um alien
    for alien in aliens_amarelos.copy():
        if alien.na_tela == False:
            aliens_amarelos.remove(alien)
            
    #Atualizar explosoes
    for explosao in explosoes:
        explosao.atualizar()
        
    #Deleta explosoes
    for explosao in explosoes.copy():
        if explosao.na_tela == False:
            explosoes.remove(explosao)
            
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
        
def testar_colisao(a, b):
    """Testa a colisao entre duas entidades"""
    if(a.rect.x < b.rect.x + b.image_width and 
        a.rect.x + a.image_width > b.rect.x and
        a.rect.y < b.rect.y + b.image_height and
        a.rect.y + a.image_height > b.rect.y):
        return True
    else:
        return False
        
def criar_explosao(screen, explosoes, coord_x, coord_y):
    nova_explosao = Explosao(screen, coord_x, coord_y)
    explosoes.append(nova_explosao)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
