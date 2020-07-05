import sys
import pygame
import random

from projetil import Projetil
from estrela import Estrela
from alien_amarelo import AlienAmarelo
from explosao import Explosao
from alien_verde import AlienVerde
from alien_vermelho import AlienVermelho
from projetil_verde import ProjetilVerde
from projetil_vermelho import ProjetilVermelho
from vida import Vida
from moeda import Moeda

def check_events(nave, screen, projeteis):
    """Responde a eventos do mouse e do teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave, projeteis, screen)
                
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, nave)
        
        
def update_screen(contador, configuracoes, screen, nave, projeteis, 
    estrelas, aliens_amarelos, aliens_verdes, explosoes, 
    projeteis_verdes, aliens_vermelhos, projeteis_vermelhos, vidas,
    moedas):
    """Atualiza as imagens na tela e faz o flip na tela"""
    #Preenche a tela com uma cor
    screen.fill(configuracoes.bg_color)

    #Criar alienígenas
    criar_entidades(screen, contador, aliens_amarelos, aliens_verdes,
        aliens_vermelhos, vidas, moedas)
    
    #Testa a colisao entre projeteis e aliens amarelos
    for projetil in projeteis:
        for alien in aliens_amarelos:
            if testar_colisao(projetil, alien):
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.na_tela = False
                projetil.na_tela = False
                
    #Testa a colisao entre projeteis e aliens verdes
    for projetil in projeteis:
        for alien in aliens_verdes:
            if testar_colisao(projetil, alien):
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.na_tela = False
                projetil.na_tela = False
                
    #Testa a colisao entre projeteis e aliens vermelhos
    for projetil in projeteis:
        for alien in aliens_vermelhos:
            if testar_colisao(projetil, alien):
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.na_tela = False
                projetil.na_tela = False
                
    #Testa a colisao entre projteis verdes e a nave
    for projetil in projeteis_verdes:
        if testar_colisao(projetil, nave):
            projetil.na_tela = False
            
    #Testa a colisao entre peojteis vermelhos e a nave
    for projetil in projeteis_vermelhos:
        if testar_colisao(projetil, nave):
            projetil.na_tela = False
    
    #Desenha as estrelas no background
    for estrela in estrelas:
        estrela.atualizar()
        
    #Atualiza uma vida
    for vida in vidas:
        vida.atualizar()
        
    #Atualiza uma moeda
    for moeda in moedas:
        moeda.atualizar()
        
    #Testa a colisao entre a nave e uma vida
    for vida in vidas:
        if testar_colisao(vida, nave):
            vida.na_tela = False
            nave.vidas += 1
            
    #Testa a colisao entre a nave e uma moeda
    for moeda in moedas:
        if testar_colisao(moeda, nave):
            moeda.na_tela = False
            nave.pontos += 500
        
    #Desenha os projeteis de uma nave
    for projetil in projeteis:
        projetil.atualizar()
        
    #Atualiza os alienigenas amarelos
    for alien in aliens_amarelos:
        alien.atualizar()
        
    #Atualiza os alienigenas verdes
    for alien in aliens_verdes:
        alien.atualizar()
        if alien.atirar == True:
            criar_projetil_verde(screen, projeteis_verdes, 
                alien.rect.x, alien.rect.y)
            alien.atirar = False,
            
    #Atualiza os alienigenas vemelhos
    for alien in aliens_vermelhos:
        alien.atualizar()
        if alien.atirar == True:
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, 0)
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, 2)
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, -2)
            alien.atirar = False
    
    #Atualiza os projeteis verdes
    for projetil in projeteis_verdes:
        projetil.atualizar()
        
    #Atualiza os projeteis vermelhos
    for projetil in projeteis_vermelhos:
        projetil.atualizar()
        
    #Deleta um projetil
    for projetil in projeteis.copy():
        if projetil.na_tela == False:
            projeteis.remove(projetil)
    
    #Deleta um alien amarelo
    for alien in aliens_amarelos.copy():
        if alien.na_tela == False:
            aliens_amarelos.remove(alien)
            
    #Deleta um alien verde
    for alien in aliens_verdes.copy():
        if alien.na_tela == False:
            aliens_verdes.remove(alien)
            
    #Deleta um alien vermelho
    for alien in aliens_vermelhos.copy():
        if alien.na_tela == False:
            aliens_vermelhos.remove(alien)
    
    #Deleta um projetil verde
    for projetil in projeteis_verdes.copy():
        if projetil.na_tela == False:
            projeteis_verdes.remove(projetil)
            
    #Deleta um projetil vermelho
    for projetil in projeteis_vermelhos.copy():
        if projetil.na_tela == False:
            projeteis_vermelhos.remove(projetil)
            
    #Deleta uma vida
    for vida in vidas.copy():
        if vida.na_tela == False:
            vidas.remove(vida)
            
    #Deleta uma moeda
    for moeda in moedas.copy():
        if moeda.na_tela == False:
            moedas.remove(moeda)
            
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
        
    return False
        
        
def criar_explosao(screen, explosoes, coord_x, coord_y):
    """Cria uma explosão em determinadas coordenadas"""
    nova_explosao = Explosao(screen, coord_x, coord_y)
    explosoes.append(nova_explosao)
    

def criar_alien_amarelo(screen, aliens_amarelos, coord_x, coord_y):
    novo_alien_amarelo = AlienAmarelo(screen, coord_x, coord_y)
    aliens_amarelos.append(novo_alien_amarelo)
    
    
def criar_alien_verde(screen, aliens_verdes, coord_x, coord_y):
    novo_alien_verde = AlienVerde(screen, coord_x, coord_y)
    aliens_verdes.append(novo_alien_verde)
    

def criar_alien_vermelho(screen, aliens_vermelhos, coord_x, coord_y):
    novo_alien_vermelho = AlienVermelho(screen, coord_x, coord_y)
    aliens_vermelhos.append(novo_alien_vermelho)
    
    
def criar_projetil_verde(screen, projeteis_verdes, coord_x, coord_y):
    novo_projetil_verde = ProjetilVerde(screen, coord_x, coord_y)
    projeteis_verdes.append(novo_projetil_verde)
    

def criar_projetil_vermelho(screen, projeteis_vermelhos, coord_x, 
    coord_y, fator_x):
    novo_projetil_vermelho = ProjetilVermelho(screen, coord_x, 
        coord_y, fator_x)
    projeteis_vermelhos.append(novo_projetil_vermelho)
    
    
def criar_vida(screen, vidas, coord_x, coord_y):
    nova_vida = Vida(screen, coord_x, coord_y)
    vidas.append(nova_vida)
    
    
def criar_moeda(screen, moedas, coord_x, coord_y):
    nova_moeda = Moeda(screen, coord_x, coord_y)
    moedas.append(nova_moeda)
    
    
def criar_entidades(screen, contador, aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, vidas, moedas):
    """Cria alienígenas de todos os tipos"""
    #Define as dimensões da tela
    screen_dimensions = pygame.display.get_surface().get_size()
    contador[0] += 1
    contador[1] += 1
    contador[3] += 1
    
    if contador[3] == 500:
        contador[3] = 0
        item = random.randint(0, 1)
        coord_x = random.randint(40, screen_dimensions[0] - 100)
        
        if item == 0:
            criar_vida(screen, vidas, coord_x, -40)
        elif item == 1:
            criar_moeda(screen, moedas, coord_x, -40)
    
    if contador[1] == 3000:
        contador[1] == 0
        if contador[2] >= 50:
            contador[2] -= 5
    
    if contador[0] >= contador[2]:
        contador[0] = 0
        tipo_alien = random.randint(0, 2)
        coord_x = random.randint(40, screen_dimensions[0] - 100)
        
        if tipo_alien == 0:
            criar_alien_amarelo(screen, aliens_amarelos, coord_x, -40)
        
        elif tipo_alien == 1:
            criar_alien_verde(screen, aliens_verdes, coord_x, -40)
            
        elif tipo_alien == 2:
            criar_alien_vermelho(screen, aliens_vermelhos, coord_x, -40)
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
