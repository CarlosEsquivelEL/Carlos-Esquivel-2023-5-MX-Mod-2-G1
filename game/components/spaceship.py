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
        self.screen = pygame.display.set_mode((1100, 600))
        self.rect.x = 300
        self.rect.y = 500
        self.speed_x = 5
        self.speed_y = 5
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

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

      self.rect.clamp_ip(self.screen.get_rect())