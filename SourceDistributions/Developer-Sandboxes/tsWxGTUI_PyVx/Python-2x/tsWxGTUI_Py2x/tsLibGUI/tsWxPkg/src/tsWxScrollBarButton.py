#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:46:21 AM rsg>"
'''
tsWxScrollBarButton.py - Class to establish a button control for
horizontal or vertical ScrollBars. Depending on the type of mouse
click, the buttons associated with the left or right arrow
will initiate events to scroll the associated text one or more
columns, horizontal pages or to the left or right most column.
The buttons associated with the up or down arrow will initiate
events to scroll the associated text one or more rows, vertical
pages or to the top or bottom most rows.
'''
#################################################################
#
# File: tsWxScrollBarButton.py
#
# Purpose:
#
#    Class to establish a button control for horizontal or
#    vertical ScrollBars. Depending on the type of mouse
#    click, the buttons associated with the left or right arrow
#    will initiate events to scroll the associated text one or
#    more columns, horizontal pages or to the left or right most
#    column. The buttons associated with the up or down arrow
#    will initiate events to scroll the associated text one or
#    more rows, vertical pages or to the top or bottom most rows.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrollBarButton import ScrollBarButton
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
#    2012/02/04 rsg Added logic to tsWxScrollBarButtonLayout to
#                   inhibit operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/04 rsg Added logic to support tsWxScrollBarButton events.
#
#    2012/02/12 rsg Conditionalized-out DEBUG statements in
#                   tsScrollBarButtonFeatureLayout.
#
#    2012/02/16 rsg Modified tsOnLeftClick, tsOnLeftDClick and
#                   tsOnRightClick to invoke tsProcessSelectedEventTable.
#
#    2012/03/08 rsg Added support for sending EVT_HSCROLLWIN...
#                   and EVT_VSCROLLWIN... from tsWxScrollBar to
#                   tsWxScrolled. This facilitated descrimination
#                   of tsWxScrollBarButton events when the associated
#                   ScrolledText had both horizontal and vertical controls.
#
#    2012/05/16 rsg Resolved single event binding limit issue by supporting
#                   internal or external handlers for LeftClick LeftDClick
#                   and RightClick.
#
#    2012/05/17 rsg Removed extraneous logic.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event>.
#
# ToDo:
#
#    2012/02/08 rsg Resolve single event binding limit issue.
#
#################################################################

__title__     = 'tsWxScrollBarButton'
__version__   = '1.8.0'
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
from tsWxEvent import EVT_COMMAND_LEFT_DCLICK  # [Left Mouse]-Button DClick
from tsWxEvent import EVT_COMMAND_RIGHT_CLICK  # [Right Mouse]-Button Click

from tsWxEvent import EVT_HSCROLLWIN_BOTTOM
from tsWxEvent import EVT_HSCROLLWIN_LINEDOWN
from tsWxEvent import EVT_HSCROLLWIN_LINEUP
from tsWxEvent import EVT_HSCROLLWIN_PAGEDOWN
from tsWxEvent import EVT_HSCROLLWIN_PAGEUP
from tsWxEvent import EVT_HSCROLLWIN_TOP

from tsWxEvent import EVT_VSCROLLWIN_BOTTOM
from tsWxEvent import EVT_VSCROLLWIN_LINEDOWN
from tsWxEvent import EVT_VSCROLLWIN_LINEUP
from tsWxEvent import EVT_VSCROLLWIN_PAGEDOWN
from tsWxEvent import EVT_VSCROLLWIN_PAGEUP
from tsWxEvent import EVT_VSCROLLWIN_TOP

