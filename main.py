import pygame
import random
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tir')
icon = pygame.image.load('tir.png')
pygame.display.set_icon(icon)
target_img = pygame.image.load('target-sport.jpg')
target_width = 80
target_height = 80
target_x = random.randint(0, 720 - target_width)
target_y = random.randint(0, 520 - target_height)

color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(target_img, (target_x, target_y))

pygame.quit()