import pygame

class SeaWeed(object):
    def __init__(self, image, x,y, speed):
        self.image_s = image
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image_s, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        if self.x > width:
            self.x = 0

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            pygame.quit()

class UpperSeaWeed(object):
    def __init__(self, image, x,y, speed):
        self.image_s = image
        self.image_b = self.image_s.get_rect()        
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image_s, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        if self.x > width:
            self.x = 0

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            pygame.quit()