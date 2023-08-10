import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

# malha
n = 10
h = 1./n
xx = np.linspace(0., 1., n+1)

# fonte
def f(x):
    return np.pi**2*np.sin(np.pi*x)

# prob discreto
A = np.zeros((n-1, n-1))
b = np.empty(n-1)

# c.c. x = 0.
A[0,0] = 2./h
A[0,1] = -1./h
b[0] = h/2 * (f(xx[1]-0.5*h) + f(xx[1]+0.5*h))

# pts internos
for i in range(1,n-2):
    A[i,i-1] = -1./h
    A[i,i] = 2./h
    A[i,i+1] = -1./h
    b[i] = h/2 * (f(xx[i+1]-0.5*h) + f(xx[i+1]+0.5*h))

# c.c. x = 1.
A[n-2,n-3] = -1./h
A[n-2,n-2] = 2./h
b[n-2] = h/2 * (f(xx[n-1]-0.5*h) + f(xx[n-1]+0.5*h))

# resol
u = npla.solve(A, b)
## c.c. (dirichlet)
u = np.concatenate(([0.],u,[0.]))

# sol exata
def ue(x):
    return np.sin(np.pi*x)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

x = np.linspace(0., 1., 100)
ax.plot(x, ue(x), label='Analítica')
ax.plot(xx, u, ls='--', marker='o', label='MEF')
ax.grid()
ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$u(x)$')
plt.savefig('fig.png')
plt.savefig('fig.pdf')
