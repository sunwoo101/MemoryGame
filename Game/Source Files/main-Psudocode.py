import pygame
import random

initialize pygame

window setup
window_width <- 800
window_height <- 600
window <- pygame.display.set_mode((window_width, window_height))
set window caption to "Memory Game"

variables
clock <- pygame.time.Clock()
fps <- 60
x_center <- window_width/2
y_center <- window_height/2
center <- x_center, y_center
button_width <- 120
button_height <- 50
input_box_width <- 400
input_box_height <- 50
character_set <- "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
word <- ""
input_text <- ""
mouse_position <- pygame.mouse.get_pos()
handled <- False

fonts
largeText <- pygame.font.Font("roboto.ttf", 60)
mediumText <- pygame.font.Font("roboto.ttf", 40)
smallText <- pygame.font.Font("roboto.ttf", 20)

colours
white <- (255, 255, 255)
black <- (0, 0, 0)
grey <- (200, 200, 200)
red <- (255, 0, 0)
bright_red <- (255, 150, 150)
green <- (0, 255, 0)
bright_green <- (150, 255, 150)
yellow <- (255, 255, 0)
bright_yellow <- (255, 255, 150)
purple <- (255, 0, 255)
bright_purple <- (255, 150, 255)

text generation
FUNCTION text_objects(text, font):
    textSurface <- font.render(text, True, black)
    RETURN textSurface, textSurface.get_rect()
ENDFUNCTION

warning generation
FUNCTION warning(text, font):
    textSurface <- font.render(text, True, red)
    RETURN textSurface, textSurface.get_rect()
ENDFUNCTION

button
FUNCTION button(button_text, button_x, button_y, button_width, button_height, inactive_colour, active_colour, action=None):
    make handled global
    make mouse position global

    mouse position
    IF mouse_position != pygame.mouse.get_pos():
        handled <- True
    ENDIF
    mouse_position <- pygame.mouse.get_pos()
    mouse_click <- pygame.mouse.get_pressed()

    setting handled to false when mouse isnt clicked
    IF mouse_click[0] = 0:
        handled <- False
    ENDIF

    detect button pressed
    IF button_x + button_width/2 > mouse_position[0] > button_x - button_width/2 AND button_y + button_height/2 > mouse_position[1] > button_y - button_height/2:
        pygame.draw.rect(window, active_colour, (button_x - button_width/2, button_y - button_height/2, button_width, button_height))
        IF mouse_click[0] = 1 AND action is not None AND not handled:
            handled <- True
            action()
        ENDIF
    ELSE:
        pygame.draw.rect(window, inactive_colour, (button_x - button_width/2, button_y - button_height/2, button_width, button_height))

    ENDIF
    TextSurf, TextRect <- text_objects(button_text, smallText)
    TextRect.center <- (button_x, button_y)
    window.blit(TextSurf, TextRect)
ENDFUNCTION

