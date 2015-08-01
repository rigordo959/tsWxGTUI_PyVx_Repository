#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:46:39 AM rsg>"
'''
tsWxScrollBarGauge.py - Class to create a horizontal or
vertical bar graph. Its highlighted and non-highlighted areas
display the position and size of text displayed in an associated
scrollable text window relative to the undisplayed text.
'''
#################################################################
#
# File: tsWxScrollBarGauge.py
#
# Purpose:
#
#    Class to create a horizontal or vertical bar graph. Its
#    highlighted and non-highlighted areas display the position
#    and size of text displayed in an associated scrollable text
#    window relative to the undisplayed text.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrollBarGauge import ScrollBarGauge as wxScrollBarGauge
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
#    Unlike other GUI's, nCurses only senses mouse position at time
#    of mouse button click. It cannot sense the mouse dragging
#    needed to provide a "thumb" by which an operator can reposition
#    ScrolledText. As a substitute, this implementation permits an
#    operator to click on the ScrollBarGauge and have the relative
#    position between the ScrollBarButtons (Up/Down Arrow) determine
#    the updated ScrolledText position (scaled between Left/Right
#    columns or Top/Bottom rows).
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
#    2012/05/13 rsg Added a class variable, self.ts_ChildForText,
#                   and a class method, tsSetChildForText.
#
#    2012/05/24 rsg Added logic to provide scrolling by clicking
#                   on ScrollBar Gauge.
#
#    2012/06/24 rsg Removed local tsAdjustScrollPosition because it
#                   now provided by tsWxScrolledText.
#
#    2012/05/25 rsg Revised logic in __init__ and in tsOnLeftClick
#                   to ensure that horizontal scrolling does not
#                   change previous vertical scrolling and that
#                   vertical scrolling does not change previous
#                   horizontal scrolling.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to tsOnLeftClick.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsWxScrollBarGauge'
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

import tsExceptions as tse
import tsLogger

import tsWxGlobals as wx

from tsWxControl import Control
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize

from tsWxEvent import EVT_COMMAND_LEFT_CLICK   # [Left Mouse]-Button Click
##from tsWxEvent import EVT_COMMAND_LEFT_DCLICK  # [Left Mouse]-Button DClick
##from tsWxEvent import EVT_COMMAND_RIGHT_CLICK  # [Right Mouse]-Button Click

##from tsWxEvent import EVT_HSCROLLWIN_THUMBRELEASE
##from tsWxEvent import EVT_VSCROLLWIN_THUMBRELEASE

from tsWxEvent import EVT_HSCROLLWIN_THUMBTRACK
from tsWxEvent import EVT_VSCROLLWIN_THUMBTRACK

themeDataBase = wx.ThemeToUse['ScrollBar']

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

# BarGraph Tokens
blankToken = ' '
standardToken = '#'

#---------------------------------------------------------------------------

