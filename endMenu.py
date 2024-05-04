import pygame
from pygame.locals import *

def end_menu(screen, font, winner):
    background_image = pygame.image.load("end.jpg").convert()  
    background_image = pygame.transform.scale(background_image,(screen.get_width(), screen.get_height()))
    screen.blit(background_image, (0, 0)) 

    title_text = font.render("Game Over", True, (255, 255, 255))
    winner_text = font.render(winner + " Wins!", True, (255, 255, 255))
    instruction_text = font.render("Press Q to quit or R to restart", True, (255, 255, 255))
    screen.blit(title_text, ((screen.get_width() - title_text.get_width()) // 2, 200))
    screen.blit(winner_text, ((screen.get_width() - winner_text.get_width()) // 2, 300))
    screen.blit(instruction_text, ((screen.get_width() - instruction_text.get_width()) // 2, 400))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_r:
                    waiting = False
