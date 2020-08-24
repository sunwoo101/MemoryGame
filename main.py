import pygame
import random

pygame.init()

# Window setup
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Window Caption
pygame.display.set_caption("Memory Game")

# Variables
clock = pygame.time.Clock()
fps = 60
x_center = window_width/2
y_center = window_height/2
center = x_center, y_center
button_width = 120
button_height = 50
input_box_width = 400
input_box_height = 50
character_set = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
word = ""
input_text = ""

# Fonts
largeText = pygame.font.Font("roboto.ttf", 60)
mediumText = pygame.font.Font("roboto.ttf", 40)
smallText = pygame.font.Font("roboto.ttf", 20)

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
bright_red = (255, 150, 150)
green = (0, 255, 0)
bright_green = (150, 255, 150)
yellow = (255, 255, 0)
bright_yellow = (255, 255, 150)
purple = (255, 0, 255)
bright_purple = (255, 150, 255)


# Text renderer
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Button renderer
def button(button_text, button_x, button_y, button_width, button_height, inactive_colour, active_colour, action=None):

    # Mouse position
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Button
    if button_x + button_width/2 > mouse_position[0] > button_x - button_width/2 and button_y + button_height/2 > mouse_position[1] > button_y - button_height/2:
        pygame.draw.rect(window, active_colour, (button_x - button_width/2, button_y - button_height/2, button_width, button_height))

        # Mouse click
        if mouse_click[0] == 1 and action is not None:
            action()

    else:
        pygame.draw.rect(window, inactive_colour, (button_x - button_width/2, button_y - button_height/2, button_width, button_height))

    # Button text
    TextSurf, TextRect = text_objects(button_text, smallText)
    TextRect.center = (button_x, button_y)
    window.blit(TextSurf, TextRect)


# Splashscreen
def splashscreen():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Splashscreen text
        TextSurf, TextRect = text_objects("Sun Woo's Memory Game", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)

        # Timer
        pygame.time.wait(2000)

        # Show menu
        menu()


# Menu
def menu():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Menu text
        TextSurf, TextRect = text_objects("Menu", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Start button
        button("Start", x_center - 200, y_center + 100, button_width, button_height, green, bright_green, difficulty_selection)

        # Instructions
        button("Instructions", x_center, y_center + 100, button_width, button_height, green, bright_green, instructions)

        # Quit button
        button("Quit", x_center + 200, y_center + 100, button_width, button_height, red, bright_red, quit)

        pygame.display.update()
        clock.tick(fps)


# Select diffuculty
def difficulty_selection():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Select diffuculty text
        TextSurf, TextRect = text_objects("Select difficulty", largeText)
        TextRect.center = (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)

        # Easy button
        button("Easy", x_center, y_center - 100, button_width, button_height, green, bright_green, easy)

        # Medium button
        button("Medium", x_center, y_center, button_width, button_height, yellow, bright_yellow, medium)

        # Hard button
        button("Hard", x_center, y_center + 100, button_width, button_height, purple, bright_purple, hard)

        # Back button
        button("Back", x_center - 250, y_center + 200, button_width, button_height, red, bright_red, menu)

        pygame.display.update()
        clock.tick(fps)


# Instructions
def instructions():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Instructions text
        TextSurf, TextRect = text_objects("How to play", largeText)
        TextRect.center = (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("A random set of characters will be displayed on the screen for a set amount of time.", smallText)
        TextRect.center = (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Easy: 5 seconds", smallText)
        TextRect.center = (x_center, y_center - 50)
        window.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Medium: 3 seconds", smallText)
        TextRect.center = (x_center, y_center - 25)
        window.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Hard: 1 seconds", smallText)
        TextRect.center = (x_center, y_center)
        window.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("After the timer is up type the characters in to the input box.", smallText)
        TextRect.center = (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)

        # Back button
        button("Back", x_center - 250, y_center + 150, button_width, button_height, red, bright_red, menu)

        pygame.display.update()
        clock.tick(fps)


# Easy
def easy():

    random_word()

    global word
    global input_text

    countdown = 5

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects(f"The word is: {word}", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)

        if countdown == 0:
            input_text = ""
            game()

        countdown -= 1


# Medium
def medium():

    random_word()

    global word
    global input_text

    countdown = 3

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects(f"The word is: {word}", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)

        if countdown == 0:
            input_text = ""
            game()

        countdown -= 1


# Hard
def hard():

    random_word()

    global word
    global input_text

    countdown = 1

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects(f"The word is: {word}", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)

        if countdown == 0:
            input_text = ""
            game()

        countdown -= 1


# Word generation
def random_word():

    global word
    word = ""

    i = 0
    while i < 6:
        word += random.choice(character_set)
        i += 1


# Game
def game():

    global input_box_width
    global input_box_height
    global input_text

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    confirm()
                else:
                    if len(input_text) < 6:
                        input_text += event.unicode

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects("Type the word below", mediumText)
        TextRect.center = (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)

        # Enter button
        button("Enter", x_center, y_center + 200, button_width, button_height, green, bright_green, confirm)

        # Input box
        pygame.draw.rect(window, black, (x_center - input_box_width/2, y_center - input_box_height/2, input_box_width, input_box_height))
        pygame.draw.rect(window, white, (x_center - (input_box_width - 10)/2, y_center - (input_box_height - 10)/2, input_box_width - 10, input_box_height - 10))

        # Input box text
        TextSurf, TextRect = text_objects(input_text, smallText)
        TextRect.center = (x_center, y_center)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)


# Confirm
def confirm():
    global word
    global input_text

    if input_text == word:
        correct()
    else:
        incorrect()


# Correct
def correct():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects("Correct", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Menu button
        button("Menu", x_center - 250, y_center + 250, button_width, button_height, green, bright_green, menu)

        # Quit button
        button("Quit", x_center + 250, y_center + 250, button_width, button_height, red, bright_red, quit)

        pygame.display.update()
        clock.tick(fps)


# Incorrect
def incorrect():

    while True:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display word
        TextSurf, TextRect = text_objects("Incorrect", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        # Menu button
        button("Menu", x_center - 250, y_center + 250, button_width, button_height, green, bright_green, menu)

        # Quit button
        button("Quit", x_center + 250, y_center + 250, button_width, button_height, red, bright_red, quit)

        pygame.display.update()
        clock.tick(fps)


# Start splashscreen
splashscreen()


# Quit
def quit():
    pygame.quit()
