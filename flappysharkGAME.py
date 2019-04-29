import pygame
import time
from background import Background
from shark import Shark
from seaweed import SeaWeed
from seaweed import UpperSeaWeed
from pygame.sprite import Group, spritecollide, spritecollideany, groupcollide
from gameover import Gameover
from gameover import TheEnd


def main():
    width = 1000
    height = 1000
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)

    # adding music
    pygame.mixer.init()
    sound = pygame.mixer.Sound('music/baby_shark_soundtrack.wav')

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Baby Daddy Shark')
    clock = pygame.time.Clock()

    # Adding image files
    seaweed_image = pygame.image.load('images/seaweed.png').convert_alpha()
    upper_seaweed_image = pygame.image.load(
        'images/upper_seaweed.png').convert_alpha()
    sharky_image = pygame.image.load(
        'images/daddy_shark_110px.png').convert_alpha()
    the_end_image = pygame.image.load('images/the_end.png').convert_alpha()



    # Adding flappybabyshark and seaweed characters:
    # seaweed = SeaWeed(seaweed_image, 1000, 600, 1)
    # upper_seaweed = UpperSeaWeed(upper_seaweed_image, 1000, -600, 1)

    seaweed = SeaWeed(seaweed_image, 1000, 600, 2)
    seaweed2 = SeaWeed(seaweed_image, 1400, 1400, 2)
    seaweed3 = SeaWeed(seaweed_image, 2000, 600, 2)
    seaweed4 = SeaWeed(seaweed_image, 2800, 1200, 2)
    seaweed5 = SeaWeed(seaweed_image, 1000, 600, 2)
    seaweed6 = SeaWeed(seaweed_image, 1400, 1400, 2)
    seaweed7 = SeaWeed(seaweed_image, 2000, 600, 2)
    seaweed8 = SeaWeed(seaweed_image, 2800, 1200, 2)
    seaweed9= SeaWeed(seaweed_image, 1000, 600, 2)
    seaweed10 = SeaWeed(seaweed_image, 1400, 1400, 2)
    seaweed11 = SeaWeed(seaweed_image, 2000, 600, 2)
    seaweed12 = SeaWeed(seaweed_image, 2800, 1200, 2)
    seaweed13 = SeaWeed(seaweed_image, 1000, 600, 2)
    seaweed14 = SeaWeed(seaweed_image, 1400, 1400, 2)
    seaweed15 = SeaWeed(seaweed_image, 2000, 600, 2)
    seaweed16 = SeaWeed(seaweed_image, 2800, 1200, 2)
    upper_seaweed = UpperSeaWeed(upper_seaweed_image, 800, -600, 2)
    upper_seaweed2 = UpperSeaWeed(upper_seaweed_image, 1400, -400, 2)
    upper_seaweed3 = UpperSeaWeed(upper_seaweed_image, 1900, -800, 2)
    upper_seaweed4 = UpperSeaWeed(upper_seaweed_image, 2300, -700, 2)
    upper_seaweed5 = UpperSeaWeed(upper_seaweed_image, 800, -600, 2)
    upper_seaweed6 = UpperSeaWeed(upper_seaweed_image, 1400, -400, 2)
    upper_seaweed7 = UpperSeaWeed(upper_seaweed_image, 1900, -800, 2)
    upper_seaweed8 = UpperSeaWeed(upper_seaweed_image, 2300, -700, 2)
    upper_seaweed9 = UpperSeaWeed(upper_seaweed_image, 800, -600, 2)
    upper_seaweed10 = UpperSeaWeed(upper_seaweed_image, 1400, -400, 2)
    upper_seaweed11 = UpperSeaWeed(upper_seaweed_image, 1900, -800, 2)
    upper_seaweed12 = UpperSeaWeed(upper_seaweed_image, 2300, -700, 2)
    upper_seaweed13 = UpperSeaWeed(upper_seaweed_image, 800, -600, 2)
    upper_seaweed14 = UpperSeaWeed(upper_seaweed_image, 1400, -400, 2)
    upper_seaweed15 = UpperSeaWeed(upper_seaweed_image, 1900, -800, 2)
    upper_seaweed16 = UpperSeaWeed(upper_seaweed_image, 2300, -700, 2)
    the_end = TheEnd(the_end_image, 3100, 500, 3)

    
    shark = Shark(100, 500)
    #shark.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    # shark.vx = 5
    # shark.vy = 5

    # shark_group = pygame.sprite.Group()
    # shark_group.add(shark)

    seaweed_group = Group()
    seaweed_group.add(seaweed, seaweed2, seaweed3, seaweed4, seaweed5, seaweed6, seaweed7, seaweed8, seaweed9, seaweed10, seaweed11, seaweed12, seaweed13, seaweed14, seaweed15, seaweed16, upper_seaweed, upper_seaweed2, upper_seaweed3, upper_seaweed4, upper_seaweed5, upper_seaweed6, upper_seaweed7, upper_seaweed8, upper_seaweed9, upper_seaweed10, upper_seaweed11, upper_seaweed12, upper_seaweed13, upper_seaweed14, upper_seaweed15, upper_seaweed16)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(shark)

    # Game loop/Event handling
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound.play()
                stop_game = True

        # draw stuff
        BackGround = Background('images/bbsharktitle.jpg', [0, 0])
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        font = pygame.font.Font(None, 50)
        text = font.render('Click to play! Survive the seaweed maze!!', True, black_color)
        screen.blit(text, (150, 750))

        pygame.display.update()
        clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 275:  # right arrow key number
                    shark.should_move("right")
                elif event.key == 276:
                    shark.should_move("left")
                elif event.key == 273:
                    shark.should_move("up")
                elif event.key == 274:
                    shark.should_move("down")
            elif event.type == pygame.KEYUP:  # the user released a key
                if event.key == 275:
                    shark.should_move("right", False)
                elif event.key == 276:
                    shark.should_move("left", False)
                elif event.key == 273:
                    shark.should_move("up", False)
                elif event.key == 274:
                    shark.should_move("down", False)
                else:
                    print(event.key)
    

    
        # Game logic

        # Draw background
        screen.fill(blue_color)

        #Updating the positions for the seaweed to move
        seaweed.update_position(width, height)
        seaweed2.update_position(width, height)
        seaweed3.update_position(width, height)
        seaweed4.update_position(width, height)
        seaweed5.update_position(width, height)
        seaweed6.update_position(width, height)
        seaweed7.update_position(width, height)
        seaweed8.update_position(width, height)
        seaweed9.update_position(width, height)
        seaweed10.update_position(width, height)
        seaweed11.update_position(width, height)
        seaweed12.update_position(width, height)
        seaweed13.update_position(width, height)
        seaweed14.update_position(width, height)
        seaweed15.update_position(width, height)
        seaweed16.update_position(width, height)
        upper_seaweed.update_position(width, height)
        upper_seaweed2.update_position(width, height)
        upper_seaweed3.update_position(width, height)
        upper_seaweed4.update_position(width, height)
        upper_seaweed5.update_position(width, height)
        upper_seaweed6.update_position(width, height)
        upper_seaweed7.update_position(width, height)
        upper_seaweed8.update_position(width, height)
        upper_seaweed9.update_position(width, height)
        upper_seaweed10.update_position(width, height)
        upper_seaweed11.update_position(width, height)
        upper_seaweed12.update_position(width, height)
        upper_seaweed13.update_position(width, height)
        upper_seaweed14.update_position(width, height)
        upper_seaweed15.update_position(width, height)
        upper_seaweed16.update_position(width, height)
        the_end.update_position(width, height)

        #Redrawing the seaweed in new positions to give it movement
        seaweed.display(screen)
        seaweed2.display(screen)
        seaweed3.display(screen)
        seaweed4.display(screen)
        seaweed5.display(screen)
        seaweed6.display(screen)
        seaweed7.display(screen)
        seaweed8.display(screen)
        seaweed9.display(screen)
        seaweed10.display(screen)
        seaweed11.display(screen)
        seaweed12.display(screen)
        seaweed13.display(screen)
        seaweed14.display(screen)
        seaweed15.display(screen)
        seaweed16.display(screen)
        upper_seaweed.display(screen)
        upper_seaweed2.display(screen)
        upper_seaweed3.display(screen)
        upper_seaweed4.display(screen)
        upper_seaweed5.display(screen)
        upper_seaweed6.display(screen)
        upper_seaweed7.display(screen)
        upper_seaweed8.display(screen)
        upper_seaweed9.display(screen)
        upper_seaweed10.display(screen)
        upper_seaweed11.display(screen)
        upper_seaweed12.display(screen)
        upper_seaweed13.display(screen)
        upper_seaweed14.display(screen)
        upper_seaweed15.display(screen)
        upper_seaweed16.display(screen)
        the_end.display(screen)


        # seaweed.display(screen)
        # upper_seaweed.display(screen)
        # seaweed.update_position(width, height)
        # upper_seaweed.update_position(width, height)

        #Shark 
        if pygame.sprite.spritecollideany(shark, seaweed_group):
            shark.kill()

            sound.stop()
        # gameover screen
            GameOver = Gameover('images/gameover.png', [0, 0])
            screen.fill([255, 255, 255])
            screen.blit(GameOver.image, GameOver.rect)
            font = pygame.font.Font(None, 50)
            #text = font.render('Click to play again!', True, black_color)
            screen.blit(text, (395, 500))


        # shark.render(screen, sharky_image)
        for entity in all_sprites:
            screen.blit(entity.image, [entity.x, entity.y])

        shark.draw_me(width, height)
        shark.update_me(width, height)

        # print("shark", shark.x, shark.y)
        # print("seaweed", seaweed.x, seaweed.y)
        # print("upper seaweed", upper_seaweed.x, upper_seaweed.y)

        # collision
        if pygame.sprite.spritecollideany(shark, seaweed_group):
            shark.kill()
            print('DEAD')

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
