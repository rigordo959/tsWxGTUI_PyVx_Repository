#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:12:40 AM rsg>"
'''
tsWxApp.py - Class to represent the application. It is used to
bootstrap the wxPython system and initialize the underlying gui
toolkit. It sets and gets application-wide properties. It
implements the windowing system main message or event loop. It
dispatches events to window instances.
'''
#################################################################
#
# File: tsWxApp.py
#
# Purpose:
#
#    Class to represent the application. It is used to bootstrap
#    the wxPython system and initialize the underlying gui
#    toolkit. It sets and gets application-wide properties. It
#    implements the windowing system main message or event loop.
#    It dispatches events to window instances.
#
# Usage (example):
#
#    # Import
#
#    from tsWxApp import App
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
#    2010/11/01 rsg Added logic to initialize App.wxTheApp.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxApp'
__version__   = '1.0.6'
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

import sys
import signal
import time

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

tsrpu = tsReportUtilities.TsReportUtilities()

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxPyOnDemandOutputWindow \
     import PyOnDemandOutputWindow as wxPyOnDemandOutputWindow
from tsWxGTUI_Py2x.tsLibGUI.tsWxPyApp import PyApp
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class App(PyApp):
    '''
    The wx.App class represents the application and is used to:

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
    # Class Variables:
    outputWindowClass = wxPyOnDemandOutputWindow
    wxTheApp = None

    #-----------------------------------------------------------------------

    def __init__(self,
                 redirect=False,
                 filename=None,
                 useBestVisual=False,
                 clearSigInt=True):
        '''
        Construct a wx.App object.

        Parameters:

            redirect - Should sys.stdout and sys.stderr be redirected?
            Defaults to True on Windows and Mac, False otherwise. If filename
            is None then output will be redirected to a window that pops up
            as needed. (You can control what kind of window is created for
            the output by resetting the class variable outputWindowClass to
            a class of your choosing.)

            filename - The name of a file to redirect output to, if redirect
            is True.

            useBestVisual - Should the app try to use the best available
            visual provided by the system (only relevant on systems that have
            more than one visual.) This parameter must be used instead of
            calling SetUseBestVisual later on because it must be set before
            the underlying GUI toolkit is initialized.

            clearSigInt - Should SIGINT be cleared? This allows the app to
            terminate upon a Ctrl-C in the console like other GUI apps will.

        Note: You should override OnInit to do applicaition initialization
        to ensure that the system, toolkit and wxWidgets are fully initialized.
        '''
        theClass = 'App'

        wx.RegisterFirstCallerClassName(self, theClass)

        # Capture initial caller parametsrs before they are changed
        self.ts_redirect = redirect
        self.ts_filename = filename
        self.ts_useBestVisual = useBestVisual
        self.ts_clearSigInt = clearSigInt
        self.outputWindowAttributes = None
        self.stdioWin = None
        self.stdioLog = None

        self.ts_ReserveRedirectArea = redirect and \
                                      filename is None

        self.ts_ReserveTaskBarArea = wx.ThemeToUse['TaskBar']['Enable']

        PyApp.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        if App.wxTheApp is None:

            App.wxTheApp = self
 
        # Make sure we can create a GUI
        if not self.IsDisplayAvailable():

            msg = "Unable to create GUI"
            raise tse.UserInterfaceException(
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)
 
        # This has to be done before OnInit
        self.SetUseBestVisual(useBestVisual)

        # Set the default handler for SIGINT.  This fixes a problem
        # where if Ctrl-C is pressed in the console that started this
        # app then it will not appear to do anything, (not even send
        # KeyboardInterrupt???)  but will later segfault on exit.  By
        # setting the default handler then the app will exit, as
        # expected (depending on platform.)
        if clearSigInt:
            try:
                signal.signal(signal.SIGINT, signal.SIG_DFL)
            except ImportError:
                pass

        # Save and redirect the stdio to a window?
        self.stdioWin = None
        self.saveStdio = (sys.stdout, sys.stderr)

##        if redirect:
##            self.RedirectStdio(self.ts_filename)

        try:
            # Initialize the specified stdout/stderr redirection.
            if self.ts_redirect:
                self.logger.debug(
                    '    Redirection: (%s); Filename: %s.' % (
                        self.ts_redirect,
                        self.ts_filename))
                self.RedirectStdio(filename=self.ts_filename)
                self.logger.debug('  Performed Redirection.')

        except AttributeError, RedirectError:
            self.logger.error('  Skipped Redirection. %s' % RedirectError)
            raise

        # Use Python's install prefix as the default
##        wx.StandardPaths.Get().SetInstallPrefix(sys.prefix)

        # Until the new native control for wxMac is up to par, still use
        # the generic one.
##        wx.SystemOptions.SetOptionInt("mac.listctrl.always_use_generic", 1)

        # This finishes the initialization of wxWindows and then calls
        # the OnInit that should be present in the derived class
        self.tsBootstrapApp()

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def __del__(self, destroy):
##        '''
##        '''
##        if destroy:
##            self.Destroy()

    #-----------------------------------------------------------------------

    def Destroy(self):
        '''
        '''
        if self.ts_redirect:
            self.RestoreStdio()

    #-----------------------------------------------------------------------

    def GetMainLoop(self):
        '''
        Return the main GUI event loop instance.

        Note: Overrides tsWxPyApp.MainLoop.
        '''
        return (PyApp.MainLoop(self))

    #-----------------------------------------------------------------------

    def MainLoop(self):
        '''
        Execute the main GUI event loop.

        Note: Overrides tsWxPyApp.MainLoop.
        '''
        PyApp.MainLoop(self)
        self.RestoreStdio()

    #-----------------------------------------------------------------------

    def OnPreInit(self):
        '''
        Things that must be done after _BootstrapApp has done its thing, but
        would be nice if they were already done by the time that OnInit is
        called.
        '''
        status = PyApp.OnPreInit(self)
        # Force redirection to start before application Frame(s).
        if status:
            print('')
        return (status)

    #-----------------------------------------------------------------------

    def RedirectStdio(self, filename=None):
        '''
        Redirect sys.stdout and sys.stderr to a file or a popup window.
        '''
        # Verify user accessibility of one library known to be in hierarchy.
        try:
            preRedirectStdioDevices = {'stdout': sys.stdout,
                                       'stderr': sys.stderr,
                                       ' stdin': sys.stdin}

            for theKey in list(preRedirectStdioDevices.keys()):
                self.logger.debug(
                    '    Saved %s %s' % (
                        theKey, preRedirectStdioDevices[theKey]))
        except Exception, preRedirectStdioDevicesError:
            msg = "tsWxApp: %s" % preRedirectStdioDevicesError
            raise tse.ProgramException(
                tse.APPLICATION_TRAP, msg)

        # Save configuration for future restoration by RestoreStdio.
        self.saveStdio = (sys.stdout, sys.stderr)

        if filename is None:

            # Redirect output to a window on the screen.
            # Capture redirected output to a default file for scrolling.
            # TBD - How can this support the ThemeToUse Timestamp feature?
            self.stdioWin = self.outputWindowClass(wx.ThemeToUse['Stdio']['Title'])
            sys.stdout = self.stdioWin
            sys.stderr = self.stdioWin

            try:
                windowStdioDevices = {'stdout': sys.stdout,
                                      'stderr': sys.stderr,
                                      ' stdin': sys.stdin}

                for theKey in list(windowStdioDevices.keys()):
                    self.logger.debug(
                        '    Saved %s %s' % (
                            theKey, windowStdioDevices[theKey]))
            except Exception, windowStdioDevicesError:
                msg = "tsWxApp: %s" % windowStdioDevicesError
                raise tse.ProgramException(
                    tse.APPLICATION_TRAP, msg)

        else:
 
            # Redirect output to the specified file.
            # Setting buffer size of 0 eliminates need for flushing.
            if wx.ThemeToUse['Stdio']['Timestamp']:
                self.stdioLog = tsCustomStdioFile(filename, 'w', 0)
            else:
                self.stdioLog = open(filename, 'w', 0)

            sys.stdout = self.stdioLog
            sys.stderr = self.stdioLog

            try:
                fileStdioDevices = {'stdout': sys.stdout,
                                      'stderr': sys.stderr,
                                      ' stdin': sys.stdin}

                for theKey in list(fileStdioDevices.keys()):
                    self.logger.debug(
                        '    Saved %s %s' % (
                            theKey, fileStdioDevices[theKey]))
            except Exception, fileStdioDevicesError:
                msg = "tsWxApp: %s" % fileStdioDevicesError
                raise tse.ProgramException(
                    tse.APPLICATION_TRAP, msg)

            theLogFileHeader = tsrpu.getSeparatorString(
                title='Begin %s on %s' % (
                    'PRINT/STDOUT/STDERR log',
                    tsrpu.getDateAndTimeString(time.time())),
                indent=0,
                position=tsrpu.layout['TitleIndent'],
                separatorCharacter='$',
                tab=4)

            self.stdioLog.write('%s\n\n' % theLogFileHeader)
            self.stdioLog.write('%s - Started logging to file "%s".\n\n' % (
                tsrpu.getDateTimeString(time.time()),
                filename))

            msg1 = 'Print statements and other standard output '
            msg2 = 'will now be directed to this file.'
            self.stdioLog.write('%s\n' % (msg1 + msg2))

            self.stdioLog.flush()

    #-----------------------------------------------------------------------

    def RestoreStdio(self):
        '''
        Restore sys.stdout and sys.stderr.
        '''
        try:
            (sys.stdout, sys.stderr) = self.saveStdio
        except AttributeError:
            pass

        self.stdioLog = None
        self.stdioWin = None

    #-----------------------------------------------------------------------

    def SetOutputWindowAttributes(self,
                                  title=None,
                                  pos=None,
                                  size=None):
        '''
        Set the title, position and/or size of the output window if the
        stdio has been redirected.
        '''
        if self.stdioWin:
            # TBD - Cannot set attributes when window does not exist.
            if title is not None:
                self.stdioWin.title = title

            if pos is not None:
                self.stdioWin.pos = pos

            if size is not None:
                self.stdioWin.size = size

    #-----------------------------------------------------------------------

    def SetTopWindow(self, frame):
        '''
        Set the main top level window.
        '''
        self.ts_TopWindow = frame

        if self.stdioWin:
            self.stdioWin.SetParent(frame)
        PyApp.SetTopWindow(self, frame)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def OnInit(self):
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

        Note: This module does not appear in wPython API for wxApp or wxPyApp.
        '''
        # TBD - Should keepgoing if method is not provided by Application.
        keepgoing = True
        if keepgoing:
            msg = "tsWxApp: Skipped by OnInit stub"
            self.logger.debug(msg)
        else:
            msg = "tsWxApp: Aborted by OnInit stub"
            raise tse.ProgramException(
                tse.APPLICATION_TRAP, msg)

        return (keepgoing)

    #-----------------------------------------------------------------------

    def tsBootstrapApp(self):
        '''
        Initialize the native GUI (curses) screen. Perform any application
        specified pre-initialization and initialization activities.
        '''
        self.logger.debug('  Begin BootstrapApp.')

        try:
            # Perform any application specified pre-initialization activities
            # that must be done after _BootstrapApp has done its thing, but
            # would be nice if they were already done by the time that OnInit
            # is called.
            self.OnPreInit()
            self.logger.debug('  Performed OnPreInit.')

        except AttributeError, OnPreInitError:
            self.logger.error('  Skipped OnPreInit. %s' % OnPreInitError)
            msg = 'CheckOnPreInitError: %s' % OnPreInitError
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        try:
            # Perform any application specified outer-loop initialization
            # activities such as the creation of frames..
            self.OnInit()
            self.logger.debug('  Performed OnInit.')

        except AttributeError, OnInitError:
            self.logger.error('  Skipped OnInit. %s' % OnInitError)
            msg = 'CheckOnInitError: %s' % OnInitError
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.logger.debug('  End BootstrapApp.')

    #-----------------------------------------------------------------------

    def tsSetStdioWindowAttributes(self,
                                   title=None,
                                   pos=None,
                                   size=None,
                                   style=None,
                                   name=None):
        '''
        Set the title, position, size, style and name of the output window
        if the stdio has been redirected.
        '''
        if self.stdioWin:
            # TBD - Cannot set attributes when window does not exist.
            myRect = self.Display.theRedirectedStdioArea
            if title is not None:
                self.stdioWin.title = title
            else:
                self.stdioWin.title = wx.ThemeToUse['Stdio']['Title']

            if pos is not None:
                self.stdioWin.pos = pos
            else:
                self.stdioWin.pos = wxPoint(myRect.x, myRect.y)

            if size is not None:
                self.stdioWin.size = size
            else:
                self.stdioWin.size = wxSize(myRect.width, myRect.height)

            if style is not None:
                self.stdioWin.style = style
            elif wx.ThemeToUse['Stdio']['Title'] == wx.StdioRedirectedTitleStr:
                self.stdioWin.style = wx.DEFAULT_STDIO_STYLE
            else:
                self.stdioWin.style = wx.DEFAULT_FRAME_STYLE

            if name is not None:
                self.stdioWin.name = name
            elif wx.ThemeToUse['Stdio']['Title'] == wx.StdioRedirectedTitleStr:
                self.stdioWin.name = wx.StdioNameStr
            else:
                self.stdioWin.name = wx.FrameNameStr

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

class tsCustomStdioFile(object):
    '''
    Class to open the specified file and then prefix output with a
    system timestamp.
    '''
    def __init__(self, name, mode, buffer):
        '''
        Construct class.
        '''
        self.ts_LineCount = 0
        self.ts_LastHeaderLine = 7
        self.ts_File = open(name, mode, buffer)

    #-----------------------------------------------------------------------

    def write(self, text):
        '''
        Output specified text with the appropriate timestamp
        prefix.
        '''
        self.ts_LineCount += 1
        if self.ts_LineCount <= self.ts_LastHeaderLine or \
           text == '\n':

            self.ts_File.write(text)

        else:

            self.ts_File.write('%s - %s' % (
                tsrpu.getDateTimeString(time.time()), text))

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
