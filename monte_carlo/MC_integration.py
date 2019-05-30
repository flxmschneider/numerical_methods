import numpy as np
import random
import matplotlib.pyplot as plt

# Funktion 1
def f(x):
    return (1+x**2)**-1

#Funktion 2
def f(y):
    return 3/(4+4*y**2-2*y-2*y**3)


N_list = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
results = []
variances = []
for N in N_list: 
    counter = 0
    y_values = []
    for i in range(N):
        x = random.random()
        y = random.random()
        if y < f(x):
            counter+=1
        y_values.append(f(x))
    variances.append(np.var(y_values))
    result = counter/N
    results.append(result) 
    print(np.pi/4 - result)

fig, ax = plt.subplots(nrows =1, ncols=2)
ax[0].plot(N_list, [np.pi/4]*len(N_list),label='Pi/4')
ax[0].plot(N_list, results, label = 'Monte Carlo')
ax[0].legend()
ax[0].set_title('Monte Carlo Integration')
ax[1].set_title('Variances')
ax[1].plot(N_list, variances)
plt.tight_layout()
plt.show()


""""
Nutzt man Funktion 1, so konvergiert die Ergebnisse für große N gegen
das zu erwartende Resultat, allerdings mit deutlich hoher Varianz. Dies
kann mithilfe von Funktion 2 deutlich verbessert werden.
"""
