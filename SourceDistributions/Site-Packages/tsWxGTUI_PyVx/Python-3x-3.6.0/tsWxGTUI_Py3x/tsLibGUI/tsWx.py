#! /usr/bin/env python
# "Time-stamp: <04/09/2015  7:00:51 AM rsg>"
'''
tsWx.py - Module to load all symbols that should appear within
the wxPython.wx emulation namespace. Included are various
classes, constants, functions and methods available for use
by applications built with components from the wxPython emulation
infrastructure.
'''
#################################################################
#
# File: tsWx.py
#
# Purpose:
#
#    Module to load all symbols that should appear within
#    the wxPython.wx emulation namespace. Included are various
#    classes, constants, functions and methods available for use
#    by applications built with toolkit components from the
#    wxPython emulation infrastructure.
#
# Usage (example):
#
#    # Import
#
#    import tsApplication as tsAPP
#    import tsExceptions as tse
#    import tsWx as wx
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
#    None
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
#    2011/12/13 rsg Added tsWxCommandLineEnv library module.
#
#    2012/01/30 rsg Added tsWxScrolled and tsWxScrolledWindow
#                   library modules.
#
#    2012/02/02 rsg Added tsWxScrollBarButton library module.
#
#    2012/02/21 rsg Added tsWxScrollBarGauge library module.
#
#    2012/02/24 rsg Added tsWxScrolledText library module.
#
#    2012/07/05 rsg Added tsWxPasswordEntryDialog and
#                   tsWxTextEntryDialog library modules.
#
#    2012/08/10 rsg Added tsWxTextEditBox library module.
#
#    2012/10/07 rsg Added tsWxNonLinkedList library module.
#
#    2013/03/01 rsg Added import tsLibGUI after tsLibraries was
#                   separated into tsLibGUI and tsLibGUI so that
#                   command line interface applications would no
#                   longer be dependant on Curses modules.
#
#    2013/07/06 rsg Added tsWxFrameButton and tsWxDialogButton.
#
#    2013/09/12 rsg Removed unused items.
#
# ToDo:
#
#    2010/07/31 rsg Used "from tsWxGlobals import *" to
#                   eliminate duplication of symbols that
#                   were already defined in tsWxGlobals.
#
#################################################################

__title__     = 'tsWx'
__version__   = '1.17.0'
__date__      = '09/12/2013'
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

#--------------------------------------------------------------------------

##from tsWxGTUI_Py3x.tsLibCLI import tsCxGlobals

##Troubleshooting = tsCxGlobals.ThemeToUse['Troubleshooting']

##Debug_CLI_Configuration = Troubleshooting['Debug_CLI_Configuration'],
##Debug_CLI_Exceptions = Troubleshooting['Debug_CLI_Exceptions']
##Debug_CLI_Launch = Troubleshooting['Debug_CLI_Launch']
##Debug_CLI_Progress = Troubleshooting['Debug_CLI_Progress']
##Debug_CLI_Termination = Troubleshooting['Debug_CLI_Termination']
##Debug_GUI_Configuration = Troubleshooting['Debug_GUI_Configuration']
##Debug_GUI_Exceptions = Troubleshooting['Debug_GUI_Exceptions']
##Debug_GUI_Launch = Troubleshooting['Debug_GUI_Launch']
##Debug_GUI_Progress = Troubleshooting['Debug_GUI_Progress']
##Debug_GUI_Termination = Troubleshooting['Debug_GUI_Termination']

#---------------------------------------------------------------------------

# Load wxPython emulation specific classes, methods, functions and constants.

# Release candidates suitable for integration with applications.
# Troubleshooting will be required before uncommenting.

# Prototypes suitable for integration with applications.
# from tsWxGTUI_Py3x.tsLibGUI import tsWx

