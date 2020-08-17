import pygame


pygame.init()


# Window size
pygame_height = (800)
pygame_width = (600)

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
purple = (200, 61, 255)
orange = (255, 170, 0)
pink = (255, 0, 149)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Window setup
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((pygame_height, pygame_width))
pygame.display.set_caption("SDD Assignment")


# Text renderer
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Main
def main():

    main = True

    # While running
    while main:
        for event in pygame.event.get():
            # If quit button pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(blue)
        largeText = pygame.font.SysFont('Comic Sans MS', 110)
        TextSurf, TextRect = text_objects("MEMORY GAME", largeText)
        TextRect.center = ((pygame_height/2), (pygame_width/2))
        gameDisplay.blit(TextSurf, TextRect)

        # Green button
        button("Start", 150, 450, 100, 50, green, bright_green, game_loop)

        # Red button
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(60)


def game_loop():

    loop2 = True

    while loop2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(blue)
        largeText = pygame.font.SysFont('Comic Sans MS', 100)
        TextSurf, TextRect = text_objects("Levels", largeText)
        TextRect.center = ((400), (100))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back", 50, 450, 100, 50, red, bright_red, main)
        button("Very Easy", 150, 250, 100, 50, purple, bright_green)
        button("Normal", 350, 250, 100, 50, orange, bright_green)
        button("Expert", 550, 250, 100, 50, pink, bright_green)

        pygame.display.update()
        clock.tick(60)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # Text
    smallText = pygame.font.SysFont("Comic Sans MS", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)


# QUIT
def quitgame():
    pygame.quit()


main()
game_loop()

pygame.quit()
