import pygame
import os, sys

upper_seaweed = os.path.join('images/upper_seaweed.png')
lower_seaweed = os.path.join('images/seaweed.png')

class Seaweed(object):
    def __init__(self, x=1000, y=500, ):
        self.image_s = pygame.image.load(lower_seaweed)
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        dist = 10
        self.dist = dist

    def lower_seaweed(self):
        dist = 10
        self.x -=dist
    
    def lower_seaweed_draw(self, surface):
        surface.blit(self.image_s, (self.x, self.y))

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            font = pygame.Font(None, 50)
            text = font.render("You lose", True, (0,0,0))
            screen.blit(text, (300,750))


class UpperSeaweed(object):
    def __init__(self, x=1000, y=500, ):
        self.image_s = pygame.image.load(upper_seaweed)
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        dist = 10
        self.dist = dist

    def upper_seaweed(self):
        dist = 10
        self.x -=dist
    
    def upper_seaweed_draw(self, surface):
        surface.blit(self.image_s, (self.x, self.y))

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            font = pygame.Font(None, 50)
            text = font.render("You lose", True, (0,0,0))
            screen.blit(text, (300,750))