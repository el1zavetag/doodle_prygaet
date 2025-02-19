import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Размер игрока
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2  # Положение по центру
        self.rect.bottom = HEIGHT - 50  # Положение внизу экрана
        self.speedy = 0  # Начальная скорость
        self.gravity = 0.6  # Гравитация
        self.speedx = 0  # Горизонтальная скорость

    def update(self):
        self.speedy += self.gravity  # Ускорение падения
        self.rect.y += self.speedy  # Перемещение по вертикали
        self.rect.x += self.speedx  # Перемещение по горизонтали

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top > HEIGHT:  # Если игрок падает ниже экрана
            self.kill()


# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 10))  # Размер
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Первая платформа
initial_platform = Platform(WIDTH // 2 - 50, HEIGHT - 40)
all_sprites.add(initial_platform)
platforms.add(initial_platform)

# Другие платформы
for i in range(5):
    p = Platform(random.randrange(WIDTH - 100), initial_platform.rect.y - 150 * (i + 1))
    all_sprites.add(p)
    platforms.add(p)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx = -10  # Движение влево
            elif event.key == pygame.K_RIGHT:
                player.speedx = 10  # Движение вправо
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speedx = 0

    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.speedy = -15  # Прыжок

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
