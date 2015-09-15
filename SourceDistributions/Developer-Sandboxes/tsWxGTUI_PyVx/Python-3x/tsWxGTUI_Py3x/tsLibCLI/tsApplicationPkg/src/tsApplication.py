#! /usr/bin/env python
#"Time-stamp: <09/14/2015  4:57:07 PM rsg>"
'''
tsApplication.py - Base class to initialize and configure the
application program launched by an operator. It enables an
application launched via a Command Line Interface (CLI) to
initialize, configure and use the same character-mode terminal
with a Graphical-style User Interface (GUI).
'''
#################################################################
#
# File: tsApplication.py
#
# Purpose:
#
#    Base class to initialize and configure the application
#    program launched by an operator. It enables an application
#    launched via a Command Line Interface (CLI) to initialize,
#    configure and use the same character-mode terminal with a
#    Graphical-style User Interface (GUI).
#
# Limitations:
#
#    1. tsApplication - Being a component of tsLibCLI, it may
#       import other components of tsLibCLI. However, to ensure
#       support for non-GUI application, it shall NOT import any
#       components of tsLibGUI. To facilitate the co-ordination
#       of a set of top-level application program processes, each
#       shall use any of the following means to report the appro-
#       priate exit codes and messages upon the application's
#       termination:
#
#       a) Launch CLI applications via tsCommandLineEnv module
#
#       b) Launch GUI applications via tsWxMultiFrameEnv module
#
#       c) Launch application via a customized version of either
#          two cited above.
#
#    2. enableDefaultCommandLineParser - Applications may provide an optional
#       method, via this invocation parameter, that shall return
#       a Python tuple (args, options). The positional arguments
#       ("args") shall be provided in a Python list format [a, b].
#       The keyword-value pairs ("options") shall be provides in a
#       Python dictionary format {'--file': 'sample.py'}. This
#       tuple-type interface shall be used regardless of the
#       enableDefaultCommandLineParser method's use of the following standard
#       Python library modues:
#
#       a) "argparse" (introduced with Python 2.7.0)
#
#       b) "optparse" (introduced with Python 2.3.0)
#
#       c) "getopts"  (introduced with Python 1.6.0)
#
# Notes:
#
#    1) "tsApplication" is a base class for launching the appli-
#        cation specified by an operator. It initializes and con-
#        figures the application using the following keyword
#        value pairs and positional arguments:
#
#        a) Input provided on the command line by an operator. The
#           command line uses a Unix-style, free-format to promote
#           future enhancement and on-going maintenance.
#
#        b) Input provided in the parameter list of the applica-
#           tion's invocation of the class instantiation. The par-
#           ameter list uses a Python-style free-format to promote
#           future enhancement and on-going maintenance.
#
#    2) "tsCommandlineEnv" is a convenience package wrapping term-
#       inal keyboard input, video display scrolled text output,
#       "tsLogger" and "tsException" services. It is a base class
#       for "tsWxMultiFrameEnv".
#
#    3) "tsWxMultiFrameEnv" is a convenience package wrapping
#       terminal keyboard & mouse input, video display row and
#       column addressable, field-editable output, "tsLogger"
#       and "tsException" services.
#
# Usage (example):
#
#     ## Add the following source code to the main application
#     ## program file.
#     ##
#     ## Note: The application is responsble for collecting,
#     ##       parsing and applying command line keyword-value
#     ##       pair options and positional arguments. The
#     ##       application is also responsible for wrapping
#     ##       itself with application-specific exception
#     ##       handlers that set exit codes and messages,
#     ##       upon termination, that may be used to coordinate
#     ##       the actions of other applications.
#
#     ## Import Module
#     import tsApplication as tsAPP
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
#----------------------------------------------------------------
#
#     ###########################################################
#
#     myApp = tsAPP.TsApplication(
#
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
#         guiTopLevelObjectId=wx.ID_ANY,
#         guiTopLevelObjectName='Sample',
#         guiTopLevelObjectParent=None,
#         guiTopLevelObjectPosition=wx.DefaultPosition,
#         guiTopLevelObjectSize=wx.DefaultSize,
#         guiTopLevelObjectStatusBar=None,
#         guiTopLevelObjectStyle=wx.DEFAULT_FRAME_STYLE,
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
#     ###########################################################
#
#     ## Simplest Form to Instantiate Module with only standard loggging
#     myApp = tsAPP.TsApplication(
#         buildTitle=__title__,
#         buildVersion=__version__,
#         buildDate=__date__,
#         buildTitleVersionDate=mainTitleVersionDate,
#         buildHeader=__header__,
#         buildPurpose=__doc__,
#         logs=[],
#         runTimeEntryPoint=main)
#
#     ###########################################################
#
#     ## Simplest Form to Instantiate Module with custom logging
#     myApp = tsAPP.TsApplication(
#         buildTitle=__title__,
#         buildVersion=__version__,
#         buildDate=__date__,
#         buildTitleVersionDate=mainTitleVersionDate,
#         buildHeader=__header__,
#         logs=['1st-Non-Default', '2nd-Non-Default', '3rd-Non-Default'],
#         runTimeEntryPoint=main)
#
#     ###########################################################
#
#     ## Launch via reference to appropriate Module Method
#     myApp.runMainApplication()
#
# Methods:
#
#    __init__ - TsApplication class constructor. Instantiates
#           class. It initializes default values for class state
#           variables. It registers and validates instantiation
#           settings input from application via caller parameter
#           list. It registers and validates operator application
#           settings inputs from command line keyword-value pairs
#           and positional arguments. Will update self.args and
#           self.options only if len(sys.argv) > 1 and if parsing
#           was successful.
#
#    callersExceptionHandler - Handle caller exception.
#
#    createLog - Capture title at run time. Create log file with
#           name derived from title, if it does not already exist.
#
#    getApp - Return application entry point.
#
#    getAssignedLogger - Return logger assigned by application.
#
#    getLaunchSettings - Return setting assigned by application
#           during it launch.
#
#    getLog - Return list of named loggers.
#
#    getRunTimeTitle - Return Run Time Title, or Build Title,
#           whichever was actually used in command line, strip-
#           ping it of any file path.
#
#    getRunTimeTitleVersionDate - Return the Build Title, Version
#           and Date (with any Run Time update) for use in command
#           line parsing help and error display output.
#
#    registerBuildAuthors - Register the authors of the module
#           source code.
#
#    registerBuildCopyright - Register the copyright notice for
#           the module source code.
#
#    registerBuildCredits - Register credits for third party
#           contributions to the module source code identifying
#           the technolgy or feature(s), applicable copyright
#           and licence.
#
#    registerBuildDate - Register the build month, day and year
#           of the module source code.
#
#    registerBuildHeader - Register the build header for the module
#           or construct one from the build title, version, date,
#           authors, copyright, license and credits.
#
#    registerBuildLicense - Register the build license for use and
#           distribution of the module source and executable code.
#
#    registerBuildPurpose - Register the build purpose of the module
#           source code.
#
#    registerBuildTitle - Register the build title of the module
#           source code.
#
#    registerBuildTitleVersionDate - Register Build Title, Version
#           and Date or construct it from available information.
#
#    registerBuildVersion - Register the build version of the module
#           source code.
#
#    registerGuiMessageFilename - Register GUI Message Log FileName.
#
#    registerGuiMessageRedirect - Register GUI Message Redirect flag.
#
#    registerGuiRequired - Register Graphical-style User Interface
#           (GUI) Required flag.
#
#    registerGuiTopLevelObject - Register GUI Top Level (Frame or
#           Dialog) Object.
#
#    registerGuiTopLevelObjectId - Register GUI Top Level (Frame
#           or Dialog) Object ID.
#
#    registerGuiTopLevelObjectName - Register GUI Top Level
#           (Frame or Dialog) Object Name.
#
#    registerGuiTopLevelObjectParent - Register GUI Top Level
#           Object (Modal Dialog) Parent (Frame).
#
#    registerGuiTopLevelObjectPosition - Register GUI Top Level
#           Object Position.
#
#    registerGuiTopLevelObjectSize - Register GUI Top Level
#           Object Size.
#
#    registerGuiTopLevelObjectStatusBar - Register GUI Top Level
#           Object Status Bar.
#
#    registerGuiTopLevelObjectStyle - Register GUI Top Level
#           Object Style.
#
#    registerGuiTopLevelObjectTitle - Register GUI Top Level
#           (Frame or Dialog) Object Title.
#
#    registerInstantiationSettings - Register Instantiation
#           Settings consisting of keyword-value pair options
#           and positonal arguments.
#
#    registerLogs - Register list of application specified log
#           files, Unix-style devices (syslog, stderr, stdout)
#           or nCurses-style device (stdscr).
#
#    registerOperatorSettings - Register command line keyword
#           options and positional arguments. Will update
#           self.args and self.options only if len(sys.argv) > 1
#           and if parsing was successful.
#
#    registerRunTimeEntryPoint - Register run time entry point
#           (e.g. "main").
#
#    runMainApplication - Initiate the application and generate
#           the appropriate exit code and message upon its term-
#           ination.
#
#    runTimeTrap - Trap unresolved "runTimeEntryPoint" KeyError
#           and AttributeError for Pylint.
#
#    resizeConsoleDisplay - Resize the Console Display if is
#           smaller than the minimum.
#
# Modifications:
#
#    2008/06/08 rsg Added comments depicting usage of "logs"
#                   keyword argument.
#
#    2013/04/07 rsg Added application launch parameter support
#                   for authors, copyright, license and credits.
#
#    2013/04/08 rsg Added GUI application launch parameter support
#                   for guiRequired, guiTopLevelObjectId,
#                   guiMessageRedirect, guiMessageFilename,
#                   guiTopLevelObject, guiTopLevelObjectName and
#                   guiTopLevelObjectTitle.
#
#    2013/04/10 rsg Added support for invocation of application
#                   supplied getOptions method since the application
#                   establishes requirements for any keyword options
#                   and positional arguments found on the command line.
#
#    2013/04/12 rsg Added getOptionsStub to be used when application
#                   defines no getOptions method. It returns a tupple
#                   containing an empty dictionary of keyword named
#                   options and an empty list of positional arguments.
#
#    2013/04/16 rsg Warn use of deprecated getOptions.
#
#    2013/04/18 rsg Remove import of tsOptionParser. Remove getOptions,
#                   getOptionsStub and getOptionsTest.
#
#    2013/04/22 rsg Restructuring of __init__ method into multiple
#                   register methods in order to reduce overall
#                   complexity
#
#    2013/04/24 rsg Added import of argparse and optparse. Replaced
#                   references to getOptions by references to
#                   parseCommandLine. Restored and updated
#                   parseCommandLine, parseCommandLineStub and
#                   parseCommandLineTest to support argtparse,
#                   getopt and optparse.
#
#    2013/04/27 rsg Re-engineered "tsApplication" to become a base
#                   class, instead of a utility, for "tsCommand-
#                   LineEnv" so that the latter could become a base
#                   class for "tsWxMultiFrameEnv". This eliminated
#                   a substantial amount of library and application
#                   code replication.
#
#    2013/04/30 rsg Modified parseCommandLineStub to return default
#                   empty values for args and options upon stub
#                   error trap.
#
#    2013/05/12 rsg Added inherited base class tsCommandLineParser
#                   after extracting the associated source code and
#                   documentation from tsApplication. The intent
#                   is to use an inheritable base class that
#                   eliminates code duplication and simplifies/
#                   modularizes the overal product.
#
#    2013/05/14 rsg Added properties and eliminated @staticmethod
#                   decorator in order to facilitate access to
#                   class methods.
#
#    2013/05/16 rsg Elimitated use of parseCommandLine to select
#                   default (tsCommandLineParser) class when value
#                   was None, or application-specified parser
#                   [class method(s) or static method(s)].
#                   Unresolved issue was inability to invoke
#                   parser method(s) with the appropriate
#                   aruments (i.e., class instance type
#                   exceptions).
#
#    2013/05/16 rsg Removed refrences to tsCommandLineParser
#                   because application must define and invoke
#                   its own command line parser. Otherwise
#                   there are unresolvable conflicts between
#                   overlaid parsing methods of the same name.
#
#    2013/05/30 rsg Added registerGuiTopLevelObjectStatusBar,
#                   as reminder for a feature that must be
#                   aligned, at run time with the Top Level
#                   GUI Object. TBD - Don't yet know how to
#                   make this work.
#
#    2013/06/01 rsg Added support for tsOperatorSettingsParser.
#
#    2013/06/03 rsg Added support for guiTopLevelObjectPosition,
#                   guiTopLevelObjectSize and guiTopLevelObjectStyle.
#
#    2013/06/11 rsg Added missing registration of buildHeader,
#                   buildPurpose and buildTitleVarsionDate
#
#    2013/06/12 rsg Add getLaunchSettings method.
#
#    2015/09/14 rsg Add resizeConsoleDisplay method to resize
#                   the console only if it smaller than the
#                   tsMinimumDisplaySize now specified in
#                   tsCxGlobals. The intent is relieve the
#                   operator of guessing at the proper size
#                   to avoid application traps upon launch.
#
# ToDo:
#
#    2013/05/30 rsg Revise design to eliminate need for
#                   registerGuiTopLevelObjectStatusBar. Perhaps
#                   the design can adjust the frame size to
#                   include the status bar rather than append
#                   it as a separate object.
#
#################################################################

