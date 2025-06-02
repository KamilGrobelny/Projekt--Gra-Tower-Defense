import math
import pygame

from settings import TILE_SIZE, DARK_GRAY, RED, GREEN, BAR_WIDTH, BAR_HEIGHT


class Tower:
    def __init__(self, grid_x, grid_y, name):
        self.x = grid_x * TILE_SIZE + TILE_SIZE // 2
        self.y = grid_y * TILE_SIZE + TILE_SIZE // 2
        self.timer = 0
        if name == 1:
            self.range = 100
            self.cooldown = 60
            self.image = pygame.image.load("images/tower1.png")

        elif name == 2:
            self.range = 100
            self.cooldown = 100
            self.image = pygame.image.load("images/tower1.png")

        elif name == 3:
            self.range = 150
            self.cooldown = 110
            self.image = pygame.image.load("images/tower1.png")

        else:
            self.range = 0
            self.cooldown = 0
            self.image = pygame.image.load("images/tower1.png")
            self.hp = 100

    def draw(self, win, name):
        image = self.image.get_rect()
        image_x = self.x - image.width // 2
        image_y = self.y - image.height // 2
        win.blit(self.image, (image_x, image_y))
        pygame.draw.circle(win, DARK_GRAY, (self.x, self.y), self.range, 1)
        if name == 4:
            bar_x = self.x - BAR_WIDTH // 2
            bar_y = self.y - 25
            current_width = BAR_WIDTH * (self.hp / 100)
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
                if name == 2:
                    enemy.hp -= 10
                enemy.hp -= 10
                self.timer = self.cooldown
                break
        
        if name == 3:
            enemies_for_tower3 = []
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    enemies_for_tower3.append(enemy)
                
            for enemy in enemies_for_tower3:
                enemy.hp -= 10
            self.timer = self.cooldown
