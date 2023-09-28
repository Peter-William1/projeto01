import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
largura = 500
altura = 500

# Crie a tela
tela = pygame.display.set_mode((largura, altura))

# Carregue a imagem de fundo
imagem_fundo = pygame.image.load("img_bg.png")

# Redimensione a imagem de fundo para as dimensões da tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

# Defina a posição inicial da imagem de fundo
posicao_fundo = imagem_fundo.get_rect()

# Defina as cores do botão
cor_botao = (186, 186, 186)  # Verde
cor_botao_clique = (111, 111, 111)  # Verde escuro (quando clicado)

# Defina as dimensões e a posição do botão
largura_botao = 200
altura_botao = 25
posicao_botao = pygame.Rect((250 - largura_botao // 2, 600 // 2 - altura_botao // 2, largura_botao, altura_botao))

# Defina a fonte do texto do botão
fonte = pygame.font.Font(None, 36)
texto_botao = fonte.render("Login", True, (0, 0, 0))  # Texto preto

# Loop principal do jogo
botao_clicado = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if posicao_botao.collidepoint(evento.pos):
                botao_clicado = True
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            if botao_clicado and posicao_botao.collidepoint(evento.pos):
                print("Botão Clique-me clicado!")
            botao_clicado = False

    # Desenhe a imagem de fundo na tela
    tela.blit(imagem_fundo, posicao_fundo)

    # Desenhe o botão na tela
    pygame.draw.rect(tela, cor_botao if not botao_clicado else cor_botao_clique, posicao_botao,0 ,100)
   
    tela.blit(texto_botao, (500 // 2 - texto_botao.get_width() // 2, 600 // 2 - texto_botao.get_height() // 2))

    # Atualize a tela
    pygame.display.update()