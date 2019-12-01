import pygame
import sys

class Game():
    def __init__(self,map): #check

        pygame.display.init()
        listmod = pygame.display.list_modes()
        listsize = []
        self.map = map

        for i in listmod:
            listsize.append(min(i))
        
        self.scale = max(listsize)//16
        self.macimg = pygame.image.load("macgyver.png")
        self.macrect = self.macimg.get_rect().move(0,self.map.startermac()*self.scale)
        self.guardianimg = pygame.image.load("guardian.png")
        self.guardianrect = self.guardianimg.get_rect()
        self.wallimg = pygame.image.load("wall.png")
        self.wallrect = self.wallimg.get_rect()
        self.syringueimg = pygame.image.load("syringue.png")
        self.syringuerect = self.syringueimg.get_rect()
        self.etherimg = pygame.image.load("ether.png")
        self.etherrect = self.etherimg.get_rect()
        self.tubeimg = pygame.image.load("tube.png")
        self.tuberect = self.tubeimg.get_rect()
        self.needleimg = pygame.image.load("needle.png")
        self.needlerect = self.needleimg.get_rect()
        self.blackimg = pygame.image.load("black.png")
        self.blackrect = self.blackimg.get_rect()
        self.screen = pygame.display.set_mode((self.scale*16, self.scale*15))
    
    def displaymap(self): #check

        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        for i in range(15):
            for j in range(15):
                if self.map.map[i][j] == "0":
                    self.screen.blit(self.wallimg,self.wallrect.move(j*self.scale, i*self.scale))
                elif self.map.map[i][j] == "2":
                    if self.map.items[(i,j)] == "needle":
                        self.screen.blit(self.needleimg, self.needlerect.move(j*self.scale, i*self.scale))
                    elif self.map.items[(i,j)] == "tube":
                        self.screen.blit(self.tubeimg, self.tuberect.move(j*self.scale, i*self.scale))
                    elif self.map.items[(i,j)] == "ether":
                        self.screen.blit(self.etherimg, self.etherrect.move(j*self.scale, i*self.scale))
                elif self.map.map[i][j] == "5":
                    self.screen.blit(self.guardianimg, self.guardianrect.move(j*self.scale, i*self.scale))
                pygame.display.flip()
        self.screen.blit(self.macimg, self.macrect)
        self.screen.blit(self.macimg, self.macimg.get_rect().move(15*self.scale, 0))
        pygame.display.flip()
                

    def move(self,mac,direction):

        self.screen.blit(self.blackimg, self.macrect)

        if direction == pygame.K_UP and self.map.moveup(mac):
            self.macrect = self.macrect.move(0, -self.scale)
            mac.i = mac.i - 1
        elif direction == pygame.K_DOWN and self.map.movedown(mac) :
            self.macrect = self.macrect.move(0, self.scale)
            mac.i = mac.i + 1
        elif direction == pygame.K_LEFT and self.map.moveleft(mac) :
            self.macrect = self.macrect.move(-self.scale, 0)
            mac.j = mac.j - 1
        elif direction == pygame.K_RIGHT and self.map.moveright(mac):
            self.macrect = self.macrect.move(self.scale, 0)
            mac.j = mac.j + 1

        self.screen.blit(self.macimg, self.macrect)
        pygame.display.flip()

    def pickup(self,mac):
        if self.map.map[mac.i][mac.j] == "2" and self.map.items[(mac.i,mac.j)] not in mac.items:
            mac.items.append(self.map.items[(mac.i,mac.j)])
            if self.map.items[(mac.i,mac.j)] == "tube":
                self.screen.blit(self.tubeimg, self.tuberect.move(15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i,mac.j)] == "needle":
                self.screen.blit(self.needleimg, self.needlerect.move(15*self.scale, len(mac.items)*self.scale))
            elif self.map.items[(mac.i,mac.j)] == "ether":
                self.screen.blit(self.etherimg, self.etherrect.move(15*self.scale, len(mac.items)*self.scale))
            pygame.display.flip()
            if len(mac.items) >= 3:
                self.screen.blit(self.blackimg, self.blackrect.move(15*self.scale, self.scale))
                self.screen.blit(self.syringueimg, self.syringuerect.move(15*self.scale, self.scale))
                self.screen.blit(self.blackimg, self.blackrect.move(15*self.scale, 2*self.scale))
                self.screen.blit(self.blackimg, self.blackrect.move(15*self.scale, 3*self.scale))
            pygame.display.flip()
        elif self.map.map[mac.i][mac.j] == "5" :
            if len(mac.items) >= 3:
                print("Victory")
            else:
                print("Defeat")
            sys.exit()