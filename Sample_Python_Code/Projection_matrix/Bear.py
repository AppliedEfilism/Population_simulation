import numpy as np
import matplotlib.pyplot as plt
import random

def make_matrix(S_c, S_s, S_a, S_r, tau_sa, tau_ar, L):

    A = np.array([
        [0,   0,                  S_a * tau_ar * L,   0  ],
        [S_c, S_s * (1 - tau_sa), 0,                  0  ],
        [0,   S_s * tau_sa,       S_a * (1 - tau_ar), S_r],
        [0,   0,                  S_a * tau_ar,       0  ]
    ])
    return A

def get_growth_rate(A):

    evals = np.linalg.eigvals(A)
    lam = max(evals.real)

    return lam

# Baseline
base_good = {'S_c': 0.60, 'S_s': 0.75, 'S_a': 0.90, 'S_r': 0.90, 'tau_sa': 0.33, 'tau_ar': 0.90, 'L': 1.10}
base_poor = {'S_c': 0.40, 'S_s': 0.60, 'S_a': 0.85, 'S_r': 0.85, 'tau_sa': 0.25, 'tau_ar': 0.60, 'L': 0.60}
base_food = {'S_c': 0.40, 'S_s': 0.60, 'S_a': 0.85, 'S_r': 0.85, 'tau_sa': 0.25, 'tau_ar': 0.95, 'L': 1.10}

# Low Removal
low_good  = {'S_c': 0.60, 'S_s': 0.75, 'S_a': 0.90, 'S_r': 0.90, 'tau_sa': 0.33, 'tau_ar': 0.95, 'L': 1.15}
low_poor  = {'S_c': 0.45, 'S_s': 0.65, 'S_a': 0.80, 'S_r': 0.80, 'tau_sa': 0.33, 'tau_ar': 0.95, 'L': 1.15}

# High Removal
high_good = {'S_c': 0.60, 'S_s': 0.75, 'S_a': 0.90, 'S_r': 0.90, 'tau_sa': 0.33, 'tau_ar': 0.95, 'L': 1.15}
high_poor = {'S_c': 0.35, 'S_s': 0.60, 'S_a': 0.70, 'S_r': 0.70, 'tau_sa': 0.33, 'tau_ar': 0.95, 'L': 1.15}

A_base_good = make_matrix(**base_good)
A_base_poor = make_matrix(**base_poor)
A_base_food = make_matrix(**base_food)
A_high_good = make_matrix(**high_good)
A_high_poor = make_matrix(**high_poor)
A_low_good  = make_matrix(**low_good)
A_low_poor  = make_matrix(**low_poor)

print(f"Baseline scenario (good): {get_growth_rate(A_base_good):.4f}")
print(f"Baseline scenario (poor): {get_growth_rate(A_base_poor):.4f}")
print(f"High removal scenario (poor): {get_growth_rate(A_high_poor):.4f}")

print("=== Comparison of anthropogenic effects ===")
print(f"Baseline                 : {get_growth_rate(A_base_poor):.4f}")
print(f"Anthropogenic food effect: {get_growth_rate(A_base_food):.4f}")
print(f"Food + removal           : {get_growth_rate(A_high_poor):.4f}")

#=================
# Time evolution simulation
#=================
nsteps = 50
nensemble = 500
p_good = 0.75  

N0 = np.array([20, 30, 30, 30])

Nmean_base = np.zeros(nsteps + 1)
Nmean_high = np.zeros(nsteps + 1)
Nmean_low  = np.zeros(nsteps + 1)
Nmean_base[0] = np.sum(N0)
Nmean_high[0] = np.sum(N0)
Nmean_low[0]  = np.sum(N0)

for i in range(nensemble):

    N_base = N0.copy()
    N_high = N0.copy()
    N_low  = N0.copy()

    for t in range(nsteps):

        p = random.random()
        
        if p < p_good:
            N_base = A_base_good @ N_base
            N_high = A_high_good @ N_high
            N_low  = A_low_good  @ N_low
        else:
            N_base = A_base_poor @ N_base
            N_high = A_high_poor @ N_high
            N_low  = A_low_poor  @ N_low
            
        Nmean_base[t+1] += np.sum(N_base)
        Nmean_high[t+1] += np.sum(N_high)
        Nmean_low[t+1]  += np.sum(N_low)

Nmean_base[1:] /= nensemble
Nmean_high[1:] /= nensemble
Nmean_low[1 :] /= nensemble

plt.plot(Nmean_base, label='Baseline', linestyle='-')
plt.plot(Nmean_high, label='High Removal', linestyle='--')
plt.plot(Nmean_low,  label='Low Removal', linestyle='-.')

plt.xlabel('Year')
plt.ylabel('Total Population')
plt.legend()
plt.grid(True, alpha=0.5)
plt.savefig('fig_stochastic_bear_matrix.png')
plt.show()