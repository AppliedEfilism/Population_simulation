import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#=================
# Parameters
#=================
L = 100
nx = 200
dx = L / nx
x_grid = np.linspace(0, L, nx)
D = 1.0
dt = 0.1
frames = 1500
alpha = D * dt / (dx ** 2)
s = 0.15

A = 0.1         
s_c = (1 - A)**2 / 4 

print(f" alpha={alpha:.2f}")
print(f" Critical sterile density (s_c) = {s_c:.4f}")

if s < s_c:
    n_plus = (1 - A - 2*s + np.sqrt((1 - A)**2 - 4*s)) / 2
    print(f" Outbreak equilibrium density (n_plus) = {n_plus:.4f}")
else:
    n_plus = 0
    print(" s >= s_c: Outbreak state does not exist.")

#=================
# Static Plot
#=================
n = np.zeros(nx)
if n_plus > 0:
    n[0:50] = n_plus 

target_steps = [0, 500, 1000,1500]
linestyles = ["-", "--", "-.", ":"]
i = 0

fig, ax = plt.subplots(figsize=(6, 4))

for step in range(frames + 1):
    if step in target_steps:
        ax.plot(x_grid, n, label=f"step: {step}", color="tab:blue", linestyle=linestyles[i])
        i += 1

    diffusion = alpha * (n[2:] - 2 * n[1:-1] + n[:-2])     
    reaction  = dt * ( n[1:-1] / (n[1:-1] + s) - A - (n[1:-1] + s) ) * n[1:-1]
    
    n[1:-1] = n[1:-1] + diffusion + reaction 
    
    # boundary condition
    n[0] = n_plus 
    n[-1] = 0     
    #n[0] = n[1]
    #n[-1] = n[-2]

ax.set_xlabel("x")
ax.set_ylabel("Density")
#ax.set_ylim(-0.05, max(n_plus + 0.2, 0.5))
ax.legend(loc="upper right")
ax.grid(True, alpha=0.5)
plt.savefig(f"fig_sit_single_eq_{s:1g}.png")
plt.show()

#=================
# Animation 
#=================
n = np.zeros(nx)
if n_plus > 0:
    n[0:50] = n_plus

fig, ax = plt.subplots()
line, = ax.plot(x_grid, n)
ax.set_xlabel("x")
ax.set_ylabel("Density")
#ax.set_ylim(-0.05, max(n_plus + 0.2, 0.5))

def update(frame):
    
    diffusion = alpha * (n[2:] - 2 * n[1:-1] + n[:-2]) 
    reaction  = dt * ( n[1:-1] / (n[1:-1] + s) - A - (n[1:-1] + s) ) * n[1:-1]
    n[1:-1] = n[1:-1] + diffusion + reaction 
    
    n[0] = n_plus
    n[-1] = 0
    #n[0] = n[1]
    #n[-1] = n[-2]
    
    line.set_ydata(n)
    ax.set_title(f"Step: {frame}")

ani = animation.FuncAnimation(fig, update, frames=frames, interval=30)
ani.save(f"fig_sit_single_eq_{s:1g}.gif", writer="pillow")