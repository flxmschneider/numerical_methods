import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return (1+x**2)**-1

N_list = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
results = []
for N in N_list: 
    counter = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if y < f(x):
            counter+=1
    result = counter/N
    results.append(result) 


plt.plot(N_list, [np.pi/4]*len(N_list),label='Pi/4')
plt.plot(N_list, results, label = 'Monte Carlo')
plt.legend()
plt.title('Monte Carlo Integration')
plt.show()
