#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:00:28 AM rsg>"
'''
tsWxEvent.py - Class to establish the structure holding
information about an event that is passed to a callback or
member function. It is an abstract base class for other
event classes.
'''
#################################################################
#
# File: tsWxEvent.py
#
# Purpose:
#
#    Class to establish the structure holding information about
#    an event that is passed to a callback or member function.
#    It is an abstract base class for other event classes.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEvent import Event
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
#    From "wxPython in Action" by Noel Rappin and Robin Dunn, Copyright 2006
#    by Manning Publications Co., 209 Bruce Park Avenue, Greenwich, CT 06830
#    Section 3.1 - What terminology do I need to understand events?
#
#    event type - An integer ID that wxPython adds to every event object.
#                 The event type gives further information about the nature
#                 of the event. For example, the event type of a
#                 wx.MouseEvent indicates whether the event is a mouse click
#                 or a mouse move.
#
#    event source - Any wxPython object that creates events. Examples are
#                 buttons, menu items, list boxes, or any other widget.
#
#    event-driven - A program structure where the bulk of time is spent
#                 waiting for, or responding to, events.
#
#    event queue - A continuously maintained list of events that have already
#                 occurred, but have not yet been processed.
#
#    event handler - A written function or method that is called in response
#                 to an event. Also called a handler function or handler
#                 method.
#
#    event binder - A wxPython object that encapsulates the relationship
#                 between a specific widget, a specific event type, and an
#                 event handler. In order to be invoked, all event handlers
#                 must be registered with an event binder.
#
#    wx.EvtHandler - A wxPython class that allows its instances to create a
#                 binding between an event binder of a specific type, an
#                 event source, and an event handler. Note that the class
#                 wx.EvtHandler is not the same thing as an event handler
#                 function or method defined previously.
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
#    2001/11/27 rsg Add stubs for new wxWidgets methods:
#                   SetSkipped, SetWasProcessed, ShouldProcessOnlyIn,
#                   ShouldPropagate and WasProcessed.
#
#    2011/03/28 rsg Add instance variables "ts_canVeto" and "ts_veto"
#                   and associated methods "CanVeto",  "GetVeto",
#                   "SetCanVeto" and "Veto".
#
#    2012/02/19 rsg Added support for sending EVT_HSCROLLWIN...
#                   and EVT_VSCROLLWIN... from tsWxScrollBar to
#                   tsWxScrolled. This facilitated descrimination
#                   of tsWxScrollBarButton events when the associated
#                   TextCtrl had both horizontal and vertical controls.
#
#    2012/05/21 rsg Added support for eventData to convey instance
#                   specific information from the triggeringObject
#                   that is associacted with the triggeringEvent.
#
#    2012/05/28 rsg Added the "tsWxEvent." prefix to all diagnostic
#                   messages. Modified __init_ definition to
#                   accept parameters or use default values for class
#                   variables unless subsequently overridden.
#
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
#    2013/07/01 rsg Added the following event definitions:
#                   # Aliases for use by Frame Button
#                   wxEVT_MINIMIZE    = wxEVT_ICONIZE,
#                   EVT_MINIMIZE      = EVT_ICONIZE,
#
#                   # Aliases for use by Frame Button
#                   wxEVT_RESTOREDOWN = wxEVT_MAXIMIZE,
#                   EVT_RESTOREDOWN   = EVT_MAXIMIZE
#
#    2013/07/01 rsg Alphabetically sorted binder definitions.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxEvent'
__version__   = '1.7.0'
__date__      = '07/01/2013'
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

import copy
import sys

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py2x.tsLibGUI.tsWxPyEventBinder import PyEventBinder

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

# Load wxPython application visible constants.

EVT_DAEMON_TIMETOSLEEP = float(0.200)
EVT_NULL = 0
EVT_FIRST = 10000
EVT_USER_FIRST = EVT_FIRST + 2000

# From event.h
# Don't propagate at all
wxEVENT_PROPAGATE_NONE = 0
# Propagate until it is processed
wxEVENT_PROPAGATE_MAX = sys.maxint

## this is the category for those events which are generated to update
## the appearance of the GUI but which (usually) do not comport data
## processing, i.e. which do not provide input or output data
## (e.g. size events, scroll events, etc).
## They are events NOT directly generated by the user's input devices.
wxEVT_CATEGORY_UI = 1

## this category groups those events which are generated directly from the
## user through input devices like mouse and keyboard and usually result in
## data to be processed from the application.
## (e.g. mouse clicks, key presses, etc)
wxEVT_CATEGORY_USER_INPUT = 2

## this category is for wxSocketEvent
wxEVT_CATEGORY_SOCKET = 4

## this category is for wxTimerEvent
wxEVT_CATEGORY_TIMER = 8

## this category is for any event used to send notifications from the
## secondary threads to the main one or in general for notifications among
## different threads (which may or may not be user-generated)
wxEVT_CATEGORY_THREAD = 16


## implementation only

## used in the implementations of wxEventLoopBase::YieldFor
wxEVT_CATEGORY_UNKNOWN = 32

## a special category used as an argument to wxEventLoopBase::YieldFor to
## indicate that Yield() should leave all wxEvents on the queue while
## emptying the native event queue (native events will be processed but
## the wxEvents they generate will be queued)
wxEVT_CATEGORY_CLIPBOARD = 64


## shortcut masks

## this category groups those events which are emitted in response to
## events of the native toolkit and which typically are not-"delayable".
##wxEVT_CATEGORY_NATIVE_EVENTS = wxEVT_CATEGORY_UI|wxEVT_CATEGORY_USER_INPUT,

## used in wxEventLoopBase::YieldFor to specify all event categories should
## be processed:
wxEVT_CATEGORY_ALL = wxEVT_CATEGORY_UI| \
                     wxEVT_CATEGORY_USER_INPUT| \
                     wxEVT_CATEGORY_SOCKET| \
                     wxEVT_CATEGORY_TIMER| \
                     wxEVT_CATEGORY_THREAD| \
                     wxEVT_CATEGORY_UNKNOWN| \
                     wxEVT_CATEGORY_CLIPBOARD

