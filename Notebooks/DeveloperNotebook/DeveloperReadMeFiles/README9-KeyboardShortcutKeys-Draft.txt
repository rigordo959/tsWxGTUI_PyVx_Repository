#-----------------------------------------------------------
#"Time-stamp: <06/08/2015  3:48:50 AM rsg>"
#-----------------------------------------------------------

=== Title Page for File: README9-KeyboardShortcutKeys.txt ==

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode 8-/16-color (xterm-family) & non-color
   (vt100-family) terminals and terminal emulators.

   You can find this and other files in the following sub-
   directories:

       <Your Working Repository>
       (e.g. "Technical_Preview") 
         |
         |  Working repository containing directories and
         |  files to be packaged into downloadable "tarball"
         |  and/or "zip" files via the setup shell scripts
         |  at the bottom of this diagram.
         |
         +-- ["Documents"]
         |     |
         |     |  This directory contains a collection of files
         |     |  which provide the Toolkit recipient with an
         |     |  understanding of the purpose, goals & capabil-
         |     |  ities, non-goals & limitations, terms & condi-
         |     |  tions and procedures for installing, operating,
         |     |  modifying and redistributing the Toolkit. 
         |     |
         |     |  Deliverable Toolkit manual pages are a
         |     |  form of online software documentation
         |     |  usually found on a Unix or Unix-like oper-
         |     |  ating system.
         |     |
         |     +-- "README9-KeyboardShortcutKeys.txt"
         |     +-- "README3-Documents.txt"
         |
         +-- ["ManPages"]
         |
         +-- ["Notebooks"]
         |
         +-- ["SourceDistributions"]
         |
         +-- "README.txt"

===================== TABLE OF CONTENTS ====================

1. Software design and implementation constraints.

2. wxWidget Accelerator Hotkeys

3. wxWidget Catching key events globally

4. Keyboard Shortcut Keys

5. Table of keyboard shortcuts

6. Computer keyboard shortcut keys

7. Microsoft Windows shortcut keys

8. Apple Macintosh shortcut keys

9. Unix and Linux shortcut keys

10. Top 10 keyboard shortcuts everyone should know

====== Software design and implementation constraints ======

1. Software design and implementation constraints

   The xterm-style 8-/16-color terminals and terminal emula-
   tors accept operator input via keyboard and mouse de-
   vices.

   The vt100-style non-color terminals and terminal emula-
   tors typically accept operator input only via keyboard
   devices. A few generate non-xterm-style mouse events
   which preciputate application traps.

   Operator input must trigger an event notification that
   must be sent to and then handled by the target GUI ob-
   ject such as a button or menu list item.

   *********************************************************
   **       FUTURE DESIGN AND IMPLEMENTATION CHANGE       **
   *********************************************************

   Consequently, in order to support color and non-color
   terminals and terminal emulators, each button and menu
   list item must provide and use an accelerator hotkey as
   well as an accelerator hotkey by which the opertor may
   change focus of a top-level GUI object (frame or dialog)
   from background to foreground thereby relegating the pre-
   vious foreground object to the background.

   Event handlers for vt100-style non-color terminals and
   terminal emulators must either disable or handle mouse
   input event notifications.

   NOTE:

       The implementation of keyboard shortcuts has been and
       should continue to be postponed until after the re-
       solution of GUI object focus changes using the curses
       panel capability. It being simpler to verify focus
       changes triggereg via a mouse than triggered via key-
       board input and recursive table lookup.

=============== wxWidget Accelerator Hotkeys ===============

2. wxWidget Accelerator Hotkeys

   Excerpt From "https://books.google.com/books?id=CyMsvtgnq0QC&pg=PA180&lpg=PA180&dq=wxWidget+Accelerator+Hotkeys&source=bl&ots=SU7wm9DnDc&sig=9_ioDyoPjZJNF2TQhQVG_6OtJLM&hl=en&sa=X&ei=NfBzVbn2JMrVsAWH6oDYBg&ved=0CD0Q6AEwBA#v=onepage&q=wxWidget%20Accelerator%20Hotkeys&f=false":

   "Accelerators

   An accelerator implements a keyboard shortcut for a menu
   command, enabling the user to execute the command quickly.
   These shortcuts take precedence over other keyboard pro-
   cessing, such as EVT_CHAR handlers. Standard shortcuts
   include Ctrl-O to open a file and Ctrl-V to paste data
   into the application. The easiest way to implement accel-
   erators is to specify them in menu items. For example:

   menu->Append(wxID_COPY, wxT("Copy\tCtrl+C"));

   wxWidgets intrprets the text after the "tab" character as
   an accelerator and adds it to the menu's accelerator
   table. In this example, when the user presses Ctrl-C the
   wxID_COPY command is sent, just as though the menu item
   was selected...."

=========== wxWidget Catching key events globally ==========

3. wxWidget Catching key events globally

   Excerpt From "https://wiki.wxwidgets.org/
                         Catching_key_events_globally":

   "Keyboard events go to the component that currently has
   focus and do not propagate to the parent; if you are try-
   ing to catch key events globally it can thus be a little
   tricky. Here are a few ways to solve this problem - keep
   in mind there are probably more than presented here.

   Before getting started, some helpful notes about cases
   where you may catching the wrong event or where you may
   not need global key catching at all:

   * Many components will only receive key events if they
     have the wxWANTS_CHARS style flag enabled; then, you
     need to catch EVT_CHAR rather than or in addition to
     EVT_KEY_DOWN.

   * For catching Enter presses on text controls, use style
     flag wxTE_PROCESS_ENTER, and catch event
     EVT_TEXT_ENTER."

