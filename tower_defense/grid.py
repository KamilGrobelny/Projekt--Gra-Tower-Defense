import pygame
import os
from settings import WIDTH, HEIGHT, TILE_SIZE, DARK_GRAY, WHITE, RED

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ładowanie teł map
def load_map_backgrounds():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    map_dir = os.path.join(script_dir, 'images', 'maps')

    backgrounds = {}
    for filename in os.listdir(map_dir):
        if filename.endswith('.png'):
            name = filename[:-4]  
            img = pygame.image.load(os.path.join(map_dir, filename)).convert()
            img = pygame.transform.scale(img, (WIDTH, HEIGHT))
            backgrounds[name] = img
    return backgrounds

def load_ui_textures():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ui_dir = os.path.join(script_dir, 'images', 'ui')

    textures = {}
    for filename in os.listdir(ui_dir):
        if filename.endswith('.png'):
            name = filename[:-4]  
            img = pygame.image.load(os.path.join(ui_dir, filename)).convert_alpha()
            textures[name] = img
    return textures

# dane
map_backgrounds = load_map_backgrounds()
textures = load_ui_textures()

# rysowanie mapy
def draw_map_background(win, map_name):
    background = map_backgrounds.get(map_name)
    if background:
        win.blit(background, (0, 0))
    else:
        print(f"Nie znaleziono tła dla mapy: {map_name}")
        win.fill((50, 50, 50))  
# pasek z góry i z dołu
def draw_sidebar(win, textures):
    side_bar_surf = textures['sidebar']
    scaled_sidebar = pygame.transform.scale(side_bar_surf, (WIDTH, TILE_SIZE))
    win.blit(scaled_sidebar, (0, 0))
    win.blit(scaled_sidebar, (0, HEIGHT - TILE_SIZE))

def draw_grid(win, path_tiles, selected_tile):
    cols = WIDTH // TILE_SIZE
    rows = (HEIGHT - 2 * TILE_SIZE) // TILE_SIZE

    for x in range(cols):
        for y in range(rows):
            grid_x = x * TILE_SIZE
            grid_y = y * TILE_SIZE + TILE_SIZE  

            rect = pygame.Rect(grid_x, grid_y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(win, WHITE, rect, 1)  

    if selected_tile:
        sx, sy = selected_tile
        if 1 <= sy < rows + 1:
            rect = pygame.Rect(sx * TILE_SIZE, sy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(win, RED, rect, 3)  

