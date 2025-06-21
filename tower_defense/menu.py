import pygame
import os

from typing import Union
from settings import WIDTH, HEIGHT, WHITE, DARK_GRAY, BLACK, FONT


def choose_mode(win: pygame.Surface) -> Union[str, None]:
    """Funkcja pozwala na wybranie trybu gry."""
    options = ["Nieskończoność", "Kampania"]
    background = pygame.image.load(os.path.join("images", "menu.png")).convert()

    while True:
        win.blit(background, (0, 0))

        title_text = FONT.render("Wybierz tryb gry:", True, BLACK)
        win.blit(
            title_text,
            (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 + 20)
        )

        buttons = []
        for i, name in enumerate(options):
            rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60 + i * 60, 200, 40)
            buttons.append((rect, name))
            pygame.draw.rect(win, DARK_GRAY, rect)
            win.blit(
                FONT.render(name, True, WHITE),
                (rect.x + 20, rect.y + 10),
            )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for rect, name in buttons:
                    if rect.collidepoint(mx, my):
                        return name


def choose_map(win: pygame.Surface, maps: dict[str, list[tuple[int, int]]]) -> Union[list[tuple[int, int]], None]:
    """Funkcja pozwala na wybranie rodzaju mapy."""
    background = pygame.image.load(os.path.join("images", "menu.png")).convert()

    while True:
        win.blit(background, (0, 0))

        title_text = FONT.render("Wybierz mapę:", True, BLACK)
        win.blit(
            title_text,
            (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 + 20)
        )

        buttons = []
        for i, name in enumerate(maps.keys()):
            rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60 + i * 60, 200, 40)
            buttons.append((rect, name))
            pygame.draw.rect(win, DARK_GRAY, rect)
            win.blit(
                FONT.render(name, True, WHITE),
                (rect.x + 20, rect.y + 10)
            )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for rect, name in buttons:
                    if rect.collidepoint(mx, my):
                        return maps[name]
