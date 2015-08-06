#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:35:56 AM rsg>"
'''
tsWxGridBagSizer.py - Class to emulate the wxPython API for non-graphical,
curses-based platforms.
'''
#################################################################
#
# File: tsWxGridBagSizer.py
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
#    from tsWxGridBagSizer import GridBagSizer
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

__title__     = 'tsWxGridBagSizer'
__version__   = '1.0.1'
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
from tsWxSizer import Sizer

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class GridBagSizer(Sizer):
    '''
    A wx.Sizer that can lay out items in a virtual grid like a
    wx.FlexGridSizer but in this case explicit positioning of the items
    is allowed using wx.GBPosition, and items can optionally span more
    than one row and/or column using wx.GBSpan. The total size of the
    virtual grid is determined by the largest row and column that items
    are positioned at, adjusted for spanning.
    '''
    def __init__(self, vgap=0, hgap=0):
        '''
        Constructor, with optional parameters to specify the gap between
        the rows and columns.
        '''
        theClass = 'GridBagSizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Sizer.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        self.ts_vgap = vgap
        self.ts_hgap = hgap

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##wx.GBSizerItem        Add(self, item, pos, span, flag, border, userData)
##Adds an item to the sizer at the grid cell pos, optionally spanning more than one row or column as specified with span.
##      AddItem(*args, **kwargs)
##Add(self, GBSizerItem item) -> wx.GBSizerItem
##bool  CheckForIntersection(self, item, excludeItem)
##Look at all items and see if any intersect (or would overlap) the given item.
##bool  CheckForIntersectionPos(self, pos, span, excludeItem)
##Look at all items and see if any intersect (or would overlap) the given position and span.
##GBSizerItem   FindItem(self, item)
##Find the sizer item for the given window or subsizer, returns None if not found.
##GBSizerItem   FindItemAtPoint(self, pt)
##Return the sizer item located at the point given in pt, or None if there is no item at that point.
##GBSizerItem   FindItemAtPosition(self, pos)
##Return the sizer item for the given grid cell, or None if there is no item at that position.
##Size  GetCellSize(self, row, col)
##Get the size of the specified cell, including hgap and vgap.
##Size  GetEmptyCellSize(self)
##Get the size used for cells in the grid with no item.
##      GetItem(self, item)
##GBPosition    GetItemPosition(self, item)
##Get the grid position of the specified item where item is either a window or subsizer that is a member of this sizer, or a zero-based index of an item.
##GBSpan        GetItemSpan(self, item)
##Get the row/col spanning of the specified item where item is either a window or subsizer that is a member of this sizer, or a zero-based index of an item.
##      SetEmptyCellSize(self, sz)
##Set the size used for cells in the grid with no item.
##bool  SetItemPosition(self, item, pos)
##Set the grid position of the specified item where item is either a window or subsizer that is a member of this sizer, or a zero-based index of an item.
##bool  SetItemSpan(self, item, span)
##Set the row/col spanning of the specified item where item is either a window or subsizer that is a member of this sizer, or a zero-based index of an item.

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
