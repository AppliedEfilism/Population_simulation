import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 1.0
N0 = 1.0
r  = 3.0

time = np.linspace(0,tf,200)
dt = 0.1
t_points = np.arange(t0, tf+dt, dt)
step = np.arange(len(t_points))

N_cont = N0 * np.exp( r * time )
N_disc = N0 * (1.0 + r * dt)**step

plt.plot( time, N_cont, label=f"Continuous", lw=3 )
plt.plot( t_points, N_disc, label=f"Discrete: dt={dt:.2f}", marker="o", ls="--", lw=1.5 )
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(True, alpha=0.5)
plt.show()