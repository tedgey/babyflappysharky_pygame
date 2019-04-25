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
    seaweed_image = pygame.image.load('images/seaweed.png').convert_alpha()
    upper_seaweed_image = pygame.image.load('images/upper_seaweed.png').convert_alpha()
    sharky_image = pygame.image.load('images/daddy_shark_110px.png').convert_alpha()

    # Adding flappybabyshark and seaweed characters:

    seaweed = SeaWeed(seaweed_image, 1000, 500, 1)
    upper_seaweed = UpperSeaWeed(upper_seaweed_image, 1000, -500, 1)

    shark = Shark([40,50])
    shark.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    shark.vx = 5
    shark.vy = 5

    shark_group = pygame.sprite.Group()
    shark_group.add(shark)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[shark.move[i]]:
                shark.rect.x += shark.vx * [-1, 1][i]

        for i in range(2):
            if key[shark.move[2:4][i]]:
                shark.rect.y += shark.vy * [-1, 1][i]

    # Game initialization

    # stop_game = False
    # while not stop_game:
    #     for event in pygame.event.get():

    #         # Event handling

    #         if event.type == pygame.QUIT:
    #             stop_game = True


        # Game logic
        seaweed.update_position(width, height)
        upper_seaweed.update_position(width, height)

        # Draw background
        screen.fill(blue_color)
        seaweed.display(screen)
        upper_seaweed.display(screen)
        shark_group.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
