#! /usr/bin/env python
# "Time-stamp: <06/06/2017  2:38:20 AM rsg>"
'''
tsWxGlobals.py - Module to establish configuration constants and
macro-type functions for the Graphical-style User Interface mode
of the "tsWxGTUI" Toolkit.
'''
#################################################################
#
# File: tsWxGlobals.py
#
# Purpose:
#
#    Module to establish configuration constants and macro-type
#    functions for the Graphical-style User Interface mode of the
#    "tsWxGTUI" Toolkit.
#
# Usage (example):
#
#    # Import
#
#    import tsWxGlobals as wx # The tsWxGTUI_PyVx Toolkit emulates the
#                             # definitions of and references to constant
#                             # and variable names used by the C++ based
#                             # wxWidgets API and the wxPython interface
#                             # wrapper used by Python programmers.
#                             #
#                             # The tsWxGlobals module and emulated
#                             # tsWxPython classes and methods are then
#                             # imported by the tsWx module to emulate
#                             # the wxPython wx module.
#                             #
#                             # The tsWx module is intended to be im-
#                             # ported by each Toolkit user applications
#                             # and Toolkit Test.
#
# Capabilities:
#
#    1. Provide a centralized mechanism for modifying/restoring those
#       configuration constants that can be interogated at runtime by
#       those software components having a "need-to-know". The intent
#       being to avoid subsequent searches to locate and modify or
#       restore a constant appropriate to the current configuration.
#
#    2. Provide a theme-based mechanism for modifying/restoring those
#       configuration constants as appropriate for the following
#       character-mode wxPython emulation:
#
#       a. Splash Screen
#
#          Docstrings to be used for Masthead, Copyright, License
#          and Notice fields appropriate for the available space
#          on the display screen.
#
#       b. Video Display Constants
#
#       c. Message Indentation Constants to facilitate trouble-
#          shooting hierarchy of emulated wxPython classes
#
#       d. wxPython object names and constants (identifiers,
#          keycodes, styles, attributes, color palette,
#          supported terminals/emulators and default fonts,
#          styles, foreground/background/markup colors etc.).
#
# Limitations:
#
#    1. The "tsWxGTUI" Toolkit is a "curses" or an "nCurses"-based,
#       character-mode emulation of the pixel-mode "wxPython" Toolkit.
#
#       a) Platforms with 32-bit processors, Python 2x or 3x (and 
#          "curses", "ncurses" 5.x or "ncurses" 6.x) support up to
#          a 16 color palette (256 foreground-background color pairs).
#
#       b) Platforms with 64-bit processors, Python 2x or 3x (and
#          "curses" or "ncurses" 5.x) support up to a 16 color palette
#          (256 foreground-background color pairs).
#
#          NOTE: The bug-fix only maintenance mode for Python 2.7.x
#                and Python 3.0.x - 3.5.0 precludes future support
#                for "ncurses" 6.x.
#
#       c) Platforms with 64-bit processors, Python 3.5.1 or later (and
#          "ncurses" 6.x) support up to a 256 color palette (65536 fore-
#          ground-background color pairs).
#
#    2. Each character-mode "graphical" element occupies a cell that
#       is assumed to be 8-pixels wide and 12-pixels high. The terminal
#       screen size will shrink or expand whenever the computer operator
#       selects a smaller or larger font.
#
#    3. The available set of alphabetic, numeric, punctuation and
#       line-drawing characters is quite limited to less than 256.
#
#    4. Overlapping the border character cells of "graphical" elements
#       is frequently used to conserve display screen real estate.
#
# Notes:
#
#    1. The "tsToolkitCLI" is designed to be independent of the
#       "tsToolkitGUI". However, its "tsApplication" module, collects
#       and distributes all the keyword-value pair options and posi-
#       tional argumets entered by the operator and those launch
#       parameters established by the application itself. This in-
#       dependence ensures that there is a common launch mechanism
#       ("tsApplication") for both CLI and GUI applications.
#
#    2. This "tsCxGlobals" module establishes a common area for defin-
#       ing system-wide CLI configuration parameters whose values may
#       be then communicated within and across a distributed system.   
#
#    3. The "tsWxGlobals" module establishes a common area for defin-
#       ing system-wide GUI configuration parameters whose values may
#       be then communicated within and across a distributed system.
#
#    4. Themes are customized sets of configuration parameters that
#       are appropriate for a desired look and feel.
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.5 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.5 (Ref. Man.).
#
# Modifications:
#
#    2010/11/06 rsg Added bit mask constants used in wxKeyEvent.
#
#    2011/03/16 rsg Added "include" constants used in wxWindow.
#
#    2011/03/17 rsg Added BACKGROUNDSTYLE constants used in
#                   wxWindow.
#
#    2011/11/17 rsg Imported curses to get the set of video
#                   display features that curses guarantees
#                   to recognize.
#
#    2011/11/21 rsg Added StdioMargin and StdioMarkup to the
#                   theme controls.
#
#    2011/11/27 rsg Added StaticBox.
#
#    2011/12/20 rsg Added USE_CURSES_PANEL_STACK.
#
#    2011/12/27 rsg Added TaskBarActiveFocusForegroundColour and
#                         TaskBarInactiveFocusForegroundColour.
#
#    2012/01/10 rsg Added DEFAULT key and value to StdioMarkup
#                   in order to improve message readability via
#                   increased brightness/contrast.
#
#    2012/01/12 rsg Changed Stdio Foreground/Background colors
#                   from bold White/Green to less distracting
#                   Black/White. Reaffirmed Foreground/Background
#                   colors of White/Black for TaskBar to match
#                   space filling gap between buttons.
#
#    2012/01/17 rsg Re-enabled USE_CURSES_PANEL_STACK after
#                   correcting WINDOW.tsRegisterClassWindow
#                   logic that obtained and stored PanelLayer
#                   info in tswxGraphicalTextUserInterface
#                   data base.
#
#    2012/01/19 rsg Added TaskBarActiveFocusBackgroundColour and
#                   TaskBarInactiveFocusBackgroundColour.
#                   Also, reverted TaskBar background color from
#                   White to Black to distinguish area from Stdio.
#
#    2012/01/20 rsg Changed Stdio Foreground/Background colors
#                   from Black/White to more readable White/Black.
#
#    2012/01/30 rsg Changed ScrollBar features to ThemeWxPython
#                   and ThemeTeamSTARS.
#
#    2012/01/31 rsg Added BORDER_SIMPLE to various default styles
#                   to compensate for applcation of BORDER_MASK
#                   (to ignore non-border styles) in tsIsBorderStyle
#                   method of tsWxWindow Class.
#
#    2012/02/07 rsg Added ThemeToUse entries for SplashScreenImage
#                   Path and File. Also re-organized disctionary
#
#    2012/02/21 rsg Added HorizontalScrollBarStr and
#                   VerticalScrollBarStr.
#
#    2012/02/21 rsg Added tsWxScrollBarGauge library module.
#
#    2012/02/24 rsg Added tsWxScrolledText library module.
#
#    2012/03/27 rsg Set "USE_CURSES_PANEL_STACK = False".
#
#    2012/06/24 rsg Added tsCaselessStringCompare.
#
#    2012/06/24 rsg Added ThumbEmulation to ScrollBar theme
#                   features.
#
#    2012/07/05 rsg Added default user text input prompt messages.
#
#    2012/07/07 rsg Added TEXT_ENTRY_DIALOG_STYLE.
#
#    2012/07/13 rsg Added wxWidgets and tsLogger Log levels with
#                   "kludged" map between former to latter.
#
#    2012/07/15 rsg Expanded configuration data for tsLogger
#                   and tsWxLog.
#
#    2012/08/10 rsg Added indentation and style definitions for
#                   tsWxTextEditBox class.
#
#    2013/07/05 rsg Added tsWxFrameButton.
#
#    2013/07/16 rsg Added logic needed for nCurses to interpret
#                   non-ASCII string data.
#
#    2013/10/21 rsg Added logic needed to display/log theme dictionary.
#
#    2013/10/24 rsg Added import tsCxGlobalsPkg.
#
#    2013/11/28 rsg Added splashscreen "doc" strings:
#                   masthead, copyright, license and notices.
#
#    2013/12/01 rsg Re-engineered splashscreen theme to include
#                   colors.
#
#    2013/12/02 rsg Added StandardTerminalEmulators in order
#                   to remove the configuration control from the
#                   tsWxGraphicalTextUserInterface module.
#
#    2013/12/23 rsg Moved xterm-256color from unsupportedTermCaps
#                   to supportedTermCaps after discovering that
#                   it is the default TERM for Fedora 19 Linux
#                   and that Mac OS X begain supporting it after
#                   Lion (10.7.5).
#
#    2014/01/01 rsg Changed Splash Screen path from src to bmp:
#                  'Path': './tsLibGUI/tsWxPkg/bmp/'.
#
#    2014/01/01 rsg Changed Splash Screen extention from img to bmp:
#                  'FileName': 'theSplashScreen.bmp'
#
#    2014/01/03 rsg Added support for xterm-16color.
#
#    2014/01/08 rsg Added support for xterm-88color. Disabled support
#                   for xterm-88color pending debugging.
#
#    2014/01/18 rsg Updated copyright notice.
#
#    2014/01/29 rsg Changed Splash Screen path from './bmp' to
#                   './logs/bmp/' so as to facilitate cleanup of files
#                   that have become outdated or no longer relevant.
#
#    2014/03/15 rsg Updated masthead, copyright, license and notice.
#
#    2014/04/05 rsg Revised capabilities item 2 to replace description
#                   of tsCxGlobals capabilities by summary of tsWxGlobals
#                   characer-mode wxPython emulation capabilities.
#
#    2014/06/13 rsg Moved term-88color and xterm-256color from
#                   supportedTermCaps to unsupportedTermCaps after
#                   receiving following message from Thomas E. Dickey:
#                   "On Thu, Jun 12, 2014 at 09:06:22AM -0400,
#                   Richard S. Gordon wrote:
#                   Hi Thomas,
#
#                   I've made a lot of progress since my last contact
#                   with you but have encountered an issue that I hope
#                   you might be able to offer some insight into
#                   its cause.
#                   ...
#                   Can you offer any insight, solution or suggestions?
#                   Is there a c-source file that I could use to test
#                   and verify the operation of the xterm-88color and
#                   xterm-256color emulators on my various host platforms? 
#
#                   sounds like
#
#                   http://invisible-island.net/ncurses/
#                          ncurses.faq.html#xterm_256color".
#
#    2014/07/04 rsg Moved term-88color and xterm-256color from
#                   unsupportedTermCaps to supportedTermCaps in order
#                   to test refactoring and other design changes to
#                   tsWxGraphicalTextUserInterface.
#
#    2014/07/18 rsg Updated copyright date.
#
#    2014/10/22 rsg Added control switch "USE_256_COLOR_PAIR_LIMIT"
#                   to establish 256 as the maximum number of
#                   available color pairs (overriding the value
#                   reported by curses). As a consequence, the
#                   tsWxGTUI  Toolkit will apply the xterm-16color
#                   palette instead of the xterm-88color and
#                   xterm-256color palette which cannot otherwise
#                   be made to work.
#
#    2014/11/16 rsg Updated copyright, license and notice data.
#                   Added logic to establish and use a Python
#                   version specific tsWxGTUI_PyVx for previous reference
#                   to "tsWxGTUI".
#
#    2014/11/22 rsg Updated ThemeWxPython to refles wxPython color
#                   scheme (Black on Silver).
#
#    2014/11/24 rsg Added 'linux' to the supported terminal emulator
#                   types.
#
#    2014/12/12 rsg Added Frederick A. Kier to the copyright notice
#                   to highlight his ground breaking role in
#                   prototyping the Command Line Interface.
#
#    2014/12/13 rsg Updated the wxPython and TeamSTARS themes to
#                   provide the Foreground and Background Colors
#                   needed by the SystemSettings.GetColour method.
#
#    2015/01/02 rsg Updated copyright, license and notice data.
#
#    2015/01/14 rsg Moved Masthead (formerly called Trademark),
#                   Copyright, License and Notice text to
#                   tsCxGlobals.
#
#    2016/03/15 rsg Set "USE_256_COLOR_PAIR_LIMIT" = True only for
#                   32-bit versions of "curses", "ncurses" 5.0 and
#                   "ncurses" 6.0.
#
#                   Set "USE_256_COLOR_PAIR_LIMIT" = False only for
#                   64-bit versions of "ncurses" 6.0 with Python
#                   3.5.1 or newer.
#
#                   Added 'Use_256_Color_Pair_Limit' entry in
#                   ThemeWxPython and ThemeTeamSTARS.
#
#    2016/12/20 rsg Update design to reflect new information about
#                   64-bit processor dependency of "ncurses" 6.0
#                   and Python 3.6.0.
#
#                   The 16-color with its associated 256-color-pair
#                   limit always applies on 32-bit processors and for
#                   software running in 32-bit compatibility-mode on
#                   64-bit processors. The Python Software foundation
#                   has declared that this limit will always apply to
#                   Python 2.x and Python 3.x through 3.5.2 releases.
#
#                   Set "USE_256_COLOR_PAIR_LIMIT" = True only for
#                   32-bit versions of "curses", "ncurses" 5.0 and
#                   "ncurses" 6.0. Also applies for versions running
#                   in 32-bit compatibility mode on 64-bit processors.
#
#                   Set "USE_256_COLOR_PAIR_LIMIT" = False only for
#                   64-bit versions of "ncurses" 6.0 with Python
#                   3.6.0 or later.
#
#    2017/06/06 rsg Correct "tsEnableColorPairLimit" method by
#                   replacing:
#                       "if (sys.maxsize <= 2**32):" by
#                       "if (sys.maxsize < 2**31):"
#                   because:
#                       for 64-bit processor:
#                                 2**64 = 18446744073709551616
#                                 2**63 =  9223372036854775808
#                           sys.maxsize =  9223372036854775807
#
#                       for 32-bit processor:
#                                 2**32 = 4294967296
#                                 2**31 = 2147483648
#                           sys.maxsize = 2147483647
#
#                       for 16-bit processor:
#                                 2**16 =      65536
#                                 2**15 =      32768
#                           sys.maxsize =      32767
#
#                       for  8-bit processor:
#                                 2**8  =        256
#                                 2**31 =        128
#                           sys.maxsize =        127
#
# ToDo:
#
#    2012/03/27 rsg Troubleshoot various unit test traps when
#                   "USE_CURSES_PANEL_STACK = True"
#
#    2012/07/03 rsg Reconcile need for Show with need for Panel Stack.
#                   (http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/
#                   panels.html). Panel Stack eExample doesn't use
#                   Show, but we need Show to delay creation of
#                   windows until distributed layouts have completed.
#
#    2012/07/15 rsg Investigate suitability and usability of
#                   tsLogger and tsWxLog configuration data.
#                   Also, eliminate duplicate definitions in
#                   tsLogger and tsWxLog.
#
#    2014/01/08 rsg Enable support for xterm-88color after debugging.
#
#    2014/01/19 rsg Complete construction, debug and test of
#                   xterm-88color and xterm-256color support.
#                   Waiting for release of ncurses wide character
#                   version of curses expected in Python 3.3 and
#                   compatible release of cygwin for windows.
#                   For details see:
#                   https://pypi.python.org/pypi/kaaedit/0.19.0
#
#################################################################

__title__     = 'tsWxGlobals'
__version__   = '1.44.1'
__date__      = '06/06/2017'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2017 ' + \
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
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t    for Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  nCurses README,v 1.23 2006/04/22'

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
import os
import platform
import sys

#---------------------------------------------------------------------------

