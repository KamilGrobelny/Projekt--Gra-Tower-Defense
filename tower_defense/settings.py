"""Ustawienia: rozmiary okienka, kolory, dane dla wrogów i wież."""
import pygame
import os

WIDTH, HEIGHT = 800, 600
ROWS, COLS = 15, 20
TILE_SIZE = WIDTH // COLS
FPS = 60
SPEED_UP_FPS = 180

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (60, 60, 60)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
BROWN = (150, 75, 0)
BLACK = (0, 0, 0)

pygame.init()
FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 64)

BASE_HP = 10
STARTING_MONEY = 500
MAX_SPAWN_INTERVAL = 120
MIN_SPAWN_INTERVAL = 10
TOWER_COST = 100
TOWER_LEVEL_UP_COST = 50
ENEMY_REWARD = {
    'small': 15, 'normal': 20, 'boss': 50, 'soldier': 25,
    'paker': 100, 'skeleton': 10, 'female': 20, 'fire': 10 
    }
BAR_WIDTH = 40
BAR_HEIGHT = 5

ENEMY_DATA = {
    'small': {
        'hp': 50, 'speed': 1.5, 'damage': 1,
        'image': os.path.join('images', 'enemy_small.png')
        },
    'normal': {
        'hp': 100, 'speed': 1, 'damage': 2,
        'image': os.path.join('images', 'enemy_normal.png')
        },
    'boss': {
        'hp': 200, 'speed': 0.4, 'damage': 4, 
        'image': os.path.join('images', 'enemy_boss.png')
        },
    'paker': {
        'hp': 250, 'speed': 0.3, 'damage': 5,
        'image': os.path.join('images', 'enemy_paker.png')
        },
    'skeleton': {
        'hp': 50, 'speed': 1, 'damage': 1,
        'image': os.path.join('images', 'enemy_skeleton.png')
        },
    'fire': {
        'hp': 30, 'speed': 1.5, 'damage': 1,
        'image': os.path.join('images', 'enemy_fire.png')
        },
    'female': {
        'hp': 80, 'speed': 1.2, 'damage': 2,
        'image': os.path.join('images', 'enemy_female.png')
        },
    'soldier': {
        'hp': 150, 'speed': 0.7, 'damage': 3,
        'image': os.path.join('images', 'enemy_soldier.png')
        }
    }

TOWER_DATA = {
    1: {
        'range': 100, 'cooldown': 60, 'damage': 10,
        'image': os.path.join('images', 'tower1.png')
        },
    2: {
        'range': 100, 'cooldown': 100, 'damage': 20,
        'image': os.path.join('images', 'tower2.png')
        },
    3: {
        'range': 110, 'cooldown': 200, 'damage': 10,
        'image': os.path.join('images', 'tower3.png')
        },
    4: {
        'range': 90, 'cooldown': 0, 'damage': 200,
        'image': os.path.join('images', 'tower4.png')
        }
    }

TOWER_LEVEL_UP_DATA = {
    1: {
        'range': 100, 'cooldown': 50, 'damage': 20,
        'image': os.path.join('images', 'tower_up1.png')
        },
    2: {
        'range': 100, 'cooldown': 100, 'damage': 30,
        'image': os.path.join('images', 'tower_up2.png')
        },
    3: {
        'range': 110, 'cooldown': 150, 'damage': 25,
        'image': os.path.join('images', 'tower_up3.png')
        },
    4: {
        'range': 120, 'cooldown': 0, 'damage': 250,
        'image': os.path.join('images', 'tower_up4.png')
        }
    }