# From _core.py
wxEVT_NULL = 0
wxEVT_FIRST = 10000
wxEVT_USER_FIRST = wxEVT_FIRST + 2000

wxEVT_COMMAND_BUTTON_CLICKED = 1
wxEVT_COMMAND_CHECKBOX_CLICKED = 2
wxEVT_COMMAND_CHOICE_SELECTED = 3
wxEVT_COMMAND_LISTBOX_SELECTED = 4
wxEVT_COMMAND_LISTBOX_DOUBLECLICKED = 5
wxEVT_COMMAND_CHECKLISTBOX_TOGGLED = 6
wxEVT_COMMAND_TEXT_UPDATED = 7
wxEVT_COMMAND_TEXT_ENTER = 8
wxEVT_COMMAND_MENU_SELECTED = 9
wxEVT_COMMAND_SLIDER_UPDATED = 10
wxEVT_COMMAND_RADIOBOX_SELECTED = 11
wxEVT_COMMAND_RADIOBUTTON_SELECTED = 12

wxEVT_COMMAND_TEXT_URL = 13
wxEVT_COMMAND_SCROLLBAR_UPDATED = 13

wxEVT_COMMAND_TEXT_MAXLEN = 14
wxEVT_COMMAND_VLBOX_SELECTED = 14

wxEVT_COMMAND_COMBOBOX_SELECTED = 15
wxEVT_COMMAND_TOOL_RCLICKED = 16
wxEVT_COMMAND_TOOL_ENTER = 17
wxEVT_COMMAND_SPINCTRL_UPDATED = 18

wxEVT_TIMER = 80

wxEVT_LEFT_DOWN = 100
wxEVT_LEFT_UP = 101
wxEVT_MIDDLE_DOWN = 102
wxEVT_MIDDLE_UP = 103
wxEVT_RIGHT_DOWN = 104
wxEVT_RIGHT_UP = 105
wxEVT_MOTION = 106
wxEVT_ENTER_WINDOW = 107
wxEVT_LEAVE_WINDOW = 108
wxEVT_LEFT_DCLICK = 109
wxEVT_MIDDLE_DCLICK = 110
wxEVT_RIGHT_DCLICK = 111
wxEVT_SET_FOCUS = 112
wxEVT_KILL_FOCUS = 113
wxEVT_CHILD_FOCUS = 114
wxEVT_MOUSEWHEEL = 115

wxEVT_NC_LEFT_DOWN = 200
wxEVT_NC_LEFT_UP = 201
wxEVT_NC_MIDDLE_DOWN = 202
wxEVT_NC_MIDDLE_UP = 203
wxEVT_NC_RIGHT_DOWN = 204
wxEVT_NC_RIGHT_UP = 205
wxEVT_NC_MOTION = 206
wxEVT_NC_ENTER_WINDOW = 207
wxEVT_NC_LEAVE_WINDOW = 208
wxEVT_NC_LEFT_DCLICK = 209
wxEVT_NC_MIDDLE_DCLICK = 210
wxEVT_NC_RIGHT_DCLICK = 211

wxEVT_CHAR = 212
wxEVT_CHAR_HOOK = 213
wxEVT_NAVIGATION_KEY = 214
wxEVT_KEY_DOWN = 215
wxEVT_KEY_UP = 216
wxEVT_HOTKEY = 217
wxEVT_SET_CURSOR = 230

wxEVT_SCROLL_TOP = 300
wxEVT_SCROLL_BOTTOM = 301
wxEVT_SCROLL_LINEUP = 302
wxEVT_SCROLL_LINEDOWN = 303
wxEVT_SCROLL_PAGEUP = 304
wxEVT_SCROLL_PAGEDOWN = 305
wxEVT_SCROLL_THUMBTRACK = 306
wxEVT_SCROLL_THUMBRELEASE = 307
wxEVT_SCROLL_CHANGED = 308

wxEVT_SCROLLWIN_TOP = 320
wxEVT_SCROLLWIN_BOTTOM = 321
wxEVT_SCROLLWIN_LINEUP = 322
wxEVT_SCROLLWIN_LINEDOWN = 323
wxEVT_SCROLLWIN_PAGEUP = 324
wxEVT_SCROLLWIN_PAGEDOWN = 325
wxEVT_SCROLLWIN_THUMBTRACK = 326
wxEVT_SCROLLWIN_THUMBRELEASE = 327

# Begin tsWxScrolled Extensions (sent from tsWxScrollBar to tsWxScrolled)
wxEVT_HSCROLLWIN_TOP = 330
wxEVT_HSCROLLWIN_BOTTOM = 331
wxEVT_HSCROLLWIN_LINEUP = 332
wxEVT_HSCROLLWIN_LINEDOWN = 333
wxEVT_HSCROLLWIN_PAGEUP = 334
wxEVT_HSCROLLWIN_PAGEDOWN = 335
wxEVT_HSCROLLWIN_THUMBTRACK = 336
wxEVT_HSCROLLWIN_THUMBRELEASE = 337

wxEVT_VSCROLLWIN_TOP = 340
wxEVT_VSCROLLWIN_BOTTOM = 341
wxEVT_VSCROLLWIN_LINEUP = 342
wxEVT_VSCROLLWIN_LINEDOWN = 343
wxEVT_VSCROLLWIN_PAGEUP = 344
wxEVT_VSCROLLWIN_PAGEDOWN = 345
wxEVT_VSCROLLWIN_THUMBTRACK = 346
wxEVT_VSCROLLWIN_THUMBRELEASE = 347
# End tsWxScrolled Extensions (sent from tsWxScrollBar to tsWxScrolled)

wxEVT_SIZE = 400
wxEVT_MOVE = 401
wxEVT_CLOSE_WINDOW = 402
wxEVT_END_SESSION = 403
wxEVT_QUERY_END_SESSION = 404
wxEVT_ACTIVATE_APP = 405
wxEVT_ACTIVATE = 409
wxEVT_CREATE = 410
wxEVT_DESTROY = 411
wxEVT_SHOW = 412

