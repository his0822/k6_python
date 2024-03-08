import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

image = pygame.image.load('./images/ship.bmp')
rect = image.get_rect()


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("skyblue")  # Fill the display with a solid color
    
    # Render the graphics here.
    # ...
    screen.blit(image, rect)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)