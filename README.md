# PlotComplexPlane
Python library for plotting complex functions transformations
# It can...
  - *plot complex planes (both transformed and original)*
  - *plot transformations of specific areas (both transformed and original)*
  - *plot lines parallel to real or imaginary axis (both transformed and original)*
# How to use:
**First** define a callable complex function:
```python
def f(z):
    return (z+1)/z
```
**Optionally** find edges of your specific area. For example: |z|=2
```python
circle = [2*(cos(x)+I*sin(x) for x in np.linspace(0, 2*pi)]
```
**Finally** choose what you want to see and call plotcp
parameter | description | type
-|:-|:-
fun | your predefined function f(z) | callable
xbound | real plot bounds | np.array([left, right])
ybound | imaginary plot bounds | np.array([bottom, top])
nsteps | how many nodes will be on each line (bigger value - smoother lines - more time to compute) | int
gridstep | spaces between lines parallel to axis | int
inits_point | array of your areas points | iterator type filled with complex points
faxis | what to display: 'origin', 'transform' or 'both' (named constants, correspondingly: ORIG, TRANSF, BOTH) | str
reim | which part to display: 'real', 'imag' or 'both' (named constants, correspondingly: RE, IM, BOTH) (**only works with grid lines, and not areas**) | str
inits_only | show initial points only? transformed or not | bool
