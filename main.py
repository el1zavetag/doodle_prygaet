import os
import sys
import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FCOLOR = WHITE


# загрузка изображения для спрайтов
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# закрытие игры
def terminate():
    pygame.quit()
    sys.exit()


# заставка игры
def first_screen():
    intro_text = ["Press any button to continue"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 550
    # выводим описание игры
    for line in intro_text:
        string_rendered = font.render(line, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 270
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(FPS)


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
        self.gravity = 0.2  # Гравитация
        self.speedx = 0  # Горизонтальная скорость

    def update(self):
        self.speedy += self.gravity  # Ускорение падения
        self.rect.y += self.speedy  # Перемещение по вертикали
        self.rect.x += self.speedx  # Перемещение по горизонтали

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        clock.tick(FPS)

        if self.rect.top > HEIGHT:  # Если игрок падает ниже экрана
            self.kill()


# спрайт одного блока
class Block(pygame.sprite.Sprite):
    # задаётся прямоугольником
    image = pygame.Surface([100, 20])
    image.fill(BLACK)

    def __init__(self, group, clock):
        super().__init__(group)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)  # рандомное значения по горизонтали
        self.rect.y = -100  # изначально блок находится в -100 координате по у
        self.clock = clock
        all_sprites.draw(screen)

    # передвижение блока на 100 пикс. ниже
    def update(self):
        screen.fill(FCOLOR)
        if self.rect.y >= HEIGHT:
            self.kill()  # когда доходит до края уничтожаем блок
            return 0
        self.rect.y += 100
        return self


# совокупность всех блоков
class Display(pygame.sprite.Sprite):

    def __init__(self, group, clock):
        super().__init__()
        Block(group, clock)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.group = group
        self.clock = clock

    def update(self):
        # добавляем новый юлок при передвижении персонажа(чтобы их бфло бесконечное количество)
        Block(self.group, self.clock)
        screen.fill(FCOLOR)
        self.group.update()  # обновляем пложение всех блоков
        clock.tick(FPS)
        return self


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Doodle prygaet')
    screen.fill(FCOLOR)
    pygame.display.update()
    clock = pygame.time.Clock()

    # если заставка была закрыта
    if first_screen():
        screen.fill(FCOLOR)
        pygame.display.update()
        # группа спрайтов игрока
        all_sprites = pygame.sprite.Group()
        # группа спрайтов блоков
        platforms = pygame.sprite.Group()
        # начальная платформа
        initial_platform = Block(platforms, clock)
        initial_platform.rect.x = WIDTH // 2
        initial_platform.rect.y = HEIGHT - 50
        # другие платформы начального экрана
        for i in range(5):
            p = Block(platforms, clock)
            p.rect.x = random.randrange(WIDTH - 50)
            p.rect.y = initial_platform.rect.y - 100 * (i + 1)
        # спрайт игрока
        player = Player()
        all_sprites.add(player)
        # спрайт фона игры (блоков)
        game = Display(platforms, clock)
        all_sprites.draw(screen)
        pygame.display.flip()
        running = True
        while running:
            pressed = pygame.key.get_pressed()
            all_sprites.draw(screen)
            pygame.display.flip()
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
            # если сталкивается с блоком
            if hits:
                player.speedy = -10  # Прыжок
                # если это не стартовый блок и игрок достиг середины экрана
                if hits[0] != initial_platform and player.rect.top <= HEIGHT // 2:
                    game.update()  # двигаем блоки(продвигаем игрока вверх)
            screen.fill(WHITE)
            all_sprites.draw(screen)
            platforms.draw(screen)
            pygame.display.flip()
        pygame.quit()
