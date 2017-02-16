#! /usr/bin/env python
# "Time-stamp: <07/14/2015 12:23:53 AM rsg>"
'''
tsWxEventLoop.py - Class uses the Standard Python Curses API to
receive keyboard and mouse events. It maps those events into
wxPython equivalent ones. It enhances the Low Level Standard
Python Curses API by scanning the stack of wxPython GUI objects
and identifying which one was visible enough to trigger the
event. It dispatch th event to the appropriate wxPython event
handler.
'''
#################################################################
#
# File: tsWxEventLoop.py
#
# Purpose:
#
#    Class uses the Standard Python Curses API to receive key-
#    board and mouse events. It maps those events into wxPython
#    equivalent ones. It enhances the Low Level Standard Python
#    Curses API by scanning the stack of wxPython GUI objects
#    and identifying which one was visible enough to trigger the
#    event. It dispatch th event to the appropriate wxPython event
#    handler.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEventLoop import EventLoop
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#    See \WR\wxWidgets-2.8.10\src\common\eventloop.cpp
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    1. Keyboard input event support subject to restrictions:
#
#       a) Apple "Cmd" (Command) Not supported on computer platforms
#          running Mac OS X, Linux or Windows.
#
#       b) Only "character" events supported; "key" press/release events Not
#          supported.
#
#       c) Only "Shift", "Ctrl" or"Alt" key can be pressed in combination with
#          a character key; combinations of "Shift", "Ctrl" and "Alt" keys are
#          Not supported. (Note: The "Alt" key event internally involves two
#          separate "ncurses" getchar operations.)
#
#    2. Mouse input event support subject to restrictions:
#
#       a) Linux (Debian-based Ubuntu 14.04) supports mouse input
#          with xterm and vt100-family emulators under its Terminal
#          application. The vt100-family supports only:
#             EVT_COMMAND_LEFT_CLICK (but not EVT_COMMAND_LEFT_DCLICK)
#             EVT_COMMAND_RIGHT_CLICK (but not EVT_COMMAND_RIGHT_DCLICK)
#
#       b) Linux (Red Hat-based Fedora 22) supports mouse input with xterm
#          and vt100-family emulators under its Terminal application.
#
#       c) Microsoft Windows (XP, 7, 8, 8.1 10) only with Red Hat-based
#          Cygwin supports mouse input with xterm and vt100-family emulators
#          under its Mintty or X11 Terminal applications.
#
#       d) Unix (Darwin-based Apple Mac OS X 10.10) supports mouse input
#          only with xterm under third-party iTerm2 Terminal application.
#          It does not support mouse input with vt100-family emulators.
#
#       e) Unix (FreeBSD-based PC-BSD 10.1) does not support mouse input
#          with vt100-family emulators under its Terminal application.
#          It does support mouse input with term-family emulators.
#
#       f) Unix (Solaris-based OpenIndiana 151a8) might not support mouse
#          input with vt100-family emulators under its Terminal application.
#          It does support mouse input with term-family emulators.
#
# Notes:
#
#    From "wxPython in Action" by Noel Rappin and Robin Dunn, Copyright 2006
#    by Manning Publications Co., 209 Bruce Park Avenue, Greenwich, CT 06830
#    Section 3.2 - What is event-driven programming?
#
#    During debugging of vt100 and vt220 unexpected mouse interrupts were
#    received. A Google search of "http://invisible-island.net/xterm/"
#    produced the explanation that Thomas E. Dickey had enhanced nCurses
#    to include more control featres of DEC vt200 terminals.
#
#    Capturing "input" data revealed that one could extract mouse position
#    and some button data (which button was operated with both pressed and
#    released states but without single, double and tripple click info.
#    The tsGetGraphicalUserInput method was then modified to simulate the
#    normal xterm-style mouse input processing.
#
#    Initial testing of the xterm-style mouse input worked on all
#    Python Curses compatible systems:
#
#                                      XTerm/            iTerm2 App for 
#    Host & Mouse    Terminal App       UXTerm App             Mac OS X
#    ============    ==============    ==============    ==============
#    Linux,       |  xterm             xterm             xterm
#                 |
#    Mac OS X,    |  xterm-color       xterm-color       xterm-color
#                 |
#    MS Windows   |  xterm-16color     xterm-16color     xterm-16color
#    XP, 7, 8, 10 |
#    with Cygwin, |  xterm-88color     xterm-88color     xterm-88color
#                 |
#    Unix         |  xterm-256color    xterm-256color    xterm-256color
#
#    Initial testing of the vt100/vt220 style mouse input worked only on
#    Linux compatible systems:
#
#                          Terminal App/     XTerm/            iTerm2 App for 
#    Host & Mouse           Cygwin Mintty     UXTerm App             Mac OS X
#    ====================  ==============    ==============    ==============
#    Linux CentOS 7.0      vt100/vt220       vt100/vt220
#
#    Linux Fedora 22       vt100/vt220       vt100/vt220       ---- N/A -----
#
#    Linux Scientific 7.0  vt100/vt220       vt100/vt220       ---- N/A -----
#
#    Linux Ubuntu 14.04    vt100/vt220       vt100/vt220       ---- N/A -----
#
#    Mac OS X              ---- N/A -----    ---- N/A -----    ---- N/A -----
#
#    MS Windows            vt100/vt220       ---- N/A -----    ---- N/A -----
#    XP, 7, 8, 10
#    with Cygwin
#
#    Unix PC-BSD 10.1      ---- N/A -----    ---- N/A -----    ---- N/A -----
#
#    Unix Solaris 11       ---- N/A -----    ---- N/A -----    ---- N/A -----
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
#    2010/09/28 rsg Modified method tsKeyboardEventGenerator to
#                   set and log returned character and flags.
#                   Under Cygwin on Windows XP, successfully distinguishes:
#                   lower case 'l' as normal 'l',
#                   upper case 'L' as shifted 'l',
#                   ctrl 'l' or ctrl 'L' as ctrl 'L',
#                   alt 'l' or 'L' as alt 'L'.
#                   Does not detect activity for 'alt-ctl' combination.
#                   Parallels crashes for 'cmd' 'l' or 'L' combination.
#
#    2010/12/15 rsg Modified "tsMouseEventGeneratortor" to pass Event,
#                   instead of PyEventBinder, type parameter to
#                   "ProcessEvent". Modification ensures that event
#                   handlers have access to the methods and instance
#                   variables associated with the "Event" class.
#
#    2010/12/19 rsg Corrected "ProcessEvent". Replaced "PyEventBinder"
#                   with traditional "Event" parameter.
#
#    2012/01/15 rsg Added white space to improve readability in
#                   preparation for changes to support dynamic
#                   overlays instead of static order of show.
#
#    2012/01/20 rsg Revised overlay comment in tsGetGraphicalUserInput.
#
#    2012/01/22 rsg Added tsUpdatePanelStack and reference in
#                   tsScanForTopMostWindow.
#
#    2012/01/25 rsg Conditionalized tsScanForTopMostWindow based on
#                   wx.USE_CURSES_PANEL_STACK. If False, it calla
#                   tsScanOrderOfShowForTopMostWindow. If True, it
#                   calls tsScanPanelStackForTopMostWindow.
#
#    2012/01/25 rsg Modified tsUpdatePanelStack to register each
#                   windowAssignedId in an orderOfShowPanelStack
#                   list.
#
#    2012/02/05 rsg Modified tsThisIsTriggeringEvent to support
#                   tsWxScrollBarButton events:
#                   EVT_COMMAND_LEFT_CLICK
#                   EVT_COMMAND_LEFT_DCLICK
#                   EVT_COMMAND_RIGHT_CLICK
#                   EVT_LEFT_DCLICK
#                   EVT_LEFT_DOWN
#                   EVT_LEFT_UP
#                   EVT_MIDDLE_DCLICK
#                   EVT_MIDDLE_DOWN
#                   EVT_MIDDLE_UP
#                   EVT_MOTION
#                   EVT_RIGHT_DCLICK
#                   EVT_RIGHT_DOWN
#                   EVT_RIGHT_UP
#
#    2012/02/06 rsg Resolved pylint error by modifying IsMain method
#                   by replacing references to "wxTheApp" by
#                   references to "wx.App.wxTheApp".
#
#    2012/02/11 rsg Re-designed tsProcessSelectedEventTable.
#
#    2012/02/12 rsg Added MouseTriggeringEventMap and MouseEventOptionMap.
#
#    2012/02/12 rsg Conditionalized-out DEBUG statements in
#                   tsUpdatePanelStack.
#
#    2012/02/21 rsg Replaced reference to tsProcessSelectedEventTable by
#                   reference to tsProcessEventTables.
#
#    2012/05/20 rsg Resolved trap for exceeding recursion stack depth by
#                   modifying tsScanDescendantOrderOfShowForTopMostWindow
#                   logic from "for aWindowId in
#                   "reversed(anAncestor.ts_DescendantOrderOfShow)" to
#                   "reversed(sorted(anAncestor.ts_DescendantOrderOfShow))".
#                   This resolved mouse click event processing associated
#                   with tsWxScrolledWindow arrow buttons.
#
#    2012/05/21 rsg Added self.ts_LastCursesGetMouseTuple to support
#                   passing mouse position via process event tables.
#
#    2012/05/31 rsg Modified tsKeyboardEventGenerator, tsMouseEventGenerator
#                   and tsTimeoutEventGenerator to conform to the wxPython
#                   style immediate and/or delayed event processing.
#                   Modifications revised logic to encode parameters into
#                   the wxPython event container and then returned the
#                   container to PyApp instead of immediately scanning for
#                   and then dispatching control to the associated event
#                   handler.
#
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
#    2012/06/24 rsg Added logic to tsThisIsTriggeringEvent that sets
#                   EventData with mouse mouseId, x, y, z, bstate.
#                   Also, invoked lower() to correct comparison of
#                   triggeringObject.ts_ClassName.lower() with
#                   wx.ScrollBarGaugeNameStr.lower().
#
#    2012/07/19 rsg Revised logic for tsKeyboardEventGenerator to
#                   support bypassEventProcessingMode.
#
#    2012/07/21 rsg Revised logic for tsKeyboardEventGenerator to
#                   support event driven equivalent of curses.textpad.
#
#    2012/07/27 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#
#    2013/07/12 rsg Added reference to wx.ENABLE_CURSES_RESIZE in
#                   tsKeyboardEventGenerator and logic to
#                   raise tse.UserInterfaceException(
#                       tse.GRAPHICAL_WINDOW_RESIZED, msg)
#
#    2013/08/28 rsg Corrected the statement of purpose.
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
#                   "from _curses import error" as _cursesErrorMethod
#
#    2014/07/11 rsg Added attribute 'WindowsByCursesPanel' to
#                   'GraphicalTextUserInterface' and modified
#                   'start' to facilitate use of curses panel object
#                   id for anticipated use, by 'tsWxEventLoop',
#                   to determine the associated wxPython object
#                   id and curses panel stacking order.
#
#    2015/06/23 rsg Added import of platform and string libraries.
#
#                   Added method "tsVT100MouseEventGenerator".
#
#                   Modified the "tsGetGraphicalUserInput" method to
#                   capture mouse input data for vt100/vt220.
#
#                   Added logic to convert 12 sequential vt100/vt220
#                   mouse input data into a single xterm-type format
#                   before initiating the mouse event generation and
#                   reporting processes.
#
#    2015/07/05 rsg Revised method "tsVT100MouseEventGenerator".
#                   Added missing "int(" to "vt100State[5]" and
#                   "vt100State[6]) with balancing ")" for con-
#                   sistancy.
#
#    2015/07/14 rsg Revised methods "tsMouseEventGenerator" and
#                   "tsVT100MouseEventGenerator". Added logic to
#                   inhibit event generation if Curses STDSCR
#                   lacks an associated wxPython GUI Object.
#
# ToDo:
#
#    2011/12/31 rsg Translate Ncurses key names to wxPython key names.
#
#    2012/01/20 rsg Review timing (beginning or end) of overlay update
#                   in tsGetGraphicalUserInput.
#
#    2012/01/27 rsg Troubleshoot why the AssignedId (106) for
#                   the screen is found in the "OrderOfShow" list
#                   but not in the "OrderOfShowPanelStack" list
#                   as reported by the tsUpdatePanelStack method
#                   during the run of test_tsWxWidgets.py. Also
#                   missing are AssignedId's for the TaskBar (111),
#                   a Frame (113), a Frame (128) and for the
#                   Communicate Frame (153).
#
#    2012/01/27 rsg Merge tsScanOrderOfShowForTopMostWindow and
#                   tsScanPanelStackForTopMostWindow into
#                   tsScanForTopMostWindow if there remain only
#                   a few conditionizable differences in the
#                   final design. As of this date, the display
#                   of foreground object do not change with panel
#                   stack shuffling.
#
#    2012/05/20 rsg Investigate the feasibility of passing mouse
#                   position via process event tables so that
#                   tsWxScrollBar gauge can be used to position
#                   the data dsplayed by tsWxScrolledText.
#                   NOTE: Criteria is passed internnally between
#                   tsWxEventLoop methods but is not currently
#                   passed as part of event notification. Perhaps
#                   data could be added to event notification's
#                   argument list.
#
#    2012/06/05 rsg Investigate techniques to accumulate window-
#                   specific keyboard input that can be edited
#                   before delivery.
#
#    2013/07/12 rsg Troubleshoot exception processing associated
#                   with raise tse.UserInterfaceException(
#                       tse.GRAPHICAL_WINDOW_RESIZED, msg)
#
#################################################################

