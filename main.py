import pygame
from map import *
from game import *
from mac import *

map = Map()
map.readmap("map.txt")
map.placeguardian()
map.placeitems()
mac = Macgyver(map.startermac())
game = Game(map)
game.displaymap()
game.pickup(mac)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            game.move(mac, event.key)
            game.pickup(mac)