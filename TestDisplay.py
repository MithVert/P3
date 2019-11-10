import pygame
import sys
pygame.display.init()
size = 48, 48
screen = pygame.display.set_mode(size)
mac = pygame.image.load("macgyver.png")
mac.convert()
size = 48*15, 48*15
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))
macrect = mac.get_rect()
macrect.move(0,0)
screen.blit(mac,macrect)
pygame.display.flip()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()