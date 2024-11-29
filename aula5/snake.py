import random
import pygame
import time

screen_width = 600
screen_height = 400

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

cor_atual = 0
cores = [preto, branco, preto, branco, preto, vermelho]
highest_score = 0

def atualizar_cor():
    global cor_atual
    if cor_atual == len(cores) - 1:
        cor_atual = 0
    else:
        cor_atual += 1
#classes

class Head():
    def __init__(self,x,y, cor_atual):
        self.x = x
        self.y = y
        self.size = 20
        self.dir = "right"
        self.score = 0
        self.cor = cores[cor_atual]
        atualizar_cor()
    
    def setUp(self):
        if self.dir != "down":
            self.dir = "up"
    
    def setDown(self):
        if self.dir != "up":
            self.dir = "down"
        
    def setRight(self):
        if self.dir != "left":
            self.dir = "right"
    
    def setLeft(self):
        if self.dir != "right":
            self.dir = "left"
    
    def update(self):
        if self.dir == "right":
            self.x += self.size
        elif self.dir == "left":
            self.x -= self.size
        elif self.dir == "up":
            self.y -= self.size
        elif self.dir == "down":
            self.y += self.size
            
    def checkCollide(self, x, y, w, h):
        return pygame.Rect(self.x, self.y, self.size, self.size).colliderect(pygame.Rect(x,y,w,h))
        
    def render(self, window):
        pygame.draw.rect(window, self.cor, pygame.Rect(self.x, self.y, self.size, self.size))

class Segment():
    def __init__(self, pattern, cor_atual):
        self.x = pattern.x
        self.y = pattern.y
        self.pattern = pattern
        self.size = 20
        self.cor = cores[cor_atual]
        atualizar_cor()
        
    def update(self):
        self.x = self.pattern.x
        self.y = self.pattern.y
        self.pattern.update()
        
    def render(self, window):
        pygame.draw.rect(window, self.cor, pygame.Rect(self.x, self.y, self.size, self.size))
        self.pattern.render(window)
        
class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20

    def render(self, window):
        # Draw the bun
        pygame.draw.rect(window, (247, 225, 164), pygame.Rect(self.x, self.y, self.size, self.size // 2))  # Top bun
        pygame.draw.rect(window, (247, 225, 164), pygame.Rect(self.x, self.y + self.size // 2, self.size, self.size // 2))  # Bottom bun
        # Draw the patty
        pygame.draw.rect(window, (160, 82, 45), pygame.Rect(self.x, self.y + self.size // 4, self.size, self.size // 2))
        # Draw the lettuce
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(self.x, self.y + self.size // 2 - 1, self.size, 2))
        
#inits 
         
pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True
pause = False
game_over = False

head = Head(20,40, cor_atual=cor_atual)
tail1 = Segment(head, cor_atual=cor_atual)
tail = Segment(tail1, cor_atual=cor_atual)
food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20)

while(running):
    pygame.draw.rect(window, (200,200,200), pygame.Rect(0,0,screen_width, screen_height))
    
    if game_over:
        if head.score > highest_score:
            highest_score = head.score
        text = font.render('Game Over! Press R to Restart', True, vermelho)
        window.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        score_text = font.render(f'Score: {head.score} | Highest Score: {highest_score}', True, vermelho)
        # Escreva score_text na tela abaixo de text
        window.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 + text.get_height() // 2))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cor_atual = 0
                    head = Head(20, 40, cor_atual=cor_atual)
                    tail1 = Segment(head, cor_atual=cor_atual)
                    tail = Segment(tail1, cor_atual=cor_atual)
                    food = Food(random.randint(0, screen_width // 20 - 1) * 20, random.randint(0, screen_height // 20 - 1) * 20)
                    game_over = False
                    pause = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                head.setUp()
            if event.key == pygame.K_s:
                head.setDown()
            if event.key == pygame.K_d:
                head.setRight()
            if event.key == pygame.K_a:
                head.setLeft()
            if event.key == pygame.K_p:
                pause = not pause
    
    if not pause:
        tail.update()
    
    if(head.checkCollide(food.x, food.y, food.size, food.size)):
        new_tail = Segment(tail, cor_atual=cor_atual)
        tail = new_tail
        head.score += 1
        food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20) 

    if head.x < 0:
        head.x = screen_width - head.size
    if head.x >= screen_width:
        head.x = 0
    if head.y < 0:
        head.y = screen_height - head.size
    if head.y >= screen_height:
        head.y = 0

    current_segment = tail
    while isinstance(current_segment, Segment):
        if head.checkCollide(current_segment.x, current_segment.y, current_segment.size, current_segment.size):
            game_over = True
            break
        current_segment = current_segment.pattern
    

    tail.render(window)
    food.render(window)
    
    pygame.display.update()
    time.sleep(0.1)