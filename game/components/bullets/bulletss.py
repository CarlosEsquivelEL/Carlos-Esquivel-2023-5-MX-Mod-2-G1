import pygame
from game.components.bullets.bullet import Bullet, Bullet_
from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY2

class BulletE(Bullet):
    WIDTH = 20
    HEIGHT = 20

    def __init__(self):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    
class BulletE2(Bullet):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self):
        self.image = BULLET_ENEMY2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
