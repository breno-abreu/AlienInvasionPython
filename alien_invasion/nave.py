import pygame

class Nave:
    """Clase que implementa a nave que será controlada pelo jogador.
    Implementação péssima no que diz respeito ao carregamento e 
    animação das imagens"""
    
    def __init__(self, screen):
        """Inicializa a nave e sua posição inicial"""
        self.screen = screen
        
        #Define qual a proporção em que a imagem da nave é em relação...
        #...a imagem atual
        self.proporcao = 6
        
        #Indica a direção em que a nave está se movimentando
        #0: parada; 1: direita; -1: esquerda
        self.direcao = 0
        
        #Velocidade de movimento da nave
        self.velocidade = 10
        
        #Contadores auxiliares da animação do fogo
        self.cont_frames_fogo = 0
        self.cont_animacao_fogo = 0
        
        #Armazena a última direção da nave antes de ficar parada
        self.ultima_direcao = 0
        
        #Armazena um fataor de inércia para a nave; NÃO FOI UTIIZADA
        self.inercia = self.velocidade
        self.cont_inercia = 0
        
        #Quantidade de vidas restantes do jogador
        self.vidas = 3
        
        #Quantidade de pontos do jogador
        self.pontos = 0
        
        #Indica se o jogador levou dano para ficar invencível
        self.invencivel = False
        
        #contadores auxiliares para quando o jogador leva dano
        self.cont_invencibilidade = 0
        self.cont_aux_invencibilidade = 0
        
        #Indica se a imagem da nave está visível ou não
        self.visivel = True
        
        #Flags de movimentação
        self.movimentando_direita = False
        self.movimentando_esquerda = False
        
        #Define as dimensões da tela
        self.screen_dimensions = pygame.display.get_surface().get_size()
        
        #Carrega a imagem de uma nave que representa uma nave parada
        self.image_centro = pygame.image.load('images/nave_centro.png')
        
        #Define as variáveis que determinam a altura e o comprimento...
        #...de uma imagem que terá sua resolução modificada
        self.image_width = (
            self.image_centro.get_width() * self.proporcao)
        self.image_height = (
            self.image_centro.get_height() * self.proporcao)
        
        #Transforma a resolução de uma imagem
        self.image_centro = pygame.transform.scale(
            self.image_centro, (self.image_width, self.image_height))
            
        #Carrega a imagem de uma nave que representa uma nave...
        #...se movendo para a esquerda, e realiza os mesmos processos...
        #...da primeira imagem carregada
        self.image_esquerda = pygame.image.load(
            'images/nave_esquerda.png')
        self.image_esquerda = pygame.transform.scale(
            self.image_esquerda, (self.image_width, self.image_height))
            
        #Carrega a imagem de uma nave que representa uma nave...
        #...se movendo para a direita, e realiza os mesmos processos...
        #...da primeira imagem carregada
        self.image_direita = pygame.image.load(
            'images/nave_direita.png')
        self.image_direita  = pygame.transform.scale(
            self.image_direita , (self.image_width, self.image_height))
        
        #Cria uma lista onde os frames do fogo serão incluídas
        self.image_fogo = []
        
        #Carrega o primeiro frame da animação do fogo
        self.image_fogo1 = pygame.image.load(
            'images/fogo1.png')
        self.image_fogo1  = pygame.transform.scale(
            self.image_fogo1 , (self.image_width, self.image_height))
        self.image_fogo.append(self.image_fogo1)
            
        #Carrega o segundo frame da animação do fogo
        self.image_fogo2 = pygame.image.load(
            'images/fogo2.png')
        self.image_fogo2  = pygame.transform.scale(
            self.image_fogo2 , (self.image_width, self.image_height))
        self.image_fogo.append(self.image_fogo2)
            
        #Carrega o terceiro frame da animação do fogo
        self.image_fogo3 = pygame.image.load(
            'images/fogo3.png')
        self.image_fogo3  = pygame.transform.scale(
            self.image_fogo3 , (self.image_width, self.image_height))
        self.image_fogo.append(self.image_fogo3)
            
        #Transforma o preto nas imagens em transparente
        self.preto = (0, 0, 0)
        self.image_centro.set_colorkey(self.preto)
        self.image_esquerda.set_colorkey(self.preto)
        self.image_direita.set_colorkey(self.preto)
        self.image_fogo1.set_colorkey(self.preto)
        self.image_fogo2.set_colorkey(self.preto)
        self.image_fogo3.set_colorkey(self.preto)
        
        #Cria o retangulo em que a imagem será aplicada
        self.rect = self.image_centro.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect_fogo = self.image_fogo1.get_rect()
        
        #Posiciona uma nave na parte de baixo e ao centro da tela
        self.rect.centerx = self.screen_rect.centerx
        self.aux_center = self.screen_rect.centerx
        self.rect.y = (
            self.screen_dimensions[1] - 2 * self.image_height + 10)
            
        #Atualiza as coordenadas do fogo
        self.rect_fogo.x = self.rect.x
        self.rect_fogo.y = self.rect.y + self.image_height
        
    def desenhar_nave(self):
        """Desenha a nave"""
        #Desenha a nave de acordo com o valor do atributo 'direcao'
        if self.direcao == 0:
            #Caso a nave esteja imóvel
            self.screen.blit(self.image_centro, self.rect)
        
        elif self.direcao == 1:
            #Caso a nave esteja se movimentando para a direita
            self.screen.blit(self.image_direita, self.rect)
        
        elif self.direcao == -1:
            #Caso a nave esteja se movimentando para a esquerda
            self.screen.blit(self.image_esquerda, self.rect)
                
    def atualizar(self):
        """Atualiza os atributos da nave, e a desenha na tela"""
        
        if self.movimentando_direita:
            #Atualiza certas variáveis caso a nave esteja se...
            #...movimentando para a direita
            self.ultima_direcao = 1
            self.cont_inercia = 0
            self.inercia = self.velocidade
            self.movimentar_direita()
        
        elif self.movimentando_esquerda:
            #Atualiza certas variáveis caso a nave esteja se...
            #...movimentando para a esquerda
            self.ultima_direcao = -1
            self.cont_inercia = 0
            self.inercia = self.velocidade
            self.movimentar_esquerda()
            
        else:
            #Estabiliza a nave caso esteja parada
            self.estabilizar()
            
        if self.invencivel == True:
            #Caso a nave tenha recebido dano, fia invencível por...
            #...um determinado tempo
            self.cont_invencibilidade += 1
            if self.cont_invencibilidade == 150:
                self.invencivel = False
                self.cont_invencibilidade = 0
        
        if self.invencivel == False:
            #Caso a nave não tenha recebido dano, desenha normalmente
            self.desenhar_nave()
            self.desenhar_fogo()
        else:
            #Caso a nave tenha recebido dano, sua imagem ficará...
            #...piscando para indicar sua invencibilidade temporária
            self.cont_aux_invencibilidade += 1
            if (self.cont_aux_invencibilidade >= 3 and 
                self.visivel == True):
                self.desenhar_nave()
                self.desenhar_fogo()
                self.visivel = False
                self.cont_aux_invencibilidade = 0
                
            elif (self.cont_aux_invencibilidade >= 1 and
                self.visivel == False):
                self.visivel = True
                self.cont_aux_invencibilidade = 0
        
    def movimentar_direita(self):
        """Movimenta a nave para a direita"""
        if self.rect.x + self.image_width <= self.screen_dimensions[0]:
            self.rect.x += self.velocidade
        self.direcao = 1
        
    def movimentar_esquerda(self):
        """Movimenta a nava para a esquerda"""
        if self.rect.x >= 0:
            self.rect.x -= self.velocidade
        self.direcao = -1
        
    def estabilizar(self):
        """Muda a animação da nave para ficar estabilizada"""
        self.direcao = 0
        
        #Código abandonado que iria criar um efeito de inércia...
        #...na nave; deixa o jogo mais difícil pois a nave se torna...
        #...mais difícil de controlar
        """if self.ultima_direcao == 1:
            self.cont_inercia += 1
            if self.cont_inercia >= 5:
                self.inercia -= 1
                if self.inercia < 0:
                    self.inercia = 0
                    
            self.rect.x += self.inercia
            
        elif self.ultima_direcao == -1:
            self.cont_inercia += 1
            if self.cont_inercia >= 3:
                self.inercia -= 1
                if self.inercia < 0:
                    self.inercia = 0
                    
            self.rect.x -= self.inercia"""
        
    def desenhar_fogo(self):
        """Desenha o fogo dos propulsores abaixo da nave"""
        self.rect_fogo.x = self.rect.x
        self.rect_fogo.y = self.rect.y + self.image_height
        self.cont_frames_fogo += 1
        
        #Muda o frame de animação do fogo a cada 4 iterações
        if self.cont_frames_fogo == 4:
            self.cont_frames_fogo = 0
            self.cont_animacao_fogo += 1
            if(self.cont_animacao_fogo > 2):
                #Quanto chega no último frame, repete a animação
                self.cont_animacao_fogo = 0
            
        #Desenha o fogo na tela
        self.screen.blit(
            self.image_fogo[self.cont_animacao_fogo], 
            self.rect_fogo)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
