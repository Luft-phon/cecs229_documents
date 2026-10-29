# Name: Phong Ngo
# Assignment #2
# Spring 2026


# ---------------- PROBLEM 1 ---------------- #
def b_rep(n, b):
    """ Converts decimal integer n into base b and returns it as a string. The base b must be an integer between 2-36."""
    digits = []  # stores the digits of the b-representation of n
    q = n
    while q != 0:
        digit = q % b  # TODO: update 'digit' to be the remainder of q divided by b
        if b > 10 and digit > 9:  # TODO: update for other bases > 10
            hex_dict = {
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
                16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
                22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R',
                28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
                34: 'Y', 35: 'Z'
            } # TODO: update for other bases > 10
            # TODO: update digit
            digit = hex_dict[digit]
        digits.append(digit)
        q = q // b  # TODO: update q to the correct value.
    return ''.join(map(str, reversed(digits)))  # TODO: return the string of digits


# ---------------- PROBLEM 2 ---------------- #
def binary_add(a, b):
    """ Adds binary strings a and b and returns the resulting binary string. """
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b

    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])

        # TODO: update result += ....
        result += str((a_i + b_i + carry) % 2)

        # TODO: update carry =
        # carry = (a_i + b_i + carry) // 2
        if (a_i + b_i + carry) >= 2:
            carry = 1
        else:
            carry = 0
    result = "".join(reversed(result))

    if carry == 1:
        result = str(carry) + result # TODO: update 'result' to the correct value."
    return result  # TODO: return the appropriate string


# ---------------- PROBLEM 3 ---------------- #
def binary_mul(a, b):
    """ Multiplies binary strings a and b and returns the resulting binary string. """
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            partial_products.append(b + "0" * i) #TODO: append the appropriate partial product
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products[0]) #TODO: input the correct arguments
        del partial_products[0]
    return result  # TODO: return the appropriate result
