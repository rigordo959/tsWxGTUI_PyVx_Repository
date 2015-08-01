#! /usr/bin/env python
# "Time-stamp: <03/18/2015  4:48:48 AM rsg>"
'''
tsWxCursesServices.py - Class of low-level Python Curses Services
wrapped with exception handlers.
'''
#################################################################
#
# File: tsWxCursesServices.py
#
# Purpose:
#
#     Dictionary of Python Curses Key Codes to be associared with
#     the terminal console keyboard.
#
# Usage (example):
#
#     ## Import Module
#     import tsWxCursesServices
#
# Requirements:
#
#    1. Input Interface
#
#       Computer Keyboard (industry standard mult-button).
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
#    1. Defines the key codes to be associated with the terminal
#       console keyboard.
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Classes:
#
#    None
#
# Methods:
#
#    None
#
# Modifications:
#
#    2015/03/17 rsg Extracted this code from the module named
#                   tsWxGraphicalTextUserInterface.py so as
#                   to facilitate the editing and maintenance
#                   of both files.
#
# ToDo:
#
#    None
#
##############################################################

__title__     = 'tsWxCursesServices'
__version__   = '2.42.1'
__date__      = '03/17/2015'
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

import curses

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
          if FIX_ME_cannot_change_color:
              reply = False
          else:
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

#---------------------------------------------------------------------------

if __name__ == '__main__':
 
    print(__header__)
