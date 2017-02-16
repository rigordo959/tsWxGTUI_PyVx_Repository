#! /usr/bin/env python
# "Time-stamp: <09/15/2015  5:45:34 AM rsg>"
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
#       text characters:
#
#       Minimum Format: 60-column by 25-row;
#           based on SplashScreen component options in tsWxGlobals
#           (and associated content in tsCxGlobals):
#
#              theMasthead
#              theCopyright
#              theLicense
#              theNotices
#
#       Recommended Format: 80-column by 50-row;
#           based on MultiFrameEnv options in tsWxDisplay:
#
#              Application Frame    (Client Area)
#              StdIO Output Frame   (Optional)
#              Task Bar Outut Frame (Optional)
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
#       a) Apple Mac OS X (eg. 10.0-10.10 etc.)
#
#       b) Cygwin (eg. 1.6-1.7) running on Microsoft Windows
#          (eg. 8.1/8/7/Vista/XP/2000)
#
#       c) Linux (eg. CentOS, Fedora, Mandriva, OpenSUSE,
#          Red Hat, Scientific, Ubuntu etc.)
#
#       d) Unix (eg. Darwin, FreeBSD, HP-UX, OpenIndiana,
#          Solaris etc.)
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
#       vt100           keyboard          Black/White  extended characters
#       vt220           keyboard          Black/White  extended characters
#       xterm           keyboard  option      8-color  extended characters
#       xterm-16color   keyboard  option     16-color  extended characters
#
#    4. Optionally allows the operator to configure the terminal (TERM)
#       to one of the following (see tsLibGUI/tsWxPkg/src/tsWxGlobals.py
#       for site-specific options):
#
#       <--- TERM --->     <-------------------- FEATURE ------------------->
#       termcap            keyboard   mouse        color  extended characters
#       --------------     --------  ------  -----------  -------------------
#       ansi(1)            keyboard              8-color  extended characters
#       cygwin(2)          keyboard              8-color  extended characters
#       vt100(3)           keyboard          Black/White  extended characters
#       vt220(3)           keyboard          Black/White  extended characters
#       xterm(4)           keyboard  option      8-color  extended characters
#       xterm-color(4)     keyboard  option      8-color  extended characters
#       xterm-16color(4)   keyboard  option     16-color  extended characters
#       xterm-88color(4)   keyboard  option     88-color  extended characters
#       xterm-256color(4)  keyboard  option    256-color  extended characters
#
#       NOTES:
#
#         (1) The ANSI terminals create a multi-color display
#             with alpha-numeric and line draw characters which feature
#             character cells composed of an array of pixel triplets.
#             Each triplet is composed of Red, Green and Blue colored
#             pixels whose intensity could be "ON" or "OFF" (Black).
#             This created an 8-color palette.
#
#             However, none of the host computers provide ANSI terminal
#             emulator which creates border lines, as of 2014/01/18.
#
#         (2) The Cygwin terminal emulator creates a multi-color display
#             with alpha-numeric and line draw characters which feature
#             character cells composed of an array of pixel triplets.
#             Each triplet is composed of Red, Green and Blue colored
#             pixels whose intensity could be "ON" or "OFF" (Black).
#             This created an 8-color palette.
#
#             No Linux, Mac OS or Unix Cygwin terminal emulators creates
#             border lines, as of 2014/01/18.
#
#             Emulating "wxPython" requires support for the associated
#             68-color palette. The "tsExGTUI" Toolkit does this by
#             the application of a color substitution which maps each
#             "wxPython" color into the appropriate "Cygwin" color.
#
#         (3) These terminal emlators create a monochrome display that
#             mimics the original Digital Equiment Corporation
#             terminal which featured character cells composed of an
#             array of pixels. All pixels were of a single color
#             (Green, Orange or typically White) which could either
#             be "ON" or "OFF" (Black).
#
#         (4) These terminal emlators create a multi-color display
#             with alpha-numeric and line draw characters which feature
#             character cells composed of an array of pixel triplets.
#             Each triplet is composed of Red, Green and Blue colored
#             pixels whose intensity could be adjusted between
#             0 (Full "OFF") to 255 (Full "ON"). This created a
#             potential 16,777,216 colors of which the terminal
#             emulator supports a palette of 88 or 256 colors.
#
#             The xterm and xterm-color emulators support 8 colors.
#             Emulating "wxPython" requires support for the associated
#             68-color palette. The "tsExGTUI" Toolkit does this by
#             the application of a color substitution which maps each
#             "wxPython" color into the appropriate "xterm" color.
#
#             The xterm-16color emulators support 16 colors (8 in
#             addition to the 8 proved by the xterm). Emulating
#             "wxPython" requires support for an enhanced 71-color
#             palette. The "tsExGTUI" Toolkit does this by the
#             application of a color substitution mapping of each
#             "wxPython" color into the appropriate "xterm-16color"
#             color.
#
#             The following workarounds resolve as yet undocumented
#             limitations of the available Curses and nCurses
#             terminal control libraries, which otherwise results
#             in the display of text with the wrong color and
#             marred by unexpected underlines:
#
#             a. Contrary to expectations, the xterm-256color emulators
#                do NOT support 256 colors (240 in addition to the 16
#                provided by xterm-16color). The Terminal under the
#                GNOME Desktop for CentOS 7.0 Linux limited the number
#                of color pairs to 256, as of 2014/10/16. This is
#                only equivalent to support for xterm-16color palette
#                with an equivalent 71-color substitution mapping.
#                Had this not been the case, Curses would have imposed
#                a 32767 limit on the number of color pairs which would
#                have been equivalent to a 181 limit on the number of
#                colors. NOTE: While the USE_256_COLOR_PAIR_LIMIT is
#                True, code that would install a 170-color prototype
#                palette is disabled.             
#
#             b. Similarly, the xterm-88color emulators do NOT support
#                88 colors (72 in addition to the 16 provided by
#                xterm-16color). NOTE: While the USE_256_COLOR_PAIR_LIMIT
#                is True, code that would install a 71-color prototype
#                palette is disabled.
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
#           2014/10/23 rsg Added the following findings:
#
#           The curses terminal control library supports a maximum of
#           256 color pairs.
#
#           Attempting to exceed the 256 limit with Python 2.2.x-2.7.8
#           and with Python 3.0.x-3.2.x defines the correct color palete
#           but displays the wrong colors and spurious underline artifacts.
#
#           Attempting to exceed the 256 limit with Python 3.3.x defines
#           and displays only the xterm-16color palette.
#
#        4. wxPython Color Terminal Emulation development status:
#
#           For the latest status, see Microsoft Excel Spreadsheet
#           file:
#
#               "Platform_Configuration.xls".
#
#           It contains the following worksheets:
#
#               "Host_Configurations"
#               "Terminal_Configuration"
#
#           Copies of the Spreadsheet are located in the following
#           distribution documentation subdirectories:
#
#             ["./Python-2x/tsWxGTUI_Py2x/tsDocGUI/MS-Excel-Files"]
#             ["./Python-3x/tsWxGTUI_Py3x/tsDocGUI/MS-Excel-Files"]
#
# Classes:
#
#    1. CursesServices(object) - A class for defining features
#       of the Python "Curses" and "_curses" modules with
#       application-specific exception handlng.
#
#    2. GraphicalTextUserInterface(CursesServices) - A class for
#       defining features of text-based, graphical user interface.
#
# Methods:
#
#    .debug_via_tsrpu
#
#    CursesServices.__init__
#    CursesServices._prog_mode
#    CursesServices._shell_mode
#    CursesServices.baudrate
#    CursesServices.beep
#    CursesServices.can_change_color
#    CursesServices.cbreak
#    CursesServices.color_content
#    CursesServices.color_pair
#    CursesServices.curs_set
#    CursesServices.def_prog_mode
#    CursesServices.def_shell_mode
#    CursesServices.delay_output
#    CursesServices.doupdate
#    CursesServices.echo
#    CursesServices.endwin
#    CursesServices.erasechar
#    CursesServices.filter
#    CursesServices.flash
#    CursesServices.flushinp
#    CursesServices.getmouse
#    CursesServices.getsyx
#    CursesServices.getwin
#    CursesServices.halfdelay
#    CursesServices.has_colors
#    CursesServices.has_ic
#    CursesServices.has_il
#    CursesServices.has_key
#    CursesServices.init_color
#    CursesServices.init_pair
#    CursesServices.initscr
#    CursesServices.isendwin
#    CursesServices.keyname
#    CursesServices.killchar
#    CursesServices.longname
#    CursesServices.meta
#    CursesServices.mouseinterval
#    CursesServices.mousemask
#    CursesServices.napms
#    CursesServices.newpad
#    CursesServices.newwin
#    CursesServices.nl
#    CursesServices.nocbreak
#    CursesServices.noecho
#    CursesServices.nonl
#    CursesServices.noqiflush
#    CursesServices.noraw
#    CursesServices.pair_content
#    CursesServices.pair_number
#    CursesServices.pflush
#    CursesServices.putp
#    CursesServices.qiflush
#    CursesServices.raw
#    CursesServices.reset_prog_mode
#    CursesServices.reset_shell_mode
#    CursesServices.runWrapper
#    CursesServices.setsyx
#    CursesServices.setupterm
#    CursesServices.start
#    CursesServices.start_color
#    CursesServices.stop
#    CursesServices.termattrs
#    CursesServices.termname
#    CursesServices.tigetflag
#    CursesServices.tigetnum
#    CursesServices.tigetstr
#    CursesServices.tparm
#    CursesServices.typeahead
#    CursesServices.unctrl
#    CursesServices.ungetch
#    CursesServices.ungetmouse
#    CursesServices.use_default_colors
#    CursesServices.use_env
#
#    GraphicalTextUserInterface.__init__
#    GraphicalTextUserInterface._cleanupWhenSignalReceived
#    GraphicalTextUserInterface._sigAbrtHandler
#    GraphicalTextUserInterface._sigIntHandler
#    GraphicalTextUserInterface.tsBuildCursesDataBase
#    GraphicalTextUserInterface.tsBuildSplashScreen
#    GraphicalTextUserInterface.tsBuildWindowDataBase
#    GraphicalTextUserInterface.tsCreateColorPairs
#    GraphicalTextUserInterface.tsErrorConsole
#    GraphicalTextUserInterface.tsExitForTerminalNotSupported
#    GraphicalTextUserInterface.tsGetAttributeValueFromColorPair
#    GraphicalTextUserInterface.tsGetBuiltInColorCount
#    GraphicalTextUserInterface.tsGetBuiltInColorPalette
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
#    GraphicalTextUserInterface.tsGetSetToUseForColorSubstituteMap
#    GraphicalTextUserInterface.tsGetTopLevelApplication
#    GraphicalTextUserInterface.tsGetWxPythonColorContent
#    GraphicalTextUserInterface.tsInfoConsole
#    GraphicalTextUserInterface.tsInstallBuiltinColorDataBase
#    GraphicalTextUserInterface.tsInstallExtendedColorDataBase
#    GraphicalTextUserInterface.tsInstallMonochromeDataBase
#    GraphicalTextUserInterface.tsPrintDataBases
#    GraphicalTextUserInterface.tsPrintWindow
#    GraphicalTextUserInterface.tsSelectApplicableColorPalette
#    GraphicalTextUserInterface.tsSetCursesColorNumber
#    GraphicalTextUserInterface.tsSetCursesColorPair
#    GraphicalTextUserInterface.tsSetCursesCursor
#    GraphicalTextUserInterface.tsSetDefaultClientTerminalDataBase
#    GraphicalTextUserInterface.tsSetDetectedClientTerminalDataBase
#    GraphicalTextUserInterface.tsSetMouseButtonCodes
#    GraphicalTextUserInterface.tsSetTopLevelApplication
#    GraphicalTextUserInterface.tsStripDictionaryName
#    GraphicalTextUserInterface.tsUpdateCursesPanels
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
#                   those ExtendedColorDataBaseRGB names to which
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
#                   tsInstallBuiltinColorDataBase. Modified code
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
#    2014/07/02 rsg Revised self.tsInstallBuiltinColorDataBase method
#                   to apply self.can_change_color by using
#                   built-in colors rather than standard RGB values.
#
#    2014/07/05 rsg Modified self.tsGetColorPairNumber to consider
#                   reply from self.can_change_color() regarding
#                   applicability of Color16SubstitutionMap for
#                   xterm-88Color and xterm-256Color. There being
#                   applicability only when the platform, or test
#                   simulation, precludes changing the 16-color
#                   built-in palette.
#
#    2014/07/10 rsg Added attribute 'WindowsByCursesPanel' to
#                   'GraphicalTextUserInterface' and modified
#                   'start' to facilitate use of curses panel object
#                   id for anticipated use, by 'tsWxEventLoop',
#                   to determine the associated wxPython object
#                   id and curses panel stacking order.
#
#    2014/07/17 rsg Substituted distribution documentation references
#                   for the now obsolete platform and terminal
#                   configuration information.
#
#    2014/07/18 rsg Revised readme_bmp_text to describe the Extended
#                   Multi-Color support as EXPERIMENTAL because
#                   Terminal/Emulator standards only support 16 colors.
#
#    2014/10/15 rsg Modified start method. Added control switch
#                   CAPTURE_BUILTIN_COLORS to select whether to
#                   capture and log built-in color palette.
#
#    2014/10/15 rsg Modified start method. Added control switches
#                   self.ts_use_reported_number_of_color_pairs and
#                   self.ts_use_implicit_number_of_color_pairs to
#                   select whether color palette reflects the reported
#                   number of color pairs or the number of colors
#                   implicit in terminal emulator name. This was
#                   introduced to accomodate discovery that
#                   CentOS LInux 7.0 reported only 256 color pairs
#                   for xterm-256color with terminal utility
#                   provided with GNOME desktop.
#
#    2014/10/16 rsg Modified methods tsGetSetToUseForColorCodeFromName
#                   and tsGetSetToUseForColorNameFromCode to use control
#                   switches self.ts_use_reported_number_of_color_pairs
#                   and self.ts_use_implicit_number_of_color_pairs.
#                   Also commented-out raising of exception upon
#                   detection of unexpected configuration.
#
#    2014/10/17 rsg Added method tsGetSetToUseForColorSubstituteMap.
#
#    2014/10/23 rsg Added control switch "USE_256_COLOR_PAIR_LIMIT"
#                   to establish 256 as the maximum number of
#                   available color pairs (overriding the value
#                   reported by curses). As a consequence, the
#                   tsWxGTUI  Toolkit will apply the xterm-16color
#                   palette instead of the xterm-88color and
#                   xterm-256color palette which cannot otherwise
#                   be made to work.
#
#    2014/10/26 rsg Refactored start method in order to assure
#                   color mapping with "USE_256_COLOR_PAIR_LIMIT".
#
#    2014/11/16 rsg Updated copyright, license and notice data.
#                   Added logic to establish and use a Python
#                   version specific tsWxGTUI_PyVx for previous
#                   reference to "tsWxGTUI".
#
#    2014/11/20 rsg Renamed a method and reference to it in order
#                   clarify its functionality. Replaced
#                   "tsInstallDefaultColorDataBase" by 
#                   "tsInstallBuiltinColorDataBase".
#
#    2014/11/24 rsg Added 'linux' to the supported terminal emulator
#                   types.
#
#    2014/12/04 rsg Added logic to extract character and attribute
#                   from background of curses screen after initscr.
#
#    2015/01/05 rsg Added Windows 10 Technical Preview (English)
#                   to README_BMP.txt.
#
#    2015/01/14 rsg Moved Masthead (formerly called Trademark),
#                   Copyright, License and Notice text from
#                   tsWxGlobals to tsCxGlobals.
#
#    2015/01/15 rsg Modified start to enable keypad mode.
#
#    2015/03/17 rsg Extracted code associated with the definition
#                   of curses key codes from the module named
#                   tsWxGraphicalTextUserInterface.py into a
#                   new module named tsWxCursesKeyCodesDataBase.py
#                   to facilitate the editing and maintenance
#                   of both files.
#
#                   Added code to import the new module.
#
#    2015/03/17 rsg Extracted code associated with the definition 
#                   of curses mouse button codes from the module
#                   named tsWxGraphicalTextUserInterface.py into
#                   a new module named
#                   tsWxCursesMouseButtonCodesDataBase.py
#                   to facilitate the editing and maintenance
#                   of both files.
#
#                   Added code to import the new module.
#
#    2015/03/17 rsg Extracted code associated with low-level 
#                   curses services from the class named
#                   GraphicalTextUserInterface into a new
#                   class named CursesServices to facilitate
#                   the editing and maintenance of this file.
#
#    2015/08/01 rsg Updated "readme_bmp_text" doc string for
#                   official Microsoft Windows 10.0 release.
#
#    2015/09/15 rsg Added __init__ code to handle SIGWINCH
#                   when operator resizes the terminal.
#
#                   Also added _sigWinchHandler.
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
#    2014/07/04 rsg Resolve platform-dependent anomalies in
#                   xterm-16color palette.
#
#                   When curses.can_change_color is True, as with
#                   Cygwin on Windows 7 (using tsInstallExtended-
#                   ColorDataBase):
#                       "test_tsWxGraphicalTextUserInterface"
#                       generates expected 16 colors by defining
#                       the color name and RGB value for each code.
#
#                   When curses.can_change_color is False, as with
#                   Scientific Linux 6.5 (using tsInstallBuiltin-
#                   ColorDataBase):
#                       "test_tsWxGraphicalTextUserInterface"
#                       generates expected colors for codes 0-7.
#                       It generates incorrect colors for codes
#                       8-15. The built-in palette features a
#                       second black (renamed gray) for code 8.
#                       The names of the last 7 codes conform
#                       to the extended color palette but the
#                       RGB values do not represent the color.
#                       Perhaps the names for codes 0-7 should
#                       simply be interchanged with those for
#                       codes 8-15. The test display would then
#                       name and show the correct color but out
#                       of the normal code sequence.
#
#    2014/12/04 rsg Resolve the failure to recognize whether
#                   the initial curses terminal screen is
#                   black-on-white or white-on-black based on
#                   terminal emulator type. The criteria
#                   should NOT be based on the terminal emulator
#                   type (cygwin, xterm, xterm-16color etc.)
#                   but rather on which host OS and Terminal
#                   Window Manager or perhaps based on what
#                   curses.getbkg reports (the latter does not
#                   seem to yield useful information):
#
#                   a) It is white-on-black for Cygwin and Xterms
#                      under Windows 7-Cygwin operating system and
#                      console or mintty Terminal window application
#
#                   b) It is black-on-white for Cygwin and Xterms
#                      under Mac OS X 10.10 operating system and
#                      Terminal window application.
#
#                   c) It is black-on-white for Cygwin and Xterms
#                      under CentOS 7 operating system and Terminal
#                      window application.
#
#                   d) It is white-on-dark-gray for Cygwin and Xterms
#                      under Fedora 21 operating system and Terminal
#                      window application.
#
##############################################################

