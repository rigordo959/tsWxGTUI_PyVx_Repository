#! /usr/bin/env python
# "Time-stamp: <09/20/2013  4:38:02 AM rsg>"
'''
test_tsWxAcceleratorEntry.py - Class to emulate the wxPython API for
non-graphical, curses-based platforms.
'''
#################################################################
#
# File: test_tsWxAcceleratorEntry.py
#
# Purpose:
#
#    Class to emulate the wxPython API for non-graphical,
#    curses-based platforms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxAcceleratorEntry import AcceleratorEntry
#
# Requirements:
#
#    wxPython 2.8.9.2.
#
# Capabilities:
#
#    wxPython 2.8.9.2.
#
# Limitations:
#
#    wxPython 2.8.9.2.
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2.
#
# Classes:
#
#    wxPython 2.8.9.2.
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

import platform

##import tsExceptions as tse

##import tsWxGlobals as wx

__title__     = 'test_tsWxAcceleratorEntry'
__version__   = '0.0.0'
__date__      = '03/20/2010'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2010 TeamSTARS. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

##DEBUG = wx.DEBUG

wxACCEL_NORMAL  = 0x0000 # no modifiers
wxACCEL_ALT     = 0x0001 # hold Alt key down
wxACCEL_CTRL    = 0x0002 # hold Ctrl key down
wxACCEL_SHIFT   = 0x0004 # hold Shift key down

if platform.system == 'Darwin':
    wxACCEL_CMD      = 0x0008 # Command key on OS X
else:
    wxACCEL_CMD      = wxACCEL_CTRL

#---------------------------------------------------------------------------

import wx

def display(x):
    flags = '%s' % x.GetFlags()
    keyCode = '%s' % x.GetKeyCode()
    command = '%s' % x.GetCommand()
    isOk = '%s' % x.IsOk()
    if x.IsOk():
        try:
            toString = '%s' % x.ToString()
        except Exception as e:
            toString = '%s' % e
    else:
        toString = ''

    print('\t%5s\t%7s\t%7s\t%7s\t"%s"' % \
          (isOk, flags, keyCode, command, toString))

if __name__ == '__main__':

    print(__header__)

    entry = wx.AcceleratorEntry()

##    print('\tIsOk\tFlags\tKeyCode\tCommand\tToString')

##    display(entry)

    ##entry.Set(100, 0, 0)
    ##display(entry)

    ##entry.Set(0, 200, 0)
    ##display(entry)

    ##entry.Set(0, 0, 300)
    ##display(entry)

    ##entry.Set(100, 200, 300)
    ##display(entry)

    separatorCommand = '=' *60
    separatorKeyCode = '-' *60

    for Command in range(0, 256, 16):
        print('\n%s' % separatorCommand)

        print('\tIsOk\tFlags\tKeyCode\tCommand\tToString')

        for keyCode in range(0, 128, 1):
            print('\n\t%s' % separatorKeyCode)

            for flag in [
                wxACCEL_NORMAL,
                wxACCEL_ALT,
                wxACCEL_CTRL,
                wxACCEL_SHIFT,
                wxACCEL_CMD,

                wxACCEL_ALT | wxACCEL_CTRL,
                wxACCEL_ALT | wxACCEL_SHIFT,
                wxACCEL_ALT | wxACCEL_CMD,

                wxACCEL_CTRL | wxACCEL_SHIFT,
                wxACCEL_CTRL | wxACCEL_CMD,
 
                wxACCEL_ALT | wxACCEL_CTRL | wxACCEL_SHIFT | wxACCEL_CMD
                ]:

                entry.Set(flag, keyCode, Command)
                display(entry)
