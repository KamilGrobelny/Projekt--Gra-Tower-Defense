import pygame
from random import choice

from maps import MAPS
from settings import (
    WIDTH, HEIGHT, WHITE, DARK_GRAY, BLACK, FONT,
    STARTING_MONEY, TOWER_COST, TOWER_LEVEL_UP_COST, ENEMY_REWARD,
    FPS, TILE_SIZE, BASE_HP
)
from grid import draw_map_background, draw_sidebar, draw_grid, map_backgrounds, textures
from enemy import Enemy
from tower import Tower
from waves import WAVES

def button_rect(a):
    return pygame.Rect(10 + 130 * a, HEIGHT - 35, 120, 30)

def game_loop(win, path_tiles, mode):
    game_over_img = pygame.image.load("images/game_over.png").convert()
    game_won_img = pygame.image.load("images/game_won.png").convert()
    game_over_img = pygame.transform.scale(game_over_img, (WIDTH, HEIGHT))
    game_won_img = pygame.transform.scale(game_won_img, (WIDTH, HEIGHT))

    for key, val in MAPS.items():
        if path_tiles == val:
            map_name = key
            break
    else:
        map_name = list(MAPS.keys())[0]

    towers = []
    enemies = []
    dying_enemies = []
    selected_tile = None
    spawn_timer = 0

    tower_button = [button_rect(i) for i in range(4)]

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
        with open("best_time.txt", "r") as f:
            best_time_seconds = int(f.read())
    except:
        best_time_seconds = 0

    while run:
        clock.tick(FPS)
        win.fill(WHITE)

        if hp < 1:
            run = False
            win.blit(game_over_img, (0, 0))
            game_over_text = FONT.render('Game over', True, WHITE)
            win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 150))

            if mode == 'Nieskończoność':
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60
                record_minutes = best_time_seconds // 60
                record_seconds = best_time_seconds % 60

                time_text = FONT.render(
                    f"Czas: {minutes:02}:{seconds:02}  |  Rekord: {record_minutes:02}:{record_seconds:02}",
                    True, WHITE
                )
                win.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 200))

            back_button = pygame.Rect(WIDTH // 2 - 100, 280, 200, 40)
            pygame.draw.rect(win, DARK_GRAY, back_button)
            win.blit(FONT.render("Powrót do menu", True, WHITE), (back_button.x + 20, back_button.y + 10))

            pygame.display.update()

            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if back_button.collidepoint(mx, my):
                            return




        if current_wave >= len(WAVES[map_name]) and mode == 'Kampania':
            win.blit(game_won_img, (0, 0))
            game_win_text = FONT.render('You won!', True, WHITE)
            win.blit(game_win_text, (WIDTH // 2 - game_win_text.get_width() // 2, 150))

            back_button = pygame.Rect(WIDTH // 2 - 100, 220, 200, 40)
            pygame.draw.rect(win, DARK_GRAY, back_button)
            win.blit(FONT.render("Powrót do menu", True, WHITE), (back_button.x + 20, back_button.y + 10))

            pygame.display.update()
            run = False
            while not run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if back_button.collidepoint(mx, my):
                            return


        draw_map_background(win, map_name)
        draw_sidebar(win, textures)
        draw_grid(win, path_tiles, selected_tile)

        if mode == 'Nieskończoność':
            spawn = 120

            if survival_timer_active:
                survival_time_frames += 1
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60

                if total_seconds > best_time_seconds:
                    best_time_seconds = total_seconds
                    with open("best_time.txt", "w") as f:
                        f.write(str(best_time_seconds))
            else:
                total_seconds = survival_time_frames // FPS
                minutes = total_seconds // 60
                seconds = total_seconds % 60

            time_text = FONT.render(
                f"Czas: {minutes:02}:{seconds:02}  |  Rekord: {best_time_seconds // 60:02}:{best_time_seconds % 60:02}",
                True, BLACK
            )
            win.blit(time_text, (10, 5))

            if not wave_in_progress:
                wave_button = pygame.Rect(WIDTH // 2 - 60, 10, 120, 30)
                pygame.draw.rect(win, DARK_GRAY, wave_button)
                start_text = FONT.render("Start ", True, WHITE)
                win.blit(start_text, (WIDTH // 2 - 30, 15))
            else:
                spawn_timer += 1
                hp_increase_timer += 1
                if hp_increase_timer >= FPS * 10:
                    enemy_hp_multiplier *= 1.1
                    hp_increase_timer = 0

                if spawn_timer >= max(spawn, 10):
                    enemies.append(Enemy(path_tiles, choice(['small', 'normal', 'boss', 'fire', 'female', 'paker', 'skeleton', 'soldier']), hp_multiplier=enemy_hp_multiplier))
                    spawn_timer = 0
                    spawn -= 1

        if mode == 'Kampania':
            wave_text = FONT.render(f"Fala: {current_wave + 1}/{len(WAVES[map_name])}", True, BLACK)
            win.blit(wave_text, (10, 10))

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

            wave_button = pygame.Rect(WIDTH // 2 - 60, 10, 120, 30)
            pygame.draw.rect(win, DARK_GRAY, wave_button)
            wave_text = FONT.render("Start wave", True, WHITE)
            win.blit(wave_text, (WIDTH // 2 - 45, 15))

        hp_text = FONT.render(f"Zycie: {hp}", True, BLACK)
        win.blit(hp_text, (WIDTH - 100, 10))

        money_text = FONT.render(f"Pieniądze: {money}", True, BLACK)
        win.blit(money_text, (WIDTH - 290, 10))

        pygame.draw.rect(win, DARK_GRAY, button_rect(5))
        win.blit(FONT.render(f"Ulepszenie", True, WHITE), (667, HEIGHT - 30))

        for number in range(4):
            pygame.draw.rect(win, DARK_GRAY, tower_button[number])
            win.blit(FONT.render(f"Wieża {number + 1}", True, WHITE), (35 + 130 * number, HEIGHT - 30))

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
                hp = max(hp - enemy.damage, 0)

        for enemy in dying_enemies:
            if enemy.death(win):
                dying_enemies.remove(enemy)

        for tower in towers:
            tower.rotate(enemies)
            tower.draw(win)
            if tower.shoot(enemies):
                towers.remove(tower)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
                        tower_button[number].collidepoint(mx, my)
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
                    button_rect(5).collidepoint(mx, my)
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