def isPathable(mazemap,x,y):
    maxima = mazemap.shape[0]
    if x>maxima or y>maxima or x<0 or y<0:
        return False
    elif mazemap[y,x].pathable:
        return True
    else:
        return isPathable(mazemap,x+1,y) or isPathable(mazemap,x-1,y) or isPathable(mazemap,x,y+1) or isPathable(mazemap,x,y-1)