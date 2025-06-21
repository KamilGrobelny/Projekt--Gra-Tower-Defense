"""Ustawienia: rozmiary okienka, kolory, dane dla wrogów i wież."""
import pygame

WIDTH, HEIGHT = 800, 600
ROWS, COLS = 15, 20
TILE_SIZE = WIDTH // COLS
FPS = 60

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (80, 80, 80)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
BROWN = (150, 75, 0)
BLACK = (0, 0, 0)

pygame.init()
FONT = pygame.font.SysFont(None, 28)

BASE_HP = 10
STARTING_MONEY = 500
TOWER_COST = 100
TOWER_LEVEL_UP_COST = 50
ENEMY_REWARD = {
    'small': 15, 'normal': 20, 'boss': 50, 'soldier': 25,
    'paker': 100, 'skeleton': 10, 'female': 20, 'fire': 10 
    }
BAR_WIDTH = 40
BAR_HEIGHT = 5

ENEMY_DATA = {
    'small': {'hp': 50, 'speed': 1.5, 'image': 'images/enemy_small.png', 'damage': 1},
    'normal': {'hp': 100, 'speed': 1, 'image': 'images/enemy_normal.png', 'damage': 2},
    'boss': {'hp': 200, 'speed': 0.4, 'image': 'images/enemy_boss.png', 'damage': 4},
    'paker': {'hp': 250, 'speed': 0.3, 'image': 'images/enemy_paker.png', 'damage': 5},
    'skeleton': {'hp': 50, 'speed': 1, 'image': 'images/enemy_skeleton.png', 'damage': 1},
    'fire': {'hp': 30, 'speed': 1.5, 'image': 'images/enemy_fire.png', 'damage': 1},
    'female': {'hp': 80, 'speed': 1.2, 'image': 'images/enemy_female.png', 'damage': 2},
    'soldier': {'hp': 150, 'speed': 0.7, 'image': 'images/enemy_soldier.png', 'damage': 3}
    }

TOWER_DATA = {
    1: {'range': 100, 'cooldown': 60, 'image': 'images/tower1.png', 'damage': 10},
    2: {'range': 100, 'cooldown': 100, 'image': 'images/tower2.png', 'damage': 20},
    3: {'range': 110, 'cooldown': 200, 'image': 'images/tower3.png', 'damage': 10},
    4: {'range': 90, 'cooldown': 0, 'image': 'images/tower4.png', 'damage': 100}
    }

TOWER_LEVEL_UP_DATA = {
    1: {'range': 100, 'cooldown': 50, 'image': 'images/tower_up1.png', 'damage': 10},
    2: {'range': 100, 'cooldown': 100, 'image': 'images/tower_up2.png', 'damage': 25},
    3: {'range': 110, 'cooldown': 150, 'image': 'images/tower_up3.png', 'damage': 10},
    4: {'range': 120, 'cooldown': 0, 'image': 'images/tower_up4.png', 'damage': 100}
    }
