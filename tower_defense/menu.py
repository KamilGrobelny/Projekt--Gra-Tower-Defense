import pygame
import os

from typing import Optional
from game import center_text
from settings import WIDTH, HEIGHT, WHITE, DARK_GRAY, BLACK


def choose_mode(
        window: pygame.Surface,
        FONT: pygame.font.Font,
        BIG_FONT: pygame.font.Font
        ) -> Optional[str]:
    """Funkcja pozwala na wybranie trybu gry."""
    options = ['Nieskończoność', 'Kampania']
    background = pygame.image.load(os.path.join('images', 'menu.png')).convert()

    while True:
        window.blit(background, (0, 0))

        title_text = BIG_FONT.render('Wybierz tryb gry:', True, BLACK)
        window.blit(
            title_text,
            (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 20)
        )

        buttons = []
        for i, name in enumerate(options):
            temp_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 60 + i*60, 200, 40)
            buttons.append((temp_rect, name))
            pygame.draw.rect(window, DARK_GRAY, temp_rect)
            window.blit(
                (text := FONT.render(name, True, WHITE)),
                center_text(text, temp_rect),
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


def choose_map(
        window: pygame.Surface,
        maps: dict[str, list[tuple[int, int]]],
        FONT: pygame.font.Font,
        BIG_FONT: pygame.font.Font
        ) -> Optional[str]:
    """Funkcja pozwala na wybranie rodzaju mapy."""
    background = pygame.image.load(os.path.join('images','menu.png')).convert()

    while True:
        window.blit(background, (0, 0))

        title_text = BIG_FONT.render('Wybierz mapę:', True, BLACK)
        window.blit(
            title_text,
            (WIDTH//2 - title_text.get_width()//2, HEIGHT//2 - 20)
        )

        buttons = []
        for i, name in enumerate(maps.keys()):
            temp_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 60 + i*60, 200, 40)
            buttons.append((temp_rect, name))
            pygame.draw.rect(window, DARK_GRAY, temp_rect)
            window.blit(
                (text := FONT.render(name, True, WHITE)),
                center_text(text, temp_rect),
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