__title__     = 'tsWxGraphicalTextUserInterface'
__version__   = '2.44.0'
__date__      = '09/15/2015'
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
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t\t\tfor Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 Free Software ' + \
                '\n\t\t\tFoundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  nCurses README,v 1.23 2006/04/22' + \
                '\n\n\t  RGB to Color Name Mapping (Triplet and Hex)' + \
                '\n\t  Copyright (c) 2010 Kevin J. Walsh' + \
                '\n\t\t\tAll rights reserved.'

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

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsCxGlobals
    import tsExceptions as tse
    import tsLogger
    from tsReportUtilities import TsReportUtilities as tsrpu
    from tsSysCommands import TsSysCommands

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))


#--------------------------------------------------------------------------

try:

    import tsLibGUI

except ImportError as importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
    from tsWxGlobals import ThemeToUse as wxThemeToUse
    from tsWxGlobals import USE_256_COLOR_PAIR_LIMIT
    from tsWxPoint import Point as wxPoint
    from tsWxRect import Rect as wxRect
    from tsWxSize import Size as wxSize

    from tsWxCursesKeyCodesDataBase import *
    from tsWxCursesMouseButtonCodesDataBase import *

    from tsWxPythonColorRGBNames import *
    from tsWxPythonColorRGBValues import *
    from tsWxPythonColorNames import *
    from tsWxPythonColor16DataBase import *
    from tsWxPythonColor16SubstitutionMap import *
    from tsWxPythonColor256DataBase import *
    from tsWxPythonColor88DataBase import *
    from tsWxPythonColor8DataBase import *
    from tsWxPythonColor8SubstitutionMap import *
    from tsWxPythonColorDataBaseRGB import *
    from tsWxPythonMonochromeDataBase import *
    from tsWxPythonPrivateLogger import *

