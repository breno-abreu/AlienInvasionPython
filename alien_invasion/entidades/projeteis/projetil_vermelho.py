import pygame

from entidades.entidade import Entidade

class ProjetilVermelho(Entidade):
    """Classe que implementa um projétil vermelho, que é criado
    por um inimigo do tipo alienígena vermelho"""
    def __init__(self, screen, coord_x, coord_y, fator_x, diretorio):
        Entidade.__init__(self, screen, diretorio, coord_x, coord_y)
        """Redefine e inicializa atributos"""
        self.velocidade = 6
        
        #Atributo que irá determinar a velocidade de movimento...
        #...do projétil no eixo x. Apenas necessário para projéteis...
        #...desse tipo
        self.fator_x = fator_x

    def atualizar(self):
        """Atualiza as coordenadas de um projétil"""
        self.rect.y += self.velocidade
        self.rect.x += self.fator_x
        self.desenhar()
        
        #Caso o projétil não esteja mais na tela, self.na_tela será...
        #...modificado para permitir sua exclusão em game_functions
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
