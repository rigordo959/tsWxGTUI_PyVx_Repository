#! /usr/bin/env python
# "Time-stamp: <07/02/2014  5:18:13 PM rsg>"
'''
tsWxGraphicalTextUserInterface.py - Class uses the Standard
Python Curses API to initialize, manage and shutdown input
(from a keyboard and mouse) and output (to a two-dimensional
display screen).
'''
#################################################################
#
# File: tsWxGraphicalTextUserInterface.py
#
# Purpose:
#
#     Class uses the Standard Python Curses API to initialize,
#     manage and shutdown input (from a keyboard and mouse) and
#     output (to a two-dimensional display screen).
#
# Usage (example):
#
#     ## Import Module
#     import tsWxGraphicalTextUserInterface as tsGTUI
#
#     ## Instantiate Module
#     theScreen = tsGTUI.GraphicalTextUserInterface(theClassName)
#
#     ## Reference Module Methods
#     results = theScreen.runWrapper(mainProgram)
#
# Requirements:
#
#    1. Input Interface
#
#       Required: Computer Keyboard (industry standard mult-button).
#
#       Optional: Computer Mouse (industry standard mult-button).
#
#    2. Output Interface
#
#       Required: Computer Monitor (industry standard 256-color,
#       8-color recommended minimum or monochrome) able to display
#       text characters (80-column by 25-row is recommended minimum
#       format).
#
#       Optional: Font type, font size, screen columns and screen
#       rows are established by manual user actions.
#
# Capabilities:
#
#    1. Identifies user terminal make, model and features.
#
#    2. Controls terminal device startup, shutdown and exception
#       handling.
#
#    3. Translates terminal color, pixel and character parameters.
#
# Limitations:
#
#    1. Assumes that the operator has logged into a computer
#       platform that supports a Python 2.x/3.x Virtual Machine:
#
#    2. Assumes availability of the new or old "curses" programming
#       library on one of the following UNIX-like systems or their
#       equivalent:
#
#       a) Apple Mac OS X (eg. 10.0-10.9 etc.)
#
#       b) Cygwin (eg. 1.6-1.7) running on Microsoft Windows
#          (eg. 8.1/8/7/Vista/XP/2000)
#
#       c) Linux (eg. Fedora, Mandriva, Red Hat, Suse, Ubuntu etc.)
#
#       d) Unix (eg. Darwin, FreeBSD, HP-UX, Solaris etc.)
#
#       The curses/ncurses library's API allows the programmer to write
#       terminal-independent, text-based user interfaces, TUIs. The
#       library's design supports alpha-numeric, punctuation and line-
#       drawing characters. It optimizes screen changes, in order to
#       reduce the latency experienced when using remote shells.
#
#    3. Recommends that the operator configure the terminal (TERM)
#       to one of the following (see tsLibGUI/tsWxPkg/src/tsWxGlobals.py
#       for site-specific options):
#
#       <--- TERM --->  <-------------------- FEATURE ------------------->
#       termcap         keyboard   mouse        color  extended characters
#       --------------  --------  ------  -----------  -------------------
#       xterm-256color  keyboard  option    256-color  extended characters
#       xterm-16color   keyboard  option     16-color  extended characters
#       xterm           keyboard  option      8-color  extended characters
#
#       NOTE: xterm-256color is still under development, as of 2014/01/18.
#
#    4. Optionally allows the operator to configure the terminal (TERM)
#       to one of the following (see tsLibGUI/tsWxPkg/src/tsWxGlobals.py
#       for out-dated site-specific options):
#
#       <--- TERM --->  <-------------------- FEATURE ------------------->
#       termcap         keyboard   mouse        color  extended characters
#       --------------  --------  ------  -----------  -------------------
#       xterm-88color   keyboard  option     88-color  extended characters
#       xterm-color     keyboard  option     16-color  extended characters
#       cygwin          keyboard              8-color  extended characters
#       vt100           keyboard          Black/White  extended characters
#       vt220           keyboard          Black/White  extended characters
#       ansi            keyboard              8-color  extended characters
#
#       NOTE: No ansi terminal emulator creates lines, as of 2014/01/18.
#
#    5. What is the difference between xterm-color & xterm-256color?
#
#       Contrary to the following stackoverflow comments, when
#       tsWxGraphicalTextUserInterface is run on Linux and Microsoft
#       Windows (with the Cygwin plug-in from Red Hat Linux) Python's
#       Curses module reports that xterm-color only has 8-colors which
#       cannot be changed.
#
#       From http://stackoverflow.com/questions/10003136/
#            what-is-the-difference-between-xterm-color-xterm-256color:
#
#       "xterm-256color describes Xterm with support for 256 colors
#       enabled. xterm-color describes an older branch of Xterm that
#       supports sixteen colors. xterm-color is not recommended,
#       since it describes a variant of Xterm that's less functional
#       and that you're not likely to be using. Usually you'll
#       want to use xterm, xterm-16color or xterm-256color.
#
#       In particular, xterm-256color is the default for Terminal
#       starting with Mac OS X 10.7 Lion, with the next-best
#       recommended values being xterm-16color or xterm (which
#       only describes support for eight ANSI colors). Prior to
#       10.7, xterm-color was the default because Terminal
#       didn't support some critical features described by the
#       recommended Xterm terminfo values, e.g., Background Color
#       Erase (BCE), modern codes for switching main/alternate
#       screens, 256 colors.
#
#       Sometimes people explicitly set TERM to xterm-color (as
#       opposed to the recommended Xterm values) to disable
#       functionality or work around incompatibilities between
#       the available terminfo values on a particular computer
#       and the terminal emulator being used.
#
#       Note that technically Terminal should have its own
#       up-to-date terminfo values that describe exactly which
#       features it supports, instead of using the values for
#       Xterm, but:
#
#       1. There isn't one that's up to date currently. nsterm
#          represents Terminal's ancestor from NeXTSTEP. Someone
#          apparently has updated nsterm recently (sometime in the
#          past couple of years), but I don't know whether that
#          has made its way into the ncurses distribution, and it
#          may not be completely up to date with Terminal in 10.7.
#
#       2. A number of programs and shell customization scripts
#          explicitly check whether $TERM starts with (or is equal to)
#          xterm. So some users would still need to know about using
#          the recommended Xterm values with Terminal for compatibility
#          with those.
#
#       If you're not familiar with the terminfo system, take a look
#       at the x-man-page://5/terminfo man page. Also, you can use
#       the infocmp command to view the current terminfo settings or
#       compare two different ones, e.g., infocmp xterm-color
#       xterm-256color will show you all the differences between
#       those two."
#
# Notes:
#
#    The Curses display is H Rows by W Columns. The Top Left corner of the
#    display is located at (Row 0, Column 0). The Bottom Right corner of
#    the display is located at (Row H-1, Column W-1).
#
#    Curses permits, without error, windows to extend beyond the right
#    border. It does not permit, without error, windows to extend beyond
#    the bottom border.
#
#    *** Google Search: NCurses 256 Color Support ***
#    But note that some terminals, while they can support 256 colors,
#    are not able to change the palette. To compile NCurses with 256
#    color support, ...
#        www.c-for-dummies.com/ncurses/256color/
#
#    Python 2.x/3.x uses installation-specific curses which may only
#    support 8 colors.
#
#    For "xterm-color", "xterm-16color", "xterm", "cygwin" and "ansi"
#    compatible displays, "tsWx" maps the 68 standard "wxPython" colors to
#    the 8 standard "curses" colors ('black', 'blue', 'cyan', 'green',
#    'magenta', 'red', 'white', 'yellow').
#
#    For "xterm-88color" and "xterm-256color" compatible displays, "tsWx"
#    supports the 68 standard "wxPython" colors ('aquamarine', 'black',
#    'blue', 'blue violet', 'brown', 'cadet blue', 'coral, 'cornflower blue',
#    'cyan', 'dark gray', 'dark green', 'dark olive green', 'dark orchid',
#    'dark slate blue', 'dark slate gray', 'dark turquoise', 'dim gray',
#    'firebrick', 'forest green', 'gold', 'goldenrod', 'gray', 'green',
#    'green yellow', 'indian red', 'khaki', 'light blue', 'light gray',
#    'light steel blue', 'lime green', 'magenta', 'maroon', 'medium
#    aquamarine', 'medium blue', 'medium forest green', 'medium goldenrod',
#    'medium orchid', 'medium sea green', 'medium slate blue', 'medium
#    spring green', 'medium turquoise', 'medium violet red', 'midnight
#    blue', 'navy', 'orange', 'orange red', 'orchid', 'pale green', 'pink',
#    'plum', 'purple', 'red', 'salmon', 'sea green', 'sienna', 'sky blue',
#    'slate blue', 'spring green', 'steel blue', 'tan', 'thistle',
#    'turquoise', 'violet', 'violet red', 'wheat', 'white', 'yellow',
#    'yellow green').
#
#    For "vt100" and "vt220" compatible monochrome displays, "tsWx" supports
#    'white' on 'black' output for the cygwin console and 'black' on 'white'
#    output for "xterm" consoles.
#
#    NOTE: Support for "vt100", "vt220" and "ansi" consoles depends on
#    availability of the appropriate terminal emulator software.
#
#       1) On Mac OS X, the "Terminal" utility creates a normal vt100
#          display but the "iTerm" application uses the color 'red' instead
#          of bold.
#
#       2) On Mac OS X, the "Terminal" utility creates a almost normal
#          ansi display using "?" for vertical lines and "q" for horizontal
#          lines. However, the "iTerm" application is unable to even
#          create the shapes of the windows.
#
#       3) On Windows, the "Cygwin XWin Server" utility creates a normal
#          display but "Cygwin Bash Shell" utility does not. Each screen
#          refresh overflows the "Redirected Output" window beyond its top
#          border leaving multiple copies of the top two lines visible.
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
#    RE-DESIGN for xterm-256color:
#
#        WEB surfing and experimentation uncovered additional curses
#        features associated with xterm, xterm-16color, xterm-88color
#        and xterm-256color.
#
#        1. The 8 colors associated with xterm (and the out-dated
#           xterm-color) are builtin and cannot be changed by the
#           application.
#
#           This module or the application is responsible for then
#           defining the associated color pairs.
#
#        2. The 16 colors associated with xterm-16color are builtin
#           and cannot be changed by the application. The application,
#           or this module, is responsible for defining the associated
#           color pairs. 
#
#           This module or the application is responsible for then
#           defining the associated color pairs.
#
#        3. The first 16 colors associated with xterm-256color (and
#           the out-dated xterm-88color) are builtin. For compatibility,
#           they should be changed by the application or this module to
#           duplicate xterm-16color.
#
#           Since there are only 32767 of the expected 65536 color
#           pairs available, there can only be 181 colors (including
#           the first 16). The tsWxGraphicalTextUserInterface must
#           define 68 of them in order to fulfill its wxPython Color
#           Set Guarantee.
#
#           This module or the application is responsible for then
#           defining the associated color pairs.
#
#        4. Color Terminal Emulation development status:
#
#              Cygwin with
#              Windows 8.1/8/7/XP  vt100   vt220
#              ------------------  ------  ------
#              has_colors          False   False
#              curses_colors       N/A     N/A
#              curses_color_pairs  N/A     N/A
#              can_change_color    N/A     N/A
#              default palette     N/A     N/A
#              custom palette      N/A     N/A
#
#              Cygwin with                         (outdated)
#              Windows 8.1/8/7/XP  cygwin  xterm   xterm-color
#              ------------------  ------  ------  -----------
#              has_colors          True    True    True
#              curses_colors       8       8       8
#              curses_color_pairs  64(8x8) 64(8x8) 64(8x8)
#              can_change_color    False   False   False
#              default palette     8       8       8
#              custom palette
#
#              Cygwin with                        (outdated)
#              Windows 8.1/8/7/XP  xterm-16color  xterm-88color  xterm-256color
#              ------------------  -------------  -------------  --------------
#              has_colors          True           True           True
#              curses_colors       16             88             256
#              curses_color_pairs  256(16x16)     7744(88x88)    32767(181x181)
#              can_change_color    True           True           True
#              default palette     16             16             16
#              custom palette                                    165
#
#
#              Linux
#              Fedora 20           xterm    xterm-16color  xterm-256color
#              ------------------  ------  -------------  --------------
#              has_colors          True                   True
#              curses_colors       8                      256
#              curses_color_pairs  64(8x8)                256(16x16)
#              can_change_color    False                  True
#              default palette     8                      16
#              custom palette                             TBD(165)
#
#              Linux
#              Scientific 6.4      xterm   xterm-16color  xterm-256color
#              ------------------  ------  -------------  -------------
#              has_colors          True                   True
#              curses_colors       8                      256
#              curses_color_pairs  64(8x8)                256(16x16)
#              can_change_color    False                  True
#              default palette     8                      16
#              custom palette                             TBD(165)
#
#              Linux
#              Ubuntu 12.04        xterm   xterm-16color  xterm-256color
#              ------------------  ------  -------------  -------------
#              has_colors          True                   True
#              curses_colors       8                      256
#              curses_color_pairs  64(8x8)                256(16x16)
#              can_change_color    False                  True
#              default palette     8                      16
#              custom palette                             TBD(165)
#
#              Mac OS X
#              Mavericks 10.9.1    xterm   xterm-16color  xterm-256color
#              ------------------  ------  -------------  --------------
#              has_colors          True    True           True
#              curses_colors       8       16             256
#              curses_color_pairs  64(8x8) 256(16x16)     32767(181x181)
#              can_change_color    False   False          True
#              default palette     8       16             16
#              custom palette                             165(Lines+ERR)
#
#              Unix
#              OpenIndiana 151a8   xterm   xterm-16color  xterm-256color
#              ------------------  ------  -------------  --------------
#              has_colors          True                   True(???)
#              curses_colors       8                      256(???)
#              curses_color_pairs  64(8x8)                256(16x16)(???)
#              can_change_color    False                  True(???)
#              default palette     8                      16(???)
#              custom palette                             TBD(165)(???)
#
#              Unix
#              PC-BSD 9.2          xterm   xterm-16color  xterm-256color
#              ------------------  ------  -------------  --------------
#              has_colors          True                   True(???)
#              curses_colors       8                      256(???)
#              curses_color_pairs  64(8x8)                256(16x16)(???)
#              can_change_color    False                  True(???)
#              default palette     8                      16(???)
#              custom palette                             TBD(165)(???)
#
# Classes:
#
#    1. GraphicalTextUserInterface(object) - A class for defining
#       features of text-based, graphical user interface.
#
#    2. PrivateLogger - A class that should only be needed when
#       this module is itself the main program. It will not be
#       needed when tsApplication establishes a fully funtional
#       logger.
#
# Methods:
#
#    GraphicalTextUserInterface
#    GraphicalTextUserInterface.__init__
#    GraphicalTextUserInterface._cleanupWhenSignalReceived
#    GraphicalTextUserInterface._prog_mode
#    GraphicalTextUserInterface._shell_mode
#    GraphicalTextUserInterface._sigAbrtHandler
#    GraphicalTextUserInterface._sigIntHandler
#    GraphicalTextUserInterface.baudrate
#    GraphicalTextUserInterface.beep
#    GraphicalTextUserInterface.can_change_color
#    GraphicalTextUserInterface.cbreak
#    GraphicalTextUserInterface.color_content
#    GraphicalTextUserInterface.color_pair
#    GraphicalTextUserInterface.curs_set
#    GraphicalTextUserInterface.def_prog_mode
#    GraphicalTextUserInterface.def_shell_mode
#    GraphicalTextUserInterface.delay_output
#    GraphicalTextUserInterface.doupdate
#    GraphicalTextUserInterface.echo
#    GraphicalTextUserInterface.endwin
#    GraphicalTextUserInterface.erasechar
#    GraphicalTextUserInterface.filter
#    GraphicalTextUserInterface.flash
#    GraphicalTextUserInterface.flushinp
#    GraphicalTextUserInterface.getmouse
#    GraphicalTextUserInterface.getsyx
#    GraphicalTextUserInterface.getwin
#    GraphicalTextUserInterface.halfdelay
#    GraphicalTextUserInterface.has_colors
#    GraphicalTextUserInterface.has_ic
#    GraphicalTextUserInterface.has_il
#    GraphicalTextUserInterface.has_key
#    GraphicalTextUserInterface.init_color
#    GraphicalTextUserInterface.init_pair
#    GraphicalTextUserInterface.initscr
#    GraphicalTextUserInterface.isendwin
#    GraphicalTextUserInterface.keyname
#    GraphicalTextUserInterface.killchar
#    GraphicalTextUserInterface.longname
#    GraphicalTextUserInterface.meta
#    GraphicalTextUserInterface.mouseinterval
#    GraphicalTextUserInterface.mousemask
#    GraphicalTextUserInterface.napms
#    GraphicalTextUserInterface.newpad
#    GraphicalTextUserInterface.newwin
#    GraphicalTextUserInterface.nl
#    GraphicalTextUserInterface.nocbreak
#    GraphicalTextUserInterface.noecho
#    GraphicalTextUserInterface.nonl
#    GraphicalTextUserInterface.noqiflush
#    GraphicalTextUserInterface.noraw
#    GraphicalTextUserInterface.pair_content
#    GraphicalTextUserInterface.pair_number
#    GraphicalTextUserInterface.pflush
#    GraphicalTextUserInterface.putp
#    GraphicalTextUserInterface.qiflush
#    GraphicalTextUserInterface.raw
#    GraphicalTextUserInterface.reset_prog_mode
#    GraphicalTextUserInterface.reset_shell_mode
#    GraphicalTextUserInterface.runWrapper
#    GraphicalTextUserInterface.setsyx
#    GraphicalTextUserInterface.setupterm
#    GraphicalTextUserInterface.start
#    GraphicalTextUserInterface.start_color
#    GraphicalTextUserInterface.stop
#    GraphicalTextUserInterface.termattrs
#    GraphicalTextUserInterface.termname
#    GraphicalTextUserInterface.tigetflag
#    GraphicalTextUserInterface.tigetnum
#    GraphicalTextUserInterface.tigetstr
#    GraphicalTextUserInterface.tparm
#    GraphicalTextUserInterface.tsBuildCursesDataBase
#    GraphicalTextUserInterface.tsBuildSplashScreen
#    GraphicalTextUserInterface.tsBuildWindowDataBase
#    GraphicalTextUserInterface.tsCreateColorPairs
#    GraphicalTextUserInterface.tsErrorConsole
#    GraphicalTextUserInterface.tsExitForTerminalNotSupported
#    GraphicalTextUserInterface.tsGetAttributeValueFromColorPair
#    GraphicalTextUserInterface.tsGetBuiltInColorCount
#    GraphicalTextUserInterface.tsGetColorCodes
#    GraphicalTextUserInterface.tsGetColorNames
#    GraphicalTextUserInterface.tsGetColorPairNumber
#    GraphicalTextUserInterface.tsGetColorRGBCodes
#    GraphicalTextUserInterface.tsGetCursesBottomPanel
#    GraphicalTextUserInterface.tsGetCursesColorContent
#    GraphicalTextUserInterface.tsGetCursesColorPair
#    GraphicalTextUserInterface.tsGetCursesDefaultColors
#    GraphicalTextUserInterface.tsGetCursesNewPanel
#    GraphicalTextUserInterface.tsGetCursesPairContent
#    GraphicalTextUserInterface.tsGetCursesTopPanel
#    GraphicalTextUserInterface.tsGetMouseButtonCodes
#    GraphicalTextUserInterface.tsGetSetToUseForColorCodeFromName
#    GraphicalTextUserInterface.tsGetSetToUseForColorNameFromCode
#    GraphicalTextUserInterface.tsGetTopLevelApplication
#    GraphicalTextUserInterface.tsGetWxPythonColorContent
#    GraphicalTextUserInterface.tsInfoConsole
#    GraphicalTextUserInterface.tsInstallDefaultColorDataBase
#    GraphicalTextUserInterface.tsInstallExtendedColorDataBase
#    GraphicalTextUserInterface.tsInstallMonochromeDataBase
#    GraphicalTextUserInterface.tsPrintDataBases
#    GraphicalTextUserInterface.tsPrintWindow
#    GraphicalTextUserInterface.tsSetCursesColorNumber
#    GraphicalTextUserInterface.tsSetCursesColorPair
#    GraphicalTextUserInterface.tsSetCursesCursor
#    GraphicalTextUserInterface.tsSetDefaultClientTerminalDataBase
#    GraphicalTextUserInterface.tsSetDetectedClientTerminalDataBase
#    GraphicalTextUserInterface.tsSetMouseButtonCodes
#    GraphicalTextUserInterface.tsSetTopLevelApplication
#    GraphicalTextUserInterface.tsStripDictionaryName
#    GraphicalTextUserInterface.tsUpdateCursesPanels
#    GraphicalTextUserInterface.typeahead
#    GraphicalTextUserInterface.unctrl
#    GraphicalTextUserInterface.ungetch
#    GraphicalTextUserInterface.ungetmouse
#    GraphicalTextUserInterface.use_default_colors
#    GraphicalTextUserInterface.use_env
#
#    PrivateLogger
#    PrivateLogger.__init__
#    PrivateLogger._log
#    PrivateLogger._output
#    PrivateLogger.alert
#    PrivateLogger.critical
#    PrivateLogger.debug
#    PrivateLogger.emergency
#    PrivateLogger.error
#    PrivateLogger.exception
#    PrivateLogger.info
#    PrivateLogger.log
#    PrivateLogger.notice
#    PrivateLogger.warning
#
# Modifications:
#
#    2010/04/03 rsg Created 68 color definitions (names, codes and
#                   rgb values) for colors "guaranteed to be
#                   recognized by wxPython". Additional definitions
#                   provided for other commonly used colors.
#
#    2010/04/10 rsg Substituted class variables for error prone
#                   class instance and various global variables.
#
#    2010/05/03 rsg Added unit test to successfully demonstrate that
#                   the required wxPython 68 color palette guaranteed
#                   to be available is supported by xterm-256color
#                   terminal or by a mapping into the 8-color palette
#                   of the xterm-color terminal. Also demonstrated
#                   the support for the vt100 monochrome terminal.
#
#    2010/05/25 rsg Revised tsInstallExtendedColorDataBase,
#                   tsInstallDefaultColorDataBase and
#                   tsGetColorPairNumber. Created a packed
#                   sequence of color pair numbers based on the number
#                   of colors instead of a sparse sequence based on
#                   a calculated color field width that supported
#                   the maximum number of curses color pairs.
#
#    2010/06/20 rsg Corrected start so that curses.mousemask(mousemask)
#                   uses the returned tuple (availmask, oldmask).
#
#    2010/07/19 rsg Revised tsInstallExtendedColorDataBase, and
#                   tsGetColorPairNumber. Created and referenced
#                   table of PairNumbersFromColorNumbers and table of
#                   ColorNumbersFromPairNumbers. The tables listed
#                   sequential color pair numbers and associated
#                   foreground and background colors. Should resolve
#                   color mismatch between 68-extended and 8-standard
#                   color sets caused by encoding foreground and
#                   background color numbers into color pair number.
#                   Python uses standard ncurses which only supports
#                   8 colors.
#
#    2010/07/27 rsg Added AcceleratorKeysByEarliestAssignedId to the
#                   Windows data base.
#
#    2010/08/02 rsg Added EventAssociationsByEarliestAssignedId to the
#                   Windows data base.
#
#    2010/08/15 rsg Added import of curses.panel module and associated
#                   functions and methods. Results are but should not
#                   be temporarey. Troubleshooting will be needed.
#
#    2010/08/25 rsg Redesigned tsInstallExtendedColorDataBase. During
#                   experimentation with "init_color.c" example from Dan
#                   Gookin's "Programmer's Guide to nCurses", observed
#                   that ncurses silently rejects changes to any of its
#                   standard 8-color definitions. It also silently
#                   rejects changes to any of the 64 color pair
#                   definitions associated with the standard 8-color
#                   definitions. Observed that color numbers 8 and above
#                   can be defined and that color pair numbers 64 and
#                   above can be defined.
#
#    2011/04/01 rsg Returned wxPoint, wxSize and wxRect instead of
#                   tuples.
#
#    2011/11/23 rsg Modified tsGetColorPairNumber to Convert
#                   input foreground and background arguments
#                   to lower case prior to table lookup,
#                   because the arguments must have the same
#                   case as the table entries.
#
#    2011/12/17 rsg Renamed newpanel to tsGetCursesNewPanel.
#
#    2011/12/22 rsg Added design note from "Writing Programs
#                   with NCURSES" by Eric S. Raymond and Zeyd
#                   M. Ben-Halim.
#
#    2012/01/05 rsg Added previously overlooked DISPLAY_REVERSE.
#
#    2012/01/07 rsg Added PanelLayer to WindowsByShowOrder.
#
#    2012/01/15 rsg Moved ToDo below Modifications section.
#                   Also removed superfluous hyphen between
#                   author initials and description.
#
#    2012/01/19 rsg Modified tsCreateColorPairs to co-locate code
#                   that is applicable only when the terminal has
#                   colors.
#
#    2012/01/19 rsg Modified has_colors to ensure that vt100 and vt220
#                   terminals cannot be reported as having colors.
#
#    2012/01/19 rsg Revised supportedTermCaps to be ['cygwin', 'xterm',
#                   'xterm-color']. Revised unsupportedTermCaps to be
#                   [ansi', 'vt100', 'vt220', 'xterm-256color]. This
#                   notifies the users of terminal problems rather than
#                   aborting for a programming error or producing
#                   corrupted xterm-256color displays because netither
#                   the Python "curses" module nor the host's "ncurses"
#                   library were built with the wide-character option.
#
#    2012/01/20 rsg Added AssignedIdByPanelLayer to WindowsByShowOrder.
#
#    2012/01/25 rsg Added OrderOfShowPanelStack to WindowsByShowOrder.
#
#    2012/03/29 rsg Applied wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK
#                   to ensure that only font style attributes are
#                   passed to curses for non-color displays (such
#                   as vt100 and vt220).
#
#    2012/07/01 rsg Added global variables WindowsByHandle, WindowsByPad
#                   and WindowsByPanelLayer to GraphicalTextUserInterface
#                   class.
#
#    2012/07/19 rsg Added import of tsWxDoubleLinkedList to manage
#                   databse associated with Keyboard Input activity.
#
#    2012/09/21 rsg Expanded list of Key Codes.
#
#    2013/03/01 rsg Added import tsCommandLineInterfaceLibrary.
#
#    2013/03/01 rsg Added import tsLibraries.
#
#    2013/07/16 rsg Replaced conditional references to tsLibraries by
#
#    2013/07/17 rsg Moved color-pair unit test code to:
#                   test_tsWxGraphicalTextUserInterface
#
#    2013/08/28 rsg Corrected the statement of purpose.
#
#    2013/09/17 rsg Added logic to set locale:
#                   import locale
#                   locale.setlocale(locale.LC_ALL, '')
#                   code = locale.getpreferredencoding()#
#
#    2013/09/17 rsg Modified file open logic in tsPrintDataBases. 2to3
#                   conversion failed to automatically replace
#                   unbuffered binary by buffered text mode causing
#                   program exception message about buffer type error:
#
#                   (unbuffered binary: buffer=0)
#                     defaultDBaseFile = open(renamedDBaseFileName,
#                                             defaultDBaseFileMode,
#                                             0)
#
#                   (buffered text: buffer=1)
#                     defaultDBaseFile = open(renamedDBaseFileName,
#                                             defaultDBaseFileMode,
#                                             1)
#
#    2013/10/19 rsg Removed import of and logic associate with
#                   tslatformRunTimeEnvironment because the
#                   method has been incorporated in tsApplication
#                   so that it is applied to both CLI and GUI
#                   applications.
#
#    2013/11/30 rsg Added platform.system() suffix to the bitmap
#                   image filename.
#
#    2013/12/01 rsg Re-engineered splashscreen theme to include
#                   colors.
#
#    2013/12/30 rsg Added tsPreserve255RGB switch.
#
#    2014/01/01 rsg Changed Splash Screen path from src to bmp:
#                  'Path': './tsLibGUI/tsWxPkg/bmp/',
#
#    2014/01/01 rsg Changed Splash Screen extention from img to bmp:
#                  'FileName': 'theSplashScreen.bmp'
#
#    2014/01/02 rsg Re-engineered the xterm-256color support to
#                   recognize the builtin, non-alterable 16-color
#                   system palette and define the extended wxPython
#                   color palette and color pairs.
#
#    2014/01/03 rsg Added support for xterm-16color.
#
#    2014/01/05 rsg Replaced floatingpoint color_content scaling
#                   (cursesMax 10000 <=> rgbMax 255) with integer
#                   arithmetc.
#
#    2014/01/07 rsg Added support for xterm-88color.
#
#    2014/01/13 rsg Replaced references to cursesColor by references
#                   to xterm8Color.
#
#    2014/01/14 rsg Commented out the curses8Color tables and the
#                   Color256 tables because they've been superceded by
#                   the xterm8, xterm16, xterm88 and xterm256 tables.
#
#    2014/01/18 rsg Updated documentation of features, constraints
#                   and design decisions.
#
#    2014/01/26 rsg Modified tsGetColorPairNumber to apply the
#                   colorSubstitutionMap, if and when it is
#                   applicable.
#
#    2014/01/29 rsg Automatically create theSplashScreenPath.
#                   Moved splash screen bit-mapped image directory
#                   into logs folder to facilitate housekeeping.
#
#    2014/01/30 rsg Changed splash screen name. Placed size and
#                   terminal/emulator name within brackets.
#
#    2014/01/30 rsg Added splash screen readme.txt file to
#                   bit-mapped image directory.
#
#    2014/02/02 rsg Modified tsInstallDefaultColorDataBase to
#                   override built-in RGB values with standard
#                   ones in order to ensure that applications
#                   produce the same display for the same named
#                   colors.
#
#    2014/02/04 rsg Restored inadvertantly deleted dictionary
#                   cursesMonochromeNameFromCode.
#
#    2014/05/10 rsg Added try-except to detect and report
#                   errno.EEXISTS which would otherwise
#                   abort startup on Python 3.3-3.4.
#
#    2014/05/11 rsg Resolved compatibility with Python 3.3 and 3.4 by
#                   replacing "import curses." by "from curses import ".
#                   This resulted in the followin:
#
#                   "import curses"
#                   "from curses import ascii"
#                   "from curses import panel"
#                   "from curses import textpad"
#                   "from curses import wrapper"
#
#                   "import _curses"
#
#    2014/05/22 rsg Added pflush method to update the virtual screen
#                   after changes in the panel stack and then update
#                   the display.
#
#    2014/06/04 rsg Troubleshoot why xterm-88color and xterm-256color
#                   create an invalid BuiltinPaletteRGB. Rather than
#                   being a Python bug, it now appears to be the result
#                   of using the wxPython color names instead of the
#                   those extendedColorDataBaseRGB names to which
#                   the wxPython ones are mapped.
#
#    2014/06/07 rsg Added DEBUG_TerminalRunTimeEnvironment and modified
#                   start to disable tsInstallBasicColorDataBase while
#                   enabling tsInstallExtendedColorDataBase for terminal
#                   emulators "cygwin", "xterm", "xterm-color" and
#                   "xterm-16color" to confirm operability of the
#                   tsInstallExtendedColorDataBase design when number
#                   of colors <= 16. Concluded that when number of colors
#                   > 16, Python curses module incorrectly "ors" text
#                   with narrow instead of wide color attribute thereby
#                   corrupting color with text attribute.
#
#    2014/06/11 rsg Modified tsInstallExtendedColorDataBase. Removed
#                   extraneous code. Adopted use of color code instead
#                   color name to facilitate comparison with
#                   tsInstallDefaultColorDataBase. Modified code
#                   performed just like default version for 8 and
#                   16 color therby validating algorithm. Modified
#                   code did NOT resolve issue for 16+ colors. Cannot
#                   determine if issue is with Python 2.73/3.23 or
#                   nCurses on Cygwin,Linux and Mac OS X.
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
#    2014/06/15 rsg Revised xterm16ColorNameFromCode,
#                   xterm88ColorNameFromCode and xterm256ColorNameFromCode
#                   to begin with xterm8ColorNameFromCode and continue with
#                   balance of xterm16ColorNameFromCode based on email from
#                   Thomas E. Dickey dated June 14, 2014. This also ensures
#                   consistancy of display for all xterms.
#
#    2014/07/02 rsg Revised start method to:
#                   1. apply self.can_change_color
#                   2. apply descending order of self.ts_curses_colors.
#
#    2014/07/02 rsg Revised self.tsInstallDefaultColorDataBase method
#                   to apply self.can_change_color by using
#                   built-in colors rather than standard RGB values.
#
# ToDo:
#
#    2010/04/03 rsg Resolve various pylint findings.
#
#    2010/04/03 rsg Troubleshoot shutdown process to restore
#                   pre-start state.
#
#    2010/07/19 rsg Resolve anomalies in xterm-256color
#                   terminal emulators. Unable to verify that
#                   all appropriate color pairs are generated.
#                   The test_tsWxFrame (derived from
#                   test_tsWxPySimpleApp) displays The TaskBar
#                   and Stdio frames in the appropriate black
#                   and green background colors. The test Frame
#                   is displayed with a dark green instead of
#                   a blue background.
#
#                   Unlike the cygwin, xterm or xterm-color,
#                   the xterm-256color emulator often displays
#                   lines streaking across text of various
#                   foreground colors against various other
#                   background colors.
#
#    2010/07/19 rsg Investigate extended support from 8-color
#                   with 64-color pairs on xterm to 256-color
#                   with 256x256-color pairs on xterm-256color
#                   platform. Will need to provide mechanism
#                   16,777216 for application to establish the
#                   subset of color posibilities in the
#                   256-color pallet.
#
#    2010/07/19 rsg Establish usage case for 256-color pallet.
#                   How are extended colors activated, by whom,
#                   when and how does user identify available
#                   colors and pairs.
#
#    2010/07/19 rsg Complete construction, debug and test of
#                   256-color support.
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

__title__     = 'tsWxGraphicalTextUserInterface'
__version__   = '2.30.0'
__date__      = '06/15/2014'
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
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t\t\tfor Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 Free Software ' + \
                '\n\t\t\tFoundation, Inc.' + \
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

import math
import os
import signal
import sys
import time
import types
import platform

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    import tsLogger
    from tsReportUtilities import TsReportUtilities as tsru
    from tsSysCommands import TsSysCommands

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))


#--------------------------------------------------------------------------

try:

    import tsLibGUI

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
    from tsWxGlobals import ThemeToUse as wxThemeToUse
    from tsWxPoint import Point as wxPoint
    from tsWxRect import Rect as wxRect
    from tsWxSize import Size as wxSize

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

hostOS = platform.system().upper()
pythonVersion = 'Python-%s' % str(platform.python_version())

#---------------------------------------------------------------------------

try:

    terminalConfig = wxThemeToUse['StandardTerminalEmulators']

    # 'StandardTerminalEmulators': {
    #     'name': 'StandardTerminalEmulators',
    #     'BlackOnWhiteDefault': [
    #         'xterm-256color',
    #         'xterm-88color',
    #         'xterm-16color',
    #         'xterm-color',
    #         'xterm',
    #         'ansi'],
    #     'WhiteOnBlackDefault': [
    #         'cygwin',
    #         'vt100',
    #         'vt220'],
    #     'nonColorTerminals': [
    #         'vt100', 'vt220'],
    #     'supportedTermCaps': [
    #         'cygwin',
    #         'vt100',
    #         'vt220',
    #         'xterm',
    #         'xterm-color',
    #         'xterm-16color',
    #         'xterm-88color',
    #         'xterm-256color'],
    #     'unsupportedTermCaps': [
    #         'ansi']
    #     },

    BlackOnWhiteDefault = terminalConfig['BlackOnWhiteDefault']
    WhiteOnBlackDefault = terminalConfig['WhiteOnBlackDefault']
    nonColorTerminals   = terminalConfig['nonColorTerminals']
    supportedTermCaps   = terminalConfig['supportedTermCaps']
    unsupportedTermCaps = terminalConfig['unsupportedTermCaps']
    BlackOnWhiteDefault = terminalConfig['BlackOnWhiteDefault']

except Exception, errorCode:

    print('%s: Configuration Error (wx.ThemeToUse); ' % __title__ + \
          'importCode=%s' % str(errorCode))

#---------------------------------------------------------------------------

