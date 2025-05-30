import pygame
import math
from settings import TILE_SIZE, RED, GREEN, BAR_WIDTH, BAR_HEIGHT


class Enemy:
    def __init__(self, path_coords):
        self.path = [
            (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)
            for x, y in path_coords
        ]
        self.x, self.y = self.path[0]
        self.path_index = 0
        self.speed = 1.5
        self.hp = 100

    def move(self):
        if self.path_index + 1 >= len(self.path):
            return 

        tx, ty = self.path[self.path_index + 1]
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)

        if dist < self.speed:
            self.x, self.y = tx, ty
            self.path_index += 1
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), 10)

        bar_x = self.x - BAR_WIDTH // 2
        bar_y = self.y - 20
        current_width = BAR_WIDTH * (self.hp / 100)
        
        pygame.draw.rect(win, RED, (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT))
        pygame.draw.rect(win, GREEN, (bar_x, bar_y, current_width, BAR_HEIGHT))
