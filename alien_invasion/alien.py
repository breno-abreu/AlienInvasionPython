import pygame

class Alien:
    """Superclasse para os três tipos de inimgos"""
    def __init__(self, screen, coord_x, coord_y, diretorio1, 
        diretorio2):
        """Inicializa atributos e carrega sua imagem"""
        self.screen = screen
        
        #Indica a proporção para aumentar o tamanho da imagem
        self.proporcao = 6
        
        #Cria uma lista que irá conter todos os frames de uma animação
        self.images = []
        
        #Variáveis auxiliares da animação
        self.cont_animacao = 0
        self.cont_frames = 0
        
        #Indica se um alien está na tela
        self.na_tela = True
        
        #Indica se um alien foir destruído
        self.destruido = False
        
        #Variáveis auxiliares do eixo x
        self.x_aux = coord_x
        self.cont_x = 0
        
        #Indica a direção de movimento de um alien
        self.direcao = 0
        
        #Indica se um alien está pronto para atirar
        self.atirar = False
        
        #Temporizador que indica se um alien está pronto para atirar
        self.cont_projetil = 0
        
        #Define as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega o primeiro frame da imagem
        self.image1 = pygame.image.load(diretorio1)
            
        #Carrega o segundo frame da imagem
        self.image2 = pygame.image.load(diretorio2)
            
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
        
        #Permite a mudança de frames
        if self.cont_animacao == 12:
            self.cont_animacao = 0
            self.cont_frames += 1
            if self.cont_frames > 1:
                self.cont_frames = 0
                
        self.screen.blit(self.images[self.cont_frames], self.rect)
