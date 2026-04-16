'''
Program: Perform matrix operations with validation
'''

import numpy as np

try:
    # Input matrix size
    r1 = int(input("Rows of Matrix A: "))
    c1 = int(input("Columns of Matrix A: "))

    r2 = int(input("Rows of Matrix B: "))
    c2 = int(input("Columns of Matrix B: "))

    print("Enter Matrix A elements:")
    A = np.array([list(map(int, input().split())) for _ in range(r1)])

    print("Enter Matrix B elements:")
    B = np.array([list(map(int, input().split())) for _ in range(r2)])

    # Addition & Subtraction
    if A.shape == B.shape:
        print("Addition:\n", A + B)
        print("Subtraction:\n", A - B)
    else:
        raise ValueError("Matrices must have same dimensions for addition/subtraction")

    # Multiplication
    if c1 == r2:
        print("Multiplication:\n", np.dot(A, B))
    else:
        raise ValueError("Invalid dimensions for multiplication")

except Exception as e:
    print("Error:", e)
