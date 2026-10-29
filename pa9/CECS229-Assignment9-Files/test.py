import pa8
import pa9

def test():
    
    print("Testing Problem 1...")
    # Write your test cases for Problem 1 here
    print("Correct pivot index:")
    print("(2, 1)")
    print("Pivot Index:")
    print(pa9.pivot_index(1,1,pa8.Matrix([[0, 1, 0],[1, 0, 0]])))
    if pa9.pivot_index(1,1,pa8.Matrix([[0, 1, 0],[1, 0, 0]])) == (2,1):
        print("Test Case 1 Passed")
    else:
        print("Test Case 1 Failed")

    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here
    print("Original Matrix:")
    matrix = pa8.Matrix([
    [0, 5, 9, 3],
    [-4, 4, -5, -3],
    [6, -3, -7, 4],
    [8, 10, -8, 7],
    [-7, -1, 7, -10]
    ])
    print(matrix)
    print("REF Matrix:")
    print(pa9.ref(matrix))
    if pa9.ref(matrix) == pa8.Matrix([
    [1.0, -1.0, 1.25, 0.75],
    [0.0, 1.0, 1.8, 0.6000000000000001],
    [-0.0, -0.0, 1.0, 0.1155778894472362],
    [-0.0, -0.0, -0.0, 1.0],
    [0.0, 0.0, 0.0, 0.0]
    ]):
        print("Test Case 2 Passed")
    else:
        print("Test Case 2 Failed")
    
    print("Testing Problem 3...")
    # Write your test cases for Problem 3 here
    
    print("Testing Problem 4...")
    # Write your test cases for Problem 4 here
    
    print("Testing Problem 5...")
    # Write your test cases for Problem 5 here
    
    print("Testing Problem 6...")
    # Write your test cases for Problem 6 here
if __name__ == "__main__":
    test()