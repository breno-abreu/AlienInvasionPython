import sys
import pygame

import game_functions as gf

class Menu:
    """Classe que descreve os três menus encontrados no jogo:
    o menu principal, a tela de high scores e a tela para o jogador
    inserir seu nome e registrar sua pontuação"""
    
    def __init__(self, screen):
        self.screen = screen
        self.opcao_menu = -1
        self.amarelo = (255, 210, 0)
        self.verde = (40, 150, 40)
        self.branco = (200, 200, 200)
        self.azul = (0, 60, 130)
        
        self.opcao = 0
        
        self.screen_dimensions = pygame.display.get_surface().get_size()
        self.screen_rect = screen.get_rect()
        
        self.fonte42 = pygame.font.Font('CompassPro.ttf', 42)
        self.fonte100 = pygame.font.Font('CompassPro.ttf', 100)
        
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
            
        self.rect_titulo = self.titulo.get_rect()
        self.rect_novo_jogo = self.novo_jogo.get_rect()
        self.rect_high_scores = self.high_scores.get_rect()
        self.rect_sair = self.sair.get_rect()
        self.rect_iniciais_texto = self.iniciais_texto.get_rect()
        self.rect_pause = self.pause.get_rect()
        self.rect_menu_principal = self.menu_principal.get_rect()
        self.rect_continuar = self.continuar.get_rect()
        
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
        
    def atualizar(self):
        """Cria um menu de acordo com a opcao recebida
        -1: menu principal
        0: iniciar jogo
        1: high scores
        2: sair
        3: menu de pause
        4: menu para o jogador digitar suas iniciais"""
        
        
        if self.opcao_menu == -1:
            if self.opcao == 0:
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.amarelo)
                    
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.branco)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.branco)
                
            elif self.opcao == 1:
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.branco)
                
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.amarelo)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.branco)
            
            elif self.opcao == 2:
                self.novo_jogo = self.fonte42.render("Novo Jogo", True, 
                    self.branco)
                
                self.high_scores = self.fonte42.render("High Scores", 
                    True, self.branco)
        
                self.sair = self.fonte42.render("Sair", True, 
                    self.amarelo)
            
            self.screen.blit(self.novo_jogo, self.rect_novo_jogo)
            self.screen.blit(self.high_scores, self.rect_high_scores)
            self.screen.blit(self.sair, self.rect_sair)
            self.screen.blit(self.titulo, self.rect_titulo)
        
        elif self.opcao_menu == 1:
            print("")
            
        elif self.opcao_menu == 3:
            if self.opcao == 0:
                self.continuar = self.fonte42.render("Continuar", True, 
                    self.amarelo)
                    
                self.menu_principal = self.fonte42.render(
                    "Menu Principal", True, self.branco)
                
            elif self.opcao == -1:
                self.continuar = self.fonte42.render("Continuar", True, 
                    self.branco)
                    
                self.menu_principal = self.fonte42.render(
                    "Menu Principal", True, self.amarelo)
            
            self.screen.blit(self.pause, self.rect_pause)
            self.screen.blit(self.continuar, self.rect_continuar)
            self.screen.blit(self.menu_principal, 
                self.rect_menu_principal)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        

