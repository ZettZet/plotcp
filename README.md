# PlotComplexPlane

Python library for plotting complex functions transformations

## It can...

- *plot complex planes (both transformed and original)*
- *plot transformations of specific areas (both transformed and original)*
- *plot lines parallel to real or imaginary axis (both transformed and original)*

## Usage
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

