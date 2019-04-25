import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Shark(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ggj/baby_shark_outlined.png').convert_alpha()
        self.speed = 5
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.key_direction_x = 0
        self.key_direction_y = 0
        self.dead = False

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_position(self):
        self.x += self.key_direction_x
        self.y += self.key_direction_y

