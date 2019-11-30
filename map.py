import random as rd
import sys

class Map():

    def __init__(self):
        
        self.map = []

    def readmap(self,mapfile): #check

        file = open(mapfile,"r", encoding='utf8')
        lines = file.readlines()
        for i in lines:
            self.map.append(i[:-1])

    def placeitems(self): #check

        maxima = 0

        itemlist=["needle","ether","tube"]
        itemcase=[]

        for i in self.map :
            maxima = maxima + i.count("1")
        
        itemplaces = rd.sample(range(maxima),3)
        c = 0
        for i in range(len(self.map)) :
            for j in range(len(self.map[i])) :
                if self.map[i][j] == "1" :
                    c = c + 1
                    if c in itemplaces:
                        self.map[i] = self.map[i][:j]+"2"+self.map[i][j+1:]
                        itemcase.append((i,j))
        
        self.items = {}

        for i in range(3):
            self.items[itemcase[i]] = itemlist[i]
            
    
    def pickedup(self,i,j):
    
        if self.map[i][j] == "2":
            self.map[i] = self.map[i][:j]+"1"+self.map[i][j+1:]
            return self.items[(i,j)]
        else:
            return None
    
    def startermac(self): #check

        for i in range(15):
            if int(self.map[i][0]) > 0:
                return i