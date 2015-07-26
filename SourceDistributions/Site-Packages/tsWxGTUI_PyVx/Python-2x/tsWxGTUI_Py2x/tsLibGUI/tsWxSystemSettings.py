#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:26:48 AM rsg>"
'''
tsWxSystemSettings.py - Class allows the application to ask for
details about the system. This can include settings such as
standard colours, fonts, and user interface element sizes.
'''
#################################################################
#
# File: tsWxSystemSettings.py
#
# Purpose:
#
#    Class allows the application to ask for details about the
#    system. This can include settings such as standard colours,
#    fonts, and user interface element sizes.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSystemSettings import SystemSettings
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
#    Under Construction. Not ready for deployment:
#
#        Returns only sample data (symbolic names except for
#        screen size and type which only becomes available to
#        application after it has shown a top level window).
#
# Notes:
#
#    Optional Key Word Argument "verbose" and default value "False"
#    has been added. This returns settings value with mnemonic name
#    associated with index. The intent is to facilitate unit testing.
#
#    A unit test module is named "test_tsWxSystemSettings".
#
#    An integration test module is named "test_tsWxWidgets". Its
#    "systemSettingsTest" method will perform the test only if the
#    "systemSettingsTestEnabled" switch has been set "True".
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    SystemSettings
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    SystemSettings.GetColour
#    SystemSettings.GetFont
#    SystemSettings.GetMetric
#    SystemSettings.GetScreenType
#    SystemSettings.HasFeature
#    SystemSettings.SetScreenType
#    SystemSettings.tsGetTerminalPixelRectangle
#    SystemSettings.tsGetTheLogger
#    SystemSettings.tsGetTheTerminal
#    SystemSettings.tsGetTheTerminalScreen
#    SystemSettings.tsSetTerminalPixelRectangle
#
# Modifications:
#
#    2014/12/12 rsg Corrected method GetScreenType
#                   to return name and value of
#                   screen type based on size of stdscr.
#
#    2014/12/13 rsg Added explanation of wxSysColours found on
#                   wxWidges web site that may be useful in future
#                   update to SystemSettings.GetColour method.
#
# ToDo:
#
#    2014/12/13 rsg Update SystemSettings.GetColour method.
#                   Replace static, sample table values with live
#                   data acquired by interogation of state variables.
#
#################################################################

__title__     = 'tsWxSystemSettings'
__version__   = '1.2.0'
__date__      = '12/13/2014'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonColor16DataBase \
     import xterm16ColorNameFromCode as tsWxGTUI16
from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonColor8DataBase \
     import xterm8ColorNameFromCode as tsWxGTUI8
from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonMonochromeDataBase \
     import cursesMonochromeNameFromCode as tsWxGTUIMonochrome
from tsWxGTUI_Py2x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#--------------------------------------------------------------------------

