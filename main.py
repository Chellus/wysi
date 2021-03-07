import pygame

pygame.init()

# window constants
window_w = 344
window_h = 242

# create window and clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

# resources
wysiImg = pygame.image.load('wysi_img.png')

# colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_green = (0, 200, 0)
green = (0, 255, 0)
# button function
def button(msg, font_size, x, y, w, h, ac, ic, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pressed = False

    # if the cursor is inside the button, we use the active color
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))

        # if the button is pressed with left click
        if click[0] == 1 and action != None:
            pressed = True
            action()

    # if the cursor is not inside the button, we use the inactive color
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))

    # text inside the button
    smallText = pygame.font.Font('freesansbold.ttf', font_size)
    textSurf = smallText.render(msg, True, black)
    textRect = textSurf.get_rect()
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(textSurf, textRect)

    return pressed

if __name__ == "__main__":
    running = True
    window.fill(white)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(30)
