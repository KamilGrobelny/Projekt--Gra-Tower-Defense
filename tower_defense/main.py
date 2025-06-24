import pygame
import os

from settings import WIDTH, HEIGHT
from maps import MAPS
from menu import choose_map, choose_mode
from game import game_loop


def main():
    """Główna pętla programu, która umożliwia wybór trybu oraz mapy gry."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pygame.init()
    FONT = pygame.font.SysFont(None, 28)
    BIG_FONT = pygame.font.SysFont(None, 64)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tower Defense')

    new_game = True
    while new_game:
        mode = choose_mode(window, FONT, BIG_FONT)
        if not mode:
            break

        map_name = choose_map(window, MAPS, FONT, BIG_FONT)
        if not map_name:
            break

        new_game = game_loop(window, map_name, mode, FONT, BIG_FONT)

    pygame.quit()


if __name__ == '__main__':
    main()
