from sympy import *
from sympy.abc import *

p = plot(1/x,(x,-4,4),ylim=(-4,4),show=False,
         line_color="blue")
p[0].label="$y=1/x$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_negativo_impar.png')

p = plot(1/x**2,(x,-4,4),ylim=(-4,4),show=False,
         line_color="blue")
p[0].label="$y=1/x^2$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_negativo_par.png')
