""" movingcar_2     TRIALLING
    I have created a car which moves with the arrow keys. However when pressed
    it only moves once, and the code is slow and laggy. a different version/way
    of doing it will be made in movingcar_2_v2."""

import pygame  # Imports the pygame module
pygame.init()

screen = pygame.display.set_mode((700, 600))  # Sets screen size
background = pygame.transform.scale(pygame.image.load('Background.png'),
                                    (700, 605))  # Import background picture
lines = pygame.transform.scale(pygame.image.load('triple lines2.png'),
                               (267, 700))
lines_2 = pygame.transform.scale(pygame.image.load('triple lines2.png'),
                                 (267, 700))
red_car = pygame.transform.scale(pygame.image.load('car_1.png'), (70, 140))
# Two lines are defined so when one disappears off screen, a second can replace
screen.blit(background, (0, -3))  # Define Background
screen.blit(lines, (216, 0))  # Define lines
screen.blit(red_car, (350, 400))
pygame.display.update()  # Update screen


def game_loop():
    car_x = 370
    car_y = 400
    road_x = 216  # Set position
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

            for event in pygame.event.get():  # Collect any external input
                if event.type == pygame.KEYDOWN:  # check if user pressed a key
                    if event.key == pygame.K_LEFT:  # Left arrow is pressed
                        car_x -= 10  # Move left 10
                    elif event.key == pygame.K_RIGHT:  # Right arrow is pressed
                        car_x += 10  # Move right 10
                    elif event.key == pygame.K_UP:  # Up arrow is pressed
                        car_y -= 10  # Move up 10
                    elif event.key == pygame.K_DOWN:  # Down arrow is pressed
                        car_y += 10  # Move down 10

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
