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

    def placeguardian(self):
        
        for i in range (len(self.map)):
            if self.map[i][-1] == "1":
                self.map[i] = self.map[i][:-1] + "5"
                break
            
    
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
    
    def moveup(self,mac):

        if mac.i > 0 :
            if int(self.map[mac.i-1][mac.j]) > 0 :
                return True
            else :
                return False
        else :
            return False

    def movedown(self,mac):

        if mac.i < 14 :
            if int(self.map[mac.i+1][mac.j]) > 0 :
                return True
            else:
                return False
        else:
            return False
    
    def moveleft(self,mac):

        if mac.j > 0:
            if int(self.map[mac.i][mac.j-1]) > 0 :
                return True
            else:
                return False
        else :
            return False
    
    def moveright(self,mac):

        if mac.j < 14 :
            if int(self.map[mac.i][mac.j+1]) > 0 :
                return True
            else :
                return False
        else :
            return False