import pygame

from entidades.entidade import Entidade

class Vida(Entidade):
    """Classe que implementa uma vida, item que dará ao jogador
    uma vida adicional caso entrem em contato"""
    def __init__(self, screen, coord_x, coord_y, hud, diretorio):
        Entidade.__init__(self, screen, diretorio, coord_x, coord_y)
        """Redefine e inicializa atributos"""
        self.velocidade = 4
        
        #Define se a vida fará parte do HUD ou não
        self.hud = hud
        
    def atualizar(self):
        """Atualiza as coordenadas de uma vida"""
        if self.hud == False:
            self.rect.y += self.velocidade
            
        self.desenhar()
        
        #Caso o projétil não esteja mais na tela, self.na_tela será
        #modificado para permitir sua exclusão em game_functions
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