from tsWxGTUI_Py3x.tsLibGUI.tsWxAcceleratorEntry import AcceleratorEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxAcceleratorTable import AcceleratorTable
from tsWxGTUI_Py3x.tsLibGUI.tsWxApp import App
from tsWxGTUI_Py3x.tsLibGUI.tsWxBoxSizer import BoxSizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxButton import Button
from tsWxGTUI_Py3x.tsLibGUI.tsWxCallLater import CallLater
from tsWxGTUI_Py3x.tsLibGUI.tsWxCaret import Caret
from tsWxGTUI_Py3x.tsLibGUI.tsWxCheckBox import CheckBox
from tsWxGTUI_Py3x.tsLibGUI.tsWxChoice import Choice
from tsWxGTUI_Py3x.tsLibGUI.tsWxColor import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxColorDatabase import ColorDatabase
from tsWxGTUI_Py3x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py3x.tsLibGUI.tsWxControlWithItems import ControlWithItems
from tsWxGTUI_Py3x.tsLibGUI.tsWxCursor import Cursor
from tsWxGTUI_Py3x.tsLibGUI.tsWxDebugHandlers import DebugHandlers
from tsWxGTUI_Py3x.tsLibGUI.tsWxDialog import Dialog
from tsWxGTUI_Py3x.tsLibGUI.tsWxDialogButton import DialogButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxDisplay import Display
from tsWxGTUI_Py3x.tsLibGUI.tsWxDoubleLinkedList import DoubleLinkedList
from tsWxGTUI_Py3x.tsLibGUI.tsWxEraseEvent import EraseEvent
from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxEventDaemon import EventDaemon
from tsWxGTUI_Py3x.tsLibGUI.tsWxEventLoop import EventLoop
from tsWxGTUI_Py3x.tsLibGUI.tsWxEventLoopActivator import EventLoopActivator
from tsWxGTUI_Py3x.tsLibGUI.tsWxEventQueueEntry import EventQueueEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxEventTableEntry import EventTableEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxEvtHandler import EvtHandler
from tsWxGTUI_Py3x.tsLibGUI.tsWxFlexGridSizer import FlexGridSizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxFocusEvent import FocusEvent
from tsWxGTUI_Py3x.tsLibGUI.tsWxFrame import Frame
from tsWxGTUI_Py3x.tsLibGUI.tsWxFrameButton import FrameButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxGauge import Gauge
from tsWxGTUI_Py3x.tsLibGUI.tsWxGlobals import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxGraphicalTextUserInterface \
     import GraphicalTextUserInterface
from tsWxGTUI_Py3x.tsLibGUI.tsWxGridBagSizer import GridBagSizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxGridSizer import GridSizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxItemContainer import ItemContainer
from tsWxGTUI_Py3x.tsLibGUI.tsWxKeyEvent import KeyEvent
from tsWxGTUI_Py3x.tsLibGUI.tsWxKeyboardState import KeyboardState
from tsWxGTUI_Py3x.tsLibGUI.tsWxListBox import ListBox
from tsWxGTUI_Py3x.tsLibGUI.tsWxLog import Log
from tsWxGTUI_Py3x.tsLibGUI.tsWxMenu import Menu
from tsWxGTUI_Py3x.tsLibGUI.tsWxMenuBar import MenuBar
from tsWxGTUI_Py3x.tsLibGUI.tsWxMouseEvent import MouseEvent
from tsWxGTUI_Py3x.tsLibGUI.tsWxMouseState import MouseState
from tsWxGTUI_Py3x.tsLibGUI.tsWxMultiFrameEnv import MultiFrameEnv
from tsWxGTUI_Py3x.tsLibGUI.tsWxNonLinkedList import NonLinkedList
from tsWxGTUI_Py3x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py3x.tsLibGUI.tsWxPanel import Panel
from tsWxGTUI_Py3x.tsLibGUI.tsWxPasswordEntryDialog import PasswordEntryDialog
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point
from tsWxGTUI_Py3x.tsLibGUI.tsWxPyApp import PyApp
from tsWxGTUI_Py3x.tsLibGUI.tsWxPyEventBinder import PyEventBinder
from tsWxGTUI_Py3x.tsLibGUI.tsWxPyOnDemandOutputWindow \
     import PyOnDemandOutputWindow
from tsWxGTUI_Py3x.tsLibGUI.tsWxPySimpleApp import PySimpleApp
from tsWxGTUI_Py3x.tsLibGUI.tsWxPySizer import PySizer

