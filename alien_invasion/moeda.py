import pygame

class Moeda:
    """Cria um projetil verde"""
    def __init__(self, screen, coord_x, coord_y):
        self.screen = screen
        self.proporcao = 6
        self.velocidade = 4
        self.na_tela = True
        
        #Guarda as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega o png do tiro
        self.image = pygame.image.load('images/moeda.png')
        
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
        self.rect.x = coord_x
        self.rect.y = coord_y
        
    def desenhar(self):
        """Desenha um projetil na tela"""
        self.screen.blit(self.image, self.rect)
        
    def atualizar(self):
        """Movimenta um projetil"""
        self.rect.y += self.velocidade
        self.desenhar()
        
        #Caso o projétil não esteja mais na tela, self.na_tela será
        #modificado para permitir sua exclusão em game_functions
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False