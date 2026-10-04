def isTriangle(x:int, y:int, z:int)->bool:
    if x>=y+z:
        return False
    elif y>=x+z:
        return False
    elif z>=x+y:
        return False
    else:
        return True