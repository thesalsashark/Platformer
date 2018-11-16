#Sprite class for pygame
import pygame
from settings import *
from color_constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(BANANA)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -5
        if keys[pygame.K_RIGHT]:
            self.vx = 5

        self.rect.x += self.vx
        self.rect.y += self.vy