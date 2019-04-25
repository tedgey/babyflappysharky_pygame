import pygame

class Shark(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/daddy_shark_110px.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
