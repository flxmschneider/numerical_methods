import numpy as np

def y(x):
    # Function from Exercise 1
    return 3+200*x-300*x**2+4*x**3-x**4

def y_2(x):
    # Funciton from Exercise 2
    return np.cos(2*np.pi*8/64*x)+0.5*np.cos(2*np.pi*24/64*x)-0.5*np.cos(2*np.pi*(8/3)/64*x)

def evaluate_y():
    N = 100
    I = np.linspace(-10,10,N)
    return [y(i) for i in I]

def find_root():
    # Finding a root by checking for sign change
    x = np.linspace(-10, 10,100)
    y = evaluate_y()
    sign_change = []
    for i in range(len(y)-1):
        if y[i]*y[i+1] < 0:
            sign_change.append(i)
    return [x[j] for j in sign_change]

def neville(data_x, data_y,x):
    # Implementation of Neville's algorithm
    n = len(data_x)
    p = np.zeros(n)
    for k in range(0,n):
        for i in range(0, n-k):
            if k == 0:
                p[i] = data_y[i]
            else:
                p[i] = ((x - data_x[i+k])*p[i] + (data_x[i]-x)*p[i+1])/(data_x[i]-data_x[i+k])
    return p[0]

def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

def natural_spline(x, y):
    # precalculations
    h = [x[i+1] - x[i] for i in range(0,len(x)-1)]
    b = [1/h[i]*(y[i+1]-y[i]) for i in range(0,len(x)-1)]
    v = [2*(h[i-1] + h[i]) for i in range(1,len(x)-1)]
    u = [6*(b[i] - b[i-1]) for i in range(1,len(x)-1)]
    M = tridiag(h[:len(h)-2],v,h[:len(h)-2]) 
    
    # Create tridiagonal system
    z = np.linalg.solve(M, u)
    Z = [0]     
    Z = np.append(Z,z)
    Z = np.append(Z,[0])
    print(M)
    print(z)
    print(u)
    return z 

print('Roots at:')
print(find_root())

y_data = evaluate_y()
x_data = np.linspace(-10, 10, 100)

x_lin = x_data[24:26]
y_lin =y_data[24:26]
lin_interpolation = neville(x_lin, y_lin, -5)
print('Value at position y(-5)=',y(-5))
print('Linear interpolation:',lin_interpolation)
print('Error: ', y(-5) - lin_interpolation)

quadratic_interpolation = neville(x_data[24:27], y_data[24:27], -5)
print('Quadratic interpolation:',quadratic_interpolation)
print('Error: ', y(-5) - quadratic_interpolation)

qubic_interpolation = neville(x_data[24:28], y_data[24:28], -5)
print('Qubic interpolation:',qubic_interpolation)
print('Error: ', y(-5) -qubic_interpolation)


print()
lin_interpolation = neville(x_data[74:76], y_lin, 5)
print('Value at position y(5)=',y(5))
print('Linear interpolation:',lin_interpolation)
print('Error: ', y(5) - lin_interpolation)

quadratic_interpolation = neville(x_data[74:77], y_data[74:77], 5)
print('Quadratic interpolation:',quadratic_interpolation)
print('Error: ', y(5) - quadratic_interpolation)

qubic_interpolation = neville(x_data[74:78], y_data[74:78], 5)
print('Qubic interpolation:',qubic_interpolation)
print('Error: ', y(5) -qubic_interpolation)


print('\nExercise 2:')

x_data = np.linspace(0,20,100)
y_data = [y_2(i) for i in x_data]
lin_interpolation = neville(x_data[59:61], y_data[59:61], 12)
print('Value at position y(12)=',y_2(12))
print('Linear interpolation:',lin_interpolation)
print('Error: ', y_2(12) - lin_interpolation)

quadratic_interpolation = neville(x_data[59:62], y_data[59:62], 12)
print('Quadratic interpolation:',quadratic_interpolation)
print('Error: ', y_2(12) - quadratic_interpolation)

qubic_interpolation = neville(x_data[59:63], y_data[59:63], 12)
print('Qubic interpolation:',qubic_interpolation)
print('Error: ', y_2(12) -qubic_interpolation)
