import pygame
import sys

class Game():
    def __init__(self,map): #check

        pygame.display.init()
        listmod = pygame.display.list_modes()
        listsize = []
        self.map = map
        self.victory = [(2,2),(2,3),(2,4)]
        self.defeat = [(1,2)]

        for i in listmod:
            listsize.append(min(i))
        
        self.scale = min(max(listsize)//16, 50)
        self.macimg = pygame.image.load("macgyver.png")
        self.macrect = self.macimg.get_rect().move(0,self.map.startermac()*self.scale)
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
    
    def displaymap(self): #check

        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        for i in range(15):
            for j in range(15):
                if self.map.map[i][j] == "0":
                    self.screen.blit(self.wallimg,self.originrect.move(j*self.scale, i*self.scale))
                elif self.map.map[i][j] == "2":
                    if self.map.items[(i,j)] == "needle":
                        self.screen.blit(self.needleimg, self.originrect.move(j*self.scale, i*self.scale))
                    elif self.map.items[(i,j)] == "tube":
                        self.screen.blit(self.tubeimg, self.originrect.move(j*self.scale, i*self.scale))
                    elif self.map.items[(i,j)] == "ether":
                        self.screen.blit(self.etherimg, self.originrect.move(j*self.scale, i*self.scale))
                elif self.map.map[i][j] == "5":
                    self.screen.blit(self.guardianimg, self.originrect.move(j*self.scale, i*self.scale))
                pygame.display.flip()
        self.screen.blit(self.macimg, self.macrect)
        for i in range(16):
            if i == 0:
                self.screen.blit(self.inventoryimg, self.originrect.move(15*self.scale, 0))
            else:
                self.screen.blit(self.whiteimg, self.originrect.move(15*self.scale, i*self.scale))
        pygame.display.flip()
                

    def move(self,mac,direction):

        self.screen.blit(self.blackimg, self.macrect)

        if direction == pygame.K_UP and self.map.canmoveup(mac):
            self.macrect = self.macrect.move(0, -self.scale)
            mac.i = mac.i - 1
        elif direction == pygame.K_DOWN and self.map.canmovedown(mac) :
            self.macrect = self.macrect.move(0, self.scale)
            mac.i = mac.i + 1
        elif direction == pygame.K_LEFT and self.map.canmoveleft(mac) :
            self.macrect = self.macrect.move(-self.scale, 0)
            mac.j = mac.j - 1
        elif direction == pygame.K_RIGHT and self.map.canmoveright(mac):
            self.macrect = self.macrect.move(self.scale, 0)
            mac.j = mac.j + 1

        self.screen.blit(self.macimg, self.macrect)
        pygame.display.flip()

    def pickup(self,mac):
        if self.map.map[mac.i][mac.j] == "2" and self.map.items[(mac.i,mac.j)] not in mac.items:
            mac.items.append(self.map.items[(mac.i,mac.j)])
            if self.map.items[(mac.i,mac.j)] == "tube":
                self.screen.blit(self.tubeimg, self.originrect.move(15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i,mac.j)] == "needle":
                self.screen.blit(self.needleimg, self.originrect.move(15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i,mac.j)] == "ether":
                self.screen.blit(self.etherimg, self.originrect.move(15*self.scale, len(mac.items)*self.scale))
            pygame.display.flip()
            if len(mac.items) >= 3:
                self.screen.blit(self.blackimg, self.originrect.move(15*self.scale, self.scale))
                self.screen.blit(self.syringueimg, self.originrect.move(15*self.scale, self.scale))
                self.screen.blit(self.whiteimg, self.originrect.move(15*self.scale, 2*self.scale))
                self.screen.blit(self.whiteimg, self.originrect.move(15*self.scale, 3*self.scale))
            pygame.display.flip()
        elif self.map.map[mac.i][mac.j] == "5" :
            if len(mac.items) >= 3:
                self.screen.fill((255,255,255))
                for p in self.victory :
                    self.screen.blit(self.littleblackimg, self.originrect.move(int(p[0]*self.scale/2), int(p[1]*self.scale/2)))
            else:
                self.screen.fill((255,255,255))
                for p in self.defeat :
                    self.screen.blit(self.littleblackimg, self.originrect.move(int(p[0]*self.scale/2), int(p[1]*self.scale/2)))
            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()