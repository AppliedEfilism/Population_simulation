import numpy as np
import matplotlib.pyplot as plt

r_list = [0.5, 3, 5]
time = np.linspace(0,1,20)
N0   = 1
markers = ["o", "s", "^"]

for i, r in enumerate(r_list):
    N = N0 * np.exp( r * time )
    plt.plot( time, N, label=f"r={r:.1f}", marker=markers[i] )

plt.xlabel("time")
plt.ylabel("population")
#plt.yscale("log")
plt.legend()
plt.grid(True,alpha=0.5)
#plt.savefig('fig_continuous_Malthus_linear.png')
#plt.savefig('fig_continuous_Malthus_log.png')
plt.show()