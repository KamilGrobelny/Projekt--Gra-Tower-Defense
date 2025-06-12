import math
import pygame

from settings import TILE_SIZE, DARK_GRAY, TOWER_DATA, TOWER_LEVEL_UP_DATA


class Tower:
    def __init__(self, grid_x, grid_y, name):
        self.name = name
        self.x = grid_x * TILE_SIZE + TILE_SIZE // 2
        self.y = grid_y * TILE_SIZE + TILE_SIZE // 2
        self.timer = 0
        self.range = TOWER_DATA[name]['range']
        self.cooldown = TOWER_DATA[name]['cooldown']
        self.damage = TOWER_DATA[name]['damage']
        self.angle = 0
        self.orig_image = pygame.image.load(TOWER_DATA[name]['image'])
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.is_max_level = False

    def draw(self, win):
        image = self.image.get_rect()
        image_x = self.x - image.width // 2
        image_y = self.y - image.height // 2
        win.blit(self.image, (image_x, image_y))
        pygame.draw.circle(win, DARK_GRAY, (self.x, self.y), self.range, 1)

    def shoot(self, enemies):
        if self.timer > 0:
            self.timer -= 1
            return

        for enemy in enemies:
            if self.name == 3 or self.name == 4:
                break
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            if dist <= self.range:
                enemy.hp -= self.damage
                self.timer = self.cooldown
                break
        
        if self.name == 3:
            enemies_for_tower3 = []
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    enemies_for_tower3.append(enemy)
                
            for enemy in enemies_for_tower3:
                enemy.hp -= self.damage
            self.timer = self.cooldown

        tower4_shots = False
        
        if self.name == 4:
            enemies_for_tower4 = []
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= 25:
                    tower4_shots = True
                
            if tower4_shots:
                for enemy in enemies:
                    if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                        enemies_for_tower4.append(enemy)

                for enemy in enemies_for_tower4:
                    enemy.hp -= self.damage

        return tower4_shots

    def rotate(self, enemies):
        if self.name == 4:
            return

        for enemy in enemies:
            dist_x = enemy.x - self.x
            dist_y = enemy.y - self.y
            dist = math.hypot(dist_x, dist_y)
            if dist <= self.range:
                self.angle = math.degrees(math.atan2(-dist_y, dist_x)) - 90
                self.image = pygame.transform.rotate(self.orig_image, self.angle)
                break

    def level_up(self):
        self.range = TOWER_LEVEL_UP_DATA[self.name]['range']
        self.cooldown = TOWER_LEVEL_UP_DATA[self.name]['cooldown']
        self.damage = TOWER_LEVEL_UP_DATA[self.name]['damage']
        self.angle = 0
        self.orig_image = pygame.image.load(TOWER_LEVEL_UP_DATA[self.name]['image'])
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.is_max_level = True
