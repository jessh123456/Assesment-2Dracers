""" surroundcars_3_v6  TRIALLING
    I have trialled a way to stop the cars overlapping in Version 5, However
    the code was chunky and didn't work. I tried a different way, but this way
    was too complicated and out of my league. I tried to test if the images
    were on top of each other but I'm not familiar with the code forms."""

import pygame  # Imports the pygame module
import random  # Imports random module


pygame.init()

screen = pygame.display.set_mode((700, 600))  # Sets screen size
background = pygame.transform.scale(pygame.image.load('Background.png'),
                                    (700, 605))  # Import background picture
lines = pygame.transform.scale(pygame.image.load('triple lines3.png'),
                               (400, 710))
lines_2 = pygame.transform.scale(pygame.image.load('triple lines3.png'),
                                 (400, 710))
red_car = pygame.transform.scale(pygame.image.load('car_1.png'), (70, 140))
car_2 = pygame.transform.scale(pygame.image.load('car_2.png'), (70, 140))
car_3 = pygame.transform.scale(pygame.image.load('car_3.png'), (70, 140))
car_4 = pygame.transform.scale(pygame.image.load('car_4.png'), (70, 140))
car_5 = pygame.transform.scale(pygame.image.load('car_5.png'), (70, 140))
car_6 = pygame.transform.scale(pygame.image.load('car_6.png'), (70, 140))
cars = [car_2, car_3, car_4, car_5, car_6]  # Different coloured cars
car_x_option = [160, 270, 370, 470]  # random lane 1 - 4
# Two lines are defined so when one disappears off screen, a second can replace
screen.blit(background, (0, -3))  # Define Background
screen.blit(lines, (150, 0))  # Define lines
screen.blit(red_car, (350, 400))
pygame.display.update()  # Update screen


