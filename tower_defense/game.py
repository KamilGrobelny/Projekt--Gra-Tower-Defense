import pygame

from settings import (
    WIDTH, HEIGHT, WHITE, DARK_GRAY, FONT,
    STARTING_MONEY, TOWER1_COST, TOWER2_COST, TOWER3_COST, TOWER4_COST, ENEMY_REWARD,
)
from grid import draw_grid
from enemy import Enemy
from tower import Tower


def game_loop(win, path_tiles):
    towers = []
    enemies = []
    selected_tile = None
    spawn_timer = 0
    button_rect = pygame.Rect(10, HEIGHT - 40, 150, 30)
    clock = pygame.time.Clock()
    run = True
    money = STARTING_MONEY

    while run:
        clock.tick(60)
        win.fill(WHITE)
        spawn_timer += 1

        if spawn_timer >= 120:
            enemies.append(Enemy(path_tiles))
            spawn_timer = 0

        draw_grid(win, path_tiles, selected_tile)

        money_text = FONT.render(f"Pieniądze: {money}", True, DARK_GRAY)
        win.blit(money_text, (WIDTH - 180, HEIGHT - 35))

        for tower in towers:
            tower.draw(win)

        for enemy in enemies[:]:
            enemy.move()
            enemy.draw(win)

            if enemy.hp <= 0:
                money += ENEMY_REWARD
                enemies.remove(enemy)
            elif enemy.path_index >= len(enemy.path) - 1:
                enemies.remove(enemy)

        for tower in towers:
            tower.shoot(enemies)

        pygame.draw.rect(win, DARK_GRAY, button_rect)
        win.blit(
            FONT.render("Buduj wieżę", True, WHITE),
            (20, HEIGHT - 35),
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if (
                    button_rect.collidepoint(mx, my)
                    and selected_tile
                    and selected_tile not in path_tiles
                ):
                    if all(
                        selected_tile != (tower.x // 50, tower.y // 50)
                        for tower in towers
                    ):
                        if money >= TOWER1_COST:
                            towers.append(Tower(*selected_tile))
                            money -= TOWER1_COST
                            selected_tile = None

                elif my < HEIGHT - 50:
                    grid_x, grid_y = mx // 50, my // 50
                    if (grid_x, grid_y) not in path_tiles:
                        selected_tile = (grid_x, grid_y)
