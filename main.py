import pygame

#initialize the pygame
pygame.init()

#create the screem
screen = pygame.display.set_mode((600, 600))


#Title and Logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))



#Game Loop (prevent the crash)
running = True
while running:

    # RGB = red,green,blue (0-255)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    player()
    pygame.display.update()