================== Keyboard Shortcut Keys ==================

4. Keyboard Shortcut Keys

   Excerpts From Wikipedia, the free encyclopedia:

   "   For Wikipedia keyboard shortcuts,
           see Wikipedia:Keyboard shortcuts.

       For a list of keyboard shortcuts,
           see Table of keyboard shortcuts.

   In computing, a keyboard shortcut is a series of one or
   several keys that invoke a software or operating system
   operation (in other words, cause an event) when triggered
   by the user. The meaning of term "keyboard shortcut" can
   vary depending on software manufacturer. For instance,
   Microsoft differentiates keyboard shortcuts from hotkeys
   ("mnemonics" on Windows) whereby the former consists of a
   specific key combination used to trigger an action, and
   the latter represents a designated letter in a menu command
   or toolbar button that when pressed together with the Alt
   key, activates such command --- whereas a "hotkey" on
   Windows is a system wide shortcut that is always available
   in all contexts as long as the program responsible for it
   is running and not suspended.

   Description

   Keyboard shortcuts are typically a means for invoking one or
   more commands using the keyboard that would otherwise be
   accessible only through a menu, a pointing device, different
   levels of a user interface, or via a command-line interface.
   Keyboard shortcuts are generally used to expedite common
   operations by reducing input sequences to a few keystrokes,
   hence the term "shortcut".[1]

   To differentiate from general keyboard input, most keyboard
   shortcuts require the user to press and hold several keys
   simultaneously or a sequence of keys one after the other.
   Unmodified key presses are sometimes accepted when the
   keyboard is not used for general input - such as with
   graphics packages e.g. Adobe Photoshop or IBM Lotus Free-
   lance Graphics. Other keyboard shortcuts use function keys
   that are dedicated for use in shortcuts and may only require
   a single keypress. For simultaneous keyboard shortcuts, one
   usually first holds down the modifier key(s), then quickly
   presses and releases the regular (non-modifier) key, and
   finally releases the modifier key(s). This distinction is
   important, as trying to press all the keys simultaneously
   will frequently either miss some of the modifier keys, or
   cause unwanted auto-repeat. Sequential shortcuts usually
   involve pressing and releasing a dedicated prefix key,
   such as the Esc key, followed by one or more keystrokes.

   Mnemonics are distinguishable from keyboard shortcuts.
   One difference between them is that the keyboard short-
   cuts are not localized on multi-language software but
   the mnemonics are generally localized to reflect the
   symbols and letters used in the specific locale. In
   most GUIs, a program's keyboard shortcuts are discover-
   able by browsing the program's menus --- the shortcut
   is indicated next to the menu choice. There are key-
   boards that have the shortcuts for a particular appli-
   cation already marked on them. These keyboards are
   often used for editing video, audio, or graphics,[2]
   as well as in software training courses. There are
   also stickers with shortcuts printed on them that can
   be applied to a regular keyboard. Reference cards
   intended to be propped up in the user's workspace
   also exist for many applications. In the past, when
   computer hardware was more standardized, it was common
   for computer books and magazines to print cards that
   were cut out, intended to be placed over the user's
   keyboard with the printed shortcuts noted next to
   the appropriate keys...."

================ Table of keyboard shortcuts ===============

5. Table of keyboard shortcuts

   From Wikipedia, the free encyclopedia:

   Excerpt From "http://en.wikipedia.org/wiki/Table_of_keyboard_shortcuts":

============= Computer keyboard shortcut keys ==============

6. Computer keyboard shortcut keys

   Excerpt From "http://www.computerhope.com/shortcut.htm":

============= Microsoft Windows shortcut keys ==============

7. Microsoft Windows shortcut keys

   Excerpt From "http://www.computerhope.com/shortcut/windows.htm":

============== Apple Macintosh shortcut keys ===============

8. Apple Macintosh shortcut keys

   Excerpt From "Apple Macintosh shortcut keys":

================ Unix and Linux shortcut keys ==============

9. Unix and Linux shortcut keys

   Excerpt From "http://www.computerhope.com/ushort.htm":

====== Top 10 keyboard shortcuts everyone should know ======

10. Top 10 keyboard shortcuts everyone should know

   Excerpt From "http://www.computerhope.com/tips/tip79.htm":



   "In computing, source code is any collection of computer
   instructions (possibly with comments) written using some
   human-readable computer language, usually as text. The
   source code of a program is specially designed to facili-
   tate the work of computer programmers, who specify the
   actions to be performed by a computer mostly by writing
   source code. The source code is often transformed by a
   compiler program into low-level machine code understood
   by the computer. The machine code might then be stored
   for execution at a later time. Alternatively, an inter-
   preter can be used to analyze and perform the outcomes
   of the source code program directly on the fly.

   Most computer applications are distributed in a form that
   includes executable files, but not their source code. If
   the source code were included, it would be useful to a
   user, programmer, or system administrator, who may wish
   to modify the program or to understand how it works.

   Aside from its machine-readable forms, source code also
   appears in books and other media; often in the form of
   small code snippets, but occasionally complete code
   bases; a well-known case is the source code of PGP."

======================= End-Of-File ========================
