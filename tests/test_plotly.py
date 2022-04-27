import numpy as np

from plotcp import plot_complex_points_plotly, plotcp_plotly, Reim


def f(z):
    return np.sin(z)


top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

ax = plotcp_plotly(f, (-4, 4), (-4, 4), reim=Reim.IM)
ax = plot_complex_points_plotly(top, name='top', color='red', fig=ax)
ax = plot_complex_points_plotly(bottom, name='bottom', fig=ax)
ax = plot_complex_points_plotly(left, name='left', fig=ax)
ax = plot_complex_points_plotly(right, name='right', fig=ax)

ax = plot_complex_points_plotly([f(z) for z in top], name='top_t', color='red', fig=ax)
ax = plot_complex_points_plotly([f(z) for z in bottom], name='bottom_t', fig=ax)
ax = plot_complex_points_plotly([f(z) for z in left], name='left_t', fig=ax)
ax = plot_complex_points_plotly([f(z) for z in right], name='right_t', fig=ax)

ax.show()
