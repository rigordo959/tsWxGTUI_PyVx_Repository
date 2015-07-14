#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:28:33 AM rsg>"
'''
tsWxTimer.py - Class to allow you to execute code at specified
intervals. Its precision is platform-dependent, but in general
will not be better than 1ms nor worse than 1s.
'''
#################################################################
#
# File: tsWxTimer.py
#
# Purpose:
#
#    Class to allow you to execute code at specified intervals.
#    Its precision is platform-dependent, but in general will
#    not be better than 1ms nor worse than 1s.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTimer import Timer
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
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxTimer'
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

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxEvtHandler import EvtHandler

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#--------------------------------------------------------------------------

class TimerDescriptor(object):
    '''
    Class to allow you to execute code at specified intervals. Its
    precision is platform-dependent, but in general will not be better
    than 1ms nor worse than 1s.

    There are three different ways to use this class:

    1) You may derive a new class from wxTimer and override the
    wxTimer.Notify member to perform the required action.

    2) You may redirect the notifications to any wxEvtHandler derived
    object by using the non-default constructor or wxTimer.SetOwner.
    Then use the EVT_TIMER macro to connect it to the event handler
    which will receive wxTimerEvent notifications.

    3) You may use a derived class and the EVT_TIMER macro to connect
    it to an event handler defined in the derived class. If the default
    constructor is used, the timer object will be its own owner object,
    since it is derived from wxEvtHandler.

    In any case, you must start the timer with wxTimer.Start() after
    constructing it before it actually starts sending notifications.
    It can be stopped later with wxTimer.Stop().

    Note: A timer can only be used from the main thread.

 
    from timer.cpp
    '''
    def __init__(self, timer):
        '''
        '''
        # Init timer descriptor
        self.ts_timer = timer
        self.ts_running = False
        self.ts_Next = None
        self.ts_Previous = None
        # TBD Number of Event Daemon ticks
        self.ts_shotTime = 0
        self.ts_DeleteFlag = None

#--------------------------------------------------------------------------

class TimerQueue(object):
    '''
    TBD Timer Queue
    '''
 
    _theQueue = []

    #-----------------------------------------------------------------------
 
    @classmethod
    def addToQueue(cls, item):
        cls._theQueue.append(item)

    #-----------------------------------------------------------------------
 
    @classmethod
    def removeFromQueue(cls, item):
        cls._theQueue.remove(item)
 
#--------------------------------------------------------------------------

class TimerScheduler(object):
    '''
    TBD Timer scheduler
    '''
    def __init__(self):
        '''
        '''
        # Init timer queue to empty
        self.timerQueue = TimerQueue()

    #-----------------------------------------------------------------------
 
    def QueueTimer(self, timer):
        '''
        TBD QueueTimer
        '''
        if timer.ts_TimerDescriptor is None:
            timer.ts_descriptor = TimerDescriptor(timer)
        self.timerQueue.addToQueue(timer.ts_descriptor)

    #-----------------------------------------------------------------------
 
    def RemoveTimer(self, timer):
        '''
        TBD RemoveTimer
        '''
        self.timerQueue.removeFromQueue(timer.ts_descriptor)

    #-----------------------------------------------------------------------
 
    def NotifyTimers(self):
        '''
        TBD NotifyTimers
        '''
        pass
 
#--------------------------------------------------------------------------

class TimerBase(EvtHandler):
    '''
 
    owner = class that has EvtHandler.
    id = id to use.
 
    Proxy of C++ Timer class.
    '''
 
    ts_scheduler = None

    #-----------------------------------------------------------------------
 
    def __init__(self,
                 owner,
                 id=wx.ID_ANY):
        '''
        Construct an interval timeout event generator.
        '''
        theClass = 'TimerBase'

        # Capture initial caller parametsrs before they are changed
        self.caller_owner = owner
        self.caller_id = id

        wx.RegisterFirstCallerClassName(self, theClass)

        EvtHandler.__init__(self)

        id = wx.ID_ANY

        self.tsBeginClassRegistration(theClass, id)

        # Init the scheduler
        if TimerBase.ts_scheduler is None:
            TimerBase.ts_scheduler = TimerScheduler()
 
        # Register each unique wxPython instance.
        self.ts_TimerAssignedId = self.tsNewId()
        self.ts_Id = id
 
        self.ts_Milliseconds = -1
        self.ts_Owner = owner
        self.ts_Tag = -1
        self.ts_running = False
        self.ts_oneShot = False
        self.ts_TimerDescriptor = None

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    wxTimerBase::~wxTimerBase()
##    {
##        // this destructor is required for Darwin
##    }

    #-----------------------------------------------------------------------

