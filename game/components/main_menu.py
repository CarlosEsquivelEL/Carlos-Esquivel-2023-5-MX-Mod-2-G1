import pygame
import sys
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, FONT_STYLE, FONT_SIZE, MENU1

class MainMenu:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = MENU1
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(FONT_STYLE, FONT_SIZE)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_menu(self):
        self.window.blit(self.background_image, (0, 0))
        self.draw_text("Press any key", self.font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    def main_loop(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    running = False
                    self.game.run()

            self.draw_menu()
            pygame.display.update()
