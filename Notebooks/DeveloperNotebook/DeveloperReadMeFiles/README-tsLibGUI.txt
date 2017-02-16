#"Time-stamp: <12/18/2016  2:54:00 PM rsg>"

================ File: README-tsLibGUI.txt =================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling on
   platforms with:

   * 64-bit processors, nCurses 6.x, 64-bit Python 3.6.x or
     later GUI applications and character-mode 256-/16-/8-
     color (xterm-family) and non-color (vt100-family)
     terminals and terminal emulators.

   * 32-bit processors, nCurses 6.x/5.x, 32-bit Python 3.5.2
     or earlier GUI applications and character-mode 16-/8-
     color (xterm-family) and non-color (vt100-family)
     terminals and terminal emulators.

===================== TABLE OF CONTENTS ====================

1. Package Organization
2. tsWxPkg

=================== PACKAGE ORGANIZATION ===================

1. Package Organization

  The library of building blocks is organized, by the
  functional scope of each component, into a collection of
  "packages". When appropriate, any package may import and
  use the services of any other tsLibGUI package.
  
  Source code is contained in the associated ["src"] sub-
  directory. Depending on its complexity, the source code
  of a package may also be sub-divided and organized into
  a set of one or more source files.
  
  Unit/Integration Test code is contained in the associated
  ["test"] sub-directory. Depending on its complexity, the
  test code of a package may also be sub-divided and organ-
  ized into a set of one or more test files.

========================== tsWxPkg =========================

2. tsWxPkg

  tsWxPkg - Collection of approximately 100 Classes that
  use the services of the Python Curses module to create a
  character-mode emulation of their pixel-mode "wxPython"
  Class counterparts. The collection includes widgets for
  frames, dialogs, panels, buttons, check boxes, radio
  boxes/buttons and scrollable text windows. It includes
  box and grid sizers. It also includes classes to emulate
  the host operating system theme-based color palette
  management, task bar, mouse click and window focus
  control services used/expected by "wxPython".

  a. tsWx - Module to load all symbols that should appear
     within the wxPython.wx emulation namespace. Included
     are various classes, constants, functions and methods
     available for use by applications built with components
     from the wxPython emulation infrastructure.

  b. tsWxGlobals - Module to emulate wxPython configuration
     constants and provide a means for site-specific style
     definitions.

     It provides a centralized mechanism for modifying/
     restoring those configuration constants that can be
     interogated at runtime by those software components
     having a "need-to-know". The intent being to avoid
     subsequent searches to locate and modify or restore
     a constant appropriate to the current configuration.

     It also provides a theme-based mechanism for modify-
     ing/restoring those configuration constants as appro-
     priate for various organizations and products.

     ThemeWxPython illustrates the monochrome color scheme
     features of the "wxWidgets" organization and its
     "wxPython" product.

     ThemeTeamSTARS illustrates the multi-color scheme
     features of the "TeamSTARS"/"Software Gadgetry"
     organization and its "tsWxGTUI" Toolkit product.

  c. tsWxGraphicalTextUserInterface - Module uses the
     Standard Python Curses API to emulate typical host
     operating system GUI window manager services.

     It initializes, manages and shuts down input (from the
     keyboard and mouse) and output to a two-dimensional
     display screen.

     It captures and logs the initial and run time GUI
     configuration to facilitate troubleshooting.

  d. Non-color (vt100 and vt220) - The character-mode
     Graphical-style User Interface emulation is mouseless
     and disables and ignores references to the 68-color
     "wxPython" palette. This results in the rendering of
     text and shape outlines in "Black" on White" or "White"
     on "Black" as appropriate for the host platform oper-
     ating system.

  e. Curses-style Multi-color (xterm, xterm-color, xterm-
     16color) - The character-mode Graphical-style User
     Interface emulation supports a mouse and maps the
     68-color "wxPython" palette into the 8-color or
     16-color "Curses" / "nCurses" palette. This results
     in the rendering of text and shapes with 64 (8x8) or
     256 (16x16) color pairs depending on the operator
     designated terminal emulator.

  f. wxPython-style Multi-color (xterm-88color and xterm-
     256color) - The character-mode Graphical-style User
     Interface emulation supports a mouse and configures
     and initializes the Red-Green-Blue settings for an
     extended 68-color "wxPython" palette. This results
     in the rendering of text and shapes with 5041 (71x71)
     or 19600 (140x140) color pairs depending on the
     operator designated terminal emulator.

  g. tsWxEventLoop - Module uses the Standard Python
     Curses API to receive keyboard and mouse events.

     It maps the Curses events into their wxPython
     equivalents.

     It enhances the Standard Python Curses API by:
     scanning the stack of tiled and overlaid wxPython
     GUI objects and identifying the one visible enough
     in the screen position to have triggered the event;
     it dispatches the event to the appropriate "wxPython"-
     style event handler. 

  h. tsWxMultiFrameEnv - Module to enable an application
     using a Command Line Interface (CLI) to launch and
     use the same character-mode terminal with a Graphi-
     cal-style User Interface (GUI).

     It uses application specified configuration keyword-
     value pair options to initialize any application
     specific logger(s).

     It wraps the CLI, underlying the GUI, and the GUI
     with exception handlers to control the exit codes
     and messages used to coordinate other application
     programs.

  i. tsWxPyOnDemandOutputWindow - Module that can be used
     for redirecting Python "stdout" and "stderr" streams.
     It will do nothing until something is written to the
     stream at which point it will write the text to the
     toolkit created "Redirected Output: stdout/stderr"
     frame located just below the application generated
     frames and dialogs, scrolling previous output up
     and off the associated screen area to make room for
     the new output.

  j. tsWxTaskBar - Module to create a task icon (button)
     for each top level window (frame, dialog etc.) in a
     toolkit created "Tasks" frame located just below the
     "Redirected Output: stdout/stderr" frame. One or more
     task icons appear within the "Tasks" frame and respond
     to mouse clicks. When the mouse clicks on a task icon,
     the focus for the associated application frame or
     dialog will be raised from background (partially or
     fully hidden) to foreground (fully visible).

  k. "wxPython"-style Widgets - Modules to emulate the
     "wxPython"-style frame, dialog, button, checkbox,
     gauge, menu bar, radio box, scroll bar, status bar etc.

  l. "wxPython"-style Sizers - Module to emulate the
     "wxPython"-style box and grid sizer, which facili-
     tate the subdivision and layout of display screen
     area.

======================= End-Of-File ========================
