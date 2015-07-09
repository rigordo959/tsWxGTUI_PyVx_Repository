#! /usr/bin/env python
#"Time-stamp: <03/28/2015  1:59:17 AM rsg>"
__doc__ = '''
test_tsApplication.py - Basic run time environment manager to
demonstrate the use of the "tsApplication" class.
'''
#################################################################
#
# File: test_tsApplication.py
#
# Purpose:
#
#     Basic run time environment manager to demonstrate the use
#     of the "tsApplication" class to initialize, configure and
#     launch an application program specified by an operator.
#     Its configuration supports those keyword value pair options
#     and positional arguments specified by the operator, on the
#     command line, and those specified by the application, in its
#     invocation parameter list.
#
# Limitations:
#
#    1) The "tsApplication" module can be used to launch only the
#       Command Line Interface portion of an applications. The
#       application designer is responsible for producing Unix-style
#       exit codes and messages, upon application termination.
#
#    2) The "tsCommandLineEnv" module, a derivative of "tsApplication"
#       can be used to launch only the Command Line Interface portion
#       of an applications. It provides a wrapper that produces Unix-
#       style exit codes and messages, upon application termination.
#
#    3) The "tsWxMultiFrameEnv" module, a derivative of "tsCommand
#       LineEnv" can be used to launch both the Command Line Interface
#       and Graphical-style User Interface portions of an applications.
#       It provides a wrapper that produces Unix-style exit codes and
#       messages, upon application termination.
#
#    4) Command line keyword-value pair option and positional argument
#       parsing uses off-the-shelf, Python version appropriate modules.
#       To facilitate portability of this sample run time environment
#       manager from one Python platform to another, it automatically
#       selects and uses latest one of following:
#
#       a) "argparse" module used with Python 2.7.0 or later
#
#       b) "optparse" module used with Python 2.3.0 or later
#
#       c) "getopt" module used with Python 1.6.0 or later
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
#    4) Standardized command line option parsing methods return
#       a dictionary, of keyword value pairs, and a list, of
#       positional arguments in the manner of the "optparse"
#       module. This should facilitate application support for
#       the evolving Python command line option parsing modules.
#       However, this requires that "tsApplication" stubs and
#       application parsing methods include a small amount of
#       extra code for the appropriate "argparse", "optparse"
#       and "getopt" output format conversion.
#
#    5) The various command line parser modules produce usage
#       help. The content and format may vary based on the
#       parser's capabilities and limitations. Considerable
#       care needs to be taken to minimize the difference in
#       order to produce a software product that retains its
#       look and feel for the end-user, regardless of the
#       hardware and software platform being used.
#
# Usage (example):
#
#     ## Reference Module Methods
#     python test_tsApplication.py
#
# Methods:
#
#    prototype - Top-level method to control application-specific
#           functions. It prints the header text containing
#           the title, version, date, authors, copyright,
#           license and credits. It demonstrates exception
#           handling by attempting to open a non-existant file.
#
#    test_tsApplication - Run time environment wrapper to
#           control startup, exception handling and shut down
#           of application module under test.
#
#    getRunTimeTitle - Return Run Time Title, or Build Title,
#           whichever was actually used in command line,
#           stripping it of any file path.
#
#    getRunTimeTitleVersionDate - Return Run Time Title, or Build
#           Title, whichever was actually used in command line,
#           stripping it of any file path.
#
# Modifications:
#
#    2013/04/07 rsg Added description of methods.
#
#    2013/04/07 rsg Revised tsAPP.TsApplication parameter
#                   list to incorporate authors, copyright,
#                   license and credits.
#
#    2013/04/08 rsg Added GUI application launch parameter support
#                   for guiRequired, guiTopLevelObjectId,
#                   guiMessageRedirect, guiMessageFilename,
#                   guiTopLevelObject, guiTopLevelObjectName and
#                   guiTopLevelObjectTitle.
#
#    2013/04/09 rsg Removed GUI application launch parameter support
#                   for guiRequired, guiTopLevelObjectId,
#                   guiMessageRedirect, guiMessageFilename,
#                   guiTopLevelObject, guiTopLevelObjectName and
#                   guiTopLevelObjectTitle because testing is more
#                   appropriate with test_tsWxMultiFrameEnv.
#
#    2013/04/12 rsg Restored and expanded GUI application launch
#                   parameter support to facilitate compatibility
#                   testing of tsCommandLineEnv and tsMultiFrameEnv.
#
#    2013/04/12 rsg Merged in ths Python version-specific command
#                   line parser and user help description from:
#                   "test_tsApplication_ArgParse",
#                   "test_tsApplication_GetOpt" and
#                   "test_tsApplication_OptParse.
#
#    2013/05/16 rsg Replaced references tp parseCommandLine by
#                   references to enableDefaultCommandlineParser.
#
#    2013/06/01 rsg Added support for tsOperatorSettingsParser.
#
# ToDo:
#
#    2013/05/04 rsg Merge command line parser change(s) to
#                   "test_tsCommandLineEnv", as corrections occur.
#
#################################################################

