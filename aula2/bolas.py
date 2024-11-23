import pygame
import time
import math
from random import randint

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

balls = []

# Escolher cor
def escolher_cor(cores):
    n = len(cores) - 1
    cor = cores[randint(0, n)]
    return cor

branco = (255,255,255)
preto = (0,0,0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
ciano = (0, 255, 255)
magenta = (255, 0 , 255)

cores = [azul, vermelho, verde, amarelo, ciano, magenta]

cor = preto


while(running):
    pygame.draw.rect(window, (255,255,255), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Leia o evento
            x, y = event.pos
            print(f"Mouse clicked at ({x}, {y})")
            cor = escolher_cor(cores)
            balls.append({
                    "cor": cor,
                    "x": x,
                    "y": y
                }
            )
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                cor = azul
            elif event.key == pygame.K_w:
                cor = verde
            elif event.key == pygame.K_s:
                cor = amarelo
            elif event.key == pygame.K_d:
                cor = vermelho
    
    for ball in balls:
        ball["x"] += randint(-3, 3)
        ball["y"] += randint(-3, 3)
        pygame.draw.circle(window,ball["cor"],(ball["x"],ball["y"]),50)
    
    pygame.display.update()
    time.sleep(0.05)
    
pygame.quit()