#! /usr/bin/env python
# "Time-stamp: <03/28/2015  4:13:31 PM rsg>"
'''
tsWxPyEventBinder.py - Instances of this class are used to bind
specific events to event handlers.
'''
#################################################################
#
# File: tsWxPyEventBinder.py
#
# Purpose:
#
#    Instances of this class are used to bind specific events
#    to event handlers.
#
# Usage (example):
#
#    # Import
#
#    from tsWxPyEventBinder import PyEventBinder
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
#    2012/06/06 rsg Changed self.evtType to self.ts_EventType.
#                   Added properties eventType and EventType
#                   as aliases for property typeId.
#
#    2012/06/23 rsg Created a placeholder for event instance
#                   argument data such as the nCurses mouse tuple.
#                   Added EventData property and associated
#                   _getEvtData and _SetData methods.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxPyEventBinder'
__version__   = '1.2.0'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

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

class PyEventBinder(object):
    '''
    Instances of this class are used to bind specific events to event
    handlers.
    '''
    def __init__(self, evtType, expectedIds=0, evtData=None):
        '''
        '''
        # Create a placeholder for event instance argument data
        # such as the nCurses mouse tuple.
        self.ts_EventData = evtData

        if DEBUG:
            # Install Logger access
            try:

                # Start the default application logger.
                self.logger = tsLogger.TsLogger(
                    threshold=tsLogger.ERROR,
                    start=time.time(),
                    name=tsLogger.StandardOutputFile)

            except Exception, e:

                self.logger = None
                msg = 'PyEventBinder._init__: Exception = %s' % e
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Check expected ids
        if expectedIds not in [0, 1, 2]:
            if DEBUG:
                msg = 'PyEventBinder._init__: Expected ids not 0, 1, or 2'
                self.logger.error(msg)
            raise ValueError, msg

        self.expectedIds = expectedIds

        # Insure we can iterate on the event type
        self.ts_EventType = wx.tsMakeIterable(evtType)

##        self.thisown = theClass

    #-----------------------------------------------------------------------

    def Bind(self,
             target,
             id1,
             id2,
             function,
             useSystemEventTable=False):
        '''
        Bind this set of event types to the target
        '''
        for et in self.ts_EventType:
            if DEBUG:
                fmt1 = 'tsWxEventBinder.Bind: et=%s; ' % str(et)
                fmt2 = 'target=%s; ' % str(target)
                fmt3 = 'id1=%d; ' % id1
                fmt4 = 'id2=%d; ' % id2
                fmt5 = 'function=%s' % function
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                self.logger.debug(msg)
            target.Connect(id1, id2, et, function)

    #-----------------------------------------------------------------------

    def Unbind(self,
               target,
               id1,
               id2,
               useSystemEventTable=False):
        '''
        Remove the event bindings.
        '''
        success = 0
        for et in self.ts_EventType:
            disconnect = target.Disconnect(id1, id2, et)
            if disconnect is not None:
                success += disconnect
            if DEBUG:
                fmt1 = 'tsWxEventBinder.Unbind: et=%s; ' % str(et)
                fmt2 = 'target=%s; ' % str(target)
                fmt3 = 'id1=%d; ' % id1
                fmt4 = 'id2=%d; ' % id2
                fmt5 = 'disconnect=%s' % disconnect
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                self.logger.debug(msg)

        return (success != 0)

    #-----------------------------------------------------------------------

    def _getEvtData(self):
        '''
        Easy with a property.
        '''
        return (self.ts_EventData)

    #-----------------------------------------------------------------------

    def _setEvtData(self, evtData):
        '''
        Easy with a property.
        '''
        self.ts_EventData = evtData

    #-----------------------------------------------------------------------

    def _getEvtType(self):
        '''
        Easy with a property.
        '''
        return (wx.tsMakeIterable(self.ts_EventType)) # (self.ts_EventType[0])

    #-----------------------------------------------------------------------

    def __call__(self, *args):
        '''
        Backwards compatibility with the old EVT_* functions.
        Should be called with either (window, func), (window, ID,
        func) or (window, ID1, ID2, func) parameters depending
        on the event type.
        '''
        assert len(args) == 2 + self.expectedIds

        id1 = wx.ID_ANY
        id2 = wx.ID_ANY
        target = args[0]

        if self.expectedIds == 0:

            func = args[1]

        elif self.expectedIds == 1:

            id1 = args[1]
            func = args[2]

        elif self.expectedIds == 2:

            id1 = args[1]
            id2 = args[2]
            func = args[3]

        else:
            if DEBUG:
                msg = 'PyEventBinder.__call__: Unexpected number of IDs'
                self.logger.error(msg)
            raise ValueError, msg

        self.Bind(target, id1, id2, func)

    #-----------------------------------------------------------------------

    EventData = property(_getEvtData, _setEvtData)
    EventType = property(_getEvtType)
    eventType = property(_getEvtType)
    typeId = property(_getEvtType)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
