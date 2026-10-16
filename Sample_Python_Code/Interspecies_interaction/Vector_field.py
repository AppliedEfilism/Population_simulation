import numpy as np
import matplotlib.pyplot as plt

# set parameters
a = 1.2   
b = 0.3   
c = 0.5  
d = 1.5  

# grid points
x_max, y_max = 10, 10
x = np.linspace(0.1, x_max, 20)
y = np.linspace(0.1, y_max, 20)
X, Y = np.meshgrid(x, y)

# Lotka-Volterra equations
vx = a * X - b * X * Y  # dx/dt
vy = c * X * Y - d * Y  # dy/dt

# normalize the vector
norm = np.sqrt(vx**2+vy**2)
vx_norm = vx / norm
vy_norm = vy / norm

# isoclines
n_array = np.linspace(0, 10, 20)
isocline_y = np.full_like(n_array, a/b) # dx/dt = 0
isocline_x = np.full_like(n_array, d/c) # dy/dt = 0

#===================
# plot
#===================
plt.figure(figsize=(6, 4))

# isoclines
plt.plot(isocline_x, n_array, label=r'$dy/dt=0$')
plt.plot(n_array, isocline_y, label=r'$dx/dt=0$')

# vector field
plt.quiver(X, Y, vx_norm, vy_norm, color='lightgray')

plt.xlim(-0.5, x_max)
plt.ylim(-0.5, y_max)
plt.xlabel(r'Prey population ($x$)')
plt.ylabel(r'Predator population ($y$)')
plt.legend()
plt.savefig('fig_predetor_prey_vector_field.png')
plt.show()