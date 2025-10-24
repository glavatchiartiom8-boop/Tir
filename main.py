import pygame
import random
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tir')
icon = pygame.image.load('tir.png')
pygame.display.set_icon(icon)
target_img = pygame.image.load('apple.png')
target_img = pygame.transform.scale(target_img, (120, 80))
target_width = 80
target_height = 80
target_x = random.randint(0, 720 - target_width)
target_y = random.randint(0, 520 - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + 120 and target_y < mouse_y < target_y + 80:
                target_x = random.randint(0, 720 - target_width)
                target_y = random.randint(0, 520 - target_height)

    screen.fill(color)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()