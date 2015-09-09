#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:11:17 AM rsg>"
'''
tsWxScrolled.py - Template Class to manage scrolling for its
client area, transforming the coordinates according to the
scrollbar positions, and setting the scroll positions, thumb
sizes and ranges according to the area in view.
'''
#################################################################
#
# File: tsWxScrolled.py
#
# Purpose:
#
#    Template Class to manage scrolling for its client area,
#    transforming the coordinates according to the scrollbar
#    positions, and setting the scroll positions, thumb sizes
#    and ranges according to the area in view.
#
# Usage (example):
#
#    # Import
#
#    from tsWxScrolled import Scrolled as wxScrolled
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
#    ################################################################
#    #               wxPython Style - Parent Rectangle              #
#    # +-Optional Label-----------------------------------------+-+ #
#    # | Client Rectangle - Top Left         scrollbar vertical |^| #
#    # |                                                        +-+ #
#    # |                                                        |#| #
#    # |                                                        |#| #
#    # |                                                        |#| #
#    # |                                                        +-+ #
#    # | scrollbar horizontal   Client Rectangle - Bottom Right |v| #
#    # +-+----------------------------------------------------+-+-+ #
#    # |<|####################################################|>| | #
#    # +-+----------------------------------------------------+-+-+ #
#    ################################################################
#
#    tsWxScrolled - Creates multiple GUI objects within the client
#        area of its parent GUI object to provide a peep hole and
#        control buttons which enable an operator to scroll through
#        text that could not otherwise be displayed all at once.
#
#        Depending on application needs, there may horizontal and/or
#        vertical scrollbars and their associated buttons and "thumb"
#        gauges.
#
#        Each instance of this top level module initiates and
#        supervises the following sub-components:
#
#    tsWxScrolledText - Creates and operates a GUI object that provides
#        the scrollable text window. It displays only the text that fits
#        within the space assigend by tsWxScrolled.
#
#        When the text is too short to fill the displayed line, The text
#        is appended with blanks.
#
#        When the text is too long for the displayed line, the displayed
#        text is truncated and appended with a tilde ("~") character
#        to alert the operator.
#
#        Depending on application needs, the starting column and/or row
#        of the text portion to be display can be set upon receipt of an
#        event notification from the associated horizontal or vertical
#        scrollbar button.
#
#        Upon each text display update, it will issue the appropriate
#        horizontal or vertical event notification to the associated
#        tsWxScrollBarGauge instance.
#
#    tsWxScrollBar - Creates and supervises a multi-component GUI object
#        with the position and size established by tsWxScrolled.
#
#        When the tsWxScrolled specified a horizontal scrollbar, this
#        instance will initiate creation of two scrollbarbuttons, one
#        for the left arrow ("<") and one for the right arrow (">").
#
#        When the tsWxScrolled specified a vertical scrollbar, this
#        instance will initiate creation of two scrollbarbuttons, one
#        for the up arrow ("^") and one for the down arrow ("v").
#
#        tsWxScrollBarButton - Creates and operates the GUI object that
#            is displayed and will respond to the event notifications
#            of the operator's mouse button clicks.
#
#            Depending on the button's purpose, it will forward the
#            appropriate horizontal or vertical event notification
#            to the associated tsWxScrolledText instance.
#
#        tsWxScrollBarGauge - Creates and operates the GUI object for
#            a horizontal or vertical bar graph whose highlighted and
#            non-highlighted areas display the position and size of
#            text displayed in the associated tsWxScrolledText window
#            relative to the undisplayed text.
#
#    Hierarchivcal Relationships
#
#    Base Class                 Panel
#                                 |
#    Class                    Scrolled
#                                 |
#                      +----------+----------+
#                      |                     |
#                  ScrollBar            ScrolledText
#                      |
#           +----------+----------+
#           |                     |
#    ScrollBarButton        ScrollBarGauge
#
#    An application establishes the requirements for scrolled
#    text. It appends one or more lines of text when needed.
#    The operator clicks on scrollbar buttons to initiate
#    repositioning of the viewing window over some portion of
#    the text.
#
#    The tsWxScrolled module is responsible for high level layout
#    of the scrolled area consisting of horizontal and/or vertical
#    scrollbars and their associated two-dimensional text area.
#    It is also responsible for modifying the controls that update
#    the display.
#
#    The tsWxScrollBar module is responsible for mid level layout
#    of the scrolled area consisting of horizontal or vertical
#    scrollbars buttons and the associated scrollbar gauge.
#
#    The tsWxScrollBarGauge is responsible for the low level
#    layout of the horizontal or vertical area that depicts the
#    relative position and size of the displayed text.
#
#    Shared control data is established and maintatined, by
#    tsWxScrolled, in a database. To facilitate rapid development,
#    access requires knowledge of the ancestor hierarchy and the
#    data identifier. It would be preferable to pass the database
#    explicitly as a parameter.
#
#           Parent             Child                 Grandchild
#        -----------    --------------------     ------------------
#
#                       +--> tsWxScrolledText
#                       |
#        txWxScrolled --+--> tsWxScrollBar--+--> tsWxScrollBarGauge
#                                           |
#                                           +--> tsWxScrollBarButton
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
#    2012/02/12 rsg Conditionalized-out DEBUG statements in
#                   tsScrolledFeatureLayout.
#
#    2012/02/16 rsg Modified tsOn... to invoke
#                   tsProcessSelectedEventTable.
#
#    2012/02/18 rsg Added logic to support the following:
#                      tsAppendText (accepsts, empty string,
#                                    simple string, and
#                                    compound string separated
#                                    by embedded '\n')
#
#                      tsUpdateScrolledText (displays only
#                         selected columns and rows,
#                         blank fills short strings,
#                         truncates long strings and terminates
#                         truncated string with '~')
#
#    2012/02/18 rsg Added logic to support the following:
#                      tsOnHScrollWinBottom
#                      tsOnHScrollWinBottom
#                      tsOnHScrollWinLineDown
#                      tsOnHScrollWinLineUp
#                      tsOnHScrollWinPageDown
#                      tsOnHScrollWinPageUp
#                      tsOnHScrollWinTop
#                      tsOnVScrollWinLineDown
#                      tsOnVScrollWinLineUp
#                      tsOnVScrollWinPageDown
#                      tsOnVScrollWinPageUp
#                      tsOnVScrollWinTop
#
#    2012/02/21 rsg Added support for sending EVT_HSCROLLWIN...
#                   and EVT_VSCROLLWIN... from tsWxScrollBar to
#                   tsWxScrolled. This facilitated descrimination
#                   of tsWxScrollBarButton events when the associated
#                   ScrolledText had both horizontal and vertical controls.
#
#    2012/02/29 rsg Re-designed tsScrolledFeatureLayout to place
#                   tsWxScrollBarText below tsWxScrollBars so that
#                   the gauge borders are always superceded by those
#                   of the tsWxScrollBarButtons (previous design placed
#                   left or up button below gauge and right or down
#                   button on top.
#
#    2012/02/29 rsg Simplified interface to tsAppendText and to
#                   tsUpdateScrolledText.
#
#    2012/03/02 rsg Revised Notes. Removed extraneous variables
#                   and code that had previusly been commented-out.
#
#    2012/03/08 rsg Modified tsAppendText to support text style
#                   (e.g. wx.DISPLAY_REVERSE) and/or foreground/
#                   background color pair attribute markup.
#
#    2012/05/13 rsg Modified tsScrolledLayout to use a dryRun argument
#                   to inhibit the invocation of tsScrolledFeatureLayout
#                   during initialization. Multiple invocations had
#                   the undesirable consequence of creating multiple
#                   versions of child features.
#
#    2012/05/17 rsg Architectural and logic changes. The module
#                   tsWxScrolled is responsible for the high level
#                   layout of Scrolled Window features. It also
#                   provides interfaces to internal features of
#                   the tsWxScrolledText and the other child modukes.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event>.
#
# ToDo:
#
#    2012/02/17 rsg Modify tsUpdateScrolledText to support
#                   indentation via tabs ('\t') and
#                   wrapped text.
#
#    2012/02/20 rsg Troubleshoot failure to receive ScrollBarButton
#                   event notifications. Observed that Parent of
#                   Button(s) is a Panel object rather than a
#                   ScrollBar object.
#
#    2012/03/08 rsg Investigate technique that might enable
#                   markup to be applied to individual lines,
#                   words, columns.
#
#    2012/05/20 rsg Current mouse interface uses LeftClick,
#                   LeftDClick and RightClick. This works well
#                   with Cygwin under Windows. The RightClick
#                   usage is prempted by Apple's Mac OS X
#                   conventions.
#
#################################################################

__title__     = 'tsWxScrolled'
__version__   = '1.7.0'
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

