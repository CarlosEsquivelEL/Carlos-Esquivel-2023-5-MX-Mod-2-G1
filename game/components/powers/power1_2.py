import pygame
from game.components.powers.powerss import Power
from game.utils.constants import HEART, SHIELD, SPACESHIP_SHIELD


class Life(Power):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self):
        self.image = HEART
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

class Shield(Power):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self):
        self.image = SHIELD
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
