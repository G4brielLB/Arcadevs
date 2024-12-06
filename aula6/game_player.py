import pygame
import time
import os

class Game():
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 400
        self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.objects = []
        self.running = True
        
    def addObject(self, new_object):
        self.objects.append(new_object)
        
    def update(self):
        for obj in self.objects:
            obj.update()
            
    def render(self):
        pygame.draw.rect(self.window, (250,250,250), pygame.Rect(0, 0, self.screen_width, self.screen_height))
        for obj in self.objects:
            obj.render(self.window)
                    
class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.speed = 4
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/eu.png"))
        
    def setUp(self, mode):
        self.up = mode
        
    def setDown(self, mode):
        self.down = mode
        
    def setRight(self, mode):
        self.right = mode
        
    def setLeft(self, mode):
        self.left = mode
        
    def update(self):
        if(self.up):
            self.y -= self.speed
        elif(self.down):
            self.y += self.speed
        if(self.right):
            self.x += self.speed
        elif(self.left):
            self.x -= self.speed
        
    def render(self, window):
        window.blit(self.sprite, (self.x, self.y))
            
if __name__ == "__main__":
    
    game = Game()
    player = Player(10,20)
    game.addObject(player)
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.setUp(True)
                if event.key == pygame.K_s:
                    player.setDown(True)
                if event.key == pygame.K_d:
                    player.setRight(True)
                if event.key == pygame.K_a:
                    player.setLeft(True)
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.setUp(False)
                if event.key == pygame.K_s:
                    player.setDown(False)
                if event.key == pygame.K_d:
                    player.setRight(False)
                if event.key == pygame.K_a:
                    player.setLeft(False)
                
        game.update()
        game.render()
        
        pygame.display.update()
        time.sleep(0.05)
        