try:

    splashScreenConfig = wxThemeToUse['SplashScreen']

    ##     'SplashScreen': {
    ##   'name': 'SplashScreen', 
    ##   'Copyright': {
    ##       'name': 'Copyright',
    ##       'text': theCopyright,
    ##       'BackgroundColour': COLOR_BLACK,
    ##       'ForegroundColour': COLOR_WHITE
    ##       },
    ##   'Enabled': True,
    ##   'Image': {
    ##       'name': 'Image',
    ##       'MakeReusable': True,
    ##       'Path': './bmp/',
    ##       'FileName': 'SplashScreen.bmp'
    ##       },
    ##   'License': {
    ##       'name': 'License',
    ##       'text': theLicense,
    ##       'BackgroundColour': COLOR_BLACK,
    ##       'ForegroundColour': COLOR_WHITE
    ##       },
    ##   'Notices': {
    ##       'name': 'Notices',
    ##       'text': theNotices,
    ##       'BackgroundColour': COLOR_BLACK,
    ##       'ForegroundColour': COLOR_WHITE
    ##       },
    ##   'ShowSeconds': 15,
    ##   'Trademark': {
    ##       'name': 'Trademark',
    ##       'text': theTrademark,
    ##       'BackgroundColour': COLOR_BLACK,
    ##       'ForegroundColour': COLOR_WHITE
    ##       }
    ##   },

    theSplashScreenCopyright = splashScreenConfig['Copyright']['text']
    theSplashScreenEnabled = splashScreenConfig['Enabled']
    theSplashScreenFileName = splashScreenConfig['Image']['FileName']
    theSplashScreenImage = splashScreenConfig['Image']
    theSplashScreenLicense = splashScreenConfig['License']['text']
    theSplashScreenMakeReusable = splashScreenConfig['Image']['MakeReusable']
    theSplashScreenNotices = splashScreenConfig['Notices']['text']
    theSplashScreenPath = splashScreenConfig['Image']['Path']
    theSplashScreenShowSeconds = splashScreenConfig['ShowSeconds']
    theSplashScreenTrademark = splashScreenConfig['Trademark']['text']

    theCopyrightBackgroundColour = splashScreenConfig['Copyright'][
        'BackgroundColour']
    thLicenseBackgroundColour = splashScreenConfig['License'][
        'BackgroundColour']
    theNoticesBackgroundColour = splashScreenConfig['Notices'][
        'BackgroundColour']
    theTrademarkBackgroundColour = splashScreenConfig['Trademark'][
        'BackgroundColour']

    theCopyrightForegroundColour = splashScreenConfig['Copyright'][
        'ForegroundColour']
    thLicenseForegroundColour = splashScreenConfig['License'][
        'ForegroundColour']
    theNoticesForegroundColour = splashScreenConfig['Notices'][
        'ForegroundColour']
    theTrademarkForegroundColour = splashScreenConfig['Trademark'][
        'ForegroundColour']

    # 2014/01/29 rsg Automatically create theSplashScreenPath.
    mkdirsHead = theSplashScreenPath
    mkdirsMode = 0777

    enable_tsInstallExtendedColorDataBase = False
    # Usage of enable_tsInstallExtendedColorDataBase
    # in start method is is follows:
    #
    # if self.ts_curses_colors == 8:

    #   if enable_tsInstallExtendedColorDataBase and \
    #      DEBUG_tsInstallExtendedColorDataBase:
    #       self.ts_has_default_colors = False
    #       self.tsInstallExtendedColorDataBase()
    #   else:
    #       # Cannot change color so must presume that
    #       # self.ts_curses_colors == len(
    #       #     xterm8ColorCodeFromName)
    #       self.ts_has_default_colors = True
    #       self.tsInstallDefaultColorDataBase()

    # elif self.ts_curses_colors == 16:

    #   if enable_tsInstallExtendedColorDataBase and \
    #      DEBUG_tsInstallExtendedColorDataBase:
    #       self.ts_has_default_colors = False
    #       self.tsInstallExtendedColorDataBase()
    #   else:
    #       # Cannot change color so must presume that
    #       # self.ts_curses_colors == len(
    #       #     xterm16ColorCodeFromName)
    #       self.ts_has_default_colors = True
    #           self.tsInstallDefaultColorDataBase()

    # elif self.ts_curses_colors == 88:

    #   # Can change the 88 colors.
    #   # Color Codes for standard 16 color set are correct.
    #   self.ts_has_default_colors = False
    #   self.tsInstallExtendedColorDataBase()

    # else:

    #   # Can change the 256 colors.
    #   # Color Codes for standard 16 color set are correct.
    #   # Color Pairs, limited to 32767, produce wrong colors
    #   self.ts_has_default_colors = False
    #   self.tsInstallExtendedColorDataBase()

    readme_bmp_text = '''# File: ".logs/bmp/README_BMP.txt"
# "Time-stamp: <06/13/2014  8:25:14 AM rsg>"

This "bmp" directory contains those Splash Screen(s) generated by:

  "/tsWxGTUI/tsLibGUI/tsWxPkg/src/tsWxGraphicalTextUserInterface.py.

A Splash Screen is displayed during the launch of a GUI-style
application program. It identifies the application`s author(s),
copyright(s) and licence(s) using information defined in:

  "/tsWxGTUI/tsLibGUI/tsWxPkg/src/tsWxGlobals.py"

Splash Screens are named for the display size (in character columns and
rows), terminal/emulator type, and host operating system.

  Examples:

      Non-Color ("wxPython" transformation maps 68-color palette
           into black with one shade of the default color)
                 Default color for displays with only
                   white, orange or green phosphor.
   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[80x15_VT100]-cygwin_nt-6.2.bmp"          (Windows 8)
   "SplashScreen-[80x15_VT220]-cygwin_nt-6.3.bmp"          (Windows 8.1)

          Basic Multi-Color ("wxPython" transformation maps
            68-color palette into 8 or 16 built-in colors)
   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-6.1.bmp"         (Windows 7)
   "SplashScreen-[60x15_XTERM]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[80x25_XTERM]-darwin.bmp"                 (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Fedora 20)
   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Ubuntu 12.04)
   "SplashScreen-[128x50_XTERM]-freebsd.bmp"               (PC-BSD 9.2)
   "SplashScreen-[128x50_XTERM]-sunos.bmp"                 (OpenIndiana 151a8)
   "SplashScreen-[60x15_XTERM-COLOR]-cygwin_nt-6.1.bmp"    (Windows 7)
   "SplashScreen-[80x15_XTERM-16COLOR]-cygwin_nt-6.3.bmp"  (Windows 8.1)

      #########################################################
      # Extended Multi-Color support is NOT available because #
      #  Terminal/Emulator standards only support 16 colors.  #
      #########################################################
           Extended Multi-Color ("wxPython" emulation maps
         68-color palette into 71 of 88 or 140 of 256 colors)
   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[80x15_XTERM-88COLOR]-cygwin_nt-6.3.bmp"  (Windows 8.1)
   "SplashScreen-[80x25_XTERM-88COLOR]-darwin.bmp"         (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM-88COLOR]-linux.bmp"          (Fedora 20)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-6.3.bmp" (Windows 8.1)
   "SplashScreen-[80x25_XTERM-256COLOR]-darwin.bmp"        (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM-256COLOR]-linux.bmp"         (Fedora 20)

A new Splash Screen is built upon the first use of a uniquely sized
command line interface display by those host operating systems that
share this directory.

  NOTE:

    Previous terminal emulator used in a command line interface shell can
    alter the built-in color palette for subsequect terminal emulators.
    Examples:

    1) The final xterm sees no color palette change if the first one is
       xterm followed by xterm-color, vt100 and xterm.

    2) The final xterm sees a dim color palette change if the first one is
       xterm followed by by xterm-16color, vt100 and xterm.

Keeping a copy here avoids spending time to rebuild the same Splash
Screen each time a GUI-style application program is launched.

You may recover disk space by deleting those Splash Screens that
have outlived their usefulness.'''

    try:
        os.makedirs(mkdirsHead, mkdirsMode)

        readme_bmp_file = os.path.join(mkdirsHead, 'README_BMP.txt')
        readme_bmp_mode = 'w'
        readme_bmp_buffering = 1
        sys.stderr.write('INFO: readme_bmp_file=%s\n' % str(readme_bmp_file))
        try:
            readme_bmpID = open(readme_bmp_file,
                                readme_bmp_mode,
                                readme_bmp_buffering)
            for aline in readme_bmp_text.split('\n'):
                bline = aline # .lstrip()
                if bline == '':
                    # sys.stderr.write('JUNK: %s\n' % str(bline))
                    readme_bmpID.write('%s\n' % bline)
                else:
                    # sys.stderr.write('JUNK: %s\n' % str(bline))
                    readme_bmpID.write('%s\n' % bline)
            readme_bmpID.flush()
            readme_bmpID.close()
        except IOError, e:
            sys.stderr.write('WARNING: <%s>' % str(e))

    except Exception, e:
        sys.stderr.write('EXCEPTION: <%s>' % str(e))

except Exception, errorCode:

    print('%s: Configuration Error (wx.ThemeToUse); ' % __title__ + \
          'importCode=%s' % str(errorCode))

#---------------------------------------------------------------------------

### TermCap Categorizations
##BlackOnWhiteDefault = ['xterm-256color',
##                     'xterm-88color',
##                     'xterm-16color',
##                     'xterm-color',
##                     'xterm',
##                     'ansi']

##WhiteOnBlackDefault = ['cygwin', 'vt100', 'vt220']

##nonColorTerminals   = ['vt100', 'vt220']

### High quality support of keyboard, display and optional mouse.
##supportedTermCaps = [
##    'cygwin',
##    'vt100',
##    'vt220',
##    'xterm',
##    'xterm-color',
##    'xterm-16color'
##    ]

### xterm-256color plagued by extraneous lines around reverse video text on:
###     Mac OS X with "X11" ("iterm" & "Terminal") applications.
###     Ubuntu "X11" ("Terminal") applications.
###     Cygwin "X11" ("Terminal") applications.
##unsupportedTermCaps = [
##    'ansi',
##    'xterm-88color',
##    'xterm-256color'
##    ]

#---------------------------------------------------------------------------

try:

    # Connect with Python's non-graphical, character-cell display services.
    import curses
    from curses import ascii
    from curses import panel
    from curses import textpad
    from curses import wrapper
    import _curses
    
