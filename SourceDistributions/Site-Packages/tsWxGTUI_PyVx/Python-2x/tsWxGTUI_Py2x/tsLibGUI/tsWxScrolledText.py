#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:08:46 AM rsg>"
'''
tsWxScrolledText.py - Class to establish a text control that
allows an array of text strings to be scrolled horizontally
and/or vertically. It may be scrolled in increments of single
or multiple columns or rows.
'''
#################################################################
#
# File: tsWxScrolledText.py
#
# Purpose:
#
#    Class to establish a text control that allows an array of
#    text strings to be scrolled horizontally and/or vertically.
#    It may be scrolled in increments of single or multiple
#    columns or rows.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrolledText import ScrolledText
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
#    See Notes section in tsWxScrolled.py
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
#    2012/02/29 rsg Simplified interface to tsAppendText and to
#                   tsUpdateScrolledText.
#
#    2012/03/02 rsg Revised Notes. Removed extraneous variables
#                   and code that had previusly been commented-out.
#
#    2012/03/08 rsg Modified tsAppendText and tsUpdateText
#                   to support text style (e.g. wx.DISPLAY_REVERSE)
#                   and/or foreground/background color pair
#                   attribute markup.
#
#    2012/05/17 rsg Architectural and logic changes. The module
#                   tsWxScrolled is responsible for the high level
#                   layout of Scrolled Window features. It also
#                   provides interfaces to internal features of
#                   the tsWxScrolledText moduke.
#
#    2012/05/25 rsg Revised logic in __init__ and in
#                   tsAdjustScrollPosition to ensure that
#                   horizontal scrolling does not change previous
#                   vertical scrolling and that vertical scrolling
#                   does not change previous horizontal scrolling.
#
# ToDo:
#
#    2012/03/08 rsg Investigate technique that might enable
#                   markup to be applied to individual lines,
#                   words, columns.
#
#    2012/06/24 rsg Investigate unexpected coupling between
#                   horizontal and vertical ScrollBar "thumb"
#                   emulation. It appears that x_pos gets
#                   changed by click on vertical gauge and
#                   that y_pos gets changed by click on vertical
#                   gauge.
#
#################################################################

__title__     = 'tsWxScrolledText'
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

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

appendTextWrapEnable = True # False

#---------------------------------------------------------------------------

