#! /usr/bin/env python
#"Time-stamp: <05/31/2014  6:56:30 AM rsg>"
'''
tsWxMultiFrameEnv.py - Class to enable an application using a
Command Line Interface (CLI) to launch and use the same char-
acter-mode terminal with a Graphical-style User Interface (GUI).
It uses application specified configuration keyword-value pair
options to initialize any application specific logger(s)
It wraps the CLI, underlying the GUI, and the GUI with exception
handlers to control the exit codes and messages used to
coordinate other application programs.
'''
#################################################################
#
# File: tsWxMultiFrameEnv.py
#
# Purpose:
#
#    Class to enable an application using a Command Line Inter-
#    face (CLI) to launch and use the same character-mode term-
#    inal with a Graphical-style User Interface (GUI). It uses
#    application specified configuration keyword-value pair
#    options to initialize any application specific logger(s)
#    It wraps the CLI, underlying the GUI, and the GUI with
#    exception handlers to control the exit codes and messages
#    used to coordinate other application programs.
#
# Limitations:
#
#
# Notes:
#
#    None.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxMultiFrameEnv import MultiFrameEnv
#
#     ##  Generalized Form to Instantiate and Launch an application
#     ##  module that uses a Command Line Interface (CLI) to a
#     ##  character-mode terminal with optional logging.
#     ##
#     ##  Configuration options enable the CLI application to launch
#     ##  and use the same character-mode terminal with a Graphical-
#     ##  style User Interface (GUI).
#     ##
#     ##  See this File's header for examples of those application
#     ##  specific source code descriptions associated with
#     ##  parameter identifiers having double-underscore ("__")
#     ##  prefix and suffix.
#     ##
#     ##  See the test_tsWxWidgets.py File's header for examples of
#     ##  the gui application options.
#
#     myApp = MultiFrameEnv(
#         #######################################################
#         # All applications (with Command Line Interface or
#         # Graphical-style User Interface) begin with the following
#         # Command Line Interface Launch configuration item list:
#
#         buildTitle=__title__,
#         buildVersion=__version__,
#         buildDate=__date__,
#         buildAuthors=__authors__,
#         buildCopyright=__copyright__,
#         buildLicense=__license__,
#         buildCredits=__credits__,
#         buildTitleVersionDate=mainTitleVersionDate,
#         buildHeader=__header__,
#         buildPurpose=__doc__,
#
#         #######################################################
#
#         # Python version appropriate Command Line Interface
#         # module(s) may be enabled to obtain non-Application-
#         # specific Keyword-Value pair Options and Positional
#         # Arguments and associated command line help:
#
#         #     "argparse" module - introduced with Python 2.7.0
#         #     "optparse" module - introduced with Python 2.3.0
#         #     "getopt"   module - introduced with Python 1.6.0
#
#         enableDefaultCommandLineParser=False # Disable unless True
#
#         #######################################################
#
#         # When appropriate, some applications also use the following
#         # Graphical-style User Interface Launch configuration item list:
#
#         guiMessageFilename=None,
#         guiMessageRedirect=True,
#         guiRequired=True,
#         guiTopLevelObject=_Communicate,
#         guiTopLevelObjectId=-1,
#         guiTopLevelObjectName='Sample',
#         guiTopLevelObjectTitle='widgets_communicate',
#
#         #######################################################
#
#         # When customized logging is appropriate, some applica-
#         # tions use the following application-specific Launch
#         # configuration item:
#
#         logs=['1st-Non-Default', ..., 'Nth-Non-Default'],
#
#         # When basic logging is appropriate, some applications
#         # use the following non-application-specific Launch
#         # configuration item:
#
#         logs=[],
#
#         #######################################################
#
#         # All applications, with Command Line Interface or with
#         # both Command Line and Graphical-style User Interfaces,
#         # wrapup their Configuration item list as follows:
#
#         runTimeEntryPoint=main)
#
#         #######################################################
#
#     ## Launch via reference to appropriate Module Method
#     myApp.Wrapper()
#
# Methods:
#
#    __init__ - Initialize Command Line Interface run time environ-
#               ment configuration options and logger(s).
#
#    Wrapper  - Defines and invokes as application independent
#               exception handlers as appropriate to control
#               exit codes and messages.
#
# Modifications:
#
#    2011/12/08 rsg Included class TsApplication to eliminate
#                   need for "from tsApplication import
#                   TsApplication". This ought to facilitad
#                   customization of command line positional
#                   and keyword arguments within the internal
#                   CliAPP.getOptions method.
#
#    2013/02/28 rsg Added import tsLibGUI.
#
#    2013/03/31 rsg Added support for License and Credits.
#
#    2013/04/27 rsg Re-engineered "tsApplication" to become a base
#                   class, instead of a utility, for "tsCommand-
#                   LineEnv" so that the latter could become a base
#                   class for "tsWxMultiFrameEnv". This eliminated
#                   a substantial amount of library and application
#                   code replication.
#
#    2013/09/16 rsg Resolved circular dependency that trapped
#                   Python-3x but not Python-2x by replacing import
#                   of tsWx with:
#
#                   from tsWxApp import App as wxApp
#
#                   from tsWxGlobals import FrameNameStr as wxFrameNameStr
#
#                   from tsWxGlobals import DefaultPosition as
#                   wxDefaultPosition
#
#                   from tsWxGlobals import DefaultSize as wxDefaultSize
#
#                   from tsWxGlobals import DEFAULT_FRAME_STYLE as
#                   wxDEFAULT_FRAME_STYLE
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsWxMultiFrameEnv'
__version__   = '2.4.0'
__date__      = '09/16/2013'
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
    '\n\t\t\twxxWidgets team.' + \
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