except ImportError, theImportError:

    if hostOS == 'WINDOWS':
        # Import is expected to fail on a non-UNIX system such as Windows.
        # Curses features are available on Cygwin, Linux and Mac OS X.
        msg1 = 'Import Error: %s' % str(theImportError)
        msg2 = "To run on %s, use CYGWIN and it's BASH or XTERM shell" % hostOS
        msg3 = "CYGWIN is available at www.cygwin.com"
        msg = '%s.  %s.  %s' % (msg1, msg2, msg3)
        raise tse.UserInterfaceException(
            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)
    else:
        # Import is not expected to fail on UNIX system.
        msg = 'Import Error: %s' % str(theImportError)
        raise tse.UserInterfaceException(
            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

##import tsWxColorDatabase

##import tsWxGlobals as wx # Invalid import because of circular dependency.
import tsCxGlobals as cx

#---------------------------------------------------------------------------

DEBUG_tsInstallExtendedColorDataBase = False # False unless troubleshooting
                                             # xterm-88color/xterm-256color

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

if DEBUG_tsInstallExtendedColorDataBase:

    myLogger = tsLogger.TsLogger(name='',
                                 threshold=tsLogger.INFO) 

    myFile = open(os.path.join(myLogger.theLogPath,
                               'debug_via_tsru.log'), 'w')

    def debug_via_tsru(myIndent=0, myDictionary=None, myConsole=sys.stdout):
        tsru.displayDictionary(0, myDictionary, myFile)

else:

    def debug_via_tsru(myIndent=0, myDictionary='', myConsole=sys.stdout):
        pass

if False:
    theDefaultModuleName = __title__
else:
    theDefaultModuleName = 'tsWxGTUI'
 
defaultLogFileName = '$%s-%s-Log.txt' % (theDefaultModuleName, hostOS)
defaultLogFileMode = 'w+'

##defaultDBaseFileName = '$%s-%s-DBase.txt' % (theDefaultModuleName, hostOS)
defaultDBaseFileName = 'TerminalRunTimeEnvironment.log'
defaultDBaseFileMode = 'w+'

EmptyString = ''

#---------------------------------------------------------------------------

# Automatic placement and dimensioning features
UseDefaultValue = -1
DefaultPosition = (UseDefaultValue, UseDefaultValue)
DefaultSize = (UseDefaultValue, UseDefaultValue)

#---------------------------------------------------------------------------

# Control switch for preserving RGB value at 255
# instead of 1000 (curses.color_content(color_number)).
tsPreserve255RGB = False
cursesColorContentRGB = 1000

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

##KEYBOARD_ENTER = 10
KEYBOARD_TIMEOUT = -1

#---------------------------------------------------------------------------

# Set of key codes that curses guarantees to recognize

##KEY_BREAK            = 0x00000101
##KEY_DOWN             = 0x00000102
##KEY_UP               = 0x00000103
##KEY_LEFT             = 0x00000104
##KEY_RIGHT            = 0x00000105
##KEY_HOME             = 0x00000106
##KEY_BACKSPACE        = 0x00000107
##KEY_F0               = 0x00000108
##KEY_F1               = 0x00000109
##KEY_F2               = 0x0000010A
##KEY_F3               = 0x0000010B
##KEY_F4               = 0x0000010C
##KEY_F5               = 0x0000010D
##KEY_F6               = 0x0000010E
##KEY_F7               = 0x0000010F
##KEY_F8               = 0x00000110
##KEY_F9               = 0x00000111
##KEY_F10              = 0x00000112
##KEY_F11              = 0x00000113
##KEY_F12              = 0x00000114
##KEY_DL               = 0x00000148
##KEY_IL               = 0x00000149
##KEY_DC               = 0x0000014A
##KEY_IC               = 0x0000014B
##KEY_EIC              = 0x0000014C
##KEY_CLEAR            = 0x0000014D
##KEY_EOS              = 0x0000014E
##KEY_EOL              = 0x0000014F
##KEY_SF               = 0x00000150
##KEY_SR               = 0x00000151
##KEY_NPAGE            = 0x00000152
##KEY_PPAGE            = 0x00000153
##KEY_STAB             = 0x00000154
##KEY_CTAB             = 0x00000155
##KEY_CATAB            = 0x00000156
##KEY_ENTER            = 0x00000157
##KEY_SRESET           = 0x00000158
##KEY_RESET            = 0x00000159
##KEY_PRINT            = 0x0000015A
##KEY_LL               = 0x0000015B
##KEY_A1               = 0x0000015C
##KEY_A3               = 0x0000015D
##KEY_B2               = 0x0000015E
##KEY_C1               = 0x0000015F
##KEY_C3               = 0x00000160
##KEY_BTAB             = 0x00000161
##KEY_BEG              = 0x00000162
##KEY_CANCEL           = 0x00000163
##KEY_CLOSE            = 0x00000164
##KEY_COMMAND          = 0x00000165
##KEY_COPY             = 0x00000166
##KEY_CREATE           = 0x00000167
##KEY_END              = 0x00000168
##KEY_EXIT             = 0x00000169
##KEY_FIND             = 0x0000016A
##KEY_HELP             = 0x0000016B
##KEY_MARK             = 0x0000016C
##KEY_MESSAGE          = 0x0000016D
##KEY_MOVE             = 0x0000016E
##KEY_NEXT             = 0x0000016F
##KEY_OPEN             = 0x00000170
##KEY_OPTIONS          = 0x00000171
##KEY_PREVIOUS         = 0x00000172
##KEY_REDO             = 0x00000173
##KEY_REFERENCE        = 0x00000174
##KEY_REFRESH          = 0x00000175
##KEY_REPLACE          = 0x00000176
##KEY_RESTART          = 0x00000177
##KEY_RESUME           = 0x00000178
##KEY_SAVE             = 0x00000179
##KEY_SBEG             = 0x0000017A
##KEY_SCANCEL          = 0x0000017B
##KEY_SCOMMAND         = 0x0000017C
##KEY_SCOPY            = 0x0000017D
##KEY_SCREATE          = 0x0000017E
##KEY_SDC              = 0x0000017F
##KEY_SDL              = 0x00000180
##KEY_SELECT           = 0x00000181
##KEY_SEND             = 0x00000182
##KEY_SEOL             = 0x00000183
##KEY_SEXIT            = 0x00000184
##KEY_SFIND            = 0x00000185
##KEY_SHELP            = 0x00000186
##KEY_SHOME            = 0x00000187
##KEY_SIC              = 0x00000188
##KEY_SLEFT            = 0x00000189
##KEY_SMESSAGE         = 0x0000018A
##KEY_SMOVE            = 0x0000018B
##KEY_SNEXT            = 0x0000018C
##KEY_SOPTIONS         = 0x0000018D
##KEY_SPREVIOUS        = 0x0000018E
##KEY_SPRINT           = 0x0000018F
##KEY_SREDO            = 0x00000190
##KEY_SREPLACE         = 0x00000191
##KEY_SRIGHT           = 0x00000192
##KEY_SRSUME           = 0x00000193
##KEY_SSAVE            = 0x00000194
##KEY_SSUSPEND         = 0x00000195
##KEY_SUNDO            = 0x00000196
##KEY_SUSPEND          = 0x00000197
##KEY_UNDO             = 0x00000198
##KEY_MOUSE            = 0x00000199
##KEY_RESIZE           = 0x0000019A
##KEY_MAX              = 0x000001FF

KeyCodes = {
    'name':                     'Curses Key Codes',
    curses.ascii.NUL:           'NULL CHAR',
    curses.ascii.SOH:           'START OF HEADING',
    curses.ascii.STX:           'START OF TEXT',
    curses.ascii.ETX:           'END OF TEXT',
    curses.ascii.EOT:           'END OF TRANSMISSION',
    curses.ascii.ENQ:           'ENQUIRY',
    curses.ascii.ACK:           'ACKNOWLEDGEMENT',
    curses.ascii.BEL:           'BELL',
    curses.ascii.BS:            'BACK SPACE',
    curses.ascii.TAB:           'HORIZONTAL TAB',
    curses.ascii.LF:            'LINE FEED',
    curses.ascii.VT:            'VERTICAL TAB',
    curses.ascii.FF:            'FORM FEED',
    curses.ascii.CR:            'CARRIAGE RETURN',
    curses.ascii.SO:            'SHIFT OUT / X-ON',
    curses.ascii.SI:            'SHIFT IN / X-OFF',
    curses.ascii.DLE:           'DATA LINE ESCAPE',
    curses.ascii.DC1:           'DEVICE CONTROL 1 (oft. XON)',
    curses.ascii.DC2:           'DEVICE CONTROL 2',
    curses.ascii.DC3:           'DEVICE CONTROL 3 (oft. XOFF)',
    curses.ascii.DC4:           'DEVICE CONTROL 4',
    curses.ascii.NAK:           'NEGATIVE ACKNOWLEDGEMENT',
    curses.ascii.SYN:           'SYNCHRONOUS IDLE',
    curses.ascii.ETB:           'END OF TRANSMIT BLOCK',
    curses.ascii.CAN:           'CANCEL',
    curses.ascii.EM:            'END OF MEDIUM',
    curses.ascii.SUB:           'SUBSTITUTE',
    curses.ascii.ESC:           'ESCAPE',
    curses.ascii.FS:            'FILE SEPARATOR',
    curses.ascii.GS:            'GROUP SEPARATOR',
    curses.ascii.RS:            'RECORD SEPARATOR',
    curses.ascii.US:            'UNIT SEPARATOR',
    curses.ascii.SP:            'SPACE',
    curses.ascii.DEL:           'DELETE',
    curses.KEY_MIN:             'KEY_MIN',
    curses.KEY_BREAK:           'KEY_BREAK',
    curses.KEY_DOWN:            'KEY_DOWN',
    curses.KEY_UP:              'KEY_UP',
    curses.KEY_LEFT:            'KEY_LEFT',
    curses.KEY_RIGHT:           'KEY_RIGHT',
    curses.KEY_HOME:            'KEY_HOME',
    curses.KEY_BACKSPACE:       'KEY_BACKSPACE',
    curses.KEY_F0:              'KEY_F0',
    curses.KEY_F1:              'KEY_F1',
    curses.KEY_F2:              'KEY_F2',
    curses.KEY_F3:              'KEY_F3',
    curses.KEY_F4:              'KEY_F4',
    curses.KEY_F5:              'KEY_F5',
    curses.KEY_F6:              'KEY_F6',
    curses.KEY_F7:              'KEY_F7',
    curses.KEY_F8:              'KEY_F8',
    curses.KEY_F9:              'KEY_F9',
    curses.KEY_F10:             'KEY_F10',
    curses.KEY_F11:             'KEY_F11',
    curses.KEY_F12:             'KEY_F12',
    curses.KEY_DL:              'KEY_DL',
    curses.KEY_IL:              'KEY_IL',
    curses.KEY_DC:              'KEY_DC',
    curses.KEY_IC:              'KEY_IC',
    curses.KEY_EIC:             'KEY_EIC',
    curses.KEY_CLEAR:           'KEY_CLEAR',
    curses.KEY_EOS:             'KEY_EOS',
    curses.KEY_EOL:             'KEY_EOL',
    curses.KEY_SF:              'KEY_SF',
    curses.KEY_SR:              'KEY_SR',
    curses.KEY_NPAGE:           'KEY_NPAGE',
    curses.KEY_PPAGE:           'KEY_PPAGE',
    curses.KEY_STAB:            'KEY_STAB',
    curses.KEY_CTAB:            'KEY_CTAB',
    curses.KEY_CATAB:           'KEY_CATAB',
    curses.KEY_ENTER:           'KEY_ENTER',
    curses.KEY_SRESET:          'KEY_SRESET',
    curses.KEY_RESET:           'KEY_RESET',
    curses.KEY_PRINT:           'KEY_PRINT',
    curses.KEY_LL:              'KEY_LL',
    curses.KEY_A1:              'KEY_A1',
    curses.KEY_A3:              'KEY_A3',
    curses.KEY_B2:              'KEY_B2',
    curses.KEY_C1:              'KEY_C1',
    curses.KEY_C3:              'KEY_C3',
    curses.KEY_BTAB:            'KEY_BTAB',
    curses.KEY_BEG:             'KEY_BEG',
    curses.KEY_CANCEL:          'KEY_CANCEL',
    curses.KEY_CLOSE:           'KEY_CLOSE',
    curses.KEY_COMMAND:         'KEY_COMMAND',
    curses.KEY_COPY:            'KEY_COPY',
    curses.KEY_CREATE:          'KEY_CREATE',
    curses.KEY_END:             'KEY_END',
    curses.KEY_EXIT:            'KEY_EXIT',
    curses.KEY_FIND:            'KEY_FIND',
    curses.KEY_HELP:            'KEY_HELP',
    curses.KEY_MARK:            'KEY_MARK',
    curses.KEY_MESSAGE:         'KEY_MESSAGE',
    curses.KEY_MOVE:            'KEY_MOVE',
    curses.KEY_NEXT:            'KEY_NEXT',
    curses.KEY_OPEN:            'KEY_OPEN',
    curses.KEY_OPTIONS:         'KEY_OPTIONS',
    curses.KEY_PREVIOUS:        'KEY_PREVIOUS',
    curses.KEY_REDO:            'KEY_REDO',
    curses.KEY_REFERENCE:       'KEY_REFERENCE',
    curses.KEY_REFRESH:         'KEY_REFRESH',
    curses.KEY_REPLACE:         'KEY_REPLACE',
    curses.KEY_RESTART:         'KEY_RESTART',
    curses.KEY_RESUME:          'KEY_RESUME',
    curses.KEY_SAVE:            'KEY_SAVE',
    curses.KEY_SBEG:            'KEY_SBEG',
    curses.KEY_SCANCEL:         'KEY_SCANCEL',
    curses.KEY_SCOMMAND:        'KEY_SCOMMAND',
    curses.KEY_SCOPY:           'KEY_SCOPY',
    curses.KEY_SCREATE:         'KEY_SCREATE',
    curses.KEY_SDC:             'KEY_SDC',
    curses.KEY_SDL:             'KEY_SDL',
    curses.KEY_SELECT:          'KEY_SELECT',
    curses.KEY_SEND:            'KEY_SEND',
    curses.KEY_SEOL:            'KEY_SEOL',
    curses.KEY_SEXIT:           'KEY_SEXIT',
    curses.KEY_SFIND:           'KEY_SFIND',
    curses.KEY_SHELP:           'KEY_SHELP',
    curses.KEY_SHOME:           'KEY_SHOME',
    curses.KEY_SIC:             'KEY_SIC',
    curses.KEY_SLEFT:           'KEY_SLEFT',
    curses.KEY_SMESSAGE:        'KEY_SMESSAGE',
    curses.KEY_SMOVE:           'KEY_SMOVE',
    curses.KEY_SNEXT:           'KEY_SNEXT',
    curses.KEY_SOPTIONS:        'KEY_SOPTIONS',
    curses.KEY_SPREVIOUS:       'KEY_SPREVIOUS',
    curses.KEY_SPRINT:          'KEY_SPRINT',
    curses.KEY_SREDO:           'KEY_SREDO',
    curses.KEY_SREPLACE:        'KEY_SREPLACE',
    curses.KEY_SRIGHT:          'KEY_SRIGHT',
    curses.KEY_SRSUME:          'KEY_SRSUME',
    curses.KEY_SSAVE:           'KEY_SSAVE',
    curses.KEY_SSUSPEND:        'KEY_SSUSPEND',
    curses.KEY_SUNDO:           'KEY_SUNDO',
    curses.KEY_SUSPEND:         'KEY_SUSPEND',
    curses.KEY_UNDO:            'KEY_UNDO',
    curses.KEY_MOUSE:           'KEY_MOUSE',
    curses.KEY_RESIZE:          'KEY_RESIZE',
    curses.KEY_MAX:             'KEY_MAX'
    }

#---------------------------------------------------------------------------

# Set of mouse button codes that curses guarantees to recognize
MouseButtonCodes = {
    'name': 'MouseButtonCodes',
    curses.BUTTON1_PRESSED: 'button 1 pressed',
    curses.BUTTON1_RELEASED: 'button 1 released',
    curses.BUTTON1_CLICKED: 'button 1 clicked',
    curses.BUTTON1_DOUBLE_CLICKED: 'button 1 double clicked',
    curses.BUTTON1_TRIPLE_CLICKED: 'button 1 triple clicked',
    curses.BUTTON2_PRESSED: 'button 2 pressed',
    curses.BUTTON2_RELEASED: 'button 2 released',
    curses.BUTTON2_CLICKED: 'button 2 clicked',
    curses.BUTTON2_DOUBLE_CLICKED: 'button 2 double clicked',
    curses.BUTTON2_TRIPLE_CLICKED: 'button 2 triple clicked',
    curses.BUTTON3_PRESSED: 'button 3 pressed',
    curses.BUTTON3_RELEASED: 'button 3 released',
    curses.BUTTON3_CLICKED: 'button 3 clicked',
    curses.BUTTON3_DOUBLE_CLICKED: 'button 3 double clicked',
    curses.BUTTON3_TRIPLE_CLICKED: 'button 3 triple clicked',
    curses.BUTTON4_PRESSED: 'button 4 pressed',
    curses.BUTTON4_RELEASED: 'button 4 released',
    curses.BUTTON4_CLICKED: 'button 4 clicked',
    curses.BUTTON4_DOUBLE_CLICKED: 'button 4 double clicked',
    curses.BUTTON4_TRIPLE_CLICKED: 'button 4 triple clicked',
    curses.BUTTON_SHIFT: 'button shift',
    curses.BUTTON_CTRL: 'button ctrl',
    curses.BUTTON_ALT: 'button alt'
    #
    # These last two codes are commented out because their inclusion
    # preempts identification of the specific mouse and button state
    # changes.
    #
    ## curses.ALL_MOUSE_EVENTS: 'report all button state changes',
    ## curses.REPORT_MOUSE_POSITION: 'report mouse movement',
    }

#---------------------------------------------------------------------------

# Set of video display features that curses guarantees to recognize
DISPLAY_BLINK = curses.A_BLINK
DISPLAY_BOLD = curses.A_BOLD
DISPLAY_DIM = curses.A_DIM
DISPLAY_NORMAL = curses.A_NORMAL
DISPLAY_REVERSE = curses.A_REVERSE
DISPLAY_STANDOUT = curses.A_STANDOUT
DISPLAY_UNDERLINE = curses.A_UNDERLINE

#---------------------------------------------------------------------------

# Set of color identifiers for built-in RGB values. It includes
# only those colors which xterm and xterm-16color guarantee
# to recognize when curses.can_change_colors is False.
##COLOR_RGB_BLACK_BUILTIN8 = 'black builtin8'
##COLOR_RGB_RED_BUILTIN8 = 'red builtin8'
##COLOR_RGB_GREEN_BUILTIN8 = 'green builtin8'
##COLOR_RGB_YELLOW_BUILTIN8 = 'yellow builtin8'
##COLOR_RGB_BLUE_BUILTIN8 = 'blue builtin8 builtin8'
##COLOR_RGB_MAGENTA_BUILTIN8 = 'magenta builtin8'
##COLOR_RGB_CYAN_BUILTIN8 = 'cyan builtin8'
##COLOR_RGB_WHITE_BUILTIN8 = 'white builtin8'
##COLOR_RGB_BLACK_BUILTIN16 = 'black builtin16'
##COLOR_RGB_RED_BUILTIN16 = 'red builtin16'
##COLOR_RGB_GREEN_BUILTIN16 = 'green builtin16'
##COLOR_RGB_YELLOW_BUILTIN16 = 'yellow builtin16'
##COLOR_RGB_BLUE_BUILTIN16 = 'blue builtin16'
##COLOR_RGB_MAGENTA_BUILTIN16 = 'magenta builtin16'
##COLOR_RGB_CYAN_BUILTIN16 = 'cyan builtin16'
##COLOR_RGB_WHITE_BUILTIN16 = 'white builtin16'
##        0:      COLOR_BLACK_BUILTIN8    0       0       0
##        1:      COLOR_RED_BUILTIN8      173     0       0
##        2:      COLOR_GREEN_BUILTIN8    0       173     0
##        3:      COLOR_YELLOW_BUILTIN8   173     173     0
##        4:      COLOR_BLUE_BUILTIN8     0       0       173
##        5:      COLOR_MAGENTA_BUILTIN8  173     0       173
##        6:      COLOR_CYAN_BUILTIN8     0       173     173
##        7:      COLOR_WHITE_BUILTIN8    173     173     173
##        8:      COLOR_BLACK_BUILTIN16   0       0       0
##        9:      COLOR_RED_BUILTIN16     255     0       0
##        10:     COLOR_GREEN16   0       255     0
##        11:     COLOR_YELLOW_BUILTIN16  255     255     0
##        12:     COLOR_BLUE_BUILTIN16    0       0       255
##        13:     COLOR_MAGENTA_BUILTIN16 255     0       255
##        14:     COLOR_CYAN_BUILTIN16    0       255     255
##        15:     COLOR_WHITE_BUILTIN16   255     255     255

#---------------------------------------------------------------------------

# Set of color identifiers for RGB values. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.
COLOR_RGB_ALICE_BLUE               = 'alice blue'
COLOR_RGB_ANTIQUE_WHITE            = 'antique white'
COLOR_RGB_ANTIQUE_WHITE1           = 'antique white1'
COLOR_RGB_ANTIQUE_WHITE2           = 'antique white2'
COLOR_RGB_ANTIQUE_WHITE3           = 'antique white3'
COLOR_RGB_ANTIQUE_WHITE4           = 'antique white4'
COLOR_RGB_AQUAMARINE               = 'aquamarine'
COLOR_RGB_AQUAMARINE1              = 'aquamarine1'
COLOR_RGB_AQUAMARINE2              = 'aquamarine2'
COLOR_RGB_AQUAMARINE3              = 'aquamarine3'
COLOR_RGB_AQUAMARINE4              = 'aquamarine4'
COLOR_RGB_AZURE                    = 'azure'
COLOR_RGB_AZURE1                   = 'azure1'
COLOR_RGB_AZURE2                   = 'azure2'
COLOR_RGB_AZURE3                   = 'azure3'
COLOR_RGB_AZURE4                   = 'azure4'
COLOR_RGB_BEIGE                    = 'beige'
COLOR_RGB_BISQUE                   = 'bisque'
COLOR_RGB_BISQUE1                  = 'bisque1'
COLOR_RGB_BISQUE2                  = 'bisque2'
COLOR_RGB_BISQUE3                  = 'bisque3'
COLOR_RGB_BISQUE4                  = 'bisque4'
COLOR_RGB_BLACK                    = 'black'
COLOR_RGB_BLANCHED_ALMOND          = 'blanched almond'
COLOR_RGB_BLUE                     = 'blue'
COLOR_RGB_BLUE1                    = 'blue1'
COLOR_RGB_BLUE2                    = 'blue2'
COLOR_RGB_BLUE3                    = 'blue3'
COLOR_RGB_BLUE4                    = 'blue4'
COLOR_RGB_BLUE_VIOLET              = 'blue violet'
COLOR_RGB_BROWN                    = 'brown'
COLOR_RGB_BROWN1                   = 'brown1'
COLOR_RGB_BROWN2                   = 'brown2'
COLOR_RGB_BURLYWOOD                = 'burlywood'
COLOR_RGB_BURLYWOOD1               = 'burlywood1'
COLOR_RGB_BURLYWOOD2               = 'burlywood2'
COLOR_RGB_BURLYWOOD3               = 'burlywood3'
COLOR_RGB_BURLYWOOD4               = 'burlywood4'
COLOR_RGB_CADET_BLUE               = 'cadet blue'
COLOR_RGB_CADET_BLUE1              = 'cadet blue1'
COLOR_RGB_CADET_BLUE2              = 'cadet blue2'
COLOR_RGB_CADET_BLUE3              = 'cadet blue3'
COLOR_RGB_CADET_BLUE4              = 'cadet blue4'
COLOR_RGB_CHARTREUSE               = 'chartreuse'
COLOR_RGB_CHARTREUSE1              = 'chartreuse1'
COLOR_RGB_CHARTREUSE2              = 'chartreuse2'
COLOR_RGB_CHARTREUSE3              = 'chartreuse3'
COLOR_RGB_CHARTREUSE4              = 'chartreuse4'
COLOR_RGB_CHOCOLATE                = 'chocolate'
COLOR_RGB_CHOCOLATE1               = 'chocolate1'
COLOR_RGB_CHOCOLATE2               = 'chocolate2'
COLOR_RGB_CHOCOLATE3               = 'chocolate3'
COLOR_RGB_CHOCOLATE4               = 'chocolate4'
COLOR_RGB_CORAL                    = 'coral'
COLOR_RGB_CORAL1                   = 'coral1'
COLOR_RGB_CORAL2                   = 'coral2'
COLOR_RGB_CORAL3                   = 'coral3'
COLOR_RGB_CORAL4                   = 'coral4'
COLOR_RGB_CORNFLOWER_BLUE          = 'cornflower blue'
COLOR_RGB_CORNSILK                 = 'cornsilk'
COLOR_RGB_CORNSILK1                = 'cornsilk1'
COLOR_RGB_CORNSILK2                = 'cornsilk2'
COLOR_RGB_CORNSILK3                = 'cornsilk3'
COLOR_RGB_CORNSILK4                = 'cornsilk4'
COLOR_RGB_CRIMSON                  = 'crimson'
COLOR_RGB_CYAN                     = 'cyan'
COLOR_RGB_CYAN1                    = 'cyan1'
COLOR_RGB_CYAN2                    = 'cyan2'
COLOR_RGB_CYAN3                    = 'cyan3'
COLOR_RGB_CYAN4                    = 'cyan4'
COLOR_RGB_DARK_BLUE                = 'dark blue'
COLOR_RGB_DARK_CYAN                = 'dark cyan'
COLOR_RGB_DARK_GOLDENROD           = 'dark goldenrod'
COLOR_RGB_DARK_GOLDENROD1          = 'dark goldenrod1'
COLOR_RGB_DARK_GOLDENROD2          = 'dark goldenrod2'
COLOR_RGB_DARK_GOLDENROD3          = 'dark goldenrod3'
COLOR_RGB_DARK_GRAY                = 'dark gray'
COLOR_RGB_DARK_GREEN               = 'dark green'
COLOR_RGB_DARK_KHAKI               = 'dark khaki'
COLOR_RGB_DARK_MAGENTA             = 'dark magenta'
COLOR_RGB_DARK_OLIVE_GREEN         = 'dark olive green'
COLOR_RGB_DARK_OLIVE_GREEN1        = 'dark olive green1'
COLOR_RGB_DARK_OLIVE_GREEN2        = 'dark olive green2'
COLOR_RGB_DARK_OLIVE_GREEN3        = 'dark olive green3'
COLOR_RGB_DARK_OLIVE_GREEN4        = 'dark olive green4'
COLOR_RGB_DARK_ORANGE              = 'dark orange'
COLOR_RGB_DARK_ORANGE1             = 'dark orange1'
COLOR_RGB_DARK_ORANGE2             = 'dark orange2'
COLOR_RGB_DARK_ORANGE3             = 'dark orange3'
COLOR_RGB_DARK_ORANGE4             = 'dark orange4'
COLOR_RGB_DARK_ORCHID              = 'dark orchid'
COLOR_RGB_DARK_ORCHID1             = 'dark orchid1'
COLOR_RGB_DARK_ORCHID2             = 'dark orchid2'
COLOR_RGB_DARK_ORCHID3             = 'dark orchid3'
COLOR_RGB_DARK_ORCHID4             = 'dark orchid4'
COLOR_RGB_DARK_RED                 = 'dark red'
COLOR_RGB_DARK_SALMON              = 'dark salmon'
COLOR_RGB_DARK_SEA_GREEN           = 'dark sea green'
COLOR_RGB_DARK_SEA_GREEN1          = 'dark sea green1'
COLOR_RGB_DARK_SEA_GREEN2          = 'dark sea green2'
COLOR_RGB_DARK_SEA_GREEN3          = 'dark sea green3'
COLOR_RGB_DARK_SEA_GREEN4          = 'dark sea green4'
COLOR_RGB_DARK_SLATE_BLUE          = 'dark slate blue'
COLOR_RGB_DARK_SLATE_GRAY          = 'dark slate gray'
COLOR_RGB_DARK_TURQUOISE           = 'dark turquoise'
COLOR_RGB_DARK_VIOLET              = 'dark violet'
COLOR_RGB_DEEP_PINK                = 'deep pink'
COLOR_RGB_DEEP_PINK4               = 'deep pink4'
COLOR_RGB_DEEP_SKY_BLUE            = 'deep sky blue'
COLOR_RGB_DEEP_SKY_BLUE1           = 'deep sky blue1'
COLOR_RGB_DEEP_SKY_BLUE2           = 'deep sky blue2'
COLOR_RGB_DEEP_SKY_BLUE3           = 'deep sky blue3'
COLOR_RGB_DEEP_SKY_BLUE4           = 'deep sky blue4'
COLOR_RGB_DIM_GRAY                 = 'dim gray'
COLOR_RGB_DODGER_BLUE              = 'dodger blue'
COLOR_RGB_DODGER_BLUE1             = 'dodger blue1'
COLOR_RGB_DODGER_BLUE2             = 'dodger blue2'
COLOR_RGB_DODGER_BLUE3             = 'dodger blue3'
COLOR_RGB_DODGER_BLUE4             = 'dodger blue4'
COLOR_RGB_FIREBRICK                = 'firebrick'
COLOR_RGB_FIREBRICK1               = 'firebrick1'
COLOR_RGB_FIREBRICK2               = 'firebrick2'
COLOR_RGB_FIREBRICK3               = 'firebrick3'
COLOR_RGB_FIREBRICK4               = 'firebrick4'
COLOR_RGB_FLORAL_WHITE             = 'floral white'
COLOR_RGB_FOREST_GREEN             = 'forest green'
COLOR_RGB_GAINSBORO                = 'gainsboro'
COLOR_RGB_GHOST_WHITE              = 'ghost white'
COLOR_RGB_GOLD                     = 'gold'
COLOR_RGB_GOLD1                    = 'gold1'
COLOR_RGB_GOLD2                    = 'gold2'
COLOR_RGB_GOLD3                    = 'gold3'
COLOR_RGB_GOLD4                    = 'gold4'
COLOR_RGB_GOLDENROD                = 'goldenrod'
COLOR_RGB_GOLDENROD1               = 'goldenrod1'
COLOR_RGB_GOLDENROD2               = 'goldenrod2'
COLOR_RGB_GOLDENROD3               = 'goldenrod3'
COLOR_RGB_GOLDENROD4               = 'goldenrod4'
COLOR_RGB_GRAY                     = 'gray'
COLOR_RGB_GRAY2                    = 'gray2'
COLOR_RGB_GRAY3                    = 'gray3'
COLOR_RGB_GRAY4                    = 'gray4'
COLOR_RGB_GRAY5                    = 'gray5'
COLOR_RGB_GRAY6                    = 'gray6'
COLOR_RGB_GRAY7                    = 'gray7'
COLOR_RGB_GRAY8                    = 'gray8'
COLOR_RGB_GRAY9                    = 'gray9'
COLOR_RGB_GRAY10                   = 'gray10'
COLOR_RGB_GRAY11                   = 'gray11'
COLOR_RGB_GRAY12                   = 'gray12'
COLOR_RGB_GRAY13                   = 'gray13'
COLOR_RGB_GRAY14                   = 'gray14'
COLOR_RGB_GRAY15                   = 'gray15'
COLOR_RGB_GRAY16                   = 'gray16'
COLOR_RGB_GRAY17                   = 'gray17'
COLOR_RGB_GRAY18                   = 'gray18'
COLOR_RGB_GRAY19                   = 'gray19'
COLOR_RGB_GRAY20                   = 'gray20'
COLOR_RGB_GRAY21                   = 'gray21'
COLOR_RGB_GRAY22                   = 'gray22'
COLOR_RGB_GRAY23                   = 'gray23'
COLOR_RGB_GRAY24                   = 'gray24'
COLOR_RGB_GRAY25                   = 'gray25'
COLOR_RGB_GRAY26                   = 'gray26'
COLOR_RGB_GRAY36                   = 'gray36'
COLOR_RGB_GRAY37                   = 'gray37'
COLOR_RGB_GRAY38                   = 'gray38'
COLOR_RGB_GRAY39                   = 'gray39'
COLOR_RGB_GRAY40                   = 'gray40'
COLOR_RGB_GRAY41                   = 'gray41'
COLOR_RGB_GRAY42                   = 'gray42'
COLOR_RGB_GRAY43                   = 'gray43'
COLOR_RGB_GRAY44                   = 'gray44'
COLOR_RGB_GRAY45                   = 'gray45'
COLOR_RGB_GRAY46                   = 'gray46'
COLOR_RGB_GRAY47                   = 'gray47'
COLOR_RGB_GRAY48                   = 'gray48'
COLOR_RGB_GRAY49                   = 'gray49'
COLOR_RGB_GRAY50                   = 'gray50'
COLOR_RGB_GRAY51                   = 'gray51'
COLOR_RGB_GRAY52                   = 'gray52'
COLOR_RGB_GRAY53                   = 'gray53'
COLOR_RGB_GRAY54                   = 'gray54'
COLOR_RGB_GRAY55                   = 'gray55'
COLOR_RGB_GRAY56                   = 'gray56'
COLOR_RGB_GRAY57                   = 'gray57'
COLOR_RGB_GRAY58                   = 'gray58'
COLOR_RGB_GRAY59                   = 'gray59'
COLOR_RGB_GRAY60                   = 'gray60'
COLOR_RGB_GRAY74                   = 'gray74'
COLOR_RGB_GRAY75                   = 'gray75'
COLOR_RGB_GRAY76                   = 'gray76'
COLOR_RGB_GRAY77                   = 'gray77'
COLOR_RGB_GRAY78                   = 'gray78'
COLOR_RGB_GRAY79                   = 'gray79'
COLOR_RGB_GRAY80                   = 'gray80'
COLOR_RGB_GRAY81                   = 'gray81'
COLOR_RGB_GRAY82                   = 'gray82'
COLOR_RGB_GRAY83                   = 'gray83'
COLOR_RGB_GRAY84                   = 'gray84'
COLOR_RGB_GRAY85                   = 'gray85'
COLOR_RGB_GRAY86                   = 'gray86'
COLOR_RGB_GRAY87                   = 'gray87'
COLOR_RGB_GRAY88                   = 'gray88'
COLOR_RGB_GRAY89                   = 'gray89'
COLOR_RGB_GRAY90                   = 'gray90'
COLOR_RGB_GRAY91                   = 'gray91'
COLOR_RGB_GRAY92                   = 'gray92'
COLOR_RGB_GRAY93                   = 'gray93'
COLOR_RGB_GRAY94                   = 'gray94'
COLOR_RGB_GRAY95                   = 'gray95'
COLOR_RGB_GRAY96                   = 'gray96'
COLOR_RGB_GRAY97                   = 'gray97'
COLOR_RGB_GRAY98                   = 'gray98'
COLOR_RGB_GRAY99                   = 'gray99'
COLOR_RGB_GRAY100                  = 'gray100'
COLOR_RGB_GREEN                    = 'green'
COLOR_RGB_GREEN1                   = 'green1'
COLOR_RGB_GREEN2                   = 'green2'
COLOR_RGB_GREEN3                   = 'green3'
COLOR_RGB_GREEN4                   = 'green4'
COLOR_RGB_GREEN_YELLOW             = 'green yellow'
COLOR_RGB_HONEYDEW                 = 'honeydew'
COLOR_RGB_HONEYDEW1                = 'honeydew1'
COLOR_RGB_HONEYDEW2                = 'honeydew2'
COLOR_RGB_HONEYDEW3                = 'honeydew3'
COLOR_RGB_HONEYDEW4                = 'honeydew4'
COLOR_RGB_HOT_PINK                 = 'hot pink'
COLOR_RGB_HOT_PINK1                = 'hot pink1'
COLOR_RGB_HOT_PINK2                = 'hot pink2'
COLOR_RGB_HOT_PINK3                = 'hot pink3'
COLOR_RGB_HOT_PINK4                = 'hot pink4'
COLOR_RGB_INDIAN_RED               = 'indian red'
COLOR_RGB_INDIGO                   = 'indigo'
COLOR_RGB_IVORY                    = 'ivory'
COLOR_RGB_IVORY1                   = 'ivory1'
COLOR_RGB_IVORY2                   = 'ivory2'
COLOR_RGB_IVORY3                   = 'ivory3'
COLOR_RGB_IVORY4                   = 'ivory4'
COLOR_RGB_KHAKI                    = 'khaki'
COLOR_RGB_KHAKI1                   = 'khaki1'
COLOR_RGB_KHAKI2                   = 'khaki2'
COLOR_RGB_KHAKI3                   = 'khaki3'
COLOR_RGB_KHAKI4                   = 'khaki4'
COLOR_RGB_LAVENDER                 = 'lavender'
COLOR_RGB_LAVENDER_BLUSH           = 'lavender blush'
COLOR_RGB_LAVENDER_BLUSH1          = 'lavender blush1'
COLOR_RGB_LAVENDER_BLUSH2          = 'lavender blush2'
COLOR_RGB_LAVENDER_BLUSH3          = 'lavender blush3'
COLOR_RGB_LAVENDER_BLUSH4          = 'lavender blush4'
COLOR_RGB_LAWN_GREEN               = 'lawn green'
COLOR_RGB_LEMON_CHIFFON            = 'lemon chiffon'
COLOR_RGB_LEMON_CHIFFON1           = 'lemon chiffon1'
COLOR_RGB_LEMON_CHIFFON2           = 'lemon chiffon2'
COLOR_RGB_LEMON_CHIFFON3           = 'lemon chiffon3'
COLOR_RGB_LEMON_CHIFFON4           = 'lemon chiffon4'
COLOR_RGB_LIGHT_BLUE               = 'light blue'
COLOR_RGB_LIGHT_BLUE1              = 'light blue1'
COLOR_RGB_LIGHT_BLUE2              = 'light blue2'
COLOR_RGB_LIGHT_BLUE3              = 'light blue3'
COLOR_RGB_LIGHT_BLUE4              = 'light blue4'
COLOR_RGB_LIGHT_CORAL              = 'light coral'
COLOR_RGB_LIGHT_CYAN               = 'light cyan'
COLOR_RGB_LIGHT_CYAN1              = 'light cyan1'
COLOR_RGB_LIGHT_CYAN2              = 'light cyan2'
COLOR_RGB_LIGHT_CYAN3              = 'light cyan3'
COLOR_RGB_LIGHT_CYAN4              = 'light cyan4'
COLOR_RGB_LIGHT_GOLDENROD          = 'light goldenrod'
COLOR_RGB_LIGHT_GOLDENROD1         = 'light goldenrod1'
COLOR_RGB_LIGHT_GOLDENROD2         = 'light goldenrod2'
COLOR_RGB_LIGHT_GOLDENROD3         = 'light goldenrod3'
COLOR_RGB_LIGHT_GOLDENROD4         = 'light goldenrod4'
COLOR_RGB_LIGHT_GOLDENROD_YELLOW   = 'light goldenrod yellow'
COLOR_RGB_LIGHT_GRAY               = 'light gray'
COLOR_RGB_LIGHT_GREEN              = 'light green'
COLOR_RGB_LIGHT_PINK               = 'light pink'
COLOR_RGB_LIGHT_PINK1              = 'light pink1'
COLOR_RGB_LIGHT_PINK2              = 'light pink2'
COLOR_RGB_LIGHT_PINK3              = 'light pink3'
COLOR_RGB_LIGHT_PINK4              = 'light pink4'
COLOR_RGB_LIGHT_SALMON             = 'light salmon'
COLOR_RGB_LIGHT_SALMON1            = 'light salmon1'
COLOR_RGB_LIGHT_SALMON2            = 'light salmon2'
COLOR_RGB_LIGHT_SALMON3            = 'light salmon3'
COLOR_RGB_LIGHT_SALMON4            = 'light salmon4'
COLOR_RGB_LIGHT_SEA_GREEN          = 'light sea green'
COLOR_RGB_LIGHT_SKY_BLUE           = 'light sky blue'
COLOR_RGB_LIGHT_SKY_BLUE1          = 'light sky blue1'
COLOR_RGB_LIGHT_SKY_BLUE2          = 'light sky blue2'
COLOR_RGB_LIGHT_SKY_BLUE3          = 'light sky blue3'
COLOR_RGB_LIGHT_SKY_BLUE4          = 'light sky blue4'
COLOR_RGB_LIGHT_SLATE_BLUE         = 'light slate blue'
COLOR_RGB_LIGHT_SLATE_GRAY         = 'light slate gray'
COLOR_RGB_LIGHT_STEEL_BLUE         = 'light steel blue'
COLOR_RGB_LIGHT_STEEL_BLUE1        = 'light steel blue1'
COLOR_RGB_LIGHT_STEEL_BLUE2        = 'light steel blue2'
COLOR_RGB_LIGHT_STEEL_BLUE3        = 'light steel blue3'
COLOR_RGB_LIGHT_STEEL_BLUE4        = 'light steel blue4'
COLOR_RGB_LIGHT_YELLOW             = 'light yellow'
COLOR_RGB_LIGHT_YELLOW1            = 'light yellow1'
COLOR_RGB_LIGHT_YELLOW2            = 'light yellow2'
COLOR_RGB_LIGHT_YELLOW3            = 'light yellow3'
COLOR_RGB_LIGHT_YELLOW4            = 'light yellow4'
COLOR_RGB_LIME_GREEN               = 'lime green'
COLOR_RGB_LINEN                    = 'linen'
COLOR_RGB_MAGENTA                  = 'magenta'
COLOR_RGB_MAGENTA1                 = 'magenta1'
COLOR_RGB_MAGENTA2                 = 'magenta2'
COLOR_RGB_MAGENTA3                 = 'magenta3'
COLOR_RGB_MAGENTA4                 = 'magenta4'
COLOR_RGB_MAROON                   = 'maroon'
COLOR_RGB_MAROON1                  = 'maroon1'
COLOR_RGB_MAROON2                  = 'maroon2'
COLOR_RGB_MAROON3                  = 'maroon3'
COLOR_RGB_MAROON4                  = 'maroon4'
COLOR_RGB_MEDIUM_AQUAMARINE        = 'medium aquamarine'
COLOR_RGB_MEDIUM_BLUE              = 'medium blue'
COLOR_RGB_MEDIUM_FOREST_GREEN      = 'medium forest green'
COLOR_RGB_MEDIUM_GOLDENROD         = 'medium goldenrod'
COLOR_RGB_MEDIUM_ORCHID            = 'medium orchid'
COLOR_RGB_MEDIUM_ORCHID1           = 'medium orchid1'
COLOR_RGB_MEDIUM_ORCHID2           = 'medium orchid2'
COLOR_RGB_MEDIUM_ORCHID3           = 'medium orchid3'
COLOR_RGB_MEDIUM_ORCHID4           = 'medium orchid4'
COLOR_RGB_MEDIUM_PURPLE            = 'medium purple'
COLOR_RGB_MEDIUM_SEA_GREEN         = 'medium sea green'
COLOR_RGB_MEDIUM_SLATE_BLUE        = 'medium slate blue'
COLOR_RGB_MEDIUM_SPRING_GREEN      = 'medium spring green'
COLOR_RGB_MEDIUM_TURQUOISE         = 'medium turquoise'
COLOR_RGB_MEDIUM_VIOLET_RED        = 'medium violet red'
COLOR_RGB_MIDNIGHT_BLUE            = 'midnight blue'
COLOR_RGB_MINT_CREAM               = 'mint cream'
COLOR_RGB_MISTY_ROSE               = 'misty rose'
COLOR_RGB_MISTY_ROSE1              = 'misty rose1'
COLOR_RGB_MISTY_ROSE2              = 'misty rose2'
COLOR_RGB_MISTY_ROSE3              = 'misty rose3'
COLOR_RGB_MISTY_ROSE4              = 'misty rose4'
COLOR_RGB_MOCCASIN                 = 'moccasin'
COLOR_RGB_NAVAJO_WHITE             = 'navajo white'
COLOR_RGB_NAVAJO_WHITE1            = 'navajo white1'
COLOR_RGB_NAVAJO_WHITE2            = 'navajo white2'
COLOR_RGB_NAVAJO_WHITE3            = 'navajo white3'
COLOR_RGB_NAVAJO_WHITE4            = 'navajo white4'
COLOR_RGB_NAVY                     = 'navy'
COLOR_RGB_NAVY_BLUE                = 'navy blue'
COLOR_RGB_OLD_LACE                 = 'old lace'
COLOR_RGB_OLIVE                    = 'olive'
COLOR_RGB_OLIVE_DRAB               = 'olive drab'
COLOR_RGB_OLIVE_DRAB1              = 'olive drab1'
COLOR_RGB_OLIVE_DRAB2              = 'olive drab2'
COLOR_RGB_OLIVE_DRAB3              = 'olive drab3'
COLOR_RGB_OLIVE_DRAB4              = 'olive drab4'
COLOR_RGB_ORANGE                   = 'orange'
COLOR_RGB_ORANGE1                  = 'orange1'
COLOR_RGB_ORANGE2                  = 'orange2'
COLOR_RGB_ORANGE3                  = 'orange3'
COLOR_RGB_ORANGE4                  = 'orange4'
COLOR_RGB_ORANGE_RED               = 'orange red'
COLOR_RGB_ORANGE_RED1              = 'orange red1'
COLOR_RGB_ORANGE_RED2              = 'orange red2'
COLOR_RGB_ORCHID                   = 'orchid'
COLOR_RGB_ORCHID1                  = 'orchid1'
COLOR_RGB_ORCHID2                  = 'orchid2'
COLOR_RGB_ORCHID3                  = 'orchid3'
COLOR_RGB_ORCHID4                  = 'orchid4'
COLOR_RGB_PALE_GOLDENROD           = 'pale goldenrod'
COLOR_RGB_PALE_GREEN               = 'pale green'
COLOR_RGB_PALE_GREEN1              = 'pale green1'
COLOR_RGB_PALE_GREEN2              = 'pale green2'
COLOR_RGB_PALE_GREEN3              = 'pale green3'
COLOR_RGB_PALE_GREEN4              = 'pale green4'
COLOR_RGB_PALE_TURQUOISE           = 'pale turquoise'
COLOR_RGB_PALE_TURQUOISE1          = 'pale turquoise1'
COLOR_RGB_PALE_TURQUOISE2          = 'pale turquoise2'
COLOR_RGB_PALE_TURQUOISE3          = 'pale turquoise3'
COLOR_RGB_PALE_TURQUOISE4          = 'pale turquoise4'
COLOR_RGB_PALE_VIOLET_RED          = 'pale violet red'
COLOR_RGB_PALE_VIOLET_RED1         = 'pale violet red1'
COLOR_RGB_PALE_VIOLET_RED2         = 'pale violet red2'
COLOR_RGB_PALE_VIOLET_RED3         = 'pale violet red3'
COLOR_RGB_PALE_VIOLET_RED4         = 'pale violet red4'
COLOR_RGB_PAPAYA_WHIP              = 'papaya whip'
COLOR_RGB_PEACH_PUFF               = 'peach puff'
COLOR_RGB_PEACH_PUFF1              = 'peach puff1'
COLOR_RGB_PEACH_PUFF2              = 'peach puff2'
COLOR_RGB_PEACH_PUFF3              = 'peach puff3'
COLOR_RGB_PEACH_PUFF4              = 'peach puff4'
COLOR_RGB_PERU                     = 'peru'
COLOR_RGB_PINK                     = 'pink'
COLOR_RGB_PINK1                    = 'pink1'
COLOR_RGB_PINK2                    = 'pink2'
COLOR_RGB_PINK3                    = 'pink3'
COLOR_RGB_PINK4                    = 'pink4'
COLOR_RGB_PLUM                     = 'plum'
COLOR_RGB_PLUM1                    = 'plum1'
COLOR_RGB_PLUM2                    = 'plum2'
COLOR_RGB_PLUM3                    = 'plum3'
COLOR_RGB_PLUM4                    = 'plum4'
COLOR_RGB_POWDER_BLUE              = 'powder blue'
COLOR_RGB_PURPLE                   = 'purple'
COLOR_RGB_PURPLE1                  = 'purple1'
COLOR_RGB_PURPLE2                  = 'purple2'
COLOR_RGB_PURPLE3                  = 'purple3'
COLOR_RGB_PURPLE4                  = 'purple4'
COLOR_RGB_RED                      = 'red'
COLOR_RGB_ROSY_BROWN               = 'rosy brown'
COLOR_RGB_ROYAL_BLUE               = 'royal blue'
COLOR_RGB_ROYAL_BLUE1              = 'royal blue1'
COLOR_RGB_ROYAL_BLUE2              = 'royal blue2'
COLOR_RGB_ROYAL_BLUE3              = 'royal blue3'
COLOR_RGB_ROYAL_BLUE4              = 'royal blue4'
COLOR_RGB_SADDLE_BROWN             = 'saddle brown'
COLOR_RGB_SALMON                   = 'salmon'
COLOR_RGB_SALMON2                  = 'salmon2'
COLOR_RGB_SALMON3                  = 'salmon3'
COLOR_RGB_SALMON4                  = 'salmon4'
COLOR_RGB_SANDY_BROWN              = 'sandy brown'
COLOR_RGB_SEA_GREEN                = 'sea green'
COLOR_RGB_SEA_GREEN1               = 'sea green1'
COLOR_RGB_SEA_GREEN2               = 'sea green2'
COLOR_RGB_SEA_GREEN3               = 'sea green3'
COLOR_RGB_SEA_GREEN4               = 'sea green4'
COLOR_RGB_SEA_SHELL                = 'sea shell'
COLOR_RGB_SEA_SHELL1               = 'sea shell1'
COLOR_RGB_SEA_SHELL2               = 'sea shell2'
COLOR_RGB_SEA_SHELL3               = 'sea shell3'
COLOR_RGB_SEA_SHELL4               = 'sea shell4'
COLOR_RGB_SIENNA                   = 'sienna'
COLOR_RGB_SIENNA2                  = 'sienna2'
COLOR_RGB_SIENNA3                  = 'sienna3'
COLOR_RGB_SIENNA4                  = 'sienna4'
COLOR_RGB_SILVER                   = 'silver'
COLOR_RGB_SKY_BLUE                 = 'sky blue'
COLOR_RGB_SKY_BLUE1                = 'sky blue1'
COLOR_RGB_SKY_BLUE2                = 'sky blue2'
COLOR_RGB_SKY_BLUE3                = 'sky blue3'
COLOR_RGB_SKY_BLUE4                = 'sky blue4'
COLOR_RGB_SLATE_BLUE               = 'slate blue'
COLOR_RGB_SLATE_BLUE1              = 'slate blue1'
COLOR_RGB_SLATE_BLUE2              = 'slate blue2'
COLOR_RGB_SLATE_BLUE3              = 'slate blue3'
COLOR_RGB_SLATE_BLUE4              = 'slate blue4'
COLOR_RGB_SLATE_GRAY               = 'slate gray'
COLOR_RGB_SNOW                     = 'snow'
COLOR_RGB_SNOW1                    = 'snow1'
COLOR_RGB_SNOW2                    = 'snow2'
COLOR_RGB_SNOW3                    = 'snow3'
COLOR_RGB_SNOW4                    = 'snow4'
COLOR_RGB_SPRING_GREEN             = 'spring green'
COLOR_RGB_SPRING_GREEN1            = 'spring green1'
COLOR_RGB_SPRING_GREEN2            = 'spring green2'
COLOR_RGB_SPRING_GREEN3            = 'spring green3'
COLOR_RGB_SPRING_GREEN4            = 'spring green4'
COLOR_RGB_STEEL_BLUE               = 'steel blue'
COLOR_RGB_STEEL_BLUE1              = 'steel blue1'
COLOR_RGB_STEEL_BLUE2              = 'steel blue2'
COLOR_RGB_STEEL_BLUE3              = 'steel blue3'
COLOR_RGB_STEEL_BLUE4              = 'steel blue4'
COLOR_RGB_TAN                      = 'tan'
COLOR_RGB_TAN1                     = 'tan1'
COLOR_RGB_TAN2                     = 'tan2'
COLOR_RGB_TAN3                     = 'tan3'
COLOR_RGB_TAN4                     = 'tan4'
COLOR_RGB_TEAL                     = 'teal'
COLOR_RGB_THISTLE                  = 'thistle'
COLOR_RGB_TOMATO                   = 'tomato'
COLOR_RGB_TOMATO1                  = 'tomato1'
COLOR_RGB_TOMATO2                  = 'tomato2'
COLOR_RGB_TOMATO3                  = 'tomato3'
COLOR_RGB_TOMATO4                  = 'tomato4'
COLOR_RGB_TURQUOISE                = 'turquoise'
COLOR_RGB_TURQUOISE1               = 'turquoise1'
COLOR_RGB_TURQUOISE2               = 'turquoise2'
COLOR_RGB_TURQUOISE3               = 'turquoise3'
COLOR_RGB_TURQUOISE4               = 'turquoise4'
COLOR_RGB_VIOLET                   = 'violet'
COLOR_RGB_VIOLET_RED               = 'violet red'
COLOR_RGB_VIOLET_RED1              = 'violet red1'
COLOR_RGB_VIOLET_RED2              = 'violet red2'
COLOR_RGB_VIOLET_RED3              = 'violet red3'
COLOR_RGB_VIOLET_RED4              = 'violet red4'
COLOR_RGB_WHEAT                    = 'wheat'
COLOR_RGB_WHEAT1                   = 'wheat1'
COLOR_RGB_WHEAT2                   = 'wheat2'
COLOR_RGB_WHEAT3                   = 'wheat3'
COLOR_RGB_WHEAT4                   = 'wheat4'
COLOR_RGB_WHITE                    = 'white'
COLOR_RGB_WHITE_SMOKE              = 'white smoke'
COLOR_RGB_YELLOW                   = 'yellow'
COLOR_RGB_YELLOW1                  = 'yellow1'
COLOR_RGB_YELLOW2                  = 'yellow2'
COLOR_RGB_YELLOW3                  = 'yellow3'
COLOR_RGB_YELLOW4                  = 'yellow4'
COLOR_RGB_YELLOW_GREEN             = 'yellow green'

#---------------------------------------------------------------------------

# RGB values for set of color identifiers. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.
extendedColorDataBaseRGB = {
    'name': 'extendedColorDataBaseRGB',
    COLOR_RGB_ALICE_BLUE: (240, 248, 255),
    COLOR_RGB_ANTIQUE_WHITE: (250, 235, 215),
    COLOR_RGB_ANTIQUE_WHITE1: (255, 239, 219),
    COLOR_RGB_ANTIQUE_WHITE2: (238, 223, 204),
    COLOR_RGB_ANTIQUE_WHITE3: (205, 192, 176),
    COLOR_RGB_ANTIQUE_WHITE4: (139, 131, 120),
    COLOR_RGB_AQUAMARINE: (127, 255, 212),
    COLOR_RGB_AQUAMARINE1: (127, 255, 212),
    COLOR_RGB_AQUAMARINE2: (118, 238, 198),
    COLOR_RGB_AQUAMARINE3: (102, 205, 170),
    COLOR_RGB_AQUAMARINE4: (69, 139, 116),
    COLOR_RGB_AZURE: (240, 255, 255),
    COLOR_RGB_AZURE1: (240, 255, 255),
    COLOR_RGB_AZURE2: (224, 238, 238),
    COLOR_RGB_AZURE3: (193, 205, 205),
    COLOR_RGB_AZURE4: (131, 139, 139),
    COLOR_RGB_BEIGE: (245, 245, 220),
    COLOR_RGB_BISQUE: (255, 228, 196),
    COLOR_RGB_BISQUE1: (255, 228, 196),
    COLOR_RGB_BISQUE2: (238, 213, 183),
    COLOR_RGB_BISQUE3: (205, 183, 158),
    COLOR_RGB_BISQUE4: (139, 125, 107),
    COLOR_RGB_BLACK: (0, 0, 0),
    COLOR_RGB_BLANCHED_ALMOND: (255, 235, 205),
    COLOR_RGB_BLUE: (0, 0, 255),
    COLOR_RGB_BLUE1: (0, 0, 255),
    COLOR_RGB_BLUE2: (0, 0, 238),
    COLOR_RGB_BLUE3: (0, 0, 205),
    COLOR_RGB_BLUE4: (0, 0, 139),
    COLOR_RGB_BLUE_VIOLET: (138, 43, 226),
    COLOR_RGB_BROWN: (165, 42, 42),
    COLOR_RGB_BROWN1: (255, 64, 64),
    COLOR_RGB_BROWN2: (238, 59, 59),
    COLOR_RGB_BURLYWOOD: (222, 184, 135),
    COLOR_RGB_BURLYWOOD1: (255, 211, 155),
    COLOR_RGB_BURLYWOOD2: (238, 197, 145),
    COLOR_RGB_BURLYWOOD3: (205, 170, 125),
    COLOR_RGB_BURLYWOOD4: (139, 115, 85),
    COLOR_RGB_CADET_BLUE: (95, 158, 160),
    COLOR_RGB_CADET_BLUE1: (152, 245, 255),
    COLOR_RGB_CADET_BLUE2: (142, 229, 238),
    COLOR_RGB_CADET_BLUE3: (122, 197, 205),
    COLOR_RGB_CADET_BLUE4: (83, 134, 139),
    COLOR_RGB_CHARTREUSE: (127, 255, 0),
    COLOR_RGB_CHARTREUSE1: (127, 255, 0),
    COLOR_RGB_CHARTREUSE2: (118, 238, 0),
    COLOR_RGB_CHARTREUSE3: (102, 205, 0),
    COLOR_RGB_CHARTREUSE4: (69, 139, 0),
    COLOR_RGB_CHOCOLATE: (210, 105, 30),
    COLOR_RGB_CHOCOLATE1: (255, 127, 36),
    COLOR_RGB_CHOCOLATE2: (238, 118, 33),
    COLOR_RGB_CHOCOLATE3: (205, 102, 29),
    COLOR_RGB_CHOCOLATE4: (139, 69, 19),
    COLOR_RGB_CORAL: (255, 127, 80),
    COLOR_RGB_CORAL1: (255, 114, 86),
    COLOR_RGB_CORAL2: (238, 106, 80),
    COLOR_RGB_CORAL3: (205, 91, 69),
    COLOR_RGB_CORAL4: (139, 62, 47),
    COLOR_RGB_CORNFLOWER_BLUE: (100, 149, 237),
    COLOR_RGB_CORNSILK: (255, 248, 220),
    COLOR_RGB_CORNSILK1: (255, 248, 220),
    COLOR_RGB_CORNSILK2: (238, 232, 205),
    COLOR_RGB_CORNSILK3: (205, 200, 177),
    COLOR_RGB_CORNSILK4: (139, 136, 120),
    COLOR_RGB_CRIMSON: (220, 20, 60),
    COLOR_RGB_CYAN: (0, 255, 255),
    COLOR_RGB_CYAN1: (0, 255, 255),
    COLOR_RGB_CYAN2: (0, 238, 238),
    COLOR_RGB_CYAN3: (0, 205, 205),
    COLOR_RGB_CYAN4: (0, 139, 139),
    COLOR_RGB_DARK_BLUE: (0, 0, 139),
    COLOR_RGB_DARK_CYAN: (0, 139, 139),
    COLOR_RGB_DARK_GOLDENROD: (184, 134, 11),
    COLOR_RGB_DARK_GOLDENROD1: (255, 185, 15),
    COLOR_RGB_DARK_GOLDENROD2: (238, 173, 14),
    COLOR_RGB_DARK_GOLDENROD3: (205, 149, 12),
    COLOR_RGB_DARK_GRAY: (169, 169, 169),
    COLOR_RGB_DARK_GREEN: (0, 100, 0),
    COLOR_RGB_DARK_KHAKI: (189, 183, 107),
    COLOR_RGB_DARK_MAGENTA: (139, 0, 139),
    COLOR_RGB_DARK_OLIVE_GREEN: (85, 107, 47),
    COLOR_RGB_DARK_OLIVE_GREEN1: (202, 255, 112),
    COLOR_RGB_DARK_OLIVE_GREEN2: (188, 238, 104),
    COLOR_RGB_DARK_OLIVE_GREEN3: (162, 205, 90),
    COLOR_RGB_DARK_OLIVE_GREEN4: (110, 139, 61),
    COLOR_RGB_DARK_ORANGE: (255, 140, 0),
    COLOR_RGB_DARK_ORANGE1: (255, 127, 0),
    COLOR_RGB_DARK_ORANGE2: (238, 118, 0),
    COLOR_RGB_DARK_ORANGE3: (205, 102, 0),
    COLOR_RGB_DARK_ORANGE4: (139, 69, 0),
    COLOR_RGB_DARK_ORCHID: (153, 50, 204),
    COLOR_RGB_DARK_ORCHID1: (191, 62, 255),
    COLOR_RGB_DARK_ORCHID2: (178, 58, 238),
    COLOR_RGB_DARK_ORCHID3: (154, 50, 205),
    COLOR_RGB_DARK_ORCHID4: (104, 34, 139),
    COLOR_RGB_DARK_RED: (139, 0, 0),
    COLOR_RGB_DARK_SALMON: (233, 150, 122),
    COLOR_RGB_DARK_SEA_GREEN: (143, 188, 143),
    COLOR_RGB_DARK_SEA_GREEN1: (193, 255, 193),
    COLOR_RGB_DARK_SEA_GREEN2: (180, 238, 180),
    COLOR_RGB_DARK_SEA_GREEN3: (155, 205, 155),
    COLOR_RGB_DARK_SEA_GREEN4: (105, 139, 105),
    COLOR_RGB_DARK_SLATE_BLUE: (72, 61, 139),
    COLOR_RGB_DARK_SLATE_GRAY: (47, 79, 79),
    COLOR_RGB_DARK_TURQUOISE: (0, 206, 209),
    COLOR_RGB_DARK_VIOLET: (148, 0, 211),
    COLOR_RGB_DEEP_PINK: (255, 20, 147),
    COLOR_RGB_DEEP_PINK4: (139, 10, 80),
    COLOR_RGB_DEEP_SKY_BLUE: (0, 191, 255),
    COLOR_RGB_DEEP_SKY_BLUE1: (0, 191, 255),
    COLOR_RGB_DEEP_SKY_BLUE2: (0, 178, 238),
    COLOR_RGB_DEEP_SKY_BLUE3: (0, 154, 205),
    COLOR_RGB_DEEP_SKY_BLUE4: (0, 104, 139),
    COLOR_RGB_DIM_GRAY: (105, 105, 105),
    COLOR_RGB_DODGER_BLUE: (30, 144, 255),
    COLOR_RGB_DODGER_BLUE1: (30, 144, 255),
    COLOR_RGB_DODGER_BLUE2: (28, 134, 238),
    COLOR_RGB_DODGER_BLUE3: (24, 116, 205),
    COLOR_RGB_DODGER_BLUE4: (16, 78, 139),
    COLOR_RGB_FIREBRICK: (178, 34, 34),
    COLOR_RGB_FIREBRICK1: (255, 48, 48),
    COLOR_RGB_FIREBRICK2: (238, 44, 44),
    COLOR_RGB_FIREBRICK3: (205, 38, 38),
    COLOR_RGB_FIREBRICK4: (139, 26, 26),
    COLOR_RGB_FLORAL_WHITE: (255, 250, 240),
    COLOR_RGB_FOREST_GREEN: (34, 139, 34),
    COLOR_RGB_GAINSBORO: (220, 220, 220),
    COLOR_RGB_GHOST_WHITE: (248, 248, 255),
    COLOR_RGB_GOLD: (255, 215, 0),
    COLOR_RGB_GOLD1: (255, 215, 0),
    COLOR_RGB_GOLD2: (238, 201, 0),
    COLOR_RGB_GOLD3: (205, 173, 0),
    COLOR_RGB_GOLD4: (139, 117, 0),
    COLOR_RGB_GOLDENROD: (218, 165, 32),
    COLOR_RGB_GOLDENROD1: (255, 193, 37),
    COLOR_RGB_GOLDENROD2: (238, 180, 34),
    COLOR_RGB_GOLDENROD3: (205, 155, 29),
    COLOR_RGB_GOLDENROD4: (139, 105, 20),
    COLOR_RGB_GRAY: (190, 190, 190),
    COLOR_RGB_GRAY2: (5, 5, 5),
    COLOR_RGB_GRAY3: (8, 8, 8),
    COLOR_RGB_GRAY4: (10, 10, 10),
    COLOR_RGB_GRAY5: (13, 13, 13),
    COLOR_RGB_GRAY6: (15, 15, 15),
    COLOR_RGB_GRAY7: (18, 18, 18),
    COLOR_RGB_GRAY8: (20, 20, 20),
    COLOR_RGB_GRAY9: (23, 23, 23),
    COLOR_RGB_GRAY10: (26, 26, 26),
    COLOR_RGB_GRAY11: (28, 28, 28),
    COLOR_RGB_GRAY12: (31, 31, 31),
    COLOR_RGB_GRAY13: (33, 33, 33),
    COLOR_RGB_GRAY14: (36, 36, 36),
    COLOR_RGB_GRAY15: (38, 38, 38),
    COLOR_RGB_GRAY16: (41, 41, 41),
    COLOR_RGB_GRAY17: (43, 43, 43),
    COLOR_RGB_GRAY18: (46, 46, 46),
    COLOR_RGB_GRAY19: (48, 48, 48),
    COLOR_RGB_GRAY20: (51, 51, 51),
    COLOR_RGB_GRAY21: (54, 54, 54),
    COLOR_RGB_GRAY22: (56, 56, 56),
    COLOR_RGB_GRAY23: (59, 59, 59),
    COLOR_RGB_GRAY24: (61, 61, 61),
    COLOR_RGB_GRAY25: (64, 64, 64),
    COLOR_RGB_GRAY26: (66, 66, 66),
    COLOR_RGB_GRAY36: (92, 92, 92),
    COLOR_RGB_GRAY37: (94, 94, 94),
    COLOR_RGB_GRAY38: (97, 97, 97),
    COLOR_RGB_GRAY39: (99, 99, 99),
    COLOR_RGB_GRAY40: (102, 102, 102),
    COLOR_RGB_GRAY41: (105, 105, 105),
    COLOR_RGB_GRAY42: (107, 107, 107),
    COLOR_RGB_GRAY43: (110, 110, 110),
    COLOR_RGB_GRAY44: (112, 112, 112),
    COLOR_RGB_GRAY45: (115, 115, 115),
    COLOR_RGB_GRAY46: (117, 117, 117),
    COLOR_RGB_GRAY47: (120, 120, 120),
    COLOR_RGB_GRAY48: (122, 122, 122),
    COLOR_RGB_GRAY49: (125, 125, 125),
    COLOR_RGB_GRAY50: (127, 127, 127),
    COLOR_RGB_GRAY51: (130, 130, 130),
    COLOR_RGB_GRAY52: (133, 133, 133),
    COLOR_RGB_GRAY53: (135, 135, 135),
    COLOR_RGB_GRAY54: (138, 138, 138),
    COLOR_RGB_GRAY55: (140, 140, 140),
    COLOR_RGB_GRAY56: (143, 143, 143),
    COLOR_RGB_GRAY57: (145, 145, 145),
    COLOR_RGB_GRAY58: (148, 148, 148),
    COLOR_RGB_GRAY59: (150, 150, 150),
    COLOR_RGB_GRAY60: (153, 153, 153),
    COLOR_RGB_GRAY74: (189, 189, 189),
    COLOR_RGB_GRAY75: (191, 191, 191),
    COLOR_RGB_GRAY76: (194, 194, 194),
    COLOR_RGB_GRAY77: (196, 196, 196),
    COLOR_RGB_GRAY78: (199, 199, 199),
    COLOR_RGB_GRAY79: (201, 201, 201),
    COLOR_RGB_GRAY80: (204, 204, 204),
    COLOR_RGB_GRAY81: (207, 207, 207),
    COLOR_RGB_GRAY82: (209, 209, 209),
    COLOR_RGB_GRAY83: (212, 212, 212),
    COLOR_RGB_GRAY84: (214, 214, 214),
    COLOR_RGB_GRAY85: (217, 217, 217),
    COLOR_RGB_GRAY86: (219, 219, 219),
    COLOR_RGB_GRAY87: (222, 222, 222),
    COLOR_RGB_GRAY88: (224, 224, 224),
    COLOR_RGB_GRAY89: (227, 227, 227),
    COLOR_RGB_GRAY90: (229, 229, 229),
    COLOR_RGB_GRAY91: (232, 232, 232),
    COLOR_RGB_GRAY92: (235, 235, 235),
    COLOR_RGB_GRAY93: (237, 237, 237),
    COLOR_RGB_GRAY94: (240, 240, 240),
    COLOR_RGB_GRAY95: (242, 242, 242),
    COLOR_RGB_GRAY96: (245, 245, 245),
    COLOR_RGB_GRAY97: (247, 247, 247),
    COLOR_RGB_GRAY98: (250, 250, 250),
    COLOR_RGB_GRAY99: (252, 252, 252),
    COLOR_RGB_GRAY100: (255, 255, 255),
    COLOR_RGB_GREEN: (0, 255, 0),
    COLOR_RGB_GREEN1: (0, 255, 0),
    COLOR_RGB_GREEN2: (0, 238, 0),
    COLOR_RGB_GREEN3: (0, 205, 0),
    COLOR_RGB_GREEN4: (0, 139, 0),
    COLOR_RGB_GREEN_YELLOW: (173, 255, 47),
    COLOR_RGB_HONEYDEW: (240, 255, 240),
    COLOR_RGB_HONEYDEW1: (240, 255, 240),
    COLOR_RGB_HONEYDEW2: (224, 238, 224),
    COLOR_RGB_HONEYDEW3: (193, 205, 193),
    COLOR_RGB_HONEYDEW4: (131, 139, 131),
    COLOR_RGB_HOT_PINK: (255, 105, 180),
    COLOR_RGB_HOT_PINK1: (255, 110, 180),
    COLOR_RGB_HOT_PINK2: (238, 106, 167),
    COLOR_RGB_HOT_PINK3: (205, 96, 144),
    COLOR_RGB_HOT_PINK4: (139, 58, 98),
    COLOR_RGB_INDIAN_RED: (205, 92, 92),
    COLOR_RGB_INDIGO: (75, 0, 130),
    COLOR_RGB_IVORY: (255, 255, 240),
    COLOR_RGB_IVORY1: (255, 255, 240),
    COLOR_RGB_IVORY2: (238, 238, 224),
    COLOR_RGB_IVORY3: (205, 205, 193),
    COLOR_RGB_IVORY4: (139, 139, 131),
    COLOR_RGB_KHAKI: (240, 230, 140),
    COLOR_RGB_KHAKI1: (255, 246, 143),
    COLOR_RGB_KHAKI2: (238, 230, 133),
    COLOR_RGB_KHAKI3: (205, 198, 115),
    COLOR_RGB_KHAKI4: (139, 134, 78),
    COLOR_RGB_LAVENDER: (230, 230, 250),
    COLOR_RGB_LAVENDER_BLUSH: (255, 240, 245),
    COLOR_RGB_LAVENDER_BLUSH1: (255, 240, 245),
    COLOR_RGB_LAVENDER_BLUSH2: (238, 224, 229),
    COLOR_RGB_LAVENDER_BLUSH3: (205, 193, 197),
    COLOR_RGB_LAVENDER_BLUSH4: (139, 131, 134),
    COLOR_RGB_LAWN_GREEN: (124, 252, 0),
    COLOR_RGB_LEMON_CHIFFON: (255, 250, 205),
    COLOR_RGB_LEMON_CHIFFON1: (255, 250, 205),
    COLOR_RGB_LEMON_CHIFFON2: (238, 233, 191),
    COLOR_RGB_LEMON_CHIFFON3: (205, 201, 165),
    COLOR_RGB_LEMON_CHIFFON4: (139, 137, 112),
    COLOR_RGB_LIGHT_BLUE: (173, 216, 230),
    COLOR_RGB_LIGHT_BLUE1: (191, 239, 255),
    COLOR_RGB_LIGHT_BLUE2: (178, 223, 238),
    COLOR_RGB_LIGHT_BLUE3: (154, 192, 205),
    COLOR_RGB_LIGHT_BLUE4: (104, 131, 139),
    COLOR_RGB_LIGHT_CORAL: (240, 128, 128),
    COLOR_RGB_LIGHT_CYAN: (224, 255, 255),
    COLOR_RGB_LIGHT_CYAN1: (224, 255, 255),
    COLOR_RGB_LIGHT_CYAN2: (209, 238, 238),
    COLOR_RGB_LIGHT_CYAN3: (180, 205, 205),
    COLOR_RGB_LIGHT_CYAN4: (122, 139, 139),
    COLOR_RGB_LIGHT_GOLDENROD: (238, 221, 130),
    COLOR_RGB_LIGHT_GOLDENROD1: (255, 236, 139),
    COLOR_RGB_LIGHT_GOLDENROD2: (238, 220, 130),
    COLOR_RGB_LIGHT_GOLDENROD3: (205, 190, 112),
    COLOR_RGB_LIGHT_GOLDENROD4: (139, 129, 76),
    COLOR_RGB_LIGHT_GOLDENROD_YELLOW: (250, 250, 210),
    COLOR_RGB_LIGHT_GRAY: (211, 211, 211),
    COLOR_RGB_LIGHT_GREEN: (144, 238, 144),
    COLOR_RGB_LIGHT_PINK: (255, 182, 193),
    COLOR_RGB_LIGHT_PINK1: (255, 174, 185),
    COLOR_RGB_LIGHT_PINK2: (238, 162, 173),
    COLOR_RGB_LIGHT_PINK3: (205, 140, 149),
    COLOR_RGB_LIGHT_PINK4: (139, 95, 101),
    COLOR_RGB_LIGHT_SALMON: (255, 160, 122),
    COLOR_RGB_LIGHT_SALMON1: (255, 160, 122),
    COLOR_RGB_LIGHT_SALMON2: (238, 149, 114),
    COLOR_RGB_LIGHT_SALMON3: (205, 129, 98),
    COLOR_RGB_LIGHT_SALMON4: (139, 87, 66),
    COLOR_RGB_LIGHT_SEA_GREEN: (32, 178, 170),
    COLOR_RGB_LIGHT_SKY_BLUE: (135, 206, 250),
    COLOR_RGB_LIGHT_SKY_BLUE1: (176, 226, 255),
    COLOR_RGB_LIGHT_SKY_BLUE2: (164, 211, 238),
    COLOR_RGB_LIGHT_SKY_BLUE3: (141, 182, 205),
    COLOR_RGB_LIGHT_SKY_BLUE4: (96, 123, 139),
    COLOR_RGB_LIGHT_SLATE_BLUE: (132, 112, 255),
    COLOR_RGB_LIGHT_SLATE_GRAY: (119, 136, 153),
    COLOR_RGB_LIGHT_STEEL_BLUE: (176, 196, 222),
    COLOR_RGB_LIGHT_STEEL_BLUE1: (202, 225, 255),
    COLOR_RGB_LIGHT_STEEL_BLUE2: (188, 210, 238),
    COLOR_RGB_LIGHT_STEEL_BLUE3: (162, 181, 205),
    COLOR_RGB_LIGHT_STEEL_BLUE4: (110, 123, 139),
    COLOR_RGB_LIGHT_YELLOW: (255, 255, 224),
    COLOR_RGB_LIGHT_YELLOW1: (255, 255, 224),
    COLOR_RGB_LIGHT_YELLOW2: (238, 238, 209),
    COLOR_RGB_LIGHT_YELLOW3: (205, 205, 180),
    COLOR_RGB_LIGHT_YELLOW4: (139, 139, 122),
    COLOR_RGB_LIME_GREEN: (50, 205, 50),
    COLOR_RGB_LINEN: (250, 240, 230),
    COLOR_RGB_MAGENTA: (255, 0, 255),
    COLOR_RGB_MAGENTA1: (255, 0, 255),
    COLOR_RGB_MAGENTA2: (238, 0, 238),
    COLOR_RGB_MAGENTA3: (205, 0, 205),
    COLOR_RGB_MAGENTA4: (139, 0, 139),
    COLOR_RGB_MAROON: (176, 48, 96),
    COLOR_RGB_MAROON1: (255, 52, 179),
    COLOR_RGB_MAROON2: (238, 48, 167),
    COLOR_RGB_MAROON3: (205, 41, 144),
    COLOR_RGB_MAROON4: (139, 28, 98),
    COLOR_RGB_MEDIUM_AQUAMARINE: (102, 205, 170),
    COLOR_RGB_MEDIUM_BLUE: (0, 0, 205),
    COLOR_RGB_MEDIUM_FOREST_GREEN: (107, 142, 35),
    COLOR_RGB_MEDIUM_GOLDENROD: (192, 192, 174),
    COLOR_RGB_MEDIUM_ORCHID: (186, 85, 211),
    COLOR_RGB_MEDIUM_ORCHID1: (224, 102, 255),
    COLOR_RGB_MEDIUM_ORCHID2: (209, 95, 238),
    COLOR_RGB_MEDIUM_ORCHID3: (180, 82, 205),
    COLOR_RGB_MEDIUM_ORCHID4: (122, 55, 139),
    COLOR_RGB_MEDIUM_PURPLE: (147, 112, 219),
    COLOR_RGB_MEDIUM_SEA_GREEN: (60, 179, 113),
    COLOR_RGB_MEDIUM_SLATE_BLUE: (123, 104, 238),
    COLOR_RGB_MEDIUM_SPRING_GREEN: (0, 250, 154),
    COLOR_RGB_MEDIUM_TURQUOISE: (72, 209, 204),
    COLOR_RGB_MEDIUM_VIOLET_RED: (199, 21, 133),
    COLOR_RGB_MIDNIGHT_BLUE: (25, 25, 112),
    COLOR_RGB_MINT_CREAM: (245, 255, 250),
    COLOR_RGB_MISTY_ROSE: (255, 228, 225),
    COLOR_RGB_MISTY_ROSE1: (255, 228, 225),
    COLOR_RGB_MISTY_ROSE2: (238, 213, 210),
    COLOR_RGB_MISTY_ROSE3: (205, 183, 181),
    COLOR_RGB_MISTY_ROSE4: (139, 125, 123),
    COLOR_RGB_MOCCASIN: (255, 228, 181),
    COLOR_RGB_NAVAJO_WHITE: (255, 222, 173),
    COLOR_RGB_NAVAJO_WHITE1: (255, 222, 173),
    COLOR_RGB_NAVAJO_WHITE2: (238, 207, 161),
    COLOR_RGB_NAVAJO_WHITE3: (205, 179, 139),
    COLOR_RGB_NAVAJO_WHITE4: (139, 121, 94),
    COLOR_RGB_NAVY: (0, 0, 128),
    COLOR_RGB_NAVY_BLUE: (0, 0, 128),
    COLOR_RGB_OLD_LACE: (253, 245, 230),
    COLOR_RGB_OLIVE: (128, 128, 0),
    COLOR_RGB_OLIVE_DRAB: (107, 142, 35),
    COLOR_RGB_OLIVE_DRAB1: (192, 255, 62),
    COLOR_RGB_OLIVE_DRAB2: (179, 238, 58),
    COLOR_RGB_OLIVE_DRAB3: (154, 205, 50),
    COLOR_RGB_OLIVE_DRAB4: (105, 139, 34),
    COLOR_RGB_ORANGE: (255, 165, 0),
    COLOR_RGB_ORANGE1: (255, 165, 0),
    COLOR_RGB_ORANGE2: (238, 154, 0),
    COLOR_RGB_ORANGE3: (205, 133, 0),
    COLOR_RGB_ORANGE4: (139, 90, 0),
    COLOR_RGB_ORANGE_RED: (255, 69, 0),
    COLOR_RGB_ORANGE_RED1: (255, 69, 0),
    COLOR_RGB_ORANGE_RED2: (238, 64, 0),
    COLOR_RGB_ORCHID: (218, 112, 214),
    COLOR_RGB_ORCHID1: (255, 131, 250),
    COLOR_RGB_ORCHID2: (238, 122, 233),
    COLOR_RGB_ORCHID3: (205, 105, 201),
    COLOR_RGB_ORCHID4: (139, 71, 137),
    COLOR_RGB_PALE_GOLDENROD: (238, 232, 170),
    COLOR_RGB_PALE_GREEN: (152, 251, 152),
    COLOR_RGB_PALE_GREEN1: (154, 255, 154),
    COLOR_RGB_PALE_GREEN2: (144, 238, 144),
    COLOR_RGB_PALE_GREEN3: (124, 205, 124),
    COLOR_RGB_PALE_GREEN4: (84, 139, 84),
    COLOR_RGB_PALE_TURQUOISE: (175, 238, 238),
    COLOR_RGB_PALE_TURQUOISE1: (187, 255, 255),
    COLOR_RGB_PALE_TURQUOISE2: (174, 238, 238),
    COLOR_RGB_PALE_TURQUOISE3: (150, 205, 205),
    COLOR_RGB_PALE_TURQUOISE4: (102, 139, 139),
    COLOR_RGB_PALE_VIOLET_RED: (219, 112, 147),
    COLOR_RGB_PALE_VIOLET_RED1: (255, 130, 171),
    COLOR_RGB_PALE_VIOLET_RED2: (238, 121, 159),
    COLOR_RGB_PALE_VIOLET_RED3: (205, 104, 137),
    COLOR_RGB_PALE_VIOLET_RED4: (139, 71, 93),
    COLOR_RGB_PAPAYA_WHIP: (255, 239, 213),
    COLOR_RGB_PEACH_PUFF: (255, 218, 185),
    COLOR_RGB_PEACH_PUFF1: (255, 218, 185),
    COLOR_RGB_PEACH_PUFF2: (238, 203, 173),
    COLOR_RGB_PEACH_PUFF3: (205, 175, 149),
    COLOR_RGB_PEACH_PUFF4: (139, 119, 101),
    COLOR_RGB_PERU: (205, 133, 63),
    COLOR_RGB_PINK: (255, 192, 203),
    COLOR_RGB_PINK1: (255, 181, 197),
    COLOR_RGB_PINK2: (238, 169, 184),
    COLOR_RGB_PINK3: (205, 145, 158),
    COLOR_RGB_PINK4: (139, 99, 108),
    COLOR_RGB_PLUM: (221, 160, 221),
    COLOR_RGB_PLUM1: (255, 187, 255),
    COLOR_RGB_PLUM2: (238, 174, 238),
    COLOR_RGB_PLUM3: (205, 150, 205),
    COLOR_RGB_PLUM4: (139, 102, 139),
    COLOR_RGB_POWDER_BLUE: (176, 224, 230),
    COLOR_RGB_PURPLE: (160, 32, 240),
    COLOR_RGB_PURPLE1: (155, 48, 255),
    COLOR_RGB_PURPLE2: (145, 44, 238),
    COLOR_RGB_PURPLE3: (125, 38, 205),
    COLOR_RGB_PURPLE4: (85, 26, 139),
    COLOR_RGB_RED: (255, 0, 0),
    COLOR_RGB_ROSY_BROWN: (188, 143, 143),
    COLOR_RGB_ROYAL_BLUE: (65, 105, 225),
    COLOR_RGB_ROYAL_BLUE1: (72, 118, 255),
    COLOR_RGB_ROYAL_BLUE2: (67, 110, 238),
    COLOR_RGB_ROYAL_BLUE3: (58, 95, 205),
    COLOR_RGB_ROYAL_BLUE4: (39, 64, 139),
    COLOR_RGB_SADDLE_BROWN: (139, 69, 19),
    COLOR_RGB_SALMON: (250, 128, 114),
    COLOR_RGB_SALMON2: (238, 130, 98),
    COLOR_RGB_SALMON3: (205, 112, 84),
    COLOR_RGB_SALMON4: (139, 76, 57),
    COLOR_RGB_SANDY_BROWN: (244, 164, 96),
    COLOR_RGB_SEA_GREEN: (46, 139, 87),
    COLOR_RGB_SEA_GREEN1: (84, 255, 159),
    COLOR_RGB_SEA_GREEN2: (78, 238, 148),
    COLOR_RGB_SEA_GREEN3: (67, 205, 128),
    COLOR_RGB_SEA_GREEN4: (46, 139, 87),
    COLOR_RGB_SEA_SHELL: (255, 245, 238),
    COLOR_RGB_SEA_SHELL1: (255, 245, 238),
    COLOR_RGB_SEA_SHELL2: (238, 229, 222),
    COLOR_RGB_SEA_SHELL3: (205, 197, 191),
    COLOR_RGB_SEA_SHELL4: (139, 134, 130),
    COLOR_RGB_SIENNA: (160, 82, 45),
    COLOR_RGB_SIENNA2: (238, 121, 66),
    COLOR_RGB_SIENNA3: (205, 104, 57),
    COLOR_RGB_SIENNA4: (139, 71, 38),
    COLOR_RGB_SILVER: (192, 192, 192),
    COLOR_RGB_SKY_BLUE: (135, 206, 235),
    COLOR_RGB_SKY_BLUE1: (135, 206, 255),
    COLOR_RGB_SKY_BLUE2: (126, 192, 238),
    COLOR_RGB_SKY_BLUE3: (108, 166, 205),
    COLOR_RGB_SKY_BLUE4: (74, 112, 139),
    COLOR_RGB_SLATE_BLUE: (106, 90, 205),
    COLOR_RGB_SLATE_BLUE1: (131, 111, 255),
    COLOR_RGB_SLATE_BLUE2: (122, 103, 238),
    COLOR_RGB_SLATE_BLUE3: (105, 89, 205),
    COLOR_RGB_SLATE_BLUE4: (71, 60, 139),
    COLOR_RGB_SLATE_GRAY: (112, 128, 144),
    COLOR_RGB_SNOW: (255, 250, 250),
    COLOR_RGB_SNOW1: (255, 250, 250),
    COLOR_RGB_SNOW2: (238, 233, 233),
    COLOR_RGB_SNOW3: (205, 201, 201),
    COLOR_RGB_SNOW4: (139, 137, 137),
    COLOR_RGB_SPRING_GREEN: (0, 255, 127),
    COLOR_RGB_SPRING_GREEN1: (0, 255, 127),
    COLOR_RGB_SPRING_GREEN2: (0, 238, 118),
    COLOR_RGB_SPRING_GREEN3: (0, 205, 102),
    COLOR_RGB_SPRING_GREEN4: (0, 139, 69),
    COLOR_RGB_STEEL_BLUE: (70, 130, 180),
    COLOR_RGB_STEEL_BLUE1: (99, 184, 255),
    COLOR_RGB_STEEL_BLUE2: (92, 172, 238),
    COLOR_RGB_STEEL_BLUE3: (79, 148, 205),
    COLOR_RGB_STEEL_BLUE4: (54, 100, 139),
    COLOR_RGB_TAN: (210, 180, 140),
    COLOR_RGB_TAN1: (255, 165, 79),
    COLOR_RGB_TAN2: (238, 154, 73),
    COLOR_RGB_TAN3: (205, 133, 63),
    COLOR_RGB_TAN4: (139, 90, 43),
    COLOR_RGB_TEAL: (0, 128, 128),
    COLOR_RGB_THISTLE: (216, 191, 216),
    COLOR_RGB_TOMATO: (255, 99, 71),
    COLOR_RGB_TOMATO1: (255, 99, 71),
    COLOR_RGB_TOMATO2: (238, 92, 66),
    COLOR_RGB_TOMATO3: (205, 79, 57),
    COLOR_RGB_TOMATO4: (139, 54, 38),
    COLOR_RGB_TURQUOISE: (64, 224, 208),
    COLOR_RGB_TURQUOISE1: (0, 245, 255),
    COLOR_RGB_TURQUOISE2: (0, 229, 238),
    COLOR_RGB_TURQUOISE3: (0, 197, 205),
    COLOR_RGB_TURQUOISE4: (0, 134, 139),
    COLOR_RGB_VIOLET: (238, 130, 238),
    COLOR_RGB_VIOLET_RED: (208, 32, 144),
    COLOR_RGB_VIOLET_RED1: (255, 62, 150),
    COLOR_RGB_VIOLET_RED2: (238, 58, 140),
    COLOR_RGB_VIOLET_RED3: (205, 50, 120),
    COLOR_RGB_VIOLET_RED4: (139, 34, 82),
    COLOR_RGB_WHEAT: (245, 222, 179),
    COLOR_RGB_WHEAT1: (255, 231, 186),
    COLOR_RGB_WHEAT2: (238, 216, 174),
    COLOR_RGB_WHEAT3: (205, 186, 150),
    COLOR_RGB_WHEAT4: (139, 126, 102),
    COLOR_RGB_WHITE: (255, 255, 255),
    COLOR_RGB_WHITE_SMOKE: (245, 245, 245),
    COLOR_RGB_YELLOW: (255, 255, 0),
    COLOR_RGB_YELLOW1: (255, 255, 0),
    COLOR_RGB_YELLOW2: (238, 238, 0),
    COLOR_RGB_YELLOW3: (205, 205, 0),
    COLOR_RGB_YELLOW4: (139, 139, 0),
    COLOR_RGB_YELLOW_GREEN: (154, 205, 50)
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n extendedColorDataBaseRGB=%s' % str(
        extendedColorDataBaseRGB))
    debug_via_tsru(myDictionary=extendedColorDataBaseRGB)

