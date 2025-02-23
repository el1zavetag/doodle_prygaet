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
def start_window():
    intro_text = ["DOODLE PRYGAET"]
    image = pygame.Surface([800, 600])
    image.fill((226, 247, 223))

    fon = pygame.transform.scale(image, (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('C:\\Users\\2V30\\PycharmProjects\\pythonProject8\\Sigmar-Regular.ttf', 70)
    text_coord = 50
    # выводим описание игры
    for line in intro_text:
        string_rendered = font.render(line, 1, (19, 50, 21))
        intro_rect = string_rendered.get_rect()
        print(intro_rect.width)
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 60
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.draw.rect(screen, (146, 173, 117), (60, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (204, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (348, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (492, 300, 110, 110))
    pygame.draw.rect(screen, (146, 173, 117), (636, 300, 110, 110))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if 60 <= pos[0] <= 170 and 300 <= pos[1] <= 410:
                    print('1')
                elif 204 <= pos[0] <= 314 and 300 <= pos[1] <= 410:
                    print('2')
                elif 348 <= pos[0] <= 458 and 300 <= pos[1] <= 410:
                    print('3')
                elif 492 <= pos[0] <= 602 and 300 <= pos[1] <= 410:
                    print('4')
                elif 636 <= pos[0] <= 746 and 300 <= pos[1] <= 410:
                    print('5')
        pygame.display.flip()
        clock.tick(FPS)

size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doodle prygaet')
screen.fill(FCOLOR)
pygame.display.update()
clock = pygame.time.Clock()
start_window()