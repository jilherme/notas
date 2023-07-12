import numpy as np
from scipy.optimize import fsolve

def euler(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y = y + h*f(t,y)
        t += h
    return t, y

def eulerimp(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y = fsolve(lambda x:
                   x - y - h*f(t+h, x),
                   x0 = y, xtol=1e-14)[0]
        t += h
    return t, y

def f(t, y):
    return 50 - 50*y

# analítica
def exata(t):
    return 1 + np.exp(-50*t)

h = 1e-1
n = round(1./h)
t,y = eulerimp(f, 0., 2., h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1.)):.1e}')
