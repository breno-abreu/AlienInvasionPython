import sys
import pygame
import random
import itertools

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
from nave import Nave

def check_events(nave, screen, projeteis, lista_auxiliar, menu):
    """Responde a eventos do mouse e do teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave, projeteis, screen, 
                lista_auxiliar, menu)
                
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, nave)
        
        
def update_screen(contador, configuracoes, screen, nave, projeteis, 
    aliens_amarelos, aliens_verdes, explosoes, 
    projeteis_verdes, aliens_vermelhos, projeteis_vermelhos, vidas,
    moedas, vidas_restantes, pontos, lista_auxiliar):
    """Atualiza as imagens na tela, faz o flip na tela, teste
    colisões entre entidades, cria entidades e remove entidades"""
    #Preenche a tela com uma cor
    #screen.fill(configuracoes.bg_color)

    #Criar alienígenas e itens quando o temporizador bater o tempo... 
    #...estipulado
    criar_entidades(screen, contador, aliens_amarelos, aliens_verdes,
        aliens_vermelhos, vidas, moedas, lista_auxiliar)
        
    #Atualiza as entidades e as desenha na tela
    atualizar_entidades(aliens_amarelos, aliens_verdes, 
        aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
        lista_auxiliar, screen, vidas, moedas, projeteis, 
        projeteis_verdes, projeteis_vermelhos)
        
    #Deleta entidades que não serão mais utilizadas
    deletar_entidades(aliens_amarelos, aliens_verdes, 
        aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
        lista_auxiliar, screen, vidas, moedas, projeteis, 
        projeteis_verdes, projeteis_vermelhos)
        
    #Testa a colisao entre entidades
    testar_colisao_listas(aliens_amarelos, aliens_verdes, 
        aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
        lista_auxiliar, screen, vidas, moedas, projeteis, 
        projeteis_verdes, projeteis_vermelhos)

    #Apaga a tela antiga e desenha a nova tela
    #pygame.display.flip()


def check_keydown_events(event, nave, projeteis, screen, 
    lista_auxiliar, menu):
    """Checa se alguma tecla está pressionada dentro do jogo"""
    if event.key == pygame.K_RIGHT:
        #Move a nava para a direita
        nave.movimentando_direita = True
    elif event.key == pygame.K_LEFT:
        #Move a nave para a esquerda
        nave.movimentando_esquerda = True
    elif event.key == pygame.K_SPACE:
        #Cria um projetil da nave
        criar_projetil(projeteis, screen, nave, lista_auxiliar)
    elif event.key == pygame.K_ESCAPE:
        #Retorna para o menu principal:
        menu.opcao_menu = 3
        menu.opcao = 0
       
def check_events_menu_principal(menu, aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
    lista_auxiliar, screen, vidas, moedas, projeteis, projeteis_verdes,
    projeteis_vermelhos):
    """Checa se alguma tecla foi pressionada no menu principal"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            #Muda a opção do menu
            if event.key == pygame.K_UP:
                if menu.opcao > 0:
                    menu.opcao -= 1
            elif event.key == pygame.K_DOWN:
                if menu.opcao < 2:
                    menu.opcao += 1
            elif event.key == pygame.K_RETURN:
                #Determina qual menu será o próximo a ser exibido,... 
                #...ou se o o jogo será iniciado
                menu.opcao_menu = menu.opcao
                if menu.opcao_menu == 0:
                    limpar_listas(aliens_amarelos, aliens_verdes, 
                        aliens_vermelhos, nave, pontos, explosoes, 
                        vidas_restantes, lista_auxiliar, screen, vidas, 
                        moedas, projeteis, projeteis_verdes,
                        projeteis_vermelhos)
                        
        
def check_events_menu_pause(menu):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            #Muda a opção do menu
            if event.key == pygame.K_UP:
                menu.opcao = 0
            elif event.key == pygame.K_DOWN:
                menu.opcao = -1
            elif event.key == pygame.K_RETURN:
                #Determina qual menu será o próximo a ser exibido,... 
                #...ou se o o jogo será iniciado
                menu.opcao_menu = menu.opcao
                menu.opcao = 0
                