except ImportError as importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#---------------------------------------------------------------------------

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

except Exception as errorCode:

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
    ##   'Masthead': {
    ##       'name': 'Masthead',
    ##       'text': theMasthead,
    ##       'BackgroundColour': COLOR_BLACK,
    ##       'ForegroundColour': COLOR_WHITE
    ##       }
    ##   },

    use_tsCxGlobals = True
    if use_tsCxGlobals:

        theSplashScreenMasthead = tsCxGlobals.theMasthead
        theSplashScreenCopyright = tsCxGlobals.theCopyright
        theSplashScreenLicense = tsCxGlobals.theLicense
        theSplashScreenNotices = tsCxGlobals.theNotices

    else:

        theSplashScreenMasthead = splashScreenConfig['Masthead']['text']
        theSplashScreenCopyright = splashScreenConfig['Copyright']['text']
        theSplashScreenLicense = splashScreenConfig['License']['text']
        theSplashScreenNotices = splashScreenConfig['Notices']['text']

    theSplashScreenEnabled = splashScreenConfig['Enabled']
    theSplashScreenFileName = splashScreenConfig['Image']['FileName']
    theSplashScreenImage = splashScreenConfig['Image']
    theSplashScreenMakeReusable = splashScreenConfig['Image']['MakeReusable']
    theSplashScreenPath = splashScreenConfig['Image']['Path']
    theSplashScreenShowSeconds = splashScreenConfig['ShowSeconds']

    theCopyrightBackgroundColour = splashScreenConfig['Copyright'][
        'BackgroundColour']
    thLicenseBackgroundColour = splashScreenConfig['License'][
        'BackgroundColour']
    theNoticesBackgroundColour = splashScreenConfig['Notices'][
        'BackgroundColour']
    theMastheadBackgroundColour = splashScreenConfig['Masthead'][
        'BackgroundColour']

    theCopyrightForegroundColour = splashScreenConfig['Copyright'][
        'ForegroundColour']
    thLicenseForegroundColour = splashScreenConfig['License'][
        'ForegroundColour']
    theNoticesForegroundColour = splashScreenConfig['Notices'][
        'ForegroundColour']
    theMastheadForegroundColour = splashScreenConfig['Masthead'][
        'ForegroundColour']

    # 2014/01/29 rsg Automatically create theSplashScreenPath.
    mkdirsHead = theSplashScreenPath
    mkdirsMode = 0o777


    readme_bmp_text = '''# File: ".logs/bmp/README_BMP.txt"
# "Time-stamp: <08/01/2015  3:28:46 AM rsg>"

This "bmp" directory contains those Splash Screen(s) generated by:

  "/%s/tsLibGUI/tsWxPkg/src/tsWxGraphicalTextUserInterface.py.
    
using information defined in:

  "/%s/tsLibGUI/tsWxPkg/src/tsWxGlobals.py"

A splash screen is a display consisting of window containing a bit-mapped
image ("bmp") identifying the current version of the software and an ab-
stract of the terms and conditions of its use and redistribution. It
appears while a program is launching. Splash screens may cover the entire
screen, or simply a rectangle near the center of the screen.

Splash Screens are named for the display size (in character columns and
rows/lines), terminal/emulator type, and host operating system.

  Examples:

          Basic Multi-Color ("wxPython" transformation maps
            68-color palette into 8 or 16 built-in colors)

   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.0.bmp"         (Placeholder for
                                                            Windows 2000)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.1.bmp"         (Windows XP)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.2.bmp"         (Placeholder for
                                                            Windows XP x64)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-6.0.bmp"         (Placeholder for
                                                            Windows Vista)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-6.1.bmp"         (Windows 7)
   "SplashScreen-[60x15_LINUX]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[60x15_XTERM]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[60x15_XTERM-COLOR]-cygwin_nt-6.1.bmp"    (Windows 7)
   "SplashScreen-[80x15_XTERM-16COLOR]-cygwin_nt-6.2.bmp"  (Windows 8)
   "SplashScreen-[80x15_XTERM-88COLOR]-cygwin_nt-6.3.bmp"  (16x16 color
                                                            pair limit
                                                            for Windows 8.1)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-6.3.bmp" (16x16 color
                                                            pair limit
                                                            for Windows 8.1)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-10.0.bmp" (16x16 color
                                                            pair limit
                                                            for Windows 10)
   "SplashScreen-[60x15_XTERM]-cygwin_nt-10.0.bmp"         (Windows 10)

   "SplashScreen-[80x25_XTERM]-darwin.bmp"                 (Mac OS 10.9.1)

   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Fedora 21)
   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Ubuntu 12.04)

   "SplashScreen-[128x50_XTERM]-freebsd.bmp"               (PC-BSD 9.2)
   "SplashScreen-[128x50_XTERM]-sunos.bmp"                 (OpenIndiana 151a8)

      Non-Color ("wxPython" transformation maps 68-color palette
      into black with one shade of the default color for displays
      having only a white, orange or green phosphor).

   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.0.bmp"          (Placeholder for
                                                            Windows 2000)
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.1.bmp"          (Windows XP)
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.2.bmp"          (Placeholder for
                                                            Windows XP x64)
   "SplashScreen-[80x40_VT100]-cygwin_nt-6.0.bmp"          (Placeholder for
                                                            Windows Vista)
   "SplashScreen-[80x15_VT100]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[80x15_VT100]-cygwin_nt-6.2.bmp"          (Windows 8)
   "SplashScreen-[80x15_VT220]-cygwin_nt-6.3.bmp"          (Windows 8.1)
   "SplashScreen-[80x15_VT220]-cygwin_nt-10.0.bmp"         (Windows 10)

      #########################################################
      # Advanced Multi-Color support is still evolving....    #
      #                                                       #
      # Terminal/Emulator standards support an undocumented   #
      # maximum of 256 color pairs. This inference resulted   #
      # from the following observations.                      #
      #                                                       #
      # Under Python 2.x and Python 3.x, most xterm-88color   #
      # and xterm-256color terminal emlators produced the     #
      # wrong colors marred by spurious umderline artifacts.  #
      #                                                       #
      # Under Python 3.3.0 with a Yosemite Mac OS X Terminal  #
      # utility, there were 256 color pairs and a 16-color    #
      # palette that worked.                                  #
      #                                                       #
      # Also, under the Python 2.7.6 with the GNOME Desktop   #
      # for CentOS 7.0 Linux, there were 256 color pairs and  #
      # a 16-color palette that worked    .                   #
      #                                                       #
      # For the color pair matrix used by the "tsWxGTUI"      #
      # Toolkit, the Advanced Multi-Color support emulates    #
      # xterm-16color and associated mapping of the wxPython  #
      # 68-color palette into the built-in 16 colors.         #
      #########################################################

   if (COLOR_PAIRS > 256) and \
      (USE_256_COLOR_PAIR_LIMIT):    # As set in tsWxGlobals.py

      Advanced Multi-Color ("wxPython" emulation maps
      68-color palette into 16 of 88 or 16 of 256 colors)

   elif (COLOR_PAIRS == 256)         # As reported by curses

      Advanced Multi-Color ("wxPython" emulation maps
      68-color palette into 16 of 88 or 16 of 256 colors)

   else:

      Advanced Multi-Color ("wxPython" emulation maps
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
have outlived their usefulness.''' % (tsWxGTUI_PyVx, tsWxGTUI_PyVx)

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
        except IOError as e:
            sys.stderr.write('WARNING: <%s>' % str(e))

    except Exception as e:
        sys.stderr.write('EXCEPTION: <%s>' % str(e))