#------------------------------------------------------------------------

import os.path
import sys
import time
import traceback

#--------------------------------------------------------------------------

##try:

##    import tsLibCLI

##except ImportError, importCode:

##    print('%s: ImportError (tsLibCLI); ' % __title__ + \
##          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    import tsLogger as Logger

    from tsApplication import TsApplication

    import tsOperatorSettingsParser

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsLibGUI

except ImportError as importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

##    import tsWx as wx # Invalid tsWx import because of circular dependency.
    from tsWxApp import App as wxApp
    from tsWxGlobals import FrameNameStr as wxFrameNameStr
    from tsWxGlobals import DefaultPosition as wxDefaultPosition
    from tsWxGlobals import DefaultSize as wxDefaultSize
    from tsWxGlobals import DEFAULT_FRAME_STYLE as wxDEFAULT_FRAME_STYLE

    MultiFrameEnvWrapperEnable = True

except Exception as exceptionCode:

    print('%s: Exception (tsLibGUI); ' % __title__ + \
          'exceptionCode=%s' % str(exceptionCode))

    MultiFrameEnvWrapperEnable = False

#------------------------------------------------------------------------

__help__ = '''
Append " -h" or " --help" to the command line before using the
"ENTER/RETURN" key.
'''

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

DebugSimulatedKeyErrorTrap = True

PySimpleAppMode = False # Set True only for Redirection, TaskBar and
                        # Single The Frame with no Dialogs

debugExitEnabled = False # True
frameSizingEnabled = True
redirectEnabled = True
runTimeTitleEnabled = True
splashScreenSeconds = 0
statusBarTestDrive = False
tracebackEnabled = False

#------------------------------------------------------------------------

