import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

f = lambda x: 1/(x-1)

p = plot(f(x), (x,-1,1-1e-5), line_color="blue", show=False)
q = plot(f(x), (x,1+1e-5,3), line_color="blue", show=False)
p.extend(q)
q = plot(-1, (x,-1,3), line_color="none", show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-20,20))
ax.plot([1,1],[-20,20],ls="--",color="red",zorder=5)
ax.text(1.75,7,"$\\displaystyle y=\\frac{1}{x-1}$",
        bbox = dict(facecolor = "white", edgecolor = "white"))
fig.savefig('fig.png', bbox_inches='tight')
