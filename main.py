import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Block(pygame.sprite.Sprite):
    image = pygame.Surface([100, 20])
    image.fill((255, 255, 255))

    def __init__(self, group, clock):
        super().__init__(group)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 350)
        self.rect.y = -100
        self.clock = clock
        all_sprites.draw(screen)

    def update(self):
        screen.fill('blue')
        if self.rect.y >= 800:
            del self
            return 0
        self.rect.y += 150
        return self


class Display(pygame.sprite.Sprite):

    def __init__(self, group, clock):
        super().__init__()
        Block(group, clock)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.group = all_sprites
        self.clock = clock

    def update(self):
        Block(all_sprites, self.clock)
        screen.fill('blue')
        all_sprites.update()
        clock.tick(10)
        return self


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game over')
    screen.fill('blue')
    pygame.display.update()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
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
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                game.update()
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]:
            game.update()
    pygame.quit()
