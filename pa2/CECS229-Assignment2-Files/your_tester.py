from pa2 import b_rep
from pa2 import binary_add
from pa2 import binary_mul

problem1 = [
    (10, 2, "1010"),
    (40, 2, "101000"),
    (10, 8, "12"),
    (40, 8, "50"),
    (10, 16, "A"),
    (40, 16, "28"),
]

problem2 = [
    ("1010", "1010", "10100"),
    ("1010", "1010", "10100"),
    ("1010", "1010", "10100"),
    ("1010", "1010", "10100"),
    ("1010", "1010", "10100"),
    ("1010", "1010", "10100"),
]

problem3 = [
    ("101101", "111", "100111011"),
    ("110011", "1011", "1000110001"),
    ("1010", "1010", "1100100"),
]

def test():
    print("Testing Problem 1...")
    for a, b, expected in problem1:
        print(f"Testing b_rep({a}, {b})")
        # print(f"Expected: {expected}")
        # print(f"Returned: {b_rep(a, b)}")
        if b_rep(a, b) == expected:
            print("Test passed.")
        else:
            print("Test failed.")
        print("-" * 50)
    # Write your test cases for Problem 1 here

    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here
    for a, b, expected in problem2:
        print(f"Testing binary_add({a}, {b})")
        # print(f"Expected: {expected}")
        # print(f"Returned: {binary_add(a, b)}")
        if binary_add(a, b) == expected:
            print("Test passed.")
        else:
            print("Test failed.")
        print("-" * 50)

    print("Testing Problem 3...")
    # Write your test cases for Problem 3 here
    for a, b, expected in problem3:
        print(f"Testing in binary_mul({a}, {b})")
        if binary_mul(a, b) == expected:
            print("Test passed.")
        else:
            print("Test failed.")
        print("-" * 50)

if __name__ == "__main__":
    test()

