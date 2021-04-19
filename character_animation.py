import pygame
pygame.init()

win =pygame.display.set_mode((500,500))
pygame.display.set_caption("Character Animation")

x = 250
y = 250
radius = 15
val = 10

run= True
while run:
    win.fill((0,0,0))
    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # MOVEMENT OF CHARACTER
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        x -= val
    if userInput[pygame.K_RIGHT]:
        x += val
    if userInput[pygame.K_UP]:
        y -= val

    if userInput[pygame.K_DOWN]:
        y += val

    pygame.time.delay(10)
    pygame.display.update()
