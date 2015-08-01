#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:06:16 AM rsg>"
__doc__ = '''
test_tsReportUtilities.py - Application program to demonstrate
the features of the tsReportUtilities class.
'''
#################################################################
#
# File: test_tsReportUtilities.py
#
# Purpose:
#
#     Application program to demonstrate the features of the
#     tsReportUtilities class.
#
# Usage (example):
#
#     python test_tsReportUtilities.py
#
# Methods:
#
# Notes:
#
# ToDo:
#   1. TBD
#
# Modifications:
#
#################################################################

__title__     = 'test_tsReportUtilities.py'
__version__   = '2.0.0'
__date__      = '05/24/2013'
__authors__   = 'Richard S. Gordon'
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

import os
import sys
import time
# from optparse import OptionParser

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

tsrpu = tsReportUtilities.TsReportUtilities()

#--------------------------------------------------------------------------

if __name__ == "__main__":

    myLogger = Logger.TsLogger(name='',
                               threshold=Logger.INFO)

    #-------------------------------------------------------------------

    def displayDictionaryTest():
        '''
        Verify use cases for displayDictionary.
        '''
        myLogger.info('\n*** DISPLAY DICTIONARY TEST ***\n')

        sequentialDictionary = {100: 'apple',
                                -1: 'pear',
                                50: 'orange',
                                25: 1234,
                                15: 1.234,
                                'name': 'sequentialDictionary'}

        releaseDictionary = {'list1': [12, 34, 56],
                             'name': 'releaseDictionary',
                             'title': __title__,
                             'version': __version__,
                             'date': __date__}

        programDictionary = {'name': 'programDictionary',
                             'list2': ['ab', 'cd', 'ef'],
                             'main': __name__,
                             'mainTitleVersionDate': mainTitleVersionDate}

        myDictionary = {
            'name': 'myDictionary',
            'contents': {'releaseDictionary': releaseDictionary,
                         'programDictionary': programDictionary,
                         'sequentialDictionary': sequentialDictionary,
                         'name': 'contents'}}

        myConsole = sys.stdout
        tsrpu.displayDictionary(0, myDictionary, myConsole)

        myFile = open(os.path.join(myLogger.theLogPath,
                                   'displayDictionaryTest.log'), 'w')

        tsrpu.displayDictionary(0, myDictionary, myFile)
        myFile.close()

    #-------------------------------------------------------------------

    def getTimeStatisticsListTest():
        '''
        Verify use cases for getTimeStatisticsList.
        '''
        startupTime = time.time()
        currentTime = startupTime + float(3600)
        myInput = '%s %s' % (str(startupTime),
                             str(currentTime))
        myLogger.info('\n*** GET STATISTICS TIME TEST ***\n')
        output = str(tsrpu.getTimeStatisticsList(startupTime,
                                                 currentTime))
        myLogger.info('  %s %s' % (myInput, output))

    #-------------------------------------------------------------------

    def getStatisticsListTest():
        '''
        Verify use cases for getStatisticsList.
        '''
        startupTime = time.time()
        currentTime = startupTime + float(3600)
        numberOfTestRuns = 100
        numberOfTestPasses = 80
        numberOfTestFailures = 20
        myInput = '%s %s %s %s %s' % (str(startupTime),
                                      str(currentTime),
                                      str(numberOfTestRuns),
                                      str(numberOfTestPasses),
                                      str(numberOfTestFailures))
        myLogger.info('\n*** GET STATISTICS LIST TEST ***\n')
        output = str(tsrpu.getStatisticsList(
            startupTime,
            currentTime,
            numberOfTestRuns,
            numberOfTestPasses,
            numberOfTestFailures))
        myLogger.info('  %s %s' % (myInput, output))

    #-------------------------------------------------------------------

    def getDayHourMinuteSecondStringTest():
        '''
        Verify use cases for getDayHourMinuteSecondString.
        '''
        myList = [0, 1, 59, 60, 120, 3599, 3600, 24*3600, 25*3600]
        myLogger.info('\n*** GET DAY HOUR MINUTE SECOND STRING TEST ***\n')
        for myInput in myList:
            myOutput = str(tsrpu.getDayHourMinuteSecondString(
                inputSeconds=myInput,
                firstDelimiter='-'))
            myLogger.info('  %s %s' % (myInput, myOutput))

    #-------------------------------------------------------------------

    def getSecondsTimeFromHoursMinutesSecondsStringTest():
        '''
        Verify use cases for getSecondsTimeFromHoursMinutesSecondsString.
        '''
        myList = [None,
                  '00:00:00',
                  '01:02:03',
                  '12:34:56',
                  '23:59:59',
                  '24:00:00']
        myLogger.info(
            '\n*** GET SECONDS TIME FROM ' + \
            'HOURS MINUTES SECONDS STRING TEST ***\n')
        for myInput in myList:
            if myInput is None:
                output = str(
                    tsrpu.getSecondsTimeFromHoursMinutesSecondsString())
            else:
                output = str(
                    tsrpu.getSecondsTimeFromHoursMinutesSecondsString(
                        myInput))
            myLogger.info('  %s %s' % (myInput, output))

    #-------------------------------------------------------------------

    def getByteCountStringsTest():
        '''
        Verify use cases for getByteCountStrings.
        '''
        myLogger.info('\n*** GET BYTE COUNT STRINGS TEST ***\n')
        for power in range(9):
            myInput = int(1.0 * 1024**power)
            output = str(tsrpu.getByteCountStrings(myInput))
            myLogger.info('  1024^%d %s' % (power, output))

    #-------------------------------------------------------------------

    def getNextPathNameTest():
        '''
        Verify use cases for getNextPathName.
        '''
        myLogger.info('\n*** GET NEXT PATH NAME TEST ***\n')
        theDirectory = './'
        theName = 'junk'
        myLogger.info(
            '  %s %s %s' % (theDirectory,
                            theName,
                            tsrpu.getNextPathName(theDirectory,
                                                  theName)))

    #-------------------------------------------------------------------

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

    #-------------------------------------------------------------------

    def theMainApplication(*args, **kw):
        '''
        Unit test suite to verify module functional capabilities and
        application program interfaces.

        NOTE: Output to stderr takes precedence over output to stdout.
        '''
        myLogger.info(__header__)

        displayDictionaryTest()
        getNextPathNameTest()
        getTimeStatisticsListTest()
        getStatisticsListTest()
        getDayHourMinuteSecondStringTest()
        getSecondsTimeFromHoursMinutesSecondsStringTest()
        getByteCountStringsTest()
        displayDictionaryTest()

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

    except Exception, e:
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

