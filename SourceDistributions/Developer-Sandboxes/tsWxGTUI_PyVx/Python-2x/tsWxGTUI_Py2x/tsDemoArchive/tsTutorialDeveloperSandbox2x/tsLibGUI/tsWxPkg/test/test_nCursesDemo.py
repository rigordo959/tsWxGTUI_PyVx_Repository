#!/usr/bin/env python
# "Time-stamp: <12/09/2013  6:13:41 AM rsg>"
__doc__ = '''
test_nCursesDemo.py - Test application for Python "Curses"
module.

  From http://docs.python.org/2/library/curses.html:
  15.11. curses --- Terminal handling for character-cell displays

Boilerplate, comments and bug fixes added by Richard S. Gordon.
'''
#################################################################
#
# File: test_nCursesDemo.py
#
# Purpose:
#
#     Test application for Python "Curses" module.
#
# Usage (example):
#
#    # Execute
#
#    python test_tsCursesSampl.py
#
# Capabilities:
#
#    1. Initialize and startup the standard terminal display screen.
#
#    2. Create a curses window and multiple panels.
#
#    3. Waits for various input from terminal keyboard.
#
#       Changes panel layout.
#
#       Output panel layout to terminal display screen.
#
#    4. Shutdown and terminate the standard terminal display screen.
#
#    5. Displays __heading__ with Copyright, Credits, License etc.
#
# Limitations:
#
#    None.
#
# Notes:
#
#    None.
#
# Classes:
#
#    None.
#
# Methods:
#
#    TBD.
#
# Modifications:
#
#    2013/12/09 rsg Initial version.
#
# ToDo:
#
#    TBD.
#
#################################################################

__title__     = 'test_nCursesDemo'
__version__   = '1.0.0'
__date__      = '12/09/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  Python Curses Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' + \
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'

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

## Note

##    Since version 5.4, the ncurses library decides how to interpret
##    non-ASCII data using the nl_langinfo function. That means that you
##    have to call locale.setlocale() in the application and encode
##    Unicode strings using one of the system's available encodings.
##    This example uses the system's default encoding:

import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
###!/usr/bin/env python
###
### $Id$
###
### (n)curses exerciser in Python, an interactive test for the curses
### module. Currently, only the panel demos are ported.

import curses
from curses import panel

def wGetchar(win = None):
    if win is None: win = stdscr
    return win.getch()

def Getchar():
    wGetchar()

#
# Panels tester
#
def wait_a_while():
    if nap_msec == 1:
        Getchar()
    else:
        curses.napms(nap_msec)

def saywhat(text):
    stdscr.move(curses.LINES - 1, 0)
    stdscr.clrtoeol()
    stdscr.addstr(text)

def mkpanel(color, rows, cols, tly, tlx):
    win = curses.newwin(rows, cols, tly, tlx)
    pan = panel.new_panel(win)
    if curses.has_colors():
        if color == curses.COLOR_BLUE:
            fg = curses.COLOR_WHITE
        else:
            fg = curses.COLOR_BLACK
        bg = color
        curses.init_pair(color, fg, bg)
        win.bkgdset(ord(' '), curses.color_pair(color))
    else:
        win.bkgdset(ord(' '), curses.A_BOLD)

    return pan

def pflush():
    panel.update_panels()
    curses.doupdate()

def fill_panel(pan):
    win = pan.window()
    num = pan.userptr()[1]

    win.move(1, 1)
    win.addstr("-pan%c-" % num)
    win.clrtoeol()
    win.box()

    maxy, maxx = win.getmaxyx()
    for y in range(2, maxy - 1):
        for x in range(1, maxx - 1):
            win.move(y, x)
            win.addch(num)