except Exception as errorCode:

    print('%s: Configuration Error (wx.ThemeToUse); ' % __title__ + \
          'importCode=%s' % str(errorCode))

#---------------------------------------------------------------------------

### TermCap Categorizations
##BlackOnWhiteDefault = [
##     'xterm-256color',
##     'xterm-88color',
##     'xterm-16color',
##     'xterm-color',
##     'xterm',
##     'ansi']

##WhiteOnBlackDefault = [
##     'cygwin',
##     'vt100',
##     'vt220']

##nonColorTerminals  = [
##     'vt100',
##     'vt220']

### High quality support of keyboard, display and optional mouse.
##supportedTermCaps = [
##    'cygwin',
##    'vt100',
##    'vt220',
##    'xterm',
##    'xterm-color',
##    'xterm-16color'
##    ]

### xterm-88color plagued by extraneous lines around reverse video text on:
###     Mac OS X with "X11" ("iterm" & "Terminal") applications.
###     Ubuntu "X11" ("Terminal") applications.
###     Cygwin "X11" ("Terminal") applications.
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
    
except ImportError as theImportError:

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

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

# 2014/06/07 rsg Added DEBUG_TerminalRunTimeEnvironment and modified
#                start to disable tsInstallBasicColorDataBase while
#                enabling tsInstallExtendedColorDataBase for terminal
#                emulators "cygwin", "xterm", "xterm-color" and
#                "xterm-16color" to confirm operability of the
#                tsInstallExtendedColorDataBase design when number
#                of colors <= 16.
##DEBUG_TerminalRunTimeEnvironment = False  # Set True only for testing

# 2014/07/04 rsg Added control switches to facilitate testing of
# extended color paletts on those platforms which do not otherwise
# prevent applications from changing the 8-color and 16-color palettes.
##DEBUG_tsInstallExtendedColorDataBase = False  # False unless troubleshooting
##                                              # xterm-88color/xterm-256color
DEBUG_tsInstallExtendedColorDataBase = True

##enable_tsInstallExtendedColorDataBase = False # Set True only for testing
enable_tsInstallExtendedColorDataBase = True

# 2014/07/04 rsg Added control switch to facilitate testing of default
# (built-in) color palette on those platforms which do not otherwise
# prevent applications from changing the 8-color and 16-color palettes.
##FIX_ME_cannot_change_color = False            # Set True only for testing
FIX_ME_cannot_change_color = False

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
#       self.tsInstallBuiltinColorDataBase()

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
#           self.tsInstallBuiltinColorDataBase()

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

if DEBUG_tsInstallExtendedColorDataBase:

    myLogger = tsLogger.TsLogger(name='',
                                 threshold=tsLogger.INFO) 

    myFile = open(os.path.join(myLogger.theLogPath,
                               'debug_via_tsrpu.log'), 'w')

    def debug_via_tsrpu(myIndent=0, myDictionary=None, myConsole=sys.stdout):
        tsrpu.displayDictionary(0, myDictionary, myFile)

else:

    def debug_via_tsrpu(myIndent=0, myDictionary='', myConsole=sys.stdout):
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

# Set of video display features that curses guarantees to recognize
DISPLAY_BLINK = curses.A_BLINK
DISPLAY_BOLD = curses.A_BOLD
DISPLAY_DIM = curses.A_DIM
DISPLAY_NORMAL = curses.A_NORMAL
DISPLAY_REVERSE = curses.A_REVERSE
DISPLAY_STANDOUT = curses.A_STANDOUT
DISPLAY_UNDERLINE = curses.A_UNDERLINE

##from tsWxPythonColorRGBNames import *

##from tsWxPythonColorRGBValues import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n ExtendedColorDataBaseRGB=%s' % str(
        ExtendedColorDataBaseRGB))
    debug_via_tsrpu(myDictionary=ExtendedColorDataBaseRGB)

##from tsWxPythonColorNames import *

##from tsWxPythonColorDataBaseRGB import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n wxPythonColorDataBaseRGB=%s' % str(
        wxPythonColorDataBaseRGB))
    debug_via_tsrpu(myDictionary=wxPythonColorDataBaseRGB)

##from tsWxPythonColor8SubstitutionMap import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n Color8SubstitutionMap=%s' % str(
        Color8SubstitutionMap))
    debug_via_tsrpu(myDictionary=Color8SubstitutionMap)

##from tsWxPythonColor16SubstitutionMap import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n Color16SubstitutionMap=%s' % str(
        Color16SubstitutionMap))
    debug_via_tsrpu(myDictionary=Color16SubstitutionMap)

##from tsWxPythonMonochromeDataBase import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n cursesMonochromeNameFromCode=%s' % str(
        cursesMonochromeNameFromCode))
    debug_via_tsrpu(myDictionary=cursesMonochromeNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n cursesMonochromeCodeFromName=%s' % str(
        cursesMonochromeCodeFromName))
    debug_via_tsrpu(myDictionary=cursesMonochromeCodeFromName)

##from tsWxPythonColor8DataBase import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8ColorNameFromCode=%s' % str(
        xterm8ColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm8ColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8ColorCodeFromName=%s' % str(
        xterm8ColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm8ColorCodeFromName)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8BuiltinColorNameFromCode=%s' % str(
        xterm8BuiltinColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm8BuiltinColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm8BuiltinColorCodeFromName=%s' % str(
        xterm8BuiltinColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm8BuiltinColorCodeFromName)

##from tsWxPythonColor16DataBase import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16ColorNameFromCode=%s' % str(
        xterm16ColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm16ColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16ColorCodeFromName=%s' % str(
        xterm16ColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm16ColorCodeFromName)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16BuiltinColorNameFromCode=%s' % str(
        xterm16BuiltinColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm16BuiltinColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm16BuiltinColorCodeFromName=%s' % str(
        xterm16BuiltinColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm16BuiltinColorCodeFromName)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm88ColorNameFromCode=%s' % str(
        xterm88ColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm88ColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm88ColorCodeFromName=%s' % str(
        xterm88ColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm88ColorCodeFromName)

##from tsWxPythonColor256DataBase import *

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm256ColorNameFromCode=%s' % str(
        xterm256ColorNameFromCode))
    debug_via_tsrpu(myDictionary=xterm256ColorNameFromCode)

if DEBUG_tsInstallExtendedColorDataBase:
    print('\n\n xterm256ColorCodeFromName=%s' % str(
        xterm256ColorCodeFromName))
    debug_via_tsrpu(myDictionary=xterm256ColorCodeFromName)

##from tsWxPythonPrivateLogger import *

#---------------------------------------------------------------------------

