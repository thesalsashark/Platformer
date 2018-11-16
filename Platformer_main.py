import pygame
import random
from settings import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()


running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    all_sprites.update()

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()