wxEVT_ICONIZE = 413
wxEVT_MINIMIZE = wxEVT_ICONIZE
wxEVT_MAXIMIZE = 414
wxRESTOREDOWN = wxEVT_MAXIMIZE
wxEVT_MOUSE_CAPTURE_CHANGED = 415
wxEVT_MOUSE_CAPTURE_LOST = 416
wxEVT_PAINT = 417
wxEVT_ERASE_BACKGROUND = 418
wxEVT_NC_PAINT = 419
wxEVT_PAINT_ICON = 420
wxEVT_MENU_OPEN = 421
wxEVT_MENU_CLOSE = 422
wxEVT_MENU_HIGHLIGHT = 423
wxEVT_CONTEXT_MENU = 424
wxEVT_SYS_COLOUR_CHANGED = 425
wxEVT_DISPLAY_CHANGED = 426
wxEVT_SETTING_CHANGED = 427
wxEVT_QUERY_NEW_PALETTE = 428
wxEVT_PALETTE_CHANGED = 429
wxEVT_JOY_BUTTON_DOWN = 430
wxEVT_JOY_BUTTON_UP = 431
wxEVT_JOY_MOVE = 432
wxEVT_JOY_ZMOVE = 433
wxEVT_DROP_FILES = 434
wxEVT_DRAW_ITEM = 435
wxEVT_MEASURE_ITEM = 436
wxEVT_COMPARE_ITEM = 437
wxEVT_INIT_DIALOG = 438
wxEVT_IDLE = 439
wxEVT_UPDATE_UI = 440
wxEVT_SIZING = 441
wxEVT_MOVING = 442
wxEVT_HIBERNATE = 443
wxEVT_COMMAND_TEXT_COPY = 444
wxEVT_COMMAND_TEXT_CUT = 445
wxEVT_COMMAND_TEXT_PASTE = 446

wxEVT_COMMAND_LEFT_CLICK = 500
wxEVT_COMMAND_LEFT_DCLICK = 501
wxEVT_COMMAND_RIGHT_CLICK = 502
wxEVT_COMMAND_RIGHT_DCLICK = 503
wxEVT_COMMAND_SET_FOCUS = 504
wxEVT_COMMAND_KILL_FOCUS = 505
wxEVT_COMMAND_ENTER = 506

wxEVT_HELP = 1050
wxEVT_DETAILED_HELP = 1051

wxEVT_COMMAND_TOOL_CLICKED = wxEVT_COMMAND_MENU_SELECTED

#---------------------------------------------------------------------------

# From _core.py
# Create some event binders
EVT_ACTIVATE = PyEventBinder(wxEVT_ACTIVATE)
EVT_ACTIVATE_APP = PyEventBinder(wxEVT_ACTIVATE_APP)
EVT_CHAR = PyEventBinder(wxEVT_CHAR)
EVT_CHAR_HOOK = PyEventBinder(wxEVT_CHAR_HOOK)
EVT_CHILD_FOCUS = PyEventBinder(wxEVT_CHILD_FOCUS)
EVT_CLOSE = PyEventBinder(wxEVT_CLOSE_WINDOW)
EVT_DISPLAY_CHANGED = PyEventBinder(wxEVT_DISPLAY_CHANGED)
EVT_DROP_FILES = PyEventBinder(wxEVT_DROP_FILES)
EVT_END_SESSION = PyEventBinder(wxEVT_END_SESSION)
EVT_ERASE_BACKGROUND = PyEventBinder(wxEVT_ERASE_BACKGROUND)
EVT_HIBERNATE = PyEventBinder(wxEVT_HIBERNATE)
EVT_HOTKEY = PyEventBinder(wxEVT_HOTKEY, 1)
EVT_ICONIZE = PyEventBinder(wxEVT_ICONIZE)
EVT_INIT_DIALOG = PyEventBinder(wxEVT_INIT_DIALOG)
EVT_KEY_DOWN = PyEventBinder(wxEVT_KEY_DOWN)
EVT_KEY_UP = PyEventBinder(wxEVT_KEY_UP)
EVT_KILL_FOCUS = PyEventBinder(wxEVT_KILL_FOCUS)
EVT_MAXIMIZE = PyEventBinder(wxEVT_MAXIMIZE)
EVT_MENU_CLOSE = PyEventBinder(wxEVT_MENU_CLOSE)
EVT_MENU_HIGHLIGHT = PyEventBinder(wxEVT_MENU_HIGHLIGHT, 1)
EVT_MENU_HIGHLIGHT_ALL = PyEventBinder(wxEVT_MENU_HIGHLIGHT)
EVT_MENU_OPEN = PyEventBinder(wxEVT_MENU_OPEN)
EVT_MINIMIZE = PyEventBinder(wxEVT_ICONIZE)
EVT_MOUSE_CAPTURE_CHANGED = PyEventBinder(wxEVT_MOUSE_CAPTURE_CHANGED)
EVT_MOUSE_CAPTURE_LOST = PyEventBinder(wxEVT_MOUSE_CAPTURE_LOST)
EVT_MOVE = PyEventBinder(wxEVT_MOVE)
EVT_MOVING = PyEventBinder(wxEVT_MOVING)
EVT_NAVIGATION_KEY = PyEventBinder(wxEVT_NAVIGATION_KEY)
EVT_NC_PAINT = PyEventBinder(wxEVT_NC_PAINT)
EVT_PAINT = PyEventBinder(wxEVT_PAINT)
EVT_PALETTE_CHANGED = PyEventBinder(wxEVT_PALETTE_CHANGED)
EVT_QUERY_END_SESSION = PyEventBinder(wxEVT_QUERY_END_SESSION)
EVT_QUERY_NEW_PALETTE = PyEventBinder(wxEVT_QUERY_NEW_PALETTE)
EVT_RESTOREDOWN = EVT_MAXIMIZE
EVT_SET_CURSOR = PyEventBinder(wxEVT_SET_CURSOR)
EVT_SET_FOCUS = PyEventBinder(wxEVT_SET_FOCUS)
EVT_SHOW = PyEventBinder(wxEVT_SHOW)
EVT_SIZE = PyEventBinder(wxEVT_SIZE)
EVT_SIZING = PyEventBinder(wxEVT_SIZING)
EVT_SYS_COLOUR_CHANGED = PyEventBinder(wxEVT_SYS_COLOUR_CHANGED)
EVT_WINDOW_CREATE = PyEventBinder(wxEVT_CREATE)
EVT_WINDOW_DESTROY = PyEventBinder(wxEVT_DESTROY)

