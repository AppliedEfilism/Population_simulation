import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 1.0
N0 = 1.0
r  = 3.0

time = np.linspace(0,tf,200)
N_cont =  N0 * np.exp( r * time )

plt.plot( time, N_cont, label=f"Continuous", lw=3 )

dt_list = [0.5, 0.25, 0.1]
markers = ["o", "s", "^"]

for i, dt in enumerate(dt_list):

    t_points = np.arange(t0, tf+dt, dt)

    r_dt = ( np.exp(r * dt) - 1.0) / dt

    step = np.arange(len(t_points))
    N_disc = N0 * (1.0 + r_dt * dt)**step

    plt.plot( t_points, N_disc, label=f"Discrete: dt={dt:.2f}", 
             marker=markers[i], 
             ls="--", lw=1.5 )

plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(True,alpha=0.5)
plt.savefig('fig_dt_comparison.png')
plt.show()

