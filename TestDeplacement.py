import pygame
import sys
pygame.init()
size = 750, 800
scale = 50
background = 0, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(background)
mac = pygame.image.load("macgyver.png")
black = pygame.image.load("black.png")
macrect = mac.get_rect()
screen.blit(mac,macrect)
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed = (0, -scale)
                screen.blit(black, macrect)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_DOWN:
                speed = (0, scale)
                screen.blit(black, macrect)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_LEFT:
                speed = (-scale, 0)
                screen.blit(black, macrect)
                macrect = macrect.move(speed)
            elif event.key == pygame.K_RIGHT:
                speed = (scale, 0)
                screen.blit(black, macrect)
                macrect = macrect.move(speed)
            screen.blit(mac,macrect)
            pygame.display.flip()