__title__     = 'tsApplication'
__version__   = '2.8.0'
__date__      = '09/14/2015'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if ((len(__credits__) == 0)):
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

## import platform
## import traceback
import os.path
import sys
import time

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    from tsCxGlobals import ThemeCxPython
    from tsCxGlobals import ThemeToUse
    import tsExceptions as tse
    import tsLogger
    # from tsCommandLineParser import TsCommandLineParser

    from tsPlatformRunTimeEnvironment import PlatformRunTimeEnvironment

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

if True:

    myOutputPath = os.path.join(
        tsLogger.TsLogger.defaultStandardOutputPath,
        'PlatformRunTimeEnvironment.log')
    myRunTimeEnvironment = PlatformRunTimeEnvironment()
    myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

#--------------------------------------------------------------------------

Troubleshooting = ThemeToUse['Troubleshooting']

Debug_CLI_Configuration = Troubleshooting['Debug_CLI_Configuration'],
Debug_CLI_Exceptions = Troubleshooting['Debug_CLI_Exceptions']
Debug_CLI_Launch = Troubleshooting['Debug_CLI_Launch']
Debug_CLI_Progress = Troubleshooting['Debug_CLI_Progress']
Debug_CLI_Termination = Troubleshooting['Debug_CLI_Termination']
Debug_GUI_Configuration = Troubleshooting['Debug_GUI_Configuration']
Debug_GUI_Exceptions = Troubleshooting['Debug_GUI_Exceptions']
Debug_GUI_Launch = Troubleshooting['Debug_GUI_Launch']
Debug_GUI_Progress = Troubleshooting['Debug_GUI_Progress']
Debug_GUI_Termination = Troubleshooting['Debug_GUI_Termination']

