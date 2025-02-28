import os
import sys
import pygame
import random
import csv

# Начальные параметры
WIDTH = 800
HEIGHT = 600
FPS = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FCOLOR = (243, 222, 211)
RECORD = 0


# загрузка изображения для спрайтов
def load_image(name, colorkey=None):
    # загружаем изображение из папки data
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


# класс финального окна
def end_screen(x):
    recs = []  # получаем имеющие записи о рекордах
    with open('records.csv', 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for rec in reader:
            recs = [int(i) for i in rec]

    # переписываем рекорд если он стал больше предыдущего
    with open('records.csv', 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if recs[x - 1] < RECORD:
            recs[x - 1] = RECORD
        writer.writerow(recs)
    intro_text = [str(RECORD), "Press ENTER to continue"]

    # Если игрок проиграл
    fon = pygame.transform.scale(load_image('game over.png'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 130
    temp = 400

    # выводим текст финишного окна
    for line in intro_text:
        string_rendered = font.render(line, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = temp
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        temp -= 210

    # если нажата enter выходим в главное меню
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
        pygame.display.flip()
        clock.tick(FPS)


# заставка игры
def first_screen():
    intro_text = ["Press any button to continue"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 550

    # выводим текст заставки
    for line in intro_text:
        string_rendered = font.render(line, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 270
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    # если нажата любая клавиша или мышка выходим в главное меню
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(FPS)


# стартовое окно
def start_window():
    intro_text = ["DOODLE PRYGAET"]
    nums = ["1", "2", "3", "4", "5"]
    image = pygame.Surface([800, 600])
    image.fill((243, 222, 211))

    fon = pygame.transform.scale(image, (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('Snap_ITC.ttf', 65)
    text_coord = 70

    # выводим описание игры
    for line in intro_text:
        string_rendered = font.render(line, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    # кнопки уровней
    pygame.draw.rect(screen, (146, 173, 117), (60, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (204, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (348, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (492, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (636, 300, 110, 110))

    text_coord = 100
    for n in nums:
        string_rendered = font.render(n, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 310
        intro_rect.x = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        text_coord += 55

    # получаем рекорды за каждый уровень
    with open('records.csv', 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        text_coord = 60
        font = pygame.font.Font(None, 30)
        for r in reader:

            # выводим рекорд за каждый уровень
            for j in r:
                string_rendered = font.render(j, 1, (19, 50, 21))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = 420
                intro_rect.x = text_coord
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                text_coord += 124

    # Выбор уровня
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                # определяем какой уровень выбран
                if 60 <= pos[0] <= 170 and 300 <= pos[1] <= 410:
                    return 1
                elif 204 <= pos[0] <= 314 and 300 <= pos[1] <= 410:
                    return 2
                elif 348 <= pos[0] <= 458 and 300 <= pos[1] <= 410:
                    return 3
                elif 492 <= pos[0] <= 602 and 300 <= pos[1] <= 410:
                    return 4
                elif 636 <= pos[0] <= 746 and 300 <= pos[1] <= 410:
                    return 5
        pygame.display.flip()
        clock.tick(FPS)


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, lvl):
        super().__init__()
        self.image_right = pygame.image.load('right.png').convert_alpha()
        self.image_left = pygame.image.load('left.png').convert_alpha()

        # По умолчанию используем изображение right.png
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2  # Положение по центру
        self.rect.bottom = HEIGHT - 50  # Положение внизу экрана
        self.speedy = 0  # Начальная скорость
        self.gravity = 0.1 + lvl * 0.05  # Гравитация
        self.speedx = 0  # Горизонтальная скорость
        self.level = lvl  # уровень игры

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.image = self.image_left  # Меняем изображение на left.png
            self.speedx = -10  # Движемся влево
        elif keys[pygame.K_RIGHT]:
            self.image = self.image_right  # Возвращаемся к right.png
        self.speedy += self.gravity  # Ускорение падения
        self.rect.y += self.speedy  # Перемещение по вертикали
        self.rect.x += self.speedx  # Перемещение по горизонтали

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        clock.tick(FPS)

        if self.rect.top >= HEIGHT:  # Если игрок падает ниже экрана
            self.kill()
            end_screen(self.level)  # Выходим в финальное окно
            return True


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
        # добавляем новый блок при передвижении персонажа(чтобы их было бесконечное количество)
        Block(self.group, self.clock)
        screen.fill(FCOLOR)
        self.group.update()  # обновляем пложение всех блоков
        clock.tick(FPS)
        return self


#Основные настройки игрового окна
def game_edit():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Doodle prygaet')
    pygame.display.update()
    clock = pygame.time.Clock()
    RECORD = 0
    return size, screen, clock, RECORD


if __name__ == '__main__':
    size, screen, clock, RECORD = game_edit()
    running = True
    # если заставка была закрыта
    if first_screen():

        # пока пользователь не закроет игру
        while running:
            size, screen, clock, RECORD = game_edit()

            # получаем уровень из стартового окна
            lvl = start_window()
            if lvl:
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
                player = Player(lvl)
                all_sprites.add(player)
                # спрайт фона игры (блоков)
                game = Display(platforms, clock)
                all_sprites.draw(screen)
                pygame.display.flip()
                finish = False

                # пока игрок не выйдет из финального окна продолжаем игру
                while not finish:
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player.speedx = -10  # Движение влево
                            elif event.key == pygame.K_RIGHT:
                                player.speedx = 10  # Движение вправо
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                player.speedx = 0

                    # получаем информацию о том, умер ли игрок
                    finish = player.update()
                    all_sprites.update()
                    # количество столкновений с блоками
                    hits = pygame.sprite.spritecollide(player, platforms, False)
                    # если сталкивается с блоком
                    if hits:
                        player.speedy = -10  # Прыжок

                        # если это не стартовый блок и игрок достиг линии обновления поля
                        if hits[0] != initial_platform and player.rect.top <= HEIGHT // 2 + 150:
                            RECORD += 1
                            game.update()  # двигаем блоки(продвигаем игрока вверх)
                    screen.fill(FCOLOR)
                    all_sprites.draw(screen)
                    platforms.draw(screen)
                    pygame.display.flip()
    pygame.quit()
