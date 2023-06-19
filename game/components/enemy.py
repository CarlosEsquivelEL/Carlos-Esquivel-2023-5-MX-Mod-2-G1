import pygame
import random
from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.spaceship import Spaceship


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_width = 60
        self.image_height = 60
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)
    

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
           self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
           self.rect.y = random.randrange(-100, -40)
           self.speedy = random.randrange(1, 10)
           self.speedx = random.randrange(-5, 5)
   
    def draw(self, screen):
        screen.blit(self.image, self.rect)
