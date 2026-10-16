import numpy as np
import matplotlib.pyplot as plt

#=================
# Basic parameters
#=================

a = 1.2 
b = 0.3   
c = 0.5  
d = 0.5
K = 15
h = 0.2

#=================
# Equations
#=================

def rate_of_change(x, y):
    #dxdt = a * x - b * x * y  
    dxdt = a * x * ( 1 - x / K ) - b * x * y  / ( 1 + h * x )
    dydt = c * x * y / ( 1 + h * x ) - d * y  
    return dxdt, dydt

#=================
# Simulation setups
#=================

ti = 0
tf = 50 
n  = 1000
dt = (tf-ti) / n  # timestep size
x_orb = np.zeros(n)
y_orb = np.zeros(n)
initial_pos = [[4, 4], [6, 4]]#, [8, 4]]

# grid points
x_max, y_max = 10, 15
x = np.linspace(0.1, x_max, 20)
y = np.linspace(0.1, y_max, 20)
X, Y = np.meshgrid(x, y)

#=================
# Vector field
#=================
#vx = a * X - b * X * Y  # dx/dt
vx = a * X * (1 - X / K ) - b * X * Y / ( 1 + h * X )  # dx/dt
vy = c * X * Y / (1 + h * X) - d * Y  # dy/dt

# normalization
norm = np.sqrt(vx**2+vy**2)
vx_norm = vx / norm
vy_norm = vy / norm

# isoclines
n_array = np.linspace(0, 20, 20)
#isocline_y = np.full_like(n_array, a/b) # dx/dt = 0
isocline_y = np.full_like(n_array, a/b) + (a/b) * ( ( h - 1 / K) * n_array - ( h / K ) * n_array**2 ) 
#isocline_x = np.full_like(n_array, d/c) # dy/dt = 0
isocline_x = np.full_like(n_array, d / ( c - h * d ) ) 

#=================
# Eigenvalues
#=================
x0 = d / (c - h * d)
y0 = (a / b) * (1 - x0 / K) * (1 + h * x0)

J11 = a * ( 1 - 2 * x0 / K ) - b * y0 / ( 1 + h * x0 )**2
J12 = -b * x0 / (1 + h * x0)
J21 = c * y0 / (1 + h * x0)**2
J22 = c * x0 / (1 + h * x0) - d

eigenvalues = np.linalg.eigvals([[J11, J12], [J21, J22]])

print(f"(x0, y0) = ({x0:.4f}, {y0:.4f})")
print(f"Eigen values: {eigenvalues[0]:.4f}, {eigenvalues[1]:.4f}")

#=================
# Plot
#=================
plt.figure(figsize=(6, 4))

# isoclines
plt.plot(isocline_x, n_array, label=r'$dy/dt=0$')
plt.plot(n_array, isocline_y, label=r'$dx/dt=0$')

# vector field
plt.quiver(X, Y, vx_norm, vy_norm, color='lightgray')

# orbits
for pos in initial_pos:

    x_orb[0] = pos[0]
    y_orb[0] = pos[1]

    for i in range(1,n):
        x = x_orb[i-1]
        y = y_orb[i-1]

        # Euler method
        #dxdt, dydt = rate_of_change(x, y)
        #x_orb[i] = x + dt * dxdt
        #y_orb[i] = y + dt * dydt
        
        # 4th order Runge-Kutta method
        k1_x, k1_y = rate_of_change(x, y)
        k2_x, k2_y = rate_of_change(x + 0.5 * dt * k1_x, y + 0.5 * dt * k1_y)
        k3_x, k3_y = rate_of_change(x + 0.5 * dt * k2_x, y + 0.5 * dt * k2_y)
        k4_x, k4_y = rate_of_change(x + dt * k3_x, y + dt * k3_y)

        x_orb[i] = x + (dt / 6.0) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        y_orb[i] = y + (dt / 6.0) * (k1_y + 2*k2_y + 2*k3_y + k4_y)

    # Orbit
    plt.plot(x_orb, y_orb, color="k")
    plt.plot(x_orb[0], y_orb[0], color="k",marker="o") # initial position

plt.xlabel(r'Prey population ($x$)')
plt.ylabel(r'Predator population ($y$)')
plt.xlim(0, x_max)
plt.ylim(0, y_max)
plt.legend(loc='upper right')
#plt.savefig('fig_predator_prey_orbit.png')
#plt.savefig('fig_predator_prey_orbit_logistic.png')
#plt.savefig('fig_predator_prey_orbit_type_II.png')
plt.show()