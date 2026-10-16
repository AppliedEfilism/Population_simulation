import numpy as np
import matplotlib.pyplot as plt

eps = 1e-12

r_b, r_r, r_c = 1.5, 4.0, 0.75   
K_b, S = 100000, 10000    
mu_b, mu_r = 54, 200   
eta_b, eta_s = 120, 60
lam_r, lam_c = 0.0, 1.0

B0, R0, C0 = 100000, 100, 1

#t_start, t_end, t_cntrl = 0, 100, 50
t_start, t_end, t_cntrl = 0, 100, 50
nsteps = 5000
dt = (t_end - t_start) / nsteps
time = np.linspace(t_start, t_end, nsteps)

y_arr = np.zeros((nsteps, 3))
y_arr[0] = np.array([B0, R0, C0])

def func(y,t):
    B, R, C = y
    dBdt = r_b * B * (1 - B/K_b) - (B/(S + B + eps)) * eta_b * R - (B/(B + R + eps)) * mu_b * C
    dRdt = r_r * R * (1 - (eta_b * eta_s * R)/(eta_b * S + eta_s * B + eps)) - (R/(B + R + eps)) * mu_r * C
    dCdt = r_c * C * (1 - (mu_b * mu_r * C)/(mu_r * B + mu_b * R + eps))

    if t>t_cntrl:
        dRdt += - lam_r * R
        dCdt += - lam_c * C

    return np.array([dBdt, dRdt, dCdt])

#=================
# main loop
#=================
for i in range(1, nsteps):

    t = time[i]
    k1 = func(y_arr[i-1], t)
    k2 = func(y_arr[i-1] + 0.5 * dt * k1, t)
    k3 = func(y_arr[i-1] + 0.5 * dt * k2, t)
    k4 = func(y_arr[i-1] + dt * k3, t)

    y_arr[i] = y_arr[i-1] + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

#=================
# Plot
#=================
#fig = plt.figure(figsize=(6, 4))
plt.plot(time, y_arr[:, 0], 'b-', label='Bird (Prey)')
plt.plot(time, y_arr[:, 1]*100, 'r--', label='Rat (Mesopredator) x100')
plt.plot(time, y_arr[:, 2]*100, 'g-.', label='Cat (Superpredator)x100')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True, alpha=0.5)
plt.tight_layout()
#plt.savefig('fig_mesopredator_release.png')
#plt.savefig('fig_mesopredator_coexistence.png')
plt.show()
