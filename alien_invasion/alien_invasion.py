import sys
import pygame

from settings import Settings
from nave import Nave
from pontos import Pontos
import game_functions as gf
from menu import Menu


def rodar_jogo():
    """Inicializa as estruturas de dados das entidades do jogo,
    inicializa as funções do pygame e roda o loop principal do jogo"""
    
    #Inicializa todos os módulos importados do pygame
    pygame.init()
    
    configuracoes = Settings()
    
    #Cria uma janela usando como base as configurações determinadas... 
    #...em Settings
    screen = pygame.display.set_mode(
        (configuracoes.screen_width, configuracoes.screen_height))
        
    #Determina o nome da janela criada anteriormente
    pygame.display.set_caption("Alien Invasion")
    
    #Inicializa um relógio para determinar um limite de iterações por...
    #...segundos; será implementado no laço principal
    clock = pygame.time.Clock()
    
    #Cria uma lista de estrelas que irão compor no background
    estrelas = []
    
    #Cria uma lista de inimigos para cada tipo
    aliens_amarelos = []
    aliens_verdes = []
    aliens_vermelhos = []
    
    #Cria uma lista para cada tipo de projétil lançado pelos inimigos
    projeteis_verdes = []
    projeteis_vermelhos = []
    
    #Cria uma lsita auxiliar, que vai conter objetos de Vida, Moeda...
    #...Projetil, ProjetilVerde e ProjetilVermelho
    lista_auxiliar = []
    
    #Cria uma lista para cada iten que o jogador poderá coletar
    vidas = []
    moedas = []
    
    #Cria uma lista para os itens que serão mostrados no HUD,...
    #....e inicializa a lista com três vidas
    vidas_restantes = []
    gf.criar_vidas_hud_inicial(screen, vidas_restantes)
    
    #Cria ums lista para os efeitos de explosão
    explosoes = []
    
    #Cria um contador usado como temporizador para ativar certas...
    #..funcionalidades; 
    #index 0: contador para criação de um novo alien
    #index 1: contador para mudança de dificuldade
    #index 2: tempo para a criação de um novo alien
    #index 3: contador para a criação de um novo item
    contador = [0, 0, 130, 0]
    
    #Cria 50 estrelas que compõe o background
    gf.criar_estrelas(screen, estrelas)
    
    #Cria um objeto de Pontos que irá desenhar a quantidade de pontos...
    #... ganhos pelo jogador na tela
    pontos = Pontos(screen)
    
    #Cria uma nave, o objeto que será controlado pelo jogador
    nave = Nave(screen)
    
    #Cria uma lista de projeteis que serão lançados pela nave
    projeteis = []
    
    #Cria um menu de opções
    menu = Menu(screen)
    
    
    while True:
        """Inicia o loop principal do jogo"""
        screen.fill(configuracoes.bg_color)
        gf.atualizar_estrelas(estrelas)
            
        if menu.opcao_menu == -1:
            #Exibe o menu principal
            gf.check_events_menu_principal(menu, aliens_amarelos, 
                aliens_verdes, aliens_vermelhos, nave, pontos, 
                explosoes, vidas_restantes, lista_auxiliar, screen, 
                vidas, moedas, projeteis, projeteis_verdes, 
                projeteis_vermelhos)
            menu.atualizar()
            
        elif menu.opcao_menu == 0:
            #Inicia o jogo
            #Aguarda eventos de entrada do mouse e do teclado
            gf.check_events(nave, screen, projeteis, lista_auxiliar, 
                menu)
        
            #Atualiza entidades e as desenha na tela
            gf.update_screen(
                contador, configuracoes, screen, nave, projeteis, 
                aliens_amarelos, aliens_verdes, explosoes, 
                projeteis_verdes, aliens_vermelhos, projeteis_vermelhos,
                vidas, moedas, vidas_restantes, pontos, lista_auxiliar)
        
    
        elif menu.opcao == 1:
            gf.check_events_menu_highscore(menu)
            menu.atualizar()
            
        elif menu.opcao_menu == 3:
            gf.check_events_menu_pause(menu)
            menu.atualizar()
        
        elif menu.opcao_menu == 2:
            sys.exit()
            
        pygame.display.flip()
            
        #Mantem o FPS do jogo estável em 100 iterações por segundo
        clock.tick(100)
        
        
if __name__ == '__main__':
    rodar_jogo()
