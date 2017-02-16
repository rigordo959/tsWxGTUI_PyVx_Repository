#"Time-stamp: <12/18/2016  2:57:19 PM rsg>"

========= File: README-wxPython_API_Reference.txt ==========

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

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./tsWxGTUI_PyVx/Documents".

===================== TABLE OF CONTENTS ====================

1. wxPython_API_Reference

   1.1 wxPython-2.8.9.2-docs

   1.2 Links to On-Line Documents

2. Making "tsWxGTUI_PyVx" a part of wxWidgets

   2.1 Low Bandwidth Optimized Character-mode Interface
       Upgrade

   2.2 Source Code and Build System Upgrade 

================== wxPython_API_Reference ==================

1. wxPython_API_Reference

   The subdirectory named "wxPython_API_References" contains
   archive copies of documentation files and directories, in
   HTML format, for versions 2.8.9.2 and 3.0.2.0 of "wxPy-
   thon" and "wxWidgets" published by Julian Smart, Robert
   Roebling et al.

   1.1 wxPython-2.8.9.2-docs

       Developers, maintainers and troubleshooters of the
       TeamSTARS "tsWxGTUI_PyVx" Toolkit may find this in-
       formation useful because the feasibility and techni-
       cal preview prototypes of the TeamSTARS "tsWxGTUI_Py-
       Vx" Toolkit product are based on the software archi-
       tecture and Application Programming Interface (API)
       of "wxPython" 2.8.9.2.

   1.2 Links to On-Line Documents

       An Internet Uniform Resource Locator (URL) link to
       wxPython-2.8.9.2-docs could NOT be provided because:

       a) "www.wxpython.org" currently links only to a "3.0
          Online Manual" (3.0.2);

       b) "www.wxwidgets.org" currently links only to a "2.8
          Online Manual" (2.8.12), a "3.0 Online Manual"
          (3.0.2) and a "Developer Manual" (3.1.0).

======== Making "tsWxGTUI_PyVx" a part of wxWidgets ========

2. Making "tsWxGTUI_PyVx" a part of wxWidgets

   Whereas there is a single TeamSTARS "tsWxGTUI_PyVx" Tool-
   kit developer, the wxWidgets Team includes six core team
   members, twelve major and an unknown number of indepen-
   dent contributors to the wxWidgets/wxPython products.

   The wxWidgets-2.8.12 (and its associated wxPython-2.8.12
   wrapper) is a pixel-mode Graphical User Interface (GUI).

   2.1 Low Bandwidth Optimized Character-mode Interface
       Upgrade

       The wxWidgets-3.0.2 (and its associated wxPython-3.0.2
       wrapper) is a pixel-mode Graphical User Interface (GUI).
       It uses the pixel-mode GUI to emulate the look and feel
       of a Command Line Interface (CLI) console. However, that
       emulation would need to add the host platform operating
       system functionality associated with the  "tsWxGTUI_PyVx"
       Toolkit's "tsWxGraphicalTextUserInterface" module:

       a) the character-mode curses-based emulation of non-
          color terminals and operator designated terminal
	  emulators such as the vt100 and vt220;

       b) the character-mode curses-based emulation of the
          multi-color terminals (associated with cygwin, lin-
          ux, Mac OS X and Unix platforms) and operator desig-
	  nated terminal emulators (such as xterm, xterm-color,
	  or, xterm-16color, xterm-88color and xterm-256color);

       c) the timer and the terminal keyboard input events;

       d) the the terminal mouse position and button input
          events and the association with the triggering GUI
          object;

       e) the setting of the RGB values for the terminal
          display's color palette;

       f) the setting of the display associated with a task
          bar and scroll bars;

       g) low bandwidth optimized character-mode communication
          between local and remote computers and terminals.

   2.2 Source Code and Build System Upgrade 

       According to a representative of the wxWidgets Team,
       "to become part of wxWidgets itself, it would need to
       be done in C++, of course -- it's a C++ library, after
       all. It would also need to be structured as a "port"
       i.e. implement wxWidgets API (that is, provide the
       implementation of the usual wxWidgets classes such as
       wxButton, wxCheckBox using Curses. This is rather dif-
       ferent than doing it in wxPython but should be relatively
       straightforward in this case.... But beyond contributing
       an initial version of it, an important question is wheth-
       er you'd be available to maintain it in the future as
       past experience shows that ports without dedicated main-
       tainer usually don't survive for long."

       a) Limited Curses-based Cross-Platform Deployment

          There are unresolved issues building wxWidgets and
	  wxPython 3.0.2 and 2.8.12 for use with Cygwin on
	  Microsoft Windows.

	  Curses is available on platforms with operating sys-
	  tems as diverse as Linux, Mac OS X and Unix. However,
	  curses is only available on Microsoft Windows plat-
	  forms with Cygwin, the free Linux-like plug-in from
	  Red Hat.

       b) It would likely be an immense challenge for a single
	  TeamSTARS "tsWxGTUI_PyVx" Toolkit developer to be-
	  come familar with the numerous wxWidget classes and
	  methods.

          Without that familiarity, the developer might be
	  tempted to alter the common (non-host operating
	  system specific) code. This would undermine the
	  wxWidgets team's own development and maintenance
	  efforts.

       c) Leaving the common (non-host operating system
          specific) code unchanged, the TeamSTARS
	  "tsWxGTUI_PyVx" Toolkit developer could create
	  a new host operating system specific package that
	  would only emulate the features of the Python
	  curses-based "tsWxGraphicalTextUserInterface" and
	  associated modules.

          This ought to be practical since this was a major
	  part of the Toolkit development effort and creat-
	  ing Python-based modules for wxWidgets classes
	  was only required becase the user might not wish
	  or be able to install the wxWidgets C++ library.

======================= End-Of-File ========================
