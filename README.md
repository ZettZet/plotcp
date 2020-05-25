# PlotComplexPlane
Python library for plotting complex functions transformation
# It can...
  - *plot complex plane (transform, original or both)*
  - *plot transformation of specific areas (transform, original or both)*
  - *plot lines parallel to real or imagin axis (transform, original or both)*
# How to use:
**Firstly** define callable complex function:
```python
def f(z):
    return (z+1)/z
```
**Optionaly** find edges of your specific area. For example: |z|=2
```python
circle = [2*(cos(x)+I*sin(x) for x in np.linspace(0, 2*pi)]
```
**Finaly** choose what you want to see and call plotcp
parametr | discribe | type
-|:-|:-
fun | your predefined fuction f(z) | func
xbound | real edges of plot | np.array([left, right])
ybound | imag edges of plot | np.array([bottom, top])
nsteps | how many nodes will be on **EACH** line (bigger value — smoother lines — more time to compute) | int
gridstep | spaces between lines parallel to axis | int
inits_point | array of your areas points | enumerable type full of complex points
faxis | what to display: 'origin', 'transform' or 'both' (may use names constants in lib: ORIG, TRANSF, BOTH) | str
reim | which part to display: 'real', 'imag' or 'both' (may use named constants in lib: RE, IM, BOTH) (**WORK ONLY WITH GRID LINES. NOT AREAS**) | str
inits_only | want to show only inints points? transformed or not | Boolean