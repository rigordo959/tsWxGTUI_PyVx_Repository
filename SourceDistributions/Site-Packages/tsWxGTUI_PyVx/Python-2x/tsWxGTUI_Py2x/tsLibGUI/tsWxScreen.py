#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:07:08 AM rsg>"
'''
tsWxScreen.py - Class to provide normal window attributes for a
pseudo parent of Top Level Windows (i.e., Frames and Dialogs)
that have designated "None" as their parent.
'''
#################################################################
#
# File: tsWxScreen.py
#
# Purpose:
#
#    Class to provide normal window attributes for a pseudo
#    parent of Top Level Windows (i.e., Frames and Dialogs)
#    that have designated "None" as their parent.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScreen import Screen
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
#    Create a Top Level Window to which all other windows are children.
#    Example, each Window (i.e., each Frame and Dialog) that has None as
#    its parent is a direct descendant (child) of the Screen. The Screen
#    is a descendant of the Top Level Window Class and therefore conveys
#    all properties of the Window Class.
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
#    2012/01/27 rsg Removed logic for splash screen since the
#                   bit mapped image loading must be handled
#                   as part of the tsWxGraphicalTextUserInterfac
#                   startup logic instead of the wxWidgets code.
#
#    2012/05/02 rsg Added self.ts_DescendantOrderOfShow to
#                   register the order of show of for this
#                   top level window and its descendants.
#
# ToDo:
#
#    2012/01/27 rsg Troubleshoot why the AssignedId (106) for
#                   the screen is found in the "OrderOfShow" list
#                   but not in the "OrderOfShowPanelStack" list
#                   as reported by the tsWxEventLoop module's
#                   tsUpdatePanelStack method during the run
#                   of test_tsWxWidgets.py. Also missing are
#                   AssignedId's for the TaskBar (111), a Frame
#                   (113), a Frame (128) and for the Communicate
#                   Frame (153).
#
#################################################################

__title__     = 'tsWxScreen'
__version__   = '1.3.0'
__date__      = '07/18/2013'
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

import time

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import EVT_SET_FOCUS
from tsWxGTUI_Py2x.tsLibGUI.tsWxGraphicalTextUserInterface \
     import GraphicalTextUserInterface as tsGTUI
from tsWxGTUI_Py2x.tsLibGUI.tsWxTopLevelWindow import TopLevelWindow
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxTextCtrl import TextCtrl as wxTextCtrl

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

BlackOnWhiteDefault = ['cygwin', 'vt100']

WhiteOnBlackDefault = ['xterm-color', 'xterm', 'ansi']

#---------------------------------------------------------------------------

class Screen(TopLevelWindow):
    '''
    Provide normal window attributes for a pseudo parent of Top Level
    Windows (i.e., Frames and Dialogs) that have designated "None" as
    their parent.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.ScreenNameStr):
        '''
        Construct class.
        '''
        theClass = 'Screen'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_title = title
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        TopLevelWindow.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        myRect = self.display.Geometry
        myClientRect = self.display.ClientArea
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              title: %s' % title)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)
            self.logger.debug('             myRect: %s' % str(myRect))
            self.logger.debug('       myClientRect: %s' % str(myClientRect))

        self.ts_Name = name
        self.ts_Parent = parent

        self.ts_DescendantOrderOfShow = [self.ts_AssignedId]

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        if self.TermName in BlackOnWhiteDefault:
            self.ts_ForegroundColour = wx.COLOR_BLACK
            self.ts_BackgroundColour = wx.COLOR_WHITE
        else:
            self.ts_ForegroundColour = wx.COLOR_WHITE
            self.ts_BackgroundColour = wx.COLOR_BLACK

##        self.ts_FocusEnabled = True
        self.SetFocus()

        self.ts_Label = title
        self.ts_Style = style
        self.ts_Title = title

        try:

            self.ts_Handle = self.display.TheTerminalScreen

            msg = 'tsWxScreen.__init__: ts_handle=%s' % self.ts_Handle
            self.logger.debug(msg)

        except Exception, handleError:

            self.ts_Handle = None

            msg = 'tsWxScreen.__init__: handleError=%s' % str(handleError)
            self.logger.warning(msg)

        try:

            # Screen is a window that represents the nCurses stdscr.
            self.tsRegisterClassWindow()

        except Exception, registerError:

            msg = 'tsWxScreen.__init__: registerError=%s' % str(registerError)
            self.logger.warning(msg)
            # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Show(self, show=True):
        '''
        Shows or hides the window. You may need to call Raise for a top
        level window if you want to bring it to top, although this is not
        needed if Show is called immediately after the frame creation.
        Returns True if the window has been shown or hidden or False if
        nothing was done because it already was in the requested state.
        '''
        if self.tsIsShowPermitted and show:

            self.ts_Shown = True

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

        else:

            self.ts_Shown = False

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetChildren(self):
        '''
        Return a list of the top level windows that are descendants of the
        screen.
        '''
        return (self.tsGetChildren())

    #-----------------------------------------------------------------------

    def tsGetTermName(self):
        '''
        Return the terminal name.
        '''
        return (self.display.TheTerminal.TermName)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Children = property(tsGetChildren)
    TermName = property(tsGetTermName)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
