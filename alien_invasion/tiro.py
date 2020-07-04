import pygame

class Tiro:
    """Classe para um tiro da nave"""
    
    def __init__(self, screen, nave):
        """Inicializa as coordenadas do tiro"""
        slef.screen = screen
        self.proporcao = 8
        self.velocidade = 3
        self.na_tela = True
        
        #Guarda as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega o png do tiro
        self.image = pygame.image.load('images/tiro.png')
        
        #Define as dimensões de uma imagem dado uma proporção
        self.image_width = (
            self.image.get_width() * self.proporcao)
        self.image_height = (
            self.image.get_height() * self.proporcao)
            
        #Atualiza a resolução da imagem
        self.image = pygame.transform.scale(
            self.image, (self.image_width, self.image_height))
            
        #Transforma o preto de uma imagem em transparente
        self.preto = (0, 0, 0)
        self.image.set_colorkey(self.preto)
        
        #Cria um retângulo onde a imagem será aplicada
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Inicializa as coordenadas do tiro
        self.rect.x = nave.rect.x
        self.rect.y = nave.rect.y
        
    def desenhar(self):
        self.screen.blit(self.image, self.rect)
        
    def atualizar(self):
        self.rect.y -= self.velocidade
        self.desenhar()
        
        if(self.rect.y >= -self._height)
            self.na_tela = False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