#---------------------------------------------------------------------------

# Set of color identifiers that the character-mode wxPython
# emulation guarantees to be recognized.
COLOR_ALICE_BLUE               = COLOR_RGB_ALICE_BLUE
COLOR_ANTIQUE_WHITE            = COLOR_RGB_ANTIQUE_WHITE
COLOR_AQUAMARINE               = COLOR_RGB_AQUAMARINE
COLOR_AZURE                    = COLOR_RGB_AZURE
COLOR_BEIGE                    = COLOR_RGB_BEIGE
COLOR_BISQUE                   = COLOR_RGB_BISQUE
COLOR_BLACK                    = COLOR_RGB_BLACK
COLOR_BLANCHED_ALMOND          = COLOR_RGB_BLANCHED_ALMOND
COLOR_BLUE                     = COLOR_RGB_BLUE
COLOR_BLUE_VIOLET              = COLOR_RGB_BLUE_VIOLET
COLOR_BROWN                    = COLOR_RGB_BROWN
COLOR_BURLYWOOD                = COLOR_RGB_BURLYWOOD
COLOR_CADET_BLUE               = COLOR_RGB_CADET_BLUE
COLOR_CHARTREUSE               = COLOR_RGB_CHARTREUSE
COLOR_CHOCOLATE                = COLOR_RGB_CHOCOLATE
COLOR_CORAL                    = COLOR_RGB_CORAL
COLOR_CORNFLOWER_BLUE          = COLOR_RGB_CORNFLOWER_BLUE
COLOR_CORNSILK                 = COLOR_RGB_CORNSILK
COLOR_CRIMSON                  = COLOR_RGB_CRIMSON
COLOR_CYAN                     = COLOR_RGB_CYAN
COLOR_DARK_BLUE                = COLOR_RGB_DARK_BLUE
COLOR_DARK_CYAN                = COLOR_RGB_DARK_CYAN
COLOR_DARK_GOLDENROD           = COLOR_RGB_DARK_GOLDENROD
COLOR_DARK_GRAY                = COLOR_RGB_DARK_GRAY
COLOR_DARK_GREEN               = COLOR_RGB_DARK_GREEN
COLOR_DARK_KHAKI               = COLOR_RGB_DARK_KHAKI
COLOR_DARK_MAGENTA             = COLOR_RGB_DARK_MAGENTA
COLOR_DARK_OLIVE_GREEN         = COLOR_RGB_DARK_OLIVE_GREEN
COLOR_DARK_ORANGE              = COLOR_RGB_DARK_ORANGE
COLOR_DARK_ORCHID              = COLOR_RGB_DARK_ORCHID
COLOR_DARK_RED                 = COLOR_RGB_DARK_RED
COLOR_DARK_SALMON              = COLOR_RGB_DARK_SALMON
COLOR_DARK_SEA_GREEN           = COLOR_RGB_DARK_SEA_GREEN
COLOR_DARK_SLATE_BLUE          = COLOR_RGB_DARK_SLATE_BLUE
COLOR_DARK_SLATE_GRAY          = COLOR_RGB_DARK_SLATE_GRAY
COLOR_DARK_TURQUOISE           = COLOR_RGB_DARK_TURQUOISE
COLOR_DARK_VIOLET              = COLOR_RGB_DARK_VIOLET
COLOR_DEEP_PINK                = COLOR_RGB_DEEP_PINK
COLOR_DEEP_SKY_BLUE            = COLOR_RGB_DEEP_SKY_BLUE
COLOR_DIM_GRAY                 = COLOR_RGB_DIM_GRAY
COLOR_DODGER_BLUE              = COLOR_RGB_DODGER_BLUE
COLOR_FIREBRICK                = COLOR_RGB_FIREBRICK
COLOR_FLORAL_WHITE             = COLOR_RGB_FLORAL_WHITE
COLOR_FOREST_GREEN             = COLOR_RGB_FOREST_GREEN
COLOR_GAINSBORO                = COLOR_RGB_GAINSBORO
COLOR_GHOST_WHITE              = COLOR_RGB_GHOST_WHITE
COLOR_GOLD                     = COLOR_RGB_GOLD
COLOR_GOLDENROD                = COLOR_RGB_GOLDENROD
COLOR_GRAY                     = COLOR_RGB_GRAY
COLOR_GREEN                    = COLOR_RGB_GREEN
COLOR_GREEN_YELLOW             = COLOR_RGB_GREEN_YELLOW
COLOR_HONEYDEW                 = COLOR_RGB_HONEYDEW
COLOR_HOT_PINK                 = COLOR_RGB_HOT_PINK
COLOR_INDIAN_RED               = COLOR_RGB_INDIAN_RED
COLOR_INDIGO                   = COLOR_RGB_INDIGO
COLOR_IVORY                    = COLOR_RGB_IVORY
COLOR_KHAKI                    = COLOR_RGB_KHAKI
COLOR_LAVENDER                 = COLOR_RGB_LAVENDER
COLOR_LAVENDER_BLUSH           = COLOR_RGB_LAVENDER_BLUSH
COLOR_LAWN_GREEN               = COLOR_RGB_LAWN_GREEN
COLOR_LEMON_CHIFFON            = COLOR_RGB_LEMON_CHIFFON
COLOR_LIGHT_BLUE               = COLOR_RGB_LIGHT_BLUE
COLOR_LIGHT_CORAL              = COLOR_RGB_LIGHT_CORAL
COLOR_LIGHT_CYAN               = COLOR_RGB_LIGHT_CYAN
COLOR_LIGHT_GOLDENROD_YELLOW   = COLOR_RGB_LIGHT_GOLDENROD_YELLOW
COLOR_LIGHT_GRAY               = COLOR_RGB_LIGHT_GRAY
COLOR_LIGHT_GREEN              = COLOR_RGB_LIGHT_GREEN
COLOR_LIGHT_PINK               = COLOR_RGB_LIGHT_PINK
COLOR_LIGHT_SALMON             = COLOR_RGB_LIGHT_SALMON
COLOR_LIGHT_SEA_GREEN          = COLOR_RGB_LIGHT_SEA_GREEN
COLOR_LIGHT_SKY_BLUE           = COLOR_RGB_LIGHT_SKY_BLUE
COLOR_LIGHT_SLATE_GRAY         = COLOR_RGB_LIGHT_SLATE_GRAY
COLOR_LIGHT_STEEL_BLUE         = COLOR_RGB_LIGHT_STEEL_BLUE
COLOR_LIGHT_STEEL_BLUE         = COLOR_RGB_LIGHT_STEEL_BLUE
COLOR_LIGHT_YELLOW             = COLOR_RGB_LIGHT_YELLOW
COLOR_LIME_GREEN               = COLOR_RGB_LIME_GREEN
COLOR_LINEN                    = COLOR_RGB_LINEN
COLOR_MAGENTA                  = COLOR_RGB_MAGENTA
COLOR_MAROON                   = COLOR_RGB_MAROON
COLOR_MEDIUM_AQUAMARINE        = COLOR_RGB_MEDIUM_AQUAMARINE
COLOR_MEDIUM_BLUE              = COLOR_RGB_MEDIUM_BLUE
COLOR_MEDIUM_FOREST_GREEN      = COLOR_RGB_MEDIUM_FOREST_GREEN
COLOR_MEDIUM_GOLDENROD         = COLOR_RGB_MEDIUM_GOLDENROD
COLOR_MEDIUM_ORCHID            = COLOR_RGB_MEDIUM_ORCHID
COLOR_MEDIUM_PURPLE            = COLOR_RGB_MEDIUM_PURPLE
COLOR_MEDIUM_SEA_GREEN         = COLOR_RGB_MEDIUM_SEA_GREEN
COLOR_MEDIUM_SLATE_BLUE        = COLOR_RGB_MEDIUM_SLATE_BLUE
COLOR_MEDIUM_SPRING_GREEN      = COLOR_RGB_MEDIUM_SPRING_GREEN
COLOR_MEDIUM_TURQUOISE         = COLOR_RGB_MEDIUM_TURQUOISE
COLOR_MEDIUM_VIOLET_RED        = COLOR_RGB_MEDIUM_VIOLET_RED
COLOR_MIDNIGHT_BLUE            = COLOR_RGB_MIDNIGHT_BLUE
COLOR_MINT_CREAM               = COLOR_RGB_MINT_CREAM
COLOR_MISTY_ROSE               = COLOR_RGB_MISTY_ROSE
COLOR_MOCCASIN                 = COLOR_RGB_MOCCASIN
COLOR_NAVAJO_WHITE             = COLOR_RGB_NAVAJO_WHITE
COLOR_NAVY                     = COLOR_RGB_NAVY
COLOR_OLD_LACE                 = COLOR_RGB_OLD_LACE
COLOR_OLIVE                    = COLOR_RGB_OLIVE
COLOR_OLIVE_DRAB               = COLOR_RGB_OLIVE_DRAB
COLOR_ORANGE                   = COLOR_RGB_ORANGE
COLOR_ORANGE_RED               = COLOR_RGB_ORANGE_RED
COLOR_ORCHID                   = COLOR_RGB_ORCHID
COLOR_PALE_GOLDENROD           = COLOR_RGB_PALE_GOLDENROD
COLOR_PALE_GREEN               = COLOR_RGB_PALE_GREEN
COLOR_PALE_TURQUOISE           = COLOR_RGB_PALE_TURQUOISE
COLOR_PALE_VIOLET_RED          = COLOR_RGB_PALE_VIOLET_RED
COLOR_PAPAYA_WHIP              = COLOR_RGB_PAPAYA_WHIP
COLOR_PEACH_PUFF               = COLOR_RGB_PEACH_PUFF
COLOR_PERU                     = COLOR_RGB_PERU
COLOR_PINK                     = COLOR_RGB_PINK
COLOR_PLUM                     = COLOR_RGB_PLUM
COLOR_POWDER_BLUE              = COLOR_RGB_POWDER_BLUE
COLOR_PURPLE                   = COLOR_RGB_PURPLE
COLOR_RED                      = COLOR_RGB_RED
COLOR_ROSY_BROWN               = COLOR_RGB_ROSY_BROWN
COLOR_ROYAL_BLUE               = COLOR_RGB_ROYAL_BLUE
COLOR_SADDLE_BROWN             = COLOR_RGB_SADDLE_BROWN
COLOR_SALMON                   = COLOR_RGB_SALMON
COLOR_SANDY_BROWN              = COLOR_RGB_SANDY_BROWN
COLOR_SEA_GREEN                = COLOR_RGB_SEA_GREEN
COLOR_SEA_SHELL                = COLOR_RGB_SEA_SHELL
COLOR_SIENNA                   = COLOR_RGB_SIENNA
COLOR_SILVER                   = COLOR_RGB_SILVER
COLOR_SKY_BLUE                 = COLOR_RGB_SKY_BLUE
COLOR_SLATE_BLUE               = COLOR_RGB_SLATE_BLUE
COLOR_SLATE_GRAY               = COLOR_RGB_SLATE_GRAY
COLOR_SNOW                     = COLOR_RGB_SNOW
COLOR_SPRING_GREEN             = COLOR_RGB_SPRING_GREEN
COLOR_STEEL_BLUE               = COLOR_RGB_STEEL_BLUE
COLOR_TAN                      = COLOR_RGB_TAN
COLOR_TEAL                     = COLOR_RGB_TEAL
COLOR_THISTLE                  = COLOR_RGB_THISTLE
COLOR_TOMATO                   = COLOR_RGB_TOMATO
COLOR_TURQUOISE                = COLOR_RGB_TURQUOISE
COLOR_VIOLET                   = COLOR_RGB_VIOLET
COLOR_VIOLET_RED               = COLOR_RGB_VIOLET_RED
COLOR_WHEAT                    = COLOR_RGB_WHEAT
COLOR_WHITE                    = COLOR_RGB_WHITE
COLOR_WHITE_SMOKE              = COLOR_RGB_WHITE_SMOKE
COLOR_YELLOW                   = COLOR_RGB_YELLOW
COLOR_YELLOW_GREEN             = COLOR_RGB_YELLOW_GREEN
#
# The wxPythonColorSubstitutionMap includes:
#     a) all  68 colors wxPython guarantees to support
#     b) the  71 (previous 68 + 3) colors for xterm-88color support
#     c) the 140 (previous 71 + 69) colors for xterm-256color support
wxPythonColorDataBaseRGB = {
    'name': 'wxPythonColorDataBaseRGB',
    COLOR_ALICE_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_ALICE_BLUE],
    COLOR_ANTIQUE_WHITE            : extendedColorDataBaseRGB[COLOR_RGB_ANTIQUE_WHITE],
    COLOR_AQUAMARINE               : extendedColorDataBaseRGB[COLOR_RGB_AQUAMARINE],
    COLOR_AZURE                    : extendedColorDataBaseRGB[COLOR_RGB_AZURE],
    COLOR_BEIGE                    : extendedColorDataBaseRGB[COLOR_RGB_BEIGE],
    COLOR_BISQUE                   : extendedColorDataBaseRGB[COLOR_RGB_BISQUE],
    COLOR_BLACK                    : extendedColorDataBaseRGB[COLOR_RGB_BLACK],
    COLOR_BLANCHED_ALMOND          : extendedColorDataBaseRGB[COLOR_RGB_BLANCHED_ALMOND],
    COLOR_BLUE                     : extendedColorDataBaseRGB[COLOR_RGB_BLUE],
    COLOR_BLUE_VIOLET              : extendedColorDataBaseRGB[COLOR_RGB_BLUE_VIOLET],
    COLOR_BROWN                    : extendedColorDataBaseRGB[COLOR_RGB_BROWN],
    COLOR_BURLYWOOD                : extendedColorDataBaseRGB[COLOR_RGB_BURLYWOOD],
    COLOR_CADET_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_CADET_BLUE],
    COLOR_CHARTREUSE               : extendedColorDataBaseRGB[COLOR_RGB_CHARTREUSE],
    COLOR_CHOCOLATE                : extendedColorDataBaseRGB[COLOR_RGB_CHOCOLATE],
    COLOR_CORAL                    : extendedColorDataBaseRGB[COLOR_RGB_CORAL],
    COLOR_CORNFLOWER_BLUE          : extendedColorDataBaseRGB[COLOR_RGB_CORNFLOWER_BLUE],
    COLOR_CORNSILK                 : extendedColorDataBaseRGB[COLOR_RGB_CORNSILK],
    COLOR_CRIMSON                  : extendedColorDataBaseRGB[COLOR_RGB_CRIMSON],
    COLOR_CYAN                     : extendedColorDataBaseRGB[COLOR_RGB_CYAN],
    COLOR_DARK_BLUE                : extendedColorDataBaseRGB[COLOR_RGB_DARK_BLUE],
    COLOR_DARK_CYAN                : extendedColorDataBaseRGB[COLOR_RGB_DARK_CYAN],
    COLOR_DARK_GOLDENROD           : extendedColorDataBaseRGB[COLOR_RGB_DARK_GOLDENROD],
    COLOR_DARK_GRAY                : extendedColorDataBaseRGB[COLOR_RGB_DARK_GRAY],
    COLOR_DARK_GREEN               : extendedColorDataBaseRGB[COLOR_RGB_DARK_GREEN],
    COLOR_DARK_KHAKI               : extendedColorDataBaseRGB[COLOR_RGB_DARK_KHAKI],
    COLOR_DARK_MAGENTA             : extendedColorDataBaseRGB[COLOR_RGB_DARK_MAGENTA],
    COLOR_DARK_OLIVE_GREEN         : extendedColorDataBaseRGB[COLOR_RGB_DARK_OLIVE_GREEN],
    COLOR_DARK_ORANGE              : extendedColorDataBaseRGB[COLOR_RGB_DARK_ORANGE],
    COLOR_DARK_ORCHID              : extendedColorDataBaseRGB[COLOR_RGB_DARK_ORCHID],
    COLOR_DARK_RED                 : extendedColorDataBaseRGB[COLOR_RGB_DARK_RED],
    COLOR_DARK_SALMON              : extendedColorDataBaseRGB[COLOR_RGB_DARK_SALMON],
    COLOR_DARK_SEA_GREEN           : extendedColorDataBaseRGB[COLOR_RGB_DARK_SEA_GREEN],
    COLOR_DARK_SLATE_BLUE          : extendedColorDataBaseRGB[COLOR_RGB_DARK_SLATE_BLUE],
    COLOR_DARK_SLATE_GRAY          : extendedColorDataBaseRGB[COLOR_RGB_DARK_SLATE_GRAY],
    COLOR_DARK_TURQUOISE           : extendedColorDataBaseRGB[COLOR_RGB_DARK_TURQUOISE],
    COLOR_DARK_VIOLET              : extendedColorDataBaseRGB[COLOR_RGB_DARK_VIOLET],
    COLOR_DEEP_PINK                : extendedColorDataBaseRGB[COLOR_RGB_DEEP_PINK],
    COLOR_DEEP_SKY_BLUE            : extendedColorDataBaseRGB[COLOR_RGB_DEEP_SKY_BLUE],
    COLOR_DIM_GRAY                 : extendedColorDataBaseRGB[COLOR_RGB_DIM_GRAY],
    COLOR_DODGER_BLUE              : extendedColorDataBaseRGB[COLOR_RGB_DODGER_BLUE],
    COLOR_FIREBRICK                : extendedColorDataBaseRGB[COLOR_RGB_FIREBRICK],
    COLOR_FLORAL_WHITE             : extendedColorDataBaseRGB[COLOR_RGB_FLORAL_WHITE],
    COLOR_FOREST_GREEN             : extendedColorDataBaseRGB[COLOR_RGB_FOREST_GREEN],
    COLOR_GAINSBORO                : extendedColorDataBaseRGB[COLOR_RGB_GAINSBORO],
    COLOR_GHOST_WHITE              : extendedColorDataBaseRGB[COLOR_RGB_GHOST_WHITE],
    COLOR_GOLD                     : extendedColorDataBaseRGB[COLOR_RGB_GOLD],
    COLOR_GOLDENROD                : extendedColorDataBaseRGB[COLOR_RGB_GOLDENROD],
    COLOR_GRAY                     : extendedColorDataBaseRGB[COLOR_RGB_GRAY],
    COLOR_GREEN                    : extendedColorDataBaseRGB[COLOR_RGB_GREEN],
    COLOR_GREEN_YELLOW             : extendedColorDataBaseRGB[COLOR_RGB_GREEN_YELLOW],
    COLOR_HONEYDEW                 : extendedColorDataBaseRGB[COLOR_RGB_HONEYDEW],
    COLOR_HOT_PINK                 : extendedColorDataBaseRGB[COLOR_RGB_HOT_PINK],
    COLOR_INDIAN_RED               : extendedColorDataBaseRGB[COLOR_RGB_INDIAN_RED],
    COLOR_INDIGO                   : extendedColorDataBaseRGB[COLOR_RGB_INDIGO],
    COLOR_IVORY                    : extendedColorDataBaseRGB[COLOR_RGB_IVORY],
    COLOR_KHAKI                    : extendedColorDataBaseRGB[COLOR_RGB_KHAKI],
    COLOR_LAVENDER                 : extendedColorDataBaseRGB[COLOR_RGB_LAVENDER],
    COLOR_LAVENDER_BLUSH           : extendedColorDataBaseRGB[COLOR_RGB_LAVENDER_BLUSH],
    COLOR_LAWN_GREEN               : extendedColorDataBaseRGB[COLOR_RGB_LAWN_GREEN],
    COLOR_LEMON_CHIFFON            : extendedColorDataBaseRGB[COLOR_RGB_LEMON_CHIFFON],
    COLOR_LIGHT_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_BLUE],
    COLOR_LIGHT_CORAL              : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_CORAL],
    COLOR_LIGHT_CYAN               : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_CYAN],
    COLOR_LIGHT_GOLDENROD_YELLOW   : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_GOLDENROD_YELLOW],
    COLOR_LIGHT_GRAY               : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_GRAY],
    COLOR_LIGHT_GREEN              : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_GREEN],
    COLOR_LIGHT_PINK               : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_PINK],
    COLOR_LIGHT_SALMON             : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_SALMON],
    COLOR_LIGHT_SEA_GREEN          : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_SEA_GREEN],
    COLOR_LIGHT_SKY_BLUE           : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_SKY_BLUE],
    COLOR_LIGHT_SLATE_GRAY         : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_SLATE_GRAY],
    COLOR_LIGHT_STEEL_BLUE         : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_STEEL_BLUE],
    COLOR_LIGHT_STEEL_BLUE         : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_STEEL_BLUE],
    COLOR_LIGHT_YELLOW             : extendedColorDataBaseRGB[COLOR_RGB_LIGHT_YELLOW],
    COLOR_LIME_GREEN               : extendedColorDataBaseRGB[COLOR_RGB_LIME_GREEN],
    COLOR_LINEN                    : extendedColorDataBaseRGB[COLOR_RGB_LINEN],
    COLOR_MAGENTA                  : extendedColorDataBaseRGB[COLOR_RGB_MAGENTA],
    COLOR_MAROON                   : extendedColorDataBaseRGB[COLOR_RGB_MAROON],
    COLOR_MEDIUM_AQUAMARINE        : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_AQUAMARINE],
    COLOR_MEDIUM_BLUE              : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_BLUE],
    COLOR_MEDIUM_FOREST_GREEN      : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_FOREST_GREEN],
    COLOR_MEDIUM_GOLDENROD         : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_GOLDENROD],
    COLOR_MEDIUM_ORCHID            : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_ORCHID],
    COLOR_MEDIUM_PURPLE            : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_PURPLE],
    COLOR_MEDIUM_SEA_GREEN         : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_SEA_GREEN],
    COLOR_MEDIUM_SLATE_BLUE        : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_SLATE_BLUE],
    COLOR_MEDIUM_SPRING_GREEN      : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_SPRING_GREEN],
    COLOR_MEDIUM_TURQUOISE         : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_TURQUOISE],
    COLOR_MEDIUM_VIOLET_RED        : extendedColorDataBaseRGB[COLOR_RGB_MEDIUM_VIOLET_RED],
    COLOR_MIDNIGHT_BLUE            : extendedColorDataBaseRGB[COLOR_RGB_MIDNIGHT_BLUE],
    COLOR_MINT_CREAM               : extendedColorDataBaseRGB[COLOR_RGB_MINT_CREAM],
    COLOR_MISTY_ROSE               : extendedColorDataBaseRGB[COLOR_RGB_MISTY_ROSE],
    COLOR_MOCCASIN                 : extendedColorDataBaseRGB[COLOR_RGB_MOCCASIN],
    COLOR_NAVAJO_WHITE             : extendedColorDataBaseRGB[COLOR_RGB_NAVAJO_WHITE],
    COLOR_NAVY                     : extendedColorDataBaseRGB[COLOR_RGB_NAVY],
    COLOR_OLD_LACE                 : extendedColorDataBaseRGB[COLOR_RGB_OLD_LACE],
    COLOR_OLIVE                    : extendedColorDataBaseRGB[COLOR_RGB_OLIVE],
    COLOR_OLIVE_DRAB               : extendedColorDataBaseRGB[COLOR_RGB_OLIVE_DRAB],
    COLOR_ORANGE                   : extendedColorDataBaseRGB[COLOR_RGB_ORANGE],
    COLOR_ORANGE_RED               : extendedColorDataBaseRGB[COLOR_RGB_ORANGE_RED],
    COLOR_ORCHID                   : extendedColorDataBaseRGB[COLOR_RGB_ORCHID],
    COLOR_PALE_GOLDENROD           : extendedColorDataBaseRGB[COLOR_RGB_PALE_GOLDENROD],
    COLOR_PALE_GREEN               : extendedColorDataBaseRGB[COLOR_RGB_PALE_GREEN],
    COLOR_PALE_TURQUOISE           : extendedColorDataBaseRGB[COLOR_RGB_PALE_TURQUOISE],
    COLOR_PALE_VIOLET_RED          : extendedColorDataBaseRGB[COLOR_RGB_PALE_VIOLET_RED],
    COLOR_PAPAYA_WHIP              : extendedColorDataBaseRGB[COLOR_RGB_PAPAYA_WHIP],
    COLOR_PEACH_PUFF               : extendedColorDataBaseRGB[COLOR_RGB_PEACH_PUFF],
    COLOR_PERU                     : extendedColorDataBaseRGB[COLOR_RGB_PERU],
    COLOR_PINK                     : extendedColorDataBaseRGB[COLOR_RGB_PINK],
    COLOR_PLUM                     : extendedColorDataBaseRGB[COLOR_RGB_PLUM],
    COLOR_POWDER_BLUE              : extendedColorDataBaseRGB[COLOR_RGB_POWDER_BLUE],
    COLOR_PURPLE                   : extendedColorDataBaseRGB[COLOR_RGB_PURPLE],
    COLOR_RED                      : extendedColorDataBaseRGB[COLOR_RGB_RED],
    COLOR_ROSY_BROWN               : extendedColorDataBaseRGB[COLOR_RGB_ROSY_BROWN],
    COLOR_ROYAL_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_ROYAL_BLUE],
    COLOR_SADDLE_BROWN             : extendedColorDataBaseRGB[COLOR_RGB_SADDLE_BROWN],
    COLOR_SALMON                   : extendedColorDataBaseRGB[COLOR_RGB_SALMON],
    COLOR_SANDY_BROWN              : extendedColorDataBaseRGB[COLOR_RGB_SANDY_BROWN],
    COLOR_SEA_GREEN                : extendedColorDataBaseRGB[COLOR_RGB_SEA_GREEN],
    COLOR_SEA_SHELL                : extendedColorDataBaseRGB[COLOR_RGB_SEA_SHELL],
    COLOR_SIENNA                   : extendedColorDataBaseRGB[COLOR_RGB_SIENNA],
    COLOR_SILVER                   : extendedColorDataBaseRGB[COLOR_RGB_SILVER],
    COLOR_SKY_BLUE                 : extendedColorDataBaseRGB[COLOR_RGB_SKY_BLUE],
    COLOR_SLATE_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_SLATE_BLUE],
    COLOR_SLATE_GRAY               : extendedColorDataBaseRGB[COLOR_RGB_SLATE_GRAY],
    COLOR_SNOW                     : extendedColorDataBaseRGB[COLOR_RGB_SNOW],
    COLOR_SPRING_GREEN             : extendedColorDataBaseRGB[COLOR_RGB_SPRING_GREEN],
    COLOR_STEEL_BLUE               : extendedColorDataBaseRGB[COLOR_RGB_STEEL_BLUE],
    COLOR_TAN                      : extendedColorDataBaseRGB[COLOR_RGB_TAN],
    COLOR_TEAL                     : extendedColorDataBaseRGB[COLOR_RGB_TEAL],
    COLOR_THISTLE                  : extendedColorDataBaseRGB[COLOR_RGB_THISTLE],
    COLOR_TOMATO                   : extendedColorDataBaseRGB[COLOR_RGB_TOMATO],
    COLOR_TURQUOISE                : extendedColorDataBaseRGB[COLOR_RGB_TURQUOISE],
    COLOR_VIOLET                   : extendedColorDataBaseRGB[COLOR_RGB_VIOLET],
    COLOR_VIOLET_RED               : extendedColorDataBaseRGB[COLOR_RGB_VIOLET_RED],
    COLOR_WHEAT                    : extendedColorDataBaseRGB[COLOR_RGB_WHEAT],
    COLOR_WHITE                    : extendedColorDataBaseRGB[COLOR_RGB_WHITE],
    COLOR_WHITE_SMOKE              : extendedColorDataBaseRGB[COLOR_RGB_WHITE_SMOKE],
    COLOR_YELLOW                   : extendedColorDataBaseRGB[COLOR_RGB_YELLOW],
    COLOR_YELLOW_GREEN             : extendedColorDataBaseRGB[COLOR_RGB_YELLOW_GREEN]
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n wxPythonColorDataBaseRGB=%s' % str(
        wxPythonColorDataBaseRGB))
    debug_via_tsru(myDictionary=wxPythonColorDataBaseRGB)

