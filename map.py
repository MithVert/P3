import numpy as np
from case import *
from functions import *
import random as rd
import sys

class Map():

    def __init__(self,mapsize):

        self.mapArray = np.full((mapsize,mapsize),Case())
        self.itemlist=["needle","ether","tube"]
        self.size = mapsize

    def readmap(self,mapfile):
        file = open(mapfile,'r')
        for i in range(15):
            line=file.readline()
            for j in range(15):
                if line[j]=="1":
                    self.mapArray[i,j].pathable=True
                elif line[j]=="0":
                    self.mapArray[i,j].wall=True
    
    def randmap(self):

        depart = rd.randint(0, 15)
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
                listMove.append(("y",1))
            choiceMove = listMove[rd.randint(0, len(listMove)-1)]
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
                    if rd.randint(0, 1):
                        j.pathable=False
                        j.wall=True
        for i in range(self.size):#defining which case is a path or a wall
            for j in range(self.size):
                if not(self.mapArray[j,i].wall or self.mapArray[j,i].pathable):
                    if isPathable(self.mapArray,j,i):
                        self.mapArray[j,i].pathable=True
                        self.mapArray[j,i].wall=False
                    else:
                        self.mapArray[j,i].wall=True
    
    def placeitems(self):
        
        for item in self.itemlist:
            x,y = rd.randint(0, 15), rd.randint(0, 15)
            while not(self.mapArray[y,x].pathable) or self.mapArray[y,x].item:
                x,y = rd.randint(0, 15), rd.randint(0, 15)
            self.mapArray[y,x].item = True
            self.mapArray[y,x].itemtype = item
    
    def pickedup(self,x,y):
    
        if self.mapArray[y,x].item:
            self.mapArray[y,x].item = False
            return self.mapArray[y,x].itemtype
        else:
            return None
    
    def startermac(self):
        for i in range(15):
            if self.mapArray[i,0].pathable:
                return i
        return 0