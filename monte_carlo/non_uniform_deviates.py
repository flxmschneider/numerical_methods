import matplotlib.pyplot as plt
import numpy as np
import random


N = int(10e4)
T = 6e3

random_numbers = []
for i in range(N):
    v = random.random()*5e4
    N = 8*np.pi*v**2/(np.exp(v/T)-1)
    random_numbers.append(N)


plt.hist(random_numbers)
plt.title('Photon distribution')
plt.ylabel('#')
plt.xlabel('K')
plt.show()
