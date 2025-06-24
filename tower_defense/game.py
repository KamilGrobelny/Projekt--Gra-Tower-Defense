import pygame
import os
from random import choice

import pygame

from maps import MAPS
from settings import (
    WIDTH, HEIGHT, WHITE, DARK_GRAY, BLACK, TILE_SIZE,
    STARTING_MONEY, TOWER_COST, TOWER_LEVEL_UP_COST, ENEMY_REWARD,
    FPS, SPEED_UP_FPS, BASE_HP, MAX_SPAWN_INTERVAL, MIN_SPAWN_INTERVAL
    )
from grid import (
    draw_map_background, draw_sidebar, draw_grid, load_ui_textures,
    load_map_backgrounds
    )
from enemy import Enemy
from tower import Tower
from waves import WAVES

def button_rect(a: int) -> pygame.Rect:
    """Zwraca prostokąt (przycisk) dla wież oraz ulepszenia."""
    return pygame.Rect(10 + 130 * a, HEIGHT - 35, 120, 30)

def center_text(text: pygame.Surface, box: pygame.Rect) -> tuple[int, int]:
    """Zwraca współrzędne przy których tekst będzie wyśrodkowany"""
    return (
        box.centerx - text.get_width()//2,
        box.centery - text.get_height()//2
        )


