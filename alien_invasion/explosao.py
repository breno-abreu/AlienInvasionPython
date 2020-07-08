import pygame

class Explosao:
    """Clase que irá implementar a animação de uma explosão"""
    def __init__(self, screen, coord_x, coord_y):
        self.screen = screen
        
        #Lista que conterá os três frames da animação
        self.images = []
        
        #Proporção da imagem será multiplicado com o valor original...
        #...criando uma imagem maior
        self.proporcao = 6
        
        #Contador que servirá de temporizador para indicar quando...
        #...a mudança de frames deve ocorrer
        self.cont_animacao = 0
        
        #Atributo que irá indicar qual frame deve ser desenhado
        self.cont_frames = 0
        
        #Indica se a animação da explosão está em andamento ou se...
        #...já foi encerrada
        self.na_tela = True
         
        #Carrega o primeiro frame da imagem
        self.image1 = pygame.image.load('images/explosao1.png')
            
        #Carrega o segundo frame da imagem
        self.image2 = pygame.image.load('images/explosao2.png')
        
        #Carrega o terceiro frame da imagem
        self.image3 = pygame.image.load('images/explosao3.png')
        
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
            
        self.image3 = pygame.transform.scale(
            self.image3, (self.image_width, self.image_height))
            
        #Transforma o preto nas imagens em transparente
        self.preto = (0, 0, 0)
        self.image1.set_colorkey(self.preto)
        self.image2.set_colorkey(self.preto)
        self.image3.set_colorkey(self.preto)
        
        #Cria o retangulo em que a imagem será aplicada
        self.rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Adiciona as imagens em uma lista
        self.images.append(self.image1)
        self.images.append(self.image2)
        self.images.append(self.image3)
        
        #Define as coordenadas iniciais
        self.rect.x = coord_x
        self.rect.y = coord_y
        
    def desenhar(self):
        """Desenha uma explosão"""
        self.cont_animacao += 1
        
        if self.cont_animacao == 8:
            #Com o auxílio do contador, muda-se o frame quando o... 
            #...mesmo atingir um valor
            self.cont_animacao = 0
            self.cont_frames += 1
            if self.cont_frames > 2:
                #Caso chegue ao último frame, muda a variável na_tela...
                #...para permitir sua exclusão
                self.cont_frames = 1
                self.na_tela = False
                
        self.screen.blit(self.images[self.cont_frames], self.rect)
                
    def atualizar(self):
        """Atualiza a explosão"""
        self.desenhar()
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
