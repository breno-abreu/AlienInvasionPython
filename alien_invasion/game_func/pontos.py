import pygame

class Pontos:
    """Classe que implementa o indicador de pontos que fica no canto
    superior direito da janela
    Poderia ser melhor implementado"""
    def __init__(self, screen):
        """Inicializa atributos, define a fonte e suas coordenadas"""
        self.screen = screen
        
        #Cria uma tripla ordenada que indica uma cor RGB, no caso,... 
        #...amarelo
        self.amarelo = (255, 210, 0)
        
        #Inicializa a string que será mastrada na tela
        self.pont_string = '0'
        
        #Define as dimensões da janela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega a fonte
        self.fonte = pygame.font.Font('CompassPro.ttf', 42)
        
        #Carrega o texto que será exibido na tela
        self.texto = self.fonte.render(self.pont_string, True, 
            self.amarelo)
            
        #Cria um retangulo onde o texto se encontra
        self.rect = self.texto.get_rect()
        
        #Define as coordenadas do texto
        self.rect.x = self.screen_dimensions[0] - 200
        self.rect.y = 10
        
    def desenhar(self):
        """Desenha o texto na tela"""
        self.texto = self.fonte.render(self.pont_string, True, 
            self.amarelo)
        self.screen.blit(self.texto, self.rect)
        
    def atualizar(self, pontuacao):
        """Recebe o valor de pontos do jogador, e salva seu valor"""
        self.pont_string = str(pontuacao)
        self.desenhar()