EVT_ENTER_WINDOW = PyEventBinder(wxEVT_ENTER_WINDOW)
EVT_LEAVE_WINDOW = PyEventBinder(wxEVT_LEAVE_WINDOW)
EVT_LEFT_DCLICK = PyEventBinder(wxEVT_LEFT_DCLICK)
EVT_LEFT_DOWN = PyEventBinder(wxEVT_LEFT_DOWN)
EVT_LEFT_UP = PyEventBinder(wxEVT_LEFT_UP)
EVT_MIDDLE_DCLICK = PyEventBinder(wxEVT_MIDDLE_DCLICK)
EVT_MIDDLE_DOWN = PyEventBinder(wxEVT_MIDDLE_DOWN)
EVT_MIDDLE_UP = PyEventBinder(wxEVT_MIDDLE_UP)
EVT_MOTION = PyEventBinder(wxEVT_MOTION)
EVT_MOUSEWHEEL = PyEventBinder(wxEVT_MOUSEWHEEL)
EVT_RIGHT_DCLICK = PyEventBinder(wxEVT_RIGHT_DCLICK)
EVT_RIGHT_DOWN = PyEventBinder(wxEVT_RIGHT_DOWN)
EVT_RIGHT_UP = PyEventBinder(wxEVT_RIGHT_UP)

# All mouse events
EVT_MOUSE_EVENTS = PyEventBinder([wxEVT_LEFT_DOWN,
                                  wxEVT_LEFT_UP,
                                  wxEVT_MIDDLE_DOWN,
                                  wxEVT_MIDDLE_UP,
                                  wxEVT_RIGHT_DOWN,
                                  wxEVT_RIGHT_UP,
                                  wxEVT_MOTION,
                                  wxEVT_LEFT_DCLICK,
                                  wxEVT_MIDDLE_DCLICK,
                                  wxEVT_RIGHT_DCLICK,
                                  wxEVT_LEAVE_WINDOW,
                                  wxEVT_ENTER_WINDOW,
                                  wxEVT_MOUSEWHEEL])
# Scrolling from wxWindow (Sent to WxScrolledWindow)
EVT_SCROLLWIN = PyEventBinder([wxEVT_SCROLLWIN_TOP,
                               wxEVT_SCROLLWIN_BOTTOM,
                               wxEVT_SCROLLWIN_LINEUP,
                               wxEVT_SCROLLWIN_LINEDOWN,
                               wxEVT_SCROLLWIN_PAGEUP,
                               wxEVT_SCROLLWIN_PAGEDOWN,
                               wxEVT_SCROLLWIN_THUMBTRACK,
                               wxEVT_SCROLLWIN_THUMBRELEASE])

EVT_SCROLLWIN_TOP = PyEventBinder(wxEVT_SCROLLWIN_TOP)
EVT_SCROLLWIN_BOTTOM = PyEventBinder(wxEVT_SCROLLWIN_BOTTOM)
EVT_SCROLLWIN_LINEUP = PyEventBinder(wxEVT_SCROLLWIN_LINEUP)
EVT_SCROLLWIN_LINEDOWN = PyEventBinder(wxEVT_SCROLLWIN_LINEDOWN)
EVT_SCROLLWIN_PAGEUP = PyEventBinder(wxEVT_SCROLLWIN_PAGEUP)
EVT_SCROLLWIN_PAGEDOWN = PyEventBinder(wxEVT_SCROLLWIN_PAGEDOWN)
EVT_SCROLLWIN_THUMBTRACK = PyEventBinder(wxEVT_SCROLLWIN_THUMBTRACK)
EVT_SCROLLWIN_THUMBRELEASE = PyEventBinder(wxEVT_SCROLLWIN_THUMBRELEASE)

# Begin tsWxScrolled Extensions (sent from tsWxScrollBar to tsWxScrolled)
EVT_HSCROLLWIN = PyEventBinder([wxEVT_HSCROLLWIN_TOP,
                                wxEVT_HSCROLLWIN_BOTTOM,
                                wxEVT_HSCROLLWIN_LINEUP,
                                wxEVT_HSCROLLWIN_LINEDOWN,
                                wxEVT_HSCROLLWIN_PAGEUP,
                                wxEVT_HSCROLLWIN_PAGEDOWN,
                                wxEVT_HSCROLLWIN_THUMBTRACK,
                                wxEVT_HSCROLLWIN_THUMBRELEASE])

EVT_HSCROLLWIN_TOP = PyEventBinder(wxEVT_HSCROLLWIN_TOP)
EVT_HSCROLLWIN_BOTTOM = PyEventBinder(wxEVT_HSCROLLWIN_BOTTOM)
EVT_HSCROLLWIN_LINEUP = PyEventBinder(wxEVT_HSCROLLWIN_LINEUP)
EVT_HSCROLLWIN_LINEDOWN = PyEventBinder(wxEVT_HSCROLLWIN_LINEDOWN)
EVT_HSCROLLWIN_PAGEUP = PyEventBinder(wxEVT_HSCROLLWIN_PAGEUP)
EVT_HSCROLLWIN_PAGEDOWN = PyEventBinder(wxEVT_HSCROLLWIN_PAGEDOWN)
EVT_HSCROLLWIN_THUMBTRACK = PyEventBinder(wxEVT_HSCROLLWIN_THUMBTRACK)
EVT_HSCROLLWIN_THUMBRELEASE = PyEventBinder(wxEVT_SCROLLWIN_THUMBRELEASE)

