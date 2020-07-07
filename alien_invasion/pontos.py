import pygame

class Pontos:
    def __init__(self, screen):
        self.screen = screen
        self.amarelo = (255, 210, 0)
        self.pont_string = '0'
        
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        self.fonte = pygame.font.Font('CompassPro.ttf', 42)
        self.texto = self.fonte.render(self.pont_string, True, 
            self.amarelo)
        self.rect = self.texto.get_rect()
        self.rect.x = self.screen_dimensions[0] - 200
        self.rect.y = 10
        
    def desenhar(self):
        self.texto = self.fonte.render(self.pont_string, True, 
            self.amarelo)
        self.screen.blit(self.texto, self.rect)
        
    def atualizar(self, pontuacao):
        self.pont_string = str(pontuacao)
        self.desenhar()
