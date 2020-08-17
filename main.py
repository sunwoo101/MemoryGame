import pygame, random

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

button_width = 100
button_height = 50

starting_speed = 10

character_set = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

# Fonts
largeText = pygame.font.Font("roboto.ttf", 60)
mediumText = pygame.font.Font("roboto.ttf", 40)
smallText = pygame.font.Font("roboto.ttf", 20)

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


# Timer (In seconds)
def timer(time):
    pygame.time.wait(time * 1000)


# Text renderer
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Button renderer
def button(button_text, button_x, button_y, button_width, button_height, inactive_colour, active_colour, action = None):

    # Mouse position
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Button
    if button_x + button_width > mouse_position[0] > button_x and button_y + button_height > mouse_position[1] > button_y:
        pygame.draw.rect(window, active_colour, (button_x, button_y, button_width, button_height))

        # Mouse click
        if mouse_click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(window, inactive_colour, (button_x, button_y, button_width, button_height))
    
    # Button text
    TextSurf, TextRect = text_objects(button_text, smallText)
    TextRect.center = (button_x + (button_width/2), button_y + (button_height/2))
    window.blit(TextSurf, TextRect)

# Splashscreen
def splashscreen():

    splashscreen = True

    while splashscreen:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Text
        TextSurf, TextRect = text_objects("Sun Woo's Memory Game", largeText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)

        # Timer
        timer(2)

        # Show menu
        menu()


# Menu
def menu():

    menu = True

    while menu:
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
        button("Start", x_center - 250, y_center + 100, button_width, button_height, green, bright_green, difficulty_selection)

        # Quit button
        button("Quit", x_center + 150, y_center + 100, button_width, button_height, red, bright_red, quit)

        pygame.display.update()
        clock.tick(fps)


# Select diffuculty
def difficulty_selection():

    difficulty_selection = True

    while difficulty_selection:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Select level text
        TextSurf, TextRect = text_objects("Select difficulty", largeText)
        TextRect.center = (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)

        # Easy button
        button("Easy", x_center - 250, y_center, button_width, button_height, green, bright_green, easy)

        # Medium button
        button("Medium", x_center - 50, y_center, button_width, button_height, red, bright_red, medium)

        # Hard button
        button("Hard", x_center + 150, y_center, button_width, button_height, red, bright_red, hard)

        # Hard button
        button("Back", x_center - 250, y_center + 150, button_width, button_height, red, bright_red, menu)

        pygame.display.update()
        clock.tick(fps)


# Easy
def easy():

    answer = ""

    i = 0
    while i < 6:
        answer += random.choice(character_set)
        i += 1

    easy = True

    while easy:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display answer
        TextSurf, TextRect = text_objects(answer, smallText)
        TextRect.center = (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)

        # 5 second timer
        timer(5)

        # Start game
        game()


# Medium
def medium():

    answer = ""

    i = 0
    while i < 6:
        answer += random.choice(character_set)
        i += 1

    medium = True

    while medium:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display answer
        TextSurf, TextRect = text_objects(answer, smallText)
        TextRect.center = (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)

        # 3 second timer
        timer(3)

        # Start game
        game()


# Hard
def Hard():

    answer = ""

    i = 0
    while i < 6:
        answer += random.choice(character_set)
        i += 1

    hard = True

    while hard:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        window.fill(white)

        # Display answer
        TextSurf, TextRect = text_objects(answer, smallText)
        TextRect.center = (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(fps)

        # 1 second timer
        timer(1)

        # Start game
        game()


# Game
def game():
    pass


# Start splashscreen
splashscreen()


# Quit
def quit():
    pygame.quit()

