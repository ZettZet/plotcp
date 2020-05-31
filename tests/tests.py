from cmath import sin

import matplotlib.pyplot as plt
import numpy as np

from plotcp import plot_complex_points, plotcp, Faxis, Reim


def f(z):
    return sin(z)


top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

ax = plotcp(f, (-4, 4), (-4, 4), faxis=Faxis.BOTH, reim=Reim.BOTH)
ax = plot_complex_points([f(z) for z in top], ax)
ax = plot_complex_points([f(z) for z in bottom], ax)
ax = plot_complex_points([f(z) for z in left], ax)
ax = plot_complex_points([f(z) for z in right], ax)

plt.show()
