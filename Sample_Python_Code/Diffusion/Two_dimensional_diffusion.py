import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 100       # 空間のサイズ（1辺の長さ）
nx = 100      # x方向の空間分割数
ny = 100      # y方向の空間分割数
dx = L / nx   # x方向の空間刻み幅
dy = L / ny   # y方向の空間刻み幅
D = 10.0       # 拡散係数
dt = 0.01      # 時間刻み幅
frames = 500  # アニメーションのフレーム数

alpha_x = D * dt / (dx ** 2)
alpha_y = D * dt / (dy ** 2)

x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)
X, Y = np.meshgrid(x, y)

n0 = 5.0
n = n0 * np.exp(-((X - L/2)**2 + (Y - L/2)**2) / (2 * D))

fig, ax = plt.subplots()
im = ax.imshow(n, cmap='viridis', origin='lower', extent=[0, L, 0, L])
cbar = fig.colorbar(im, ax=ax, label="Density")
ax.set_xlabel("x")
ax.set_ylabel("y")

def update(frame):

    n[1:-1, 1:-1] = n[1:-1, 1:-1] \
                    + alpha_x * (n[1:-1, 2:] - 2*n[1:-1, 1:-1] + n[1:-1, :-2]) \
                    + alpha_y * (n[2:, 1:-1] - 2*n[1:-1, 1:-1] + n[:-2, 1:-1])

    im.set_array(n)
    
    im.set_clim(vmin=0, vmax=np.max(n))
    
    return [im]

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1, blit=False)
ani.save("fig_diffusion_2d.gif", writer="pillow")
plt.show() 
