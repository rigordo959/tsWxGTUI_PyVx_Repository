#! /usr/bin/env python
# "Time-stamp: <03/28/2015  9:16:10 AM rsg>"
'''
tsWxEventDaemon.py - Class to establish a scheduling mechanism
to control the timing and sequencing of event processing.
'''
#################################################################
#
# File: tsWxEventDaemon.py
#
# Purpose:
#
#    Class to establish a scheduling mechanism to control the
#    timing and sequencing of event processing.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEventDaemon import Daemon
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#    See \WR\wxWidgets-2.8.10\src\common\event.cpp
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
#    None.
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
#    None.
#
# ToDo:
#
#    Under Construction.
#
#################################################################

__title__     = 'tsWxEventDaemon'
__version__   = '1.0.0'
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

import time
from threading import Thread

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

class EventDaemon(Thread):
    '''
    Establish a scheduling mechanism to control the timing and sequencing
    of event processing.

    Note: time.sleep is not guaranteed to sleep the right amount of time.
        It could be less (signal occured) or more.  Thus, we need to use
        the time before and after the sleep to determine how much time
        was slept.
    '''
 
    def __init__(self, timeToSleep=wx.EVT_DAEMON_TIMETOSLEEP):
        '''
        '''
        Thread.__init__(self)
        self.timeToSleep = timeToSleep
        self.previousTime = 0.0

    #-----------------------------------------------------------------------
 
    def run(self):
        currentTime = time.time()
        while True:
            self.previousTime = currentTime
            time.sleep(self.timeToSleep)
            currentTime = time.time()
            timeDifference = currentTime - self.previousTime
            if False:
                msg = 'Warning: _EventDaemon.run does not use ' + \
                      'timeDifference=%s' % timeDifference
                print(msg)
            else:
                pass
                # TBD Process the Timer queue
                # TBD Process the trigger waiting queue

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
