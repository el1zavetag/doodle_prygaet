import os
import sys
import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 60
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


def terminate():
    pygame.quit()
    sys.exit()


def first_screen():
    intro_text = ["Press any button to continue"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 500
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('green'))
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
            del self  # когда доходит до края уничтожаем блок
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
        self.group = all_sprites
        self.clock = clock

    def update(self):
        # добавляем новый юлок при передвижении персонажа(чтобы их бфло бесконечное количество)
        Block(all_sprites, self.clock)
        screen.fill(FCOLOR)
        all_sprites.update()  # обновляем пложение всех блоков
        clock.tick(10)
        return self


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Doodle prygaet')
    screen.fill(FCOLOR)
    pygame.display.update()
    clock = pygame.time.Clock()
    if first_screen():
        screen.fill(FCOLOR)
        pygame.display.update()
        # группа спрайтов для блоков
        all_sprites = pygame.sprite.Group()
        # спрайт фона игры
        game = Display(all_sprites, clock)
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
                # если нажали правую или левую стрелку меняем фон
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                    game.update()
            # если правая или левая кнопка зажаты меняем фон
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]:
                game.update()
        pygame.quit()
