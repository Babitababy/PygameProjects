#import pygame
import pygame

#Initilize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#changing Title
pygame.display.set_caption("First Game")

#changing Icon
logo = pygame.image.load('icon.jpg')
pygame.display.set_icon(logo)


#Do this to make the screen available until close button is pressed
#Game Loop

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB - red, Green, Blue
    screen.fill((255, 0, 255))
    #update the screen
    pygame.display.update()


