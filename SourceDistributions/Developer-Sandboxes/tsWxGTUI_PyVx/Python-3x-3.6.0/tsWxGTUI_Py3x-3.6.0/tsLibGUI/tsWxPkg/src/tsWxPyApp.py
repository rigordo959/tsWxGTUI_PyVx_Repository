#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:42:07 AM rsg>"
'''
tsWxPyApp.py - Class to emulate the wxPython API for
non-graphical, curses-based platforms.
'''
#################################################################
#
# File: tsWxPyApp.py
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
#    from tsWxPyApp import PyApp
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
#    2012/05/29 rsg Fix typographical errors.
#
#    2012/05/30 rsg Moved wxWidgets-specific event handling code
#                   from tsWxEventLoop directly into tsWxPyApp to
#                   avoid tsWxEvtHandler import conflict error.
#
#    2012/08/01 rsg Added logic to __init__ to set Screen (with its
#                   stdcr handle) as default recipient of Text Entry
#                   Input from Keyboard.
#
# ToDo:
#
#    2010/03/13 rsg Investigate tsGetGraphicalUserInput trap which
#                   occurs when wheel mouse rotates.
#
#    2010/03/14 rsg Investigate how tsGetGraphicalUserInput could
#                   detect which button, radiobutton, checkbox
#                   or menubar items are hidden and should not be
#                   selected.
#
#    2010/03/14 rsg Investigate how tsGetGraphicalUserInput could
#                   detect which menubar item has been selected.
#
#    2011/04/01 rsg Used wxPoint, wxSize and wxRect instead of
#                   tuples for StdScreenGeometry.
#
#################################################################

__title__     = 'tsWxPyApp'
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

import time
# import Queue

import tsExceptions as tse
import tsWxGlobals as wx
import tsWxGraphicalTextUserInterface as tsGTUI

from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
from tsWxEvent import Event
from tsWxEventLoop import EventLoop
from tsWxEvtHandler import EvtHandler
from tsWxTaskBar import TaskBar as wxTaskBar
from tsWxRect import Rect as wxRect
from tsWxScreen import Screen as wxScreen


tsWxGTUI_DataBase = tsGTUI.GraphicalTextUserInterface

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DEBUG_MOUSE = True

# Derived from default window names in tsWxGlobals.
# However, case reflects usage in class definitation files.
firstCallerClassNames = list(wx.indentation.keys())

#---------------------------------------------------------------------------

