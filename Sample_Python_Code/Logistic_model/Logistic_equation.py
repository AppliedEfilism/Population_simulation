import numpy as np
import matplotlib.pyplot as plt

n=50
t0 = 0
tf = 10
dt = (tf-t0)/(n-1)
r = 1
K = 100

time = np.linspace(t0, tf, n)
N = np.zeros(n)
Nint = [10, 150]
linestyles = ["-", "--"]

for j, N0 in enumerate(Nint):
    N[0]=N0
    for i in range(1,n):
        N_i = N[i-1]
        dN = r * N_i * ( 1 - N_i / K ) * dt
        N[i] = N_i + dN

    plt.plot(time, N, ls=linestyles[j], label=rf"$N_0={N[0]:.0f}$")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid(True,alpha=0.5)
plt.legend()
plt.savefig('fig_logistic_equation.png')
plt.show()
