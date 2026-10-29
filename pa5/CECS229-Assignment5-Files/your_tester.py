from pa5 import shift_encrypt, shift_decrypt, rsa_encrypt, rsa_decrypt


def test():
    print("Testing Problem 1...")
    # Write your test cases for Problem 1 here
    text = "PIRATE ATTACK"
    k = 10
    expected = "ZSBKDO KDDKMU"
    received = shift_encrypt(text, k)

    if expected == received:
        print("Test pass")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    else:
        print("Test fail")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    print("\n")

    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here
    text = "VCHSAPUL"
    k = 7
    expected = "OVALTINE"
    received = shift_decrypt(text, k)

    if expected == received:
        print("Test pass")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    else:
        print("Test fail")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    print("\n")

    print("Testing Problem 3...")
    # Write your test cases for Problem 3 here
    text = "UPLOADS"
    n = 3233
    e = 17
    expected = "2545275712111718"
    received = rsa_encrypt(text, n, e)

    if expected == received:
        print("Test pass")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    else:
        print("Test fail")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    print("\n")

    print("Testing Problem 4...")
    # Write your test cases for Problem 4 
    text = "09810461"
    p = 43
    q = 59
    e = 13
    expected = "HELP"
    received = rsa_decrypt(text, p, q, e)

    if expected == received:
        print("Test pass")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    else:
        print("Test fail")
        print(f"Expected: {expected}")
        print(f"Received: {received}")
    
if __name__ == "__main__":
    test()
    






