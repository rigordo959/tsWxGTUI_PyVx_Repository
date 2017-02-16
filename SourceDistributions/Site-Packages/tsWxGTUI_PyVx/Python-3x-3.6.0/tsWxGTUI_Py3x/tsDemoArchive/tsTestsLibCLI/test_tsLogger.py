#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:04:57 AM rsg>"
__doc__ = '''
test_tsLogger - Class to define and handle event message formatting
and output.
'''
#################################################################
#
# File: test_tsLogger
#
# Purpose:
#
#    Class to define and handle event message formatting
#    and output.
#
# Limitations:
#
#    1. Event message formating typically includes the following:
#        <Time Stamp> <Severity Level> <User Supplied Message>
#
#    2. Lower (Debug, Info and Notify) severity level event
#       messages are intended to be output to stdout and/or to a
#       user specified file.
#
#    3. Higher (Warning, Error, Critical and Emergency) severity
#       level event messages are intended to be output to stderr,
#       syslog and/or to a user specified file.
#
#    4. The Application Program Interface is modeled after but
#       does not use the standard Python Logging module.
#
#    5. The standard Python textwrap module is used to format
#       multi-line event messages.
#
# Usage (example):
#
#     ## Import Module
#     import tsLogger as Logger
#
#     ## Instantiate Module
#     myLogger = Logger.TsLogger(threshold=Logger.ERROR,
#                                start=time.time(),
#                                name='./myError.log')
#
#     ## Reference Module Methods
#     myLogger.log(Logger.ERROR, 'Timeout. Remote Host not available.')
#     myLogger.error('Timeout. Remote Host not available.')
#
# Methods:
#
#     myLogger.debug('Debug Level message.')
#     myLogger.info('Info Level message.')
#     myLogger.warning('Warning Level message.')
#     myLogger.error('Error Level message.')
#     myLogger.critical('Critical Level message.')
#     myLogger.log(Logger.ERROR, 'Timeout. Remote Host not available.')
#
# Modifications:
#
#   2007/08/03 RSG Modified "_open" to add information about
#                  when logging started to the named file.
#
#   2011/01/26 RSG Added assertTest.
#
#   2013/06/29 RSG Updated to reflect changes to tsLogger.
#
#   2013/11/13 rsg Re-assigned Private severity level from 60 to
#                  1 because nothing should be higher than
#                  CRITICAL OR EMERGENCY.
#
# ToDo:
#
#   1. Methods should support *args and **kw.
#
#################################################################

__title__     = 'test_tsLogger'
__version__   = '2.1.0'
__date__      = '11/13/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  Python Logging Module API Features: ' + \
                '\n\t  Copyright (C) 2001-2010 Vinay Sajip. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  Copyright (c) 2001-2013 ' + \
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
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

# from optparse import OptionParser
import os.path
import sys
import time
import traceback
import types

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsLogger
from tsWxGTUI_Py3x.tsLibCLI import tsReportUtilities

#--------------------------------------------------------------------------

TROUBLE_SHOOTING_DEBUG = False # DEBUG is reserved for tsLogger DEBUG level

#--------------------------------------------------------------------------

if __name__ == "__main__":

    def wrapperTest():
        '''
        Verify operation of logging to devices and files.
        '''
##        def taskTest():
##            '''
##            Verify logging to application log.
##            '''
##            theName = 'taskTest.log'
##            defaultLogger = TsLogger(threshold=INFO,
##                                     start=time.time())
##            print('\tStarted Logging to %s' % defaultLogger.name)
##            defaultLogger.info('Started Logging to %s' % defaultLogger.name)

##            print('\tDefault Task: %s' % \
##                  defaultLogger.theTopLevelApplicationTask)
##            defaultLogger.info('Default Task: %s' % \
##                          defaultLogger.theTopLevelApplicationTask)

##            theName = 'taskTest.log'
##            myLogger = TsLogger(threshold=INFO,
##                                start=time.time(),
##                                name=theName)
##            print('\tStarted Logging to %s' % myLogger.name)
##            myLogger.info('Started Logging to %s' % myLogger.name)

