import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image_widht = 40
        self.image_height = 60
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_widht, self.image_height))
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(sel, keyboard_events):
        pass