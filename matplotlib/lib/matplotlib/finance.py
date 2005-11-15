"""
A collection of modules for collecting, analyzing and plotting
financial data.   User contributions welcome!

"""
#from __future__ import division  
import time, warnings
from urllib import urlopen


try: import datetime
except ImportError:
    raise SystemExit('The finance module requires datetime support (python2.3)')

from matplotlib import verbose
from artist import Artist
from dates import date2num, num2date
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.colors import colorConverter
from lines import Line2D, TICKLEFT, TICKRIGHT
from patches import Rectangle
from matplotlib.transforms import scale_transform, Value, zero, one, \
     scale_sep_transform, blend_xy_sep_transform

from pylab import gca



def parse_yahoo_historical(fh):
    """
    Parse the historical data in file handle fh from yahoo finance and return
    results as a list of

    d, open, close, high, low, volume
    
    where d is a floating poing representation of date, as returned by date2num

    """
    results = []



    lines = fh.readlines()
    for line in lines[1:]:

        vals = line.split(',')
        if len(vals)!=7: continue
        datestr = vals[0]
        dt = datetime.date(*time.strptime(datestr, '%d-%b-%y')[:3])
        d = date2num(dt)
        open, high, low, close =  [float(val) for val in vals[1:5]]
        volume = int(vals[5])

        results.append((d, open, close, high, low, volume))
    results.reverse()
    return results
    
def quotes_historical_yahoo(ticker, date1, date2):

    """
    Get historical data for ticker between date1 and date2.  date1 and
    date2 are datetime instances
    
    results are a list of

    d, open, close, high, low, volume
    
    where d is a floating poing representation of date, as returned by date2num
    """


    d1 = (date1.month-1, date1.day, date1.year)
    d2 = (date2.month-1, date2.day, date2.year)    


    urlFmt = 'http://table.finance.yahoo.com/table.csv?a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&s=%s&y=0&g=d&ignore=.csv'
    url =  urlFmt % (d1[0], d1[1], d1[2],
                     d2[0], d2[1], d2[2], ticker)

    ticker = ticker.upper()

    try: ret = parse_yahoo_historical(urlopen(url))
    except IOError, exc:
        warnings.warn('urlopen() failure\n' + url + '\n' + exc.strerror[1])
        return None

    return ret 

        
def plot_day_summary(ax, quotes, ticksize=3,
                     colorup='k', colordown='r',
                     ):
    """
    quotes is a list of (time, open, close, high, low, ...) tuples
    
    Represent the time, open, close, high, low as a vertical line
    ranging from low to high.  The left tick is the open and the right
    tick is the close.

    time must be in float date format - see date2num

    ax          : an Axes instance to plot to
    ticksize    : open/close tick marker in points
    colorup     : the color of the lines where close >= open
    colordown   : the color of the lines where close <  open    
    return value is a list of lines added
    """




    lines = []
    for q in quotes:

        t, open, close, high, low = q[:5]

        if close>=open : color = colorup
        else           : color = colordown

        vline = Line2D(
            xdata=(t, t), ydata=(low, high),
            color=color,
            antialiased=False,   # no need to antialias vert lines
            )

        oline = Line2D(
            xdata=(t, t), ydata=(open, open),
            color=color,
            antialiased=False,
            marker=TICKLEFT,
            markersize=ticksize,
            )

        cline = Line2D(
            xdata=(t, t), ydata=(close, close),
            color=color,
            antialiased=False,
            markersize=ticksize,
            marker=TICKRIGHT)

        lines.extend((vline, oline, cline))
        ax.add_line(vline)
        ax.add_line(oline)
        ax.add_line(cline)


    ax.autoscale_view()

    return lines


def candlestick(ax, quotes, width=0.2, colorup='k', colordown='r',
                alpha=1.0):

    """

    quotes is a list of (time, open, close, high, low, ...)  tuples.
    As long as the first 5 elements of the tuples are these values,
    the tuple can be as long as you want (eg it may store volume).

    time must be in float days format - see date2num
    
    Plot the time, open, close, high, low as a vertical line ranging
    from low to high.  Use a rectangular bar to represent the
    open-close span.  If close >= open, use colorup to color the bar,
    otherwise use colordown

    ax          : an Axes instance to plot to
    width       : fraction of a day for the rectangle width
    colorup     : the color of the rectangle where close >= open
    colordown   : the color of the rectangle where close <  open    
    alpha       : the rectangle alpha level
    
    return value is lines, patches where lines is a list of lines
    added and patches is a list of the rectangle patches added
    """


    OFFSET = width/2.0
    

    lines = []
    patches = []
    for q in quotes:
        t, open, close, high, low = q[:5]

        if close>=open :
            color = colorup
            lower = open
            height = close-open
        else           :
            color = colordown
            lower = close
            height = open-close

        vline = Line2D(
            xdata=(t, t), ydata=(low, high),
            color='k',
            linewidth=0.5,
            antialiased=True,   
            )        

        rect = Rectangle(
            xy    = (t-OFFSET, lower),
            width = width,
            height = height, 
            facecolor = color,
            edgecolor = color,            
            )
        rect.set_alpha(alpha)


        lines.append(vline)
        patches.append(rect)
        ax.add_line(vline)
        ax.add_patch(rect)        
    ax.autoscale_view()

    return lines, patches


