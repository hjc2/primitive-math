
def increment(x):
    """increments a number \n
    f(x) = x + 1"""
    return(x + 1)


def decrement(x):
    """decrements a number \n 
    f(x) = x - 1"""
    return(x - 1)


def add(x, y):
    """adds two numbers \n
    f(x, y) = x + y
    """
    if(y > 0):
        return(increment(add(x, y - 1)))
    else:
        return(x)


def multiply(x, y):
    """multiplies two numbers \n
    f(x) = x * y 
    """
    if(y > 1):
        return(add(x, multiply(x, y - 1)))
    if(y == 1):
        return(x)


def power(x, y):
    """takes the power of a number \n
    f(x) = x^y
    """
    if(y >= 1):
        return(multiply(x, power(x, y - 1)))
    if(y == 0):
        return(1)
