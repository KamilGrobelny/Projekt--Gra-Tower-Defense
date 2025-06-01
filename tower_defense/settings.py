import pygame

WIDTH, HEIGHT = 800, 600
ROWS, COLS = 12, 16
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

STARTING_MONEY = 500
TOWER_COST = 100
ENEMY_REWARD = {'small': 5, 'normal': 10, 'boss': 50}
BAR_WIDTH = 40
BAR_HEIGHT = 5

ENEMY_DATA = {'small':{'hp':50, 'speed':1.5, 'image':'images/enemy_small.png'},
               'normal':{'hp':100, 'speed':1, 'image':'images/enemy_normal.png'},
               'boss':{'hp':200, 'speed':1.2, 'image':'images/enemy_boss.png'}}