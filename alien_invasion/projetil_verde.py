import pygame

from entidade import Entidade

class ProjetilVerde(Entidade):
    """Classe que implementa um projétil verde, que é criado
    por um inimigo do tipo alienígena verde"""
    def __init__(self, screen, coord_x, coord_y, diretorio):
        Entidade.__init__(self, screen, diretorio, coord_x, coord_y)
        """Redefine e inicializa atributos"""
        self.velocidade = 8
            
            
            
            
            
            
            
            
            
            
            
            
            
            
