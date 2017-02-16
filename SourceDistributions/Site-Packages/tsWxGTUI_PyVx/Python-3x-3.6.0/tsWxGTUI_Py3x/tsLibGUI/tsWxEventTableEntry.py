#! /usr/bin/env python
# "Time-stamp: <03/28/2015  9:19:40 AM rsg>"
'''
tsWxEventTableEntry.py - Class to establish a container for
event table information (eventType, id, lastId, func, userData).
'''
#################################################################
#
# File: tsWxEventTableEntry.py
#
# Purpose:
#
#    Class to establish a container for event table information
#    (eventType, id, lastId, func, userData).
#
# Usage (example):
#
#    # Import
#
#    from tsWxEventTableEntry import EventTableEntry
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
#    2012/06/06 rsg Changed self.evtType to self.ts_EventType.
#                   Added properties eventType and EventType
#                   as aliases for evtType.
#
# ToDo:
#
#    Under Construction.
#
#################################################################

__title__     = 'tsWxEventTableEntry'
__version__   = '1.1.0'
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

import copy

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class EventTableEntry(object):
    '''
    Establish a container for event table information (eventType, id,
    lastId, func, userData).

    Note: eventSink is the reference to the object that contains
          the func.  Should not be needed in pure python
    '''
 
    def __init__(self, eventType, id, lastId, func=None, userData=None):
        '''
        '''
        if userData is not None:
            self.ts_callbackUserData = copy.deepcopy(userData)
        else:
            self.ts_callbackUserData = userData

        self.ts_EventType = eventType
        self.ts_func = func
        self.ts_id = id
        self.ts_lastId = lastId

    #-----------------------------------------------------------------------
 
    def getEventType(self):
        return (self.ts_EventType)

    #-----------------------------------------------------------------------

    def getId(self):
        return (self.ts_id)

    #-----------------------------------------------------------------------

    def getLastId(self):
        return (self.ts_lastId)

    #-----------------------------------------------------------------------

    def getFunc(self):
        return (self.ts_func)

    #-----------------------------------------------------------------------

    def getUserData(self):
        '''
        TBD userData??
        '''
        return (self.ts_callbackUserData)

    #-----------------------------------------------------------------------

    EventType = property(getEventType)
    eventType = property(getEventType)
    evtType = property(getEventType)
    func = property(getLastId)
    id = property(getId)
    lastId = property(getFunc)
    userData = property(getUserData)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