EVT_VSCROLLWIN = PyEventBinder([wxEVT_VSCROLLWIN_TOP,
                                wxEVT_VSCROLLWIN_BOTTOM,
                                wxEVT_VSCROLLWIN_LINEUP,
                                wxEVT_VSCROLLWIN_LINEDOWN,
                                wxEVT_VSCROLLWIN_PAGEUP,
                                wxEVT_VSCROLLWIN_PAGEDOWN,
                                wxEVT_VSCROLLWIN_THUMBTRACK,
                                wxEVT_VSCROLLWIN_THUMBRELEASE])

EVT_VSCROLLWIN_TOP = PyEventBinder(wxEVT_VSCROLLWIN_TOP)
EVT_VSCROLLWIN_BOTTOM = PyEventBinder(wxEVT_VSCROLLWIN_BOTTOM)
EVT_VSCROLLWIN_LINEUP = PyEventBinder(wxEVT_VSCROLLWIN_LINEUP)
EVT_VSCROLLWIN_LINEDOWN = PyEventBinder(wxEVT_VSCROLLWIN_LINEDOWN)
EVT_VSCROLLWIN_PAGEUP = PyEventBinder(wxEVT_VSCROLLWIN_PAGEUP)
EVT_VSCROLLWIN_PAGEDOWN = PyEventBinder(wxEVT_VSCROLLWIN_PAGEDOWN)
EVT_VSCROLLWIN_THUMBTRACK = PyEventBinder(wxEVT_VSCROLLWIN_THUMBTRACK)
EVT_VSCROLLWIN_THUMBRELEASE = PyEventBinder(wxEVT_VSCROLLWIN_THUMBRELEASE)
# End tsWxScrolled Extensions (sent from tsWxScrollBar to tsWxScrolled)

# Scrolling from wxSlider and wxScrollBar
EVT_SCROLL_TOP = PyEventBinder(wxEVT_SCROLL_TOP)
EVT_SCROLL_BOTTOM = PyEventBinder(wxEVT_SCROLL_BOTTOM)
EVT_SCROLL_LINEUP = PyEventBinder(wxEVT_SCROLL_LINEUP)
EVT_SCROLL_LINEDOWN = PyEventBinder(wxEVT_SCROLL_LINEDOWN)
EVT_SCROLL_PAGEUP = PyEventBinder(wxEVT_SCROLL_PAGEUP)
EVT_SCROLL_PAGEDOWN = PyEventBinder(wxEVT_SCROLL_PAGEDOWN)
EVT_SCROLL_THUMBTRACK = PyEventBinder(wxEVT_SCROLL_THUMBTRACK)
EVT_SCROLL_THUMBRELEASE = PyEventBinder(wxEVT_SCROLL_THUMBRELEASE)
EVT_SCROLL_CHANGED = PyEventBinder(wxEVT_SCROLL_CHANGED)

EVT_SCROLL = PyEventBinder([wxEVT_SCROLL_TOP,
                            wxEVT_SCROLL_BOTTOM,
                            wxEVT_SCROLL_LINEUP,
                            wxEVT_SCROLL_LINEDOWN,
                            wxEVT_SCROLL_PAGEUP,
                            wxEVT_SCROLL_PAGEDOWN,
                            wxEVT_SCROLL_THUMBTRACK,
                            wxEVT_SCROLL_THUMBRELEASE,
                            wxEVT_SCROLL_CHANGED])

# Scrolling from sxSlider and sxScrollBar with an id
EVT_COMMAND_SCROLL = PyEventBinder([wxEVT_SCROLL_TOP,
                                    wxEVT_SCROLL_BOTTOM,
                                    wxEVT_SCROLL_LINEUP,
                                    wxEVT_SCROLL_LINEDOWN,
                                    wxEVT_SCROLL_PAGEUP,
                                    wxEVT_SCROLL_PAGEDOWN,
                                    wxEVT_SCROLL_THUMBTRACK,
                                    wxEVT_SCROLL_THUMBRELEASE,
                                    wxEVT_SCROLL_CHANGED], 1)

EVT_COMMAND_SCROLL_TOP = PyEventBinder(wxEVT_SCROLL_TOP, 1)
EVT_COMMAND_SCROLL_BOTTOM = PyEventBinder(wxEVT_SCROLL_BOTTOM, 1)
EVT_COMMAND_SCROLL_LINEUP = PyEventBinder(wxEVT_SCROLL_LINEUP, 1)
EVT_COMMAND_SCROLL_LINEDOWN = PyEventBinder(wxEVT_SCROLL_LINEDOWN, 1)
EVT_COMMAND_SCROLL_PAGEUP = PyEventBinder(wxEVT_SCROLL_PAGEUP, 1)
EVT_COMMAND_SCROLL_PAGEDOWN = PyEventBinder(wxEVT_SCROLL_PAGEDOWN, 1)
EVT_COMMAND_SCROLL_THUMBTRACK = PyEventBinder(wxEVT_SCROLL_THUMBTRACK, 1)
EVT_COMMAND_SCROLL_THUMBRELEASE = PyEventBinder(wxEVT_SCROLL_THUMBRELEASE, 1)
EVT_COMMAND_SCROLL_CHANGED = PyEventBinder(wxEVT_SCROLL_CHANGED, 1)
EVT_COMMAND_SCROLL_ENDSCROLL = EVT_COMMAND_SCROLL_CHANGED

EVT_BUTTON = PyEventBinder(wxEVT_COMMAND_BUTTON_CLICKED, 1)
EVT_CHECKBOX = PyEventBinder(wxEVT_COMMAND_CHECKBOX_CLICKED, 1)
EVT_CHOICE = PyEventBinder(wxEVT_COMMAND_CHOICE_SELECTED, 1)
EVT_LISTBOX = PyEventBinder(wxEVT_COMMAND_LISTBOX_SELECTED, 1)
EVT_LISTBOX_DCLICK = PyEventBinder(wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, 1)
EVT_MENU = PyEventBinder(wxEVT_COMMAND_MENU_SELECTED, 1)
EVT_MENU_RANGE = PyEventBinder(wxEVT_COMMAND_MENU_SELECTED, 2)
EVT_SLIDER = PyEventBinder(wxEVT_COMMAND_SLIDER_UPDATED, 1)
EVT_RADIOBOX = PyEventBinder(wxEVT_COMMAND_RADIOBOX_SELECTED, 1)
EVT_RADIOBUTTON = PyEventBinder(wxEVT_COMMAND_RADIOBUTTON_SELECTED, 1)

