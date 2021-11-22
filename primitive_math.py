
def add(x, y):
    if(y > 0):
        return(1 + add(x, y - 1))
    else:
        return(x)