from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor16DataBase import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor16SubstitutionMap import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor256DataBase import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor88DataBase import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor8DataBase import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColor8SubstitutionMap import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColorDataBaseRGB import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColorNames import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColorRGBNames import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColorRGBValues import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonMonochromeDataBase import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonPrivateLogger import PrivateLogger
from tsWxGTUI_Py3x.tsLibGUI.tsWxRadioBox import RadioBox
from tsWxGTUI_Py3x.tsLibGUI.tsWxRadioButton import RadioButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect
from tsWxGTUI_Py3x.tsLibGUI.tsWxScreen import Screen
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrollBar import ScrollBar
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrollBarButton import ScrollBarButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrollBarGauge import ScrollBarGauge
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrolled import Scrolled
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrolledText import ScrolledText
from tsWxGTUI_Py3x.tsLibGUI.tsWxScrolledWindow import ScrolledWindow
from tsWxGTUI_Py3x.tsLibGUI.tsWxShowEvent import ShowEvent
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizer import Sizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizerFlags import SizerFlags
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizerItem import SizerItem
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizerItemList import SizerItemList
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizerSpacer import SizerSpacer
from tsWxGTUI_Py3x.tsLibGUI.tsWxSlider import Slider
from tsWxGTUI_Py3x.tsLibGUI.tsWxSplashScreen import SplashScreen
from tsWxGTUI_Py3x.tsLibGUI.tsWxStaticBox import StaticBox
from tsWxGTUI_Py3x.tsLibGUI.tsWxStaticBoxSizer import StaticBoxSizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxStaticLine import StaticLine
from tsWxGTUI_Py3x.tsLibGUI.tsWxStaticText import StaticText
from tsWxGTUI_Py3x.tsLibGUI.tsWxStatusBar import StatusBar
from tsWxGTUI_Py3x.tsLibGUI.tsWxSystemSettings import SystemSettings
from tsWxGTUI_Py3x.tsLibGUI.tsWxTaskBar import TaskBar
from tsWxGTUI_Py3x.tsLibGUI.tsWxTextCtrl import TextCtrl
from tsWxGTUI_Py3x.tsLibGUI.tsWxTextEditBox import TextEditBox
from tsWxGTUI_Py3x.tsLibGUI.tsWxTextEntry import TextEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxTextEntryDialog import TextEntryDialog
from tsWxGTUI_Py3x.tsLibGUI.tsWxTimer import Timer
from tsWxGTUI_Py3x.tsLibGUI.tsWxToggleButton import ToggleButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxTopLevelWindow import TopLevelWindow
from tsWxGTUI_Py3x.tsLibGUI.tsWxValidator import Validator
from tsWxGTUI_Py3x.tsLibGUI.tsWxWindow import Window
from tsWxGTUI_Py3x.tsLibGUI.tsWxWindowCurses import WindowCurses

#---------------------------------------------------------------------------

### Load wxPython application visible constants.

##EVT_DAEMON_TIMETOSLEEP = float(0.200)
##EVT_NULL = 0
##EVT_FIRST = 10000
##EVT_USER_FIRST = EVT_FIRST + 2000

# From _core.py
# Create some event binders
##    EVT_SIZE = tsEvent.EVT_SIZE
##    EVT_SIZING = tsEvent.EVT_SIZING
##    EVT_MOVE = tsEvent.EVT_MOVE
##    EVT_MOVING = tsEvent.EVT_MOVING
##    EVT_CLOSE = tsEvent.EVT_CLOSE
##    EVT_END_SESSION = tsEvent.EVT_END_SESSION
##    EVT_QUERY_END_SESSION = tsEvent.EVT_QUERY_END_SESSION
##    EVT_PAINT = tsEvent.EVT_PAINT
##    EVT_NC_PAINT = tsEvent.EVT_NC_PAINT
##    EVT_ERASE_BACKGROUND = tsEvent.EVT_ERASE_BACKGROUND
##    EVT_CHAR = tsEvent.EVT_CHAR
##    EVT_KEY_DOWN = tsEvent.EVT_KEY_DOWN
##    EVT_KEY_UP = tsEvent.EVT_KEY_UP
##    EVT_HOTKEY = tsEvent.EVT_HOTKEY
##    EVT_CHAR_HOOK = tsEvent.EVT_CHAR_HOOK
##    EVT_MENU_OPEN = tsEvent.EVT_MENU_OPEN
##    EVT_MENU_CLOSE = tsEvent.EVT_MENU_CLOSE
##    EVT_MENU_HIGHLIGHT = tsEvent.EVT_MENU_HIGHLIGHT
##    EVT_MENU_HIGHLIGHT_ALL = tsEvent.EVT_MENU_HIGHLIGHT
##    EVT_SET_FOCUS = tsEvent.EVT_SET_FOCUS
##    EVT_KILL_FOCUS = tsEvent.EVT_KILL_FOCUS
##    EVT_CHILD_FOCUS = tsEvent.EVT_CHILD_FOCUS
##    EVT_ACTIVATE = tsEvent.EVT_ACTIVATE
##    EVT_ACTIVATE_APP = tsEvent.EVT_ACTIVATE_APP
##    EVT_HIBERNATE = tsEvent.EVT_HIBERNATE
##    EVT_DROP_FILES = tsEvent.EVT_DROP_FILES
##    EVT_INIT_DIALOG = tsEvent.EVT_INIT_DIALOG
##    EVT_SYS_COLOUR_CHANGED = tsEvent.EVT_SYS_COLOUR_CHANGED
##    EVT_DISPLAY_CHANGED = tsEvent.EVT_DISPLAY_CHANGED
##    EVT_SHOW = tsEvent.EVT_SHOW
##    EVT_MAXIMIZE = tsEvent.EVT_MAXIMIZE
##    EVT_MINIMIZE = tsEvent.EVT_ICONIZE
##    EVT_RESTOREDOWN = tsEvent.EVT_MAXIMIZE
##    EVT_ICONIZE = tsEvent.EVT_ICONIZE
##    EVT_NAVIGATION_KEY = tsEvent.EVT_NAVIGATION_KEY
##    EVT_PALETTE_CHANGED = tsEvent.EVT_PALETTE_CHANGED
##    EVT_QUERY_NEW_PALETTE = tsEvent.EVT_QUERY_NEW_PALETTE
##    EVT_WINDOW_CREATE = tsEvent.EVT_WINDOW_CREATE
##    EVT_WINDOW_DESTROY = tsEvent.EVT_WINDOW_DESTROY
##    EVT_SET_CURSOR = tsEvent.EVT_SET_CURSOR
##    EVT_MOUSE_CAPTURE_CHANGED = tsEvent.EVT_MOUSE_CAPTURE_CHANGED
##    EVT_MOUSE_CAPTURE_LOST = tsEvent.EVT_MOUSE_CAPTURE_LOST

