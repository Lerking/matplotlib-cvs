#Controlling the properties of axis text using handles

# See axis_text_themes.py for a more elegant, pythonic way to control
# fonts.  After all, if we were slaves to matlab , we wouldn't be
# using python!

from matplotlib.matlab import *


def f(t):
    s1 = sin(2*pi*t)
    e1 = exp(-t)
    return multiply(s1,e1)

t1 = arange(0.0, 5.0, 0.1)
t2 = arange(0.0, 5.0, 0.02)


subplot(111)
plot(t1, f(t1), 'bo', t2, f(t2), 'k')
text(3.5, 0.6, 'f(t) = exp(-t) sin(2 pi t)')
ttext = title('Fun with text!')
ytext = ylabel('Damped oscillation')
xtext = xlabel('time (s)')

set(ttext, 'fontsize', 14)
set(ttext, 'color', 'r')
set(ttext, 'fontangle', 'italic')

set(xtext, 'fontsize', 12)
set(xtext, 'fontname', 'Courier')
set(xtext, 'fontweight', 'ultrabold')
set(xtext, 'color', 'g')

set(ytext, 'fontsize', 12)
set(ytext, 'fontname', 'Helvetica')
set(ytext, 'fontweight', 'light')
set(ytext, 'color', 'b')

# TODO: fix me
#xticklabels = get(gca(), 'xticklabels')
#yticklabels = get(gca(), 'yticklabels')
#set(xticklabels, 'fontweight', 'bold')
#set(yticklabels, 'fontangle', 'italic')

show()
