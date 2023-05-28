""" endgame_5_2
    In this version, I have re-started the game by re-calling the loop and
    emptying the red_car + car_group. This way the user can play again without
    having to restart the game."""

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
arrows = pygame.transform.scale(pygame.image.load('arrows.png'), (300, 140))
msg_font = pygame.font.SysFont("freesansbold.ttf", 80)
small_msg_font = pygame.font.SysFont("freesansbold.ttf", 30)
space_font = pygame.font.SysFont("freesansbold.ttf", 50)
instructions = True  # Runs instructions loop until space key is pressed
white = (255, 255, 255)  # Background instructions colour
green = (136, 228, 28)  # Background instructions colour
red = (255, 29, 25)  # Background instructions colour
black = (0, 0, 0)  # Text colour

car_x_option = [185, 298, 405, 515]  # random lane 1 - 4
# Two lines are defined so when one disappears off screen, a second can replace
screen.blit(background, (0, -3))  # Define Background
screen.blit(lines, (150, 0))  # Define lines
screen.blit(arrows, (197, 290))
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("2D Racers - by Jess Hansen")
pygame.display.update()  # Update screen


class Red_Car(pygame.sprite.Sprite):
    def __init__(self, red_car_x, red_car_y):
        super().__init__()
        self.red_car_x = red_car_x
        self.red_car_y = red_car_y
        self.image = pygame.transform.scale(pygame.image.load('car_1.png'),
                                            (70, 140))
        self.rect = self.image.get_rect(center=(self.red_car_x - 35,
                                                self.red_car_y - 70))
        self.rect = pygame.Rect(self.red_car_x - 35, self.red_car_y - 70, 60,
                                120)

    def update(self):
        self.rect.center = (self.red_car_x, self.red_car_y)
        key = pygame.key.get_pressed()  # check if user has pressed a key
        if key[pygame.K_LEFT]:  # Left arrow is pressed
            if self.red_car_x >= 190:  # Limit so car doesn't go off screen
                self.red_car_x -= 10  # Move left 10
        if key[pygame.K_RIGHT]:  # Right arrow is pressed
            if self.red_car_x <= 511:  # Limit so car doesn't go off screen
                self.red_car_x += 10  # Move right 10


class Car_Info(pygame.sprite.Sprite):  # Class
    def __init__(self, car_x, car_y):
        super().__init__()
        self.car_x = car_x  # Car x position
        self.car_y = car_y  # Car y position
        self.cars = []  # Car list
        # Car images as sprites
        self.cars.append(pygame.transform.scale(
            pygame.image.load("car_2.png"), (70, 140)))
        self.cars.append(pygame.transform.scale(
            pygame.image.load("car_3.png"), (70, 140)))
        self.cars.append(pygame.transform.scale(
            pygame.image.load("car_4.png"), (70, 140)))
        self.cars.append(pygame.transform.scale(
            pygame.image.load("car_5.png"), (70, 140)))
        self.cars.append(pygame.transform.scale(
            pygame.image.load("car_6.png"), (70, 140)))

        self.image = random.choice(self.cars)  # Randomly selects a sprite
        self.rect = self.image.get_rect(center=(self.car_x, self.car_y))
        # Rectangle of image
        self.speed = random.randint(7, 11)  # Random speed

    def update(self):
        self.car_y += self.speed  # car moves down
        self.rect = self.image.get_rect(center=(self.car_x, self.car_y))
        if self.car_y > 750:  # when car is off the screen
            self.kill()  # remove from sprite group


def instructions_message(msg, txt_colour, bkgd_colour, msg_2, msg_3, msg_4):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(350, 175))
    screen.blit(txt, text_box)
    small_txt = small_msg_font.render(msg_2, True, txt_colour, bkgd_colour)
    small_txt_box = txt.get_rect(center=(513, 455))
    screen.blit(small_txt, small_txt_box)
    small_txt2 = small_msg_font.render(msg_3, True, txt_colour, bkgd_colour)
    small_txt_box2 = txt.get_rect(center=(555, 478))
    screen.blit(small_txt2, small_txt_box2)
    space_txt = space_font.render(msg_4, True, txt_colour, bkgd_colour)
    space_txt_box = txt.get_rect(center=(473, 260))
    screen.blit(space_txt, space_txt_box)


def end_game_message(msg, txt_colour, bkgd_colour, msg_2):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(350, 175))
    screen.blit(txt, text_box)
    small_txt2 = small_msg_font.render(msg_2, True, txt_colour, bkgd_colour)
    small_txt_box2 = txt.get_rect(center=(270, 400))
    screen.blit(small_txt2, small_txt_box2)


def game_loop():
    red_car_x = 402  # Set position
    red_car_y = 460
    road_x = 150  # Set position
    road_y = 0
    road2_y = 701
    MOVEMENT = 12  # How much the lines will move by (CONSTANT)
    run1 = False  # Starts lines
    run2 = False  # Starts lines
    clock = pygame.time.Clock()  # Define clock
    quit_game = False  # When player presses 'X' to quit
    game_over = False  # When player dies
    car_group = pygame.sprite.Group()
    red_car_group = pygame.sprite.Group()
    red_car = Red_Car(red_car_x, red_car_y)
    red_car_group.add(red_car)
    while not quit_game:  # For future use when the 'x' in the corner is used
        while not game_over:
            clock.tick(30)  # Clock tick set
            road_y_position = pygame.Rect(road_x, road_y, 50, 700)
            road2_y_position = pygame.Rect(road_x, road2_y, 50, 700)

            red_car_group.update()  # Player car movements updated

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

            collisions = pygame.sprite.spritecollide(red_car, car_group, False)
            if collisions:
                game_over = True

            # Spawn cars
            if random.randrange(1, 30) == 5:  # Random time for cars to appear
                if len(car_group) < 4:  # Only 4 cars at a time
                    car_pos_x = random.choice(car_x_option)  # Choose a car
                    car_pos_y = random.randint(-200, -100)  # Random
                    # y-coordinate between -200 and -100 to prevent cars
                    # appearing in a line
                    if not any(abs(-200 <= car.car_y <= -50) for
                               car in car_group):  # If no car is between -200
                        # and -50, then spawn a car.
                        while any(abs(car_pos_x - car.car_x) < 60 for car
                                  in car_group):  # Check if a car is beside it
                            car_pos_x = random.choice(car_x_option)  # Changing
                            # x position until not on another car
                        car = Car_Info(car_pos_x, car_pos_y)
                        car_group.add(car)

            # Update game objects
            car_group.update()  # Update obstacle positions

            # Draw game objects
            red_car_group.draw(screen)
            car_group.draw(screen)  # Prints cars
            pygame.display.update()  # Updates screen
        end_game_message("You died!", black, red, "Press [Q] to quit, or "
                                                  "[SPACE] to play again")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit_game = True
                    quit()
                elif event.key == pygame.K_SPACE:
                    game_over = False
                    car_group.empty()  # Clear car sprite group
                    red_car_group.empty()  # Clear red car sprite group
                    screen.blit(background, (0, -3))  # Define Background
                    game_loop()  # Restart the game


instructions_message("Welcome to 3D Racers!", black, red, "Press the arrow "
                                                          "keys to move,",
                     "Avoid oncoming "
                     "cars!", "Press "
                              "[Space] "
                              "to begin!")
pygame.display.update()  # Update screen

while instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            quit()
        keys = pygame.key.get_pressed()  # check if user has pressed space
        if keys[pygame.K_SPACE]:
            instructions = False
            screen.blit(background, (0, -3))  # Define Background
            game_loop()  # Calls Game loop function
