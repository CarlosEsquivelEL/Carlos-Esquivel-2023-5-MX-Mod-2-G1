import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, FONT_STYLE, FONT_SIZE

class Score:
    def __init__(self):
        self.value = 0
        self.max_score = self.load_max_score()
        self.enemies_eliminated = 0
        self.font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        self.color = WHITE
        self.x = 10
        self.y = 10

    def reset(self):
        self.value = 0
        self.enemies_eliminated = 0

    def increase_score(self, points):
        self.value += points

    def increase_enemies_eliminated(self):
        self.enemies_eliminated += 1

    def update_max_score(self):
        if self.value > self.max_score:
            self.max_score = self.value

    def draw(self, screen):
        score_text = self.font.render("Score: " + str(self.value), True, self.color)
        screen.blit(score_text, (self.x, self.y))

        enemies_eliminated_text = self.font.render("Enemies Eliminated: " + str(self.enemies_eliminated), True, self.color)
        screen.blit(enemies_eliminated_text, (self.x, self.y + 30))

    def draw_max_score(self, screen):
        max_score_text = self.font.render("Max Score: " + str(self.max_score), True, self.color)
        screen.blit(max_score_text, (self.x, self.y + 60))

    def load_max_score(self):
        try:
            with open('max_score.txt', 'r') as file:
                max_score = int(file.read())
        except FileNotFoundError:
            max_score = 0
        return max_score

    def save_max_score(self):
        with open('max_score.txt', 'w') as file:
            file.write(str(self.max_score))
