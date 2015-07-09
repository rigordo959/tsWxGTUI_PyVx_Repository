#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:41:03 AM rsg>"
'''
tsWxObject.py - Base class for most wx objects, although in
wxPython not much functionality is needed nor exposed.
'''
#################################################################
#
# File: tsWxObject.py
#
# Purpose:
#
#    Base class for most wx objects, although in wxPython not
#    much functionality is needed nor exposed.
#
# Usage (example):
#
#    # Import
#
#    from tsWxObject import Object
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
#    1. Though the tsWx package strives to be compatible with wxPython
#       applications, it provides support for only a subset of the
#       WxPython API that includes Frames, Dialogs, Panels, Buttons,
#       CheckBoxes, and Text. It provides support for color and non-color
#       (monochrome) display screens. When appropriate, it maps wxPython
#       color references to one of the following eight colors:
#       BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN and WHITE.
#
#    2. Though it creates GUI elements, it cannot create ones that exceed
#       beyond the boundaries of the system console (ansi, vt100) or shell
#       session console  (cygwin, xterm, xterm-color) used to launch the
#       wxPython application.
#
#       NOTE: It is the operator's responsibility to select, create and
#             adequately size the shell session or system console.
#
#    3. Though it supports GUI dimensions in pixel units, it does not
#       support fonts, icons or picture images.
#
#    4. Tough it supports window borders, it simulates border line features
#       via unique ASCII text characters.
#
#    5. Though it supports status bar (line) features, it overlays status
#       bar panel borders to conserve display screen real estate.
#
#    6. Thos it supports redirection of stdout/stderr, it places the
#       PyOnDemandOutputWindow at the bottom of the display screen.
#
#    7. Though wxPython applications typically run in its own window on
#       a single host computer console and has an associated task bar entry,
#       each tsWx application must run in its own host computer console
#       session which provide aits own task bar entry to enable the operator
#       to switch focus to a "hidden" window.
#
# Background:
#
#    1. wxPython is a GUI toolkit for the Python programming language. It
#       allows Python programmers to create programs with a robust, highly
#       functional graphical user interface, simply and easily. It is
#       implemented as a Python extension module (native code) that wraps
#       the popular wxWidgets cross platform GUI library, which is written
#       in C++.
#
#       Like Python and wxWidgets, wxPython is Open Source which means that
#       it is free for anyone to use and the source code is available for
#       anyone to look at and modify. Or anyone can contribute fixes or
#       enhancements to the project.
#
#       wxPython is a cross-platform toolkit. This means that the same
#       program will run on multiple platforms without modification.
#       Currently supported platforms are 32-bit Microsoft Windows, most
#       Unix or unix-like systems, and Macintosh OS X.
#
#       Since the language is Python, wxPython programs are simple, easy to
#       write and easy to understand.
#
#    2. TeamSTARS developed package "tsWx" to emulate selected features
#       of "wxPython" for those application platfoms that have only
#       non-graphical terminals. Implementation is in Python to facilitate.
#       maintenance and avoid the complexities of adapting the multi-platform
#       wxWidgets source code.
#
# Notes:
#
#    1. Class "Object" is the base class for most wx objects, although in
#       wxPython not much functionality is needed nor exposed.
#
#       The first instantiation of Class "Object" initializes the "curses"
#       display screen, keboard and optional mouse. It accomplishes this
#       via TeamSTARS' "tsWxGraphicalTextUserInterface" library module.
#
#    2. The "tsWx" package is designed for use with the "tsApplication",
#       "tsLogger" and "tsException" packagea. Applications that avail
#       themselves to those TeamSTARS packages can coordinate input via
#       keyboard and mouse with output to a file and/or to the terminal
#       (via "curses" display, stdout or stderr). Upon termination,
#       applications can return a meaningful exit code to facilitate
#       integration with other applications for purposes of automation.
#
#    3. wxWindow is the base class for all windows and represents any visible
#       object on screen. All controls, top level windows and so on are
#       windows. Sizers and device contexts are not, however, as they don't
#       appear on screen themselves.
#
#    4. A frame is a window whose size and position can (usually) be changed
#       by the user. It usually has thick borders and a title bar, and can
#       optionally contain a menu bar, toolbar and status bar. A frame can
#       contain any window that is not a frame or dialog.
#
#       A frame that has a status bar and toolbar created via the
#       CreateStatusBar/CreateToolBar functions manages these windows, and
#       adjusts the value returned by GetClientSize to reflect the remaining
#       size available to application windows.
#
#    5. A panel is a window on which controls are placed. It is usually placed
#       within a frame. It contains minimal extra functionality over and above
#       its parent class wxWindow; its main purpose is to be similar in
#       appearance and functionality to a dialog, but with the flexibility of
#       having any window as a parent.
#
#    6. A control is generally a small window which processes user input and/or
#       displays one or more item of data.
#
#    7. A dialog box is a window with a title bar and sometimes a system menu,
#       which can be moved around the screen. It can contain controls and other
#       windows and is often used to allow the user to make some choice or to
#       answer a question.
#
#    8. An event is a structure holding information about an event passed to a
#       callback or member function. wxEvent used to be a multipurpose event
#       object, and is an abstract base class for other event classes.
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
#    2010/10/10 rsg Invoked "tsResetEventAndAcceleratorTables" during
#                   "tsBeginClassRegistration".
#
#    2010/10/11 rsg Moved methods "tsResetEventAndAcceleratorTables" and
#                   "tsUpdateEventAndAcceleratorTables" from tsWxWindow.
#
#    2011/06/10 rsg Added remarks to tsNewId from Window IDs.
#
#    2012/02/08 rsg Corrected logic associated with SystemEventTable
#                   and UserEventTable to support multiple event
#                   bindings.
#
#    2012/05/26 rsg Modified design to re-use the PyApp instance
#                   instead of creating a second instance  during
#                   instantiation of the EvtHandler class.
#                   Added global class variables PyAPP_Object and
#                   PyApp_EventQueue. Unfortunately, this did not
#                   prevent creation of a second log file directory.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxObject'
__version__   = '1.5.0'
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

