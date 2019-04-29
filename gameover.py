import pygame


class Gameover(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/gameover.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class TheEnd(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        # if self.x > width:
        #     self.x = 0
    