import pygame
import time
import math

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

#classes

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 100
        self.speed = 10
        self.points = 0
        
        self.up = False
        self.down = False
        self.time = True
    
    def setUp(self,mode):
        self.up = mode
    
    def setDown(self,mode):
        self.down = mode
    
    def setTime(self, mode):
        self.time = mode
    
    def update(self):
        if(self.up):
            if(self.y > 0):
                self.y -= self.speed
            else:
                self.y = 0
        elif(self.down):
            if(self.y < screen_height - self.h):
                self.y += self.speed
            else:
                self.y = screen_height - self.h
    
    def render(self,window):
        pygame.draw.rect(window, (255,255,255), pygame.Rect(self.x,self.y,self.w,self.h))

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

#variables
player_1 = Player(screen_width-30,120)
player_2 = Player(10,120)
ball = Ball(screen_width // 2, screen_height // 2, 5)

running = True

while(running):
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1.setUp(True)
            if event.key == pygame.K_DOWN:
                player_1.setDown(True)
            if event.key == pygame.K_w:
                player_2.setUp(True)
            if event.key == pygame.K_s:
                player_2.setDown(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1.setUp(False)
            if event.key == pygame.K_DOWN:
                player_1.setDown(False)
            if event.key == pygame.K_w:
                player_2.setUp(False)
            if event.key == pygame.K_s:
                player_2.setDown(False)

    player_1.update()
    player_2.update()
    ball.update()
    
    ball_rect = pygame.Rect(ball.x,ball.y,ball.r,ball.r)
    player1_rect = pygame.Rect(player_1.x,player_1.y,player_1.w,player_1.h)
    player2_rect = pygame.Rect(player_2.x,player_2.y,player_2.w,player_2.h)
    
    if(ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect)):
        ball.revertX()
        
    if(ball.x < 0 or ball.x > screen_width):
        ball.reset()
    
    player_1.render(window)
    player_2.render(window)
    ball.render(window)

    
    
    pygame.display.update()
    time.sleep(0.05)