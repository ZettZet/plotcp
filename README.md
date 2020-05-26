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
xbound | real plot bounds | Tuple[left: int, right: int]
ybound | imaginary plot bounds | Tuple[top: int, bottom: int]
nsteps | how many nodes will be on each line (bigger value - smoother lines - more time to compute) | int
gridstep | spaces between lines parallel to axis | int
inits_point | array of your areas points | optional iterator
faxis | what to display: 'origin', 'transform' or 'both' (named constants, correspondingly: Faxis.ORIG, Faxis.TRANSF, Faxis.BOTH) | Faxis(Flag)
reim | which part to display: 'real', 'imag' or 'both' (named constants, correspondingly: Reim.RE, Reim.IM, Reim.BOTH) (**only works with grid lines, and not areas**) | Reim(Flag)
inits_only | show initial points only? transformed or not | bool