tsPythonVersion = sys.version[0:5]
if (tsPythonVersion >= '1') and (tsPythonVersion < '2'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py1x'

elif (tsPythonVersion >= '2') and (tsPythonVersion < '3'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py2x'

elif (tsPythonVersion >= '3') and (tsPythonVersion < '4'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py3x'

else:

    # Presume tsWxGTUI_PyVx reflects default Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_PyVx'

ProductName   = 'TeamSTARS "%s" Toolkit' % tsWxGTUI_PyVx
SubSystemName = '"tsToolkitGUI"'
VendorName    = 'Richard S. Gordon, a.k.a. Software Gadgetry'
ThemeDate     = __date__

####################################################################
# Since version 5.4, the ncurses library decides how to interpret
# non-ASCII data using the nl_langinfo function. That means that you
# have to call locale.setlocale() in the application and encode
# Unicode strings using one of the system's available encodings.
# The following logic uses the system's default encoding:
#
import locale
locale.setlocale(locale.LC_ALL, '')
nCursesEncoding = locale.getpreferredencoding()
#
# Then use nCursesEncoding as the encoding for str.encode() calls.
####################################################################

#--------------------------------------------------------------------------

try:

    import tsLibCLI

    import tsCxGlobals

    Troubleshooting = tsCxGlobals.ThemeToUse['Troubleshooting']

    Debug_CLI_Configuration = Troubleshooting['Debug_CLI_Configuration'],
    Debug_CLI_Exceptions = Troubleshooting['Debug_CLI_Exceptions']
    Debug_CLI_Launch = Troubleshooting['Debug_CLI_Launch']
    Debug_CLI_Progress = Troubleshooting['Debug_CLI_Progress']
    Debug_CLI_Termination = Troubleshooting['Debug_CLI_Termination']
    Debug_GUI_Configuration = Troubleshooting['Debug_GUI_Configuration']
    Debug_GUI_Exceptions = Troubleshooting['Debug_GUI_Exceptions']
    Debug_GUI_Launch = Troubleshooting['Debug_GUI_Launch']
    Debug_GUI_Progress = Troubleshooting['Debug_GUI_Progress']
    Debug_GUI_Termination = Troubleshooting['Debug_GUI_Termination']

except ImportError as importCode:

    fmt1 = '%s: ImportError (tsLibCLI); ' % __title__
    fmt2 = 'importCode=%s' % str(importCode)
    msg = fmt1 + fmt2
    print(msg)

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    import tsLogger as Logger
    from tsReportUtilities import TsReportUtilities as tsrpu

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

DEBUG = Debug_CLI_Launch # TBD - Retain True to prevent Unimplemented Traps
VERBOSE = True

#---------------------------------------------------------------------------

System = platform.system()
Platform = '__TSWXCURSES__'

if (Platform == '__SMARTPHONE__'):
    # No borders by default on limited size screen
    USE_BORDER_BY_DEFAULT = False
else:
    USE_BORDER_BY_DEFAULT = True

USE_ACCESSIBILITY = False
USE_CARET = False
USE_CONSTRAINTS = False
USE_DRAG_AND_DROP = False
USE_HELP = False
USE_MENUS = False
USE_PALETTE = False
USE_SYSTEM_OPTIONS = False
USE_TOOLTIPS = False
USE_VALIDATORS = False

DefaultValidator = None

#---------------------------------------------------------------------------

def tsEnableColorPairLimit():
    '''
    Test computer hardware and software color palette configuration.

    Return "True" if "AT&T curses"/"ncurses 5.x" library is 32-bit and
    therefore supports up to 16 colors and 256 (16x16) color pairs;

       NOTE: Early "AT&T curses"/"ncurses 5.0" 32-bit implementations
             erroneously reported support for 256 colors with up to
             32767 color pairs.

    Return "False" if "ncurses 6.0" library, released 8 August 2015,
    is running on a 64-bit processor and is no longer constrained to
    emulate "ncurses 5.9" running on a 32-bit processor with up to
    16 colors.

       From "http://invisible-island.net/ncurses/announce.html":

          "These notes are for ncurses 6.0, released August 8, 2015.

          This release is designed to be source-compatible with ncurses
          5.0 through 5.9; providing a new application binary interface
          (ABI). Although the source can still be configured to support
          the ncurses 5 ABI, the intent of the release is to provide
          extensions which are generally useful, but binary-incompatible
          with ncurses 5:

             * Extend the cchar_t structure to allow more than 16 colors
               to be encoded.

             * Modify the encoding of mouse state to make room for a 5th
               mouse button. That allows one to use ncurses with a wheel
               mouse with xterm or similar X terminal emulators.
    '''
    
    myLoggerCLI = Logger.TsLogger(name='',
                                   threshold=Logger.INFO)

    if (sys.maxsize < 2**31):

        # 32-bit processors (or 64-bit processors running in 32-bit
        # compatibility mode) can only support up to 16 colors and up to
        # 256 color pairs (16 foreground colors x 16 background colors)
        HAS_256_COLOR_PAIR_LIMIT = True
        print('ALERT: tsWxGlobals ' + \
              '32-bit processor with ncurses 5.0:\n' + \
              'HAS_256_COLOR_PAIR_LIMIT=%s; sys.maxsize=%s' % (
                  str(HAS_256_COLOR_PAIR_LIMIT), str(sys.maxsize)))

    elif (tsPythonVersion <= '3.6.0'):

        # Regardless if 32-bit or 64-bit processor, Python 2.0.0 - 2.7.13 and
        # Python 3.0.0 - 3.6.0 can only support a maximum of 256 color pairs 
        # (16 foreground colors x 16 background colors)
        HAS_256_COLOR_PAIR_LIMIT = True
        print('ALERT: tsWxGlobals ' + \
              '64-bit processr with 32-bit ncurses 5.0/6.0;\n' + \
              'HAS_256_COLOR_PAIR_LIMIT=%s; tsPythonVersion=%s' % (
                  str(HAS_256_COLOR_PAIR_LIMIT), str(tsPythonVersion)))

    else:

        # Python, if 64-bit processor, beginning with 3.6.1 can support more
        # than 256 color pairs
        # (256 foreground colors x 256 background colors)
        HAS_256_COLOR_PAIR_LIMIT = False
        print('ALERT: tsWxGlobals ' + \
              '64-bit processr with ncurses 6.0 and Python > 3.6.0;\n' + \
              'HAS_256_COLOR_PAIR_LIMIT=%s; tsPythonVersion=%s' % (
                  str(HAS_256_COLOR_PAIR_LIMIT), str(tsPythonVersion)))

    return HAS_256_COLOR_PAIR_LIMIT

USE_256_COLOR_PAIR_LIMIT = tsEnableColorPairLimit()

#--------------------------------------------------------------------------

#########################################################################

theMasthead = tsCxGlobals.theMasthead
theCopyright = tsCxGlobals.theCopyright
theLicense = tsCxGlobals.theLicense
theNotices = tsCxGlobals.theNotices

theTrademark = theMasthead

#---------------------------------------------------------------------------
#
#    DESIGN NOTE:
#
#       From: Writing Programs with NCURSES
#
#             by Eric S. Raymond and Zeyd M. Ben-Halim
#             updates since release 1.9.9e by Thomas Dickey
#
#       The Panels Library:
#
#             The ncurses library by itself provides good support for
#             screen displays in which the windows are tiled (non-
#             overlapping). In the more general case that windows may
#             overlap, you have to use a series of wnoutrefresh() calls
#             followed by a doupdate(), and be careful about the order
#             you do the window refreshes in. It has to be bottom-
#             upwards, otherwise parts of windows that should be
#             obscured will show through.
#
#             When your interface design is such that windows may dive
#             deeper into the visibility stack or pop to the top at
#             runtime, the resulting book-keeping can be tedious and
#             difficult to get right. Hence the panels library.
#
#             NOTE: Limited screen real estate typically necessitates
#                   the overlapping of window objects. When the
#                   operator needs to see the features of a partially
#                   or totally hidden object, a Graphical User Interface
#                   uses a Task Bar with buttons for each frame or
#                   dialog. After moving the mouse over the button for
#                   the hidden object, the operator can click on the
#                   mouse button to bring a hidden background object
#                   to the visible foreground. The nCurses-based design
#                   provides a similar Task Bar.
#
#                   However, the current design's use of the wxWidgets-/
#                   wxPython-style "Show" method is incompatible with
#                   use of the nCurses Panel (Stack) library as evidenced
#                   by sample code (See http://tldp.org/HOWTO/NCURSES-
#                   Programming-HOWTO/panels.html). The sample code
#                   doesn't use components associated with "Show" method,
#                   but the wxPython emulation depends on them to accomodate
#                   a delay in the creation of nCurses windows until after
#                   the completion of associated distributed layouts.
#
USE_CURSES_PANEL_STACK = True # Might be ineffective. See NOTE above.
ENABLE_CURSES_RESIZE = False  # User Interface Exception NOT yet working.

#---------------------------------------------------------------------------

# Set of video display constants to specify character cell attributes:

DISPLAY_ALTCHARSET = curses.A_ALTCHARSET # Alternate character set mode.
DISPLAY_BLINK      = curses.A_BLINK      # Blink mode.
DISPLAY_BOLD       = curses.A_BOLD       # Bold mode.
DISPLAY_DIM        = curses.A_DIM        # Dim mode.
DISPLAY_NORMAL     = curses.A_NORMAL     # Normal attribute.
DISPLAY_REVERSE    = curses.A_REVERSE    # Reverse background and
                                         # foreground colors.
DISPLAY_STANDOUT   = curses.A_STANDOUT   # Standout mode.
DISPLAY_UNDERLINE  = curses.A_UNDERLINE  # Underline mode.

#---------------------------------------------------------------------------

# Define the number of tab positions that facilitate debugging the
# hierarchy of classes and modules via their entry and exit milestones.
#
# NOTE: Does not include those modules introduced by refactoring of
#       tsWxGraphicalTextUserInterface which are unconditionally
#       imported locally:
#           tsWxPythonColorRGBNames
#           tsWxPythonColorRGBValues
#           tsWxPythonColorNames
#           tsWxPythonColor16DataBase
#           tsWxPythonColor16SubstitutionMap
#           tsWxPythonColor256DataBase
#           from tsWxPythonColor88DataBase
#           from tsWxPythonColor8DataBase
#           tsWxPythonColor8SubstitutionMap
#           tsWxPythonColorDataBaseRGB
#           tsWxPythonMonochromeDataBase
#           tsWxPythonPrivateLogger

indentation = {
    'AcceleratorEntry': 1,
    'AcceleratorTable': 2,
    'App': 4,
    'BoxSizer': 3,
    'Button': 5,
    'Caret': 1,
    'CheckBox': 5,
    'CheckListBox': 7,
    'Color': 2,
    'ColorDatabase': 1,
    'Control': 4,
    'Cursor': 2,
    'Dialog': 5,
    'DialogButton': 6,
    'Display': 1,
    'DoubleLinkedList': None,
    'DoubleLinkedListNode': None,
    'Event': 2,
    'EventLoop': 1,
    'EventLoopActivator': 1,
    'EvtHandler': 2,
    'FlexGridSizer': 4,
    'FocusEvent': 3,
    'Frame': 5,
    'FrameButton': 6,
    'Gauge': 5,
    'Globals': None,
    'GraphicalTextUserInterface': 1,
    'GridBagSizer': 5,
    'GridSizer': 3,
    'KeyEvent': 3,
    'LayoutAlgorithm': 2,
    'Menu': 3,
    'MenuBar': 4,
    'MouseEvent': 3,
    'MouseState': None,
    'Object': 1,
    'Panel': 4,
    'PasswordEntryDialog': 7,
    'Point': None,
    'PyApp': 3,
    'PyEventBinding': 1,
    'PyOnDemandOutputWindow': 5,
    'PyOnDemandStdioWindow': 5,
    'PySimpleApp': 5,
    'PySizer': 3,
    'RadioBox': 5,
    'RadioButton': 5,
    'Rect': None,
    'Screen': 5,
    'ScrollBar': 5,
    'ScrollBarButton': 5,
    'ScrollBarGauge': 5,
    'ScrolledText': 5,
    'ScrolledWindow': 5,
    'ShowEvent': 3,
    'Size': None,
    'Sizer': 2,
    'SizerFlags': 1,
    'SizerSpacer': 3,
    'SizerItem': 2,
    'Slider': 5,
    'SplashScreen': 5,
    'StaticBox': 5,
    'StaticBoxSizer': 4,
    'StaticLine': 5,
    'StaticText': 5,
    'StatusBar': 4,
    'SystemSettings': None,
    'TaskBar': 5,
    'TextCtrl': 5,
    'TextEditBox': 7,
    'TextEntryDialog': 6,
    'Timer': 4, # Child of TimerBase instead of EvtHandler.
    'TimerBase': 3, # Child of EvtHandler; Parent of Timer.
    'TimerDescriptor': None,
    'TimerQueue': None,
    'TimerScheduler': None,
    'ToggleButton': 5,
    'TopLevelWindow': 4,
    'Validator': 3,
    'Window': 3,
    'WindowCurses': 3

##    'ActivateEvent': 3,
##    'AuiManagerEvent': 3,
##    'BookCtrlBaseEvent': 3,
##    'CalculateLayoutEvent': 3,
##    'CallLater': 3,
##    'ChildFocusEvent': 3,
##    'ChoicebookEvent': 3,
##    'ClipboardTextEvent': 3,
##    'CloseEvent': 3,
##    'CollapsiblePaneEvent': 3,
##    'ColourPickerEvent': 3,
##    'CommandEvent': 3,
##    'ContextMenuEvent': 3,
##    'DateEvent': 3,
##    'DisplayChangedEvent': 3,
##    'DropFilesEvent': 3,
##    'EraseEvent': 3,
##    'EventLoopGuarantor': 3,
##    'FileDirPickerEvent': 3,
##    'FindDoalogEvent': 3,
##    'FocusEvent': 3,
##    'FontPickerEvent': 3,
##    'HelpEvent': 3,
##    'HyperlinkEvent': 3,
##    'IconizeEvent': 3,
##    'IdleEvent': 3,
##    'InitDialogEvent': 3,
##    'JoystickEvent': 3,
##    'ListEvent': 3,
##    'MaximizeEvent': 3,
##    'MenuEvent': 3,
##    'MouseCaptureChangedEvent': 3,
##    'MouseCaptureLostEvent': 3,
##    'NavigationKeyEvent': 3,
##    'NcPaintEvent': 3,
##    'NotebookEvent': 3,
##    'NotifyEvent': 3,
##    'PaintEvent': 3,
##    'PaletteChangedEvent': 3,
##    'PowerEvent': 3,
##    'ProcessEvent': 3,
##    'PyEvent': 3,
##    'QueryLayoutInfoEvent': 3,
##    'QueryNewPaletteEvent': 3,
##    'ScrollEvent': 3,
##    'ScrollWinEvent': 3,
##    'SetCursorEvent': 3,
##    'SizeEvent': 3,
##    'SpinEvent': 3,
##    'SysColourChangedEvent': 3,
##    'TaskBarIconEvent': 3,
##    'TimerEvent': 3,

    }

#---------------------------------------------------------------------------

EmptyList = []
EmptyString = ''
PyEmptyStringArray = []

pageWidth = 80
pageLength = 66

#---------------------------------------------------------------------------

# Default user text input prompt messages
ID_TEXT = 3000
GetTextFromUserPromptStr = 'Input Text'
GetPasswordFromUserPromptStr = 'Enter Password'

# Default tsApplication names
cliLoggerNameStr = 'cliAPP'
guiLoggerNameStr = 'guiAPP'

# Default wxPython window names
BitmapRadioButtonNameStr = 'radioButton'
ButtonNameStr = 'button'
CheckBoxNameStr = 'check'
ChoiceNameStr = 'choice'
ComboBoxNameStr = 'comboBox'
ControlNameStr = 'control'
CursorNameStr = 'cursor'
DialogNameStr = 'dialog'
DialogButtonNameStr = 'dialogButton'
FrameNameStr = 'frame'
FrameButtonNameStr = 'frameButton'
GaugeNameStr = 'gauge'
ListBoxNameStr = 'listBox'
MenuBarNameStr = 'menuBar'
NotebookNameStr = 'notebook'
PanelNameStr = 'panel'
PasswordEntryDialogNameStr = 'passwordEntryDialog'
RadioBoxNameStr = 'radioBox'
RadioButtonNameStr = 'radioButton'
ScreenNameStr = 'screen'
ScrollBarButtonNameStr = 'scrollBarButton'
ScrollBarGaugeNameStr = 'scrollBarGauge'
ScrollBarNameStr = 'scrollBar'
HorizontalScrollBarNameStr = 'horizontalScrollBar'
VerticalScrollBarNameStr = 'verticalScrollBar'
ScrolledNameStr = 'scrolled'
ScrolledTextNameStr = 'scrolledText'
SliderNameStr = 'slider'
SplashScreenNameStr = 'splashScreen'
StaticBitmapNameStr = 'staticBitmap'
StaticBoxNameStr = 'groupBox'
StaticLineNameStr = 'staticLine'
StaticTextNameStr = 'staticText'
StatusBarNameStr = 'statusBar'
StatusLineNameStr = 'status_line'
StdioNameStr = 'stdio'
StdioTitleStr = 'tsWxPython: stdout/stderr'
StdioRedirectedTitleStr = 'Redirected Output: stdout/stderr'
TaskBarNameStr = 'TaskBar'
TaskBarTitleStr = 'Tasks'
TextCtrlNameStr = 'text'
TextEditBoxNameStr = 'textEditBox'
TextEntryDialogNameStr = 'textEntryDialog'
ToggleButtonNameStr = 'wxToggleButton'
ToolBarNameStr = 'toolbar'
TreeCtrlNameStr = 'treeCtrl'

# Import dependency precludes use of isinstance(window, type(TopLevelWindow)
TopLevelClasses = ['Frame',
                   'Dialog',
                   'PasswordEntryDialog',
                   'Screen',
                   'SplashScreen',
                   'TaskBar',
                   'TextEntryDialog']

#---------------------------------------------------------------------------

# Modeled after enum in sizer.h file of wxWidgets.
Item_None   = 0
Item_Window = 1
Item_Sizer  = 2
Item_Spacer = 3
Item_Max    = 4

# Modeled after enum in window.h file of wxWidgets.

OrderBefore = 0 # insert before the given window
OrderAfter  = 1 # insert after the given window

# Modeled after enum in layout.h file of wxWidgets.

Unconstrained = 0
AsIs          = 1
PercentOf     = 2
Above         = 3
Below         = 4
LeftOf        = 5
RightOf       = 6
SameAs        = 7
Absolute      = 8 

#---------------------------------------------------------------------------

# Automatic wxPython object placement and dimensioning features
DefaultCoord = -1

UseDefaultValue = DefaultCoord

DefaultValue = DefaultCoord

DefaultPosition = (DefaultCoord, DefaultCoord)

DefaultRectangle = (DefaultCoord, DefaultCoord,
                    DefaultCoord, DefaultCoord)

DefaultSize = (DefaultCoord, DefaultCoord)

DefaultVideoMode = 'Curses'

NullAcceleratorTable = []

#---------------------------------------------------------------------------

# wxWidgets Stock Logging Levels

LOG_FatalError = 0 # program can't continue, abort immediately
LOG_Error      = 1 # a serious error, user must be informed about it
LOG_Warning    = 2 # user is normally informed about it but may be ignored
LOG_Message    = 3 # normal message (i.e. normal output of a non GUI app)
LOG_Status     = 4 # informational: might go to the status line of GUI app
LOG_Info       = 5 # informational message (a.k.a. 'Verbose')
LOG_Debug      = 6 # never shown to the user, disabled in release mode
LOG_Trace      = 7 # trace messages are also only enabled in debug mode
LOG_Progress   = 8 # used for progress indicator (not yet)
LOG_User       = 100 # user defined levels start here
LOG_Max        = 10000

# The following defines tsLogger sverity levels which
# may be used as a threshold filter for console output.
NOTSET        = 0
DEBUG         = 10
INFO          = 20
NOTICE        = INFO + 5
WARNING       = 30
ALERT         = WARNING + 5
ERROR         = 40
CRITICAL      = 50
EMERGENCY     = CRITICAL + 5

#---------------------------------------------------------------------------

#The stock wxPython IDs and sample labels are

ACCEL_ALT                 = 0x00000001
if System == 'Darwin':
    ACCEL_CMD             = 0x00000008
else:
    ACCEL_CMD             = 0x00000002
ACCEL_CTRL                = 0x00000002
ACCEL_NORMAL              = 0x00000000
ACCEL_SHIFT               = 0x00000004
ADJUST_MINSIZE            = 0
ALWAYS_SHOW_SB            = 0x00800000
BACKINGSTORE              = 0
BACKWARD                  = 0x00002000
BG_STYLE_COLOUR           = 2
BG_STYLE_CUSTOM           = 3
BG_STYLE_SYSTEM           = 1
BI_EXPAND                 = 0x00002000
BORDER                    = 0x02000000
BORDER_DEFAULT            = 0
BORDER_DOUBLE             = 0x10000000
BORDER_MASK               = 0x1F200000
BORDER_NONE               = 0x00200000
BORDER_RAISED             = 0x04000000
BORDER_SIMPLE             = 0x02000000
BORDER_STATIC             = 0x01000000
BORDER_SUNKEN             = 0x08000000
BORDER_THEME              = BORDER_DOUBLE
BOTTOM                    = 0x00000080
BU_BOTTOM                 = 0x00000200
BU_EXACTFIT               = 0x00000001
BU_LEFT                   = 0x00000040
BU_RIGHT                  = 0x00000100
BU_TOP                    = 0x00000080
ButtonSizerFlags          = 0x0000809E
CANCEL                    = 0x00000010
CAPTION                   = 0x20000000
CB_DROPDOWN               = 0x00000020
CB_READONLY               = 0x00000010
CB_SIMPLE                 = 0x00000004
CB_SORT                   = 0x00000008
CENTER                    = 0x00000001
CENTER_FRAME              = 0x00000000
CENTER_ON_SCREEN          = 0x00000002
CENTRE                    = 0x00000001
CENTRE_ON_SCREEN          = 0x00000002
CHK_2STATE                = 0
CHK_3STATE                = 0x00001000
CHK_ALLOW_3RD_STATE_FOR_USER = 0x00002000
CHK_CHECKED               = 0x00000001
CHK_UNCHECKED             = 0x00000000
CHK_UNDETERMINED          = 0x00000002
CLIP_CHILDREN             = 0x00400000
CLIP_SIBLINGS             = 0x20000000
CLOSE_BOX                 = 0x00001000
COLOURED                  = 0x00000800
DEFAULT_CONTROL_BORDER    = BORDER_SUNKEN # 0x08000000
DIALOG_EX_CONTEXTHELP     = 0x00000080
DIALOG_EX_METAL           = 0x00000040
DOUBLE_BORDER             = BORDER_DOUBLE # 0x10000000
DOWN                      = 0x00000080
EAST                      = 0x00000020
EXPAND                    = 0x00002000
FIXED_LENGTH              = 0x00000400
FIXED_MINSIZE             = 0x00008000
FORWARD                   = 0x00001000
FRAME_DRAWER              = 0x00000020
FRAME_EX_CONTEXTHELP      = 0x00000080
FRAME_EX_METAL            = 0x00000040
FRAME_NO_WINDOW_MENU      = 0x00000100
FRAME_SHAPED              = 0x00000010
FRAME_TOOL_WINDOW         = 0x00000004
FULL_REPAINT_ON_RESIZE    = 0x00010000

GA_HORIZONTAL             = 0x00000004
GA_VERTICAL               = 0x00000008

SL_HORIZONTAL             = GA_HORIZONTAL
SL_VERTICAL               = GA_VERTICAL

GROW                      = 0x00002000
HELP                      = 0x00008000
HSCROLL                   = 0x40000000
ICON_ASTERISK             = 0x00000800
ICON_ERROR                = 0x00000200
ICON_EXCLAMATION          = 0x00000100
ICON_HAND                 = 0x00000200
ICON_INFORMATION          = 0x00000800
ICON_QUESTION             = 0x00000400
ICON_STOP                 = 0x00000200
ICON_WARNING              = 0x00000100
Layout_Default            = 0
Layout_LeftToRight        = 1
Layout_RightToLeft        = 2
LB_ALWAYS_SB              = 0x00000400
LB_EXTENDED               = 0x00000080
LB_HSCROLL                = 0x40000000
LB_INT_HEIGHT             = 0x00000800
LB_MULTIPLE               = 0x00000040
LB_NEEDED_SB              = 0x00000200
LB_OWNERDRAW              = 0x00000100
LB_SINGLE                 = 0x00000020
LB_SORT                   = 0x00000010
LEFT                      = 0x00000010
LI_HORIZONTAL             = 0x00000004
LI_VERTICAL               = 0x00000008
MAXIMIZE_BOX              = 0x00000200
MB_DOCKABLE               = 0x00000001
MENU_TEAROFF              = 0x00000001
MINIMIZE_BOX              = 0x00000400
MORE                      = 0x00010000
NORTH                     = 0x00000040
NO_BORDER                 = BORDER_NONE #0x00200000
NO_DEFAULT                = 0x00000080
NO_FULL_REPAINT_ON_RESIZE = 0x00000000
OK                        = 0x00000004
POPUP_WINDOW              = 0x00020000
PYAPP_ASSERT_SURPRESS     = 1
PYAPP_ASSERT_EXCEPTION    = 2
PYAPP_ASSERT_DIALOG       = 4
PYAPP_ASSERT_LOG          = 8
RAISED_BORDER             = BORDER_RAISED # 0x04000000
RA_HORIZONTAL             = 0x00000004
RA_LEFTTORIGHT            = 0x00000001
RA_SPECIFY_COLS           = 0x00000004
RA_SPECIFY_ROWS           = 0x00000008
RA_TOPTOBOTTOM            = 0x00000002
RA_USE_CHECKBOX           = 0x00000010
RA_VERTICAL               = 0x00000008
RB_GROUP                  = 0x00000004
RB_SINGLE                 = 0x00000008
RB_USE_CHECKBOX           = 0x00000010
RESERVE_SPACE_EVEN_IF_HIDDEN = 0x0002
RESET                     = 0x00004000
RESIZE_BORDER             = 0x00000040
RETAINED                  = 0
RIGHT                     = 0x00000020
SB_HORIZONTAL             = 0x00000004
SB_VERTICAL               = 0x00000008
SETUP                     = 0x00020000
SHAPED                    = 0x00004000
SHRINK                    = 0x00001000
SIMPLE_BORDER             = BORDER_SIMPLE # 0x02000000

SIZE_USE_EXISTING         = 0x0000
SIZE_AUTO_WIDTH           = 0x0001
SIZE_AUTO_HEIGHT          = 0x0002
SIZE_AUTO                 = (SIZE_AUTO_WIDTH | SIZE_AUTO_HEIGHT)
SIZE_ALLOW_MINUS_ONE      = 0x0004
SIZE_NO_ADJUSTMENTS       = 0x0008
SIZE_FORCE                = 0x0010
SIZE_FORCE_EVENT          = 0x0020 

SOUTH                     = 0x00000080
SP_ARROW_KEYS             = 0x00001000
SP_HORIZONTAL             = 0x00000004
SP_VERTICAL               = 0x00000008
SP_WRAP                   = 0x00002000
STATIC_BORDER             = BORDER_STATIC # 0x01000000
STAY_ON_TOP               = 0x00008000
STRETCH_NOT               = 0x00000000
ST_DOTS_END               = 0x00000004
ST_DOTS_MIDDLE            = 0x00000002
ST_NO_AUTORESIZE          = 0x00000001
ST_SIZEGRIP               = 0x00000010
SUNKEN_BORDER             = BORDER_SUNKEN # 0x08000000
SYSTEM_MENU               = 0x00000800
TAB_TRAVERSAL             = 0x00080000
TC_BOTTOM                 = 0x00000080
TC_FIXEDWIDTH             = 0x00000020
TC_LEFT                   = 0x00000020
TC_MULTILINE              = 0x00000200
TC_OWNERDRAW              = 0x00000400
TC_RIGHT                  = 0x00000040
TC_RIGHTJUSTIFY           = 0x00000010
TC_TOP                    = 0x00000000
TITLE                     = 0x0000C000
TOP                       = 0x00000040
TRANSPARENT_WINDOW        = 0x00100000
UP                        = 0x00000040

UPDATE_UI_NONE            = 0x0000,
UPDATE_UI_RECURSE         = 0x0001,
UPDATE_UI_FROMIDLE        = 0x0002 # Invoked from On(Internal)Idle

VSCROLL                   = 0x80000000
WANTS_CHARS               = 0x00040000
WEST                      = 0x00000010
WINDOW_DEFAULT_VARIANT    = 'window-default-variant' 
WINDOW_VARIANT_NORMAL     = 0
WS_EX_BLOCK_EVENTS        = 0x00000002
WS_EX_CONTEXTHELP         = 0x00000080
WS_EX_PROCESS_IDLE        = 0x00000010
WS_EX_PROCESS_UI_UPDATES  = 0x00000020
WS_EX_THEMED_BACKGROUND   = 0x00000008
WS_EX_TRANSIENT           = 0x00000004
WS_EX_VALIDATE_RECURSIVELY = 0x00000001
YES_DEFAULT               = 0x00000000
YES                       = 0x00000002
NO                        = 0x00000008

ALL                       = 0x00000040 | 0x00000080 | 0x00000020 | 0x00000010
ALIGN_BOTTOM              = 0x00000400
ALIGN_CENTER_HORIZONTAL   = 0x00000100
ALIGN_CENTER_VERTICAL     = 0x00000800
ALIGN_LEFT                = 0x00000000
ALIGN_MASK                = 0x00000F00
ALIGN_NOT                 = 0x00000000
ALIGN_RIGHT               = 0x00000200
ALIGN_TOP                 = 0x00000000
ALIGN_CENTER              = ALIGN_CENTER_HORIZONTAL | ALIGN_CENTER_VERTICAL
HORIZONTAL                = 0x00000004
VERTICAL                  = 0x00000008
BOTH                      = HORIZONTAL | VERTICAL
ICON_MASK                 = ICON_EXCLAMATION | \
                            ICON_ERROR | \
                            ICON_QUESTION | \
                            ICON_INFORMATION
YES_NO                    = YES | NO

WANTS_CHARS               = 0x00040000

# values which define the behaviour for resizing wxFlexGridSizer cells in the
# "non-flexible" direction
#
# wxFlexSizerGrowMode (simulates enumerated values)
#
# don't resize the cells in non-flexible direction at all
FLEX_GROWMODE_NONE        = 0x00000000

# uniformly resize only the specified ones (default)
FLEX_GROWMODE_SPECIFIED   = 0x00000001

# uniformly resize all cells
FLEX_GROWMODE_ALL         = 0x00000002

# background is erased in the EVT_ERASE_BACKGROUND handler or using the
# system default background if no such handler is defined (this is the
# default style)
BG_STYLE_ERASE = 0

# background is erased by the system, no EVT_ERASE_BACKGROUND event is
# generated at all
BG_STYLE_SYSTEM = 1

# background is erased in EVT_PAINT handler and not erased at all before
# it, this should be used if the paint handler paints over the entire
# window to avoid flicker
BG_STYLE_PAINT = 2

# this is a Mac-only style, don't use in portable code
BG_STYLE_TRANSPARENT = 4

# this style is deprecated and doesn't do anything, don't use
BG_STYLE_COLOUR = 8

# this style is deprecated and is synonymous with BG_STYLE_PAINT, use
# the new name
BG_STYLE_CUSTOM = BG_STYLE_PAINT

BACKGROUNDSTYLE = [BG_STYLE_COLOUR,
                   BG_STYLE_CUSTOM,
                   BG_STYLE_ERASE,
                   BG_STYLE_PAINT,
                   BG_STYLE_SYSTEM,
                   BG_STYLE_TRANSPARENT
                   ]

DEFAULT_DIALOG_STYLE = BORDER_SIMPLE | \
                       CAPTION | \
                       CLOSE_BOX | \
                       MAXIMIZE_BOX | \
                       MINIMIZE_BOX | \
                       RESIZE_BORDER | \
                       SYSTEM_MENU

DEFAULT_FRAME_STYLE = BORDER_SIMPLE | \
                      CAPTION | \
                      CLOSE_BOX | \
                      MAXIMIZE_BOX | \
                      MINIMIZE_BOX | \
                      RESIZE_BORDER | \
                      SYSTEM_MENU

DEFAULT_SPLASHSCREEN_STYLE = TRANSPARENT_WINDOW

if True:
    DEFAULT_STDIO_STYLE = BORDER_SIMPLE | \
                          CAPTION
else:
    DEFAULT_STDIO_STYLE = BORDER_SIMPLE | \
                          CAPTION | \
                          CLOSE_BOX | \
                          MAXIMIZE_BOX | \
                          MINIMIZE_BOX | \
                          RESIZE_BORDER

DEFAULT_TASK_STYLE = BORDER_SIMPLE | \
                     CAPTION | \
                     RESIZE_BORDER

PASSWORD_ENTRY_DIALOG_STYLE = DEFAULT_DIALOG_STYLE | \
                          OK | \
                          CANCEL | \
                          CENTRE

TEXT_ENTRY_DIALOG_STYLE = DEFAULT_DIALOG_STYLE | \
                          OK | \
                          CANCEL | \
                          CENTRE

TextEntryDialogStyle = TEXT_ENTRY_DIALOG_STYLE

DEFAULT_MENUBAR_STYLE = BORDER_SIMPLE

DEFAULT_PANEL_STYLE = TAB_TRAVERSAL | NO_BORDER

DEFAULT_TEXTEDITBOX_STYLE = NO_BORDER

## DEFAULT_STATUSBAR_STYLE = BORDER_SIMPLE
DEFAULT_STATUSBAR_STYLE = BORDER_SIMPLE | \
                          FULL_REPAINT_ON_RESIZE | \
                          ST_SIZEGRIP

DEFAULT_WIDGET_STYLE = NO_BORDER

WINDOW_STYLE_MASK = ALWAYS_SHOW_SB | \
                    BORDER_MASK | \
                    CLIP_CHILDREN | \
                    CLIP_SIBLINGS | \
                    FULL_REPAINT_ON_RESIZE | \
                    HSCROLL | \
                    POPUP_WINDOW | \
                    RETAINED | \
                    TAB_TRAVERSAL | \
                    TRANSPARENT_WINDOW | \
                    VSCROLL | \
                    WANTS_CHARS

NOT_FOUND                 = -1
SCREEN_STYLE_DEFAULT      = 0

SHARED_IMAGE              = TRANSPARENT_WINDOW

EVT_DAEMON_TIMETOSLEEP = float(0.200)
EVT_NULL = 0
EVT_FIRST = 10000
EVT_USER_FIRST = EVT_FIRST + 2000

MOUSE_BTN_ANY             = -1
MOUSE_BTN_NONE            = -1
MOUSE_BTN_LEFT            = 0
MOUSE_BTN_MIDDLE          = 1
MOUSE_BTN_RIGHT           = 2

#---------------------------------------------------------------------------
# wxCursor Stock Cursor IDs

CURSOR_ARROW = 1
CURSOR_ARROWWAIT = 27
CURSOR_BLANK = 26
CURSOR_BULLSEYE = 3
CURSOR_CHAR = 4
CURSOR_COPY_ARROW = 1
CURSOR_CROSS = 5
CURSOR_DEFAULT = 1
CURSOR_HAND = 6
CURSOR_IBEAM = 7
CURSOR_LEFT_BUTTON = 8
CURSOR_MAGNIFIER = 9
CURSOR_MIDDLE_BUTTON = 10
CURSOR_NO_ENTRY = 11
CURSOR_PAINT_BRUSH = 12
CURSOR_PENCIL = 13
CURSOR_POINT_LEFT = 14
CURSOR_POINT_RIGHT = 15
CURSOR_QUESTION_ARROW = 16
CURSOR_RIGHT_ARROW = 2
CURSOR_RIGHT_BUTTON = 17
CURSOR_SIZENESW = 18
CURSOR_SIZENS = 19
CURSOR_SIZENWSE = 20
CURSOR_SIZEWE = 21
CURSOR_SIZING = 22
CURSOR_SPRAYCAN = 23
CURSOR_WAIT = 24
CURSOR_WATCH = 25

# wxCursor Stock Cursor Names

CURSOR_ARROW_NAME = 'CURSOR_ARROW'
CURSOR_ARROWWAIT_NAME = 'CURSOR_ARROWWAIT'
CURSOR_BLANK_NAME = 'CURSOR_BLANK'
CURSOR_BULLSEYE_NAME = 'CURSOR_BULLSEYE'
CURSOR_CHAR_NAME = 'CURSOR_CHAR'
CURSOR_COPY_ARROW_NAME = 'CURSOR_COPY_ARROW'
CURSOR_CROSS_NAME = 'CURSOR_CROSS'
CURSOR_DEFAULT_NAME = 'CURSOR_DEFAULT'
CURSOR_HAND_NAME = 'CURSOR_HAND'
CURSOR_IBEAM_NAME = 'CURSOR_IBEAM'
CURSOR_LEFT_BUTTON_NAME = 'CURSOR_LEFT_BUTTON'
CURSOR_MAGNIFIER_NAME = 'CURSOR_MAGNIFIER'
CURSOR_MIDDLE_BUTTON_NAME = 'CURSOR_MIDDLE_BUTTON'
CURSOR_NO_ENTRY_NAME = 'CURSOR_NO_ENTRY'
CURSOR_PAINT_BRUSH_NAME = 'CURSOR_PAINT_BRUSH'
CURSOR_PENCIL_NAME = 'CURSOR_PENCIL'
CURSOR_POINT_LEFT_NAME = 'CURSOR_POINT_LEFT'
CURSOR_POINT_RIGHT_NAME = 'CURSOR_POINT_RIGHT'
CURSOR_QUESTION_ARROW_NAME = 'CURSOR_QUESTION_ARROW'
CURSOR_RIGHT_ARROW_NAME = 'CURSOR_RIGHT_ARROW'
CURSOR_RIGHT_BUTTON_NAME = 'CURSOR_RIGHT_BUTTON'
CURSOR_SIZENES_NAME = 'CURSOR_SIZENESW'
CURSOR_SIZENS_NAME = 'CURSOR_SIZENS'
CURSOR_SIZENWSE_NAME = 'CURSOR_SIZENWSE'
CURSOR_SIZEWE_NAME = 'CURSOR_SIZEWE'
CURSOR_SIZING_NAME = 'CURSOR_SIZING'
CURSOR_SPRAYCAN_NAME = 'CURSOR_SPRAYCAN'
CURSOR_WAIT_NAME = 'CURSOR_WAIT'
CURSOR_WATCH_NAME = 'CURSOR_WATCH'

#---------------------------------------------------------------------------
# wxTextCtrl style flags

TE_NO_VSCROLL             = 0x0002
TE_AUTO_SCROLL            = 0x0008

TE_READONLY               = 0x0010
TE_MULTILINE              = 0x0020
TE_PROCESS_TAB            = 0x0040

TE_LEFT                   = 0x0000
TE_CENTER                 = ALIGN_CENTER_HORIZONTAL # 0x0100
TE_RIGHT                  = ALIGN_RIGHT             # 0x0200
TE_CENTRE                 = TE_CENTER

TE_RICH                   = 0x0080

TE_PROCESS_ENTER          = 0x0400
TE_PASSWORD               = 0x0800

TE_AUTO_URL               = 0x1000

TE_NOHIDESEL              = 0x2000

# use HSCROLL to not wrap text at all, wxTE_CHARWRAP to wrap it at any
# position and wxTE_WORDWRAP to wrap at words boundary
#
# if no wrapping style is given at all, the control wraps at word boundary
TE_DONTWRAP               = HSCROLL
TE_CHARWRAP               = 0x4000  # wrap at any position
TE_WORDWRAP               = 0x0001  # wrap only at words boundaries
TE_BESTWRAP               = 0x0000  # this is the default

#---------------------------------------------------------------------------

# The "&" precedes the character chosen for use as the accelerator hot-key.
ID_ABOUT = '&About'
ID_ADD = 'Add'
ID_NONE = -3
ID_SEPARATOR = -2
ID_ANY = -1
ID_LOWEST = 4999
ID_HIGHEST = 5999
ID_APPLY = '&Apply'
ID_BACKWARD = '&Back'
ID_BOLD = '&Bold'
ID_CANCEL = '&Cancel'
ID_CLEAR = '&Clear'
ID_CLOSE = '&Close'
ID_COPY = '&Copy'
ID_CUT = 'Cu&t'
ID_DELETE = '&Delete'
ID_DOWN = '&Down'
ID_EDIT = '&Edit'
ID_EXIT = '&Quit'
ID_FILE = '&File'
ID_FIND = '&Find'
ID_FORWARD = '&Forward'
ID_HELP = '&Help'
ID_HOME = '&Home'
ID_INDENT = 'Indent'
ID_INDEX = '&Index'
ID_ITALIC = '&Italic'
ID_JUSTIFY_CENTER = 'Centered'
ID_JUSTIFY_FILL = 'Justified'
ID_JUSTIFY_LEFT = 'Align Left'
ID_JUSTIFY_RIGHT = 'Align Right'
ID_NEW = '&New'
ID_NO = '&No'
ID_OK = '&OK'
ID_OPEN = '&Open'
ID_PASTE = '&Paste'
ID_PREFERENCES = '&Preferences'
ID_PREVIEW = 'Print previe&w'
ID_PRINT = '&Print'
ID_PROPERTIES = '&Properties'
ID_REDO = '&Redo'
ID_REFRESH = 'Refresh'
ID_REMOVE = 'Remove'
ID_REPLACE = 'Rep&lace'
ID_REVERT_TO_SAVED = 'Revert to Saved'
ID_SAVE = '&Save'
ID_SAVEAS = 'Save &As...'
ID_SELECTALL = 'Select all'
ID_STOP = '&Stop'
ID_UNDELETE = 'Undelete'
ID_UNDERLINE = '&Underline'
ID_UNDO = '&Undo'
ID_UNINDENT = '&Unindent'
ID_UP = '&Up'
ID_YES = '&Yes'
ID_ZOOM_100 = '&Actual Size'
ID_ZOOM_FIT = 'Zoom to &Fit'
ID_ZOOM_IN = 'Zoom &In'
ID_ZOOM_OUT = 'Zoom &Out'

ITEM_SEPARATOR = -1
ITEM_NORMAL = 0
ITEM_CHECK = 1
ITEM_RADIO = 2
ITEM_MAX = 3

#---------------------------------------------------------------------------

ALPHA_TRANSPARENT = 0
ALPHA_OPAQUE = 255

#---------------------------------------------------------------------------

# Set of color identifiers. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.
COLOR_ALICE_BLUE               = 'alice blue'
COLOR_ANTIQUE_WHITE            = 'antique white'
COLOR_ANTIQUE_WHITE1           = 'antique white1'
COLOR_ANTIQUE_WHITE2           = 'antique white2'
COLOR_ANTIQUE_WHITE3           = 'antique white3'
COLOR_ANTIQUE_WHITE4           = 'antique white4'
COLOR_AQUAMARINE               = 'aquamarine'
COLOR_AQUAMARINE1              = 'aquamarine1'
COLOR_AQUAMARINE2              = 'aquamarine2'
COLOR_AQUAMARINE3              = 'aquamarine3'
COLOR_AQUAMARINE4              = 'aquamarine4'
COLOR_AZURE                    = 'azure'
COLOR_AZURE1                   = 'azure1'
COLOR_AZURE2                   = 'azure2'
COLOR_AZURE3                   = 'azure3'
COLOR_AZURE4                   = 'azure4'
COLOR_BEIGE                    = 'beige'
COLOR_BISQUE                   = 'bisque'
COLOR_BISQUE1                  = 'bisque1'
COLOR_BISQUE2                  = 'bisque2'
COLOR_BISQUE3                  = 'bisque3'
COLOR_BISQUE4                  = 'bisque4'
COLOR_BLACK                    = 'black'
COLOR_BLANCHED_ALMOND          = 'blanched almond'
COLOR_BLUE                     = 'blue'
COLOR_BLUE1                    = 'blue1'
COLOR_BLUE2                    = 'blue2'
COLOR_BLUE3                    = 'blue3'
COLOR_BLUE4                    = 'blue4'
COLOR_BLUE_VIOLET              = 'blue violet'
COLOR_BROWN                    = 'brown'
COLOR_BROWN1                   = 'brown1'
COLOR_BROWN2                   = 'brown2'
COLOR_BURLYWOOD                = 'burlywood'
COLOR_BURLYWOOD1               = 'burlywood1'
COLOR_BURLYWOOD2               = 'burlywood2'
COLOR_BURLYWOOD3               = 'burlywood3'
COLOR_BURLYWOOD4               = 'burlywood4'
COLOR_CADET_BLUE               = 'cadet blue'
COLOR_CADET_BLUE1              = 'cadet blue1'
COLOR_CADET_BLUE2              = 'cadet blue2'
COLOR_CADET_BLUE3              = 'cadet blue3'
COLOR_CADET_BLUE4              = 'cadet blue4'
COLOR_CHARTREUSE               = 'chartreuse'
COLOR_CHARTREUSE1              = 'chartreuse1'
COLOR_CHARTREUSE2              = 'chartreuse2'
COLOR_CHARTREUSE3              = 'chartreuse3'
COLOR_CHARTREUSE4              = 'chartreuse4'
COLOR_CHOCOLATE                = 'chocolate'
COLOR_CHOCOLATE1               = 'chocolate1'
COLOR_CHOCOLATE2               = 'chocolate2'
COLOR_CHOCOLATE3               = 'chocolate3'
COLOR_CHOCOLATE4               = 'chocolate4'
COLOR_CORAL                    = 'coral'
COLOR_CORAL1                   = 'coral1'
COLOR_CORAL2                   = 'coral2'
COLOR_CORAL3                   = 'coral3'
COLOR_CORAL4                   = 'coral4'
COLOR_CORNFLOWER_BLUE          = 'cornflower blue'
COLOR_CORNSILK                 = 'cornsilk'
COLOR_CORNSILK1                = 'cornsilk1'
COLOR_CORNSILK2                = 'cornsilk2'
COLOR_CORNSILK3                = 'cornsilk3'
COLOR_CORNSILK4                = 'cornsilk4'
COLOR_CRIMSON                  = 'crimson'
COLOR_CYAN                     = 'cyan'
COLOR_CYAN1                    = 'cyan1'
COLOR_CYAN2                    = 'cyan2'
COLOR_CYAN3                    = 'cyan3'
COLOR_CYAN4                    = 'cyan4'
COLOR_DARK_BLUE                = 'dark blue'
COLOR_DARK_CYAN                = 'dark cyan'
COLOR_DARK_GOLDENROD           = 'dark goldenrod'
COLOR_DARK_GOLDENROD1          = 'dark goldenrod1'
COLOR_DARK_GOLDENROD2          = 'dark goldenrod2'
COLOR_DARK_GOLDENROD3          = 'dark goldenrod3'
COLOR_DARK_GRAY                = 'dark gray'
COLOR_DARK_GREEN               = 'dark green'
COLOR_DARK_KHAKI               = 'dark khaki'
COLOR_DARK_MAGENTA             = 'dark magenta'
COLOR_DARK_OLIVE_GREEN         = 'dark olive green'
COLOR_DARK_OLIVE_GREEN1        = 'dark olive green1'
COLOR_DARK_OLIVE_GREEN2        = 'dark olive green2'
COLOR_DARK_OLIVE_GREEN3        = 'dark olive green3'
COLOR_DARK_OLIVE_GREEN4        = 'dark olive green4'
COLOR_DARK_ORANGE              = 'dark orange'
COLOR_DARK_ORANGE1             = 'dark orange1'
COLOR_DARK_ORANGE2             = 'dark orange2'
COLOR_DARK_ORANGE3             = 'dark orange3'
COLOR_DARK_ORANGE4             = 'dark orange4'
COLOR_DARK_ORCHID              = 'dark orchid'
COLOR_DARK_ORCHID1             = 'dark orchid1'
COLOR_DARK_ORCHID2             = 'dark orchid2'
COLOR_DARK_ORCHID3             = 'dark orchid3'
COLOR_DARK_ORCHID4             = 'dark orchid4'
COLOR_DARK_RED                 = 'dark red'
COLOR_DARK_SALMON              = 'dark salmon'
COLOR_DARK_SEA_GREEN           = 'dark sea green'
COLOR_DARK_SEA_GREEN1          = 'dark sea green1'
COLOR_DARK_SEA_GREEN2          = 'dark sea green2'
COLOR_DARK_SEA_GREEN3          = 'dark sea green3'
COLOR_DARK_SEA_GREEN4          = 'dark sea green4'
COLOR_DARK_SLATE_BLUE          = 'dark slate blue'
COLOR_DARK_SLATE_GRAY          = 'dark slate gray'
COLOR_DARK_TURQUOISE           = 'dark turquoise'
COLOR_DARK_VIOLET              = 'dark violet'
COLOR_DEEP_PINK                = 'deep pink'
COLOR_DEEP_PINK4               = 'deep pink4'
COLOR_DEEP_SKY_BLUE            = 'deep sky blue'
COLOR_DEEP_SKY_BLUE1           = 'deep sky blue1'
COLOR_DEEP_SKY_BLUE2           = 'deep sky blue2'
COLOR_DEEP_SKY_BLUE3           = 'deep sky blue3'
COLOR_DEEP_SKY_BLUE4           = 'deep sky blue4'
COLOR_DIM_GRAY                 = 'dim gray'
COLOR_DODGER_BLUE              = 'dodger blue'
COLOR_DODGER_BLUE1             = 'dodger blue1'
COLOR_DODGER_BLUE2             = 'dodger blue2'
COLOR_DODGER_BLUE3             = 'dodger blue3'
COLOR_DODGER_BLUE4             = 'dodger blue4'
COLOR_FIREBRICK                = 'firebrick'
COLOR_FIREBRICK1               = 'firebrick1'
COLOR_FIREBRICK2               = 'firebrick2'
COLOR_FIREBRICK3               = 'firebrick3'
COLOR_FIREBRICK4               = 'firebrick4'
COLOR_FLORAL_WHITE             = 'floral white'
COLOR_FOREST_GREEN             = 'forest green'
COLOR_GAINSBORO                = 'gainsboro'
COLOR_GHOST_WHITE              = 'ghost white'
COLOR_GOLD                     = 'gold'
COLOR_GOLD1                    = 'gold1'
COLOR_GOLD2                    = 'gold2'
COLOR_GOLD3                    = 'gold3'
COLOR_GOLD4                    = 'gold4'
COLOR_GOLDENROD                = 'goldenrod'
COLOR_GOLDENROD1               = 'goldenrod1'
COLOR_GOLDENROD2               = 'goldenrod2'
COLOR_GOLDENROD3               = 'goldenrod3'
COLOR_GOLDENROD4               = 'goldenrod4'
COLOR_GRAY                     = 'gray'
COLOR_GRAY2                    = 'gray2'
COLOR_GRAY3                    = 'gray3'
COLOR_GRAY4                    = 'gray4'
COLOR_GRAY5                    = 'gray5'
COLOR_GRAY6                    = 'gray6'
COLOR_GRAY7                    = 'gray7'
COLOR_GRAY8                    = 'gray8'
COLOR_GRAY9                    = 'gray9'
COLOR_GRAY10                   = 'gray10'
COLOR_GRAY11                   = 'gray11'
COLOR_GRAY12                   = 'gray12'
COLOR_GRAY13                   = 'gray13'
COLOR_GRAY14                   = 'gray14'
COLOR_GRAY15                   = 'gray15'
COLOR_GRAY16                   = 'gray16'
COLOR_GRAY17                   = 'gray17'
COLOR_GRAY18                   = 'gray18'
COLOR_GRAY19                   = 'gray19'
COLOR_GRAY20                   = 'gray20'
COLOR_GRAY21                   = 'gray21'
COLOR_GRAY22                   = 'gray22'
COLOR_GRAY23                   = 'gray23'
COLOR_GRAY24                   = 'gray24'
COLOR_GRAY25                   = 'gray25'
COLOR_GRAY26                   = 'gray26'
COLOR_GRAY36                   = 'gray36'
COLOR_GRAY37                   = 'gray37'
COLOR_GRAY38                   = 'gray38'
COLOR_GRAY39                   = 'gray39'
COLOR_GRAY40                   = 'gray40'
COLOR_GRAY41                   = 'gray41'
COLOR_GRAY42                   = 'gray42'
COLOR_GRAY43                   = 'gray43'
COLOR_GRAY44                   = 'gray44'
COLOR_GRAY45                   = 'gray45'
COLOR_GRAY46                   = 'gray46'
COLOR_GRAY47                   = 'gray47'
COLOR_GRAY48                   = 'gray48'
COLOR_GRAY49                   = 'gray49'
COLOR_GRAY50                   = 'gray50'
COLOR_GRAY51                   = 'gray51'
COLOR_GRAY52                   = 'gray52'
COLOR_GRAY53                   = 'gray53'
COLOR_GRAY54                   = 'gray54'
COLOR_GRAY55                   = 'gray55'
COLOR_GRAY56                   = 'gray56'
COLOR_GRAY57                   = 'gray57'
COLOR_GRAY58                   = 'gray58'
COLOR_GRAY59                   = 'gray59'
COLOR_GRAY60                   = 'gray60'
COLOR_GRAY74                   = 'gray74'
COLOR_GRAY75                   = 'gray75'
COLOR_GRAY76                   = 'gray76'
COLOR_GRAY77                   = 'gray77'
COLOR_GRAY78                   = 'gray78'
COLOR_GRAY79                   = 'gray79'
COLOR_GRAY80                   = 'gray80'
COLOR_GRAY81                   = 'gray81'
COLOR_GRAY82                   = 'gray82'
COLOR_GRAY83                   = 'gray83'
COLOR_GRAY84                   = 'gray84'
COLOR_GRAY85                   = 'gray85'
COLOR_GRAY86                   = 'gray86'
COLOR_GRAY87                   = 'gray87'
COLOR_GRAY88                   = 'gray88'
COLOR_GRAY89                   = 'gray89'
COLOR_GRAY90                   = 'gray90'
COLOR_GRAY91                   = 'gray91'
COLOR_GRAY92                   = 'gray92'
COLOR_GRAY93                   = 'gray93'
COLOR_GRAY94                   = 'gray94'
COLOR_GRAY95                   = 'gray95'
COLOR_GRAY96                   = 'gray96'
COLOR_GRAY97                   = 'gray97'
COLOR_GRAY98                   = 'gray98'
COLOR_GRAY99                   = 'gray99'
COLOR_GRAY100                  = 'gray100'
COLOR_GREEN                    = 'green'
COLOR_GREEN1                   = 'green1'
COLOR_GREEN2                   = 'green2'
COLOR_GREEN3                   = 'green3'
COLOR_GREEN4                   = 'green4'
COLOR_GREEN_YELLOW             = 'green yellow'
COLOR_HONEYDEW                 = 'honeydew'
COLOR_HONEYDEW1                = 'honeydew1'
COLOR_HONEYDEW2                = 'honeydew2'
COLOR_HONEYDEW3                = 'honeydew3'
COLOR_HONEYDEW4                = 'honeydew4'
COLOR_HOT_PINK                 = 'hot pink'
COLOR_HOT_PINK1                = 'hot pink1'
COLOR_HOT_PINK2                = 'hot pink2'
COLOR_HOT_PINK3                = 'hot pink3'
COLOR_HOT_PINK4                = 'hot pink4'
COLOR_INDIAN_RED               = 'indian red'
COLOR_INDIGO                   = 'indigo'
COLOR_IVORY                    = 'ivory'
COLOR_IVORY1                   = 'ivory1'
COLOR_IVORY2                   = 'ivory2'
COLOR_IVORY3                   = 'ivory3'
COLOR_IVORY4                   = 'ivory4'
COLOR_KHAKI                    = 'khaki'
COLOR_KHAKI1                   = 'khaki1'
COLOR_KHAKI2                   = 'khaki2'
COLOR_KHAKI3                   = 'khaki3'
COLOR_KHAKI4                   = 'khaki4'
COLOR_LAVENDER                 = 'lavender'
COLOR_LAVENDER_BLUSH           = 'lavender blush'
COLOR_LAVENDER_BLUSH1          = 'lavender blush1'
COLOR_LAVENDER_BLUSH2          = 'lavender blush2'
COLOR_LAVENDER_BLUSH3          = 'lavender blush3'
COLOR_LAVENDER_BLUSH4          = 'lavender blush4'
COLOR_LAWN_GREEN               = 'lawn green'
COLOR_LEMON_CHIFFON            = 'lemon chiffon'
COLOR_LEMON_CHIFFON1           = 'lemon chiffon1'
COLOR_LEMON_CHIFFON2           = 'lemon chiffon2'
COLOR_LEMON_CHIFFON3           = 'lemon chiffon3'
COLOR_LEMON_CHIFFON4           = 'lemon chiffon4'
COLOR_LIGHT_BLUE               = 'light blue'
COLOR_LIGHT_BLUE1              = 'light blue1'
COLOR_LIGHT_BLUE2              = 'light blue2'
COLOR_LIGHT_BLUE3              = 'light blue3'
COLOR_LIGHT_BLUE4              = 'light blue4'
COLOR_LIGHT_CORAL              = 'light coral'
COLOR_LIGHT_CYAN               = 'light cyan'
COLOR_LIGHT_CYAN1              = 'light cyan1'
COLOR_LIGHT_CYAN2              = 'light cyan2'
COLOR_LIGHT_CYAN3              = 'light cyan3'
COLOR_LIGHT_CYAN4              = 'light cyan4'
COLOR_LIGHT_GOLDENROD          = 'light goldenrod'
COLOR_LIGHT_GOLDENROD1         = 'light goldenrod1'
COLOR_LIGHT_GOLDENROD2         = 'light goldenrod2'
COLOR_LIGHT_GOLDENROD3         = 'light goldenrod3'
COLOR_LIGHT_GOLDENROD4         = 'light goldenrod4'
COLOR_LIGHT_GOLDENROD_YELLOW   = 'light goldenrod yellow'
COLOR_LIGHT_GRAY               = 'light gray'
COLOR_LIGHT_GREEN              = 'light green'
COLOR_LIGHT_PINK               = 'light pink'
COLOR_LIGHT_PINK1              = 'light pink1'
COLOR_LIGHT_PINK2              = 'light pink2'
COLOR_LIGHT_PINK3              = 'light pink3'
COLOR_LIGHT_PINK4              = 'light pink4'
COLOR_LIGHT_SALMON             = 'light salmon'
COLOR_LIGHT_SALMON1            = 'light salmon1'
COLOR_LIGHT_SALMON2            = 'light salmon2'
COLOR_LIGHT_SALMON3            = 'light salmon3'
COLOR_LIGHT_SALMON4            = 'light salmon4'
COLOR_LIGHT_SEA_GREEN          = 'light sea green'
COLOR_LIGHT_SKY_BLUE           = 'light sky blue'
COLOR_LIGHT_SKY_BLUE1          = 'light sky blue1'
COLOR_LIGHT_SKY_BLUE2          = 'light sky blue2'
COLOR_LIGHT_SKY_BLUE3          = 'light sky blue3'
COLOR_LIGHT_SKY_BLUE4          = 'light sky blue4'
COLOR_LIGHT_SLATE_BLUE         = 'light slate blue'
COLOR_LIGHT_SLATE_GRAY         = 'light slate gray'
COLOR_LIGHT_STEEL_BLUE         = 'light steel blue'
COLOR_LIGHT_STEEL_BLUE1        = 'light steel blue1'
COLOR_LIGHT_STEEL_BLUE2        = 'light steel blue2'
COLOR_LIGHT_STEEL_BLUE3        = 'light steel blue3'
COLOR_LIGHT_STEEL_BLUE4        = 'light steel blue4'
COLOR_LIGHT_YELLOW             = 'light yellow'
COLOR_LIGHT_YELLOW1            = 'light yellow1'
COLOR_LIGHT_YELLOW2            = 'light yellow2'
COLOR_LIGHT_YELLOW3            = 'light yellow3'
COLOR_LIGHT_YELLOW4            = 'light yellow4'
COLOR_LIME_GREEN               = 'lime green'
COLOR_LINEN                    = 'linen'
COLOR_MAGENTA                  = 'magenta'
COLOR_MAGENTA1                 = 'magenta1'
COLOR_MAGENTA2                 = 'magenta2'
COLOR_MAGENTA3                 = 'magenta3'
COLOR_MAGENTA4                 = 'magenta4'
COLOR_MAROON                   = 'maroon'
COLOR_MAROON1                  = 'maroon1'
COLOR_MAROON2                  = 'maroon2'
COLOR_MAROON3                  = 'maroon3'
COLOR_MAROON4                  = 'maroon4'
COLOR_MEDIUM_AQUAMARINE        = 'medium aquamarine'
COLOR_MEDIUM_BLUE              = 'medium blue'
COLOR_MEDIUM_FOREST_GREEN      = 'medium forest green'
COLOR_MEDIUM_GOLDENROD         = 'medium goldenrod'
COLOR_MEDIUM_ORCHID            = 'medium orchid'
COLOR_MEDIUM_ORCHID1           = 'medium orchid1'
COLOR_MEDIUM_ORCHID2           = 'medium orchid2'
COLOR_MEDIUM_ORCHID3           = 'medium orchid3'
COLOR_MEDIUM_ORCHID4           = 'medium orchid4'
COLOR_MEDIUM_PURPLE            = 'medium purple'
COLOR_MEDIUM_SEA_GREEN         = 'medium sea green'
COLOR_MEDIUM_SLATE_BLUE        = 'medium slate blue'
COLOR_MEDIUM_SPRING_GREEN      = 'medium spring green'
COLOR_MEDIUM_TURQUOISE         = 'medium turquoise'
COLOR_MEDIUM_VIOLET_RED        = 'medium violet red'
COLOR_MIDNIGHT_BLUE            = 'midnight blue'
COLOR_MINT_CREAM               = 'mint cream'
COLOR_MISTY_ROSE               = 'misty rose'
COLOR_MISTY_ROSE1              = 'misty rose1'
COLOR_MISTY_ROSE2              = 'misty rose2'
COLOR_MISTY_ROSE3              = 'misty rose3'
COLOR_MISTY_ROSE4              = 'misty rose4'
COLOR_MOCCASIN                 = 'moccasin'
COLOR_NAVAJO_WHITE             = 'navajo white'
COLOR_NAVAJO_WHITE1            = 'navajo white1'
COLOR_NAVAJO_WHITE2            = 'navajo white2'
COLOR_NAVAJO_WHITE3            = 'navajo white3'
COLOR_NAVAJO_WHITE4            = 'navajo white4'
COLOR_NAVY                     = 'navy'
COLOR_NAVY_BLUE                = 'navy blue'
COLOR_OLD_LACE                 = 'old lace'
COLOR_OLIVE                    = 'olive'
COLOR_OLIVE_DRAB               = 'olive drab'
COLOR_OLIVE_DRAB1              = 'olive drab1'
COLOR_OLIVE_DRAB2              = 'olive drab2'
COLOR_OLIVE_DRAB3              = 'olive drab3'
COLOR_OLIVE_DRAB4              = 'olive drab4'
COLOR_ORANGE                   = 'orange'
COLOR_ORANGE1                  = 'orange1'
COLOR_ORANGE2                  = 'orange2'
COLOR_ORANGE3                  = 'orange3'
COLOR_ORANGE4                  = 'orange4'
COLOR_ORANGE_RED               = 'orange red'
COLOR_ORANGE_RED1              = 'orange red1'
COLOR_ORANGE_RED2              = 'orange red2'
COLOR_ORCHID                   = 'orchid'
COLOR_ORCHID1                  = 'orchid1'
COLOR_ORCHID2                  = 'orchid2'
COLOR_ORCHID3                  = 'orchid3'
COLOR_ORCHID4                  = 'orchid4'
COLOR_PALE_GOLDENROD           = 'pale goldenrod'
COLOR_PALE_GREEN               = 'pale green'
COLOR_PALE_GREEN1              = 'pale green1'
COLOR_PALE_GREEN2              = 'pale green2'
COLOR_PALE_GREEN3              = 'pale green3'
COLOR_PALE_GREEN4              = 'pale green4'
COLOR_PALE_TURQUOISE           = 'pale turquoise'
COLOR_PALE_TURQUOISE1          = 'pale turquoise1'
COLOR_PALE_TURQUOISE2          = 'pale turquoise2'
COLOR_PALE_TURQUOISE3          = 'pale turquoise3'
COLOR_PALE_TURQUOISE4          = 'pale turquoise4'
COLOR_PALE_VIOLET_RED          = 'pale violet red'
COLOR_PALE_VIOLET_RED1         = 'pale violet red1'
COLOR_PALE_VIOLET_RED2         = 'pale violet red2'
COLOR_PALE_VIOLET_RED3         = 'pale violet red3'
COLOR_PALE_VIOLET_RED4         = 'pale violet red4'
COLOR_PAPAYA_WHIP              = 'papaya whip'
COLOR_PEACH_PUFF               = 'peach puff'
COLOR_PEACH_PUFF1              = 'peach puff1'
COLOR_PEACH_PUFF2              = 'peach puff2'
COLOR_PEACH_PUFF3              = 'peach puff3'
COLOR_PEACH_PUFF4              = 'peach puff4'
COLOR_PERU                     = 'peru'
COLOR_PINK                     = 'pink'
COLOR_PINK1                    = 'pink1'
COLOR_PINK2                    = 'pink2'
COLOR_PINK3                    = 'pink3'
COLOR_PINK4                    = 'pink4'
COLOR_PLUM                     = 'plum'
COLOR_PLUM1                    = 'plum1'
COLOR_PLUM2                    = 'plum2'
COLOR_PLUM3                    = 'plum3'
COLOR_PLUM4                    = 'plum4'
COLOR_POWDER_BLUE              = 'powder blue'
COLOR_PURPLE                   = 'purple'
COLOR_PURPLE1                  = 'purple1'
COLOR_PURPLE2                  = 'purple2'
COLOR_PURPLE3                  = 'purple3'
COLOR_PURPLE4                  = 'purple4'
COLOR_RED                      = 'red'
COLOR_ROSY_BROWN               = 'rosy brown'
COLOR_ROYAL_BLUE               = 'royal blue'
COLOR_ROYAL_BLUE1              = 'royal blue1'
COLOR_ROYAL_BLUE2              = 'royal blue2'
COLOR_ROYAL_BLUE3              = 'royal blue3'
COLOR_ROYAL_BLUE4              = 'royal blue4'
COLOR_SADDLE_BROWN             = 'saddle brown'
COLOR_SALMON                   = 'salmon'
COLOR_SALMON2                  = 'salmon2'
COLOR_SALMON3                  = 'salmon3'
COLOR_SALMON4                  = 'salmon4'
COLOR_SANDY_BROWN              = 'sandy brown'
COLOR_SEA_GREEN                = 'sea green'
COLOR_SEA_GREEN1               = 'sea green1'
COLOR_SEA_GREEN2               = 'sea green2'
COLOR_SEA_GREEN3               = 'sea green3'
COLOR_SEA_GREEN4               = 'sea green4'
COLOR_SEA_SHELL                = 'sea shell'
COLOR_SEA_SHELL1               = 'sea shell1'
COLOR_SEA_SHELL2               = 'sea shell2'
COLOR_SEA_SHELL3               = 'sea shell3'
COLOR_SEA_SHELL4               = 'sea shell4'
COLOR_SIENNA                   = 'sienna'
COLOR_SIENNA2                  = 'sienna2'
COLOR_SIENNA3                  = 'sienna3'
COLOR_SIENNA4                  = 'sienna4'
COLOR_SILVER                   = 'silver'
COLOR_SKY_BLUE                 = 'sky blue'
COLOR_SKY_BLUE1                = 'sky blue1'
COLOR_SKY_BLUE2                = 'sky blue2'
COLOR_SKY_BLUE3                = 'sky blue3'
COLOR_SKY_BLUE4                = 'sky blue4'
COLOR_SLATE_BLUE               = 'slate blue'
COLOR_SLATE_BLUE1              = 'slate blue1'
COLOR_SLATE_BLUE2              = 'slate blue2'
COLOR_SLATE_BLUE3              = 'slate blue3'
COLOR_SLATE_BLUE4              = 'slate blue4'
COLOR_SLATE_GRAY               = 'slate gray'
COLOR_SNOW                     = 'snow'
COLOR_SNOW1                    = 'snow1'
COLOR_SNOW2                    = 'snow2'
COLOR_SNOW3                    = 'snow3'
COLOR_SNOW4                    = 'snow4'
COLOR_SPRING_GREEN             = 'spring green'
COLOR_SPRING_GREEN1            = 'spring green1'
COLOR_SPRING_GREEN2            = 'spring green2'
COLOR_SPRING_GREEN3            = 'spring green3'
COLOR_SPRING_GREEN4            = 'spring green4'
COLOR_STEEL_BLUE               = 'steel blue'
COLOR_STEEL_BLUE1              = 'steel blue1'
COLOR_STEEL_BLUE2              = 'steel blue2'
COLOR_STEEL_BLUE3              = 'steel blue3'
COLOR_STEEL_BLUE4              = 'steel blue4'
COLOR_TAN                      = 'tan'
COLOR_TAN1                     = 'tan1'
COLOR_TAN2                     = 'tan2'
COLOR_TAN3                     = 'tan3'
COLOR_TAN4                     = 'tan4'
COLOR_TEAL                     = 'teal'
COLOR_THISTLE                  = 'thistle'
COLOR_TOMATO                   = 'tomato'
COLOR_TOMATO1                  = 'tomato1'
COLOR_TOMATO2                  = 'tomato2'
COLOR_TOMATO3                  = 'tomato3'
COLOR_TOMATO4                  = 'tomato4'
COLOR_TURQUOISE                = 'turquoise'
COLOR_TURQUOISE1               = 'turquoise1'
COLOR_TURQUOISE2               = 'turquoise2'
COLOR_TURQUOISE3               = 'turquoise3'
COLOR_TURQUOISE4               = 'turquoise4'
COLOR_VIOLET                   = 'violet'
COLOR_VIOLET_RED               = 'violet red'
COLOR_VIOLET_RED1              = 'violet red1'
COLOR_VIOLET_RED2              = 'violet red2'
COLOR_VIOLET_RED3              = 'violet red3'
COLOR_VIOLET_RED4              = 'violet red4'
COLOR_WHEAT                    = 'wheat'
COLOR_WHEAT1                   = 'wheat1'
COLOR_WHEAT2                   = 'wheat2'
COLOR_WHEAT3                   = 'wheat3'
COLOR_WHEAT4                   = 'wheat4'
COLOR_WHITE                    = 'white'
COLOR_WHITE_SMOKE              = 'white smoke'
COLOR_YELLOW                   = 'yellow'
COLOR_YELLOW1                  = 'yellow1'
COLOR_YELLOW2                  = 'yellow2'
COLOR_YELLOW3                  = 'yellow3'
COLOR_YELLOW4                  = 'yellow4'
COLOR_YELLOW_GREEN             = 'yellow green'

#---------------------------------------------------------------------------

# wxPython KeyCodes

WXK_BACK             = 0x00000008
WXK_TAB              = 0x00000009
WXK_RETURN           = 0x0000000D
WXK_ESCAPE           = 0x0000001B
WXK_SPACE            = 0x00000020
WXK_DELETE           = 0x0000007F
WXK_SPECIAL1         = 0x000000C1
WXK_SPECIAL2         = 0x000000C2
WXK_SPECIAL3         = 0x000000C3
WXK_SPECIAL4         = 0x000000C4
WXK_SPECIAL5         = 0x000000C5
WXK_SPECIAL6         = 0x000000C6
WXK_SPECIAL7         = 0x000000C7
WXK_SPECIAL8         = 0x000000C8
WXK_SPECIAL9         = 0x000000C9
WXK_SPECIAL10        = 0x000000CA
WXK_SPECIAL11        = 0x000000CB
WXK_SPECIAL12        = 0x000000CC
WXK_SPECIAL13        = 0x000000CD
WXK_SPECIAL14        = 0x000000CE
WXK_SPECIAL15        = 0x000000CF
WXK_SPECIAL16        = 0x000000D0
WXK_SPECIAL17        = 0x000000D1
WXK_SPECIAL18        = 0x000000D2
WXK_SPECIAL19        = 0x000000D3
WXK_START            = 0x0000012C
WXK_LBUTTON          = 0x0000012D
WXK_RBUTTON          = 0x0000012E
WXK_CANCEL           = 0x0000012F
WXK_MBUTTON          = 0x00000130
WXK_CLEAR            = 0x00000131
WXK_SHIFT            = 0x00000132
WXK_ALT              = 0x00000133
WXK_CONTROL          = 0x00000134
WXK_MENU             = 0x00000135
WXK_PAUSE            = 0x00000136
WXK_CAPITAL          = 0x00000137
WXK_END              = 0x00000138
WXK_HOME             = 0x00000139
WXK_LEFT             = 0x0000013A
WXK_UP               = 0x0000013B
WXK_RIGHT            = 0x0000013C
WXK_DOWN             = 0x0000013D
WXK_SELECT           = 0x0000013E
WXK_PRINT            = 0x0000013F
WXK_EXECUTE          = 0x00000140
WXK_SNAPSHOT         = 0x00000141
WXK_INSERT           = 0x00000142
WXK_HELP             = 0x00000143
WXK_NUMPAD0          = 0x00000144
WXK_NUMPAD1          = 0x00000145
WXK_NUMPAD2          = 0x00000146
WXK_NUMPAD3          = 0x00000147
WXK_NUMPAD4          = 0x00000148
WXK_NUMPAD5          = 0x00000149
WXK_NUMPAD6          = 0x0000014A
WXK_NUMPAD7          = 0x0000014B
WXK_NUMPAD8          = 0x0000014C
WXK_NUMPAD9          = 0x0000014D
WXK_MULTIPLY         = 0x0000014E
WXK_ADD              = 0x0000014F
WXK_SEPARATOR        = 0x00000150
WXK_SUBTRACT         = 0x00000151
WXK_DECIMAL          = 0x00000152
WXK_DIVIDE           = 0x00000153
WXK_F1               = 0x00000154
WXK_F2               = 0x00000155
WXK_F3               = 0x00000156
WXK_F4               = 0x00000157
WXK_F5               = 0x00000158
WXK_F6               = 0x00000159
WXK_F7               = 0x0000015A
WXK_F8               = 0x0000015B
WXK_F9               = 0x0000015C
WXK_F10              = 0x0000015D
WXK_F11              = 0x0000015E
WXK_F12              = 0x0000015F
WXK_F13              = 0x00000160
WXK_F14              = 0x00000161
WXK_F15              = 0x00000162
WXK_F16              = 0x00000163
WXK_F17              = 0x00000164
WXK_F18              = 0x00000165
WXK_F19              = 0x00000166
WXK_F20              = 0x00000167
WXK_F21              = 0x00000168
WXK_F22              = 0x00000169
WXK_F23              = 0x0000016A
WXK_F24              = 0x0000016B
WXK_NUMLOCK          = 0x0000016C
WXK_SCROLL           = 0x0000016D
WXK_PAGEUP           = 0x0000016E
WXK_PAGEDOWN         = 0x0000016F
WXK_NUMPAD_SPACE     = 0x00000170
WXK_NUMPAD_TAB       = 0x00000171
WXK_NUMPAD_ENTER     = 0x00000172
WXK_NUMPAD_F1        = 0x00000173
WXK_NUMPAD_F2        = 0x00000174
WXK_NUMPAD_F3        = 0x00000175
WXK_NUMPAD_F4        = 0x00000176
WXK_NUMPAD_HOME      = 0x00000177
WXK_NUMPAD_LEFT      = 0x00000178
WXK_NUMPAD_UP        = 0x00000179
WXK_NUMPAD_RIGHT     = 0x0000017A
WXK_NUMPAD_DOWN      = 0x0000017B
WXK_NUMPAD_PAGEUP    = 0x0000017C
WXK_NUMPAD_PAGEDOWN  = 0x0000017D
WXK_NUMPAD_END       = 0x0000017E
WXK_NUMPAD_BEGIN     = 0x0000017F
WXK_NUMPAD_INSERT    = 0x00000180
WXK_NUMPAD_DELETE    = 0x00000181
WXK_NUMPAD_EQUAL     = 0x00000182
WXK_NUMPAD_MULTIPLY  = 0x00000183
WXK_NUMPAD_ADD       = 0x00000184
WXK_NUMPAD_SEPARATOR = 0x00000185
WXK_NUMPAD_SUBTRACT  = 0x00000186
WXK_NUMPAD_DECIMAL   = 0x00000187
WXK_NUMPAD_DIVIDE    = 0x00000188
WXK_WINDOWS_LEFT     = 0x00000189
WXK_WINDOWS_RIGHT    = 0x0000018A
WXK_WINDOWS_MENU     = 0x0000018B
WXK_COMMAND          = 0x0000018C

#---------------------------------------------------------------------------

# These are the bit mask constants used in wxKeyEvent

wxMOD_NONE      = 0x0000
wxMOD_ALT       = 0x0001
wxMOD_CONTROL   = 0x0002
wxMOD_ALTGR     = wxMOD_ALT | wxMOD_CONTROL
wxMOD_SHIFT     = 0x0004
wxMOD_META      = 0x0008
wxMOD_WIN       = wxMOD_META
if System == 'Darwin':
    wxMOD_CMD       = wxMOD_META
else:
    wxMOD_CMD       = wxMOD_CONTROL
wxMOD_ALL       = 0xffff

#---------------------------------------------------------------------------
# Emulation-specific (non-wxPython) symbols

# Setup display change rate for normal or debugging operation.
if DEBUG:
    napTimeMilliseconds = 5000 # Non-zero value facilitates debugging
else:
    napTimeMilliseconds = 0  # Zero value optimizes peformance

# TBD - Arbitrary value
caretBlinkMilliseconds = 1000

# Caret Visibility Constants
caretInvisible = 0
caretNormal = 1
caretVeryVisible = 2

# Display (typical VGA) 640 pixels wide x 480 pixels high
SCREEN_WIDTH_PIXELS_DEFAULT = 640
SCREEN_HEIGHT_PIXELS_DEFAULT = 480

# Font (typical character) 8 pixels wide by 12 pixels high
SCREEN_WIDTH_CHARACTERS_DEFAULT = 80
SCREEN_HEIGHT_CHARACTERS_DEFAULT = 40

pixelWidthPerCharacter = SCREEN_WIDTH_PIXELS_DEFAULT // \
                         SCREEN_WIDTH_CHARACTERS_DEFAULT

pixelHeightPerCharacter = SCREEN_HEIGHT_PIXELS_DEFAULT // \
                          SCREEN_HEIGHT_CHARACTERS_DEFAULT

# Assumptions:
#   Screen is typically 80 characters x 25 lines
#   Window is 80 characters x 5 lines (2 for border + 3 for message)
minScreenWidth = 34 * pixelWidthPerCharacter
minScreenHeight = 18 * pixelHeightPerCharacter
minRedirectedHeight = 3 * pixelHeightPerCharacter
RedirectedWindowHeight = {'minDisplay': (minScreenWidth, minScreenHeight),
                          'minHeightPercent': 17,
                          'maxHeightPercent': 20}

#---------------------------------------------------------------------------

ThemeWxPython = {
    'ProductName': ProductName,
    'VendorName': VendorName,
    'SubSystemName': SubSystemName,
    'ThemeName': 'ThemeWxPython',
    'ThemeDate': ThemeDate,

    'Use_256_Color_Pair_Limit': USE_256_COLOR_PAIR_LIMIT,

    'name': 'tsWxPython',

    'BackgroundColour': COLOR_SILVER,
    'ForegroundColour': COLOR_BLACK,

    'CharacterCellAlignment': True, # Supports ScrollBars

    'Dialog': {
        'name': 'Dialog', 
        'ButtonBarDefault': '[?][X]',
        'CloseButtonLabel': '&X\tCtrl-X',
        'HelpButtonLabel': '&?\tCtrl-?',
        'IconizeButtonLabel': '&_\tCtrl-_',
        'MaximizeButtonLabel': '&Z\tCtrl-Z',
        'RestoreDownButtonLabel': '&z\tCtrl-z',
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLACK
        },

    'Frame': {
        'name': 'Frame', 
        'ButtonBarDefault': '[_][Z][X]',
        'CloseButtonLabel': '&X\tCtrl-X',
        'HelpButtonLabel': '&?\tCtrl-?',
        'IconizeButtonLabel': '&_\tCtrl-_',
        'MaximizeButtonLabel': '&Z\tCtrl-Z',
        'RestoreDownButtonLabel': '&z\tCtrl-z',
        'BackgroundColour': COLOR_BLACK,
        'ForegroundColour': COLOR_SILVER
       },

    'Logging': {
        'name': 'Logging', 
        'tsLoggerLevels': {
            'name': 'tsLoggerLevels', 
            'Emergency': EMERGENCY,
            'Critical': CRITICAL,
            'Error': ERROR,
            'Alert': ALERT,
            'Warning': WARNING,
            'Notice': NOTICE,
            'Info': INFO,
            'Debug': DEBUG,
            'NotSet': NOTSET
            },

        'tsLoggerStandardTargets': {
            'name': 'tsLoggerStandardTargets', 
            'StandardOutputFile': '',
            'StandardOutputDevice': 'stdout',
            'StandardErrorDevice': 'stderr',
            'StandardScreenDevice': 'stdscr',
            'SystemLogDevice': 'syslog'
            },

        'wxLogLevels': {
            'name': 'wxLogLevels', 

            # program can't continue, abort immediately
            'LOG_FatalError': CRITICAL,

            # a serious error, user must be informed about it
            'LOG_Error': ERROR,

            # user is normally informed about it
            # but warning may be ignored
            'LOG_Warning': WARNING,

            # normal message (i.e. normal output
            # of a non GUI app)
            'LOG_Message': NOTICE,

            # informational: might go to the status
            # line of GUI app
            'LOG_Status': NOTICE,

            # informational message (a.k.a. 'Verbose')
            'LOG_Info': INFO,

            # never shown to the user, disabled in release mode
            'LOG_Debug': DEBUG,

            # trace messages are also only enabled in debug mode
            'LOG_Trace': DEBUG,

            # used for progress indicator (not yet)
            'LOG_Progress': NOTICE,

            # user defined levels start here
            'LOG_User': NOTICE
            },

        'wxLogStandardTargets': {
            'name': 'wxLogStandardTargets', 
            'wxLogStderr': 'stderr',
            'wxLogStream': 'stdout',
            'wxLogGui': 'stdscr',
            'wxLogWindow': 'window',
            'wxLogNull': 'bitbucket'
            }
        },

    'MenuBar': {
        'name': 'MenuBar', 
        'BackgroundColour': COLOR_SILVER,
        'ForegroundColour': COLOR_BLACK,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'MinScreenDimensions': {
        'name': 'MinScreenDimensions', 
        'FrameWidth': 34 * pixelWidthPerCharacter,
        'FrameHeight': 3 * pixelHeightPerCharacter,
        'MenuBarHeight': 3 * pixelHeightPerCharacter,
        'ToolBarHeight': 3 * pixelHeightPerCharacter,
        'StatusBarHeight': 3 * pixelHeightPerCharacter,
        'RedirectionHeight': 3 * pixelHeightPerCharacter,
        'TaskBarHeight': 3 * pixelHeightPerCharacter},

    'PasswordEntryDialog': {
        'name': 'PasswordEntryDialog', 
        'BackgroundColour': COLOR_SILVER,
        'ForegroundColour': COLOR_BLACK,

        'ButtonSeparatorLine': True,

        'MinSize': (50 * pixelWidthPerCharacter,
                    8 * pixelHeightPerCharacter),

        'Modal': {
            'CursesTextpadTextbox': True # non-event driven
            },

        'StripSpaces': True,

        'TextBoxBackgroundColour': COLOR_SILVER,
        'TextBoxForegroundColour': COLOR_BLACK
        },

    'ReportUtilities': {
        'name': 'ReportUtilities', 
        'pageWidth': pageWidth,
        'pageLength': pageWidth,
        'layout': {'name': 'layout',
                   'TitleWidth': pageWidth - 2,
                   'TitleLeft': 0,
                   'TitleIndent': 8,
                   'TitleCenter': (pageWidth - 2) // 2,
                   'TitlePrefix': ' ',
                   'TitleSuffix': ' ',
                   'spacesPerIndent': 2}},

    'ScrollBar': {
        'name': 'ScrollBar', 
        'ArrowBorder': True, # Establishes box around features
        'ArrowDown': 'v',
        'ArrowLeft': '<',
        'ArrowRight': '>',
        'ArrowUp': '^',
        'DualScrollBarSpacer': True, # Dual ScrollBar Allignment
        'BackgroundColour': COLOR_SILVER,
        'ForegroundColour': COLOR_BLACK,
        'Overlap': True,
        'ThumbHorizontalMin': 20,
        'ThumbVerticalMin': 3,
        'ThumbEmulation': True},

    'SplashScreen': {
        'name': 'SplashScreen', 
        'Copyright': {
            'name': 'Copyright',
            'text': theCopyright,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_WHITE
            },
        'Enabled': True,
        'Image': {
            'name': 'Image', 
            'MakeReusable': True,
            'Path': './logs/bmp/',
            'FileName': 'SplashScreen.bmp'
            },
        'License': {
            'name': 'License',
            'text': theLicense,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_WHITE
            },
        'Notices': {
            'name': 'Notices',
            'text': theNotices,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_WHITE
            },
        'ShowSeconds': 15,
        'Masthead': {
            'name': 'Masthead',
            'text': theMasthead,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_WHITE
            }
        },

    'StandardTerminalEmulators': {
        'name': 'StandardTerminalEmulators',
        'BlackOnWhiteDefault': [
            'linux'],
        'WhiteOnBlackDefault': [
            'ansi',
            'cygwin',
            'vt100',
            'vt220',
            'xterm',
            'xterm-16color',
            'xterm-256color',
            'xterm-88color',
            'xterm-color'],
        'nonColorTerminals': [
            'vt100',
            'vt220'],
        'supportedTermCaps': [
            'cygwin',
            'linux',
            'vt100',
            'vt220',
            'xterm',
            'xterm-color',
            'xterm-16color',
            'xterm-88color',
            'xterm-256color'],
        'unsupportedTermCaps': [
            'ansi']
        },

    'StatusBar': {
        'name': 'StatusBar', 
        'Ellipses': True,
        'Margin': (1 * pixelWidthPerCharacter,
                   1 * pixelHeightPerCharacter),
        'Overlay': True,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'Stdio': {
        'name': 'Stdio', 
                      
        # A White or Black Background for Stdio area focuses
        # the operator more on the application area than on
        # the system information area. An alternative Green
        # Background distracts the operator from the
        # application area.

        # 'StdioBackgroundColour': COLOR_WHITE,  # COLOR_GREEN,
        # 'StdioForegroundColour': COLOR_BLACK,  # COLOR_WHITE,

        'BackgroundColour': COLOR_SILVER, # COLOR_GREEN,
        'ForegroundColour': COLOR_BLACK,  # COLOR_WHITE,

        'Margin': (0 * pixelWidthPerCharacter,
                   0 * pixelHeightPerCharacter),

        # The output message markup is an optional, non-wxWidgets
        # feature that requires the application programmer to
        # prefix seleceted messages with a key words identifying
        # the severity of the condition. The message must also
        # be terminated with a newline ("\n") suffix.
        'Markup': {
            'name': 'Markup', 
            'DEFAULT': {
                'name': 'DEFAULT', 

                # 'Background': COLOR_WHITE,   # Default background
                # 'Foreground': COLOR_BLACK,   # Most visible color

                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color

                'Attributes': [DISPLAY_NORMAL]},

            'DEBUG': {
                'name': 'DEBUG', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'INFO': {
                'name': 'INFO', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'NOTICE': {
                'name': 'NOTICE', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'WARNING': {
                'name': 'WARNING', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]},

            'ALERT': {
                'name': 'ALERT', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'ERROR': {
                'name': 'ERROR', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'CRITICAL': {
                'name': 'CRITICAL', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]},

            'EMERGENCY': {
                'name': 'EMERGENCY', 
                'Background': COLOR_SILVER,  # Default background
                'Foreground': COLOR_BLACK,   # Most visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]}},

        'ScrollableLogFile': True,
        'Timestamp': True,
        'Title': StdioRedirectedTitleStr
        },

    'TaskBar': {
        'name': 'TaskBar', 
        'Enable': True, # Must always be True for name & time display. 

        # An area for the application name, activity indicators (spinning
        # baton, date and time) and buttons that shift focus from one
        # Frame or Dialog to another, thereby moving partially concealed
        # background objects to the fully visible foreground.

    ##                  # A White Background for TaskBar and Stdio focuses
    ##                  # the operator more on the application area than on
    ##                  # the system area.
    ##                  'ActiveFocusBackgroundColour': COLOR_WHITE,
    ##                  'ActiveFocusForegroundColour': COLOR_BLUE,
    ##                  'BackgroundColour': COLOR_WHITE,
    ##                  'ForegroundColour': COLOR_BLACK,
    ##                  'InactiveFocusBackgroundColour': COLOR_WHITE,
    ##                  'InactiveFocusForegroundColour': COLOR_BLACK,

        # The Black Background distinguishes TaskBar from Stdio
        # The colored Buttons then draw operator attention to
        # control features.

        'ActiveFocusBackgroundColour': COLOR_BLACK,
        'ActiveFocusForegroundColour': COLOR_YELLOW,
        'BackgroundColour': COLOR_BLACK,
        'ForegroundColour': COLOR_WHITE,
        'InactiveFocusBackgroundColour': COLOR_BLACK,
        'InactiveFocusForegroundColour': COLOR_CYAN,

        'Title': TaskBarTitleStr,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'TextEditBox': {
        'name': 'TextEditBox', 
        'EventDriven': True
        },

    'TextEntryDialog': {
        'name': 'TextEntryDialog', 
        'BackgroundColour': COLOR_SILVER,
        'ForegroundColour': COLOR_BLACK,

        'ButtonSeparatorLine': True,

        'MinSize': (50 * pixelWidthPerCharacter,
                    8 * pixelHeightPerCharacter),

        'Modal': {
            'name': 'Modal', 
            'CursesTextpadTextbox': False # non-event driven
            },

        'StripSpaces': True,

        'TextBoxBackgroundColour': COLOR_SILVER,
        'TextBoxForegroundColour': COLOR_BLACK
        },

    'Troubleshooting': tsCxGlobals.ThemeToUse['Troubleshooting']

    }

#---------------------------------------------------------------------------

ThemeTeamSTARS = {
    'ProductName': ProductName,
    'SubSystemName': SubSystemName,
    'VendorName': VendorName,
    'ThemeName': 'ThemeTeamSTARS',
    'ThemeDate': ThemeDate,

    'Use_256_Color_Pair_Limit': USE_256_COLOR_PAIR_LIMIT,

    'name': 'ThemeTeamSTARS',

    'BackgroundColour': COLOR_BLUE,
    'ForegroundColour': COLOR_WHITE,

    'CharacterCellAlignment': True, # Supports ScrollBars

    'Dialog': {
        'name': 'Dialog', 
        'ButtonBarDefault': '[?][X]',
        'CloseButtonLabel': '&X\tCtrl-X',
        'HelpButtonLabel': '&?\tCtrl-?',
        'IconizeButtonLabel': '&_\tCtrl-_',
        'MaximizeButtonLabel': '&Z\tCtrl-Z',
        'RestoreDownButtonLabel': '&z\tCtrl-z',
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLUE
        },

    'Frame': {
        'name': 'Frame', 
        'ButtonBarDefault': '[_][Z][X]',
        'CloseButtonLabel': '&X\tCtrl-X',
        'HelpButtonLabel': '&?\tCtrl-?',
        'IconizeButtonLabel': '&_\tCtrl-_',
        'MaximizeButtonLabel': '&Z\tCtrl-Z',
        'RestoreDownButtonLabel': '&z\tCtrl-z',
        'BackgroundColour': COLOR_BLUE,
        'ForegroundColour': COLOR_WHITE
        },

    'Logging': {
        'name': 'Logging', 
        'tsLoggerLevels': {
            'name': 'tsLoggerLevels', 
            'Emergency': EMERGENCY,
            'Critical': CRITICAL,
            'Error': ERROR,
            'Alert': ALERT,
            'Warning': WARNING,
            'Notice': NOTICE,
            'Info': INFO,
            'Debug': DEBUG,
            'NotSet': NOTSET
            },

        'tsLoggerStandardTargets': {
            'name': 'tsLoggerStandardTargets', 
            'StandardOutputFile': '',
            'StandardOutputDevice': 'stdout',
            'StandardErrorDevice': 'stderr',
            'StandardScreenDevice': 'stdscr',
            'SystemLogDevice': 'syslog'
            },

        'wxLogLevels': {
            'name': 'wxLogLevels', 

            # program can't continue, abort immediately
            'LOG_FatalError': CRITICAL,

            # a serious error, user must be informed about it
            'LOG_Error': ERROR,

            # user is normally informed about it
            # but warning may be ignored
            'LOG_Warning': WARNING,

            # normal message (i.e. normal output
            # of a non GUI app)
            'LOG_Message': NOTICE,

            # informational: might go to the status
            # line of GUI app
            'LOG_Status': NOTICE,

            # informational message (a.k.a. 'Verbose')
            'LOG_Info': INFO,

            # never shown to the user, disabled in release mode
            'LOG_Debug': DEBUG,

            # trace messages are also only enabled in debug mode
            'LOG_Trace': DEBUG,

            # used for progress indicator (not yet)
            'LOG_Progress': NOTICE,

            # user defined levels start here
            'LOG_User': NOTICE
            },

        'wxLogStandardTargets': {
            'name': 'wxLogStandardTargets', 
            'wxLogStderr': 'stderr',
            'wxLogStream': 'stdout',
            'wxLogGui': 'stdscr',
            'wxLogWindow': 'window',
            'wxLogNull': 'bitbucket'
            }
        },

    'MenuBar': {
        'name': 'MenuBar', 
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLUE,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'MinScreenDimensions': {
        'name': 'MinScreenDimensions', 
        'FrameWidth': 34 * pixelWidthPerCharacter,
        'FrameHeight': 3 * pixelHeightPerCharacter,
        'MenuBarHeight': 3 * pixelHeightPerCharacter,
        'ToolBarHeight': 3 * pixelHeightPerCharacter,
        'StatusBarHeight': 3 * pixelHeightPerCharacter,
        'RedirectionHeight': 3 * pixelHeightPerCharacter,
        'TaskBarHeight': 3 * pixelHeightPerCharacter},

    'PasswordEntryDialog': {
        'name': 'PasswordEntryDialog', 
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLUE,

        'ButtonSeparatorLine': True,

        'MinSize': (50 * pixelWidthPerCharacter,
                    8 * pixelHeightPerCharacter),

        'Modal': {
            'name': 'Modal', 
            'CursesTextpadTextbox': True # non-event driven
            },

        'StripSpaces': True,

        'TextBoxBackgroundColour': COLOR_YELLOW,
        'TextBoxForegroundColour': COLOR_BLACK
        },

    'ReportUtilities': {
        'name': 'ReportUtilities', 
        'pageWidth': pageWidth,
        'pageLength': pageWidth,
        'layout': {'name': 'layout',
                   'TitleWidth': pageWidth - 2,
                   'TitleLeft': 0,
                   'TitleIndent': 8,
                   'TitleCenter': (pageWidth - 2) // 2,
                   'TitlePrefix': ' ',
                   'TitleSuffix': ' ',
                   'spacesPerIndent': 2}},

    'ScrollBar': {
        'name': 'ScrollBar', 
        'ArrowBorder': True, # Establishes box around features
        'ArrowDown': 'v',
        'ArrowLeft': '<',
        'ArrowRight': '>',
        'ArrowUp': '^',
        'DualScrollBarSpacer': True, # Dual ScrollBar Allignment
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLACK,
        'Overlap': True,
        'ThumbHorizontalMin': 20,
        'ThumbVerticalMin': 3,
        'ThumbEmulation': True},

    'SplashScreen': {
        'name': 'SplashScreen', 
        'Enabled': True,
        'Copyright': {
            'name': 'Copyright',
            'text': theCopyright,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_WHITE
            },
        'Enabled': True,
        'Image': {
            'name': 'Image', 
            'MakeReusable': True,
            'Path': './logs/bmp/',
            'FileName': 'SplashScreen.bmp'
            },
        'License': {
            'name': 'License',
            'text': theLicense,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_YELLOW
            },
        'Notices': {
            'name': 'Notices',
            'text': theNotices,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_YELLOW
            },
        'ShowSeconds': 15,
        'Masthead': {
            'name': 'Masthead',
            'text': theMasthead,
            'BackgroundColour': COLOR_BLACK,
            'ForegroundColour': COLOR_CYAN
            }
        },

    'StandardTerminalEmulators': {
        'name': 'StandardTerminalEmulators',
        'BlackOnWhiteDefault': [
            'linux'],
        'WhiteOnBlackDefault': [
            'ansi',
            'cygwin',
            'vt100',
            'vt220',
            'xterm',
            'xterm-16color',
            'xterm-256color',
            'xterm-88color',
            'xterm-color'],
        'nonColorTerminals': [
            'vt100',
            'vt220'],
        'supportedTermCaps': [
            'cygwin',
            'linux',
            'vt100',
            'vt220',
            'xterm',
            'xterm-color',
            'xterm-16color',
            'xterm-88color',
            'xterm-256color'],
        'unsupportedTermCaps': [
            'ansi']
        },

    'StatusBar': {
        'name': 'StatusBar', 
        'Ellipses': True,
        'Margin': (1 * pixelWidthPerCharacter,
                   1 * pixelHeightPerCharacter),
        'Overlay': True,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'Stdio': {
        'name': 'Stdio', 
              
        # A White or Black Background for Stdio area focuses
        # the operator more on the application area than on
        # the system information area. An alternative Green
        # Background distracts the operator from the
        # application area.

        # 'StdioBackgroundColour': COLOR_WHITE,  # COLOR_GREEN,
        # 'StdioForegroundColour': COLOR_BLACK,  # COLOR_WHITE,

        'BackgroundColour': COLOR_BLACK,  # COLOR_GREEN,
        'ForegroundColour': COLOR_WHITE,  # COLOR_WHITE,

        'Margin': (0 * pixelWidthPerCharacter,
                   0 * pixelHeightPerCharacter),

        # The output message markup is an optional, non-wxWidgets
        # feature that requires the application programmer to
        # prefix seleceted messages with a key words identifying
        # the severity of the condition. The message must also
        # be terminated with a newline ("\n") suffix.
        'Markup': {
            'name': 'Markup', 
            'DEFAULT': {
                'name': 'DEFAULT', 

                # 'Background': COLOR_WHITE,   # Default background
                # 'Foreground': COLOR_BLACK,   # Most visible color

                'Background': COLOR_BLACK,   # Default background
                'Foreground': COLOR_WHITE,   # Most visible color

                'Attributes': [DISPLAY_NORMAL]},

            'DEBUG': {
                'name': 'DEBUG', 
                'Background': COLOR_MAGENTA, # Debug background
                'Foreground': COLOR_WHITE,   # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'INFO': {
                'name': 'INFO', 
                'Background': COLOR_BLUE,     # Comment background
                'Foreground': COLOR_CYAN,     # Lower visible color
                'Attributes': [DISPLAY_NORMAL]},

            'NOTICE': {
                'name': 'NOTICE', 
                'Background': COLOR_BLUE,     # Comment background
                'Foreground': COLOR_WHITE,    # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'WARNING': {
                'name': 'WARNING', 
                'Background': COLOR_BLACK,     # Advice background
                'Foreground': COLOR_YELLOW,    # A visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]},

            'ALERT': {
                'name': 'ALERT', 
                'Background': COLOR_BLACK,     # Advice background
                'Foreground': COLOR_CYAN,      # A visible color
                'Attributes': [DISPLAY_NORMAL]},

            'ERROR': {
                'name': 'ERROR', 
                'Background': COLOR_BLACK,     # Advice background
                'Foreground': COLOR_RED,       # Most visible color
                'Attributes': [DISPLAY_NORMAL]},

            'CRITICAL': {
                'name': 'CRITICAL', 
                'Background': COLOR_BLACK,     # Advice background
                'Foreground': COLOR_YELLOW,    # A visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]},

            'EMERGENCY': {
                'name': 'EMERGENCY', 
                'Background': COLOR_BLACK,     # Advise background
                'Foreground': COLOR_WHITE,     # Most visible color
                'Attributes': [DISPLAY_NORMAL, DISPLAY_BLINK]}},

        'ScrollableLogFile': True,
        'Timestamp': True,
        'Title': StdioRedirectedTitleStr
        },

    'TaskBar': {
        'name': 'TaskBar', 
        'Enable': True, # Must always be True for name & time display. 

        # An area for the application name, activity indicators (spinning
        # baton, date and time) and buttons that shift focus from one
        # Frame or Dialog to another, thereby moving partially concealed
        # background objects to the fully visible foreground.

    ##
    ##                  # A White Background for TaskBar and Stdio focuses
    ##                  # the operator more on the application area than on
    ##                  # the system area.
    ##                  'ActiveFocusBackgroundColour': COLOR_WHITE,
    ##                  'ActiveFocusForegroundColour': COLOR_BLUE,
    ##                  'BackgroundColour': COLOR_WHITE,
    ##                  'ForegroundColour': COLOR_BLACK,
    ##                  'InactiveFocusBackgroundColour': COLOR_WHITE,
    ##                  'InactiveFocusForegroundColour': COLOR_BLACK,

        # The Black Background distinguishes TaskBar from Stdio
        # The colored Buttons then draw operator attention to
        # control features.
        'ActiveFocusBackgroundColour': COLOR_BLACK,
        'ActiveFocusForegroundColour': COLOR_YELLOW,
        'BackgroundColour': COLOR_BLACK,
        'ForegroundColour': COLOR_WHITE,
        'InactiveFocusBackgroundColour': COLOR_BLACK,
        'InactiveFocusForegroundColour': COLOR_CYAN,

        'Title': TaskBarTitleStr,
        'WindowHeight': 3 * pixelHeightPerCharacter
        },

    'TextEditBox': {
        'name': 'TextEditBox', 
        'EventDriven': True
        },

    'TextEntryDialog': {
        'name': 'TextEntryDialog', 
        'BackgroundColour': COLOR_WHITE,
        'ForegroundColour': COLOR_BLUE,

        'ButtonSeparatorLine': True,

        'MinSize': (50 * pixelWidthPerCharacter,
                    8 * pixelHeightPerCharacter),

        'Modal': {
            'name': 'Modal',
            'CursesTextpadTextbox': False # non-event driven
            },

        'StripSpaces': True,

        'TextBoxBackgroundColour': COLOR_YELLOW,
        'TextBoxForegroundColour': COLOR_BLACK
        },

    'Troubleshooting': tsCxGlobals.ThemeToUse['Troubleshooting']

    }

## hemeToUse = ThemeWxPython
ThemeToUse = ThemeTeamSTARS

#--------------------------------------------------------------------------

lastWindowId = None

def nextWindowId():
    '''
    Generate next in sequence of unique IDs upon request of the application
    program. NOTE: This is independent of internal assignedID generation.
    '''
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

#---------------------------------------------------------------------------

def RegisterFirstCallerClassName(theClassInstance, theClassName):
    '''
    Register the first caller class name.
    '''
    theFirstCallerClass = theClassInstance
    try:
        theFirstCallerClass = theClassInstance.theFirstCallerClass
    except AttributeError:
        theClassInstance.theFirstCallerClass = theFirstCallerClass

    theFirstCallerClassName = theClassName
    try:
        theFirstCallerClassName = theClassInstance.theFirstCallerClassName
    except AttributeError:
        theClassInstance.theFirstCallerClassName = theFirstCallerClassName

#---------------------------------------------------------------------------
 
def tsGetClassInstanceFromTuple(theTuple, theClass):
    '''
    Generate the specified class instance from the specified tuple.
    '''
    if isinstance(theTuple, tuple):
        args = []
        for item in theTuple:
            args.append(item)
        theInstance = theClass(*args)
    else:
        theInstance = theTuple

    return (theInstance)

#---------------------------------------------------------------------------
 
def tsMakeIterable(theInput):
    '''
    Generate the specified class instance from the specified tuple.
    '''
    if isinstance(theInput, list) or \
       isinstance(theInput, tuple):
        theIterable = theInput
    else:
        theIterable = [theInput]

    return (theIterable)

#---------------------------------------------------------------------------

def tsCaselessStringCompare(string1, string2):
    '''
    Return True, only if two text strings are identical except for
    upper/lower case. Otherwise, return False.
    '''
    if string1.lower() == string2.lower():
        match = True
    else:
        match = False

    return (match)

#---------------------------------------------------------------------------

def tsGetCharacterValues(pixelCols, pixelRows):
    '''
    Convert pixel measurments (size or position) to their
    equivalent character ones.
    '''
    if pixelRows == DefaultCoord:
        characterRows = pixelRows
    else:
        # Round up to the next whole character
        characterRows = int(float(
            pixelRows + (pixelHeightPerCharacter - 1)) / float(
                pixelHeightPerCharacter))

    if pixelCols == DefaultCoord:
        characterCols = pixelCols
    else:
        # Round up to the next whole character
        characterCols = int(float(
            pixelCols + (pixelWidthPerCharacter - 1)) / float(
                pixelWidthPerCharacter))

    return (characterCols, characterRows)

#---------------------------------------------------------------------------

def tsGetPixelValues(characterCols, characterRows):
    '''
    Convert character measurments (size or position) to their
    equivalent pixel ones.
    '''
    if characterRows == DefaultCoord:
        pixelRows = characterRows
    else:
        pixelRows = int(characterRows * pixelHeightPerCharacter)

    if characterCols == DefaultCoord:
        pixelCols = characterCols
    else:
        pixelCols = int(characterCols * pixelWidthPerCharacter)

    return (pixelCols, pixelRows)

#---------------------------------------------------------------------------

def Max(a, b):
    '''
    Cast both operands to the same type before comparing them to avoid
    warnings about signed/unsigned comparisons from some compilers
    '''
    if ((isinstance(a, float)) or \
        (isinstance(b, float))):

        return (max(float(a), float(b)))

    else:

        return (max(int(a), int(b)))

#---------------------------------------------------------------------------

def Min(a, b):
    '''
    Cast both operands to the same type before comparing them to avoid
    warnings about signed/unsigned comparisons from some compilers
    '''
    if ((isinstance(a, float)) or \
        (isinstance(b, float))):

        return (min(float(a), float(b)))

    else:

        return (min(int(a), int(b)))

#---------------------------------------------------------------------------

if __name__ == '__main__':

    #-------------------------------------------------------------------

    print(__header__)

    #-------------------------------------------------------------------

    myLoggerCLI = Logger.TsLogger(name='',
                                   threshold=Logger.INFO)

    #-------------------------------------------------------------------

    sizex, sizey = tsCxGlobals.get_terminal_size()
    print('\n  width = %d; height = %d' % (sizex, sizey))

    current_os = platform.system()
    print('\n  current_os = %s' % current_os)

    #-------------------------------------------------------------------

    level = 0
    myDictionaryCLI = tsCxGlobals.ThemeToUse
    myConsole = sys.stdout
    tsrpu.displayDictionary(level, myDictionaryCLI, myConsole)

    myFileCLI = open(os.path.join(myLoggerCLI.theLogPath,
                               'tsCxGlobalsDictionaryTest.log'), 'w', 1)

    tsrpu.displayDictionary(level, myDictionaryCLI, myFileCLI)
    myFileCLI.close()

    #-------------------------------------------------------------------

    myLoggerGUI = Logger.TsLogger(name='',
                                  threshold=Logger.INFO)

    #-------------------------------------------------------------------

    level = 0
    myDictionaryGUI = ThemeToUse
    myConsole = sys.stdout
    tsrpu.displayDictionary(level, myDictionaryGUI, myConsole)

    myFileGUI = open(os.path.join(myLoggerGUI.theLogPath,
                                  'tsWxGlobalsDictionaryTest.log'), 'w', 1)

    tsrpu.displayDictionary(level, myDictionaryGUI, myFileGUI)
    myFileGUI.close()
