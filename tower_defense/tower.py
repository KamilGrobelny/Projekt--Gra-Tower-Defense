import math
import pygame

from settings import TILE_SIZE, DARK_GRAY, RED, GREEN, BAR_WIDTH, BAR_HEIGHT, TOWER_DATA, TOWER_LEVEL_UP_DATA


class Tower:
    def __init__(self, grid_x, grid_y, name):
        self.x = grid_x * TILE_SIZE + TILE_SIZE // 2
        self.y = grid_y * TILE_SIZE + TILE_SIZE // 2
        self.timer = 0
        self.range = TOWER_DATA[name]['range']
        self.cooldown = TOWER_DATA[name]['cooldown']
        self.damage = TOWER_DATA[name]['damage']
        self.angle = 0
        self.orig_image = pygame.image.load(TOWER_DATA[name]['image'])
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        if name == 4:
            self.hp = TOWER_DATA[name]['hp']
            self.max_hp = TOWER_DATA[name]['hp']

    def draw(self, win, name):
        image = self.image.get_rect()
        image_x = self.x - image.width // 2
        image_y = self.y - image.height // 2
        win.blit(self.image, (image_x, image_y))
        pygame.draw.circle(win, DARK_GRAY, (self.x, self.y), self.range, 1)
        if name == 4:
            bar_x = self.x - BAR_WIDTH // 2
            bar_y = self.y - 25
            current_width = BAR_WIDTH * (self.hp / self.max_hp)
            pygame.draw.rect(win, RED, (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT))
            pygame.draw.rect(win, GREEN, (bar_x, bar_y, current_width, BAR_HEIGHT))

    def shoot(self, enemies, name):
        if self.timer > 0:
            self.timer -= 1
            return

        for enemy in enemies:
            if name == 3 or name == 4:
                break
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            if dist <= self.range:
                enemy.hp -= self.damage
                self.timer = self.cooldown
                break
        
        if name == 3:
            enemies_for_tower3 = []
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    enemies_for_tower3.append(enemy)
                
            for enemy in enemies_for_tower3:
                enemy.hp -= self.damage
            self.timer = self.cooldown

    def rotate(self, enemies):
        for enemy in enemies:
            dist_x = enemy.x - self.x
            dist_y = enemy.y - self.y
            dist = math.hypot(dist_x, dist_y)
            if dist <= self.range:
                self.angle = math.degrees(math.atan2(-dist_y, dist_x)) - 90
                self.image = pygame.transform.rotate(self.orig_image, self.angle)
                break

class Tower_level_up(Tower):
    def __init__(self, grid_x, grid_y, name):
        Tower.__init__(self, grid_x, grid_y, name)
        self.range = TOWER_LEVEL_UP_DATA[name]['range']
        self.cooldown = TOWER_LEVEL_UP_DATA[name]['cooldown']
        self.damage = TOWER_LEVEL_UP_DATA[name]['damage']
        self.angle = 0
        self.orig_image = pygame.image.load(TOWER_LEVEL_UP_DATA[name]['image'])
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        if name == 4:
            self.hp = TOWER_LEVEL_UP_DATA[name]['hp']
            self.max_hp = TOWER_LEVEL_UP_DATA[name]['hp']
