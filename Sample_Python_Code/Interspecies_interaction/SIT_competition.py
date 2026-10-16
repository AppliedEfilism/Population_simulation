import matplotlib.pyplot as plt
import numpy as np

# =================
# Basic parameters
# =================
a = 0.8  
b = 0.2  
k = 0.001  
gamma = 0.8

# =================
# Equations
# =================

def rate_of_change(N, S):

  eps = 1e-10
  total = N + S + eps

  dNdt = (a * N / total - b) * N - k * N * total
  dSdt = gamma * N - b * S
  return dNdt, dSdt


# =================
# Simulation setups
# =================
ti = 0
tf = 200
n = 10000
dt = (tf - ti) / n  # timestep size
x_orb = np.zeros(n)
y_orb = np.zeros(n)
initial_pos = [[100, 10], [80, 10], [60, 10], [40, 10], [20, 10]]

# grid points
x_max, y_max = 120, 200
x = np.linspace(0.1, x_max, 20)
y = np.linspace(0.1, y_max, 20)
X, Y = np.meshgrid(x, y)

# =================
# Vector field
# =================
vx = (a * X / (X + Y) - b) * X - k * X * (X + Y)  # dN/dt
vy = gamma * X - b * Y  # dS/dt

# normalization
norm = np.sqrt(vx**2 + vy**2)
vx_norm = vx / norm
vy_norm = vy / norm

# isoclines
n_array = np.linspace(0.1, x_max, 100)
# dS/dt = 0 -> S = (gamma / b) * N
isocline_S = (gamma / b) * n_array
# dN/dt = 0 -> S = (-b + sqrt(b^2 + 4*k*a*N)) / (2*k) - N
isocline_N = (-b + np.sqrt(b**2 + 4 * k * a * n_array)) / (2 * k) - n_array

# =================
# Plot
# =================
plt.figure(figsize=(6, 4))

# isoclines
plt.plot(n_array, isocline_N, label=r"$dN/dt=0$", color="tab:blue")
plt.plot(n_array, isocline_S, label=r"$dS/dt=0$", color="tab:orange")

# vector field
plt.quiver(X, Y, vx_norm, vy_norm, color="lightgray")

# orbits
for pos in initial_pos:

  x_orb[0] = pos[0]
  y_orb[0] = pos[1]

  for i in range(1, n):
    x = x_orb[i - 1]
    y = y_orb[i - 1]

    # 4th order Runge-Kutta method
    k1_x, k1_y = rate_of_change(x, y)
    k2_x, k2_y = rate_of_change(x + 0.5 * dt * k1_x, y + 0.5 * dt * k1_y)
    k3_x, k3_y = rate_of_change(x + 0.5 * dt * k2_x, y + 0.5 * dt * k2_y)
    k4_x, k4_y = rate_of_change(x + dt * k3_x, y + dt * k3_y)

    x_orb[i] = x + (dt / 6.0) * (k1_x + 2 * k2_x + 2 * k2_x + k4_x)
    y_orb[i] = y + (dt / 6.0) * (k1_y + 2 * k2_y + 2 * k2_y + k4_y)

  # Orbit
  plt.plot(x_orb, y_orb, color="k")
  plt.plot(x_orb[0], y_orb[0], color="k", marker="o")  # initial position

plt.xlabel(r"Fertile population ($N$)")
plt.ylabel(r"Sterile population ($S$)")
plt.xlim(-10, x_max)
plt.ylim(-10, y_max)
plt.legend(loc="upper right")
plt.savefig(f'fig_sit_competition_orbit_{gamma:1g}.png')
plt.show()