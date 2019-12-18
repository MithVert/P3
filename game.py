import pygame
import sys


class Game():

    """game is the main class of the program 
    it is the one which controls the display 
    and uses the other classes as ressources"""

    def __init__(self, map):

        # these lines creates a list containing all the available resolutions

        pygame.display.init()
        listmod = pygame.display.list_modes()
        listsize = []
        self.map = map

        for i in listmod:
            listsize.append(min(i))

        # so we can now define the resolution of our game
        # scale being the pixel height and lenght of every case of the maze
        self.scale = min(max(listsize)//16, 50)

        # loading every image and creating two rect objects to place the images
        # note that only Macgyver will have a rect object which will move
        # while all other object will always be placed compare to the origin
        # and therefore uses the same rect : originrect
        self.macimg = pygame.image.load("macgyver.png")
        self.macrect = self.macimg.get_rect().move(
            0, self.map.startermac()*self.scale)
        self.guardianimg = pygame.image.load("guardian.png")
        self.originrect = self.guardianimg.get_rect()
        self.wallimg = pygame.image.load("wall.png")
        self.syringueimg = pygame.image.load("syringue.png")
        self.etherimg = pygame.image.load("ether.png")
        self.tubeimg = pygame.image.load("tube.png")
        self.needleimg = pygame.image.load("needle.png")
        self.blackimg = pygame.image.load("black.png")
        self.littleblackimg = pygame.image.load("littleblack.png")
        self.inventoryimg = pygame.image.load("inventory.png")
        self.whiteimg = pygame.image.load("white.png")
        self.screen = pygame.display.set_mode((self.scale*16, self.scale*15))
        self.victory = pygame.transform.scale(
            pygame.image.load("victory.png"), (self.scale*16, self.scale*15))
        self.defeat = pygame.transform.scale(
            pygame.image.load("defeat.png"), (self.scale*16, self.scale*15))

    def displaymap(self):

        # browsing through the map file and displaying every case of the mazes

        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        for i in range(15):
            for j in range(15):
                if self.map[i, j] == "0":
                    self.screen.blit(
                        self.wallimg, self.originrect.move(
                            j*self.scale, i*self.scale))
                elif self.map[i, j] == "2":
                    if self.map.items[(i, j)] == "needle":
                        self.screen.blit(
                            self.needleimg, self.originrect.move(
                                j*self.scale, i*self.scale))
                    elif self.map.items[(i, j)] == "tube":
                        self.screen.blit(
                            self.tubeimg, self.originrect.move(
                                j*self.scale, i*self.scale))
                    elif self.map.items[(i, j)] == "ether":
                        self.screen.blit(
                            self.etherimg, self.originrect.move(
                                j*self.scale, i*self.scale))
                elif self.map[i, j] == "5":
                    self.screen.blit(
                        self.guardianimg, self.originrect.move(
                            j*self.scale, i*self.scale))
                pygame.display.flip()
        self.screen.blit(self.macimg, self.macrect)

        # distinguishing the last column from the rest
        # with a white background
        # so the user doesn't mistake the inventory for the maze

        for i in range(16):
            self.screen.blit(
                self.whiteimg, self.originrect.move(
                    15*self.scale, i*self.scale))
            self.screen.blit(
                self.inventoryimg, self.originrect.move(
                    15*self.scale, 0))
        pygame.display.flip()

    def move(self, mac, direction):

        # moving mac and updating the display accordingly
        # as long as Mac can effectively move this way

        self.screen.blit(self.blackimg, self.macrect)

        if direction == pygame.K_UP and self.map.canmoveup(mac):
            self.macrect = self.macrect.move(0, -self.scale)
            mac.i = mac.i - 1
        elif direction == pygame.K_DOWN and self.map.canmovedown(mac):
            self.macrect = self.macrect.move(0, self.scale)
            mac.i = mac.i + 1
        elif direction == pygame.K_LEFT and self.map.canmoveleft(mac):
            self.macrect = self.macrect.move(-self.scale, 0)
            mac.j = mac.j - 1
        elif direction == pygame.K_RIGHT and self.map.canmoveright(mac):
            self.macrect = self.macrect.move(self.scale, 0)
            mac.j = mac.j + 1

        self.screen.blit(self.macimg, self.macrect)
        pygame.display.flip()

    def pickup(self, mac):

        # pickup is the action mac will always do when he enters a case
        # therefore it is not only about looting objects
        # but also about fighting the guardian

        # first we verify wether there is a object to loot
        if self.map[mac.i, mac.j] == "2" \
            and self.map.items[(mac.i, mac.j)] not in mac.items:
            mac.items.append(self.map.items[(mac.i, mac.j)])
            if self.map.items[(mac.i, mac.j)] == "tube":
                self.screen.blit(
                    self.tubeimg, self.originrect.move(
                        15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i, mac.j)] == "needle":
                self.screen.blit(
                    self.needleimg, self.originrect.move(
                        15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i, mac.j)] == "ether":
                self.screen.blit(
                    self.etherimg, self.originrect.move(
                        15*self.scale, len(mac.items)*self.scale))
            pygame.display.flip()
            # if there were one to loot,
            # we check wether he can craft his syringue already
            if len(mac.items) >= 3:
                self.screen.blit(
                    self.whiteimg, self.originrect.move(
                        15*self.scale, self.scale))
                self.screen.blit(
                    self.syringueimg, self.originrect.move(
                        15*self.scale, self.scale))
                self.screen.blit(
                    self.whiteimg, self.originrect.move(
                        15*self.scale, 2*self.scale))
                self.screen.blit(
                    self.whiteimg, self.originrect.move(
                        15*self.scale, 3*self.scale))
            pygame.display.flip()
        # then we check wether he may fight the guardian
        elif self.map[mac.i, mac.j] == "5":
            if len(mac.items) >= 3:
                    self.screen.blit(self.victory, self.originrect)
            else:
                    self.screen.blit(self.defeat, self.originrect)
            pygame.display.flip()
            # once the player either won or lost,
            # we wait for him to close the window
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

