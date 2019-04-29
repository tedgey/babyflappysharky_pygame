import pygame
import time
import os, sys
import random
from pygame.sprite import Group, spritecollide, spritecollideany, collide_rect

upper_seaweed = os.path.join('images/upper_seaweed.png')
lower_seaweed = os.path.join('images/seaweed.png')
sharky_image = os.path.join('images/daddy_shark_110px.png')

class Shark(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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

    def draw(self, screen):
        screen.blit(self.image_s, (self.x,self.y))


class Seaweed(pygame.sprite.Sprite):
    def __init__(self, x=1000, y=500, ):
        pygame.sprite.Sprite.__init__(self)
        self.image_s = pygame.image.load(lower_seaweed)
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        dist = 10
        self.dist = dist

    def lower_seaweed(self):
        dist = 10
        self.x -=dist
    
    def lower_seaweed_draw(self, screen):
        screen.blit(self.image_s, (self.x, self.y))

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            print('collision!!!!!!!!!!!')



class UpperSeaweed(pygame.sprite.Sprite):
    def __init__(self, x=1000, y=500, ):
        pygame.sprite.Sprite.__init__(self)
        self.image_s = pygame.image.load(upper_seaweed)
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        dist = 10
        self.dist = dist

    def upper_seaweed(self):
        dist = 10
        self.x -=dist
    
    def upper_seaweed_draw(self, screen):
        screen.blit(self.image_s, (self.x, self.y))

    #def checkCollision(self, sprite1, sprite2):
        # if pygame.sprite.spritecollideany(shark, seaweed_group):
        #     shark.kill()
        #     print('DEAD')


def main():
    width = 1000
    height = 1000
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Baby Daddy Shark')
    clock = pygame.time.Clock()

    lower_seaweed = Seaweed()
    upper_seaweed = UpperSeaweed()
    shark = Shark()
    seaweed_group = Group()
    seaweed_group.add(lower_seaweed, upper_seaweed)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if upper_seaweed.x < 0:
                y = random.randint(10, 190)
                upper_seaweed = UpperSeaweed(640, y)

            if pygame.sprite.spritecollideany(shark, seaweed_group):
                shark.kill()
                print('DEAD')
            # upper_seaweed.checkCollision(shark.image_b, upper_seaweed.image_b)

            # upper_seaweed.checkCollision(shark.image_b, upper_seaweed.image_b)
            # lower_seaweed.checkCollision(shark.image_b, lower_seaweed.image_b)
        shark.handle_keys()
        upper_seaweed.upper_seaweed()
        lower_seaweed.lower_seaweed()

        screen.fill(blue_color)
        shark.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
