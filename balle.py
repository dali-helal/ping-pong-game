import pygame
from pygame.locals import *

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reflect_horizontal(self):
        self.speed_x *= -1

    def reflect_vertical(self):
        self.speed_y *= -1
    def collision(self,targetRect):
        return self.rect.colliderect(targetRect)
