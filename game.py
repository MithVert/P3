import pygame

class Game():
    def __init__(self, mac, listinit):
        self.mac = mac
        self.displaysize = listinit[0]
        self.scale = listinit[1]
        self.macimg = listinit[2]
        self.macrect = self.macimg.get_rect()
        self.guardianimg = listinit[3]
        self.guardianrect = self.guardianimg.get_rect()
        self.wallimg = listinit[4]
        self.wallrect = self.wallimg.get_rect()
        self.blackimg = listinit[5]
        self.blackrect = self.blackimg.get_rect()
        self.syringueimg = listinit[6]
        self.syringuerect = self.syringueimg.get_rect()
        self.etherimg = listinit[7]
        self.etherrect = self.etherimg.get_rect()
        self.tubeimg = listinit[8]
        self.tuberect = self.tubeimg.get_rect()
        self.needleimg = listinit[9]
        self.needlerect = self.needleimg.get_rect()
        self.screen = pygame.display.set_mode(self.displaysize)
    
    def displaymap(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        for i in range(15):

            for j in range(15):

                if self.mac.map.mapArray[j,i].wall:

                    self.wallrect.move(i*self.scale,j*self.scale)
                    self.screen.blit(self.wallimg,self.wallrect)

                elif self.mac.map.mapArray[j,i].guardian:

                    self.guardianrect.move(i*self.scale,j*self.scale)
                    self.screen.blit(self.guardianimg,self.guardianrect)
                    

                elif self.mac.map.mapArray[j,i].item:

                    if self.mac.map.mapArray[j,i].itemtype == "ether":

                        self.etherrect.move(i*self.scale,j*self.scale)
                        self.screen.blit(self.etherimg,self.etherrect)

                    elif self.mac.map.mapArray[j,i].itemtype == "tube":

                        self.tuberect.move(i*self.scale,j*self.scale)
                        self.screen.blit(self.tubeimg,self.tuberect)

                    elif self.mac.map.mapArray[j,i].itemtype == "needle":

                        self.needlerect.move(i*self.scale,j*self.scale)
                        self.screen.blit(self.needleimg,self.needlerect)
                        
                pygame.display.flip()

        pygame.display.flip()

    def move(self,direction):
        self.screen.blit(self.blackimg, self.macrect)
        self.mac.move(direction)
        self.macrect.move(self.mac.x, self.mac.y)
        self.screen.blit(self.macimg, self.macrect)
        self.mac.pickup()
        if self.mac.map.mapArray[self.mac.y,self.mac.x].guardian:
            self.mac.combat()
        pygame.display.flip()