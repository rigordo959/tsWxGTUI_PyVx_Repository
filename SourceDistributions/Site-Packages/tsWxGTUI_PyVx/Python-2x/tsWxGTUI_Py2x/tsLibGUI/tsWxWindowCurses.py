#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:30:39 AM rsg>"
'''
tsWxWindowCurses.py - Base class for all windows and represents any
visible object on the screen. All controls, top level windows
and so on are wx.Windows. Sizers and device contexts are not
however, as they do not appear on screen themselves.
'''
#################################################################
#
# File: tsWxWindowCurses.py
#
# Purpose:
#
#    Base class for all windows and represents any visible object
#    on the screen. All controls, top level windows and so on are
#    wx.Windows. Sizers and device contexts are not however, as
#    they do not appear on screen themselves.
#
# Usage (example):
#
#    # Import
#
#    from tsWxWindowCurses import WindowCurses
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
#    The wxPython emulator introduces the concept of the Earliest
#    Ancestor for each Top-Level Window and decendent child window.
#    The intent is to facilitate visibility determination when
#    windows are fully or partially overlaid by windows associated
#    with another Top-Level Window. Unless the application developer
#    or user has designted the Top-Level Window to have focus, the
#    emulator will assume that components of newer Top-Level Windows
#    should overlay components of older Top-Level Windows.
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    WindowCurses
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    WindowCurses.__init__
#    WindowCurses.tsCursesAddCh
#    WindowCurses.tsCursesAddNStr
#    WindowCurses.tsCursesAddStr
#    WindowCurses.tsCursesAttrOff
#    WindowCurses.tsCursesAttrOn
#    WindowCurses.tsCursesAttrSet
#    WindowCurses.tsCursesBeep
#    WindowCurses.tsCursesBkgd
#    WindowCurses.tsCursesBkgdSet
#    WindowCurses.tsCursesBorder
#    WindowCurses.tsCursesBox
#    WindowCurses.tsCursesCaretVisibility
#    WindowCurses.tsCursesChgAt
#    WindowCurses.tsCursesClear
#    WindowCurses.tsCursesClearOk
#    WindowCurses.tsCursesClrToBot
#    WindowCurses.tsCursesClrToEol
#    WindowCurses.tsCursesDoUpdate
#    WindowCurses.tsCursesEcho
#    WindowCurses.tsCursesErase
#    WindowCurses.tsCursesFlash
#    WindowCurses.tsCursesFlushInp
#    WindowCurses.tsCursesGetBegYX
#    WindowCurses.tsCursesGetMaxYX
#    WindowCurses.tsCursesGetParYX
#    WindowCurses.tsCursesGetYX
#    WindowCurses.tsCursesHasColors
#    WindowCurses.tsCursesInch
#    WindowCurses.tsCursesInstr
#    WindowCurses.tsCursesMoveCursor
#    WindowCurses.tsCursesNewWindow
#    WindowCurses.tsCursesNewWindowGenealogy
#    WindowCurses.tsCursesNoEcho
#    WindowCurses.tsCursesPanelUpdatePanels
#    WindowCurses.tsCursesPflush
#    WindowCurses.tsCursesScroll
#    WindowCurses.tsCursesScrollOk
#    WindowCurses.tsCursesTermname
#    WindowCurses.tsCursesTextpad
#    WindowCurses.tsCursesTextpadDoCommand
#    WindowCurses.tsCursesTextpadEdit
#    WindowCurses.tsCursesTextpadGather
#    WindowCurses.tsCursesTextpadStripspaces
#    WindowCurses.tsCursesWindowNoutRefresh
#    WindowCurses.tsCursesWindowRedrawWin
#
# Modifications:
#
#    2010/03/07 rsg Added event handlers for OnClose, OnMaximize and
#                   OnMinimize.
#
#    2010/03/19 rsg Enabled SetAcceleratorTable. Needed because
#                   cygwin terminal does not support mouse.
#
#    2010/07/16 rsg Modified tsCreateButtonLine to support
#                   use of "&" to designate accelerator
#                   character.
#
#    2010/08/10 rsg Added ts_HotKeyData to retain location of "&"
#                   which designates the accelerator character and
#                   the applicable Alt-Ctrl-Shift key combination.
#
#    2010/08/27 rsg Modified tsBuildCursesNewWindowGenealogy to
#                   capture data from self.ts_SystemEventTable
#                   and self.ts_UserEventTable.
#
#    2010/08/31 rsg For consistancy with wxPython and industry
#                   conventions, changed characterCellAccelerator
#                   to "tsGTUI.DISPLAY_UNDERLINE"
#                   from "tsGTUI.DISPLAY_BOLD".
#
#    2010/10/20 rsg Simplify Window.Layout method's access to
#                   Sizer.Layout.
#
#    2011/12/04 rsg Corrected tsIsBorderStyle. Return False when
#                   style == 0 or style == wx.BORDER_NONE.
#
#    2011/12/05 rsg Applied bold attribute to tsCreateLabelLine.
#
#    2011/12/17 rsg Added self.ts_PanelLayer invocation in
#                   tsRegisterClassWindow in order to track
#                   curses.panel type objects.
#
#    2011/12/26 rsg Added logic to tsWindowLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2011/12/28 rsg Modified SetFocusFromKbd by adding
#                   curses.doupdate() after
#                   curses.panel.update_panels().
#
#    2011/12/29 rsg Added tsCursesHasColors to prevent
#                   application from trapping if terminal
#                   (such as vt100) only supports black on
#                   white or white on black.
#
#    2012/01/15 rsg Removed code for unused originalAlgorothm
#                   from tsBuildCursesNewWindowGenealogy method.
#
#    2012/01/17 rsg Added conditional logic to RegisterClassWindow
#                   that creates and registers a curses panel
#                   layer only when a new windows has an
#                   associated handle. The conditional logic also
#                   was moved ahead of the data base update logic
#                   to correct the erroneous PanelLayer = None.
#
#    2012/01/19 rsg Revert back to Show without any ShowTiled and
#                   ShowOverlayed special cases.
#
#    2012/01/20 rsg Modified tsRegisterShowOrder to register
#                   PanelLayer in addition to AssignedId.
#
#    2012/01/20 rsg Modified tsRegisterShowOrder to register
#                   AssignedIdByPanelLayer.
#
#    2012/01/25 rsg Added OrderOfShowPanelStack to tsRegisterShowOrder.
#
#    2012/01/25 rsg Substituted "tsWxGTUI_DataBase" in references
#                   to "tsGTUI.GraphicalTextUserInterface".
#
#    2012/01/31 rsg Revised tsIsBorderStyle to apply BORDER_MASK
#                   to ignore non-border styles.

