#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:39:52 AM rsg>"
'''
test_tsWxPySimpleApp.py - Application program to mimic some
features of the Graphical TextUser Interface.
'''
#################################################################
#
# File: test_tsWxPySimpleApp.py.py
#
# Purpose:
#
#    Application program to mimic some features of the
#    Graphical Text User Interface.
#
#
#    1. Frame
#    2. one main panel added to Frame
#    3. two panels, one left and one right, added to main panel
#    4. two buttons in the left panel (plus and minus)
#    5. one text widget in the right panel used as a counter
#    6. the plus button will add one to the counter
#    7. the minus button will subtract one from the counter
#
# Limitations:
#
#    1) None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxPySimpleApp.py
#
# Methods:
#
# ToDo:
#   1. Show menu help in status bar - works on MS Windows
#   2. Fix minimum size - can resize the Frame too small
#      added fix - doesn't quite work on MacOS, need to check MS Windows
#
# Modifications:
#
#################################################################

__title__     = 'test_tsWxPySimpleApp'
__version__   = '0.0.2'
__date__      = '06/25/2009'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2009 TeamSTARS. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__,
                                         __line2__,
                                         __line3__)

mainTitleVersionDate = __line1__

import sys
import time
import traceback

try:
    import tsLibraries
except:
    pass

import tsApplication as tsAPP
import tsExceptions as tse
import tsLogger as Logger

try:
    import wx
except ImportError as wxImportError:
    import tsWx as wx

WXPYTHON_EMULATION = True

__help__ = '''
This program shows the most basic wxPython application. It creates a frame
and displays "Hello World".
'''

mainTitleVersionDate = __line1__

#---------------------------------------------------------------------------

class cliAPP(tsAPP.TsApplication):
    '''
    Class to establish the application specific control components.
    '''
    def __init__(self, *args, **kw):
        '''
        Add our main entry point to kw
        Init tsApp
        '''
        kw['main'] = self.main
        tsAPP.TsApplication.__init__(self, *args, **kw)
        self.theWindowLogger = Logger.TsLogger(threshold = Logger.DEBUG,
                                               start = time.time(),
                                               name = 'stdscr')

    def main(self):
        '''
        Get a wx App
        Build the communicate Frame
        Enter wx main loop
        '''
        app = wx.PySimpleApp(redirect=True,
                             filename=None)
        frame = wx.Frame(None, title='Hello World')
        frame.Show()

        message = 'Started timestamped wxPython: stdout/stderr\n\n' + \
                  'Print statements and other standard output ' + \
                  'will now be directed to this window.'

        self.theWindowLogger.info(message)

        self.theWindowLogger.debug('Before MainLoop')
        print("Before MainLoop")
        app.MainLoop()
        print("After MainLoop")
        self.theWindowLogger.debug('After MainLoop')

#---------------------------------------------------------------------------

if __name__ == '__main__':
    '''
    Create my App
    Run the main entry point
    '''
    # Remember original stdout and stderr
    #  WxPython makes them graphical
    _stdout = sys.stdout
    _stderr = sys.stderr

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:
        theApplication = cliAPP(
            header=__header__,
            mainTitleVersionDate=mainTitleVersionDate,
            title=__title__,
            version=__version__,
            date=__date__,
            logs=[])

        theApplication.runMain()

    except Exception as e:
        if isinstance(e, tse.TsExceptions):
            msg = str(e)
            tse.displayError(e)
            exitStatus = e.exitCode
        else:
            msg = None
            _stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

##    print __header__
#    _stdout.write(__header__)

    if msg == tse.NO_ERROR:
        _stdout.write(msg + '\n')

    elif msg is not None:
        _stderr.write(msg.replace('"', '') + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)