EVT_SCROLLBAR = PyEventBinder(wxEVT_COMMAND_SCROLLBAR_UPDATED, 1)
EVT_VLBOX = PyEventBinder(wxEVT_COMMAND_VLBOX_SELECTED, 1)
EVT_COMBOBOX = PyEventBinder(wxEVT_COMMAND_COMBOBOX_SELECTED, 1)
EVT_TOOL = PyEventBinder(wxEVT_COMMAND_TOOL_CLICKED, 1)
EVT_TOOL_RANGE = PyEventBinder(wxEVT_COMMAND_TOOL_CLICKED, 2)
EVT_TOOL_RCLICKED = PyEventBinder(wxEVT_COMMAND_TOOL_RCLICKED, 1)
EVT_TOOL_RCLICKED_RANGE = PyEventBinder(wxEVT_COMMAND_TOOL_RCLICKED, 2)
EVT_TOOL_ENTER = PyEventBinder(wxEVT_COMMAND_TOOL_ENTER, 1)
EVT_CHECKLISTBOX = PyEventBinder(wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, 1)

EVT_COMMAND_LEFT_CLICK = PyEventBinder(wxEVT_COMMAND_LEFT_CLICK, 1)
EVT_COMMAND_LEFT_DCLICK = PyEventBinder(wxEVT_COMMAND_LEFT_DCLICK, 1)
EVT_COMMAND_RIGHT_CLICK = PyEventBinder(wxEVT_COMMAND_RIGHT_CLICK, 1)
EVT_COMMAND_RIGHT_DCLICK = PyEventBinder(wxEVT_COMMAND_RIGHT_DCLICK, 1)
EVT_COMMAND_SET_FOCUS = PyEventBinder(wxEVT_COMMAND_SET_FOCUS, 1)
EVT_COMMAND_KILL_FOCUS = PyEventBinder(wxEVT_COMMAND_KILL_FOCUS, 1)
EVT_COMMAND_ENTER = PyEventBinder(wxEVT_COMMAND_ENTER, 1)

EVT_IDLE = PyEventBinder(wxEVT_IDLE)

EVT_UPDATE_UI = PyEventBinder(wxEVT_UPDATE_UI, 1)
EVT_UPDATE_UI_RANGE = PyEventBinder(wxEVT_UPDATE_UI, 2)

EVT_CONTEXT_MENU = PyEventBinder(wxEVT_CONTEXT_MENU)

EVT_TEXT_CUT = PyEventBinder(wxEVT_COMMAND_TEXT_CUT)
EVT_TEXT_COPY = PyEventBinder(wxEVT_COMMAND_TEXT_COPY)
EVT_TEXT_PASTE = PyEventBinder(wxEVT_COMMAND_TEXT_PASTE)

# from _misc.py
EVT_TIMER = PyEventBinder(wxEVT_TIMER, 1)
EVT_JOY_BUTTON_DOWN = PyEventBinder(wxEVT_JOY_BUTTON_DOWN)
EVT_JOY_BUTTON_UP = PyEventBinder(wxEVT_JOY_BUTTON_UP)
EVT_JOY_MOVE = PyEventBinder(wxEVT_JOY_MOVE)
EVT_JOY_ZMOVE = PyEventBinder(wxEVT_JOY_ZMOVE)
EVT_JOYSTICK_EVENTS = PyEventBinder([wxEVT_JOY_BUTTON_DOWN,
                                     wxEVT_JOY_BUTTON_UP,
                                     wxEVT_JOY_MOVE,
                                     wxEVT_JOY_ZMOVE])

# From _controls.py
EVT_HELP = PyEventBinder(wxEVT_HELP, 1)
EVT_HELP_RANGE = PyEventBinder(wxEVT_HELP, 2)
EVT_DETAILED_HELP = PyEventBinder(wxEVT_DETAILED_HELP, 1)
EVT_DETAILED_HELP_RANGE = PyEventBinder(wxEVT_DETAILED_HELP, 2)

#---------------------------------------------------------------------------

def EVT_COMMAND(win, id, cmd, func):
    '''
    Does not fit PyEventBinder.
    '''
    win.Connect(id, -1, cmd, func)

#---------------------------------------------------------------------------

def EVT_COMMAND_RANGE(win, id1, id2, cmd, func):
    '''
    Does not fit PyEventBinder.
    '''
    win.Connect(id1, id2, cmd, func)

#---------------------------------------------------------------------------

class Event(Object):
    '''
    An event is a structure holding information about an event passed to
    a callback or member function. wx.Event is an abstract base class for
    other event classes.
    '''
    # Define Class Variables
    CurrentEvtId = wxEVT_NULL # Initialize the set of unique Event IDs

    def __init__(self,
                 id=wx.ID_ANY,
                 callbackUserData=None,
                 canVeto=False,
                 eventCategory=wxEVT_CATEGORY_UI,
                 eventCriteria=None,
                 eventData=None,
                 eventObject=None, # added
                 eventSource=None, # Deprecated ???
                 eventType=None,
                 handlerToProcessOnlyIn=None, # added
                 isCommandEvent=False,
                 propagationLevel=wxEVENT_PROPAGATE_NONE,
                 skipped=False,
                 timeStamp=0L,
                 veto=False,
                 wasProcessed=False):
        '''
        Constructor.
        '''
        theClass = 'Event'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        self.ts_id = id

        self.ts_CanVeto = canVeto
        self.ts_Veto = veto
        self.ts_callbackUserData = callbackUserData
        self.ts_EventCategory = eventCategory
        self.ts_EventCriteria = eventCriteria
        self.ts_EventData = eventData
        self.ts_EventSource = eventSource
        self.ts_EventType = eventType
        self.ts_isCommandEvent = False

        # Indicates how many levels the event can propagate.
        # This member is protected and should typically only be set in the
        # constructors of the derived classes. It may be temporarily changed
        # by StopPropagation() and ResumePropagation() and tested with
        # ShouldPropagate().
        #
        # The initial value is set to either wxEVENT_PROPAGATE_NONE
        # (by default) meaning that the event shouldn't be propagated at all
        # or to wxEVENT_PROPAGATE_MAX (for command events) meaning that it
        # should be propagated as much as necessary.
        #
        # Any positive number means that the event should be propagated but
        # no more than the given number of times. E.g. the propagation level
        # may be set to 1 to propagate the event to its parent only, but not
        # to its grandparent.
        self.ts_propagationLevel = wxEVENT_PROPAGATE_NONE

        self.ts_skipped = skipped
        self.ts_timeStamp = timeStamp
        self.ts_wasProcessed = wasProcessed

