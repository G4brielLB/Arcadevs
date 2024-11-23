import pygame
import time

# Dimensões da tela
screen_width = 1200
screen_height = 800

# Cores
branco = (255,255,255)
preto = (0,0,0)

# Inicializa o Pygame e cria a janela
pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cruz de Malta")
font = pygame.font.SysFont('Tahoma', 150, True, False)

t = 3

# Loop principal
running = True
while running:
    # Cor de fundo (branco)
    window.fill(preto)
    
    # Clube de Regatas
    window.blit(font.render("C", True, branco), (100, 100))
    window.blit(font.render("R", True, branco), (200,100))
    # Vasco da Gama
    window.blit(font.render("V", True, branco), (900, 550))
    window.blit(font.render("G", True, branco), (1000, 550))

    # Desenha duas linhas na diagonal do canto inferior esquerdo para o canto superior direito
    pygame.draw.line(window, branco, (0, screen_height), (screen_width, 0), 500)

    # Desenha uma cruz no centro da tela
    pygame.draw.polygon(window, (255, 0, 0), [(screen_width // 2 - t*25, screen_height // 2 - t*50), 
                                            (screen_width // 2 + t*25, screen_height // 2 - t*50), 
                                            (screen_width // 2 + 3*10, screen_height // 2 - t*10), 
                                            (screen_width // 2 + t*50, screen_height // 2 - t*25), 
                                            (screen_width // 2 + t*50, screen_height // 2 + t*25), 
                                            (screen_width // 2 + t*10, screen_height // 2 + t*10), 
                                            (screen_width // 2 + t*25, screen_height // 2 + t*50), 
                                            (screen_width // 2 - t*25, screen_height // 2 + t*50), 
                                            (screen_width // 2 - t*10, screen_height // 2 + t*10), 
                                            (screen_width // 2 - t*50, screen_height // 2 + t*25), 
                                            (screen_width // 2 - t*50, screen_height // 2 - t*25), 
                                            (screen_width // 2 - t*10, screen_height // 2 - t*10)])

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Atualiza a tela
    pygame.display.update()
    
    # Controle de FPS
    time.sleep(0.16)

# Fecha o Pygame
pygame.quit()
