import numpy as np
import matplotlib.pyplot as plt

n = 200
t0 = 0
tf = 10
dt = (tf-t0)/(n-1)
r = 3
K = 50
a = 10

time = np.linspace(t0, tf, n)
N = np.zeros(n)
Nint = [20, 80, 9]
linestyles = ["-", "--","-."]

for j, N0 in enumerate(Nint):
    N[0]=N0
    for i in range(1,n):
        N_i = N[i-1]
        dN = r * N_i * ( N_i - a ) * ( 1 - N_i / K ) * dt / K
        N[i] = N_i + dN

    plt.plot(time, N, ls=linestyles[j], label=rf"$N_0={N[0]:.0f}$")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid(True,alpha=0.5)
plt.legend()
plt.savefig('fig_allee_threshold.png')
plt.show()