from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxPanel import Panel as wxPanel
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxScrollBar import ScrollBar as wxScrollBar
from tsWxGTUI_Py2x.tsLibGUI.tsWxScrolledText \
     import ScrolledText as wxScrolledText
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Scrolled(wxPanel):
    '''
    The wxScrolled class manages scrolling for its client area, transforming
    the coordinates according to the scrollbar positions, and setting the
    scroll positions, thumb sizes and ranges according to the area in view.

    There are two commonly used (but not the only possible!) specializations
    of this class:

    wxScrolledWindow, aka wxScrolled<wxPanel>, is equivalent to
    wxScrolledWindow from earlier versions. Derived from wxPanel, it shares
    wxPanel behaviour with regard to TAB traversal and focus handling. Use
    this if the scrolled window will have child controls.

    wxScrolledCanvas, aka wxScrolled<wxWindow>, derives from wxWindow and
    so does not handle children specially. This is suitable e.g. for
    implementing scrollable controls such as tree or list controls.

    Starting from version 2.4 of wxWidgets, there are several ways to use
    a wxScrolledWindow (and now wxScrolled). In particular, there are three
    ways to set the size of the scrolling area:

    One way is to set the scrollbars directly using a call to SetScrollbars().
    This is the way it used to be in any previous version of wxWidgets and
    it will be kept for backwards compatibility.

    An additional method of manual control, which requires a little less
    computation of your own, is to set the total size of the scrolling area
    by calling either wxWindow::SetVirtualSize(), or wxWindow::FitInside(),
    and setting the scrolling increments for it by calling SetScrollRate().
    Scrolling in some orientation is enabled by setting a non-zero increment
    for it.

    The most automatic and newest way is to simply let sizers determine the
    scrolling area. This is now the default when you set an interior sizer
    into a wxScrolled with wxWindow::SetSizer(). The scrolling area will be
    set to the size requested by the sizer and the scrollbars will be
    assigned for each orientation according to the need for them and the
    scrolling increment set by SetScrollRate(). As above, scrolling is only
    enabled in orientations with a non-zero increment. You can influence
    the minimum size of the scrolled area controlled by a sizer by calling
    wxWindow::SetVirtualSizeHints(). (Calling SetScrollbars() has analogous
    effects in wxWidgets 2.4 -- in later versions it may not continue to
    override the sizer.)

    Note that if maximum size hints are still supported by
    wxWindow::SetVirtualSizeHints(), use them at your own dire risk.
    They may or may not have been removed for 2.4, but it really only makes
    sense to set minimum size hints here. We should probably replace
    wxWindow::SetVirtualSizeHints() with wxWindow::SetMinVirtualSize() or
    similar and remove it entirely in future.

    Todo: review docs for this class replacing SetVirtualSizeHints() with
    SetMinClientSize(). As with all windows, an application can draw onto
    a wxScrolled using a device context.

    You have the option of handling the OnPaint handler or overriding the
    wxScrolled::OnDraw() function, which is passed a pre-scrolled device
    context (prepared by wxScrolled::DoPrepareDC()).

    If you do not wish to calculate your own scrolling, you must call
    DoPrepareDC() when not drawing from within OnDraw(), to set the device
    origin for the device context according to the current scroll position.

    A wxScrolled will normally scroll itself and therefore its child windows
    as well. It might however be desired to scroll a different window than
    itself: e.g. when designing a spreadsheet, you will normally only have
    to scroll the (usually white) cell area, whereas the (usually grey) label
    area will scroll very differently. For this special purpose, you can
    call SetTargetWindow() which means that pressing the scrollbars will
    scroll a different window.

    Note that the underlying system knows nothing about scrolling coordinates,
    so that all system functions (mouse events, expose events, refresh calls
    etc) as well as the position of subwindows are relative to the
    "physical" origin of the scrolled window. If the user insert a child
    window at position (10,10) and scrolls the window down 100 pixels
    (moving the child window out of the visible area), the child window
    will report a position of (10,-90).

    Styles
    This class supports the following styles:

    wxRETAINED:
    Uses a backing pixmap to speed refreshes. Motif only.
    Events emitted by this class
    The following event handler macros redirect the events to member
    function handlers (func) with prototypes like:

    void handlerFuncName(wxScrollWinEvent& event)
    Event macros for events emitted by this class:

    EVT_SCROLLWIN(func):
    Process all scroll events.
    EVT_SCROLLWIN_TOP(func):
    Process wxEVT_SCROLLWIN_TOP scroll-to-top events.
    EVT_SCROLLWIN_BOTTOM(func):
    Process wxEVT_SCROLLWIN_BOTTOM scroll-to-bottom events.
    EVT_SCROLLWIN_LINEUP(func):
    Process wxEVT_SCROLLWIN_LINEUP line up events.
    EVT_SCROLLWIN_LINEDOWN(func):
    Process wxEVT_SCROLLWIN_LINEDOWN line down events.
    EVT_SCROLLWIN_PAGEUP(func):
    Process wxEVT_SCROLLWIN_PAGEUP page up events.
    EVT_SCROLLWIN_PAGEDOWN(func):
    Process wxEVT_SCROLLWIN_PAGEDOWN page down events.
    EVT_SCROLLWIN_THUMBTRACK(func):
    Process wxEVT_SCROLLWIN_THUMBTRACK thumbtrack events (frequent events
    sent as the user drags the thumbtrack).
    EVT_SCROLLWIN_THUMBRELEASE(func):
    Process wxEVT_SCROLLWIN_THUMBRELEASE thumb release events.
    Note:
    Do not confuse wxScrollWinEvents generated by this class with
    wxScrollEvent objects generated by wxScrollBar and wxSlider.

    Remarks:
    Use wxScrolled for applications where the user scrolls by a fixed amount,
    and where a (page) can be interpreted to be the current visible portion
    of the window. For more sophisticated applications, use the wxScrolled
    implementation as a guide to build your own scroll behaviour or use
    wxVScrolledWindow or its variants.

    Since:
    The wxScrolled template exists since version 2.9.0. In older versions,
    only wxScrolledWindow (equivalent of wxScrolled<wxPanel>) was available.
    '''
    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.HSCROLL | wx.VSCROLL,
                 name=wx.ScrolledNameStr):
        '''
        Construct and show a generic Window.
        '''
        theClass = 'ScrolledWindow'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        wxPanel.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         name=name)

        self.tsBeginClassRegistration(theClass, id)

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        #-------------------------------------------------------------------

        myRect, myClientRect = self.tsScrolledLayout(
            parent, pos, size, style, name, dryRun=True)

        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Label = label
        self.ts_Name = name
        self.ts_Parent = parent

        thePosition = self.Position
        theSize = self.Size

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_BackgroundColour = wx.ThemeToUse[
            'ScrollBar']['BackgroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse[
            'ScrollBar']['ForegroundColour'].lower()

        #-------------------------------------------------------------------

        # Begin Scrolled Class Instance Variable Initialization

##        self.curLine = []
##        self.drawing = False
##        self.ts_ScrolledTextLines = []
##        self.x = 0
##        self.y = 0

##        self.ts_MaxTextCols = 0
##        self.ts_MaxTextRows = 0
        self.ts_ChildForDualScrollBarAlignment = None
        self.ts_ChildForHorizontalScrollBar = None
        self.ts_ChildForText = None
        self.ts_ChildForVerticalScrollBar = None

##        self.ts_AutoScrolling = False
##        self.ts_Retained = False
##        self.ts_ScaleX = float(0.0)
##        self.ts_ScaleY = float(0.0)
##        self.ts_TargetWindow = None
##        self.ts_ViewStart = None
##        self.ts_Window = self # TBD - Is this required and appropriate
##        self.ts_xScrollLines = 0
##        self.ts_xScrollLinesPerPage = 0
##        self.ts_xScrollPixelsPerLine = 0
##        self.ts_xScrollPosition = 0
##        self.ts_yScrollLines = 0
##        self.ts_yScrollLinesPerPage = 0
##        self.ts_yScrollPixelsPerLine = 0
##        self.ts_yScrollPosition = 0

        # End Scrolled Class Instance Variable Initialization

        #-------------------------------------------------------------------

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def AdjustScrollbars(self):
        '''
        TBD - Under Construction.
        '''
        msg = 'NotImplementedError: %s' % \
            'AdjustScrollbars in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        {
##            static wxRecursionGuardFlag s_flagReentrancy;
##            wxRecursionGuard guard(s_flagReentrancy);
##            if ( guard.IsInside() )
##            {
##                // don't reenter AdjustScrollbars() while another call to
##                // AdjustScrollbars() is in progress because this may lead to calling
##                // ScrollWindow() twice and this can really happen under MSW if
##                // SetScrollbar() call below adds or removes the scrollbar which
##                // changes the window size and hence results in another
##                // AdjustScrollbars() call
##                return;
##            }

##            int w = 0, h = 0;
##            int oldw, oldh;

##            int oldXScroll = m_xScrollPosition;
##            int oldYScroll = m_yScrollPosition;

##            // VZ: at least under Windows this loop is useless because when scrollbars
##            //     [dis]appear we get a WM_SIZE resulting in another call to
##            //     AdjustScrollbars() anyhow. As it doesn't seem to do any harm I leave
##            //     it here for now but it would be better to ensure that all ports
##            //     generate EVT_SIZE when scrollbars [dis]appear, emulating it if
##            //     necessary, and remove it later
##            // JACS: Stop potential infinite loop by limiting number of iterations
##            int iterationCount = 0;
##            const int iterationMax = 5;
##            do
##            {
##                iterationCount ++;

##                GetTargetSize(&w, 0);

##                // scroll lines per page: if 0, no scrolling is needed
##                int linesPerPage;

##                if ( m_xScrollPixelsPerLine == 0 )
##                {
##                    // scrolling is disabled
##                    m_xScrollLines = 0;
##                    m_xScrollPosition = 0;
##                    linesPerPage = 0;
##                }
##                else // might need scrolling
##                {
##                    // Round up integer division to catch any "leftover" client space.
##                    const int wVirt = m_targetWindow->GetVirtualSize().GetWidth();
##                    m_xScrollLines = (wVirt + m_xScrollPixelsPerLine - 1) // m_xScrollPixelsPerLine;

##                    // Calculate page size i.e. number of scroll units you get on the
##                    // current client window.
##                    linesPerPage = w // m_xScrollPixelsPerLine;

##                    // Special case. When client and virtual size are very close but
##                    // the client is big enough, kill scrollbar.
##                    if ((linesPerPage < m_xScrollLines) && (w >= wVirt)) ++linesPerPage;

