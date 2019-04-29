import pygame

class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/daddy_shark_110px.png').convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.centery = self.y
        self.speed = 5

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, pressed_keys):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