__title__     = 'test_tsApplication'
__version__   = '1.11.0'
__date__      = '06/01/2013'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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

import os.path
import platform
import sys
import traceback

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------

DEBUG = False

DebugKeyValueUndefined     = False
DebugSimulatedKeyErrorTrap = False
EnableOptionsGNU = True

theAssignedLogger = None

#--------------------------------------------------------------------------

if __name__ == '__main__':


    #----------------------------------------------------------------------

    def exitTest():
        '''
        Simulated Input / Output Exception to induce termination
        with an exit code and message.
        '''
 
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = tsLogger.TsLogger(threshold=tsLogger.DEBUG,
                                     name='exitTest')

        message = 'ExitTest'

        myLogger.debug('***** ExitTest %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def getRunTimeTitle():
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

        return (fileName)

    #----------------------------------------------------------------------

    def getRunTimeTitleVersionDate():
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        runTimeTitle = getRunTimeTitle()
        if runTimeTitle == __title__:

            runTimeTitleVersionDate = mainTitleVersionDate

        else:

            runTimeTitleVersionDate = '%s, v%s (build %s)' % (
                runTimeTitle, __version__, __date__)

        return (runTimeTitleVersionDate)

    #----------------------------------------------------------------------

    def prototype(*args, **kw):
        '''
        Simulated main program entry point with simulated exception
        inducing exit test.
        '''
        print('\n%s\n' % getRunTimeTitleVersionDate())

        rawArgsOptions = sys.argv[1:]
        print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        theModule = tsOperatorSettingsParser
        theClass = theModule.TsOperatorSettingsParser()
        (args, options) = theClass.parseCommandLineDispatch()

        if True or DEBUG:

            print('\n\ttsCommandLineEnv.prototype (parameter list): ' + \
                  '\n\t\targs=%s;\n\t\tkw=%s' % (str(args),
                                                 str(kw)))

            print('\n\ttsCommandLineEnv.prototype (command line argv): ' + \
                  '\n\t\targs=%s;\n\t\toptions (unsorted)=%s' % (
                      str(args),
                      str(options)))

            fmt1 = '\n\ttsCommandLineEnv.prototype (command line argv): '
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                value = '"%s"' % options[key]
                if text == '':
                    text = '{%s: %s' % (str(key), str(value))
                else:
                    text += ', %s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        exitTest()

    #----------------------------------------------------------------------

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:

        theApplication = tsAPP.TsApplication(

            buildTitle=__title__,
            buildVersion=__version__,
            buildDate=__date__,
            buildAuthors=__authors__,
            buildCopyright=__copyright__,
            buildLicense=__license__,
            buildCredits=__credits__,
            buildTitleVersionDate=mainTitleVersionDate,
            buildHeader=__header__,
            buildPurpose=__doc__,

            enableDefaultCommandLineParser=False,

##          guiMessageFilename=None,
##          guiMessageRedirect=False,
##          guiRedirects=False,
##          guiRequired=False,
##          guiTopLevelObject=None,
##          guiTopLevelObjectId=None,
##          guiTopLevelObjectName=None,
##          guiTopLevelObjectParent=None,
##          guiTopLevelObjectTitle=None,

            logs=[tsLogger.StandardOutputFile, 'Dummy#2', 'Dummy#3'],

            runTimeEntryPoint=prototype)

        results = (theApplication.args, theApplication.options)
        print('results="%s"' % str(results))
        theAssignedLogger = theApplication.logger
        theApplication.runMainApplication()

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
