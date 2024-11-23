'''
classes: dino, cactos, (aves)
interação entre objetos: dino tocar no cacto
vitoria  
'''
import pygame
import time
import math
import random

screen_width = 600
screen_height = 400
gravity = 1
highest_score = 0

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

#classes

class Dino():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20
        self.speed = 20
        self.score = 0
        self.highest_score = 0
        
        self.up = False
        self.time = True
    
    def setUp(self,mode):
        self.up = mode
    
    def setTime(self, mode):
        self.time = mode
    
    def update(self):
        if self.up and self.y + self.h > screen_height -50:
            self.y -= self.speed
            self.speed -= gravity
        else:
            self.y += self.speed
            self.speed += gravity

        if self.y + self.h >= screen_height:
            self.y = screen_height - self.h
            self.speed = 10
    
    def render(self,window):
        # Draw the body
        pygame.draw.rect(window, (0,255,0), pygame.Rect(self.x, self.y,self.w,self.h))
        # Draw the head
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(self.x + 15, self.y - 10, 10, 10))
        # Draw the legs
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(self.x + 5, self.y + 20, 5, 10))
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(self.x + 10, self.y + 20, 5, 10))

class Ball():
    def __init__(self,x,y,dy):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.r = 15
        self.dx = -10
        self.dy = dy
        
    def revertX(self):
        self.dx *= -1
        
    def reset(self):
        self.revertX()
        self.x = self.init_x 
        self.y = self.init_y 
        
    def update(self):
        if (self.y + self.r) >= screen_height or (self.y) <= 0:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy
    
    def render(self,window):
        pygame.draw.ellipse(window, (255,255,255), pygame.Rect(self.x,self.y,self.r,self.r))
        
class Obstacle():
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def update(self):
        self.x -= self.speed
        if self.x + self.w < 0:
            self.x = screen_width

    def render(self, window):
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.x, self.y, self.w, self.h))

class Game():
    def __init__(self):
        self.speed = 3
        self.score = 0
        self.time_min = 1
        self.time_max = 10

    def reset(self):
        self.speed = 3
        self.score = 0

    def update(self):
        self.score += 1
        self.speed += 0.01

    def render(self, window):
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        window.blit(score_text, (10, 10))

#variables
dino = Dino(60, screen_height - 110)
game = Game()
obstacles = []
timing = 0

running = True
game_over = False

while(running):
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP and not game_over:
                dino.setUp(True)
            if event.key == pygame.K_RETURN and game_over:  # Reiniciar ao pressionar Enter
                game.reset()
                dino = Dino(60, screen_height - 30)
                obstacles = []
                game_over = False
                timing = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dino.setUp(False)

    if not game_over:
        dino.update()

        Dino1_rect = pygame.Rect(dino.x,dino.y,dino.w,dino.h)

        timing += 1
        if timing >= 60 * random.randint(1, 7):  # 60 frames per second * 3 to 5 seconds
            obs = Obstacle(screen_width, screen_height - 20, 20, 20, game.speed)
            obstacles.append(obs)
            timing = 0
        
        try:
            for obstacle in obstacles:
                obstacle.update()
                obstacle.render(window)
                if Dino1_rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h)):
                    highest_score = max(highest_score, game.score) + 1 # Atualizar highest_score
                    game_over = True
                obstacle.x -= obstacle.speed
                obstacle.speed -= 0.01
                if obstacle.x < 0:
                    obstacles.remove(obstacle)
        except:
            pass

        
        game.render(window)
        game.update()
        dino.render(window)
    
    else:  # Tela de fim de jogo
        game_over_text = font.render("Game Over! Press Enter to Restart", True, (255, 255, 255))
        score_text = font.render(f'Score: {game.score}', True, (255, 255, 255))
        high_score_text = font.render(f'High Score: {highest_score}', True, (255, 255, 0))
        window.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 60))
        window.blit(score_text, (screen_width // 2 - 80, screen_height // 2))
        window.blit(high_score_text, (screen_width // 2 - 120, screen_height // 2 + 40))
        
    pygame.display.update()
    time.sleep(0.05)
    