Toolkit_Developer_Guide = '''
From:

    http://docs.wxwidgets.org/trunk/
           settings_8h.html#a44ad26cbd8d579d1b7eff7015c8bd24b

Possible values for wxSystemSettings::GetColour() parameter.

These values map 1:1 the native values supported by the Windows`
GetSysColor function. Note that other ports (other than wxMSW)
will try to provide meaningful colours but they usually map the
same colour to various wxSYS_COLOUR_* values.

Enumerator

wxSYS_COLOUR_SCROLLBAR               # The scrollbar grey area.

wxSYS_COLOUR_DESKTOP                 # The desktop colour.

wxSYS_COLOUR_ACTIVECAPTION           # Active window caption colour.

wxSYS_COLOUR_INACTIVECAPTION         # Inactive window caption colour.

wxSYS_COLOUR_MENU                    # Menu background colour.

wxSYS_COLOUR_WINDOW                  # Window background colour.

wxSYS_COLOUR_WINDOWFRAME             # Window frame colour.

wxSYS_COLOUR_MENUTEXT                # Colour of the text used in the menus.

wxSYS_COLOUR_WINDOWTEXT              # Colour of the text used in generic
                                     # windows.

wxSYS_COLOUR_CAPTIONTEXT             # Colour of the text used in captions,
                                     # size boxes and scrollbar arrow boxes.

wxSYS_COLOUR_ACTIVEBORDER            # Active window border colour.

wxSYS_COLOUR_INACTIVEBORDER          # Inactive window border colour.

wxSYS_COLOUR_APPWORKSPACE            # Background colour for MDI applications.

wxSYS_COLOUR_HIGHLIGHT               # Colour of item(s) selected in a control.

wxSYS_COLOUR_HIGHLIGHTTEXT           # Colour of the text of item(s) selected
                                     # in a control.

wxSYS_COLOUR_BTNFACE                 # Face shading colour on push buttons.

wxSYS_COLOUR_BTNSHADOW               # Edge shading colour on push buttons.

wxSYS_COLOUR_GRAYTEXT                # Colour of greyed (disabled) text.

wxSYS_COLOUR_BTNTEXT                 # Colour of the text on push buttons.

wxSYS_COLOUR_INACTIVECAPTIONTEXT     # Colour of the text in active captions.

wxSYS_COLOUR_BTNHIGHLIGHT            # Highlight colour for buttons.

wxSYS_COLOUR_3DDKSHADOW              # Dark shadow colour for three-dimensional
                                     # display elements.

wxSYS_COLOUR_3DLIGHT                 # Light colour for three-dimensional
                                     # display elements.

wxSYS_COLOUR_INFOTEXT                # Text colour for tooltip controls.

wxSYS_COLOUR_INFOBK                  # Background colour for tooltip controls.

wxSYS_COLOUR_LISTBOX                 # Background colour for list-like
                                     # controls.

wxSYS_COLOUR_HOTLIGHT                # Colour for a hyperlink or hot-tracked
                                     # item.

wxSYS_COLOUR_GRADIENTACTIVECAPTION   # Right side colour in the color gradient
                                     # of an active window`s title bar.

wxSYS_COLOUR_ACTIVECAPTION           # specifies the left side color.

wxSYS_COLOUR_GRADIENTINACTIVECAPTION # Right side colour in the color gradient
                                     # of an inactive window`s title bar.

wxSYS_COLOUR_INACTIVECAPTION         # specifies the left side color.

wxSYS_COLOUR_MENUHILIGHT             # The colour used to highlight menu items
                                     # when the menu appears as a flat menu.
                                     #
                                     # The highlighted menu item is outlined
                                     # with wxSYS_COLOUR_HIGHLIGHT.

wxSYS_COLOUR_MENUBAR                 # The background colour for the menu bar
                                     # when menus appear as flat menus.
                                     #
                                     # However, wxSYS_COLOUR_MENU continues
                                     # to specify the background color of the
                                     # menu popup.

wxSYS_COLOUR_LISTBOXTEXT             # Text colour for list-like controls.
                                     #
                                     # Since
                                     #      2.9.0

wxSYS_COLOUR_LISTBOXHIGHLIGHTTEXT    # Text colour for the unfocused selection
                                     # of list-like controls.
                                     #
                                     # Since
                                     #      2.9.1

wxSYS_COLOUR_BACKGROUND              # Synonym for wxSYS_COLOUR_DESKTOP.

wxSYS_COLOUR_3DFACE                  # Synonym for wxSYS_COLOUR_BTNFACE.

wxSYS_COLOUR_3DSHADOW                # Synonym for wxSYS_COLOUR_BTNSHADOW.

wxSYS_COLOUR_BTNHILIGHT              # Synonym for wxSYS_COLOUR_BTNHIGHLIGHT.

wxSYS_COLOUR_3DHIGHLIGHT             # Synonym for wxSYS_COLOUR_BTNHIGHLIGHT.

wxSYS_COLOUR_3DHILIGHT               # Synonym for wxSYS_COLOUR_BTNHIGHLIGHT.

wxSYS_COLOUR_FRAMEBK                 # Synonym for wxSYS_COLOUR_BTNFACE.
                                     #
                                     # On wxMSW this colour should be used as
                                     # the background colour of wxFrames which
                                     # are used as containers of controls;
                                     # this is in fact the same colour used
                                     # for the borders of controls like
                                     # e.g. wxNotebook or for the background
                                     # of e.g. wxPanel.
                                     #
                                     # Since
                                     #      2.9.0


wxSYS_MOUSE_BUTTONS                  # Number of buttons on mouse,
                                     # or zero if no mouse was installed.

wxSYS_BORDER_X                       # Width of single border.

wxSYS_BORDER_Y                       # Height of single border.

wxSYS_CURSOR_X                       # Width of cursor.

wxSYS_CURSOR_Y                       # Height of cursor.

wxSYS_DCLICK_X                       # Width in pixels of rectangle within
                                     # which two successive mouse clicks must
                                     # fall to generate a double-click.

wxSYS_DCLICK_Y                       # Height in pixels of rectangle within
                                     # which two successive mouse clicks must
                                     # fall to generate a double-click.

wxSYS_DRAG_X                         # Width in pixels of a rectangle centered
                                     # on a drag point to allow for limited
                                     # movement of the mouse pointer before
                                     # a drag operation begins.

wxSYS_DRAG_Y                         # Height in pixels of a rectangle
                                     # centered on a drag point to allow for
                                     # limited movement of the mouse pointer
                                     # before a drag operation begins.

wxSYS_EDGE_X                         # Width of a 3D border, in pixels.

wxSYS_EDGE_Y                         # Height of a 3D border, in pixels.

wxSYS_HSCROLL_ARROW_X                # Width of arrow bitmap on horizontal
                                     # scrollbar.

wxSYS_HSCROLL_ARROW_Y                # Height of arrow bitmap on horizontal
                                     # scrollbar.

wxSYS_HTHUMB_X                       # Width of horizontal scrollbar thumb.

wxSYS_ICON_X                         # The default width of an icon.

wxSYS_ICON_Y                         # The default height of an icon.

wxSYS_ICONSPACING_X                  # Width of a grid cell for items in large
                                     # icon view, in pixels. Each item fits
                                     # into a rectangle of this size when
                                     # arranged.

wxSYS_ICONSPACING_Y                  # Height of a grid cell for items in
                                     # large icon view, in pixels. Each item
                                     # fits into a rectangle of this size
                                     # when arranged.

wxSYS_WINDOWMIN_X                    # Minimum width of a window.

wxSYS_WINDOWMIN_Y                    # Minimum height of a window.

wxSYS_SCREEN_X                       # Width of the screen in pixels.

wxSYS_SCREEN_Y                       # Height of the screen in pixels.

wxSYS_FRAMESIZE_X                    # Width of the window frame for a
                                     # wxTHICK_FRAME window.

wxSYS_FRAMESIZE_Y                    # Height of the window frame for a
                                     # wxTHICK_FRAME window.

wxSYS_SMALLICON_X                    # Recommended width of a small icon
                                     # (in window captions, and small
                                     # icon view).

wxSYS_SMALLICON_Y                    # Recommended height of a small icon
                                     # (in window captions, and small
                                     # icon view).

wxSYS_HSCROLL_Y                      # Height of horizontal scrollbar in
                                     # pixels.

wxSYS_VSCROLL_X                      # Width of vertical scrollbar in pixels.

wxSYS_VSCROLL_ARROW_X                # Width of arrow bitmap on a vertical
                                     # scrollbar.

wxSYS_VSCROLL_ARROW_Y                # Height of arrow bitmap on a vertical
                                     # scrollbar.

wxSYS_VTHUMB_Y                       # Height of vertical scrollbar thumb.

wxSYS_CAPTION_Y                      # Height of normal caption area.

wxSYS_MENU_Y                         # Height of single-line menu bar.

wxSYS_NETWORK_PRESENT                # 1 if there is a network present,
                                     # 0 otherwise.

wxSYS_PENWINDOWS_PRESENT             # 1 if PenWindows is installed,
                                     # 0 otherwise.

wxSYS_SHOW_SOUNDS                    # Non-zero if the user requires an
                                     # application to present information
                                     # visually in situations where it
                                     # would otherwise present the information
                                     # only in audible form; zero otherwise.

wxSYS_SWAP_BUTTONS                   # Non-zero if the meanings of the left
                                     # and right mouse buttons are swapped;
                                     # zero otherwise.

wxSYS_DCLICK_MSEC                    # Maximal time, in milliseconds, which
                                     # may pass between subsequent clicks
                                     # for a double click to be generated.

wxSYS_OEM_FIXED_FONT                 # Original equipment manufacturer
                                     # dependent fixed-pitch font.

wxSYS_ANSI_FIXED_FONT                # Windows fixed-pitch (monospaced) font.

wxSYS_ANSI_VAR_FONT                  # Windows variable-pitch (proportional)
                                     # font.

wxSYS_SYSTEM_FONT                    # System font.
                                     # By default, the system uses the system
                                     # font to draw menus, dialog box
                                     # controls, and text.

wxSYS_DEVICE_DEFAULT_FONT            # Device-dependent font (Windows NT and
                                     # later only).

wxSYS_DEFAULT_GUI_FONT               # Default font for user interface
                                     # objects such as menus and dialog boxes.
                                     # Note that with modern GUIs nothing
                                     # guarantees that the same font is used
                                     # for all GUI elements, so some controls
                                     # might use a different font by default.
'''

