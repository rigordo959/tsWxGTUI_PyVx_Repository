#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:47:37 AM rsg>"
'''
tsWxTopLevelWindow.py - Common base class for wxDialog and
wxFrame. It is an abstract base class meaning that you never
work with objects of this class directly, but all of its
methods are also applicable for the two classes above.

Note that the instances of wxTopLevelWindow are managed by
wxWidgets in the internal top level (task bar) window list.
'''
#################################################################
#
# File: tsWxTopLevelWindow.py
#
# Purpose:
#
#    Common base class for wxDialog and wxFrame. It is an
#    abstract base class meaning that you never work with objects
#    of this class directly, but all of its methods are also
#    applicable for the two classes above.
#
#    Note that the instances of wxTopLevelWindow are managed by
#    wxWidgets in the internal top level (task bar) window list.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTopLevelWindow import TopLevelWindow
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
#    None.
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
#    2010/10/03 rsg - Moved instance variables for the top-level
#                     buttons (OnClose, OnHelp, OnMaximize,
#                     OnMinimize and OnRestore) from Dialog and
#                     Frame.
#
#    2011/12/22 rsg - Added debug message for handling of
#                     tsOnCloseClick: EVT_CLOSE for [X]-Button
#                     of named Top-Level-Window.
#
#    2012/02/21 rsg Modified tsOn... to invoke
#                   tsProcessEventTables.
#
#    2012/07/28 rsg Added evt argument to each tsOn<event>.
#
#    2013/07/06 rsg Removed each tsOn<event> made obsolete
#                   by tsWxFrameButton and tsWxDialogButton.
#
#    2013/07/07 rsg Added self.ts_Closed, self.ts_HelpAsked,
#                   self.ts_Iconize, self.ts_Maximize,
#                   self.ts_RestoreDown and associated Get
#                   and Set methods and properties.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxTopLevelWindow'
__version__   = '1.3.0'
__date__      = '07/07/2013'
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
from tsWxGTUI_Py2x.tsLibGUI.tsWxWindow import Window

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class TopLevelWindow(Window):
    '''
    Common base class for wxDialog and wxFrame. It is an abstract base
    class meaning that you never work with objects of this class directly,
    but all of its methods are also applicable for the two classes above.

    Note that the instances of wxTopLevelWindow are managed by wxWidgets
    in the internal top level (task bar) window list.
    '''
    def __init__(self):
        '''
        '''
        theClass = 'TopLevelWindow'

        wx.RegisterFirstCallerClassName(self, theClass)

        Window.__init__(self, None)

        id = wx.ID_ANY

        self.tsBeginClassRegistration(theClass, id)

        self.ts_DefaultItem = None
##        self.ts_EnableCloseButton = False
        self.ts_Icons = []
##        self.thisown = None
        self.ts_Closed = False
        self.ts_HelpAsked = False
        self.ts_Iconized = False
        self.ts_Maximized = False
        self.ts_RestoreDown = False
        self.ts_ReserveTaskBarArea = wx.ThemeToUse['TaskBar']['Enable']
        self.ts_Shape = None
        self.ts_Title = None
        self.ts_TmpDefaultItem = None

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def CenterOnScreen(self, dir=wx.BOTH):
##        '''
##        Center the window on screen.
##        '''
##        self.CenterOnScreen(direction=dir)

    #-----------------------------------------------------------------------
 
