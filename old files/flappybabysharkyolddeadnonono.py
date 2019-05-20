import pygame
import time
from sharkyeet import Shark
from seaweed import SeaWeed
from seaweed import UpperSeaWeed



def main():
    width = 1000
    height = 1000
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Baby Daddy Shark')
    clock = pygame.time.Clock()


    # Adding image files
    lower_seaweed_image = pygame.image.load('images/seaweed.png').convert_alpha()
    upper_seaweed_image = pygame.image.load('images/upper_seaweed.png').convert_alpha()
    # sharky_image = pygame.image.load('images/daddy_shark_110px.png').convert_alpha()

    # Adding flappybabyshark and seaweed characters:

    lower_seaweed = SeaWeed(lower_seaweed_image, 1000,500, 1)
    upper_seaweed = UpperSeaWeed(upper_seaweed_image, 1000, -500, 1)

    # shark = Shark(sharky_image, 40,50)
    # shark.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    # shark.vx = 5
    # shark.vy = 5

    # shark_group = pygame.sprite.Group()
    # shark_group.add(shark)

    shark = Shark()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # key = pygame.key.get_pressed()

        upper_seaweed.checkCollision(shark.image_b, upper_seaweed.image_b)

        # for i in range(2):
        #     if key[shark.move[i]]:
        #         shark.rect.x += shark.vx * [-1, 1][i]

        # for i in range(2):
        #     if key[shark.move[2:4][i]]:
        #         shark.rect.y += shark.vy * [-1, 1][i]
    
        # Game logic
        lower_seaweed.update_position(width, height)
        upper_seaweed.update_position(width, height)
        
        screen.fill(blue_color)
        lower_seaweed.display(screen)
        upper_seaweed.display(screen)
        # shark_group.draw(screen)
        shark.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
