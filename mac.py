class Macgyver():
    def __init__(self,y,):
        self.x = 0
        self.y = y
        self.rect = pygame.rect(self.x, self.y)
        self.items = []
    
    def pickup(self, map):
        if map.mapArray[self.y, self.x].item:
            self.items.append(map.mapArray[self.y, self.x].itemtype)

    def combat(self, map):
        if "syringue" in self.items:
            print("VICTORY")
            sys.exit()
        else:
            print ("DEFEAT")
            sys.exit()

    def move(self, direction, size, scale, map):
        if direction == "UP":
            if self.y > 0:
                if map.mapArray[self.y - 1,self.x].pathable:
                    self.y = self.y - scale
        elif direction == "DOWN":
            if self.y < size[1] - scale :
                if map.mapArray[self.y + 1,self.x].pathable:
                    self.y = self.y + scale
        elif direction == "LEFT":
            if self.x > 0:
                if map.mapArray[self.y,self.x - 1].pathable:
                    self.x = self.x - scale
        elif direction == "RIGHT":
            if self.x < size[0] - scale:
                if map.mapArray[self.y,self.x + 1].pathable:
                    self.x = self.x + scale