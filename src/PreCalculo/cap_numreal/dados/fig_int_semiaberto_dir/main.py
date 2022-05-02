import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

fig, ax = plt.subplots()
fig.set_size_inches(6.4,1.05)
ax.axis("off")
ax.set_xlim((-4,4))
ax.set_ylim((-0.2,0.1))
ax.arrow(0,0,4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.025,
         head_length = 0.1,
         overhang=1.0)
ax.arrow(0,0,-4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.025,
         head_length = 0.1,
         overhang=1.0)

ax.plot([-2,2],[0,0],color="blue")

ax.plot([-2],[0],ls='',marker='o',markersize=5,color='blue',
        markerfacecolor='blue')
ax.text(-2-0.1, -0.1, "a")

ax.plot([2],[0],ls='',marker='o',markersize=5,color='blue',
        markerfacecolor='white')
ax.text(2, -0.1, "b")


plt.savefig("main.png", bbox_inches='tight', pad_inches=0)
