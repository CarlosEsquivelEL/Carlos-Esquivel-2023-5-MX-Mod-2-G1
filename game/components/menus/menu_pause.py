import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE, MENU2

class PauseMenu:
    def __init__(self, game):
        self.game = game
        self.window = game.screen
        self.background_image = MENU2
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(FONT_STYLE, 60)
        self.button_font = pygame.font.Font(FONT_STYLE, 40)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_menu(self):
        self.window.blit(self.background_image, (0, 0))
        self.draw_text("Paused", self.font, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        pygame.draw.rect(self.window, (255, 255, 255), (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 25, 150, 50))
        self.draw_text("Resume", self.button_font, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.draw.rect(self.window, (255, 255, 255), (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 50, 150, 50))
        self.draw_text("Quit", self.button_font, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75)

    def main_loop(self):
        running = True
        paused = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if SCREEN_WIDTH // 2 - 75 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 75 and SCREEN_HEIGHT // 2 - 25 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 25:
                        running = False
                        paused = False
                    elif SCREEN_WIDTH // 2 - 75 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 75 and SCREEN_HEIGHT // 2 + 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 100:
                        pygame.quit()
                        quit()

            if not paused:
                break

            self.draw_menu()
            pygame.display.update()

        self.game.resume_game()
