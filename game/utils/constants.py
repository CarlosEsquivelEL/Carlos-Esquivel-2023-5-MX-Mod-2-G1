import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Spaceship/spaceship_shield.png'))
MENU1 = pygame.image.load(os.path.join(IMG_DIR, "MENU/MENU1.png"))
MENU2 = pygame.image.load(os.path.join(IMG_DIR, "MENU/MENU2.jpg"))
MENU3 = pygame.image.load(os.path.join(IMG_DIR, "MENU/MENU3.jpg"))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY2 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
SPACESHIP_SHIELD_WIDTH = 60
SPACESHIP_SHIELD_HEIGHT = 80
SPACESHIP_SHIELD = pygame.transform.scale(SPACESHIP_SHIELD, (SPACESHIP_SHIELD_WIDTH, SPACESHIP_SHIELD_HEIGHT))
FONT_STYLE = 'freesansbold.ttf'
FONT_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)