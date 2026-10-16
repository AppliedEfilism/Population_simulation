import random
import numpy as np
import matplotlib.pyplot as plt

N = 10000    
nsteps = 10000
time = np.arange(nsteps + 1) 

path_ensemble = []
for i in range(N):
    x = 0
    path = [x]
    for _ in range(nsteps):  
        dx = random.choice([-1, 1])           
        x += dx
        path.append(x)
        
    path_ensemble.append(path)

arr = np.array(path_ensemble)

var_list = np.var(arr, axis=0)
var_theory = time

it    = nsteps
arr_t = arr[:, it]

sigma = np.sqrt(it)
x_coord = np.linspace(-4 * sigma, 4 * sigma, 500)
rho     = (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-x_coord**2 / (2 * sigma**2))

plt.figure()
plt.hist(arr_t, bins=50, density=True, alpha=0.5, color='C0', edgecolor='black', label=f'Simulation (t={it})')
plt.plot(x_coord, rho, 'r-', linewidth=2, label=r'Gaussian ($\sigma^2=t$)')
plt.xlabel(r'$x$')
plt.ylabel(r'$\rho(x)$')
plt.legend()
plt.xlim(-4*sigma, 4*sigma)
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig('fig_random_walk_pdf.png')
plt.show()