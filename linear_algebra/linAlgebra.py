import numpy as np

def create_matrix(n, eps=10**(-5)):
    matrix = np.zeros((n,n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i-1,j-1] = (np.cos(i+eps)+np.sin(j+eps))**(-1)
    return matrix

def create_b(n, eps=10**(-5)):
    b = np.zeros(n)
    for i in range(1,n+1):
        b[i-1] = (1/i)-eps
    return b

def create_linear_equation(n, eps = 10**(-5)):
    A = create_matrix(n, eps)
    b = create_b(n, eps)
    return (A,b)

def determinant_of_3x3(A):
    return A[0,0]*A[1,1]*A[2,2]\
            +A[0,1]*A[1,2]*A[2,0]\
            +A[0,2]*A[1,0]*A[2,1]\
            -A[0,2]*A[1,1]*A[2,0]\
            -A[2,1]*A[1,2]*A[0,0]\
            -A[2,2]*A[1,0]*A[0,1]

A = create_matrix(3)
print(A)
print(determinant_of_3x3(A))
print(np.linalg.det(A))
