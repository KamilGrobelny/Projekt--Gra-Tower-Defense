import math
import pygame

from settings import TILE_SIZE, DARK_GRAY


class Tower:
    def __init__(self, grid_x, grid_y):
        self.x = grid_x * TILE_SIZE + TILE_SIZE // 2
        self.y = grid_y * TILE_SIZE + TILE_SIZE // 2
        self.range = 100
        self.cooldown = 60
        self.timer = 0

    def draw(self, win):
        pygame.draw.circle(win, DARK_GRAY, (self.x, self.y), 15)
        pygame.draw.circle(win, DARK_GRAY, (self.x, self.y), self.range, 1)

    def shoot(self, enemies):
        if self.timer > 0:
            self.timer -= 1
            return

        for enemy in enemies:
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            if dist <= self.range:
                enemy.hp -= 10
                self.timer = self.cooldown
                break