##        self.thisown = theClass

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def CanVeto(self):
        '''
        '''
        return (self.ts_CanVeto)

    #-----------------------------------------------------------------------

    def Clone(self):
        '''
        Returns a copy of the event.

        Any event that is posted to the wxWidgets event system for later
        action (via wxEvtHandler::AddPendingEvent, wxEvtHandler::QueueEvent
        or wxPostEvent()) must implement this method.

        All wxWidgets events fully implement this method, but any derived
        events implemented by the user should also implement this method
        just in case they (or some event derived from them) are ever posted.

        All wxWidgets events implement a copy constructor, so the easiest
        way of implementing the Clone function is to implement a copy
        constructor for a new event (call it MyEvent) and then define the
        Clone function like this:

        wxEvent *Clone() const { return new MyEvent(*this); }
        '''
        theClone = copy.copy(self)
        self.logger.debug(
            'tsWxEvent.theClone %s (%s).' % (
                theClone.ClassName, id(theClone)))
        return (theClone)

    #-----------------------------------------------------------------------

    def GetEventCategory(self):
        '''
        Returns a generic category for this event.

        wxEvent implementation returns wxEVT_CATEGORY_UI by default.

        This function is used to selectively process events in
        wxEventLoopBase::YieldFor.
        '''
        self.logger.debug(
            'tsWxEvent.GetEventCategory %s (%s).' % (
                self, self.ts_EventCategory))
        return (self.ts_EventCategory)

    #-----------------------------------------------------------------------

    def GetEventCriteria(self):
        '''
        Returns the criteria for generating this event.

        wxEvent implementation returns None by default.
        '''
        self.logger.debug(
            'tsWxEvent.GetEventCriteria %s (%s).' % (
                self, str(self.ts_EventCriteria)))
        return (self.ts_EventCriteria)

    #-----------------------------------------------------------------------

    def GetEventData(self):
        '''
        Returns instance specific data for this event.
        '''
        self.logger.debug(
            'tsWxEvent.GetEventData %s (%s).' % (
                self, str(self.ts_EventData)))
        return (self.ts_EventData)

    #-----------------------------------------------------------------------

    def GetEventSource(self):
        '''
        Returns the identifier of the given event source.
        '''
        self.logger.debug(
            'tsWxEvent.GetEventSource %s (%s).' % (
                self, self.ts_EventSource))
        return (self.ts_EventSource)

    #-----------------------------------------------------------------------

    def GetEventType(self):
        '''
        Returns the identifier of the given event type, such as
        wxEVT_COMMAND_BUTTON_CLICKED.
        '''
        self.logger.debug(
            'tsWxEvent.GetEventType %s (%s).' % (
                self, self.ts_EventType))
        return (self.ts_EventType)

    #-----------------------------------------------------------------------

    def GetId(self):
        '''
        Returns the identifier associated with this event, such as a button
        command id.
        '''
        self.logger.debug(
            'tsWxEvent.GetId %s (%s).' % (self, self.ts_id))
        return (self.ts_id)

    #-----------------------------------------------------------------------

    def GetSkipped(self):
        '''
        Returns true if the event handler should be skipped, false otherwise.
        '''
        self.logger.debug(
            'tsWxEvent.GetSkipped %s (%s).' % (self, self.ts_skipped))
        return (self.ts_skipped)

    #-----------------------------------------------------------------------

    def GetTimestamp(self):
        '''
        Gets the timestamp for the event.

        The timestamp is the time in milliseconds since some fixed moment
        (not necessarily the standard Unix Epoch, so only differences
        between the timestamps and not their absolute values usually make
        sense).

        Warning:

        wxWidgets returns a non-NULL timestamp only for mouse and key
        events (see wxMouseEvent and wxKeyEvent).
        '''
        self.logger.debug(
            'tsWxEvent.GetTimestamp %s (%s).' % (self, self.ts_timeStamp))
        return (self.ts_timeStamp)

    #-----------------------------------------------------------------------

    def GetVeto(self):
        '''
        '''
        if (self.ts_CanVeto and \
            self.ts_Veto):

            veto = True

        else:

            veto = False

        return (veto)

    #-----------------------------------------------------------------------

    def IsCommandEvent(self):
        '''
        Returns true if the event is or is derived from wxCommandEvent
        else it returns false.

        Note: Exists only for optimization purposes.
        '''
        self.logger.debug(
            'tsWxEvent.IsCommandEvent %s (%s).' % (
                self, self.ts_isCommandEvent))
        return (self.ts_isCommandEvent)

    #-----------------------------------------------------------------------

    def ResumePropagation(self, propagationLevel):
        '''
        Sets the propagation level to the given value (for example returned
        from an earlier call to wxEvent::StopPropagation).
        '''
        self.logger.debug(
            'tsWxEvent.ResumePropagation %s (%s).' % (
                self, propagationLevel))
        self.ts_propagationLevel = propagationLevel

    #-----------------------------------------------------------------------

    def SetCanVeto(self, canVeto=True):
        '''
        '''
        self.ts_CanVeto = canVeto

    #-----------------------------------------------------------------------

    def SetEventCategory(self, category=wxEVT_CATEGORY_UI):
        '''
        Sets the category forthis event.

        wxEvent implementation sets wxEVT_CATEGORY_UI by default.
        '''
        self.logger.debug(
            'tsWxEvent.SetEventCcategory %s (%s).' % (
                self, str(category)))
        self.ts_EventCategory = category

    #-----------------------------------------------------------------------

    def SetEventCriteria(self, criteria=None):
        '''
        Sets the criteria for generating this event.

        wxEvent implementation sets None by default.
        '''
        self.logger.debug(
            'tsWxEvent.SetEventCriteria %s (%s).' % (
                self, str(criteria)))
        self.ts_EventCriteria = criteria

    #-----------------------------------------------------------------------

    def SetEventData(self, data):
        '''
        Sets the event data.
        '''
        self.logger.debug(
            'tsWxEvent.SetEventData %s (%s).' % (self, str(data)))
        self.ts_EventData = data

    #-----------------------------------------------------------------------

    def SetEventSource(self, src):
        '''
        Sets the event source.
        '''
        self.logger.debug(
            'tsWxEvent.SetEventSource %s (%s).' % (self, src))
        self.ts_EventSource = src

    #-----------------------------------------------------------------------

    def SetEventType(self, typ):
        '''
        Sets the event type.
        '''
        self.logger.debug(
            'tsWxEvent.SetEventType %s (%s).' % (self, typ))
        self.ts_EventType = typ

    #-----------------------------------------------------------------------

    def SetId(self, id):
        '''
        Sets the identifier associated with this event, such as a button
        command id.
        '''
        self.logger.debug(
            'tsWxEvent.SetId %s (%s).' % (self, id))
        self.ts_id = id

    #-----------------------------------------------------------------------

    def SetSkipped(self, skip):
        '''
        '''
        self.logger.debug(
            'tsWxEvent.SetSkipped %s (%s).' % (self, skip))
        self.ts_skipped = skip

    #-----------------------------------------------------------------------

    def SetTimestamp(self, ts):
        '''
        Sets the timestamp for the event.
        '''
        self.logger.debug(
            'tsWxEvent.SetTimestamp %s (%s).' % (self, ts))
        self.ts_timeStamp = ts

    #-----------------------------------------------------------------------

    def SetWasProcessed(self, processed):
        '''
        '''
        self.logger.debug(
            'tsWxEvent.SetWasProcessed %s (%s).' % (self, processed))
        self.ts_wasProcessed = processed

    #-----------------------------------------------------------------------

    def ShouldProcessOnlyIn(self):
        '''
        '''
        status = False
        self.logger.debug(
            'tsWxEvent.ShouldProcessOnlyIn %s; status=%s.' % (self, status))
        return (status)

    #-----------------------------------------------------------------------

    def ShouldPropagate(self):
        '''
        Test if this event should be propagated or not, i.e.
        if the propagation level is currently greater than 0.
        '''
        self.logger.debug(
            'tsWxEvent.ShouldPropagate %s (%s).' % (
                self, self.ts_propagationLevel))
        if self.ts_propagationLevel > 0:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def Skip(self, skip=True):
        '''
        This method can be used inside an event handler to control whether
        further event handlers bound to this event will be called after the
        current one returns.

        Without Skip() (or equivalently if Skip(false) is used), the event
        will not be processed any more. If Skip(true) is called, the event
        processing system continues searching for a further handler function
        for this event, even though it has been processed already in the
        current handler.

        In general, it is recommended to skip all non-command events to allow
        the default handling to take place. The command events are, however,
        normally not skipped as usually a single command such as a button
        click or menu item selection must only be processed by one handler.
        '''
        self.logger.debug(
            'tsWxEvent.Skip %s (%s).' % (self, skip))
        self.ts_skipped = skip

    #-----------------------------------------------------------------------

    def StopPropagation(self):
        '''
        Stop the event from propagating to its parent window.

        Returns the old propagation level value which may be later passed
        to ResumePropagation() to allow propagating the event again.
        '''
        self.logger.debug(
            'tsWxEvent.StopPropagation %s (%s).' % (
                self, self.ts_propagationLevel))
        temp = self.ts_propagationLevel
        self.ts_propagationLevel = 0
        return (temp)

    #-----------------------------------------------------------------------

    def Veto(self, veto=True):
        '''
        '''
        # GetVeto() will return false anyhow...
        self.logger.wxCHECK_RET(
            self.ts_CanVeto,
            'call to Veto() ignored (cannot veto this event)')
        self.ts_Veto = veto

    #-----------------------------------------------------------------------

    def WasProcessed(self):
        '''
        '''
        status = self.ts_wasProcessed
        self.logger.debug(
            'tsWxEvent.WasProcessed %s; status=%s.' % (self, status))
        return (status)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    @staticmethod
    def tsNewEvtId():
        '''
        Create a unique ID.
        '''
        # skip the part of IDs space that contains hard-coded values:
        if (Event.CurrentEvtId < wx.EVT_USER_FIRST):
            Event.CurrentEvtId = wx.EVT_USER_FIRST
        else:
            Event.CurrentEvtId += 1

        return (Event.CurrentEvtId)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetCurrentEvtId():
        '''
        Return latest ID.
        '''
        return (Event.CurrentEvtId)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsRegisterId(usedId):
        '''
        Adjust latest ID to reflect specified new one.
        '''
        if (usedId > Event.CurrentEvtId):
            Event.CurrentEvtId = usedId

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    EventCriteria = property(GetEventCriteria, SetEventCriteria)
    EventData = property(GetEventData, SetEventData)
    EventTimestamp = property(GetTimestamp, SetTimestamp)
    EventSource = property(GetEventSource, SetEventSource)
    EventType = property(GetEventType, SetEventType)
    Id = property(GetId, SetId)
    Skipped = property(GetSkipped)
##    thisown: The membership flag
    Timestamp = property(GetTimestamp, SetTimestamp)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
