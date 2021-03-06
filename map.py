import random as rd
import sys


class Map():

    """this class enables to get all the maze's data
    and to place items, macgyver and the guardian in the maze"""

    def __init__(self):

        self.map = []

    def __getitem__(self, ij):
        return self.map[ij[0]][ij[1]]

    def readmap(self, mapfile):
        # reading file map.txt
        file = open(mapfile, "r", encoding='utf8')
        lines = file.readlines()
        # removing "/n" at the end of each line while creating the map object
        for i in lines:
            self.map.append(i[:-1])

    def placeitems(self):

        maxima = 0
        itemlist = ["needle", "ether", "tube"]
        itemcase = []

        # getting the number of maze's case eligible to have an object
        for i in self.map:
            maxima = maxima + i.count("1")
        # chosing 3 different cases among them
        itemplaces = rd.sample(range(maxima), 3)
        c = 0
        # browsing map object while placing the items on the chosen cases
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "1":
                    if c in itemplaces:
                        self.map[i] = self.map[i][:j]+"2"+self.map[i][j+1:]
                        itemcase.append((i, j))
                    c = c + 1
        # distinguishing one item from the other by listing and naming them
        self.items = {}
        for i in range(3):
            self.items[itemcase[i]] = itemlist[i]

    def placeguardian(self):
        # browsing last column of the map to place the guardian there
        for i in range(len(self.map)):
            if self.map[i][-1] == "1":
                self.map[i] = self.map[i][:-1] + "5"
                break

    def startermac(self):
        # browsing first column of the map to place macgyver there
        for i in range(15):
            if int(self.map[i][0]) > 0:
                return i

    def pickedup(self, i, j):
        # returning the object to pickup in this maze's case
        if self.map[i][j] == "2":
            self.map[i] = self.map[i][:j]+"1"+self.map[i][j+1:]
            return self.items[(i, j)]
        else:
            return None



    def canmoveup(self, mac):

        """ checks wether mac can move up
        to a maze's case without going through 
        the walls or out of the map, returns Bool"""

        if mac.i > 0:
            if int(self.map[mac.i-1][mac.j]) > 0:
                return True
            else:
                return False
        else:
            return False

    def canmovedown(self, mac):

        """ checks wether mac can move down
        to a maze's case without going through 
        the walls or out of the map, returns Bool"""

        if mac.i < 14:
            if int(self.map[mac.i+1][mac.j]) > 0:
                return True
            else:
                return False
        else:
            return False

    def canmoveleft(self, mac):

        """ checks wether mac can move left
        to a maze's case without going through 
        the walls or out of the map, returns Bool"""

        if mac.j > 0:
            if int(self.map[mac.i][mac.j-1]) > 0:
                return True
            else:
                return False
        else:
            return False

    def canmoveright(self, mac):

        """ checks wether mac can move right
        to a maze's case without going through 
        the walls or out of the map, returns Bool"""

        if mac.j < 14:
            if int(self.map[mac.i][mac.j+1]) > 0:
                return True
            else:
                return False
        else:
            return False

