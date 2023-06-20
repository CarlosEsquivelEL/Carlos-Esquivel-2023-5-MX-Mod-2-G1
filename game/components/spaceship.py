import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP
from game.components.bullet import Bullet

class Spaceship(Sprite):
    def __init__(self):
        self.image_width = 40
        self.image_height = 60
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.screen = pygame.display.set_mode((1100, 600))
        self.rect.x = 300
        self.rect.y = 500
        self.speed_x = 5
        self.speed_y = 5
        self.bullets = []

    def update(self, events):
        if events[pygame.K_LEFT] and events[pygame.K_UP]:
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        elif events[pygame.K_LEFT] and events[pygame.K_DOWN]:
            self.rect.x -= self.speed_x
            self.rect.y += self.speed_y
        elif events[pygame.K_RIGHT] and events[pygame.K_UP]:
            self.rect.x += self.speed_x
            self.rect.y -= self.speed_y
        elif events[pygame.K_RIGHT] and events[pygame.K_DOWN]:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        elif events[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        elif events[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        elif events[pygame.K_UP]:
            self.rect.y -= self.speed_y
        elif events[pygame.K_DOWN]:
            self.rect.y += self.speed_y
        elif events[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet = Bullet()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.y = self.rect.y
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.clamp_ip(self.screen.get_rect())
