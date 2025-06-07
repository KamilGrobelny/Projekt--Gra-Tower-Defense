import pygame
from random import choice

from maps import MAPS
from settings import (
    WIDTH, HEIGHT, WHITE, DARK_GRAY, FONT,
    STARTING_MONEY, TOWER_COST, ENEMY_REWARD,
    FPS, TILE_SIZE, BASE_HP
)
from grid import draw_grid
from enemy import Enemy
from tower import Tower
from waves import WAVES


def button_rect(a):
    return pygame.Rect(10 + 130 * a, HEIGHT - 40, 120, 30)


def game_loop(win, path_tiles, mode):
    for key, val in MAPS.items():
        if path_tiles == val:
            map = key

    towers = []
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

    current_wave = 0
    wave_in_progress = False
    wave_timer = 0
    enemy_spawn_index = 0
    time_between_spawns = 30
    hp = BASE_HP

    while run:
        clock.tick(FPS)
        win.fill(WHITE)

        if hp < 1:
            run = False
            game_over_text = FONT.render('Game over', True, WHITE)
            win.fill('GRAY')
            win.blit(
                game_over_text,
                (WIDTH // 2 - game_over_text.get_width() // 2, 150)
            )
            pygame.display.update()
            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        if current_wave >= len(WAVES[map]) and mode == 'Kampania':
            game_win_text = FONT.render('You won', True, WHITE)
            win.fill('GRAY')
            win.blit(
                game_win_text,
                (WIDTH // 2 - game_win_text.get_width() // 2, 150)
            )
            pygame.display.update()
            run = False
            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        draw_grid(win, path_tiles, selected_tile)

        if mode == 'Nieskończoność':
            spawn = 120

            if not wave_in_progress:
                wave_button = pygame.Rect(WIDTH // 2 - 60, 10, 120, 30)
                pygame.draw.rect(win, DARK_GRAY, wave_button)
                start_text = FONT.render("Start ", True, WHITE)
                win.blit(start_text, (WIDTH // 2 - 30, 15))
            else:
                spawn_timer += 1

                if spawn_timer >= max(spawn, 10):
                    enemies.append(
                        Enemy(path_tiles, choice(['small', 'normal', 'boss']))
                    )
                    spawn_timer = 0
                    spawn -= 1

        if mode == 'Kampania':
            wave_text = FONT.render(
                f"Fala: {current_wave + 1}/{len(WAVES[map])}", True, DARK_GRAY
            )
            win.blit(wave_text, (10, 10))

            if wave_in_progress and current_wave < len(WAVES[map]):
                wave = WAVES[map][current_wave]
                if enemy_spawn_index < sum(count for _, count in wave):
                    wave_timer += 1
                    if wave_timer >= time_between_spawns:
                        total_spawned = 0
                        for enemy_type, count in wave:
                            if enemy_spawn_index < total_spawned + count:
                                enemies.append(Enemy(path_tiles, enemy_type))
                                break
                            total_spawned += count

                        enemy_spawn_index += 1
                        wave_timer = 0
                elif not enemies:
                    wave_in_progress = False
                    enemy_spawn_index = 0
                    current_wave += 1

            wave_button = pygame.Rect(WIDTH // 2 - 60, 10, 120, 30)
            pygame.draw.rect(win, DARK_GRAY, wave_button)
            wave_text = FONT.render("Start wave", True, WHITE)
            win.blit(wave_text, (WIDTH // 2 - 45, 10))

        hp_text = FONT.render(f"Zycie: {hp}", True, DARK_GRAY)
        win.blit(hp_text, (WIDTH - 180, 10))

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
                hp -= 1
                if enemy.type == 'Boss':
                    hp -= 4

        for enemy in dying_enemies:
            if enemy.death(win):
                dying_enemies.remove(enemy)

        for tower in towers:
            tower.rotate(enemies)
            tower.draw(win)
            tower.shoot(enemies)

        for number in range(4):
            pygame.draw.rect(win, DARK_GRAY, tower_button[number])
            win.blit(
                FONT.render(f"Wieża {number + 1}", True, WHITE),
                (35 + 130 * number, HEIGHT - 35)
            )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if not wave_in_progress and current_wave < len(WAVES[map]):
                    if wave_button.collidepoint(mx, my):
                        wave_in_progress = True

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
                            selected_tile != (
                                tower.x // TILE_SIZE, tower.y // TILE_SIZE
                            )
                            for tower in towers
                        ):
                            if money >= TOWER_COST:
                                towers.append(
                                    Tower(*selected_tile, number + 1)
                                )
                                money -= TOWER_COST
                                selected_tile = None

                        for tower in towers:
                            if (
                                selected_tile == (
                                    tower.x // TILE_SIZE, tower.y // TILE_SIZE
                                )
                                and not tower.is_max_level
                            ):
                                if money >= TOWER_COST:
                                    tower.level_up()
                                    money -= TOWER_COST
                                    selected_tile = None
                                    break

                    elif my < HEIGHT - TILE_SIZE:
                        grid_x, grid_y = mx // TILE_SIZE, my // TILE_SIZE
                        selected_tile = (grid_x, grid_y)
