import pygame
import random

class Estrela:
    """Classe de uma estrela no background"""
    
    def __init__(self, screen):
        """Cria uma estrela com tamanho, velocidade,
        e coordenadas aleatórias"""
        self.screen = screen
        
        #Define a velocidade da estrela
        self.velocidade = random.randint(8, 20)
        
        #Define o tamanho da estrela
        self.tamanho = random.randint(2, 5)
        
        #Define as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Cria o retangulo que representa uma estrela
        self.rect = pygame.Rect(0, 0, self.tamanho, self.tamanho)
        
        #Posiciona uma estrela com coordenadas aleatórias
        self.rect.x = random.randint(0, self.screen_dimensions[0])
        self.rect.y = random.randint(0, self.screen_dimensions[1])

        #Define a cor da estrela
        self.cor = (150, 170, 170)
        
    def desenhar(self):
        """Desenha uma estrela na tela"""
        pygame.draw.rect(self.screen, self.cor, self.rect)
        
    def atualizar(self):
        """Atualiza as coordenadas da estrela e a desenha"""
        self.rect.y += self.velocidade
        self.desenhar()
        
        if self.rect.y >= self.screen_dimensions[1]:
            self.rect.y = 0
        
        