#---------------------------------------------------------------------------

# Dictionary mapping the set of wxPython colors, guaranteed to be recognized,
# into the standard set of eight available curses colors.
#
# Note: This tabulation will not apply when the terminal type is
#       xterm-16color, xterm-88color or xterm-256color. Needless to say,
#       it will not apply when the terminal type is vt100 or xterm.
color8SubstitutionMap = {
    'name': 'color8SubstitutionMap',
    COLOR_AQUAMARINE: COLOR_CYAN,
    COLOR_BLACK: COLOR_BLACK,
    COLOR_BLUE: COLOR_BLUE,
    COLOR_BLUE_VIOLET: COLOR_BLUE,
    COLOR_BROWN: COLOR_YELLOW,
    COLOR_CADET_BLUE: COLOR_BLUE,
    COLOR_CORAL: COLOR_RED,
    COLOR_CORNFLOWER_BLUE: COLOR_BLUE,
    COLOR_CYAN: COLOR_CYAN,
    COLOR_DARK_GRAY: COLOR_BLACK,
    COLOR_DARK_GREEN: COLOR_GREEN,
    COLOR_DARK_OLIVE_GREEN: COLOR_GREEN,
    COLOR_DARK_ORCHID: COLOR_MAGENTA,
    COLOR_DARK_SLATE_BLUE: COLOR_BLUE,
    COLOR_DARK_SLATE_GRAY: COLOR_BLACK,
    COLOR_DARK_TURQUOISE: COLOR_CYAN,
    COLOR_DIM_GRAY: COLOR_BLACK,
    COLOR_FIREBRICK: COLOR_RED,
    COLOR_FOREST_GREEN: COLOR_GREEN,
    COLOR_GOLD: COLOR_YELLOW,
    COLOR_GOLDENROD: COLOR_YELLOW,
    COLOR_GRAY: COLOR_BLACK,
    COLOR_GREEN: COLOR_GREEN,
    COLOR_GREEN_YELLOW: COLOR_GREEN,
    COLOR_INDIAN_RED: COLOR_RED,
    COLOR_KHAKI: COLOR_YELLOW,
    COLOR_LIGHT_BLUE: COLOR_BLUE,
    COLOR_LIGHT_GRAY: COLOR_BLACK,
    COLOR_LIGHT_STEEL_BLUE: COLOR_BLUE,
    COLOR_LIME_GREEN: COLOR_GREEN,
    COLOR_MAGENTA: COLOR_MAGENTA,
    COLOR_MAROON: COLOR_RED,
    COLOR_MEDIUM_AQUAMARINE: COLOR_CYAN,
    COLOR_MEDIUM_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_FOREST_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_GOLDENROD: COLOR_YELLOW,
    COLOR_MEDIUM_ORCHID: COLOR_MAGENTA,
    COLOR_MEDIUM_SEA_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_SLATE_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_SPRING_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_TURQUOISE: COLOR_CYAN,
    COLOR_MEDIUM_VIOLET_RED: COLOR_RED,
    COLOR_MIDNIGHT_BLUE: COLOR_BLUE,
    COLOR_NAVY: COLOR_BLUE,
    COLOR_OLIVE: COLOR_GREEN,
    COLOR_ORANGE: COLOR_RED,
    COLOR_ORANGE_RED: COLOR_RED,
    COLOR_ORCHID: COLOR_MAGENTA,
    COLOR_PALE_GREEN: COLOR_GREEN,
    COLOR_PINK: COLOR_RED,
    COLOR_PLUM: COLOR_MAGENTA,
    COLOR_PURPLE: COLOR_RED,
    COLOR_RED: COLOR_RED,
    COLOR_SALMON: COLOR_RED,
    COLOR_SEA_GREEN: COLOR_GREEN,
    COLOR_SIENNA: COLOR_RED,
    COLOR_SILVER: COLOR_WHITE,
    COLOR_SKY_BLUE: COLOR_CYAN,
    COLOR_SLATE_BLUE: COLOR_BLUE,
    COLOR_SPRING_GREEN: COLOR_GREEN,
    COLOR_STEEL_BLUE: COLOR_BLUE,
    COLOR_TAN: COLOR_YELLOW,
    COLOR_TEAL: COLOR_CYAN,
    COLOR_THISTLE: COLOR_BLACK,
    COLOR_TURQUOISE: COLOR_CYAN,
    COLOR_VIOLET: COLOR_MAGENTA,
    COLOR_VIOLET_RED: COLOR_RED,
    COLOR_WHEAT: COLOR_YELLOW,
    COLOR_WHITE: COLOR_WHITE,
    COLOR_YELLOW: COLOR_YELLOW,
    COLOR_YELLOW_GREEN: COLOR_YELLOW
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n color8SubstitutionMap=%s' % str(
        color8SubstitutionMap))
    debug_via_tsru(myDictionary=color8SubstitutionMap)

#---------------------------------------------------------------------------

# Dictionary mapping the set of wxPython colors, guaranteed to be recognized,
# into the standard set of 16 available curses colors.
#
# Note: This tabulation will not apply when the terminal type is
#       xterm-8color. Needless to say, it will not apply when the terminal
#       type is ansi, vt100 or xterm.
color16SubstitutionMap = {
    'name': 'color16SubstitutionMap',
    COLOR_AQUAMARINE: COLOR_CYAN,
    COLOR_BLACK: COLOR_BLACK,
    COLOR_BLUE: COLOR_BLUE,
    COLOR_BLUE_VIOLET: COLOR_BLUE,
    COLOR_BROWN: COLOR_MAROON,
    COLOR_CADET_BLUE: COLOR_BLUE,
    COLOR_CORAL: COLOR_RED,
    COLOR_CORNFLOWER_BLUE: COLOR_BLUE,
    COLOR_CYAN: COLOR_CYAN,
    COLOR_DARK_GRAY: COLOR_BLACK,
    COLOR_DARK_GREEN: COLOR_GREEN,
    COLOR_DARK_OLIVE_GREEN: COLOR_GREEN,
    COLOR_DARK_ORCHID: COLOR_MAGENTA,
    COLOR_DARK_SLATE_BLUE: COLOR_BLUE,
    COLOR_DARK_SLATE_GRAY: COLOR_BLACK,
    COLOR_DARK_TURQUOISE: COLOR_CYAN,
    COLOR_DIM_GRAY: COLOR_GRAY,
    COLOR_FIREBRICK: COLOR_RED,
    COLOR_FOREST_GREEN: COLOR_GREEN,
    COLOR_GOLD: COLOR_YELLOW,
    COLOR_GOLDENROD: COLOR_YELLOW,
    COLOR_GRAY: COLOR_GRAY,
    COLOR_GREEN: COLOR_GREEN,
    COLOR_GREEN_YELLOW: COLOR_GREEN,
    COLOR_INDIAN_RED: COLOR_RED,
    COLOR_KHAKI: COLOR_YELLOW,
    COLOR_LIGHT_BLUE: COLOR_BLUE,
    COLOR_LIGHT_GRAY: COLOR_BLACK,
    COLOR_LIGHT_STEEL_BLUE: COLOR_BLUE,
    COLOR_LIME_GREEN: COLOR_LIME_GREEN,
    COLOR_MAGENTA: COLOR_MAGENTA,
    COLOR_MAROON: COLOR_MAROON,
    COLOR_MEDIUM_AQUAMARINE: COLOR_CYAN,
    COLOR_MEDIUM_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_FOREST_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_GOLDENROD: COLOR_YELLOW,
    COLOR_MEDIUM_ORCHID: COLOR_MAGENTA,
    COLOR_MEDIUM_SEA_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_SLATE_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_SPRING_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_TURQUOISE: COLOR_CYAN,
    COLOR_MEDIUM_VIOLET_RED: COLOR_RED,
    COLOR_MIDNIGHT_BLUE: COLOR_BLUE,
    COLOR_NAVY: COLOR_NAVY,
    COLOR_OLIVE: COLOR_OLIVE,
    COLOR_ORANGE: COLOR_RED,
    COLOR_ORANGE_RED: COLOR_RED,
    COLOR_ORCHID: COLOR_MAGENTA,
    COLOR_PALE_GREEN: COLOR_GREEN,
    COLOR_PINK: COLOR_RED,
    COLOR_PLUM: COLOR_MAGENTA,
    COLOR_PURPLE: COLOR_PURPLE,
    COLOR_RED: COLOR_RED,
    COLOR_SALMON: COLOR_RED,
    COLOR_SEA_GREEN: COLOR_GREEN,
    COLOR_SIENNA: COLOR_RED,
    COLOR_SILVER: COLOR_SILVER,
    COLOR_SKY_BLUE: COLOR_CYAN,
    COLOR_SLATE_BLUE: COLOR_BLUE,
    COLOR_SPRING_GREEN: COLOR_GREEN,
    COLOR_STEEL_BLUE: COLOR_BLUE,
    COLOR_TAN: COLOR_YELLOW,
    COLOR_TEAL: COLOR_TEAL,
    COLOR_THISTLE: COLOR_BLACK,
    COLOR_TURQUOISE: COLOR_CYAN,
    COLOR_VIOLET: COLOR_MAGENTA,
    COLOR_VIOLET_RED: COLOR_RED,
    COLOR_WHEAT: COLOR_YELLOW,
    COLOR_WHITE: COLOR_WHITE,
    COLOR_YELLOW: COLOR_YELLOW,
    COLOR_YELLOW_GREEN: COLOR_YELLOW
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n color16SubstitutionMap=%s' % str(
        color16SubstitutionMap))
    debug_via_tsru(myDictionary=color16SubstitutionMap)

#---------------------------------------------------------------------------

# Set of monochrome color numbers and names
# which curses guarantees to recognize.
cursesMonochromeNameFromCode = {
    'name': 'cursesMonochromeNameFromCode',
    0: COLOR_BLACK
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n cursesMonochromeNameFromCode=%s' % str(
        cursesMonochromeNameFromCode))
    debug_via_tsru(myDictionary=cursesMonochromeNameFromCode)

#---------------------------------------------------------------------------

# Set of monochrome color names and numbers
# which curses guarantees to recognize.
cursesMonochromeCodeFromName = {
    'name': 'cursesMonochromeCodeFromName',
    COLOR_BLACK: 0
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n cursesMonochromeCodeFromName=%s' % str(
        cursesMonochromeCodeFromName))
    debug_via_tsru(myDictionary=cursesMonochromeCodeFromName)

###---------------------------------------------------------------------------

### Set of color names and numbers
### which curses guarantees to recognize.
##curses8ColorCodeFromName = {
##    'name': 'curses8ColorCodeFromName',
##    COLOR_BLACK: 0,
##    COLOR_RED: 1,
##    COLOR_GREEN: 2,
##    COLOR_YELLOW: 3,
##    COLOR_BLUE: 4,
##    COLOR_MAGENTA: 5,
##    COLOR_CYAN: 6,
##    COLOR_WHITE: 7
##    }

###---------------------------------------------------------------------------

### Set of color numbers and names
### which curses guarantees to recognize.
##curses8ColorNameFromCode = {
##    'name': 'curses8ColorNameFromCode',
##    curses.COLOR_BLACK: COLOR_BLACK,
##    curses.COLOR_RED: COLOR_RED,
##    curses.COLOR_GREEN: COLOR_GREEN,
##    curses.COLOR_YELLOW: COLOR_YELLOW,
##    curses.COLOR_BLUE: COLOR_BLUE,
##    curses.COLOR_MAGENTA: COLOR_MAGENTA,
##    curses.COLOR_CYAN: COLOR_CYAN,
##    curses.COLOR_WHITE: COLOR_WHITE
##    }

###---------------------------------------------------------------------------

### Set of color numbers which wxPython emulator will recognize.
##COLOR8_NUMBER_BLACK = curses.COLOR_BLACK      # 0
##COLOR8_NUMBER_RED = curses.COLOR_RED          # 1
##COLOR8_NUMBER_GREEN = curses.COLOR_GREEN      # 2
##COLOR8_NUMBER_YELLOW = curses.COLOR_YELLOW    # 3
##COLOR8_NUMBER_BLUE = curses.COLOR_BLUE        # 4
##COLOR8_NUMBER_MAGENTA = curses.COLOR_MAGENTA  # 5
##COLOR8_NUMBER_CYAN = curses.COLOR_CYAN        # 6
##COLOR8_NUMBER_WHITE = curses.COLOR_WHITE      # 7

#---------------------------------------------------------------------------

xterm8ColorNameFromCode = {
    'name': 'xterm8ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8ColorNameFromCode=%s' % str(
        xterm8ColorNameFromCode))
    debug_via_tsru(myDictionary=xterm8ColorNameFromCode)

#---------------------------------------------------------------------------

xterm8ColorCodeFromName = {}
for colorCode in xterm8ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm8ColorCodeFromName['name'] = 'xterm8ColorCodeFromName'
    else:
        colorName = xterm8ColorNameFromCode[colorCode]
        xterm8ColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8ColorCodeFromName=%s' % str(
        xterm8ColorCodeFromName))
    debug_via_tsru(myDictionary=xterm8ColorCodeFromName)

#---------------------------------------------------------------------------

xterm8BuiltinColorNameFromCode = {
    'name': 'xterm8BuiltinColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8BuiltinColorNameFromCode=%s' % str(
        xterm8BuiltinColorNameFromCode))
    debug_via_tsru(myDictionary=xterm8BuiltinColorNameFromCode)

#---------------------------------------------------------------------------

xterm8BuiltinColorCodeFromName = {}
for colorCode in xterm8BuiltinColorNameFromCode.keys():
    if colorCode == 'name':
        xterm8ColorCodeFromName['name'] = 'xterm8BuiltinColorCodeFromName'
    else:
        colorName = xterm8BuiltinColorNameFromCode[colorCode]
        xterm8BuiltinColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8BuiltinColorCodeFromName=%s' % str(
        xterm8BuiltinColorCodeFromName))
    debug_via_tsru(myDictionary=xterm8BuiltinColorCodeFromName)

#---------------------------------------------------------------------------

##xterm16ColorNameFromCode = {
##    'name': 'xterm16ColorNameFromCode',
##    0: COLOR_BLACK,
##    1: COLOR_RED,
##    2: COLOR_GREEN,
##    3: COLOR_YELLOW,
##    4: COLOR_BLUE,
##    5: COLOR_MAGENTA,
##    6: COLOR_CYAN,
##    7: COLOR_WHITE,
##    8: COLOR_MAROON,
##    9: COLOR_OLIVE,
##    10: COLOR_NAVY,
##    11: COLOR_PURPLE,
##    12: COLOR_TEAL,
##    13: COLOR_SILVER,
##    14: COLOR_GRAY,
##    15: COLOR_LIME_GREEN
##    }

xterm16ColorNameFromCode = {
    'name': 'xterm16ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE,
    8: COLOR_GRAY,
    9: COLOR_MAROON,
    10: COLOR_LIME_GREEN,
    11: COLOR_OLIVE,
    12: COLOR_NAVY,
    13: COLOR_PURPLE,
    14: COLOR_TEAL,
    15: COLOR_SILVER
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16ColorNameFromCode=%s' % str(
        xterm16ColorNameFromCode))
    debug_via_tsru(myDictionary=xterm16ColorNameFromCode)

#---------------------------------------------------------------------------

xterm16ColorCodeFromName = {}
for colorCode in xterm16ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm16ColorCodeFromName['name'] = 'xterm16ColorCodeFromName'
    else:
        colorName = xterm16ColorNameFromCode[colorCode]
        xterm16ColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16ColorCodeFromName=%s' % str(
        xterm16ColorCodeFromName))
    debug_via_tsru(myDictionary=xterm16ColorCodeFromName)

#---------------------------------------------------------------------------

xterm16BuiltinColorNameFromCode = {
    'name': 'xterm16BuiltinColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE,
    8: COLOR_GRAY,
    9: COLOR_MAROON,
    10: COLOR_LIME_GREEN,
    11: COLOR_BROWN,
    12: COLOR_NAVY,
    13: COLOR_PURPLE,
    14: COLOR_TEAL,
    15: COLOR_SILVER
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16BuiltinColorNameFromCode=%s' % str(
        xterm16BuiltinColorNameFromCode))
    debug_via_tsru(myDictionary=xterm16BuiltinColorNameFromCode)

#---------------------------------------------------------------------------

xterm16BuiltinColorCodeFromName = {}
for colorCode in xterm16BuiltinColorNameFromCode.keys():
    if colorCode == 'name':
        xterm16ColorCodeFromName['name'] = 'xterm16BuiltinColorCodeFromName'
    else:
        colorName = xterm16BuiltinColorNameFromCode[colorCode]
        xterm16BuiltinColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16BuiltinColorCodeFromName=%s' % str(
        xterm16BuiltinColorCodeFromName))
    debug_via_tsru(myDictionary=xterm16BuiltinColorCodeFromName)

#---------------------------------------------------------------------------

xterm88ColorNameFromCode = {
    'name': 'xterm88ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE,
    8: COLOR_GRAY,
    9: COLOR_MAROON,
    10: COLOR_LIME_GREEN,
    11: COLOR_OLIVE,
    12: COLOR_NAVY,
    13: COLOR_PURPLE,
    14: COLOR_TEAL,
    15: COLOR_SILVER,
    16: COLOR_AQUAMARINE,
    17: COLOR_BLUE_VIOLET,
    18: COLOR_BROWN,
    19: COLOR_CADET_BLUE,
    20: COLOR_CORAL,
    21: COLOR_CORNFLOWER_BLUE,
    22: COLOR_DARK_GRAY,
    23: COLOR_DARK_GREEN,
    24: COLOR_DARK_OLIVE_GREEN,
    25: COLOR_DARK_ORCHID,
    26: COLOR_DARK_SLATE_BLUE,
    27: COLOR_DARK_SLATE_GRAY,
    28: COLOR_DARK_TURQUOISE,
    29: COLOR_DIM_GRAY,
    30: COLOR_FIREBRICK,
    31: COLOR_FOREST_GREEN,
    32: COLOR_GOLD,
    33: COLOR_GOLDENROD,
    34: COLOR_GREEN_YELLOW,
    35: COLOR_INDIAN_RED,
    36: COLOR_KHAKI,
    37: COLOR_LIGHT_BLUE,
    38: COLOR_LIGHT_GRAY,
    39: COLOR_LIGHT_STEEL_BLUE,
    40: COLOR_MEDIUM_AQUAMARINE,
    41: COLOR_MEDIUM_BLUE,
    42: COLOR_MEDIUM_FOREST_GREEN,
    43: COLOR_MEDIUM_GOLDENROD,
    44: COLOR_MEDIUM_ORCHID,
    45: COLOR_MEDIUM_SEA_GREEN,
    46: COLOR_MEDIUM_SLATE_BLUE,
    47: COLOR_MEDIUM_SPRING_GREEN,
    48: COLOR_MEDIUM_TURQUOISE,
    49: COLOR_MEDIUM_VIOLET_RED,
    50: COLOR_MIDNIGHT_BLUE,
    51: COLOR_ORANGE,
    52: COLOR_ORANGE_RED,
    53: COLOR_ORCHID,
    54: COLOR_PALE_GREEN,
    55: COLOR_PINK,
    56: COLOR_PLUM,
    57: COLOR_SALMON,
    58: COLOR_SEA_GREEN,
    59: COLOR_SIENNA,
    60: COLOR_SKY_BLUE,
    61: COLOR_SLATE_BLUE,
    62: COLOR_SPRING_GREEN,
    63: COLOR_STEEL_BLUE,
    64: COLOR_TAN,
    65: COLOR_THISTLE,
    66: COLOR_TURQUOISE,
    67: COLOR_VIOLET,
    68: COLOR_VIOLET_RED,
    69: COLOR_WHEAT,
    70: COLOR_YELLOW_GREEN
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm88ColorNameFromCode=%s' % str(
        xterm88ColorNameFromCode))
    debug_via_tsru(myDictionary=xterm88ColorNameFromCode)

#---------------------------------------------------------------------------

xterm88ColorCodeFromName = {}
for colorCode in xterm88ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm88ColorCodeFromName['name'] = 'xterm88ColorCodeFromName'
    else:
        colorName = xterm88ColorNameFromCode[colorCode]
        xterm88ColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm88ColorCodeFromName=%s' % str(
        xterm88ColorCodeFromName))
    debug_via_tsru(myDictionary=xterm88ColorCodeFromName)

#---------------------------------------------------------------------------

xterm256ColorNameFromCode = {
    'name': 'xterm256ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE,
    8: COLOR_GRAY,
    9: COLOR_MAROON,
    10: COLOR_LIME_GREEN,
    11: COLOR_OLIVE,
    12: COLOR_NAVY,
    13: COLOR_PURPLE,
    14: COLOR_TEAL,
    15: COLOR_SILVER,
    16: COLOR_AQUAMARINE,
    17: COLOR_BLUE_VIOLET,
    18: COLOR_BROWN,
    19: COLOR_CADET_BLUE,
    20: COLOR_CORAL,
    21: COLOR_CORNFLOWER_BLUE,
    22: COLOR_DARK_GRAY,
    23: COLOR_DARK_GREEN,
    24: COLOR_DARK_OLIVE_GREEN,
    25: COLOR_DARK_ORCHID,
    26: COLOR_DARK_SLATE_BLUE,
    27: COLOR_DARK_SLATE_GRAY,
    28: COLOR_DARK_TURQUOISE,
    29: COLOR_DIM_GRAY,
    30: COLOR_FIREBRICK,
    31: COLOR_FOREST_GREEN,
    32: COLOR_GOLD,
    33: COLOR_GOLDENROD,
    34: COLOR_GREEN_YELLOW,
    35: COLOR_INDIAN_RED,
    36: COLOR_KHAKI,
    37: COLOR_LIGHT_BLUE,
    38: COLOR_LIGHT_GRAY,
    39: COLOR_LIGHT_STEEL_BLUE,
    40: COLOR_MEDIUM_AQUAMARINE,
    41: COLOR_MEDIUM_BLUE,
    42: COLOR_MEDIUM_FOREST_GREEN,
    43: COLOR_MEDIUM_GOLDENROD,
    44: COLOR_MEDIUM_ORCHID,
    45: COLOR_MEDIUM_SEA_GREEN,
    46: COLOR_MEDIUM_SLATE_BLUE,
    47: COLOR_MEDIUM_SPRING_GREEN,
    48: COLOR_MEDIUM_TURQUOISE,
    49: COLOR_MEDIUM_VIOLET_RED,
    50: COLOR_MIDNIGHT_BLUE,
    51: COLOR_ORANGE,
    52: COLOR_ORANGE_RED,
    53: COLOR_ORCHID,
    54: COLOR_PALE_GREEN,
    55: COLOR_PINK,
    56: COLOR_PLUM,
    57: COLOR_SALMON,
    58: COLOR_SEA_GREEN,
    59: COLOR_SIENNA,
    60: COLOR_SKY_BLUE,
    61: COLOR_SLATE_BLUE,
    62: COLOR_SPRING_GREEN,
    63: COLOR_STEEL_BLUE,
    64: COLOR_TAN,
    65: COLOR_THISTLE,
    66: COLOR_TURQUOISE,
    67: COLOR_VIOLET,
    68: COLOR_VIOLET_RED,
    69: COLOR_WHEAT,
    70: COLOR_YELLOW_GREEN,
    71: COLOR_ALICE_BLUE,
    72: COLOR_ANTIQUE_WHITE,
    73: COLOR_AZURE,
    74: COLOR_BEIGE,
    75: COLOR_BISQUE,
    76: COLOR_BLANCHED_ALMOND,
    77: COLOR_BURLYWOOD,
    78: COLOR_CHARTREUSE,
    79: COLOR_CHOCOLATE,
    80: COLOR_CORNSILK,
    81: COLOR_CRIMSON,
    82: COLOR_DARK_BLUE,
    83: COLOR_DARK_CYAN,
    84: COLOR_DARK_GOLDENROD,
    85: COLOR_DARK_KHAKI,
    86: COLOR_DARK_MAGENTA,
    87: COLOR_DARK_ORANGE,
    88: COLOR_DARK_RED,
    89: COLOR_DARK_SALMON,
    90: COLOR_DARK_SEA_GREEN,
    91: COLOR_DARK_VIOLET,
    92: COLOR_DEEP_PINK,
    93: COLOR_DEEP_SKY_BLUE,
    94: COLOR_DODGER_BLUE,
    95: COLOR_FLORAL_WHITE,
    96: COLOR_GAINSBORO,
    97: COLOR_GHOST_WHITE,
    98: COLOR_HONEYDEW,
    99: COLOR_HOT_PINK,
    100: COLOR_INDIGO,
    101: COLOR_IVORY,
    102: COLOR_LAVENDER,
    103: COLOR_LAVENDER_BLUSH,
    104: COLOR_LAWN_GREEN,
    105: COLOR_LEMON_CHIFFON,
    106: COLOR_LIGHT_CORAL,
    107: COLOR_LIGHT_CYAN,
    108: COLOR_LIGHT_GOLDENROD_YELLOW,
    109: COLOR_LIGHT_GREEN,
    110: COLOR_LIGHT_PINK,
    111: COLOR_LIGHT_SALMON,
    112: COLOR_LIGHT_SEA_GREEN,
    113: COLOR_LIGHT_SKY_BLUE,
    114: COLOR_LIGHT_SLATE_GRAY,
    115: COLOR_LIGHT_YELLOW,
    116: COLOR_LINEN,
    117: COLOR_MEDIUM_PURPLE,
    118: COLOR_MINT_CREAM,
    119: COLOR_MISTY_ROSE,
    120: COLOR_MOCCASIN,
    121: COLOR_NAVAJO_WHITE,
    122: COLOR_OLD_LACE,
    123: COLOR_OLIVE_DRAB,
    124: COLOR_PALE_GOLDENROD,
    125: COLOR_PALE_TURQUOISE,
    126: COLOR_PALE_VIOLET_RED,
    127: COLOR_PAPAYA_WHIP,
    128: COLOR_PEACH_PUFF,
    129: COLOR_PERU,
    130: COLOR_POWDER_BLUE,
    131: COLOR_ROSY_BROWN,
    132: COLOR_ROYAL_BLUE,
    133: COLOR_SADDLE_BROWN,
    134: COLOR_SANDY_BROWN,
    135: COLOR_SEA_SHELL,
    136: COLOR_SLATE_GRAY,
    137: COLOR_SNOW,
    138: COLOR_TOMATO,
    139: COLOR_WHITE_SMOKE
    }

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm256ColorNameFromCode=%s' % str(
        xterm256ColorNameFromCode))
    debug_via_tsru(myDictionary=xterm256ColorNameFromCode)

#---------------------------------------------------------------------------

xterm256ColorCodeFromName = {}
for colorCode in xterm256ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm256ColorCodeFromName['name'] = 'xterm256ColorCodeFromName'
    else:
        colorName = xterm256ColorNameFromCode[colorCode]
        xterm256ColorCodeFromName[colorName] = colorCode

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm256ColorCodeFromName=%s' % str(
        xterm256ColorCodeFromName))
    debug_via_tsru(myDictionary=xterm256ColorCodeFromName)

#---------------------------------------------------------------------------

