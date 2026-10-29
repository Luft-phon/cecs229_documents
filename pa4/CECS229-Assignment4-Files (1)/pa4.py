# Name: Phong Ngo
# Assignment #4
# Spring 2026

import math

# Place any necessary functions from Assignment 3 here.

def ext_gcd(a, b):
    if b == 0:
      return (a, 1, 0)
    else:
      g, x, y = ext_gcd(b, a % b) # recursive call
      s = y
      t = x - (a // b) * y
      return g, s, t


""" ----------------- PROBLEM 1 ----------------- """

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


""" ----------------- PROBLEM 2 ----------------- """

def solve_linear_congruence(a, b, m, low, high):
  """ Computes all solutions to the equivalence ax ≡ b (mod m) that are in the range [low, high].
    :param a (int) - the coefficient of variable x.
    :param b (int) - the value that a * x is congruent to under modulus m.
    :param m (int) - the modulus that is > 0.
    :param low (int) - the lower bound for the solution range.
    :param high (int) - the upper bound for the solution range.
    :raises: ValueError if high < low or if m < 1.
    """
  if high < low: # TODO: check if high < low.
    raise ValueError(f"solve_linear_congruence() does not support the upper bound {high} less than the lower bound {low}")
  if m < 1: # TODO: check modulus m for validity.
    raise ValueError(f"solve_linear_congruence() does not support 0 or negative modulus m = {m}")
  
  # TODO: generate a list of solutions to the linear congruence a*x=b(mod m) by iterating through the range and testing each value to see if it is a solution and adding it to the list.
  solutions = [] 
  for x in range(low, high + 1):
    if a * x % m == b % m:
      solutions.append(x)

  return solutions

  
