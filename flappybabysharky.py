import pygame

from sharkyeet import Shark

from seaweed import SeaWeed


def main():
    width = 1000
    height = 1000
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Adding image files
    seaweed_image = pygame.image.load('images/seaweed.png').convert_alpha()

    # Adding flappybabyshark and seaweed characters:

    seaweed = SeaWeed(seaweed_image, 1000, 500, 1)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        seaweed.update_position(width, height)

        # Draw background
        screen.fill(blue_color)

        # Game display
        seaweed.display(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
