from pa1 import congruent_to

def test():
    print("Testing Problem 1...\n")

    tests = [
        (3, 5, -10, 15),
        (12, 15, -29, -11),
        (-20, 4, 3, 21),
        (0, 3, -5, 5),
        (7, 2, 0, 10)
    ]

    for a, m, low, high in tests:
        result = congruent_to(a, m, low, high)
        print(f"Testing Problem 1: a = {a}, m = {m}, low = {low}, high = {high}")
        print(f"Returned: {result}")
        print("-" * 50)
        