##                    if (linesPerPage >= m_xScrollLines)
##                    {
##                        // we're big enough to not need scrolling
##                        linesPerPage =
##                        m_xScrollLines =
##                        m_xScrollPosition = 0;
##                    }
##                    else // we do need a scrollbar
##                    {
##                        if ( linesPerPage < 1 )
##                            linesPerPage = 1;

##                        // Correct position if greater than extent of canvas minus
##                        // the visible portion of it or if below zero
##                        const int posMax = m_xScrollLines - linesPerPage;
##                        if ( m_xScrollPosition > posMax )
##                            m_xScrollPosition = posMax;
##                        else if ( m_xScrollPosition < 0 )
##                            m_xScrollPosition = 0;
##                    }
##                }

##                m_win->SetScrollbar(wxHORIZONTAL, m_xScrollPosition,
##                                    linesPerPage, m_xScrollLines);

##                // The amount by which we scroll when paging
##                SetScrollPageSize(wxHORIZONTAL, linesPerPage);

##                GetTargetSize(0, &h);

##                if ( m_yScrollPixelsPerLine == 0 )
##                {
##                    // scrolling is disabled
##                    m_yScrollLines = 0;
##                    m_yScrollPosition = 0;
##                    linesPerPage = 0;
##                }
##                else // might need scrolling
##                {
##                    // Round up integer division to catch any "leftover" client space.
##                    const int hVirt = m_targetWindow->GetVirtualSize().GetHeight();
##                    m_yScrollLines = ( hVirt + m_yScrollPixelsPerLine - 1 ) // m_yScrollPixelsPerLine;

##                    // Calculate page size i.e. number of scroll units you get on the
##                    // current client window.
##                    linesPerPage = h // m_yScrollPixelsPerLine;

##                    // Special case. When client and virtual size are very close but
##                    // the client is big enough, kill scrollbar.
##                    if ((linesPerPage < m_yScrollLines) && (h >= hVirt)) ++linesPerPage;

##                    if (linesPerPage >= m_yScrollLines)
##                    {
##                        // we're big enough to not need scrolling
##                        linesPerPage =
##                        m_yScrollLines =
##                        m_yScrollPosition = 0;
##                    }
##                    else // we do need a scrollbar
##                    {
##                        if ( linesPerPage < 1 )
##                            linesPerPage = 1;

##                        // Correct position if greater than extent of canvas minus
##                        // the visible portion of it or if below zero
##                        const int posMax = m_yScrollLines - linesPerPage;
##                        if ( m_yScrollPosition > posMax )
##                            m_yScrollPosition = posMax;
##                        else if ( m_yScrollPosition < 0 )
##                            m_yScrollPosition = 0;
##                    }
##                }

##                m_win->SetScrollbar(wxVERTICAL, m_yScrollPosition,
##                                    linesPerPage, m_yScrollLines);

##                // The amount by which we scroll when paging
##                SetScrollPageSize(wxVERTICAL, linesPerPage);


##                // If a scrollbar (dis)appeared as a result of this, adjust them again.
##                oldw = w;
##                oldh = h;

##                GetTargetSize( &w, &h );
##            } while ( (w != oldw || h != oldh) && (iterationCount < iterationMax) );

##        #ifdef __WXMOTIF__
##            // Sorry, some Motif-specific code to implement a backing pixmap
##            // for the wxRETAINED style. Implementing a backing store can't
##            // be entirely generic because it relies on the wxWindowDC implementation
##            // to duplicate X drawing calls for the backing pixmap.

##            if ( m_targetWindow->GetWindowStyle() & wxRETAINED )
##            {
##                Display* dpy = XtDisplay((Widget)m_targetWindow->GetMainWidget());

##                int totalPixelWidth = m_xScrollLines * m_xScrollPixelsPerLine;
##                int totalPixelHeight = m_yScrollLines * m_yScrollPixelsPerLine;
##                if (m_targetWindow->GetBackingPixmap() &&
##                   !((m_targetWindow->GetPixmapWidth() == totalPixelWidth) &&
##                     (m_targetWindow->GetPixmapHeight() == totalPixelHeight)))
##                {
##                    XFreePixmap (dpy, (Pixmap) m_targetWindow->GetBackingPixmap());
##                    m_targetWindow->SetBackingPixmap((WXPixmap) 0);
##                }

##                if (!m_targetWindow->GetBackingPixmap() &&
##                   (m_xScrollLines != 0) && (m_yScrollLines != 0))
##                {
##                    int depth = wxDisplayDepth();
##                    m_targetWindow->SetPixmapWidth(totalPixelWidth);
##                    m_targetWindow->SetPixmapHeight(totalPixelHeight);
##                    m_targetWindow->SetBackingPixmap((WXPixmap) XCreatePixmap (dpy, RootWindow (dpy, DefaultScreen (dpy)),
##                      m_targetWindow->GetPixmapWidth(), m_targetWindow->GetPixmapHeight(), depth));
##                }

##            }
##        #endif // Motif

##            if (oldXScroll != m_xScrollPosition)
##            {
##               if (m_xScrollingEnabled)
##                    m_targetWindow->ScrollWindow( m_xScrollPixelsPerLine * (oldXScroll - m_xScrollPosition), 0,
##                                                  GetScrollRect() );
##               else
##                    m_targetWindow->Refresh(true, GetScrollRect());
##            }

##            if (oldYScroll != m_yScrollPosition)
##            {
##                if (m_yScrollingEnabled)
##                    m_targetWindow->ScrollWindow( 0, m_yScrollPixelsPerLine * (oldYScroll-m_yScrollPosition),
##                                                  GetScrollRect() );
##                else
##                    m_targetWindow->Refresh(true, GetScrollRect());
##            }
##        }

##        void wxScrollHelper::DoPrepareDC(wxDC& dc)
##        {
##            wxPoint pt = dc.GetDeviceOrigin();
##        #ifdef __WXGTK__
##            // It may actually be correct to always query
##            // the m_sign from the DC here, but I leve the
##            // #ifdef GTK for now.
##            if (m_win->GetLayoutDirection() == wxLayout_RightToLeft)
##                dc.SetDeviceOrigin( pt.x + m_xScrollPosition * m_xScrollPixelsPerLine,
##                                    pt.y - m_yScrollPosition * m_yScrollPixelsPerLine );
##            else
##        #endif
##                dc.SetDeviceOrigin( pt.x - m_xScrollPosition * m_xScrollPixelsPerLine,
##                                    pt.y - m_yScrollPosition * m_yScrollPixelsPerLine );
##            dc.SetUserScale( m_scaleX, m_scaleY );
##        }

    #-----------------------------------------------------------------------

    def CalcScrolledPosition(self, x, y, xx, yy):
        '''
        Translates the logical coordinates to the device ones.
        For example, if a window is scrolled 10 pixels to the bottom,
        the device coordinates of the origin are (0, 0) (as always),
        but the logical coordinates are (0, 10) and so the call to
        CalcScrolledPosition(0, 10, &xx, &yy) will return 0 in yy.
        '''
        msg = 'NotImplementedError: %s' % \
            'CalcScrolledPosition in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if (xx > 0):
##            xx = x - (self.ts_xScrollPosition * wx.pixelWidthPerCharacter)

##        if (yy > 0):
##            yy = y - (self.ts_yScrollPosition * wx.pixelHeightPerCharacter)

##        return wxPoint(xx, yy)

    #-----------------------------------------------------------------------

    def CalcScrollInc(self, event):
        '''
        TBD - Under Construction.
        '''
        msg = 'NotImplementedError: %s' % \
            'CalcScrollInc in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        {
##            int pos = event.GetPosition();
##            int orient = event.GetOrientation();

##            int nScrollInc = 0;
##            if (event.GetEventType() == wxEVT_SCROLLWIN_TOP)
##            {
##                    if (orient == wxHORIZONTAL)
##                        nScrollInc = - m_xScrollPosition;
##                    else
##                        nScrollInc = - m_yScrollPosition;
##            } else
##            if (event.GetEventType() == wxEVT_SCROLLWIN_BOTTOM)
##            {
##                    if (orient == wxHORIZONTAL)
##                        nScrollInc = m_xScrollLines - m_xScrollPosition;
##                    else
##                        nScrollInc = m_yScrollLines - m_yScrollPosition;
##            } else
##            if (event.GetEventType() == wxEVT_SCROLLWIN_LINEUP)
##            {
##                    nScrollInc = -1;
##            } else
##            if (event.GetEventType() == wxEVT_SCROLLWIN_LINEDOWN)
##            {
##                    nScrollInc = 1;
##            } else
##            if (event.GetEventType() == wxEVT_SCROLLWIN_PAGEUP)
##            {
##                    if (orient == wxHORIZONTAL)
##                        nScrollInc = -GetScrollPageSize(wxHORIZONTAL);
##                    else
##                        nScrollInc = -GetScrollPageSize(wxVERTICAL);
##            } else
##            if (event.GetEventType() == wxEVT_SCROLLWIN_PAGEDOWN)
##            {
##                    if (orient == wxHORIZONTAL)
##                        nScrollInc = GetScrollPageSize(wxHORIZONTAL);
##                    else
##                        nScrollInc = GetScrollPageSize(wxVERTICAL);
##            } else
##            if ((event.GetEventType() == wxEVT_SCROLLWIN_THUMBTRACK) ||
##                (event.GetEventType() == wxEVT_SCROLLWIN_THUMBRELEASE))
##            {
##                    if (orient == wxHORIZONTAL)
##                        nScrollInc = pos - m_xScrollPosition;
##                    else
##                        nScrollInc = pos - m_yScrollPosition;
##            }