EnableParseCommandLine = True
EnableParseCommandLineWarning = True
EnableOptionsGNU = True

IgnoreOperatorSettings = True

StripPathFromRunTimeTitle = True # Strip any path from sys.argv[0]

KeyValueUndefinedTrap = True

DEBUG = False
DebugKeyValueUndefined = False
DebugSimulatedKeyErrorTrap = False

#--------------------------------------------------------------------------

class TsApplication(object):
    '''
    Base class to initialize and configure the application program
    launched by an operator. Its configuration supports those
    keyword-value pair options and positional arguments specified
    by the application, in its invocation parameter list. It validates
    the keyword-value pair options and positional arguments. It enables
    an application launched via a Command Line Interface (CLI) to
    initialize, configure and use the same character-mode terminal with
    a Graphical-style User Interface (GUI).
    '''

    #----------------------------------------------------------------------

    # Class Instance Variables
    _App = None
    _Logs = {}
    _TheAsignedLogger = None

    #----------------------------------------------------------------------
 
    def __init__(self, *args, **kw):
        '''
        Class constructor.
        '''
        #------------------------------------------------------------------

        # Remember class instance for global use by static methods
        TsApplication._App = self # class instance variable

        # Remember command line settings inputs from operator
        self.sysArgv = sys.argv # system provided command line arguments

        # Remember application settings inputs from caller parameter list
        self.tsAppArgs = args # class instantiation positional argument list
        self.tsAppKw = kw # class instantiation keyword value pair option dict.

        #------------------------------------------------------------------

        # Initialize inherited base class
        # TsCommandLineParser.__init__(self)

        self.resizeConsoleDisplay()

        #------------------------------------------------------------------

        # Initialize default values for class state variables.
        self.applicationStyle = mainTitleVersionDate # Title, Version, Date
        self.currentTime = time.time() # current application date & time
        self.shutdownTime = self.currentTime # default startup date & time
        self.startupTime = self.currentTime # default shutdown date & time

        self.args = None # command line positional argument list
        self.options = None # command line keyword value pair option dict.

        self.buildTitle = None # module name (without file extension)
        self.buildVersion = None # latest module edit version x.y.z
        self.buildDate = None # latest module edit day/month/year
        self.buildAuthors = None # name of module creator(s) and maintainer(s)
        self.buildCopyright = None # copyright year, owner(s) name and rights
        self.buildLicense = None # terms & conditions for module use
        self.buildCredits = None # contributor role, name, copyright & license
        self.buildTitleVersionDate = None # caption: Title, Version, Date
        self.buildHeader = None # application startup banner
        self.buildPurpose = None # application usage purpose (from doc string)

        self.enableDefaultCommandLineParser = False # Disable unless True

        self.guiMessageFilename = None # GUI log filename when Redirected
        self.guiMessageRedirect = None # enables Redirected GUI log when True
        self.guiRequired = None # disables GUI-type application unless True
        self.guiTopLevelObject = None # wxPython-style GUI Object
        self.guiTopLevelObjectId = None # wxPython-style GUI Object Id
        self.guiTopLevelObjectName = None # wxPython-style GUI Object Name
        self.guiTopLevelObjectParent = None # wxPython-style GUI Object Parent
        self.guiTopLevelObjectPosition = None # wxPython-style GUI Object Pos
        self.guiTopLevelObjectSize = None # wxPython-style GUI Object Size
        self.guiTopLevelObjectStatusBar = None # wxPython-style GUI Object
                                               # Status Bar
        self.guiTopLevelObjectStyle = None # wxPython-style GUI Object Style
        self.guiTopLevelObjectTitle = None # wxPython-style GUI Object Title
        #
        self.logs=[] # list of command line log devices / filenames
                     # [] or [' '] defaults to runtime (or module) name.log

        self.logger = None # connection to event message output device/file
        #
        # Run Time Title, or Build Title, whichever was actually used
        # in command line.
        self.runTimeEntryPoint = None # application Python entry point
        self.runTimeTitle = None # Base name of file invoked by operator.
        self.runTimeTitleVersionDate = None # one-line build identifier

        #------------------------------------------------------------------

        # Register and validate class instantiation settings input from
        # application via caller parameter list
        self.registerInstantiationSettings()

        # Register and validate operator application settings inputs from
        # command line keyword-value pairs and positional arguments. Will
        # update self.args and self.options only if len(sys.argv) > 1 and
        # if parsing was successful.
        # self.registerOperatorSettings()

    #----------------------------------------------------------------------

    def callersExceptionHandler(self, callersException):
        '''
        Handle caller exception.
        '''
        return (0, 'Test msg "%s".' % callersException)

    #----------------------------------------------------------------------
 
    def createLog(self, logName=tsLogger.StandardOutputFile):
        '''
        Capture title at run time. Create log file with name derived from
        title, if it does not already exist.
        '''
        if StripPathFromRunTimeTitle:

            if logName == tsLogger.StandardOutputFile:

                # Capture Title at run time.
                argv = sys.argv
                (head, tail) = os.path.split(argv[0])
                (fileName, fileExt) = os.path.splitext(tail)

            else:

                # Strip off caller specified path and extension
                (head, tail) = os.path.split(logName)
                (fileName, fileExt) = os.path.splitext(tail)

            name = logName
            longName = '%s.log' % fileName

        else:

            # Capture Title at run time.
            argv = sys.argv
            (head, tail) = os.path.split(argv[0])
            (fileName, fileExt) = os.path.splitext(tail)

            if fileName == self.buildTitle:

                # Use programmer specified name
                prefix = '%s' % self.buildTitle

            else:

                # Use operator specified name - operator renamed executable.
                prefix = '%s' % fileName

            # Does log already exist?
            try:
                x = tsLogger.TsLogger.activeLoggerIDs[logName]
                # Is it the DummyLogger?
                if isinstance(x, tsLogger.TsLogger):
                    raise tse.ProgramException(
                        tse.ARGUMENT_KEY_NOT_VALID,
                        'Log named "%s" already exists' % logName)
            except KeyError:
                pass

            if logName == tsLogger.StandardOutputFile:
                # Create the default log
                name = '%s' % prefix
            else:
                # Create a non default log
                name = '%s_%s' % (prefix, logName)

            longName = '%s.log' % name

        theLogger = tsLogger.TsLogger(threshold=tsLogger.DEBUG,
                                      start=time.time(),
                                      name=longName)

        if DEBUG:

            fmt1 = 'tsApplication.createLog:'
            fmt2 = '(head, tail) = %s' % (
                str((head, tail)))
            fmt3 = '(fileName, fileExt) = %s' % (
                str((fileName, fileExt)))
            msg = '\n\t%s\n\n\t\t%s\n\n\t\t%s' % (fmt1, fmt2, fmt3)
            self.logger.debug(msg)

            theLogger.info('Startup of <%s>.' % name)
            theLogger.info('Log Name is <%s>.' % longName)

