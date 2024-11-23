import pygame
import time
import math

screen_width = 600
screen_height = 400
H = 100
W = 20

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

#classes

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = W
        self.h = H
        self.speed = 5
        self.down = False
        self.up = False
        self.points = 0

    #def setDy(self, new_dy):
    #    self.dy = new_dy

    def setUp(self, up):
        self.up = up

    def setDown(self, down):
        self.down = down

    def setPoints(self):
        self.points += 1

    def update(self):
        if self.up and self.y > 0:
                self.y -= self.speed
        elif self.down and self.y < screen_height - H:
                self.y += self.speed
    
    def render(self,window):
        pygame.draw.rect(window, (255,255,255), pygame.Rect(self.x,self.y,self.w,self.h))

class Ball():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.dx = 2
        self.dy = 2

    def update(self, player_1, player_2):
        self.x += self.dx
        self.y += self.dy
        if self.y < self.r or self.y > screen_height - self.r:
            self.dy *= -1
        if self.x < 0 or self.x > screen_width:
            self.dx = 2
            self.dy = 2
            if self.x < 0:
                player_2.setPoints()
            else:
                player_1.setPoints()
            self.dx *= -1
            self.x, self.y = screen_width // 2, screen_height // 2
        if (self.x - self.r < player_1.x + player_1.w and self.y > player_1.y and self.y < player_1.y + player_1.h) or \
           (self.x + self.r > player_2.x and self.y > player_2.y and self.y < player_2.y + player_2.h):
            # Se a bola bater no player acima do meio ele vai para cima, se for abaixo do meio vai para baixo
            self.dx *= -1.1
            self.dy *= 1.1
            if self.x - self.r < player_1.x + player_1.w:
                if self.y < player_1.y + player_1.h / 2:
                    self.dy = -abs(self.dy)
                else:
                    self.dy = abs(self.dy)
            elif self.x + self.r > player_2.x:
                if self.y < player_2.y + player_2.h / 2:
                    self.dy = -abs(self.dy)
                else:
                    self.dy = abs(self.dy)

    def render(self, window):
        pygame.draw.circle(window, (255,255,255), (self.x, self.y), self.r)

# Variables
player_1 = Player(10, (screen_height - H) / 2)
player_2 = Player(screen_width - W - 10, (screen_height - H)/ 2)
ball = Ball(screen_width // 2, screen_height // 2, 10)

running = True

while(running):
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2.setUp(True)
            elif event.key == pygame.K_DOWN:
                player_2.setDown(True)
            if event.key == pygame.K_w:
                player_1.setUp(True)
            elif event.key == pygame.K_s:
                player_1.setDown(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2.setUp(False)
            elif event.key == pygame.K_DOWN:
                player_2.setDown(False)
            if event.key == pygame.K_w:
                player_1.setUp(False)
            elif event.key == pygame.K_s:
                player_1.setDown(False)

    player_1.update()
    player_2.update()
    ball.update(player_1, player_2)

    player_1.render(window)
    player_2.render(window)
    ball.render(window)

    # Escreva os pontos dos jogadores centralizados em cima
    text = font.render(f"{player_1.points} x {player_2.points}", True, (255,255,255))
    window.blit(text, (screen_width // 2 - text.get_width() // 2, 10))

    pygame.display.update()
    time.sleep(0.01)
    