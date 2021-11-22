
def increment(x):
    """increments a number"""
    return(x + 1)

def decrement(x):
    """decrements a number \n 
    f(x) = x - 1"""
    return(x - 1)

def add(x, y):
    """adds two numbers"""
    if(y > 0):
        return(increment(add(x, y - 1)))
    else:
        return(x)

def multiply(x, y):
    """multiplies two numbers"""
    if(y > 1):
        return(add(x, multiply(x, y - 1)))
    if(y == 1):
        return(x)