import pygame
import sys
from map import *
from mac  import *
from initprgm import *
from game import *

print("Initialisation")
listinit = initprgm()
print("Creating Map")
map = Map(listinit[0][1])
map.readmap("map.txt")
print("Placing items")
map.placeitems()
print("Placing Macgyver")
mac = Macgyver(map.startermac(), map)
print("Drawing map")
game = Game(mac, listinit)
game.displaymap()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                game.move("UP")
            elif event.key == pygame.K_DOWN:
                game.move("DOWN")
            elif event.key == pygame.K_LEFT:
                game.move("LEFT")
            elif event.key == pygame.K_RIGHT:
                game.move("RIGHT")