##        if True or DEBUG:

##            myOutputPath = os.path.join(
##                tsLogger.TsLogger.defaultStandardOutputPath,
##                'PlatformRunTimeEnvironment.log')
##            myRunTimeEnvironment = PlatformRunTimeEnvironment()
##            myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

        return (theLogger)

    #----------------------------------------------------------------------

    # @staticmethod
    def getApp(self):
        '''
        Return class instance for the invoking application.
        '''
        return (self)

    #----------------------------------------------------------------------

    def getAssignedLogger(self):
        '''
        Return logger assigned by application.
        '''
        return (self.logger)

    #----------------------------------------------------------------------

    def getLaunchSettings(self):
        '''
        Return setting assigned by application during it launch.
        '''
        args = []
        options = {
            'buildTitle': self.buildTitle,
            'buildVersion': self.buildVersion,
            'buildDate': self.buildDate,
            'buildAuthors': self.buildAuthors,
            'buildCopyright': self.buildCopyright,
            'buildLicense': self.buildLicense,
            'buildCredits': self.buildCredits,
            'buildTitleVersionDate': self.buildTitleVersionDate,
            'buildHeader': self.buildHeader,
            'buildPurpose': self.buildPurpose
            }

        if True or DEBUG:
            print('\n\nTsApplication.getLaunchSettings\n')
            print('args=\n\t%s\n' % str(args))
            print('options=\n\t%s\n' % str(options))
            print('buildTitle=\n\t%s\n' % options['buildTitle'])
            print('buildVersion=\n\t%s\n' % options['buildVersion'])
            print('buildDate=\n\t%s\n' % options['buildDate'])
            print('buildAuthors=\n\t%s\n' % options['buildAuthors'])
            print('buildCopyright=\n\t%s\n' % options['buildCopyright'])
            print('buildLicense=\n\t%s\n' % options['buildLicense'])
            print('buildCredits=\n\t%s\n' % options['buildCredits'])
            print('buildTitleVersionDate=\n\t%s\n' % \
                  options['buildTitleVersionDate'])
            print('buildHeader=\n\t%s\n' % options['buildHeader'])
            print('buildPurpose=\n\t%s\n' % options['buildPurpose'])

        return (args, options)

    #----------------------------------------------------------------------

    def getLog(self, logName=tsLogger.StandardOutputFile):
        '''
        Return list of named loggers.
        '''
        try:

            reply = TsApplication._Logs[logName]

        except KeyError:

            try:

                reply = self.createLog(logName=logName)

            except Exception as e:

                reply = None
                msg = 'tsApplication.getLog: Exception=<%s>.' % str(e)
                self.logger.error(msg)
                raise tse.ProgramException(tse.ARGUMENT_KEY_NOT_VALID, msg)

        return (reply)

    #----------------------------------------------------------------------

    def getRunTimeTitle(self):
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        # Capture Command Line Arguments.
        argv = sys.argv

        # Separate File Path from its associated File Name and Extension
        (filePath, fileNameExt) = os.path.split(argv[0])

        # Separate File Name from its associated Extension
        (fileName, fileExt) = os.path.splitext(fileNameExt)

        if DEBUG:

            fmt1 = 'tsApplication.getRunTimeTitle:'
            fmt2 = '(filePath, fileNameExt)) = %s' % (
                str((filePath, fileNameExt)))
            fmt3 = '(fileName, fileExt) = %s' % (
                str(((fileName, fileExt))))
            msg = '\n\t%s\n\n\t\t%s\n\n\t\t%s' % (fmt1, fmt2, fmt3)
            self.logger.debug(msg)

        self.runTimeTitle = fileName
        return (self.runTimeTitle)

    #------------------------------------------------------------------

    def getRunTimeTitleVersionDate(self):
        '''
        Return the Build Title, Version and Date (with any Run Time update)
        for use in command line parsing help and error display output.
        '''
        self.runTimeTitle = self.getRunTimeTitle()
        if self.runTimeTitle == self.buildTitle:

            self.runTimeTitleVersionDate = self.buildTitleVersionDate

        else:

            self.runTimeTitleVersionDate = '%s, v%s (build %s)' % (
                self.runTimeTitle, self.buildVersion, self.buildDate)

        return (self.runTimeTitleVersionDate)

    #----------------------------------------------------------------------

    def registerBuildAuthors(self):
        '''
        Register the authors of the module source code. For example:
        "Frederick A. Kier & Richard S. Gordon".
        '''
        try:
            self.buildAuthors = self.tsAppKw['buildAuthors']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildAuthors" = <"%s">.' % str(self.buildAuthors))
        except KeyError:
            self.buildAuthors = ''
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildAuthors" not defined, ' + \
                'using <"%s">' % str(self.buildAuthors))

    #----------------------------------------------------------------------

    def registerBuildCopyright(self):
        '''
        Register the copyright notice for the module source code. For
        example:
        "Copyright (c) 2007-2013. All rights reserved.".
        '''
        try:
            self.buildCopyright = self.tsAppKw['buildCopyright']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildCopyright" = <"%s">.' % str(self.buildCopyright))
        except KeyError:
            self.buildCopyright = ''
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildCopyright" not defined, ' + \
                'using <"%s">' % str(self.buildCopyright))

    #----------------------------------------------------------------------

    def registerBuildCredits(self):
        '''
        Register credits for third party contributions to the module
        source code identifying the technolgy or feature(s), applic-
        able copyright and licence. For example:
        "
        Credits:

                tsLibCLI Import & Application Launch Features:
                Copyright (c) 2007-2009 Frederick A. Kier.
                              All rights reserved.

        "
        '''
        try:
            self.buildCredits = self.tsAppKw['buildCredits']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildCredits" = <"%s">.' % str(self.buildCredits))
        except KeyError:
            self.buildCredits = ''
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildCredits" not defined, ' + \
                'using <"%s">' % str(self.buildCredits))

    #----------------------------------------------------------------------

    def registerBuildDate(self):
        '''
        Register the build month, day and year of the module source code.
        For example:
        "04/22/2013".
        '''
        try:
            self.buildDate = self.tsAppKw['buildDate']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildDate" = <"%s">.' % str(self.buildDate))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found.' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                self.buildDate = __date__
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "buildDate" = <"%s">.' % str(self.buildDate))

    #----------------------------------------------------------------------

    def registerBuildHeader(self):
        '''
        Register the build header for the module or construct one from
        the build title, version, date, authors, copyright, license
        and credits. For example,
        "

        test_tsApplication, v1.5.0 (build 04/18/2013)

          Author(s): Frederick A. Kier & Richard S. Gordon
          Copyright (c) 2007-2013 Frederick A. Kier & Richard S. Gordon.
                        All rights reserved.
          GNU General Public License, Version 3, 29 June 2007

          Credits:

                  tsLibCLI Import & Application Launch Features:
                  Copyright (c) 2007-2009 Frederick A. Kier.
                                All rights reserved.
        "
        '''
        try:
            self.buildHeader = self.tsAppKw['buildHeader']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildHeader" = <"%s">.' % str(self.buildHeader))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                kwLine1 = '%s, v%s (build %s)' % (self.buildTitle,
                                                  self.buildVersion,
                                                  self.buildDate)
                kwLine2 = 'Author(s): %s' % self.buildAuthors
                kwLine3 = '%s' % self.buildCopyright

                if len(self.buildCredits) == 0:
                    kwLine4 = '%s' % self.buildLicense
                else:
                    kwLine4 = '%s%s' % (self.buildLicense, self.buildCredits)

                self.buildHeader = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (kwLine1,
                                                                     kwLine2,
                                                                     kwLine3,
                                                                     kwLine4)
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDerived "buildHeader" = <"%s">.' % str(
                        self.buildHeader))

    #----------------------------------------------------------------------

    def registerBuildLicense(self):
        '''
        Register the build license for use and distribution of the module
        source and executable code. For example:
        "GNU General Public License,  Version 3, 29 June 2007".
        '''
        try:
            self.buildLicense = self.tsAppKw['buildLicense']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildLicense" = <"%s">.' % str(self.buildLicense))
        except KeyError:
            self.buildLicense = ''
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"license" not defined, ' + \
                'using <"%s">' % str(self.buildLicense))

    #----------------------------------------------------------------------

    def registerBuildPurpose(self):
        '''
        Register the build purpose of the module source code. For example:
        "tsApplication".
        '''
        try:
            self.buildPurpose = self.tsAppKw['buildPurpose']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildPurpose" = <"%s">.' % str(self.buildPurpose))
        except KeyError:
            self.buildPurpose = ''
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"purpose" not defined, ' + \
                'using <"%s">' % str(self.buildPurpose))

    #----------------------------------------------------------------------

    def registerBuildTitle(self):
        '''
        Register the build title of the module source code. For example:
        "tsApplication".
        '''
        try:
            self.buildTitle = self.tsAppKw['buildTitle']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildTitle" = <"%s">.' % str(self.buildTitle))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found.' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                self.buildTitle = __title__
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "buildTitle" = <"%s">.' % str(
                        self.buildTitle))

    #----------------------------------------------------------------------

    def registerBuildTitleVersionDate(self):
        '''
        Register Build Title, Version and Date or construct it from available
        information. For example:
        "tsApplication, v1.5.0 (build 04/18/2013)"
        '''
        try:
            self.buildTitleVersionDate = self.tsAppKw['buildTitleVersionDate']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildTitleVersionDate" = ' + \
                '<"%s">.' % self.buildTitleVersionDate)
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found.' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                self.buildTitleVersionDate = '%s, v%s (build %s)' % (
                    self.buildTitle,
                    self.buildVersion,
                    self.buildDate)

    #----------------------------------------------------------------------

    def registerBuildVersion(self):
        '''
        Register the build version of the module source code. For example:
        "1.7.0".
        '''
        try:
            self.buildVersion = self.tsAppKw['buildVersion']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"buildVersion" = <"%s">.' % str(self.buildVersion))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found.' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                self.buildVersion = __version__
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "buildVersion" = <"%s">.' % str(
                        self.buildVersion))

    #----------------------------------------------------------------------

    def registerGuiMessageFilename(self):
        '''
        Register GUI Message Log FileName.
        '''
        try:
            self.guiMessageFilename = self.tsAppKw['guiMessageFilename']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiMessageFilename" = <"%s">.' % str(
                    self.guiMessageFilename))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiMessageFilename = 'guiMessageFilename'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiMessageFilename" = <"%s">.' % str(
                        self.guiMessageFilename))

    #----------------------------------------------------------------------

    def registerGuiMessageRedirect(self):
        '''
        Register GUI Message Redirect flag.
        '''
        try:
            self.guiMessageRedirect = self.tsAppKw['guiMessageRedirect']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiMessageRedirect" = ' + \
                '<"%s">.' % self.guiMessageRedirect)
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiMessageRedirect = 'guiMessageRedirect'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiMessageRedirect" = <"%s">.' % str(
                        self.guiMessageRedirect))

    #----------------------------------------------------------------------

    def registerGuiRequired(self):
        '''
        Register Graphical-style User Interface (GUI) Required flag.
        '''
        try:
            self.guiRequired = self.tsAppKw['guiRequired']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiRequired" = <"%s">.' % str(
                    self.guiRequired))

        except KeyError:
            self.guiRequired = False
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '"guiRequired" not found, ' + \
                'using <"%s">' % str(self.guiRequired))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObject(self):
        '''
        Register GUI Top Level (Frame or Dialog) Object.
        '''
        try:
            self.guiTopLevelObject = self.tsAppKw['guiTopLevelObject']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObject" = <"%s">.' % str(
                    self.guiTopLevelObject))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObject = 'guiTopLevelObject'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObject" = <"%s">.' % str(
                        self.guiTopLevelObject))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectId(self):
        '''
        Register GUI Top Level (Frame or Dialog) Object ID.
        '''
        try:
            self.guiTopLevelObjectId = self.tsAppKw['guiTopLevelObjectId']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectId" = <"%s">.' % str(
                    self.guiTopLevelObjectId))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectId = 'guiTopLevelObjectId'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectId" = <"%s">.' % str(
                        self.guiTopLevelObjectId))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectName(self):
        '''
        Register GUI Top Level (Frame or Dialog) Object Name.
        '''
        try:
            self.guiTopLevelObjectName = self.tsAppKw['guiTopLevelObjectName']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectName" = <"%s">.' % str(
                    self.guiTopLevelObjectName))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectName = 'guiTopLevelObjectName'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectName" = <"%s">.' % str(
                        self.guiTopLevelObjectName))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectParent(self):
        '''
        Register GUI Top Level Object (Modal Dialog) Parent (Frame).
        '''
        try:
            self.guiTopLevelObjectParent = self.tsAppKw[
                'guiTopLevelObjectParent']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectParent" = <"%s">.' % str(
                    self.guiTopLevelObjectParent))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectParent = 'guiTopLevelObjectParent'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectParent" = <"%s">.' % str(
                        self.guiTopLevelObjectParent))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectPosition(self):
        '''
        Register GUI Top Level Object Position (Frame).
        '''
        try:
            self.guiTopLevelObjectPosition = self.tsAppKw[
                'guiTopLevelObjectPosition']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectPosition" = <"%s">.' % str(
                    self.guiTopLevelObjectPosition))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectPosition = 'guiTopLevelObjectPosition'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectPosition" = <"%s">.' % str(
                        self.guiTopLevelObjectPosition))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectSize(self):
        '''
        Register GUI Top Level Object Size (Frame).
        '''
        try:
            self.guiTopLevelObjectSize = self.tsAppKw[
                'guiTopLevelObjectSize']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectSize" = <"%s">.' % str(
                    self.guiTopLevelObjectSize))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectSize = 'guiTopLevelObjectSize'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectSize" = <"%s">.' % str(
                        self.guiTopLevelObjectSize))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectStatusBar(self):
        '''
        Register GUI Top Level Object Status Bar.
        '''
        try:
            self.guiTopLevelObjectStatusBar = self.tsAppKw[
                'guiTopLevelObjectStatusBar']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectStatusBar" = <"%s">.' % str(
                    self.guiTopLevelObjectStatusBar))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectStatusBar = 'guiTopLevelObjectStatusBar'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectStatusBar" = <"%s">.' % str(
                        self.guiTopLevelObjectStatusBar))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectStyle(self):
        '''
        Register GUI Top Level Object Style (Frame).
        '''
        try:
            self.guiTopLevelObjectStyle = self.tsAppKw[
                'guiTopLevelObjectStyle']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectStyle" = <"%s">.' % str(
                    self.guiTopLevelObjectStyle))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectStyle = 'guiTopLevelObjectStyle'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectStyle" = <"%s">.' % str(
                        self.guiTopLevelObjectStyle))

    #----------------------------------------------------------------------

    def registerGuiTopLevelObjectTitle(self):
        '''
        Register GUI Top Level (Frame or Dialog) Object Title.
        '''
        try:
            self.guiTopLevelObjectTitle = self.tsAppKw[
                'guiTopLevelObjectTitle']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"guiTopLevelObjectTitle" = <"%s">.' % str(
                    self.guiTopLevelObjectTitle))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(
                        requiredKeyError))
            else:
                self.guiTopLevelObjectTitle = 'guiTopLevelObjectTitle'
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDummy "guiTopLevelObjectTitle" = <"%s">.' % str(
                        self.guiTopLevelObjectTitle))

    #----------------------------------------------------------------------

    def registerInstantiationSettings(self):
        '''
        Register Instantiation Settings consisting of keyword-value pair
        options and positonal arguments.
        '''
        self.runTimeTitle = self.getRunTimeTitle()

        self.registerLogs()

        # Begin Required Parameters for Run Time Identification
        self.registerBuildTitle()
        self.registerBuildVersion()
        self.registerBuildDate()
        # End Required Parameters for Run Time Identification

        # Begin Optional Parameters for Copyright Notification
        self.registerBuildAuthors()
        self.registerBuildCopyright()
        self.registerBuildLicense()
        self.registerBuildCredits()
        self.registerBuildTitleVersionDate()
        self.registerBuildHeader()
        self.registerBuildPurpose()
        # End Optional Parameters for Copyright Notification

        # Begin Required Parameters for Command Line Application Launch
        self.registerRunTimeEntryPoint()
        # self.registerCliApplicationOptionParser()
        # End Required Parameters for Command Line Application Launch

        # Begin Optional Parameters for
        # Graphical User Interface Application Launch
        self.registerGuiRequired()

        if self.guiRequired:

            # Begin Required Parameters for
            # Graphical User Interface Application Launch
            self.registerGuiTopLevelObjectId()
            self.registerGuiMessageRedirect()
            self.registerGuiMessageFilename()
            self.registerGuiTopLevelObject()
            self.registerGuiTopLevelObjectName()
            self.registerGuiTopLevelObjectParent()
            self.registerGuiTopLevelObjectPosition()
            self.registerGuiTopLevelObjectSize()
            self.registerGuiTopLevelObjectStatusBar()
            self.registerGuiTopLevelObjectStyle()
            self.registerGuiTopLevelObjectTitle()
            # End Required Parameters for
            # Graphical User Interface Application Launch

        # End Optional Parameters for
        # Graphical User Interface Application Launch

        # Begin Required or Derived Parameters for
        # Run Time Identification
        self.registerBuildTitleVersionDate()
        self.registerBuildHeader()
        self.registerRunTimeEntryPoint()
        # End Required or Derived Parameters for
        # Run Time Identification

        if DEBUG:
            print('sysArgv=%s' % \
                  str(self.sysArgv))
            print('buildTitle=%s' % \
                  self.buildTitle)
            print('buildVersion=%s' % \
                  self.buildVersion)
            print('buildDate=%s' % \
                  self.buildDate)
            print('buildAuthors=%s' % \
                  self.buildAuthors)
            print('buildCopyright=%s' % \
                  self.buildCopyright)
            print('buildLicense=%s' %
                  self.buildLicense)
            print('buildTitleVersionDate=%s' % \
                  self.buildTitleVersionDate)
            print('buildHeader=%s' % \
                  self.buildHeader)
            print('enableDefaultCommandLineParser=%s' % \
                  self.enableDefaultCommandLineParser)

            if self.guiRequired:

                print('guiMessageFilename=%s' % \
                      self.guiMessageFilename)
                print('guiMessageRedirect=%s' % \
                      self.guiMessageRedirect)
                print('guiTopLevelObject=%s' % \
                      str(self.guiTopLevelObject))
                print('guiTopLevelObjectId=%s' % \
                      self.guiTopLevelObjectId)
                print('guiTopLevelObjectName=%s' % \
                      self.guiTopLevelObjectName)
                print('guiTopLevelObjectParent=%s' % \
                      self.guiTopLevelObjectParent)
                print('guiTopLevelObjectTitle=%s' % \
                      self.guiTopLevelObjectTitle)
            print('logs=%s' % \
                  str(self.logs))
            print('runTimeTitle=%s' % \
                  self.runTimeTitle)
            print('runTimeEntryPoint=%s' % \
                  str(self.runTimeEntryPoint))

    #----------------------------------------------------------------------

    def registerLogs(self):
        '''
        Register list of application specified log files, Unix-style
        devices (syslog, stderr, stdout) or nCurses-style device (stdscr).

        NOTES:

        1) Standard device names (as defined in tsLogger module):

               StandardOutputFile = ""
               StandardOutputDevice = "stdout"
               StandardErrorDevice = "stderr"
               StandardScreenDevice = "stdscr"
               SystemLogDevice = "syslog"

        2) Logs keyword is a list of log file/device names

        3) Log names are to be prefixed by the program name

        4) Log names are to be suffixed by ".log"

        5) If keyword does not exist; then no logs created

        6) If Empty list; then create default log " "

        7) If non-empty list; then create default log and logs
           defined in list
        '''
        try:
            self.logs = self.tsAppKw['logs']
        except KeyError:
            self.logs = ['']

        # Create default log
        LogID = tsLogger.StandardOutputFile
        self.logger = tsLogger.TsLogger(
            name=tsLogger.StandardOutputFile,
            threshold=tsLogger.INFO)
        TsApplication._Logs[LogID] = self.logger
        TsApplication._TheAssignedLogger = self.logger

        # Create designated logs
        if DEBUG:
            print('self.logs=<"%s">' % str(self.logs))
        self.logger.info(
            'tsApplication.TsApplication: ' + \
            '\n\t"logs": <"%s">' % str(self.logs))
        for theName in self.logs:
            LogID = theName
            TsApplication._Logs[LogID] = tsLogger.TsLogger(
                name=LogID,
                threshold=tsLogger.INFO)

        # Log the comand line
        self.logger.info(
            'tsApplication.TsApplication: ' + \
            '\n\t"Command Line": <"%s">' % str(sys.argv))

    #----------------------------------------------------------------------

