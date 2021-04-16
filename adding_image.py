#import pygame
import pygame

#Initilize the pygame
pygame.init()

#create the window screen
screen = pygame.display.set_mode((800,600))


# Adding Imgge
image = pygame.image.load('aeroplane.jpg')
X_axis = 200
Y_axis = 200

def Game():
    screen.blit(image, (X_axis, Y_axis))


#Do this to make the screen available until close button is pressed
#Game Loop

running= True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Game()
    #update the screen
    pygame.display.update()


