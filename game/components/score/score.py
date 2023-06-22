import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, FONT_STYLE, FONT_SIZE, MENU1

class Score:
    def __init__(self, enemy_handler):
        
        self.enemy_handler = enemy_handler
        self.value = 0
        self.font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        self.color = WHITE
        self.x = 10
        self.y = 10

    def increase_score(self, points):
        self.value += points

    def draw(self, screen):
        score_text = self.font.render("Score: " + str(self.value), True, self.color)
        screen.blit(score_text, (self.x, self.y))

    def increase_score(self, points):
        self.value += points
        if self.value >= 600:
            self.enemy_handler.regenerate_enemies()
        elif self.value >= 250:
            self.enemy_handler.regenerate_enemies()
