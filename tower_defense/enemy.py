import pygame
import math
import random
from settings import TILE_SIZE, RED, GREEN, BAR_WIDTH, BAR_HEIGHT, ENEMY_DATA


class Enemy:
    def __init__(self, path_coords, enemy_type, hp_multiplier=1.0):
        offset = random.randint(-20, 20)
        self.path = [
            (x * TILE_SIZE + TILE_SIZE // 2 + offset, y * TILE_SIZE + TILE_SIZE // 2 + offset)
            for x, y in path_coords
        ]
        self.x, self.y = self.path[0]
        self.angle = -90
        self.path_index = 0
        self.speed = ENEMY_DATA[enemy_type]['speed']
        
        # Skalowanie HP
        base_hp = ENEMY_DATA[enemy_type]['hp']
        self.hp = int(base_hp * hp_multiplier)
        self.max_hp = int(base_hp * hp_multiplier)

        self.orig_image = pygame.image.load(ENEMY_DATA[enemy_type]['image']).convert_alpha()
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
    
        self.type = enemy_type
    
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
        win.blit(self.image, self.image_top_left_corner())

        bar_x = self.x - BAR_WIDTH // 2
        bar_y = self.y - 20
        current_width = BAR_WIDTH * (self.hp / self.max_hp)
        
        pygame.draw.rect(win, RED, (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT))
        pygame.draw.rect(win, GREEN, (bar_x, bar_y, current_width, BAR_HEIGHT))

    def rotate(self):
        if self.path_index + 1 >= len(self.path):
            return
        
        tx, ty = self.path[self.path_index + 1]
        move_vect = (tx - self.x, ty - self.y)

        self.angle = math.degrees(math.atan2(-move_vect[1], move_vect[0])) - 90
        self.image = pygame.transform.rotate(self.orig_image, self.angle)

    def image_top_left_corner(self):
        image = self.image.get_rect()
        image_x = self.x - image.width // 2
        image_y = self.y - image.height // 2
        return (image_x, image_y)
    
    def death(self, win, step=10):
        alpha = self.image.get_alpha()
        alpha = max(0, alpha - step)
        self.image.set_alpha(alpha)
        win.blit(self.image, self.image_top_left_corner())
        return alpha == 0
