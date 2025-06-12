import pygame

WIDTH, HEIGHT = 800, 600
ROWS, COLS = 15, 20
TILE_SIZE = WIDTH // COLS
FPS = 60

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
BROWN = (150, 75, 0)

pygame.init()
FONT = pygame.font.SysFont(None, 28)

BASE_HP = 10
STARTING_MONEY = 500
TOWER_COST = 100
ENEMY_REWARD = {'small': 5, 'normal': 10, 'boss': 50}
BAR_WIDTH = 40
BAR_HEIGHT = 5

ENEMY_DATA = {'small':{'hp':50, 'speed':1.5, 'image':'images/enemy_small.png'},
               'normal':{'hp':100, 'speed':1, 'image':'images/enemy_normal.png'},
               'boss':{'hp':200, 'speed':0.4, 'image':'images/enemy_boss.png'}}

TOWER_DATA = {1: {'range': 100, 'cooldown': 60, 'image': 'images/tower1.png', 'damage': 10},
              2: {'range': 100, 'cooldown': 100, 'image': 'images/tower1a.png', 'damage': 20},
              3: {'range': 150, 'cooldown': 110, 'image': 'images/tower1b.png', 'damage': 10},
              4: {'range': 75, 'cooldown': 0, 'image': 'images/tower1c.png', 'damage': 100}}

TOWER_LEVEL_UP_DATA = {1: {'range': 100, 'cooldown': 50, 'image': 'images/tower2.png', 'damage': 10},
                       2: {'range': 100, 'cooldown': 100, 'image': 'images/tower2a.png', 'damage': 25},
                       3: {'range': 150, 'cooldown': 130, 'image': 'images/tower2b.png', 'damage': 10},
                       4: {'range': 90, 'cooldown': 0, 'image': 'images/tower2c.png', 'damage': 100}}
