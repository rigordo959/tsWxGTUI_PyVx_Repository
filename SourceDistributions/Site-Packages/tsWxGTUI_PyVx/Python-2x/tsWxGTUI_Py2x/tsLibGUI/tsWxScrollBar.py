#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:06:38 AM rsg>"
'''
tsWxScrollBar.py - Class to establish a ScrollBar which is a
control that represents a horizontal or vertical scrollbar. It
is distinct from the two scrollbars that some windows provide
automatically, but the two types of scrollbar share the way
events are received.
'''
#################################################################
#
# File: tsWxScrollBar.py
#
# Purpose:
#
#    Class to establish a ScrollBar which is a control that
#    represents a horizontal or vertical scrollbar. It is
#    distinct from the two scrollbars that some windows provide
#    automatically, but the two types of scrollbar share the way
#    events are received.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrollBar import ScrollBar as App
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
#    2011/12/26 rsg Added logic to tsScrollBarLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/12 rsg Conditionalized-out DEBUG statements in
#                   tsScrollBarFeatureLayout.
#
#    2012/02/16 rsg Modified tsOnScroll... handlers to invoke
#                   tsProcessSelectedEventTable.
#
#    2012/02/21 rsg Added support for sending EVT_HSCROLLWIN...
#                   and EVT_VSCROLLWIN... from tsWxScrollBar to
#                   tsWxScrolled. This facilitated descrimination
#                   of tsWxScrollBarButton events when the associated
#                   TextCtrl had both horizontal and vertical controls.
#
#    2012/02/27 rsg Re-designed tsScrollBarFeatureLayout to place
#                   tsWxScrollBarGauge below tsWxScrollBarButtons
#                   so that the gauge borders are always superceded
#                   by those of the buttons (previous design placed
#                   left or Up button below gauge and right or down
#                   button on top.
#
#    2012/05/13 rsg Modified tsScrollBarLayout to use a dryRun argument
#                   to inhibit the invocation of tsScrollBarFeatureLayout
#                   during initialization. Multiple invocations had
#                   the undesirable consequence of creating multiple
#                   versions of child features.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event>.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxScrollBar'
__version__   = '1.6.0'
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
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxScrollBarButton \
     import ScrollBarButton as wxScrollBarButton
from tsWxGTUI_Py2x.tsLibGUI.tsWxScrollBarGauge \
     import ScrollBarGauge as wxScrollBarGauge
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

UseScrollBarButton = True

#---------------------------------------------------------------------------

class ScrollBar(Control):
    '''
    A wxScrollBar is a control that represents a horizontal or vertical
    scrollbar. It is distinct from the two scrollbars that some windows
    provide automatically, but the two types of scrollbar share the way
    events are received.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.SB_HORIZONTAL,
                 validator=wx.DefaultValidator,
                 name=wx.ScrollBarNameStr):
        '''
        Construct a wx.ScrollBar object.
        '''
        theClass = 'ScrollBar'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
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

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
##        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        self.tsBeginClassRegistration(theClass, id)

        myRect, myClientRect = self.tsScrollBarLayout(
            parent, pos, size, style, name, dryRun=True)

        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
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

        if True:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'ScrollBar']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ScrollBar']['ForegroundColour'].lower()

        elif True:
            self.ts_BackgroundColour = wx.COLOR_CYAN
            self.ts_ForegroundColour = wx.COLOR_WHITE
        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()

        self.ts_Style = style

        self.ts_Name = name

        # Begin database from tsWxScrolled

        # Begin Scrolled Class Instance Variable Initialization

        # The lines contains the list of text available for scrolling.
##        self.ts_ScrolledLines = self.Parent.ts_ScrolledLines
##        self.ts_MaxTextCols = self.Parent.ts_MaxTextCols
##        self.ts_MaxTextRows = self.Parent.ts_MaxTextRows
        # End database from tsWxScrolled

        # The range is the total number of units associated with the
        # view represented by the scrollbar. For a table with 15 columns,
        # the range would be 15.
##        self.ts_SB_Range = None

        # The thumb size is the number of units that are currently visible.
        # For the table example, the window might be sized so that only 5
        # columns are currently visible, in which case the application
        # would set the thumb size to 5. When the thumb size becomes the
        # same as or greater than the range, the scrollbar will be
        # automatically hidden on most platforms.
##        self.ts_SB_ThumbSize = None

        # The page size is the number of units that the scrollbar should
        # scroll by, when "paging" through the data. This value is normally
        # the same as the thumb size length, because it is natural to
        # assume that the visible window size defines a page.
##        self.ts_SB_PageSize = None

        # The scrollbar position is the current thumb position. Most
        # applications will find it convenient to provide a function
        # called AdjustScrollbars() which can be called initially, from
        # an OnSize event handler, and whenever the application data
        # changes in size. It will adjust the view, object and page size
        # according to the size of the window and the size of the data.
##        self.ts_SB_Position = None
##        self.ts_SB_ThumbPosition = None

        self.ts_ChildForDownArrow = None
        self.ts_ChildForHorizontalGauge = None
        self.ts_ChildForLeftArrow = None
        self.ts_ChildForRightArrow = None
        self.ts_ChildForUpArrow = None
        self.ts_ChildForVerticalGauge = None

        self.ts_ChildForText = None

        # self.tsBindMouseEvents()

        # TBD - Remove this.
        if True:
            self.tsShow()

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.SB_HORIZONTAL,
               validator=wx.DefaultValidator,
               name=wx.ScrollBarNameStr,
               pixels=True):
        '''
        Do the 2nd phase and create the GUI control.
        '''
##        if parent is None:
##            myParent = self.stdscr
##        else:
##            myParent = parent

        myRect, myClientRect = self.tsScrollBarLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. (Static method)
        '''
        return (wx.WINDOW_VARIANT_NORMAL)

    #-----------------------------------------------------------------------

