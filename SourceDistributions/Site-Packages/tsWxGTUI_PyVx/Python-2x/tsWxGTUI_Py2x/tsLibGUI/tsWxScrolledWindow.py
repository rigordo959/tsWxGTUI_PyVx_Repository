#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:12:20 AM rsg>"
'''
tsWxScrolledWindow.py - Class to manage scrolling for its
client area, transforming the coordinates according to the
scrollbar positions, and setting the scroll positions, thumb
sizes and ranges according to the area in view.
'''
#################################################################
#
# File: tsWxScrolledWindow.py
#
# Purpose:
#
#    Class to manage scrolling for its client area, transforming
#    the coordinates according to the scrollbar positions, and
#    setting the scroll positions, thumb sizes and ranges
#    according to the area in view.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrolledWindow import ScrolledWindow as wxScrolledWindow
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Notes:
#
#    See Notes section in tsWxScrolled.py
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Modifications:
#
#    2012/03/01 rsg Replaced wxPython-style logic with those of
#                   the base class, tsWxScrolled.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxScrolledWindow'
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

from tsWxGTUI_Py2x.tsLibGUI.tsWxScrolled import Scrolled

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class ScrolledWindow(Scrolled):
    '''
    The wxScrolledWindow class manages scrolling for its client area,
    transforming the coordinates according to the scrollbar positions,
    and setting the scroll positions, thumb sizes and ranges according
    to the area in view.

    Starting from version 2.4 of wxWidgets, there are several ways to use
    a wxScrolledWindow. In particular, there are now three ways to set the
    size of the scrolling area:

    One way is to set the scrollbars directly using a call to
    wxScrolledWindow::SetScrollbars. This is the way it used to be in
    any previous version of wxWidgets and it will be kept for backwards
    compatibility.

    An additional method of manual control, which requires a little less
    computation of your own, is to set the total size of the scrolling
    area by calling either wxWindow::SetVirtualSize, or wxWindow::FitInside,
    and setting the scrolling increments for it by calling
    wxScrolledWindow::SetScrollRate. Scrolling in some orientation is
    enabled by setting a non-zero increment for it.

    The most automatic and newest way is to simply let sizers determine
    the scrolling area. This is now the default when you set an interior
    sizer into a wxScrolledWindow with wxWindow::SetSizer. The scrolling
    area will be set to the size requested by the sizer and the scrollbars
    will be assigned for each orientation according to the need for them
    and the scrolling increment set by wxScrolledWindow::SetScrollRate.
    As above, scrolling is only enabled in orientations with a non-zero
    increment. You can influence the minimum size of the scrolled area
    controlled by a sizer by calling wxWindow::SetVirtualSizeHints.
    (calling wxScrolledWindow::SetScrollbars has analogous effects in
    wxWidgets 2.4 -- in later versions it may not continue to override
    the sizer)

    Note: if Maximum size hints are still supported by SetVirtualSizeHints,
    use them at your own dire risk. They may or may not have been removed
    for 2.4, but it really only makes sense to set minimum size hints here.
    We should probably replace SetVirtualSizeHints with SetMinVirtualSize
    or similar and remove it entirely in future.

    As with all windows, an application can draw onto a wxScrolledWindow
    using a device context.

    You have the option of handling the OnPaint handler or overriding the
    OnDraw function, which is passed a pre-scrolled device context
    (prepared by DoPrepareDC).

    If you do not wish to calculate your own scrolling, you must call
    DoPrepareDC when not drawing from within OnDraw, to set the device
    origin for the device context according to the current scroll position.

    A wxScrolledWindow will normally scroll itself and therefore its
    child windows as well. It might however be desired to scroll a
    different window than itself: e.g. when designing a spreadsheet,
    you will normally only have to scroll the (usually white) cell area,
    whereas the (usually grey) label area will scroll very differently.
    For this special purpose, you can call SetTargetWindow which means
    that pressing the scrollbars will scroll a different window.

    Note that the underlying system knows nothing about scrolling
    coordinates, so that all system functions (mouse events, expose events,
    refresh calls etc) as well as the position of subwindows are relative
    to the "physical" origin of the scrolled window. If the user insert
    a child window at position (10,10) and scrolls the window down 100
    pixels (moving the child window out of the visible area), the child
    window will report a position of (10,-90).

    Derived from

    wxPanel
    wxWindow
    wxEvtHandler
    wxObject
    '''

    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.HSCROLL | wx.VSCROLL,
                 name=wx.PanelNameStr):
        '''
        Construct and show a generic Window.
        '''
        theClass = 'ScrolledWindow'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Scrolled.__init__(self,
                          parent,
                          id=id,
                          pos=pos,
                          size=size,
                          style=style,
                          name=name)

        self.tsBeginClassRegistration(theClass, id)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        self.ts_BackgroundColour = wx.ThemeToUse['ForegroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse['BackgroundColour'].lower()

        myRect, myClientRect = self.tsScrolledLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