def demo_panels(win):
    global stdscr, nap_msec, mod
    stdscr = win
    nap_msec = 1
    mod = ["test", "TEST", "(**)", "*()*", "<-->", "LAST"]

    stdscr.refresh()

    for y in range(0, curses.LINES - 1):
        for x in range(0, curses.COLS):
            stdscr.addstr("%d" % ((y + x) % 10))
    for y in range(0, 1):
        p1 = mkpanel(curses.COLOR_RED,
                     curses.LINES // 2 - 2,
                     curses.COLS // 8 + 1,
                     0,
                     0)
        p1.set_userptr("p1")

        p2 = mkpanel(curses.COLOR_GREEN,
                     curses.LINES // 2 + 1,
                     curses.COLS // 7,
                     curses.LINES // 4,
                     curses.COLS // 10)
        p2.set_userptr("p2")

        p3 = mkpanel(curses.COLOR_YELLOW,
                     curses.LINES // 4,
                     curses.COLS // 10,
                     curses.LINES // 2,
                     curses.COLS // 9)
        p3.set_userptr("p3")

        p4 = mkpanel(curses.COLOR_BLUE,
                     curses.LINES // 2 - 2,
                     curses.COLS // 8,
                     curses.LINES // 2 - 2,
                     curses.COLS // 3)
        p4.set_userptr("p4")

        p5 = mkpanel(curses.COLOR_MAGENTA,
                     curses.LINES // 2 - 2,
                     curses.COLS // 8,
                     curses.LINES // 2,
                     curses.COLS // 2 - 2)
        p5.set_userptr("p5")

        fill_panel(p1)
        fill_panel(p2)
        fill_panel(p3)
        fill_panel(p4)
        fill_panel(p5)
        p4.hide()
        p5.hide()
        pflush()
        saywhat("press any key to continue")
        wait_a_while()

        saywhat("h3 s1 s2 s4 s5;press any key to continue")
        p1.move(0, 0)
        p3.hide()
        p1.show()
        p2.show()
        p4.show()
        p5.show()
        pflush()
        wait_a_while()

        saywhat("s1; press any key to continue")
        p1.show()
        pflush()
        wait_a_while()

        saywhat("s2; press any key to continue")
        p2.show()
        pflush()
        wait_a_while()

        saywhat("m2; press any key to continue")
        p2.move(curses.LINES // 3 + 1, curses.COLS // 8)
        pflush()
        wait_a_while()

        saywhat("s3; press any key to continue")
        p3.show()
        pflush()
        wait_a_while()

        saywhat("m3; press any key to continue")
        p3.move(curses.LINES // 4 + 1, curses.COLS // 15)
        pflush()
        wait_a_while()

        saywhat("b3; press any key to continue")
        p3.bottom()
        pflush()
        wait_a_while()

        saywhat("s4; press any key to continue")
        p4.show()
        pflush()
        wait_a_while()

        saywhat("s5; press any key to continue")
        p5.show()
        pflush()
        wait_a_while()

        saywhat("t3; press any key to continue")
        p3.top()
        pflush()
        wait_a_while()

        saywhat("t1; press any key to continue")
        p1.show()
        pflush()
        wait_a_while()

        saywhat("t2; press any key to continue")
        p2.show()
        pflush()
        wait_a_while()

        saywhat("t3; press any key to continue")
        p3.show()
        pflush()
        wait_a_while()

        saywhat("t4; press any key to continue")
        p4.show()
        pflush()
        wait_a_while()

        for itmp in range(0, 6):
            w4 = p4.window()
            w5 = p5.window()

            saywhat("m4; press any key to continue")
            w4.move(curses.LINES // 8, 1)
            w4.addstr(mod[itmp])
            p4.move(curses.LINES // 6, itmp * curses.COLS // 8)
            w5.move(curses.LINES // 6, 1)
            w5.addstr(mod[itmp])
            pflush()
            wait_a_while()

            saywhat("m5; press any key to continue")
            w4.move(curses.LINES // 6, 1)
            w4.addstr(mod[itmp])
            p5.move(curses.LINES // 3 - 1, itmp * 10 + 6)
            w5.move(curses.LINES // 8, 1)
            w5.addstr(mod[itmp])
            pflush()
            wait_a_while()

        saywhat("m4; press any key to continue")
        p4.move(curses.LINES // 6, (itmp + 1) * curses.COLS // 8)
        pflush()
        wait_a_while()

        saywhat("t5; press any key to continue")
        p5.top()
        pflush()
        wait_a_while()

        saywhat("t2; press any key to continue")
        p2.top()
        pflush()
        wait_a_while()

        saywhat("t1; press any key to continue")
        p1.top()
        pflush()
        wait_a_while()

        saywhat("d2; press any key to continue")
        del p2
        pflush()
        wait_a_while()

        saywhat("h3; press any key to continue")
        p3.hide()
        pflush()
        wait_a_while()

        saywhat("d1; press any key to continue")
        del p1
        pflush()
        wait_a_while()

        saywhat("d4; press any key to continue")
        del p4
        pflush()
        wait_a_while()

        saywhat("d5; press any key to continue")
        del p5
        pflush()
        wait_a_while()
        if nap_msec == 1:
            break
        nap_msec = 100

#
# one fine day there'll be the menu at this place
#
curses.wrapper(demo_panels)
print(__header__)
