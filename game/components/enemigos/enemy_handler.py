import random
from game.components.enemigos.enemies import EnemyRed, EnemyBlue
from game.utils.constants import SCREEN_WIDTH

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.wave_count = 0

    def update(self):
        for enemy in self.enemies:
            enemy.update()

        if len(self.enemies) == 0:
            self.regenerate_enemies()

        self.update_bullets()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        self.draw_bullets(screen)

    def regenerate_enemies(self):
        self.wave_count += 1

        if self.wave_count == 1:
            self.generate_red_enemies(4)
        elif self.wave_count == 2:
            self.generate_red_enemies(10)
        elif self.wave_count == 3:
            self.generate_blue_enemies(6)
        elif self.wave_count == 4:
            self.generate_red_enemies(8)
            self.generate_blue_enemies(8)
        else:
            # Reset wave count and generate a new wave
            self.wave_count = 0
            self.regenerate_enemies()

    def generate_red_enemies(self, count):
        for _ in range(count):
            enemy = EnemyRed()
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.WIDTH)
            self.enemies.append(enemy)

    def generate_blue_enemies(self, count):
        for _ in range(count):
            enemy = EnemyBlue()
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.WIDTH)
            self.enemies.append(enemy)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot_bullets(self):
        for enemy in self.enemies:
            if random.randint(1, 50) == 1:
                bullet = enemy.shoot()
                self.bullets.append(bullet)
