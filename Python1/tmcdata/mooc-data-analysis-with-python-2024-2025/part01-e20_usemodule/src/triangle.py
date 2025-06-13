__version__ = "1.0.0"
__author__ = "XINJIAN QI"
__doc__ ="triangle functions"

from math import sqrt

def hypotenuse (l1:int, l2: int):
    """Computes the length of the hypotenuse of a right-angled triangle
    with sides of length a and b."""    
    return sqrt(l1 ** 2 + l2 ** 2)


def area (l1: int, l2: int):
    """Computes the area of a right-angled triangle
    with sides of length a and b."""
    return l1 * l2 * 1/2
 
