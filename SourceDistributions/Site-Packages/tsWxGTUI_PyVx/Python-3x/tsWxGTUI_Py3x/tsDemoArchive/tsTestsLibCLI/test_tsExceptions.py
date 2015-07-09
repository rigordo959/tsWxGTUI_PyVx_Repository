#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:02:11 AM rsg>"
__doc__ = '''
test_tsExceptions.py - Application program to demonstrate the
features of the tsExceptions class.
'''
#################################################################
#
# File: testApplication.py
#
# Purpose:
#
#    Application program to demonstrate the features of the
#    tsExceptions class.
#
# Usage (example):
#
#     ## Reference Module Methods
#     python test_tsExceptions.py
#
# Methods:
#
#
# Modifications:
#
#    2013/07/17 rsg Invoked DiagnosticException Unknown Error
#                   for exit test.
#
# ToDo:
#
#1. TBD.
#
#################################################################

__title__     = 'test_tsExceptions'
__version__   = '2.1.0'
__date__      = '07/17/2013'
__authors__   = 'Richard S. Gordon & Frederick A. Kier'
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

from optparse import OptionParser
import os.path
import sys
import traceback

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py3x.tsLibCLI import tsLogger as Logger

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

    print(__header__)

    myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                               name='runtime')

##    def getOptions():
##        '''
##        Parse the command line and return a list of positional arguments
##        and a dictionanary of keyword options.

##        NOTE: Requirement is an inappropriate, oversimplification.
##              Invoking argparse or optparse (deprecated with Python 2.7.0)
##              do not produce equivalent output without substantial post
##              processing that has not yet been created. This may explain
##              inability to migrate use of tsApplication to tsCommandLineEnv
##              or to tsWxMultiFrameEnv.
##        '''
##        parser = OptionParser(usage='''\
##        %prog [options]...

##        Capture current hardware and software information
##        about the run time environment for the user process.
##        ''')

##        (options, args) = parser.parse_args()
##        if len(args) != 0:
##            parser.print_help()
##            sys.exit(1)

##        return (args, options)

    #----------------------------------------------------------------------

    def diagnosticExceptionTest():
        exceptionName = tse.DIAGNOSTIC_EXCEPTION

        for errorName in tse.DiagnosticException.errorNames:
            message = 'Test(%s, %s)' % (exceptionName, errorName)

            myLogger.debug('***** %s / %s *****' % (exceptionName, errorName))
            try:
                raise tse.DiagnosticException(errorName, message)
            except tse.DiagnosticException as e1:
                tse.displayError(e1)
            except Exception as e1:
                sys.stderr.write('Unknown exception: %s' % e1)

    #----------------------------------------------------------------------

    def inputoutputExceptionTest():
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION

        for errorName in tse.InputOutputException.errorNames:
            message = 'Test(%s, %s)' % (exceptionName, errorName)

            myLogger.debug('***** %s / %s *****' % (exceptionName, errorName))
            try:
                raise tse.InputOutputException(errorName, message)
            except tse.InputOutputException as e1:
                tse.displayError(e1)
            except Exception as e1:
                sys.stderr.write('Unknown exception: %s' % e1)

    #----------------------------------------------------------------------

    def programExceptionTest():
        exceptionName = tse.PROGRAM_EXCEPTION

        for errorName in tse.ProgramException.errorNames:
            message = 'Test(%s, %s)' % (exceptionName, errorName)

            myLogger.debug('***** %s / %s *****' % (exceptionName, errorName))
            try:
                raise tse.ProgramException(errorName, message)
            except tse.ProgramException as e1:
                tse.displayError(e1)
            except Exception as e1:
                sys.stderr.write('Unknown exception: %s' % e1)

    #----------------------------------------------------------------------

    def userInterfaceExceptionTest():
        exceptionName = tse.USER_INTERFACE_EXCEPTION

        for errorName in tse.UserInterfaceException.errorNames:
            message = 'Test(%s, %s)' % (exceptionName, errorName)

            myLogger.debug('***** %s / %s *****' % (exceptionName, errorName))
            try:
                raise tse.UserInterfaceException(errorName, message)
            except tse.UserInterfaceException as e1:
                tse.displayError(e1)
            except Exception as e1:
                sys.stderr.write('Unknown exception: %s' % e1)

    #----------------------------------------------------------------------

    def exitTest():
        exceptionName = tse.DIAGNOSTIC_EXCEPTION
        errorName = 'Unknown Diagnostic Error'

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def theMainApplication(*args, **kw):
        myLogger.debug(__header__)
 
        programExceptionTest()
        inputoutputExceptionTest()
        diagnosticExceptionTest()
        userInterfaceExceptionTest()
        exitTest()

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
                # getOptions=getOptions,
                runTimeTitle='main',
                logs=[],
                runTimeEntryPoint=theMainApplication)

        theApplication.runMainApplication()

    except Exception as e:
        if isinstance(e, tse.TsExceptions):
            msg = str(e).replace("'", "")
            tse.displayError(e)
            exitStatus = e.exitCode
        else:
            msg = None
            sys.stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

    if msg == tse.NO_ERROR:
        sys.stdout.write(msg + '\n')
    elif msg is not None:
        sys.stderr.write(msg + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)

