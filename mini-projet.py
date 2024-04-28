import pygame
from pygame.locals import *
import random
from balle import Ball
from startMenu import start_menu
from endMenu import end_menu

def main():
    pygame.init()
    WIDTH_SCREEN, HEIGHT_SCREEN = 960, 720
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    fond = pygame.image.load("pingPong.png").convert()
    screen.blit(fond, (0, 0))

    ball_radius = 10
    ball_speed_x = 7
    ball_speed_y = 7

    paddle_width = 15
    paddle_height = 100
    paddle_speed = 7

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
   

    ball = Ball(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, ball_radius, random.choice([-1, 1]) * ball_speed_x, random.choice([-1, 1]) * ball_speed_y)
    player1 = pygame.Rect(50, HEIGHT_SCREEN / 2 - paddle_height / 2, paddle_width, paddle_height)
    player2 = pygame.Rect(895, HEIGHT_SCREEN / 2 - paddle_height / 2, paddle_width, paddle_height)

    score1 = 0
    score2 = 0
    font = pygame.font.Font(None, 50)

    start_menu(screen, font)

    start_time = pygame.time.get_ticks()
    timer_font = pygame.font.Font(None, 36)
    game_duration = 60  

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and player1.top > 0:
            player1.y -= paddle_speed
        if keys[pygame.K_s] and player1.bottom < HEIGHT_SCREEN:
            player1.y += paddle_speed
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT_SCREEN:
            player2.y += paddle_speed

        ball.move()

        if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT_SCREEN:
            ball.reflect_vertical()
        if ball.rect.left <= 0:
            ball = Ball(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, ball_radius, random.choice([-1, 1]) * ball_speed_x, random.choice([-1, 1]) * ball_speed_y)
            score2 += 1
        if ball.rect.right >= WIDTH_SCREEN:
            ball = Ball(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, ball_radius, random.choice([-1, 1]) * ball_speed_x, random.choice([-1, 1]) * ball_speed_y)
            score1 += 1

        if ball.rect.colliderect(player1) or ball.rect.colliderect(player2):
            ball.reflect_horizontal()

        screen.blit(fond, (0, 0))

        pygame.draw.rect(screen, BLUE, player1)
        pygame.draw.rect(screen, RED, player2)
        pygame.draw.ellipse(screen, WHITE, ball.rect)

        # Render timer text
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(game_duration - elapsed_time, 0)
        timer_text = timer_font.render("Time: " + str(remaining_time), True, WHITE)
        screen.blit(timer_text, ((WIDTH_SCREEN - timer_text.get_width()) // 2, 50))

        score_text1 = font.render(str(score1), True, BLUE)
        score_text2 = font.render(str(score2), True, RED)

        screen.blit(score_text1, (WIDTH_SCREEN // 4, 50))  # 1/4
        screen.blit(score_text2, (WIDTH_SCREEN * 3 // 4, 50))  # 3/4

        if remaining_time == 0 or score1 == 15 or score2 == 15:
            winner = "Player 1" if score1 > score2 else "Player 2"
            end_menu(screen, font, winner)
            start_menu(screen, font)
            start_time = pygame.time.get_ticks()
            score1 = 0
            score2 = 0
            ball = Ball(WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2, ball_radius, random.choice([-1, 1]) * ball_speed_x, random.choice([-1, 1]) * ball_speed_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
