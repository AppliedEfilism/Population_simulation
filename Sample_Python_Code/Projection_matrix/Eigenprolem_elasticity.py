import numpy as np
import matplotlib.pyplot as plt

eps = 1e-6

def get_growth_rate(A):

    evals, evecs = np.linalg.eig(A)
    lam = np.max(evals)

    return lam

def calc_elasticity(A, x, lam_std):

    lam = get_growth_rate(A)
    dlam_dx = ( lam - lam_std ) / eps

    elasticity = ( x / lam_std) * dlam_dx

    return elasticity 

# standard matrix
a11 = 1.1
a12 = 1.0
a21 = 0.7
a22 = 0.8
A = np.array( [ [a11, a12], [a21, a22] ] )
lam_std = get_growth_rate(A)

# elasticity
A11e = np.array( [ [a11+eps, a12], [a21, a22] ] )
A12e = np.array( [ [a11, a12+eps], [a21, a22] ] )
A21e = np.array( [ [a11, a12], [a21+eps, a22] ] )
A22e = np.array( [ [a11, a12], [a21, a22+eps] ] )

e11 = calc_elasticity(A11e, a11, lam_std)
e12 = calc_elasticity(A12e, a12, lam_std)
e21 = calc_elasticity(A21e, a21, lam_std)
e22 = calc_elasticity(A22e, a22, lam_std)

plt.bar( ["a11", "a12", "a21", "a22"], [e11, e12, e21, e22], width=0.5)

plt.xlabel('Matrix element')
plt.ylabel('Elasticity')
plt.grid(True, alpha=0.3)
plt.savefig('fig_matrix_model_sample_elasticity.png')
plt.show()