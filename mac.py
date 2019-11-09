class Macgyver():
    def __init__(self,y, map):
        self.x = 0
        self.y = y
        self.rect = pygame.rect(self.x, self.y)
        self.items = []
        self.map = map
    
    def pickup(self):
        if self.map.mapArray[self.y, self.x].item:
            self.items.append(self.map.mapArray[self.y, self.x].itemtype)

    def combat(self):
        if "syringue" in self.items:
            return "VICTORY"
        else:
            return "DEFEAT"

    def move(self, direction):
        if direction == "UP":
            if self.y > 0:
                if self.map.mapArray[self.y - 1,self.x].pathable:
                    self.y = self.y - 1
        elif direction == "DOWN":
            if self.y < self.map.size - 1 :
                if self.map.mapArray[self.y + 1,self.x].pathable:
                    self.y = self.y + 1
        elif direction == "LEFT":
            if self.x > 0:
                if self.map.mapArray[self.y,self.x - 1].pathable:
                    self.x = self.x - 1
        elif direction == "RIGHT":
            if self.x < self.map.size - 1:
                if self.map.mapArray[self.y,self.x + 1].pathable:
                    self.x = self.x + 1
        self.rect = pygame.rect(self.x, self.y)