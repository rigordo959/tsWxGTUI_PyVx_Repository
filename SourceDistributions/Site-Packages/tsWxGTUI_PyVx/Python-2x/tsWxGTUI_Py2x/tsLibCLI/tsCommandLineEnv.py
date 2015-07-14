#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:13:44 AM rsg>"
'''
tsCommandLineEnv.py - Class to initialize and configure the
application program launched by an operator. It delivers those
keyword-value pair options and positional arguments specified
by the application, in its invocation parameter list. It wraps
the Command Line Interface application with exception handlers
to control exit codes and messages that may be used to co-
ordinate other application programs.
'''
#################################################################
#
# File: tsCommandLineEnv.py
#
# Purpose:
#
#    Class to initialize and configure the application program
#    launched by an operator. It delivers those keyword-value
#    pair options and positional arguments specified by the
#    application, in its invocation parameter list. It wraps
#    the Command Line Interface application with exception hand-
#    lers to control exit codes and messages that may be used to
#    coordinate other application programs.
#
# Limitations:
#
#    1. tsApplication - A component of tsLibCLI, it provides
#       application initialization, configuration validation
#       and launch services for both the Command Line Interface
#       (CLI) and for its subsequent launch and transition to
#       the Graphical-style User Interface (GUI). Being a com-
#       ponent of tsLibCLI, tsApplication can import other
#       components of tsLibCLI. However, since tsLibGUI is
#       is built upon tsLibCLI, tsApplication may NOT import any
#       any tsLibGUI components. Centralizing the option input
#       and validation, in tsApplication, ensures the uniqueness
#       of any option in the combined set of CLI and GUI options.
#
#    2. tsCommandLineEnv - A component of tsLibCLI, it uses
#       tsApplication to provide CLI-specific convenience
#       wrapper functions. It can import other components of
#       tsLibCLI. However, since tsLibGUI is built upon tsLibCLI,
#       tsCommandLineEnv may NOT import any tsLibGUI components.
#
#    3. tsWxMultiFrameEnv - A component of tsLibGUI, it uses
#       tsApplication to provide GUI-specific convenience
#       wrapper functions. It can import other components of
#       tsLibCLI. Since tsLibGUI is built upon tsLibCLI,
#       tsWxMultiFrameEnv may also import other tsLibGUI components.
#
#    4. parseCommandLine - The application supplied method must deliver
#       a tuple of options (in dictionary format) and args (in list
#       format) regardless of the application's use of "argparse",
#       "optparse" (which became deprecated at Python 2.7.0) or
#       "getopts" (which became deprecated at Python 2.3).
#
# Notes:
#
#    None
#
# Usage (example):
#
#     ## Add the following source code to the main application
#     ## program file.
#     ##
#     ## Note: The application is responsble for collecting,
#     ##       parsing and applying command line keyword-value
#     ##       pair options and positional arguments. The
#     ##       application is also responsible for customizing
#     ##       an instance of "tsCommandLineEnv" to wrap itself
#     ##       with application-specific exception handlers that
#     ##       set exit codes and messages, upon termination,
#     ##       that may be used to coordinate the actions of
#     ##       other applications.
#
#     ## Import Module
#     from tsCommandLineEnv import CommandLineEnv
#
#     ##  Generalized Form to Instantiate and Launch an application
#     ##  module that uses a Command Line Interface (CLI) to a
#     ##  character-mode terminal with optional logging.
#     ##
#     ##  See this File's header for examples of those application
#     ##  specific source code descriptions associated with
#     ##  parameter identifiers having double-underscore ("__")
#     ##  prefix and suffix.
#     ##
#     ##  See the test_tsWxWidgets.py File's header for examples of
#     ##  the gui application option usage.
#
#     ###########################################################
#
#     myApp = CommandLineEnv(
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
#         guiTopLevelObjectId=-1,
#         guiTopLevelObjectName='Sample',
#         guiTopLevelObjectParent='Sample',
#         guiTopLevelObjectStatusBar=None,
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
#     myApp = CommandLineEnv(
#         buildTitle=__title__,
#         buildVersion=__version__,
#         buildDate=__date__,
#         buildTitleVersionDate=mainTitleVersionDate,
#         buildHeader=__header__,
#         logs=[],
#         runTimeEntryPoint=main)
#
#     ###########################################################
#
#     ## Simplest Form to Instantiate Module with custom logging
#     myApp = CommandLineEnv(
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
#    2013/06/01 rsg Added support for tsOperatorSettingsParser.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsCommandLineEnv'
__version__   = '1.6.0'
__date__      = '06/15/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'

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
import traceback

#------------------------------------------------------------------------

# Enable Command Line Interface Application Launch Support
#
# NOTE: tsCommandLineEnv is a convenience package wrapping terminal
#       keyboard input, scrolled video display output, tsLogger and
#       tsException services.

from tsWxGTUI_Py2x.tsLibCLI import tsApplication
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser

CommandLineEnvWrapperEnable = True

#------------------------------------------------------------------------

DEBUG = False # Set True to log run time parameters and exit.
VERBOSE = False

DebugSimulatedKeyErrorTrap = True

runTimeTitleEnabled = True
tracebackEnabled = False

#------------------------------------------------------------------------

__help__ = '''
Append " -h" or " --help" to the command line before using the
"ENTER/RETURN" key.
'''

#------------------------------------------------------------------------

class CommandLineEnv(tsApplication.TsApplication):
    '''
    Class to initialize and configure the application program launched
    by an operator. It delivers those keyword-value pair options and
    positional arguments specified by the application, in its invocation
    parameter list. It wraps the Command Line Interface application with
    exception handlers to control exit codes and messages that may be
    used to coordinate other application programs.
    '''
    #--------------------------------------------------------------------
    # Begin Class Variables

    # End Class Variables
    #--------------------------------------------------------------------
    def __init__(self, *args, **kw):
        '''
        Class constructor.
        '''

        #------------------------------------------------------------------

        tsApplication.TsApplication.__init__(self, *args, **kw)

        if self.enableDefaultCommandLineParser:

            theModule = tsOperatorSettingsParser
            theClass = theModule.TsOperatorSettingsParser()
            (args, options) = theClass.parseCommandLineDispatch()
            self.args = args
            self.options = options

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
                print(msg)


        except Exception, preImportDevicesError:

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

            if False and DEBUG:

                (args, options) = self.getLaunchSettings()

                print('\n\n\tCommandLineEnv.Wrapper')
                print('\n\n\targs=%s' % str(args))
                print('\n\n\toptions=%s' % str(options))
 
##            self.runTimeEntryPoint(instantiationSettings=(args, options))
            self.runTimeEntryPoint()

        except Exception, applicationError:

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

if __name__ == '__main__':

    print(__header__)
