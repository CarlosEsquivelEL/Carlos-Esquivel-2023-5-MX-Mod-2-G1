import pygame
from game.components.enemigos.enemy import Enemy
from game.components.enemigos.enemy_ import Enemy2
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyRed(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

class EnemyBlue(Enemy2):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)