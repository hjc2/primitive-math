
def add(x, y): #adds two numbers
    if(y > 0):
        return(1 + add(x, y - 1))
    else:
        return(x)

"""docstring"""
def multiply(x, y):
    if(y > 1):
        return(add(x, multiply(x, y - 1)))
    if(y == 1):
        return(x)