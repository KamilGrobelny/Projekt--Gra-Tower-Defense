import unittest
from unittest.mock import patch, MagicMock
import pygame
from enemy import Enemy
from settings import TILE_SIZE, TOWER_LEVEL_UP_DATA
from tower import Tower
import grid


class TestEnemy(unittest.TestCase):
    @patch('pygame.transform.rotate')
    @patch('pygame.image.load')
    def setUp(self, mock_load, mock_rotate):
        pygame.init()

        dummy_surface = pygame.Surface((40, 40), pygame.SRCALPHA)

        mock_image = MagicMock()
        mock_image.convert_alpha.return_value = dummy_surface
        mock_load.return_value = mock_image

        mock_rotate.return_value = dummy_surface

        self.mock_image = dummy_surface
        self.path_coords = [(1, 1), (2, 1)]
        self.enemy = Enemy(self.path_coords, 'normal', hp_multiplier=1.0)

    def test_initial_position(self):
        self.assertEqual(self.enemy.path_index, 0)
        self.assertEqual(self.enemy.hp, 100)
        self.assertEqual(self.enemy.damage, 2)

    def test_move_increases_path_index(self):
        self.enemy.speed = 1000  
        self.enemy.move()
        self.assertEqual(self.enemy.path_index, 1)

    def test_rotation_angle(self):
        self.enemy.rotate()
        self.assertIsInstance(self.enemy.angle, float)

    def test_death_fade(self):

        mock_surface = MagicMock()
        mock_surface.get_alpha.return_value = 5
        mock_surface.set_alpha.return_value = None

        self.enemy.image = mock_surface

        window = MagicMock()
        done = self.enemy.death(window, step=10)

        self.assertTrue(done)
    
class TestTower(unittest.TestCase):
    def setUp(self):
        self.grid_x = 1
        self.grid_y = 2
        self.tower_type = 1

        self.patcher_img = patch('pygame.image.load', return_value=MagicMock())
        self.mock_img = self.patcher_img.start()

        self.patcher_rot = patch('pygame.transform.rotate', return_value=MagicMock())
        self.mock_rot = self.patcher_rot.start()

        self.tower = Tower(self.grid_x, self.grid_y, self.tower_type)

    def tearDown(self):
        self.patcher_img.stop()
        self.patcher_rot.stop()

    def test_initial_position(self):
        expected_x = self.grid_x * TILE_SIZE + TILE_SIZE // 2
        expected_y = self.grid_y * TILE_SIZE + TILE_SIZE // 2
        self.assertEqual(self.tower.x, expected_x)
        self.assertEqual(self.tower.y, expected_y)

    def test_level_up_range(self):
        self.tower.level_up()
        self.assertTrue(self.tower.is_max_level)
        self.assertEqual(self.tower.range, TOWER_LEVEL_UP_DATA[self.tower_type]['range']) 

    def test_level_up_cooldown(self):
        self.tower.level_up()
        self.assertTrue(self.tower.is_max_level)
        self.assertEqual(self.tower.cooldown, TOWER_LEVEL_UP_DATA[self.tower_type]['cooldown']) 

    def test_level_up_damage(self):
        self.tower.level_up()
        self.assertTrue(self.tower.is_max_level)
        self.assertEqual(self.tower.damage, TOWER_LEVEL_UP_DATA[self.tower_type]['damage'])          

    def test_shoot_single_target(self):
        enemy = MagicMock()
        enemy.x = self.tower.x
        enemy.y = self.tower.y
        enemy.hp = 100
        self.tower.shoot([enemy])
        self.assertLess(enemy.hp, 100)

    def test_rotate_faces_enemy(self):
        enemy = MagicMock()
        enemy.x = self.tower.x + 10
        enemy.y = self.tower.y
        self.tower.rotate([enemy])
        self.mock_rot.assert_called()

class TestInteractions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1)) 

    def setUp(self):
       
        self.tower = Tower(grid_x=5, grid_y=5, tower_type=1)
        self.enemy = Enemy([(0, 0), (10, 10)], 'normal', hp_multiplier=1.0)
        self.enemy.x = self.tower.x  
        self.enemy.y = self.tower.y

    def test_tower_damages_enemy(self):
        original_hp = self.enemy.hp
        self.tower.timer = 0  
        self.tower.shoot([self.enemy])
        self.assertLess(self.enemy.hp, original_hp)

    def test_tower_respects_cooldown(self):
        self.tower.timer = 5
        original_hp = self.enemy.hp
        self.tower.shoot([self.enemy])
        self.assertEqual(self.enemy.hp, original_hp)  

    def test_tower_only_hits_in_range(self):
        self.enemy.x += 999 
        original_hp = self.enemy.hp
        self.tower.timer = 0
        self.tower.shoot([self.enemy])
        self.assertEqual(self.enemy.hp, original_hp)

    def test_tower_rotates_to_enemy(self):
        initial_angle = self.tower.angle
        self.tower.rotate([self.enemy])
        self.assertNotEqual(self.tower.angle, initial_angle)

    def test_tower4_explodes(self):
        
        tower4 = Tower(grid_x=5, grid_y=5, tower_type=4)
        self.enemy.x = tower4.x
        self.enemy.y = tower4.y
        result = tower4.shoot([self.enemy])
        self.assertTrue(result)

    def test_tower4_does_not_explode_when_enemy_far(self):
        tower4 = Tower(grid_x=5, grid_y=5, tower_type=4)
        self.enemy.x += 999
        self.enemy.y += 999
        result = tower4.shoot([self.enemy])
        self.assertFalse(result)   

class TestEnemyTypes(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1, 1))

    def test_fast_enemy_moves_more(self):
        fast = Enemy([(0, 0), (100, 0)], 'small', hp_multiplier=1.0)
        slow = Enemy([(0, 0), (100, 0)], 'boss', hp_multiplier=1.0)

        for _ in range(10):
            fast.move()
            slow.move()

        self.assertGreater(fast.x, slow.x)

    def test_high_hp_enemy_takes_longer_to_die(self):
        boss = Enemy([(0, 0), (100, 0)], 'boss', hp_multiplier=1.0)
        fire = Enemy([(0, 0), (100, 0)], 'fire', hp_multiplier=1.0)


        boss.hp -= 50
        fire.hp -= 50

        self.assertGreater(boss.hp, 0)
        self.assertLessEqual(fire.hp, 0)

    def test_damage_values_correct(self):
        paker = Enemy([(0, 0), (100, 0)], 'paker', hp_multiplier=1.0)
        fire = Enemy([(0, 0), (100, 0)], 'fire', hp_multiplier=1.0)

        self.assertGreater(paker.damage, fire.damage)

    
    
if __name__ == '__main__':
    unittest.main()