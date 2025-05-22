import pygame

from settings import TILE_SIZE, GRAY, DARK_GRAY, BLUE, BROWN, ROWS, COLS


def draw_grid(win, path_tiles, selected=None):
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if (x, y) in path_tiles:
                pygame.draw.rect(win, BROWN, rect)
            elif selected == (x, y):
                pygame.draw.rect(win, BLUE, rect)
            else:
                pygame.draw.rect(win, GRAY, rect)
            pygame.draw.rect(win, DARK_GRAY, rect, 1)
