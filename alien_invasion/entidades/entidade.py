import pygame

class Entidade:
    """Classe que implementa uma entidade, serve de superclasse para
    algumas classes de objetos que são desenhados na tela"""
    def __init__(self, screen, diretorio, coord_x, coord_y):
        self.screen = screen
        
        #Atributo que define a velocidade de movimento de uma entidade
        self.velocidade = 0
        
        #Atributo que armazena a proporção de uma imagem.
        #Será multiplicada com as dimensões normais da imagem para...
        #...criar uma imagem maior
        self.proporcao = 6
        
        #Atributo que revela se uma entidade está presente na janela...
        #...principal, caso seja False, a entidade deve ser excluída
        self.na_tela = True
        
        #Atributo que armazena as dimensões da janela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Define uma tripla ordenada com os valores de RGB para...
        #...definir a cor preta
        self.preto = (0, 0, 0)
        
        #Carrega sua imagem
        self.image = pygame.image.load(diretorio)
        
        #Define as dimensões de uma imagem dado uma proporção
        self.image_width = (
            self.image.get_width() * self.proporcao)
        self.image_height = (
            self.image.get_height() * self.proporcao)
            
        #Atualiza a resolução da imagem
        self.image = pygame.transform.scale(
            self.image, (self.image_width, self.image_height))
            
        #Transforma o preto de uma imagem em transparente
        self.image.set_colorkey(self.preto)
        
        #Cria um retângulo onde a imagem será aplicada
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Inicializa as coordenadas da entidade
        self.rect.x = coord_x
        self.rect.y = coord_y
        
    def desenhar(self):
        """Desenha uma entidade na tela"""
        self.screen.blit(self.image, self.rect)
        
    def atualizar(self):
        """Atualiza as coordenadas de uma entidade"""
        self.rect.y += self.velocidade
        self.desenhar()
        
        #Caso a entidade não esteja mais na tela, self.na_tela será
        #modificado para permitir sua exclusão em game_functions
        if self.rect.y >= self.screen_dimensions[1]:
            self.na_tela = False