class ScrolledText(Control):
    '''
    Class to establish a text control that allows an array of text strings
    to be scrolled horizontally and/or vertically. It may be scrolled in
    increments of single or multiple columns or rows.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 value=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.ScrolledTextNameStr):
        '''
        Create a Control. Normally you should only call this from a subclass
        (_init__) as a plain old wx.Control is not very useful.
        '''
        theClass = 'ScrolledText'

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         validator=validator,
                         name=name)

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_value = value
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              value: %s' % value)
            self.logger.debug('                pos: %s' % self.Position)
            self.logger.debug('               size: %s' % self.Size)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('          validator: %s' % validator)
            self.logger.debug('               name: %s' % name)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:

            self.ts_GrandParent = None

        else:

            self.ts_GrandParent = parent.Parent

        if False:

            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()

            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()

        elif  (self.tsCursesHasColors):

            self.ts_BackgroundColour = self.ts_Parent.ts_BackgroundColour

            self.ts_ForegroundColour = self.ts_Parent.ts_ForegroundColour

        else:

            self.ts_BackgroundColour = None

            self.ts_ForegroundColour = None

        self.ts_Style = style

        self.ts_Name = name
        self.ts_Label = value
        self.ts_Text = value
        self.ts_Row = 0
        self.ts_Col = 0
        self.ts_LineNumber = 0

        myRect, myClientRect = self.tsScrolledTextLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        #-------------------------------------------------------------------

        # Begin Scrolled Class Instance Variable Initialization
        # The following definitions are required to resolve
        # pylint warnings about definitions outside of __init__.
        self.curLine = []
        self.drawing = False

        self.ts_AutoScrolling = False
        self.ts_MaxTextCols = 0
        self.ts_MaxTextRows = 0
        self.ts_Retained = False
        self.ts_ScaleX = float(1.0) # 0.0 in wxWidgets
        self.ts_ScaleY = float(1.0) # 0.0 in wxWidgets
        self.ts_ScrolledTextLines = []
        self.ts_ScrolledTextMarkup = []
        self.ts_TargetWindow = None
        self.ts_ViewStart = False
        self.ts_Window = self # TBD - Is this required and appropriate

        #-------------------------------------------------------------------

        self.ts_xScrollLines = 0
        self.ts_xScrollLinesPerPage = (
            myClientRect.width // wx.pixelWidthPerCharacter)
        self.ts_xScrollPixelsPerLine = wx.pixelWidthPerCharacter
        self.ts_xScrollPosition = 0

        parentStyle = self.Parent.ts_Style

        if (((parentStyle & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
            ((parentStyle & wx.HSCROLL) == wx.HSCROLL)):

            self.ts_ChildForHorizontalScrollBar = None
            self.ts_xScrollingEnabled = True

            self.Bind(EVT_HSCROLLWIN_BOTTOM, self.tsOnHScrollWinBottom)
            self.Bind(EVT_HSCROLLWIN_LINEDOWN, self.tsOnHScrollWinLineDown)
            self.Bind(EVT_HSCROLLWIN_LINEUP, self.tsOnHScrollWinLineUp)
            self.Bind(EVT_HSCROLLWIN_PAGEDOWN, self.tsOnHScrollWinPageDown)
            self.Bind(EVT_HSCROLLWIN_PAGEUP, self.tsOnHScrollWinPageUp)
            self.Bind(EVT_HSCROLLWIN_TOP, self.tsOnHScrollWinTop)

        else:

            self.ts_ChildForHorizontalScrollBar = None
            self.ts_xScrollingEnabled = False

        #-------------------------------------------------------------------

        self.ts_yScrollLines = 0
        self.ts_yScrollLinesPerPage = (
            myClientRect.height // wx.pixelHeightPerCharacter)
        self.ts_yScrollPixelsPerLine = wx.pixelHeightPerCharacter
        self.ts_yScrollPosition = 0

        if (((parentStyle & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
            ((parentStyle & wx.VSCROLL) == wx.VSCROLL)):

            self.ts_ChildForVerticalScrollBar = None
            self.ts_yScrollingEnabled = True

            self.Bind(EVT_VSCROLLWIN_BOTTOM, self.tsOnVScrollWinBottom)
            self.Bind(EVT_VSCROLLWIN_LINEDOWN, self.tsOnVScrollWinLineDown)
            self.Bind(EVT_VSCROLLWIN_LINEUP, self.tsOnVScrollWinLineUp)
            self.Bind(EVT_VSCROLLWIN_PAGEDOWN, self.tsOnVScrollWinPageDown)
            self.Bind(EVT_VSCROLLWIN_PAGEUP, self.tsOnVScrollWinPageUp)
            self.Bind(EVT_VSCROLLWIN_TOP, self.tsOnVScrollWinTop)

        else:

            self.ts_ChildForVerticalScrollBar = None
            self.ts_yScrollingEnabled = False
 
        # End Scrolled Class Instance Variable Initialization

        #-------------------------------------------------------------------

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)


        if True:
            self.tsShow()

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               value=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               name=wx.TextCtrlNameStr,
               pixels=True):
        '''
        Actually create the GUI TextCtrl for 2-phase creation.
        '''
        if DEBUG:
            # Resolve pylint warning "Unused argument 'value'"
            self.logger.debug('tsWxScrolledText.Create: value=%s' % value)
 
        myRect, myClientRect = self.tsScrolledTextLayout(
            parent, pos, size, style, name)

        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        myRect = self.tsGetRectangle(pos, size)

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        if not (self.ts_Handle is None):
            self.ts_ViewStart = True

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def GetValue(self):
        '''
        '''
        if self.ts_Text is None:
            value = ''
        else:
            value = self.ts_Text
        return (value)

    #-----------------------------------------------------------------------

    def Scroll(self, x_pos, y_pos):
        '''
        Scrolls a window so the view start is at the given point.

        Parameters

        x_pos - The x position to scroll to, in scroll units.

        y_pos - The y position to scroll to, in scroll units.

        Remarks

        The positions are in scroll units, not pixels, so to convert
        to pixels you will have to multiply by the number of pixels
        per scroll increment. If either parameter is -1, that position
        will be ignored (no change in that direction).

        Column 0, Row 0 Position (x_pos, y_pos) = (0, 0) is left-most
        column on top-most row.

        Column 1, Row 1 Position (x_pos, y_pos) = (1, 1) is one column
        to the right and one row down.
        '''
        if self.ts_xScrollingEnabled:

            # Horizontal Scroll Bar
            if x_pos > -1:
                self.ts_xScrollPosition = x_pos

        if self.ts_yScrollingEnabled:

            # Vertical Scroll Bar
            if y_pos > -1:
                self.ts_yScrollPosition = y_pos

        self.tsUpdateText()

    #-----------------------------------------------------------------------

    def SetDefaultStyle(self, style):
        '''
        '''
        self.ts_Style = style
        return (True)

    #-----------------------------------------------------------------------

    def SetValue(self, value):
        '''
        '''
        if self.ts_Text is None:
            self.ts_Text = ''
        else:
            self.ts_Text = value
        self.ts_Label = self.ts_Text

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    def tsAdjustScrollPosition(self, evt, orientation):
        '''
        Calculate and set the horizontal or vertical scrolled text position
        corresponding to the relative caret position on the ScrollBarGauge
        at the time the operator clicked the mouse button.
        '''
        ####################################################################
        # Decode the mouse position data associated with mouse click event.
        (mouseId, x, y, z, bstate) = evt.EventData

        ####################################################################
        # Update minimum and maximum number of text rows
        # available for display.
##        minTextCols = 0
        maxTextCols = self.ts_MaxTextCols
##        minTextRows = 0
        maxTextRows = self.ts_MaxTextRows
        maxPageCols = self.ts_xScrollLinesPerPage
        maxPageRows = self.ts_yScrollLinesPerPage

        maxPage = wxPoint(maxPageCols, maxPageRows)
        maxText = wxPoint(maxTextCols, maxTextRows)

        if DEBUG:
            fmt0 = 'tsWxScrolledText.tsAdjustScrollPosition=%s; ' % str(self)
            fmt1 = 'className=%s; maxPage=%s; maxText=%s' % (
                self.ts_ClassName, str(maxPage), str(maxText))
            msg = fmt0 + fmt1
            self.logger.debug(msg)
            print('NOTICE: %s\n' % msg)

        ####################################################################
        # Convert mouse position into text row or col position.
        if self.ts_yScrollingEnabled and (orientation == wx.SB_VERTICAL):

            ################################################################
            # Update default text col position and simulated features.
            x_pos = self.ts_xScrollPosition

            # Scroll Text within Vertical ScrollBar Gauge
            yOffset = y - (self.ts_ClientRect.y / wx.pixelHeightPerCharacter)

            ySlope = float(max(0, maxTextRows - maxPageRows)) / (
                float(self.ts_ClientRect.height / wx.pixelHeightPerCharacter))

            y_pos = int(ySlope * float(yOffset))

            if DEBUG:
                fmt0 = 'tsWxScrolledText.' + \
                       'tsAdjustScrollPosition=%s; ' % str(self)
                fmt1 = 'y=%d; ' % y
                fmt2 = 'yOffset=%d; ' % yOffset
                fmt3 = 'ySlope=%f; ' % ySlope
                fmt4 = 'y_pos=%d' % y_pos
                msg = fmt0 + fmt1 + fmt2 + fmt3 + fmt4
                self.logger.debug(msg)
                print('NOTICE: %s\n' % msg)

        if self.ts_xScrollingEnabled and (orientation == wx.SB_HORIZONTAL):

            ################################################################
            # Update default text row position and simulated features.
            y_pos = self.ts_yScrollPosition

            # Scroll Text within Horizontal ScrollBar Gauge
            xOffset = x - (self.ts_ClientRect.x / wx.pixelWidthPerCharacter)

            xSlope = float(max(0, maxTextCols - maxPageCols)) / (
                float(self.ts_ClientRect.width / wx.pixelWidthPerCharacter))

            x_pos = int(xSlope * float(xOffset))

            if DEBUG:
                fmt0 = 'tsWxScrolledText.' + \
                       'tsAdjustScrollPosition=%s; ' % str(self)
                fmt1 = 'x=%d; ' % x
                fmt2 = 'xOffset=%d; ' % xOffset
                fmt3 = 'xSlope=%f; ' % xSlope
                fmt4 = 'x_pos=%d' % x_pos
                msg = fmt0 + fmt1 + fmt2 + fmt3 + fmt4
                self.logger.debug(msg)
                print('NOTICE: %s\n' % msg)

        self.Scroll(x_pos, y_pos)

    #-----------------------------------------------------------------------

    def tsAppendText(self, text, markup=None):
        '''
        Appends the text argument to the end of the text in the control.
        The insertion point also moves to the end of the control.

        Parameters:

        text - String of ascii text characters. Accepted values include
               empty string, simple string, and compound string separated
               by embedded "\n".

        markup - curses text markup ored with color pair number
        '''
        if False:
            print('tsWxScrolledText.tsAppendText: text="%s"' % text)

        newLines = text.split('\n')
        for aLine in newLines:
            self.ts_MaxTextCols = max(self.ts_MaxTextCols,
                                      len(aLine))
            self.ts_ScrolledTextLines += [aLine]
            self.ts_ScrolledTextMarkup += [markup]
            self.ts_MaxTextRows += 1

        self.ts_xScrollLines = self.ts_MaxTextCols
        self.ts_yScrollLines = self.ts_MaxTextRows

        # Update any displayed text.
        self.tsUpdateText()

##        if True:
##            self.tsOnHScrollWinLineDown()
##            self.tsOnVScrollWinLineDown()
##            self.tsOnHScrollWinLineDown()
##            self.tsOnVScrollWinLineDown()
##            self.tsOnHScrollWinTop()
##            self.tsOnVScrollWinTop()

    #-----------------------------------------------------------------------

    def tsGetChildForHorizontalScrollBar(self):
        '''
        Return control link to Scrolled.ChildForHorizontalScrollBar.
        '''
        return (self.ts_ChildForHorizontalScrollBar)

    #-----------------------------------------------------------------------

    def tsGetChildForVerticalScrollBar(self):
        '''
        Return control link to Scrolled.ChildForVerticalScrollBar.
        '''
        return (self.ts_ChildForVerticalScrollBar)

    #-----------------------------------------------------------------------

    def tsHScrollUpdate(self):
        '''
        Update the horizontal scrollbar gauge to highlight the position and
        size of the displayed text relative to the undisplayed text.
        '''
        firstCol = self.ts_xScrollPosition
        maxCols = self.ts_xScrollLines
        lastCol = min(maxCols, firstCol + self.ts_xScrollLinesPerPage)

        self.ts_ChildForHorizontalScrollBar.tsUpdateHorizontalGauge(
            firstCol,
            lastCol,
            maxCols)

    #-----------------------------------------------------------------------

    def tsOnHScrollWin(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnHScrollWin'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinBottom(self, evt):
        '''
        Set scroll position to page containing right-most column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinBottom: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = max(
                0,
                (self.ts_MaxTextCols - self.ts_xScrollLinesPerPage))

            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineDown(self, evt):
        '''
        Set scroll position to next column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinLineDown: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = min(
                self.ts_xScrollPosition + 1,
                self.ts_MaxTextCols)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinLineUp: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = max(
                0,
                self.ts_xScrollPosition - 1)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinPageDown: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = min(
                (self.ts_xScrollPosition + self.ts_xScrollLinesPerPage),
                self.ts_MaxTextCols)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinPageUp: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = max(
                0,
                (self.ts_xScrollPosition - self.ts_xScrollLinesPerPage))
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnHScrollWinThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnHScrollWinThumbRelease'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinThumbTrack(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnHScrollWinThumbTrack'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinTop(self, evt):
        '''
        Set scroll position to left-most column.
        '''
        msg = 'tsWxScrolledText.tsOnHScrollWinTop: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_xScrollingEnabled:

            self.ts_xScrollPosition = 0
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWin(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnVScrollWin'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinBottom(self, evt):
        '''
        Set scroll position to page containing bottom-most row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinBottom: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = max(
                0,
                (self.ts_MaxTextRows - self.ts_yScrollLinesPerPage))

            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineDown(self, evt):
        '''
        Set scroll position to next row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinLineDown: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = min(
                self.ts_yScrollPosition + 1,
                self.ts_MaxTextRows)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinLineUp: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = max(
                0,
                self.ts_yScrollPosition - 1)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinPageDown: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        maxRows = self.ts_yScrollLines
        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = min(
                (self.ts_yScrollPosition + self.ts_yScrollLinesPerPage),
                maxRows)
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinPageUp: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = max(
                0,
                (self.ts_yScrollPosition - self.ts_yScrollLinesPerPage))
            self.tsUpdateText()

    #-----------------------------------------------------------------------

    def tsOnVScrollWinThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnVScrollWinThumbRelease'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinThumbTrack(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raised in tsWxScrolledText.' +\
              'tsOnVScrollWinThumbTrack'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinTop(self, evt):
        '''
        Set scroll position to top-most row.
        '''
        msg = 'tsWxScrolledText.tsOnVScrollWinTop: ' + \
              'self=%s' % str(self)

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        if True or self.ts_yScrollingEnabled:

            self.ts_yScrollPosition = 0
            self.tsUpdateText()

    #-----------------------------------------------------------------------

##    def tsOnHScrollBottom(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_BOTTOM
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollBottom.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnHScrollLineDown(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_LINEDOWN
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollLineDown.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnHScrollLineUp(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_LINEUP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollLineUp.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnHScrollPageDown(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_PAGEDOWN
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollPageDown.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnHScrollPageUp(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_PAGEUP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollPageUp.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnHScrollTop(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_HSCROLLWIN_TOP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnHScrollTop.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollBottom(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_BOTTOM
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollBottom.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollLineDown(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_LINEDOWN
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollLineDown.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollLineUp(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_LINEUP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollLineUp.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollPageDown(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_PAGEDOWN
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollPageDown.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollPageUp(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_PAGEUP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollPageUp.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

##    #-----------------------------------------------------------------------

##    def tsOnVScrollTop(self, evt):
##        '''
##        '''
##        triggeringEvent = EVT_VSCROLLWIN_TOP
##        triggeringObject = self
##        objectCriteria = 'tsWxScrollBar processing tsOnVScrollTop.'

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsScrolledTextLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        label = self.ts_Text

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(wx.pixelWidthPerCharacter,
                                      wx.pixelHeightPerCharacter)
            elif label.find('\n') == -1:
                # TBD - Remove adjustment for extra cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[ ]')) * wx.pixelWidthPerCharacter,
                    wx.pixelHeightPerCharacter)
            else:
                # TBD - Remove adjustment for extra cursor width
                theLines = label.split('\n')
                maxWidth = 0
                maxHeight = len(theLines)
                for aLine in theLines:
                    if len(aLine) > maxWidth:
                        maxWidth = len(aLine)
                theLabelSize = wxSize(
                    (maxWidth + len('[ ]')) * wx.pixelWidthPerCharacter,
                    maxHeight * wx.pixelHeightPerCharacter)

            self.logger.debug(
                '      theLabelSize (end): %s' % theLabelSize)

            if thePosition == theDefaultPosition:

                # theDefaultPosition
                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theLabelSize.width,
                                theLabelSize.height)

            else:

                # Not theDefaultPosition
                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theLabelSize.width,
                                theLabelSize.height)

        else:

            # Not theDefaultSize
            if thePosition == theDefaultPosition:

                # theDefaultPosition
                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theSize.width,
                                theSize.height)

            else:

                # Not theDefaultPosition
                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theSize.width,
                                theSize.height)

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + theBorder.height,
                              myRect.width - 2 * theBorder.width,
                              myRect.height - 2 * theBorder.height)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; label=%s; myRect=%s' % \
              (parent, pos, size, name, label, myRect)

        self.logger.debug('    tsTextCtrlLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsSetChildForHorizontalScrollBar(self, child=None):
        '''
        Set control link to Scrolled.ChildForHorizontalScrollBar.
        '''
        self.ts_ChildForHorizontalScrollBar = child

    #-----------------------------------------------------------------------

    def tsSetChildForVerticalScrollBar(self, child=None):
        '''
        Set control link to Scrolled.ChildForVerticalScrollBar.
        '''
        self.ts_ChildForVerticalScrollBar = child

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update TextCtrl specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:
                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            value=self.ts_Text,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the ScrolledText.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()
                self.tsCreateLabel()

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def tsUpdateText(self):
        '''
        Displays only selected columns and rows, blank fills short strings,
        truncates long strings and terminates truncated string with '~')
        '''
        theTextCtrl = self # self.ts_ChildForText
        theTextCtrlClientRect = theTextCtrl.ClientRect

        maxCols = theTextCtrlClientRect.width // wx.pixelWidthPerCharacter
        maxRows = theTextCtrlClientRect.height // wx.pixelHeightPerCharacter

        firstDisplayedCol = self.ts_xScrollPosition
        firstDisplayedRow = self.ts_yScrollPosition

        # lastDisplayedCol = firstDisplayedCol + maxCols
        lastDisplayedRow = firstDisplayedRow + maxRows

        for row in range(firstDisplayedRow, lastDisplayedRow):

            if row < len(self.ts_ScrolledTextLines):

                aLine = self.ts_ScrolledTextLines[row]
                aText = aLine[firstDisplayedCol:len(aLine)]

                markup = self.ts_ScrolledTextMarkup[row]

            else:

                aLine = ''
                aText = aLine

                markup = None

            if (len(aText) <= maxCols):
                fill = ' ' * (maxCols - len(aText))
                viewableText = aText + fill
            else:
                # viewableText = aText[0:maxCols - 1] + '~'
                viewableText = aText[0:maxCols]

            theCol = 0 + \
                     theTextCtrl.tsIsBorderThickness(self.ts_Style,
                                                     pixels=False).width

            theRow = 0 + row - firstDisplayedRow + \
                     theTextCtrl.tsIsBorderThickness(self.ts_Style,
                                                     pixels=False).height

            theTextCtrl.tsCursesAddStr(theCol,
                                       theRow,
                                       viewableText,
                                       attr=markup,
                                       pixels=False)

            if DEBUG:

                verificationText = theTextCtrl.tsCursesInstr(
                    theCol,
                    theRow,
                    n=len(viewableText),
                    pixels=False)

                if viewableText != verificationText:

                    self.logger.error(
                        'tsWxScrolledText.tsUpdateText: ' + \
                        'failed verification: ' + \
                        '\nwrote:"%s"; \n read:"%s"' % (
                            viewableText, verificationText))

        # Update any horizontal scrollbar gauge.
        if not (self.ts_ChildForHorizontalScrollBar is None):
##            print('tsWxScrolledText.tsUpdateText: calling tsHScrollUpdate')
            self.tsHScrollUpdate()

        # Update any vertical scrollbar gauge.
        if not (self.ts_ChildForVerticalScrollBar is None):
##            print('tsWxScrolledText.tsUpdateText: calling tsVScrollUpdate')
            self.tsVScrollUpdate()

    #-----------------------------------------------------------------------

    def tsVScrollUpdate(self):
        '''
        Update the vertical scrollbar gauge to highlight the position and
        size of the displayed text relative to the undisplayed text.
        '''
        firstRow = self.ts_yScrollPosition
        maxRows = self.ts_yScrollLines
        lastRow = min(maxRows, firstRow + self.ts_yScrollLinesPerPage)
 
        self.ts_ChildForVerticalScrollBar.tsUpdateVerticalGauge(
            firstRow,
            lastRow,
            maxRows)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
