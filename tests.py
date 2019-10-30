import sys, pygame
from os import path, chdir
chdir(path.dirname(path.realpath(sys.argv[0])))
pygame.init()
size = 750,800
black =0,0,0
screen = pygame.display.set_mode(size)
mac = pygame.image.load("MacGyver50.png")
macrect=mac.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(black)
        screen.blit(mac,macrect)
        pygame.display.flip()
