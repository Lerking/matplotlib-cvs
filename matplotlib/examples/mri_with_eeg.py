# note, this is currentl *very slow*.  I'm working on improving the
# efficiency of pcolor.  If you want to run this example and your
# computer is not very fast, I suggest you grab a cup of coffee while
# it runs

from matplotlib.matlab import *
from matplotlib.lines import Line2D

# I use if 1 to break up the different regions of code visually

if 1:   # load the data
    # data are 256x256 16 bit integers
    dfile = 'data/s1045.ima'
    im = fromstring(file(dfile, 'rb').read(), Int16).astype(Float)
    im.shape = 256, 256
    # flip upside down
    im = array([im[i] for i in arange(255,-1,-1)])

if 1: # plot the MRI in pcolor
    subplot(221)
    pcolor(im, shading='flat')
    axis('off')

if 1:  # plot the histogram of MRI intensity
    subplot(222)
    im.shape = 256*256,
    im = take(im, nonzero(im)) # ignore the background
    im = im/(2.0**15) # normalize
    hist(im, 100)
    set(gca(), 'xticks', [-1, -.5, 0, .5, 1])
    set(gca(), 'yticks', [])
    xlabel('intensity')
    ylabel('MRI density')

if 1:   # plot the EEG
    # load the data
    numSamples, numRows = 800,4
    data = fromstring(file('data/eeg.dat', 'rb').read(), Float)
    data.shape = numSamples, numRows
    t = arange(numSamples)/float(numSamples)*10.0
    ticklocs = []
    ax = subplot(212)
    for i in range(numRows):
        thisLine = Line2D(ax.dpi, ax.bbox, t, data[:,i]-data[0,i],
                          transx=ax.xaxis.transData, transy=ax.yaxis.transData)
        thisLine.set_vertical_offset(3*i)
        ax.add_line(thisLine)
        ticklocs.append(3*i)

    set(gca(), 'xticks', arange(10))
    set(gca(), 'yticks', ticklocs)
    set(gca(), 'yticklabels', ['PG3', 'PG5', 'PG7', 'PG9'])
    #set(gca(), 'ylim', [0, 20])
    xlabel('time (s)')


#savefig('mri_with_eeg')
show()
