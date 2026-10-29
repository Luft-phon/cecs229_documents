import math


""" ----------------- PROBLEM 1 ----------------- """

class Vec:
    def __init__(self, contents=[]):
        """ Constructor defaults to empty vector
        :param contents: list type; list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents

    def __abs__(self):
        """ Overloads the built-in function abs(v) to return the Euclidean norm of the vector.
        :returns: float type; the Euclidean norm of the vector.
        """
        # TODO: Find the Euclidian norm of the vector.
        sum = 0
        for x in self.elements:
            sum = sum + pow(x, 2)
        magnitude = math.sqrt(sum)  
        # TODO: Return correct result.
        return magnitude

    def __add__(self, other):
        """ Overloads the + operator to support Vec + Vec
        :raises: ValueError if vectors are not same length.
        :returns: Vec type; a Vec object that is the sum vector of this Vec and 'other' Vec
        """
        # TODO: Add self and other vector objects.
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be the same length.")
        v = []
        for i in range(len(self.elements)):
            totals = self.elements[i] + other.elements[i]
            v.append(totals)
        # TODO: Return resulting vector object
        return Vec(v)

    def __sub__(self, other):
        """ Overloads the - operator to support Vec - Vec
        :raises: ValueError if vectors are not same length
        :returns: Vec type; a Vec object that is the difference vector of this Vec and 'other' Vec
        """
        # TODO: Add self and other vector objects.
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be the same length.")
        v = []
        for i in range(len(self.elements)):
            totals = self.elements[i] - other.elements[i]
            v.append(totals)
        # TODO: Return resulting vector object
        return Vec(v)

    def __mul__(self, other):
        """ Overloads the * operator to support
              - Vec * Vec (dot product) raises ValueError if vectors are not
                same length in the case of dot product; returns scalar
              - Vec * float (component-wise product); returns Vec object
              - Vec * int (component-wise product); returns Vec object
        """
        scalar = 0
        if type(other) == Vec:  # define dot product
            # TODO: Implement dot product
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must be the same length.")
            for i in range(len(self.elements)):
                scalar += self.elements[i] * other.elements[i]
            # TODO: Return resulting scalar value
            return scalar
            

        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            # TODO: Implement scalar multiplication.
            v = []
            for i in range(len(self.elements)):
                mul = other * self.elements[i]
                v.append(mul) 
            # TODO: Return the resulting vector.
            return Vec(v)

    def __rmul__(self, other):
        """ Overloads the * operation to support
              - float * Vec; returns Vec object
              - int * Vec; returns Vec object
        """
        # TODO: Implement scalar multiplication.
        v = self.__mul__(other)
        # TODO: Return the resulting vector.
        return v

    def __str__(self):
        """Returns string representation of this Vec object."""
        return str(self.elements)
