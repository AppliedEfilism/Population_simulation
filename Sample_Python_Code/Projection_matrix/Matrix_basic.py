import numpy as np

# define matrices
A = np.array([[0.4, 1.2],
              [0.6, 0.8]]) 

B = np.array([[0.1, 0.1],
              [0.2, 0.1]])

# print the matrices
print(f"A={A}")
print(f"B={B}") 

# print the matrix elements
print(f"a11={A[0,0]}, a12={A[0,1]}, a21={A[1,0]}, a22={A[1,1]}")

# print the sum of matrices
C = A + B
print(f"A+B={C}")

# print the product of matrices
N = A @ B
print(f"AB={N}")

A=np.array([[1, 2],
            [0, 1]])
B=np.array([[1, -1], 
            [1, 0]])
print(f"AB={A@B}")

# check the commutativity
A=np.array([[1, 2],
            [0, -1]])
B=np.array([[1, 0],
            [1, 1]])

print(f"AB={A@B}")
print(f"BA={B@A}")

