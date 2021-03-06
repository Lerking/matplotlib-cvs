from matplotlib.numerix import which

if which[0] == "numarray":
    from numarray.fft import *
elif which[0] == "numeric":
    from FFT import *
elif which[0] == "numpy":
    from numpy.dft import *
else:
    raise RuntimeError("invalid numerix selector")
