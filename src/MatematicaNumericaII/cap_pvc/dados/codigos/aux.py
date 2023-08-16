import numpy as np
import numpy.linalg as npla
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

# parâmetros
n = 10000
h = 1./n
xx = np.linspace(0., 1., n+1)

# c.c. Dirichlet
ua = 1.
ub = -1.

def f(x, u, ux):
    return u**2 - cos(pi*x)**2 - pi**2*cos(pi*x)

def fu(x, u, ux):
    return 2*u

def fux(x, u, ux):
    return 0.

# rhs
def F(u):
    y = np.empty(n+1)
    # f_1
    y[0] = u[0] - ua
    # f_i
    for i in range(1,n):
        ux = u[i+1]/(2*h) - u[i-1]/(2*h) 
        y[i] = -1./h**2*u[i-1] + 2./h**2*u[i] - 1./h**2*u[i+1] \
            + f(xx[i], u[i], ux)
    # f_{n+1}
    y[n] = u[n] - ub

    return y

# jacobiana
def J(u):
    J = np.zeros((n+1,n+1))
    J[0,0] = 1.
    for i in range(1,n):
        ux = 1./(2*h)*u[i+1] - 1./(2*h)*u[i-1]
        J[i,i-1] = -1./h**2 - 1/(2*h)\
            * fux(xx[i], u[i], ux)
        J[i,i] = 2/h**2 + fu(xx[i], u[i], ux)
        J[i,i+1] = -1./h**2 + 1/(2*h)\
            * fux(xx[i], u[i], ux)
    J[n,n] = 1.

    return J

# aprox inicial
u = np.zeros(n+1)

# iterações de Newton
maxiter = 10
for k in range(maxiter):

    # passo de Newton
    dlta = npla.solve(J(u), -F(u))

    # atualização
    u += dlta

    ndlta = npla.norm(dlta)
    print(f'{k+1}: norm = {ndlta:.2e}')
    if (ndlta < 1e-10):
        print('convergiu.')
        break

def ue(x):
    return cos(pi*x)

print(f'{h:.1e}: err ={ npla.norm(u - ue(xx)):.1e}')

#plt.plot(xx, u)
#plt.plot(xx, ue(xx))
#plt.show()
