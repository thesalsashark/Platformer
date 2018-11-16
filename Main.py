import pygame
import random
from settings import *

class Game:
    def __init__(self):
        # Initialize game window and other things
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start new game
        all_sprites = pygame.sprite.Group()

    def run(self):
        self.playing = True
            while self.playing:
                self.clock.tick(fps)

    def update(self):
        # game loop update
        pass

    def events(self):
        # game loop events
        pass

    def draw(self):
        # game loop draw
        pass

    def show_start_screen(self):
        pass

    def show_game_over(self):
        pass

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_game_over()

pygame.quit()