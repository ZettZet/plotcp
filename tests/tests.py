from plotcp import *
from cmath import sin
import numpy as np
import matplotlib.pyplot as plt


def f(z):
    return sin(z)


top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

ax = plotcp(f, (-4, 4), (-4, 4), init_points=[top, bottom, right, left], faxis=Faxis.BOTH,
            reim=Reim.BOTH, inits=Inits.BOTH)

plt.show()
