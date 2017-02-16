#! /usr/bin/env python
# "Time-stamp: <10/25/2013  7:31:14 AM rsg>"
'''
tsWxEventQueueEntry.py - Class to establish a container for
the triggering object, triggering data and triggering event.
'''
#################################################################
#
# File: tsWxEventQueueEntry.py
#
# Purpose:
#
#    Class to establish a container for the triggering object,
#    triggering data and triggering event.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEventQueueEntry import EventQueueEntry
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
#    2012/05/21 rsg Added support for triggeringData that
#                   conveys instance specific information from
#                   the triggeringObject that is associacted
#                   with the triggeringEvent.
#
#    2012/05/21 rsg Re-organized the methods into alphabetical order.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxEventQueueEntry'
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

##import tsWxGlobals as wx # Invalid import because of circular dependency.
import tsCxGlobals as cx

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

class EventQueueEntry(object):
    '''
    Establish a  a container for the triggering object, triggering data and
    triggering event.
    '''
    def __init__(self,
                 triggeringObject=None,
                 triggeringEvent=None,
                 triggeringData=None):
        '''
        Construct a container for triggering object and triggering event.
        '''
        self.ts_TriggeringObject = triggeringObject
        self.ts_TriggeringEvent = triggeringEvent
        self.ts_TriggeringData = triggeringData

    #-----------------------------------------------------------------------
 
    def __del__(self):
        '''
        Destroy a container for triggering object and triggering event.
        '''
        del self.ts_TriggeringObject
        del self.ts_TriggeringEvent
        del self.ts_TriggeringData
        del self

    #-----------------------------------------------------------------------

    def GetTriggeringData(self):
        '''
        Return TriggeringData
        '''
        return (self.ts_TriggeringData)

    #-----------------------------------------------------------------------

    def GetTriggeringEvent(self):
        '''
        Return TriggeringEvent
        '''
        return (self.ts_TriggeringEvent)

    #-----------------------------------------------------------------------
 
    def GetTriggeringObject(self):
        '''
        Return TriggeringObject
        '''
        return (self.ts_TriggeringObject)

    #-----------------------------------------------------------------------
 
    def GetTriggeringObjectParent(self):
        '''
        Return Parent of TriggeringObject
        '''
        try:
            return (self.ts_TriggeringObject.ts_Parent)
        except Exception, e:
            return (None)

    #-----------------------------------------------------------------------

    TriggeringData = property(GetTriggeringData)
    TriggeringEvent = property(GetTriggeringEvent)
    TriggeringObject = property(GetTriggeringObject)
    TriggeringObjectParent = property(GetTriggeringObjectParent)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
