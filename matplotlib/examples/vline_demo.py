from matplotlib.matlab import *
from RandomArray import normal
from Numeric import sin, exp, multiply, absolute, pi

def f(t):
    s1 = sin(2*pi*t)
    e1 = exp(-t)
    return absolute(multiply(s1,e1))+.05


t = arange(0.0, 5.0, 0.1)
s = f(t)
nse = multiply(normal(0.0, 0.3, t.shape), s)

plot(t, s+nse, 'b^')
vlines(t, 0, s, color='k')
xlabel('time (s)')
title('Comparison of model with data')
show()
