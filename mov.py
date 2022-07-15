import pygame

class Samsung(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/samsung.png")
        self.image = pygame.transform.scale(self.image, (426, 141))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed