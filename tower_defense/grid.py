import pygame
import os
from settings import WIDTH, HEIGHT, TILE_SIZE, GRAY, RED


def load_map_backgrounds() -> dict[str, pygame.Surface]:
    """Ładuje wszystkie tła map z katalogu maps.
    
    Przeszukuje katalog 'images/maps' w poszukiwaniu plików PNG,
    ładuje je jako powierzchnie, skaluje do rozmiarów ekranu 
    i zwraca jako słownik z nazwami plików (bez rozszerzeń) jako
    kluczami.
    
    Zwraca:
        Słownik mapujący nazwy map na odpowiadające im powierzchnie
        z tłem.
    """
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


def load_ui_textures() -> dict[str, pygame.Surface]:
    """Ładuje wszystkie tekstury UI z katalogu ui.
    
    Przeszukuje katalog 'images/ui' w poszukiwaniu plików
    z rozszerzeniem .png, ładuje je jako powierzchnie
    z zachowaniem przezroczystości i zwraca jako słownik z nazwami 
    plików (bez rozszerzeń) jako kluczami.
    
    Zwraca:
        Słownik mapujący nazwy tekstur na odpowiadające im powierzchnie.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ui_dir = os.path.join(script_dir, 'images', 'ui')

    textures = {}
    for filename in os.listdir(ui_dir):
        if filename.endswith('.png'):
            name = filename[:-4]  
            img = pygame.image.load(os.path.join(ui_dir, filename)).convert_alpha()
            textures[name] = img
    return textures


def draw_map_background(window: pygame.Surface, map_name: str, map_backgrounds: dict[str, pygame.Surface]) -> None:
    """Rysuje (wkleja) określone tło mapy na podanej powierzchni.
    
    Argumenty:
        window: Powierzchnia, na której należy narysować tło.
        map_name: Nazwa tła mapy do narysowania.
        
    Jeśli podane tło mapy nie zostanie znalezione, wypełnia powierzchnię
    ciemnoszarym kolorem i wyświetla komunikat o błędzie.
    """
    background = map_backgrounds.get(map_name)
    if background:
        window.blit(background, (0, 0))
    else:
        print(f'Nie znaleziono tła dla mapy: {map_name}')
        window.fill((50, 50, 50))


def draw_sidebar(window: pygame.Surface, textures: dict[str, pygame.Surface]) -> None:
    """Rysuje (wkleja) pasek boczny (UI) u góry i na dole ekranu.
    
    Argumenty:
        window: Powierzchnia, na której należy narysować paski.
        textures: Słownik zawierający teksturę paska bocznego.
        
    Skaluje teksturę 'sidebar' do szerokości ekranu i rysuje ją
    zarówno u góry, jak i na dole ekranu.
    """
    side_bar_surf = textures['sidebar']
    scaled_sidebar = pygame.transform.scale(side_bar_surf, (WIDTH, TILE_SIZE))
    window.blit(scaled_sidebar, (0, 0))
    window.blit(scaled_sidebar, (0, HEIGHT - TILE_SIZE))


def draw_grid(window: pygame.Surface, selected_tile: tuple[int, int]) -> None:
    """Rysuje siatkę na obszarze gry i podświetla wybrany kafelek.
    
    Argumenty:
        window: Powierzchnia, na której należy narysować siatkę.
        selected_tile: Współrzędne aktualnie wybranego kafelka (x, y).
        
    Rysuje białą siatkę na obszarze gry (między paskami bocznymi) i
    podświetla wybrany kafelek czewoną ramką, jeśli znajduje się w granicach.
    """
    cols = WIDTH // TILE_SIZE
    rows = (HEIGHT - 2 * TILE_SIZE) // TILE_SIZE

    for x in range(cols):
        for y in range(rows):
            grid_x = x * TILE_SIZE
            grid_y = y * TILE_SIZE + TILE_SIZE  

            rect = pygame.Rect(grid_x, grid_y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(window, GRAY, rect, 1)  

    if selected_tile:
        sx, sy = selected_tile
        if 1 <= sy < rows + 1:
            rect = pygame.Rect(sx * TILE_SIZE, sy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(window, RED, rect, 3)