import pygame

pygame.init()

# Window setup
window_width = 1280
window_height = 720
x_center = window_width/2
y_center = window_height/2
center = x_center, y_center
window = pygame.display.set_mode((window_width, window_height))

# Window Caption
pygame.display.set_caption("Memory Game")

# Variables
clock = pygame.time.Clock()
starting_speed = 10

# Fonts
largeText = pygame.font.Font("roboto.ttf", 100)
mediumText = pygame.font.Font("roboto.ttf", 75)
smallText = pygame.font.Font("roboto.ttf", 20)

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
purple = (200, 61, 255)
orange = (255, 170, 0)
pink = (255, 0, 149)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


# Text renderer
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Splashscreen
def splashscreen():

    splashscreen = True

    while splashscreen:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                splashscreen = False

        # Background
        window.fill(white)

        # Text
        TextSurf, TextRect = text_objects("Sun Woo's Memory Game", mediumText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)

        pygame.time.wait(2000)

        menu()
        splashscreen = False


# Menu
def menu():

    menu = True

    while menu:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

            print(event)

        # Background
        window.fill(white)

        # Text
        TextSurf, TextRect = text_objects("Menu", mediumText)
        TextRect.center = (center)
        window.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)


splashscreen()
pygame.quit()
