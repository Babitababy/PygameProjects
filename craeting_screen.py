#import pygame
import pygame

#Initilize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((700,600))

#Do this to make the screen available until close button is pressed
#Game Loop

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



