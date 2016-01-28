#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:18:40 AM rsg>"
'''
tsWxEvtHandler.py - Class to handle events from the windowing
system.
'''
#################################################################
#
# File: tsWxEvtHandler.py
#
# Purpose:
#
#    Class to handle events from the windowing system.
#
# Usage (example):
#
#    # Import
#
#    from tsWxEvtHandler import EvtHandler
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
#    From "wxPython in Action" by Noel Rappin and Robin Dunn, Copyright
#    2006 by Manning Publications Co., 209 Bruce Park Avenue, Greenwich,
#    CT 06830
#
#    Section 3.4.1 - Understanding the event handling process
#
#    The following pseudo code characterizes the event handling process.
#
#    def tsEventHandlingProcess(self,
#                               triggeringObject=None,
#                               triggeringEvent=None):
#        '''

#        triggeringObject - The Window/Control Object most likey to handle
#        the triggeringEvent.

#        triggeringEvent - The event from Keyboard, Mouse/Pointer, Timer, etc.

#        The event process begins with the object that triggered the event.
#        Typically, wxPython looks first at the triggering object for a bound
#        handler function matching the event type. If one is found, the method
#        is executed. If not, wxPython checks to see if the event propagates
#        up the container hierarchy. If so, the parent widget is checked, up
#        the hirerarchy, until wxPython either finds a handler function or hits
#        a top-level object. If the event does not propagate, wxPython still
#        checks the application object for a handler method before finishing.
#        When an event handler is run, the process typically ends. However,
#        the function can tell wxPython to continue searching for handlers.
#        '''
#        if (triggeringObject is None) and \
#           (triggeringEvent is None):

#            fmt1 = 'Missing arguments for tsEventHandlingProcess '
#            fmt2 = 'in tsWxEventLoop.'
#            msg = fmt1 + fmt2
#            self.logger.error(msg)
#            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

#        # Starting Point: Event Triggered
#        #
#        # Python Object is TriggeringObject
#        if triggeringObject.isEnabled:
#            # Yes, is enabled
#            if triggeringObject.hasMatchingHandler(triggeringEvent):
#                # Yes, has matching handler
#                # Python Event Handling Method
#                skip = triggeringObject.eventHandler()
#                if skip:
#                    # Yes, no matching event handler
#                    if triggeringObject.shouldPropagate:
#                        # Yes. event should propagate
#                        if triggeringObject.isThisTheApp:
#                            # Yes, this is the app
#                            done = True
#                        else:
#                            # No, this is not the app
#                            # Python Object is container
#                            # Process Python Object
#                            self.tsEventHandlingProcess(
#                                triggeringObject.parent,
#                                triggeringEvent)
#                            # TBD - Is Done appropriate?
#                            done = True
#                    else:
#                        # No, event should not propagate
#                        done = True
#        else:
#            # No, is not enabled
#            if triggeringObject.shouldPropagate:
#                # Yes, should propagate
#                if triggeringObject.isThisTheApp:
#                    # Yes, this is the app
#                    done = True
#                else:
#                    # No, this is not the app
#                    # Python Object is container
#                    # Process Python Object
#                    self.tsEventHandlingProcess(
#                        triggeringObject.parent,
#                        triggeringEvent)
#                    done = True
#            else:
#                # No, should not propagate
#                # Python Object is Application (i.e., wxPyApp mainloop)
#                applicationObject = triggeringObject.ts_EarliestAncestor
#                self.tsEventHandlingProcess(
#                    applicationObject,
#                    triggeringEvent)
#                done = True
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
#    2010/11/27 rsg Introduced stubs for wxWidgets 2.9.1.1 event
#                   handling methods.
#
#    2010/12/01 rsg Removed support for multiple instances of
#                   tsWxEvtHandler and associated clas variables.
#
#    2010/12/06 rsg Renamed "tsProcessCursesEvent" to
#                   "tsProcessBoundEvent". The method is used
#                   by "ProcessEvent" to handle events created
#                   via "PyEventBinder". Such events do not have
#                   access to the methods and instance variables
#                   associated with the "Event" class.
#
#    2010/12/13 rsg Renamed "tsProcessBoundEvent" to
#                   "tsProcessPyEventBinderEvent". It identifies
#                   and initiates the appropriate event handler
#                   for those events associated with "PyEventBinder".
#                   Such events do not otherwise have access to
#                   the methods and instance variables associated
#                   with the "Event" class.
#
#    2010/12/13 rsg Created "tsProcessNonPyEventBinderEvent". It
#                   identifies and initiates the appropriate event
#                   handler for those events not associated with
#                   "PyEventBinder". Such events have access to
#                   the methods and instance variables associated
#                   with the "Event" class.
#
#    2010/12/19 rsg Corrected "ProcessEvent". Replaced "PyEventBinder"
#                   with traditional "Event" parameter.
#
#    2010/12/20 rsg Merged "tsProcessNonPyEventBinderEvent" back into
#                   "ProcessEvent" and added appropriate link to
#                   "tsProcessPyEventBinderEvent".
#
#    2012/02/12 rsg Modified tsProcessPyEventBinderEvent to
#                   replace event table references to 'objectAssignedId'
#                   by references to 'source'.
#
#    2012/02/21 rsg Added tsProcessEventTables.
#
#    2012/05/21 rsg Added triggeringMouseTuple argument to the methods
#                   tsProcessEventTables and tsProcessSelectedEventTable.
#                   The optional argument passes mouse position.
#
#    2012/05/21 rsg Added EvtHandler._PendingEventList and
#                   EvtHandler._PendingEventHandlerList.
#
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
#    2012/07/27 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#
#    2013/07/01 rsg Upgraded to use threads and ProcessEvent.
#
# ToDo:
#
#    2010/11/29 - Complete the definition of the underlying
#                 infrastructure.
#
#################################################################

__title__     = 'tsWxEvtHandler'
__version__   = '2.0.0'
__date__      = '07/02/2013'
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

try:
    import thread
    import threading
except ImportError:
    thread = None

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI.tsWxDoubleLinkedList import DoubleLinkedList
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxEventDaemon import EventDaemon
from tsWxGTUI_Py2x.tsLibGUI.tsWxEventLoop import EventLoop as wxEventLoop
from tsWxGTUI_Py2x.tsLibGUI.tsWxEventQueueEntry import EventQueueEntry
from tsWxGTUI_Py2x.tsLibGUI.tsWxEventTableEntry import EventTableEntry
from tsWxGTUI_Py2x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py2x.tsLibGUI.tsWxPyEventBinder import PyEventBinder

#--------------------------------------------------------------------------

##from tsWxApp import App as wxApp # WARNING: Raises fatal import error.
wxTheApp = None # wxApp.wxTheApp