class CursesServices(object):
    '''
    '''

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        '''
        pass

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
        except Exception as e:
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
        except Exception as e:
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
          if FIX_ME_cannot_change_color:
              reply = False
          else:
              reply = curses.can_change_color()
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
            except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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

        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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

        except Exception as e:

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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
            except Exception as e:
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
            except Exception as e:
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

        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
            reply = curses.longname().decode("ascii", "strict") 
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
            reply = curses.termname().decode("ascii", "strict")
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
            msg = 'use_default_colors: %s' % str(e)
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

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
            self.ts_wxPython_panels = {}
            self.ts_wxPython_panels['name'] = 'wxPythonPanels'

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

##                    self.ts_stdscr.keypad(0) # Disable keypad mode
                    self.ts_stdscr.keypad(1) # Enable keypad mode

                except Exception as e:

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

            value = self.ts_stdscr.getbkgd()
            characterValue = (value & 0xFF00) >> 8
            attributeValue = (value & 0x00FF)
            self.logger.debug('str(getbkgd)="%s"; type="%s", 0x%X, 0x%X' % (
                str(value), str(type(value)), characterValue, attributeValue))

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
            except Exception as e:
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

                self.tsGetBuiltInColorPalette()

                if self.ts_can_change_color:

                    self.tsSelectApplicableColorPalette()
                    self.tsInstallExtendedColorDataBase()

                else:

                    self.tsSelectApplicableColorPalette()
                    self.tsInstallBuiltinColorDataBase()

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
                can_change_color=self.ts_can_change_color,
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
            except Exception as e:
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

            except Exception as themeErrorCode:

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

            except IOError as ioErrorCode:

                bitmap = None
                self.logger.debug('Splash Screen File IOError: %s' % str(
                    ioErrorCode))

                self.tsBuildSplashScreen()

                time.sleep(theSplashScreenShowSeconds)

            except curses.error as splashScreenErrorCode:

                bitmap.close()
                self.logger.error('Splash Screen GetWin Error: %s' % str(
                    splashScreenErrorCode))

            except Exception as otherErrorCode:

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
            except Exception as e:
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
#---------------------------------------------------------------------------

class GraphicalTextUserInterface(CursesServices):
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

    WindowsByCursesPanel = {}
    WindowsByCursesPanel['name'] = 'WindowsByCursesPanel'

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

    # Added 2015/01/25
    WindowAssignedIdByCursesPanelLayer = {}
    WindowAssignedIdByCursesPanelLayer[
        'name'] = 'WindowAssignedIdByCursesPanelLayer'

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
            signal.signal(signal.SIGWINCH, self._sigWinchHandler)

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
            except Exception as e:
                try:
                    self.logger = PrivateLogger()
                    self.ts_has_logger = True
                    GraphicalTextUserInterface.HasLogger = self.ts_has_logger
                except Exception as e:
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

            except Exception as startError:

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
 
    def _sigWinchHandler(self, dummy, unused):
        '''
        Resize Curses-based GUI on SIGWINCH.
        '''
        try:
            self.logger.warning('Received SIGWINCH')
        except AttributeError:
            pass
 
        self._resizeWhenSignalReceived()

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
 
    def _resizeWhenSignalReceived(self):
        '''
        Resize or shutdown cleanly on signal.
        '''
        fmt1 = "%s" % __title__
        fmt2 = "_resizeWhenSignalReceived"
        fmt3 = "SIGWINCH handler NOT implemented"
        msg = "%s.%s: %s." % (fmt1, fmt2, fmt3)
        print(msg)
        self.logger.error(msg)
        self.stop()
        exit(0)

    #-----------------------------------------------------------------------

    def tsBuildSplashScreen(self):
        '''
        Build the SplashScreen to fit available screen.

        1. Traditional (Color SVGA) application SplashScreens:
           (1024 x 768 pixel) / (128 columns x 64 rows)
           include a Masthead, Copyright and License.

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


        splashScreenMasthead = []
        linesMasthead = theSplashScreenMasthead.split('\n')
        maxMastheadWidth = 0
        maxMastheadHeight = 0
        for aLine in linesMasthead:
            maxMastheadWidth = max(
                maxMastheadWidth, len(aLine))
            maxMastheadHeight += 1
            splashScreenMasthead += [aLine]
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxMastheadWidth=%d; maxMastheadHeight=%d' % (
                maxMastheadWidth, maxMastheadHeight))

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
        # if (space becomes ample at 60 cols x 42 rows):
        #    1. masthead
        #    2. copyright
        #    3. license
        #
        # elif space becomes usable at 60 cols x 32 rows:
        #    1. copyright
        #    2. license
        #
        # elif space becomes marginal at 60 cols x 14 rows:
        #    1. See "Notice.txt" file...
        #
        # else space becomes unusable below 60 cols x 14 rows:
        #    1. Report and trap operator configuration error

        maxHeight = (maxMastheadHeight + \
                     maxCopyrightHeight + \
                     maxLicenseHeight)

        maxWidth = max(maxMastheadWidth,
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
                theMastheadForegroundColour, theMastheadBackgroundColour)
            for currentText in linesMasthead:
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

            except Exception as errorCode:

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

            if ((self.ts_termname.lower() == 'cygwin') or \
                (self.ts_termname.lower() == 'xterm') or \
                (self.ts_termname.lower() == 'xterm-color')):

                # if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorCodeFromName)

                    set_to_use_name = 'xterm8ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm8BuiltinColorCodeFromName'

            elif (self.ts_termname.lower() == 'xterm-16color'):

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorCodeFromName)

                    set_to_use_name = 'xterm16ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm16BuiltinColorCodeFromName'

            elif (self.ts_termname.lower() == 'xterm-88color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    if self.can_change_color():

                        set_to_use = self.tsStripDictionaryName(
                            xterm16ColorCodeFromName)

                        set_to_use_name = 'xterm16ColorCodeFromName'

                    else:

                        set_to_use = self.tsStripDictionaryName(
                            xterm16BuiltinColorCodeFromName)

                        set_to_use_name = 'xterm16BuiltinColorCodeFromName'

                else:

                    # Though self.ts_curses_colors == 88, there is only
                    # capacity to define and mix 181 colors.
                    # (wxPython emulation supports 71 of 88 colors).
                    set_to_use = self.tsStripDictionaryName(
                        xterm88ColorCodeFromName)

                    set_to_use_name = 'xterm88ColorCodeFromName'

            elif (self.ts_termname.lower() == 'xterm-256color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    if self.can_change_color():

                        set_to_use = self.tsStripDictionaryName(
                            xterm16ColorCodeFromName)

                        set_to_use_name = 'xterm16ColorCodeFromName'

                    else:

                        set_to_use = self.tsStripDictionaryName(
                            xterm16BuiltinColorCodeFromName)

                        set_to_use_name = 'xterm16BuiltinColorCodeFromName'

                else:

                    # Though self.ts_curses_colors == 256, there is only
                    # capacity to define and mix 181 colors
                    # (wxPython emulation supports 140 of 256 colors).
                    set_to_use = self.tsStripDictionaryName(
                        xterm256ColorCodeFromName)

                    set_to_use_name = 'xterm256ColorCodeFromName'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 8) or \
                   (self.ts_curses_color_pairs == 64))):

                # if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorCodeFromName)

                    set_to_use_name = 'xterm8ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm8BuiltinColorCodeFromName'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 16) or \
                   (self.ts_curses_color_pairs == 256))):

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorCodeFromName)

                    set_to_use_name = 'xterm16ColorCodeFromName'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorCodeFromName)

                    set_to_use_name = 'xterm16BuiltinColorCodeFromName'

            else:

                fmt1 = 'tsGetSetToUseForColorCodeFromName '
                fmt2 = '(unexpected configuration): \n'
                fmt3 = '\t has_colors=%s \n' % self.ts_has_colors
                fmt4 = '\t can_change_color=%s \n' % self.can_change_color()
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
        fmt3 = '\t can_change_color=%s \n' % self.can_change_color()
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

            if ((self.ts_termname.lower() == 'cygwin') or \
                (self.ts_termname.lower() == 'xterm') or \
                (self.ts_termname.lower() == 'xterm-color')):

                # if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorNameFromCode)

                    set_to_use_name = 'xterm8ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm8BuiltinColorNameFromCode'

            elif (self.ts_termname.lower() == 'xterm-16color'):

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorNameFromCode)

                    set_to_use_name = 'xterm16ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm16BuiltinColorNameFromCode'

            elif (self.ts_termname.lower() == 'xterm-88color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    if self.can_change_color():

                        set_to_use = self.tsStripDictionaryName(
                            xterm16ColorNameFromCode)

                        set_to_use_name = 'xterm16ColorNameFromCode'

                    else:

                        set_to_use = self.tsStripDictionaryName(
                            xterm16BuiltinColorNameFromCode)

                        set_to_use_name = 'xterm16BuiltinColorNameFromCode'

                else:

                    # Though self.ts_curses_colors == 88, there is only
                    # capacity to define and mix 181 colors.
                    # (wxPython emulation supports 71 of 88 colors).
                    set_to_use = self.tsStripDictionaryName(
                        xterm88ColorNameFromCode)

                    set_to_use_name = 'xterm88ColorNameFromCode'

            elif (self.ts_termname.lower() == 'xterm-256color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    if self.can_change_color():

                        set_to_use = self.tsStripDictionaryName(
                            xterm16ColorNameFromCode)

                        set_to_use_name = 'xterm16ColorNameFromCode'

                    else:

                        set_to_use = self.tsStripDictionaryName(
                            xterm16BuiltinColorNameFromCode)

                        set_to_use_name = 'xterm16BuiltinColorNameFromCode'

                else:

                    # Though self.ts_curses_colors == 256, there is only
                    # capacity to define and mix 181 colors
                    # (wxPython emulation supports 140 of 256 colors).
                    set_to_use = self.tsStripDictionaryName(
                        xterm256ColorNameFromCode)

                    set_to_use_name = 'xterm256ColorNameFromCode'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 8) or \
                   (self.ts_curses_color_pairs == 64))):

                # if self.ts_curses_colors == 8:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm8ColorNameFromCode)

                    set_to_use_name = 'xterm8ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm8BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm8BuiltinColorNameFromCode'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 16) or \
                   (self.ts_curses_color_pairs == 256))):

                # if self.ts_curses_colors == 16:

                if self.can_change_color():

                    set_to_use = self.tsStripDictionaryName(
                        xterm16ColorNameFromCode)

                    set_to_use_name = 'xterm16ColorNameFromCode'

                else:

                    set_to_use = self.tsStripDictionaryName(
                        xterm16BuiltinColorNameFromCode)

                    set_to_use_name = 'xterm16BuiltinColorNameFromCode'

            else:

                fmt1 = 'tsGetSetToUseForColorNameFromCode '
                fmt2 = '(unexpected configuration): \n'
                fmt3 = '\t has_colors=%s \n' % self.ts_has_colors
                fmt4 = '\t can_change_color=%s \n' % self.can_change_color()
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
        fmt3 = '\t can_change_color=%s \n' % self.can_change_color()
        fmt4 = '\t curses_colors=%s \n' % self.ts_curses_colors
        fmt5 = '\t set_to_use_name=%s' % set_to_use_name
        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
        self.logger.alert(msg)

        return (set_to_use)

    #-----------------------------------------------------------------------

    def tsGetSetToUseForColorSubstituteMap(self):
        '''
        Return the set_to_use appropriate for the current terminal
        emulator.
        '''
        if self.ts_has_colors:

            if ((self.ts_termname.lower() == 'cygwin') or \
                (self.ts_termname.lower() == 'xterm') or \
                (self.ts_termname.lower() == 'xterm-color')):

                # if self.ts_curses_colors == 8:

                set_to_use = Color8SubstitutionMap

                set_to_use_name = 'Color8SubstitutionMap'

            elif (self.ts_termname.lower() == 'xterm-16color'):

                set_to_use = Color16SubstitutionMap

                set_to_use_name = 'Color16SubstitutionMap'

            elif (self.ts_termname.lower() == 'xterm-88color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    set_to_use = Color16SubstitutionMap

                    set_to_use_name = 'Color16SubstitutionMap'

                else:

                    # Though self.ts_curses_colors == 88, there is only
                    # capacity to define and mix 181 colors.
                    # (wxPython emulation supports 71 of 88 colors).

                    set_to_use = None

                    set_to_use_name = 'No Color88SubstitutionMap'

            elif (self.ts_termname.lower() == 'xterm-256color'):

                if ((self.ts_curses_color_pairs == 256) or \
                    (USE_256_COLOR_PAIR_LIMIT)):

                    set_to_use = Color16SubstitutionMap

                    set_to_use_name = 'Color16SubstitutionMap'

                else:

                    # Though self.ts_curses_colors == 88, there is only
                    # capacity to define and mix 181 colors.
                    # (wxPython emulation supports 71 of 88 colors).

                    set_to_use = None

                    set_to_use_name = 'No Color88SubstitutionMap'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 8) or \
                   (self.ts_curses_color_pairs == 64))):

                # if self.ts_curses_colors == 8:

                set_to_use = Color8SubstitutionMap

                set_to_use_name = 'Color8SubstitutionMap'

            elif ((self.ts_termname.lower() == 'linux') and \
                  ((self.ts_curses_colors == 16) or \
                   (self.ts_curses_color_pairs == 256))):

                # if self.ts_curses_colors == 16:

                set_to_use = Color16SubstitutionMap

                set_to_use_name = 'Color16SubstitutionMap'

            else:

                fmt1 = 'tsGetSetToUseForColorSubstituteMap '
                fmt2 = '(unexpected configuration): \n'
                fmt3 = '\t has_colors=%s \n' % self.ts_has_colors
                fmt4 = '\t can_change_color=%s \n' % self.can_change_color()
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
        fmt3 = '\t can_change_color=%s \n' % self.can_change_color()
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
        termname=EmptyString
        ):
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

            # Added 2015/01/25
            'WindowAssignedIdByCursesPanelLayer': \
            GraphicalTextUserInterface.WindowAssignedIdByCursesPanelLayer,

            'WindowsByPanelLayer': \
            GraphicalTextUserInterface.WindowsByPanelLayer,

            'WindowsByShowOrder': \
            GraphicalTextUserInterface.WindowsByShowOrder,

            'WindowsByCursesPanel': \
            GraphicalTextUserInterface.WindowsByCursesPanel,

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

        except Exception as e:

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

            theColorSubstututeMap = self.tsGetSetToUseForColorSubstituteMap()

            if self.ts_curses_colors == 8:

                # ColorSubstitutionDataBase does exist
                foregroundMap = theColorSubstututeMap[foreground]
                backgroundMap = theColorSubstututeMap[background]

            elif self.ts_curses_colors == 16:

                # ColorSubstitutionDataBase does exist
                foregroundMap = theColorSubstututeMap[foreground]
                backgroundMap = theColorSubstututeMap[background]

