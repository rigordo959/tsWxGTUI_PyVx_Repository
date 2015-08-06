#! /usr/bin/env python
# "Time-stamp: <05/06/2015  6:24:56 AM rsg>"
'''
tsWxAcceleratorTable.py - Class to allow the application to
specify a table of keyboard shortcuts for menu or button
commands. The object wxNullAcceleratorTable is defined to be
a table with no data, and is the initial accelerator table
for a window.
'''
#################################################################
#
# File: tsWxAcceleratorTable.py
#
# Purpose:
#
#    Class to allow the application to specify a table of
#    keyboard shortcuts for menu or button commands. The object
#    wxNullAcceleratorTable is defined to be a table with no
#    data, and is the initial accelerator table for a window.
#
# Usage (example):
#
#    # Import
#
#    from tsWxAcceleratorTable import AcceleratorTable
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
#################################################################

__title__     = 'tsWxAcceleratorTable'
__version__   = '1.0.1'
__date__      = '04/01/2013'
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

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py3x.tsLibGUI.tsWxAcceleratorEntry import AcceleratorEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxObject import Object

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class AcceleratorTable(Object):
    '''
    An accelerator table allows the application to specify a table of
    keyboard shortcuts for menus or other commands. On Windows, menu
    or button commands are supported; on GTK, only menu commands are
    supported.

    The object wx.NullAcceleratorTable is defined to be a table with
    no data, and is the initial accelerator table for a window.

    An accelerator takes precedence over normal processing and can be
    a convenient way to program some event handling. For example, you
    can use an accelerator table to make a hotkey generate an event
    no matter which window within a frame has the focus.

    Example (from "wxPython in Action", pg. 308):
    acceltbl = wxAcceleratorTable([(wx.ACCEL_CTRL, ord('Q'), exit.GetId())])
    '''
    def __init__(self, entries):
        '''
        '''
        theClass = 'AcceleratorTable'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

 
        self.ts_AceleratorTable = wx.NullAcceleratorTable
        for anEntry in entries:

            self.ts_AceleratorTable += [anEntry]

        self.tsEndClassRegistration(theClass)

##    def __del__(self):
##        '''
##        '''
##        pass

    def IsOk(self):
        '''
        TBD - Not sure of functional requirements. The
        wx.AcceleratorTable.IsOk.__doc__ reports
        IsOk(self) -> bool.
        '''
        if self.ts_AceleratorTable == []:
            msg = '%s: ts_AceleratorTable is empty (%s)' % \
                  (__title__, self.ts_AceleratorTable)
            self.logger.error(msg)
            return (False)
        else:
            for entry in self.ts_AceleratorTable:
                actualType = type(entry)
                expectedType = AcceleratorEntry
                if not isinstance(entry, expectedType):
                    msg = '%s: actualType (%s) is not expectedType (%s)' % \
                          (__title__, actualType, expectedType)
                    self.logger.error(msg)
                    return (False)
                else:
                    msg = '%s: actualType (%s) is expectedType (%s)' % \
                          (__title__, actualType, expectedType)
                    self.logger.debug(msg)

                actualIsOk = entry.IsOk()
                expectedIsOk = True
                if not entry.IsOk():
                    msg = '%s: actualIsOk (%s) is not expectedIsOk (%s)' % \
                          (__title__, actualIsOk, expectedIsOk)
                    self.logger.error(msg)
                    return (False)
                else:
                    msg = '%s: actualIsOk (%s) is expectedIsOk (%s)' % \
                          (__title__, actualIsOk, expectedIsOk)
                    self.logger.debug(msg)

            return (True)

    def Ok(self):
        '''
        TBD - Not sure of functional requirements. The
        wx.AcceleratorTable.Ok.__doc__ reports
        IsOk(self) -> bool.
        '''
        return (self.IsOk())

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
