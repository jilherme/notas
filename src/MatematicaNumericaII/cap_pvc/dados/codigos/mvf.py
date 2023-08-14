import numpy as np

# fonte
def f(x):
  return np.pi**2*np.sin(np.pi*x)

# malha
n = 10
h = 1./n
xx = np.linspace(h/2, 1.-h/2, n)

# prob. discreto
A = np.zeros((n,n))
b = np.empty(n)

# c.c. x = 0
A[0,0] = 3./h**2
A[0,1] = -1./h**2
b[0] = f(xx[0])

# pts internos
for i in range(1,n-1):
  A[i,i-1] = -1./h**2
  A[i,i] = 2./h**2
  A[i,i+1] = -1./h**2
  b[i] = f(xx[i])

# c.c. x = 1
A[n-1,n-2] = -1./h**2
A[n-1,n-1] = 3./h**2
b[n-1] = f(xx[n-1])

# resol prob disc
u = npla.solve(A, b)

xx = np.concatenate(([0.],xx,[1.]))
u = np.concatenate(([0.],u,[0.]))