class PyApp(EvtHandler):
    '''
    The wx.PyApp class represents the application and is used to:

        * bootstrap the wxPython system and initialize the underlying gui
          toolkit
        * set and get application-wide properties
        * implement the windowing system main message or event loop, and to
          dispatch events to window instances
        * etc.

    Every application must have a wx.App instance, and all creation of UI
    objects should be delayed until after the wx.App object has been created
    in order to ensure that the gui platform and wxWidgets have been fully
    initialized.

    Normally you would derive from this class and implement an OnInit method
    that creates a frame and then calls self.SetTopWindow(frame).
    '''
    # Class variables

    _KeepGoing = False
    _OnExitCompleted = False
    _TheGeometry = None

    ts_WxApp = None

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        Create a new application object, starting the bootstrap process.
        '''

        theClass = 'PyApp'

        wx.RegisterFirstCallerClassName(self, theClass)

        # Initiate bootstrap process

        EvtHandler.__init__(self)

        applicationId = wx.ID_ANY

        self.tsBeginClassRegistration(theClass, applicationId)

        self.ts_theTerminal = tsGTUI.GraphicalTextUserInterface(theClass)
        try:
            if True:
                PyApp._TheGeometry = self.ts_theTerminal.StdscrGeometryPixels
            else:
                (theScreenX,
                 theScreenY,
                 theScreenWidth,
                 theScreenHeight) = self.ts_theTerminal.StdscrGeometry

                PyApp._TheGeometry = wxRect(
                    theScreenX * wx.pixelWidthPerCharacter,
                    theScreenY * wx.pixelHeightPerCharacter,
                    theScreenWidth * wx.pixelWidthPerCharacter,
                    theScreenHeight * wx.pixelHeightPerCharacter)

        except AttributeError:
            PyApp._TheGeometry = wxRect(-1, -1, -1, -1)

        self.ts_Active = True
        self.ts_AppName = None
        self.ts_AssertMode = False
        self.ts_ClassName = theClass
        self.ts_EventLoop = None
        self.ts_Exit = False
        self.ts_ExitMainLoop = False
        self.ts_ExitOnFrameDelete = True
        self.ts_IdleEvents = False
        self.ts_IsActive = False
        self.ts_LayoutDirection = wx.Layout_Default

        self.ts_PrintMode = wx.UseDefaultValue

##        self.ts_thisown = None

        # Create a Frame that encompasses entire curses screen (stdscr).
        # It is the default for handling mouse clicks outside of those
        # top-level windows (frames and dialogs), and their children,
        # that do not fully occupy the curses screen.
        theParent = None
        self.ts_TheTopUserWindow = None
        self.ts_TheTopWindow = wxScreen(
            theParent,
            id=wx.ID_ANY,
            title='Screen',
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.DEFAULT_FRAME_STYLE,
            name=wx.ScreenNameStr)

        # Set default Window that will receive Keyboard Text Entry Input.
        # Must bypass use of self.tsRegisterKeyboardInputOrder()
        try:

            tsWxGTUI_DataBase.KeyboardInputRecipients[
                'lifoList'] = self.ts_TheTopWindow

        except Exception as errorCode:

            msg = 'txWxPyApp.__init__: errorCode=""%s"' % str(errorCode)
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.ts_Traits = None
        self.ts_UseBestVisual = True
        self.ts_VendorName = wx.ThemeToUse['VendorName']

        if wx.ThemeToUse['TaskBar']['Enable']:
            self.ts_TaskWin = self.tsCreateTaskBar()
            self.ts_TaskWin.Show()
            self.ts_TaskWin.tsShowTaskBar()
        else:
            self.ts_TaskWin = None

        # Set True for Event Handling
        PyApp._KeepGoing = True
        PyApp._OnExitCompleted = False
        self.ts_IdleQueue = wxDoubleLinkedList()

        self.logger.debug(
            'tsWxPyApp.keepGoing: %s for %s (0x%X).' % (PyApp._KeepGoing,
                                                theClass,
                                                id(self)))
 
        PyApp.ts_WxApp = self

##        self.ts_BootstrapApp()

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def __del__(self):
##        '''
##        '''
##        pass

    #-----------------------------------------------------------------------

    def Dispatch(self):
        '''
        Process the first event in the event queue (blocks until an event
        appears if there are none currently).
        '''
        while True:

            # Suspend execution for the given number of seconds. The argument
            # may be a floating point number to indicate a more precise sleep
            # time. The actual suspension time may be less than that requested
            # because any caught signal will terminate the sleep() following
            # execution of that signal catching routine. Also, the suspension
            # time may be longer than requested by an arbitrary amount because
            # of the scheduling of other activity in the system.
            if self.ts_IdleQueue.GetCount() == 0:

                time.sleep(0.010)

            else:

                node = self.ts_IdleQueue.Pop()
                event = node.GetUserData()
                print('tsWxPyApp.Dispatch: event=%s' % str(event))

    #-----------------------------------------------------------------------

    def Exit(self):
        '''
        Exit the main loop thus terminating the application. :see: wx.Exit
        '''
        self.ts_Exit = True

    #-----------------------------------------------------------------------

    def ExitMainLoop(self):
        '''
        Exit the main GUI loop during the next iteration of the main loop,
        (i.e. it does not stop the program immediately!)
        (i.e....).
        '''
        self.ts_ExitMainLoop = True

    #-----------------------------------------------------------------------

    def FilterEvent(self, event):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def GetAppName(self):
        '''
        Get the application name.
        '''
        return (self.ts_AppName)

    #-----------------------------------------------------------------------

    def GetAssertMode(self):
        '''
        Get the current OnAssert behaviour setting.
        '''
        return (self.ts_AssertMode)

    #-----------------------------------------------------------------------

    def GetClassName(self):
        '''
        Get the application class name.
        '''
        return (self.ts_ClassName)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetComCtl32Version():
        '''
        Returns 400, 470, 471, etc. for comctl32.dll.
        Returns 4.00, 4.70, 4.71 or 0 if it was not found at all.
        Raises an exception on non-Windows platforms.
        '''
        return (0)

    #-----------------------------------------------------------------------

    def GetExitOnFrameDelete(self):
        '''
        Get the current exit behaviour setting.
        '''
        return (self.ts_ExitOnFrameDelete)

    #-----------------------------------------------------------------------

    def GetLayoutDirection(self):
        '''
        Return the layout direction for the current locale.
        '''
        return (self.ts_LayoutDirection)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetMacAboutMenuItemId():
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetMacAboutMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    @staticmethod
    def GetMacExitMenuItemId():
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetMacExitMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetMacHelpMenuTitleName():
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetMacHelpMenuTitleName'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetMacPreferencesMenuItemId():
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetMacPreferencesMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetMacSupportPCMenuShortcuts():
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetMacSupportPCMenuShortcuts'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetPrintMode(self):
        '''
        Get the current Print Mode behaviour setting.
        '''
        return (self.ts_PrintMode)

    #-----------------------------------------------------------------------

    def GetTopWindow(self):
        '''
        Return the main top level window (if it had not been set previously
        with SetTopWindow(), will return just some top level window and, if
        there not any, will return None)
        '''
        reply = None
        if self.ts_TheTopUserWindow is not None:

            # Return the main top level window established by application
            reply = self.ts_TheTopUserWindow

        else:

            lastTask = len(self.ts_WindowTopLevelTasks) - 1

            # Return just some top level window if there are any.
            # Skip task bar and stdio redirection
            for aTask in self.ts_WindowTopLevelTasks:

                if aTask.ts_Name == wx.TaskBarNameStr:

                    pass

                elif aTask.ts_Name == wx.StdioNameStr:

                    pass

                else:

                    reply = aTask
                    break

        return (reply)

    #-----------------------------------------------------------------------

    def GetTraits(self):
        '''
        Return (and create if necessary) the app traits object to which we
        delegate for everything which either should be configurable by the
        user (then he can change the default behaviour simply by overriding
        CreateTraits() and returning his own traits object) or which is
        GUI/console dependent as then wx.AppTraits allows us to abstract
        the differences behind the common facade.
        '''
        return (self.ts_Traits)

    #-----------------------------------------------------------------------

    def GetUseBestVisual(self):
        '''
        Get current UseBestVisual setting.
        '''
        return (self.ts_UseBestVisual)

    #-----------------------------------------------------------------------

    def GetVendorName(self):
        '''
        Get the application vendor name.
        '''
        return (self.ts_VendorName)

    #-----------------------------------------------------------------------

    def HandleEvent(self, handler, funct, event):
        '''
        This function simply invokes the given method funct of the
        specified event handler, handler, with the event as parameter.
        '''
        return (handler.funct(event))

    #-----------------------------------------------------------------------

    def IsActive(self):
        '''
        Return True if our app has focus.
        '''
        return (self.ts_IsActive)

    #-----------------------------------------------------------------------

    @staticmethod
    def IsDisplayAvailable():
        '''
        Tests if it is possible to create a GUI in the current environment.
        This will mean different things on the different platforms.

        * On X Windows systems this function will return False if it is not
        able to open a connection to the X display, which can happen if
        $DISPLAY is not set, or is not set correctly.
 
        * On Mac OS X a False return value will mean that wx is not able to
        access the window manager, which can happen if logged in remotely
        or if running from the normal version of python instead of the
        framework version, (i.e., pythonw.)
 
        * On MS Windows...
        '''
        if PyApp._TheGeometry == wxRect(-1, -1, -1, -1):
            termname = None
        else:
            try:
                termname = tsGTUI.GraphicalTextUserInterface.TermName
            except AttributeError:
                termname = None

        displayAvailable = termname is not None
 
        return (displayAvailable)

    #-----------------------------------------------------------------------

    @staticmethod
    def IsMainLoopRunning():
        '''
        Returns True if we are running the main loop, i.e. if the events
        can currently be dispatched.
        '''
        # TBD - Should this be "PyApp._OnExitCompleted" or "KeepGoing"?
        return (PyApp._KeepGoing)

    #-----------------------------------------------------------------------

    def MainLoop(self):
        '''
        Execute the main GUI loop, the function does not normally return
        until all top level windows have been closed and destroyed.
        '''

        self.logger.debug('-------- Begin MainLoop.')

        # Create an event loop and make it active.  If you are
        # only going to temporarily have a nested event loop then
        # you should get a reference to the old one and set it as
        # the active event loop when you are done with this one...
        evtloop = EventLoop(parent=self)
        old = EventLoop.GetActive()
        EventLoop.SetActive(evtloop)
        self.ts_EventLoop = evtloop

        # This outer loop determines when to exit the application,
        # for this example we let the main frame reset this flag
        # when it closes.
        while PyApp._KeepGoing:

            # At this point in the outer loop you could do
            # whatever you implemented your own MainLoop for.  It
            # should be quick and non-blocking, otherwise your GUI
            # will freeze.

            # call_your_code_here()

            # This inner loop will process any GUI events
            # until there are no more waiting.
            while evtloop.Pending():

                evtloop.Dispatch()

            # Send idle events to idle handlers.  You may want to
            # throttle this back a bit somehow so there is not too
            # much CPU time spent in the idle handlers.  For this
            # example, I'll just snooze a little...
            time.sleep(0.50)
            self.ProcessIdle()

        EventLoop.SetActive(old)
        self.ts_EventLoop = old

        if not PyApp._OnExitCompleted:
            try:
                self.OnExit()
                self.logger.debug('tsWxPyApp.Performed OnExit.')
            except AttributeError:
                self.logger.debug('tsWxPyApp.Skipped OnExit.')
            PyApp._OnExitCompleted = True

        self.logger.debug('-------- End MainLoop.')

    #-----------------------------------------------------------------------

    def OnExit(self):
        '''
        Override this member function for any processing which needs to be
        done as the application is about to exit. OnExit is called after
        destroying all application windows and controls, but before wxWidgets
        cleanup. Note that it is not called at all if {OnInit} failed.

        The return value of this function is currently ignored, return the
        same value as returned by the base class method if you override it.
        '''
        return (True)

    #-----------------------------------------------------------------------

    def OnPreInit(self):
        '''
        This must be provided by the application, and will usually create the
        application main window, optionally calling {wxApp::SetTopWindow}.
        You may use {OnExit} to clean up anything initialized here, provided
        that the function returns true.

        Notice that if you want to to use the command line processing provided
        by wxWidgets you have to call the base class version in the derived
        class OnInit().

        Return true to continue processing, false to exit the application
        immediately.
        '''
        # TBD - Should keepgoing if method is not provided by Application.
        keepgoing = True
        if keepgoing:
            msg = "tsWxPyApp: Skipped by OnPreInit stub"
            self.logger.debug(msg)
        else:
            msg = "tsWxPyApp: Aborted by OnPreInit stub"
            raise tse.ProgramException(
                tse.APPLICATION_TRAP, msg)

        return (keepgoing)

    #-----------------------------------------------------------------------

    def Pending(self):
        '''
        Returns True if there are unprocessed events in the event queue.
        '''
        return (False)

    #-----------------------------------------------------------------------

    def ProcessIdle(self):
        '''
        Called from the MainLoop when the application becomes idle (there
        are no pending events) and sends a wx.IdleEvent to all interested
        parties. Returns True if more idle events are needed, False if not.
        '''
        try:
            theEvent = self.ts_EventLoop.tsGetGraphicalUserInput()
        except Exception as userInputError:
            msg = 'tsWxPyApp.ProcessIdle: userInputError="%s".' % \
                  str(userInputError)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
 
        status = self.ProcessIdleEvent()

        return status

    #-----------------------------------------------------------------------
 
    def ProcessIdleEvent(self):
        '''
        Called from the MainLoop when the application becomes idle (there
        are no pending events) and sends a wx.IdleEvent to all interested
        parties. Returns True if more idle events are needed, False if not.
        '''
        status = True
 
        ## self.logger.debug('ProcessIdleEvent: Enter.')

        ## self.logger.debug('ProcessIdleEvent: status = %s.' % status)

        ## self.logger.debug('ProcessIdleEvent: Exit.')

        if wx.ThemeToUse['TaskBar']['Enable']:
            if self.ts_TaskWin is None:
                self.logger.debug(
                    'ProcessIdleEvent: Creating task bar.')
                self.ts_TaskWin = self.tsCreateTaskBar()
                self.ts_TaskWin.Show()
                self.logger.debug(
                    'ProcessIdleEvent: Removed Simulated task bar.')

            self.ts_TaskWin.tsShowTaskBar()

        return (status)

    #-----------------------------------------------------------------------
 
    def ProcessIdleNoEvent(self):
        '''
        Called from the MainLoop when the application becomes idle (there
        are no pending events) and sends a wx.IdleEvent to all interested
        parties. Returns True if more idle events are needed, False if not.
        '''
        if wx.ThemeToUse['TaskBar']['Enable']:
            if self.ts_TaskWin is None:
                self.logger.debug(
                    'ProcessIdleNoEvent: Creating task bar.')
                self.ts_TaskWin = self.tsCreateTaskBar()
                self.ts_TaskWin.Show()
                self.logger.debug(
                    'ProcessIdleNoEvent: Removed Simulated task bar.')

            self.ts_TaskWin.tsShowTaskBar()

        return (True)

    #-----------------------------------------------------------------------

    def ProcessPendingEvents(self):
        '''
        Process all events in the Pending Events list -- it is necessary
        to call this function to process posted events. This normally happens
        during each event loop iteration.
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'ProcessPendingEvents')

    #-----------------------------------------------------------------------

    def SendIdleEvents(self, win, event):
        '''
        Send idle event to window and all subwindows.Returns True if more
        idle time is requested.
        '''
        return (True)

    #-----------------------------------------------------------------------

    def SetAppName(self, name):
        '''
        Set the application name. This value may be used automatically by
        wx.Config and such.
        '''
        self.ts_AppName = name

    #-----------------------------------------------------------------------

    def SetAssertMode(self, mode):
        '''
        Set the OnAssert behaviour for debug and hybrid builds. The
        following flags may be or-ed together:

        wx.PYAPP_ASSERT_SUPPRESS  - Do not do anything
 
        wx.PYAPP_ASSERT_EXCEPTION - Turn it into a Python exception if
        possible (default)
 
        wx.PYAPP_ASSERT_DIALOG    - Display a message dialog
 
        wx.PYAPP_ASSERT_LOG       - Write the assertion info to the wx.Log
        '''
        self.ts_AssertMode = mode

    #-----------------------------------------------------------------------

    def SetClassName(self, name):
        '''
        Set the application class name. This value may be used for
        X-resources if applicable for the platform
        '''
        self.ts_ClassName = name

    #-----------------------------------------------------------------------

    def SetExitOnFrameDelete(self, flag):
        '''
        Control the exit behaviour: by default, the program will exit the
        main loop (and so, usually, terminate) when the last top-level
        program window is deleted. Beware that if you disable this behaviour
        (with SetExitOnFrameDelete(False)), you will have to call
        ExitMainLoop() explicitly from somewhere.
        '''
        self.ExitOnFrameDelete = flag

    #-----------------------------------------------------------------------

    @staticmethod
    def SetMacAboutMenuItemId(val):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetMacAboutMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    @staticmethod
    def SetMacExitMenuItemId(val):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetMacExitMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def SetMacHelpMenuTitleName(val):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetMacHelpMenuTitleName'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def SetMacPreferencesMenuItemId(val):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetMacPreferencesMenuItemId'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def SetMacSupportPCMenuShortcuts(val):
        '''
        '''

        msg = 'NotImplementedError: %s' % 'SetMacSupportPCMenuShortcuts'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetPrintMode(self, mode):
        '''
        '''
        self.ts_PrintMode = mode

    #-----------------------------------------------------------------------

    def SetTopWindow(self, win):
        '''
        Set the main top level window.
        '''
        self.ts_TheTopUserWindow = win

    #-----------------------------------------------------------------------

    def SetUseBestVisual(self, flag, forceTrueColour=False):
        '''
        Set whether the app should try to use the best available visual
        on systems where more than one is available, (Sun, SGI, XFree86 4,
        etc.)
        '''
        self.ts_UseBestVisual = (flag | forceTrueColour)

    #-----------------------------------------------------------------------

    def SetVendorName(self, name):
        '''
        Set the application vendor name. This value may be used automatically
        by wx.Config and such.
        '''
        self.ts_VendorName = name

    #-----------------------------------------------------------------------

    def WakeUpIdle(self):
        '''
        Make sure that idle events are sent again. :see: wx.WakeUpIdle
        TBD ts_IdleEvents??
        '''
        try:
            self.ts_IdleQueue.Add('Test') # ('test', False)
        except Exception as queueError:
            pass
        self.ts_IdleEvents = True

    #-----------------------------------------------------------------------

    def Yield(self, onlyIfNeeded=False):
        '''
        Process all currently pending events right now, instead of waiting
        until return to the event loop. It is an error to call Yield
        recursively unless the value of onlyIfNeeded is True.
        '''
        return (onlyIfNeeded)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions
 
    def tsCreateTaskBar(self):
        '''
        Create the frame to contain the focus selector buttons.
        '''
        thePosition = wx.DefaultPosition
        self.logger.debug('tsCreateTaskBar: thePosition=%s.' % \
                          str(thePosition))

        theSize = wx.DefaultSize
        self.logger.debug('tsCreateTaskBar: theSize=%s.' % \
                          str(theSize))

        theParent = None

        taskBar = wxTaskBar(theParent,
                            id=wx.ID_ANY,
                            title=wx.TaskBarTitleStr,
                            pos=thePosition,
                            size=theSize,
                            style=wx.DEFAULT_TASK_STYLE,
                            name=wx.TaskBarNameStr)

        self.logger.debug('tsCreateTaskBar: taskBar.Rect=%s.' % \
                          str(taskBar.Rect))
        return (taskBar)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Active = property(IsActive)
    AppName = property(GetAppName, SetAppName)
    AssertMode = property(GetAssertMode, SetAssertMode)
    ClassName = property(GetClassName, SetClassName)
    ExitOnFrameDelete = property(GetExitOnFrameDelete, SetExitOnFrameDelete)
    LayoutDirection = property(GetLayoutDirection)
    PrintMode = property(GetPrintMode, SetPrintMode)
##    thisown: The membership flag
    TopWindow = property(GetTopWindow, SetTopWindow)
    Traits = property(GetTraits)
    UseBestVisual = property(GetUseBestVisual, SetUseBestVisual)
    VendorName = property(GetVendorName, SetVendorName)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    print(
        'ProductName: %s\n' % wx.ThemeToUse['ProductName'])
    print(
        ' VendorName: %s\n' % wx.ThemeToUse['VendorName'])
    print(
        '  ThemeName: %s\n' % wx.ThemeToUse['ThemeName'])
    print(
        '  ThemeDate: %s\n' % wx.ThemeToUse['ThemeDate'])