def game_loop():
    red_car_x = 370  # Set position
    red_car_y = 400
    road_x = 150  # Set position
    road_y = 0
    road2_y = 701
    MOVEMENT = 10  # How much the lines will move by (CONSTANT)
    car_move = random.randrange(5, 9)
    car_move2 = random.randrange(5, 9)
    car_move3 = random.randrange(5, 9)
    car_move4 = random.randrange(5, 9)
    car_move5 = random.randrange(5, 9)
    car_x = 0  # X position for each of the random cars
    car_x2 = 0
    car_x3 = 0
    car_x4 = 0
    car_x5 = 0
    car_y = -150  # Y position for each of the random cars
    car_y2 = -150
    car_y3 = -150
    car_y4 = -150
    car_y5 = -150
    chosen_car = random.choice(cars)  # Random colour of cars
    chosen_car2 = random.choice(cars)
    chosen_car3 = random.choice(cars)
    chosen_car4 = random.choice(cars)
    chosen_car5 = random.choice(cars)
    car_position = pygame.Rect(car_x, car_y, 45, 45)
    car_2_position = pygame.Rect(car_x2, car_y2, 45, 45)
    car_3_position = pygame.Rect(car_x3, car_y3, 45, 45)
    car_4_position = pygame.Rect(car_x4, car_y4, 45, 45)
    car_5_position = pygame.Rect(car_x5, car_y5, 45, 45)
    car_list = [car_2_position, car_5_position, car_3_position, car_4_position]
    car_list2 = [car_position, car_5_position, car_3_position, car_4_position]
    car_list3 = [car_position, car_5_position, car_2_position, car_4_position]
    car_list4 = [car_position, car_5_position, car_3_position, car_2_position]
    car_list5 = [car_position, car_2_position, car_3_position, car_4_position]
    car_appearance = random.randrange(100, 500)  # random time cars will appear
    run = False  # Start random cars
    run1 = False  # Starts lines
    run2 = False  # Starts lines
    run3 = False  # Start random cars
    run4 = False  # Start random cars
    run5 = False  # Start random cars
    run6 = False  # Start random cars
    first_time = True  # Starts cars
    clock = pygame.time.Clock()  # Define clock
    quit_game = False  # When player presses 'X' to quit
    game_over = False  # When player dies
    while not quit_game:  # For future use when the 'x' in the corner is used
        while not game_over:
            clock.tick(30)  # Clock tick set
            road_y_position = pygame.Rect(road_x, road_y, 50, 700)
            road2_y_position = pygame.Rect(road_x, road2_y, 50, 700)
            screen.blit(red_car, (red_car_x, red_car_y))
            pygame.display.update()  # Display update

            keys = pygame.key.get_pressed()  # check if user has pressed a key
            if keys[pygame.K_LEFT]:  # Left arrow is pressed
                if red_car_x >= 160:  # Limit so car doesn't go off screen
                    red_car_x -= 10  # Move left 10
            if keys[pygame.K_RIGHT]:  # Right arrow is pressed
                if red_car_x <= 470:  # Limit so car doesn't go off screen
                    red_car_x += 10  # Move right 10

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

            if first_time:  # to start cars
                if car_y == -150:  # only choose colour and lane once
                    chosen_car = random.choice(cars)  # Choose a colour
                    car_x = random.choice(car_x_option)  # Choose a lane
                    car_move = random.randrange(5, 9)  # Random speed
                car_y += car_move  # Car moves down by random speed
                car_position = pygame.Rect(car_x, car_y, 80, 80)
                screen.blit(chosen_car, car_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y >= 600:  # if car is off-screen
                    first_time = False  # Stop running loop
                    car_y = -150  # Car resets to top

            if car_y > car_appearance:  # Random time to appear
                run = True
            if run:
                if car_y2 == -150:  # only choose colour and lane once
                    chosen_car2 = random.choice(cars)  # Choose a colour
                    car_x2 = random.choice(car_x_option)  # Choose a lane
                    car_move2 = random.randrange(5, 9)  # Random speed
                for car in car_list2:
                    if pygame.Rect.colliderect(car_2_position, car):
                        print("detected")  # Testing purposes
                        car_move2 = 5
                car_y2 += car_move2  # Car moves down by random speed
                car_2_position = pygame.Rect(car_x2, car_y2, 80, 80)
                screen.blit(chosen_car2, car_2_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y2 >= 600:  # if car is off-screen
                    car_y2 = -150  # Car resets to top
                    run = False  # Stop running loop

            if car_y2 > car_appearance:  # Random time to appear
                run3 = True
            if run3:
                if car_y3 == -150:  # only choose colour and lane once
                    chosen_car3 = random.choice(cars)  # Choose a colour
                    car_x3 = random.choice(car_x_option)  # Choose a lane
                    car_move3 = random.randrange(5, 9)  # Random speed
                for car in car_list3:
                    if pygame.Rect.colliderect(car_3_position, car):
                        print("detected")
                        car_move3 = 5
                car_y3 += car_move3  # Car moves down by random speed
                car_3_position = pygame.Rect(car_x3, car_y3, 80, 80)
                screen.blit(chosen_car3, car_3_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y3 >= 600:  # if car is off-screen
                    car_y3 = -150  # Car resets to top
                    run3 = False  # Stop running loop

            if car_y3 > car_appearance:  # Random time to appear
                run4 = True
            if run4:
                if car_y4 == -150:  # only choose colour and lane once
                    chosen_car4 = random.choice(cars)  # Choose a colour
                    car_x4 = random.choice(car_x_option)  # Choose a lane
                    car_move4 = random.randrange(5, 9)  # Random speed
                for car in car_list4:
                    if pygame.Rect.colliderect(car_4_position, car):
                        print("detected")
                        car_move4 = 5
                car_y4 += car_move4  # Car moves down by random speed
                car_4_position = pygame.Rect(car_x4, car_y4, 80, 80)
                screen.blit(chosen_car4, car_4_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y4 >= 600:  # if car is off-screen
                    car_y4 = -150  # Car resets to top
                    run4 = False  # Stop running loop

            if car_y4 > car_appearance:  # Random time to appear
                run5 = True
            if run5:
                if car_y5 == -150:  # only choose colour and lane once
                    chosen_car5 = random.choice(cars)  # Choose a colour
                    car_x5 = random.choice(car_x_option)  # Choose a lane
                    car_move5 = random.randrange(5, 9)  # Random speed
                for car in car_list5:
                    if pygame.Rect.colliderect(car_5_position, car):
                        print("detected")
                        car_move5 = 5
                car_y5 += car_move5  # Car moves down by random speed
                car_5_position = pygame.Rect(car_x5, car_y5, 80, 80)
                screen.blit(chosen_car5, car_5_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y5 >= 600:  # if car is off-screen
                    car_y5 = -150  # Car resets to top
                    run5 = False  # Stop running loop

            if car_y5 > car_appearance:  # Random time to appear
                run6 = True
            if run6:
                if car_y == -150:  # only choose colour and lane once
                    chosen_car = random.choice(cars)  # Choose a colour
                    car_x = random.choice(car_x_option)  # Choose a lane
                    car_move = random.randrange(5, 9)  # Random speed
                for car in car_list:
                    if pygame.Rect.colliderect(car_position, car):
                        print("detected")
                        car_move = 5
                car_y += car_move  # Car moves down by random speed
                car_position = pygame.Rect(car_x, car_y, 80, 80)
                screen.blit(chosen_car, car_position)  # Print car
                car_appearance = random.randrange(100, 500)  # random time next
                # car will appear
                if car_y >= 600:  # if car is off-screen
                    car_y = -150  # Car resets to top
                    run6 = False  # Stop running loop
            screen.blit(red_car, (red_car_x, red_car_y))
            pygame.display.update()


game_loop()  # Calls Game loop function