__title__     = 'tsWxEventLoop'
__version__   = '1.13.0'
__date__      = '07/14/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

import copy
import curses
from curses import ascii
from curses import error as cursesErrorMethod
from curses import panel
from curses import textpad
from curses import wrapper
import _curses
from _curses import error as _cursesErrorMethod

import platform
import string
##import sys
import time
## import types
## import Queue

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py3x.tsLibGUI.tsWxDoubleLinkedList import \
     DoubleLinkedList as wxDoubleLinkedList
from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py3x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect

##### Begin Events not defined in module tsWxEvent
## from tsWxEvent import EVT_MIDDLE_CLICK
## from tsWxEvent import EVT_MIDDLE_TCLICK
## from tsWxEvent import EVT_RIGHT_CLICK
## from tsWxEvent import EVT_RIGHT_TCLICK
## from tsWxEvent import wxEVT_COMMAND_LEFT_TCLICK
## from tsWxEvent import wxEVT_COMMAND_RIGHT_TCLICK
##### End Events not defined in module tsWxEvent

##from tsWxEvent import Event
##from tsWxEvent import wxEVENT_PROPAGATE_MAX
##from tsWxEvent import wxEVENT_PROPAGATE_NONE

##from tsWxEvent import wxEVT_CATEGORY_TIMER
##from tsWxEvent import wxEVT_CATEGORY_USER_INPUT

##from tsWxEvent import wxEVT_CHAR
##from tsWxEvent import wxEVT_COMMAND_TEXT_ENTER
##from tsWxEvent import wxEVT_TIMER

##from tsWxEvent import EVT_CHAR
##from tsWxEvent import EVT_TIMER

##from tsWxEvent import EVT_COMMAND_LEFT_CLICK
##from tsWxEvent import EVT_COMMAND_LEFT_DCLICK
##from tsWxEvent import EVT_COMMAND_RIGHT_CLICK
##from tsWxEvent import EVT_COMMAND_RIGHT_DCLICK
##from tsWxEvent import EVT_COMMAND_SET_FOCUS
##from tsWxEvent import EVT_LEFT_DOWN
##from tsWxEvent import EVT_LEFT_UP
##from tsWxEvent import EVT_MIDDLE_DCLICK
##from tsWxEvent import EVT_MIDDLE_DOWN
##from tsWxEvent import EVT_MIDDLE_UP
##from tsWxEvent import EVT_MOUSEWHEEL
##from tsWxEvent import EVT_NULL
##from tsWxEvent import EVT_RIGHT_DCLICK
##from tsWxEvent import EVT_RIGHT_DOWN
##from tsWxEvent import EVT_RIGHT_UP
##from tsWxEvent import wxEVT_CATEGORY_ALL

##from tsReportUtilities import TsReportUtilities as tsrpu
##from tsWxButton import Button as wxButton
## from tsWxEventLoop import EventLoop as wxEventLoop
##from tsWxEvtHandler import EvtHandler
##from tsWxTaskBar import TaskBar as wxTaskBar
##from tsWxPoint import Point as wxPoint
##from tsWxRect import Rect as wxRect
##from tsWxScreen import Screen as wxScreen
##from tsWxWindow import Window

tsWxGTUI_DataBase = tsGTUI.GraphicalTextUserInterface

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DEBUG_MOUSE = True

bypassEventProcessingMode = True

# Derived from default window names in tsWxGlobals.
# However, case reflects usage in class definitation files.
firstCallerClassNames = list(wx.indentation.keys())

#---------------------------------------------------------------------------

# Map of Mouse Button/Wheel State Changes and associated triggering events.
MouseTriggeringEventMap = {
    'LeftClicked':    EVT_COMMAND_LEFT_CLICK,
    'LeftDClicked':   EVT_COMMAND_LEFT_DCLICK,
    'LeftDown':       EVT_LEFT_DOWN,
    'LeftTClicked':   None, # EVT_COMMAND_LEFT_TCLICK
    'LeftUp':         EVT_LEFT_UP,
    'MiddleClicked':  None, # EVT_MIDDLE_CLICK
    'MiddleDClicked': EVT_MIDDLE_DCLICK,
    'MiddleDown':     EVT_MIDDLE_DOWN,
    'MiddleTClicked': None, # EVT_MIDDLE_TCLICK
    'MiddleUp':       EVT_MIDDLE_UP,
    'RightClicked':   EVT_COMMAND_RIGHT_CLICK,
    'RightDClicked':  EVT_RIGHT_DCLICK,
    'RightDown':      EVT_RIGHT_DOWN,
    'RightTClicked':  None, # EVT_RIGHT_TCLICK
    'RightUp':        EVT_RIGHT_UP,
    'WheelClicked':   None, # EVT_MOUSEWHEEL,
    'WheelDClicked':  None, # EVT_MOUSEWHEEL,
    'WheelDown':      None, # EVT_MOUSEWHEEL,
    'WheelTClicked':  None, # EVT_MOUSEWHEEL,
    'WheelUp':        None  # EVT_MOUSEWHEEL,
}

#---------------------------------------------------------------------------

# Map of Mouse Event Options.
MouseEventOptionMap = {
    'AltDown':  None,
    'CmdDown':  None,
    'CtrlDown': None
}

#---------------------------------------------------------------------------

class EventLoop(object):
    '''
    Base class for all event loop implementations.

    An event loop is a class which queries the queue of native events sent
    to the wxWidgets application and dispatches them to the appropriate
    wxEvtHandlers.

    An object of this class is created by wxAppTraits::CreateEventLoop() and
    used by wxApp to run the main application event loop. Temporary event
    loops are usually created by wxDialog::ShowModal().

    You can create your own event loop if you need, provided that you restore
    the main event loop once yours is destroyed (see wxEventLoopActivator).
    '''
    # Class Variables:

    ts_Active = None
    ts_EscapeActive = False

    #-----------------------------------------------------------------------

    def __init__(self, parent=None):
        '''
        '''
        theClass = 'EventLoop'

        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

        self.ts_Parent = parent

        if parent is None:

            self.logger = tsLogger.TsLogger(
                threshold=tsLogger.ERROR,
                start=time.time(),
                name=tsLogger.StandardOutputFile)

            msg = 'NotImplementedError: %s' % '__init__ in tsWxEventLoop'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            self.logger = parent.logger
            self.stdscr = parent.stdscr
            self.ts_theTerminal = parent.ts_theTerminal
            self.ts_TheWindows = parent.ts_TheWindows
            self.ts_WindowsByAssignedId = parent.ts_WindowsByAssignedId

        self.ts_Active = EventLoop.ts_Active
        self.ts_IdleTimeQueue = wxDoubleLinkedList(lifoMode=False)
        self.ts_LastCursesGetMouseTuple = None
        self.ts_MouseLastXYZ = (-1, -1, -1)
        self.ts_RealTimeQueue = wxDoubleLinkedList(lifoMode=False)
        self.ts_EventsToProcessInsideYield = wxEVT_CATEGORY_ALL
        self.ts_IsInsideYield = False
        self.ts_VT100_MouseState = []

        # Create reference to mouse button code dictionary.
        # ScanForInput requires removal of dictionary name from key list.
        self.ts_MouseButtonCodes = copy.deepcopy(
            tsGTUI.MouseButtonCodes)
        del self.ts_MouseButtonCodes['name']

        # TBD - Accumulate window-specific keyboard input
        #       that can be edited before delivery
        self.myChar = None

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def __del__(self):
##        '''
##        '''
##        del self

    #-----------------------------------------------------------------------

    def Dispatch(self):
        '''
        Dispatches the next event in the windowing system event queue.
        '''
        node = self.ts_RealTimeQueue.Pop()
        event = node.GetUserData()

        eventData = event.EventData
        eventType = event.EventType
        objectCriteria = event.EventCriteria
        objectId = event.EventSource.ts_AssignedId
        triggeringEvent = event
        triggeringObject = event.EventSource

##      print(dir(event))
##        print('tsWxEventLoop.Dispatch: ' + \
##              'Criteria=%s; Data=%s; Object%s; Timestamp=%s; Type%s' % (
##                  str(event.EventCriteria),
##                  str(event.EventData),
##                  str(event.EventSource),
##                  str(event.EventTimestamp),
##                  str(event.EventType)))

        if False and bypassEventProcessingMode:

##            theEvent = Event(
##                id=wx.ID_ANY,
##                callbackUserData=None,
##                canVeto=False,
##                eventCategory=wxEVT_CATEGORY_USER_INPUT,
##                eventCriteria=objectCriteria,
##                eventData=triggeringMouseTuple,
##                eventSource=triggeringObject,
##                eventType=triggeringEvent.eventType,
##    ##            eventType=triggeringEvent.ts_EventType,
##                isCommandEvent=False,
##                propagationLevel=wxEVENT_PROPAGATE_NONE,
##                skipped=False,
##                timeStamp=time.time(),
##                veto=False,
##                wasProcessed=False)

            results = self.tsProcessEventTables(
                objectCriteria=objectCriteria,
                objectId=objectId,
                triggeringEvent=triggeringEvent,
                triggeringObject=triggeringObject)

        else:

            self.tsProcessEventTables(
                objectCriteria=event.EventCriteria,
                objectId=event.EventSource.ts_AssignedId,
                triggeringEvent=event.EventType,
                triggeringObject=event.EventSource)

##        msg = 'NotImplementedError: %s' % 'Dispatch in tsWxEventLoop'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (True)

    #-----------------------------------------------------------------------

    def DispatchTimeout(self, timeout=0):
        '''
        Dispatch an event but not wait longer than the specified timeout
        for it.
        '''
##      self.ts_RealTimeQueue.TBD

        msg = 'NotImplementedError: %s' % 'DispatchTimeout in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (0)

    #-----------------------------------------------------------------------

    def Exit(self, rc):
        '''
        Exit from the loop with the given exit code.
        '''
        msg = 'NotImplementedError: %s' % 'Exit in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        pass

    #-----------------------------------------------------------------------

    @staticmethod
    def GetActive():
        '''
        Return the currently active (running) event loop.
        '''
