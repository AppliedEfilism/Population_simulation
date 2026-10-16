import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 100
nx = 200
dx = L / nx
r = 0.5
K = 10.0
D = 1.0
dt = 0.05
frames = 1500
alpha = D * dt / (dx ** 2)

print(f" alpha={alpha:.2f}")

n = np.zeros(nx)
n[0:20] = K # Initialize left side

target_steps = [0, 500, 1000]
linestyles = ["-", "--", "-."]
i = 0

fig, ax = plt.subplots(figsize=(6, 4))

for step in range(frames + 1):
    if step in target_steps:
        ax.plot(np.linspace(0, L, nx), n, label=f"step: {step}", color="tab:blue", linestyle=linestyles[i])
        i += 1

    diffusion = alpha * (n[2:] - 2 * n[1:-1] + n[:-2]) 
    reaction  = dt * r * n[1:-1] * (1 - n[1:-1] / K)
    n[1:-1] = n[1:-1] + diffusion + reaction 
    
    n[0] = K
    n[-1] = 0

ax.set_xlabel("x")
ax.set_ylabel("Density")
ax.set_ylim(-0.5, K + 1.0)
ax.legend()
ax.grid(True, alpha=0.5)
plt.savefig("fig_fisher_kpp.png")
plt.show()

#=================
# Animation 
#=================
n = np.zeros(nx)
n[0:20] = K
fig, ax = plt.subplots()
line, = ax.plot(n) 
ax.set_xlabel("x")
ax.set_ylabel("Density")

def update(frame):
    
    diffusion = alpha * (n[2:] - 2 * n[1:-1] + n[:-2]) 
    reaction  = dt * r * n[1:-1] * (1 - n[1:-1] / K)
    n[1:-1] = n[1:-1] + diffusion + reaction 
    
    n[0] = K
    n[-1] = 0
    
    line.set_ydata(n)
    ax.set_title(f"Step: {frame}")

ani = animation.FuncAnimation(fig, update, frames=frames, interval=30)
ani.save("fig_fisher_KPP.gif", writer="pillow")