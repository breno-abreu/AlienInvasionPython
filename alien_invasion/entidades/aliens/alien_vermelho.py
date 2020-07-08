import pygame

from entidades.aliens.alien import Alien

class AlienVermelho(Alien):
    """Classe que implementa um inimigo alienígena vermelho"""
    def __init__(self, screen, coord_x, coord_y, diretorio1, 
        diretorio2):
        Alien.__init__(self, screen, coord_x, coord_y, diretorio1, 
            diretorio2)
        """Inicializa atributos"""
        #Determina a velocidade de movimento
        self.velocidade = 1
        
        #Determina a quantidade de pontos que o jogador irá ganhar...
        #...quanto um alien é derrotado
        self.pontos = 50
        
    def atualizar(self):
        """Atualiza as coordenadas e desenha o alien"""
        self.rect.y += self.velocidade
        self.cont_projetil += 1
        
        #Alien atira um projetil quando o temporizador atinge um...
        #...tempo predeterminado
        if self.cont_projetil >= 120:
            self.cont_projetil = 0
            self.atirar = True
        
        #Caso o alien esteja fora da tela, será excluído
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
        
        self.desenhar()
        
        
        
        
        


