# Name: Phong Ngo
# Spring 2026
# Assignment 5 - Cryptography

import math

# utility functions

def num_to_char(num):
    """ Converts the number 00-25 into a character A-Z.
        :param num: string/int - the number to convert.
        :returns: a character in the range A-Z.
    """
    return chr(int(num) + 65)


def char_to_num(c):
    """ Converts the char A-Z into a string value 00-25.
        :param c: char - the character to convert.
        :returns: a string representation of the number 00-25.
    """
    val = ord(c) - 65
    if val < 10:
        return "0" + str(val)
    return str(val)


def blocksize(n):
    """ Calculates and returns the size of a block for RSA encryption/decryption
        using the "25" rule.
        :param n: integer - the n value from an RSA key.
        :returns: an integer for the block size.
    """
    block = "25"
    while int(block) < n:
        block += "25"
    return len(block) - 2



# Place your code for mod_inv and bezout_coeffs from Assignment 3 and 4 here.
def bezout_coeffs(a, b):
  """ Uses the Extended Euclidian Algorithm to compute the Bezout coefficients of two given positive integers.
      :param a: positive integer > 0
      :param b: positive integer > 0
      :returns: tuple of the bezout coefficients (s, t).
  """
  # TODO: Iteratively or recursively calculate the values s and t using the Extended Euclidian Algorithm.
  def ext_gcd(a, b):
    if b == 0:
      return (a, 1, 0)
    else:
      g, x, y = ext_gcd(b, a % b) # recursive call
      s = y
      t = x - (a // b) * y
      return g, s, t
 
  g, s, t = ext_gcd(a, b)
  # TODO: Return the final values for s and t as a tuple (s, t)
  return (s, t)

def ext_gcd(a, b):
    if b == 0:
      return (a, 1, 0)
    else:
      g, x, y = ext_gcd(b, a % b) # recursive call
      s = y
      t = x - (a // b) * y
      return g, s, t  
      
def mod_inv(a, m):
  """ Computes the inverse of value a under modulus m.
    :param a (int) - the value to find the inverse of under modulus m.
    :param m (int) - the modulus that is > 0.
    :returns the integer inverse of a under modulus m in range [0, m-1].
    :raises: ValueError if m < 1 or if a and m are not relatively prime.
  """
  if m <= 0 : # TODO: check modulus m for validity.
    raise ValueError(f"mod_inv(a, m) does not support 0 or negative modulus m = {m}.")

  if math.gcd(a, m) != 1: # TODO: check that the gcd is relatively prime 
    raise ValueError(f"mod_inv(a, m) does not support integers that are not relatively prime.")
  
  # TODO: reduce value a to be in range [0, m-1]
  
  while a < 0:
    a += m

  # TODO: use the Extended Euclidian Algorithm to find the Bezout coefficient of value a.

  inverse = ext_gcd(a, m)[1]

  # TODO: reduce the calculated inverse to be in range [0, m-1]
  while inverse < 0:
    inverse += m

  return inverse


# ----------------- PROBLEM 1 ----------------- #

def shift_encrypt(text, k):
    """ Returns the encrypted text using a shift cipher with shift value k.
        :param text: string - the plaintext that will be encrypted.
        :param k: integer - the key, which is the shift to apply for the cipher.
        :returns: encrypted text as a string.
    """
    # convert plaintext to uppercase
    text = text.upper()
    
    # initialize encryption string
    s = ""
    
    # TODO: iterate through each character in the plaintext, if it is a space, add
    # it to the encryption string, otherwise apply the shift function using the key
    # and add the result to the encryption string.
    for char in text:
		    if char == " ":
			    s += char
		    else:
			    converted_num = char_to_num(char)
			    encrypted_num = (int(converted_num) + k) % 26
			    encrypted_char = num_to_char(encrypted_num)
			    s += encrypted_char
            
    # return the encryption string
    return s


# ----------------- PROBLEM 2 ----------------- #

def shift_decrypt(text, k):
    """ Returns decrypted text using a reversed shift cipher with shift value k.
        Note: If text was encrypted using a different shift value k, then the resulting
        decrypted text will not be correct.  The shift value k must be the same shift
        value that was used to encrypt the original plaintext.
        :param text: string - the encrypted text that was encrypted with key k, that will
        be decrypted with key k.
        :param k: integer - the key, which is the shift to apply for the cipher.
        :returns: decrypted text as a string.
    """
    # initialize decryption string
    s = ""
    
    # TODO: iterate through each character in the ciphertext, if it is a space, add
    # it to the decryption string, otherwise apply the reversed shift function using 
    # the key and add the result to the decryption string.
    for char in text:
		    if char == " ":
			    s += char
		    else:
			    converted_num = char_to_num(char)
			    decrypted_num = (int(converted_num) - k) % 26
			    decrypted_char = num_to_char(decrypted_num)
			    s += decrypted_char
            
    # return the decryption string
    return s


# # ----------------- PROBLEM 3 ----------------- #

def rsa_encrypt(text, n, e):
    """ Returns the encrypted number string using RSA encryption function: f(m) = m^e mod n,
        given the plaintext and key (n, e).
        :param text: string - the plaintext that will be encrypted.
        :param n: integer - the modulus for the RSA encryption function.
        :param e: integer - the exponent for the RSA encryption function.
        :returns: the encrypted number string.
    """
    # remove any spaces that are in the message and convert to upper case
    text = text.replace(" ", "")
    text = text.upper()
    
    # TODO: find blocksize
    block_size = blocksize(n)
    letter_per_block = block_size // 2
    # TODO: pad with X if text will be insufficient to fill all blocks
    while len(text) % letter_per_block != 0:
        text += "X"

    # TODO: convert text to numbers
    numbers = ""
    for char in text:
      numbers += char_to_num(char)

    # TODO: separate the string of numbers into a list of blocks
    blocks = []
    for i in range(0, len(numbers), block_size):
      blocks.append(numbers[i:i + block_size])

    # TODO: encrypt each block and build the ciphertext
    cipher = ""
    for block in blocks:
        m = int(block)
        c = str(pow(m, e, n))
        if len(c) < block_size:
          c = "0" * (block_size - len(c)) + c     
          # c = c.zfill(block_size)    
        cipher += c         
    # return the ciphertext
    return cipher


# # ----------------- PROBLEM 4 ----------------- #

def rsa_decrypt(text, p, q, e):
    """Returns the decrypted text using RSA decryption function: f^-1(c) = c^e' mod (p*q),
    given the encrypted number string and key (p, q, e).  Note: p and q must be the same
    prime numbers that were used to create product n when the text was encrypted.
    The value of e must also be the same.
    :param text: string - the encrypted text that will be decrypted.
    :param p: integer - the first prime number that is used to produce the product n,
    which is the modulus of the RSA decryption function.
    :param q: integer - the second prime number that is used to produce the product n,
    which is the modulus of the RSA decryption function.
    :param e: integer - the exponent for the RSA encryption function.  The exponent
    must satisfy gcd(e, (p-1)*(q-1)) = 1.
    :returns: the decrypted text as a string.
    """
    # TODO: calculate n
    n = p * q

    # TODO: find blocksize
    block_size = blocksize(n)

    # TODO: separate the encrypted string of numbers into a list of blocks
    blocks = []
    for i in range(0, len(text), block_size):
      blocks.append(text[i:i + block_size])
    # TODO: decrypt each block and build the message as a string of numbers
    inve_e = mod_inv(e, (p-1)*(q-1))
    numbers = ""
    for block in blocks:
      c = int(block)
      m = str(pow(c, inve_e, n))
      if len(m) < block_size:
        m = "0"*(block_size - len(m)) + m
      numbers += m

    # TODO: convert each of the 2 digit numbers into letters
    decrypted_text = ""
    for i in range(0, len(numbers), 2):           # range(start, stop, step)
      number = int(numbers[i:i+2])                # slice the string of numbers into 2 digit numbers
      decrypted_text += num_to_char(number)       # convert each 2 digit number into letters
	
        
    # return the dectrypted text
    return decrypted_text