##    EVT_LEFT_DOWN = tsEvent.EVT_LEFT_DOWN
##    EVT_LEFT_UP = tsEvent.EVT_LEFT_UP
##    EVT_MIDDLE_DOWN = tsEvent.EVT_MIDDLE_DOWN
##    EVT_MIDDLE_UP = tsEvent.EVT_MIDDLE_UP
##    EVT_RIGHT_DOWN = tsEvent.EVT_RIGHT_DOWN
##    EVT_RIGHT_UP = tsEvent.EVT_RIGHT_UP
##    EVT_MOTION = tsEvent.EVT_MOTION
##    EVT_LEFT_DCLICK = tsEvent.EVT_LEFT_DCLICK
##    EVT_MIDDLE_DCLICK = tsEvent.EVT_MIDDLE_DCLICK
##    EVT_RIGHT_DCLICK = tsEvent.EVT_RIGHT_DCLICK
##    EVT_LEAVE_WINDOW = tsEvent.EVT_LEAVE_WINDOW
##    EVT_ENTER_WINDOW = tsEvent.EVT_ENTER_WINDOW
##    EVT_MOUSEWHEEL = tsEvent.EVT_MOUSEWHEEL

##    # All mouse events
##    EVT_MOUSE_EVENTS = tsEvent.EVT_MOUSE_EVENTS
##    # Scrolling from wxWindow (Sent to WxScrolledWindow
##    EVT_SCROLLWIN = tsEvent.EVT_SCROLLWIN

##    EVT_SCROLLWIN_TOP = tsEvent.EVT_SCROLLWIN_TOP
##    EVT_SCROLLWIN_BOTTOM = tsEvent.EVT_SCROLLWIN_BOTTOM
##    EVT_SCROLLWIN_LINEUP = tsEvent.EVT_SCROLLWIN_LINEUP
##    EVT_SCROLLWIN_LINEDOWN = tsEvent.EVT_SCROLLWIN_LINEDOWN
##    EVT_SCROLLWIN_PAGEUP = tsEvent.EVT_SCROLLWIN_PAGEUP
##    EVT_SCROLLWIN_PAGEDOWN = tsEvent.EVT_SCROLLWIN_PAGEDOWN
##    EVT_SCROLLWIN_THUMBTRACK = tsEvent.EVT_SCROLLWIN_THUMBTRACK
##    EVT_SCROLLWIN_THUMBRELEASE = tsEvent.EVT_SCROLLWIN_THUMBRELEASE

