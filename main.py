import pygame
from mov import Samsung
pygame.init()

# Important
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables
samsung = Samsung(0, 0)
up = False
down = False
right = False
left = False
clock = pygame.time.Clock()

down = True
right = True

'''Boucle jeu'''
running = True
while running:

    '''Evenements'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    '''Affichage'''
    screen.blit(screen, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(samsung.image, samsung.rect)
    pygame.display.flip()

    '''Déplacement'''
    if samsung.rect.y >= 939:
        down = False
        up = True
    if samsung.rect.x >= 1494:
        right = False
        left = True
    if samsung.rect.y <= 0:
        up = False
        down = True
    if samsung.rect.x <= 0:
        left = False
        right = True

    if down == True:
        samsung.move_down()
    if up == True:
        samsung.move_up()
    if right == True:
        samsung.move_right()
    if left == True:
        samsung.move_left()

    clock.tick(60)
pygame.quit()