##        msg = 'NotImplementedError: %s' % 'GetActive in tsWxEventLoop'
##        # self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        return (EventLoop.ts_Active)

    #-----------------------------------------------------------------------

    def IsEventAllowedInsideYield(self, wxEventCategory):
        '''
        Returns true if the given event category is allowed inside a
        YieldFor() call (i.e.
        '''
        msg = 'NotImplementedError: %s' % \
            'IsEventAllowedInsideYield in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (False)

    #-----------------------------------------------------------------------

    def IsMain(self):
        '''
        Returns true if this is the main loop executed by wxApp::OnRun().
        '''
        try:

            if (not (wx.App.wxTheApp is None)):
                return (wx.App.wxTheApp.GetMainLoop() == self)
            return (False)

        except Exception as isMainError:

            fmt1 = 'NotImplementedError: %s; ' % 'IsMain in tsWxEventLoop'
            fmt2 = 'Exeption: %s'
            msg = fmt1 + fmt2
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsOk(self):
        '''
        Use this to check whether the event loop was successfully
        created before using it.
        '''
        msg = 'NotImplementedError: %s' % 'IsOk in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (False)

    #-----------------------------------------------------------------------

    def IsRunning(self):
        '''
        Return true if this event loop is currently running.
        '''
        msg = 'NotImplementedError: %s' % 'IsRunning in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (False)

    #-----------------------------------------------------------------------

    def IsYielding(self):
        '''
        Returns true if called from inside Yield() or from inside YieldFor().
        '''
        msg = 'NotImplementedError: %s' % 'IsYielding in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (False)

    #-----------------------------------------------------------------------

    def OnExit(self):
        '''
        This function is called before the event loop terminates, whether
        this happens normally (because of Exit() call) or abnormally
        (because of an exception thrown from inside the loop).
        '''
        msg = 'NotImplementedError: %s' % 'OnExit in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        pass

    #-----------------------------------------------------------------------

    def Pending(self):
        '''
        Return true if any events are available.
        '''
        if self.ts_RealTimeQueue.GetCount() > 0:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def ProcessIdle(self):
        '''
        This virtual function is called when the application becomes idle
        and normally just sends wxIdleEvent to all interested parties.
        '''
##      self.ts_RealTimeQueue.TBD

        msg = 'NotImplementedError: %s' % 'ProcessIdle in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        pass

    #-----------------------------------------------------------------------

    def Run(self):
        '''
        Start the event loop, return the exit code when it is finished.
        '''
        msg = 'NotImplementedError: %s' % 'Run in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (0)

    #-----------------------------------------------------------------------

    @staticmethod
    def SetActive(loop):
        '''
        Set currently active (running) event loop.
        '''
##        msg = 'NotImplementedError: %s' % 'SetActive in tsWxEventLoop'
##        # self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        EventLoop.ts_Active = loop

    #-----------------------------------------------------------------------

    def WakeUp(self):
        '''
        Called by wxWidgets to wake up the event loop even if it is
        currently blocked inside Dispatch().
        '''
        msg = 'NotImplementedError: %s' % 'WakeUp in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        pass

    #-----------------------------------------------------------------------

    def WakeUpIdle(self):
        '''
        Makes sure that idle events are sent again.
        '''
        msg = 'NotImplementedError: %s' % 'WakeUpIdle in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        pass

    #-----------------------------------------------------------------------

    def Yield(self, onlyIfNeeded=False):
        '''
        Yields control to pending messages in the windowing system.
        '''
        msg = 'NotImplementedError: %s' % 'Yield in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (True)

    #-----------------------------------------------------------------------

    def YieldFor(self, eventsToProcess):
        '''
        Works like Yield() with onlyIfNeeded == true, except that it
        allows the caller to specify a mask of the wxEventCategory values
        which indicates which events should be processed and which should
        instead be "delayed" (i.e.
        '''
        msg = 'NotImplementedError: %s' % 'YieldFor in tsWxEventLoop'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (True)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetEventHandler(self, objectId, evt):
        '''
        '''
        topLevelId = self.ts_WindowsByAssignedId[
            objectId].ts_EarliestAncestor

        systemEventTable = self.ts_WindowsByAssignedId[
            topLevelId].ts_SystemEventTable[objectId] # [topLevelId]

##        msg = 'systemEventTable[%d]=%s' %(topLevelId, str(systemEventTable))
##        self.logger.debug('NOTICE: %s' % msg)
##        self.logger.debug(msg)

        msg = 'tsWxEventLoop.tsGetEventHandler: ' + \
            'topLevelId="%s"; objectId="%s"; evt="%s"' % (
                str(topLevelId), str(objectId), str(evt))
        self.logger.debug(msg)
        return (None)

    #-----------------------------------------------------------------------

    def tsGetGraphicalUserInput(self):
        '''
        Receive and categorize keyboard and mouse input. Identify target
        GUI object and generate the appropriate event notification.
        '''
        # Begin Overlay Show mechanism
        if wx.USE_CURSES_PANEL_STACK:
            # Updates the virtual screen after changes in the panel stack.
            # This does not call curses.doupdate(), so you will have to do
            # this yourself
            curses.panel.update_panels()
            curses.doupdate()
        # End Overlay Show mechanism

        # Refresh window info with latest info
        # Should lastest available come from tsWxPyApp or tsGTUI data base?
        if True:
            # Parent's private Data Base
            self.ts_TheWindows = self.ts_Parent.ts_TheWindows
            self.ts_WindowsByAssignedId = self.ts_Parent.ts_WindowsByAssignedId
        else:
            sharedDataBase = tsWxGTUI_DataBase
            self.ts_TheWindows = sharedDataBase.TheWindows
            self.ts_WindowsByAssignedId = sharedDataBase.WindowsByAssignedId

        # Get access to curses keyboard, mouse and display screen devices.
        window = self.stdscr.Stdscr

        # Get starting position and size of stdscr
        # in character (curses) units
        (begin_y, begin_x) = window.getbegyx()
        (max_y, max_x) = window.getmaxyx()

        # Convert starting position and size of stdscr
        # from character to pixel (wxPython) units
        (x, y) = wx.tsGetPixelValues(begin_x, begin_y)
        (width, height) = wx.tsGetPixelValues(max_x, max_y)

        # Build wxPython rectangle object
        stdscrPixelGrid = wxRect(x, y, width, height)

        # Note - Can only recognize mouse events via stdscr.
        # Children of stdscr can only interpret mouse events as indivudal
        # characters.
        ch = window.getch()

        # restore focus to window
        ## window.redrawwin()

        # Categorize keyboard and mouse input.
        if ch == tsGTUI.KEYBOARD_TIMEOUT:

            # Process a Timeout Event

            # Update data base logs
            if True:
                self.stdscr.tsPrintDataBases()

            theEvent = self.tsTimeoutEventGenerator()

        elif ch == curses.KEY_MOUSE:

            # Process a Mouse Event

            # Update data base logs
            if True:
                self.stdscr.tsPrintDataBases()

            theEvent = self.tsMouseEventGenerator(ch)

        elif self.ts_theTerminal.HasMouse:

            # Process a Key Event

            # Update data base logs
            if True:
                self.stdscr.tsPrintDataBases()

            theEvent = self.tsKeyboardEventGenerator(ch)

        elif len(self.ts_VT100_MouseState) < 12:

            # Process a derived vt100/vt220 Mouse Event
            # See: http://invisible-island.net/xterm/ctlseqs/ctlseqs.html

            if True: # string.find(platform.system(), 'CYGWIN') == 0:

                # Accelerate each set of vt100/vt220 Mouse input
                # by waiting in the following loop for individual
                # event notifications.
                for i in range(12):

                    self.ts_VT100_MouseState += [ch]

                    if DEBUG and False:
                        msg = 'tsWxEventLoop.tsGetGraphicalUserInput: ' + \
                              '\n\tMouse Input: ' + \
                              '"%s" (0x%x) expected for "%s".' % \
                              (str(ch), int(ch), tsWxGTUI_DataBase.TermName)

                        print('DEBUG: %s' % msg)
                        self.logger.debug(msg)

                    ch = window.getch()

            else: # True for non-Cygwin

                # Wait for individual vt100/vt220 Mouse input
                # by waiting in caller's loop for individual
                # event notifications.
                self.ts_VT100_MouseState += [ch]

                if DEBUG and False:
                    msg = 'tsWxEventLoop.tsGetGraphicalUserInput: ' + \
                          '\n\tMouse Input: "%s" (0x%x) expected for "%s".' % \
                          (str(ch), int(ch), tsWxGTUI_DataBase.TermName)

                    print('DEBUG: %s' % msg)
                    self.logger.debug(msg)

            if len(self.ts_VT100_MouseState) == 12:

                if DEBUG and False:
                    msg = 'tsWxEventLoop.tsGetGraphicalUserInput: ' + \
                          '\n\tts_VT100_MouseState: "%s".' % \
                          str(self.ts_VT100_MouseState)

                    print('DEBUG: %s' % msg)
                    self.logger.debug(msg)

                # Update data base logs
                if True:
                    self.stdscr.tsPrintDataBases()

                theEvent = self.tsVT100MouseEventGenerator(
                    self.ts_VT100_MouseState)
                self.ts_VT100_MouseState = []

        else:

            # Process an unexpected Mouse Event

            msg = 'tsWxEventLoop.tsGetGraphicalUserInput: ' + \
                  '\n\tMouse Input: "%s" (0x%x) NOT expected for "%s".' % \
                  (str(ch), int(ch), tsWxGTUI_DataBase.TermName)

            print('DEBUG: %s' % msg)
            self.logger.debug(msg)

    #-----------------------------------------------------------------------

    def tsIsThisTheMouseState(self, bstate, mask):
        '''
        '''
        if ((bstate & mask) == mask):
            match = True
        else:
            match = False
        return (match)

    #-----------------------------------------------------------------------

    def tsKeyboardEventGenerator(self, ch):
        '''
        TBD - Under Construction. Does not yet generate wxPython Key Names,
        Key Codes or Raw Key Codes.

        Categorize keyboard input. Identify target GUI object and generate
        the appropriate event notification.

        The event class contains information about keypress and character
        events. These events are only sent to the widget that currently has
        the keyboard focus.

        Notice that there are three different kinds of keyboard events in
        wxWidgets: key down and up events and char events. The difference
        between the first two is clear - the first corresponds to a key press
        and the second to a key release - otherwise they are identical. Just
        note that if the key is maintained in a pressed state you will
        typically get a lot of (automatically generated) down events but only
        one up so it is wrong to assume that there is one up event corres-
        ponding to each down one.

        Both key events provide untranslated key codes while the char event
        carries the translated one. The untranslated code for alphanumeric
        keys is always an upper case value. For the other keys it is one of
        WXK_XXX values from the keycodes table. The translated key is, in
        general, the character the user expects to appear as the result of
        the key combination when typing the text into a text entry zone, for
        example.

        A few examples to clarify this (all assume that CAPS LOCK is unpressed
        and the standard US keyboard): when the "A" key is pressed, the key
        down event key code is equal to ASCII A == 65. But the char event key
        code is ASCII a == 97. On the other hand, if you press both SHIFT and
        "A" keys simultaneously , the key code in key down event will still
        be just "A" while the char event key code parameter will now be "A"
        as well.

        Although in this simple case it is clear that the correct key code
        could be found in the key down event handler by checking the value
        returned by ShiftDown, in general you should use EVT_CHAR for this
        as for non alphanumeric keys or non-US keyboard layouts the
        translation is keyboard-layout dependent and can only be done
        properly by the system itself.

        Another kind of translation is done when the control key is pressed:
        for example, for CTRL-A key press the key down event still carries
        the same key code "A" as usual but the char event will have key code
        of 1, the ASCII value of this key combination.

        You may discover how the other keys on your system behave inter-
        actively by running the KeyEvents sample in the wxPython demo and
        pressing some keys while the blue box at the top has the keyboard
        focus.

        Note: If a key down event is caught and the event handler does not
        call event.Skip() then the coresponding char event will not happen.
        This is by design and enables the programs that handle both types
        of events to be a bit simpler.

        Note for Windows programmers: The key and char events in wxWidgets are
        similar to but slightly different from Windows WM_KEYDOWN and WM_CHAR
        events. In particular, Alt-x combination will generate a char event in
        wxWidgets (unless it is used as an accelerator).

        Tip: be sure to call event.Skip() for events that you do not process
        in key event function, otherwise menu shortcuts may cease to work under
        Windows.
        '''
        try:

            if ch == curses.KEY_RESIZE:

                theCharacter = ch
                theKeyName = 'KEY_RESIZE'
                theFlags = ''

                if wx.ENABLE_CURSES_RESIZE:

                    msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Key: Session Window Resize is enabled.'
                    self.logger.debug(msg)

                    raise tse.UserInterfaceException(
                        tse.GRAPHICAL_WINDOW_RESIZED, msg)

                else:

                    msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Key: Session Window Resize is NOT supported.'
                    self.logger.error(msg)

            elif ch == curses.KEY_MAX:

                theCharacter = ch
                theKeyName = 'KEY_MAX'
                theFlags = ''

                msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                    'Key: Session Window Max Size is NOT supported.'
                self.logger.error(msg)

            elif ch == curses.KEY_MIN:

                theCharacter = ch
                theKeyName = 'KEY_MIN'
                theFlags = ''

                msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                    'Key: Session Window Min Size is NOT supported.'
                self.logger.error(msg)

            else:

                # Return the name of the key numbered k.
                # The name of a key generating printable ASCII character is
                # the "key's" character. The name of a control-key
                # combination is a two-character string consisting of a
                # caret followed by the corresponding printable ASCII
                # character. The name of an alt-key combination (128-255)
                # is a string consisting of the prefix "M-" followed by
                # the name of the corresponding ASCII character.
                theKeyname = curses.keyname(ch)
                if EventLoop.ts_EscapeActive:
                    theFlags = 'Alt-'
                    theCharacter = theKeyname.upper()
                    EventLoop.ts_EscapeActive = False

                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Alt Key: "%s" ' % theKeyname
                    fmt2 = '(0x%2.2X); ' % ch
                    fmt3 = 'Flags: "%s"; ' % theFlags
                    fmt4 = 'Character: "%s"' % theCharacter
                    msg = fmt1 + fmt2 + fmt3 + fmt4
                    print('NOTICE: %s\n' % msg)
                    self.logger.debug(msg)

                elif len(theKeyname) == 1:
                    theFlags = ''
                    theCharacter = theKeyname

                    if (64 < ord(theKeyname)) and \
                       (ord(theKeyname) < 91):
                        theFlags = 'Shift'
                        theCharacter = theKeyname.lower()

                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Normal Key: "%s" ' % theKeyname
                    fmt2 = '(0x%2.2X); ' % ch
                    fmt3 = 'Flags: "%s"; ' % theFlags
                    fmt4 = 'Character: "%s"' % theCharacter
                    msg = fmt1 + fmt2 + fmt3 + fmt4
                    print('NOTICE: %s\n' % msg)
                    self.logger.debug(msg)

                elif (len(theKeyname) == 2) and \
                     theKeyname[0] == '^' and \
                     theKeyname[1] == '[':
                    EventLoop.ts_EscapeActive = True
                    theFlags = 'Alt-'
                    theCharacter = ch

                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Escape Key: "%s" ' % theKeyname
                    fmt2 = '(0x%2.2X); ' % ch
                    fmt3 = 'Flags: "%s"; ' % theFlags
                    fmt4 = 'Character: "%s"' % theCharacter
                    msg = fmt1 + fmt2 + fmt3 + fmt4
                    print('NOTICE: %s\n' % msg)
                    self.logger.debug(msg)

                elif (len(theKeyname) == 2) and theKeyname[0] == '^':
                    theFlags = 'Ctrl-'
                    theCharacter = theKeyname[1:2]

                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Control Key: "%s" ' % theKeyname
                    fmt2 = '(0x%2.2X); ' % ch
                    fmt3 = 'Flags: "%s"; ' % theFlags
                    fmt4 = 'Character: "%s"' % theCharacter
                    msg = fmt1 + fmt2 + fmt3 + fmt4
                    print('NOTICE: %s\n' % msg)
                    self.logger.debug(msg)

