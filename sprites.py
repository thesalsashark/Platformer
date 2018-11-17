# Sprite class for pygame
import pygame
from settings import *
from color_constants import *
from random import choice
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.running = False
        self.jumping = False
        self.falling = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        # self.image = pygame.Surface((30, 40))
        self.image = player_image
        self.direction = 'front'
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)
        self.pos = vec(display_width/2, display_height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.jumping_frames_r = jump_cycle
        self.jumping_frames_l = []
        for frame in self.jumping_frames_r:
            frame_l = pygame.transform.flip(frame, True, False)
            self.jumping_frames_l.append(frame_l)

        self.walking_frames_r = walk_cycle
        self.walking_frames_l = []
        for frame in self.walking_frames_r:
            frame_l = pygame.transform.flip(frame, True, False)
            self.walking_frames_l.append(frame_l)

        self.running_frames_r = run_cycle
        self.running_frames_l = []
        for frame in self.running_frames_r:
            frame_l = pygame.transform.flip(frame, True, False)
            self.running_frames_l.append(frame_l)

        self.dead_frames = dead_cycle

        self.idle_frames_r = idle_cycle
        self.idle_frames_l = []
        for frame in self.idle_frames_r:
            frame_l = pygame.transform.flip(frame, True, False)
            self.idle_frames_l.append(frame_l)

        self.fall_frames_r = fall_cycle
        self.fall_frames_l = []
        for frame in self.fall_frames_r:
            frame_l = pygame.transform.flip(frame, True, False)
            self.fall_frames_l.append(frame_l)

    def jump(self):
        # jump only if standing on platform
        self.jumping = True
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -player_jump

    def update(self):
        self.animate()
        self.acc = vec(0, player_grav)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            self.acc.x = -player_acc
        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.acc.x = player_acc
        if keys[pygame.K_UP]:
            self.direction = 'front'
            self.acc.y = -player_acc
        if keys[pygame.K_DOWN]:
            self.direction = 'front'
            self.acc.y = player_acc

        # apply friction
        self.acc.x += self.vel.x * player_fric

        # equations for motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + (0.5 * self.acc)

        # wrap around the sides of the screen
        if self.pos.x > display_width + self.rect.width/2:
            self.pos.x = 0 - self.rect.width/2
        if self.pos.x < 0 - self.rect.width/2:
            self.pos.x = display_width + self.rect.width/2

        self.rect.midbottom = self.pos

    def animate(self):
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            if self.vel.y > 0:
                self.jumping = True
            else:
                self.running = True
        else:
            self.running = False

        # Idle
        if not self.jumping and not self.running:
            if now - self.last_update > 220:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_r)
                midbottom = self.rect.midbottom
                if self.direction == 'right':
                    self.image = self.idle_frames_r[self.current_frame]
                else:
                    self.image = self.idle_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.midbottom = midbottom

        # Running
        if self.running:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_frames_r)
                midbottom = self.rect.midbottom
                # if self.vel.x > 0:
                if self.direction == 'right':
                    self.image = self.running_frames_r[self.current_frame]
                else:
                    self.image = self.running_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.midbottom = midbottom

        # Jumping
        if self.vel.y < 0:
            self.jumping = True
            self.running = False
        elif self.vel.y > 0:
            self.jumping = False
            self.running = False
            self.falling = True
        else:
            self.jumping = False
            self.falling = False
        if self.jumping:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.jumping_frames_r)
                midbottom = self.rect.midbottom
                if self.direction == 'right':
                    self.image = self.jumping_frames_r[self.current_frame]
                else:
                    self.image = self.jumping_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.midbottom = midbottom

        # Falling
        if self.falling:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.fall_frames_r)
                midbottom = self.rect.midbottom
                if self.direction == 'right':
                    self.image = self.fall_frames_r[self.current_frame]
                else:
                    self.image = self.fall_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.midbottom = midbottom


class Platform(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = choice(platform_img_list)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y