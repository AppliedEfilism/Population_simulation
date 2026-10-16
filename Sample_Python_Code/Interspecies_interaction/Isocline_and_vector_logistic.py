import numpy as np
import matplotlib.pyplot as plt

# set parameters
a = 1.2 
b = 0.3   
c = 0.5  
d = 1.5  
K = 10

# grid points
x_max, y_max = 10, 10
x = np.linspace(0.1, x_max, 20)
y = np.linspace(0.1, y_max, 20)
X, Y = np.meshgrid(x, y)

# Lotka-Volterra equations
vx = a * X * (1 - X / K ) - b * X * Y  # dx/dt
vy = c * X * Y - d * Y  # dy/dt

# normalize the vector
norm = np.sqrt(vx**2+vy**2)
vx_norm = vx / norm
vy_norm = vy / norm

# isoclines
n_array = np.linspace(0, 10, 20)
isocline_y = (a/b) * (1 - n_array/K)    # dx/dt = 0
isocline_x = np.full_like(n_array, d/c) # dy/dt = 0

#===================
# plot
#===================
plt.figure(figsize=(8, 6))

# isoclines
plt.plot(isocline_x, n_array, label='dy/dt=0')
plt.plot(n_array, isocline_y, label='dx/dt=0')

# vector field
plt.quiver(X, Y, vx_norm, vy_norm, color='lightgray')

plt.xlim(-0.5, x_max)
plt.ylim(-0.5, y_max)
plt.xlabel('Prey population ($x$)')
plt.ylabel('Predator population ($y$)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('fig_sample_predetor_prey_logistic.png')
plt.show()