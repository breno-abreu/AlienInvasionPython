import sys
import pygame

import game_func.game_functions as gf

class Menu:
    """Classe que descreve os três menus encontrados no jogo:
    o menu principal, a tela de high scores e a tela para o jogador
    inserir seu nome e registrar sua pontuação"""
    
    def __init__(self, screen):
        self.screen = screen
        
        #Atributo que indica qual o menu que deve ser executado
        self.opcao_menu = -1
        
        #Definir cores que serão usadas nos textos
        self.amarelo = (255, 210, 0)
        self.verde = (40, 150, 40)
        self.branco = (200, 200, 200)
        self.azul = (0, 60, 130)
        self.vermelho = (200, 0, 0)
        
        self.opcao = 0
        self.texto_arquivo = ''
        self.linhas_texto = []
        
        #Define as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        self.screen_rect = screen.get_rect()
        
        #Carrega as fontes dos textos
        self.fonte42 = pygame.font.Font('CompassPro.ttf', 42)
        self.fonte100 = pygame.font.Font('CompassPro.ttf', 100)
        
        #Carrega os textos com suas fontes e cores
        self.titulo = self.fonte100.render("Alien Invasion", 
                True, self.verde)
        self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
            self.amarelo)
        self.high_scores = self.fonte42.render("High Scores", 
                    True, self.branco)
        self.sair = self.fonte42.render("Sair", True, 
            self.amarelo)
        self.iniciais_texto = self.fonte42.render(
            "Digite suas iniciais: ", True, self.amarelo)
        self.pause = self.fonte100.render("Pause", 
            True, self.azul)
        self.continuar = self.fonte42.render("Continuar", True, 
            self.amarelo)
        self.menu_principal = self.fonte42.render("Menu Principal", 
            True, self.branco)
        self.texto_highscore = self.fonte42.render(self.texto_arquivo, 
                    True, self.branco)
        self.morreu = self.fonte100.render("YOU DIED", 
            True, self.vermelho)
            
        #Cria os retângulos onde os textos serão desenhados
        self.rect_titulo = self.titulo.get_rect()
        self.rect_novo_jogo = self.novo_jogo.get_rect()
        self.rect_high_scores = self.high_scores.get_rect()
        self.rect_sair = self.sair.get_rect()
        self.rect_iniciais_texto = self.iniciais_texto.get_rect()
        self.rect_pause = self.pause.get_rect()
        self.rect_menu_principal = self.menu_principal.get_rect()
        self.rect_continuar = self.continuar.get_rect()
        self.rect_texto_highscore = self.texto_highscore.get_rect()
        self.rect_morreu = self.morreu.get_rect()
        
        #Define as coordenadas de cada texto
        self.rect_titulo.centerx = self.screen_rect.centerx
        self.rect_titulo.y = 200
        
        self.rect_novo_jogo.centerx = self.screen_rect.centerx
        self.rect_novo_jogo.y = 400
        
        self.rect_high_scores.centerx = self.screen_rect.centerx
        self.rect_high_scores.y = 450
        
        self.rect_sair.centerx = self.screen_rect.centerx
        self.rect_sair.y = 500
        
        self.rect_pause.centerx = self.screen_rect.centerx
        self.rect_pause.y = 200
        
        self.rect_continuar.centerx = self.screen_rect.centerx
        self.rect_continuar.y = 400
        
        self.rect_menu_principal.centerx = self.screen_rect.centerx
        self.rect_menu_principal.y = 450
        
        self.rect_texto_highscore.centerx = self.screen_rect.centerx
        self.rect_texto_highscore.y = 200
        
        self.rect_morreu.centerx = self.screen_rect.centerx
        self.rect_morreu.y = 200
        
    def atualizar(self):
        """Cria um menu de acordo com a opcao recebida
        -1: menu principal
        0: iniciar jogo
        1: high scores
        2: sair
        3: menu de pause
        4: menu para o jogador digitar suas iniciais
        5: tela de morte"""
        
        if self.opcao_menu == -1:
            #Exibe o menu principal
            if self.opcao == 0:
                #Realça o texto "Novo Jogo"
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.amarelo)
                    
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.branco)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.branco)
                
            elif self.opcao == 1:
                #Realça o texto "High Scores"
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.branco)
                
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.amarelo)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.branco)
            
            elif self.opcao == 2:
                #Realça o texto "Sair"
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.branco)
                
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.branco)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.amarelo)
            
            #Desenha os textos na tela
            self.screen.blit(self.novo_jogo, self.rect_novo_jogo)
            self.screen.blit(self.high_scores, self.rect_high_scores)
            self.screen.blit(self.sair, self.rect_sair)
            self.screen.blit(self.titulo, self.rect_titulo)
        
        elif self.opcao_menu == 1:
            #Exibe os cinco primeiros maiores pontos
            for i in range(len(self.linhas_texto)):
                self.texto_highscore = self.fonte42.render(
                    self.linhas_texto[i], True, self.branco)
                    
                self.rect_texto_highscore.y += 50
                
                self.screen.blit(self.texto_highscore, 
                    self.rect_texto_highscore)
            
            self.rect_texto_highscore.y = 200
            
        elif self.opcao_menu == 3:
            #Exibe a tela de pause
            if self.opcao == 0:
                #Realça o texto "Continuar"
                self.continuar = self.fonte42.render("Continuar", True, 
                    self.amarelo)
                    
                self.menu_principal = self.fonte42.render(
                    "Menu Principal", True, self.branco)
                
            elif self.opcao == -1:
                #Realça o texto "Menu Principal"
                self.continuar = self.fonte42.render("Continuar", True, 
                    self.branco)
                    
                self.menu_principal = self.fonte42.render(
                    "Menu Principal", True, self.amarelo)
            
            #Desenha os textos na tels
            self.screen.blit(self.pause, self.rect_pause)
            self.screen.blit(self.continuar, self.rect_continuar)
            self.screen.blit(self.menu_principal, 
                self.rect_menu_principal)
                
        elif self.opcao_menu == 5:
            #Exibe o texto na tela quando o jogador morre
            self.screen.blit(self.morreu, self.rect_morreu)
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        

