import pygame
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bulletss import BulletE

class Enemy(pygame.sprite.Sprite):
    width = 500

    def __init__(self, image):
        super().__init__()
        self.image_width = 60
        self.image_height = 60
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)
        self.shoot_timer = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
           self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
           self.rect.y = random.randrange(-100, -40)
           self.speedy = random.randrange(1, 10)
           self.speedx = random.randrange(-5, 5)

        self.shoot_timer += 1  
        if self.shoot_timer >= 180:
            self.shoot()
            self.shoot_timer = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        bullet = BulletE()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.bottom
        return bullet
