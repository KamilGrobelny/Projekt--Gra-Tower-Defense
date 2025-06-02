import pygame
from random import choice

from settings import (
    WIDTH, HEIGHT, WHITE, DARK_GRAY, FONT,
    STARTING_MONEY, TOWER_COST, ENEMY_REWARD
)
from grid import draw_grid
from enemy import Enemy
from tower import Tower

def button_rect(a):
    return pygame.Rect(10 + 130 * a, HEIGHT - 40, 120, 30)

def game_loop(win, path_tiles):
    towers1 = []
    towers2 = []
    towers3 = []
    towers4 = []
    towers = [
        towers1,
        towers2,
        towers3,
        towers4
    ]
    enemies = []
    dying_enemies = []
    selected_tile = None
    spawn_timer = 0
    tower_button = [
        button_rect(0),
        button_rect(1),
        button_rect(2),
        button_rect(3)
    ]
    clock = pygame.time.Clock()
    run = True
    money = STARTING_MONEY

    while run:
        clock.tick(60)
        win.fill(WHITE)
        spawn_timer += 1

        if spawn_timer >= 120:
            enemies.append(Enemy(path_tiles, choice(['small', 'normal', 'boss'])))
            spawn_timer = 0

        draw_grid(win, path_tiles, selected_tile)

        money_text = FONT.render(f"Pieniądze: {money}", True, DARK_GRAY)
        win.blit(money_text, (WIDTH - 180, HEIGHT - 35))

        for enemy in enemies:
            enemy.move()
            enemy.rotate()
            enemy.draw(win)

            if enemy.hp <= 0:
                money += ENEMY_REWARD.get(enemy.type)
                enemies.remove(enemy)
                dying_enemies.append(enemy)

            elif enemy.path_index >= len(enemy.path) - 1:
                enemies.remove(enemy)

        for enemy in dying_enemies:
            if enemy.death(win):
                dying_enemies.remove(enemy)

        for number in range(4):
            for tower in towers[number]:
                tower.draw(win, number + 1)
        
        for number in range(4):
            for tower in towers[number]:
                tower.shoot(enemies, number + 1)

        for number in range(4):
            pygame.draw.rect(win, DARK_GRAY, tower_button[number])
            win.blit(
                FONT.render(f"Wieża {number + 1}", True, WHITE),
                (35 + 130 * number, HEIGHT - 35),
            )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                for number in range(4):
                    condition = [
                        selected_tile not in path_tiles,
                        selected_tile not in path_tiles,
                        selected_tile not in path_tiles,
                        selected_tile in path_tiles
                    ]
                    if (
                        tower_button[number].collidepoint(mx, my)
                        and selected_tile
                        and condition[number]
                    ):
                        if all(
                            selected_tile != (tower.x // 50, tower.y // 50)
                            for tower in towers1 or towers2 or towers3 or towers4
                        ):
                            if money >= TOWER_COST:
                                towers[number].append(Tower(*selected_tile, number + 1))
                                money -= TOWER_COST
                                selected_tile = None

                    elif my < HEIGHT - 50:
                        grid_x, grid_y = mx // 50, my // 50
                        selected_tile = (grid_x, grid_y)
