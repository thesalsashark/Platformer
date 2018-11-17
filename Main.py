import pygame
import random
from settings import *
from color_constants import *
from sprites import *
from os import path


class Game:
    def __init__(self):
        # Initialize game window and other things
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # All graphics and sounds etc
        # Load high score
        self.dir = path.dirname(__file__)
        try:
            with open(path.join(self.dir, HS_FILE), 'r') as f:
                self.highscore = int(f.read())
                f.close()
        except:
            self.highscore = 0

    def new(self):
        # start new game
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in platform_list:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        # If player reaches top 1/4 of the screen
        if self.player.rect.top <= display_height/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= display_height:
                    plat.kill()
                    self.score += 1

        # Die
        if self.player.rect.bottom > display_height:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        # Spawn new platforms
        while len(self.platforms) < 6:
            p_width = random.randrange(50, 100)
            p = Platform(self, random.randrange(0, display_width - p_width),
                         random.randrange(-10, -5))
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        # game loop draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 20, BLACK, 30, 5)
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(title, 50, BANANA, display_width/2, display_height/4)
        self.draw_text("Press any key to begin", 22, BANANA, display_width/2, display_height * (1/2))
        self.draw_text("Arrows to move, Space to jump", 22, BANANA, display_width/2, display_height * (3/4))
        self.draw_text("High Score: " + str(self.highscore), 22, BANANA, display_width/2, 15)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                    # pygame.quit()
                    # quit()
                if event.type == pygame.KEYUP:
                    waiting = False

    def show_game_over(self):
        # Show game over/go screen
        if not self.running:
            return
        self.draw_text("Game Over", 50, BANANA, display_width/2, display_height/4)
        self.draw_text("Score: " + str(self.score), 22, BANANA, display_width/2, display_height * (1/2))
        self.draw_text("Press any key to play again", 22, BANANA, display_width/2, display_height * (3/4))
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("You got a new high score!", 22, BANANA, display_width/2, (display_height * (1/2)) + 25)
            with open(path.join(self.dir, HS_FILE), 'w+') as f:
                f.write(str(self.highscore))
                f.close()
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, BANANA, display_width / 2, (display_height * (1 / 2)) + 25)
        pygame.display.flip()
        self.wait_for_key()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_game_over()

pygame.quit()
