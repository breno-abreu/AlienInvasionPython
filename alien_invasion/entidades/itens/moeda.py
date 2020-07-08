import pygame

from entidades.entidade import Entidade

class Moeda(Entidade):
    """Classe que implementa uma moeda, item que derá ao jogador
    uma quantidade de pontos determinada"""
    def __init__(self, screen, coord_x, coord_y, diretorio):
        Entidade.__init__(self, screen, diretorio, coord_x, coord_y)
        """Redefine e inicializa atributos"""
        self.velocidade = 4
        
        #Atributo que define a quantidade de pontos recebido pelo...
        #...jogador ao entrar em contato com uma moeda
        self.pontos = 200
