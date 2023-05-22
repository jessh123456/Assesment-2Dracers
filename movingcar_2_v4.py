""" movingcar_2_v4
    When the red car goes to the side of the road, it starts to draw itself.
    I have found that the easiest way to fix this is by making a third
    version of the dotted lines which is wider and will cover the
    extra cars."""

import pygame  # Imports the pygame module
pygame.init()

screen = pygame.display.set_mode((700, 600))  # Sets screen size
background = pygame.transform.scale(pygame.image.load('Background.png'),
                                    (700, 605))  # Import background picture
lines = pygame.transform.scale(pygame.image.load('triple lines3.png'),
                               (400, 700))
lines_2 = pygame.transform.scale(pygame.image.load('triple lines3.png'),
                                 (400, 700))
red_car = pygame.transform.scale(pygame.image.load('car_1.png'), (70, 140))
# Two lines are defined so when one disappears off screen, a second can replace
screen.blit(background, (0, -3))  # Define Background
screen.blit(lines, (150, 0))  # Define lines
screen.blit(red_car, (350, 400))
pygame.display.update()  # Update screen


def game_loop():
    car_x = 370
    car_y = 400
    road_x = 150  # Set position
    road_y = 0
    road2_y = 701
    MOVEMENT = 5   # How much the lines will move by (CONSTANT)
    run1 = False
    run2 = False
    clock = pygame.time.Clock()  # Define clock
    quit_game = False  # When player presses 'X' to quit
    game_over = False  # When player dies
    while not quit_game:  # For future use when the 'x' in the corner is used
        while not game_over:
            clock.tick(30)  # Clock tick set
            road_y_position = pygame.Rect(road_x, road_y, 50, 700)
            road2_y_position = pygame.Rect(road_x, road2_y, 50, 700)
            screen.blit(red_car, (car_x, car_y))
            pygame.display.update()  # Display update

            keys = pygame.key.get_pressed()  # check if user has pressed a key
            if keys[pygame.K_UP]:  # Up arrow is pressed
                if car_y >= 30:  # Limit so car doesn't go off screen
                    car_y -= 10  # Move up 10
            if keys[pygame.K_DOWN]:  # Down arrow is pressed
                if car_y <= 430:  # Limit so car doesn't go off screen
                    car_y += 10  # Move down 10
            if keys[pygame.K_LEFT]:  # Left arrow is pressed
                if car_x >= 160:  # Limit so car doesn't go off screen
                    car_x -= 10  # Move left 10
            if keys[pygame.K_RIGHT]:  # Right arrow is pressed
                if car_x <= 470:  # Limit so car doesn't go off screen
                    car_x += 10  # Move right 10

            if road_y > 5:
                run1 = True  # So continues to run until over y = 700
            if run1:
                if road2_y > 700:
                    road2_y = -695  # Resets to top of screen
                road2_y += MOVEMENT  # Move by 5
                screen.blit(lines, road2_y_position)  # Update screen
                if road2_y > 700:
                    run1 = False  # Restarts loop

            if road2_y > 5:
                run2 = True  # So continues to run until over y = 700
            if run2:
                if road_y > 700:
                    road_y = -695  # Resets to top of screen
                road_y += MOVEMENT  # Move by 5
                screen.blit(lines, road_y_position)  # Update screen
                if road_y > 700:
                    run2 = False  # Restarts loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                    quit()


game_loop()  # Calls Game loop function
