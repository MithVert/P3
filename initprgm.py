import pygame

def initprgm():
    pygame.display.init()
    listmod = pygame.display.list_modes()
    listsize = []
    for i in listmod:
        listsize.append(min(i))
    scale = max(listsize) // 16
    #displaysize = scale, scale
    displaysize = scale * 16, scale*15
    screen = pygame.display.set_mode(displaysize)
    mac = pygame.image.load("macgyver.png")
    #mac = mac.convert()
    guardian = pygame.image.load("guardian.png")
    #guardian = guardian.convert()
    wall = pygame.image.load("wall.png")
    #wall = wall.convert()
    black = pygame.image.load("black.png")
    #black = black.convert()
    syringue = pygame.image.load("syringue.png")
    #syringue = syringue.convert()
    ether = pygame.image.load("ether.png")
    #ether = ether.convert()
    tube = pygame.image.load("tube.png")
    #tube = tube.convert()
    needle = pygame.image.load("needle.png")
    #needle = needle.convert()
    #displaysize = scale * 16, scale*15
    #screen = pygame.display.set_mode(displaysize)
    return displaysize, scale, mac, guardian, wall, black, syringue, ether, tube, needle, screen