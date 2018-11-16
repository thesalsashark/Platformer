import pygame
import random
from settings import *
from color_constants import *
from sprites import *

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
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        g.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop update
        self.all_sprites.update()

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                quit()

    def draw(self):
        # game loop draw
        self.screen.fill(ALICEBLUE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

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