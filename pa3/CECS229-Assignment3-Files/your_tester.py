from pa3 import gcd, primes, bezout_coeffs


def test():
    print("Testing Problem 1...")
    # Write your test cases for Problem 1 here
    a = 2
    b = 20
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    received = primes(a, b)
    print(f"Testing primes({a}, {b})....\nExpected: {expected}\nReceived: {received}")

    if expected == received:
        print("\nTest PASSED!")
    else:
        print("\nTest FAILED.")


    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here
    a = 20 
    b = 10
    expected = 10
    received = gcd(a, b)
    print(f"Testing gcd({a}, {b}):")
    print(f"Expected: {expected}")
    print(f"Received: {received}")

    if expected == received:
        print("\nTest PASSED!")
    else:
        print("\nTest FAILED.")

    print("Testing Problem 3...")
    # Write your test cases for Problem 3 here

if __name__ == "__main__":
    test()