##        wxTimerEvent event(m_idTimer, m_milli);
##        event.SetEventSource(this);
##        (void)m_owner->ProcessEvent(event);
##    }

    #-----------------------------------------------------------------------
 
    def GetOwner(self):
        '''
        '''
        return self.ts_Owner

    #-----------------------------------------------------------------------
 
    def GetId(self):
        '''
        '''
        if self.ts_Id != wx.ID_ANY:
            return (self.ts_Id)
        else:
            return (self.ts_TimerAssignedId)

    #-----------------------------------------------------------------------

    def GetInterval(self):
        '''
        '''
        return self.ts_Milliseconds

    #-----------------------------------------------------------------------

    def IsOneShot(self):
        '''
        TBD
        '''
        return self.ts_oneShot

    #-----------------------------------------------------------------------

    def IsRunning(self):
        '''
        TBD
        '''
        return self.ts_running

    #-----------------------------------------------------------------------

    def Notify(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Notify in tsWxTimer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##    void wxTimerBase::Notify()
##    {
##        // the base class version generates an event if it has owner - which it
##        // should because otherwise nobody can process timer events
##        wxCHECK_RET( m_owner, _T("wxTimer::Notify() should be overridden.") );

    #-----------------------------------------------------------------------

    def SetOwner(self, owner, id):
        '''
        TBD
        '''
        if owner is not None:
            self.ts_Owner = owner
        if id != wx.ID_ANY:
            self.ts_Id = id

    #-----------------------------------------------------------------------
 
    @staticmethod
    def NotifyTimers():
        if TimerBase.ts_scheduler is not None:
            TimerBase.ts_scheduler.NotifyTimers()

    #-----------------------------------------------------------------------

    def Start(self, milliseconds, oneShot=False):
        '''
        TBD - Add to EventDaemon queue.
        '''
        if self.ts_running:
            self.Stop()
 
        if milliseconds != -1:
            self.ts_Milliseconds = milliseconds
 
        # TBD self.ts_Tag = self.TimeoutAdd(self.ts_Milliseconds, self.tsTimeoutCallback)
 
        self.ts_oneShot = oneShot

        self.ts_scheduler.QueueTimer(self)
 
        return (True)

##    bool wxTimerBase::Start(int milliseconds, bool oneShot)
##    {
##        // under MSW timers only work when they're started from the main thread so
##        // let the caller know about it
##    #if wxUSE_THREADS
##        wxASSERT_MSG( wxThread::IsMain(),
##                      _T("timer can only be started from the main thread") );
##    #endif // wxUSE_THREADS

##        if ( IsRunning() )
##        {
##            // not stopping the already running timer might work for some
##            // platforms (no problems under MSW) but leads to mysterious crashes
##            // on the others (GTK), so to be on the safe side do it here
##            Stop();
##        }

##        if ( milliseconds != -1 )
##        {
##            m_milli = milliseconds;
##        }

##        m_oneShot = oneShot;

##        return true;
##    }

    #-----------------------------------------------------------------------

    def Stop(self):
        '''
        TBD - Remove from EventDaemon queue.
        '''
        self.ts_scheduler.RemoveTimer(self)

    #-----------------------------------------------------------------------

    Id = property(GetId)
    Interval = property(GetInterval)
    Owner = property(GetOwner, SetOwner)

    #-----------------------------------------------------------------------

##    // ============================================================================
##    // wxTimerBase implementation
##    // ============================================================================

#--------------------------------------------------------------------------

class Timer(TimerBase):
    '''
 
    owner = class that has EvtHandler.
    id = id to use.
 
    Proxy of C++ Timer class.
    '''
    def __init__(self,
                 owner=None,
                 id=wx.ID_ANY):
        '''
        Construct an interval timeout event generator.
        '''
        theClass = 'Timer'

        wx.RegisterFirstCallerClassName(self, theClass)

        TimerBase.__init__(self, owner, id)

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('              owner: %s' % owner)
            self.logger.debug('                 id: %s' % id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('    TimerAssignedId: %s' % self.ts_TimerAssignedId)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        self.Stop()

    #-----------------------------------------------------------------------

    def Destroy(self):
        '''
        NO-OP: Timers must be destroyed by normal reference counting.
        '''
        del self

    #-----------------------------------------------------------------------

    def Stop(self):
        '''
        TBD - Remove from EventDaemon queue
        '''
        if not self.ts_running:
            return
        if self.ts_Tag != -1:
            self.ts_Tag = -1
 
        self.ts_scheduler.RemoveTimer(self)

    #----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsTimeoutCallback(self):
        '''
        '''
        # Don't change the order of anything in this callback!

        if (self.IsOneShot()):
            self.Stop()

        # When getting called from GDK's timer handler we
        # are no longer within GDK's grab on the GUI
        # thread so we must lock it here ourselves.
        # TBD gdk_threads_enter()

        self.Notify()

        # Release lock again.
        # TBD gdk_threads_leave()

        if (self.IsOneShot()):
            return (False)

        return (True)
 
    # End tsWx API Extensions
    #----------------------------------------------------------------------

#--------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

