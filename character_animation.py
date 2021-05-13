import pygame
pygame.init()

walkRight =[pygame.image.load('R1.png'), pygame.image.load('R2.png'),pygame.image.load('R3.png'),
            pygame.image.load('R4.png'), pygame.image.load('R5.png'),pygame.image.load('R6.png'),
            pygame.image.load('R7.png'), pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft =[pygame.image.load('L1.png'), pygame.imag.load('L2.png'), pygame.image.load('L3.png'),
           pygame.image.load('L4.png'), pygame.imag.load('L5.png'), pygame.image.load('L6.png'),
           pygame.image.load('L7.png'), pygame.imag.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Character Animation")

x = 50
y = 425
width = 64
height = 64
val = 5
isJump = False
jumpCount = 10

#mainLoop
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > val:
        x -= val
    if keys[pygame.K_RIGHT] and x < 500 - width - val:
        x += val
    if not (isJump):
        if keys[pygame.K_UP] and y > val:
            y -= val
        if keys[pygame.K_DOWN] and y < 500 -height - val:
            y += val
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg =1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2) *0.5 *neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount =10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()