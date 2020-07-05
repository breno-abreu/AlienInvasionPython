import pygame

class AlienAmarelo:
    """Classe para um inimigo alienígena amarelo"""
    def __init__(self, screen, coord_x, coord_y):
        """Inicializa a imagem, a velocidade e as coordenadas"""
        self.screen = screen
        self.proporcao = 6
        self.velocidade = 2
        self.images = []
        self.cont_animacao = 0
        self.cont_frames = 0
        self.na_tela = True
        
        #Define as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega o primeiro frame da imagem
        self.image1 = pygame.image.load('images/alien_amarelo1.png')
            
        #Carrega o segundo frame da imagem
        self.image2 = pygame.image.load('images/alien_amarelo2.png')
            
        #Define as variáveis que determinam a altura e o comprimento...
        #...de uma imagem que terá sua resolução modificada
        self.image_width = (
            self.image1.get_width() * self.proporcao)
        self.image_height = (
            self.image1.get_height() * self.proporcao)
            
        #Transforma a resolução das imagens
        self.image1 = pygame.transform.scale(
            self.image1, (self.image_width, self.image_height))
            
        self.image2 = pygame.transform.scale(
            self.image2, (self.image_width, self.image_height))
            
        #Transforma o preto nas imagens em transparente
        self.preto = (0, 0, 0)
        self.image1.set_colorkey(self.preto)
        self.image2.set_colorkey(self.preto)
        
        #Cria o retangulo em que a imagem será aplicada
        self.rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Adiciona as imagens em uma lista
        self.images.append(self.image1)
        self.images.append(self.image2)
        
        #Define as coordenadas iniciais
        self.rect.x = coord_x
        self.rect.y = coord_y
        
    def desenhar(self):
        """Desenha um alien na tela"""
        self.cont_animacao += 1
        
        if self.cont_animacao == 12:
            self.cont_animacao = 0
            self.cont_frames += 1
            if self.cont_frames > 1:
                self.cont_frames = 0
                
        self.screen.blit(self.images[self.cont_frames], self.rect)
        
    def atualizar(self):
        """Atualiza as coordenadas e desenha o alien"""
        self.rect.y += self.velocidade
        
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
        
        self.desenhar()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