if thread is None:
    useThreads = False
else:
    useThreads = True

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class EvtHandler(Object):
    '''
    A class that can handle events from the windowing system.

    wxWindow is (and therefore all window classes are) derived from this class.

    When events are received, wxEvtHandler invokes the method listed in the
    event table using itself as the object. When using multiple inheritance
    it is imperative that the wxEvtHandler(-derived) class is the first class
    inherited such that the this pointer for the overall object will be
    identical to the this pointer of the wxEvtHandler portion.
    '''
    # Class Variables

    _PendingEventList = DoubleLinkedList()
    _PendingEventHandlerList = DoubleLinkedList()

    #-----------------------------------------------------------------------
 
    def __init__(self):
        '''
        Constructor.
        '''
        theClass = 'EvtHandler'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        self.ts_CurrentlyActiveHandler = None

        self.ts_DynamicEventTable = []
        self.ts_Enabled = True
        self.ts_EvtHandlerEnabled = False
        self.ts_NextHandler = None
        self.ts_PendingEventList = EvtHandler._PendingEventList
        self.ts_PendingEventHandlerList = EvtHandler._PendingEventHandlerList
        self.ts_PreviousHandler = None

        # no client data (yet)
        self.ts_ClientData = None
        self.ts_ClientDataType = None
        self.ts_ClientObject = None

        self.ts_TriggeringEvent = None
        self.ts_TriggeringObject = None
        self.ts_EventQueueEntry = None

        if useThreads:
            self.logger.debug('Starting Event Daemon Thread')
            self.ts_EventDaemonThread = EventDaemon(
                wx.EVT_DAEMON_TIMETOSLEEP)
            self.ts_EventDaemonThread.setDaemon(True)
            self.ts_EventDaemonThread.setName('EventDaemon')
            self.ts_EventDaemonThread.start()
 
        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        Destructor.

        If the handler is part of a chain, the destructor will unlink
        itself and restore the previous and next handlers so that they
        point to each other.
        '''
        self.logger.debug(
            'Starting tsWxEvtHandler.__del__ for %s.' % str(self))

        self.Unlink()

        if (self.ts_DynamicEventTable is not None):

            for entry in self.ts_DynamicEventTable:

                # Remove ourselves from sink destructor notifications
                # (this has usually been done, in wxTrackable destructor)
                eventSink = entry.GetEvtHandler()
                if (eventSink is not None):

                    evtConnRef = self.FindRefInTrackerList(eventSink)
                    if (evtConnRef):

                        eventSink.RemoveNode(evtConnRef)
                        del evtConnRef

                del entry.ts_CallbackUserData
                del entry

            self.ts_DynamicEventTable = []

        # Remove us from the list of the pending events if necessary.
        if (wxTheApp is not None):
            self.RemovePendingEventHandler()

        self.DeletePendingEvents()

        # we only delete object data, not untyped
##        if (self.ts_ClientDataType == wxClientData_Object):
##            del self.ts_ClientObject

        self.logger.debug(
            'Ending tsWxEvtHandler.__del__ for %s.' % str(self))

    #-----------------------------------------------------------------------

    def AddPendingEvent(self, event):
        '''
        Post an event to be processed later.

        This function is similar to QueueEvent() but cannot be used to post
        events from worker threads for the event objects with wxString
        fields (i.e. in practice most of them) because of an unsafe use of
        the same wxString object which happens because the wxString field
        in the original event object and its copy made internally by this
        function share the same string buffer internally. Use QueueEvent()
        to avoid this.

        A copy of event is made by the function, so the original can be
        deleted as soon as function returns (it is common that the original
        is created on the stack). This requires that the wxEvent::Clone()
        method be implemented by event so that it can be duplicated and
        stored until it gets processed.

        Parameters:

        event   Event to add to the pending events queue.

        Reimplemented in wxWindow.
 
        From event.cpp
        '''
        # Step 1 - Add event to list of pending events
        eventCopy = event.Clone()
        self.ts_PendingEventList.append(eventCopy)

        # Step 2 - Add this event handler to list of event handlers
        #          that have pending events.
        self.ts_PendingEventHandlerList.append(self)

        # Step 3 - Inform the system that new pending events are somewhere.
        #          And, that these should be processed in idle time.
        if wxTheApp is not None:
            # TBD check for app = None
            wxTheApp.WakeUpIdle()

    #-----------------------------------------------------------------------

    def Bind(self,
             event,
             handler=None,
             source=None,
             id=wx.ID_ANY,
             id2=wx.ID_ANY,
             useSystemEventTable=False):
        '''
        Bind an event to an event handler.

        This offers basically the same functionality as Connect(), but
        it is more flexible as it also allows you to use ordinary
        functions and arbitrary functors as event handlers. It is also
        less restrictive then Connect() because you can use an arbitrary
        method as an event handler, where as Connect() requires a
        wxEvtHandler derived handler.

        See Dynamic Event Handling for more detailed explanation of this
        function and the Event Sample sample for usage examples.

        event: One of the EVT_* objects that specifies the
               the type of event to bind.
 
        handler: A callable object to be invoked when the event is
                 delivered to self.  Pass None to disconnect an
                 event handler.
 
        source: Sometimes the event originates from a different window
                than self, but you still want to catch it in self.  (For
                example, a button event delivered to a frame.)  By passing
                the source of the event, the event handling system is able
                to differentiate between the same event type from different
                controls.
 
        id: Used to specify the event source by ID instead of instance.
 
        id2: Used, as lastId, when it is desirable to bind a handler to a
             range of ids, such as with EVT_MENU_RANGE.
        '''
 
        if handler is None:
            return (self.Unbind(event,
                                source,
                                id,
                                id2,
                                useSystemEventTable=useSystemEventTable))

        if source is None:
            source = self
##            if id == wx.ID_ANY:
##                id = self.GetId()
##        else:
##            id = source.NewId()

        try:

            event.Bind(self,
                       id,
                       id2,
                       handler,
                       useSystemEventTable=useSystemEventTable)
 
            self.SetEvtHandlerEnabled(True)

            source.tsUpdateEventAndAcceleratorTables(
                event,
                handler,
                source,
                id,
                id2,
                useSystemEventTable=useSystemEventTable)

        except Exception, sourceError:

            msg = 'Bind in tsWxEvtHandler: Exception=%s' % \
                  str(sourceError)
            print(msg)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Connect(self,
                id,
                lastId,
                eventType,
                func,
                userData=None,
                eventSink=None):
        '''
        Connects the given function dynamically with the event handler,
        id and event type.

        Notice that Bind() provides a more flexible and safer way to do
        the same thing as Connect(), please use it in any new code -- while
        Connect() is not formally deprecated due to its existing widespread
        usage, it has no advantages compared to Bind().

        This is an alternative to the use of static event tables. It is more
        flexible as it allows to connect events generated by some object to
        an event handler defined in a different object of a different class
        (which is impossible to do directly with the event tables -- the
        events can be only handled in another object if they are propagated
        upwards to it). Do make sure to specify the correct eventSink when
        connecting to an event of a different object.

        See Dynamic Event Handling for more detailed explanation of this
        function and the Event Sample sample for usage examples.

        This specific overload allows you to connect an event handler to a
        range of source IDs. Do not confuse source IDs with event types:
        source IDs identify the event generator objects (typically wxMenuItem
        or wxWindow objects) while the event type identify which type of
        events should be handled by the given function (an event generator
        object may generate many different types of events!).
        '''
        # Create the entry
        entry = EventTableEntry(eventType, id, lastId, func, userData)
        # Insert it at the front so most recent additions are found first.
        self.ts_DynamicEventTable.insert(0, entry)

    #-----------------------------------------------------------------------

    def DeletePendingEvents(self):
        '''
        Deletes all events queued on this event handler using QueueEvent()
        or AddPendingEvent().

        Use with care because the events which are deleted are (obviously)
        not processed and this may have unwanted consequences (e.g. user
        actions events will be lost).

        Reimplemented in wxAppConsole.
        '''
        try:

            if (self.ts_PendingEvents is not None):
                self.ts_PendingEvents.DeleteContents(True)
                del self.ts_PendingEvents
                self.ts_PendingEvents = None

        except Exception, deletePendingEventsError:
 
            fmt1 = 'NotImplementedError: %s' % \
                   'DeletePendingEvents in tsWxEvtHandler. '
            fmt2 = 'Exception: %s' % deletePendingEventsError
            msg = fmt1 + fmt2
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            fmt1 = 'NotImplementedError: %s' % \
                   'DeletePendingEvents in tsWxEvtHandler. '
            fmt2 = 'Exception: %s' % deletePendingEventsError
            msg = fmt1 + fmt2
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Disconnect(self,
                   id,
                   lastId,
                   eventType,
                   func=None,
                   userData=None,
                   eventSink=None):
        '''
        Disconnects the given function dynamically from the event handler,
        using the specified parameters as search criteria and returning
        true if a matching function has been found and removed.

        This method can only disconnect functions which have been added
        using the Connect() method. There is no way to disconnect functions
        connected using the (static) event tables.
        '''
        for entry in self.ts_DynamicEventTable:
            # Is this the one?
            if (entry.id == id and
                ((entry.lastId == lastId) or (lastId == wx.ID_ANY)) and
                ((entry.eventType == eventType) or (eventType is None)) and
                ((entry.func == func) or (func is None)) and
                ((entry.userData == userData) or (userData is None))):
                # Remove it
                self.ts_DynamicEventTable.remove(entry)
                return (True)

            else:
                return (False)

    #-----------------------------------------------------------------------

    def DoTryChain(self, event):
        '''
        '''
        try:

            h = self.GetNextHandler()
            while h is not None:

                # We need to process this event at the level of this handler
                # only right now, the pre-/post-processing was either already
                # done by ProcessEvent() from which we were called or will
                # be done by it when we return.
                #
                # However we must call ProcessEvent() and not TryHereOnly()
                # because the existing code (including some in wxWidgets
                # itself) expects the overridden ProcessEvent() in its
                # custom event handlers pushed on a window to be called.
                #
                # So we must call ProcessEvent() but it must not do what it
                # usually does. To resolve this paradox we set up a special
                # flag inside the object itself to let ProcessEvent() know
                # that it shouldn't do any pre/post-processing for this
                # event if it gets it. Note that this only applies to this
                # handler, if the event is passed to another one by
                # explicitly calling its ProcessEvent(), pre/post-processing
                # should be done as usual.
                #
                # Final complication is that if the implementation of
                # ProcessEvent() called wxEvent::DidntHonourProcessOnlyIn()
                # (as the gross hack that is
                # wxScrollHelperEvtHandler::ProcessEvent() does) and
                # ignored our request to process event in this handler only,
                # we have to compensate for it by not processing the event
                # further because this was already done by that rogue event
                # handler.
                wxEventProcessInHandlerOnly.ProcessInHandlerOnly(event, h)
                if ( h.ProcessEvent(event) ):

                    # Make sure "skipped" flag is not set as the event was
                    # really processed in this case. Normally it shouldn't
                    # be set anyhow but make sure just in case the user
                    # code does something strange.
                    event.Skip(False)

                    return (True)


                if ( not event.ShouldProcessOnlyIn(h) ):

                    # Still return true to indicate that no further
                    # processing should be undertaken but ensure that
                    # "skipped" flag is set so that the caller knows that
                    # the event was not really processed.
                    event.Skip()

                    return (True)

            return (False)

        except Exception, errorCode:

            msg = 'NotImplementedError: %s' % \
                  'DoTryChain in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def FilterEvent(self):
        '''
        '''
        try:

            if wxTheApp is None:

                # process the events normally by default
                return (-1)

            else:

                wxTheApp.FilterEvent()

        except Exception, errorCode:

            msg = 'NotImplementedError: ' + \
                  'FilterEvent in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def FindRefInTrackerList(self, eventSink):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'FindRefInTrackerList in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetClientData(self):
        '''
        Returns user-supplied client data.

        Remarks:

        Normally, any extra data the programmer wishes to associate with the
        object should be made available by deriving a new class with new data
        members.

        See also:

        SetClientData()
        '''
        try:
            # It is not an error to call GetClientData() on a
            # window which does not have client data at all.
            # None will be returned

            if (self.ts_ClientDataType is not None): # != wxClientData_Object):

                msg = 'This window does not have client data'
                self.logger.error(msg)
                return (None)

            return (self.ts_ClientData)

        except Exception, getClientDataError:

            msg = 'NotImplementedError: ' + \
                  'GetClientData in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetClientObject(self):
        '''
        Returns a pointer to the user-supplied client data object.

        See also:

        SetClientObject(), wxClientData
        '''
        msg = 'NotImplementedError: %s' % \
              'GetClientObject in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetEventHashTable(self):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'GetEventHashTable in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetEvtHandlerEnabled(self):
        '''
        Returns true if the event handler is enabled, false otherwise.

        See also:

        SetEvtHandlerEnabled()
        '''
        return (self.ts_EvtHandlerEnabled)

    #-----------------------------------------------------------------------

    def GetId(self):
        '''
        Returns the identifier of the window.
        '''
        if True:
            return (self.ts_AssignedId)
        else:
            return (self.ts_Id)

    #-----------------------------------------------------------------------

    def GetNextHandler(self):
        '''
        Returns the pointer to the next handler in the chain.

        See also:

        SetNextHandler(), GetPreviousHandler(), SetPreviousHandler(),
        wxWindow::PushEventHandler, wxWindow::PopEventHandler
        '''
        if self.ts_CurrentlyActiveHandler is None:
            nextHandler = self.ts_CurrentlyActiveHandler
        else:
            nextHandler = self.ts_CurrentlyActiveHandler.ts_NextHandler

        self.ts_CurrentlyActiveHandler = nextHandler
        return (self.ts_CurrentlyActiveHandler)

    #-----------------------------------------------------------------------

    def GetPreviousHandler(self):
        '''
        Returns the pointer to the previous handler in the chain.

        See also:

        SetPreviousHandler(), GetNextHandler(), SetNextHandler(),
        wxWindow::PushEventHandler, wxWindow::PopEventHandler
        '''
        if self.ts_CurrentlyActiveHandler is None:
            previousHandler = self.ts_CurrentlyActiveHandler
        else:
            previousHandler = self.ts_CurrentlyActiveHandler.ts_PreviousHandler

        self.ts_CurrentlyActiveHandler = previousHandler
        return (self.ts_CurrentlyActiveHandler)

    #-----------------------------------------------------------------------

    def IsUnlinked(self):
        '''
        Returns true if the next and the previous handler pointers of this
        event handler instance are None.

        Since:

        2.9.0

        See also:

        SetPreviousHandler(), SetNextHandler()
        '''
        try:

            if self.ts_CurrentlyActiveHandler is None:
                return(True)
            else:
                currentHandler = self.ts_CurrentlyActiveHandler
                nextHandler = currentHandler.ts_NextHandler
                previousHandler = currentHandler.ts_PreviousHandler

                return ((previousHandler is None) and \
                        (nextHandler is None))

        except Exception, isUnlinkedError:

            msg = 'NotImplementedError: ' + \
                  'IsUnlinked in tsWxEvtHandler. ' + \
                  'Exception: %s' % isUnlinkedError
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessEvent(self, event):
        '''
        Processes an event, searching event tables and calling zero or more
        suitable event handler function(s).

        Normally, your application would not call this function: it is
        called in the wxWidgets implementation to dispatch incoming user
        interface events to the framework (and application).

        However, you might need to call it if implementing new functionality
        (such as a new control) where you define new event types, as opposed
        to allowing the user to override virtual functions.

        Notice that you do not usually need to override ProcessEvent() to
        customize the event handling, overriding the specially provided
        TryBefore() and TryAfter() functions is usually enough. For example,
        wxMDIParentFrame may override TryBefore() to ensure that the menu
        events are processed in the active child frame before being processed
        in the parent frame itself.

        The normal order of event table searching is as follows:

        1) wxApp::FilterEvent() is called. If it returns anything but -1
        (default) the processing stops here.

        2) TryBefore() is called (this is where wxValidator are taken into
        account for wxWindow objects). If this returns true, the function
        exits.

        3) If the object is disabled (via a call to
        wxEvtHandler::SetEvtHandlerEnabled) the function skips to step (7).

        4) Dynamic event table of the handlers bound using Bind<>() is
        searched. If a handler is found, it is executed and the function
        returns true unless the handler used wxEvent::Skip() to indicate
        that it did not handle the event in which case the search continues.

        5) Static events table of the handlers bound using event table
        macros is searched for this event handler. If this fails, the base
        class event table table is tried, and so on until no more tables
        exist or an appropriate function was found. If a handler is found,
        the same logic as in the previous step applies.

        6) The search is applied down the entire chain of event handlers
        (usually the chain has a length of one). This chain can be formed
        using wxEvtHandler::SetNextHandler():

        (referring to the image, if A->ProcessEvent is called and it does
        not handle the event, B->ProcessEvent will be called and so on...).
        Note that in the case of wxWindow you can build a stack of event
        handlers (see wxWindow::PushEventHandler() for more info). If any
        of the handlers of the chain return true, the function exits.
        '''
        return (self.tsProcessPyEventBinderEvent(event))

    #-----------------------------------------------------------------------

    def InactivatedProcessEvent(self, event):
        '''
        From: http://docs.wxwidgets.org/trunk/
              classwx_evt_handler.html#65968dd27f3aac7718f2dd6b2ddd5a08

        Processes an event, searching event tables and calling zero or more
        suitable event handler function(s).

        Normally, your application would not call this function: it is
        called in the wxWidgets implementation to dispatch incoming user
        interface events to the framework (and application).

        However, you might need to call it if implementing new functionality
        (such as a new control) where you define new event types, as opposed
        to allowing the user to override virtual functions.

        Notice that you do not usually need to override ProcessEvent() to
        customize the event handling, overriding the specially provided
        TryBefore() and TryAfter() functions is usually enough. For example,
        wxMDIParentFrame may override TryBefore() to ensure that the menu
        events are processed in the active child frame before being processed
        in the parent frame itself.

        The normal order of event table searching is as follows:

        1) wxApp::FilterEvent() is called. If it returns anything but -1
        (default) the processing stops here.

        2) TryBefore() is called (this is where wxValidator are taken into
        account for wxWindow objects). If this returns true, the function
        exits.

        3) If the object is disabled (via a call to
        wxEvtHandler::SetEvtHandlerEnabled) the function skips to step (7).

        4) Dynamic event table of the handlers bound using Bind<>() is
        searched. If a handler is found, it is executed and the function
        returns true unless the handler used wxEvent::Skip() to indicate
        that it did not handle the event in which case the search continues.

        5) Static events table of the handlers bound using event table
        macros is searched for this event handler. If this fails, the base
        class event table table is tried, and so on until no more tables
        exist or an appropriate function was found. If a handler is found,
        the same logic as in the previous step applies.

        6) The search is applied down the entire chain of event handlers
        (usually the chain has a length of one). This chain can be formed
        using wxEvtHandler::SetNextHandler():

        (referring to the image, if A->ProcessEvent is called and it does
        not handle the event, B->ProcessEvent will be called and so on...).
        Note that in the case of wxWindow you can build a stack of event
        handlers (see wxWindow::PushEventHandler() for more info). If any
        of the handlers of the chain return true, the function exits.
        '''
        # The very first thing we do is to allow the application to hook into
        # event processing in order to globally pre-process all events.
        #
        # Note that we should only do it if we're the first event handler
        # called to avoid calling FilterEvent() multiple times as the event
        # goes through the event handler chain and possibly upwards in the
        # window hierarchy.
        try:

            if (not event.WasProcessed()):

                # Allow the application to hook into event processing
                if wxTheApp is None:

                    # Simulate the application filtering event processing
                    rc = self.FilterEvent(event)
                    if rc != -1:

                        fmt1 = 'Unexpected wxApp.FilterEvent return value'
                        fmt2 = '%s' % str(rc == 1 | rc == 0)
                        msg = fmt1 + fmt2
                        self.logger.error(msg)

                        return (rc != 0)

                else:

                    # Allow the application to filter event processing
                    rc = wxTheApp.FilterEvent(event)
                    if rc != -1:

                        fmt1 = 'Unexpected wxApp.FilterEvent return value'
                        fmt2 = '%s' % str(rc == 1 | rc == 0)
                        msg = fmt1 + fmt2
                        self.logger.error(msg)

                        return (rc != 0)

                    # else: proceed normally

        except Exception, errorCode:

            fmt1 = 'ProcessEvent at event.WasProcessed '
            fmt2 = 'for Event=%s ' % str(event)
            fmt3 = 'Exception=%s' % str(errorCode)
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

        # Short circuit the event processing logic if we're requested
        # to process this event in this handler only, see DoTryChain()
        # for more details.
        try:

            # TBD - Enable until requirements have been resolved.
            if True or (event.ShouldProcessOnlyIn()):

                return (self.TryBeforeAndHere(event))

        except Exception, errorCode:

            fmt1 = 'ProcessEvent at event.ShouldProcessOnlyIn '
            fmt2 = 'for Event=%s ' % str(event)
            fmt3 = 'Exception=%s' % str(errorCode)
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

        # Try to process the event in this handler itself.
        try:

            # TBD - Disable until requirements have been resolved.
            if False and (self.ProcessEventLocally(event)):

                # It is possible that DoTryChain() called from
                # ProcessEventLocally() returned true but the event was not
                # really processed: this happens if a custom handler ignores
                # the request to process the event in this handler only and
                # in this case we should skip the post processing done in
                # TryAfter() but still return the correct value ourselves to
                # indicate whether we did or did not find a handler for this
                # event.
                if (isinstance(event.GetEventType(), PyEventBinder)):

                    # Process an ncurses emulated wxWidgets/wxPython Event
                    return (self.tsProcessPyEventBinderEvent(event))

                return (not event.GetSkipped())

        except Exception, errorCode:

            fmt1 = 'ProcessEvent at self.ProcessEventLocally '
            fmt2 = 'for Event=%s ' % str(event)
            fmt3 = 'Exception=%s' % str(errorCode)
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

        # If we still didn't find a handler, propagate the event upwards the
        # window chain and/or to the application object.
        try:

            # TBD - Disable until requirements have been resolved.
            if False and (self.TryAfter(event)):

                return (True)

        except Exception, errorCode:

            fmt1 = 'ProcessEvent at self.TryAfter '
            fmt2 = 'for Event=%s ' % str(event)
            fmt3 = 'Exception=%s' % str(errorCode)
            msg = fmt1 + fmt2 + fmt3
            self.logger.error(msg)

        # No handler found anywhere, bail out.
        fmt1 = 'ProcessEvent at No Handler Found '
        fmt2 = 'for Event=%s ' % str(event)
        fmt3 = 'Exception=%s' % str(errorCode)
        msg = fmt1 + fmt2 + fmt3
        self.logger.error(msg)

        return (False)

    #-----------------------------------------------------------------------

    def ProcessEventIfMatchesId(self, entry, event):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'ProcessEventIfMatchesId in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessEventLocally(self, event):
        '''
        Try to process the event in this handler and all those chained to it.

        As explained in ProcessEvent() documentation, the event handlers
        may be chained in a doubly-linked list. This function tries to
        process the event in this handler (including performing any
        pre-processing done in TryBefore(), e.g. applying validators)
        and all those following it in the chain until the event is processed
        or the chain is exhausted.

        This function is called from ProcessEvent() and, in turn, calls
        TryThis() for each handler in turn. It is not virtual and so cannot
        be overridden but can, and should, be called to forward an event to
        another handler instead of ProcessEvent() which would result in a
        duplicate call to TryAfter(), e.g. resulting in all unprocessed
        events being sent to the application object multiple times.

        Since:

        2.9.1

        Parameters:

        event   Event to process.

        Returns:

        true if this handler of one of those chained to it processed the
        event.
        '''
        try:

            # Try the hooks which should be called before our own handlers
            # and this handler itself first. Notice that we should not call
            # ProcessEvent() on this one as we're already called from it,
            # which explains why we do it here and not in DoTryChain()
            return (self.TryBeforeAndHere(event) or self.DoTryChain(event))

        except Exception, ProcessEventLocallyError:

            msg = 'NotImplementedError: ' + \
                  'ProcessEventLocally in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessPendingEvents(self):
        '''
        Processes the pending events previously queued using QueueEvent()
        or AddPendingEvent(); you must call this function only if you are
        sure there are pending events for this handler, otherwise a wxCHECK
        will fail.

        The real processing still happens in ProcessEvent() which is called
        by this function.

        Note that this function needs a valid application object (see
        wxAppConsole::GetInstance()) because wxApp holds the list of the
        event handlers with pending events and this function manipulates
        that list.

        Reimplemented in wxAppConsole, and wxWindow.
        '''
        # Process the number of events present when we enter.
        # This prevents an infinite loop since another event could
        # be posted by the event handler execution.
        count = len(self.ts_PendingEvents)
        for event in self.ts_PendingEvents[:count]:
            # Remove the event before processing it.
            # A nested event loop (e.g. modal dialog) might
            # process the same event again.
            self.ts_PendingEvents.remove(event)
            # Process the event.
            self.ProcessEvent(event)

    #-----------------------------------------------------------------------

    def QueueEvent(self, event):
        '''
        Queue event for a later processing.

        This method is similar to ProcessEvent() but while the latter is
        synchronous, i.e. the event is processed immediately, before the
        function returns, this one is asynchronous and returns immediately
        while the event will be processed at some later time (usually
        during the next event loop iteration).

        Another important difference is that this method takes ownership
        of the event parameter, i.e. it will delete it itself. This implies
        that the event should be allocated on the heap and that the pointer
        cannot be used any more after the function returns (as it can be
        deleted at any moment).

        QueueEvent() can be used for inter-thread communication from the
        worker threads to the main thread, it is safe in the sense that
        it uses locking internally and avoids the problem mentioned in
        AddPendingEvent() documentation by ensuring that the event object
        is not used by the calling thread any more. Care should still be
        taken to avoid that some fields of this object are used by it,
        notably any wxString members of the event object must not be
        shallow copies of another wxString object as this would result
        in them still using the same string buffer behind the scenes.
        For example:

        #     void FunctionInAWorkerThread(const wxString& str)
        #     {
        #         wxCommandEvent* evt = new wxCommandEvent;

        #         // NOT evt->SetString(str) as this would be a shallow copy
        #         evt->SetString(str.c_str()); // make a deep copy

        #         wxTheApp->QueueEvent( evt );
        #     }

        # Note that you can use wxThreadEvent instead of wxCommandEvent to
        # avoid this problem:

        #     void FunctionInAWorkerThread(const wxString& str)
        #     {
        #         wxThreadEvent evt;
        #         evt->SetString(str);

        #         // wxThreadEvent::Clone() makes sure that the internal
        #         // wxString member is not shared by other wxString
        #         // instances:
        #         wxTheApp->QueueEvent( evt.Clone() );
        #     }