##    def GetPageSize(self):
##        '''
##        The page size is the number of units that the scrollbar should
##        scroll by, when "paging" through the data. This value is normally
##        the same as the thumb size length, plus the size of the scrollbar
##        arrrows, because it is natural to assume that the visible window
##        size defines a page.
##        '''
##        if self.ts_SB_PageSize is None:

##            if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##                ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##                value = self.ts_ClientRect.width // \
##                        wx.pixelWidthPerCharacter

##                self.ts_SB_PageSize = value

##            else:

##                # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##                #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##                value = self.ts_ClientRect.height // \
##                        wx.pixelHeightPerCharacter

##                self.ts_SB_PageSize = value

##        else:

##            value = self.ts_SB_PageSize

##        return (value)

    #-----------------------------------------------------------------------

##    def GetRange(self):
##        '''
##        The range is the total number of units associated with the
##        view represented by the scrollbar. For a table with 15 columns,
##        the range would be 15.
##        '''
####        {
####            return (int)(m_adjust->upper+0.5);
####        }
##        if self.ts_SB_Range is None:

##            if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##                ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##                value = self.ts_ClientRect.width // \
##                        wx.pixelWidthPerCharacter

##                self.ts_SB_Range = value

##            else:

##                # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##                #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##                value = self.ts_ClientRect.height // \
##                        wx.pixelHeightPerCharacter

##                self.ts_SB_Range = value

##        else:

##            value = self.ts_SB_Range

##        return (value)

    #-----------------------------------------------------------------------

##    def GetThumbLength(self):
##        '''
##        # The scrollbar position is the current thumb position. Most
##        # applications will find it convenient to provide a function
##        # called AdjustScrollbars() which can be called initially, from
##        # an OnSize event handler, and whenever the application data
##        # changes in size. It will adjust the view, object and page size
##        # according to the size of the window and the size of the data.
##        self.ts_SB_ThumbPosition = None
##        '''
####        {
####            return 0;
####        }
##        if self.ts_SB_ThumbLength is None:

##            if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##                ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##                value = self.ts_ClientRect.width // \
##                        wx.pixelWidthPerCharacter

##                self.ts_SB_ThumbLength = value

##            else:

##                # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##                #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##                value = self.ts_ClientRect.height // \
##                        wx.pixelHeightPerCharacter

####                self.ts_SB_ThumbLength = value

##        else:

##            value = self.ts_SB_ThumbLength

##        return (value)

    #-----------------------------------------------------------------------

##    def GetThumbPosition(self):
##        '''
##        The scrollbar position is the current thumb position. Most
##        applications will find it convenient to provide a function
##        called AdjustScrollbars() which can be called initially, from
##        an OnSize event handler, and whenever the application data
##        changes in size. It will adjust the view, object and page size
##        according to the size of the window and the size of the data.
##        '''
####        {
####            double val = m_adjust->value;
####            return (int)(val < 0 ? val - 0.5 : val + 0.5);
####        }
##        if self.ts_SB_ThumbPosition is None:

