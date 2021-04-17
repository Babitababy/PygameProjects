# Import pygame
import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('gfg.png')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Rotate the image by any degree
image = pygame.transform.rotate(image, 180)

# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)

# Prepare loop condition
running = False

# Event loop
while not running:

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    # Background Color
    screen.fill((255, 255, 255))

    # Show the image
    screen.blit(image, DEFAULT_IMAGE_POSITION)

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)




