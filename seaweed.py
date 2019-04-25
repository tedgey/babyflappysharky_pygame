import pygame

class SeaWeed:
    def __init__(self, image, x,y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        if self.x > width:
            self.x = 0

class UpperSeaWeed:
    def __init__(self, image, x,y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        if self.x > width:
            self.x = 0