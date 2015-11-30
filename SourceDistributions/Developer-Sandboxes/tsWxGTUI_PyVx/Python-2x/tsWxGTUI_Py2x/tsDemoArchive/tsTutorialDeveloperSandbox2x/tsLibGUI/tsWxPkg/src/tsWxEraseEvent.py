#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:30:46 AM rsg>"
'''
tsWxEraseEvent.py - Class to emulate the wxPython API for non-graphical,
curses-based platforms.
'''
#################################################################
#
# File: tsWxEraseEvent.py
#
# Purpose:
#
#    Class to emulate the wxPython API for non-graphical,
#    curses-based platforms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEraseEvent import EraseEvent
#
# Requirements:
#
#    wxPython 2.8.9.2.
#
# Capabilities:
#
#    wxPython 2.8.9.2.
#
# Limitations:
#
#    wxPython 2.8.9.2.
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2.
#
# Classes:
#
#    wxPython 2.8.9.2.
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    Modify code to interpret event type.
#
#################################################################

__title__     = 'tsWxEraseEvent'
__version__   = '0.1.0'
__date__      = '04/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibGUI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Curses Module API & ' + \
                'Run Time Library Features:' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  wxWidgets (formerly wxWindows) & ' + \
                'wxPython API Features:' + \
                '\n\t  Copyright (c) 1992-2008 Julian Smart, ' + \
                'Robert Roebling,' + \
                '\n\t\t\tVadim Zeitlin and other members of the ' + \
                '\n\t\t\twxWidgets team.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  wxWindows Library License' + \
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'

__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if len( __credits__) == 0:
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

import tsWxGlobals as wx
from tsWxEvent import Event

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class EraseEvent(Event):
    '''
    An erase event is sent when a window background needs to be repainted.

    On some platforms, such as GTK+, this event is simulated (simply
    generated just before the paint event) and may cause flicker. It is
    therefore recommended that you set the text background colour explicitly
    in order to prevent flicker. The default background colour under GTK+
    is grey.

    To intercept this event, use the EVT_ERASE_BACKGROUND macro in an event
    table definition.

    You must call wxEraseEvent.GetDC and use the returned device context if
    it is non-NULL. If it is NULL, create your own temporary wxClientDC object.
    '''
    def __init__(self, Id=wx.ID_ANY, dc=None):
        '''
        Constructs a wx.EraseEvent.
        '''
        theClass = 'EraseEvent'

        wx.RegisterFirstCallerClassName(self, theClass)

        Event.__init__(self)

        self.tsBeginClassRegistration(theClass, Id)
 
        self.ts_DC = dc
##        self.thisown = theClass

        self.tsEndClassRegistration(theClass)
 
    def GetDC(self):
        '''
        Return the device context the event handler should draw upon.
        '''
        return (self.ts_DC)

    DC = property(GetDC)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
