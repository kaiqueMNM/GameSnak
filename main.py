#configurações iniciais 
import pygame 
import random

pygame.init()
pygame.display.set_caption("jogo snake python")
largura , altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
verde = (0, 255, 0)

# parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

# função para rodar o jogo
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0 
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = [] 

    comida_x, comida_y = gerar_comida()

    # Variáveis de registro de pontuação máxima
    pontuacao = 0
    recorde = 0

    # Fonte para exibir a pontuação
    fonte = pygame.font.Font(None, 36)

    while not fim_jogo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

            # Tratar eventos de teclado para mover a cobra
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x != tamanho_quadrado:
                    velocidade_x = -tamanho_quadrado
                    velocidade_y = 0
                if evento.key == pygame.K_RIGHT and velocidade_x != -tamanho_quadrado:
                    velocidade_x = tamanho_quadrado
                    velocidade_y = 0
                if evento.key == pygame.K_UP and velocidade_y != tamanho_quadrado:
                    velocidade_x = 0
                    velocidade_y = -tamanho_quadrado
                if evento.key == pygame.K_DOWN and velocidade_y != -tamanho_quadrado:
                    velocidade_x = 0
                    velocidade_y = tamanho_quadrado
            
        # Atualizar a posição da cobra
        x += velocidade_x
        y += velocidade_y

        tela.fill(preta)

        # Desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Verificar colisão da cobra com a comida
        if (x, y) == (comida_x, comida_y):
            tamanho_cobra += 1
            pontuacao += 10  # Aumente a pontuação
            comida_x, comida_y = gerar_comida()

        # Verificar se a cobra bateu na parede
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # Verificar se a cobra bateu em si mesma
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # Desenhar a cobra
        desenhar_cobra(tamanho_quadrado, pixels)

        # Atualizar a pontuação em tempo real
        texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, branca)
        tela.blit(texto_pontuacao, (10, 10))

        # Atualizações da tela
        pygame.display.update()
        relogio.tick(velocidade_jogo)

    # Atualizar o recorde se necessário
    if pontuacao > recorde:
        recorde = pontuacao
        # Salvar o recorde em um arquivo (você precisa implementar a função de salvar)

    # Imprimir a pontuação e o recorde
    print("Pontuação: ", pontuacao)
    print("Recorde: ", recorde)

# Chamar a função principal do jogo
rodar_jogo()
