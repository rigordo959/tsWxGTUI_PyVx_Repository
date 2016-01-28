#! /usr/bin/env python
#"Time-stamp: <04/20/2015  7:20:32 AM rsg>"
'''
tsGistGetTerminalSize.py - Module for acquiring the character
size of the Python console window as tuple (width, height) on host
operating systems (such as Linux, Mac OS X, Microsoft Windows and
Unix).
'''

#################################################################
#
# File: tsGistGetTerminalSize.py
#
# Purpose:
#
#     Module for acquiring the character size of the Python
#     console window as tuple (width, height) on host operating
#     systems (such as Linux, Mac OS X, Microsoft Windows and
#     Unix).
#
# Limitations:
#
#    None.
#
# Notes:
#
#    Derived from: https://gist.github.com/jtriley/1108174
#    by Justin T. Riley, created "terminalsize.py" for
#    gist 2011-07-26T14:59:00-07:00.
#
# Usage:
#
#    ## Import example:
#
#        import tsGistGetTerminalSize
#
#    ## Execute example:
#
#        python tsGistGetTerminalSize.py
#
# Methods:
#
#    __main__ - Print tuple (width, height) on linux, mac os x,
#                          windows, cygwin(windows)
#
#    get_terminal_size() - Return tuple (width, height) on
#                          linux, mac os x, windows,
#                          cygwin(windows)
#
#    _get_terminal_size_linux() -  Return tuple (width, height) on
#                          linux, mac os x and non-xterm on
#                          cygwin(windows)
#
#    _get_terminal_size_tput() - Return tuple (width, height) in
#                          cygwin's xterm on windows.
#
#    _get_terminal_size_windows() - Return tuple (width, height) on
#                          windows.
#
# Modifications:
#
#    2013/10/17 rsg Documented gist source and modifications.
#                   Converted print statement to print function.
#                   Added __header__ and current_os to print
#                   output.
#                   Created Python 3.x port from Python 2..x
#
#    2015/03/22 rsg Conditionalized use of subprocess.
#
#    2015/04/20 rsg Modified method _get_terminal_size_tput
#                   to replace reference to sts.version by
#                   reference to sys.version. Also replaced
#                   "except:" by "except Exception,
#                   tsGetHostConsoleDisplaySizeErrorCode".
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsGistGetTerminalSize'
__version__   = '1.1.0'
__date__      = '04/20/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013-2015 ' + \
    '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
    'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  terminalsize (https://gist.github.com/' + \
                'jtriley/1108174) Features: ' + \
                '\n\t  Copyright (c) 2011 Justin T. Riley.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if ((len(__credits__) == 0)):
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

import os
import shlex
import struct
import sys
import platform
import subprocess

#--------------------------------------------------------------------------
 
def get_terminal_size():
    """ getTerminalSize()
     - get width and height of console
     - works on linux,os x,windows,cygwin(windows)
     originally retrieved from:
     http://stackoverflow.com/questions/566746/
            how-to-get-console-window-width-in-python
    """
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        print("default")
        tuple_xy = (80, 25)      # default value
    return tuple_xy

#--------------------------------------------------------------------------
 
def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass

#--------------------------------------------------------------------------

def _get_terminal_size_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/
    #             how-do-i-find-the-width-height-of-a-terminal-window
    #
    # RSG Added exception handler for use by Python versions < 2.4
    #     that do not support subprocess operations.
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except Exception, tsGetHostConsoleDisplaySizeErrorCode:
        fmt1 = 'WARNING: '
        fmt2 = '"_get_terminal_size_tput" not supported with '
        fmt3 = '\n\tsys.version=%s; \n' % str(sys.version)
        fmt4 = '\n\terrorCode: %s' % str(
	    tsGetHostConsoleDisplaySizeErrorCode)
        msg = fmt1 + fmt2 + fmt3 + fmt4
        print(msg)
        pass

#--------------------------------------------------------------------------
 
def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

    print(__header__)

    sizex, sizey = get_terminal_size()
    print('\n  width = %d; height = %d' % (sizex, sizey))

    current_os = platform.system()
    print('\n  current_os = %s' % current_os)
