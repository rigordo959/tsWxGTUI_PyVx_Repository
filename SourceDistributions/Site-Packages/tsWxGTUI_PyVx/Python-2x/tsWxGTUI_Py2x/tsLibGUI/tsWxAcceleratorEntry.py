#! /usr/bin/env python
# "Time-stamp: <03/28/2015  7:58:30 AM rsg>"
'''
tsWxAcceleratorEntry.py - Class to establish an object used by
an application wishing to create an accelerator table
(see wxAcceleratorTable).
'''
#################################################################
#
# File: tsWxAcceleratorEntry.py
#
# Purpose:
#
#    Class to establish an object used by an application wishing
#    to create an accelerator table (see wxAcceleratorTable).
#
# Usage (example):
#
#    # Import
#
#    from tsWxAcceleratorEntry import AcceleratorEntry
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    2012/07/29 rsg Corrected staticmethod Create to eliminate
#                   references to self.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxAcceleratorEntry'
__version__   = '1.0.1'
__date__      = '04/0/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'

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

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class AcceleratorEntry(object):
    '''
    A class used to define items in an wx.AcceleratorTable. wxPython
    programs can choose to use wx.AcceleratorEntry objects, but using
    a list of 3-tuple of integers (flags, keyCode, cmdID) usually
    works just as well. See __init__ for use of the tuple values.
    '''
    def __init__(self, flags=0, keyCode=0, cmdID=0):
        '''
        Construct a wx.AcceleratorEntry.

        flags - A bitmask of wx.ACCEL_ALT, wx.ACCEL_SHIFT, wx.ACCEL_CTRL,
        wx.ACCEL_CMD, or wx.ACCEL_NORMAL used to specify which modifier
        keys are held down. (type=int)

        keyCode - The keycode to be detected. (type=int)

        cmdID - The menu or control command ID to use for the accellerator
        event. (type=int)
        '''
        theClass = 'AcceleratorEntry'

        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

        try:
            CmdID = int(cmdID)
            Flags = int(flags)
            KeyCode = int(keyCode)

            self.ts_AcceleratorEntry = (Flags, KeyCode, CmdID)
        except:
            self.ts_AcceleratorEntry = None

##        self.tsEndClassRegistration(theClass)

##    def __del__(self):
##        '''
##        '''
##        pass

    @staticmethod
    def Create(str):
        '''
        Create accelerator corresponding to the specified string, or None
        if it could not be parsed.
        '''
        try:

            (flags, keyCode, cmdID) = str.split('-')

            CommandID = int(cmdID)
            Flags = int(flags)
            KeyCode = int(keyCode)

            passed = True

        except:

            passed = False

        if passed:

            return (AcceleratorEntry(flags=Flags,
                                     keyCode=KeyCode,
                                     cmdID=CommandID))
        else:

            return (None)

    def FromString(self, str):
        '''
        Returns true if the given string correctly initialized this object.
        '''
        try:
            (flags, keyCode, cmdID) = str.split('-')

            CmdID = int(cmdID)
            Flags = int(flags)
            KeyCode = int(keyCode)

            self.ts_AcceleratorEntry = (Flags, KeyCode, CmdID)
            passed = True
        except:
            self.ts_AcceleratorEntry = None
            passed = False

        return (passed)

    def GetCommand(self):
        '''
        Get the AcceleratorEntry command ID.
        '''
        if self.ts_AcceleratorEntry is None:
            cmdID = None
        else:
            (flags, keyCode, cmdID) = self.ts_AcceleratorEntry

        return (cmdID)

    def GetFlags(self):
        '''
        Get the AcceleratorEntry flags.
        '''
        if self.ts_AcceleratorEntry is None:
            flags = None
        else:
            (flags, keyCode, cmdID) = self.ts_AcceleratorEntry

        return (flags)

    def GetKeyCode(self):
        '''
        Get the AcceleratorEntry keycode.
        '''
        if self.ts_AcceleratorEntry is None:
            keyCode = None
        else:
            (flags, keyCode, cmdID) = self.ts_AcceleratorEntry

        return (keyCode)

    def IsOk(self):
        '''
        '''
        if self.ts_AcceleratorEntry is None:
            return (False)
        else:
            return (True)

    def Set(self, flags, keyCode, cmdID):
        '''
        (Re)set the attributes of a wx.AcceleratorEntry.
        '''
        try:
            CmdID = int(cmdID)
            Flags = int(flags)
            KeyCode = int(keyCode)

            self.ts_AcceleratorEntry = (Flags, KeyCode, CmdID)
        except:
            self.ts_AcceleratorEntry = None

    def ToString(self):
        '''
        Returns a string representation for the this accelerator.
        '''
        textCmdID = str(self.GetCommand())
        textFlags = str(self.GetFlags())
        textKeyCode = str(self.GetKeyCode())
 
        text = '%s-%s-%s' % (textFlags, textKeyCode, textCmdID)
        return (text)

    Command = property(GetCommand)
    Flags = property(GetFlags)
    KeyCode = property(GetKeyCode)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