def check_keyup_events(event, nave):
    """Checa se uma tecla parou de ser pressionada"""
    if event.key == pygame.K_RIGHT:
        nave.movimentando_direita = False
    elif event.key == pygame.K_LEFT:
        nave.movimentando_esquerda = False
        
        
def criar_projetil(projeteis, screen, nave, lista_auxiliar):
    """Cria um novo projétil lançado pelo jogador"""
    novo_projetil = Projetil(screen, nave)
    projeteis.append(novo_projetil)
    lista_auxiliar.append(novo_projetil)
    
    
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
    """Cria um novo alien amarelo"""
    novo_alien_amarelo = AlienAmarelo(screen, coord_x, coord_y)
    aliens_amarelos.append(novo_alien_amarelo)
    
    
def criar_alien_verde(screen, aliens_verdes, coord_x, coord_y):
    """Cria um novo alien verde"""
    novo_alien_verde = AlienVerde(screen, coord_x, coord_y)
    aliens_verdes.append(novo_alien_verde)
    

def criar_alien_vermelho(screen, aliens_vermelhos, coord_x, coord_y):
    """Cria um novo alien vermelho"""
    novo_alien_vermelho = AlienVermelho(screen, coord_x, coord_y)
    aliens_vermelhos.append(novo_alien_vermelho)
    
    
def criar_projetil_verde(screen, projeteis_verdes, coord_x, coord_y,
    lista_auxiliar):
    """Cria um novo projétil verde, criado por aliens verdes"""
    novo_projetil_verde = ProjetilVerde(screen, coord_x, coord_y)
    projeteis_verdes.append(novo_projetil_verde)
    lista_auxiliar.append(novo_projetil_verde)
    

def criar_projetil_vermelho(screen, projeteis_vermelhos, coord_x, 
    coord_y, fator_x, lista_auxiliar):
    """Cria um novo projétil vermelho, criado por aliens vemelhos"""
    novo_projetil_vermelho = ProjetilVermelho(screen, coord_x, 
        coord_y, fator_x)
    projeteis_vermelhos.append(novo_projetil_vermelho)
    lista_auxiliar.append(novo_projetil_vermelho)
    
    
def criar_vida(screen, vidas, coord_x, coord_y, lista_auxiliar):
    """Cria uma vida que pdoe ser coletada pelo jogador"""
    nova_vida = Vida(screen, coord_x, coord_y, False)
    vidas.append(nova_vida)
    lista_auxiliar.append(nova_vida)
    
    
def criar_vida_hud(screen, vidas_restantes):
    """Adiciona uma vida no HUD"""
    coord_x = 20 + len(vidas_restantes) * 60
    nova_vida = Vida(screen, coord_x, 10, True)
    vidas_restantes.append(nova_vida)
    
    
def criar_vidas_hud_inicial(screen, vidas_restantes):
    """Cria três vidas no HUD no início do jogo"""
    for i in range(3):
        criar_vida_hud(screen, vidas_restantes)
    
    
def criar_moeda(screen, moedas, coord_x, coord_y, lista_auxiliar):
    """Cria uma nova moeda"""
    nova_moeda = Moeda(screen, coord_x, coord_y)
    moedas.append(nova_moeda)
    lista_auxiliar.append(nova_moeda)
    

def remove_vida_hud(vidas_restantes):
    """Remove uma vida do HUD"""
    if len(vidas_restantes) > 0:
        del vidas_restantes[len(vidas_restantes) - 1]
    
    
def criar_entidades(screen, contador, aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, vidas, moedas, lista_auxiliar):
    """Cria alienígenas de todos os tipos"""
    #Armazena as dimensões da tela
    screen_dimensions = pygame.display.get_surface().get_size()
    
    #Incrementa os contadores
    contador[0] += 1
    contador[1] += 1
    contador[3] += 1
    
    #Caso o contador 3 atinja o tempo, criar uma vida ou uma moeda
    if contador[3] == 500:
        contador[3] = 0
        item = random.randint(0, 1)
        coord_x = random.randint(40, screen_dimensions[0] - 100)
        
        if item == 0:
            criar_vida(screen, vidas, coord_x, -40, lista_auxiliar)
        elif item == 1:
            criar_moeda(screen, moedas, coord_x, -40, lista_auxiliar)
    
    #Caso o contador 1 atinja o tempo, aumenta a velocidade em que...
    #...um alienígena será criado
    if contador[1] == 3000:
        contador[1] == 0
        if contador[2] >= 50:
            contador[2] -= 5
    
    #Caso o contador 0 atinja o tempo indicado pelo contador 2, ...
    #...um alienígena será criado aleatoriamente
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
            