#--------------------------------------------------------------------------

class SystemSettings(object):
    '''
    Class allows the application to ask for details about the
    system. This can include settings such as standard colours,
    fonts, and user interface element sizes.
    '''
    # Class Variables
    #----------------------------------------------------------------------

    # wxSystemColour
    wxSYS_COLOUR_SCROLLBAR                  = 1
    wxSYS_COLOUR_DESKTOP                    = 2
    wxSYS_COLOUR_ACTIVECAPTION              = 3
    wxSYS_COLOUR_INACTIVECAPTION            = 4
    wxSYS_COLOUR_MENU                       = 5
    wxSYS_COLOUR_WINDOW                     = 6
    wxSYS_COLOUR_WINDOWFRAME                = 7
    wxSYS_COLOUR_MENUTEXT                   = 8
    wxSYS_COLOUR_WINDOWTEXT                 = 9
    wxSYS_COLOUR_CAPTIONTEXT                = 10
    wxSYS_COLOUR_ACTIVEBORDER               = 11
    wxSYS_COLOUR_INACTIVEBORDER             = 12
    wxSYS_COLOUR_APPWORKSPACE               = 13
    wxSYS_COLOUR_HIGHLIGHT                  = 14
    wxSYS_COLOUR_HIGHLIGHTTEXT              = 15
    wxSYS_COLOUR_BTNFACE                    = 16
    wxSYS_COLOUR_BTNSHADOW                  = 17
    wxSYS_COLOUR_GRAYTEXT                   = 18
    wxSYS_COLOUR_BTNTEXT                    = 19
    wxSYS_COLOUR_INACTIVECAPTIONTEXT        = 20
    wxSYS_COLOUR_BTNHIGHLIGHT               = 21
    wxSYS_COLOUR_3DDKSHADOW                 = 22
    wxSYS_COLOUR_3DLIGHT                    = 23
    wxSYS_COLOUR_INFOTEXT                   = 24
    wxSYS_COLOUR_INFOBK                     = 25
    wxSYS_COLOUR_LISTBOX                    = 26
    wxSYS_COLOUR_HOTLIGHT                   = 27
    wxSYS_COLOUR_GRADIENTACTIVECAPTION      = 28
    wxSYS_COLOUR_ACTIVECAPTION              = 29
    wxSYS_COLOUR_GRADIENTINACTIVECAPTION    = 30
    wxSYS_COLOUR_INACTIVECAPTION            = 31
    wxSYS_COLOUR_MENUHILIGHT                = 32
    wxSYS_COLOUR_MENUBAR                    = 33
    wxSYS_COLOUR_LISTBOXTEXT                = 34
    wxSYS_COLOUR_LISTBOXHIGHLIGHTTEXT       = 35

    # synonyms
    #
    # Unit testing is possible if synonyms are added
    # to dictioary only with their own unique index.
    wxSYS_COLOUR_BACKGROUND                 = 36 # wxSYS_COLOUR_DESKTOP
    wxSYS_COLOUR_3DFACE                     = 37 # wxSYS_COLOUR_BTNFACE
    wxSYS_COLOUR_3DSHADOW                   = 38 # wxSYS_COLOUR_BTNSHADOW
    wxSYS_COLOUR_BTNHILIGHT                 = 39 # wxSYS_COLOUR_BTNHIGHLIGHT
    wxSYS_COLOUR_3DHIGHLIGHT                = 40 # wxSYS_COLOUR_BTNHIGHLIGHT
    wxSYS_COLOUR_3DHILIGHT                  = 41 # wxSYS_COLOUR_BTNHIGHLIGHT
    wxSYS_COLOUR_FRAMEBK                    = 42 # wxSYS_COLOUR_BTNFACE

    wxSystemColour = {
        wxSYS_COLOUR_SCROLLBAR: (
            'wxSYS_COLOUR_SCROLLBAR',
            wx.ThemeToUse['ScrollBar']['BackgroundColour']),

        wxSYS_COLOUR_DESKTOP: (
            'wxSYS_COLOUR_DESKTOP',
            wx.ThemeToUse['BackgroundColour']),

        wxSYS_COLOUR_ACTIVECAPTION: (
            'wxSYS_COLOUR_ACTIVECAPTION', None),

        wxSYS_COLOUR_INACTIVECAPTION: (
            'wxSYS_COLOUR_INACTIVECAPTION', None),

        wxSYS_COLOUR_MENU: (
            'wxSYS_COLOUR_MENU',
            wx.ThemeToUse['MenuBar']['BackgroundColour']),

        wxSYS_COLOUR_WINDOW: (
            'wxSYS_COLOUR_WINDOW',
            wx.ThemeToUse['Frame']['ForegroundColour']),

        wxSYS_COLOUR_WINDOWFRAME: (
            'wxSYS_COLOUR_WINDOWFRAME',
            wx.ThemeToUse['Frame']['BackgroundColour']),

        wxSYS_COLOUR_MENUTEXT: (
            'wxSYS_COLOUR_MENUTEXT',
            wx.ThemeToUse['MenuBar']['ForegroundColour']),

        wxSYS_COLOUR_WINDOWTEXT: (
            'wxSYS_COLOUR_WINDOWTEXT',
            wx.ThemeToUse['Frame']['BackgroundColour']),

        wxSYS_COLOUR_CAPTIONTEXT: (
            'wxSYS_COLOUR_CAPTIONTEXT', None),

        wxSYS_COLOUR_ACTIVEBORDER: (
            'wxSYS_COLOUR_ACTIVEBORDER', None),

        wxSYS_COLOUR_INACTIVEBORDER: (
            'wxSYS_COLOUR_INACTIVEBORDE', None),

        wxSYS_COLOUR_APPWORKSPACE: (
            'wxSYS_COLOUR_APPWORKSPACE', None),

        wxSYS_COLOUR_HIGHLIGHT: (
            'wxSYS_COLOUR_HIGHLIGHT', None),

        wxSYS_COLOUR_HIGHLIGHTTEXT: (
            'wxSYS_COLOUR_HIGHLIGHTTEXT', None),

        wxSYS_COLOUR_BTNFACE: (
            'wxSYS_COLOUR_BTNFACE',
            wx.ThemeToUse['Frame']['ForegroundColour']),

        wxSYS_COLOUR_BTNSHADOW: (
            'wxSYS_COLOUR_BTNSHADOW', None),

        wxSYS_COLOUR_GRAYTEXT: (
            'wxSYS_COLOUR_GRAYTEXT', None),

        wxSYS_COLOUR_BTNTEXT: (
            'wxSYS_COLOUR_BTNTEXT',
            wx.ThemeToUse['Frame']['BackgroundColour']),

        wxSYS_COLOUR_INACTIVECAPTIONTEXT: (
            'wxSYS_COLOUR_INACTIVECAPTIONTEXT', None),

        wxSYS_COLOUR_BTNHIGHLIGHT: (
            'wxSYS_COLOUR_BTNHIGHLIGHT', None),

        wxSYS_COLOUR_3DDKSHADOW: (
            'wxSYS_COLOUR_3DDKSHADOW', None),

        wxSYS_COLOUR_3DLIGHT: (
            'wxSYS_COLOUR_3DLIGHT', None),

        wxSYS_COLOUR_INFOTEXT: (
            'wxSYS_COLOUR_INFOTEXT', None),

        wxSYS_COLOUR_INFOBK: (
            'wxSYS_COLOUR_INFOBK', None),

        wxSYS_COLOUR_LISTBOX: (
            'wxSYS_COLOUR_LISTBOX', None),

        wxSYS_COLOUR_HOTLIGHT: (
            'wxSYS_COLOUR_HOTLIGHT', None),

        wxSYS_COLOUR_GRADIENTACTIVECAPTION: (
            'wxSYS_COLOUR_GRADIENTACTIVECAPTION', None),

        wxSYS_COLOUR_ACTIVECAPTION: (
            'wxSYS_COLOUR_ACTIVECAPTION', None),

        wxSYS_COLOUR_GRADIENTINACTIVECAPTION: (
            'wxSYS_COLOUR_GRADIENTINACTIVECAPTION', None),

        wxSYS_COLOUR_INACTIVECAPTION: (
            'wxSYS_COLOUR_INACTIVECAPTION', None),

        wxSYS_COLOUR_MENUHILIGHT: (
            'wxSYS_COLOUR_MENUHILIGHT', None),

        wxSYS_COLOUR_MENUBAR: (
            'wxSYS_COLOUR_MENUBAR', None),

        wxSYS_COLOUR_LISTBOXTEXT: (
            'wxSYS_COLOUR_LISTBOXTEXT', None),

        wxSYS_COLOUR_LISTBOXHIGHLIGHTTEXT: (
            'wxSYS_COLOUR_LISTBOXHIGHLIGHTTEXT', None),

        wxSYS_COLOUR_BACKGROUND: (
            'wxSYS_COLOUR_BACKGROUND',
            wx.ThemeToUse['BackgroundColour']),

        wxSYS_COLOUR_3DFACE: (
            'wxSYS_COLOUR_3DFACE', None),

        wxSYS_COLOUR_3DSHADOW: (
            'wxSYS_COLOUR_3DSHADOW', None),

        wxSYS_COLOUR_BTNHILIGHT: (
            'wxSYS_COLOUR_BTNHILIGHT', None),

        wxSYS_COLOUR_3DHIGHLIGHT: (
            'wxSYS_COLOUR_3DHIGHLIGHT', None),

        wxSYS_COLOUR_3DHILIGHT: (
            'wxSYS_COLOUR_3DHILIGH', None),

        wxSYS_COLOUR_FRAMEBK: (
            'wxSYS_COLOUR_FRAMEBK',
            wx.ThemeToUse['Frame']['ForegroundColour'])
        }

    #----------------------------------------------------------------------

    # wxSystemFeature
    wxSYS_CAN_DRAW_FRAME_DECORATIONS = 1
    wxSYS_CAN_ICONIZE_FRAME          = 2
    wxSYS_TABLET_PRESENT             = 3

    wxSystemFeature = {
        wxSYS_CAN_DRAW_FRAME_DECORATIONS: (
            'wxSYS_CAN_DRAW_FRAME_DECORATIONS', False),
        wxSYS_CAN_ICONIZE_FRAME: (
            'wxSYS_CAN_ICONIZE_FRAME', False),
        wxSYS_TABLET_PRESENT: (
            'wxSYS_TABLET_PRESENT', False)
        }

    #----------------------------------------------------------------------

    # wxSystemFont
    wxSYS_OEM_FIXED_FONT             = 1
    wxSYS_ANSI_FIXED_FONT            = 2
    wxSYS_ANSI_VAR_FONT              = 3
    wxSYS_SYSTEM_FONT                = 4
    wxSYS_DEVICE_DEFAULT_FONT        = 5
    wxSYS_DEFAULT_GUI_FONT           = 6

    defaultFont = 'Courier 12pt (%dx%d pixels)' % (
        wx.pixelWidthPerCharacter, wx.pixelHeightPerCharacter)

    wxSystemFont = {
        wxSYS_OEM_FIXED_FONT: (
            'wxSYS_OEM_FIXED_FONT', defaultFont),

        wxSYS_ANSI_FIXED_FONT: (
            'wxSYS_ANSI_FIXED_FONT', defaultFont),

        wxSYS_ANSI_VAR_FONT: (
            'wxSYS_ANSI_VAR_FONT', defaultFont),

        wxSYS_SYSTEM_FONT: (
            'wxSYS_SYSTEM_FONT', defaultFont),

        wxSYS_DEVICE_DEFAULT_FONT: (
            'wxSYS_DEVICE_DEFAULT_FONT', defaultFont),

        wxSYS_DEFAULT_GUI_FONT: (
            'wxSYS_DEFAULT_GUI_FONT', defaultFont)
        }

    #----------------------------------------------------------------------

    # wxSystemMetric
    wxSYS_MOUSE_BUTTONS       = 1
    wxSYS_BORDER_X            = 2
    wxSYS_BORDER_Y            = 3
    wxSYS_CURSOR_X            = 4
    wxSYS_CURSOR_Y            = 5
    wxSYS_DCLICK_X            = 6
    wxSYS_DCLICK_Y            = 7
    wxSYS_DRAG_X              = 8
    wxSYS_DRAG_Y              = 9
    wxSYS_EDGE_X              = 10
    wxSYS_EDGE_Y              = 11
    wxSYS_HSCROLL_ARROW_X     = 12
    wxSYS_HSCROLL_ARROW_Y     = 13
    wxSYS_HTHUMB_X            = 14
    wxSYS_ICON_X              = 15
    wxSYS_ICON_Y              = 16
    wxSYS_ICONSPACING_X       = 17
    wxSYS_ICONSPACING_Y       = 18
    wxSYS_WINDOWMIN_X         = 19
    wxSYS_WINDOWMIN_Y         = 20
    wxSYS_SCREEN_X            = 21
    wxSYS_SCREEN_Y            = 22
    wxSYS_FRAMESIZE_X         = 23
    wxSYS_FRAMESIZE_Y         = 24
    wxSYS_SMALLICON_X         = 25
    wxSYS_SMALLICON_Y         = 26
    wxSYS_HSCROLL_Y           = 27
    wxSYS_VSCROLL_X           = 28
    wxSYS_VSCROLL_ARROW_X     = 29
    wxSYS_VSCROLL_ARROW_Y     = 30
    wxSYS_VTHUMB_Y            = 31
    wxSYS_CAPTION_Y           = 32
    wxSYS_MENU_Y              = 33
    wxSYS_NETWORK_PRESENT     = 34
    wxSYS_PENWINDOWS_PRESENT  = 35
    wxSYS_SHOW_SOUNDS         = 36
    wxSYS_SWAP_BUTTONS        = 37
    wxSYS_DCLICK_MSEC         = 38

    wxSystemMetric = {
        wxSYS_MOUSE_BUTTONS: (
            'wxSYS_MOUSE_BUTTONS', True),
        wxSYS_BORDER_X: (
            'wxSYS_BORDER_X', 1),
        wxSYS_BORDER_Y: (
            'wxSYS_BORDER_Y', 1),
        wxSYS_CURSOR_X: (
            'wxSYS_CURSOR_X', None),
        wxSYS_CURSOR_Y: (
            'wxSYS_CURSOR_Y', None),
        wxSYS_DCLICK_X: (
            'wxSYS_DCLICK_X', None),
        wxSYS_DCLICK_Y: (
            'wxSYS_DCLICK_Y', None),
        wxSYS_DRAG_X: (
            'wxSYS_DRAG_X', None),
        wxSYS_DRAG_Y: (
            'wxSYS_DRAG_Y', None),
        wxSYS_EDGE_X: (
            'wxSYS_EDGE_X', 1), # wxWidgets defaults to 2
        wxSYS_EDGE_Y: (
            'wxSYS_EDGE_Y', 1), # wxWidgets defaults to 2
        wxSYS_HSCROLL_ARROW_X: (
            'wxSYS_HSCROLL_ARROW_X', None),
        wxSYS_HSCROLL_ARROW_Y: (
            'wxSYS_HSCROLL_ARROW_X', None),
        wxSYS_HTHUMB_X: (
            'wxSYS_HTHUMB_X', None),
        wxSYS_ICON_X: (
            'wxSYS_ICON_X', None),
        wxSYS_ICON_Y: (
            'wxSYS_ICON_Y', None),
        wxSYS_ICONSPACING_X: (
            'wxSYS_ICONSPACING_X', None),
        wxSYS_ICONSPACING_Y: (
            'wxSYS_ICONSPACING_Y', None),
        wxSYS_WINDOWMIN_X: (
            'wxSYS_WINDOWMIN_X', None),
        wxSYS_WINDOWMIN_Y: (
            'wxSYS_WINDOWMIN_Y', None),
        wxSYS_SCREEN_X: (
            'wxSYS_SCREEN_X',
            None), # SystemSettings.tsGetTheTerminalScreen().width,
        wxSYS_SCREEN_Y: (
            'wxSYS_SCREEN_Y',
            None), # SystemSettings.tsGetTheTerminalScreen().height,
        wxSYS_FRAMESIZE_X: (
            'wxSYS_FRAMESIZE_X', None),
        wxSYS_FRAMESIZE_Y: (
            'wxSYS_FRAMESIZE_Y', None),
        wxSYS_SMALLICON_X: (
            'wxSYS_SMALLICON_X', None),
        wxSYS_SMALLICON_Y: (
            'wxSYS_SMALLICON_Y', None),
        wxSYS_HSCROLL_Y: (
            'wxSYS_HSCROLL_Y', None),
        wxSYS_VSCROLL_X: (
            'wxSYS_VSCROLL_X', None),
        wxSYS_VSCROLL_ARROW_X: (
            'wxSYS_VSCROLL_ARROW_X', None),
        wxSYS_VSCROLL_ARROW_Y: (
            'wxSYS_VSCROLL_ARROW_Y', None),
        wxSYS_VTHUMB_Y: (
            'wxSYS_VTHUMB_Y', None),
        wxSYS_CAPTION_Y: (
            'wxSYS_CAPTION_Y', None),
        wxSYS_MENU_Y: (
            'wxSYS_MENU_Y', None),
        wxSYS_NETWORK_PRESENT: (
            'wxSYS_NETWORK_PRESENT', None),
        wxSYS_PENWINDOWS_PRESENT: (
            'wxSYS_PENWINDOWS_PRESENT', None),
        wxSYS_SHOW_SOUNDS: (
            'wxSYS_SHOW_SOUNDS', None),
        wxSYS_SWAP_BUTTONS: (
            'wxSYS_SWAP_BUTTONS', None),
        wxSYS_DCLICK_MSEC: (
            'wxSYS_DCLICK_MSEC', None)
        }

    #----------------------------------------------------------------------

    # wxSystemScreenType
    wxSYS_SCREEN_NONE    = 0 #   not yet defined
    wxSYS_SCREEN_TINY    = 1 #   <  320x240
    wxSYS_SCREEN_PDA     = 2 #   >= 320x240
    wxSYS_SCREEN_SMALL   = 3 #   >= 640x480
    wxSYS_SCREEN_DESKTOP = 4 #   >= 800x600

    wxSystemScreenType = {
        wxSYS_SCREEN_NONE: (None, 0),
        wxSYS_SCREEN_TINY: ('Tiny', 1),
        wxSYS_SCREEN_PDA: ('PDA', 2),
        wxSYS_SCREEN_SMALL: ('Small', 3),
        wxSYS_SCREEN_DESKTOP: ('Desktop', 4)
        }

    systemScreenType = wxSystemScreenType[wxSYS_SCREEN_NONE]

    #----------------------------------------------------------------------

    @staticmethod
    def GetColour(index, verbose=False, internal=False):
        '''
        Returns a system colour. The returned colour is always valid.
        '''
        if internal:

            try:

                theValue = index
                if curses.has_colors():
                    if curses.COLOR_PAIRS >= 256:
                        theDataBase = tsWxGTUI16
                    else:
                        theDataBase = tsWxGTUI8
                else:
                    theDataBase = tsWxGTUIMonochrome
                theName = theDataBase[index]

            except KeyError, errorCode:

                theName = 'ERROR: ' + \
                          'SystemSettings.GetColour KeyError=%s' % errorCode
                theValue = errorCode

        else:

            try:

                (theName, theValue) = SystemSettings.wxSystemColour[index]

            except KeyError, errorCode:

                theName = 'ERROR: ' + \
                          'SystemSettings.GetColour KeyError=%s' % errorCode
                theValue = errorCode

        if verbose:
            return (theName, theValue)
        else:
            return (theValue)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetFont(index, verbose=False):
        '''
        Returns a system font. The returned font is always valid.
        '''
        try:

            (theName, theValue) = SystemSettings.wxSystemFont[index]

        except KeyError, errorCode:

            theName = 'ERROR: SystemSettings.GetFont KeyError=%s' % errorCode
            theValue = -1

        if verbose:
            return (theName, theValue)
        else:
            return (theValue)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetMetric(index, win=None, verbose=False):
        '''
        Returns the value of a system metric, or -1 if the metric is not
        supported on the current system.

        The value of win determines if the metric returned is a global
        value or a wxWindow  based value, in which case it might determine
        the widget, the display the window is on, or something similar. The
        window given should be as close to the metric as possible
        (e.g a wxTopLevelWindow in case of the wxSYS_CAPTION_Y metric).

        index can be one of the wxSystemMetric enum values.

        win is a pointer to the window for which the metric is requested.
        Specifying the win parameter is encouraged, because some metrics
        on some ports are not supported without one, or they might be
        capable of reporting better values if given one. If a window does
        not make sense for a metric, one should still be given, as for
        example it might determine which displays cursor width is requested
        with wxSYS_CURSOR_X.
        '''

        myDisplay = Object.TheDisplay
        if (myDisplay is None):

            print('GetMetric: myDisplay=%s' % myDisplay)
            liveSystemMetric = SystemSettings.wxSystemMetric

        else:

            myTermRect = Object.TheDisplay.TerminalPixelRectangle
            print('GetMetric: myTermRect=%s' % myTermRect)

            if (win is None):

                myWinRect = myTermRect

            else:

                myWinRect = win.ts_Rect

            print('GetMetric: myWinRect=%s' % myWinRect)

            (virtual_screen_cursor_y,
             virtual_screen_cursor_x) = curses.getsyx() 

            liveSystemMetric = {
                SystemSettings.wxSYS_MOUSE_BUTTONS: (
                    'wxSYS_MOUSE_BUTTONS',
                    True),

                SystemSettings.wxSYS_BORDER_X: (
                    'wxSYS_BORDER_X',
                    myTermRect.x + myTermRect.width),

                SystemSettings.wxSYS_BORDER_Y: (
                    'wxSYS_BORDER_Y',
                    myTermRect.y + myTermRect.height),

                SystemSettings.wxSYS_CURSOR_X: (
                    'wxSYS_CURSOR_X',
                    virtual_screen_cursor_x* wx.pixelWidthPerCharacter),

                SystemSettings.wxSYS_CURSOR_Y: (
                    'wxSYS_CURSOR_Y',
                    virtual_screen_cursor_y * wx.pixelHeightPerCharacter),

                # Assume use of curses default value for each of two clicks
                SystemSettings.wxSYS_DCLICK_X: (
                    'wxSYS_DCLICK_X',
                    200 * 2),

                # Assume use of curses default value for each of two clicks
                SystemSettings.wxSYS_DCLICK_Y: (
                    'wxSYS_DCLICK_Y',
                    200 * 2),

                SystemSettings.wxSYS_DRAG_X: (
                    'wxSYS_DRAG_X',
                    None),

                SystemSettings.wxSYS_DRAG_Y: (
                    'wxSYS_DRAG_Y',
                    None),

                SystemSettings.wxSYS_EDGE_X: (
                    'wxSYS_EDGE_X',
                    1), # wxWidgets defaults to 2

                SystemSettings.wxSYS_EDGE_Y: (
                    'wxSYS_EDGE_Y',
                    1), # wxWidgets defaults to 2

                SystemSettings.wxSYS_HSCROLL_ARROW_X: (
                    'wxSYS_HSCROLL_ARROW_X',
                    None),

                SystemSettings.wxSYS_HSCROLL_ARROW_Y: (
                    'wxSYS_HSCROLL_ARROW_X',
                    None),

                SystemSettings.wxSYS_HTHUMB_X: (
                    'wxSYS_HTHUMB_X',
                    None),

                SystemSettings.wxSYS_ICON_X: (
                    'wxSYS_ICON_X',
                    None),

                SystemSettings.wxSYS_ICON_Y: (
                    'wxSYS_ICON_Y',
                    None),

                SystemSettings.wxSYS_ICONSPACING_X: (
                    'wxSYS_ICONSPACING_X',
                    None),

                SystemSettings.wxSYS_ICONSPACING_Y: (
                    'wxSYS_ICONSPACING_Y',
                    None),

                SystemSettings.wxSYS_WINDOWMIN_X: (
                    'wxSYS_WINDOWMIN_X',
                    None),

                SystemSettings.wxSYS_WINDOWMIN_Y: (
                    'wxSYS_WINDOWMIN_Y',
                    None),

                SystemSettings.wxSYS_SCREEN_X: (
                    'wxSYS_SCREEN_X',
                    myTermRect.x + myTermRect.width),

                SystemSettings.wxSYS_SCREEN_Y: (
                    'wxSYS_SCREEN_Y',
                    myTermRect.y + myTermRect.height),

                SystemSettings.wxSYS_FRAMESIZE_X: (
                    'wxSYS_FRAMESIZE_X',
                    myWinRect.x + myWinRect.width),

                SystemSettings.wxSYS_FRAMESIZE_Y: (
                    'wxSYS_FRAMESIZE_Y',
                    myWinRect.y + myWinRect.height),

                SystemSettings.wxSYS_SMALLICON_X: (
                    'wxSYS_SMALLICON_X',
                    None),

                SystemSettings.wxSYS_SMALLICON_Y: (
                    'wxSYS_SMALLICON_Y',
                    None),

                SystemSettings.wxSYS_HSCROLL_Y: (
                    'wxSYS_HSCROLL_Y',
                    None),

                SystemSettings.wxSYS_VSCROLL_X: (
                    'wxSYS_VSCROLL_X',
                    None),

                SystemSettings.wxSYS_VSCROLL_ARROW_X: (
                    'wxSYS_VSCROLL_ARROW_X',
                    None),

                SystemSettings.wxSYS_VSCROLL_ARROW_Y: (
                    'wxSYS_VSCROLL_ARROW_Y',
                    None),

                SystemSettings.wxSYS_VTHUMB_Y: (
                    'wxSYS_VTHUMB_Y',
                    None),

                SystemSettings.wxSYS_CAPTION_Y: (
                    'wxSYS_CAPTION_Y',
                    None),

                SystemSettings.wxSYS_MENU_Y: (
                    'wxSYS_MENU_Y',
                    None),

                SystemSettings.wxSYS_NETWORK_PRESENT: (
                    'wxSYS_NETWORK_PRESENT',
                    None),

                SystemSettings.wxSYS_PENWINDOWS_PRESENT: (
                    'wxSYS_PENWINDOWS_PRESENT',
                    None),

                SystemSettings.wxSYS_SHOW_SOUNDS: (
                    'wxSYS_SHOW_SOUNDS',
                    None),

                SystemSettings.wxSYS_SWAP_BUTTONS: (
                    'wxSYS_SWAP_BUTTONS',
                    None),

                SystemSettings.wxSYS_DCLICK_MSEC: (
                    'wxSYS_DCLICK_MSEC',
                    None)
                }

        try:

            (theName, theValue) = liveSystemMetric[index]

        except KeyError, errorCode:

            theName = 'ERROR: SystemSettings.GetMetric KeyError=%s' % errorCode
            theValue = -1

        if verbose:
            return (theName, theValue)
        else:
            return (theValue)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetScreenType(verbose=False):
        '''
        Returns the screen type.
        '''
        # wxUnix will be used on small devices, too.
        x = SystemSettings.GetMetric(SystemSettings.wxSYS_SCREEN_X)
        y = SystemSettings.GetMetric(SystemSettings.wxSYS_SCREEN_Y)
        print('DEBUG: tsWxSystemSettings.GetScreenType: X=%d; Y=%d.' % (x, y))

        if ((x == -1) or (y == -1)):

            (theName, theValue) = SystemSettings.wxSystemScreenType[
                SystemSettings.wxSYS_SCREEN_NONE]

        elif ((x >= 800) and (y >= 600)):

            (theName, theValue) = SystemSettings.wxSystemScreenType[
                SystemSettings.wxSYS_SCREEN_DESKTOP]

        elif ((x >= 640) and (y >= 480)):

            (theName, theValue) = SystemSettings.wxSystemScreenType[
                SystemSettings.wxSYS_SCREEN_SMALL]

        elif ((x >= 320) and (y >= 240)):

            (theName, theValue) = SystemSettings.wxSystemScreenType[
                SystemSettings.wxSYS_SCREEN_PDA]

        else:

            (theName, theValue) = SystemSettings.wxSystemScreenType[
                SystemSettings.wxSYS_SCREEN_TINY]

        if verbose:
            print('DEBUG: tsWxSystemSettings.GetScreenType: ' + \
                  'theName=%s, theValue=%d.' % (theName, theValue))
            return (theName, theValue)
        else:
            print('DEBUG: tsWxSystemSettings.GetScreenType: ' + \
                  'theValue=%d.' % theValue)
            return (theValue)

    #-----------------------------------------------------------------------

    @staticmethod
    def HasFeature(index, verbose=False):
        '''
        Returns true if the port has certain feature.
        '''
        try:

            (theName, theValue) = SystemSettings.wxSystemFeature[index]

        except KeyError, errorCode:

            theName = 'ERROR: SystemSettings. HasFeature KeyError=%s' % \
                      errorCode
            theValue = errorCode

        if verbose:
            return (theName, theValue)
        else:
            return (theValue)

    #-----------------------------------------------------------------------

    @staticmethod
    def SetScreenType(screen):
        '''
        '''
        SystemSettings.systemScreenType = screen

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    @staticmethod
    def tsGetTerminalPixelRectangle():
        '''
        Returns the bounding rectangle the client area of the display,
        i.e., without taskbars and such.
        '''
        try:

            rect = Object.TheDisplay.TerminalPixelRectangle

        except AttributeError:

            rect = wxRect(-1, -1, -1, -1)

        return (rect)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetTheLogger():
        '''
        Return the logger instance.
        '''
        return (Object.TheLogger)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetTheTerminalScreen():
        '''
        Return the screen instance.
        '''
        return (Object.TheTerminalScreen)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetTheTerminal():
        '''
        Return the terminal instance.
        '''
        return (Object.TheTerminal)

    #-----------------------------------------------------------------------

    @staticmethod
    def tsSetTerminalPixelRectangle():
        '''

        Updates the system terminal geometry metrics.
        '''
        systemTerminalPixelRectangle = Object.TheDisplay.TerminalPixelRectangle
        systemTerminalPixelWidth = systemTerminalPixelRectangle.width
        systemTerminalPixelHeight = systemTerminalPixelRectangle.height

        index = SystemSettings.wxSYS_SCREEN_X
        SystemSettings.wxSystemMetric[index] = systemTerminalPixelWidth
        print('wxSystemMetric[%d] = %s' % (
            index, str(SystemSettings.wxSystemMetric[index])))

        index = SystemSettings.wxSYS_SCREEN_Y
        SystemSettings.wxSystemMetric[index] = systemTerminalPixelHeight
        print('wxSystemMetric[%d] = %s' % (
            index, str(SystemSettings.wxSystemMetric[index])))

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