##            print('\tTask: %s' % myLogger.theTopLevelApplicationTask)
##            myLogger.info('Task: %s' % myLogger.theTopLevelApplicationTask)

        #-------------------------------------------------------------------

        def propertyTest(myLogger):
            '''
            Verify logger properties.
            '''
            try:
                myLogger.info(
                    'appLogger= "%s"' % myLogger.appLogger)
                myLogger.info(
                    'theLogName= "%s"' % myLogger.theLogName)
                myLogger.info(
                    'theLogPath= "%s"' % myLogger.theLogPath)
                level = myLogger.theLogThreshold
                levelName = getLevelName(level)
                myLogger.info(
                    'theLogThreshold= "%s" (%s)' % (levelName, level))
            except Exception as propertyErrorCode:
                myLogger.error(
                    'propertyErrorCode="%s"' % propertyErrorCode)

        #-------------------------------------------------------------------

        def levelTest(myLogger):
            '''
            Verify logging for each level.
            '''
            availableLevels = [
                tsLogger.NOTSET,
                tsLogger.PRIVATE,
                # tsLogger.DEBUG_TRACE_LEVEL,
                tsLogger.DEBUG,
                tsLogger.INFO,
                tsLogger.NOTICE,
                tsLogger.WARNING,
                tsLogger.ALERT,
                tsLogger.ERROR,
                tsLogger.CRITICAL,
                tsLogger.EMERGENCY]

            if TROUBLE_SHOOTING_DEBUG:

                print('begin levelTest on <%s>' % myLogger.thisLogName)

            for level in availableLevels:

                levelName = tsLogger.getLevelName(level)

                myLogger.log(
                    level,
                    '%s Level report on <%s>' % (levelName,
                                                 myLogger.thisLogName))

            if TROUBLE_SHOOTING_DEBUG:

                print('end levelTest on <%s>' % myLogger.thisLogName)


        #-------------------------------------------------------------------

        def deviceTest():
            '''
            Verify logging to stdout, stderr and syslog.
            '''
            separator = '-' * (72 - 8)
            for device in tsLogger._deviceList:
                print('\n\t%s' % separator)
                myLogger = tsLogger.TsLogger(threshold=tsLogger.INFO,
                                    start=time.time(),
                                    name=device)
                print('\tName: %s' % myLogger.thisRegisteredName)
                print('\tID: %s' % myLogger.thisLogID)
                levelTest(myLogger)

                if False and TROUBLE_SHOOTING_DEBUG:
                    # Cannot close shared devices because there is
                    # no mechanism to automatically re-open them.
                    myLogger.close()

        #-------------------------------------------------------------------

        def fileTest():
            '''
            Verify logging to files.
            '''
            separator = '-' * (72 - 8)
            for device in ['', 'myMethod.log']:
                print('\n\t%s' % separator)
                myLogger = tsLogger.TsLogger(threshold = tsLogger.NOTSET,
                                    start = time.time(),
                                    name = device)
                print('\tName: %s' % myLogger.thisRegisteredName)
                print('\tID: %s' % myLogger.thisLogID)
                levelTest(myLogger)

        #-------------------------------------------------------------------

        def descriptionTest():
            '''
            Verify text wrapping operation when outputting multi-line text
            to logger.
            '''
            myLogger = tsLogger.TsLogger(threshold = tsLogger.ERROR,
                                start = time.time(),
                                name = 'myDescription.log',
                                file_header = 'Error Report Started',
                                file_footer = 'Error Report Finished',
                                width = 70,
                                initial_indent = '\t',
                                subsequent_indent = '\t')
            print('\tName: %s' % myLogger.thisRegisteredName)
            print('\tID: %s' % myLogger.thisLogID)

            paragraph = "The textwrap module provides two convenience" \
                        " functions, wrap() and fill(), as well as" \
                        " TextWrapper, the class that does all the work,"\
                        " and a utility function dedent(). If you're just" \
                        " wrapping or filling one or two text strings, the" \
                        " convenience functions should be good enough;" \
                        " otherwise, you should use an instance of" \
                        " TextWrapper for efficiency."

            message = ['1st line; no tabs']
            myLogger.description(message,
                                 level = tsLogger.ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #1')

            message = ['2nd line;\tone tab']
            myLogger.description(message,
                                 level = tsLogger.ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #2')

            message = ['3rd line;\t\ttwo tabs',
                       '',
                       paragraph]
            myLogger.description(message,
                                 level = tsLogger.ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #3')
            myLogger.close()

        #-------------------------------------------------------------------

        def rewriteTest():
            '''
            '''
            myLogger = tsLogger.TsLogger(threshold = tsLogger.WARNING,
                                start = time.time(),
                                name = 'myProgress.log')
            print('\tName: %s' % myLogger.thisRegisteredName)
            print('\tID: %s' % myLogger.thisLogID)
            myLogger.progress('No Level update', level = tsLogger.NOTSET)
            myLogger.progress('Debug Level update', level = tsLogger.DEBUG)
            myLogger.progress('Info Level update', level = tsLogger.INFO)
            myLogger.progress('Warning Level update', level = tsLogger.WARNING)
            myLogger.progress('Error Level update', level = tsLogger.ERROR)
            myLogger.progress('Critical Level update', level = tsLogger.CRITICAL)

            myLogger.event('\n\nFinished New Logging Tests\n\n')
            myLogger.close()

        #-------------------------------------------------------------------

        def assertTest():
            '''
            '''

            def pseudoOp(number):
                print(number)

            myDebugHandlers = tsLogger.TsLogger(threshold = tsLogger.DEBUG,
                                       start = time.time(),
                                       name = 'myAsserts.log')

            conditions = [True, False]
            line = 0
            for cond in conditions:

                print('#################### cond=%s ####################' % cond)
                line += 1 # 1
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxASSERT(
                            cond)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 2
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxASSERT_MSG(
                            cond,
                            msg='Sample #%d' % line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 3
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK(
                            cond,
                            rc=123 + line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 4
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK_MSG(
                            cond,
                            rc=123 + line,
                            msg='Sample #%d' % line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 5
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK2(
                            cond,
                            op=pseudoOp(line))))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 6
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK2_MSG(
                            cond,
                            op=pseudoOp(line),
                            msg='Sample #%d' % line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 7
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxFAIL()))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 8
                try:
                    print('line= %d; rc=%s' % (
                        line, myDebugHandlers.wxFAIL_COND_MSG(
                            cond, msg='Sample #%d' % line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 9
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxFAIL_MSG(
                            msg='Sample #%d' % line)))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 10
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxTRAP()))
                except Exception as errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

        #-------------------------------------------------------------------

        separator = '-' * 72
        # taskTest()
        print('\n%s' % separator)
        deviceTest()

        print('\n%s' % separator)
        fileTest()

        print('\n%s' % separator)
        descriptionTest()

        print('\n%s' % separator)
        rewriteTest()

        print('\n%s' % separator)
        assertTest()

        print('\n%s' % separator)

        myLogger = tsLogger.TsLogger(threshold = tsLogger.DEBUG,
                            start = time.time(),
                            name = 'myProperties.log')

        level=0
        head = myLogger.tsGetLoggerPath()
        tail = 'tsLogger-Dict.txt'
        deviceName = '%s/%s' % (head, tail)
        myFile = open(deviceName, 'w+')
        myDictionary = tsLogger.TsLogger.activeLoggerIDs
        tsReportUtilities.TsReportUtilities.displayDictionary(
            level, myDictionary, myFile, myLogger=None)
        myFile.close()

        propertyTest(myLogger)

    def getOptions():
        '''
        Parse the command line and return a list of positional arguments
        and a dictionanary of keyword options.

        NOTE: Requirement is an inappropriate, oversimplification.
              Invoking argparse or optparse (deprecated with Python 2.7.0)
              do not produce equivalent output without substantial post
              processing that has not yet been created. This may explain
              inability to migrate use of tsApplication to tsCommandLineEnv
              or to tsWxMultiFrameEnv.
        '''
        parser = OptionParser(usage='''\
        %prog [options]...

        Capture current hardware and software information
        about the run time environment for the user process.
        ''')

        (options, args) = parser.parse_args()
        if len(args) != 0:
            parser.print_help()
            sys.exit(1)

        return (args, options)

    def theMainApplication(*args, **kw):
        '''
        Unit test suite to verify module functional capabilities and
        application program interfaces.

        NOTE: Output to stderr takes precedence over output to stdout.
        '''
        print(__header__)

        wrapperTest()

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
        sys.stdout.write('\n' + msg + '\n')
    elif msg is not None:
        sys.stderr.write(msg + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)