import tsExceptions as tse
import tsLogger

import tsWxGlobals as wx
## from tsWxEvent import EVT_SET_FOCUS
from tsWxDebugHandlers import DebugHandlers
from tsWxDisplay import Display as wxDisplay
from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
from tsWxGraphicalTextUserInterface import GraphicalTextUserInterface as tsGTUI
from tsWxRect import Rect as wxRect

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

PYLINT_INIT_ERROR_VALID = False
PERFORMANCE_PREFERENCE = True

#---------------------------------------------------------------------------

class Object(object):
    '''
    The base class for most wx objects, although in wxPython not much
    functionality is needed nor exposed.
    '''

    # Class variables that must be resolved at run time.
    # Manage set of unique IDs.
    CurrentId = 100
    PyApp_EventQueue = None
    PyApp_Object = None
    TheDisplay = None
    TheLogger = None
    TheTerminal = None
    TheTerminalScreen = None

    def __init__(self):
        '''
        Constructor.
        '''
        theClass = 'Object'

        wx.RegisterFirstCallerClassName(self, theClass)

        id = wx.ID_ANY

        # Establish connection with application logger and log the beginning
        # of class registration. Then establish application access to display
        # top-level window and to curses screen and windows.

        if Object.TheLogger is None:

            Object.PyApp_Object = self

            Object.PyApp_EventQueue = wxDoubleLinkedList()

            self.tsBeginClassRegistration(theClass, id)

            self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Destroy(self):
        '''
        Deletes the C++ object this Python object is a proxy for.
        '''
        msg = 'NotImplementedError: %s' % 'Destroy in tsWxObject'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetClassInfo(self):
        '''
        Return information about the class.
        '''
        info = {}

        try:
            info['assignedId'] = self.ts_Id
        except AttributeError:
            info['assignedId'] = None

        try:
            info['earliestAncestor'] = self.ts_EarliestAncestor
        except AttributeError:
            info['earliestAncestor'] = None

        try:
            info['name'] = self.GetClassName()
        except AttributeError:
            info['name'] = None

        try:
            info['parent'] = self.ts_Parent
        except AttributeError:
            info['parent'] = None

        try:
            info['type'] = type(self)
        except AttributeError:
            info['type'] = None

        return (info)

    #-----------------------------------------------------------------------

    def GetClassName(self):
        '''
        Returns the class name of the C++ class using wxRTTI.
        '''
        return (self.ts_ClassName)

    #-----------------------------------------------------------------------

    def IsSameAs(self, p):
        '''
        For wx.Objects that use C++ reference counting internally, this
        method can be used to determine if two objects are referencing
        the same data object.
        '''
        return (id(p) == id(self))

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetClassNameIndent(self, theClassName):
        '''
        Return the hierarchical level associated with the specified class
        for use in indenting the logging of class initialization entry and
        exit.
        '''
        try:
            indent = wx.indentation[theClassName]
        except KeyError as e:
            indent = None
            msg = 'tsGetClassNameIndent Error: %s' % e
            raise tse.ProgramException(
                tse.ARGUMENT_KEY_NOT_VALID, msg)

        return (indent)

    #-----------------------------------------------------------------------

    def tsGetTerminalPixelRectangle(self):
        '''
        Returns the bounding rectangle the client area of the display,
        i.e., without taskbars and such.
        '''
        return (Object.Display.TerminalPixelRectangle)

    #-----------------------------------------------------------------------

    def tsGetTheLogger(self):
        '''
        Return the logger instance.
        '''
        return (Object.Display.TheLogger)

    #-----------------------------------------------------------------------

    def tsGetTheTerminalScreen(self, theClass):
        '''
        Return the screen instance.
        '''
        return (Object.Display.TheTerminalScreen)

    #-----------------------------------------------------------------------

    def tsGetTheTerminal(self, theClass):
        '''
        Return the terminal instance.
        '''
        return (Object.Display.TheTerminal)

    #-----------------------------------------------------------------------

    def tsGetThisOwn(self):
        '''
        Return MembershipFlag.
        '''
        # return (self.ts_MembershipFlag)

        # TBD - Requirements not established.
        # Research (instrumented wxPython Frame demo)
        # "self.thisown" is of boolean type and always False.
        return (False)

    #-----------------------------------------------------------------------

    def tsRegisterClassNameAndMembershipFlag(self, theClass):
        '''
        Record Class Name and Membership Flag instance variables.
        '''
        # Register only new Class Names.
        try:
            # Check if Class Name previously registered.
            if isinstance(self.GetClassName(), type(theClass)):
                # The Class previously registered.
                pass

        except AttributeError:
            # Register the class name of the C++ class using wxRTTI.
            self.ts_ClassName = theClass

            # Register the Class Membership Flag
            self.ts_MembershipFlag = []

        if theClass not in self.ts_MembershipFlag:
            # TBD - Restore the chronological registration caused by
            # delaying tsBeginClassRegistration until a class
            # (such as Frame) had initialized each of its
            # ancestorial base classes (ending with Object).

            if PERFORMANCE_PREFERENCE:
                # Noticably faster but chronologically reversed.
                self.ts_MembershipFlag.append(theClass)
            else:
                # Noticable slower but chronologically correct.
                self.ts_MembershipFlag.insert(0, theClass)

    #-----------------------------------------------------------------------

    def tsInstallTheLoggerAccess(self, indent, theClass, applicationId):
        '''
        Establish connection with application logger.
        '''

        # Setup logger features access
        if (Object.TheLogger is None):

            try:

                # Start the default application logger.
                self.logger = tsLogger.TsLogger(
                    threshold=tsLogger.ERROR,
                    start=time.time(),
                    name=tsLogger.StandardOutputFile)

            except Exception as e:

                self.logger = None
                msg = 'tsInstallTheLoggerAccess: Exception = %s' % e
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            Object.TheLogger = self.logger

            msg = '%s%s.tsInstallLoggerAccess to %s for class %s (%s)' % (
                indent, __title__, self.logger, theClass, applicationId)
            self.logger.debug(msg)

        else:

            # Use the existing application logger
            self.logger = Object.TheLogger
            msg = '%s%s.tsInstallLoggerAccess with %s for class %s (%s)' % (
                indent, __title__, self.logger, theClass, applicationId)
            self.logger.debug(msg)
 
    #-----------------------------------------------------------------------

    def tsInstallTheTerminalAccess(self, indent, theClass, applicationId):
        '''
        Establish those display areas reserved for task bar and stdio
        redirection. Create links to the internal information needed
        to monitor and control the physical screen and virtual windows
        of the Graphical Text User Interface.
        '''

        # Setup display features access

        if Object.TheDisplay is None:

            # Start Curses interface.
            reserveTaskBarAreaFlag = True
            reserveRedirectAreaFlag = True # Should default be True or False?
            reserveAreaFlags = {
                'ReserveTaskBarArea': reserveTaskBarAreaFlag,
                'ReserveRedirectArea': reserveRedirectAreaFlag}

            try:

                parent = self
                self.display = wxDisplay(parent, reserveAreaFlags)
                fmt = '%s%s.tsInstallTheTerminalAccess ' + \
                      'to %s for class %s (%s)'
                msg = fmt % (indent,
                             __title__,
                             self.display,
                             theClass,
                             applicationId)
                self.logger.debug(msg)

            except Exception as e:

                self.display = None
                msg = '%s.tsInstallTheTerminalAccess: Exception = %s' % \
                      (__title__, e)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            Object.TheDisplay = self.display

            try:

                self.terminal = self.display.TheTerminal

            except AttributeError as e:

                self.terminal = None
                msg = 'tsInstallTheTerminalAccess: Exception = %s' % e
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            Object.TheTerminal = self.terminal

            try:

                self.stdscr = self.display.TheTerminal

            except AttributeError as e:

                self.stdscr = None
                msg = 'tsInstallTheTerminalAccess: Exception = %s' % e
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            Object.TheTerminalScreen = self.stdscr

        else:

            self.display = Object.TheDisplay
            self.terminal = Object.TheTerminal
            self.stdscr = Object.TheTerminalScreen

            fmt = '%s%s.tsInstallTheTerminalAccess with %s for class %s (%s)'
            msg = fmt % (indent,
                         __title__,
                         self.display,
                         theClass,
                         applicationId)
            self.logger.debug(msg)

    #-----------------------------------------------------------------------

    def tsBeginClassRegistration(self, theClass, applicationId):
        '''
        Establish connection with application logger. Log the beginning of
        class registration.

        Establish application access to display top-level window and to
        curses screen and windows.
        '''

        indent = '--' * self.tsGetClassNameIndent(theClass)

        # Establish connection with logger devices and files.
        self.tsInstallTheLoggerAccess(indent, theClass, applicationId)

        # Establish those display areas reserved for task bar and stdio
        # redirection. Create links to the internal information needed
        # to monitor and control the physical screen and virtual windows
        # of the Graphical Text User Interface.
        self.tsInstallTheTerminalAccess(indent, theClass, applicationId)

        # Register each unique wxPython instance.
        self.ts_AssignedId = self.tsNewId()

        # Register each application developer instance.
        # NOTE: Application developer is responsible for uniqueness.
        #       Newest instance overwrites previously registered one.
        if applicationId == wx.ID_ANY:
            self.ts_Id = self.ts_AssignedId + 32768
        else:
            self.ts_Id = applicationId
