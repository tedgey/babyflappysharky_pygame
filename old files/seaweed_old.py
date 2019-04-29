import pygame

class SeaWeed(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        print("seaweed", self.rect)
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        # if self.x > width:
        #     self.x = 0

class UpperSeaWeed(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        print("upper seaweed", self.rect)
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        # if self.x > width:
        #     self.x = 0
    

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
    