##            if (orient == wxHORIZONTAL)
##            {
##                if (m_xScrollPixelsPerLine > 0)
##                {
##                    if ( m_xScrollPosition + nScrollInc < 0 )
##                    {
##                        // As -ve as we can go
##                        nScrollInc = -m_xScrollPosition;
##                    }
##                    else // check for the other bound
##                    {
##                        const int posMax = m_xScrollLines - m_xScrollLinesPerPage;
##                        if ( m_xScrollPosition + nScrollInc > posMax )
##                        {
##                            // As +ve as we can go
##                            nScrollInc = posMax - m_xScrollPosition;
##                        }
##                    }
##                }
##                else
##                    m_targetWindow->Refresh(true, GetScrollRect());
##            }
##            else
##            {
##                if ( m_yScrollPixelsPerLine > 0 )
##                {
##                    if ( m_yScrollPosition + nScrollInc < 0 )
##                    {
##                        // As -ve as we can go
##                        nScrollInc = -m_yScrollPosition;
##                    }
##                    else // check for the other bound
##                    {
##                        const int posMax = m_yScrollLines - m_yScrollLinesPerPage;
##                        if ( m_yScrollPosition + nScrollInc > posMax )
##                        {
##                            // As +ve as we can go
##                            nScrollInc = posMax - m_yScrollPosition;
##                        }
##                    }
##                }
##                else
##                {
##                    // VZ: why do we do this? (FIXME)
##                    m_targetWindow->Refresh(true, GetScrollRect());
##                }
##            }

##            return nScrollInc;
##        }
##        return int

    #-----------------------------------------------------------------------

    def CalcUnscrolledPosition(self, x, y, xx, yy):
        '''
        Translates the device coordinates to the logical ones. For
        example, if a window is scrolled 10 pixels to the bottom,
        the device coordinates of the origin are (0, 0) (as always),
        but the logical coordinates are (0, 10) and so the call to
        CalcUnscrolledPosition(0, 0, &xx, &yy) will return 10 in yy.
        '''
        msg = 'NotImplementedError: %s' % \
            'CalcUnscrolledPosition in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if (xx > 0):
##            xx = x + (self.ts_xScrollPosition * wx.pixelWidthPerCharacter)

##        if (yy > 0):
##            yy = y + (self.ts_yScrollPosition * wx.pixelHeightPerCharacter)

##        return wxPoint(xx, yy)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=-wx.ID_ANY,
               # label=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.HSCROLL | wx.VSCROLL,
               name=wx.PanelNameStr,
               pixels=True):
        '''
        Creates the window for two-step construction. Derived classes
        should call or replace this function.
        '''
        myRect, myClientRect = self.tsScrolledLayout(
            parent, pos=pos, size=size, style=style, name=name, pixels=pixels)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def DisableKeyboardScrolling(self):
        '''
        Disable use of keyboard keys for scrolling.

        By default cursor movement keys (including Home, End, Page Up and
        Down) are used to scroll the window appropriately. If the derived
        class uses these keys for something else, e.g. changing the
        currently selected item, this function can be used to disable this
        behaviour as it is not only not necessary then but can actually
        be actively harmful if another object forwards a keyboard event
        corresponding to one of the above keys to us using
        ProcessWindowEvent() because the event will always be processed
        which can be undesirable.
        '''
        msg = 'NotImplementedError: %s' % \
            'DisableKeyboardScrolling in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def DoPrepareDC(self, dc):
        '''
        Call this function to prepare the device context for drawing a
        scrolled image. It sets the device origin according to the current
        scroll position.

        DoPrepareDC is called automatically within the default
        wxScrolledWindow::OnPaint event handler, so your
        wxScrolledWindow::OnDraw override will be passed a pre-scrolled
        device context. However, if you wish to draw from outside of
        OnDraw (via OnPaint), or you wish to implement OnPaint yourself,
        you must call this function yourself.
        '''
        msg = 'NotImplementedError: %s' % 'DoPrepareDC in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        {
##            wxPoint pt = dc.GetDeviceOrigin();
##        #ifdef __WXGTK__
##            // It may actually be correct to always query
##            // the m_sign from the DC here, but I leve the
##            // #ifdef GTK for now.
##            if (m_win->GetLayoutDirection() == wxLayout_RightToLeft)
##                dc.SetDeviceOrigin( pt.x + m_xScrollPosition * m_xScrollPixelsPerLine,
##                                    pt.y - m_yScrollPosition * m_yScrollPixelsPerLine );
##            else
##        #endif
##                dc.SetDeviceOrigin( pt.x - m_xScrollPosition * m_xScrollPixelsPerLine,
##                                    pt.y - m_yScrollPosition * m_yScrollPixelsPerLine );
##            dc.SetUserScale( m_scaleX, m_scaleY );
##        }

    #-----------------------------------------------------------------------

    def EnableScrolling(self, x_scrolling=False, y_scrolling=False):
        '''
        Enable or disable physical scrolling in the given direction.
        Physical scrolling is the physical transfer of bits up or down
        the screen when a scroll event occurs. If the application
        scrolls by a variable amount (e.g. if there are different font
        sizes) then physical scrolling will not work, and you should
        switch it off. Note that you will have to reposition child
        windows yourself, if physical scrolling is disabled.

        Parameters

        xScrolling

        If true, enables physical scrolling in the x direction.
        yScrolling

        If true, enables physical scrolling in the y direction.
        Remarks

        Physical scrolling may not be available on all platforms.
        Where it is available, it is enabled by default.
        '''
        self.ts_xScrollingEnabled = x_scrolling
        self.ts_yScrollingEnabled = y_scrolling

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        users system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See wx.Window.SetWindowVariant for more about this.
        '''
        return variant

    #-----------------------------------------------------------------------

    def GetScaleX(self):
        '''
        Return the ScaleX status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0.0)
        else:
            return (self.ts_ChildForText.ts_ScaleX)

    #-----------------------------------------------------------------------

    def GetScaleY(self):
        '''
        Return the ScaleY status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0.0)
        else:
            return (self.ts_ChildForText.ts_ScaleY)

    #-----------------------------------------------------------------------

    def GetScrollPageSize(self, orient):
        '''
        Return the ScalePageSize status of tsWxScrolledText for the
        designated orientation.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:

            if (orient == wx.HORIZONTAL):
                return (self.ts_ChildForText.ts_xScrollLinesPerPage)
            else:
                return (self.ts_ChildForText.ts_yScrollLinesPerPage)

    #-----------------------------------------------------------------------

    def GetScrollPixelsPerUnit(self):
        '''
        Get the number of pixels per scroll unit (line) of tsWxScrolledText,
        in each direction, as set by wxScrolledWindow::SetScrollbars. A
        value of zero indicates no scrolling in that direction.

        Parameters

        xUnit

        Receives the number of pixels per horizontal unit.
        yUnit

        Receives the number of pixels per vertical unit.
        '''
        if self.ts_ChildForText is None:
            xUnit = 0
            yUnit = 0
        else:
            xUnit = self.ts_ChildForText.ts_xScrollPixelsPerLine
            yUnit = self.ts_ChildForText.ts_yScrollPixelsPerLine

        return (xUnit, yUnit)

    #-----------------------------------------------------------------------

    def GetScrollRect(self):
        '''
        Return the Scrolled Window Rectangle of tsWxScrolledText.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'GetScrollRect in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if self.ts_ChildForText is None:
##            return wxRect(0, 0, 0, 0)
##        else:
##            return (self.ts_ChildForText.Rect)

    #-----------------------------------------------------------------------

    def GetSizeAvailableForScrollTarget(self):
        '''
        Function which must be overridden to implement the size available
        for the scroll target for the given size of the main window.

        This method must be overridden if SetTargetWindow() is used
        (it is never called otherwise). The implementation should decrease
        the size to account for the size of the non-scrollable parts of the
        main window and return only the size available for the scrollable
        window itself. E.g. in the example given in SetTargetWindow()
        documentation the function would subtract the height of the
        header window from the vertical component of size.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'GetSizeAvailableForScrollTarget in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # return (self.ts_TargetClientSize)

    #-----------------------------------------------------------------------

    def GetTargetRect(self):
        '''
        Return Target Rectangle.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetTargetRect in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if self.ts_TargetWindow is None:
##            myRect = wxRect(0, 0, 0, 0)
##        else:
##            myRect = self.ts_TargetWindow.Rect
##        return (myRect)

    #-----------------------------------------------------------------------

    def GetTargetSize(self):
        '''
        Return Target Size.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetTargetSize in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if self.ts_TargetWindow is None:
##            mySize = wxSize(0, 00)
##        else:
##            mySize = self.ts_TargetWindow.Size
##        return (mySize)

    #-----------------------------------------------------------------------

    def GetTargetWindow(self):
        '''
        Return Target Window.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetTargetWindow in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        return (self.ts_TargetWindow)

    #-----------------------------------------------------------------------

    def GetViewStart(self):
        '''
        Get the position at which the visible portion of the window starts.

        Parameters

        x - Receives the first visible x position in scroll units.
        y - Receives the first visible y position in scroll units.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetViewStart in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        x = self.ts_xScrollPosition
##        y = self.ts_yScrollPosition