##    # Scrolling from wxSlider and wxScrollBar
##    EVT_SCROLL_TOP = tsEvent.EVT_SCROLL_TOP
##    EVT_SCROLL_BOTTOM = tsEvent.EVT_SCROLL_BOTTOM
##    EVT_SCROLL_LINEUP = tsEvent.EVT_SCROLL_LINEUP
##    EVT_SCROLL_LINEDOWN = tsEvent.EVT_SCROLL_LINEDOWN
##    EVT_SCROLL_PAGEUP = tsEvent.EVT_SCROLL_PAGEUP
##    EVT_SCROLL_PAGEDOWN = tsEvent.EVT_SCROLL_PAGEDOWN
##    EVT_SCROLL_THUMBTRACK = tsEvent.EVT_SCROLL_THUMBTRACK
##    EVT_SCROLL_THUMBRELEASE = tsEvent.EVT_SCROLL_THUMBRELEASE
##    EVT_SCROLL_CHANGED = tsEvent.EVT_SCROLL_CHANGED

##    EVT_SCROLL = tsEvent.EVT_SCROLL

##    # Scrolling from sxSlider and sxScrollBar with an id
##    EVT_COMMAND_SCROLL = tsEvent.EVT_COMMAND_SCROLL
##    EVT_COMMAND_SCROLL_TOP = tsEvent.EVT_COMMAND_SCROLL_TOP
##    EVT_COMMAND_SCROLL_BOTTOM = tsEvent.EVT_COMMAND_SCROLL_BOTTOM
##    EVT_COMMAND_SCROLL_LINEUP = tsEvent.EVT_COMMAND_SCROLL_LINEUP
##    EVT_COMMAND_SCROLL_LINEDOWN = tsEvent.EVT_COMMAND_SCROLL_LINEDOWN
##    EVT_COMMAND_SCROLL_PAGEUP = tsEvent.EVT_COMMAND_SCROLL_PAGEUP
##    EVT_COMMAND_SCROLL_PAGEDOWN = tsEvent.EVT_COMMAND_SCROLL_PAGEDOWN
##    EVT_COMMAND_SCROLL_THUMBTRACK = tsEvent.EVT_COMMAND_SCROLL_THUMBTRACK
##    EVT_COMMAND_SCROLL_THUMBRELEASE = tsEvent.EVT_COMMAND_SCROLL_THUMBRELEASE
##    EVT_COMMAND_SCROLL_CHANGED = tsEvent.EVT_COMMAND_SCROLL_CHANGED
##    EVT_COMMAND_SCROLL_ENDSCROLL = EVT_COMMAND_SCROLL_CHANGED

##    EVT_BUTTON = tsEvent.EVT_BUTTON
##    EVT_CHECKBOX = tsEvent.EVT_CHECKBOX
##    EVT_CHOICE = tsEvent.EVT_CHOICE
##    EVT_LISTBOX = tsEvent.EVT_LISTBOX
##    EVT_LISTBOX_DCLICK = tsEvent.EVT_LISTBOX_DCLICK
##    EVT_MENU = tsEvent.EVT_MENU
##    EVT_MENU_RANGE = tsEvent.EVT_MENU_RANGE
##    EVT_SLIDER = tsEvent.EVT_SLIDER
##    EVT_RADIOBOX = tsEvent.EVT_RADIOBOX
##    EVT_RADIOBUTTON = tsEvent.EVT_RADIOBUTTON
##    EVT_SCROLLBAR = tsEvent.EVT_SCROLLBAR
##    EVT_VLBOX = tsEvent.EVT_VLBOX
##    EVT_COMBOBOX = tsEvent.EVT_COMBOBOX
##    EVT_TOOL = tsEvent.EVT_TOOL
##    EVT_TOOL_RANGE = tsEvent.EVT_TOOL_RANGE
##    EVT_TOOL_RCLICKED = tsEvent.EVT_TOOL_RCLICKED
##    EVT_TOOL_RCLICKED_RANGE = tsEvent.EVT_TOOL_RCLICKED_RANGE
##    EVT_TOOL_ENTER = tsEvent.EVT_TOOL_ENTER
##    EVT_CHECKLISTBOX = tsEvent.EVT_CHECKLISTBOX

##    EVT_COMMAND_LEFT_CLICK = tsEvent.EVT_COMMAND_LEFT_CLICK
##    EVT_COMMAND_LEFT_DCLICK = tsEvent.EVT_COMMAND_LEFT_DCLICK
##    EVT_COMMAND_RIGHT_CLICK = tsEvent.EVT_COMMAND_RIGHT_CLICK
##    EVT_COMMAND_RIGHT_DCLICK = tsEvent.EVT_COMMAND_RIGHT_DCLICK
##    EVT_COMMAND_SET_FOCUS = tsEvent.EVT_COMMAND_SET_FOCUS
##    EVT_COMMAND_KILL_FOCUS = tsEvent.EVT_COMMAND_KILL_FOCUS
##    EVT_COMMAND_ENTER = tsEvent.EVT_COMMAND_ENTER

