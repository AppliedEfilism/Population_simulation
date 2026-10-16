import numpy as np
import matplotlib.pyplot as plt

eps = 1e-6

def make_matrix(S1,S2,F1,F2):

    row1 = [S1 * F1, 
            np.sqrt(S1) * F2 * np.sqrt(S2)]
    row2 = [S1, S2]

    A = np.array( [ row1, row2 ] ) 

    return A

def get_growth_rate(A):

    evals = np.linalg.eigvals(A)
    lam = np.max(evals.real)

    return lam

def calc_elasticity(A, x, lam_std):

    lam = get_growth_rate(A)
    dlam_dx = ( lam - lam_std ) / eps

    elasticity = ( x / lam_std) * dlam_dx

    return elasticity 

# basic parameters
S1 = 0.5
S2 = 0.7
F1 = 1.58
F2 = 3.78
reduction = [0, 0.25, 0.5, 0.75]

A_std = make_matrix(S1, S2, F1, F2)
lam_std = get_growth_rate(A_std)
print(f'Standard matrix: a11={A_std[0,0]:.3f}, a12={A_std[0,1]:.3f}, a21={A_std[1,0]:.3f}, a22={A_std[1,1]:.3f}')
print(f'Standard growth rate: {lam_std:.3f}')

lam_TNR = []
lam_LC  = []
for r in reduction:

    rate = 1.0 - r
    A_TNR = make_matrix(S1, S2, F1 * rate, F2 * rate)
    A_LC  = make_matrix(S1 * rate, S2 * rate, F1, F2)
    
    lam_TNR.append( get_growth_rate(A_TNR) )
    lam_LC.append( get_growth_rate(A_LC) )

# elasticity
AS1 = make_matrix(S1+eps,S2,F1,F2)
AS2 = make_matrix(S1,S2+eps,F1,F2)
AF1 = make_matrix(S1,S2,F1+eps,F2)
AF2 = make_matrix(S1,S2,F1,F2+eps)

eS1 = calc_elasticity(AS1, S1, lam_std)
eS2 = calc_elasticity(AS2, S2, lam_std)
eF1 = calc_elasticity(AF1, F1, lam_std)    
eF2 = calc_elasticity(AF2, F2, lam_std)

plt.plot(reduction, lam_TNR, marker="o", label='TNR')
plt.plot(reduction, lam_LC,  marker="o",label='LC')
plt.axhline(1.0, linestyle=':',color="k") 
plt.xlabel('Reduction rate (%)')
plt.ylabel(r'Growth Rate ($\lambda$)')
plt.xlim(0,0.75)
plt.xticks(reduction)
plt.grid(True, alpha=0.5)
plt.legend()
#plt.savefig('fig_andersen_model_reduction.png')
plt.show()
plt.close()


plt.bar( ["S1", "S2", "F1", "F2"], [eS1, eS2, eF1, eF2], width=0.5)
plt.xlabel('Survival and fecundity rates')
plt.ylabel('Elasticity')
plt.grid(True, alpha=0.5)
#plt.savefig('fig_andersen_model_elasticity.png')
plt.show()
plt.close()