def plot_day_summary2(ax, opens, closes, highs, lows, ticksize=4,
                      colorup='k', colordown='r',
                     ):
    """
    
    Represent the time, open, close, high, low as a vertical line
    ranging from low to high.  The left tick is the open and the right
    tick is the close.

    ax          : an Axes instance to plot to
    ticksize    : size of open and close ticks in points
    colorup     : the color of the lines where close >= open
    colordown   : the color of the lines where close <  open    

    return value is a list of lines added
    """

    # note this code assumes if any value open, close, low, high is
    # missing they all are missing

    rangeSegments = [ ((i, low), (i, high)) for i, low, high in zip(xrange(len(lows)), lows, highs) if low != -1 ]

    # the ticks will be from ticksize to 0 in points at the origin and
    # we'll translate these to the i, close location
    openSegments = [  ((-ticksize, 0), (0, 0)) ]

    # the ticks will be from 0 to ticksize in points at the origin and
    # we'll translate these to the i, close location
    closeSegments = [ ((0, 0), (ticksize, 0)) ]


    offsetsOpen = [ (i, open) for i, open in zip(xrange(len(opens)), opens) if open != -1 ]

    offsetsClose = [ (i, close) for i, close in zip(xrange(len(closes)), closes) if close != -1 ]


    scale = ax.figure.dpi * Value(1/72.0)
    
    tickTransform = scale_transform( scale, zero())

    r,g,b = colorConverter.to_rgb(colorup)
    colorup = r,g,b,1
    r,g,b = colorConverter.to_rgb(colordown)
    colordown = r,g,b,1
    colord = { True : colorup,
               False : colordown,
               }
    colors = [colord[open<close] for open, close in zip(opens, closes) if open!=-1 and close !=-1]

    assert(len(rangeSegments)==len(offsetsOpen))
    assert(len(offsetsOpen)==len(offsetsClose))
    assert(len(offsetsClose)==len(colors))

    useAA = 0,   # use tuple here
    lw = 1,      # and here
    rangeCollection = LineCollection(rangeSegments,
                                     colors       = colors,
                                     linewidths   = lw,
                                     antialiaseds = useAA,
                                     )

    openCollection = LineCollection(openSegments,
                                    colors       = colors,
                                    antialiaseds = useAA,
                                    linewidths   = lw,
                                    offsets      = offsetsOpen,
                                    transOffset  = ax.transData,
                                   )
    openCollection.set_transform(tickTransform)
    
    closeCollection = LineCollection(closeSegments,
                                     colors       = colors,
                                     antialiaseds = useAA,
                                     linewidths   = lw,
                                     offsets      = offsetsClose,
                                     transOffset  = ax.transData,
                                     )
    closeCollection.set_transform(tickTransform)

    minx, maxx = (0, len(rangeSegments))
    miny = min([low for low in lows if low !=-1])
    maxy = max([high for high in highs if high != -1])
    corners = (minx, miny), (maxx, maxy)
    ax.update_datalim(corners)
    ax.autoscale_view()

    # add these last
    ax.add_collection(rangeCollection)
    ax.add_collection(openCollection)
    ax.add_collection(closeCollection)
    return rangeCollection, openCollection, closeCollection


def candlestick2(ax, opens, closes, highs, lows, width=4,
                 colorup='k', colordown='r',
                 alpha=0.75,
                ):
    """
    
    Represent the open, close as a bar line and high low range as a
    vertical line.


    ax          : an Axes instance to plot to
    width       : the bar width in points
    colorup     : the color of the lines where close >= open
    colordown   : the color of the lines where close <  open    
    alpha       : bar transparency
    
    return value is lineCollection, barCollection
    """

    # note this code assumes if any value open, close, low, high is
    # missing they all are missing
    right = width/2.0
    left = -width/2.0
    
    barVerts = [ ( (left, 0), (left, close-open), (right, close-open), (right, 0) ) for open, close in zip(opens, closes) if open != -1 and close!=-1 ]

    rangeSegments = [ ((i, low), (i, high)) for i, low, high in zip(xrange(len(lows)), lows, highs) if low != -1 ]



    offsetsBars = [ (i, open) for i,open in zip(xrange(len(opens)), opens) if open != -1 ]

    sx = ax.figure.dpi * Value(1/72.0)  # scale for points
    sy = (ax.bbox.ur().y() - ax.bbox.ll().y()) / (ax.viewLim.ur().y() - ax.viewLim.ll().y()) 

    barTransform = scale_sep_transform(sx,sy)
                                           

    
    r,g,b = colorConverter.to_rgb(colorup)
    colorup = r,g,b,alpha
    r,g,b = colorConverter.to_rgb(colordown)
    colordown = r,g,b,alpha
    colord = { True : colorup,
               False : colordown,
               }
    colors = [colord[open<close] for open, close in zip(opens, closes) if open!=-1 and close !=-1]


    assert(len(barVerts)==len(rangeSegments))
    assert(len(rangeSegments)==len(offsetsBars))
    assert(len(offsetsBars)==len(colors))

    useAA = 0,  # use tuple here
    lw = 0.5,   # and here
    rangeCollection = LineCollection(rangeSegments,
                                     colors       = ( (0,0,0,1), ),
                                     linewidths   = lw,
                                     antialiaseds = useAA,
                                     )


    barCollection = PolyCollection(barVerts,
                                   facecolors   = colors,
                                   edgecolors   = ( (0,0,0,1), ),
                                   antialiaseds = useAA,
                                   linewidths   = lw,
                                   offsets      = offsetsBars,
                                   transOffset  = ax.transData,
                                   )
    barCollection.set_transform(barTransform)




    minx, maxx = (0, len(rangeSegments))
    miny = min([low for low in lows if low !=-1])
    maxy = max([high for high in highs if high != -1])

    corners = (minx, miny), (maxx, maxy)
    ax.update_datalim(corners)
    ax.autoscale_view()

    # add these last
    ax.add_collection(barCollection)
    ax.add_collection(rangeCollection)
    return rangeCollection, barCollection

