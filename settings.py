import pygame
from color_constants import *
vec = pygame.math.Vector2

title = "Bingo Bounce"
display_width = 480
display_height = 600
fps = 60
FONT_NAME = 'arial'
BGCOLOR = ALICEBLUE
HS_FILE = "highscore.txt"

# Player Properties
player_acc = 0.5
player_fric = -.02
player_grav = .2
player_jump = 8

# Player images
idle_cycle = [pygame.image.load('image/cat/Idle (1).png'),
              pygame.image.load('image/cat/Idle (2).png'),
              pygame.image.load('image/cat/Idle (3).png'),
              pygame.image.load('image/cat/Idle (4).png'),
              pygame.image.load('image/cat/Idle (5).png'),
              pygame.image.load('image/cat/Idle (6).png'),
              pygame.image.load('image/cat/Idle (7).png'),
              pygame.image.load('image/cat/Idle (8).png')
              ]

jump_cycle = [pygame.image.load('image/cat/Jump (1).png'),
              pygame.image.load('image/cat/Jump (2).png'),
              pygame.image.load('image/cat/Jump (3).png'),
              pygame.image.load('image/cat/Jump (4).png'),
              pygame.image.load('image/cat/Jump (5).png'),
              pygame.image.load('image/cat/Jump (6).png'),
              pygame.image.load('image/cat/Jump (7).png'),
              pygame.image.load('image/cat/Jump (8).png')
              ]

run_cycle = [pygame.image.load('image/cat/Run (1).png'),
             pygame.image.load('image/cat/Run (2).png'),
             pygame.image.load('image/cat/Run (3).png'),
             pygame.image.load('image/cat/Run (4).png'),
             pygame.image.load('image/cat/Run (5).png'),
             pygame.image.load('image/cat/Run (6).png'),
             pygame.image.load('image/cat/Run (7).png'),
             pygame.image.load('image/cat/Run (8).png')
             ]

walk_cycle = [pygame.image.load('image/cat/Walk (1).png'),
              pygame.image.load('image/cat/Walk (2).png'),
              pygame.image.load('image/cat/Walk (3).png'),
              pygame.image.load('image/cat/Walk (4).png'),
              pygame.image.load('image/cat/Walk (5).png'),
              pygame.image.load('image/cat/Walk (6).png'),
              pygame.image.load('image/cat/Walk (7).png'),
              pygame.image.load('image/cat/Walk (8).png')
              ]

fall_cycle = [pygame.image.load('image/cat/Fall (1).png'),
              pygame.image.load('image/cat/Fall (2).png'),
              pygame.image.load('image/cat/Fall (3).png'),
              pygame.image.load('image/cat/Fall (4).png'),
              pygame.image.load('image/cat/Fall (5).png'),
              pygame.image.load('image/cat/Fall (6).png'),
              pygame.image.load('image/cat/Fall (7).png'),
              pygame.image.load('image/cat/Fall (8).png')
              ]

dead_cycle = [pygame.image.load('image/cat/Dead (1).png'),
              pygame.image.load('image/cat/Dead (2).png'),
              pygame.image.load('image/cat/Dead (3).png'),
              pygame.image.load('image/cat/Dead (4).png'),
              pygame.image.load('image/cat/Dead (5).png'),
              pygame.image.load('image/cat/Dead (6).png'),
              pygame.image.load('image/cat/Dead (7).png'),
              pygame.image.load('image/cat/Dead (8).png')
              ]

player_image = idle_cycle[0]
# player_left = run_cycle[0]
# player_right = run_cycle[0]
player_height = player_image.get_height()/2

# Platform properties

# Platform images
platform_list = [(0, 500),
                 (100, 400),
                 (350, 300),
                 (150, 225),
                 (200, 175),
                 (300, 50),
                 ]

# Starting platforms
platform_img_list = [pygame.image.load('image/platforms/PNG/Environment/ground_grass.png'),
                     pygame.image.load('image/platforms/PNG/Environment/ground_grass_broken.png'),
                     pygame.image.load('image/platforms/PNG/Environment/ground_grass_small.png'),
                     pygame.image.load('image/platforms/PNG/Environment/ground_grass_small_broken.png')
                     ]