#    2012/02/04 rsg Added tsRoundHorizontal and tsRoundVertical
#                   methods.
#
#    2012/02/16 rsg Modified tsOn... to invoke
#                   tsProcessSelectedEventTable.
#
#    2012/02/21 rsg Removed tsProcessSelectedEventTable because it
#                   and its controller, tsProcessEventTable, are
#                   provided by tsWxEvtHandler.
#
#    2012/03/05 rsg Added split option to tsRoundHorizontal and
#                   tsRoundVertical methods.
#
#    2012/03/05 rsg Added tsRoundXY method which combines the
#                   actions of methods tsRoundHorizontal and
#                   tsRoundVertical.
#
#    2012/03/12 rsg Added tsCursesInch and tsCursesInstr methods.
#
#    2012/03/29 rsg Applied wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK
#                   to ensure that only font style attributes are
#                   passed to curses for non-color displays (such
#                   as vt100 and vt220).
#
#    2012/05/01 rsg Added logic to tsBuildCursesNewWindowGenealogy
#                   for including DescendantOrderOfShow.
#
#    2012/05/05 rsg Modified tsCursesInch to return attribute
#                   in addition to the character.
#
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
#    2012/07/01 rsg Added registration of WindowsByHandle, WindowsByPad
#                   and WindowsByPanelLayer in GraphicalTextUserInterface
#                   class.
#
#    2012/07/03 rsg Added tsCursesDoUpdate, tsCursesPanelUpdatePanels,
#                   tsCursesWindowNoutRefresh and
#                   tsCursesWindowRedrawWin.
#
#    2012/07/07 rsg Imported curses.textpad. Added tsCursesBeep,
#                   tsCursesTextPad and its associated methods.
#
#    2012/07/19 rsg Added class variable TheKeyboardInputRecipient.
#
#    2012/07/21 rsg Added the following curses interface modules, in
#                   support of tsWxTextEntryDialog:
#                   tsCursesEcho, tsCursesFlash, tsCursesFlushInp,
#                   tsCursesMoveCursor and tsCursesNoEcho.
#
#    2012/08/15 rsg Added methods to erase or clear the various
#                   portions of the windows associated with curses
#                   handles.
#
#    2012/09/18 rsg Added logic to tsCursesCaretVisibility that
#                   returns the previous or default visibility level.
#
#    2013/06/21 rsg Referenced high-level self.tsCursesPanelUpdatePanels()
#                   instead of low-level curses.panel.update_panel()
#
#    2013/06/21 rsg Referenced high-level self.tsCursesDoUpdate()
#                   instead of low-level curses.doupdate()
#
#    2013/06/21 rsg Moved tsTaskBarTopTask, tsTaskBarTopChild and
#                   tsTaskBarDumpPanelStack from tsWxTaskBar to
#                   tsWxWindows.
#
#    2013/07/10 rsg Various updates associated with panel layer
#                   hiding when closing and iconizing a window.
#
#    2013/07/18 rsg Added method tsIsShowPermitted to facilitate
#                   the imposition of a permanent CLOSE or temporary
#                   ICONIZE override to the permission for showing of
#                   a window, ita children and its ancestors.
#
#    2013/10/25 rsg Added Troubleshooting definitions and applied
#                   them to definition of DEBUG.
#
#    2014/01/03 rsg Updated Copyright.
#
#    2014/01/13 rsg Replaced references to tsGTUI.color256 by references
#                   to tsGTUI.xterm256Color for compatibility with the
#                   re-designed tsWxGraphicalTextUserInterface module.
#
#    2014/05/11 rsg Resolved compatibility with Python 3.3 and 3.4 by
#                   replacing "import curses." by "from curses import ".
#                   This resulted in the followin:
#
#                   "import curses"
#                   "from curses import ascii"
#                   "from curses import error" as cursesErrorMethod
#                   "from curses import panel"
#                   "from curses import textpad"
#                   "from curses import wrapper"
#
#                   "import _curses"
#
#    2014/05/19 rsg Interchanged position of boilerplate for Classes
#                   and Methods and added alphabetical list of methods.
#
#    2014/05/22 rsg Added tsCursesPflush method in attempt to apply
#                   wx.USE_CURSES_PANEL_STACK.
#
#    2014/06/28 rsg Added tsCursesBaudRate method.
#
# ToDo:
#
#    2011/12/26 rsg Troubleshoot tsWindowLayout. Resolve why
#                   Window based Controls do not initialize via
#                   self.ts_Handle = None. Thought I did that for:
#                   Button, CheckBox, Gauge, RadioBox, RadioButton,
#                   StaticText, TaskBarButton and TextCtrl.
#
#    2011/12/28 rsg Research SetFocusFromKbd. Need to discover
#                   what new information needs to be set and what
#                   old information needs to be cleared.
#                   NOTE: SetFocusFromKbd actions need to be
#                   coordinated with those of TaskBar.
#
#################################################################