def volume_overlay(ax, opens, closes, volumes,
                   colorup='k', colordown='r',
                   width=4, alpha=1.0):
    """
    Add a volume overlay to the current axes.  The opens and closes
    are used to determine the color of the bar.  -1 is missing.  If a
    value is missing on one it must be missing on all

    ax          : an Axes instance to plot to
    width       : the bar width in points
    colorup     : the color of the lines where close >= open
    colordown   : the color of the lines where close <  open    
    alpha       : bar transparency


    """

    r,g,b = colorConverter.to_rgb(colorup)
    colorup = r,g,b,alpha
    r,g,b = colorConverter.to_rgb(colordown)
    colordown = r,g,b,alpha
    colord = { True : colorup,
               False : colordown,
               }
    colors = [colord[open<close] for open, close in zip(opens, closes) if open!=-1 and close !=-1]

    right = width/2.0
    left = -width/2.0

    
    bars = [ ( (left, 0), (left, v), (right, v), (right, 0)) for v in volumes if v != -1 ]

    sx = ax.figure.dpi * Value(1/72.0)  # scale for points
    sy = (ax.bbox.ur().y() - ax.bbox.ll().y()) / (ax.viewLim.ur().y() - ax.viewLim.ll().y()) 

    barTransform = scale_sep_transform(sx,sy)

    offsetsBars = [ (i, 0) for i,v in enumerate(volumes) if v != -1 ]

    barCollection = PolyCollection(bars,
                                   facecolors   = colors,
                                   edgecolors   = ( (0,0,0,1), ),
                                   antialiaseds = (0,),
                                   linewidths   = (0.5,),
                                   offsets      = offsetsBars,
                                   transOffset  = ax.transData,
                                   )
    barCollection.set_transform(barTransform)






    minx, maxx = (0, len(offsetsBars))
    miny = 0
    maxy = max([v for v in volumes if v!=-1])
    corners = (minx, miny), (maxx, maxy)
    ax.update_datalim(corners)
    ax.autoscale_view()

    # add these last
    return barCollection

    


def index_bar(ax, vals,
              facecolor='b', edgecolor='l',
              width=4, alpha=1.0, ):
    """
    Add a bar collection graph with height vals (-1 is missing).

    ax          : an Axes instance to plot to
    width       : the bar width in points
    alpha       : bar transparency


    """

    facecolors = (colorConverter.to_rgba(facecolor, alpha),)
    edgecolors = (colorConverter.to_rgba(edgecolor, alpha),)

    right = width/2.0
    left = -width/2.0

    
    bars = [ ( (left, 0), (left, v), (right, v), (right, 0)) for v in vals if v != -1 ]

    sx = ax.figure.dpi * Value(1/72.0)  # scale for points
    sy = (ax.bbox.ur().y() - ax.bbox.ll().y()) / (ax.viewLim.ur().y() - ax.viewLim.ll().y()) 

    barTransform = scale_sep_transform(sx,sy)

    offsetsBars = [ (i, 0) for i,v in enumerate(vals) if v != -1 ]

    barCollection = PolyCollection(bars,
                                   facecolors   = facecolors,
                                   edgecolors   = edgecolors,
                                   antialiaseds = (0,),
                                   linewidths   = (0.5,),
                                   offsets      = offsetsBars,
                                   transOffset  = ax.transData,
                                   )
    barCollection.set_transform(barTransform)






    minx, maxx = (0, len(offsetsBars))
    miny = 0
    maxy = max([v for v in vals if v!=-1])
    corners = (minx, miny), (maxx, maxy)
    ax.update_datalim(corners)
    ax.autoscale_view()

    # add these last
    ax.add_collection(barCollection)
    return barCollection

    