##            elif ((USE_256_COLOR_PAIR_LIMIT) and \
##                  (self.ts_curses_color_pairs >= 256)):

            elif ((USE_256_COLOR_PAIR_LIMIT) or \
                  (self.ts_curses_color_pairs == 256)):

                # ColorSubstitutionDataBase does exist
                foregroundMap = theColorSubstututeMap[foreground]
                backgroundMap = theColorSubstututeMap[background]

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

            except Exception as e:

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

    def tsSelectApplicableColorPalette(self):
        '''
        '''

        if self.ts_use_reported_number_of_color_pairs:

            # Begin self.ts_use_reported_number_of_color_pairs

            # Assumes that terminal emulator might support
            # fewer number of colors than specified by name. 
            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if self.ts_curses_colors < len(set_to_use):

                fmt1 = 'tsSelectApplicableColorPalette ' + \
                       'in %s:'  % __title__
                fmt2 = 'Too few colors %d < %d.' % (
                    self.ts_curses_colors,
                    len(set_to_use))
                msg = '%s %s' % (fmt1, fmt2)
                self.logger.error('   %s' % msg)
                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

            elif (self.ts_curses_colors == 8):

                if self.ts_can_change_color:

                    # Can change the 8 colors by defining
                    # Codes, Names and RGB Values for 8 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 8.
                    #
                    #   2  Number of Color Pairs is limited to 64.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 8 colors.
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 8 colors by defining
                    # Codes, Names and RGB Values for 8 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 8.
                    #
                    #   2  Number of Color Pairs is limited to 64.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 8 colors.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            elif (((self.ts_curses_colors == 16) or \
                   (self.ts_curses_color_pairs == 256)) or \
                  ((USE_256_COLOR_PAIR_LIMIT) and \
                   (self.ts_curses_colors > 16))):

                # When self.ts_curses_color_pairs >= 256, there is only
                # capacity to define and mix 16 colors.

                if self.ts_can_change_color:

                    # Can change the 16 colors by defining
                    # Codes, Names and RGB Values for 16 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 16 colors.
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 16 colors by defining
                    # Codes, Names and RGB Values for 16 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 16 colors.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            elif (self.ts_curses_colors == 88):

                if self.ts_can_change_color:

                    # Can change the 88 colors by defining
                    # Codes, Names and RGB Values for 68+ set of
                    # wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 88.
                    #
                    #   2  Number of Color Pairs is limited to 7744.
                    #
                    #   3. Unknown cause for anomalies of wrong colors
                    #      and text attibutes (spurious underlines).
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 88 colors.
                    #
                    # Codes, Names and RGB Values preset only for
                    # xterm-16color.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

