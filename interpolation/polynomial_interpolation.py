import numpy as np

def y(x):
    return 3+200*x-300*x**2+4*x**3-x**4

def evaluate_y():
    N = 100
    I = np.linspace(-10,10,N)
    return [y(i) for i in I]

def neville(data_x, data_y,x):
    n = len(data_x)
    p = np.zeros(n)
    for k in range(0,n):
        for i in range(0, n-k):
            if k == 0:
                p[i] = data_y[i]
            else:
                p[i] = ((x - data_x[i+k])*p[i] + (data_x[i]-x)*p[i+1])/(data_x[i]-data_x[i+k])
    return p[0]

y_data = evaluate_y()
x_data = np.linspace(-10, 10, 100)

x_lin = x_data[24:26]
y_lin =y_data[24:26]
lin_interpolation = neville(x_lin, y_lin, -5)
print('Value at position y(-5)=',y(-5))
print('Linear interpolation:',lin_interpolation)
print('Error: ', y(-5) - lin_interpolation)

quadratic_interpolation = neville(x_data[24:27], y_data[24:27], -5)
print('Value at position y(-5)=',y(-5))
print('Quadratic interpolation:',quadratic_interpolation)
print('Error: ', y(-5) - quadratic_interpolation)

qubic_interpolation = neville(x_data[24:28], y_data[24:28], -5)
print('Value at position y(-5)=',y(-5))
print('Linear interpolation:',qubic_interpolation)
print('Error: ', y(-5) -qubic_interpolation)