##    EVT_IDLE = tsEvent.EVT_IDLE

##    EVT_UPDATE_UI = tsEvent.EVT_UPDATE_UI
##    EVT_UPDATE_UI_RANGE = tsEvent.EVT_UPDATE_UI_RANGE

##    EVT_CONTEXT_MENU = tsEvent.EVT_CONTEXT_MENU

##    EVT_TEXT_CUT = tsEvent.EVT_TEXT_CUT
##    EVT_TEXT_COPY = tsEvent.EVT_TEXT_COPY
##    EVT_TEXT_PASTE = tsEvent.EVT_TEXT_PASTE

##    # from _misc.py
##    EVT_TIMER = tsEvent.EVT_TIMER
##    EVT_JOY_BUTTON_DOWN = tsEvent.EVT_JOY_BUTTON_DOWN
##    EVT_JOY_BUTTON_UP = tsEvent.EVT_JOY_BUTTON_UP
##    EVT_JOY_MOVE = tsEvent.EVT_JOY_MOVE
##    EVT_JOY_ZMOVE = tsEvent.EVT_JOY_ZMOVE
##    EVT_JOYSTICK_EVENTS = tsEvent.EVT_JOYSTICK_EVENTS

##    # From _controls.py
##    EVT_HELP = tsEvent.EVT_HELP
##    EVT_HELP_RANGE = tsEvent.EVT_HELP_RANGE
##    EVT_DETAILED_HELP = tsEvent.EVT_DETAILED_HELP
##    EVT_DETAILED_HELP_RANGE = tsEvent.EVT_DETAILED_HELP_RANGE

#---------------------------------------------------------------------------

# TBD Need splitter events _windows.py
# TBD Need taskbar events _windows.py
# TBD Need find events _windows.py
# TBD Need text events from _controls.py
# TBD Need spin events from _controls.py
# TBD Need toggle events from _controls.py
# TBD Need notebook events from _controls.py
# TBD Need listbook events from _controls.py
# TBD Need choicebook events from _controls.py
# TBD Need treebook events from _controls.py
# TBD Need toolbox events from _controls.py
# TBD Need list events from _controls.py
# TBD Need tree events from _controls.py
# TBD Need hyperlink event from _controls.py
# TBD Need picker events from _controls.py
# TBD Need panne event from _controls.py
# TBD Need search events from _controls.py
# TBD Need power events from _misc.py
# TBD Need dynamic events from gizmos.py
# TBD Need stc events from stc.py
# TBD Need aui events from aui.py
# TBD Need auinotebook events from aui.py
# TBD Need richtext events from richtext.py
# TBD Need wizard events from wizard.py
# TBD Need webkit events from webkit.py
# TBD Need media events from media.py
# TBD Need html events from html.py
# TBD Need grid events from grid.py
# TBD Need calendar events from calendar.py
# TBD Need flatnotebook events from flatnotebook.py

#---------------------------------------------------------------------------

# TBD Not found
#  Not in wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.) source tree
#  EVT_COMMAND_TEXT_UPDATED = 7
#  EVT_COMMAND_TEXT_ENTER = 8
#  EVT_COMMAND_TEXT_URL = 13
#  EVT_COMMAND_TEXT_MAXLEN = 14
#  EVT_COMMAND_SPINCTRL_UPDATED = 18
#  EVT_NC_LEFT_DOWN = 200
#  EVT_NC_LEFT_UP = 201
#  EVT_NC_MIDDLE_DOWN = 202
#  EVT_NC_MIDDLE_UP = 203
#  EVT_NC_RIGHT_DOWN = 204
#  EVT_NC_RIGHT_UP = 205
#  EVT_NC_MOTION = 206
#  EVT_NC_ENTER_WINDOW = 207
#  EVT_NC_MIDDLE_DCLICK = 210
#  EVT_NC_RIGHT_DCLICK = 211
#  EVT_NC_LEAVE_WINDOW = 208
#  EVT_NC_LEFT_DCLICK = 209
#  EVT_PAINT_ICON = 420
#  EVT_SETTING_CHANGED = 427
#  EVT_DRAW_ITEM = 435
#  EVT_COMPARE_ITEM = 437
#  EVT_MEASURE_ITEM = 436

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
