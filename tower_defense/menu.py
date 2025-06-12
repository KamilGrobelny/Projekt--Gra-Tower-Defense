import pygame

from settings import WIDTH, WHITE, DARK_GRAY, FONT


def choose_mode(win):
    options = ["Nieskończoność", "Kampania"]

    while True:
        win.fill(WHITE)
        win.blit(
            FONT.render("Wybierz tryb gry:", True, DARK_GRAY),
            (WIDTH // 2 - 80, 40),
        )

        buttons = []
        for i, name in enumerate(options):
            rect = pygame.Rect(WIDTH // 2 - 100, 100 + i * 60, 200, 40)
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


def choose_map(win, maps):
    while True:
        win.fill(WHITE)
        win.blit(
            FONT.render("Wybierz mapę:", True, DARK_GRAY),
            (WIDTH // 2 - 60, 40),
        )

        buttons = []
        for i, name in enumerate(maps.keys()):
            rect = pygame.Rect(WIDTH // 2 - 100, 100 + i * 60, 200, 40)
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
                        return maps[name]