##            if self.ts_Id in self.ts_WindowsById.keys():
##                self.logger.warning(
##                    'Duplicate Id (%d) replaces predecessor.' % self.ts_Id)

        self.ts_EarliestAncestor = None
        self.ts_TheWindows = tsGTUI.TheWindows
        self.ts_TopLevelWindows = tsGTUI.TopLevelWindows
        self.ts_WindowHandles = tsGTUI.WindowHandles
        self.ts_WindowIndex = tsGTUI.TheWindows['windowIndex']
        self.ts_WindowTopLevelTasks = tsGTUI.WindowTopLevelTasks
        self.ts_WindowsByAssignedId = tsGTUI.WindowsByAssignedId
        self.ts_WindowsById = tsGTUI.WindowsById
        self.ts_WindowsByName = tsGTUI.WindowsByName
        self.ts_WindowsByShowOrder = tsGTUI.WindowsByShowOrder

        self.ts_SystemEventTable = {}
        self.ts_SystemEventTable['name'] = 'SystemEventTable'
        self.ts_UserEventTable = {}
        self.ts_UserEventTable['name'] = 'UserEventTable'

        self.tsRegisterClassNameAndMembershipFlag(theClass)

    #-----------------------------------------------------------------------

    def tsEndClassRegistration(self, theClass):
        '''
        Log the ending of class registration.
        '''
        indent = '--' * self.tsGetClassNameIndent(theClass)
        self.logger.debug(
            '%s End %s (0x%X).' % (indent, theClass, id(self)))

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetTheId(mySelf):
        '''
        Return the ID associated with this class instance.
        '''
        return id(mySelf)

    #----------------------------------------------------------------------

    @staticmethod
    def tsNewId():
        '''
        Create a unique ID.

        Remarks:
        Various controls and other parts of wxWidgets need an ID. Sometimes
        the ID may be directly provided by the user or have a predefined
        value, such as wxID_OPEN. Often, however, the value of the ID is
        unimportant and is created automatically by calling
        wxWindow::NewControlId or by passing wxID_ANY as the ID of an
        object.

        There are two ways to generate an ID. One way is to start at a
        negative number, and for each new ID, return the next smallest
        number. This is fine for systems that can use the full range of
        negative numbers for IDs, as this provides more than enough IDs
        and it would take a very very long time to run out and wrap
        around. However, some systems cannot use the full range of the
        ID value. Windows, for example, can only use 16 bit IDs, and
        only has about 32000 possible automatic IDs that can be
        generated by wxWindow::NewControlId. If the program runs long
        enough, depending on the program itself, using this first method
        would cause the IDs to wrap around into the positive ID range
        and cause possible clashes with any directly specified ID values.

        The other way is to keep track of the IDs returned by
        wxWindow::NewControlId and do not return them again until the
        ID is completely free and not being used by any other objects.
        This will make sure that the ID values do not clash with one
        another. This is accomplished by keeping a reference count for
        each of the IDs that can possibly be returned by
        wxWindow::NewControlId. Other IDs are not reference counted.
        '''
        # skip the part of IDs space that contains hard-coded values:
        if Object.CurrentId < wx.ID_LOWEST:
            Object.CurrentId += 1
        elif Object.CurrentId > wx.ID_HIGHEST:
            Object.CurrentId += 1
        else:
            Object.CurrentId = wx.ID_HIGHEST + 1

        return (Object.CurrentId)

    #----------------------------------------------------------------------

    @staticmethod
    def tsGetCurrentId():
        '''
        Return latest ID.
        '''
        return (Object.CurrentId)

    #----------------------------------------------------------------------

    @staticmethod
    def tsRegisterId(usedId):
        '''
        Adjust latest ID to reflect specified new one.
        '''
        if (usedId > Object.CurrentId):

            Object.CurrentId = usedId

    #-----------------------------------------------------------------------

    def tsUpdateEventAndAcceleratorTables(self,
                                          event,
                                          handler,
                                          source,
                                          id=wx.ID_ANY,
                                          id2=wx.ID_ANY,
                                          useSystemEventTable=False):
        '''
        Bind with event and accelerator System and User tables.
 
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
 
        id2: Used when it is desirable to bind a handler to a range of ids,
             such as with EVT_MENU_RANGE.
        '''
        theEvent = event
        theHandler = handler
        theSource = source

        if id == wx.ID_ANY:
            theId = self.tsNewId()
        else:
            theId = id

        if id2 == wx.ID_ANY:
            theId2 = self.tsNewId()
        else:
            theId2 = id2

        # theAssignedId = theSource.ts_AssignedId
        theLabel = theSource.GetLabel()

        theAssignedEventBindingId = self.tsNewId()
        theEventBindingName = 'EventBinding-%d' % theAssignedEventBindingId

        theSystemEventTable = theSource.ts_SystemEventTable
        theUserEventTable = theSource.ts_UserEventTable

        if useSystemEventTable:

            if not (theEventBindingName in list(theSystemEventTable.keys())):

                theSystemEventTable[theEventBindingName] = {}