##            if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##                ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##                value = 0 * self.ts_ClientRect.width // \
##                        wx.pixelWidthPerCharacter

##                self.ts_SB_ThumbPosition = value

##            else:

##                # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##                #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##                value = 0 * self.ts_ClientRect.height // \
##                        wx.pixelHeightPerCharacter

##                self.ts_SB_ThumbPosition = value

##        else:

##            value = self.ts_SB_ThumbPosition

##        return (value)

    #-----------------------------------------------------------------------

##    def GetThumbSize(self):
##        '''

##        The thumb size is the number of units that are currently visible.
##        For the table example, the window might be sized so that only 5
##        columns are currently visible, in which case the application
##        would set the thumb size to 5. When the thumb size becomes the
##        same as or greater than the range, the scrollbar will be
##        automatically hidden on most platforms.
##        '''
####        {
####            return (int)(m_adjust->page_size+0.5);
####        }
##        if self.ts_SB_ThumbSize is None:

##            if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##                ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##                value = self.ts_ClientRect.width // \
##                        wx.pixelWidthPerCharacter

##                self.ts_SB_ThumbSize = value

##            else:

##                # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##                #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##                value = self.ts_ClientRect.height // \
##                        wx.pixelHeightPerCharacter

##                self.ts_SB_ThumbSize = value

##        else:

##            value = self.ts_SB_ThumbSize

##        return (value)

    #-----------------------------------------------------------------------

    def IsVertical(self):
        '''
        '''
        if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
            ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

            value =  False

        else:

            # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
            #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

            value =  True

        return (value)

    #-----------------------------------------------------------------------

##    def SetScrollbar(self, position, thumbSize, range, pageSize):
##        '''
##        Sets the scrollbar properties.

##        Parameters:

##        position        The position of the scrollbar in scroll units.

##        thumbSize       The size of the thumb, or visible portion of the
##                        scrollbar, in scroll units.

##        range           The maximum position of the scrollbar.

##        pageSize        The size of the page size in scroll units. This
##                        is the number of units the scrollbar will scroll
##                        when it is paged up or down. Often it is the same
##                        as the thumb size.

##        refresh         true to redraw the scrollbar, false otherwise.

##        Remarks:

##        Let us say you wish to display 50 lines of text, using the same
##        font. The window is sized so that you can only see 16 lines at
##        a time. You would use:

##                    scrollbar->SetScrollbar(0, 16, 50, 15);

##        The page size is 1 less than the thumb size so that the last
##        line of the previous page will be visible on the next page,
##        to help orient the user. Note that with the window at this
##        size, the thumb position can never go above 50 minus 16, or 34.
##        You can determine how many lines are currently visible by
##        dividing the current view size by the character height in
##        pixels. When defining your own scrollbar behaviour, you will
##        always need to recalculate the scrollbar settings when the
##        window size changes. You could therefore put your scrollbar
##        calculations and SetScrollbar() call into a function named
##        AdjustScrollbars, which can be called initially and also
##        from a wxSizeEvent event handler function.
##        '''
##        self.ts_SB_PageSize = pageSize
##        self.ts_SB_Position = position
##        self.ts_SB_Range = range
##        self.ts_SB_ThumbSize = thumbSize

    #-----------------------------------------------------------------------

##    def SetThumbPosition(self, viewStart):
##        '''
##        The scrollbar position is the current thumb position. Most
##        applications will find it convenient to provide a function
##        called AdjustScrollbars() which can be called initially, from
##        an OnSize event handler, and whenever the application data
##        changes in size. It will adjust the view, object and page size
##        according to the size of the window and the size of the data.
##        '''
##        self.ts_SB_ThumbPosition = viewStart

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

##    def tsBindMouseEvents(self):
##        '''
##        Automatically Bind the mouse event(s) ASAP (now).
##        Register event(s) in the SystemEventTable.
##        '''
##        if (((self.ts_Style & wx.SB_HORIZONTAL) == wx.SB_HORIZONTAL) or \
##            ((self.ts_Style & wx.HSCROLL) == wx.HSCROLL)):

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_LINEUP
##            handler = self.tsOnHScrollLineUp
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_LINEDOWN
##            handler = self.tsOnHScrollLineDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_PAGEUP
##            handler = self.tsOnHScrollPageDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_PAGEDOWN
##            handler = self.tsOnHScrollPageDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_TOP
##            handler = self.tsOnHScrollTop
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_HSCROLLWIN_BOTTOM
##            handler = self.tsOnHScrollBottom
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##        else:

