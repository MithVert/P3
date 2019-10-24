class Map():
    def __init__(self,file=mapfile, rand=False):
        self.mapArray = np.full((mapsize,mapsize),Case())
        self.itemlist=["needle","ether","tube"]
        if not(rand):
            file = open(mapfile,'r')
            for i in range(mapsize):
                line=file.readline()
                for j in range(mapsize):
                    if line[j]=="1":
                        self.mapArray[i,j].pathable=True
                        if i=="0":
                            global mac=Macgyver(j)
                    elif line[j]=="0":
                        self.mapArray[i,j].wall=True
                    else:
                        #error
        else:#randomized map
            depart = randint(mapsize-1)#creating the path to go from one side to another
            mazeExit=False
            y=depart
            global mac=Macgyver(depart)
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
                if y < mapsize-1:
                    listMove.append("y",1)
                choiceMove = listMove[randint(len(listMove)-1)]
                if choiceMove[0] == "x":
                    x = x + choiceMove[1]
                    if x == mapsize-1:
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
            for i in range(mapsize):#defining which case is a path or a wall
                for j in range(mapsize):
                    if not(j.wall or j.pathable)
                        if isPathable(self.mapArray,j,i):
                            self.mapArray[j,i].pathable=True
                            self.mapArray[j,i].wall=False
                        else:
                            self.mapArray[j,i].wall=True