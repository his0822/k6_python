import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


image = pygame.image.load('./Ch12/images/ship.bmp')
image_rect = image.get_rect()
image_rect.midbottom = screen.get_rect().midbottom


BULLET_color =(255,0,0)

def create_bullet(image_rect):
    bullet = pygame.Rect(0,0,5,50)
    bullet.midtop = image_rect.midtop
    bullet.top -= image_rect.height
    return bullet

def update_bullets(screen_rect, bullets):
    new_bullets = []
    for bullt in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -= 1
            new_bullets.append(bullet)
    return new_bullets



while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_rect.left -= 20
            if event.key == pygame.K_RIGHT:
                image_rect.right += 20
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(image_rect))

    # Do logical updates here.
    # ...

    screen.fill("skyblue")  # Fill the display with a solid color
    
    # Render the graphics here.
    # ...

    for bullet in bullets:
        bullet.top -= 10
    
    screen.blit(image, image_rect)
    
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_color, bullet)
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)