##                theSystemEventTable[theEventBindingName][
##                    'name'] = theEventBindingName

            theSystemEventTable[theEventBindingName] = {
                'event': theEvent,
                'eventType': theEvent.ts_EventType,
                'handler': theHandler,
                'id': theId,
                'id2':theId2,
                'label': theLabel,
                'name': theEventBindingName,
                'source': theSource.ts_AssignedId}

        else:

            if not (theEventBindingName in list(theUserEventTable.keys())):

                theUserEventTable[theEventBindingName] = {}
##                theUserEventTable[theEventBindingName][
##                    'name'] = theEventBindingName

            theUserEventTable[theEventBindingName] = {
                'event': theEvent,
                'handler': theHandler,
                'id': theId,
                'id2':theId2,
                'label': theLabel,
                'name': theEventBindingName,
                'source': theSource.ts_AssignedId}

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ClassName = property(GetClassName)

    if True:
        # tsWx API Extension
        thisown = property(tsGetThisOwn)
    else:
        # non-tsWx API Extension
        thisown = property(lambda x: x.this.own(),
                           lambda x, v: x.this.own(v),
                           doc='The membership flag')

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

##    import tsApplication as tsAPP
##    import sys
##    import traceback

##    def theMainApplication():
##        print __header__
##        myObject = Object()

