import os
from sys import exit
import pygame
import numpy

pygame.init()
window = pygame.display.set_mode((500, 500))

class Cube(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(Cube, self).__init__()
        self.image = pygame.image.load(os.path.join('isometricCube', 'assets', 'cube.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass


main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(Cube.image, (10, 10))

    print('cube drawn?')

    pygame.display.flip()