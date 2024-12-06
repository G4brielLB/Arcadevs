import pygame
import time
import os

screen_width = 600
screen_height = 400
camera_x = 0
camera_y = 0

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((screen_width,screen_height))
        self.objects = []
        self.running = True
        
    def addObject(self, new_object):
        self.objects.append(new_object)
        
    def update(self):
        for obj in self.objects:
            obj.update()
            
    def render(self):
        pygame.draw.rect(self.window, (0,0,0), pygame.Rect(0, 0, screen_width, screen_height))
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
        global camera_x
        global camera_y
        
        if(self.up):
            self.y -= self.speed
        elif(self.down):
            self.y += self.speed
        if(self.right):
            self.x += self.speed
        elif(self.left):
            self.x -= self.speed
            
        camera_x = self.x - (screen_width // 2)
        camera_y = self.y - (screen_height // 2)
        
    def render(self, window):
        # pygame.draw.rect(window, (50,100,50), pygame.Rect(self.x, self.y, self.size, self.size))
        window.blit(self.sprite, (self.x - camera_x, self.y - camera_y))
        
class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = None
        
    def update(self):
        return
        
    def render(self, window):
        global camera_x
        global camera_y
        
        window.blit(self.sprite, (self.x - camera_x, self.y - camera_y))
        
class Grass(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/grama.png"))
        
class Water(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/water.png"))
        
            
if __name__ == "__main__":
    
    game = Game()
    player = Player(10,20)
    
    for i in range(20):
        for j in range(20):
            game.addObject(Grass(i * 40,j * 40))
    
    for i in range(4,12):
        for j in range(4,12):
            game.addObject(Water(i * 40,j * 40))
    
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