##        return (x, y)

    #-----------------------------------------------------------------------

    def GetVirtualSize(self):
        '''
        Gets the size in device units of the scrollable window area
        (as opposed to the client size, which is the area of the
        window currently visible).

        Parameters

        x - Receives the length of the scrollable window, in pixels.
        y - Receives the height of the scrollable window, in pixels.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'GetVirtualSize in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsAutoScrolling(self):
        '''
        Return True only if AutoScrolling is currently active.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_AutoScrolling)

    #-----------------------------------------------------------------------

    def IsRetained(self):
        '''
        Motif only: true if the window has a backing bitmap.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_Retained)

    #-----------------------------------------------------------------------

    def OnDraw(self, dc):
        '''
        Called by the default paint event handler to allow the
        application to define painting behaviour without having to
        worry about calling wxScrolledWindow::DoPrepareDC.

        Instead of overriding this function you may also just process
        the paint event in the derived class as usual, but then you
        will have to call DoPrepareDC() yourself.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'OnDraw in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrepareDC(self, dc):
        '''
        This function is for backwards compatibility only and simply
        calls DoPrepareDC now. Notice that it is not called by the
        default paint event handle (DoPrepareDC() is), so overriding
        this method in your derived class is useless.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'PrepareDC in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

##void wxScrollHelperNative::DoScroll(int orient,
##                                    GtkAdjustment *adj,
##                                    int pos,
##                                    int pixelsPerLine,
##                                    int *posOld)
##{
##    if ( pos != -1 && pos != *posOld && pixelsPerLine )
##    {
##        int max = (int)(adj->upper - adj->page_size + 0.5);
##        if (max < 0)
##            max = 0;
##        if (pos > max)
##            pos = max;
##        if (pos < 0)
##            pos = 0;

##        adj->value = pos;

##        int diff = (*posOld - pos)*pixelsPerLine;
##        m_targetWindow->ScrollWindow(orient == wxHORIZONTAL ? diff : 0,
##                                     orient == wxHORIZONTAL ? 0 : diff);

##        *posOld = pos;

##        m_win->GtkUpdateScrollbar(orient);
##    }
##}

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
        if not (self.ts_ChildForText is None):

            self.ts_ChildForText.Scroll(x_pos, y_pos)

    #-----------------------------------------------------------------------

    def SetScale(self, xs, ys):
        '''
        TBD - Under Construction.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'SetScale in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetScrollbars(self,
                      pixelsPerUnitX,
                      pixelsPerUnitY,
                      noUnitsX,
                      noUnitsY,
                      xPos=0,
                      yPos=0,
                      noRefresh=False):
        '''
        Sets up vertical and/or horizontal scrollbars.

        Parameters

        pixelsPerUnitX
        Pixels per scroll unit in the horizontal direction.

        pixelsPerUnitY
        Pixels per scroll unit in the vertical direction.

        noUnitsX
        Number of units in the horizontal direction.

        noUnitsY
        Number of units in the vertical direction.

        xPos
        Position to initialize the scrollbars in the horizontal
        direction, in scroll units.

        yPos
        Position to initialize the scrollbars in the vertical
        direction, in scroll units.

        noRefresh
        Will not refresh window if true.

        Remarks

        The first pair of parameters give the number of pixels per
        scroll step, i.e. amount moved when the up or down scroll
        arrows are pressed. The second pair gives the length of
        scrollbar in scroll steps, which sets the size of the virtual window.

        xPos and yPos optionally specify a position to scroll to immediately.

        For example, the following gives a window horizontal and vertical
        scrollbars with 20 pixels per scroll step, and a size of 50 steps
        (1000 pixels) in each direction.

        window->SetScrollbars(20, 20, 50, 50);

        wxScrolledWindow manages the page size itself, using the current
        client window size as the page size.

        Note that for more sophisticated scrolling applications, for
        example where scroll steps may be variable according to the
        position in the document, it will be necessary to derive a
        new class from wxWindow, overriding OnSize and adjusting the
        scrollbars appropriately.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % \
            'SetScrollbars in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if True:
##            xx = 0 # TBD - value
##            yy = 0 # TBD - value
##            xPos, yPos = self.CalcUnscrolledPosition(xPos, yPos, xx, yy)
##            do_refresh = (
##              ((noUnitsX != 0) and (self.ts_xScrollLines == 0)) or

##              ((noUnitsX < self.ts_xScrollLines) and \
##               (xPos > (pixelsPerUnitX * noUnitsX))) or

##              ((noUnitsY != 0) and (self.ts_yScrollLines == 0)) or

##              ((noUnitsY < self.ts_yScrollLines) and \
##               (yPos > (pixelsPerUnitY * noUnitsY))) or

##              ((xPos != self.ts_xScrollPosition) or

##              (yPos != self.ts_yScrollPosition))
##            )

##            self.ts_xScrollPixelsPerLine = pixelsPerUnitX
##            self.ts_yScrollPixelsPerLine = pixelsPerUnitY
##            self.ts_xScrollPosition = xPos
##            self.ts_yScrollPosition = yPos

##            w = noUnitsX * pixelsPerUnitX
##            h = noUnitsY * pixelsPerUnitY

##            # For better backward compatibility we set persisting limits
##            # here not just the size.  It makes SetScrollbars 'sticky'
##            # emulating the old non-autoscroll behaviour.
##            #   self.ts_TargetWindow->SetVirtualSizeHints( w, h )

##            # The above should arguably be deprecated, this however we still
##            # need.

##            # take care not to set 0 virtual size, 0 means that we do not have
##            # any scrollbars and hence we should use the real size instead of
##            # the virtual one which is indicated by using wxDefaultCoord
####            self.ts_TargetWindow.SetVirtualSize(w ? w : wxDefaultCoord,
####                                                h ? h : wxDefaultCoord)
##            self.ts_TargetWindow.SetVirtualSize(max(w, wx.DefaultCoord),
##                                                max(h, wx.DefaultCoord))

##            if (do_refresh and not noRefresh):
##                self.ts_TargetWindow.Refresh(True, self.GetScrollRect())

##            # If the target is not the same as the window with the scrollbars,
##            # then we need to update the scrollbars here, since they will not
##            # have been updated by SetVirtualSize().
##            if (self.ts_TargetWindow != self.ts_Window):
##                self.AdjustScrollbars()
##            else:
##                # otherwise this has been done by AdjustScrollbars, above
##                pass
##        else:

##            msg = 'NotImplementedError: ' + \
##                  '%s' % \
##                  'SetScrollbars in tsWxScrolled'
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetScrollPageSize(self, orient, pageSize):
        '''
        TBD - Under Construction.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'SetScrollPageSize in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if True:

##            if (orient == wx.HORIZONTAL):

##                self.ts_xScrollLinesPerPage = pageSize

##            else:

##                self.ts_yScrollLinesPerPage = pageSize

##        else:

##            msg = 'NotImplementedError: ' + \
##                  '%s' % 'SetScrollPageSize in tsWxScrolled'
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetScrollRate(self, xstep, ystep):
        '''
        Set the horizontal and vertical scrolling increment only.
        See the pixelsPerUnit parameter in SetScrollbars.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'SetScrollRate in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        if True:

##            old_x = self.ts_xScrollPixelsPerLine * self.ts_xScrollPosition
##            old_y = self.ts_yScrollPixelsPerLine * self.ts_yScrollPosition

##            self.ts_xScrollPixelsPerLine = xstep
##            self.ts_yScrollPixelsPerLine = ystep

##            new_x = self.ts_xScrollPixelsPerLine * self.ts_xScrollPosition
##            new_y = self.ts_yScrollPixelsPerLine * self.ts_yScrollPosition

##            self.SetScrollPos(wx.HORIZONTAL, self.ts_xScrollPosition)
##            self.SetScrollPos(wx.VERTICAL, self.ts_yScrollPosition)
##            self.ScrollWindow(old_x - new_x, old_y - new_y)

##            self.AdjustScrollbars()

##        else:

##            msg = 'NotImplementedError: ' + \
##                  '%s' % 'SetScrollRate in tsWxScrolled'
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetTargetWindow(self, target):
        '''
        Call this function to tell wxScrolled to perform the actual
        scrolling on a different window (and not on itself).

        This method is useful when only a part of the window should be
        scrolled. A typical example is a control consisting of a fixed
        header and the scrollable contents window: the scrollbars are
        attached to the main window itself, hence it, and not the
        contents window must be derived from wxScrolled, but only
        the contents window scrolls when the scrollbars are used.
        To implement such setup, you need to call this method with
        the contents window as argument.

        Notice that if this method is used,
        GetSizeAvailableForScrollTarget() method must be overridden.
        '''
        msg = 'NotImplementedError: ' + \
            '%s' % 'SetTargetWindow in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        self.logger.wxASSERT_MSG(
##            (not (target is None)),
##            'SetTargetWindow: target cannot be %s' % target)

##        if self.ts_TargetWindow != target:

##            self.ts_TargetWindow = target

    #-----------------------------------------------------------------------

    def ShowScrollbars(self, horiz=False, vert=False):
        '''
        Set the scrollbar visibility.

        By default the scrollbar in the corresponding direction is only
        shown if it is needed, i.e. if the virtual size of the scrolled
        window in this direction is greater than the current physical
        window size. Using this function the scrollbar visibility can be
        changed to be:

        wxSHOW_SB_ALWAYS: To always show the scrollbar, even if it is not
        needed currently (wxALWAYS_SHOW_SB style can be used during the
        window creation to achieve the same effect but it applies in both
        directions).

        wxSHOW_SB_NEVER: To never show the scrollbar at all. In this case
        the program should presumably provide some other way for the user
        to scroll the window.

        wxSHOW_SB_DEFAULT: To restore the default behaviour described above.

        Parameters:
        horz    The desired visibility for the horizontal scrollbar.
        vert    The desired visibility for the vertical scrollbar.
        '''

        msg = 'NotImplementedError: ' + \
            '%s' % 'ShowScrollbars in tsWxScrolled'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

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
        if self.ts_ChildForText is None:
            self.logger.error(
                'tsWxScrolled.tsAppendText: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:
            if False:
                print('tsWxScrolled.tsAppendText: text="%s"' % text)

            self.ts_ChildForText.tsAppendText(text, markup)

    #-----------------------------------------------------------------------

    def tsGet_AutoScrolling(self):
        '''
        Return the AutoScrolling status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_AutoScrolling)

    #-----------------------------------------------------------------------

    def tsGet_MaxTextCols(self):
        '''
        Return the MaxTextCols status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_MaxTextCols)

    #-----------------------------------------------------------------------

    def tsGet_MaxTextRows(self):
        '''
        Return the MaxTextRows status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_MaxTextRows)

    #-----------------------------------------------------------------------

    def tsGet_Retained(self):
        '''
        Return the Retained status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_Retained)

    #-----------------------------------------------------------------------

    def tsGet_ScaleX(self):
        '''
        Return the ScaleX status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0.0)
        else:
            return (self.ts_ChildForText.ts_ScaleX)

    #-----------------------------------------------------------------------

    def tsGet_ScaleY(self):
        '''
        Return the ScaleY status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0.0)
        else:
            return (self.ts_ChildForText.ts_ScaleY)

    #-----------------------------------------------------------------------

    def tsGet_ScrolledTextLines(self):
        '''
        Return the ScrolledTextLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return ([])
        else:
            return (self.ts_ChildForText.ts_ScrolledTextLines)

    #-----------------------------------------------------------------------

    def tsGet_TargetWindow(self):
        '''
        Return the TargetWindow status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (None)
        else:
            return (self.ts_ChildForText.ts_TargetWindow)

    #-----------------------------------------------------------------------

    def tsGet_ViewStart(self):
        '''
        Return the ViewStart status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_ViewStart)

    #-----------------------------------------------------------------------

    def tsGet_xScrollLines (self):
        '''
        Return the xScrollLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_xScrollLines)

    #-----------------------------------------------------------------------

    def tsGet_xScrollLinesPerPage(self):
        '''
        Return the xScrollLinesPerPage status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_xScrollLinesPerPage)

    #-----------------------------------------------------------------------

    def tsGet_xScrollPixelsPerLine(self):
        '''
        Return the xScrollPixelsPerLine status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_xScrollPixelsPerLine)

    #-----------------------------------------------------------------------

    def tsGet_xScrollPosition(self):
        '''
        Return the xScrollPosition status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_xScrollPosition)

    #-----------------------------------------------------------------------

    def tsGet_xScrollingEnabled(self):
        '''
        Return the xScrollingEnabled status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_xScrollingEnabled)

    #-----------------------------------------------------------------------

    def tsGet_yScrollLines(self):
        '''
        Return the yScrollLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_yScrollLines)

    #-----------------------------------------------------------------------

    def tsGet_yScrollLinesPerPage(self):
        '''
        Return the yScrollLinesPerPage status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_yScrollLinesPerPage)

    #-----------------------------------------------------------------------

    def tsGet_yScrollPixelsPerLine(self):
        '''
        Return the yScrollPixelsPerLine status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_yScrollPixelsPerLine)

    #-----------------------------------------------------------------------

    def tsGet_yScrollPosition(self):
        '''
        Return the yScrollPosition status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (0)
        else:
            return (self.ts_ChildForText.ts_yScrollPosition)

    #-----------------------------------------------------------------------

    def tsGet_yScrollingEnabled(self):
        '''
        Return the yScrollingEnabled status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:
            return (False)
        else:
            return (self.ts_ChildForText.ts_yScrollingEnabled)

    #-----------------------------------------------------------------------