##                elif (len(theKeyname) == 3) and theKeyname[0:2] == 'M-':
##                    # TBD - Under Construction.
##                    # Notes: "M-" observed only with Mac Terminal session;
##                    #        Not observed with Cygwin or Mac iTerm sessions.
##                    Normal Key: "l" (0x6C); Flags: ""; Character: "l"
##                    Unknown Key: "M-B" (0xC2); Flags: ""; Character: "194"
##                    Unknown Key: "M-," (0xAC); Flags: ""; Character: "172"
##
##                    EventLoop.ts_EscapeActive = True
##                    theFlags = 'Alt-'
##                    theCharacter = ch

##                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
##                           'Escape Key (Mac Terminal): "%s" ' % theKeyname
##                    fmt2 = '(0x%2.2X); ' % ch
##                    fmt3 = 'Flags: "%s"; ' % theFlags
##                    fmt4 = 'Character: "%s"' % theCharacter
##                    msg = fmt1 + fmt2 + fmt3 + fmt4
##                    print('NOTICE: %s\n' % msg)
##                    self.logger.debug(msg)

                else:
                    theFlags = ''
                    theCharacter = ch

                    fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                        'Unknown Key: "%s" ' % theKeyname
                    fmt2 = '(0x%2.2X); ' % ch
                    fmt3 = 'Flags: "%s"; ' % theFlags
                    fmt4 = 'Character: "%s"' % theCharacter
                    msg = fmt1 + fmt2 + fmt3 + fmt4
                    print('NOTICE: %s\n' % msg)
                    self.logger.debug(msg)

        except Exception as e:
            msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                'Exception: %s' % str(e)
            self.logger.error(msg)
            print('NOTICE: %s\n' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Begin Kludge

        if wx.USE_CURSES_PANEL_STACK:
            topPanelHandle = curses.panel.top_panel()
            topWindow = tsWxGTUI_DataBase.WindowsByPanelLayer[topPanelHandle]

        triggeringEvent = EVT_CHAR
        triggeringKeyboardTuple = (ch, theCharacter, theKeyname, theFlags)
        triggeringEvent.EventData = triggeringKeyboardTuple
        try:

            triggeringObject = tsWxGTUI_DataBase.KeyboardInputRecipients[
                'lifoList'][0]

            objectId = triggeringObject.ts_AssignedId

        except Exception as errorCode:

            triggeringObject = self
            objectId = triggeringObject.ts_AssignedId

            msg = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
                'errorCode=""%s"' % str(errorCode)
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        objectCriteria = msg

        fmt1 = 'tsWxEventLoop.tsKeyboardEventGenerator: ' + \
            'Key: "%s" ' % theKeyname
        fmt2 = '(0x%2.2X); ' % ch
        fmt3 = 'Flags: "%s"; ' % theFlags
        fmt4 = 'Character: "%s"; ' % theCharacter
        fmt5 = 'triggeringEvent=%s; ' % str(triggeringEvent)
        fmt6 = 'triggeringObject=%s' % str(triggeringObject)
        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6
        print('NOTICE: %s\n' % msg)
        self.logger.debug(msg)

        # End Kludge

##        theEvent = Event(
##            id=wx.ID_ANY,
##            callbackUserData=None,
##            canVeto=False,
##            eventCategory=wxEVT_CATEGORY_USER_INPUT,
##            eventCriteria='tsGTUI.KEYBOARD_INPUT',
##            eventData=triggeringKeyboardTuple, # theCharacter,
##            eventSource='TBD-KEYBOARD_INPUT',
##            eventType=wxEVT_CHAR,
##            isCommandEvent=False,
##            propagationLevel=wxEVENT_PROPAGATE_NONE,
##            skipped=False,
##            timeStamp=time.time(),
##            veto=False,
##            wasProcessed=False)

        if bypassEventProcessingMode:

            results = self.tsProcessEventTables(
                objectCriteria=objectCriteria,
                objectId=objectId,
                triggeringEvent=triggeringEvent,
                triggeringObject=triggeringObject)

        return (triggeringEvent)

    #-----------------------------------------------------------------------

    def tsLookupButton(self, mouseId, x, y, z, bstate):
        '''
        Search the list of Buttons for the one containing the caretPoint.
        '''

        lookup = self.ts_MouseButtonCodes

        state = ''
        for buttonKey in list(lookup.keys()):
            if buttonKey == 'name':
                pass

            elif bstate & buttonKey and \
                 bstate & curses.BUTTON_SHIFT:
                # TBD - This button combination is not recognized.
                state = '%s shift' % lookup[buttonKey]

            elif bstate & buttonKey and \
                 bstate & curses.BUTTON_CTRL:
                # TBD - This button combination is not recognized.
                state = '%s ctrl' % lookup[buttonKey]

            elif bstate & buttonKey and \
                 bstate & curses.BUTTON_ALT:
                # TBD - This button combination is not recognized.
                state = '%s alt' % lookup[buttonKey]

                #
                # These last two codes are commented out because their
                # inclusion preempts identification of the specific mouse
                # and button state changes.
                #
                ## elif bstate & buttonKey and \
                ##      bstate & curses.ALL_MOUSE_EVENTS]:
                ##     # TBD - This button combination is not recognized.
                ##     state = '%s report all button state changes' % \
                ##             buttonKey

                ## elif bstate & buttonKey and \
                ##      bstate & curses.REPORT_MOUSE_POSITION]:
                ##     # TBD - This button combination is not recognized.
                ##     state = '%s report mouse movement' % buttonKey

            elif bstate & buttonKey:
                state = '%s' % lookup[buttonKey]

        fmt = 'tsWxEventLoop.tsLookupButton: ' + \
            'Mouse: id=%2.2s ' + \
            'x=%3.3s ' + \
            'y=%3.3s ' + \
            'z=%3.3s ' + \
            'bstate=0x%4.4X ' + \
            'state=%s'
        self.logger.debug(fmt % (mouseId, x, y, z, bstate, state))

        return (state)

    #-----------------------------------------------------------------------

    def  tsLookupWindows(self, theWindows, caretPoint, x, y):
        '''
        Search the list of Windows for candidates containing the caretPoint.
        '''

        for i in range(0, theWindows[
            tsWxGTUI_DataBase.TheWindows['windowIndex']]):
            aWindow = theWindows[i]

            if aWindow['theFirstCallerClassName'] in firstCallerClassNames:
                try:
                    theKeys = list(aWindow.keys())

                    msgCaret = 'Caret at %s' % str(caretPoint)

                    msgClass = ''
                    if 'theFirstCallerClassName' in theKeys:
                        msgClass = '; Class (%s)' % \
                            aWindow['theFirstCallerClassName']

                    msgName = ''
                    if 'name' in theKeys:
                        msgName = '; name (%s)' % aWindow['name']

                    msgLabel = ''
                    if 'Label' in theKeys:
                        msgLabel = '; Label (%s)' % aWindow['Label']

                    theLink = tsWxGTUI_DataBase
                    ancestor = theLink.WindowTopLevelAncestors[aWindow]

                    msgAncestor = ''
                    if ancestor is not None:
                        msgAncestor = '; ancestor (%s)' % ancestor['name']

                    msg = 'tsWxEventLoop.tsLookupWindows: ' + \
                        '%s%s%s%s%s' % (msgCaret,
                                        msgClass,
                                        msgName,
                                        msgLabel,
                                        msgAncestor)

                    self.logger.debug(msg)

                except Exception as theExceptionError:
                    msg = 'tsWxEventLoop.tsLookupWindows: ' + \
                        '%s.' % str(theExceptionError)
                    self.logger.error(msg)

    #-----------------------------------------------------------------------

    def tsMouseEventGenerator(self, ch):
        '''
        Categorize mouse input. Identify triggering object and generate
        the appropriate triggering event notification.
        '''
        self.ts_LastCursesGetMouseTuple = curses.getmouse()

        (mouseId, x, y, z, bstate) = self.ts_LastCursesGetMouseTuple

        (triggeringObject,
         objectId,
         objectCriteria) = self.tsThisIsTriggeringObject(
             mouseId, x, y, z, bstate)

        if triggeringObject is None:

            # Curses STDSCR area without associated wxPython GUI object,
            msg = 'Curses STDSCR area without ' + \
                  'associated wxPython GUI object.'
            print('DEBUG: %s' % msg)

        else:

            # Curses STDSCR area with associated wxPython GUI object.
            triggeringEvent = self.tsThisIsTriggeringEvent(
                mouseId, x, y, z, bstate, objectId)

            if DEBUG:

                fmt1 = 'tsWxEventLoop.tsMouseEventGenerator: '
                fmt2 = 'triggeringMouseTuple=%s' % str(
                    self.ts_LastCursesGetMouseTuple)
                fmt3 = 'triggeringObject=%s; id=%d; className=%s' % (
                    str(triggeringObject),
                    triggeringObject.ts_AssignedId,
                    triggeringObject.ts_ClassName)
                msg = fmt1 + fmt2 + fmt3
                self.logger.notice(msg)
                print('NOTICE: %s\n' % msg)

            if triggeringObject.ts_ClassName.lower() == \
               wx.ScrollBarGaugeNameStr.lower():

                triggeringMouseTuple = self.ts_LastCursesGetMouseTuple

            else:

                triggeringMouseTuple = None

            if bypassEventProcessingMode:

                results = self.tsProcessEventTables(
                    objectCriteria=objectCriteria,
                    objectId=objectId,
                    triggeringEvent=triggeringEvent,
                    triggeringObject=triggeringObject)

            else:

                theEvent = Event(
                    id=wx.ID_ANY,
                    callbackUserData=None,
                    canVeto=False,
                    eventCategory=wxEVT_CATEGORY_USER_INPUT,
                    eventCriteria=objectCriteria,
                    eventData=triggeringMouseTuple,
                    eventSource=triggeringObject,
                    eventType=triggeringEvent.EventType,
                    isCommandEvent=False,
                    propagationLevel=wxEVENT_PROPAGATE_NONE,
                    skipped=False,
                    timeStamp=time.time(),
                    veto=False,
                    wasProcessed=False)

                self.ts_RealTimeQueue.Add(theEvent)

    #-----------------------------------------------------------------------

    def tsProcessEventTables(self,
                             objectCriteria=None,
                             objectId=None,
                             triggeringEvent=None,
                             triggeringObject=None):
        '''
        Dispatch the triggering event to one or more event handlers
        identified in the system or user event table of the triggering
        object and its ancestors.

        Return True if an event handler found. False if no event handler
        found.
        '''
        self.logger.wxASSERT_MSG(
            (not (triggeringObject is None)),
            msg='tsWxEventLoop.tsProcessEventTables: ' + \
            'triggeringObject is None.')

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxEventLoop.tsProcessEventTables: ' + \
            'objectId is None.')

        self.logger.wxASSERT_MSG(
            (not (triggeringEvent is None)),
            msg='tsWxEventLoop.tsProcessEventTables: ' + \
            'triggeringEvent is None.')

        precedenceSequence = [True, False]
        triggeringEventType = triggeringEvent.ts_EventType[0]

        if DEBUG:
            self.logger.debug(
                'tsWxEventLoop.tsProcessEventTables: ' +\
                'for objectCriteria=%s; triggeringEventType=%s' % (
                    objectCriteria,
                    triggeringEventType))

        targetObject = triggeringObject
        targetObjectList = {}
        results = False

        while ((not results) and (not (targetObject is None))):

            try:
                targetObjectLabel = targetObject.GetLabel()
            except Exception as errorCode:
                targetObjectLabel = None
            targetObjectList[
                targetObjectLabel] = targetObject.ts_AssignedId
            for precedence in precedenceSequence:

                if self.tsProcessSelectedEventTable(
                    objectCriteria=objectCriteria,
                    objectId=objectId,
                    triggeringEvent=triggeringEvent,
                    triggeringObject=targetObject,
                    useSystemEventTable=precedence):

                    results = True

                    if DEBUG:
                        msg = 'tsWxEventLoop.tsProcessEventTables: ' + \
                            'results=%s; targetObjectList=%s' % (
                                results, targetObjectList)
                        self.logger.debug(msg)

                    break

            targetObject = targetObject.Parent

    #-----------------------------------------------------------------------

    def tsProcessSelectedEventTable(self,
                                    objectCriteria=None,
                                    objectId=None,
                                    triggeringEvent=None,
                                    triggeringObject=None,
                                    useSystemEventTable=True):
        '''
        Return True after dispatching the triggering event to an event
        handler identified in the system or user event table of the.
        triggering object. Return False if no event handler found.
        '''
        self.logger.wxASSERT_MSG(
            (not (objectCriteria is None)),
            msg='Invalid objectCriteria=%s' % objectCriteria)

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxEventLoop.tsProcessSelectedEventTable: ' + \
            'objectId=%s' % objectId)

        self.logger.wxASSERT_MSG(
            (not (triggeringEvent is None)),
            msg='tsWxEventLoop.tsProcessSelectedEventTable: ' + \
            'triggeringEvent=%s' % triggeringEvent)

        self.logger.wxASSERT_MSG(
            (not (triggeringObject is None)),
            msg='tsWxEventLoop.tsProcessSelectedEventTable: ' + \
            'triggeringObject=%s' % triggeringObject)

        triggeringEventData = triggeringEvent.EventData

        results = False

        if True or DEBUG:
            fmt1 = 'tsWxEventLoop.tsProcessSelectedEventTable: '
            fmt2 = 'objectCriteria=%s; ' % objectCriteria
            fmt3 = 'objectId=%s; ' % objectId
            fmt4 = 'triggeringEvent=%s; ' % str(triggeringEvent)
            fmt5 = 'triggeringEventData=%s; ' % str(triggeringEventData)
            fmt6 = 'triggeringObject=%s; ' % str(triggeringObject)
            fmt7 = 'useSystemEventTable=%s' % str(useSystemEventTable)
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6 + fmt7
            self.logger.debug(msg)

        # Process the non-focus event explicity associated with
        # triggering object.
        try:

            # The triggeringEvent is an iterable evtType (i.e., a list).
            triggeringEventType = triggeringEvent.ts_EventType[0]

        except Exception as eventError:

            msg = 'tsWxEventLoop.tsProcessSelectedEventTable: ' + \
                'eventError="%s"' % str(eventError)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        try:

            objectAssignedId = triggeringObject.ts_AssignedId
            objectName = triggeringObject.ts_Name

            if useSystemEventTable:

                selectedEventTable = triggeringObject.ts_SystemEventTable

            else:

                selectedEventTable = triggeringObject.ts_UserEventTable

            for theEventTableEntryKey in list(selectedEventTable.keys()):

                if theEventTableEntryKey == 'name':

                    pass

                else:

                    theEventTableEntry = selectedEventTable[
                        theEventTableEntryKey]

                    selectedEvent = theEventTableEntry['event']
                    # The selectedEvent is an iterable evtType (i.e., a list).
                    selectedEventType = selectedEvent.ts_EventType[0]

                    if selectedEventType == triggeringEventType:

                        if False and DEBUG:
                            fmt1 = 'tsWxEventLoop.'
                            fmt2 = 'tsProcessSelectedEventTable: '
                            fmt3 = 'triggeringEventType=' + \
                                '%s; ' % triggeringEventType
                            fmt4 = 'selectedEventType=' + \
                                '%s\n' % selectedEventType
                            msg = fmt1 + fmt2 + fmt3 + fmt4
                            self.logger.debug('DEBUG: %s\n' % msg)

                        selectedEventHandler = theEventTableEntry['handler']

                        selectedEventHandler(triggeringEvent)

                        results = True

                    else:

                        if False and DEBUG:
                            fmt1 = 'tsWxEventLoop.'
                            fmt2 = 'tsProcessSelectedEventTable: '
                            fmt3 = 'triggeringEvent=%s; ' % triggeringEvent
                            fmt4 = 'selectedEvent=%s\n' % selectedEvent
                            msg = fmt1 + fmt2 + fmt3 + fmt4
                            self.logger.debug('DEBUG: %s\n' % msg)

        except Exception as objectError:

            msg = 'tsWxEventLoop.tsProcessSelectedEventTable: ' + \
                'objectError="%s"' % str(objectError)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (results)

    #-----------------------------------------------------------------------

    def tsResizeHandler(self, signal):
        '''
        TBD - Not sure this is functional or needed.
        '''
        curses.endwin()

        # Needs to be called after an endwin() so ncurses will initialize
        # itself with the new terminal dimensions.
        window = self.ts_Handle

        window.refresh()
        window.clear()

##      mvprintw(0, 0, "COLS = %d, LINES = %d", COLS, LINES)
##      refresh()

    #-----------------------------------------------------------------------

    def tsScanDescendantOrderOfShowForTopMostWindow(
        self, theWindows, caretPoint):
        '''
        Return the non-overlayed, top most window in a list of candidate
        windows that should be associated with the caret and mouse click.
        '''
        fmt1 = 'tsWxEventLoop.tsScanDescendantOrderOfShowForTopMostWindow: '
        fmt2 = 'theWindows (top-most): %s' % theWindows
        fmt3 = 'caretPoint: %s' % str(caretPoint)
        msg = fmt1 + fmt2 + fmt3
        self.logger.debug(msg)

        theEarliestAncestors = theWindows

        criteriaText = ''

        # Displays character under caret only for underlying "stdscr".
        # Have not yet determined stacking level for "window" overlays.
        stdscr = self.stdscr.Stdscr
        attributedCharacterUnderCaret = stdscr.inch(caretPoint.y, caretPoint.x)
        if False:
            attribute = (
                int(attributedCharacterUnderCaret) & 0xFF00) / 256
        else:
            attribute = (
                int(attributedCharacterUnderCaret) & 0xFFFFFF00)

        characterUnderCaret = chr(
            int(attributedCharacterUnderCaret) & 0xFF)

        msg = 'tsWxEventLoop.tsThisIsTriggeringObject: ' + \
            'characterUnderCaret(lowest)=0x%x (%c)' % \
            (ord(characterUnderCaret), characterUnderCaret)
        criteriaText += msg
        self.logger.debug(msg)

        objectId = None
        triggeringObject = None

        try:
            for anAncestor in theEarliestAncestors:

                self.logger.debug(
                    'tsWxEventLoop.' + \
                    'tsScanDescendantOrderOfShowForTopMostWindow: ' + \
                    'anAncestor=%s; anAncestor.ts_AssignedId=%d' % (
                        str(anAncestor),
                        anAncestor.ts_AssignedId))

                for aWindowId in reversed(sorted(
                    anAncestor.ts_DescendantOrderOfShow)):

                    aWindow = tsWxGTUI_DataBase.WindowsByAssignedId[aWindowId]

                    self.logger.debug(
                        'tsWxEventLoop.' + \
                        'tsScanDescendantOrderOfShowForTopMostWindow: ' + \
                        'aWindowId=%d; anAncestor.ts_AssignedId=%d' % (
                            aWindowId, anAncestor.ts_AssignedId))

                    if aWindow.ts_Rect.Inside(caretPoint):

                        triggeringObject = aWindow
                        objectId = aWindowId

                        fmt1 = 'tsWxEventLoop.' + \
                            'tsScanDescendantOrderOfShowForTopMostWindow: '
                        fmt2 = 'caretPoint=%s ' % str(caretPoint)
                        fmt3 = 'inside aWindow.ts_Rect=%s' % str(
                            aWindow.ts_Rect)
                        msg = fmt1 + fmt2 + fmt3
                        self.logger.debug(msg)

                        break

                    else:

                        fmt1 = 'tsWxEventLoop.' + \
                            'tsScanDescendantOrderOfShowForTopMostWindow: '
                        fmt2 = 'caretPoint=%s ' % str(caretPoint)
                        fmt3 = 'NOT inside aWindow.ts_Rect=%s' % str(
                            aWindow.ts_Rect)
                        msg = fmt1 + fmt2 + fmt3
                        self.logger.debug(msg)

                if not (triggeringObject is None):

                    break

        except Exception as errorCode:

            triggeringObject = None
            msg = 'tsWxEventLoop.' + \
                'tsScanDescendantOrderOfShowForTopMostWindoww: ' + \
                'Exception: "%s".' % str(errorCode)
            criteriaText += '; %s' % msg
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        if (triggeringObject is None):

            msg = 'tsWxEventLoop.' + \
                'tsScanDescendantOrderOfShowForTopMostWindow: ' + \
                'Failed to establish triggeringObject'
            criteriaText += '; %s' % msg
            self.logger.debug(msg)

        else:

            try:

                theWindow = triggeringObject
                objectId = theWindow.ts_AssignedId

                # TBD - Try to display character under caret for theWindow.
                deltaPoint = caretPoint - \
                    wxPoint(theWindow.ts_Rect.x, theWindow.ts_Rect.y)

                msg = 'deltaPoint(highest)=%s' % deltaPoint
                criteriaText += '; %s' % msg
                self.logger.debug(msg)

                (dx, dy) = wx.tsGetCharacterValues(deltaPoint.x, deltaPoint.y)

                if True:
                    (characterUnderCaret,
                     attributeUnderCaret) = theWindow.tsCursesInch(
                         dy, dx, pixels=True)
                else:
                    (characterUnderCaret,
                     attributeUnderCaret) = theWindow.tsCursesInch(
                         dy, dx)

                msg = 'tsWxEventLoop.' + \
                    'tsScanDescendantOrderOfShowForTopMostWindow: ' + \
                    'characterUnderCaret(highest)=0x%x (%c)' % \
                    (ord(characterUnderCaret), characterUnderCaret)

                criteriaText += '; %s' % msg
                self.logger.debug(msg)

            except Exception as errorCode:

                triggeringObject = None
                msg = 'tsWxEventLoop.' + \
                    'tsScanDescendantOrderOfShowForTopMostWindow: ' + \
                    'Exception: "%s".' % str(errorCode)
                criteriaText += '; %s' % msg
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        self.myChar = characterUnderCaret
        objectCriteria = '[%s]' % criteriaText

        fmt1 = 'tsWxEventLoop.' + \
            'tsScanDescendantOrderOfShowForTopMostWindow: '
        fmt2 = 'characterUnderCaret="%s"' % characterUnderCaret
        fmt3 = 'objectCriteria= "[%s]"' % str(criteriaText)
        msg = fmt1 + fmt2 + fmt3
        self.logger.debug(msg)

        return (triggeringObject, objectId, objectCriteria)

    #-----------------------------------------------------------------------

    def tsScanWindowsByCursesPanel(
        self, theWindows, caretPoint):
        '''
        TBD - Under construction. Do not use.

        Return the overlayed, top most window in a list of candidate
        windows that should be associated with the caret and mouse click.
        '''
        fmt1 = 'tsWxEventLoop.tsScanWindowsByCursesPanel: '
        fmt2 = 'theWindows (top-most): %s' % theWindows
        fmt3 = 'caretPoint: %s' % str(caretPoint)
        msg = fmt1 + fmt2 + fmt3
        print(msg)
        self.logger.debug(msg)

        theEarliestAncestors = theWindows

        try:
            myList = wxDoubleLinkedList()
            bottom_panel = curses.panel.bottom_panel()
            print('bottom_panel=%s' % str(bottom_panel))
            top_panel = curses.panel.top_panel()
            print('top_panel=%s' % str(top_panel))
            aPanel = bottom_panel
            myPanelDescendantOrderOfShow = []
            myDataBase = tsGTUI.GraphicalTextUserInterface
            done = False
            while not done:
                myList.InsertAsTail(panel)
                myPanelDescendantOrderOfShow += []
                if aPanel == top_panel:
                    done = True
                else:
                    aPanel = aPanel.above() 
                    print('aPanel=%s' % str(aPanel))

                    aWindow = myDataBase.WindowsByPanelLayer[aPanel]
                    myPanelDescendantOrderOfShow += [aWindow.ts_AssignedId]
                    print('aWindow=%s; AssignedId=%d' % (
                        str(aWindow), aWindow.ts_AssignedId))
        except Exception as errorCode:
            fmt1 = 'tsWxEventLoop.tsScanWindowsByCursesPanel: '
            fmt2 = 'errorCode=%s' % str(errorCode)
            msg = fmt1 + fmt2
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        fmt1 = 'tsWxEventLoop.tsScanWindowsByCursesPanel: '
        fmt2 = '\nmyPanelDescendantOrderOfShow: %s' % str(
            myPanelDescendantOrderOfShow)
        fmt3 = '\nOrderOfShowPanelStack: %s' % str(
            myDataBase.WindowDataBase[
                'WindowsByShowOrder']['OrderOfShowPanelStack'])
        msg = fmt1 + fmt2 + fmt3
        print(msg)
        self.logger.debug(msg)

        criteriaText = ''

        # Displays character under caret only for underlying "stdscr".
        # Have not yet determined stacking level for "window" overlays.
        stdscr = self.stdscr.Stdscr
        attributedCharacterUnderCaret = stdscr.inch(caretPoint.y, caretPoint.x)
        attribute = (int(attributedCharacterUnderCaret) & 0xFF00) / 256
        characterUnderCaret = chr(
            int(attributedCharacterUnderCaret) & 0xFF)

        msg = 'tsWxEventLoop.tsThisIsTriggeringObject: ' + \
            'characterUnderCaret(lowest)=0x%x (%c)' % \
            (ord(characterUnderCaret), characterUnderCaret)
        criteriaText += msg
        self.logger.debug(msg)

        objectId = None
        triggeringObject = None

        if True:

            # Unknown algorithm based on myPanelDescendantOrderOfShow
            try:

                for aWindowId in reversed(sorted(
                    myPanelDescendantOrderOfShow)):

                    aWindow = tsWxGTUI_DataBase.WindowsByAssignedId[
                        aWindowId]

                    self.logger.debug(
                        'tsWxEventLoop.' + \
                        'tsScanWindowsByCursesPanel: ' + \
                        'aWindowId=%d' % aWindowId)

                    if aWindow.ts_Rect.Inside(caretPoint):

                        triggeringObject = aWindow
                        objectId = aWindowId

                        fmt1 = 'tsWxEventLoop.' + \
                            'tsScanWindowsByCursesPanel: '
                        fmt2 = 'caretPoint=%s ' % str(caretPoint)
                        fmt3 = 'inside aWindow.ts_Rect=%s' % str(
                            aWindow.ts_Rect)
                        msg = fmt1 + fmt2 + fmt3
                        self.logger.debug(msg)

                        break

                    else:

                        fmt1 = 'tsWxEventLoop.' + \
                            'tsScanWindowsByCursesPanel: '
                        fmt2 = 'caretPoint=%s ' % str(caretPoint)
                        fmt3 = 'NOT inside aWindow.ts_Rect=%s' % str(
                            aWindow.ts_Rect)
                        msg = fmt1 + fmt2 + fmt3
                        self.logger.debug(msg)

            except Exception as errorCode:

                triggeringObject = None
                msg = 'tsWxEventLoop.' + \
                    'tsScanWindowsByCursesPanel: ' + \
                    'Exception: "%s".' % str(errorCode)
                criteriaText += '; %s' % msg
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        elif False:

            # Known working algorithm based on myPanelDescendantOrderOfShow
            try:

                for anAncestor in theEarliestAncestors:

                    self.logger.debug(
                        'tsWxEventLoop.' + \
                        'tsScanWindowsByCursesPanel: ' + \
                        'anAncestor=%s; anAncestor.ts_AssignedId=%d' % (
                            str(anAncestor),
                            anAncestor.ts_AssignedId))

                    for aWindowId in reversed(sorted(
                        myPanelDescendantOrderOfShow)):

                        aWindow = tsWxGTUI_DataBase.WindowsByAssignedId[
                            aWindowId]

                        self.logger.debug(
                            'tsWxEventLoop.' + \
                            'tsScanWindowsByCursesPanel: ' + \
                            'aWindowId=%d; anAncestor.ts_AssignedId=%d' % (
                                aWindowId, anAncestor.ts_AssignedId))

                        if aWindow.ts_Rect.Inside(caretPoint):

                            triggeringObject = aWindow
                            objectId = aWindowId

                            fmt1 = 'tsWxEventLoop.' + \
                                'tsScanWindowsByCursesPanel: '
                            fmt2 = 'caretPoint=%s ' % str(caretPoint)
                            fmt3 = 'inside aWindow.ts_Rect=%s' % str(
                                aWindow.ts_Rect)
                            msg = fmt1 + fmt2 + fmt3
                            self.logger.debug(msg)

                            break

                        else:

                            fmt1 = 'tsWxEventLoop.' + \
                                'tsScanWindowsByCursesPanel: '
                            fmt2 = 'caretPoint=%s ' % str(caretPoint)
                            fmt3 = 'NOT inside aWindow.ts_Rect=%s' % str(
                                aWindow.ts_Rect)
                            msg = fmt1 + fmt2 + fmt3
                            self.logger.debug(msg)

                    if not (triggeringObject is None):

                        break

            except Exception as errorCode:

                triggeringObject = None
                msg = 'tsWxEventLoop.' + \
                    'tsScanWindowsByCursesPanel: ' + \
                    'Exception: "%s".' % str(errorCode)
                criteriaText += '; %s' % msg
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            # Known working algorithm based on ts_DescendantOrderOfShow
            try:

                for anAncestor in theEarliestAncestors:

                    self.logger.debug(
                        'tsWxEventLoop.' + \
                        'tsScanWindowsByCursesPanel: ' + \
                        'anAncestor=%s; anAncestor.ts_AssignedId=%d' % (
                            str(anAncestor),
                            anAncestor.ts_AssignedId))

                    for aWindowId in reversed(sorted(
                        anAncestor.ts_DescendantOrderOfShow)):

                        aWindow = tsWxGTUI_DataBase.WindowsByAssignedId[
                            aWindowId]

                        self.logger.debug(
                            'tsWxEventLoop.' + \
                            'tsScanWindowsByCursesPanel: ' + \
                            'aWindowId=%d; anAncestor.ts_AssignedId=%d' % (
                                aWindowId, anAncestor.ts_AssignedId))

                        if aWindow.ts_Rect.Inside(caretPoint):

                            triggeringObject = aWindow
                            objectId = aWindowId

                            fmt1 = 'tsWxEventLoop.' + \
                                'tsScanWindowsByCursesPanel: '
                            fmt2 = 'caretPoint=%s ' % str(caretPoint)
                            fmt3 = 'inside aWindow.ts_Rect=%s' % str(
                                aWindow.ts_Rect)
                            msg = fmt1 + fmt2 + fmt3
                            self.logger.debug(msg)

                            break

                        else:

                            fmt1 = 'tsWxEventLoop.' + \
                                'tsScanWindowsByCursesPanel: '
                            fmt2 = 'caretPoint=%s ' % str(caretPoint)
                            fmt3 = 'NOT inside aWindow.ts_Rect=%s' % str(
                                aWindow.ts_Rect)
                            msg = fmt1 + fmt2 + fmt3
                            self.logger.debug(msg)

                    if not (triggeringObject is None):

                        break

            except Exception as errorCode:

                triggeringObject = None
                msg = 'tsWxEventLoop.' + \
                    'tsScanWindowsByCursesPanel: ' + \
                    'Exception: "%s".' % str(errorCode)
                criteriaText += '; %s' % msg
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        if (triggeringObject is None):

            msg = 'tsWxEventLoop.' + \
                'tsScanWindowsByCursesPanel: ' + \
                'Failed to establish triggeringObject'
            criteriaText += '; %s' % msg
            self.logger.debug(msg)

        else:

            try:

                theWindow = triggeringObject
                objectId = theWindow.ts_AssignedId

                # TBD - Try to display character under caret for theWindow.
                deltaPoint = caretPoint - \
                    wxPoint(theWindow.ts_Rect.x, theWindow.ts_Rect.y)

                msg = 'deltaPoint(highest)=%s' % deltaPoint
                criteriaText += '; %s' % msg
                self.logger.debug(msg)

                (dx, dy) = wx.tsGetCharacterValues(deltaPoint.x, deltaPoint.y)

                if True:
                    (characterUnderCaret,
                     attributeUnderCaret) = theWindow.tsCursesInch(
                         dy, dx, pixels=True)
                else:
                    (characterUnderCaret,
                     attributeUnderCaret) = theWindow.tsCursesInch(
                         dy, dx)

                msg = 'tsWxEventLoop.' + \
                    'tsScanWindowsByCursesPanel: ' + \
                    'characterUnderCaret(highest)=0x%x (%c)' % \
                    (ord(characterUnderCaret), characterUnderCaret)

                criteriaText += '; %s' % msg
                self.logger.debug(msg)

            except Exception as errorCode:

                triggeringObject = None
                msg = 'tsWxEventLoop.' + \
                    'tsScanWindowsByCursesPanel: ' + \
                    'Exception: "%s".' % str(errorCode)
                criteriaText += '; %s' % msg
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        self.myChar = characterUnderCaret
        objectCriteria = '[%s]' % criteriaText

        fmt1 = 'tsWxEventLoop.' + \
            'tsScanWindowsByCursesPanel: '
        fmt2 = 'characterUnderCaret="%s"' % characterUnderCaret
        fmt3 = 'objectCriteria= "[%s]"' % str(criteriaText)
        msg = fmt1 + fmt2 + fmt3
        self.logger.debug(msg)

        return (triggeringObject, objectId, objectCriteria)

    #-----------------------------------------------------------------------

    def tsScanDescendantPanelStackForTopMostWindow(
        self, theWindows, caretPoint):
        '''
        TBD - Obsolete. Do not use.

        Return the overlayed, top most window in a list of candidate
        windows that should be associated with the caret and mouse click.
        '''
        fmt1 = 'tsWxEventLoop.tsScanDescendantPanelStackForTopMostWindow: '
        fmt2 = 'theWindows (top-most): %s' % theWindows
        fmt3 = 'caretPoint: %s' % str(caretPoint)
        msg = fmt1 + fmt2 + fmt3
        self.logger.debug(msg)

        triggeringObject = None

        try:

            ancestorDict = {}
            for aWindow in candidateWindows:
                ts_EarliestAncestor = aWindow['EarliestAncestor']
                candidateAssignedId = aWindow['AssignedId']
                ancestorDict[ts_EarliestAncestor] = candidateAssignedId
                fmt = 'tsWxEventLoop.' + \
                      'tsScanDescendantPanelStackForTopMostWindow: ' + \
                      'candidateAssignedId=%d, ' + \
                      'ts_EarliestAncestor=%s'
                msg = fmt % (candidateAssignedId, ts_EarliestAncestor)
                self.logger.debug(msg)

            rankingDict = {}
            index = -1
            for assignedId in \
                tsWxGTUI_DataBase.WindowsByShowOrder[
                    'OrderOfShowPanelStack']:

                index += 1
                rankingDict[assignedId] = index
                fmt = 'tsWxEventLoop.' + \
                      'tsScanDescendantPanelStackForTopMostWindow: ' + \
                      'Index=%d, rankingDict=%s'
                msg = fmt % (index, rankingDict)
                self.logger.debug(fmt % (index, rankingDict))

            count = index + 1

            highestRank = -1
            highestCandidateId = -1
            for aWindow in candidateWindows:

                msg = 'tsWxEventLoop.' + \
                      'tsScanDescendantPanelStackForTopMostWindow: ' + \
                      'Sorting aWindowId=%d' % aWindow['AssignedId']
                self.logger.debug(msg)
                candidateId = aWindow['AssignedId']
                ancestorId = aWindow['EarliestAncestor']
                try:

                    candidateRank = rankingDict[candidateId]

                except Exception as rankingDictError:

                    fmt = 'tsWxEventLoop.' + \
                          'tsScanDescendantPanelStackForTopMostWindow: ' + \
                          'candidateId=%d;' + \
                          'rankingDictError=%s'
                    msg = fmt % (candidateId, str(rankingDictError))
                    self.logger.error(msg)

                if candidateRank > highestRank:

                    highestRank = candidateRank
                    highestCandidateId = candidateId

            try:

                theWindow = self.ts_WindowsByAssignedId[highestCandidateId]
                self.logger.debug(
                    'tsWxEventLoop.' + \
                    'tsScanDescendantPanelStackForTopMostWindow: ' + \
                    'highestCandidateId=%s; highestRank=%d; name=%s' % \
                    (highestCandidateId, highestRank, theWindow.ts_Name))

                topMostWindow = theWindow

            except Exception as theWindowsByAssignedIdError:

                msg = 'tsWxEventLoop.' + \
                      'tsScanDescendantPanelStackForTopMostWindow: ' + \
                      'Exception (theWindow: %s' % \
                      theWindowsByAssignedIdError
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        except Exception as theScanForTopMostWindowError:

            msg = 'tsWxEventLoop.' + \
                  'tsScanDescendantPanelStackForTopMostWindow: ' + \
                  'Exception: %s' % \
                  str(theScanForTopMostWindowError)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.logger.debug('tsWxEventLoop.' + \
                          'tsScanDescendantPanelStackForTopMostWindow: ' + \
                          'End')

        return (topMostWindow)

    #-----------------------------------------------------------------------

    def tsScanForTopMostWindow(self, theWindows, caretPoint):
        '''
        Return the top most window in a list of candidate windows that
        should be associated with the caret and mouse click.
        '''
        if True: # wx.USE_CURSES_PANEL_STACK:

            # Discover changes to order of show made via recent taskbar
            # button click operations that changed the panel stack.

            self.tsUpdatePanelStack()

            theScanner = self.tsScanWindowsByCursesPanel

        else:

            # Discover changes to order of show made via recent
            # window creation operations by the application program.

            theScanner = self.tsScanDescendantOrderOfShowForTopMostWindow

        (triggeringObject,
         objectId,
         objectCriteria) = theScanner(theWindows, caretPoint)

        return (triggeringObject, objectId, objectCriteria)

    #-----------------------------------------------------------------------

    def tsThisIsTriggeringEvent(self,
                                mouseId,
                                x,
                                y,
                                z,
                                bstate,
                                objectId):
        '''
        Identify the triggering event.
        '''
        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxEventLoop.tsThisIsTriggeringEvent: ' + \
            'objectId is None.')

        # Convert curses mouse state into wxPython mouse state and then
        # establish the appropriate wxPython mouse event type.
        results = {
            'name': 'MouseState',

            # "mouseId" is a short integer value used to make a destinction
            # between multiple pointing devices, for example on a laptop
            # with both a mouse pad and external mouse.
            'mouseId': mouseId,

            # "x" is an integer value representing the row in which the
            # mouse pointer was at during the event. Values start a 0 for
            # the leftmost column.
            'x': x * wx.pixelWidthPerCharacter,

            # "y" is an integer value representing the column in which the
            # mouse pointer was at during the event. Values start a 0 for
            # the topmost row.
            'y': y * wx.pixelHeightPerCharacter,

            # "z" is an integer value reserved for future use, though it
            # might be for reading the wheel button.
            'z': z,

            # "objectId" is an integer value reserved for future use to
            # make a destinction between multiple GUI objects, for example
            # the "assignedId" for a frame, dialog, checkbox, radio box,
            # button, textctrl etc.
            'objectId': objectId,

            'bstate': bstate,

            'LeftDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON1_PRESSED),

            'LeftUp': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON1_RELEASED),

            'LeftClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON1_CLICKED),

            'LeftDClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON1_DOUBLE_CLICKED),

            'LeftTClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON1_TRIPLE_CLICKED),

            'MiddleDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON2_PRESSED),

            'MiddleUp': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON2_RELEASED),

            'MiddleClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON2_CLICKED),

            'MiddleDClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON2_DOUBLE_CLICKED),

            'MiddleTClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON2_TRIPLE_CLICKED),

            'RightDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON3_PRESSED),

            'RightUp': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON3_RELEASED),

            'RightClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON3_CLICKED),

            'RightDClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON3_DOUBLE_CLICKED),

            'RightTClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON3_TRIPLE_CLICKED),

            'WheelDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON4_PRESSED),

            'WheelUp': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON4_RELEASED),

            'WheelClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON4_CLICKED),

            'WheelDClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON4_DOUBLE_CLICKED),

            'WheelTClicked': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON4_TRIPLE_CLICKED),

            'ShiftDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON_SHIFT),

            # "Cmd" is a pseudo key which is the same as Control for PC
            # and Unix platforms but the special "Apple" (a.k.a as
            # "Command") key on Macs.
            'CmdDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON_CTRL),

            'CtrlDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON_CTRL),

            'AltDown': self.tsIsThisTheMouseState(
                bstate, curses.BUTTON_ALT)
        }

        triggeringEvent = None
        for theKey in list(MouseTriggeringEventMap.keys()):

            fmt1 = 'tsWxEventLoop.tsThisIsTriggeringEvent: '
            fmt2 = 'results[%s]=%s; ' % (theKey, results[theKey])
            fmt3 = 'triggeringEvent=%s' % MouseTriggeringEventMap[theKey]
            msg = fmt1 + fmt2 + fmt3
            self.logger.debug(msg)

            if results[theKey]:

                theValue = MouseTriggeringEventMap[theKey]

                if triggeringEvent is None:

                    fmt1 = 'tsWxEventLoop.tsThisIsTriggeringEvent: '
                    fmt2 = 'can process ' + \
                        'triggeringEvent=%s; ' % theValue

                    triggeringEvent = theValue

                else:

                    fmt1 = 'tsWxEventLoop.tsThisIsTriggeringEvent: '
                    fmt2 = 'cannot process ' + \
                        'triggeringEvent=%s; ' % theValue

                msg = fmt1 + fmt2
                self.logger.debug(msg)

        triggeringEvent.EventData = (mouseId, x, y, z, bstate)

        return (triggeringEvent)

    #-----------------------------------------------------------------------

    def tsThisIsTriggeringObject(self, mouseId, x, y, z, bstate):
        '''
        Identify the "objectId" of the GUI object (frame, dialog, checkbox,
        radio box, button, textctrl etc.) to receive the mouse event.
        '''
        theButtonState = self.tsLookupButton(mouseId, x, y, z, bstate)

        # Convert from Character to Pixel co-ordinates
        (caretX, caretY) = wx.tsGetPixelValues(x, y)
        caretPoint = wxPoint(caretX, caretY)

        theWindows = reversed(
            tsWxGTUI_DataBase.WindowTopLevelTasks) # self.ts_TheWindows

        self.logger.debug('tsWxEventLoop.tsThisIsTriggeringObject: ' + \
                          'theWindows=%s.' % \
                          str(theWindows))

        (triggeringObject,
         objectId,
         objectCriteria) = self.tsScanForTopMostWindow(
             theWindows, caretPoint)

        self.logger.debug('***** myChar="%s"' % self.myChar)

        return (triggeringObject, objectId, objectCriteria)

    #-----------------------------------------------------------------------

    def tsTimeoutEventGenerator(self):
        '''
        Categorize timer input. Identify target GUI object and generate
        the appropriate event notification.

        TBD - Under Construction. Scan for the caretPoint, if available.
        '''
        if DEBUG_MOUSE:

            try:
                (mouseId, x, y, z, bstate) = curses.getmouse()

                if self.ts_MouseLastXYZ != (x, y, z):

                    fmt = 'tsWxEventLoop.tsTimeoutEventGenerator: ' + \
                        'Mouse: id=%2.2s ' + \
                        'x=%3.3s ' + \
                        'y=%3.3s ' + \
                        'z=%3.3s ' + \
                        'bstate=0x%4.4X'
                    self.logger.debug(fmt % (mouseId, x, y, z, bstate))
                    self.ts_MouseLastXYZ = (x, y, z)

            except Exception as getMouseError:

                (x, y, z) = (0, 0, 0)

                if self.ts_MouseLastXYZ != (x, y, z):
                    terminal = tsWxGTUI_DataBase.TermName

                    msg = 'tsWxEventLoop.tsTimeoutEventGenerator: ' + \
                        'Mouse: Not supported by "%s".' % terminal
                    self.ts_MouseLastXYZ = (x, y, z)
                    self.logger.error(msg)
                    # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        theEvent = Event(
            id=wx.ID_ANY,
            callbackUserData=None,
            canVeto=False,
            eventCategory=wxEVT_CATEGORY_TIMER,
            eventCriteria='tsGTUI.TERMINAL_TIMEOUT',
            eventData=None,
            eventSource='TBD-TERMINAL_TIMEOUT',
            eventType=wxEVT_TIMER,
            isCommandEvent=False,
            propagationLevel=wxEVENT_PROPAGATE_NONE,
            skipped=False,
            timeStamp=time.time(),
            veto=False,
            wasProcessed=False)

        return (theEvent)

    #-----------------------------------------------------------------------

    def tsUpdatePanelStack(self):
        '''
        Scan PanelStack from bottom to top and register updated
        position of each overlay layer in associated data base.
        '''
        self.logger.wxASSERT_MSG(
            (wx.USE_CURSES_PANEL_STACK),
            msg='tsWxEventLoop.tsUpdatePanelStack: ' + \
            'wx.USE_CURSES_PANEL_STACK != True.')

        #-------------------------------------------------------------------
        # Begin connection setup to Data Base
        # (Note: established by tsWxWindow.tsRegisterShowOrder)

        database = tsWxGTUI_DataBase

        # Begin setup to Read-Only Data Base
        panelLayerRegistry = database.WindowsByShowOrder[
            'PanelLayer']

        assignedIdRegistry = database.WindowsByShowOrder[
            'AssignedIdByPanelLayer']

        windowIdRegistry = database.WindowsByAssignedId

        if False and DEBUG and VERBOSE:

            print('DEBUG: tsWxEventLoop.tsUpdatePanelStack: ' + \
                  'panelLayerRegistry=%s\n' % str(
                      panelLayerRegistry))

            print('DEBUG: tsWxEventLoop.tsUpdatePanelStack: ' + \
                  'assignedIdRegistry=%s\n' % str(
                      assignedIdRegistry))

            print('DEBUG: tsWxEventLoop.tsUpdatePanelStack: ' + \
                  'windowIdRegistry=%s\n' % str(
                      windowIdRegistry))

        # End setup to Read-Only Data Base

        # Begin setup to Read-Write Data Base
        # (Note: The operator can change focus from one window object
        # to another by positioning the mouse over and clicking a mouse
        # button on a visible window oject. When the focus is changed,
        # the overlay layers should be shuffled to place the earliest
        # ancestor of the window object and its decendents on the top
        # of the panel stack. For example, when a button associated
        # with the taskbar is clicked, tsWxTaskBar.tsTaskBarTopTask
        # shuffles the sequence of overlay layers, but does not change
        # the data base. In the future, a generalize version of logic
        # might be moved into tsWxEventLoop.)
        panelStack = database.WindowsByShowOrder[
            'PanelStack']

        orderOfShowPanelStack = database.WindowsByShowOrder[
            'OrderOfShowPanelStack']

        orderOfShow = database.WindowsByShowOrder[
            'OrderOfShow']
        # End setup to Read-Write Data Base

        # End connection setup to Data Base
        #-------------------------------------------------------------------

        # Update Panel Stack with latest keyboard focus changes.

        panelStack = {}
        orderOfShowPanelStack = []

        done = False
        count = -1
        while (not done):

            try:

                if count == -1:

                    cursesPanel = curses.panel.bottom_panel()

                else:

                    cursesPanel = cursesPanel.above()

                count += 1
                windowAssignedId = assignedIdRegistry[cursesPanel]
                window = windowIdRegistry[windowAssignedId]

                panelStack[count] = {
                    'cursesPanel': cursesPanel,
                    'window': window,
                    'windowAssignedId': windowAssignedId
                }

                orderOfShowPanelStack += [windowAssignedId]

                if False and DEBUG and VERBOSE:

                    try:
                        windowLabel = window.GetLabel()
                    except Exception as errorCode:
                        windowLabel = None

                    fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                    fmt2 = 'panelStack[%d] ' % count
                    fmt3 = 'for windowAssignedId %d; ' %  windowAssignedId
                    fmt4 = 'panel=%s ' % cursesPanel
                    fmt5 = 'window: name=%s; label=%s' % (
                        window.ts_Name, windowLabel)
                    msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                    print('DEBUG: %s\n' % msg)

            except cursesErrorMethod:

                done = True

                if False and DEBUG and VERBOSE:

                    fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                    fmt2 = 'panelStack[%d] ' % count
                    fmt3 = 'curses.error'
                    msg = fmt1 + fmt2 + fmt3
                    print('ERROR: %s\n' % msg)

                break

            except KeyError:

                if False and DEBUG and VERBOSE:

                    fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                    fmt2 = 'panelStack[%d] ' % count
                    fmt3 = 'curses.error'
                    msg = fmt1 + fmt2 + fmt3
                    print('ERROR: KeyError for %s\n' % msg)

                done = True
                break

            except Exception as errorCode:

                if False and DEBUG and VERBOSE:

                    substring = "'NoneType' object has no attribute " \
                        "'above'"
                    index = errorCode.find(substring)

                    if index > -1:

                    # Substring Found

                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                        fmt2 = 'panelStack[%d] ' % count
                        fmt3 = 'Found %s at %d ' % (substring, index)
                        fmt4 = 'errorCode=%s' % str(errorCode)
                        msg = fmt1 + fmt2 + fmt3 + fmt4
                        print('DEBUG: %s\n' % msg)

                    else:

                        # Substring Not Found
                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                        fmt2 = 'panelStack[%d] ' % count
                        fmt3 = 'errorCode=%s' % str(errorCode)
                        msg = fmt1 + fmt2 + fmt3
                        print('ERROR: %s\n' % msg)

                done = True
                break

        if False and DEBUG and VERBOSE:
            for entry in orderOfShow:

                if not (entry in orderOfShowPanelStack):
                    try:
                        window = 0 # windowIdRegistry[entry]
                        name = 'unknown' # window.ts_Name

                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                        fmt2 = 'orderOfShowPanelStack missing %s (%s) ' % (
                            entry,
                            name)
                        fmt3 = 'found in orderOfShow'
                        print('WARNING: %s\n' % fmt1 + fmt2 + fmt3)
                    except Exception as errorCode:
                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: orderOfShow '
                        fmt2 = 'entry=%s; errorCode=%s' % (entry, errorCode)
                        print('ERROR: %s\n' % fmt1 + fmt2)

            for entry in orderOfShowPanelStack:

                if not (entry in orderOfShow):
                    try:
                        window = 0 # windowIdRegistry[entry]
                        name = 'unknown' # window.ts_Name
                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: '
                        fmt2 = 'orderOfShow missing %s (%s) ' % (entry,
                                                                 name)
                        fmt3 = 'found in orderOfShowPanelStack'
                        print('WARNING: %s\n' % fmt1 + fmt2 + fmt3)
                    except Exception as errorCode:
                        fmt1 = 'tsWxEventLoop.tsUpdatePanelStack: ' + \
                            'orderOfShowPanelStack '
                        fmt2 = 'entry=%s; errorCode=%s' % (entry, errorCode)
                        print('ERROR: %s\n' % fmt1 + fmt2)

    #-----------------------------------------------------------------------

    def tsVT100MouseEventGenerator(self, vt100State):
        '''
        Categorize mouse input. Identify triggering object and generate
        the appropriate triggering event notification.

        Examples:

            Sequence --- close box with mouse pressed           
            0   escape          27
            1                   91
            2                   77
            3   button+32       pressed  32
            4   x + 33          95
            5   y + 33          39

            Sequence --- close box with mouse released          
            6   escape          27
            7                   91
            8                   77
            9   buttons ?       released 35
            10  x + 33          95
            11  y + 33          39
        '''