##        myObject.logger.debug(
##            'ClassName: %s' % myObject.ClassName)
##        myObject.logger.debug(
##            'ts_MembershipFlag: %s' % myObject.ts_MembershipFlag)
##        myObject.logger.debug(
##            'thisown: %s' % myObject.thisown)
##        myObject.logger.debug(
##            'IsSameAs (True): %s' % myObject.IsSameAs(myObject))
##        myObject.logger.debug(
##            'IsSameAs (False): %s' % myObject.IsSameAs('Junk'))
##        myObject.logger.debug(
##            'Destroy  (True): %s' % myObject.Destroy())
##        myObject.logger.debug(
##            'Destroy  (False): %s' % myObject.Destroy())

##        # myObject.logger.debug(
##        #     'tsGetTerminalPixelRectangle: %s' % \
##        #     myObject.tsGetTerminalPixelRectangle())

##    exitStatus = tse.NONERROR_ERROR_CODE
##    msg = tse.NO_ERROR

##    try:
##        theApplication = tsAPP.TsApplication(
##            header=__header__,
##            main=theMainApplication,
##            mainTitleVersionDate=mainTitleVersionDate,
##            title=__title__,
##            version=__version__,
##            date=__date__,
##            logs=[])

##        theApplication.runMain()

##    except Exception, applicationError:
##        if isinstance(applicationError, tse.TsExceptions):
##            msg = str(applicationError).replace("'", "")
##            tse.displayError(applicationError)
##            exitStatus = applicationError.exitCode
##        else:
##            msg = None
##            sys.stderr.write(traceback.format_exc())
##            exitStatus = tse.INVALID_ERROR_CODE

##    if msg == tse.NO_ERROR:
##        sys.stdout.write(msg)
##    elif msg is not None:
##        sys.stderr.write(msg)

##    # Return (exitStatus)
##    sys.exit(exitStatus)
