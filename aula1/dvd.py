import pygame
import time
from random import randint

# Dimensões da tela
screen_width = 900
screen_height = 600

# Cores
branco = (255,255,255)
preto = (0,0,0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
ciano = (0, 255, 255)
magenta = (255, 0 , 255)

cores = [azul, vermelho, verde, amarelo, ciano, magenta, branco]

# Escolher cor
def escolher_cor(cores):
    n = len(cores) - 1
    cor = cores[randint(0, n)]
    return cor

font_size = 70

# Inicializa o Pygame e cria a janela
pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DVD")
font = pygame.font.SysFont('Tahoma', font_size, True, False)

quadrado = {
    'x':  150,
    'y': 150,
    'lado': 50,
    'speed_x': 6,
    'speed_y': 5
}

dvd = {
    'x': 100,
    'y': 100,
    'speed_x': 6,
    'speed_y': 5
}

cor = branco

# Loop principal
running = True
while running:


    # Cor de fundo (branco)
    window.fill(preto)
    
    #pygame.draw.rect(window, cor, pygame.Rect(quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))

    window.blit(font.render("DVD", True, cor), (dvd['x'], dvd['y']))

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    """
    if (quadrado['x'] <= 0 or quadrado['x'] + quadrado['lado'] >= screen_width):
        quadrado['speed_x'] = quadrado['speed_x'] * -1
        cor = escolher_cor(cores)

    if (quadrado['y'] <= 0 or quadrado['y'] + quadrado['lado'] >= screen_height):
        quadrado['speed_y'] = quadrado['speed_y'] * -1
        cor = escolher_cor(cores)

    """
    if (dvd['x'] <= 0 or dvd['x'] + 2*font_size >= screen_width):
        dvd['speed_x'] = dvd['speed_x'] * -1
        cor = escolher_cor(cores)

    if (dvd['y'] + font_size/2 <= 0 or dvd['y'] + font_size >= screen_height):
        dvd['speed_y'] = dvd['speed_y'] * -1
        cor = escolher_cor(cores)
    

    quadrado['x'] += quadrado['speed_x']
    quadrado['y'] += quadrado['speed_y']
    
    dvd['x'] += dvd['speed_x']
    dvd['y'] += dvd['speed_y']

    # Atualiza a tela
    pygame.display.update()
    
    # Controle de FPS
    time.sleep(0.05)

# Fecha o Pygame
pygame.quit()
