import pygame

from entidades.aliens.alien import Alien

class AlienAmarelo(Alien):
    """Classe que implementa um inimigo alienígena amarelo"""
    def __init__(self, screen, coord_x, coord_y, diretorio1, 
        diretorio2):
        Alien.__init__(self, screen, coord_x, coord_y, diretorio1, 
            diretorio2)
        """Inicializa atributos"""
        #Determina a velocidade de movimento
        self.velocidade = 3
        
        #Determina a quantidade de pontos que o jogador irá ganhar...
        #...quanto um alien é derrotado
        self.pontos = 30
        
    def atualizar(self):
        """Atualiza as coordenadas e desenha o alien"""
        self.rect.y += self.velocidade
        
        #Muda a direção no eixo x em que o alien se movimenta
        #Produz uma trajetória em zig-zag
        if self.direcao == 0:
            self.rect.x += self.velocidade / 2
        else:
            self.rect.x -= self.velocidade / 2
            
        self.cont_x += 1
        
        #Quando o alien anda a uma determinada distância no eixo x...
        #...suia direção é invertida
        if self.cont_x >= 80:
            self.cont_x = 0
            if self.direcao == 0:
                self.direcao = 1
            else:
                self.direcao = 0
        
        #Caso o alien esteja fora da tela, será excluído
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
        
        self.desenhar()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
