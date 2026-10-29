from pa4 import mod_inv, solve_linear_congruence

test_case_1 = [
    # ===== VALID CASES =====
    (3, 11, 4),      # 3*4 = 12 ≡ 1 mod 11
    (5, 13, 8),      # 5*8 = 40 ≡ 1 mod 13
    (7, 17, 5),      # 7*5 = 35 ≡ 1 mod 17
    (11, 19, 7),     # 11*7 = 77 ≡ 1 mod 19
    (1, 7, 1),       # 1 luôn có inverse là 1
    (10, 17, 12),    # 10*12 = 120 ≡ 1 mod 17

    # ===== FAIL CASES =====
    (2, 0, ValueError),      # modulus = 0
    (3, 1, ValueError),      # modulus = 1 (không có inverse)
    (0, 7, ValueError),      # a = 0
    (6, 9, ValueError),      # gcd(6,9) != 1
    (12, 18, ValueError),    # gcd != 1
    (-3, 11, 7),             # nếu hỗ trợ normalize: -3 ≡ 8 mod 11 → inverse = 7
    (3.5, 11, TypeError),    # không phải số nguyên
    ("3", 11, TypeError),    # sai kiểu dữ liệu
]

def test():
    print("Testing Problem 1...")
    # Write your test cases for Problem 1 here
    for a, b, expected in test_case_1:
        result = mod_inv(a, b)
        print(f"Expected: {expected}, Result: {result}")
        if expected == result:
            print("Pass")
        else:
            print("Fail")
    


    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here

if __name__ == "__main__":
    test()