class cliAPP(TsApplication):
    '''
    Class to enable an application using a Command Line Interface (CLI)
    to launch and use a character-mode terminal. It uses application
    specified configuration keyword-value pair options to initialize any
    application specific logger(s) It wraps the CLI with exception
    handlers to control the exit codes and messages used to coordinate
    other application programs.
    '''
    #--------------------------------------------------------------------
    # Begin Class Variables
    # End Class Variables
    #--------------------------------------------------------------------

    def __init__(self, *args, **kw):
        '''
        Class constructor.
        '''
        TsApplication.__init__(self, *args, **kw)

        # print(str(dir(self)))

    #-----------------------------------------------------------------------

    def guiModeLauncher(self):
        '''
        Get a wx App
        Build the communicate Frame
        Enter wx main loop
        '''
        print("Before guiLauncher")
        # self.guiMessageFilename      # GUI log filename when Redirected
        # self.guiMessageRedirect      # enables Redirected GUI log when True
        # self.guiRequired             # enables GUI-mode, if True
        # self.guiTopLevelObject       # wxPython-style GUI Object
        # self.guiTopLevelObjectId     # wxPython-style GUI Object Id
        # self.guiTopLevelObjectName   # wxPython-style GUI Object Name
        # self.guiTopLevelObjectParent # wxPython-style GUI Object Parent
        # self.guiTopLevelObjectPosition # wxPython-style GUI Object Position
        # self.guiTopLevelObjectSize   # wxPython-style GUI Object Size
        # self.guiTopLevelObjectStyle  # wxPython-style GUI Object Style
        # self.guiTopLevelObjectTitle  # wxPython-style GUI Object Title
        self.guiLauncher = wxApp(redirect=self.guiMessageRedirect,
                                 filename=self.guiMessageFilename)
        print("After guiLauncher")

        # Update undefined guiTopLevelObkect attributes
        # with appropriate wxPython defaults because
        # tsLibCLI lacked access to tsLibGUI definitions.
        #
        if True:

            if self.guiTopLevelObjectName is None:
                self.guiTopLevelObjectName = wxFrameNameStr
                self.logger.warning(
                    'Default for guiTopLevelObjectName is ' + \
                    '"%s"' % self.guiTopLevelObjectName)

            if self.guiTopLevelObjectPosition is None:
                self.guiTopLevelObjectPosition = wxDefaultPosition
                self.logger.warning(
                    'Default for guiTopLevelObjectPosition is ' + \
                    '"%s"' % str(self.guiTopLevelObjectPosition))

            if self.guiTopLevelObjectSize is None:
                self.guiTopLevelObjectSize = wxDefaultSize
                self.logger.warning(
                    'Default for guiTopLevelObjectSize is ' + \
                    '"%s"' % str(self.guiTopLevelObjectSize))

            if self.guiTopLevelObjectStyle is None:
                self.guiTopLevelObjectStyle = wxDEFAULT_FRAME_STYLE
                self.logger.warning(
                    'Default for guiTopLevelObjectStyle is ' + \
                    '"%s"' % str(self.guiTopLevelObjectStyle))

            if self.guiTopLevelObjectTitle is None:
                self.guiTopLevelObjectTitle = 'guiTopLevelObject'
                self.logger.warning(
                    'Default for guiTopLevelObjectTitle is ' + \
                    '"%s"' % self.guiTopLevelObjectTitle)

        self.guiLaunchFrame = self.guiTopLevelObject(
            self.guiTopLevelObjectParent,
            id=self.guiTopLevelObjectId,
            title=self.guiTopLevelObjectTitle,
            pos=self.guiTopLevelObjectPosition,
            size=self.guiTopLevelObjectSize,
            style=self.guiTopLevelObjectStyle,
            name=self.guiTopLevelObjectName
        )
        self.guiLaunchFrame.Show(True)

        if statusBarTestDrive:
            self.guiLauncher.theStatusBar = theStatusBar

        print("Before MainLoop")
        self.guiLauncher.MainLoop()
        print("After MainLoop")

##        theGUI = guiAPP(redirect=self.guiMessageRedirect,
##                      filename=self.guiMessageFilename)
##      try:

##          theGUI.OnInit()

####        if statusBarTestDrive:
####            theGUI.theStatusBar = theStatusBar

##          self.logger.debug("Before MainLoop")
##          theGUI.MainLoop()
##          self.logger.debug("After MainLoop")