labelDataBase = wx.ThemeToUse['ScrollBar']

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class ScrollBarButton(Control):
    '''
    Class to establish a button control for horizontal or vertical
    ScrollBars. Depending on the type of mouse click, the buttons
    associated with the left or right arrow will initiate events to
    scroll the associated text one or more columns, horizontal pages
    or to the left or right most column. The buttons associated with
    the up or down arrow will initiate events to scroll the associated
    text one or more rows, vertical pages or to the top or bottom most
    rows.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.ScrollBarButtonNameStr,
                 useClientArea=True):
        '''
        Create and show a button. The preferred way to create standard buttons
        is to use a standard ID and an empty label. In this case wxWigets will
        automatically use a stock label that corresponds to the ID given.
        These labels may vary across platforms as the platform itself will
        provide the label if possible. In addition, the button will be
        decorated with stock icons under GTK+ 2.
        '''
        theClass = 'ScrollBarButton'

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
        self.caller_label = label
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
            self.logger.debug('              label: %s' % label)
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

        if False:
            # Leaves artifacts of different color than parent background.
            self.ts_BackgroundColour = wx.ThemeToUse[
                'ScrollBar']['ForegroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ScrollBar']['BackgroundColour'].lower()
        else:
            # Inter-button spaces have same color as parent background.
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_Label = label
        self.ts_ButtonText = self.tsStripAcceleratorTextLabel(label)

        self.ts_ArrowDownEnabled = False
        self.ts_ArrowLeftEnabled = False
        self.ts_ArrowRightEnabled = False
        self.ts_ArrowUpEnabled = False

        if self.GetLabel().find(wx.ThemeToUse['ScrollBar'][
            'ArrowUp']) > -1:

            self.ts_ArrowUpEnabled = True

        elif self.GetLabel().find(wx.ThemeToUse['ScrollBar'][
            'ArrowDown']) > -1:

            self.ts_ArrowDownEnabled = True

        elif self.GetLabel().find(wx.ThemeToUse['ScrollBar'][
            'ArrowLeft']) > -1:

            self.ts_ArrowLeftEnabled = True

        elif self.GetLabel().find(wx.ThemeToUse['ScrollBar'][
            'ArrowRight']) > -1:

            self.ts_ArrowRightEnabled = True

        else:

            msg = 'tsWxScrollBarButton.__init__: ' + \
                'Invalid Arrow=%s' % self.GetLabel()
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.ts_UseClientArea = useClientArea
        self.ts_Validator = validator

        (myRect, myClientRect) = self.tsScrollBarButtonLayout(
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
        except Exception, errorCode:
            msg = 'tsWxScrollBarButton.__init__: errorCode=%s' % str(errorCode)
            print('ERROR: %s\n' % msg)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            # Assume unit test usage hierarchy
            self.ts_Scrolled = None
            # Assume DEBUG mode for test_tsWxScrollBar
            self.ts_ScrolledText = self
        # End linkage setup for distributed mouse click handling
        ####################################################################

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        event = EVT_COMMAND_LEFT_DCLICK
        handler = self.tsOnLeftDClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        event = EVT_COMMAND_RIGHT_CLICK
        handler = self.tsOnRightClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=-1,
               label=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               validator=wx.DefaultValidator,
               name=wx.ScrollBarButtonNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        if label == wx.EmptyString:
            # Prevent pylint warning.
            pass

        (myRect, myClientRect) = self.tsScrollBarButtonLayout(
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

##    TBD - Should be staticmethod
##    @staticmethod
    def GetDefaultSize(self):
        '''
        Returns the default button size for this platform.
        '''
        thickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=False)

        if False:
            width = (len(self.ts_ButtonText) + 1) * wx.pixelWidthPerCharacter

            height = (1) * wx.pixelHeightPerCharacter
        else:
            width = (thickness.width + \
                     len(self.ts_ButtonText) + 2) * wx.pixelWidthPerCharacter

            height = (thickness.height + 2) * wx.pixelHeightPerCharacter

        return (wxSize(width, height))

    #-----------------------------------------------------------------------

    def tsGetScrolledText(self):
        '''
        Return the top level link to the ScrolledText associated with this
        ScrollBarButton.
        '''
        return (self.ts_ScrolledText)

    #-----------------------------------------------------------------------

    def SetDefault(self):
        '''
        This sets the button to be the default item for the panel or
        dialog box.
        '''
        self.ts_Default = True

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        msg = 'tsWxScrollBarButton.tsOnLeftClick=%s; label=%s' % (
            str(self), str(self.GetLabel()))

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        triggeringObject = self.ts_ScrolledText
        objectId = triggeringObject.ts_AssignedId
        
        if self.ts_ArrowUpEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinLineUp()

            objectCriteria = 'EVT_VSCROLLWIN_LINEUP for [^]-Button'
            triggeringEvent = EVT_VSCROLLWIN_LINEUP

        elif self.ts_ArrowDownEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinLineDown()

            objectCriteria = 'EVT_VSCROLLWIN_LINEDOWN for [v]-Button'
            triggeringEvent = EVT_VSCROLLWIN_LINEDOWN

        elif self.ts_ArrowLeftEnabled:

            # self.ts_ScrolledText.tsOnHScrollWinLineUp()

            objectCriteria = 'EVT_HSCROLLWIN_LINEUP for [<]-Button'
            triggeringEvent = EVT_HSCROLLWIN_LINEUP

        else:

            # self.ts_ScrolledText.tsOnHScrollWinLineDown()

            objectCriteria = 'EVT_HSCROLLWIN_LINEDOWN for [>]-Button'
            triggeringEvent = EVT_HSCROLLWIN_LINEDOWN

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnLeftDClick(self, evt):
        '''
        '''
        msg = 'tsWxScrollBarButton.tsOnLeftDClick=%s; label=%s' % (
            str(self), str(self.GetLabel()))

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        triggeringObject = self.ts_ScrolledText
        objectId = triggeringObject.ts_AssignedId

        if self.ts_ArrowUpEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinPageUp()

            objectCriteria = 'EVT_VSCROLLWIN_PAGEUP for [^]-Button'
            triggeringEvent = EVT_VSCROLLWIN_PAGEUP

        elif self.ts_ArrowDownEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinPageDown()

            objectCriteria = 'EVT_VSCROLLWIN_PAGEDOWN for [v]-Button'
            triggeringEvent = EVT_VSCROLLWIN_PAGEDOWN

        elif self.ts_ArrowLeftEnabled:

            # self.ts_ScrolledText.tsOnHScrollWinPageUp()

            objectCriteria = 'EVT_HSCROLLWIN_PAGEUP for [<]-Button'
            triggeringEvent = EVT_HSCROLLWIN_PAGEUP

        else:

            # self.ts_ScrolledText.tsOnHScrollWinPageDown()

            objectCriteria = 'EVT_HSCROLLWIN_PAGEDOWN for [>]-Button'
            triggeringEvent = EVT_HSCROLLWIN_PAGEDOWN

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnRightClick(self, evt):
        '''
        '''
        msg = 'tsWxScrollBarButton.tsOnRightClick=%s; label=%s' % (
            str(self), str(self.GetLabel()))

        if DEBUG:
            print('DEBUG: %s\n' % msg)

        self.logger.debug(msg)

        triggeringObject = self.ts_ScrolledText
        objectId = triggeringObject.ts_AssignedId

        if self.ts_ArrowUpEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinTop()

            objectCriteria = 'EVT_VSCROLLWIN_TOP for [^]-Button'
            triggeringEvent = EVT_VSCROLLWIN_TOP

        elif self.ts_ArrowDownEnabled:

            # self.ts_ScrolledText.tsOnVScrollWinBottom()

            objectCriteria = 'EVT_VSCROLLWIN_BOTTOM for [v]-Button'
            triggeringEvent = EVT_VSCROLLWIN_BOTTOM

        elif self.ts_ArrowLeftEnabled:

            # self.ts_ScrolledText.tsOnHScrollWinTop()

            objectCriteria = 'EVT_HSCROLLWIN_TOP for [<]-Button'
            triggeringEvent = EVT_HSCROLLWIN_TOP

        else:

            # self.ts_ScrolledText.tsOnHScrollWinBottom()

            objectCriteria = 'EVT_HSCROLLWIN_BOTTOM for [>]-Button'
            triggeringEvent = EVT_HSCROLLWIN_BOTTOM

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinBottom(self, evt):
        '''
        Set scroll position to page containing right-most column.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollWinBottom: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinBottom(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinBottom: ' + \
##            'EVT_HSCROLLWIN_BOTTOM ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_HSCROLLWIN_BOTTOM

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineDown(self, evt):
        '''
        Set scroll position to next column.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollLineDown: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinLineDown(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinLineDown: ' + \
##            'EVT_HSCROLLWIN_LINEDOWN ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_HSCROLLWIN_LINEDOWN

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous column.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollWinLineUp: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinLineUp(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinLineUp: ' + \
##            'EVT_HSCROLLWIN_LINEUP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowUp']

##        triggeringEvent = EVT_HSCROLLWIN_LINEUP

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page column.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollWinPageDown: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinPageDown(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinPageDown: ' + \
##            'EVT_HSCROLLWIN_PAGEDOWN ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_HSCROLLWIN_PAGEDOWN

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page column.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollWinPageUp: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinPageUp(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinPageUp: ' + \
##            'EVT_HSCROLLWIN_PAGEUP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowUp']

##        triggeringEvent = EVT_HSCROLLWIN_PAGEUP

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
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnHScrollWinTop: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnHScrollWinTop(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnHScrollWinTop: ' + \
##            'EVT_HSCROLLWIN_TOP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowUp']

##        triggeringEvent = EVT_HSCROLLWIN_TOP

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
        if ((self.ts_ScrolledText == self) or
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinBottom: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinBottom(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinBottom: ' + \
##            'EVT_VSCROLLWIN_BOTTOM ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_VSCROLLWIN_BOTTOM

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineDown(self, evt):
        '''
        Set scroll position to next row.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinLineDown: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinLineDown(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinLineDown: ' + \
##            'EVT_VSCROLLWIN_LINEDOWN ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_VSCROLLWIN_LINEDOWN

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous row.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinLineUp: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinLineUp(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinLineUp: ' + \
##            'EVT_VSCROLLWIN_LINEUP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_VSCROLLWIN_LINEUP

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page row.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinPageDown: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinPageDown(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinPageDown: ' + \
##            'EVT_VSCROLLWIN_PAGEDOWN ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowDown']

##        triggeringEvent = EVT_VSCROLLWIN_PAGEDOWN

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page row.
        '''
        if ((self.ts_ScrolledText == self) or \
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinPageUp: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinPageUp(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinPageUp: ' + \
##            'EVT_VSCROLLWIN_PAGEUP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowUp']

##        triggeringEvent = EVT_VSCROLLWIN_PAGEUP

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
        if ((self.ts_ScrolledText == self) or
            (self.ts_ScrolledText is None)):

            msg = 'tsWxScrollBarButton.tsOnVScrollWinTop: ' + \
                  'self.ts_ScrolledText=%s' % self.ts_ScrolledText

            if DEBUG:
                print('DEBUG: %s\n' % msg)

            self.logger.error(msg)

        else:

            self.ts_ScrolledText.tsOnVScrollWinTop(evt)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'tsWxScrollBarButton.tsOnVScrollWinTop: ' + \
##            'EVT_VSCROLLWIN_TOP ' + \
##            'for [%s]-Button' % wx.ThemeToUse[
##                'ScrollBar']['ArrowUp']

##        triggeringEvent = EVT_VSCROLLWIN_TOP

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsScrollBarButtonLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)

        if style is None:
            # Prevent pylint warning.
            pass

        if DEBUG:
            fmt1 = 'tsScrollBarButtonLayout: '
            fmt2 = 'parent=%s; ' % str(parent)
            fmt3 = 'pos=%s; ' % str(pos)
            fmt4 = 'size=%s; ' % str(size)
            fmt5 = 'style=0x%X' % style
            msg =  fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            self.logger.debug(msg)

        if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

            arrowWidth = 3 * wx.pixelWidthPerCharacter
            arrowHeight = 3 * wx.pixelHeightPerCharacter
            # arrowStyle = wx.BORDER_SIMPLE

        else:

            arrowWidth = 1 * wx.pixelWidthPerCharacter
            arrowHeight = 1 * wx.pixelHeightPerCharacter
            # arrowStyle = wx.BORDER_NONE

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)

        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        label = self.ts_ButtonText

        # Ignore UseClientArea because cursor wraps beyond bottom
        # when last character has been output.
        if self.ts_UseClientArea:
            offset = wxPoint(wx.pixelWidthPerCharacter,
                             wx.pixelHeightPerCharacter)
        else:
            offset = wxPoint(0, 0)

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if (label == wx.EmptyString) or \
               (len(label) == 1):
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(
                    arrowWidth * wx.pixelWidthPerCharacter,
                    arrowHeight * wx.pixelHeightPerCharacter)

            elif label.find('\n') == -1:
                # TBD - Remove adjustment for extra cursor width
                theLabelSize = wxSize(
                    (len(label) + arrowWidth - 1) * wx.pixelWidthPerCharacter,
                    arrowHeight * wx.pixelHeightPerCharacter)
            else:
                # TBD - Remove adjustment for extra cursor width
                theLines = label.split('\n')
                maxWidth = 0
                maxHeight = len(theLines) + arrowHeight - 1
                for aLine in theLines:
                    if len(aLine) > maxWidth:
                        maxWidth = len(aLine) + arrowWidth - 1
                theLabelSize = wxSize(
                    maxWidth * wx.pixelWidthPerCharacter,
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

                myRect = wxRect(offset.x + thePosition.x,
                                offset.y + thePosition.y,
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

                myRect = wxRect(offset.x + thePosition.x,
                                offset.y + thePosition.y,
                                theSize.width,
                                theSize.height)

        myClientRect = wxRect(myRect.x,
                              myRect.y,
                              myRect.width,
                              myRect.height)

        self.tsTrapIfTooSmall(name, myRect)
        fmt = 'parent=%s; pos=%s; size=%s; ' + \
            'name="%s"; label="%s"; myRect=%s'
        msg = fmt % (parent, str(pos), str(size), name, label, str(myRect))

        self.logger.debug('    tsScrollBarButtonLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsSetChildForText(self, control=None):
        '''
        Set the top level link to the ScrolledText associated with this
        ScrollBarButton.
        '''
        childForText = control

        try:

            if ((not (childForText is self)) and \
                (not (childForText is None))):

                fmt1 = 'tsWxScrollBarButton.tsSetChildForText: '

                try:

                    fmt2 = 'tsWxScrollBarButton=%d (%s); ' % (
                        self.ts_AssignedId, str(self))

                except Exception:

                    fmt2 = 'tsWxScrollBarButton=%s; ' % str(self)

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

        except Exception, errorCode:

            msg = 'tsWxScrollBarButton.tsSetChildForText: '

            self.logger.error('%s; errorCode=%s' % (msg, str(errorCode)))

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Button specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            label=self.ts_Label,
                            pos=self.ts_Rect.Position,
                            size=self.ts_Rect.Size,
                            style=self.ts_Style,
                            validator=self.ts_Validator,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s.tsShow; %s' % (__title__, e))

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
            self.tsCreateScrollBarButton()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