##            # if (((self.ts_Style & wx.SB_VERTICAL) == wx.SB_VERTICAL) or \
##            #     ((self.ts_Style & wx.VSCROLL) == wx.VSCROLL)):

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_LINEUP
##            handler = self.tsOnVScrollLineUp
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_LINEDOWN
##            handler = self.tsOnVScrollLineDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_PAGEUP
##            handler = self.tsOnVScrollPageDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_PAGEDOWN
##            handler = self.tsOnVScrollPageDown
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_TOP
##            handler = self.tsOnVScrollTop
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##            #---------------------------------------------------------------

##            event = EVT_VSCROLLWIN_BOTTOM
##            handler = self.tsOnVScrollBottom
##            source = self
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

    #-----------------------------------------------------------------------

##    def tsGetChildForDualScrollBarAlignment(self):
##        '''
##        Return control link to Scrolled.ChildForDualScrollBarAlignment.
##        '''
##        return (self.ts_ChildForDualScrollBarAlignment)

    #-----------------------------------------------------------------------

##    def tsGetChildForHorizontalScrollBar(self):
##        '''
##        Return control link to Scrolled.ChildForHorizontalScrollBar.
##        '''
##        return (self.ts_ChildForHorizontalScrollBar)

    #-----------------------------------------------------------------------

##    def tsGetChildForText(self):
##        '''
##        Return control link to Scrolled.ChildForText.
##        '''
##        return (self.ts_ChildForText)

    #-----------------------------------------------------------------------

##    def tsGetChildForVerticalScrollBar(self):
##        '''
##        Return control link to Scrolled.ChildForVerticalScrollBar.
##        '''
##        return (self.ts_ChildForVerticalScrollBar)

    #-----------------------------------------------------------------------

##    def tsOnHScroll(self, evt):
##        '''
##        '''
##        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
##              'tsOnHScroll'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollBottom(self, evt):
        '''
        Set scroll position to page containing right-most column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollBottom'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = max(
##                0,
##                ((self.maxWidth // wx.pixelWidthPerCharacter) - \
##                 self.ts_xScrollLinesPerPage))

##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnHScrollLineDown(self, evt):
        '''
        Set scroll position to next column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollLineDown'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = min(
##                self.ts_xScrollPosition + 1,
##                self.maxWidth // wx.pixelWidthPerCharacter)
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnHScrollLineUp(self, evt):
        '''
        Set scroll position to previous column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollLineUp'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = max(
##                0,
##                self.ts_xScrollPosition - 1)
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnHScrollPageDown(self, evt):
        '''
        Set scroll position to next page column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollPageDown'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = min(
##                (self.ts_xScrollPosition + \
##                 (self.ts_xScrollLinesPerPage),
##                self.maxWidth // wx.pixelWidthPerCharacter))
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnHScrollPageUp(self, evt):
        '''
        Set scroll position to previous page column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollPageUp'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = max(
##                0,
##                (self.ts_xScrollPosition - \
##                 (self.ts_xScrollLinesPerPage)))
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnHScrollThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollThumbRelease'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollThumbTrack(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollThumbTrack'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHScrollTop(self, evt):
        '''
        Set scroll position to left-most column.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnHScrollTop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_xScrollingEnabled:

##            self.ts_xScrollPosition = 0
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

##    def tsOnVScroll(self, evt):
##        '''
##        '''
##        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
##              'tsOnVScroll'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollBottom(self, evt):
        '''
        Set scroll position to page containing bottom-most row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollBottom'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = max(
##                0,
##                ((self.maxHeight - self.ts_yScrollPixelsPerLine) // \
##                 wx.pixelHeightPerCharacter))

##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnVScrollLineDown(self, evt):
        '''
        Set scroll position to next row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollLineDown'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = min(
##                self.ts_yScrollPosition + 1,
##                self.maxHeight // wx.pixelHeightPerCharacter)
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnVScrollLineUp(self, evt):
        '''
        Set scroll position to previous row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollLineUp'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = max(
##                0,
##                self.ts_yScrollPosition - 1)
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnVScrollPageDown(self, evt):
        '''
        Set scroll position to next page row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollPageDown'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = min(