def atualizar_estrelas(estrelas):
    """Desenha as estrelas no background"""
    for estrela in estrelas:
        estrela.atualizar()
        
def atualizar_entidades(aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
    lista_auxiliar, screen, vidas, moedas, projeteis, projeteis_verdes,
    projeteis_vermelhos):
    """Atualiza entidades e as desenha na tela"""
        
    #Atualiza as vidas, moedas, projeteis da nave, pojeteis verdes e...
    #...projeteis vermelhos
    for entidade in lista_auxiliar:
        entidade.atualizar()
        
    #Atualiza os alienigenas amarelos
    for alien in aliens_amarelos:
        alien.atualizar()
        
    #Atualiza os alienigenas verdes
    for alien in aliens_verdes:
        alien.atualizar()
        if alien.atirar == True:
            criar_projetil_verde(screen, projeteis_verdes, 
                alien.rect.x, alien.rect.y, lista_auxiliar)
            alien.atirar = False,
            
    #Atualiza os alienigenas vemelhos
    for alien in aliens_vermelhos:
        alien.atualizar()
        if alien.atirar == True:
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, 0, lista_auxiliar)
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, 2, lista_auxiliar)
            criar_projetil_vermelho(screen, projeteis_vermelhos, 
                alien.rect.x, alien.rect.y, -2, lista_auxiliar)
            alien.atirar = False
            
    #Atualiza a nave
    nave.atualizar()
            
    #Atualiza as explosoes
    for explosao in explosoes:
        explosao.atualizar()
    
    #Atualiza os pontos na tela
    pontos.atualizar(nave.pontos)
        
    #Atualiza as vidas do HUD
    for vida in vidas_restantes:
        vida.atualizar()
    
    
def deletar_entidades(aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
    lista_auxiliar, screen, vidas, moedas, projeteis, projeteis_verdes, 
    projeteis_vermelhos):
    """Deleta entidades que não estão mais sendo utilizadas"""
    #Deleta um projetil
    for projetil in projeteis.copy():
        if projetil.contato == True:
            projeteis.remove(projetil)
            lista_auxiliar.remove(projetil)
            
        elif projetil.na_tela == False:
            if nave.pontos > 0:
                nave.pontos -= 5
            projeteis.remove(projetil)
            lista_auxiliar.remove(projetil)
    
    #Deleta um alien amarelo
    for alien in aliens_amarelos.copy():
        if alien.na_tela == False:
            if nave.pontos > 0:
                nave.pontos -= 10
            aliens_amarelos.remove(alien)
            
        elif alien.destruido == True:
            aliens_amarelos.remove(alien)
            
    #Deleta um alien verde
    for alien in aliens_verdes.copy():
        if alien.na_tela == False:
            if nave.pontos > 0:
                nave.pontos -= 10
            aliens_verdes.remove(alien)
            
        elif alien.destruido == True:
            aliens_verdes.remove(alien)
            
    #Deleta um alien vermelho
    for alien in aliens_vermelhos.copy():
        if alien.na_tela == False:
            if nave.pontos > 0:
                nave.pontos -= 10
            aliens_vermelhos.remove(alien)
            
        elif alien.destruido == True:
            aliens_vermelhos.remove(alien)
    
    #Deleta um projetil verde
    for projetil in projeteis_verdes.copy():
        if projetil.na_tela == False:
            projeteis_verdes.remove(projetil)
            lista_auxiliar.remove(projetil)
            
    #Deleta um projetil vermelho
    for projetil in projeteis_vermelhos.copy():
        if projetil.na_tela == False:
            projeteis_vermelhos.remove(projetil)
            lista_auxiliar.remove(projetil)
            
    #Deleta uma vida
    for vida in vidas.copy():
        if vida.na_tela == False:
            vidas.remove(vida)
            lista_auxiliar.remove(vida)
            
    #Deleta uma moeda
    for moeda in moedas.copy():
        if moeda.na_tela == False:
            moedas.remove(moeda)
            lista_auxiliar.remove(moeda)
        
    #Deleta explosoes
    for explosao in explosoes.copy():
        if explosao.na_tela == False:
            explosoes.remove(explosao)
                
        
