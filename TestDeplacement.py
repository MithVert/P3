import pygame
import sys
pygame.init()
size = 750, 800
scale = 50
background = 0, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(background)
mac = pygame.image.load("MacGyver50.png")
macrect = mac.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed = (0, -scale)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_DOWN:
                speed = (0, scale)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_LEFT:
                speed = (-scale, 0)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_RIGHT:
                speed = (scale, 0)
                macrect = macrect.move(speed)
            screen.fill(background)
            screen.blit(mac,macrect)
            pygame.display.flip()