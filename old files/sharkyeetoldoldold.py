import pygame
import os, sys

sharky_image = os.path.join('images/daddy_shark_110px.png')

class Shark(object):
    def __init__(self):
        self.image_s = pygame.image.load(sharky_image)
        self.image_b = self.image_s.get_rect()
        self.x = 40
        self.y = 50

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 2
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image_s, (self.x,self.y))

# class Shark(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load('images/daddy_shark_110px.png').convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.center = pos