def testar_colisao_listas(aliens_amarelos, aliens_verdes, 
    aliens_vermelhos, nave, pontos, explosoes, vidas_restantes, 
    lista_auxiliar, screen, vidas, moedas, projeteis, projeteis_verdes, 
    projeteis_vermelhos):
    """Percorre as listas e detecta colisões entre as entidades"""
     #Testa a colisao entre projeteis e aliens amarelos
    for projetil in projeteis:
        for alien in aliens_amarelos:
            if testar_colisao(projetil, alien):
                nave.pontos += alien.pontos
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.destruido = True
                projetil.contato = True
            
    #Testa a colisao entre projeteis e aliens verdes
    for projetil in projeteis:
        for alien in aliens_verdes:
            if testar_colisao(projetil, alien):
                nave.pontos += alien.pontos
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.destruido = True
                projetil.contato = True
                
    #Testa a colisao entre projeteis e aliens vermelhos
    for projetil in projeteis:
        for alien in aliens_vermelhos:
            if testar_colisao(projetil, alien):
                nave.pontos += alien.pontos
                criar_explosao(
                    screen, explosoes, alien.rect.x, alien.rect.y)
                alien.destruido = True
                projetil.contato = True
                
    #Testa a colisao entre projeteis verdes e a nave
    for projetil in projeteis_verdes:
        if testar_colisao(projetil, nave) and nave.invencivel == False:
            projetil.na_tela = False
            criar_explosao(
                    screen, explosoes, nave.rect.x, nave.rect.y)
            remove_vida_hud(vidas_restantes)
            nave.invencivel = True
            
    #Testa a colisao entre projeteis vermelhos e a nave
    for projetil in projeteis_vermelhos:
        if testar_colisao(projetil, nave) and nave.invencivel == False:
            projetil.na_tela = False
            criar_explosao(
                    screen, explosoes, nave.rect.x, nave.rect.y)
            remove_vida_hud(vidas_restantes)
            nave.invencivel = True
            
    #Testa colisão entre a nave e alienígenas amarelos
    for alien in aliens_amarelos:
        if testar_colisao(alien, nave) and nave.invencivel == False:
            remove_vida_hud(vidas_restantes)
            nave.invencivel = True
            
    #Testa colisão entre a nave e alienígenas vermelhos
    for alien in aliens_vermelhos:
        if testar_colisao(alien, nave) and nave.invencivel == False:
            remove_vida_hud(vidas_restantes)
            nave.invencivel = True
            
    #Testa colisão entre a nave e alienígenas verdes
    for alien in aliens_verdes:
        if testar_colisao(alien, nave) and nave.invencivel == False:
            remove_vida_hud(vidas_restantes)
            nave.invencivel = True
    
    #Testa a colisao entre a nave e uma vida
    for vida in vidas:
        if testar_colisao(vida, nave):
            vida.na_tela = False
            nave.vidas += 1
            criar_vida_hud(screen, vidas_restantes)
            
    #Testa a colisao entre a nave e uma moeda
    for moeda in moedas:
        if testar_colisao(moeda, nave):
            moeda.na_tela = False
            nave.pontos += 500


def limpar_listas(aliens_amarelos, aliens_verdes, aliens_vermelhos, 
    nave, pontos, explosoes, vidas_restantes, lista_auxiliar, screen, 
    vidas, moedas, projeteis, projeteis_verdes, projeteis_vermelhos):
    
    nave.pontos = 0
    nave.vidas = 3
    nave.invencivel = False
    nave.rect.x = nave.aux_center

    aliens_amarelos.clear()
    aliens_verdes.clear()
    aliens_vermelhos.clear()
    pontos.def_string = '0'
    explosoes.clear()
    
    vidas_restantes.clear()
    criar_vidas_hud_inicial(screen, vidas_restantes)
    
    lista_auxiliar.clear()
    vidas.clear()
    moedas.clear()
    projeteis.clear()
    projeteis_verdes.clear()
    projeteis_vermelhos.clear()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
