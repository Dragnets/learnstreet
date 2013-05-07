#Basic calculator project
import math
def cube(n):
    return n**3
    """
    Return the cube of a number, an integer provided as 'n'
    """
    "REPLACE THIS CODE WITH YOUR CUBE METHOD"

def squareroot(n):
    if n < 0:
        return "NAN"
    else:
        return math.sqrt(n)
    """
    Returns the square root of the number n. If n < 0, 
    then return the string "NAN" (Not A Number)
    """
    "REPLACE THIS CODE WITH YOUR SQUAREROOT METHOD"

def negate(n):
    return -n
    """ Return the negative value of the argument 'n'.
    """
    "REPLACE THIS CODE WITH YOUR NEGATE METHOD"

def factorial(n):
    if n == 0:
        return 1
    if n<0:
        return "NAN"
    return n*factorial(n-1)
    """Return n factorial
    The factorial of anything <= 1 is 1.
    The factorial of any integer greater than 1 is the product of all
    the integers from 1 to the number itself. For example,
    4 factorial = 1 x 2 x 3 x 4 = 24.
    """
    "REPLACE THIS CODE WITH YOUR FACTORIAL METHOD"
