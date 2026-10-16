import numpy as np
import matplotlib.pyplot as plt

a = 1.2   
b = 0.3   
c = 0.5  
d = 1.5  

n_array = np.linspace(0, 10, 20)
isocline_y = np.full_like(n_array, a/b) # dx/dt = 0
isocline_x = np.full_like(n_array, d/c) # dy/dt = 0

plt.figure(figsize=(6, 4))
plt.plot(isocline_x, n_array, label="dy/dt=0")
plt.plot(n_array, isocline_y, label="dx/dt=0")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('fig_predetor_prey_isocline.png')
plt.show()
