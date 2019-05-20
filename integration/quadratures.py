import numpy as np
import matplotlib.pyplot as plt

def trapezoidal(f, a, b, n):
    n = int(n)
    h = float(b-a)/n
    result = 0.5*f(a)+0.5*f(b)
    for i in range(1,n):
        result += f(a+h*i)
    result *= h
    return result

def simpson(f, a, b, n):
    h = float(b-a)/n
    result =np.sum([f(a+h*(2*i-2))+4*f(a+(2*i-1)*h)+f(a+2*i*h) for i in range(1,int(n/2))])*h/3
    return result

def I_1(theta):
    m=2
    n=4
    return np.sin(theta)**(2*m-1) * np.cos(theta)**(2*n-1) 

def extended_formula1(f, a, b, n):
    h = float(b-a)/n
    result = h*3/2*(f(a+2*h)+f(a+(n-1)*h))
    result += h*np.sum([f(a+i*h) for i in range(2,n-2)])
    return result

def extended_formula2(f, a,b,n):
    h = float(b-a)/n
    result = h*(27/12*f(a+2*h)+13/12*f(a+4*h)+13/12*f(a+(n-3)*h)+27/12*f(a+(n-1)*h))
    result += np.sum([h*4/3*f(a+i*h) for i in range(5,n,2)])
    result += np.sum([h*2/3*f(a+i*h) for i in range(6,n,2)])
    return result

print(trapezoidal(I_1, 0, 0.5*np.pi, 100))
print(simpson(I_1, 0, 0.5*np.pi, 100))
print(extended_formula2(I_1, 0, 0.5*np.pi, 100))
print(extended_formula1(I_1, 0, 0.5*np.pi, 100))

trapez_list = []
simpson_list = []
N_list = np.linspace(1, 21,5)
print(N_list)
for N in N_list:
    trapez_list.append(trapezoidal(I_1, 0, 0.5*np.pi, N)) 
    simpson_list.append(simpson(I_1, 0, 0.5*np.pi, N))

plt.plot(N_list, trapez_list, label='Trapez')
plt.plot(N_list, simpson_list, label='Simpson')
plt.legend()
plt.title('Comparison of Simpsons and Trapezoidal Formula')
plt.show()