##                (self.ts_yScrollPosition + self.ts_yScrollLinesPerPage),
##                (self.maxHeight // wx.pixelHeightPerCharacter))
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnVScrollPageUp(self, evt):
        '''
        Set scroll position to previous page row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollPageUp'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = max(
##                0,
##                (self.ts_yScrollPosition - self.ts_yScrollLinesPerPage))
##            self.tsUpdateScrolledText()

    #-----------------------------------------------------------------------

    def tsOnVScrollThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollThumbRelease'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollThumbTrack(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollThumbTrack'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnVScrollTop(self, evt):
        '''
        Set scroll position to top-most row.
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrollBar.' +\
              'tsOnVScrollTop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if self.ts_yScrollingEnabled:

##            self.ts_yScrollPosition = 0
##            self.tsUpdateScrolledText()

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

    def tsScrollBarLayout(self,
                          parent,
                          pos=wx.DefaultPosition,
                          size=wx.DefaultSize,
                          style=wx.HSCROLL | wx.VSCROLL,
                          name=wx.ScrollBarNameStr,
                          dryRun=False,
                          pixels=True):
        '''
        Calculate position and size of Scroll Bar based upon arguments.
        '''
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        if thePosition == theDefaultPosition and \
           theSize == theDefaultSize:

            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            parent.ClientArea.width,
                            parent.ClientArea.height)


        elif thePosition == theDefaultPosition:

            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            theSize.width,
                            theSize.height)

        elif theSize == theDefaultSize:

            myRect = wxRect(
                thePosition.x,
                thePosition.y,
                parent.ClientArea.width - thePosition.x,
                parent.ClientArea.height - thePosition.y)

        else:

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

        self.ts_Rect = myRect

        if self.tsIsBorderStyle(style):

            self.ts_ClientRect = wxRect(
                (self.ts_Rect.x + theBorder.width),
                (self.ts_Rect.y + theBorder.height),
                (self.ts_Rect.width - (2 * theBorder.width)),
                (self.ts_Rect.height - (2 * theBorder.height)))

        else:

            self.ts_ClientRect = self.ts_Rect

        if not dryRun:

            self.tsScrollBarFeatureLayout(self.ts_ClientRect, style)

        return (self.ts_Rect, self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def tsScrollBarFeatureLayout(self, clientRect, style):
        '''
        Calculate position and size of Scroll Bar features based upon
        arguments.
        '''
        parent = self

        if False and DEBUG:
            fmt1 = 'tsScrollBarFeatureLayout: '
            fmt2 = 'parent=%s; ' % parent
            fmt3 = 'clientRect=%s; ' % str(clientRect)
            fmt4 = 'style=0x%X' % style
            msg = fmt1 + fmt2 + fmt3 + fmt4
            print('NOTICE: %s\n' % msg)

        if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

            arrowWidth = 3 * wx.pixelWidthPerCharacter
            arrowHeight = 3 * wx.pixelHeightPerCharacter
            arrowStyle = wx.BORDER_SIMPLE

        else:

            arrowWidth = 1 * wx.pixelWidthPerCharacter
            arrowHeight = 1 * wx.pixelHeightPerCharacter
            arrowStyle = wx.BORDER_NONE

        if wx.ThemeToUse['ScrollBar']['Overlap']:

            overlapHorizontal = 1 * wx.pixelWidthPerCharacter
            overlapVertical = 1 * wx.pixelHeightPerCharacter

        else:

            overlapHorizontal = 0
            overlapVertical = 0

        childForLeftArrow = None
        childForHorizontalGauge = None
        childForRightArrow = None

        childForUpArrow = None
        childForVerticalGauge = None
        childForDownArrow = None

        if ((style & wx.SB_HORIZONTAL) or \
            (style & wx.HSCROLL)):

            # Horizontal Scroll Bar
            ################################################################
            #            wxPython Style - Parent Client Rectangle          #
            # +----------------------------------------------------------+ #
            # | Client Rectangle - Top Left                              | #
            # |                                                          | #
            # |                                                          | #
            # |                                                          | #
            # |                                                          | #
            # |                                                          | #
            # |                                                          | #
            # |                                                          | #
            # | scrollbar horizontal     Client Rectangle - Bottom Right | #
            # +-+------------------------------------------------------+-+ #
            # |<|######################################################|>| #
            # +-+------------------------------------------------------+-+ #
            ################################################################

            childForHorizontalGauge = wxScrollBarGauge(
                parent,
                id=wx.ID_ANY,
                # label='childForBarGraph',
                pos=((clientRect.x + arrowWidth - overlapHorizontal),
                     clientRect.y),
                size=((clientRect.width - (
                    2 * arrowWidth) + (
                        3 * overlapHorizontal)),
                      arrowHeight),
                style=arrowStyle | wx.SB_HORIZONTAL,
                name=wx.PanelNameStr)
##            childForHorizontalGauge.ts_BackgroundColour = wx.ThemeToUse[
##                'ScrollBar']['ForegroundColour'].lower()
##            childForHorizontalGauge.ts_ForegroundColour = wx.ThemeToUse[
##                'ScrollBar']['BackgroundColour'].lower()

            if UseScrollBarButton:

                childForLeftArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowLeft'],
                    pos=(clientRect.x, clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

                childForRightArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowRight'],
                    pos=((clientRect.x + clientRect.width - (
                          arrowWidth)),
                         clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

            else:

                childForLeftArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowLeft'],
                    pos=(clientRect.x, clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

                childForRightArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowRight'],
                    pos=((clientRect.x + clientRect.width - (
                          arrowWidth)),
                         clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

        else:

            # Vertical Scroll Bar
            ################################################################
            #               wxPython Style - Parent Rectangle              #
            # +--------------------------------------------------------+-+ #
            # | Client Rectangle - Top Left         scrollbar vertical |^| #
            # |                                                        +-+ #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        +-+ #
            # | scrollbar horizontal   Client Rectangle - Bottom Right |v| #
            # +--------------------------------------------------------+-+ #
            ################################################################

            childForVerticalGauge = wxScrollBarGauge(
                parent,
                id=wx.ID_ANY,
                # label='childForBarGraph',
                pos=(clientRect.x, (
                    clientRect.y + arrowHeight - overlapVertical)),
                size=(clientRect.width,
                      (clientRect.height + (2 * overlapVertical) - (
                          2 * arrowHeight))),
                style=arrowStyle | wx.SB_VERTICAL,
                name=wx.PanelNameStr)
##            childForVerticalGauge.ts_BackgroundColour = wx.ThemeToUse[
##                'ScrollBar']['ForegroundColour'].lower()
##            childForVerticalGauge.ts_ForegroundColour = wx.ThemeToUse[
##                'ScrollBar']['BackgroundColour'].lower()

            if UseScrollBarButton:

                childForUpArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowUp'],
                    pos=(clientRect.x, clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

                childForDownArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowDown'],
                    pos=(clientRect.x,
                         (clientRect.y  + clientRect.height - arrowHeight)),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

            else:

                childForUpArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowUp'],
                    pos=(clientRect.x, clientRect.y),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

                childForDownArrow = wxScrollBarButton(
                    parent,
                    id=wx.ID_ANY,
                    label=wx.ThemeToUse['ScrollBar']['ArrowDown'],
                    pos=(clientRect.x,
                         (clientRect.y  + clientRect.height - arrowHeight)),
                    size=(arrowWidth, arrowHeight),
                    style=wx.BORDER_SIMPLE,
                    # validator=wx.DefaultValidator,
                    name=wx.ScrollBarButtonNameStr,
                    useClientArea=False)

        self.ts_ChildForDownArrow = childForDownArrow
        self.ts_ChildForHorizontalGauge = childForHorizontalGauge
        self.ts_ChildForLeftArrow = childForLeftArrow
        self.ts_ChildForRightArrow = childForRightArrow
        self.ts_ChildForUpArrow = childForUpArrow
        self.ts_ChildForVerticalGauge = childForVerticalGauge

        return (self.ts_Rect, self.ts_ClientRect)

    #-----------------------------------------------------------------------

##    def tsSetChildForDualScrollBarAlignment(self, child=None):
##        '''
##        Set control link to Scrolled.ChildForDualScrollBarAlignment.
##        '''
##        self.ts_ChildForDualScrollBarAlignment = child

    #-----------------------------------------------------------------------

##    def tsSetChildForHorizontalScrollBar(self, child=None):
##        '''
##        Set control link to Scrolled.ChildForHorizontalScrollBar.
##        '''
##        self.ts_ChildForHorizontalScrollBar = child

    #-----------------------------------------------------------------------

    def tsSetChildForText(self, child=None):
        '''
        Set control link to Scrolled.ChildForText.
        '''
        childForText = child

        self.ts_ChildForText = childForText

        if not (childForText is None):

            fmt1 = 'tsWxScrollBar.tsSetChildForText: '
            fmt2 = 'assignedId=%d; ' % self.ts_AssignedId
            fmt3 = 'childForText=%d; ' % childForText.ts_AssignedId

            if (self.ts_ChildForLeftArrow is None):

                fmt4 = 'LeftArrow=%s; ' % str(self.ts_ChildForLeftArrow)

            else:

                fmt4 = 'LeftArrow=%d; ' % self.ts_ChildForLeftArrow.ts_AssignedId

                self.ts_ChildForLeftArrow.tsSetChildForText(
                    self.ts_ChildForText)

            if (self.ts_ChildForRightArrow is None):

                fmt5 = 'RightArrow=%s; ' % str(self.ts_ChildForRightArrow)

            else:

                fmt5 = 'RightArrow=%d; ' % self.ts_ChildForRightArrow.ts_AssignedId

                self.ts_ChildForRightArrow.tsSetChildForText(
                    self.ts_ChildForText)

            if (self.ts_ChildForHorizontalGauge is None):

                fmt6 = 'HorizontalGauge=%s; ' % str(self.ts_ChildForHorizontalGauge)

            else:

                fmt6 = 'HorizontalGauge=%d; ' % self.ts_ChildForHorizontalGauge.ts_AssignedId

                self.ts_ChildForHorizontalGauge.tsSetChildForText(
                    self.ts_ChildForText)

            if (self.ts_ChildForUpArrow is None):

                fmt7 = 'UpArrow=%s; ' % str(self.ts_ChildForUpArrow)

            else:

                fmt7 = 'UpArrow=%d; ' % self.ts_ChildForUpArrow.ts_AssignedId

                self.ts_ChildForUpArrow.tsSetChildForText(
                    self.ts_ChildForText)

            if (self.ts_ChildForDownArrow is None):

                fmt8 = 'DownArrow=%s; ' % str(self.ts_ChildForDownArrow)

            else:

                fmt8 = 'DownArrow=%d; ' % self.ts_ChildForDownArrow.ts_AssignedId

                self.ts_ChildForDownArrow.tsSetChildForText(
                    self.ts_ChildForText)

            if (self.ts_ChildForVerticalGauge is None):

                fmt9 = 'VerticalGauge=%s; ' % str(self.ts_ChildForVerticalGauge)

            else:

                fmt9 = 'VerticalGauge=%d; ' % self.ts_ChildForVerticalGauge.ts_AssignedId

                self.ts_ChildForVerticalGauge.tsSetChildForText(
                    self.ts_ChildForText)

            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6 + fmt7 + fmt8 + fmt9
            print('NOTICE: %s\n' % msg)

    #-----------------------------------------------------------------------

##    def tsSetChildForVerticalScrollBar(self, child=None):
##        '''
##        Set control link to Scrolled.ChildForVerticalScrollBar.
##        '''
##        self.ts_ChildForVerticalScrollBar = child

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Scroll Bar specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.ts_Parent,
                            id=self.ts_AssignedId,
                            pos=(self.Position.x, self.Position.y),
                            size=(self.Size.width, self.Size.height),
                            style=self.ts_Style,
                            name=self.ts_Name,
                            pixels=True)

            try:

                self.tsRegisterShowOrder()

            except Exception, e:

                self.logger.error('%s; %s' % (__title__, e))


            if self.ts_Style & wx.HSCROLL:
                featureList = [self.ts_ChildForLeftArrow,
                               self.ts_ChildForHorizontalGauge,
                               self.ts_ChildForRightArrow]
            else:
                featureList = [self.ts_ChildForUpArrow,
                               self.ts_ChildForVerticalGauge,
                               self.ts_ChildForDownArrow]

            for feature in featureList:

                if not (feature is None):

                    feature.tsShow()

            self.tsUpdate()

    #-----------------------------------------------------------------------
 
    def tsUpdate(self):
        '''
        Draw the actual features of the Scroll Bar.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()

    ##        if self.ts_Style & wx.HSCROLL:
    ##            featureList = [self.ts_ChildForLeftArrow,
    ##                           self.ts_ChildForHorizontalGauge,
    ##                           self.ts_ChildForRightArrow]
    ##        else:
    ##            featureList = [self.ts_ChildForUpArrow,
    ##                           self.ts_ChildForVerticalGauge,
    ##                           self.ts_ChildForDownArrow]

    ##        for feature in featureList:

    ##            if not (feature is None):

    ##                if feature == self.ts_ChildForLeftArrow:

    ##                    feature.tsCursesAddStr(
    ##                        1,
    ##                        1,
    ##                        '*',
    ##                        attr=None,
    ##                        pixels=False)

    ##                    feature.tsShow()

        return (self.ts_Handle is not None)

##    #-----------------------------------------------------------------------

##    def tsUpdateScrolledText(self,
##                             text=wx.EmptyString,
##                             breakLongWords=True,
##                             expandTabs=True,
##                             fixSentenceEndings=False,
##                             initialIndent='',
##                             markup=None,
##                             newLine=True,
##                             replaceWhitespace=False,
##                             subsequentIndent='',
##                             theLineNumberWidth=0,
##                             topOfForm=False,
##                             wrap=False):
##        '''
##        Appends the text argument to the end of the text in the control.
##        The insertion point also moves to the end of the control.

##        Displays only selected columns and rows, blank fills short strings,
##        truncates long strings and terminates truncated string with '~')

##        Parameters:

##        text - String of ascii text characters. Accepted values include
##               empty string, simple string, and compound string separated
##               by embedded "\n".
##        '''
##        if text != wx.EmptyString:
##            newLines = text.split('\n')
##            for aLine in newLines:
##                self.ts_MaxTextCols = max(self.ts_MaxTextCols,
##                                          len(aLine))
##                self.lines += [aLine]

##        theTextCtrl = self.ts_ChildForText
##        theTextCtrlClientRect = theTextCtrl.ClientRect

##        maxCols = theTextCtrlClientRect.width // wx.pixelWidthPerCharacter
##        maxRows = theTextCtrlClientRect.height // wx.pixelHeightPerCharacter

##        if True:

##            firstDisplayedCol = self.ts_xScrollPosition

##            firstDisplayedRow = self.ts_yScrollPosition

##        else:

##            firstDisplayedCol = 0 + (
##                self.ts_xScrollPosition // wx.pixelWidthPerCharacter)

##            firstDisplayedRow = 0 + (
##                self.ts_yScrollPosition // wx.pixelHeightPerCharacter)

##        lastDisplayedCol = firstDisplayedCol + maxCols
##        lastDisplayedRow = firstDisplayedRow + min(maxRows, len(self.lines))

##        for row in range(firstDisplayedRow, lastDisplayedRow):

##            if row < len(self.lines):
##                aLine = self.lines[row]
##                aText = aLine[firstDisplayedCol:len(aLine)]
##            else:
##                aLine = ''
##                aText = aLine
##            if (len(aText) <= maxCols):
##                fill = ' ' * (maxCols - len(aText))
##                viewableText = aText + fill
##            else:
##                viewableText = aText[0:maxCols - 1] + '~'

##            theCol = 1 + \
##                     theTextCtrl.tsIsBorderThickness(self.ts_Style,
##                                                     pixels=False).width

##            theRow = 1 + row - firstDisplayedRow + \
##                     theTextCtrl.tsIsBorderThickness(self.ts_Style,
##                                                     pixels=False).height

##            theTextCtrl.tsCursesAddStr(theCol,
##                                       theRow,
##                                       viewableText,
##                                       attr=None,
##                                       pixels=False)

##        if not (self.ts_ChildForHorizontalScrollBar is None):
##            myHScrollBar = self.ts_ChildForHorizontalScrollBar
##            myHScrollGauge = myHScrollBar.ts_ChildForHorizontalGauge
##            myHScrollUpdate = myHScrollGauge.tsHScrollUpdate
##            myHScrollUpdate()

##        if not (self.ts_ChildForVerticalScrollBar is None):
##            myVScrollBar = self.ts_ChildForVerticalScrollBar
##            myVScrollGauge = myVScrollBar.ts_ChildForVerticalGauge
##            myVScrollUpdate = myVScrollGauge.tsVScrollUpdate
##            myVScrollUpdate()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

##    PageSize = property(GetPageSize)
##    Range = property(GetRange)
##    ThumbPosition = property(GetThumbPosition, SetThumbPosition)
##    ThumbSize = property(GetThumbSize)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
