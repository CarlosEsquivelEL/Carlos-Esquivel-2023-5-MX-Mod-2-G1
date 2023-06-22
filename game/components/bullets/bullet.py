import pygame
from game.utils.constants import BULLET

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image_width = 20
        self.image_height = 20
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.top
        self.rect.x = self.rect.centerx
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Bullet_(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_width = 20
        self.image_height = 20
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.top
        self.rect.x = self.rect.centerx
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)