import pygame
import time
import math

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

quadrado = {
    "x": 100,
    "y": 100,
    "size": 100,
    "speed_x": 1,
    "speed_y": 1
}

esquerda = False
direita = False
cima = False
baixo = False

gravity = 0.5
can_jump = False

while(running):
    pygame.draw.rect(window, (255,255,255), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            esquerda = True
        elif event.key == pygame.K_RIGHT:
            direita = True
        if event.key == pygame.K_UP:
            if can_jump:
                quadrado["y"] -= 100
        #if event.key == pygame.K_DOWN:
        #    baixo = True
        #if event.key == pygame.K_SPACE:
        #    print("ESPAÇO")
        #    quadrado["y"] -= 50
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            esquerda = False
        elif event.key == pygame.K_RIGHT:
            direita = False
            print("indo pro lado direito")
        if event.key == pygame.K_UP:
            #cima = False
            #quadrado["y"] -= 50
            pass
        #if event.key == pygame.K_DOWN:
        #    baixo = False
        #if event.key == pygame.K_SPACE:
        #    print("ESPAÇO")
        #    quadrado["y"] -= 50
        
    if direita:
        quadrado["x"] += quadrado["speed_x"]
        print("indo pro lado direito")
    elif esquerda:
        quadrado["x"] -= quadrado["speed_x"]
        print("indo pro lado esquerdo")

    if quadrado["y"] < screen_height - quadrado["size"]:
        can_jump = False
        quadrado["y"] += gravity
    else:
        can_jump = True
        quadrado["y"] = screen_height - quadrado["size"]
        
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event)
    
    # print(pygame.mouse.get_pressed())      

    pygame.draw.rect(window,(0,0,0), pygame.Rect(quadrado["x"],quadrado["y"],quadrado["size"],quadrado["size"]))
    
    pygame.display.update()
    time.sleep(0.005)
    
pygame.quit()