class ScrollBarGauge(Control):
    '''
    Class to create a horizontal or vertical bar graph. Its highlighted
    and non-highlighted areas display the position and size of text
    displayed in an associated scrollable text window relative to the
    undisplayed text.

    The max buffer length represents the largest horizontal column or
    vertical row count.

    The gauge is empty only when there are no columns or rows displayed
    (i.e. when the max buffer length is zero).

    The gauge is filled only when all columns or all rows are displayed.

    The gauge is partially filled only when some columns or rows are
    displayed.

    The highlighted area for the gauge begins at the relative column or
    row of the displayed text. The highlighted area ends at the relative
    column or row of the displayed text. For example:

    0 % - The column or row begins or ends at the left-most horizontal
          or vertical position in the list of text strings.

    25% - The column or row begins at the first quarter horizontal or
          vertical position in the list of text strings.

    50% - The column or row begins or ends at the midpoint horizontal
          or vertical position in the list of text strings.

    75% - The column or row begins or ends at the third quarter
          horizontal or vertical position in the list of text
          strings.

    100% - The column or row begins or ends at the right-most
          horizontal or bottom-most vertical position in the list
          of text strings.

    The length of the displayed bar is in proportion to the percentage
    of columns or rows displayed relative to their associated maximums.

    # Sample Horizontal Gauge                         Scrolled Text
    #
    #      +----------+---------+---------+---------+ 0% Offset
    #   0% |                                        | Empty 0% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 0% Offset
    #   0% |##########                              | First 25% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 25% Offset
    #  25% |          ##########                    | Second 25% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 50% Offset
    #  50% |                    ##########          | Third 25% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 75% Offset
    #  75% |                              ##########| Fourth 25% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 0% Offset
    #   0% |####################                    | First 50% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 25% Offset
    #  25% |          ####################          | Middle 50% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 50% Offset
    #  50% |                    ####################| Last 50% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 0% Offset
    #   0% |##############################          | First 75% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 25% Offset
    #  25% |          ##############################| Last 75% max buffer
    #      +----------+---------+---------+---------+
    #
    #      +----------+---------+---------+---------+ 0% Offset
    # 100% |########################################| All 100% max buffer
    #      +----------+---------+---------+---------+

    The user may left click on the gauge to reposition the scrolled text
    offset anywhere between its 0% and 100% limits.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 range=100,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.SB_HORIZONTAL,
                 validator=wx.DefaultValidator,
                 name=wx.ScrollBarGaugeNameStr):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        theClass = 'ScrollBarGauge'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_range = range
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         validator=validator,
                         name=name)

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              range: %s' % range)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Default = False

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        if True:
            # Leaves artifacts of different color than parent background.
            self.ts_BackgroundColour = wx.ThemeToUse[
                'ScrollBar']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ScrollBar']['ForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        self.ts_Style = style

        if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
            ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):
            self.ts_Orientation = wx.SB_HORIZONTAL
        else:
            self.ts_Orientation = wx.SB_VERTICAL

        myRect, myClientRect = self.tsScrollBarGaugeLayout(
            parent, pos, size, style, name)

        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        ####################################################################
        # Begin linkage setup for distributed mouse click handling
        #     SetChildForText enables Scrolled and/or ScrollBar to
        #     establish linkage between ScrollBarButton and
        #     ScrolledText.
        try:

            # Assume normal usage hierarchy
            self.ts_ScrollBar    = self.ts_Parent
            self.ts_Scrolled     = self.ts_ScrollBar.ts_Parent
            # Assume tsSetChildForText not yet used to override target
            self.ts_ScrolledText = self.ts_Scrolled.ts_ChildForText

        except Exception as errorCode:

            msg = 'tsWxScrollBarGauge.__init__: errorCode=%s' % str(errorCode)
            print('ERROR: %s\n' % msg)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            # Assume unit test usage hierarchy
            self.ts_Scrolled = None
            # Assume DEBUG mode for test_tsWxScrollBar
            self.ts_ScrolledText = self
        # End linkage setup for distributed mouse click handling
        ####################################################################

        self.ts_BarGraph = []
        self.ts_Range = range

        self.ts_GaugeThumbLines = 0

        self.ts_ChildForText = None

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        # Postpone Automatic Bind of all ScrollBarGauge events until
        # parent has invoked tsSetChildForText.
        self.ts_TriggeringCriteria = None
        self.ts_TriggeringEvent = None

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               range=100,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.GA_HORIZONTAL,
               validator=wx.DefaultValidator,
               name=wx.ScrollBarGaugeNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        myRect, myClientRect = self.tsScrollBarGaugeLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignored under other platforms. Under Mac, it will change the size of
        the returned font. See wx.Window.SetWindowVariant for more about this.
        '''
        return (variant)

    #-----------------------------------------------------------------------

    def GetRange(self):
        '''
        Return the maximum number of characters when the gauge is at 100%.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetRange in tsWxScrollBarGauge'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (self.ts_Range)

    #-----------------------------------------------------------------------
 
    def IsVertical(self):
        '''
        '''
        return (not (self.ts_Style & wx.SB_HORIZONTAL))

    #-----------------------------------------------------------------------
 
    def SetRange(self, range):
        '''
        Set the maximum number characters when the gauge is at 100%.
        '''
        self.ts_Range = range

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    def tsBestSize(self):
        '''
        '''
        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=True)

        gaugeThickness = 1
        gaugeLength = 10
 
        if self.ts_Style & wx.SB_VERTICAL:
            # Vertical
            best = wxSize(
                (gaugeThickness * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (gaugeLength * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))
        else:
            # Horizontal
            best = wxSize(
                (gaugeLength * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (gaugeThickness * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))

        return (best)

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        if True or DEBUG:
            fmt1 = 'tsWxScrollBarGauge.tsOnLeftClick=%s; ' % str(self)
            fmt2 = 'evt=%s' % str(evt)
            msg = fmt1 + fmt2

            self.logger.debug(msg)
            print(msg)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        targetObject = self.ts_ScrolledText

##        results = self.tsProcessEventTables(
##            objectCriteria=self.ts_TriggeringCriteria,
##            objectId=objectId,
##            triggeringEvent=self.ts_TriggeringEvent,
##            triggeringObject=triggeringObject)

        if themeDataBase['ThumbEmulation']:

            self.ts_ScrolledText.tsAdjustScrollPosition(
                evt, self.ts_Orientation)

    #-----------------------------------------------------------------------

    def tsScrollBarGaugeLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of gauge based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)
 
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        label = self.ts_Name

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[]')) * wx.pixelWidthPerCharacter,
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

            if False and thePosition == theDefaultPosition:
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

            if False and thePosition == theDefaultPosition:
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

        myClientRect = wxRect(myRect.x,
                              myRect.y,
                              myRect.width,
                              myRect.height)

        if ((self.Parent.ts_Style & wx.SB_HORIZONTAL) or \
            (self.Parent.ts_Style & wx.HSCROLL)):

            self.ts_GaugeThumbLines = (
                self.ts_ClientRect.width // wx.pixelWidthPerCharacter)

        else:

            self.ts_GaugeThumbLines = (
                self.ts_ClientRect.height // wx.pixelHeightPerCharacter)

        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.tsTrapIfTooSmall(name, myRect)
        fmt = 'parent=%s; pos=%s; size=%s; ' + \
              'name="%s"; label="%s"; myRect=%s'
        msg = fmt % (parent, str(pos), str(size), name, label, str(myRect))

        self.logger.debug('    tsScrollBarGaugeLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsSetChildForText(self, control=None):
        '''
        Set the top level link to the ScrolledText associated with this
        ScrollBarGauge.
        '''
        childForText = control

        try:

            if ((not (childForText is self)) and \
                (not (childForText is None))):

                fmt1 = 'tsWxScrollBarGauge.tsSetChildForText: '

                try:

                    fmt2 = 'tsWxScrollBarGauge=%d (%s); ' % (
                        self.ts_AssignedId, str(self))

                except Exception:

                    fmt2 = 'tsWxScrollBarGauge=%s; ' % str(self)

                try:

                    fmt3 = 'tsWxScrollBar=%d (%s); ' % (
                        self.ts_ScrollBar.ts_AssignedId,
                        str(self.ts_ScrollBar))

                except Exception:

                    fmt3 = 'tsWxScrollBar=%s; ' % str(self.ts_ScrollBar)

                try:

                    fmt4 = 'tsWxScrolledText=%d (%s); ' % (
                        self.ts_ScrolledText.ts_AssignedId,
                        str(self.ts_ScrolledText))

                except Exception:

                    fmt4 = 'tsWxScrolledText=%s; ' % str(self.ts_ScrolledText)

                try:

                    fmt5 = 'childForText=%s (%s); ' % (
                        str(childForText), str(childForText))

                    self.ts_ScrolledText = childForText

                    msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                    self.logger.debug(msg)

                except Exception:

                    fmt5 = 'childForText=%s; ' % str(childForText)

                    msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                    self.logger.error(msg)

                self.ts_ScrolledText = childForText

        except Exception as errorCode:

            msg = 'tsWxScrollBarGauge.tsSetChildForText: '

            self.logger.error('%s; errorCode=%s' % (msg, str(errorCode)))

        # Automatically Bind all ScrollBarGauge events ASAP (now).
        # Will register event in the SystemEventTable.
        if ((self.Parent.ts_Style & wx.SB_HORIZONTAL) or \
            (self.Parent.ts_Style & wx.HSCROLL)):

            self.ts_TriggeringCriteria = 'EVT_VSCROLLWIN_THUMBTRACK ' + \
                                         'for [V-Thumb]-Gauge'

            self.ts_TriggeringEvent = EVT_VSCROLLWIN_THUMBTRACK

            handler = self.ts_ScrolledText.tsOnHScrollWinThumbTrack

        else:

            self.ts_TriggeringCriteria = 'EVT_HSCROLLWIN_THUMBTRACKP ' + \
                                         'for [H-Thumb]-Gauge'

            self.ts_TriggeringEvent = EVT_HSCROLLWIN_THUMBTRACK

            handler = self.ts_ScrolledText.tsOnVScrollWinThumbTrack

        source = self
        self.Bind(self.ts_TriggeringEvent,
                  handler,
                  source,
                  useSystemEventTable=True)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update ScrollBarGauge specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            range=0,
                            pos=self.ts_Rect.Position,
                            size=self.ts_Rect.Size,
                            style=self.ts_Style,
                            validator=self.ts_Validator,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Button.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            self.tsCreateBorder()

    #-----------------------------------------------------------------------

    def tsUpdateHorizontalGauge(self,
                                firstCol,
                                lastCol,
                                maxCols):
        '''
        Update the horizontal scrollbar gauge to highlight the position and
        size of the displayed text relative to the undisplayed text.
        '''
        self.tsUpdate()

        self.SetRange(maxCols)

##        if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##            ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

        firstCell = 0
        lastCell = self.ts_GaugeThumbLines

##        print('tsUpdateHorizontalGauge: ' + \
##              'firstCol=%d; lastCol=%d; maxCols=%d; lastCell=%d' % (
##            firstCol, lastCol, maxCols, lastCell))

        fill = []
        for pos in range(firstCell, lastCell):
            fill += ' '

        startingCell = int(0.5 + (
            (float(firstCol) / float(maxCols)) * float(lastCell - 1)))

        endingCell =  int(0.5 + (
            (float(lastCol) / float(maxCols)) * float(lastCell - 1)))

        for col in range(startingCell, endingCell, 1):
            fill[col] = '#'
##            print('***** col=%d; fill=%s' % (
##                col, fill[col]))

        self.ts_BarGraph = fill

        row = firstCell + 1
        for col in range(firstCell, lastCell):
            if fill[col] == '#':
                self.tsCursesAddCh(
                    col, row, fill[col], attr=wx.DISPLAY_REVERSE, pixels=False)
            else:
                self.tsCursesAddCh(
                    col, row, fill[col], attr=None, pixels=False)

    #-----------------------------------------------------------------------

    def tsUpdateVerticalGauge(self,
                              firstRow,
                              lastRow,
                              maxRows):
        '''
        Update the vertical scrollbar gauge to highlight the position and
        size of the displayed text relative to the undisplayed text.
        '''
        self.tsUpdate()

        self.SetRange(maxRows)

##        if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##            ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

        firstCell = 0
        lastCell = self.ts_GaugeThumbLines

##        print('tsUpdateVerticalGauge: ' + \
##              'firstRow=%d; lastRow=%d; maxRows=%d; lastCell=%d' % (
##            firstRow, lastRow, maxRows, lastCell))

        fill = []
        for pos in range(firstCell, lastCell):
            fill += ' '

        startingCell = int(0.5 + (
            (float(firstRow) / float(maxRows)) * float(lastCell - 1)))
        endingCell =  int(0.5 + (
            (float(lastRow) / float(maxRows)) * float(lastCell - 1)))

        for row in range(startingCell, endingCell, 1):
            fill[row] = '#'
##            print('***** row=%d; fill=%s' % (
##                row, fill[row]))

        self.ts_BarGraph = fill

        col = firstCell + 1
        for row in range(firstCell, lastCell):
            if fill[row] == '#':
                self.tsCursesAddCh(
                    col, row, fill[row], attr=wx.DISPLAY_REVERSE, pixels=False)
            else:
                self.tsCursesAddCh(
                    col, row, fill[row], attr=None, pixels=False)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
