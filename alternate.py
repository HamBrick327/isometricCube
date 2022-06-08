import os
from sys import exit
import pygame
import numpy

pygame.init()
window = pygame.display.set_mode((500, 500))
cube = pygame.image.load(os.path.join('isometricCube', 'assets', 'cube.png'))


'''
class Cube(pygame.sprite.Sprite):
    def __init__(self):
    
    def draw(self, x, y): #prolly not right but idk. worried about the self argument inside the function
        window.blit(self.image, (x, y))

    def update(self):
        pass
'''

def draw(image, x, y):
    window.blit(image, (x, y))

main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((255, 255, 255))
    draw(cube, 10, 10)

    print('cube drawn?')

    pygame.display.flip()