##                    elif ((self.ts_curses_colors == 16) or \
##                          ((USE_256_COLOR_PAIR_LIMIT) and \
##                           (self.ts_curses_color_pairs >= 256))):

            elif (self.ts_curses_colors == 256):

                if self.ts_can_change_color:

                    # Can change the 256 colors by defining
                    # Codes, Names and RGB Values for 68+ set of
                    # wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 181.
                    #
                    #   2  Number of Color Pairs is limited to 32767.
                    #
                    #   3. Unknown cause for anomalies of wrong colors
                    #      and text attibutes (spurious underlines).
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 256 colors.
                    #
                    # Codes, Names and RGB Values preset only for
                    # xterm-16color.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            else:

                fmt1 = 'tsSelectApplicableColorPalette ' + \
                       'in %s:'  % __title__
                fmt2 = 'Too many colors %d > %d.' % (
                    self.ts_curses_colors,
                    len(set_to_use))
                msg = '%s %s' % (fmt1, fmt2)
                self.logger.error('   %s' % msg)
                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)
            # End self.ts_use_reported_number_of_color_pairs

        else:

            # Begin self.ts_use_implicit_number_of_color_pairs

            # Assumes that terminal emulator always supports
            # the number of colors specified by name. 

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            if self.ts_curses_colors < len(set_to_use):

                fmt1 = 'tsSelectAdvancedDefaultColorPalette ' + \
                       'in %s:'  % __title__
                fmt2 = 'Too few colors %d < %d.' % (
                    self.ts_curses_colors,
                    len(set_to_use))
                msg = '%s %s' % (fmt1, fmt2)
                self.logger.error('   %s' % msg)
                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

            elif self.ts_curses_colors == 8:

                if self.ts_can_change_color:

                    # Can change the 8 colors by defining
                    # Codes, Names and RGB Values for 8 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 8.
                    #
                    #   2  Number of Color Pairs is limited to 64.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 8 colors.
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 8 colors by defining
                    # Codes, Names and RGB Values for 8 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 8.
                    #
                    #   2  Number of Color Pairs is limited to 64.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 8 colors.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            elif (self.ts_curses_colors == 16):

                # When self.ts_curses_color_pairs >= 256, there is only
                # capacity to define and mix 16 colors.

                if self.ts_can_change_color:

                    # Can change the 16 colors by defining
                    # Codes, Names and RGB Values for 16 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 16 colors.
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 16 colors by defining
                    # Codes, Names and RGB Values for 16 of
                    # 68+ set of wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    #
                    #   3. Must provide mapping of 68+ set of
                    #      wxPython colors into set of 16 colors.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            elif (self.ts_curses_colors == 88):

                if self.ts_can_change_color:

                    # Can change the 88 colors by defining
                    # Codes, Names and RGB Values for 68+ set of
                    # wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 88.
                    #
                    #   2  Number of Color Pairs is limited to 7744.
                    #
                    #   3. Unknown cause for anomalies of wrong colors
                    #      and text attibutes (spurious underlines).
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 88 colors.
                    #
                    # Codes, Names and RGB Values preset only for
                    # xterm-16color.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            elif (self.ts_curses_colors == 256):

                if self.ts_can_change_color:

                    # Can change the 256 colors by defining
                    # Codes, Names and RGB Values for 68+ set of
                    # wxPython colors.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 181.
                    #
                    #   2  Number of Color Pairs is limited to 32767.
                    #
                    #   3. Unknown cause for anomalies of wrong colors
                    #      and text attibutes (spurious underlines).
                    self.ts_has_default_colors = False
                    self.tsInstallExtendedColorDataBase()

                else:

                    # Cannot change the 256 colors.
                    #
                    # Codes, Names and RGB Values preset only for
                    # xterm-16color.
                    #
                    # NOTES:
                    #
                    #   1. Number of Colors is limited to 16.
                    #
                    #   2  Number of Color Pairs is limited to 256.
                    self.ts_has_default_colors = True
                    self.tsInstallBuiltinColorDataBase()

            else:

                fmt1 = 'tsSelectAdvancedDefaultColorPalette ' + \
                       'in %s:'  % __title__
                fmt2 = 'Too many colors %d > %d.' % (
                    self.ts_curses_colors,
                    len(set_to_use))
                msg = '%s %s' % (fmt1, fmt2)
                self.logger.error('   %s' % msg)
                raise tse.UserInterfaceException(
                    tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

            # End self.ts_use_implicit_number_of_color_pairs

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

    def tsGetBuiltInColorPalette(self):
        '''
        Gather the terminal specific color palette that was built-in (preset)
        by the host computer operating system when the application program
        was launched.
        '''
        self.ts_builtin_palette = {}
        self.ts_builtin_palette['name'] = 'BuiltinPaletteRGB'
        self.ts_can_change_color = self.can_change_color()
        self.ts_curses_color_pairs = curses.COLOR_PAIRS
        self.ts_curses_colors = curses.COLORS
        maxCursesScale =1000
        maxColorScale = 255

        # 2014/10/15 rsg Added control switch to select whether
        # color palette reflects the reported number of color
        # pairs or the number of colors implicit in terminal
        # emulator name.
        fmt1 = 'tsGetBuiltInColorPalette: '

        if ((self.ts_curses_colors in [8, 16]) or \
            (self.ts_curses_color_pairs in [64, 256])):

            # (self.ts_curses_color_pairs in [64, 256]) == True
            # Expecting: cygwin, xterm, xterm-color, xterm-16color
            # Disfunctional: xterm-88color, xterm-256color 
            # Work-around: xterm-88color, xterm-256color 
            self.ts_use_reported_number_of_color_pairs = True
            self.ts_use_implicit_number_of_color_pairs = not(
                self.ts_use_reported_number_of_color_pairs)

            fmt2 = '\n\tuse_reported_number_of_color_pairs=%s; ' % \
                   str(self.ts_use_reported_number_of_color_pairs)
            fmt3 = '\n\t\tcolors=%d; ' % self.ts_curses_colors

            if ((self.ts_curses_colors == 8) and \
                (self.ts_curses_color_pairs == 64)):

                # Expecting: cygwin, xterm, xterm-color 
                fmt4 = '\n\t\tcolor_pairs(%d)' % \
                       (self.ts_curses_color_pairs)

                self.logger.debug(fmt1 + fmt2 + fmt3 + fmt4)

            elif ((self.ts_curses_colors == 16) and \
                  (self.ts_curses_color_pairs == 256)):

                # Expecting: xterm-16color 
                fmt4 = '\n\t\tcolor_pairs(%d)' % \
                       (self.ts_curses_color_pairs)

                self.logger.debug(fmt1 + fmt2 + fmt3 + fmt4)

            else:

                # Work-around: xterm-88color, xterm-256color 
                fmt4 = '\n\t\tcolor_pairs=%d != (colors**2)=%d' % \
                       (self.ts_curses_color_pairs,
                        self.ts_curses_colors**2)

                self.logger.warning(fmt1 + fmt2 + fmt3 + fmt4)

        elif ((self.ts_curses_colors in [88, 256]) or \
              (self.ts_curses_color_pairs in [7744, 32767])):

            # ((self.ts_curses_colors in [88, 256]) or \
            #  (self.ts_curses_color_pairs in [7744, 32767))
            # Disfunctional: xterm-88color, xterm-256color 
            self.ts_use_implicit_number_of_color_pairs = True
            self.ts_use_reported_number_of_color_pairs = not(
                self.ts_use_implicit_number_of_color_pairs)

            fmt2 = '\n\tuse_implicit_number_of_color_pairs=%s; ' % \
                   str(self.ts_use_implicit_number_of_color_pairs)
            fmt3 = '\n\t\tcolors=%d; ' % self.ts_curses_colors
            fmt4 = '\n\t\tcolor_pairs=%d < %d' % \
                   (self.ts_curses_color_pairs,
                    self.ts_curses_colors**2)

            self.logger.warning(fmt1 + fmt2 + fmt3 + fmt4)

        else:

            fmt2 = '\n\tuse unexpected configuration: \n'
            fmt3 = '\n\t\tcolors=%d; ' % self.ts_curses_colors
            fmt4 = '\n\t\tcolor_pairs=%d' % self.ts_curses_color_pairs

            self.logger.eror(fmt1 + fmt2 + fmt3 + fmt4)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        CAPTURE_BUILTIN_COLORS = True
        if CAPTURE_BUILTIN_COLORS:

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
            self.ts_can_change_color)

        return
 
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
            anRGBCode = ExtendedColorDataBaseRGB[aName]
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

        except Exception as e:

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

        except Exception as e:

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
            colorRGB = ExtendedColorDataBaseRGB[colorName]
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

        except Exception as e:

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

        except Exception as e:

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

        except Exception as e:

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

        except Exception as e:

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

            except Exception as e:

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
        self.ts_can_change_color = False # None
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

    def tsInstallBuiltinColorDataBase(self):
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
            '    Begin tsInstallBuiltinColorDataBase')

        set_to_use = self.tsGetSetToUseForColorNameFromCode()

        if DEBUG_tsInstallExtendedColorDataBase:
            print('\n\n tsInstallBuiltinColorDataBase=%s' % str(
                set_to_use))
            debug_via_tsrpu(myDictionary=set_to_use)

        ## colorSubstitutionMap = None

        if True: # DEBUG and VERBOSE:

            fmt1 = 'tsInstallBuiltinColorDataBase ' + \
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

            colorSubstitutionMap = Color8SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n xterm8BuiltinColorNameFromCode=%s' % str(
                    xterm8BuiltinColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm8BuiltinColorNameFromCode)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        elif ((self.ts_curses_colors == 16) and \
              (self.ts_termname == 'xterm-16color')):

            set_to_use = self.tsStripDictionaryName(
                xterm16BuiltinColorNameFromCode)

            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n xterm16BuiltinColorNameFromCode=%s' % str(
                    set_to_use))
                debug_via_tsrpu(myDictionary=set_to_use)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        elif (((USE_256_COLOR_PAIR_LIMIT) and \
               (self.ts_curses_color_pairs >= 256)) and \
              ((self.ts_termname == 'xterm-88color') or \
               (self.ts_termname == 'xterm-256color'))):

            set_to_use = self.tsStripDictionaryName(
                xterm16BuiltinColorNameFromCode)

            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n USE_256_COLOR_PAIR_LIMIT with ' + \
                      'xterm16BuiltinColorNameFromCode=%s' % str(
                      set_to_use))
                debug_via_tsrpu(myDictionary=set_to_use)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        elif ((self.ts_termname == 'linux') and \
              ((self.ts_curses_colors == 8) or \
               (self.ts_curses_color_pairs == 16))):

            set_to_use = self.tsStripDictionaryName(
                xterm8BuiltinColorNameFromCode)

            colorSubstitutionMap = Color8SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n xterm8BuiltinColorNameFromCode=%s' % str(
                    xterm8BuiltinColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm8BuiltinColorNameFromCode)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        elif ((self.ts_termname == 'linux') and \
              ((self.ts_curses_colors == 16) or \
               (self.ts_curses_color_pairs == 256))):

            set_to_use = self.tsStripDictionaryName(
                xterm16BuiltinColorNameFromCode)

            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n xterm16BuiltinColorNameFromCode=%s' % str(
                    set_to_use))
                debug_via_tsrpu(myDictionary=set_to_use)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        else:

            fmt1 = 'tsInstallBuiltinColorDataBase (invalid config): \n'
            fmt2 = '\tcurses_colors=%d \n' % self.ts_curses_colors
            fmt3 = '\ttermname=%s' % self.ts_termname
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

        if True: # DEBUG and VERBOSE:
            fmt1 = 'tsInstallBuiltinColorDataBase ' + \
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

