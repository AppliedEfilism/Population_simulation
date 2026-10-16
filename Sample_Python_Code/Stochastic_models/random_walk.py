import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000
nsteps = 500   
time = np.arange(nsteps + 1) 

path_ensemble = []
for i in range(N):
    x = 0
    path = [x]
    for t in range(nsteps+1):
        dx = random.choice([-1, 1])           
        x += dx
        path.append(x)
        
    path_ensemble.append(path)

path_mean = []
var_list = []

'''
for t in range(nsteps+1):

    sum_x = 0
    for i in range(N):
        sum_x += path_ensemble[i][t]
    
    x_mean = sum_x / N
    path_mean.append(x_mean)

    sum_diff_sq = 0
    for i in range(N):
        sum_diff_sq += (path_ensemble[i][t] - x_mean) ** 2
        
    var = sum_diff_sq / N 
    var_list.append(var)
'''

arr = np.array(path_ensemble)
var_list = np.var(arr, axis=0)

var_theory = time

plt.plot(var_list,   label="Simulation")
plt.plot(var_theory, label="Theory")
plt.xlabel('Time step')
plt.ylabel('variance')
plt.legend()
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig('fig_random_walk_variance.png')
plt.show()


for i in range(20):
    plt.plot(path_ensemble[i], color='k', alpha=0.5)
plt.xlabel('Time step')
plt.ylabel('x')
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig('fig_random_walk_paths.png')
plt.show()