##    def tsOnLeftClick(self):
##        '''
##        '''
##        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
##              'tsOnLeftClick'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        precedenceSequence = [True, False]
##        for precedence in precedenceSequence:

##            self.tsProcessSelectedEventTable(
##                objectCriteria=objectCriteria,
##                objectId=objectId,
##                triggeringEvent=triggeringEvent,
##                triggeringObject=triggeringObject,
##                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

##    def tsOnLeftDClick(self):
##        '''
##        '''
##        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
##              'tsOnLeftDClick'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        precedenceSequence = [True, False]
##        for precedence in precedenceSequence:

##            self.tsProcessSelectedEventTable(
##                objectCriteria=objectCriteria,
##                objectId=objectId,
##                triggeringEvent=triggeringEvent,
##                triggeringObject=triggeringObject,
##                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

##    def tsOnRightClick(self):
##        '''
##        '''
##        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
##              'tsOnRighttClick'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        precedenceSequence = [True, False]
##        for precedence in precedenceSequence:

##            self.tsProcessSelectedEventTable(
##                objectCriteria=objectCriteria,
##                objectId=objectId,
##                triggeringEvent=triggeringEvent,
##                triggeringObject=triggeringObject,
##                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

    def tsOnHScrollWin(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollWinBottom: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinBottom(evt)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineDown(self, evt):
        '''
        Set scroll position to next column.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollLineDown: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinLineDown(evt)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous column.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollWinLineUp: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinLineUp(evt)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page column.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollWinPageDown: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinPageDown(evt)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page column.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollWinPageUp: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinPageUp(evt)

    #-----------------------------------------------------------------------

    def tsOnHScrollWinThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnHScrollWinTop: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnHScrollWinTop(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWin(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinBottom: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinBottom(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineDown(self, evt):
        '''
        Set scroll position to next row.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinLineDown: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinLineDown(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinLineUp(self, evt):
        '''
        Set scroll position to previous row.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinLineUp: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinLineUp(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageDown(self, evt):
        '''
        Set scroll position to next page row.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinPageDown: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinPageDown(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinPageUp(self, evt):
        '''
        Set scroll position to previous page row.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinPageUp: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinPageUp(evt)

    #-----------------------------------------------------------------------

    def tsOnVScrollWinThumbRelease(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolled.' +\
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
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsOnVScrollWinTop: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)
        else:

            self.ts_ChildForText.tsOnVScrollWinTop(evt)

    #-----------------------------------------------------------------------

    def tsScrolledLayout(self,
                         parent,
                         pos=wx.DefaultPosition,
                         size=wx.DefaultSize,
                         style=wx.HSCROLL | wx.VSCROLL,
                         name=wx.ScrolledNameStr,
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

            self.tsScrolledFeatureLayout(self.ts_ClientRect,
                                         style=style)

        return (self.ts_Rect, self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def tsScrolledFeatureLayout(self, clientRect, style):
        '''
        Calculate position and size of Scroll Bar features based upon
        arguments.
        '''
        parent = self

        if False and DEBUG:
            fmt1 = 'tsScrolledFeatureLayout: '
            fmt2 = 'parent=%s; ' % parent
            fmt3 = 'clientRect=%s; ' % str(clientRect)
            fmt4 = 'style=0x%X' % style
            msg = fmt1 + fmt2 + fmt3 + fmt4
            print('NOTICE: %s\n' % msg)

        if wx.ThemeToUse['ScrollBar']['Overlap']:

            overlapHorizontal = 1 * wx.pixelWidthPerCharacter
            overlapVertical = 1 * wx.pixelHeightPerCharacter

        else:

            overlapHorizontal = 0
            overlapVertical = 0

        if (((style & wx.SB_HORIZONTAL) or (style & wx.HSCROLL)) and \
            (not ((style & wx.SP_VERTICAL) or (style & wx.VSCROLL)))):

            # Horizontal Scroll Bar (wider without Vertical Scroll Bar)
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

            if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

                horizontalScrollBarThicknessRows = 3
                verticalScrollBarThicknessCols = 0

            else:

                horizontalScrollBarThicknessRows = 1
                verticalScrollBarThicknessCols = 0

            childForDualScrollBarAlignment = None

            childForText = wxScrolledText(
                parent,
                id=wx.ID_ANY,
                value=self.ts_Label,
                pos=(self.tsRoundHorizontal(clientRect.x),
                     self.tsRoundVertical(clientRect.y)),
                size=(self.tsRoundHorizontal(
                    clientRect.width - (
                        verticalScrollBarThicknessCols * \
                        wx.pixelWidthPerCharacter)),
                      self.tsRoundVertical(
                          clientRect.height - (
                              horizontalScrollBarThicknessRows * \
                              wx.pixelHeightPerCharacter))),
                style=wx.BORDER_SIMPLE,
                name=wx.ScrolledTextNameStr)

            childForHorizontalScrollBar = wxScrollBar(
                parent,
                id=wx.ID_ANY,
                pos=(self.tsRoundHorizontal(clientRect.x),
                     self.tsRoundVertical(
                         clientRect.y + \
                         clientRect.height - (
                             horizontalScrollBarThicknessRows * \
                             wx.pixelHeightPerCharacter))),
                size=(self.tsRoundHorizontal(clientRect.width - (
                    verticalScrollBarThicknessCols * \
                    wx.pixelWidthPerCharacter)),
                      self.tsRoundVertical(
                          (horizontalScrollBarThicknessRows * \
                           wx.pixelHeightPerCharacter))),
                style=wx.SB_HORIZONTAL,
                # validator=wx.DefaultValidator,
                name=wx.HorizontalScrollBarNameStr)

            childForVerticalScrollBar = None

        elif (((style & wx.SP_VERTICAL) or (style & wx.VSCROLL)) and \
              (not ((style & wx.SB_HORIZONTAL) or (style & wx.HSCROLL)))):

            # Vertical Scroll Bar (higher without Horizontal Scroll Bar)
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

            if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

                horizontalScrollBarThicknessRows = 0
                verticalScrollBarThicknessCols = 3

            else:

                horizontalScrollBarThicknessRows = 0
                verticalScrollBarThicknessCols = 1

            childForDualScrollBarAlignment = None

            childForHorizontalScrollBar = None

            childForText = wxScrolledText(
                parent,
                id=wx.ID_ANY,
                value=self.ts_Label,
                pos=(self.tsRoundHorizontal(clientRect.x),
                     self.tsRoundVertical(clientRect.y)),
                size=(self.tsRoundHorizontal(clientRect.width - (
                    verticalScrollBarThicknessCols * \
                    wx.pixelWidthPerCharacter)),
                      self.tsRoundVertical(clientRect.height + (
                          (horizontalScrollBarThicknessRows * \
                           wx.pixelHeightPerCharacter)))),
                style=wx.BORDER_SIMPLE,
                name=wx.ScrolledTextNameStr)

            childForVerticalScrollBar = wxScrollBar(
                parent,
                id=wx.ID_ANY,
                pos=(self.tsRoundHorizontal(clientRect.x + clientRect.width - \
                                            (verticalScrollBarThicknessCols * \
                                             wx.pixelWidthPerCharacter)),
                     self.tsRoundVertical(clientRect.y)),
                size=(self.tsRoundHorizontal(verticalScrollBarThicknessCols * \
                                             wx.pixelWidthPerCharacter),
                      self.tsRoundVertical(
                          clientRect.height - (
                              horizontalScrollBarThicknessRows * \
                              wx.pixelHeightPerCharacter))),
                style=wx.SB_VERTICAL,
                # validator=wx.DefaultValidator,
                name=wx.VerticalScrollBarNameStr)

        else:

            # Both Horizontal (narrower) & Vertical (shorter) Scroll Bars
            ################################################################
            #               wxPython Style - Parent Rectangle              #
            # +--------------------------------------------------------+-+ #
            # | Client Rectangle - Top Left         scrollbar vertical |^| #
            # |                                                        +-+ #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        |#| #
            # |                                                        +-+ #
            # | scrollbar horizontal   Client Rectangle - Bottom Right |v| #
            # +-+----------------------------------------------------+-+-+ #
            # |<|####################################################|>| | #
            # +-+----------------------------------------------------+-+-+ #
            ################################################################

            if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

                horizontalScrollBarThicknessRows = 3
                verticalScrollBarThicknessCols = 3

            else:

                horizontalScrollBarThicknessRows = 1
                verticalScrollBarThicknessCols = 1

            childForDualScrollBarAlignment = wxPanel(
                parent,
                id=wx.ID_ANY,
                # label=self.ts_Label,
                pos=(self.tsRoundHorizontal(
                    clientRect.x + clientRect.width - \
                    (verticalScrollBarThicknessCols * \
                     wx.pixelWidthPerCharacter)),
                     self.tsRoundVertical(
                         clientRect.y + clientRect.height - (
                             horizontalScrollBarThicknessRows * \
                             wx.pixelHeightPerCharacter))),
                size=(self.tsRoundHorizontal(
                    verticalScrollBarThicknessCols * \
                    wx.pixelWidthPerCharacter),
                      self.tsRoundVertical(
                          horizontalScrollBarThicknessRows * \
                          wx.pixelHeightPerCharacter)),
                style=0, # Inhibit any distracting border.
                name=wx.PanelNameStr)
            childForDualScrollBarAlignment.ts_BackgroundColour = wx.ThemeToUse[
                'ScrollBar']['BackgroundColour'].lower()
            childForDualScrollBarAlignment.ts_ForegroundColour = wx.ThemeToUse[
                'ScrollBar']['ForegroundColour'].lower()

            childForText = wxScrolledText(
                parent,
                id=wx.ID_ANY,
                value=self.ts_Label,
                pos=(self.tsRoundHorizontal(clientRect.x),
                     self.tsRoundVertical(clientRect.y)),
                size=(self.tsRoundHorizontal(
                    clientRect.width - (
                        verticalScrollBarThicknessCols * \
                        wx.pixelWidthPerCharacter)),
                      self.tsRoundVertical(
                          clientRect.height - (
                              horizontalScrollBarThicknessRows * \
                              wx.pixelHeightPerCharacter))),
                style=wx.BORDER_SIMPLE,
                name=wx.ScrolledTextNameStr)

            childForHorizontalScrollBar = wxScrollBar(
                parent,
                id=wx.ID_ANY,
                pos=(self.tsRoundHorizontal(clientRect.x),
                     self.tsRoundVertical(
                         clientRect.y + \
                         clientRect.height - (
                             horizontalScrollBarThicknessRows * \
                             wx.pixelHeightPerCharacter))),
                size=(self.tsRoundHorizontal(clientRect.width - (
                    verticalScrollBarThicknessCols * \
                    wx.pixelWidthPerCharacter)),
                      self.tsRoundVertical(
                          (horizontalScrollBarThicknessRows * \
                           wx.pixelHeightPerCharacter))),
                style=wx.SB_HORIZONTAL,
                # validator=wx.DefaultValidator,
                name=wx.HorizontalScrollBarNameStr)

            childForVerticalScrollBar = wxScrollBar(
                parent,
                id=wx.ID_ANY,
                pos=(self.tsRoundHorizontal(
                    clientRect.x + clientRect.width - \
                    (verticalScrollBarThicknessCols * \
                     wx.pixelWidthPerCharacter)),
                     self.tsRoundVertical(
                         clientRect.y)),
                size=(self.tsRoundHorizontal(
                    verticalScrollBarThicknessCols * \
                    wx.pixelWidthPerCharacter),
                      self.tsRoundVertical(
                          clientRect.height - (
                              horizontalScrollBarThicknessRows * \
                              wx.pixelHeightPerCharacter))),
                style=wx.SB_VERTICAL,
                # validator=wx.DefaultValidator,
                name=wx.VerticalScrollBarNameStr)

        # Begin Scrolled Class Instance Variable Update
##        self.ts_TargetWindow = childForText
##        self.ts_xScrollLines = 0
##        self.ts_xScrollLinesPerPage = childForText.ClientRect.width // \
##                                      wx.pixelWidthPerCharacter
##        self.ts_xScrollPixelsPerLine = wx.pixelWidthPerCharacter
##        self.ts_xScrollPosition = 0
##        if (childForHorizontalScrollBar is None):
##            self.ts_xScrollingEnabled = False
##        else:
##            self.ts_xScrollingEnabled = True
##        self.ts_yScrollLines = 0
##        self.ts_yScrollLinesPerPage = childForText.ClientRect.height // \
##                                      wx.pixelHeightPerCharacter
##        self.ts_yScrollPixelsPerLine = wx.pixelHeightPerCharacter
##        self.ts_yScrollPosition = 0
##        if (childForVerticalScrollBar is None):
##            self.ts_yScrollingEnabled = False
##        else:
##            self.ts_yScrollingEnabled = True

        self.ts_ChildForDualScrollBarAlignment = childForDualScrollBarAlignment
        self.ts_ChildForHorizontalScrollBar = childForHorizontalScrollBar
        self.ts_ChildForText = childForText
        self.ts_ChildForVerticalScrollBar = childForVerticalScrollBar

        #-------------------------------------------------------------------

        if (not (childForText is None)):

            if (not (childForHorizontalScrollBar is None)):

                childForText.tsSetChildForHorizontalScrollBar(
                    childForHorizontalScrollBar.ts_ChildForHorizontalGauge)

            if (not (childForVerticalScrollBar is None)):

                childForText.tsSetChildForVerticalScrollBar(
                    childForVerticalScrollBar.ts_ChildForVerticalGauge)

        #-------------------------------------------------------------------

##        if ((self.Parent.ts_Style & wx.SB_HORIZONTAL) or \
##            (self.Parent.ts_Style & wx.HSCROLL)):

##            self.ts_ChildForText.ts_xScrollingEnabled = True

##        else:

##            self.ts_ChildForText.ts_xScrollingEnabled = False

##        if ((self.Parent.ts_Style & wx.SB_VERTICAL) or \
##            (self.Parent.ts_Style & wx.VSCROLL)):

##            self.ts_ChildForText.ts_yScrollingEnabled = True

##        else:

##            self.ts_ChildForText.ts_yScrollingEnabled = False

##        fmt1 = 'tsWxScrolled.__init__: '
##        fmt2 = 'xScrollingEnabled=%s; ' % str(self.ts_xScrollingEnabled)
##        fmt3 = 'yScrollingEnabled=%s; ' % str(self.ts_yScrollingEnabled)
##        msg = fmt1 + fmt2 + fmt3
##        self.logger.debug(msg)

##        self.Bind(EVT_COMMAND_LEFT_CLICK, self.tsOnLeftClick)
##        self.Bind(EVT_COMMAND_LEFT_DCLICK, self.tsOnLeftDClick)
##        self.Bind(EVT_COMMAND_RIGHT_CLICK, self.tsOnRightClick)

        if not (childForHorizontalScrollBar is None):

            self.ts_xScrollingEnabled = True

            source = childForHorizontalScrollBar
            self.Bind(EVT_HSCROLLWIN_BOTTOM,
                      self.tsOnHScrollWinBottom,
                      source.ts_ChildForRightArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_HSCROLLWIN_LINEDOWN,
                      self.tsOnHScrollWinLineDown,
                      source.ts_ChildForRightArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_HSCROLLWIN_LINEUP,
                      self.tsOnHScrollWinLineUp,
                      source.ts_ChildForLeftArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_HSCROLLWIN_PAGEDOWN,
                      self.tsOnHScrollWinPageDown,
                      source.ts_ChildForRightArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_HSCROLLWIN_PAGEUP,
                      self.tsOnHScrollWinPageUp,
                      source.ts_ChildForLeftArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_HSCROLLWIN_TOP,
                      self.tsOnHScrollWinTop,
                      source.ts_ChildForLeftArrow,
                      useSystemEventTable=True)

##          self.Bind(EVT_HSCROLLWIN,
##                    self.tsOnHScrollWin)
##          self.Bind(EVT_HSCROLLWIN_THUMBRELEASE,
##                    self.tsOnHScrollWinThumbRelease)
##          self.Bind(EVT_HSCROLLWIN_THUMBTRACK,
##                    self.tsOnHScrollWinThumbTrack)

        if ((not (childForText is None)) and \
            (not (childForVerticalScrollBar is None))):

            self.ts_yScrollingEnabled = True

            source = childForVerticalScrollBar
            self.Bind(EVT_VSCROLLWIN_BOTTOM,
                      self.tsOnVScrollWinBottom,
                      source.ts_ChildForDownArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_VSCROLLWIN_LINEDOWN,
                      self.tsOnVScrollWinLineDown,
                      source.ts_ChildForDownArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_VSCROLLWIN_LINEUP,
                      self.tsOnVScrollWinLineUp,
                      source.ts_ChildForUpArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_VSCROLLWIN_PAGEDOWN,
                      self.tsOnVScrollWinPageDown,
                      source.ts_ChildForDownArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_VSCROLLWIN_PAGEUP,
                      self.tsOnVScrollWinPageUp,
                      source.ts_ChildForUpArrow,
                      useSystemEventTable=True)
            self.Bind(EVT_VSCROLLWIN_TOP,
                      self.tsOnVScrollWinTop,
                      source.ts_ChildForUpArrow,
                      useSystemEventTable=True)

##          self.Bind(EVT_VSCROLLWIN,
##                    self.tsOnVScrollWin)
##          self.Bind(EVT_VSCROLLWIN_THUMBRELEASE,
##                    self.tsOnVScrollWinThumbRelease)
##          self.Bind(EVT_VSCROLLWIN_THUMBTRACK,
##                    self.tsOnVScrollWinThumbTrack)

        if not (childForText is None):

            fmt1 = 'tsWxScrolled.tsScrolledFeatureLayout: '
            fmt2 = 'assignedId=%d; ' % self.ts_AssignedId
            fmt3 = 'childForText=%d; ' % childForText.ts_AssignedId

            if (childForHorizontalScrollBar is None):

                fmt4 = 'HScrollBar=%s; ' % str(childForHorizontalScrollBar)

            else:

                fmt4 = 'HScrollBar=%d; ' % childForHorizontalScrollBar.ts_AssignedId
                childForHorizontalScrollBar.tsSetChildForText(childForText)

            if (childForVerticalScrollBar is None):

                fmt5 = 'VScrollBar=%s; ' % str(childForVerticalScrollBar)

            else:

                fmt5 = 'VScrollBar=%d; ' % childForVerticalScrollBar.ts_AssignedId

                childForVerticalScrollBar.tsSetChildForText(childForText)

            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            print('NOTICE: %s\n' % msg)

        # End Scrolled Class Instance Variable Update

        return (self.ts_Rect, self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def tsSet_AutoScrolling(self, value=False):
        '''
        Set the AutoScrolling status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_AutoScrolling: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_AutoScrolling = value

    #-----------------------------------------------------------------------

    def tsSet_MaxTextCols(self, value=0):
        '''
        Set the MaxTextCols status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_MaxTextCols: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_MaxTextCols = value

    #-----------------------------------------------------------------------

    def tsSet_MaxTextRows(self, value=0):
        '''
        Set the MaxTextRows status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_MaxTextRows: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_MaxTextRows = value

    #-----------------------------------------------------------------------

    def tsSet_Retained(self, value=False):
        '''
        Set the Retained status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_Retained: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_Retained = value

    #-----------------------------------------------------------------------

    def tsSet_ScrolledTextLines(self, value=0):
        '''
        Set the ScrolledTextLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_ScrolledTextLines: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_ScrolledTextLines = value

    #-----------------------------------------------------------------------

    def tsSet_TargetWindow(self, value=None):
        '''
        Set the TargetWindow status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_TargetWindow: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_TargetWindow = value

    #-----------------------------------------------------------------------

    def tsSet_ViewStart(self, value=False):
        '''
        Set the ViewStart status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_ViewStart: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_ViewStart = value

    #-----------------------------------------------------------------------

    def tsSet_xScrollLines (self, value=0):
        '''
        Set the xScrollLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_xScrollLines: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_xScrollLines = value

    #-----------------------------------------------------------------------

    def tsSet_xScrollLinesPerPage(self, value=0):
        '''
        Set the xScrollLinesPerPage status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_xScrollLinesPerPage: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_xScrollLinesPerPage = value

    #-----------------------------------------------------------------------

    def tsSet_xScrollPixelsPerLine(self, value=0):
        '''
        Set the xScrollPixelsPerLine status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_xScrollPixelsPerLine: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_xScrollPixelsPerLine = value

    #-----------------------------------------------------------------------

    def tsSet_xScrollPosition(self, value=0):
        '''
        Set the xScrollPosition status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_xScrollPosition: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_xScrollPosition = value

    #-----------------------------------------------------------------------

    def tsSet_xScrollingEnabled(self, value=False):
        '''
        Set the xScrollingEnabled status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_xScrollingEnabled: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_xScrollingEnabled = value

    #-----------------------------------------------------------------------

    def tsSet_yScrollLines(self, value=0):
        '''
        Set the yScrollLines status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_yScrollLines: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_yScrollLines = value

    #-----------------------------------------------------------------------

    def tsSet_yScrollLinesPerPage(self, value=0):
        '''
        Set the yScrollLinesPerPage status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_yScrollLinesPerPage: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_yScrollLinesPerPage = value

    #-----------------------------------------------------------------------

    def tsSet_yScrollPixelsPerLine(self, value=0):
        '''
        Set the yScrollPixelsPerLine status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_yScrollPixelsPerLine: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_yScrollPixelsPerLine = value

    #-----------------------------------------------------------------------

    def tsSet_yScrollPosition(self, value=0):
        '''
        Set the yScrollPosition status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_yScrollPosition: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_yScrollPosition = value

    #-----------------------------------------------------------------------

    def tsSet_yScrollingEnabled(self, value=False):
        '''
        Set the yScrollingEnabled status of tsWxScrolledText.
        '''
        if self.ts_ChildForText is None:

            self.logger.error(
                'tsWxScrolled.tsSet_yScrollingEnabled: ' + \
                'self.ts_ChildForText=%s' % self.ts_ChildForText)

        else:

            self.ts_ChildForText.ts_yScrollingEnabled = value

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Scrolled Window specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            # label=self.ts_Label,
                            # value=self.ts_Text,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.Name,
                            pixels=True)
            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

            featureList = [self.ts_ChildForDualScrollBarAlignment,
                           self.ts_ChildForHorizontalScrollBar,
                           self.ts_ChildForText,
                           self.ts_ChildForVerticalScrollBar]

            for feature in featureList:

                if not (feature is None):

                    feature.tsShow()

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Scrolled Window.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()
                if self.tsIsBorderStyle(style=self.ts_Style):
                    self.tsCreateLabel()

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

##    def tsUpdateScrolledText(self):
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
##        self.ts_ChildForText.tsUpdateText()

##        firstCol = 0
##        lastCol = 0
##        maxCols = 0
##        if not (self.ts_ChildForHorizontalScrollBar is None):
##            myHScrollBar = self.ts_ChildForHorizontalScrollBar
##            myHScrollGauge = myHScrollBar.ts_ChildForHorizontalGauge
##            myHScrollUpdate = myHScrollGauge.tsUpdateHorizontalGauge
##            myHScrollUpdate(firstCol, lastCol, maxCols)

##        firstRow = 0
##        lastRow = 0
##        maxRows = 0
##        if not (self.ts_ChildForVerticalScrollBar is None):
##            myVScrollBar = self.ts_ChildForVerticalScrollBar
##            myVScrollGauge = myVScrollBar.ts_ChildForVerticalGauge
##            myVScrollUpdate = myVScrollGauge.tsUpdateVerticalGauge
##            myVScrollUpdate(firstRow, lastRow, maxRows)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    # Properties (global data shared amongst Scrolled children)
    AutoScrolling = property(tsGet_AutoScrolling, tsSet_AutoScrolling)
    MaxTextCols = property(tsGet_MaxTextCols, tsSet_MaxTextCols)
    MaxTextRows = property(tsGet_MaxTextRows, tsSet_MaxTextRows)
    Retained = property(tsGet_Retained, tsSet_Retained)
    ScaleX = property(tsGet_ScaleX)
    ScaleY = property(tsGet_ScaleY)
    ScrolledTextLines = property(
        tsGet_ScrolledTextLines, tsSet_ScrolledTextLines)
    TargetWindow = property(tsGet_TargetWindow, tsSet_TargetWindow)
    ViewStart = property(tsGet_ViewStart)
    xScrollLines = property(tsGet_xScrollLines, tsSet_xScrollLines)
    xScrollLinesPerPage = property(
        tsGet_xScrollLinesPerPage, tsSet_xScrollLinesPerPage)
    xScrollPixelsPerLine = property(
        tsGet_xScrollPixelsPerLine, tsSet_xScrollPixelsPerLine)
    xScrollPosition = property(tsGet_xScrollPosition, tsSet_xScrollPosition)
    xScrollingEnabled = property(
        tsGet_xScrollingEnabled, tsSet_xScrollingEnabled)
    yScrollLines = property(tsGet_yScrollLines, tsSet_yScrollLines)
    yScrollLinesPerPage = property(
        tsGet_yScrollLinesPerPage, tsSet_yScrollLinesPerPage)
    yScrollPixelsPerLine = property(
        tsGet_yScrollPixelsPerLine, tsSet_yScrollPixelsPerLine)
    yScrollPosition = property(tsGet_yScrollPosition, tsSet_yScrollPosition)
    yScrollingEnabled = property(
        tsGet_yScrollingEnabled, tsSet_yScrollingEnabled)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
