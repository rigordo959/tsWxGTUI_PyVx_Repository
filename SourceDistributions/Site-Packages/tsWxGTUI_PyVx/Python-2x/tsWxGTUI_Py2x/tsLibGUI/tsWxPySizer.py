#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:53:14 AM rsg>"
'''
tsWxPySizer.py - A special version of wx.Sizer that has been
instrumented to allow the C++ virtual methods to be overloaded
in Python derived classes. You would derive from this class
if you are wanting to implement a custom sizer in Python code.
'''
#################################################################
#
# File: tsWxPySizer.py
#
# Purpose:
#
#    A special version of wx.Sizer that has been instrumented to
#    allow the C++ virtual methods to be overloaded in Python
#    derived classes. You would derive from this class if you are
#    wanting to implement a custom sizer in Python code
#
# Usage (example):
#
#    # Import
#
#    from tsWxPySizer import PySizer
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxPySizer'
__version__   = '1.0.0'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxSizer import Sizer
from tsWxGTUI_Py2x.tsLibGUI.tsWxWindow import Window

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DEFAULT_POS = wxPoint(wx.DefaultPosition)
DEFAULT_SIZE = wxSize(wx.DefaultSize)

#---------------------------------------------------------------------------

class PySizer(Sizer):
    '''
    wx.PySizer is a special version of wx.Sizer that has been instrumented
    to allow the C++ virtual methods to be overloaded in Python derived
    classes. You would derive from this class if you are wanting to implement
    a custom sizer in Python code. Simply implement CalcMin and RecalcSizes
    in the derived class and you are all set.

    When Layout is called it first calls CalcMin followed by RecalcSizes so
    you can optimize a bit by saving the results of CalcMin and reusing them
    in RecalcSizes.

    wxPython Note: If you wish to create a sizer class in wxPython you
    should derive the class from wxPySizer in order to get Python-aware
    capabilities for the various virtual methods.
    '''

    def __init__(self):
        '''
        The constructor.

        Creates a wx.PySizer. Must be called from the __init__ in the
        derived class.
        '''
        theClass = 'PySizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Sizer.__init__(self)

        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)
 
##        self.ts_Children = wxSizerItemList()
##        self.ts_ContainingWindow = None
##        self.ts_MinSize = None
##        self.ts_Position = None
##        self.ts_Size = None

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        Calculate the total minimum width and height needed by all items
        in the sizer according to this sizer layout algorithm.

        This method is abstract and has to be overwritten by any derived
        class.

        Here, the sizer will do the actual calculation of its childrens
        minimal sizes.

        Implemented in wxGridBagSizer, and wxBoxSizer.
        '''
        width = 0
        height = 0
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item = node.GetUserData()

            size = wxSize(0, 0)
            if (isinstance(self, Window)):
                try:
                    parent = self.ts_Parent
                    theClientRect = parent.ClientArea
                except AttributeError:
                    parent = None
                    theClientRect = wxRect(0, 0, 0, 0)

                width = theClientRect.width
                height = theClientRect.height
                minSize = wxSize(width, height)

                self.logger.debug(
                    'CalcMin: item=%s; minSize=%s; width=%s; height=%s' % (
                    str(item), str(minSize), str(width), str(height)))

                size = minSize
                self.logger.debug('CalcMin: size=%s' % size)

            return (size)

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        Recalculate (if necessary) the position and size of each item and
        then call item.SetDimension to do the actual positioning and sizing
        of the items within the space alloted to this sizer.
        '''
        # find the space allotted to this sizer
        pos = self.GetPosition()
        size = self.GetSize()
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item = node.GetUserData()
            # TBD # ...
            itemPos = pos
            itemSize = size
            item.SetDimension(itemPos, itemSize)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
    # Properties

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
