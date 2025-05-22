import pygame

from settings import WIDTH, HEIGHT
from maps import MAPS
from menu import choose_map, choose_mode
from game import game_loop


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")

    mode = choose_mode(win)
    if not mode:
        return

    path = choose_map(win, MAPS)
    if path:
        game_loop(win, path)


if __name__ == "__main__":
    main()
