import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 100       # 空間のサイズ
nx = 100      # 空間の分割数
dx = L / nx   # 空間刻み幅
D = 1.0       # 拡散係数
dt = 0.1      # 時間刻み幅
frames = 500
alpha = D * dt / (dx ** 2)

n = np.zeros(nx)
n[nx//2] = 10.0

#=================
# Static plot
#=================
target_steps = [10, 100, 500]
linestyles = ["-", "--", "-."]
i=0
for step in range(frames + 1):
    if step in target_steps:
        plt.plot(n, label=f"step: {step}", color="tab:blue", linestyle=linestyles[i])
        i+=1

    n[1:-1] = n[1:-1] + alpha * (n[2:] - 2 * n[1:-1] + n[:-2])

plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True, alpha=0.5)
plt.savefig("fig_diffusion_snapshots.png")
plt.show()

#=================
# Animation 
#=================
n = np.zeros(nx)
n[nx//2] = 10.0
fig, ax = plt.subplots()
line, = ax.plot(n) 
ax.set_xlabel("x")
ax.set_ylabel("Density")

def update(frame):
    
    n[1:-1] = n[1:-1] + alpha * (n[2:] - 2*n[1:-1] + n[:-2])
    
    line.set_ydata(n)
    ax.set_title(f"Step: {frame}")

ani = animation.FuncAnimation(fig, update, frames=frames, interval=30)
ani.save("fig_diffusion_1d.gif", writer="pillow")
#plt.show()