##            rgb = ExtendedColorDataBaseRGB[aName] 
##            red = rgb[0]
##            green = rgb[1]
##            blue = rgb[2] 
##            self.tsSetCursesColorNumber(aCode, red, green, blue)

##            GraphicalTextUserInterface.ColorDataBaseRGB[aName] = (
##                red, green, blue)

            GraphicalTextUserInterface.ColorDataBaseRGB[
                aName] = self.ts_builtin_palette[aName]

##            (r, g, b) = self.tsGetCursesColorContent(aCode)

##            if True or DEBUG:

##                if ((abs(red - r) <= 1) and \
##                    (abs(green - g) <= 1) and \
##                    (abs(blue - b) <= 1)):
##                    match = True
##                else:
##                    match = False
##                msg = 'tsInstallBuiltinColorDataBase: ' + \
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
                debug_via_tsrpu(
                    myDictionary=GraphicalTextUserInterface.ColorDataBase)

            self.logger.debug(
                'installed ColorDataBaseID = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseID))

            if DEBUG_tsInstallExtendedColorDataBase:
                print(
                    '\n\n GraphicalTextUserInterface.ColorDataBaseID=%s' % str(
                    GraphicalTextUserInterface.ColorDataBaseID))
                debug_via_tsrpu(
                    myDictionary=GraphicalTextUserInterface.ColorDataBaseID)

            self.logger.debug(
                'installed ColorDataBaseRGB = %s' % \
                str(GraphicalTextUserInterface.ColorDataBaseRGB))

            if DEBUG_tsInstallExtendedColorDataBase:
                print(
                    '\n\n GraphicalTextUserInterface.' + \
                    'ColorDataBaseRGBe=%s' % str(
                    GraphicalTextUserInterface.ColorDataBaseRGB))
                debug_via_tsrpu(
                    myDictionary=GraphicalTextUserInterface.ColorDataBaseRGB)

            self.logger.debug(
                'installed ColorSubstitutionDataBase = %s' % \
                str(GraphicalTextUserInterface.ColorSubstitutionDataBase))

            if DEBUG_tsInstallExtendedColorDataBase:
                print(
                    '\n\n GraphicalTextUserInterface.' + \
                    'ColorSubstitutionDataBase=%s' % str(
                    GraphicalTextUserInterface.ColorSubstitutionDataBase))
                debug_via_tsrpu(
                    myDictionary=\
                    GraphicalTextUserInterface.ColorSubstitutionDataBase)

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
            print(
                '\n\n GraphicalTextUserInterface.' + \
                'ColorDataBasePairID=%s' % str(
                GraphicalTextUserInterface.ColorDataBasePairID))
            debug_via_tsrpu(
                myDictionary=\
                GraphicalTextUserInterface.ColorDataBasePairID)

        self.logger.debug(
            '    End tsInstallBuiltinColorDataBase')

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
            colorSubstitutionMap = Color8SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm8ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm8ColorNameFromCode)

        elif (self.ts_termname == 'xterm-16color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()
            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm16ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm16ColorNameFromCode)

        elif (((USE_256_COLOR_PAIR_LIMIT) and \
               (self.ts_curses_color_pairs >= 256)) and \
              ((self.ts_termname == 'xterm-88color') or \
               (self.ts_termname == 'xterm-256color'))):

            set_to_use = self.tsStripDictionaryName(
                xterm16ColorNameFromCode)

            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                      set_to_use))
                debug_via_tsrpu(myDictionary=set_to_use)

                print('\n\n colorSubstitutionMap=%s' % str(
                    colorSubstitutionMap))
                debug_via_tsrpu(myDictionary=colorSubstitutionMap)

        elif (self.ts_termname == 'xterm-88color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            colorSubstitutionMap = None

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm88ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm88ColorNameFromCode)

        elif (self.ts_termname == 'xterm-256color'):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()

            colorSubstitutionMap = None

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                    xterm256ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm256ColorNameFromCode)

        elif ((self.ts_termname == 'linux') and \
              ((self.ts_curses_colors == 8) or \
               (self.ts_curses_color_pairs == 16))):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()
            colorSubstitutionMap = Color8SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:

                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm8ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm8ColorNameFromCode)

        elif ((self.ts_termname == 'linux') and \
              ((self.ts_curses_colors == 16) or \
               (self.ts_curses_color_pairs == 256))):

            set_to_use = self.tsGetSetToUseForColorNameFromCode()
            colorSubstitutionMap = Color16SubstitutionMap

            if DEBUG_tsInstallExtendedColorDataBase:
                print('\n\n GraphicalTextUserInterface.' + \
                      'tsInstallExtendedColorDataBase=%s' % str(
                  xterm16ColorNameFromCode))
                debug_via_tsrpu(myDictionary=xterm16ColorNameFromCode)

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
            debug_via_tsrpu(myDictionary=set_to_use)

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

        theMap = colorSubstitutionMap
        GraphicalTextUserInterface.ColorSubstitutionDataBase = theMap

        #---------------------------------------------------
        # Register entries in color name, code and rgb data bases
        for aCode in range(available_colors):
            aName = set_to_use[aCode]
            aBuiltinRGB = self.tsGetCursesColorContent(aCode)
            aExtendedRGB = ExtendedColorDataBaseRGB[aName]
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

                # (red, green, blue) = ExtendedColorDataBaseRGB[aName]
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
        except Exception as e:
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

        timestamp = tsrpu.getDateTimeString(time.time(), msec=True)

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

        tsrpu.displayDictionary(
            0,
            GraphicalTextUserInterface.CursesDataBase,
            defaultDBaseFile,
            myLogger=None)

        defaultDBaseFile.flush()

        tsrpu.displayDictionary(
            0,
            GraphicalTextUserInterface.WindowDataBase,
            defaultDBaseFile,
            myLogger=None)

        defaultDBaseFile.flush()

        timestamp = tsrpu.getDateTimeString(time.time(), msec=True)

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