##        self.ts_LastCursesGetMouseTuple = curses.getmouse()

##        (mouseId, x, y, z, bstate) = self.ts_LastCursesGetMouseTuple

        mouseId = vt100State[3]

        new_design_not_ready = True

        if new_design_not_ready:

            x = int(vt100State[4] - 33)
            y = int(vt100State[5] - 33)
            z = int(vt100State[9] - 35)
            if (int(vt100State[9] - 35) == 0):
                bstate = curses.BUTTON1_CLICKED
            elif (int(vt100State[9] - 35) == 1):
                bstate = curses.BUTTON2_CLICKED
            elif (int(vt100State[9] - 35) == 2):
                bstate = curses.BUTTON3_CLICKED

        else:

            x_pressed = int(vt100State[4] - 33)
            y_pressed = int(vt100State[5] - 33)
            z_pressed = int(vt100State[9] - 35)

            x_released = int(vt100State[4+6] - 33)
            y_released = int(vt100State[5+6] - 33)
            z_released = int(vt100State[9] - 35)

            x_displacement = int(x_released - x_pressed)
            y_displacement = int(y_released - y_pressed)
            z_displacement = int(z_released - z_pressed)

            x = x_pressed
            y = y_pressed
            z = z_pressed

            if ((x_displacement == 0) and \
                (y_displacement == 0) and \
                (z_displacement == 0)):

                # Simple mouse click
                if (int(vt100State[9] - 35) == 0):
                    bstate = curses.BUTTON1_CLICKED
                elif (int(vt100State[9] - 35) == 1):
                    bstate = curses.BUTTON2_CLICKED
                elif (int(vt100State[9] - 35) == 2):
                    bstate = curses.BUTTON3_CLICKED

            else:

                # Character string selection
                msg = 'Character string selection: ' + \
                      'Pressed = %s; Released = %s' % (
                          str(x_pressed, y_pressed, z_pressed),
                          str(x_released, y_released, z_released))
                self.logger.notice(msg)
                print('NOTICE: %s\n' % msg)