##    def CentreOnScreen(self, dir=wx.BOTH):
##        '''
##        Center the window on screen.
##        '''
##        self.CenterOnScreen(direction=dir)

    #-----------------------------------------------------------------------

    def EnableCloseButton(self, enable):
        '''
        Return True if close button enabled state is being changed.
        Return False if close button enabled state is NOT being changed.
        '''
        if enable:

            if self.ts_EnableCloseButton == enable:
                return (False)
            else:
                self.ts_EnableCloseButton = enable
            return (True)

        else:

            if self.ts_EnableCloseButton == enable:
                return (False)
            else:
                self.ts_EnableCloseButton = enable
            return (True)

    #-----------------------------------------------------------------------

    def GetClosed(self):
        '''
        Return True if top level window has been closed.
        Return False if top level window has NOT been closed.
        '''
        if self.ts_Closed:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def GetDefaultItem(self):
        '''
        Get the default child of this parent, i.e. the first one
        '''
        if self.Children is None:
            return (None)
        else:
            return self.Children[0]

    #-----------------------------------------------------------------------

    def GetHelpAsked(self):
        '''
        Return True if top level window has been asked for Help.
        Return False if top level window has NOT been asked for Help.
        '''
        if self.ts_HelpAsked:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def GetIcon(self):
        '''
        TBD
        '''
        if self.ts_Icons == []:
            return (None)
        else:
            return (self.ts_Icons[0])

    #-----------------------------------------------------------------------

    def GetIconized(self):
        '''
        Return True if top level window has been iconized.
        Return False if top level window has NOT been iconized.
        '''
        if self.ts_Iconized:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def GetMaximized(self):
        '''
        Return True if top level window has been maximuzed.
        Return False if top level window has NOT been maximized.
        '''
        if self.ts_Maximized:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def GetRestoreDown(self):
        '''
        Return True if top level window has been restoredown.
        Return False if top level window has NOT been restoredown.
        '''
        if self.ts_RestoreDown:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def GetTitle(self):
        '''
        TBD - Return title or None as appropriate.
        '''
        try:
            return (self.ts_Title)
        except AttributeError:
            return (None)

    #-----------------------------------------------------------------------

    def GetTmpDefaultItem(self):
        '''
        Return the temporary default item, which can be None.
        '''
        return (self.ts_TmpDefaultItem)

    #-----------------------------------------------------------------------

    def Iconize(self, iconize):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def IsActive(self):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsAlwaysMaximized(self):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsClosed(self):
        '''
        '''
        return (self.ts_Closed)

    #-----------------------------------------------------------------------

    def IsFullScreen(self):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsHelpAsked(self):
        '''
        '''
        return (self.ts_HelpAsked)

    #-----------------------------------------------------------------------

    def IsIconized(self):
        '''
        '''
        return (self.ts_Iconized)

    #-----------------------------------------------------------------------

    def IsMaximized(self):
        '''
        '''
        return (self.ts_Maximized)

    #-----------------------------------------------------------------------

    def IsRestoreDown(self):
        '''
        '''
        return (self.ts_RestoreDown)

    #-----------------------------------------------------------------------

    def MacGetMetalAppearance(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def MacGetUnifiedAppearance(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def MacSetMetalAppearance(self, on):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def Maximize(self, maximize):
        '''
        '''
        self.ts_Maximize = maximize

    #-----------------------------------------------------------------------

    def RequestUserAttention(self, flags):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def RestoreDown(self, restore):
        '''
        '''
        self.ts_RestoreDown = restore

    #-----------------------------------------------------------------------

    def SetClosed(self, closed):
        '''
        '''
        if closed:
            self.ts_Closed = True
            self.ts_HelpAsked = False
            self.ts_Iconized = False
            self.ts_Maximized = False
            self.ts_RestoreDown = False
        else:
            self.ts_Closed = False

    #-----------------------------------------------------------------------

    def SetDefaultItem(self, child):
        '''
        Set this child as default, return the old default.
        '''
        oldDefault = self.DefaultItem
        self.DefaultItem = child
        return (oldDefault)

    #-----------------------------------------------------------------------

    def SetHelpAsked(self, helpAsked):
        '''
        '''
        if (not self.ts_Closed) and helpAsked:
            self.ts_HelpAsked = True
        else:
            self.ts_HelpAsked = False

    #-----------------------------------------------------------------------

    def SetIcon(self, icon):
        '''
        '''
        self.ts_Icons.append(icon)

    #-----------------------------------------------------------------------

    def SetIconized(self, iconized):
        '''
        '''
        if (not self.ts_Closed) and iconized:
            self.ts_Iconized = True
        else:
            self.ts_Iconized = False

    #-----------------------------------------------------------------------

    def SetIcons(self, icons):
        '''
        '''
        for icon in icons:
            self.ts_Icons.append(icon)

    #-----------------------------------------------------------------------

    def SetMaximized(self, maximized):
        '''
        '''
        if (not self.ts_Closed) and maximized:
            self.ts_Maximized = True
        else:
            self.ts_Maximized = False

    #-----------------------------------------------------------------------

    def SetRestoreDown(self, restoredown):
        '''
        '''
        if (not self.ts_Closed) and restoredown:
            self.ts_RestoreDown = True
        else:
            self.ts_RestoreDown = False

    #-----------------------------------------------------------------------

    def SetShape(self, region):
        '''
        '''
        self.ts_Shape = region

    #-----------------------------------------------------------------------

    def SetTitle(self, title):
        '''
        '''
        self.ts_Title = title

    #-----------------------------------------------------------------------

    def SetTmpDefaultItem(self, win):
        '''
        Set this child as temporary default
        '''
        self.ts_TmpDefaultItem = win

    #-----------------------------------------------------------------------

    def ShowFullScreen(self, show, style):
        '''
        '''
        # TBD - Under Construction.
        # Extent resize of the top level window to include its children.
        theDisplay = self.Display
 
        theDisplayPos = wxPoint(theDisplay.ClientArea.x,
                                theDisplay.ClientArea.y)

        theDisplaySize = wxSize(theDisplay.ClientArea.width,
                                theDisplay.ClientArea.height)

        self.logger.debug(
            '      ShowFullScreen (screen): pos=%s; size=%s.' % (
                str(theDisplayPos), str(theDisplaySize)))

        self.Rect = wxRect(theDisplayPos.x,
                           theDisplayPos.y,
                           theDisplaySize.width,
                           theDisplaySize.height)

        self.logger.debug(
            '      Need Event to ShowFullScreen (rect): %s.' % (
                str(self.Rect)))

        return (show)

    #-----------------------------------------------------------------------

    DefaultItem = property(GetDefaultItem, SetDefaultItem)
    Closed = property(GetClosed, SetClosed)
    HelpAsked = property(GetHelpAsked, SetHelpAsked)
    Icon = property(GetIcon, SetIcon)
    Iconized = property(GetIconized, SetIconized)
    Maximized = property(GetMaximized, SetMaximized)
    RestoreDown = property(GetRestoreDown, SetRestoreDown)
##    thisown: The membership flag
    Title = property(GetTitle, SetTitle)
    TmpDefaultItem = property(GetTmpDefaultItem, SetTmpDefaultItem)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
