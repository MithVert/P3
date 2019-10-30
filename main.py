import numpy as np
import pygame as pg
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
# os.chdir("/home/gery/Documents/OC/Macgyver/code")
from map import *
from case import *
# from errors import *
# from game  import *
# from mac  import *
# from item import *
import parameters as par
import functions as fct
mac = pygame.image.load("MacGyver50.png")