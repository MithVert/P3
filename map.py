
class Map():

    def __init__(self,mapsize):

        self.mapArray = np.full((mapsize,mapsize),Case())
        self.itemlist=["needle","ether","tube"]
        self.size = mapsize

    def readmap(self,mapfile):

        file = open(mapfile,'r')
        for i in range(self.size):
            line=file.readline()
            for j in range(self.size):
                if line[j]=="1":
                    self.mapArray[i,j].pathable=True
                elif line[j]=="0":
                    self.mapArray[i,j].wall=True
    
    def randmap(self):

        depart = randint(self.size-1)
        mazeExit=False
        y=depart
        x=0
        while mazeExit == False:
            self.mapArray[y,x].pathable = True
            listMove=[]
            listMove.append(("x",1))
            listMove.append(("x",1))
            listMove.append(("x",1))
            if x>0:
                listMove.append(("x",-1))
            if y>0:
                listMove.append(("y",-1))
            if y < self.size-1:
                listMove.append("y",1)
            choiceMove = listMove[randint(len(listMove)-1)]
            if choiceMove[0] == "x":
                x = x + choiceMove[1]
                if x == self.size-1:
                    mazeExit=True
                    self.mapArray[y,x].guardian=True
                    self.mapArray[y,x].pathable=True
            else:
                y = y + choiceMove[1]
        for i in self.mapArray:#placing walls randomly
            for j in i:
                if not(j.wall or j.pathable):
                    if randint(1):
                        j.pathable=False
                        j.wall=True
        for i in range(self.size):#defining which case is a path or a wall
            for j in range(self.size):
                if not(j.wall or j.pathable):
                    if isPathable(self.mapArray,j,i):
                        self.mapArray[j,i].pathable=True
                        self.mapArray[j,i].wall=False
                    else:
                        self.mapArray[j,i].wall=True
    
    def placeitems(self):

        for item in self.itemlist:
            x,y = randint(self.size), randint(self.size)
            while not(self.mapArray[y,x].pathable) or self.mapArray[y,x].item:
                x,y = randint(self.size), randint(self.size)
            self.mapArray[y,x].item = True
            self.mapArray[y,x].itemtype = item
    
    def pickedup(self,x,y):
    
        if self.mapArray[y,x].item:
            self.mapArray[y,x].item = False
            return self.mapArray[y,x].itemtype
        else:
            return None