##    def registerOperatorSettings(self):
##        '''
##        Register command line keyword options and positional arguments.
##        Will update self.args and self.options only if len(sys.argv) > 1
##        and if parsing was successful.
##        '''
##        try:

##            self.enableDefaultCommandLineParser = self.tsAppKw['enableDefaultCommandLineParser']
##            if EnableParseCommandLineWarning:
##                self.logger.warning(
##                    'tsApplication.TsApplication: ' + \
##                    '\n\t"enableDefaultCommandLineParser" from CLI: <"%s">' % \
##                    str(self.enableDefaultCommandLineParser))
##            else:
##                self.logger.info(
##                    'tsApplication.TsApplication: ' + \
##                    '\n\t"enableDefaultCommandLineParser" from CLI: <"%s">' % \
##                    str(self.enableDefaultCommandLineParser))

##        except KeyError:

##            self.enableDefaultCommandLineParser = False

##            self.logger.info(
##                'tsApplication.TsApplication: ' + \
##                '\n\t"enableDefaultCommandLineParser" not defined, ' + \
##                'using stub <"%s"> from tsApplication' % \
##                str(self.enableDefaultCommandLineParser))

##      # Performs non-application-specific command line parsing
##      # when enabled.
##      try:

##          if self.enableDefaultCommandLineParser:

