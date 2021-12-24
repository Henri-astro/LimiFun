# LimiFunc

LimiFunc is a program that computes the limiting function of a point cloud.

## The main program

### Dependencies

Python 3.8.10

### Usage

The main program is located in src/FindBound.py in this package. It contains the function FindBoundaries, which computes a linear function, f(x) = a + bx, as the limit of the point cloud in 2D linear space.

FindBoundaries( xvalues, yvalues, BPos, Max )

- xvalues: an array for all the xvalues of the point cloud
- yvalues: an array for all the yvalues of the point cloud
- BPos: true, if the slope of the limiting function shall be positive, otherwise: false
- Max: true, if the upper limit of the point cloud shall be found, otherwise: false

- returns: a,b

Additionally there are 3 helper functions to compute the limiting function in log space:

- FindBoundariesLogX( xvalues, yvalues, BPos, Max ): the is computed in log(x),y
- FindBoundariesLogY( xvalues, yvalues, BPos, Max ): the is computed in x,log(y)
- FindBoundariesLog( xvalues, yvalues, BPos, Max ): the is computed in log(x),log(y)

The last two functions return 10^a,b instead of a,b.

The mathematical basis are described in Appendix A of Wirth et al. (2022).

## Examples

### Dependencies

Python 3.8.10
Matplotlib 3.5.1

### Usage

This package is shipped with two examples that may be found in the folder example_src.

- PlotForApp: contains a function to reproduce fig. A1 from Wirth et al. (2022)
- Plot6.py: contains a function to reproduce fig. 6 from Wirth et al. (2022)

Both examples can be called using:
```
python3 RunAllEx.py
```

## References

TODO
