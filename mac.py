class Macgyver(y, mazemap, size, scale):
    def __init__(self):
        self.x = 0
        self.y = y
        self.rect = pygame.rect(self.x, self.y)
        self.items = []
    def pickup(self, map):
        
    def combat(self, map):
        if "syringue" in self.items:
            print("VICTORY")
            sys.exit()
        else:
            print ("DEFEAT")
            sys.exit()
    def move(self, direction):
        if direction == "UP":
            if self.y > 0:
                self.y = self.y - scale
        elif direction == "DOWN":
            if self.y < size[1] - scale :
                self.y = self.y + scale
        elif direction == "LEFT":
            if self.x > 0:
                self.x = self.x - scale
        elif direction == "RIGHT":
            if self.x < size[0] - scale:
                self.x = self.x + scale