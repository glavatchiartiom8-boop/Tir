import pygame
from pygame.examples.sprite_texture import running

pygame.init()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()