class PrivateLogger(object):
    '''
    The PrivateLogger class.

    It should only be needed when this module is itself the main program.
    It will not be needed when tsApplication establishes a fully funtional
    logger.
    '''

    # The following defines sverity levels which may be used as
    # a threshold filter for console output.
    NOTSET        = 0
    DEBUG         = 10
    INFO          = 20
    NOTICE        = INFO + 5
    WARNING       = 30
    ALERT         = WARNING + 5
    ERROR         = 40
    CRITICAL      = 50
    EMERGENCY     = CRITICAL + 5

    # The following defines a pseudo level which may be used to add stack
    # backtrace to console output.
    DEBUG_TRACE_LEVEL = DEBUG - 5

    # The following defines a pseudo level which may be used to surpress
    # console output.
    PRIVATE       = CRITICAL + 10
    PRIVATENAME   = 'PRIVATE'

    LOG_PATH      = "./"
    LOG_NAME      = "message"
    LOG_EXTENSION = ".log"
    APPEND        = "a"
    TRUNCATE      = "w"
    DEFAULT_LOG_FILE_MODE = TRUNCATE

    threshold = {NOTSET: NOTSET,
                 DEBUG: DEBUG,
                 INFO: INFO,
                 NOTICE: NOTICE,
                 WARNING: WARNING,
                 ALERT: ALERT,
                 ERROR: ERROR,
                 CRITICAL: CRITICAL,
                 EMERGENCY: EMERGENCY,
                 PRIVATE: PRIVATE}

    category = {NOTSET: 'NOTSET',
                DEBUG: 'DEBUG',
                INFO: 'INFO',
                NOTICE: 'NOTICE',
                WARNING: 'WARNING',
                ALERT: 'ALERT',
                ERROR: 'ERROR',
                CRITICAL: 'CRITICAL',
                EMERGENCY: 'EMERGENCY',
                PRIVATE: 'PRIVATE'}

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        '''
        self.theThreshold = DEBUG
        timestamp = tsru.getDateTimeString(time.time(), msec=True)
        ts_logFile = '%s/%s' % (
            tsLogger.TsLogger.defaultStandardOutputPath,
            defaultLogFileName)
        self.theFile = open(ts_logFile, defaultLogFileMode, 0)
        self.theFile.write('%s - %s\n' % (
            timestamp, 'Started logging to file "%s"' % ts_logFile))

        self.theFile.flush()

    #-----------------------------------------------------------------------

    def alert(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ALERT'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.ALERT, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def critical(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
 
        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.CRITICAL, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def debug(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.DEBUG, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def emergency(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'EMERGENCY'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
 
        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.EMERGENCY, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def error(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.ERROR, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def exception(self, msg, *args):
        '''
        Convenience method for logging an ERROR with exception information.
        '''
        self.error(*(msg,) + args, **{'exc_info': 1})

    #-----------------------------------------------------------------------

    def info(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'INFO'.
 
        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.INFO, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def _log(self, level, msg, args, exc_info = None, extra = None):
        '''
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        '''
        if self.theThreshold <= level:
            timestamp = tsru.getDateTimeString(time.time(), msec = True)

            record = '%s %9.9s: %s' % (timestamp,
                                       PrivateLogger.category[level],
                                       msg)
            self._output(record, level = level)

    #-----------------------------------------------------------------------

    def log(self, level, msg, *args, **kwargs):
        '''
        Log 'msg % args' with the integer severity 'level'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
 
        logger.log(level, "We have a %s", "mysterious problem", exc_info = 1)
        '''
        if not isinstance(level, int):
            raise tse.ProgramException(tse.ARGUMENT_TYPE_NOT_VALID,
                                       'Expected=%s; Actual=%s.' % \
                                       (int, type(level)))

        if level >= self.theThreshold:
            self._log(*(level, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def notice(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'NOTICE'.
 
        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.NOTICE, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def warning(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.WARNING, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def _output(self, text, level = NOTSET, newline = True):
        '''
        Output message to console and/or file.
        '''
        if newline:
            message = text + '\n'
        else:
            message = text

        if PrivateLogger.NOTSET < level and \
           level >= self.theThreshold and \
           level < PrivateLogger.PRIVATE:
            if level >= PrivateLogger.WARNING:
                # Send to stderr
                sys.stderr.write(message)
            else:
                # Send to stdout
                sys.stdout.write(message)

        if PrivateLogger.NOTSET < level and \
           level >= self.theThreshold and \
           level <= PrivateLogger.PRIVATE:
            if self.theFile is not None:
                # Send to file
                self.theFile.write(message)
                self.theFile.flush()

#---------------------------------------------------------------------------

class GraphicalTextUserInterface(object):
    '''
    Class uses the Standard Python Curses API to initialize, manage and
    shutdown input (from a keyboard and mouse) and output (to a two-
    dimensional display screen).
    '''
    #-----------------------------------------------------------------------
    # Class Variables
    OperationsShutdown = True
    TopLevelApplication = None

    # Setup un-initialized state for curses.
    BackgroundColor = None
    BuiltinPaletteRGB = None
    CanChangeColor = None
    ColorDataBase = None
    ColorDataBaseID = None
    ColorDataBasePairID = None
    ColorSubstitutionDataBase = None
    CursesColorPairs = None
    CursesColors = None
    CursesPanels = None
    ForegroundColor = None
    HasColors = None
    HasDisplay = None
    HasKeyboard = None
    HasLogger = None
    HasMouse = None
    HostOS = hostOS
    LongName = None
    Mmask = None
    MouseButtonCodes = None
    PythonVersion =pythonVersion
    Stdscr = None
    StdscrGeometry = None
    StdscrGeometryPixels = None
    TermName = None

    CursesDataBase = None

    #-----------------------------------------------------------------------

    # Setup un-initialized state for wxPython.
    KeyboardInputRecipients = {}
    KeyboardInputRecipients['name'] = 'KeyboardInputRecipients'
    KeyboardInputRecipients['lifoList'] = []

    TopLevelWindows = {}
    TopLevelWindows['name'] = 'TopLevelWindows'

    WindowHandles = {}
    WindowHandles['name'] = 'WindowHandles'

    TheWindows = {}
    TheWindows['name'] = 'TheWindows'
    TheWindows['windowIndex'] = -1

    WindowsByAssignedId = {}
    WindowsByAssignedId['name'] = 'WindowsByAssignedId'

    WindowsByHandle = {}
    WindowsByHandle['name'] = 'WindowsByHandle'

    WindowsById = {}
    WindowsById['name'] = 'WindowsById'

    WindowsByName = {}
    WindowsByName['name'] = 'WindowsByName'

##    WindowsByPad = {}
##    WindowsByPad['name'] = 'WindowsByPad'

    WindowsByPanelLayer = {}
    WindowsByPanelLayer['name'] = 'WindowsByPanelLayer'

    WindowsByShowOrder = {}
    WindowsByShowOrder['name'] = 'WindowsByShowOrder'
    WindowsByShowOrder['OrderOfShow'] = []
    WindowsByShowOrder['OrderOfShowPanelStack'] = []
    WindowsByShowOrder['PanelLayer'] = []

    WindowsByShowOrder['PanelStack'] = {}
    WindowsByShowOrder['PanelStack'][
        'name'] = 'PanelStack'
 
    WindowsByShowOrder['AssignedIdByPanelLayer'] = {}
    WindowsByShowOrder['AssignedIdByPanelLayer'][
        'name'] = 'AssignedIdByPanelLayer'

    WindowTopLevelAncestors = {}
    WindowTopLevelAncestors['name'] = 'WindowTopLevelAncestors'

    WindowTopLevelTasks = []

    AcceleratorKeysByEarliestAssignedId = {}
    AcceleratorKeysByEarliestAssignedId[
        'name'] = 'AcceleratorKeysByEarliestAssignedId'

    AcceleratorTableByAssignedId = {}
    AcceleratorTableByAssignedId[
        'name'] = 'AcceleratorTableByAssignedId'

    EventAssociationsByEarliestAssignedId = {}
    EventAssociationsByEarliestAssignedId[
        'name'] = 'EventAssociationsByEarliestAssignedId'

    WindowDataBase = None

    #-----------------------------------------------------------------------

    def __init__(self, theCallerClass, **kw):
        '''
        Initialize Curses and publish related information.
        '''
        theClass = 'GraphicalTextUserInterface'
 
        if GraphicalTextUserInterface.OperationsShutdown:

            self.runningChildren = []
            signal.signal(signal.SIGINT, self._sigIntHandler)
            signal.signal(signal.SIGABRT, self._sigAbrtHandler)

            # Initialize curses
            self.ClassName = theClass
            self.thisown = None
            self.theCanvas = None

            GraphicalTextUserInterface.BackgroundColor = None
            GraphicalTextUserInterface.BuiltinPaletteRGB = None
            GraphicalTextUserInterface.CanChangeColor = False
            GraphicalTextUserInterface.ColorDataBase = None
            GraphicalTextUserInterface.ColorDataBaseID = None
            GraphicalTextUserInterface.ColorDataBasePairID = None
            GraphicalTextUserInterface.ColorDataBaseRGB = None
            GraphicalTextUserInterface.ColorSubstitutionDataBase = None
            GraphicalTextUserInterface.CursesColorPairs = None
            GraphicalTextUserInterface.CursesColors = None
            GraphicalTextUserInterface.CursesPanels = None
            GraphicalTextUserInterface.ForegroundColor = None
            GraphicalTextUserInterface.HasColors = False
            GraphicalTextUserInterface.HasDisplay = False
            GraphicalTextUserInterface.HasKeyboard = False
            GraphicalTextUserInterface.HasLogger = False
            GraphicalTextUserInterface.HasMouse = False
            GraphicalTextUserInterface.LongName = None
            GraphicalTextUserInterface.Mmask = None
            GraphicalTextUserInterface.MouseButtonCodes = None
            GraphicalTextUserInterface.Stdscr = None
            GraphicalTextUserInterface.StdscrGeometry = None
            GraphicalTextUserInterface.StdscrGeometryPixels = None
            GraphicalTextUserInterface.TermName = None

            try:
                self.logger = tsLogger.TsLogger(
                    threshold=tsLogger.DEBUG,
                    start=time.time(),
                    name=tsLogger.StandardOutputFile)
                self.ts_has_logger = True
                GraphicalTextUserInterface.HasLogger = self.ts_has_logger
            except Exception, e:
                try:
                    self.logger = PrivateLogger()
                    self.ts_has_logger = True
                    GraphicalTextUserInterface.HasLogger = self.ts_has_logger
                except Exception, e:
                    self.ts_has_logger = False
                    GraphicalTextUserInterface.HasLogger = self.ts_has_logger
                    msg = '%s.__init__ Logger not available: %s' % \
                          (__title__, str(e))
                    raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            self.logger.debug(
                'Begin %s (0x%X) for %s.' % (
                    theClass, id(self), theCallerClass))

##            if DEBUG:
##                myOutputPath = os.path.join(
##                    tsLogger.TsLogger.defaultStandardOutputPath,
##                    'PlatformRunTimeEnvironment.log')
##                myRunTimeEnvironment = PlatformRunTimeEnvironment()
##                myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

            self.tsSetDefaultClientTerminalDataBase()

            try:

                self.start()

            except Exception, startError:

                abortMsg = '  Abort %s (0x%X) for %s; Exception: %s' % (
                    theClass, id(self), theCallerClass, startError)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, abortMsg)

            self.logger.debug(
                'End %s (0x%X) for %s.' % (
                    theClass, id(self), theCallerClass))

        else:
            pass

    #-----------------------------------------------------------------------

    def tsBuildSplashScreen(self):
        '''
        Build the SplashScreen to fit available screen.

        1. Traditional (Color SVGA) application SplashScreens:
           (1024 x 768 pixel) / (128 columns x 64 rows)
           include a Trademark, Copyright and License.

        2. Traditional (Color VGA) application SplashScreens:
           (640 x 480 pixel) / (80 columns x 40 rows)
           include a Copyright and License.

        3. Traditional (Non-Color VT100) application SplashScreens:
           (640 x 300 pixel) / (80 columns x 25 rows)
           include a Copyright and License.

        4. Barely usable application SplashScreens:
           (480 x 192 pixels) / (60 columns x 16 rows)
           include a brief Notice that identifies external text files.
        '''

        (stdscrY, stdscrX) = self.ts_stdscr.getbegyx()
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'stdscrY=%d; stdscrX=%d' % (
                stdscrY, stdscrX))
        (stdscrHeight, stdscrWidth) = self.ts_stdscr.getmaxyx()
        currentX = stdscrX
        currentY = stdscrY
        availableWidth = stdscrWidth
        availableHeight = stdscrHeight
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'availableWidth=%d; availableHeight=%d' % (
                availableWidth, availableHeight))


        splashScreenTrademark = []
        linesTrademark = theSplashScreenTrademark.split('\n')
        maxTrademarkWidth = 0
        maxTrademarkHeight = 0
        for aLine in linesTrademark:
            maxTrademarkWidth = max(
                maxTrademarkWidth, len(aLine))
            maxTrademarkHeight += 1
            splashScreenTrademark += [aLine]
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxTrademarkWidth=%d; maxTrademarkHeight=%d' % (
                maxTrademarkWidth, maxTrademarkHeight))

        splashScreenCopyright = []
        linesCopyright = theSplashScreenCopyright.split('\n')
        maxCopyrightWidth = 0
        maxCopyrightHeight = 0
        for aLine in linesCopyright:
            maxCopyrightWidth = max(
                maxCopyrightWidth, len(aLine))
            maxCopyrightHeight += 1
            splashScreenCopyright += [aLine]
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxCopyrightWidth=%d; maxCopyrightHeight=%d' % (
                maxCopyrightWidth, maxCopyrightHeight))

        splashScreenLicense = []
        linesLicense = theSplashScreenLicense.split('\n')
        maxLicenseWidth = 0
        maxLicenseHeight = 0
        for aLine in linesLicense:
            maxLicenseWidth = max(
                maxLicenseWidth, len(aLine))
            maxLicenseHeight += 1
            splashScreenLicense += [aLine]
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxLicenseWidth=%d; maxLicenseHeight=%d' % (
                maxLicenseWidth, maxLicenseHeight))

        splashScreenNotices = []
        linesNotices = theSplashScreenNotices.split('\n')
        maxNoticesWidth = 0
        maxNoticesHeight = 0
        for aLine in linesNotices:
            maxNoticesWidth = max(
                maxNoticesWidth, len(aLine))
            maxNoticesHeight += 1
            splashScreenNotices += [aLine]
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxNoticesWidth=%d; maxNoticesHeight=%d' % (
                maxNoticesWidth, maxNoticesHeight))
        #
        # if (space becomes ample at 60 cols x 47 rows):
        #    1. trademark
        #    2. copyright
        #    3. license
        #
        # elif space becomes usable at 60 cols x 35 rows:
        #    1. copyright
        #    2. license
        #
        # elif space becomes marginal at 60 cols x 14 rows:
        #    1. See "Notice.txt" file...
        #
        # else space becomes unusable below 60 cols x 14 rows:
        #    1. Report and trap operator configuration error

        maxHeight = (maxTrademarkHeight + \
                     maxCopyrightHeight + \
                     maxLicenseHeight)

        maxWidth = max(maxTrademarkWidth,
                       maxCopyrightWidth,
                       maxLicenseWidth)

        if ((availableWidth >= maxWidth) and \
            (availableHeight >= maxHeight)):

            isAmpleSpace = True
            isUsableSpace = False
            isMinimalSpace = False
            isUnusableSpace = False

        else:

            isAmpleSpace = False

            maxHeight = (maxCopyrightHeight + \
                         maxLicenseHeight)

            maxWidth = max(maxCopyrightWidth,
                           maxLicenseWidth)

            if ((availableWidth >= maxWidth) and \
                (availableHeight >= maxHeight)):

                isUsableSpace = True
                isMinimalSpace = False
                isUnusableSpace = False

            else:

                isUsableSpace = False

                maxHeight = maxNoticesHeight

                maxWidth = maxNoticesWidth

                if ((availableWidth >= maxWidth) and \
                    (availableHeight >= maxHeight)):

                    isMinimalSpace = True
                    isUnusableSpace = False

                else:

                    isMinimalSpace = False
                    isUnusableSpace = True

        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxWidth=%d; maxHeight=%d' % (
                maxWidth, maxHeight))

        fmt1 = 'tsBuildSplashScreen: ' + \
            'isAmpleSpace (%s); ' % str(isAmpleSpace)
        fmt2 = 'isUsableSpace (%s); ' % str(isUsableSpace)
        fmt3 = 'isMinimalSpace (%s); ' % str(isMinimalSpace)
        fmt4 = 'isUnusableSpace (%s)' % str(isUnusableSpace)
        msg = fmt1 + fmt2 + fmt3 + fmt4
        self.logger.debug(msg)

        horizontalMargin = (stdscrWidth - maxWidth) // 2
        verticalMargin = (stdscrHeight - maxHeight) // 2

        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'horizontalMargin=%d; verticalMargin=%d' % (
                horizontalMargin, verticalMargin))

        nlines = maxHeight
        ncols = maxWidth
        begin_y = max(0, verticalMargin  - 1)
        begin_x = max(0, horizontalMargin - 1)
##      win = curses.newwin(nlines, ncols, begin_y, begin_x)
        win = curses.newwin(maxHeight,
                            maxWidth,
                            verticalMargin,
                            horizontalMargin)
##      pad = curses.newpad(100, 100)

        if isAmpleSpace:

            self.logger.debug(
                'tsBuildSplashScreen: ' + \
                'maxWidth=%d; maxHeight=%d' % (
                    maxWidth, maxHeight))

            currentX = 0
            currentY = 0
            availableWidth = maxWidth
            availableHeight = maxHeight

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                theTrademarkForegroundColour, theTrademarkBackgroundColour)
            for currentText in linesTrademark:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            currentY += 0

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                theCopyrightForegroundColour, theCopyrightBackgroundColour)
            for currentText in linesCopyright:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            currentY += 0

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                thLicenseForegroundColour, thLicenseBackgroundColour)
            for currentText in linesLicense:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            win.refresh()

##          pminrow = 0
##          pmincol = 0
##          sminrow = pminrow + 1
##          smincol = pmincol + 1
##          smaxrow = availableHeight - 1
##          smaxcol = availableWidth - 1
##          pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

        elif isUsableSpace:

            self.logger.debug(
                'tsBuildSplashScreen: ' + \
                'maxWidth=%d; maxHeight=%d' % (
                    maxWidth, maxHeight))

            currentX = stdscrX
            currentY = stdscrY
            availableWidth = stdscrWidth
            availableHeight = stdscrHeight

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                theCopyrightForegroundColour, theCopyrightBackgroundColour)
            for currentText in linesCopyright:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            currentY += 0

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                thLicenseForegroundColour, thLicenseBackgroundColour)
            for currentText in linesLicense:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            win.refresh()
##          pminrow = 0
##          pmincol = 0
##          sminrow = pminrow + 1
##          smincol = pmincol + 1
##          smaxrow = availableHeight - 1
##          smaxcol = availableWidth - 1
##          pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

        elif isMinimalSpace:

            self.logger.debug(
                'tsBuildSplashScreen: ' + \
                'maxWidth=%d; maxHeight=%d' % (
                    maxWidth, maxHeight))

            currentX = stdscrX
            currentY = stdscrY
            availableWidth = stdscrWidth
            availableHeight = stdscrHeight

            attr = DISPLAY_BOLD | self.tsGetAttributeValueFromColorPair(
                theNoticesForegroundColour, theNoticesBackgroundColour)
            for currentText in linesNotices:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            win.refresh()
##          pminrow = 0
##          pmincol = 0
##          sminrow = pminrow + 1
##          smincol = pmincol + 1
##          smaxrow = availableHeight - 1
##          smaxcol = availableWidth - 1
##          pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

        else:

            self.logger.debug(
                'tsBuildSplashScreen: ' + \
                'maxWidth=%d; maxHeight=%d' % (
                    maxWidth, maxHeight))

            currentX = stdscrX
            currentY = stdscrY
            availableWidth = stdscrWidth
            availableHeight = stdscrHeight

            attr = DISPLAY_REVERSE | self.tsGetAttributeValueFromColorPair(
                theNoticesForegroundColour, theNoticesBackgroundColour)
            for currentText in linesNotices:
                fill = ' ' * (maxWidth - len(currentText) - 1)
                win.addstr(currentY,
                           currentX,
                           '%s%s' % (currentText, fill),
                           attr)
##              pad.addstr(currentY,
##                         currentX,
##                         '%s%s' % (currentText, fill),
##                         attr)
                currentY += 1

            win.refresh()
##          pminrow = 0
##          pmincol = 0
##          sminrow = pminrow + 1
##          smincol = pmincol + 1
##          smaxrow = availableHeight - 1
##          smaxcol = availableWidth - 1
##          pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

        if theSplashScreenMakeReusable:

            platformSuffix = '-[%dx%d_%s]-%s.bmp' % (
                stdscrWidth,
                stdscrHeight,
                self.ts_termname.upper(),
                platform.system().lower())

            splashScreenFileName = os.path.join(
                theSplashScreenPath,
                theSplashScreenFileName)

            bitmapImageFileName = splashScreenFileName.replace(
                '.bmp', platformSuffix)

            try:

                bitmapImageFileID = open(bitmapImageFileName, mode='w+b')

                win.putwin(bitmapImageFileID)
        ##          pad.putwin(bitmapImageFileID)
                bitmapImageFileID.close()

            except Exception, errorCode:

                fmt1 = 'tsBuildSplashScreen: '
                fmt2 = 'bitmapImageFileName (%s); ' % str(bitmapImageFileName)
                fmt3 = 'errorCode (%s); ' % str(errorCode)
                msg = fmt1 + fmt2 + fmt3
                self.logger.warning(msg)

##                raise tse.UserInterfaceException(
##                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def tsGetSetToUseForColorCodeFromName(self):
        '''
        Return the set_to_use appropriate for the current terminal
        emulator. Stripped of its dictionary name to faciliate the
        determination of the number of colors, the set_to_use can be
        used to return the color code number associated with the
        specified color name.
        '''
        if self.ts_has_colors:

            if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorCodeFromName)

                    set_to_use_name = 'xterm8ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm8BuiltinColorCodeFromName'

            elif self.ts_curses_colors == 16:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorCodeFromName)

                    set_to_use_name = 'xterm16ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm16BuiltinColorCodeFromName'

            elif (self.ts_termname =='xterm-88color') or \
                 (self.ts_curses_colors == 88):

                set_to_use = self.tsStripDictionaryName(
                    xterm88ColorCodeFromName)

                set_to_use_name = 'xterm88ColorCodeFromName'

            elif (self.ts_termname =='xterm-256color') or \
                 (self.ts_curses_colors == 256):

                # Though self.ts_curses_colors == 256, there is only
                # capacity to define and mix 181 colors.
                set_to_use = self.tsStripDictionaryName(
                    xterm256ColorCodeFromName)

                set_to_use_name = 'xterm256ColorCodeFromName'

            else:

                fmt1 = 'tsGetSetToUseForColorCodeFromName '
                fmt2 = '(unexpected configuration): \n'
                fmt3 = '\t has_colors=%s \n' % self.ts_has_colors
                fmt4 = '\t can_change_color=%s \n' % self.can_change_color
                fmt5 = '\t curses_colors=%s' % self.ts_curses_colors
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                self.logger.error(msg)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        else:

            set_to_use = self.tsStripDictionaryName(
                    cursesMonochromeCodeFromName)

            set_to_use_name = 'cursesMonochromeCodeFromName'

        fmt1 = 'tsGetSetToUseForColorCodeFromName: \n'
        fmt2 = '\t has_colors=%s \n' % self.ts_has_colors
        fmt3 = '\t can_change_color=%s \n' % self.can_change_color
        fmt4 = '\t curses_colors=%s \n' % self.ts_curses_colors
        fmt5 = '\t set_to_use_name=%s' % set_to_use_name
        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
        self.logger.alert(msg)

        return (set_to_use)

    #-----------------------------------------------------------------------

    def tsGetSetToUseForColorNameFromCode(self):
        '''
        Return the set_to_use appropriate for the current terminal
        emulator. Stripped of its dictionary name to faciliate the
        determination of the number of colors, the set_to_use can be
        used to return the color name associated with the specified
        color code number.
        '''
        if self.ts_has_colors:

            if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorNameFromCode)

                    set_to_use_name = 'xterm8ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm8BuiltinColorNameFromCode'

            elif self.ts_curses_colors == 16:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorNameFromCode)

                    set_to_use_name = 'xterm16ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm16BuiltinColorNameFromCode'

            elif (self.ts_termname == 'xterm-88color') or \
                 (self.ts_curses_colors == 88):

                set_to_use = self.tsStripDictionaryName(
                    xterm88ColorNameFromCode)

                set_to_use_name = 'xterm88ColorNameFromCode'

            elif (self.ts_termname == 'xterm-256color') or \
                 (self.ts_curses_colors == 256):

                # Though self.ts_curses_colors == 256, there is only
                # capacity to define and mix 181 colors.
                set_to_use = self.tsStripDictionaryName(
                    xterm256ColorNameFromCode)

                set_to_use_name = 'xterm256ColorNameFromCode'

            else:

                fmt1 = 'tsGetSetToUseForColorNameFromCode '
                fmt2 = '(unexpected configuration): \n'
                fmt3 = '\t has_colors=%s \n' % self.ts_has_colors
                fmt4 = '\t can_change_color=%s \n' % self.can_change_color
                fmt5 = '\t curses_colors=%s' % self.ts_curses_colors
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                self.logger.error(msg)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        else:

            set_to_use = self.tsStripDictionaryName(
                    cursesMonochromeNameFromCode)

            set_to_use_name = 'cursesMonochromeNameFromCode'

        fmt1 = 'tsGetSetToUseForColorNameFromCode: \n'
        fmt2 = '\t has_colors=%s \n' % self.ts_has_colors
        fmt3 = '\t can_change_color=%s \n' % self.can_change_color
        fmt4 = '\t curses_colors=%s \n' % self.ts_curses_colors
        fmt5 = '\t set_to_use_name=%s' % set_to_use_name
        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
        self.logger.alert(msg)
 
        return (set_to_use)

    #-----------------------------------------------------------------------

    def tsGetTopLevelApplication(self):
        '''
        Return the class instance of the Top Level Application GUI object.
        '''
        return (GraphicalTextUserInterface.TopLevelApplication)

    #-----------------------------------------------------------------------

    def tsSetTopLevelApplication(self, theApplication):
        '''
        Set the class instance of the Top Level Application GUI object.
        '''
        GraphicalTextUserInterface.TopLevelApplication = theApplication

    #-----------------------------------------------------------------------

    def tsSetDefaultClientTerminalDataBase(self):
        '''
        Enter the terminal-independent features of the client dictionary.
        '''
        pass

    #-----------------------------------------------------------------------

    def tsSetDetectedClientTerminalDataBase(
        self,
        background=None,
        builtin_palette=None,
        can_change_color=None,
        curses_color_pairs=None,
        curses_colors=None,
        curses_panels=None,
        foreground=None,
        geometry=None,
        geometryPixels=None,
        has_colors=False,
        has_default_colors=False,
        has_display=False,
        has_keyboard=False,
        has_logger=False,
        has_mouse=False,
        longname=EmptyString,
        mmask=0,
        mouseButtonCodes=None,
        stdscr=None,
        termname=EmptyString):
        '''
        Enter the terminal-specific features of the client dictionary.
        '''
        GraphicalTextUserInterface.BackgroundColor = background
        GraphicalTextUserInterface.BuiltinPaletteRGB = builtin_palette
        GraphicalTextUserInterface.CanChangeColor = can_change_color
        GraphicalTextUserInterface.CursesColorPairs = curses_color_pairs
        GraphicalTextUserInterface.CursesColors = curses_colors
        GraphicalTextUserInterface.CursesPanels = curses_panels
        GraphicalTextUserInterface.ForegroundColor = foreground
        GraphicalTextUserInterface.HasColors = has_colors
        GraphicalTextUserInterface.HasDefaultColors = has_default_colors
        GraphicalTextUserInterface.HasDisplay = has_display
        GraphicalTextUserInterface.HasKeyboard = has_keyboard
        GraphicalTextUserInterface.HasLogger = has_logger
        GraphicalTextUserInterface.HasMouse = has_mouse
        GraphicalTextUserInterface.LongName = longname
        GraphicalTextUserInterface.Mmask = mmask
        GraphicalTextUserInterface.MouseButtonCodes = mouseButtonCodes
        GraphicalTextUserInterface.Stdscr = stdscr
        GraphicalTextUserInterface.StdscrGeometry = geometry
        GraphicalTextUserInterface.StdscrGeometryPixels = geometryPixels
        GraphicalTextUserInterface.TermName = termname

        self.tsPrintDataBases()

    #-----------------------------------------------------------------------

    def start(self):
        '''
        Initialize the curses keyboard, display and optional mouse.
        '''
        try:
            self.logger.debug('  Begin Curses Start.')

            # Start the standard screen.
            self.ts_stdscr = self.initscr()

            self.stdscr = self.ts_stdscr
            self.logger.debug(
                '    stdscr = %s' % self.ts_stdscr)

            self.ts_has_display = True
            self.ts_has_keyboard = True
            self.ts_curses_panels = {}
            self.ts_curses_panels['name'] = 'CursesPanels'

            # Get Screen Geometry
            try:

                (stdscrY, stdscrX) = self.ts_stdscr.getbegyx()
                (stdscrHeight, stdscrWidth) = self.ts_stdscr.getmaxyx()

            except AttributeError:

                (stdscrY, stdscrX) = (0, 0)
                (stdscrHeight, stdscrWidth) = (0, 0)

            if True:
                self.ts_stdscrGeometry = wxRect(
                    stdscrX, stdscrY, stdscrWidth, stdscrHeight)
            else:
                self.ts_stdscrGeometry = (
                    stdscrX, stdscrY, stdscrWidth, stdscrHeight)


            self.logger.debug(
                '    stdscrGeometry = %s' % str(self.ts_stdscrGeometry))

            if True:
                self.ts_stdscrGeometryPixels = wxRect(
                    stdscrX * pixelWidthPerCharacter,
                    stdscrY * pixelHeightPerCharacter,
                    stdscrWidth * pixelWidthPerCharacter,
                    stdscrHeight * pixelHeightPerCharacter)
            else:
                self.ts_stdscrGeometryPixels = (
                    stdscrX * pixelWidthPerCharacter,
                    stdscrY * pixelHeightPerCharacter,
                    stdscrWidth * pixelWidthPerCharacter,
                    stdscrHeight * pixelHeightPerCharacter)

            self.logger.debug(
                '    stdscrGeometryPixels = %s' % str(
                    self.ts_stdscrGeometryPixels))

            self.ts_termname = self.termname()

            self.logger.debug(
                '    termname = %s' % self.ts_termname)

            self.ts_longname = self.longname()

            self.logger.debug(
                '    longname = %s' % self.ts_longname)

            if self.ts_termname not in supportedTermCaps:

                msg = 'Begin Curses Stop.'
                self.logger.debug('    %s' % msg)
                self.echo()
                self.nocbreak()
                self.noraw()

                try:

                    self.ts_stdscr.keypad(0)

                except Exception, e:

                    msg = 'Pre-Python 2.6 keypad(0) failure: %s.' % str(e)
                    self.logger.warning('     %s' % msg)
##                self.echo()
 
                ## self.ts_curs_set(1)
                try:

                    self.endwin()
                    GraphicalTextUserInterface.OperationsShutdown = True
                    msg = 'End Curses Stop.'


                except _curses.error:

                    msg = 'Unexpected endwin failure.'

                self.logger.debug('     %s' % msg)
 
                self.tsExitForTerminalNotSupported(self.ts_termname)

            if self.ts_termname in BlackOnWhiteDefault:
                self.ts_foreground = COLOR_BLACK
                self.ts_background = COLOR_WHITE
            else:
                self.ts_foreground = COLOR_WHITE
                self.ts_background = COLOR_BLACK

            self.logger.debug(
                '    foreground = %s' % self.ts_foreground)

            self.logger.debug(
                '    background = %s' % self.ts_background)

            try:
                # Sets the mouse events to be reported, and returns a tuple
                # (availmask, oldmask). availmask indicates which of the
                # specified mouse events can be reported; on complete failure
                # it returns 0. oldmask is the previous value of the given
                # window's mouse event mask. If this function is never called,
                # no mouse events are ever reported.
                (availmask, oldmask) = self.mousemask(
                    curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
                self.ts_mmask = availmask
            except Exception, e:
                self.ts_mmask = 0

            self.logger.debug(
                '    mmask = %s' % str(self.ts_mmask))

            if self.ts_mmask == 0:
                self.ts_has_mouse = False
            else:
                self.ts_has_mouse = True
            self.ts_MouseButtonCodes = self.tsSetMouseButtonCodes(
                self.ts_has_mouse)

            self.logger.debug(
                '    has_mouse = %s' % self.ts_has_mouse)

            self.logger.debug(
                '    MouseButtonCodes = %s' % str(self.ts_MouseButtonCodes))

            self.ts_has_colors = self.has_colors()

            self.logger.debug(
                '    has_colors = %s' % self.ts_has_colors)

            if self.ts_has_colors:

                # Initialize eight basic colors (black, red, green, yellow,
                # blue, magenta, cyan, and white), and two global variables
                # in the curses module, COLORS and COLOR_PAIRS, containing
                # the maximum number of colors and color-pairs the terminal
                # can support. It also restores the colors on the terminal to
                # the values they had when the terminal was just turned on.
                self.start_color()

                self.ts_builtin_palette = {}
                self.ts_builtin_palette['name'] = 'BuiltinPaletteRGB'
                self.can_change_color = self.can_change_color()
                self.ts_curses_color_pairs = curses.COLOR_PAIRS
                self.ts_curses_colors = curses.COLORS
                maxCursesScale =1000
                maxColorScale = 255

                if True:
                    for i in range(0, curses.COLORS):
                        (r, g, b) = curses.color_content(i)
                        (red, green, blue) = (
                            int((int(r) * maxColorScale) // maxCursesScale),
                            int((int(g) * maxColorScale) // maxCursesScale),
                            int((int(b) * maxColorScale) // maxCursesScale))
                        colorHEX = ((red << 16) + \
                                    (green << 8) + \
                                    (blue))
                        colorRGB = '(%3d, %3d, %3d)' % (red, green, blue)
                        self.logger.alert(
                            'start: i=%3d; content=0x%6.6X=%s' % (
                            i,
                            colorHEX,
                            colorRGB))

                self.logger.debug(
                    '    curses_colors = %d' % self.ts_curses_colors)

                self.logger.debug(
                    '    curses_color_pairs = %d' % \
                    self.ts_curses_color_pairs)

                self.logger.debug(
                    '    can_change_color = %s' % \
                    self.can_change_color)

                set_to_use = self.tsGetSetToUseForColorNameFromCode()

                if self.ts_curses_colors < len(set_to_use):

                    fmt1 = 'start in %s:'  % __title__
                    fmt2 = 'Too few colors %d < %d.' % (
                        self.ts_curses_colors,
                        len(set_to_use))
                    msg = '%s %s' % (fmt1, fmt2)
                    self.logger.error('   %s' % msg)
                    raise tse.UserInterfaceException(
                        tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

                elif  self.can_change_color and \
                      self.ts_curses_colors == 256:

                    # Can change the 256 colors.
                    # Color Codes for standard 16 color set are correct.
                    # Color Pairs, limited to 32767, produce wrong colors
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                elif self.can_change_color and \
                     self.ts_curses_colors == 88:

                    # Can change the 88 colors.
                    # Color Codes for standard 16 color set are correct.
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                elif self.can_change_color and \
                     self.ts_curses_colors == 16:

                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                elif self.can_change_color and \
                     self.ts_curses_colors == 8:

                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                elif self.ts_curses_colors == 16:

                    # Cannot change color so must presume that
                    # self.ts_curses_colors == len(
                    #     xterm16ColorCodeFromName)

                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change color so must presume that
                    # self.ts_curses_colors == len(
                    #     xterm8ColorCodeFromName)

                    self.ts_has_default_colors = True
                    self.tsInstallDefaultColorDataBase()

            else:

                self.tsInstallMonochromeDataBase()

            set_to_use = self.tsGetSetToUseForColorNameFromCode()
            self.ts_max_colors = min(
                self.ts_curses_colors, len(set_to_use))
            self.ts_max_color_pairs = min(
                self.ts_curses_color_pairs, self.ts_max_colors**2)

            # Record the User Terminal Information
            self.tsSetDetectedClientTerminalDataBase(
                background=self.ts_background,
                builtin_palette=self.ts_builtin_palette,
                can_change_color=self.can_change_color,
##                curses_color_pairs=self.ts_curses_color_pairs,
##                curses_colors=self.ts_curses_colors,
                curses_color_pairs=self.ts_max_color_pairs,
                curses_colors=self.ts_max_colors,
                curses_panels=self.ts_curses_panels,
                foreground=self.ts_foreground,
                geometry=self.ts_stdscrGeometry,
                geometryPixels=self.ts_stdscrGeometryPixels,
                has_colors=self.ts_has_colors,
                has_default_colors=self.ts_has_default_colors,
                has_display=self.ts_has_display,
                has_keyboard=self.ts_has_keyboard,
                has_logger=self.ts_has_logger,
                has_mouse=self.ts_has_mouse,
                longname=self.ts_longname,
                mmask=self.ts_mmask,
                mouseButtonCodes=self.ts_MouseButtonCodes,
                stdscr=self.ts_stdscr,
                termname=self.ts_termname)

            # Turn off echoing of keys, and enter cbreak mode,
            # where no buffering is performed on keyboard input
            self.noecho()
            self.raw()
            self.cbreak()

            # Terminals usually return special keys, such as the cursor keys
            # or navigation keys such as Page Up and Home, as a multibyte
            # escape sequence. While you could write your application to
            # expect such sequences and process them accordingly, curses can
            # do it for you, returning a special value such as
            # curses.KEY_LEFT. To get curses to do the job, you have
            # to enable keypad mode.
            try:
                self.ts_stdscr.keypad(1)
            except Exception, e:
                msg = 'start: Pre-Python 2.6 keypad(1) failure: %s.' % str(e)
                self.logger.warning('     %s' % msg)
            ## self.meta(1)
            self.halfdelay(10) # use set_input_timeouts to adjust
            # In keypad mode, escape sequences for special keys
            # (like the cursor keys) will be interpreted and
            # a special value like curses.KEY_LEFT will be returned
            self.ts_stdscr.keypad(1)
            ## stdscr.keypad(0)
            self.ts_stdscr.scrollok(0)
            msg = 'End Curses Start.'
            self.logger.debug('  %s' % msg)
            GraphicalTextUserInterface.OperationsShutdown = False

            # def_program_mode must be invoked after def_shell_mode
            # self.def_program_mode()

        except _curses.error:
            GraphicalTextUserInterface.OperationsShutdown = True
            msg = 'Abort Curses Start.'
            self.logger.debug('  %s' % msg)
            self.stop()
            sys.exit(1)

        if theSplashScreenEnabled and theSplashScreenMakeReusable:

            try:

                currentDirectory = os.getcwd()

                fmt1 = 'start: wxThemeToUse: '
                fmt2 = 'currentDirectory=%s; ' % currentDirectory
                fmt3 = 'theSplashScreenPath=%s; ' % theSplashScreenPath
                fmt4 = 'theSplashScreenFileName=%s' % theSplashScreenFileName
                msg = fmt1 + fmt2 + fmt3 + fmt4
                self.logger.notice(msg)

            except Exception, themeErrorCode:

                currentDirectory = os.getcwd()

                fmt1 = 'start: wxThemeToUse: '
                fmt2 = 'themeErrorCode=%s' % str(themeErrorCode)
                msg = fmt1 + fmt2
                self.logger.error(msg)

            try:

                # (stdscrY, stdscrX) = self.ts_stdscr.getbegyx()
                # (stdscrHeight, stdscrWidth) = self.ts_stdscr.getmaxyx()
                bitmapX = stdscrX
                bitmapY = stdscrY
                bitmapWidth = stdscrWidth
                bitmapHeight = stdscrHeight

                platformSuffix = '-[%dx%d_%s]-%s.bmp' % (
                    bitmapWidth,
                    bitmapHeight,
                    self.ts_termname.upper(),
                    platform.system().lower())

                self.logger.notice(
                    'start: platformSuffix=%s' % platformSuffix)

                if False:

                    # Use Relative Path
                    splashScreenFileName = theSplashScreenPath + \
                                           theSplashScreenFileName

                else:

                    #Use Absolute Path
                    splashScreenFileName = os.path.join(
                        theSplashScreenPath,
                        theSplashScreenFileName)

                bitmapImageFileName = splashScreenFileName.replace(
                    '.bmp', platformSuffix)

                self.logger.notice(
                    'start: bitmapImageFileName=%s' % bitmapImageFileName)

                mode = 'rb'

                bitmap = open(bitmapImageFileName, mode)

                bitmapID = curses.getwin(bitmap)
                self.logger.debug('type(bitmapID)=%s' % type(
                    bitmapID))

                bitmapID.refresh()
                bitmap.close()

                time.sleep(theSplashScreenShowSeconds)

            except IOError, ioErrorCode:

                bitmap = None
                self.logger.debug('Splash Screen File IOError: %s' % str(
                    ioErrorCode))

                self.tsBuildSplashScreen()

                time.sleep(theSplashScreenShowSeconds)

            except curses.error, splashScreenErrorCode:

                bitmap.close()
                self.logger.error('Splash Screen GetWin Error: %s' % str(
                    splashScreenErrorCode))

            except Exception, otherErrorCode:

##                (stdscrY, stdscrX) = self.ts_stdscr.getbegyx()
##                (stdscrHeight, stdscrWidth) = self.ts_stdscr.getmaxyx()
##                availableWidth = stdscrWidth
##                availableHeight = stdscrHeight

##                pminrow = stdscrY
##                pmincol = stdscrX
##                sminrow = pminrow + 1
##                smincol = pmincol + 1
##                smaxrow = availableHeight - 1
##                smaxcol = availableWidth - 1
##                pad = bitmapID
##                pad.refresh(
##                    pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)
##                pad.close()

##                time.sleep(theSplashScreenShowSeconds)

                bitmap.close()
                self.logger.error('Splash Screen Other Error: %s' % str(
                    otherErrorCode))

        elif theSplashScreenEnabled:

            self.tsBuildSplashScreen()

            time.sleep(theSplashScreenShowSeconds)

        # Erase Splash Screen
        self.ts_stdscr.erase()
        self.ts_stdscr.refresh()
        curses.doupdate()

    #-----------------------------------------------------------------------
 
    def stop(self):
        '''
        Restore the screen to its previouse command line interface mode
        state.
        '''
        if not GraphicalTextUserInterface.OperationsShutdown:
            self.logger.debug('  Begin Curses Stop.')
            self.echo()
            self.nocbreak()
            self.noraw()
            try:
                self.ts_stdscr.keypad(0)
            except Exception, e:
                self.logger.warning(
                    '     Pre-Python 2.6 keypad(0) failure: %s.' % str(e))
##            self.echo()

            ## self.ts_curs_set(1)
            try:
                self.reset_shell_mode()
                self.endwin()
                self.ts_has_display = False
                self.ts_has_keyboard = False
            except _curses.error:
                # don't block original error with curses error
                self.logger.debug(
                    '   Curses Error (%s).' % str(_curses.error))

            GraphicalTextUserInterface.BackgroundColor = None
            GraphicalTextUserInterface.CanChangeColor = False
            GraphicalTextUserInterface.ColorDataBase = None
            GraphicalTextUserInterface.ColorDataBaseID = None
            GraphicalTextUserInterface.ColorDataBasePairID = None
            GraphicalTextUserInterface.ColorDataBaseRGB = None
            GraphicalTextUserInterface.ColorSubstitutionDataBase = None
            GraphicalTextUserInterface.CursesColorPairs = None
            GraphicalTextUserInterface.CursesColors = None
            GraphicalTextUserInterface.ForegroundColor = None
            GraphicalTextUserInterface.HasColors = False
            GraphicalTextUserInterface.HasDisplay = self.ts_has_display
            GraphicalTextUserInterface.HasKeyboard = self.ts_has_keyboard
            GraphicalTextUserInterface.HasLogger = False
            GraphicalTextUserInterface.HasMouse = False
            GraphicalTextUserInterface.LongName = None
            GraphicalTextUserInterface.Mmask = None
            GraphicalTextUserInterface.MouseButtonCodes = None
            GraphicalTextUserInterface.Stdscr = None
            GraphicalTextUserInterface.StdscrGeometry = None
            GraphicalTextUserInterface.StdscrGeometryPixels = None
            GraphicalTextUserInterface.TermName = None
            GraphicalTextUserInterface.OperationsShutdown = True

            mySysCommands = TsSysCommands()
            command = 'stty sane'
            msg = mySysCommands.tsGetStatusOutput(command)
            self.logger.debug('%s: %s' % (command, str(msg)))
            command = 'clear'
            msg = mySysCommands.tsGetStatusOutput(command)
            self.logger.debug('%s: %s' % (command, str(msg)))
 
        self.logger.debug('  End Curses Stop.')

    #-----------------------------------------------------------------------

    def runWrapper(self, mainProgram):
        '''
        Calls mainProgram in fullscreen mode.  Returns to normal on exit.

        This method should be called to wrap the main program loop of
        an application.
 
        Exception tracebacks are displayed in normal mode.
        '''
        try:
            self.logger.debug('Begin Curses Wrapper.')
            self.start()
            self.logger.debug('  Begin Main Program from Wrapper.')
            return mainProgram()

        finally:
            self.logger.debug('  End Main Program from Wrapper.')
            self.stop()
            self.logger.debug('End Curses Wrapper.')

    #-----------------------------------------------------------------------

    def tsBuildCursesDataBase(self):
        '''
        Build the curses database for toolkit and application debugging.
        '''
        stuff = {
            'BackgroundColor': \
            GraphicalTextUserInterface.BackgroundColor,

            'BuiltinPaletteRGB': \
            GraphicalTextUserInterface.BuiltinPaletteRGB,

            'CanChangeColor': \
            GraphicalTextUserInterface.CanChangeColor,

            'ColorDataBase': \
            GraphicalTextUserInterface.ColorDataBase,

            'ColorDataBaseID': \
            GraphicalTextUserInterface.ColorDataBaseID,

            'ColorDataBasePairID': \
            GraphicalTextUserInterface.ColorDataBasePairID,

            'ColorDataBaseRGB': \
            GraphicalTextUserInterface.ColorDataBaseRGB,

            'ColorSubstitutionDataBase': \
            GraphicalTextUserInterface.ColorSubstitutionDataBase,

            'CursesColorPairs': \
            GraphicalTextUserInterface.CursesColorPairs,

            'CursesColors': \
            GraphicalTextUserInterface.CursesColors,

            'CursesPanels': \
            GraphicalTextUserInterface.CursesPanels,

            'ForegroundColor': \
            GraphicalTextUserInterface.ForegroundColor,

            'HasColors': \
            GraphicalTextUserInterface.HasColors,

            'HasDisplay': \
            GraphicalTextUserInterface.HasDisplay,

            'HasKeyboard' : \
            GraphicalTextUserInterface.HasKeyboard,

            'HasLogger': \
            GraphicalTextUserInterface.HasLogger,

            'HasMouse': \
            GraphicalTextUserInterface.HasMouse,

            'HostOS': \
            GraphicalTextUserInterface.HostOS,

            'LongName': \
            GraphicalTextUserInterface.LongName,

            'Mmask': \
            GraphicalTextUserInterface.Mmask,

            'MouseButtonCodes': \
            GraphicalTextUserInterface.MouseButtonCodes,

            'PythonVersion': \
            GraphicalTextUserInterface.PythonVersion,

            'Stdscr': \
            GraphicalTextUserInterface.Stdscr,

            'StdscrGeometry': \
            GraphicalTextUserInterface.StdscrGeometry,

            'StdscrGeometryPixels': \
            GraphicalTextUserInterface.StdscrGeometryPixels,

            'TermName': \
            GraphicalTextUserInterface.TermName,

            'name': \
            'CursesDataBase'
        }

        return (stuff)

    #-----------------------------------------------------------------------

    def tsBuildWindowDataBase(self):
        '''
        Build the emulated wxPython database for toolkit and application
        debugging.
        '''
        stuff = {
            'KeyboardInputRecipients':
            GraphicalTextUserInterface.KeyboardInputRecipients,

            'TopLevelWindows': \
            GraphicalTextUserInterface.TopLevelWindows,

            'WindowHandles': \
            GraphicalTextUserInterface.WindowHandles,

            'TheWindows': \
            GraphicalTextUserInterface.TheWindows,

            'WindowTopLevelAncestors': \
            GraphicalTextUserInterface.WindowTopLevelAncestors,

            'WindowTopLevelTasks': \
            GraphicalTextUserInterface.WindowTopLevelTasks,

            'AcceleratorKeysByEarliestAssignedId': \
            GraphicalTextUserInterface.AcceleratorKeysByEarliestAssignedId,

            'AcceleratorTableByAssignedId': \
            GraphicalTextUserInterface.AcceleratorTableByAssignedId,

            'EventAssociationsByEarliestAssignedId': \
            GraphicalTextUserInterface.EventAssociationsByEarliestAssignedId,

            'WindowsByAssignedId': \
            GraphicalTextUserInterface.WindowsByAssignedId,

            'WindowsByHandle': \
            GraphicalTextUserInterface.WindowsByHandle,

            'WindowsById': \
            GraphicalTextUserInterface.WindowsById,

            'WindowsByName': \
            GraphicalTextUserInterface.WindowsByName,

##            'WindowsByPad': \
##            GraphicalTextUserInterface.WindowsByPad,

            'WindowsByPanelLayer': \
            GraphicalTextUserInterface.WindowsByPanelLayer,

            'WindowsByShowOrder': \
            GraphicalTextUserInterface.WindowsByShowOrder,

            'name': \
            'WindowDataBase'
        }

        return (stuff)

    #-----------------------------------------------------------------------

    def tsInfoConsole(self, infoMsg, indent=0):
        '''
        Output message to the standard output console.
        '''
        if indent > 0:
            sys.stdout.write('\n%s INFO:%s' % (' ' * indent, infoMsg))
        else:
            sys.stdout.write('\n INFO:%s' % infoMsg)

    #-----------------------------------------------------------------------

    def tsErrorConsole(self, errorMsg, indent=0):
        '''
        Output message to the standard error console.
        '''
        if indent > 0:
            sys.stderr.write('\n%sERROR:%s' % (' ' * indent, errorMsg))
        else:
            sys.stderr.write('\nERROR:%s' % errorMsg)

    #-----------------------------------------------------------------------

    def tsPrintWindow(self,
                     window,
                     row,
                     col,
                     printMsg,
                     attrib=None,
                     EnableClearToEndOfLine=False):
        '''
        Output message to window.
        '''
        if EnableClearToEndOfLine:
            window.clrtoeol()

        if attrib is None:
            window.addstr(row, col, printMsg)
        else:
            window.attron(attrib)
            window.addstr(row, col, printMsg)
            window.attroff(attrib)

    #-----------------------------------------------------------------------

    def tsExitForTerminalNotSupported(self, termname):
        '''
        Simulate Program Exception handling when the runMain
        method is neither monitoring nor controlling class
        initialization.
        '''
        # UserInterfaceException. GRAPHICAL_WINDOW_NOT_VALID
        exitStatus = 143

        self.stop()

        for text in __header__.split('\n'):
            sys.stderr.write('\n%s' % text)

        exitMsg1 = 'User Interface Exception: '
        exitMsg2 = 'Graphical Window Not valid. '
        exitMsg3 = '(ExitCode #%d)' % int(exitStatus)
        sys.stderr.write('\n%s%s%s' % (exitMsg1, exitMsg2, exitMsg3))

        fmt = '  The "%s" terminal is not supported.'
        exitMsg4 = fmt % termname
        sys.stderr.write('\n\n%s' % exitMsg4)

        fmt = '  Terminal choices include: %s. '
        exitMsg5 = fmt % supportedTermCaps
        sys.stderr.write('\n%s' % exitMsg5)

        exitMsg6 = '  Please replace the "%s" terminal.' % termname
        sys.stderr.write('\n\n%s\n' % exitMsg6)

        sys.stderr.write('\n%s%s%s\n' % (exitMsg1, exitMsg2, exitMsg3))
        sys.exit(exitStatus)

    #-----------------------------------------------------------------------

    def tsStripDictionaryName(self, inputDictionary):
        '''
        Return a copy of the specified dictionary, without its name
        annotation, so that its size (derived from len(dictionary)) reflects
        the number of color codes/names (curses or emulated wxPython)
        available to the toolkit and application with the current terminal
        emulator.
        '''
        outputDictionary = {}
        for theEntry in list(inputDictionary.keys()):
            if theEntry == 'name':
                # Exclude dictionary name annotation from output
                pass
            else:
                # Include color code/name in output
                outputDictionary[theEntry] = inputDictionary[theEntry]

        return (outputDictionary)

    #-----------------------------------------------------------------------

    def tsCreateColorPairs(self):
        '''
        Activate available foreground and background color combinations.
        '''

        try:
            if self.ts_has_colors:

                set_to_use = self.tsGetSetToUseForColorNameFromCode()

                pair_number = -1
                for foreground_code in sorted(list(set_to_use.keys())):
                    foreground_name = set_to_use[foreground_code]

                    fg_number = foreground_code

                    for background_code in sorted(list(set_to_use.keys())):
                        background_name = set_to_use[background_code]

                        bg_number = background_code

                        pair_number += 1

                        if pair_number == 0:

                            # The 0 color pair is wired to white on black
                            # and cannot be changed.
                            self.init_pair(pair_number, fg_number, bg_number)

                        else:

                            # Changes the definition of a color-pair. It takes
                            # three arguments: the number of the color-pair to
                            # be changed, the foreground color number, and the
                            # background color number. The value of pair_number
                            # must be between 1 and COLOR_PAIRS - 1
                            # (the 0 color pair is wired to white on black
                            # and cannot be changed). The value of fg and bg
                            # arguments must be between 0 and COLORS.
                            # If the color-pair was previously initialized,
                            # the screen is refreshed and all occurrences of
                            # that color-pair are changed to the new
                            # definition.
                            self.init_pair(pair_number, fg_number, bg_number)

            else:
                # Identifier (0-63) = <forground id (0-7)><background id (0-7)>
                set_to_use = self.tsStripDictionaryName(
                        cursesMonochromeCodeFromName)

        except Exception, e:

            msg = 'tsCreateColorPairs failure: %s.' % str(e)
            self.logger.error('     %s' % msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def tsGetColorPairNumber(self, foreground, background):
        '''
        Encode foreground and background color into the associated
        curses color pair number.
        '''
        if self.ts_has_colors:

            if self.ts_curses_colors == 8:

                # ColorSubstitutionDataBase does exist
                foregroundMap = color8SubstitutionMap[foreground]
                backgroundMap = color8SubstitutionMap[background]

            elif self.ts_curses_colors == 16:

                # ColorSubstitutionDataBase does exist
                foregroundMap = color16SubstitutionMap[foreground]
                backgroundMap = color16SubstitutionMap[background]

            elif self.ts_curses_colors == 88:

                # ColorSubstitutionDataBase does NOT exist
                foregroundMap = foreground
                backgroundMap = background

            elif self.ts_curses_colors == 256:

                # ColorSubstitutionDataBase does NOT exist
                foregroundMap = foreground
                backgroundMap = background

            else:

                # ColorSubstitutionDataBase does not exist
                foregroundMap = 1 # foreground
                backgroundMap = 0 # background

            # Support xterm, xterm-color, xterm-16color
            # xterm-88color and xterm-256color terminal emulators.
            set_to_use = self.tsGetSetToUseForColorCodeFromName()
            available_colors = len(list(set_to_use.keys()))

            try:

                fg = set_to_use[foregroundMap.lower()]
                bg = set_to_use[backgroundMap.lower()]

            except Exception, e:

                self.logger.error(
                    'Exception (tsGetColorPairNumber): %s' % str(e))

                if self.ts_termname in BlackOnWhiteDefault:
                    fg = set_to_use[COLOR_BLACK]
                    bg = set_to_use[COLOR_WHITE]
                else:
                    fg = set_to_use[COLOR_WHITE]
                    bg = set_to_use[COLOR_BLACK]

            pair_number = GraphicalTextUserInterface.ColorDataBasePairID[
                'PairNumbersFromColorNumbers'][(fg, bg)]

        else:

            # Support vt100 (monochrome) type terminals.
            foregroundMap = foreground
            backgroundMap = background

            fg = -1
            bg = 0
            pair_number = 0

        if True or (DEBUG and VERBOSE):
            msg1 = 'tsGetColorPairNumber: ' + \
                   'Foreground "%s" -> "%d"' % (foregroundMap, fg)
            msg2 = 'Background "%s" -> "%d"' % (backgroundMap, bg)
            msg3 = msg1 + msg2
            msg4 = 'Color pair found: %d; %s.' % (pair_number,
                                                  msg3)
            self.logger.debug(msg4)

        return (pair_number)

    #-----------------------------------------------------------------------

    def tsGetAttributeValueFromColorPair(self, foreground, background):
        '''
        Encode foreground and background color into the associated
        curses color attribute value.
        '''
        pair_number = self.tsGetColorPairNumber(foreground, background)

        attribute = self.color_pair(pair_number)

        return (attribute)

    #-----------------------------------------------------------------------

    def tsGetBuiltInColorCount(self):
        '''
        Return the number of built-in curses colors, those colors which
        cannot be changed.
        '''
        if self.ts_has_colors:

            if self.ts_curses_colors == 8:

                count = self.ts_curses_colors

            elif self.ts_curses_colors == 16:

                count = self.ts_curses_colors

            else:

                count = min(16, self.ts_curses_colors)

            if True or (DEBUG and VERBOSE):
                fmt1 = 'tsGetBuiltInColorCount: ' + \
                       '\n\thas_colors = "%s"' % str(self.ts_has_colors)
                fmt2 = '\n\tcurses_colors = "%d"' % self.ts_curses_colors
                msg = fmt1 + fmt2
                self.logger.debug(msg)

        else:

            if True or (DEBUG and VERBOSE):
                fmt1 = 'tsGetBuiltInColorCount: ' + \
                       '\n\thas_colors = "%s"' % str(self.ts_has_colors)
                fmt2 = '\n\tcurses_colors = "%d"' % self.ts_curses_colors
                msg = fmt1 + fmt2
                self.logger.error(msg)

            count = 0

        return (count)

    #-----------------------------------------------------------------------

    def tsGetColorNames(self):
        '''
        Return the curses color names.
        '''
        set_to_use = self.tsGetSetToUseForColorNameFromCode()

        return (set_to_use)

    #-----------------------------------------------------------------------

    def tsGetColorCodes(self):
        '''
        Return the curses color codes.
        '''
        set_to_use = self.tsGetSetToUseForColorCodeFromName()

        return (set_to_use)

    #-----------------------------------------------------------------------

    def tsGetColorRGBCodes(self):
        '''
        Return the RGB color codes for the current terminal emulator.
        '''
        set_to_use = tsGetSetToUseForColorNameFromCode()

        theRGBCodes = []
        for aName in list(set_to_use.keys()):
            anRGBCode = extendedColorDataBaseRGB[aName]
            theRGBCodes.append(anRGBCode)
 
        return (theRGBCodes)

    #-----------------------------------------------------------------------

    def tsGetCursesDefaultColors(self):
        '''
        Gather the initial curses color palette and register it in
        the GraphicalTextUserInterface.ColorDataBaseRGB.
        '''
        set_to_use = self.tsGetSetToUseForColorNameFromCode()

##      # set_to_use = self.tsStripDictionaryName(xterm256NameFromCode)
##        maxCursesScale =1000
##        maxColorScale = 255

        try:
            for color_number in range(0, self.ts_curses_colors):
                if color_number < len(set_to_use):
                    color_name = set_to_use[color_number]
                else:
                    color_name = 'XTERM256_NUMBER_%d' % color_number
                color_content = self.tsGetCursesColorContent(color_number)
                red = color_content[0]
                green = color_content[1]
                blue = color_content[2]
                GraphicalTextUserInterface.ColorDataBaseRGB[
                    color_name] = color_content
                self.logger.debug(
                    'tsGetCursesDefaultColors: ' + \
                    '%s = (%d, %d, %d) %s' % (color_name,
                                              red,
                                              green,
                                              blue,
                                              str(color_content)))

        except Exception, e:

            self.logger.error('tsGetCursesDefaultColors: %s' % str(e))

    #-----------------------------------------------------------------------

    def tsGetCursesColorContent(self, color_number):
        '''
        Returns the intensity of the red, green, and blue (RGB) components
        in the color designated by the color_number, which must be between
        0 and COLORS. A 3-tuple is returned, containing the R,G,B values
        for the given color, which will be between 0 (no component) and
        255 (maximum amount of component).

        NOTE: Curses returns an R, G, B values between 0  and 1000.
        '''
        maxCursesScale = 1000
        maxColorScale = 255

        try:

            (r, g, b) = self.color_content(color_number)
            if tsPreserve255RGB:
                # Each r, g, b value must be between 0 and 255.
                red = int(r)
                green = int(g)
                blue = int(b)
            else:
                # Each r, g, b value must be between 0 and 1000.
                (red, green, blue) = (
                    ((int(r) * maxColorScale) // maxCursesScale),
                    ((int(g) * maxColorScale) // maxCursesScale),
                    ((int(b) * maxColorScale) // maxCursesScale))

        except Exception, e:

            # Invalid curses color number; set default COLOR_BLACK
            (red, green, blue) = (0, 0, 0)

            self.logger.error('tsGetCursesColorContent: %s' % str(e))

        return (red, green, blue)

    #-----------------------------------------------------------------------

    def tsGetWxPythonColorContent(self, color_number):
        '''
        Returns the intensity of the red, green, and blue (RGB) components
        in the color color_number, which must be between 0 and COLORS. A
        3-tuple is returned, containing the R,G,B values for the given
        color, which will be between 0 (no component) and 255 (maximum
        amount of component).
        '''
        colorName = xterm256ColorNameFromCode[color_number]
        try:

##            ## colorRGB = wxPython256ColorRGBFromColorName[colorName]
##            # print('colorName= %s; value=%s' % (colorName, str(value)))
##            red = (colorRGB & 0xFF0000) >> 16
##            green = (colorRGB & 0x00FF00) >> 8
##            blue = (colorRGB & 0x0000FF)
##            self.logger.debug(
##                "tsGetWxPythonColorContent: ' + \
##                '%3d, '%20s', %3d, %3d, %3d, 0x%6.6X" % (
##                    color_number,
##                    colorName,
##                    red,
##                    green,
##                    blue,
##                    colorRGB))
            colorRGB = extendedColorDataBaseRGB[colorName]
            red = colorRGB[0]
            green = colorRGB[1]
            blue = colorRGB[2]
            self.logger.debug(
                "tsGetWxPythonColorContent: ' + \
                '%3d, '%20s', %3d, %3d, %3d, %s" % (
                    color_number,
                    colorName,
                    red,
                    green,
                    blue,
                    str(colorRGB)))

        except Exception, e:

            # Invalid curses color number; set default COLOR_BLACK
            (red, green, blue) = (0, 0, 0)

            self.logger.error('tsGetWxPythonColorContent: %s' % str(e))

        return (red, green, blue)

    #-----------------------------------------------------------------------

    def tsSetCursesColorNumber(self, color_number, red, green, blue):
        '''
        Changes the definition of a color, taking the number of the color
        to be changed followed by three RGB values (for the amounts of red,
        green, and blue components). The value of color_number must be
        between 0 and COLORS. Each of r, g, b, must be a value between 0
        and 1000. When init_color() is used, all occurrences of that color
        on the screen immediately change to the new definition. This
        function is a no-op on most terminals; it is active only if
        can_change_color() returns 1.
        '''
        maxColorScale = 255
        minColorScale = 0

        maxCursesScale = 1000
        minCursesScale = minColorScale

        if red < minColorScale:
            colorRed = minColorScale
        elif red > maxColorScale:
            colorRed = maxColorScale
        else:
            colorRed = red

        if green < minColorScale:
            colorGreen = minColorScale
        elif green > maxColorScale:
            colorGreen = maxColorScale
        else:
            colorGreen = green

        if blue < minColorScale:
            colorBlue = minColorScale
        elif red > maxColorScale:
            colorBlue = maxColorScale
        else:
            colorBlue = blue

        if tsPreserve255RGB:

            # Each r, g, b value must be between 0 and 255.
            r = colorRed
            g = colorGreen
            b = colorBlue

        else:

            # Each r, g, b value must be between 0 and 1000.
            r = (colorRed * maxCursesScale) // maxColorScale
            g = (colorGreen * maxCursesScale) // maxColorScale
            b = (colorBlue * maxCursesScale) // maxColorScale

        try:

            if self.can_change_color():
                self.init_color(color_number, r, g, b)

            (rGet, gGet, bGet) = self.color_content(color_number)
            if (rGet == r) and \
               (gGet == g) and \
               (bGet == b):
                msg1 = 'tsSetCursesColorNumber (%d): ' % color_number
                msg2 = '(Red, Green, Blue)=(%d, %d, %d)' % (
                    colorRed, colorGreen, colorBlue)
                msg3 = 'Output RGB=(%d, %d, %d) is ' % (r, g, b)
                msg4 = 'Input RGB=(%d, %d, %d)' % (rGet, gGet, bGet)
                msg5 = msg1 + msg2 + msg3 + msg4
                self.logger.debug(msg5)
            else:
                msg1 = 'tsSetCursesColorNumber (%d): ' % color_number
                msg2 = '(Red, Green, Blue)=(%d, %d, %d)' % (
                    colorRed, colorGreen, colorBlue)
                msg3 = 'Output RGB=(%d, %d, %d) is NOT ' % (r, g, b)
                msg4 = 'Input RGB=(%d, %d, %d)' % (rGet, gGet, bGet)
                msg5 = msg1 + msg2 + msg3 + msg4
                self.logger.warning(msg5)

        except Exception, e:

            # Invalid curses color
            self.logger.error('tsSetCursesColorNumber (%d): %s' % \
                              (color_number, str(e)))

    #-----------------------------------------------------------------------

    def tsGetCursesColorPair(self, pair_number):
        '''
        Returns the attribute value for displaying text in the specified
        color. This attribute value can be combined with A_STANDOUT,
        A_REVERSE, and the other A_* attributes. pair_number() is the
        counterpart to this function.
        '''
        try:

            attr = self.color_pair(pair_number)

        except Exception, e:

            self.logger.error('tsGetCursesColorPair ' + \
                              '(substituting WHITE on BLACK): %s' % str(e))

            # Invalid curses pair number;
            # Get default for COLOR_WHITE on COLOR_BLACK
            attr = self.color_pair(0)

        return (attr)

    #-----------------------------------------------------------------------

    def tsSetCursesCursor(self, visibility):
        '''
        Sets the cursor state. visibility can be set to 0, 1, or 2, for
        invisible, normal, or very visible. If the terminal supports the
        visibility requested, the previous cursor state is returned;
        otherwise, an exception is raised. On many terminals, the
        "visible" mode is an underline cursor and the "very visible"
        mode is a block cursor.
        '''
        try:

            curses.curs_set(visibility)

        except Exception, e:

            self.logger.error('tsSetCursesCursor: %s' % str(e))

    #-----------------------------------------------------------------------

    def tsSetCursesColorPair(self, pair_number, fg, bg):
        '''
        Changes the definition of a color-pair. It takes three arguments:
        the number of the color-pair to be changed, the foreground color
        number, and the background color number. The value of pair_number
        must be between 1 and COLOR_PAIRS - 1 (the 0 color pair is wired
        to white on black and cannot be changed). The value of fg and bg
        arguments must be between 0 and COLORS. If the color-pair was
        previously initialized, the screen is refreshed and all occurrences
        of that color-pair are changed to the new definition.
        '''
        if self.ts_has_colors:

            try:

                self.init_pair(pair_number, fg, bg)

            except Exception, e:

                self.logger.error('tsSetCursesColorPair: %s' % str(e))

    #-----------------------------------------------------------------------

    def tsGetCursesPairContent(self, pair_number):
        '''
        Returns a tuple (fg, bg) containing the colors for the requested
        color pair. The value of pair_number must be between 1 and
        COLOR_PAIRS - 1
        '''
        if (self.ts_has_colors and \
            ((0 < pair_number) and \
             (pair_number < curses.COLOR_PAIRS))):

            (fg, bg) = self.pair_content(pair_number)

        else:

            self.logger.error('tsGetCursesPairContent: ' + \
                              'substituting WHITE on BLACK.')

            # Invalid curses pair number.
            # The 0 color pair is wired to white on black and cannot
            # be changed.

            (fg, bg) = (curses.COLOR_WHITE, curses.COLOR_BLACK)

        return (fg, bg)

    #-----------------------------------------------------------------------

    def tsGetMouseButtonCodes(self):
        '''
        '''
        return (self.ts_MouseButtonCodes)

    #-----------------------------------------------------------------------

    def tsSetMouseButtonCodes(self, has_mouse):
        '''
        Establish dictionary of curses default mouse codes, if applicable.
        '''

        if has_mouse:

            # Return dictionary of default curses button codes
            reply = MouseButtonCodes

        else:

            # Return indicator that no button codes are available
            reply = None

        return (reply)

    #-----------------------------------------------------------------------

    def tsInstallMonochromeDataBase(self):
        '''
        Install the monochrome (non-color black & white) database.
        '''
        self.logger.debug(
            '    Begin tsInstallMonochromeDataBase')

        self.ts_builtin_palette = True # None
        self.can_change_color = False # None
        self.ts_curses_color_pairs = False # None
        self.ts_curses_colors = False # None
        self.ts_has_colors = False # None
        self.ts_has_default_colors = True # None

        GraphicalTextUserInterface.ColorDataBase = None
        GraphicalTextUserInterface.ColorDataBaseID = None
        GraphicalTextUserInterface.ColorDataBaseRGB = None
        GraphicalTextUserInterface.ColorDataBasePairID = None
        GraphicalTextUserInterface.ColorSubstitutionDataBase = None

        self.logger.debug(
            '    End tsInstallMonochromeDataBase')

    #-----------------------------------------------------------------------

    def tsInstallDefaultColorDataBase(self):
        '''
        Install the default (8-/16-color) database appropriate for
        "cygwin", "xterm", "xterm-color" and "xterm-16color"
        terminal and terminal emulator displays. The default
        colors are the built-in ones established by the curses or
        mcurses library itself, rather than the industry standard
        RGB values established by tsInstallExtendedColorDataBase.

        NOTES:

        1. "xterm8" denotes use of the traditioal and current curses
           8-color palette. Colors are defined by a blend of the Red,
           Green and Blue primary colors having color intensity within
           the range of 0 to 255.

        2. "xterm16" denotes use of the current curses 16-color palette.
           Colors are defined by a blend of the Red, Green and Blue
           primary colors having color intensity within the range of
           0 to 255.

        3. When tsWxGraphicalTextUserInterface is run on Linux and
           Microsoft Windows (with the Cygwin plug-in from Red Hat
           Linux) the Python Curses module reports that xterm-color
           only has 8-colors and that the colors cannot be changed.
           Consequently, this method successfully treats it as if it
           were an "xterm8".       

        4. Blends of the Red, Green and Blue primary colors create a
           virtual rainbow of colors. Examples:

           Black      = (  0,   0,   0)
           Red        = (255,   0,   0)
           Green      = (  0, 255,   0)
           Blue       = (  0,   0, 255)
           Lime Green = ( 50, 205,  50)
           White      = (255, 255, 255)
        '''

##      if self.can_change_color():

##        Re-assign colors to apply industry standard RGB values
##        regardless of built-in terminal or terminal emulator
##        configuration.

##        xterm8ColorNameFromCode = {         xterm16ColorNameFromCode = {
##        0: COLOR_BLACK,       xterm8        0: COLOR_BLACK,
##        1: COLOR_RED,     xterm8--> xterm16 1: COLOR_MAROON,
##        2: COLOR_GREEN,       xterm8        2: COLOR_GREEN,
##        3: COLOR_YELLOW,  xterm8--> xterm16 3: COLOR_OLIVE,
##        4: COLOR_BLUE,    xterm8--> xterm16 4: COLOR_NAVY,
##        5: COLOR_MAGENTA, xterm8--> xterm16 5: COLOR_PURPLE,
##        6: COLOR_CYAN,    xterm8--> xterm16 6: COLOR_TEAL,
##        7: COLOR_WHITE}   xterm8--> xterm16 7: COLOR_SILVER,
##                                    xterm16 8: COLOR_GRAY,
##                                     xterm8 9: COLOR_RED,
##                                    xterm16 10: COLOR_LIME_GREEN,
##                                     xterm8 11: COLOR_YELLOW,
##                                     xterm8 12: COLOR_BLUE,
##                                     xterm8 13: COLOR_MAGENTA,
##                                     xterm8 14: COLOR_CYAN,
##                                     xterm8 15: COLOR_WHITE}

##      else:

##        Apply built-in terminal or terminal emulator configuration.

##        0:      COLOR_BLACK   0       0       0
##        1:      COLOR_RED     173     0       0
##        2:      COLOR_GREEN   0       173     0
##        3:      COLOR_YELLOW  173     173     0
##        4:      COLOR_BLUE    0       0       173
##        5:      COLOR_MAGENTA 173     0       173
##        6:      COLOR_CYAN    0       173     173
##        7:      COLOR_WHITE   173     173     173
##        8:      COLOR_BLACK   0       0       0
##        9:      COLOR_RED     255     0       0
##        10:     COLOR_GREEN   0       255     0
##        11:     COLOR_YELLOW  255     255     0
##        12:     COLOR_BLUE    0       0       255
##        13:     COLOR_MAGENTA 255     0       255
##        14:     COLOR_CYAN    0       255     255
##        15:     COLOR_WHITE   255     255     255

        self.logger.debug(
            '    Begin tsInstallDefaultColorDataBase')

        set_to_use = self.tsGetSetToUseForColorNameFromCode()

        if DEBUG_tsInstallExtendedColorDataBase:
            print('\n\n tsInstallDefaultColorDataBase=%s' % str(
                set_to_use))
            debug_via_tsru(myDictionary=set_to_use)

        colorSubstitutionMap = None

        if True: # DEBUG and VERBOSE:
            fmt1 = 'tsInstallDefaultColorDataBase ' + \
                   '(terminal independant default): \n'
            fmt2 = '\ttermname=%s \n' % self.ts_termname
            fmt3 = '\tcurses_colors=%d \n' % self.ts_curses_colors
            fmt4 = '\tcan_change_color=%d \n' % self.can_change_color()
            fmt5 = '\tset_to_use=%s' % str(set_to_use)
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            self.logger.notice(msg)

        if ((self.ts_curses_colors == 8) and \
            ((self.ts_termname == 'cygwin') or \
             (self.ts_termname == 'xterm') or \
             (self.ts_termname == 'xterm-color'))):

            set_to_use = self.tsStripDictionaryName(
                xterm8BuiltinColorNameFromCode)

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n xterm8BuiltinColorNameFromCode=%s' % str(
                    set_to_use))
                debug_via_tsru(myDictionary=set_to_use)

            colorSubstitutionMap = color8SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n colorSubstitutionMap=%s' % str(
                    set_to_use))
                debug_via_tsru(myDictionary=set_to_use)

        elif ((self.ts_curses_colors == 16) and \
              (self.ts_termname == 'xterm-16color')):

            # TERM=xterm-16color
            set_to_use = self.tsStripDictionaryName(
                xterm16BuiltinColorNameFromCode)

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n xterm16BuiltinColorNameFromCode=%s' % str(
                    set_to_use))
                debug_via_tsru(myDictionary=set_to_use)

            colorSubstitutionMap = color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n colorSubstitutionMap=%s' % str(
                    set_to_use))
                debug_via_tsru(myDictionary=set_to_use)

        else:

            fmt1 = 'tsInstallDefaultColorDataBase (invalid config): \n'
            fmt2 = '\tcurses_colors=%d \n' % self.ts_curses_colors
            fmt3 = '\ttermname=%s' % self.ts_termname
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        if True: # DEBUG and VERBOSE:
            fmt1 = 'tsInstallDefaultColorDataBase ' + \
                   '(terminal-specific default): \n'
            fmt2 = '\ttermname=%s \n' % self.ts_termname
            fmt3 = '\tcurses_colors=%d \n' % self.ts_curses_colors
            fmt4 = '\tcan_change_colors=%d \n' % self.can_change_color()
            fmt5 = '\tset_to_use=%s' % str(set_to_use)
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            self.logger.notice(msg)

        available_colors = len(list(set_to_use.keys()))

        GraphicalTextUserInterface.ColorDataBase = {}
        GraphicalTextUserInterface.ColorDataBase[
            'name'] = 'ColorDataBase'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBaseID = {}
        GraphicalTextUserInterface.ColorDataBaseID[
            'name'] = 'ColorDataBaseID'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBaseRGB = {}
        GraphicalTextUserInterface.ColorDataBaseRGB[
            'name'] = 'ColorDataBaseRGB'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID = {}
        GraphicalTextUserInterface.ColorDataBasePairID[
            'name'] = 'ColorDataBasePairID'

        GraphicalTextUserInterface.ColorDataBasePairID[
            'PairNumbersFromColorNumbers'] = {}

        GraphicalTextUserInterface.ColorDataBasePairID[
            'PairNumbersFromColorNumbers'][
            'name'] = 'PairNumbersFromColorNumbers'

        GraphicalTextUserInterface.ColorDataBasePairID[
            'ColorNumbersFromPairNumbers'] = {}

        GraphicalTextUserInterface.ColorDataBasePairID[
            'ColorNumbersFromPairNumbers'][
            'name'] = 'ColorNumbersFromPairNumbers'

        #---------------------------------------------------

        theMap = colorSubstitutionMap
        GraphicalTextUserInterface.ColorSubstitutionDataBase = theMap

        #---------------------------------------------------
        # Fill in color name, code and rgb data bases
        for aCode in sorted(list(set_to_use.keys())):

            aName = set_to_use[aCode]
            self.ts_builtin_palette[
                aName] = self.tsGetCursesColorContent(aCode)
            GraphicalTextUserInterface.ColorDataBase[aName] = aCode
            GraphicalTextUserInterface.ColorDataBaseID[aCode] = aName

##            # Override Built-In Color Content
##            # to ensure standard RGB values

##            rgb = extendedColorDataBaseRGB[aName] 
##            red = rgb[0]
##            green = rgb[1]
##            blue = rgb[2] 
##            self.tsSetCursesColorNumber(aCode, red, green, blue)

##            GraphicalTextUserInterface.ColorDataBaseRGB[aName] = (
##                red, green, blue)

##            (r, g, b) = self.tsGetCursesColorContent(aCode)

##            if True or DEBUG:

##                if ((abs(red - r) <= 1) and \
##                    (abs(green - g) <= 1) and \
##                    (abs(blue - b) <= 1)):
##                    match = True
##                else:
##                    match = False
##                msg = 'tsInstallDefaultColorDataBase: ' + \
##                      'color (%d / %s) match = %s, ' % (
##                          aCode, aName, match) + \
##                      'curses = %s; wxPython = %s\n' % (
##                          (r, g, b), (red, green, blue))
##                if match:
##                    self.logger.debug(msg)
##                else:
##                    self.logger.error(msg)

        #---------------------------------------------------

        if True or (DEBUG and VERBOSE):
            self.logger.debug(
                'installed built-in ColorDataBase = %s' % \
                str(GraphicalTextUserInterface.ColorDataBase))

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.ColorDataBase=%s' % str(
                    GraphicalTextUserInterface.ColorDataBase))
                debug_via_tsru(myDictionary=GraphicalTextUserInterface.ColorDataBase)

            self.logger.debug(
                'installed ColorDataBaseID = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseID))

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.ColorDataBaseID=%s' % str(
                    GraphicalTextUserInterface.ColorDataBaseID))
                debug_via_tsru(myDictionary=GraphicalTextUserInterface.ColorDataBaseID)

            self.logger.debug(
                'installed ColorDataBaseRGB = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseRGB))

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.ColorDataBaseRGBe=%s' % str(
                    GraphicalTextUserInterface.ColorDataBaseRGB))
                debug_via_tsru(myDictionary=GraphicalTextUserInterface.ColorDataBaseRGB)

            self.logger.debug(
                'installed ColorSubstitutionDataBase = %s' % \
                str(GraphicalTextUserInterface.ColorSubstitutionDataBase))

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.ColorSubstitutionDataBase=%s' % str(
                    GraphicalTextUserInterface.ColorSubstitutionDataBase))
                debug_via_tsru(myDictionary=GraphicalTextUserInterface.ColorSubstitutionDataBase)

        #---------------------------------------------------

        # Fill in color pair data bases
        pair_number = -1
        for fg_number in sorted(list(set_to_use.keys())):
            foreground_name = set_to_use[fg_number]
            for bg_number in sorted(list(set_to_use.keys())):
                backround_name = set_to_use[bg_number]
                pair_number += 1
                GraphicalTextUserInterface.ColorDataBasePairID[
                    'PairNumbersFromColorNumbers'][
                    (fg_number, bg_number)] = pair_number

                GraphicalTextUserInterface.ColorDataBasePairID[
                    'ColorNumbersFromPairNumbers'][
                    pair_number] = (fg_number, bg_number)

                if pair_number == 0:

                    # The 0 color pair is wired to white on black
                    # and cannot be changed.
                    pass

                else:

                    # Changes the definition of a color-pair. It takes
                    # three arguments: the number of the color-pair to
                    # be changed, the foreground color number, and the
                    # background color number. The value of pair_number
                    # must be between 1 and COLOR_PAIRS - 1 (the 0 color
                    # pair is wired to white on black and cannot be
                    # changed). The value of fg and bg arguments must be
                    # between 0 and COLORS. If the color-pair was
                    # previously initialized, the screen is refreshed
                    # and all occurrences of that color-pair are changed
                    # to the new definition.
                    if self.ts_has_colors:
                        self.init_pair(pair_number, fg_number, bg_number)
                    else:
                        pass

        self.logger.debug(
            'installed built-in ColorDataBasePairID = %s' % \
            str(GraphicalTextUserInterface.ColorDataBasePairID))

        if DEBUG_tsInstallExtendedColorDataBase:
            print('\n\n GraphicalTextUserInterface.ColorDataBasePairID=%s' % str(
                GraphicalTextUserInterface.ColorDataBasePairID))
            debug_via_tsru(myDictionary=GraphicalTextUserInterface.ColorDataBasePairID)

        self.logger.debug(
            '    End tsInstallDefaultColorDataBase')

    #-----------------------------------------------------------------------

    def tsInstallExtendedColorDataBase(self):
        '''
        Install the extended 88-color or 256-color database.
        '''
        self.logger.debug(
            '    Begin tsInstallExtendedColorDataBase')

        if ((self.ts_termname == 'cygwin') or \
            (self.ts_termname == 'xterm') or \
            (self.ts_termname == 'xterm-color')):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm8ColorNameFromCode))
                debug_via_tsru(myDictionary=xterm8ColorNameFromCode)

        elif (self.ts_termname == 'xterm-16color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm16ColorNameFromCode))
                debug_via_tsru(myDictionary=xterm16ColorNameFromCode)

        elif (self.ts_termname == 'xterm-88color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm88ColorNameFromCode))
                debug_via_tsru(myDictionary=xterm88ColorNameFromCode)

        elif (self.ts_termname == 'xterm-256color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                    xterm256ColorNameFromCode))
                debug_via_tsru(myDictionary=xterm256ColorNameFromCode)

        else:

            fmt1 = 'tsInstallExtendedColorDataBase (invalid config):'
            fmt2 = 'curses_colors=%d' % self.ts_curses_colors
            fmt3 = 'termname=%s' % self.ts_termname
            msg = '%s\n\t%s\n\t%s' % (fmt1, fmt2, fmt3)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        available_colors = len(list(set_to_use.keys()))

        if DEBUG_tsInstallExtendedColorDataBase:
            print('\n\n GraphicalTextUserInterface.' + \
                  'tsInstallExtendedColorDataBase: ' + \
                  'available_colors=%s' % str(
                available_colors))
            debug_via_tsru(myDictionary=set_to_use)

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBase = {}
        GraphicalTextUserInterface.ColorDataBase[
            'name'] = 'ColorDataBase'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBaseID = {}
        GraphicalTextUserInterface.ColorDataBaseID[
            'name'] = 'ColorDataBaseID'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBaseRGB = {}
        GraphicalTextUserInterface.ColorDataBaseRGB[
            'name'] = 'ColorDataBaseRGB'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID = {}
        GraphicalTextUserInterface.ColorDataBasePairID[
            'name'] = 'ColorDataBasePairID'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID[
            'PairNumbersFromColorNumbers'] = {}

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID[
            'PairNumbersFromColorNumbers'][
            'name'] = 'PairNumbersFromColorNumbers'

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID[
            'ColorNumbersFromPairNumbers'] = {}

        #---------------------------------------------------

        GraphicalTextUserInterface.ColorDataBasePairID[
            'ColorNumbersFromPairNumbers'][
            'name'] = 'ColorNumbersFromPairNumbers'

        #---------------------------------------------------

        theMap = None
        GraphicalTextUserInterface.ColorSubstitutionDataBase = theMap

        #---------------------------------------------------
        # Register entries in color name, code and rgb data bases
        for aCode in range(available_colors):
            aName = set_to_use[aCode]
            aBuiltinRGB = self.tsGetCursesColorContent(aCode)
            aExtendedRGB = extendedColorDataBaseRGB[aName]
            self.ts_builtin_palette[aName] = aBuiltinRGB
            GraphicalTextUserInterface.ColorDataBase[aName] = aCode
            GraphicalTextUserInterface.ColorDataBaseID[aCode] = aName
            GraphicalTextUserInterface.ColorDataBaseRGB[
                aName] = aExtendedRGB

            if True or (DEBUG and VERBOSE):
                fmt0 = 'registered entries in extended ColorDataBase: '
                fmt1 = '\n\t aCode=%d; ' % aCode
                fmt2 = 'aName=%s; ' % aName
                fmt3 = 'aBuiltinRGB=%s; ' % str(aBuiltinRGB)
                fmt4 = 'aExtendedRGB=%s' % str(aExtendedRGB)
                msg = fmt0 + fmt1 + fmt2 + fmt3 + fmt4
                self.logger.debug(msg)

        #---------------------------------------------------

        if True or (DEBUG and VERBOSE):
            self.logger.debug(
                'installed standard ColorDataBase = %s' % \
                str(GraphicalTextUserInterface.ColorDataBase))

            self.logger.debug(
                'installed standard ColorDataBaseID = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseID))

            self.logger.debug(
                'installed standard ColorDataBaseRGB = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseRGB))

            self.logger.debug(
                'installed standard ColorSubstitutionDataBase = %s' % \
                str(GraphicalTextUserInterface.ColorSubstitutionDataBase))

        #---------------------------------------------------

        # Fill in color name, code and rgb data bases
        for aCode in range(available_colors):

            aName = GraphicalTextUserInterface.ColorDataBaseID[aCode]
            aExtendedRGB = GraphicalTextUserInterface.ColorDataBaseRGB[aName]

            if False: # aCode < standard_colors:
                # standard color should already be registered
                pass
            else:
                # register extended color

                # (red, green, blue) = extendedColorDataBaseRGB[aName]
                rgb = aExtendedRGB
                red = rgb[0]
                green = rgb[1]
                blue = rgb[2] 
                self.tsSetCursesColorNumber(aCode, red, green, blue)

                (r, g, b) = self.tsGetCursesColorContent(aCode)

                if True or DEBUG:

                    if ((abs(red - r) <= 1) and \
                        (abs(green - g) <= 1) and \
                        (abs(blue - b) <= 1)):
                        match = True
                    else:
                        match = False
                    msg = 'tsInstallExtendedColorDataBase: ' + \
                          'color (%d / %s) match = %s, ' % (
                              aCode, aName, match) + \
                          'curses = %s; wxPython = %s\n' % (
                              (r, g, b), (red, green, blue))
                    if match:
                        self.logger.debug(msg)
                    else:
                        self.logger.error(msg)

##        if True or (DEBUG and VERBOSE):

##            self.logger.debug(
##                'installed extended ColorDataBase = %s' % \
##                str(GraphicalTextUserInterface.ColorDataBase))

##            self.logger.debug(
##                'installed extended ColorDataBaseID = %s' % \
##                str(GraphicalTextUserInterface.ColorDataBaseID))

##            self.logger.debug(
##                'installed extended ColorDataBaseRGB = %s' % \
##                str(GraphicalTextUserInterface.ColorDataBaseRGB))

##            self.logger.debug(
##                'installed extended ColorSubstitutionDataBase = %s' % \
##                str(GraphicalTextUserInterface.ColorSubstitutionDataBase))

        # Fill in color pair data bases
        pair_number = -1 # standard_color_pairs
        for fg_number in range(available_colors):

            foreground_name = GraphicalTextUserInterface.ColorDataBaseID[
                fg_number]

            for bg_number in range(available_colors):

                background_name = GraphicalTextUserInterface.ColorDataBaseID[
                    bg_number]

                # register extended color
                pair_number += 1

                GraphicalTextUserInterface.ColorDataBasePairID[
                    'PairNumbersFromColorNumbers'][
                    (fg_number, bg_number)] = pair_number

                GraphicalTextUserInterface.ColorDataBasePairID[
                    'ColorNumbersFromPairNumbers'][
                    pair_number] = (fg_number, bg_number)

                if pair_number == 0:

                    # The 0 color pair is wired to white on black
                    # and cannot be changed.
                    pass

                else:

                    # Changes the definition of a color-pair. It takes
                    # three arguments: the number of the color-pair to
                    # be changed, the foreground color number, and the
                    # background color number. The value of pair_number
                    # must be between 1 and COLOR_PAIRS - 1 (the 0 color
                    # pair is wired to white on black and cannot be
                    # changed). The value of fg and bg arguments must be
                    # between 0 and COLORS. If the color-pair was
                    # previously initialized, the screen is refreshed
                    # and all occurrences of that color-pair are changed
                    # to the new definition.
                    if self.ts_has_colors:
                        self.init_pair(pair_number, fg_number, bg_number)
                    else:
                        pass
                        # self.init_pair(pair_number, fg_number, bg_number)

        self.logger.debug(
            'installed extended ColorDataBasePairID = %s' % \
            str(GraphicalTextUserInterface.ColorDataBasePairID))

        self.logger.debug(
            '    End tsInstallExtendedColorDataBase')

    #-----------------------------------------------------------------------
 
    def _sigIntHandler(self, dummy, unused):
        '''
        Shutdown cleanly on SIGINT.
        '''
        try:
            self.logger.warning('Received SIGINT')
        except AttributeError:
            pass
 
        self._cleanupWhenSignalReceived()

##        msg = 'User interrupt received'
##        raise tse.UserInterfaceException(
##            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def _sigAbrtHandler(self, dummy, unused):
        '''
        Shutdown cleanly on SIGABRT.
        '''
        try:
            self.logger.warning('Received SIGABRT')
        except AttributeError:
            pass

        self._cleanupWhenSignalReceived()

##        msg = 'Termination signal received'
##        raise tse.UserInterfaceException(
##            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------
 
    def _cleanupWhenSignalReceived(self):
        '''
        Shutdown cleanly on signals.
        '''
        self.stop()
        exit(0)

##        # Terminate any running children
##        for runningChild in self.runningChildren:
##            # Is the child still running?
##            if runningChild.poll() is not None:
##                try:
##                    self.logger.warning(
##                        '  Child %d is not running', runningChild.pid)
##                except AttributeError:
##                    pass
##                pass
##            # Yes, send him an abort signal
##            try:
##                self.logger.warning('  Child %d is running', runningChild.pid)
##                self.logger.warning('    Sending abort signal')
##            except AttributeError:
##                pass
##            os.kill(runningChild.pid, signal.SIGABRT)
##            # Wait for child terminated
##            try:
##                self.logger('    Waiting for termination')
##            except AttributeError:
##                pass
##            maximumTime = self.childTerminationMaximumTime
##            timeIncrement = self.childTerminationTimeIncrement
##            currentTime = 0.0
##            while runningChild.poll() is None:
##                if currentTime < maximumTime:
##                    time.sleep(timeIncrement)
##                    currentTime += timeIncrement
##                else:
##                    try:
##                        self.logger.warning('    Child not terminated after %2.2f', currentTime)
##                    except AttributeError:
##                        pass
##                    os.kill(runningChild.pid, signal.SIGKILL)
##                    break
##            try:
##                self.logger.warning('    Child terminated')
##            except AttributeError:
##                pass

    #-----------------------------------------------------------------------

    def baudrate(self):
        '''
        Returns the output speed of the terminal in bits per second. On
        software terminal emulators it will have a fixed high value.
        Included for historical reasons; in former times, it was used to
        write output loops for time delays and occasionally to change
        interfaces depending on the line speed.
        '''
        try:
            reply = curses.baudrate()
        except Exception, e:
            reply = 0
            msg = 'baudrate: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def beep(self):
        '''
        Emit a short attention sound.
        '''
        try:
            curses.baudrate()
        except Exception, e:
            msg = 'baudrate: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def can_change_color(self):
        '''
        Returns true or false, depending on whether the programmer can
        change the colors displayed by the terminal.
        '''
        try:
##          FIX_ME_cannot_change_color = False # True
##          if FIX_ME_cannot_change_color:
##              reply = False
##          else:
##              reply = curses.can_change_color()
            reply = curses.can_change_color()
        except Exception, e:
            reply = False
            msg = 'can_change_color: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def cbreak(self):
        '''
        Enter cbreak mode. In cbreak mode (sometimes called "rare" mode)
        normal tty line buffering is turned off and characters are available
        to be read one by one. However, unlike raw mode, special characters
        (interrupt, quit, suspend, and flow control) retain their effects on
        the tty driver and calling program. Calling first raw() then cbreak()
        leaves the terminal in cbreak mode.
        '''
        try:
            curses.cbreak()
        except Exception, e:
            msg = 'cbreak: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def color_content(self, color_number):
        '''
        Returns the intensity of the red, green, and blue (RGB) components
        in the color color_number, which must be between 0 and COLORS. A
        3-tuple is returned, containing the R,G,B values for the given color,
        which will be between 0 (no component) and 1000 (maximum amount of
        component).
        '''
        try:
            reply = curses.color_content(color_number)
##          self.logger.alert('color_content (%d %s): reply=%s' % (
##              color_number,
##              str(GraphicalTextUserInterface.ColorDataBaseID[color_number]),
##              str(reply)))
        except Exception, e:
            reply = (0, 0, 0)
            msg = 'color_content: %d; %s' % (
                color_number, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def color_pair(self, color_number):
        '''
        Returns the attribute value for displaying text in the specified
        color. This attribute value can be combined with A_STANDOUT,
        A_REVERSE, and the other A_* attributes. pair_number() is the
        counterpart to this function.
        '''
        if self.ts_has_colors:
            try:
                reply = curses.color_pair(color_number)
            except Exception, e:
                reply = 0
                msg = 'color_pair: %d; %s' % (
                    color_number, str(e))
                self.logger.error(msg)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)
        else:
            reply = 0

        return (reply)

    #-----------------------------------------------------------------------

    def curs_set(self, visibility):
        '''
        Sets the cursor state. visibility can be set to 0, 1, or 2, for
        invisible, normal, or very visible. If the terminal supports the
        visibility requested, the previous cursor state is returned;
        otherwise, an exception is raised. On many terminals, the "visible"
        mode is an underline cursor and the "very visible" mode is a block
        cursor.
        '''
        try:
            previousState = curses.curs_set(visibility)
            return (previousState)
        except Exception, e:
            msg = 'curs_set: %d; %s' % (
                visibility, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def def_prog_mode(self):
        '''
        Saves the current terminal mode as the "program" mode, the mode when
        the running program is using curses. (Its counterpart is the "shell"
        mode, for when the program is not in curses.) Subsequent calls to
        reset_prog_mode() will restore this mode.
        '''
        try:
            curses.def_prog_mode()
        except Exception, e:
            msg = 'def_prog_mode: %s' % str(e)
            self.logger.error(msg)

    #-----------------------------------------------------------------------

    def def_shell_mode(self):
        '''
        Saves the current terminal mode as the "shell" mode, the mode when
        the running program is not using curses. (Its counterpart is the
        "program" mode, when the program is using curses capabilities.)
        Subsequent calls to reset_shell_mode() will restore this mode.
        '''
        try:
            curses.def_shell_mode()
        except Exception, e:
            msg = 'def_shell_mode: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def delay_output(self, ms):
        '''
        Inserts an ms millisecond pause in output.
        '''
        try:
            curses.delay_output(ms)
        except Exception, e:
            msg = 'delay_output: %d; %s' % (
                ms, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def doupdate(self):
        '''
        Update the physical screen. The curses library keeps two data
        structures, one representing the current physical screen contents
        and a virtual screen representing the desired next state. The
        doupdate() ground updates the physical screen to match the virtual
        screen.

        The virtual screen may be updated by a noutrefresh() call after
        write operations such as addstr() have been performed on a window.
        The normal refresh() call is simply noutrefresh() followed by
        doupdate(); if you have to update multiple windows, you can speed
        performance and perhaps reduce screen flicker by issuing noutrefresh()
        calls on all windows, followed by a single doupdate().
        '''
        try:
            if wx.USE_CURSES_PANEL_STACK:
                self.pflush()
            curses.doupdate()
        except Exception, e:
            msg = 'doupdate: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def echo(self):
        '''
        Enter echo mode. In echo mode, each character input is echoed to
        the screen as it is entered.
        '''
        try:
            curses.echo()
        except Exception, e:
            msg = 'echo: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def endwin(self):
        '''
        De-initialize the library, and return terminal to normal status.
        '''
        try:

            self.reset_shell_mode()

            curses.endwin()

        except Exception, e:
            msg = 'endwin: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def erasechar(self):
        '''
        Returns the user current erase character. Under Unix operating
        systems this is a property of the controlling tty of the curses
        program, and is not set by the curses library itself.
        '''
        try:
            reply = curses.erasechar()
        except Exception, e:
            reply = None
            msg = 'erasechar: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def filter(self):
        '''
        The filter() routine, if used, must be called before initscr() is
        called. The effect is that, during those calls, LINES is set to 1;
        the capabilities clear, cup, cud, cud1, cuu1, cuu, vpa are disabled;
        and the home string is set to the value of cr. The effect is that
        the cursor is confined to the current line, and so are screen updates.
        This may be used for enabling character-at-a-time line editing
        without touching the rest of the screen.
        '''
        try:
            curses.filter()
        except Exception, e:
            msg = 'filter: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def flash(self):
        '''
        Flash the screen. That is, change it to reverse-video and then
        change it back in a short interval. Some people prefer such as
        "visible bell" to the audible attention signal produced by beep().
        '''
        try:
            curses.flash()
        except Exception, e:
            msg = 'flash: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def flushinp(self):
        '''
        Flush all input buffers. This throws away any typeahead that has
        been typed by the user and has not yet been processed by the program.
        '''
        try:
            curses.flushinp()
        except Exception, e:
            msg = 'flushinp: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def getmouse(self):
        '''
        After getch() returns KEY_MOUSE to signal a mouse event, this method
        should be call to retrieve the queued mouse event, represented as a
        5-tuple (id, x, y, z, bstate). id is an ID value used to distinguish
        multiple devices, and x, y, z are the event coordinates. (z is
        currently unused.). bstate is an integer value whose bits will be
        set to indicate the type of event, and will be the bitwise OR of one
        or more of the following constants, where n is the button number from
        1 to 4: BUTTONn_PRESSED, BUTTONn_RELEASED, BUTTONn_CLICKED,
        BUTTONn_DOUBLE_CLICKED, BUTTONn_TRIPLE_CLICKED, BUTTON_SHIFT,
        BUTTON_CTRL, BUTTON_ALT.
        '''
        try:
            reply = curses.getmouse()
        except Exception, e:
            reply = None
            msg = 'getmouse: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def getsyx(self):
        '''
        Returns the current coordinates of the virtual screen cursor in y
        and x. If leaveok is currently true, then -1,-1 is returned.
        '''
        try:
            reply = curses.getsyx()
        except Exception, e:
            reply = None
            msg = 'getsyx: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def getwin(self, file):
        '''
        Reads window related data stored in the file by an earlier putwin()
        call. The routine then creates and initializes a new window using
        that data, returning the new window object.
        '''
        try:
            reply = curses.getwin(file)
        except Exception, e:
            reply = None
            msg = 'getwin: %s; %s' % (
                str(file), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def has_colors(self):
        '''
        Returns true if the terminal can display colors; otherwise, it
        returns false.
        '''
        try:

            if curses.has_colors():

                if (self.termname().lower() in nonColorTerminals):

                    reply = False

                    fmt1 = 'Override: has_colors now %s ' % str(reply)
                    fmt2 = 'for terminal %s' % self.termname().lower()
                    self.logger.error(fmt1 + fmt2)

                else:

                    reply = True

            else:

                reply = False

        except Exception, e:

            reply = False
            msg = 'has_colors: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def has_ic(self):
        '''
        Returns true if the terminal has insert- and delete- character
        capabilities. This function is included for historical reasons
        only, as all modern software terminal emulators have such
        capabilities.
        '''
        try:
            reply = curses.has_ic()
        except Exception, e:
            reply = False
            msg = 'has_ic: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def has_il(self):
        '''
        Returns true if the terminal has insert- and delete-line
        capabilities, or can simulate them using scrolling regions. This
        function is included for historical reasons only, as all modern
        software terminal emulators have such capabilities.
        '''
        try:
            reply = curses.has_il()
        except Exception, e:
            reply = False
            msg = 'has_il: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def has_key(self, ch):
        '''
        Takes a key value ch, and returns true if the current terminal type
        recognizes a key with that value.
        '''
        try:
            reply = curses.baudrate()
        except Exception, e:
            reply = False
            msg = 'baudrate: %s; %s' % (
                str(ch), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def halfdelay(self, tenths):
        '''
        Used for half-delay mode, which is similar to cbreak mode in that
        characters typed by the user are immediately available to the
        program. However, after blocking for tenths tenths of seconds, an
        exception is raised if nothing has been typed. The value of tenths
        must be a number between 1 and 255. Use nocbreak() to leave
        half-delay mode.
        '''
        try:
            curses.halfdelay(tenths)
        except Exception, e:
            msg = 'halfdelay: %d; %s' % (
                str(tenths), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def init_color(self, color_number, r, g, b):
        '''
        Changes the definition of a color, taking the number of the color to
        be changed followed by three RGB values (for the amounts of red,
        green, and blue components). The value of color_number must be
        between 0 and COLORS. Each of r, g, b, must be a value between 0 and
        1000. When init_color() is used, all occurrences of that color on
        the screen immediately change to the new definition. This function
        is a no-op on most terminals; it is active only if can_change_color()
        returns 1.
        '''
        if self.has_colors():

            try:
                curses.init_color(color_number, r, g, b)
            except Exception, e:
                msg = 'init_color: (%d, %d, %d) -> %d; %s' % (
                    r, g, b, color_number, str(e))
                self.logger.error(msg)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        elif DEBUG:

            fmt1 = 'init_color: Termname=%s; ' % str(self.termname())
            fmt2 = 'does NOT support colors ' + \
                  '(%d, %d, %d) -> %d' % (r, g, b, color_number)
            self.logger.debug(fmt1 + fmt2)

    #-----------------------------------------------------------------------

    def init_pair(self, pair_number, fg, bg):
        '''
        Changes the definition of a color-pair. It takes three arguments:
        the number of the color-pair to be changed, the foreground color
        number, and the background color number. The value of pair_number
        must be between 1 and COLOR_PAIRS - 1 (the 0 color pair is wired
        to white on black and cannot be changed). The value of fg and bg
        arguments must be between 0 and COLORS. If the color-pair was
        previously initialized, the screen is refreshed and all occurrences
        of that color-pair are changed to the new definition.
        '''
        if self.has_colors():

            try:
                curses.init_pair(pair_number, fg, bg)
##                if True or DEBUG:
##                    (fg_actual, bg_actual) = curses.pair_content(pair_number)
##                    if (fg_actual, bg_actual) != (fg, bg):
##                        msg = '(%d, %d) != (%d, %d)' % (
##                            fg_actual, bg_actual, fg, bg)
##                        self.logger.error(msg)
##                    else:
##                        fg_attribute = curses.color_pair(fg)
##                        bg_attribute = curses.color_pair(bg)
##                        msg = '(%d, %d) == (%d, %d); attr = (0x%x, 0x%X)' % (
##                            fg_actual, bg_actual, fg, bg,
##                            fg_attribute, bg_attribute)
##                        self.logger.notice(msg)
            except Exception, e:
                msg = 'init_pair: (%d, %d) -> %d; %s' % (
                    fg, bg, pair_number, str(e))
                self.logger.error(msg)

                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        elif DEBUG:

            fmt1 = 'init_pair: Termname=%s; ' % str(self.termname())
            fmt2 = 'does NOT support colors ' + \
                  '(%d, %d) -> %d' % (fg, bg, pair_number)
            self.logger.debug(fmt1 + fmt2)

    #-----------------------------------------------------------------------

    def initscr(self):
        '''
        Initialize the library. Returns a WindowObject which represents the
        whole screen. Note: If there is an error opening the terminal, the
        underlying curses library may cause the interpreter to exit.
        '''
        try:
            reply = curses.initscr()

            # def_shell_mode must be invoked after initscr
            self.def_shell_mode()

        except Exception, e:
            reply = None
            msg = 'initscr: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def isendwin(self):
        '''
        Returns true if endwin() has been called (that is, the curses
        library has been deinitialized).
        '''
        try:
            reply = curses.isendwin()
        except Exception, e:
            reply = False
            msg = 'isendwin: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def keyname(self, k):
        '''
        Return the name of the key numbered k. The name of a key generating
        printable ASCII character is the key character. The name of a
        control-key combination is a two-character string consisting of
        a caret followed by the corresponding printable ASCII character. The
        name of an alt-key combination (128-255) is a string consisting of
        the prefix "M-" followed by the name of the corresponding ASCII
        character.
        '''
        try:
            reply = curses.keyname(k)
        except Exception, e:
            reply = None
            msg = 'keyname: %s; %s' % (
                str(k), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def killchar(self):
        '''
        Returns the user current line kill character. Under Unix operating
        systems this is a property of the controlling tty of the curses
        program, and is not set by the curses library itself.
        '''
        try:
            reply = curses.killchar()
        except Exception, e:
            reply = None
            msg = 'killchar: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def longname(self):
        '''
        Returns a string containing the terminfo long name field describing
        the current terminal. The maximum length of a verbose description
        is 128 characters. It is defined only after the call to initscr().
        '''
        try:
            reply = str(curses.longname())
        except Exception, e:
            reply = None
            msg = 'longname: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def meta(self, yes):
        '''
        If yes is 1, allow 8-bit characters to be input. If yes is 0, allow
        only 7-bit chars.
        '''
        try:
            curses.meta(yes)
        except Exception, e:
            msg = 'meta: %s; %s' % (
                str(yes), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def mouseinterval(self, interval):
        '''
        Sets the maximum time in milliseconds that can elapse between press
        and release events in order for them to be recognized as a click,
        and returns the previous interval value. The default value is 200
        msec, or one fifth of a second.
        '''
        try:
            curses.mouseinterval(interval)
        except Exception, e:
            msg = 'mouseinterval: %d; %s' % (
                interval, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def mousemask(self, mousemask):
        '''
        Sets the mouse events to be reported, and returns a tuple (availmask,
        oldmask). availmask indicates which of the specified mouse events
        can be reported; on complete failure it returns 0. oldmask is the
        previous value of the given window mouse event mask. If this function
        is never called, no mouse events are ever reported.
        '''
        try:
            reply = curses.mousemask(mousemask)
        except Exception, e:
            reply = None
            msg = 'mousemask: %s; %s' % (
                str(mousemask), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def napms(self, ms):
        '''
        Sleep for ms milliseconds.
        '''
        try:
            curses.napms(ms)
        except Exception, e:
            msg = 'napms: %d; %s' % (
                ms, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def newpad(self, nlines, ncols):
        '''
        Creates and returns a pointer to a new pad data structure with the
        given number of lines and columns. A pad is returned as a window
        object.

        A pad is like a window, except that it is not restricted by the
        screen size, and is not necessarily associated with a particular
        part of the screen. Pads can be used when a large window is needed,
        and only a part of the window will be on the screen at one time.
        Automatic refreshes of pads (such as from scrolling or echoing of
        input) do not occur. The refresh() and noutrefresh() methods of a
        pad require 6 arguments to specify the part of the pad to be
        displayed and the location on the screen to be used for the display.
        The arguments are pminrow, pmincol, sminrow, smincol, smaxrow,
        smaxcol; the p arguments refer to the upper left corner of the pad
        region to be displayed and the s arguments define a clipping box
        on the screen within which the pad region is to be displayed.
        '''
        try:
            reply = curses.newpad(nlines, ncols)
        except Exception, e:
            reply = None
            msg = 'newpad: (%d, %d): %s' % (
                nlines, ncols, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def newwin(self, nlines, ncols, begin_y, begin_x):
        '''
        Return a new window, whose left-upper corner is at (begin_y,
        begin_x), and whose height/width is nlines/ncols.
 
        By default, the window will extend from the specified position to
        the lower right corner of the screen.
        '''
        try:
            reply = curses.newwin(nlines, ncols, begin_y, begin_x)
        except Exception, e:
            reply = None
            msg = 'newwin: (%d, %d, %d, %d); %s' % (
                nlines, ncols, begin_y, begin_x, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------


    def nl(self):
        '''
        Enter newline mode. This mode translates the return key into newline
        on input, and translates newline into return and line-feed on output.
        Newline mode is initially on.
        '''
        try:
            curses.nl()
        except Exception, e:
            msg = 'nl: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def nocbreak(self):
        '''
        Leave cbreak mode. Return to normal "cooked" mode with line buffering.
        '''
        try:
            curses.nocbreak()
        except Exception, e:
            msg = 'nocbreak: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def noecho(self):
        '''
        Leave echo mode. Echoing of input characters is turned off.
        '''
        try:
            curses.noecho()
        except Exception, e:
            msg = 'noecho: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def nonl(self):
        '''
        Leave newline mode. Disable translation of return into newline on
        input, and disable low-level translation of newline into newline/
        return on output (but this does not change the behavior of
        addch("\n"), which always does the equivalent of return and line
        feed on the virtual screen). With translation off, curses can
        sometimes speed up vertical motion a little; also, it will be able
        to detect the return key on input.
        '''
        try:
            curses.nonl()
        except Exception, e:
            msg = 'nonl: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def noqiflush(self):
        '''
        When the noqiflush routine is used, normal flush of input and output
        queues associated with the INTR, QUIT and SUSP characters will not
        be done. You may want to call noqiflush() in a signal handler if
        you want output to continue as though the interrupt had not
        occurred, after the handler exits.
        '''
        try:
            curses.noqiflush()
        except Exception, e:
            msg = 'noqiflush: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def noraw(self):
        '''
        Leave raw mode. Return to normal "cooked" mode with line buffering.
        '''
        try:
            curses.noraw()
        except Exception, e:
            msg = 'noraw: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def pair_content(self, pair_number):
        '''
        Returns a tuple (fg, bg) containing the colors for the requested
        color pair. The value of pair_number must be between 1 and
        COLOR_PAIRS - 1.
        '''
        try:
            reply = curses.pair_content(pair_number)
        except Exception, e:
            reply = (7, 0)
            msg = 'pair_content: %d; %s' % (
                pair_number, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def pair_number(self, attr):
        '''
        Returns the number of the color-pair set by the attribute value
        attr. color_pair() is the counterpart to this function.
        '''
        try:
            reply = curses.pair_number(attr)
        except Exception, e:
            reply = 0
            msg = 'pair_number: %s; %s' % (
                str(attr), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def pflush(self, updateDisplay=False):
        '''
        Update the virtual screen after changes in the panel stack and
        then update the display.
        '''
        try:
            curses.panel.update_panels()
            if updateDisplay:
                curses.doupdate()
        except Exception, e:
            msg = 'pflush: updateDisplay=%s; %s' % (
                str(updateDisplay), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def putp(self, string):
        '''
        Equivalent to tputs(str, 1, putchar); emits the value of a specified
        terminfo capability for the current terminal. Note that the output
        of putp always goes to standard output.
        '''
        try:
            curses.putp(string)
        except Exception, e:
            msg = 'putp: %s; %s' % (
                str(string), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def qiflush(self, flag=True):
        '''
        If flag is false, the effect is the same as calling noqiflush().
        If flag is true, or no argument is provided, the queues will be
        flushed when these control characters are read.
        '''
        try:
            curses.qiflush(flag)
        except Exception, e:
            msg = 'qiflush: %s; %s' % (
                str(flag), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def raw(self):
        '''
        Enter raw mode. In raw mode, normal line buffering and processing
        of interrupt, quit, suspend, and flow control keys are turned
        off; characters are presented to curses input functions one by one.
        '''
        try:
            curses.raw()
        except Exception, e:
            msg = 'raw: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def reset_prog_mode(self):
        '''
        Restores the terminal to "program" mode, as previously saved by
        def_prog_mode().
        '''
        try:
            curses.reset_prog_mode()
        except Exception, e:
            msg = 'reset_prog_mode: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def reset_shell_mode(self):
        '''
        Restores the terminal to "shell" mode, as previously saved by
        def_shell_mode().
        '''
        try:
            curses.reset_shell_mode()
        except Exception, e:
            msg = 'reset_shell_mode: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def setsyx(self, y, x):
        '''
        Sets the virtual screen cursor to y, x. If y and x are both -1,
        then leaveok is set.
        '''
        try:
            curses.setsyx(y, x)
        except Exception, e:
            msg = 'setsyx: (%d, %d); %s' % (
                y, x, str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def setupterm(self, termstr, fd):
        '''
        Initializes the terminal. termstr is a string giving the terminal
        name; if omitted, the value of the TERM environment variable will
        be used. fd is the file descriptor to which any initialization
        sequences will be sent; if not supplied, the file descriptor for
        sys.stdout will be used.
        '''
        try:
            curses.setupterm(termstr, fd)
        except Exception, e:
            msg = 'setupterm: (%s, %s); %s' % (
                str(termstr), str(fd), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def start_color(self):
        '''
        Must be called if the programmer wants to use colors, and before
        any other color manipulation routine is called. It is good
        practice to call this routine right after initscr().
 
        start_color() initializes eight basic colors (black, red, green,
        yellow, blue, magenta, cyan, and white), and two global variables
        in the curses module, COLORS and COLOR_PAIRS, containing the
        maximum number of colors and color-pairs the terminal can support.
        It also restores the colors on the terminal to the values they had
        when the terminal was just turned on.
        '''
        try:
            curses.start_color()
        except Exception, e:
            msg = 'start_color: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def termattrs(self):
        '''
        Returns a logical OR of all video attributes supported by the
        terminal. This information is useful when a curses program needs
        complete control over the appearance of the screen.
        '''
        try:
            reply = curses.termattrs()
        except Exception, e:
            reply = 0
            msg = 'termattrs: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def termname(self):
        '''
        Returns the value of the environment variable TERM, truncated
        to 14 characters.
        '''
        try:
            reply = str(curses.termname())
        except Exception, e:
            reply = None
            msg = 'termname: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def tigetflag(self, capname):
        '''
        Returns the value of the Boolean capability corresponding to the
        terminfo capability name capname. The value -1 is returned if
        capname is not a Boolean capability, or 0 if it is canceled or
        absent from the terminal description.
        '''
        try:
            reply = curses.tigetflag(capname)
        except Exception, e:
            reply = -1
            msg = 'tigetflag: %s; %s' %(
                str(capname), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def tigetnum(self, capname):
        '''
        Returns the value of the numeric capability corresponding to the
        terminfo capability name capname. The value -2 is returned if
        capname is not a numeric capability, or -1 if it is canceled or
        absent from the terminal description.
        '''
        try:
            reply = curses.tigetnum(capname)
        except Exception, e:
            reply = -1
            msg = 'tigetnum: %s; %s' % (
                str(capname), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def tigetstr(self, capname):
        '''
        Returns the value of the string capability corresponding to the
        terminfo capability name capname. None is returned if capname is
        not a string capability, or is canceled or absent from the
        terminal description.
        '''
        try:
            reply = curses.tigetstr(capname)
        except Exception, e:
            reply = None
            msg = 'tigetstr: %s; %s' % (
                str(capname), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def tparm(self, *strarg):
        '''
        Instantiates the string str with the supplied parameters, where
        str should be a parameterized string obtained from the terminfo
        database. E.g. tparm(tigetstr("cup"), 5, 3) could result in
        "\033[6;4H", the exact result depending on terminal type.
        '''
        try:
            curses.tparm(strarg)
        except Exception, e:
            msg = 'tparm: %s; %s' % (
                str(strarg), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def typeahead(self, fd):
        '''
        Specifies that the file descriptor fd be used for typeahead
        checking. If fd is -1, then no typeahead checking is done.
        The curses library does "line-breakout optimization" by
        looking for typeahead periodically while updating the screen.
        If input is found, and it is coming from a tty, the current
        update is postponed until refresh or doupdate is called again,
        allowing faster response to commands typed in advance. This
        function allows specifying a different file descriptor for
        typeahead checking.
        '''
        try:
            curses.typeahead(fd)
        except Exception, e:
            msg = 'typeahead: %s; %s' % (
                str(fd), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------


    def unctrl(self, ch):
        '''
        Returns a string which is a printable representation of the
        character ch. Control characters are displayed as a caret
        followed by the character, for example as ^C. Printing
        characters are left as they are.
        '''
        try:
            reply = curses.unctrl(ch)
        except Exception, e:
            reply = None
            msg = 'unctrl: %s; %s' % (
                str(ch), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def ungetch(self, ch):
        '''
        Push ch so the next getch() will return it. Note: Only one ch
        can be pushed before getch() is called.
        '''
        try:
            curses.ungetch(ch)
        except Exception, e:
            msg = 'ungetch: %s; %s' % (
                str(ch), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def ungetmouse(self, id, x, y, z, bstate):
        '''
        Push a KEY_MOUSE event onto the input queue, associating the given
        state data with it.
        '''
        try:
            curses.ungetmouse(id, x, y, z, bstate)
        except Exception, e:
            msg = 'ungetmouse: (%s, %s, %s, %s, %s); %s' %(
                str(id), str(x), str(y), str(z), str(bstate), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def use_env(self, flag):
        '''
        If used, this function should be called before initscr() or
        newterm are called. When flag is false, the values of lines and
        columns specified in the terminfo database will be used, even
        if environment variables LINES and COLUMNS (used by default)
        are set, or if curses is running in a window (in which case
        default behavior would be to use the window size if LINES and
        COLUMNS are not set).
        '''
        try:
            curses.use_env(flag)
        except Exception, e:
            msg = 'use_env: %s; %s' % (
                str(flag), str(e))
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def use_default_colors(self):
        '''
        Allow use of default values for colors on terminals supporting this
        feature. Use this to support transparency in your application. The
        default color is assigned to the color number -1. After calling this
        function, init_pair(x, curses.COLOR_RED, -1) initializes, for
        instance, color pair x to a red foreground color on the default
        background.
        '''
        try:
            curses.use_default_colors()
        except Exception, e:
            msg = 'use_default_colors: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def tsGetCursesBottomPanel(self):
        '''
        Returns the bottom panel in the panel stack.
        '''
        return (curses.panel.bottom_panel())

    #-----------------------------------------------------------------------

    def tsGetCursesNewPanel(self, win):
        '''
        Returns a panel object, associating it with the given window win.
        Be aware that you need to keep the returned panel object referenced
        explicitly. If you do not, the panel object is garbage collected
        and removed from the panel stack.
        '''
        try:
            reply = curses.panel.new_panel(win)
        except Exception, e:
            reply = None
            msg = 'tsCursesNewPanel: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        return (reply)

    #-----------------------------------------------------------------------

    def tsGetCursesTopPanel(self):
        '''
        Returns the top panel in the panel stack.
        '''
        return (curses.panel.top_panel())

    #-----------------------------------------------------------------------

    def tsUpdateCursesPanels(self):
        '''
        Updates the virtual screen after changes in the panel stack.
        This does not call curses.doupdate(), so you will have to do
        this yourself.
        '''
        curses.panel.update_panels()

    #-----------------------------------------------------------------------

    def tsPrintDataBases(self):
        '''
        '''
        CursesDataBase = self.tsBuildCursesDataBase()
        GraphicalTextUserInterface.CursesDataBase = CursesDataBase

        WindowDataBase = self.tsBuildWindowDataBase()
        GraphicalTextUserInterface.WindowDataBase = WindowDataBase

        timestamp = tsru.getDateTimeString(time.time(), msec=True)

        renamedDBaseFileName = '%s/%s' % (
            tsLogger.TsLogger.defaultStandardOutputPath,
            defaultDBaseFileName.replace(
                'DBase',
                '%s-DBase' % GraphicalTextUserInterface.TermName))

        defaultDBaseFile = open(
            renamedDBaseFileName,
            defaultDBaseFileMode,
            1)

        defaultDBaseFile.write('%s\n\n' % str(__header__))

        defaultDBaseFile.write('%s - %s\n' % (
            timestamp,
            'Started logging to file "%s"' % renamedDBaseFileName))

        defaultDBaseFile.flush()

        tsru.displayDictionary(0,
                               GraphicalTextUserInterface.CursesDataBase,
                               defaultDBaseFile,
                               myLogger=None)

        defaultDBaseFile.flush()

        tsru.displayDictionary(0,
                               GraphicalTextUserInterface.WindowDataBase,
                               defaultDBaseFile,
                               myLogger=None)

        defaultDBaseFile.flush()

        timestamp = tsru.getDateTimeString(time.time(), msec=True)

        defaultDBaseFile.write('%s - %s\n' % (
            timestamp,
            'Ended logging to file "%s"' % renamedDBaseFileName))

        defaultDBaseFile.flush()

        defaultDBaseFile.close()

#---------------------------------------------------------------------------

if __name__ == '__main__':
 
    print(__header__)

#     ## Import Module
#     import tsWxGraphicalTextUserInterface as tsGTUI
    tsWxGraphicalTextUserInterface = GraphicalTextUserInterface
    tsGTUI = tsWxGraphicalTextUserInterface
#
#     ## Instantiate Module
#     theScreen = tsGTUI.GraphicalTextUserInterface(theClassName)
    theClassName = 'debug'
    theScreen = tsGTUI(theClassName)
#
#     ## Reference Module Methods
#     results = theScreen.runWrapper(mainProgram)