##      except Exception:
##          theGUI.OnExit()

    #--------------------------------------------------------------------

    def Wrapper(self):
        '''
        Defines and invokes application independent exception handlers
        as appropriate to control exit codes and messages.
        '''
        # Verify user accessibility of one library known to be in hierarchy.
        try:

            preImportDevices = {'stdout': sys.stdout,
                                'stderr': sys.stderr,
                                ' stdin': sys.stdin}
            if DEBUG:
                msg = "tsCommandLineEnv: preImportDevices=%s" % \
                    preImportDevices
                self.logger.debug(msg)


        except Exception as preImportDevicesError:

            msg = "tsCommandLineEnv: %s" % preImportDevicesError
            raise tse.ProgramException(
                tse.APPLICATION_TRAP, msg)

        # Remember original stdout and stderr
        _stdout = sys.stdout
        _stderr = sys.stderr

        #------------------------------------------------------------------

        exitStatus = tse.NONERROR_ERROR_CODE
        msg = tse.NO_ERROR

        try:

            self.runTimeEntryPoint()
            self.guiModeLauncher()

        except tse.UserInterfaceException as userErrorCode:

            msg = 'EXCEPTION: tsMultiFrameEnv.cliWrapper: ' + \
                'userErrorCode="%s"' % str(userErrorCode)
            sys.stderr.write(msg)
##            if isinstance(applicationError, tse.TsExceptions):

##              self.runTimeEntryPoint()
##              self.guiModeLauncher()

##                msg = str(applicationError).replace("'", "")
##                tse.displayError(applicationError)
##                exitStatus = applicationError.exitCode

        except Exception as applicationError:

            if isinstance(applicationError, tse.TsExceptions):

                msg = str(applicationError).replace("'", "")
                tse.displayError(applicationError)
                exitStatus = applicationError.exitCode

            else:

                msg = None
                sys.stderr.write(traceback.format_exc())
                exitStatus = tse.INVALID_ERROR_CODE

        if msg == tse.NO_ERROR:
            sys.stdout.write(msg)
        elif msg is not None:
            sys.stderr.write(msg)

        # Return (exitStatus)
        sys.exit(exitStatus)

#------------------------------------------------------------------------

##class guiAPP(wxApp):
##    '''
##    Class to establish a graphical console user interface.
##    '''
##    def __init__(self,
##                 redirect=True,
##                 filename=None):
##        '''
##        '''
##        # self.guiMessageFilename      # GUI log filename when Redirected
##        # self.guiMessageRedirect      # enables Redirected GUI log when True
##        # self.guiRequired             # enables GUI-mode, if True
##        # self.guiTopLevelObject       # wxPython-style GUI Object
##        # self.guiTopLevelObjectId     # wxPython-style GUI Object Id
##        # self.guiTopLevelObjectName   # wxPython-style GUI Object Name
##        # self.guiTopLevelObjectParent # wxPython-style GUI Object Parent
##        # self.guiTopLevelObjectTitle  # wxPython-style GUI Object Title

##        wxApp.__init__(self,
##                       redirect=redirect,
##                       filename=filename)

##    #--------------------------------------------------------------------

##    def OnInit(self):
##        '''
##        This must be provided by the the, and will usually
##        create the the main window, optionally calling
##        {wxApp::SetTopWindow}. You may use {OnExit} to clean up
##        anything initialized here, provided that the function returns
##        true.

##        Notice that if you want to to use the command line processing
##        provided by wxWidgets you have to call the base class version
##        in the derived class OnInit().

##        Return true to continue processing, false to exit the
##        the immediately.
##        '''
##        self.logger.debug('\n\t\tguiAPP.OnInit')

##        theTopLevelObject = self.guiTopLevelObject
##        theParent = self.guiTopLevelObjectParent
##        theId = self.guiTopLevelObjectId
##        theTitle = self.guiTopLevelObjectTitle
##        theName = self.guiTopLevelObjectName

##        theFrame = theTopLevelObject(
##            theParent,
##            id=theId,
##            title=theTitle,
##            name=theName)
##        self.SetTopWindow(theFrame)

