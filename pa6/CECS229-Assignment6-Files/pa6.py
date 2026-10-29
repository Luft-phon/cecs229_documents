import math

""" ----------------- PROBLEM 1 ----------------- """


def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    :param S: set type; a set of complex numbers
    :param z0: complex type; a complex number
    :return: set type; a set consisting of points in S translated by z0
    """
    # TODO: Implement this function
    complex_number = set()
    for w in S:
        w = w + z0
        complex_number.add(w)
    return complex_number  # TODO: Return correct result


""" ----------------- PROBLEM 2 ----------------- """


def scale(S, k):
    """
    scales the complex numbers of set S by k.
    :param S: set type; a set of complex numbers
    :param k: float type; positive real number
    :return: set type; a set consisting of points in S scaled by k
    :raise: raises ValueError if k <= 0
    """
    # TODO: Implement this function.
    if k <= 0:
        raise ValueError("k must be a positive real number")
    complex_number = set()
    for w in S:
        w = w * k
        complex_number.add(w)
    return complex_number # TODO: Return correct result


""" ----------------- PROBLEM 3 ----------------- """


def rotate(S, tau):
    """
    rotates the complex numbers of set S by tau radians.  
    :param S: set type; - set of complex numbers
    :param tau: float type; radian measure of the rotation value. 
                If negative, the rotation is clockwise.  
                If positive the rotation is counterclockwise. 
                If zero, no rotation.
    :returns: set type; a set consisting of points in S rotated by tau radians
    """
    # TODO: Implement this function. 
    complex_number = set()
    for w in S:
        w = w * (math.cos(tau) + 1j * math.sin(tau))
        complex_number.add(w)
    return complex_number # TODO: Return correct result
