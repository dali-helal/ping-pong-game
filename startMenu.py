import pygame
from pygame.locals import *

def start_menu(screen, font):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    background_image = pygame.image.load("start.jpg").convert()  
    background_image = pygame.transform.scale(background_image,(screen.get_width(), screen.get_height()))
    screen.blit(background_image, (0, 0)) 

    title_text = font.render("Ping Pong Game", True, WHITE)
    sub_text = font.render("Press SPACE to start the game", True, WHITE)
    screen.blit(title_text, ((screen.get_width() - title_text.get_width()) // 2, 200))
    screen.blit(sub_text, ((screen.get_width() - sub_text.get_width()) // 2, 300))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False