##              # Invoke application-independent default method:
##              #
##              #     a) Provides minimal usage help
##              #
##              #     b) Provides means to invoke automatic and
##              #        manual Python version specific parser
##              #        selection
##              #
##              (args, options) = self.parseCommandLineStub()

##      except Exception, errorCode:

##          args = []
##          options = {}
##            self.logger.error(
##                'tsApplication.TsApplication: ' + \
##                '\n\t"self.parseCommandLineStub" errorCode, ' + \
##                '<"%s">' % \
##                str(errorCode))
 
##        (self.args, self.options) = (args, options)

    #----------------------------------------------------------------------

    def registerRunTimeEntryPoint(self):
        '''
        Register run time entry point (e.g. "main").
        '''
        try:
            self.runTimeEntryPoint = self.tsAppKw['runTimeEntryPoint']
            self.logger.info(
                'tsApplication.TsApplication: ' + \
                '\n\t"runTimeEntryPoint" = <"%s">.' % str(
                    self.runTimeEntryPoint))
        except KeyError as requiredKeyError:
            if KeyValueUndefinedTrap:
                self.logger.error('tsApplication.TsApplication: ' + \
                                  '"%s" not found' % requiredKeyError)
                raise tse.ProgramException(
                    tse.ARGUMENT_KEY_NOT_VALID,
                    'Argument named "%s" not found' % str(requiredKeyError))
            else:
                self.runTimeEntryPoint = self.runTimeTrap
                self.logger.error(
                    'tsApplication.TsApplication: ' + \
                    '\n\tDerived "runTimeEntryPoint" = <"%s">.' % str(
                        self.runTimeEntryPoint))

    #----------------------------------------------------------------------

    def resizeConsoleDisplay(self):
        '''
        Resize the Console Display if is smaller than the minimum.

        It must be invoked before the application outputs anything to
        the console display; else resizing will not occur.
        '''
        RecommendedDisplaySize = ThemeCxPython['tsRecommendedDisplaySize']
        MinimumDisplaySize = ThemeCxPython['tsMinimumDisplaySize']
        ConsoleDisplaySize = ThemeCxPython['tsConsoleDisplaySize']

        if ((ConsoleDisplaySize['Rows'] >= MinimumDisplaySize['Rows']) and \
              (ConsoleDisplaySize['Cols'] >= MinimumDisplaySize['Cols'])):

            rows = ConsoleDisplaySize['Rows']
            cols = ConsoleDisplaySize['Cols']

        else:

            rows = MinimumDisplaySize['Rows']
            cols = MinimumDisplaySize['Cols']

            print("\x1b[8;%s;%st") % (str(rows), str(cols))

    #----------------------------------------------------------------------

    def runMainApplication(self):
        '''
        Initiate the application and generate the appropriate exit code
        and message upon its termination.
        '''

##      TBD:
##          Does this method ever return?
##          According to wxPython: The application only exits via the
##          occurance of an exception.

        self.runTimeEntryPoint()

    #----------------------------------------------------------------------

    def runTimeTrap(self):
        '''
        Trap unresolved "runTimeEntryPoint" KeyError and AttributeError
        for Pylint.
        '''
        logger = self.getLog()
        trapMsg = 'Argument named "%s" not found in module "%s"' % \
                  ('runTimeEntryPoint', self.buildTitle)
        logger.critical(trapMsg)
        raise tse.ProgramException(
            tse.ARGUMENT_KEY_NOT_VALID, trapMsg)

    #-----------------------------------------------------------------------

    # Bottom = property(GetBottom, SetBottom)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