def game_loop(
        window: pygame.Surface,
        map_name: str,
        mode: str,
        FONT: pygame.font.Font,
        BIG_FONT: pygame.font.Font
        ) -> bool:
    """
    Główna pętla gry.

    Atrybuty:
        window: Powierzchnia do rysowania
        map_name: nazwa aktualnej mapy
        mode: tryb gry

    Zwraca:
        bool: True: gracz wrócił do menu, False: zakończył grę.
    """

    game_over_img = pygame.image.load(os.path.join('images', 'game_over.png')).convert()
    game_won_img = pygame.image.load(os.path.join('images', 'game_won.png')).convert()
    game_over_img = pygame.transform.scale(game_over_img, (WIDTH, HEIGHT))
    game_won_img = pygame.transform.scale(game_won_img, (WIDTH, HEIGHT))

    textures = load_ui_textures()
    map_backgrounds = load_map_backgrounds()

    path_tiles = MAPS[map_name]

    towers = []
    enemies = []
    dying_enemies = []
    selected_tile = None
    spawn_timer = 0
    spawn_interval = MAX_SPAWN_INTERVAL
    current_fps = FPS

    tower_buttons = [button_rect(i) for i in range(4)]

    clock = pygame.time.Clock()
    run = True
    money = STARTING_MONEY

    current_wave = 0
    wave_in_progress = False
    wave_timer = 0
    enemy_spawn_index = 0
    time_between_spawns = 30
    hp = BASE_HP
    enemy_hp_multiplier = 1.0
    hp_increase_timer = 0

    survival_time_frames = 0                   
    survival_timer_active = False             

    try:
        with open('best_time.txt', 'r') as f:
            best_time_seconds = int(f.read())
    except FileNotFoundError:
        best_time_seconds = 0

    while run:
        clock.tick(current_fps)
        window.fill(WHITE)

        if hp <= 0:
            run = False
            window.blit(game_over_img, (0, 0))
            game_over_text = BIG_FONT.render('Game over', True, WHITE)
            window.blit(game_over_text,
                        (WIDTH//2 - game_over_text.get_width()//2, 140))

            if mode == 'Nieskończoność':
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60
                record_minutes = best_time_seconds // 60
                record_seconds = best_time_seconds % 60

                time_text = FONT.render(
                    f'Czas: {minutes:02}:{seconds:02}  |  Rekord: '
                    f'{record_minutes:02}:{record_seconds:02}',
                    True, WHITE
                )
                window.blit(time_text, 
                            (WIDTH//2 - time_text.get_width()//2, 200))

            back_button = pygame.Rect(WIDTH//2 - 100, 280, 200, 40)
            pygame.draw.rect(window, DARK_GRAY, back_button)
            window.blit(
                (text:=FONT.render('Powrót do menu', True, WHITE)),
                center_text(text, back_button)
                )

            pygame.display.update()

            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if back_button.collidepoint(mx, my):
                            return True

        if current_wave >= len(WAVES[map_name]) and mode == 'Kampania':
            window.blit(game_won_img, (0, 0))
            game_win_text = BIG_FONT.render('You won!', True, WHITE)
            window.blit(game_win_text, 
                        (WIDTH//2 - game_win_text.get_width()//2, 150))

            back_button = pygame.Rect(WIDTH//2 - 100, 220, 200, 40)
            pygame.draw.rect(window, DARK_GRAY, back_button)
            window.blit(FONT.render('Powrót do menu', True, WHITE), 
                        (back_button.x + 20, back_button.y + 10))

            pygame.display.update()
            run = False
            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if back_button.collidepoint(mx, my):
                            return True

        draw_map_background(window, map_name, map_backgrounds)
        draw_sidebar(window, textures)
        draw_grid(window, selected_tile)

        if mode == 'Nieskończoność':

            if survival_timer_active:
                survival_time_frames += 1
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60

                if total_seconds > best_time_seconds:
                    best_time_seconds = total_seconds
                    with open('best_time.txt', 'w') as f:
                        f.write(str(best_time_seconds))
            else:
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60

            time_text = FONT.render(
                f'Czas: {minutes:02}:{seconds:02}  |  Rekord: '
                f'{best_time_seconds // 60:02}:{best_time_seconds % 60:02}',
                True, BLACK
                )
            window.blit(time_text, (10, 10))

            if not wave_in_progress:
                wave_button = pygame.Rect(WIDTH // 2 - 60, 5, 120, 30)
                pygame.draw.rect(window, DARK_GRAY, wave_button)
                start_text = FONT.render('Start ', True, WHITE)
                window.blit(start_text, center_text(start_text, wave_button))
            else:
                spawn_timer += 1
                hp_increase_timer += 1
                if hp_increase_timer >= FPS * 10:
                    enemy_hp_multiplier *= 1.1
                    hp_increase_timer = 0

                if spawn_timer >= max(spawn_interval, MIN_SPAWN_INTERVAL):
                    enemy_choice = choice([
                        'small', 'normal', 'boss', 'fire','female', 'paker',
                        'skeleton', 'soldier'
                        ])
                    enemies.append(Enemy(
                        path_tiles, enemy_choice, 
                        hp_multiplier=enemy_hp_multiplier
                        ))
                    spawn_timer = 0
                    spawn_interval -= 1

        elif mode == 'Kampania':
            wave_text = FONT.render(
                f'Fala: {current_wave + 1}/{len(WAVES[map_name])}', True, BLACK
                )
            window.blit(wave_text, (10, 10))

            if wave_in_progress and current_wave < len(WAVES[map_name]):
                wave = WAVES[map_name][current_wave]
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

            wave_button = pygame.Rect(WIDTH//2 - 90, 5, 180, 30)
            pygame.draw.rect(window, DARK_GRAY, wave_button)
            wave_text = FONT.render('Rozpocznij falę', True, WHITE)
            window.blit(wave_text, center_text(wave_text, wave_button))

        hp_text = FONT.render(f'Życie: {hp}', True, BLACK)
        window.blit(hp_text, (WIDTH - 100, 10))

        money_text = FONT.render(f'Pieniądze: {money}', True, BLACK)
        window.blit(money_text, (WIDTH - 290, 10))

        upgrade_button = button_rect(5)
        pygame.draw.rect(window, DARK_GRAY, upgrade_button)
        upgrade_text = FONT.render(f'Ulepszenie', True, WHITE)
        window.blit(upgrade_text, center_text(upgrade_text, upgrade_button))

        for number in range(4):
            pygame.draw.rect(window, DARK_GRAY, tower_buttons[number])
            window.blit(FONT.render(f'Wieża {number + 1}', True, WHITE), (35 + 130*number, HEIGHT - 30))

        for enemy in enemies:
            enemy.move()
            enemy.rotate()
            enemy.draw(window)

            if enemy.hp <= 0:
                money += ENEMY_REWARD.get(enemy.type)
                enemies.remove(enemy)
                dying_enemies.append(enemy)
            elif enemy.path_index >= len(enemy.path) - 1:
                enemies.remove(enemy)
                hp = max(hp - enemy.damage, 0)

        for enemy in dying_enemies:
            if enemy.death(window):
                dying_enemies.remove(enemy)
            window.blit(
                FONT.render(f'+{ENEMY_REWARD[enemy.type]}', True, WHITE),
                (enemy.x - 15, enemy.y - 25)
                )

        for tower in towers:
            tower.rotate(enemies)
            tower.draw(window)
            if tower.shoot(enemies):
                towers.remove(tower)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if not wave_in_progress:
                    if wave_button.collidepoint(mx, my):
                        wave_in_progress = True
                        if mode == 'Nieskończoność':
                            survival_timer_active = True  

                for number in range(4):
                    condition = [
                        selected_tile not in path_tiles,
                        selected_tile not in path_tiles,
                        selected_tile not in path_tiles,
                        selected_tile in path_tiles
                    ]

                    if (
                        tower_buttons[number].collidepoint(mx, my)
                        and selected_tile
                        and condition[number]
                    ):
                        if all(
                            selected_tile != (tower.x // TILE_SIZE, tower.y // TILE_SIZE)
                            for tower in towers
                        ):
                            if money >= TOWER_COST:
                                towers.append(Tower(*selected_tile, number + 1))
                                money -= TOWER_COST
                                selected_tile = None

                if (
                    upgrade_button.collidepoint(mx, my)
                    and selected_tile
                ):
                    for tower in towers:
                        if (
                            selected_tile == (tower.x // TILE_SIZE, tower.y // TILE_SIZE)
                            and not tower.is_max_level
                            and money >= TOWER_LEVEL_UP_COST
                        ):
                            tower.level_up()
                            money -= TOWER_LEVEL_UP_COST
                            selected_tile = None
                            break

                elif my < HEIGHT - TILE_SIZE:
                    grid_x, grid_y = mx // TILE_SIZE, my // TILE_SIZE
                    if TILE_SIZE <= my < HEIGHT - TILE_SIZE:
                        selected_tile = (grid_x, grid_y)
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_fps = SPEED_UP_FPS
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    current_fps = FPS