__title__     = 'tsWxWindowCurses'
__version__   = '1.24.0'
__date__      = '06/28/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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

import curses
##from curses import ascii
from curses import panel
from curses import textpad
##from curses import wrapper
#
import _curses

import os
import sys
import types
import traceback

from textwrap import TextWrapper

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsApplication
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvtHandler import EvtHandler
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxSystemSettings \
     import SystemSettings as wxSystemSettings

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

tsWxGTUI_DataBase = tsGTUI.GraphicalTextUserInterface

DEFAULT_POS = wxPoint(wx.DefaultPosition)
DEFAULT_SIZE = wxSize(wx.DefaultSize)

#--------------------------------------------------------------------------

class WindowCurses(object):
    '''
    wx.Window is the base class for all windows and represents any visible
    object on the screen. All controls, top level windows and so on are
    wx.Windows. Sizers and device contexts are not however, as they do not
    appear on screen themselves.
    '''

    #-----------------------------------------------------------------------
    # Class Variables

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        Constructs a window, which can be a child of a frame, dialog
        or any other non-control window.
        '''
        theClass = 'WindowCurses'

        wx.RegisterFirstCallerClassName(self, theClass)

    #-----------------------------------------------------------------------

    def tsCursesAddCh(self, x, y, character, attr=None, pixels=True):
        '''
        Paint character ch at (y, x) with attributes attr, overwriting any
        character previously painter at that location. By default, the
        character position and attributes are the current settings for
        the window object
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if pixels:
                (xCol, yRow) = self.tsGetCharacterValues(x, y)
            else:
                (xCol, yRow) = (x, y)

            if attr is None:

                window.addch(int(yRow), int(xCol), ord(character))

            else:

                if self.stdscr.HasColors:

                    theAttr = attr

                else:

                    try:

                        theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                    except Exception, errorCode:

                        DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                        theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                window.addch(int(yRow), int(xCol), ord(character), theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesAddNStr(self, x, y, string, n, attr=None, pixels=True):
        '''
        Paint at most n characters of the string str at (y, x) with
        attributes attr, overwriting anything previously on the display.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if pixels:
                (xCol, yRow) = self.tsGetCharacterValues(x, y)
            else:
                (xCol, yRow) = (x, y)

            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                       pixels=False)
            width = self.Rect.width - 2 * borderThickness.width
            excess = xCol + len(string) - width
            if xCol + len(string) < width:
                myString = string
            elif excess < 0:
                myString = wx.EmptyString
            else:
                myString = string[0:len(string) - excess]

            if myString != wx.EmptyString:

                if attr is None:

                    window.addnstr(int(yRow), int(xCol), myString, n)

                else:

                    if self.stdscr.HasColors:

                        theAttr = attr

                    else:

                        try:

                            theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                        except Exception, errorCode:

                            DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                            theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                    window.addnstr(int(yRow), int(xCol), myString, n, theAttr)

                status = True

            else:

                status = False

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesAddStr(self, x, y, string, attr=None, pixels=True):
        '''
        Paint the string str at (y, x) with attributes attr, overwriting
        anything previously on the display.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if pixels:
                (xCol, yRow) = self.tsGetCharacterValues(x, y)
            else:
                (xCol, yRow) = (x, y)

            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                       pixels=False)
            width = self.Rect.width - 2 * borderThickness.width
            excess = xCol + len(string) - width
            if xCol + len(string) < width:
                myString = string
            elif excess < 0:
                myString = wx.EmptyString
            else:
                myString = string[0:len(string) - excess]

            if myString != wx.EmptyString:

                if attr is None:

                    window.addstr(int(yRow), int(xCol), myString)

                else:

                    if self.stdscr.HasColors:

                        theAttr = attr

                    else:

                        try:

                            theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                        except Exception, errorCode:

                            DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                            theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                    window.addstr(int(yRow), int(xCol), myString, theAttr)

                status = True

            else:

                status = False

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesAttrOff(self, attr):
        '''
        Remove attribute attr from the ``background'' set applied to all
        writes to the current window.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:

            if self.stdscr.HasColors:

                theAttr = attr

            else:

                try:

                    theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                except Exception, errorCode:

                    DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                    theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

            window.attroff(theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesAttrOn(self, attr):
        '''
        Add attribute attr from the ``background'' set applied to all
        writes to the current window.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:

            if self.stdscr.HasColors:

                theAttr = attr

            else:

                try:

                    theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                except Exception, errorCode:

                    DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                    theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

            window.attron(theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesAttrSet(self, attr):
        '''
        Set the ``background set of attributes to attr. This set is
        initially 0 (no attributes).
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:

            if self.stdscr.HasColors:

                theAttr = attr

            else:

                try:

                    theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                except Exception, errorCode:

                    DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                    theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

            window.attrset(theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesBaudRate(self):
        '''
        Return the output speed of the terminal in bits per second. On
        software terminal emulators it will have a fixed high value.
        Included for historical reasons; in former times, it was used
        to write output loops for time delays and occasionally to
        change interfaces depending on the line speed.
        '''
        curses.baudrate()

    #-----------------------------------------------------------------------

    def tsCursesBeep(self):
        '''
        Emit a short attention sound.
        '''
        curses.beep()

    #-----------------------------------------------------------------------

    def tsCursesBkgd(self, ch=' ', attr=None):
        '''
        Sets the background property of the window to the character ch, with
        attributes attr. The change is then applied to every character
        position in that window:

        * The attribute of every character in the window is changed to the
        new background attribute.

        * Wherever the former background character appears, it is changed to
        the new background character.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if self.stdscr.HasColors:
                foreground = self.GetForegroundColour()
                background = self.GetBackgroundColour()
                self.logger.debug(
                    '         foreground: %s' % foreground)
                self.logger.debug(
                    '         background: %s' % background)
                attr = self.stdscr.tsGetAttributeValueFromColorPair(
                    foreground,
                    background)

            if attr is None:

                window.bkgd(ch)

            else:

                if self.stdscr.HasColors:

                    theAttr = attr

                else:

                    try:

                        theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                    except Exception, errorCode:

                        DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                        theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                window.bkgd(ch, theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesBkgdSet(self, ch=' ', attr=None):
        '''
        Sets the window background. A window background consists of a
        character and any combination of attributes. The attribute part
        of the background is combined (ORed) with all non-blank characters
        that are written into the window. Both the character and attribute
        parts of the background are combined with the blank characters.
        The background becomes a property of the character and moves with
        the character through any scrolling and insert/delete line/character
        operations.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if  self.stdscr.HasColors:
                foreground = self.GetForegroundColour()
                background = self.GetBackgroundColour()
                self.logger.debug(
                    '         foreground: %s' % foreground)
                self.logger.debug(
                    '         background: %s' % background)
                attr = self.stdscr.tsGetAttributeValueFromColorPair(
                    foreground,
                    background)

            if attr is None:
                window.bkgdset(ch)
            else:

                if self.stdscr.HasColors:

                    theAttr = attr

                else:

                    try:

                        theAttr = attr & wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                    except Exception, errorCode:

                        DISPLAY_NON_COLOR_ATTRIBUTE_MASK = 0x3F0000
                        theAttr = attr & DISPLAY_NON_COLOR_ATTRIBUTE_MASK

                window.bkgdset(ch, theAttr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesBorder(self, ls, rs, ts, bs, tl, tr, bl, br):
        '''
        Draw a border around the edges of the window. Each parameter specifies
        the character to use for a specific part of the border; see the table
        below for more details. The characters can be specified as integers or
        as one-character strings.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            window.border(ls, rs, ts, bs, tl, tr, bl, br)
            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesBox(self, vertch=None, horch=None):
        '''
        Similar to border(), but both ls and rs are vertch and both ts and
        bs are horch. The default corner characters are always used by this
        function.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if vertch is None:
                vertch = curses.ACS_VLINE

            if horch is None:
                horch = curses.ACS_HLINE

            window.box(vertch, horch)
            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesCaretVisibility(self, visibility=wx.caretInvisible):
        '''
        Sets the cursor state. visibility can be set to 0, 1, or 2, for
        invisible, normal, or very visible. If the terminal supports the
        visibility requested, the previous cursor state is returned;
        otherwise, an exception is raised. On many terminals, the
        "visible" mode is an underline cursor and the "very visible"
        mode is a block cursor.
        '''
        try:

            return (curses.curs_set(visibility))

        except Exception, errorCode:

            fmt1 = 'tsWxWindow.tsCursesCaretVisibility: '
            fmt2 = 'errorCode="%s".' % str(errorCode)
            msg = fmt1 + fmt2
            print('WARNING: %s\n' % msg)
            self.logger.warning(msg)
            curses.curs_set(visibility)

            return (wx.caretNormal)

    #-----------------------------------------------------------------------

    def tsCursesChgAt(self,
                      x=wx.DefaultValue,
                      y=wx.DefaultValue,
                      num=-1,
                      attr=wx.DISPLAY_NORMAL,
                      pixels=True):
        '''
        Sets the attributes of num characters at the current cursor
        position, or at position (y, x) if supplied. If no value of
        num is given or num = -1, the attribute will be set on all the
        characters to the end of the line. This function does not move
        the cursor. The changed line will be touched using the touchline()
        method so that the contents will be redisplayed by the next
        window refresh.
        '''
        window = self.ts_Handle
        if window is None:

            status = False

        else:

            if pixels:

                (xCol,  yRow) = wx.tsGetCharacterValues(x, y)

            else:

                (xCol,  yRow) = (x, y)

            if ((xCol == wx.DefaultValue) and \
                (yRow == wx.DefaultValue)):

                window.chgat(num, attr)

            else:

                window.chgat(yRow, xCol, num, attr)

    #-----------------------------------------------------------------------

    def tsCursesClear(self):
        '''
        Like erase(), but also causes the whole window to be repainted
        upon next call to refresh().
        '''
        window = self.ts_Handle
        if not (window is None):

            window.clear()

    #-----------------------------------------------------------------------

    def tsCursesClearOk(self, yes):
        '''
        If yes is 1, the next call to refresh() will clear the window
        completely.
        '''
        window = self.ts_Handle
        if not (window is None):

            if yes:
                window.clearok(1)
            else:
                window.clearok(0)

    #-----------------------------------------------------------------------

    def tsCursesClrToBot(self):
        '''
        Erase from cursor to the end of the window: all lines below
        the cursor are deleted, and then the equivalent of clrtoeol()
        is performed.
        '''
        window = self.ts_Handle
        if not (window is None):

            window.clrtobot()

    #-----------------------------------------------------------------------

    def tsCursesClrToEol(self):
        '''
        Erase from cursor to the end of the line.
        '''
        window = self.ts_Handle
        if not (window is None):

            window.clrtoeol()

    #-----------------------------------------------------------------------

    def tsCursesDoUpdate(self):
        '''
        Update the physical screen. The curses library keeps two data
        structures, one representing the current physical screen contents
        and a virtual screen representing the desired next state. The
        doupdate() ground updates the physical screen to match the virtual
        screen.

        The virtual screen may be updated by a noutrefresh() call after
        write operations such as addstr() have been performed on a window.
        The normal refresh() call is simply noutrefresh() followed by
        doupdate(); if you have to update multiple windows, you can speed
        performance and perhaps reduce screen flicker by issuing
        noutrefresh() calls on all windows, followed by a single
        doupdate().
        '''
        if wx.USE_CURSES_PANEL_STACK:
            self.tsCursesPflush()

        curses.doupdate()

    #----------------------------------------------------------------------

    def tsCursesEcho(self):
        '''
        Enter echo mode. In echo mode, each character input is echoed
        to the screen as it is entered.
        '''
        curses.echo()

    #-----------------------------------------------------------------------

    def tsCursesErase(self):
        '''
        Clear the window.
        '''
        window = self.ts_Handle
        if not (window is None):

            window.erase()

    #-----------------------------------------------------------------------

    def tsCursesFlash(self):
        '''
        Flash the screen. That is, change it to reverse-video and then
        change it back in a short interval. Some people prefer such as
        "visible bell" to the audible attention signal produced by
        beep().
        '''
        curses.flash()

    #----------------------------------------------------------------------

    def tsCursesFlushInp(self):
        '''
        Flush all input buffers. This throws away any typeahead that has
        been typed by the user and has not yet been processed by the
        program.
        '''
        curses.flushinp()

    #----------------------------------------------------------------------

    def tsCursesGetBegYX(self, pixels=True):
        '''
        Return a tuple (y, x) of co-ordinates of upper-left corner.
        '''
        window = self.ts_Handle
        if window is None:
            (begin_y, begin_x) = (-1, -1)
        else:
            try:
                (begin_y, begin_x) = window.getbegyx()

            except Exception, cursesError:
                msg = 'Window tsCursesGetBegYX Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if pixels:
            return (self.tsGetPixelValues(begin_x, begin_y))
        else:
            return (begin_x, begin_y)

    #-----------------------------------------------------------------------

    def tsCursesGetMaxYX(self, pixels=True):
        '''
        Return a tuple (y, x) of the height and width of the window.
        '''
        window = self.ts_Handle
        if window is None:
            (max_y, max_x) = (-1, -1)
        else:
            try:
                (max_y, max_x) = window.getmaxyx()

            except Exception, cursesError:
                msg = 'Window tsCursesGetMaxYX Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if pixels:
            return (self.tsGetPixelValues(max_x, max_y))
        else:
            return (max_x, max_y)

    #-----------------------------------------------------------------------

    def tsCursesGetParYX(self, pixels=True):
        '''
        Returns the beginning coordinates of this window relative to its
        parent window into two integer variables y and x. Returns -1,-1
        if this window has no parent.
        '''
        window = self.ts_Handle
        if window is None:
            (par_y, par_x) = (-1, -1)
        else:
            try:
                (par_y, par_x) = window.getparyx()

            except Exception, cursesError:
                msg = 'Window tsCursesGetParYX Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if pixels:
            return (self.tsGetPixelValues(par_x, par_y))
        else:
            return (par_x, par_y)

    #-----------------------------------------------------------------------

    def tsCursesGetYX(self, pixels=True):
        '''
        Return a tuple (y, x) of current cursor position relative to the
        window upper-left corner.
        '''
        window = self.ts_Handle
        if window is None:
            (y, x) = (-1, -1)
        else:
            try:
                (y, x) = window.getyx()

            except Exception, cursesError:
                msg = 'Window tsCursesGetYX Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if pixels:
            return (self.tsGetPixelValues(x, y))
        else:
            return (x, y)

    #-----------------------------------------------------------------------

    def tsCursesHasColors(self):
        '''
        Returns true if the terminal can display colors; otherwise, it
        returns false.
        '''
        if self.stdscr.Stdscr.has_colors():
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def tsCursesInch(self, x, y, win=None, pixels=True):
        '''
        Return the character and its associated attributes at the specified
        caret horizontal (x) and vertical (y) position for the curses window
        associated with the default or specified GUI object.

        The position may be specified in pixel or character cell units.
        '''
        if win is None:

            # Default GUI Object
            window = self.ts_Handle

        else:

            # Specified GUI Objec
            if win == self.stdscr.Stdscr:

                window = self.stdscr.Stdscr

            else:

                window = win.ts_Handle

        if window is None:

            # Curses GUI Object does not exist
            character = chr(0x00) # ASCII "nul"
            attribute = 0

        else:

            # Curses GUI Object does exist
            if pixels:

                # Convert caret pixel to character cell position
                (caretX, caretY) = wx.tsGetPixelValues(x, y)

            else:

                # Use caret character cell position
                (caretX, caretY) = (x, y)

            # Get the character at the given position in the window. The
            # bottom 8 bits are the character proper, and upper bits are
            # the attributes.

            attributedCharacterUnderCaret = window.inch(caretY, caretX)

            if False:
                attribute = (
                    int(attributedCharacterUnderCaret) & 0xFF00) / 256
            else:
                attribute = (
                    int(attributedCharacterUnderCaret) & 0xFFFFFF00)

            character = chr(
                int(attributedCharacterUnderCaret) & 0xFF)

            msg = 'tsWxWindow.tsCursesInch: ' + \
                'characterUnderCaret=0x%x (%c)' % \
                (ord(character), character)
            self.logger.debug(msg)

        return (character, attribute)

    #-----------------------------------------------------------------------

    def tsCursesInstr(self, x, y, n=None, pixels=True):
        '''
        Returns a string of characters, extracted from the window starting
        at the current cursor position, or at y, x if specified. Attributes
        are stripped, by curses window.instr(), from the characters. If n
        is specified, curses window.instr() returns a string at most n
        characters long (exclusive of the trailing NUL).
        '''
        window = self.ts_Handle
        if window is None:
            string = None
        else:
            if pixels:
                (xCol, yRow) = self.tsGetCharacterValues(x, y)
            else:
                (xCol, yRow) = (x, y)

            if n is None:
                string = window.instr(int(yRow), int(xCol))
            else:
                string = window.instr(int(yRow), int(xCol), int(n))

        return (string)

    #----------------------------------------------------------------------

    def tsCursesMoveCursor(self, window, new_x, new_y, pixels=True):
        '''
        Move cursor to (new_y, new_x).
        '''
        if pixels:

            x = new_x // wx.pixelWidthPerCharacter
            y = new_y // wx.pixelHeightPerCharacter

        else:

            x = new_x
            y = new_y

        window.ts_Handle.move(y, x)

    #-----------------------------------------------------------------------

    def tsCursesNewWindow(self, rect, pixels=True):
        '''
        Create native curses GUI window.
        '''
        if pixels:
            (begin_x, begin_y) = self.tsGetCharacterValues(
                max(rect.x, 0),
                max(rect.y, 0))

            (ncols, nrows) = self.tsGetCharacterValues(
                max(rect.width, 0),
                max(rect.height, 0))

        else:
            (begin_x, begin_y) = (
                max(rect.x, 0),
                max(rect.y, 0))

            (ncols, nrows) = (
                max(rect.width, 0),
                max(rect.height, 0))

        newwinRect = wxRect(begin_x, begin_y, ncols, nrows)

        (begin_y_stdscr, begin_x_stdscr) = self.stdscr.Stdscr.getbegyx()
        (max_y_stdscr, max_x_stdscr) = self.stdscr.Stdscr.getmaxyx()

        stdscrRect = wxRect(
            begin_x_stdscr, begin_y_stdscr, max_x_stdscr, max_y_stdscr)


        newwinPixelsRect = wxRect(begin_x * wx.pixelWidthPerCharacter,
                                  begin_y * wx.pixelHeightPerCharacter,
                                  ncols * wx.pixelWidthPerCharacter,
                                  nrows * wx.pixelHeightPerCharacter)
        stdscrPixelsRect = wxRect(
            begin_x_stdscr * wx.pixelWidthPerCharacter,
            begin_y_stdscr * wx.pixelHeightPerCharacter,
            max_x_stdscr * wx.pixelWidthPerCharacter,
            max_y_stdscr * wx.pixelHeightPerCharacter)

        if stdscrPixelsRect.InsideRect(newwinPixelsRect):

            try:
                self.ts_Handle = curses.newwin(int(nrows),
                                               int(ncols),
                                               int(begin_y),
                                               int(begin_x))
                theHandle = self.ts_Handle

                self.logger.debug(
                    '              curses handle: %s' % theHandle)

                self.tsRegisterClassWindow()

            except Exception, cursesError:
                self.ts_Handle = None
                theHandle = self.ts_Handle

                self.logger.debug(
                    '              curses handle: %s' % theHandle)
                msg = 'Window tsCursesNewWindow Error: %s' % str(cursesError)
                self.logger.error(msg)
                # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        elif newwinPixelsRect.Left < stdscrPixelsRect.Left:
            msg = 'Left Column of "%s" %s is too far left of "Screen" %s' % \
                (self.Name, newwinPixelsRect, stdscrPixelsRect)
            self.logger.error('window.tsCursesNewWindow: %s' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        elif newwinPixelsRect.Right > stdscrPixelsRect.Right:
            msg = 'Right Column of "%s" %s is too far right of "Screen" %s' % \
                (self.Name, newwinPixelsRect, stdscrPixelsRect)
            self.logger.error('window.tsCursesNewWindow: %s' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        elif newwinPixelsRect.Top < stdscrPixelsRect.Top:
            msg = 'Top Row of "%s" %s is above top of "Screen" %s' % \
                (self.Name, newwinPixelsRect, stdscrPixelsRect)
            self.logger.error('window.tsCursesNewWindow: %s' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        elif newwinPixelsRect.Bottom > stdscrPixelsRect.Bottom:
            msg = 'Bottom Row of "%s" %s is below bottom of "Screen" %s' % \
                (self.Name, newwinPixelsRect, stdscrPixelsRect)
            self.logger.error('window.tsCursesNewWindow: %s' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:
            msg = '\n  All Borders of "%s" %s are outside of %s' % \
                (self.Name, newwinRect, stdscrRect)
            self.logger.error('window.tsCursesNewWindow: %s' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        (begin_y_parent, begin_x_parent) = theHandle.getparyx()

        (begin_y_actual, begin_x_actual) = theHandle.getbegyx()
        (max_y_actual, max_x_actual) = theHandle.getmaxyx()

        (begin_y_cursor, begin_x_cursor) = theHandle.getyx()

        self.logger.debug(
            '   tsCursesNewWindow parent: %s' % wxPoint(
                begin_x_parent, begin_y_parent))

        self.logger.debug(
            '   tsCursesNewWindow actual: %s' % wxRect(
                begin_x_actual, begin_y_actual, max_x_actual, max_y_actual))

        self.logger.debug(
            '   tsCursesNewWindow cursor: %s' % wxPoint(
                begin_x_cursor, begin_y_cursor))

        if True:
            self.tsCursesNewWindowGenealogy()

        return (theHandle)

    #-----------------------------------------------------------------------

    def tsCursesNewWindowGenealogy(self):
        '''
        Record genealogy information about the creator of a new curses window.
        '''

        handleSelf = self

        handleDict = {}

        try:
            handleDict['ClassName'] = handleSelf.ts_ClassName
        except AttributeError, e:
            handleDict['ClassName'] = 'N/A because %s' % e

        try:
            handleDict[
                'theFirstCallerClassName'] = \
                handleSelf.theFirstCallerClassName
        except AttributeError, e:
            handleDict['theFirstCallerClassName'] = 'N/A because %s' % e

        try:
            handleDict['Name'] = handleSelf.ts_Name
        except AttributeError, e:
            handleDict['Name'] = 'N/A because %s' % e

        try:
            handleDict['Label'] = handleSelf.ts_Label
        except AttributeError, e:
            handleDict['Label'] = 'N/A because %s' % e

        try:
            handleDict['Title'] = handleSelf.ts_Title
        except AttributeError, e:
            handleDict['Title'] = 'N/A because %s' % e

        try:
            handleDict['windowIndex'] = handleSelf.ts_WindowIndex
        except AttributeError, e:
            handleDict['windowIndex'] = 'N/A because %s' % e

        try:
            handleDict['AssignedId'] = handleSelf.ts_AssignedId
        except AttributeError, e:
            handleDict['AssignedId'] = 'N/A because %s' % e

        try:
            handleDict['Handle'] = handleSelf.ts_Handle
        except AttributeError, e:
            handleDict['Handle'] = 'N/A because %s' % e

        try:
            handleDict['Parent'] = handleSelf.ts_Parent
            if (handleSelf.ts_Parent is None) and \
               (handleSelf.ts_ClassName in wx.TopLevelClasses):
                handleDict['Parent'] = '%s (stdscr)' % handleSelf.ts_Parent
        except AttributeError, e:
            handleDict['Parent'] = 'N/A because %s' % e

        try:
            handleDict['Parent windowIndex'] = \
                handleSelf.ts_Parent.ts_WindowIndex
        except AttributeError, e:
            handleDict['Parent windowIndex'] = 'N/A because %s' % e

        try:
            handleDict['Parent Name'] = handleSelf.ts_Parent.ts_Name
        except AttributeError, e:
            handleDict['Parent Name'] = 'N/A because %s' % e

        try:
            handleDict['Parent Label'] = handleSelf.ts_Parent.ts_Label
        except AttributeError, e:
            handleDict['Parent Label'] = 'N/A because %s' % e

        try:
            handleDict['Parent Title'] = handleSelf.ts_Parent.ts_Title
        except AttributeError, e:
            handleDict['Parent Title'] = 'N/A because %s' % e

        try:
            handleDict['Parent AssignedId'] = \
                handleSelf.ts_Parent.ts_AssignedId
        except AttributeError, e:
            handleDict['Parent AssignedId'] = 'N/A because %s' % e

        try:
            handleDict['Parent Handle'] = handleSelf.ts_Parent.ts_Handle
        except AttributeError, e:
            handleDict['Parent Handle'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent'] = handleSelf.ts_Parent.ts_Parent
            if (handleSelf.ts_Parent.ts_Parent is None) and \
               (handleSelf.ts_Parent.ts_ClassName in wx.TopLevelClasses):
                handleDict['GrandParent'] = '%s (stdscr)' % \
                    handleSelf.ts_Parent.ts_Parent
        except AttributeError, e:
            handleDict['GrandParent'] = 'N/A because %s' % e


        try:
            handleDict['GrandParent windowIndex'] = \
                handleSelf.ts_Parent.ts_Parent.ts_WindowIndex
        except AttributeError, e:
            handleDict['GrandParent windowIndex'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent Name'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Name
        except AttributeError, e:
            handleDict['GrandParent Name'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent Label'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Label
        except AttributeError, e:
            handleDict['GrandParent Label'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent Title'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Title
        except AttributeError, e:
            handleDict['GrandParent Title'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent AssignedId'] = \
                handleSelf.ts_Parent.ts_Parent.ts_AssignedId
        except AttributeError, e:
            handleDict['GrandParent AssignedId'] = 'N/A because %s' % e

        try:
            handleDict['GrandParent Handle'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Handle
        except AttributeError, e:
            handleDict['GrandParent Handle'] = 'N/A because %s' % e

        self.logger.debug(
            '   tsCursesNewWindowGenealogy handleDict=%s' % \
            str(handleDict).replace(
                '{', '{\n\t').replace(
                    '}', '}\n').replace(
                        ', ', ',\n\t'))

    #----------------------------------------------------------------------

    def tsCursesNoEcho(self):
        '''
        Leave echo mode. Echoing of input characters is turned off.
        '''
        curses.noecho()

    #-----------------------------------------------------------------------

    def tsCursesPanelUpdatePanels(self):
        '''
        Updates the virtual screen after changes in the panel stack. This
        does not call curses.doupdate(), so you will have to do this
        yourself.
        '''
        curses.panel.update_panels()

    #-----------------------------------------------------------------------

    def tsCursesPflush(self, updateDisplay=False):
        '''
        Update the virtual screen after changes in the panel stack and
        then optionally update the display.
        '''
        try:
            self.tsCursesPanelUpdatePanels()
            if updateDisplay:
                curses.doupdate()
        except Exception, e:
            msg = 'tsCursesPflush: updateDisplay=%s; %s' % (
                str(updateDisplay), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def tsCursesScroll(self, lines=1):
        '''
        Scroll the screen or scrolling region upward by lines lines.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            try:
                window.scroll(int(lines))
                status = True

            except Exception, cursesError:
                msg = 'Window tsCursesScroll Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesScrollOk(self, flag):
        '''
        Controls what happens when the cursor of a window is moved off the
        edge of the window or scrolling region, either as a result of a
        newline action on the bottom line, or typing the last character of
        the last line. If flag is false, the cursor is left on the bottom
        line. If flag is true, the window is scrolled up one line. Note that
        in order to get the physical scrolling effect on the terminal, it
        is also necessary to call idlok().
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            try:
                window.scrollok(int(flag))
                status = True

            except Exception, cursesError:
                msg = 'Window tsCursesScrollOk Error: %s' % str(cursesError)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (status)

    #-----------------------------------------------------------------------

    def tsCursesTermname(self):
        '''
        Return name of display terminal.
        '''
        try:
            termname = str(curses.termname())
        except AttributeError:
            termname = None

        return (termname)

    #-----------------------------------------------------------------------

    def tsCursesTextpad(self, win):
        '''
        The curses.textpad module provides a Textbox class that handles
        elementary text editing in a curses window, supporting a set of
        keybindings resembling those of Emacs (thus, also of Netscape
        Navigator, BBedit 6.x, FrameMaker, and many other programs).
        The module also provides a rectangle-drawing function useful for
        framing text boxes or for other purposes.

        Return a textbox widget object. The win argument should be a
        curses WindowObject in which the textbox is to be contained.
        The edit cursor of the textbox is initially located at the upper
        left hand corner of the containing window, with coordinates (0, 0).
        The instance stripspaces flag is initially on.
        '''
##        from: http://stackoverflow.com/questions/4581441/
##              edit-text-using-python-and-curses-textbox-widget

##        import curses
##        import curses.textpad

##        stdscr = curses.initscr()
##        # don't echo key strokes on the screen
##        curses.noecho()
##        # read keystrokes instantly, without waiting for enter to ne pressed
##        curses.cbreak()
##        # enable keypad mode
##        stdscr.keypad(1)
##        stdscr.clear()
##        stdscr.refresh()
##        win = curses.newwin(5, 60, 5, 10)
##        tb = curses.textpad.Textbox(win)
##        text = tb.edit()
##        curses.beep()
##        win.addstr(4,1,text.encode('utf_8'))

        self.logger.wxASSERT_MSG(
            (not (win is None)),
            msg='tsWxWindow.tsCursesTextpad: ' + \
            'win is None.')

        return (curses.textpad.Textbox(win))

    #-----------------------------------------------------------------------

    def tsCursesTextpadDoCommand(self, textBox, ch):
        '''
        Process a single command keystroke. Here are the supported special
        keystrokes:

        Keystroke Action
        Control-A Go to left edge of window.
        Control-B Cursor left, wrapping to previous line if appropriate.
        Control-D Delete character under cursor.
        Control-E Go to right edge (stripspaces off) or end of line
                  (stripspaces on).
        Control-F Cursor right, wrapping to next line when appropriate.
        Control-G Terminate, returning the window contents.
        Control-H Delete character backward.
        Control-J Terminate if the window is 1 line, otherwise insert newline.
        Control-K If line is blank, delete it, otherwise clear to end of line.
        Control-L Refresh screen.
        Control-N Cursor down; move down one line.
        Control-O Insert a blank line at cursor location.
        Control-P Cursor up; move up one line.

        Move operations do nothing if the cursor is at an edge where the
        movement is not possible. The following synonyms are supported
        where possible:

        Constant      Keystroke
        KEY_LEFT      Control-B
        KEY_RIGHT     Control-F
        KEY_UP        Control-P
        KEY_DOWN      Control-N
        KEY_BACKSPACE Control-h

        All other keystrokes are treated as a command to insert the given
        character and move right (with line wrapping).
        '''
        textBox.do_command(ch)

    #-----------------------------------------------------------------------

    def tsCursesTextpadEdit(self, textBox, validator):
        '''
        This is the entry point you will normally use. It accepts editing
        keystrokes until one of the termination keystrokes is entered. If
        validator is supplied, it must be a function. It will be called
        for each keystroke entered with the keystroke as a parameter;
        command dispatch is done on the result. This method returns the
        window contents as a string; whether blanks in the window are
        included is affected by the stripspaces member.
        '''
        return (textBox.edit(validator))

    #-----------------------------------------------------------------------

    def tsCursesTextpadGather(self, textBox):
        '''
        This method returns the window contents as a string; whether blanks
        in the window are included is affected by the stripspaces member.
        '''
        return (textBox.gather())

    #-----------------------------------------------------------------------

    def tsCursesTextpadStripspaces(self):
        '''
        This data member is a flag which controls the interpretation of
        blanks in the window. When it is on, trailing blanks on each line
        are ignored; any cursor motion that would land the cursor on a
        trailing blank goes to the end of that line instead, and trailing
        blanks are stripped when the window contents are gathered.
        '''
        pass

    #-----------------------------------------------------------------------

    def tsCursesWindowNoutRefresh(self, win):
        '''
        Mark for refresh but wait. This function updates the data structure
        representing the desired state of the window, but does not force an
        update of the physical screen. To accomplish that, call doupdate().
        '''
        win.noutrefresh()

    #-----------------------------------------------------------------------

    def tsCursesWindowRedrawWin(self, win):
        '''
        Touches the entire window, causing it to be completely redrawn on
        the next refresh() call.
        '''
        win.redrawwin()
