import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura_janela = 800
altura_janela = 600

# Defina as cores
cor_fundo = (255, 255, 255)
cor_caixa = (200, 200, 200)
cor_caixa_ativa = (150, 150, 150)
cor_texto = (0, 0, 0)

# Crie a janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Caixa de Texto Pygame")

# Crie uma fonte
fonte = pygame.font.Font(None, 36)

# Variáveis para controlar a caixa de entrada de texto
texto = ""
caixa_ativa = False

# Variáveis para controlar a repetição da tecla Backspace
backspace_pressionado = False
tempo_ultimo_backspace = 0
intervalo_backspace = 250  # Intervalo em milissegundos

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if caixa_retangulo.collidepoint(event.pos):
                caixa_ativa = not caixa_ativa  # Inverte o estado de ativação da caixa
            else:
                caixa_ativa = False
        elif event.type == pygame.KEYDOWN:
            if caixa_ativa:
                if event.key == pygame.K_RETURN:
                    # Processar o texto inserido
                    print("Texto inserido:", texto)
                    texto = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Habilita a repetição do Backspace e registra o tempo do último Backspace
                    backspace_pressionado = True
                    tempo_ultimo_backspace = pygame.time.get_ticks()
                else:
                    # Adicionar caracteres digitados
                    texto += event.unicode
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                # Desabilita a repetição do Backspace quando a tecla é liberada
                backspace_pressionado = False

    # Se a tecla Backspace estiver pressionada, remova caracteres gradualmente em intervalos
    if backspace_pressionado and (pygame.time.get_ticks() - tempo_ultimo_backspace) >= intervalo_backspace:
        if texto:
            texto = texto[:-1]
        tempo_ultimo_backspace = pygame.time.get_ticks()

    # Preencher a tela com a cor de fundo
    janela.fill(cor_fundo)

    # Determinar a cor da caixa de acordo com seu estado
    cor_caixa_atual = cor_caixa_ativa if caixa_ativa else cor_caixa

    # Desenhar a caixa de entrada de texto
    caixa_retangulo = pygame.Rect(200, 275, 400, 50)
    pygame.draw.rect(janela, cor_caixa_atual, caixa_retangulo)

    # Desenhar o texto inserido
    texto_surface = fonte.render(texto, True, cor_texto)
    janela.blit(texto_surface, (caixa_retangulo.x + 10, caixa_retangulo.y + 10))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
