import numpy as np

def create_matrix(n, eps=10**(-5)):
    matrix = np.zeros((n,n))
    for i in range(1,n):
        for j in range(1,n):
            matrix[i,j] = (np.cos(i+eps)+np.sin(j+eps))**(-1)

    return matrix


def create_b(n, eps=10**(-5)):
    b = np.zeros(n)
    for i in range(1,n):
        b[i] = (1/i)-eps
    return b

def create_linear_equation(n, eps = 10**(-5)):
    A = create_matrix(n, eps)
    b = create_b(n, eps)
    return (A,b)

print(create_linear_equation(4))
