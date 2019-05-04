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

def det_of_3x3(A):
    return A[0,0]*A[1,1]*A[2,2]\
            +A[0,1]*A[1,2]*A[2,0]\
            +A[0,2]*A[1,0]*A[2,1]\
            -A[0,2]*A[1,1]*A[2,0]\
            -A[2,1]*A[1,2]*A[0,0]\
            -A[2,2]*A[1,0]*A[0,1]

def cramers_rule(A):
    x = np.zeros(3)
    for i in range(3):
        x[i] = det_of_3x3(A[:,i])/det_of_3x3(A)

A = create_matrix(3)
b = list(create_b(3))

A_1, A_2, A_3= list(A.T[0,:]),list(A.T[1,:]), list(A.T[2,:])

A_b_1 = np.array([b,A_2,A_3]).T
A_b_2 = np.array([A_1,b,A_3]).T
A_b_3 = np.array([A_1,A_2,b]).T

A_i = [A_b_1, A_b_2, A_b_3] 

x = [det_of_3x3(a_i)/det_of_3x3(A) for a_i in A_i]
print('Result x: ',x)
R = np.dot(A,x)-b
print('Residual vector R: ',R)