splashscreen
FUNCTION splashscreen():
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Splashscreen text
        TextSurf, TextRect <- text_objects("Sun Woo's Memory Game", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Display update
        pygame.display.update()
        clock.tick(fps)
        # Timer
        pygame.time.wait(2000)
        # Show menu
        menu()
    ENDWHILE
ENDFUNCTION

menu
FUNCTION menu():
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Menu text
        TextSurf, TextRect <- text_objects("Menu", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Start button
        button("Start", x_center - 200, y_center + 100, button_width, button_height, green, bright_green, difficulty_selection)
                                                                                                           ENDIF
        # Instructions button
        button("Instructions", x_center, y_center + 100, button_width, button_height, green, bright_green, instructions)
        # Quit button
        button("Quit", x_center + 200, y_center + 100, button_width, button_height, red, bright_red, quit)
        # Display update
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
ENDFUNCTION

difficulty selection
FUNCTION difficulty_selection():
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Select diffuculty text
        TextSurf, TextRect <- text_objects("Select difficulty", largeText)
        TextRect.center <- (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)
        # Easy button
        button("Easy", x_center, y_center - 100, button_width, button_height, green, bright_green, easy)
        # Medium button
        button("Medium", x_center, y_center, button_width, button_height, yellow, bright_yellow, medium)
        # Hard button
        button("Hard", x_center, y_center + 100, button_width, button_height, purple, bright_purple, hard)
        # Back button
        button("Back", x_center - 250, y_center + 200, button_width, button_height, red, bright_red, menu)
        # Display update
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
ENDFUNCTION

instructions
FUNCTION instructions():
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Instructions text
        TextSurf, TextRect <- text_objects("How to play", largeText)
        TextRect.center <- (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect <- text_objects("A random set of characters will be displayed on the screen for a set amount of time.", smallText)

        TextRect.center <- (x_center, y_center - 100)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect <- text_objects("Easy: 5 seconds", smallText)
        TextRect.center <- (x_center, y_center - 50)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect <- text_objects("Medium: 3 seconds", smallText)
        TextRect.center <- (x_center, y_center - 25)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect <- text_objects("Hard: 1 seconds", smallText)
        TextRect.center <- (x_center, y_center)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect <- text_objects("After the timer is up type the characters in to the input box.", smallText)
        TextRect.center <- (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)
        # Back button
        button("Back", x_center - 250, y_center + 150, button_width, button_height, red, bright_red, menu)
        # Display update
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
ENDFUNCTION

easy
FUNCTION easy():
    random_word()
    make input_text global
    countdown <- 5
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Display word
        TextSurf, TextRect <- text_objects(f"The word is: {word}", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Display countdown
        TextSurf, TextRect <- text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center <- (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)
        # Display update
        pygame.display.update()
        clock.tick(1)
        # Start game when timer reaches 0
        countdown -= 1
        IF countdown = 0:
            input_text <- ""
            game()
        ENDIF
    ENDWHILE
ENDFUNCTION

medium
FUNCTION medium():
    random_word()
    make input_text global
    countdown <- 3
    WHILE True:
        # If exit button pressed
        FOR event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        ENDFOR
        # Background
        window.fill(white)
        # Display word
        TextSurf, TextRect <- text_objects(f"The word is: {word}", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Display countdown
        TextSurf, TextRect <- text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center <- (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)
        # Display update
        pygame.display.update()
        clock.tick(1)
        # Start game when timer reaches 0
        countdown -= 1
        IF countdown = 0:
            input_text <- ""
            game()
        ENDIF
    ENDWHILE
# Hard
ENDFUNCTION

FUNCTION hard():
    random_word()
    global input_text
    countdown <- 1
    while True:
        # If exit button pressed
        for event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Display word
        TextSurf, TextRect <- text_objects(f"The word is: {word}", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Display countdown
        TextSurf, TextRect <- text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center <- (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)
        # Display update
        pygame.display.update()
        clock.tick(1)
        # Start game when timer reaches 0
        countdown -= 1
        IF countdown = 0:
            input_text <- ""
            game()
        ENDIF
    ENDWHILE
# Word generation
ENDFUNCTION

FUNCTION random_word():
    global word
    word <- ""
    i <- 0
    while i < 6:
        word += random.choice(character_set)
        i += 1
    ENDWHILE
# Game
ENDFUNCTION

FUNCTION game():
    global input_text
    global clicked
    input_box_selected <- False
    while True:
        # Mouse events
        mouse_position <- pygame.mouse.get_pos()
        # Events
        for event in pygame.event.get():
            # If exit button pressed
            IF event.type = pygame.QUIT:
                quit()
            # Selecting the input box
            ENDIF
            IF event.type = pygame.MOUSEBUTTONDOWN:
                IF x_center + input_box_width/2 > mouse_position[0] > x_center - input_box_width/2 AND y_center + input_box_height/2 > mouse_position[1] > y_center - input_box_height/2:
                    input_box_selected <- True
                ELSE:
                    input_box_selected <- False
                ENDIF
            # Detect keys
            ENDIF
            IF event.type = pygame.KEYDOWN:
                IF input_box_selected:
                    IF event.key = pygame.K_BACKSPACE:
                        input_text <- input_text[:-1]
                    ELSEIF event.key = pygame.K_RETURN:
                        confirm()
                    ELSE:
                        IF len(input_text) < 6:
                            input_text += event.unicode
            ENDIF
                ENDIF
                    ENDIF
                        ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Title text
        TextSurf, TextRect <- text_objects("Type the word below", mediumText)
        TextRect.center <- (x_center, y_center - 200)
        window.blit(TextSurf, TextRect)
        # Enter button
        button("Enter", x_center, y_center + 200, button_width, button_height, green, bright_green, confirm)
        # Input box
        IF input_box_selected:
            # Box
            pygame.draw.rect(window, black, (x_center - input_box_width/2, y_center - input_box_height/2, input_box_width, input_box_height))
            pygame.draw.rect(window, white, (x_center - (input_box_width - 10)/2, y_center - (input_box_height - 10)/2, input_box_width - 10, input_box_height - 10))
            # Text
            TextSurf, TextRect <- text_objects(input_text, smallText)
            TextRect.center <- (x_center, y_center)
            window.blit(TextSurf, TextRect)
        ELSE:
            # Box
            pygame.draw.rect(window, black, (x_center - input_box_width/2, y_center - input_box_height/2, input_box_width, input_box_height))
            pygame.draw.rect(window, grey, (x_center - (input_box_width - 10)/2, y_center - (input_box_height - 10)/2, input_box_width - 10, input_box_height - 10))
            # Text
            TextSurf, TextRect <- text_objects(input_text, smallText)
            TextRect.center <- (x_center, y_center)
            window.blit(TextSurf, TextRect)
            # Warning
            TextRect.center <- (x_center, y_center + 40)
            window.blit(TextSurf, TextRect)
        # Display update
        ENDIF
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
# Confirm
ENDFUNCTION

FUNCTION confirm():
    global word
    global input_text
    IF input_text = word:
        correct()
    ELSE:
        incorrect()
    ENDIF
# Correct
ENDFUNCTION

FUNCTION correct():
    while True:
        # If exit button pressed
        for event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Display correct
        TextSurf, TextRect <- text_objects("Correct", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Menu button
        button("Menu", x_center - 250, y_center + 250, button_width, button_height, green, bright_green, menu)
        # Quit button
        button("Quit", x_center + 250, y_center + 250, button_width, button_height, red, bright_red, quit)
        # Display update
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
# Incorrect
ENDFUNCTION

FUNCTION incorrect():
    global word
    while True:
        # If exit button pressed
        for event in pygame.event.get():
            IF event.type = pygame.QUIT:
                quit()
            ENDIF
        # Background
        ENDFOR
        window.fill(white)
        # Display incorrect
        TextSurf, TextRect <- text_objects("Incorrect", largeText)
        TextRect.center <- (center)
        window.blit(TextSurf, TextRect)
        # Display answer
        TextSurf, TextRect <- text_objects(f"The correct answer was {word}", smallText)
        TextRect.center <- (x_center, y_center + 50)
        window.blit(TextSurf, TextRect)
        # Menu button
        button("Menu", x_center - 250, y_center + 250, button_width, button_height, green, bright_green, menu)
        # Quit button
        button("Quit", x_center + 250, y_center + 250, button_width, button_height, red, bright_red, quit)
        # Display update
        pygame.display.update()
        clock.tick(fps)
    ENDWHILE
# Start splashscreen
ENDFUNCTION

splashscreen()
# Quit
FUNCTION quit():
    pygame.quit()