##        Finally notice that this method automatically wakes up the event
##        loop if it is currently idle by calling wxWakeUpIdle() so there
##        is no need to do it manually when using it.

##        Since:
##        2.9.0

##        Parameters:

##        event         A heap-allocated event to be queued, QueueEvent() takes
##        ownership of it. This parameter should not be NULL.

##        Reimplemented in wxWindow.
        '''
        msg = 'NotImplementedError: %s' % \
              'QueueEvent in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ReceivePendingEventHandler(self):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'ReceivePendingEventHandler in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RemovePendingEventHandler(self):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'RemovePendingEventHandler in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SafelyProcessEvent(self, event):
        '''
        Rrocesses an event by calling ProcessEvent() and handles any
        exceptions that occur in the process.

        If an exception is thrown in event handler,
        wxApp::OnExceptionInMainLoop is called.

        Parameters:

        event   Event to process.

        Returns:

        true if the event was processed, false if no handler was found
        or an exception was thrown.

        See also:

        wxWindow::HandleWindowEvent

        Reimplemented in wxWindow.
        '''
        try:

            try:
                return (self.ProcessEvent(event))

            except Exception, errorCode:

                # notice that we do it in 2 steps to avoid warnings about
                # possibly uninitialized loop variable from some versions
                # of g++ which are not smart enough to figure out that
                # GetActive() doesn't throw and so that loop will always
                # be initialized
                wxEventLoop.ts_loop = None
                try:

                    wxEventLoop.ts_loop = wxEventLoop.GetActive()

                    if (wxTheApp is not None or \
                        wxTheApp.OnExceptionInMainLoop()):

                        if (wxEventLoop.ts_loop is not None):
                            wxEventLoop.ts_loop.Exit()

                    # else: continue running current event loop

                    return (False)

                except Exception, loopErrorCode:

                    # OnExceptionInMainLoop() threw, possibly rethrowing the same
                    # exception again: very good, but we still need Exit() to
                    # be called
                    if (wxEventLoop.ts_loop is not None):
                        wxEventLoop.ts_loop.Exit()
                    raise Exception

        except Exception, errorCode:

            msg = 'NotImplementedError: ' + \
                  'SafelyProcessEvent in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SearchDynamicEventTable(self, event):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def SearchEventTable(self, table, event):
        '''
        Searches the event table, executing an event handler function if
        an appropriate one is found.

        Parameters:

        table   Event table to be searched.

        event   Event to be matched against an event table entry.

        Returns:

        true if a suitable event handler function was found and executed,
        and the function did not call wxEvent::Skip.

        Remarks:

        This function looks through the object event table and tries to
        find an entry that will match the event. An entry will match if:

        The event type matches, and

        the identifier or identifier range matches, or the event table entry
        identifier is zero.

        If a suitable function is called but calls wxEvent::Skip, this
        function will fail, and searching will continue.

        Todo:

        this function in the header is listed as an "implementation only"
        function; are we sure we want to document it?

        See also:

        ProcessEvent()
        '''
        try:

            eventType = event.GetEventType()
            i = 0
            while table.entries[i].ts_fn != 0:

                entry = table.entries[i]
                if (eventType == entry.ts_EventType):

                    if (self.ProcessEventIfMatchesId(entry, event)):
                        return (True)

                i += 1

            return (False)

        except Exception, errorCode:

            msg = 'NotImplementedError: %s' % \
                  'SearchEventTable in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetClientData(self, data):
        '''
        Sets user-supplied client data.

        Parameters:

        data    Data to be associated with the event handler.

        Remarks:

        Normally, any extra data the programmer wishes to associate with the
        object should be made available by deriving a new class with new data
        members. You must not call this method and SetClientObject on the
        same class - only one of them.

        See also:

        GetClientData()
        '''
        msg = 'NotImplementedError: %s' % \
              'SetClientData in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetClientObject(self, data):
        '''
        Set the client data object.

        Any previous object will be deleted.

        See also:

        GetClientObject(), wxClientData
        '''
        msg = 'NotImplementedError: %s' % \
              'SetClientObject in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetEvtHandlerEnabled(self, enabled):
        '''
        Enables or disables the event handler.

        Parameters:

        enabled         true if the event handler is to be enabled, false
        if it is to be disabled.

        Remarks:

        You can use this function to avoid having to remove the event
        handler from the chain, for example when implementing a dialog
        editor and changing from edit to test mode.

        See also:

        GetEvtHandlerEnabled()
        '''
        self.ts_EvtHandlerEnabled = enabled

    #-----------------------------------------------------------------------

    def SetNextHandler(self, handler):
        '''
        Sets the pointer to the next handler.

        Remarks:

        See ProcessEvent() for more info about how the chains of event
        handlers are internally used. Also remember that wxEvtHandler
        uses double-linked lists and thus if you use this function, you
        should also call SetPreviousHandler() on the argument passed to
        this function:

            handlerA->SetNextHandler(handlerB);
            handlerB->SetPreviousHandler(handlerA);

        Parameters:

        handler         The event handler to be set as the next handler.
                        Cannot be NULL.
        See also:

        How Events are Processed

        Reimplemented in wxWindow.
        '''
        self.ts_NextHandler = handler

    #-----------------------------------------------------------------------

    def SetPreviousHandler(self, handler):
        '''
        Sets the pointer to the previous handler.

        All remarks about SetNextHandler() apply to this function as well.

        Parameters:

        handler  The event handler to be set as the previous handler.
                 Cannot be NULL.

        See also:

        How Events are Processed

        Reimplemented in wxWindow.
        '''
        self.ts_PreviousHandler = handler

    #-----------------------------------------------------------------------

    def TryAfter(self, event):
        '''
        Method called by ProcessEvent() as last resort.

        This method can be overridden to implement post-processing for
        the events which were not processed anywhere else.

        The base class version handles forwarding the unprocessed events
        to wxApp at wxEvtHandler level and propagating them upwards the
        window child-parent chain at wxWindow level and so should usually
        be called when overriding this method:

        class MyClass : public BaseClass // inheriting from wxEvtHandler
        {
        ...
        protected:
            virtual bool TryAfter(wxEvent& event)
            {
                if ( BaseClass::TryAfter(event) )
                    return true;

                return MyPostProcess(event);
            }
        };

        See also:

        ProcessEvent()
        '''
        msg = 'NotImplementedError: %s' % \
              'TryAfter in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def TryBefore(self, event):
        '''
        Method called by ProcessEvent() before examining this object
        event tables.

        This method can be overridden to hook into the event processing
        logic as early as possible. You should usually call the base
        class version when overriding this method, even if wxEvtHandler
        itself does nothing here, some derived classes do use this
        method, e.g. wxWindow implements support for wxValidator in it.

        Example:

        class MyClass : public BaseClass // inheriting from wxEvtHandler
        {
        ...
        protected:
            virtual bool TryBefore(wxEvent& event)
            {
                if ( MyPreProcess(event) )
                    return true;

                return BaseClass::TryBefore(event);
            }
        };

        See also:

        ProcessEvent()
        '''
        msg = 'NotImplementedError: %s' % \
              'TryBefore in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def TryBeforeAndHere(self, event):
        '''
        '''
        msg = 'NotImplementedError: ' + \
              'TryBeforeAndHere in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def TryHereOnly(self, event):
        '''
        '''
        try:

            # If the event handler is disabled it doesn't process any events
            if (not self.GetEvtHandlerEnabled() ):
                return (False)

            # Handle per-instance dynamic event tables first
            if (self.ts_DynamicEventTable != []) and \
               (self.SearchDynamicEventTable(event)):
                return (True)

            # Then static per-class event tables
            if (self.GetEventHashTable().HandleEvent(event)):
                return (True)

            # We don't have a handler for this event.
            return (False)

        except Exception, errorCode:

            msg = 'NotImplementedError: ' + \
                  'TryHereOnly in tsWxEvtHandler.'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def TryParent(self, event):
        '''
        TBD
        '''
        if self.ts_TriggeringObject is None:

            status = False

        else:

            status = False

##            try:

##                self.ts_TriggeringObject.Parent.GetNextHandler().ProcessEvent(
##                    event)
##                status = True

##            except Exception, tryError:

##                msg = 'TryParent: TriggeringObject=%s; Exception "%s"' % (
##                    self.ts_TriggeringObject,
##                    tryError)
##                self.logger.error(msg)
##                status = False

        return (status)

    #-----------------------------------------------------------------------

    def TryThis(self, event):
        '''
        Try to process the event in this event handler.

        This method is called from ProcessEventLocally() and thus,
        indirectly, from ProcessEvent(), please see the detailed
        description of the event processing logic there.

        It is currently not virtual and so may not be overridden.

        Since:

        2.9.1

        Parameters:

        event   Event to process.

        Returns:

        true if this object itself defines a handler for this event and
        the handler did not skip the event.
        '''
        msg = 'NotImplementedError: ' + \
              'TryThis in tsWxEvtHandler.'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def TryValidator(self, event):
        '''
        TBD
        '''
        theSourceKey = self.ts_AssignedId
        theEventKey = event.ts_EventType

        if self.ts_TriggeringObject is None:

            status = False

        else:

            status = False

##            try:

##                if event.ts_EventType == self.ts_SystemEventTable[
##                    self.ts_AssignedId]['event']['evtType']:

##                    myHandler = self.ts_SystemEventTable[
##                        self.ts_AssignedId]['handler']

##                self.ts_TriggeringObject.Parent.GetNextHandler().ProcessEvent(
##                    event)

##                status = True

##            except Exception, tryError:

##                msg = 'TryValidator: TriggeringObject=%s; Exception "%s"' % (
##                    self.ts_TriggeringObject,
##                    tryError)
##                self.logger.error(msg)
##                status = False

        return (status)

    #-----------------------------------------------------------------------

    def Unbind(self,
               event,
               source=None,
               id=wx.ID_ANY,
               id2=wx.ID_ANY,
               useSystemEventTable=False):
        '''
        Disconencts the given function from the event handler, using the
        specified parameters as search criteria and returning true if
        a matching function has been found and removed.
        '''
        if source is not None:
            id = source.GetId()

        return event.Unbind(self, id, id2)

    #-----------------------------------------------------------------------

    def Unlink(self):
        '''
        Unlinks this event handler from the chain it is part of (if any);
        then links the "previous" event handler to the "next" one (so that
        the chain will not be interrupted).
        '''
        try:
            # this event handler must take itself out of the chain of handlers:

            if (self.ts_PreviousHandler is not None):

                self.ts_PreviousHandler.SetNextHandler(self.ts_NextHandler)

            if (self.ts_NextHandler is not None):

                self.ts_NextHandler.SetPreviousHandler(self.ts_PreviousHandler)

            self.ts_NextHandler = None
            self.ts_PreviousHandler = None

        except Exception, unlinkError:

            msg = 'NotImplementedError: ' + \
                  'Unlink in tsWxEvtHandler. ' + \
                  'Exception: %s' % unlinkError
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsProcessEventTables(self,
                             objectCriteria=None,
                             objectId=None,
                             triggeringEvent=None,
                             triggeringObject=None):
        '''
        Dispatch the triggering event to one or more event handlers
        identified in the system or user event table of the triggering
        object and its ancestors.

        Return True if an event handler found. False if no event handler
        found.
        '''
        results = False

        precedenceSequence = [True, False]
        triggeringEventType = triggeringEvent.ts_EventType[0]

        if DEBUG:
            print('tsWxEvtHandler.tsProcessEventTables: ' +\
                  'for objectCriteria=%s; triggeringEventType=%s' % (
                      objectCriteria,
                      triggeringEventType))

        targetObject = triggeringObject
        targetObjectList = {}
        results = False

        while ((not results) and (not (targetObject is None))):

            targetObjectLabel = targetObject.GetLabel()
            targetObjectList[
                targetObjectLabel] = targetObject.ts_AssignedId
            for precedence in precedenceSequence:

                if self.tsProcessSelectedEventTable(
                    objectCriteria=objectCriteria,
                    objectId=objectId,
                    triggeringEvent=triggeringEvent,
                    triggeringObject=targetObject,
                    useSystemEventTable=precedence):

                    results = True

            targetObject = targetObject.Parent

        if DEBUG:
            msg = 'tsWxEvtHandler.tsProcessEventTables: ' + \
                  'results=%s; targetObjectList=%s' % (
                      results, targetObjectList)
            print(msg)

    #-----------------------------------------------------------------------

    def tsProcessPyEventBinderEvent(self, event):
        '''
        Processes an event, searching event tables and call zero or more
        suitable event handler function(s).

        This method is used by "ProcessEvent" to handle events created
        via "PyEventBinder". Such events do not have access to the methods
        and instance variables associated with the "Event" class.

        Parameter:

        event - PyEventBinder type object (NOT an Event class instance)
        '''
        triggeringEvent = event
        triggeringObject = event.GetEventSource()

        # Construct an EventQueueEntry.
        self.ts_EventQueueEntry = EventQueueEntry(triggeringObject,
                                                  triggeringEvent)

        self.logger.debug(
            'tsWxEvtHandler.tsProcessPyEventBinderEvent: ' + \
            'objectId=%s; eventType=%s' % (
                str(triggeringObject.ts_AssignedId),
                str(triggeringEvent.GetEventType())))

        try:

            eventType = triggeringEvent.GetEventType()

        except Exception, eventError:

            eventType = None
            msg = 'tsWxEvtHandler.tsProcessPyEventBinderEvent: ' + \
                  'triggeringEvent.GetEventType: ' + \
                  'eventError="%s"' % str(
                      eventError)
            self.logger.error(msg)

        try:

            objectAssignedId = triggeringObject.ts_AssignedId
            objectName = triggeringObject.ts_Name

##            junk = self.tsProcessEventTable(
##                objectCriteria=wx.EmptyString,
##                objectId=objectAssignedId,
##                triggeringEvent=triggeringEvent,
##                triggeringObject=triggeringObject,
##                useSystemEventTable=True)

            print('NOTICE: Junk=%s\n' % junk)

        except Exception, objectError:

            objectAssignedId = wx.ID_ANY
            objectName =None

            msg = 'tsWxEvtHandler.tsProcessPyEventBinderEvent: ' + \
                  'objectError="%s"' % str(
                      objectError)
            self.logger.error(msg)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsProcessSelectedEventTable(self,
                                    objectCriteria=None,
                                    objectId=None,
                                    triggeringEvent=None,
                                    triggeringObject=None,
                                    useSystemEventTable=True):
        '''
        Return True after dispatching the triggering event to an event
        handler identified in the system or user event table of the.
        triggering object. Return False if no event handler found.
        '''
        self.logger.wxASSERT_MSG(
            (not (triggeringObject is None)),
            msg='tsWxEvtHandler.tsProcessSelectedEventTable: ' + \
            'triggeringObject is None.')

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxEvtHandler.tsProcessSelectedEventTable: ' + \
            'objectId is None.')

        self.logger.wxASSERT_MSG(
            (not (triggeringEvent is None)),
            msg='tsWxEvtHandlerp.tsProcessSelectedEventTable: ' + \
            'triggeringEvent is None.')

        results = False

        if True or DEBUG:
            fmt1 = 'tsWxEvtHandler.tsProcessSelectedEventTable: '
            fmt2 = 'objectCriteria=%s; ' % objectCriteria
            fmt3 = 'objectId=%s; ' % objectId
            fmt4 = 'triggeringEvent=%s; ' % str(triggeringEvent)
            fmt5 = '' # 'triggeringMouseTuple=%s; ' % str(triggeringMouseTuple)
            fmt6 = 'triggeringObject=%s; ' % str(triggeringObject)
            fmt7 = 'useSystemEventTable=%s' % str(useSystemEventTable)
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6 + fmt7
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

        self.logger.wxASSERT_MSG(
            (not (triggeringEvent is None)),
             msg='Invalid triggeringEvent=%s' % triggeringEvent)

        self.logger.wxASSERT_MSG(
            (not (triggeringObject is None)),
             msg='Invalid triggeringObject=%s' % triggeringObject)

        self.logger.wxASSERT_MSG(
            (not (objectCriteria is None)),
             msg='Invalid objectCriteria=%s' % objectCriteria)

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
             msg='Invalid objectId=%s' % objectId)

        # Process the non-focus event explicity associated with
        # triggering object.
        try:

            # The triggeringEvent is an iterable evtType (i.e., a list).
            triggeringEventType = triggeringEvent.ts_EventType[0]

        except Exception, eventError:

            msg = 'tsWxEvtHandler.tsProcessSelectedEventTable: ' + \
                  'eventError="%s"' % str(eventError)
            self.logger.error(msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        try:

            objectAssignedId = triggeringObject.ts_AssignedId
            objectName = triggeringObject.ts_Name

            if useSystemEventTable:

                selectedEventTable = triggeringObject.ts_SystemEventTable

            else:

                selectedEventTable = triggeringObject.ts_UserEventTable

            for theEventTableEntryKey in selectedEventTable.keys():

                if theEventTableEntryKey == 'name':

                    pass

                else:

                    theEventTableEntry = selectedEventTable[
                        theEventTableEntryKey]

                    selectedEvent = theEventTableEntry['event']
                    # The selectedEvent is an iterable evtType (i.e., a list).
                    selectedEventType = selectedEvent.ts_EventType[0]

                    if selectedEventType == triggeringEventType:

                        if DEBUG:
                            fmt1 = 'tsWxEvtHandler.'
                            fmt2 = 'tsProcessSelectedEventTable: '
                            fmt3 = 'triggeringEventType=' + \
                                   '%s; ' % triggeringEventType
                            fmt4 = 'selectedEventType=' + \
                                   '%s\n' % selectedEventType
                            msg = fmt1 + fmt2 + fmt3 + fmt4
                            print('DEBUG: %s\n' % msg)

                        selectedEventHandler = theEventTableEntry['handler']

                        selectedEventHandler(triggeringEvent)

                    else:

                        if DEBUG:
                            fmt1 = 'tsWxEvtHandler.'
                            fmt2 = 'tsProcessSelectedEventTable: '
                            fmt3 = 'triggeringEvent=%s; ' % triggeringEvent
                            fmt4 = 'selectedEvent=%s\n' % selectedEvent
                            msg = fmt1 + fmt2 + fmt3 + fmt4
                            print('DEBUG: %s\n' % msg)

        except Exception, objectError:

            msg = 'tsWxEvtHandler.tsProcessSelectedEventTable: ' + \
                  'objectError="%s"' % str(objectError)
            self.logger.error(msg)
            if DEBUG:
                print('ERROR: %s\n' % msg)
##          raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (results)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    EvtHandlerEnabled = property(GetEvtHandlerEnabled, SetEvtHandlerEnabled)
    NextHandler = property(GetNextHandler, SetNextHandler)
    PreviousHandler = property(GetPreviousHandler, SetPreviousHandler)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
