# PlotComplexPlane

Python library for plotting complex functions transformations

## It can...

- *plot complex planes (both transformed and original)*
- *plot transformations of specific areas (both transformed and original)*
- *plot lines parallel to real or imaginary axis (both transformed and original)*

## Usage
### plotcp
To plot f(z) = (z+1)/z with x bound from -4 to 4 and y bound from -4 to 4

```python3
from plotcp import plotcp


def f(z: complex) -> complex: # Define function to plot
    return (z+1)/z


# Call plotcp
# Second and third arguments define limits of a plot
ax = plotcp(f, (-4, 4), (-4, 4))
```
For full parameters list check ```help(plotcp.plotcp)```
### plot_complex_points
```python3
from cmath import sin

import matplotlib.pyplot as plt
import numpy as np

from plotcp import plot_complex_points

def f(z):
    return sin(z)


# Define area to be plotted
top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

# Plot original area
ax = plot_complex_points(top)
ax = plot_complex_points(bottom, ax=ax)
ax = plot_complex_points(left, ax=ax)
ax = plot_complex_points(right, ax=ax)


# Apply function to area and plot it on a new plot
ax2 = plot_complex_points([f(z) for z in top])
ax2 = plot_complex_points([f(z) for z in bottom], ax=ax2)
ax2 = plot_complex_points([f(z) for z in left], ax=ax2)
ax2 = plot_complex_points([f(z) for z in right], ax=ax2)

plt.show()
```
For full parameters list check ```help(plotcp.plot_complex_points)```