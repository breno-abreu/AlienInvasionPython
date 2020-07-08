import pygame

from entidade import Entidade

class Projetil(Entidade):
    """Classe que implementa um projétil lançado pela nave controlada
    pelo jogador"""
    
    def __init__(self, screen, nave, diretorio):
        Entidade.__init__(self, screen, diretorio, 0, 0)
        """Inicializa e redefine atrubutos"""
        self.velocidade = 20
        
        #Atributo que indica se houve contado com um inimigo
        self.contato = False
        
        #Inicializa as coordenadas do tiro
        self.rect.x = nave.rect.x
        self.rect.y = nave.rect.y
        
    def atualizar(self):
        """Movimenta um projetil"""
        self.rect.y -= self.velocidade
        self.desenhar()
        
        #Caso o projétil não esteja mais na tela, self.na_tela será
        #modificado para permitir sua exclusão em game_functions
        if self.rect.y <= -self.image_height:
            self.na_tela = False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