##        return (True)

##    #--------------------------------------------------------------------

##    def OnExit(self):
##        '''
##        Override this member function for any processing which needs
##        to be done as the GUI part of the application is about to exit.

##      OnExit is     called after destroying all the windows and controls,
##        but before wxWidgets cleanup. Note that it is not called at
##        all if {OnInit} failed.

##        The return value of this function is currently ignored,
##        return the same value as returned by the base class method
##        if you override it.
##        '''
##        self.logger.debug('\n\t\tguiAPP.OnExit')

    #--------------------------------------------------------------------

##    def Launcher(self):
##        '''
##        Launches and terminates the Graphical-style User Interface.
##        '''
##        self.logger.debug('\n\tguiAPP.ModeChanger')
##      try:
##          self.OnInit()
##      except Exception:
##          self.OnExit()

    #--------------------------------------------------------------------

##            # self.ModeChanger()
##          # self.guiMessageFilename  # GUI log filename when Redirected
##          # self.guiMessageRedirect  # enables Redirected GUI log when True
##          # self.guiRequired         # enables GUI-mode, if True
##          # self.guiTopLevelObject   # wxPython-style GUI Object
##          # self.guiTopLevelObjectId # wxPython-style GUI Object Id
##          # self.guiTopLevelObjectName   # wxPython-style GUI Object Name
##          # self.guiTopLevelObjectParent # wxPython-style GUI Object Parent
##          # self.guiTopLevelObjectTitle  # wxPython-style GUI Object Title
##            self.app = tsWxApp(redirect=self.guiMessageRedirect,
##                               filename=self.guiMessageFilename)

##          theTopLevelObject = self.guiTopLevelObject
##          theParent = self.guiTopLevelObjectParent
##          theId = self.guiTopLevelObjectId
##          theTitle = self.guiTopLevelObjectTitle
##          theName = self.guiTopLevelObjectName

##          theFrame = theTopLevelObject(
##              theParent,
##              id=theId,
##              title=theTitle,
##              name=theName)
##          self.app.SetTopWindow(theFrame)


####            if statusBarTestDrive:
####                app.theStatusBar = theStatusBar

##            print("Before MainLoop")
##            self.guiApp.MainLoop()
##            print("After MainLoop")

#------------------------------------------------------------------------

class MultiFrameEnv(cliAPP):
    '''
    Class to enable an application using a Command Line Interface (CLI)
    to launch and use the same character-mode terminal with a
    Graphical-style User Interface (GUI). It uses application specified
    configuration keyword-value pair options to initialize any
    application specific logger(s) It wraps the CLI, underlying the GUI,
    and the GUI with exception handlers to control the exit codes and
    messages used to coordinate other application programs.

    NOTE: tsWxMultiFrameEnv is a convenience package wrapping terminal
          keyboard & mouse input, field-editable video display output,
          tsLogger and tsException services.
    '''
    #--------------------------------------------------------------------
    # Begin Class Variables
    # End Class Variables
    #--------------------------------------------------------------------

    def __init__(self, *args, **kw):
        '''
        Class constructor.
        '''
        cliAPP.__init__(self, *args, **kw)

        # self.guiMessageFilename      # GUI log filename when Redirected
        # self.guiMessageRedirect      # enables Redirected GUI log when True
        # self.guiRequired             # enables GUI-mode, if True
        # self.guiTopLevelObject       # wxPython-style GUI Object
        # self.guiTopLevelObjectId     # wxPython-style GUI Object Id
        # self.guiTopLevelObjectName   # wxPython-style GUI Object Name
        # self.guiTopLevelObjectParent # wxPython-style GUI Object Parent
        # self.guiTopLevelObjectTitle  # wxPython-style GUI Object Title

##        if self.guiRequired:

##            guiAPP.__init__(self,
##                            redirect=self.guiMessageRedirect,
##                            filename=self.guiMessageFilename)

        if True and DEBUG:
            print(str(dir(self)))

#------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
