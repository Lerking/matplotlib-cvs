# wrap the plot commands defined in axes.  The code generated by this
# file is pasted into pylab.py


__fmt = """\

# this function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def %(func)s(*args, **kwargs):
    # allow callers to override the hold state by passing hold=True|False
    b = ishold()
    h = popd(kwargs, 'hold', None)
    if h is not None:
        hold(h)
    try:
        ret =  gca().%(func)s(*args, **kwargs)
    except ValueError, msg:
        msg = raise_msg_to_str(msg)
        error_msg(msg)
        hold(b)
    else:
        draw_if_interactive()
        %(mappable)s
        hold(b)
        return ret
%(func)s.__doc__ = Axes.%(func)s.__doc__ + \"\"\"
Addition kwargs: hold = [True|False] overrides default hold state\"\"\"
""" 


# these methods are all simple wrappers of Axes methods by the same
# name.  
_methods = (
    'axhline',
    'axhspan',
    'axvline',
    'axvspan',
    'bar',
    'barh',
    'cla',
    'cohere',
    'contour',
    'csd',
    'errorbar',
    'fill',
    'grid',
    'hist',
    'hlines',
    'imshow',
    'legend',
    'loglog',
    'pcolor',
    'pcolor_classic',
    'plot',
    'plot_date',
    'psd',
    'scatter',
    'scatter_classic',
    'semilogx',
    'semilogy',
    'specgram',
    'spy',
    'spy2',
    'stem',
    'table',
    'text',
    'vlines',
    )

cmappable = {
    'scatter' : 'gci._current = ret',
    'pcolor'  : 'gci._current = ret',
    'imshow'  : 'gci._current = ret',
    'spy2'  : 'gci._current = ret',    
    'specgram'  : 'gci._current = ret[-1]',
}


for func in _methods:
    if cmappable.has_key(func):
        mappable = cmappable[func]
    else:
        mappable = ''
    print __fmt%locals()
