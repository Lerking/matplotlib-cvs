"""
Render to gtk from agg
"""
from __future__ import division
import os

import matplotlib
from matplotlib.figure import Figure
from backend_agg import FigureCanvasAgg
from backend_gtk import gtk, FigureManagerGTK, FigureCanvasGTK,\
     show, draw_if_interactive,\
     error_msg_gtk, NavigationToolbar, PIXELS_PER_INCH, backend_version, \
     NavigationToolbar2GTK
from _gtkagg import agg_to_gtk_drawable


DEBUG = False

class NavigationToolbar2GTKAgg(NavigationToolbar2GTK):
    def _get_canvas(self, fig):
        return FigureCanvasGTKAgg(fig)
    

class FigureManagerGTKAgg(FigureManagerGTK):
    def _get_toolbar(self, canvas):
        # must be inited after the window, drawingArea and figure
        # attrs are set
        if matplotlib.rcParams['toolbar']=='classic':
            toolbar = NavigationToolbar (canvas, self.window)
        elif matplotlib.rcParams['toolbar']=='toolbar2':
            toolbar = NavigationToolbar2GTKAgg (canvas, self.window)
        else:
            toolbar = None
        return toolbar
    
def new_figure_manager(num, *args, **kwargs):
    """
    Create a new figure manager instance
    """
    if DEBUG: print 'backend_gtkagg.new_figure_manager'
    thisFig = Figure(*args, **kwargs)
    canvas = FigureCanvasGTKAgg(thisFig)
    return FigureManagerGTKAgg(canvas, num)


class FigureCanvasGTKAgg(FigureCanvasGTK, FigureCanvasAgg):

    def configure_event(self, widget, event=None):
        if DEBUG: print 'FigureCanvasGTKAgg.configure_event'
        if widget.window is None:
            return 
        try:
            del self.renderer
        except AttributeError:
            pass
        w,h = widget.window.get_size()
        if w==1 or h==1: return # empty fig

        # compute desired figure size in inches
        dpival = self.figure.dpi.get()
        winch = w/dpival
        hinch = h/dpival
        self.figure.set_figsize_inches(winch, hinch)
        self._need_redraw = True
        
        if DEBUG: print 'FigureCanvasGTKAgg.configure_event end'        
        return True
    
    def _render_figure(self, pixmap, width, height):
        FigureCanvasAgg.draw(self)
        agg_to_gtk_drawable(pixmap, self.renderer._renderer, None)

    def blit(self, bbox=None):
        agg_to_gtk_drawable(self._pixmap, self.renderer._renderer, bbox)
        x, y, w, h = self.allocation
        self.window.draw_drawable (self.style.fg_gc[self.state], self._pixmap,
                                   x, y, x, y, w, h)
        self._need_redraw = False

    def print_figure(self, filename, dpi=150,
                     facecolor='w', edgecolor='w',
                     orientation='portrait'):
        if DEBUG: print 'FigureCanvasGTKAgg.print_figure'
        # delete the renderer to prevent improper blitting after print

        root, ext = os.path.splitext(filename)       
        ext = ext.lower()[1:]
        if ext == 'jpg':
            FigureCanvasGTK.print_figure(self, filename, dpi, facecolor,
                                         edgecolor, orientation)
            
        else:
            agg = self.switch_backends(FigureCanvasAgg)
            try: agg.print_figure(filename, dpi, facecolor, edgecolor, orientation)
            except IOError, msg:
                error_msg_gtk('Failed to save\nError message: %s'%(msg,), self)

        self.figure.set_canvas(self)
