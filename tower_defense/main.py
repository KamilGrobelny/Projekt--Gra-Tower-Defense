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
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")

    new_game = True
    while new_game:
        mode = choose_mode(win)
        if not mode:
            break

        path = choose_map(win, MAPS)
        if not path:
            break

        new_game = game_loop(win, path, mode)

    pygame.quit()


if __name__ == "__main__":
    main()