##                if (int(vt100State[9] - 35) == 0):
##                    bstate = curses.BUTTON1_PRESSED
##                elif (vt100State[9] - 35) == 1:
##                    bstate = curses.BUTTON2_PRESSED
##                elif (vt100State[9] - 35) == 2:
##                    bstate = curses.BUTTON3_PRESSED
                if (int(vt100State[9] - 35) == 0):
                    bstate = curses.BUTTON1_CLICKED
                elif (int(vt100State[9] - 35) == 1):
                    bstate = curses.BUTTON2_CLICKED
                elif (int(vt100State[9] - 35) == 2):
                    bstate = curses.BUTTON3_CLICKED

        (triggeringObject,
         objectId,
         objectCriteria) = self.tsThisIsTriggeringObject(
             mouseId, x, y, z, bstate)

        if triggeringObject is None:

            # Curses STDSCR area without associated wxPython GUI object,
            msg = 'Curses STDSCR area without ' + \
                  'associated wxPython GUI object.'
            print('DEBUG: %s' % msg)

        else:

            # Curses STDSCR area with associated wxPython GUI object.
            triggeringEvent = self.tsThisIsTriggeringEvent(
                mouseId, x, y, z, bstate, objectId)

            if DEBUG:

                fmt1 = 'tsWxEventLoop.tsVT100MouseEventGenerator: '
                fmt2 = 'triggeringMouseTuple=%s' % str(
                    self.ts_LastCursesGetMouseTuple)
                fmt3 = 'triggeringObject=%s; id=%d; className=%s' % (
                    str(triggeringObject),
                    triggeringObject.ts_AssignedId,
                    triggeringObject.ts_ClassName)
                msg = fmt1 + fmt2 + fmt3
                self.logger.notice(msg)
                print('NOTICE: %s\n' % msg)

            if triggeringObject.ts_ClassName.lower() == \
               wx.ScrollBarGaugeNameStr.lower():

                triggeringMouseTuple = self.ts_LastCursesGetMouseTuple

            else:

                triggeringMouseTuple = None

            if bypassEventProcessingMode:

                results = self.tsProcessEventTables(
                    objectCriteria=objectCriteria,
                    objectId=objectId,
                    triggeringEvent=triggeringEvent,
                    triggeringObject=triggeringObject)

            else:

                theEvent = Event(
                    id=wx.ID_ANY,
                    callbackUserData=None,
                    canVeto=False,
                    eventCategory=wxEVT_CATEGORY_USER_INPUT,
                    eventCriteria=objectCriteria,
                    eventData=triggeringMouseTuple,
                    eventSource=triggeringObject,
                    eventType=triggeringEvent.EventType,
                    isCommandEvent=False,
                    propagationLevel=wxEVENT_PROPAGATE_NONE,
                    skipped=False,
                    timeStamp=time.time(),
                    veto=False,
                    wasProcessed=False)

                self.ts_RealTimeQueue.Add(theEvent)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
