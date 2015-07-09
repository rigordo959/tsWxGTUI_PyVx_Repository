#! /usr/bin/env python
#"Time-stamp: <02/24/2015  4:57:17 AM rsg>"
'''
tsReportUtilities.py - Class defining methods used to format
information: date and time (begin, end and elapsed), file size
(with kilo-, mega-, giga-, tera-, peta-, exa-, zeta- and
yotta-byte units) and nested Python dictionaries.
'''
#################################################################
#
# File: tsReportUtilities.py
#
# Purpose:
#
#     Class defining methods used to format information: date
#     and time (begin, end and elapsed), file size (with kilo-,
#     mega-, giga-, tera-, peta-, exa-, zeta- and yotta-byte
#     units) and nested Python dictionaries.
#
# Usage (example):
#
#     # Import
#     from tsReportUtilities import TsReportUtilities as tsrpu
#
# Methods:
#
#    displayDictionary - Recursive method to display nested entries
#        in configuration dictionary.
#
#    getByteCountStrings - Return a tupple with the text represent-
#        ations of a value.
#
#    getDateAndTimeString - Construct timestamp string (in "Date at
#        Time" format).
#
#    getDateTimeString - Construct timestamp string suitable for
#        use as label or alternatively for use as filename.
#
#    getDayHourMinuteSecondString - Convert time from seconds to
#        string format.
#
#    getDictionaryKeyTypeList - Return a sorted list containing
#        the key type in the specified dictionary.
#
#    getElapsedTimeString - Construct elapsed time in days, hours,
#        minutes, seconds between supplied startup and current
#        time inputs in seconds since the UNIX epoch.
#
#    getHourMinuteSecondString - Construct elapsed time in days,
#        hours, minutes, seconds between supplied startup and current
#        time inputs in seconds since the UNIX epoch.
#
#    getIndentString - Construct a string of white space appropriate
#        for indenting level.
#
#    getNextPathName - Construct the path to the next log file.
#
#    getSecondsTimeFromHoursMinutesSecondsString - Convert time from
#        string to seconds format.
#
#    getSelectedDictionaryEntries - Return a dictioanry containing
#        the specified type of entries from the specified dictionary.
#
#    getSeparatorString - Construct a string of title and white space
#        to separate one section of text from another.
#
#    getStatisticsList - Create test summary after elapesed time and
#        statistics details on the number of test runs, number of
#        passing test runs, number of failing test runs, startup
#        timestamp, shutdown timestamp and elapsed timesrtamp.
#
#    getTimeStatisticsList - Generate Startup, Current (or Shutdown)
#        and Elapsed Time strings.
#
#    getYearMonthDayString - Construct date string (in "Year-Month-Day"
#        format) from time in seconds since UNIX epoch.
#
# Notes:
#
#   1).  Must NOT create circular dependency on tsLogger class because
#        it will interfere with tsLibCLI import.
#
# Modifications:
#
#   2008/02/05 rsg  Modified displayDictionary. Will append
#                   hex ASCII value for integer type dictionary
#                   entries.
#
#   2011/05/15 rsg  Redesigned displayDictionary to categorize
#                   dictionary keys before sorting into ascending
#                   order because Python 3.2 does not sort mixture
#                   of int and str types.
#
#   2013/04/18 rsg  Removed dependence on tsLogger class because
#                   circular dependency interferes with import.
#
#   2013/06/21 rsg  Added msecDelimiter definitions to facilitate
#                   compatibility of tsLogger with Pythonlogging:
#
#                   pythonLoggingMsecDelimiter = ','
#                   tsLoggerMsecDelimiter = '.'
#                   msecDelimiter = pythonLoggingMsecDelimiter
#
#   2013/06/30 rsg  Added path and file naming rule references to
#                   getDateTimeString.
#
#                   Added FileNameTimeDashFormat flag and added logic
#                   to control file name format:
#
#                   True  returns "2010-05-13-at-04-17-49" for
#                                 May 13, 2010 at 04:17:49).
#
#                   False returns "2010-05-13-at-04_17_49" for
#                                 May 13, 2010 at 04:17:49).
#
# ToDo:
#
#   1. Resolve application segmentation fault when import ts enabled.
#
#   2. tsfl.TsFileLock(tsfl.TsFileLock.EVENTID) does not work yet.
#
#################################################################

__title__     = 'tsReportUtilities.py'
__version__   = '2.1.0'
__date__      = '06/30/2013'
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

#--------------------------------------------------------------------------

import glob
import os
import os.path
import sys
import time
from types import *

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#---------------------------------------------------------------------------

try:

    import tsExceptions as tse
    # import tsLogger as Logger

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

## import tsFileLock as tsfl

DEBUG = False

pythonLoggingMsecDelimiter = ','
tsLoggerMsecDelimiter = '.'
msecDelimiter = pythonLoggingMsecDelimiter
FileNameTimeDashFormat = True

#---------------------------------------------------------------------------

class TsReportUtilities(object):
    '''
    Class defining methods used to format information: date and time
    (begin, end and elapsed), file size (with kilo-, mega-, giga-,
    tera-, peta-, exa-, zeta- and yotta-byte units) and nested Python
    dictionaries.
    '''
    # Report Header Controls
    # for 12 point/10 pitch (1 inch = 6 lines and 10 characters)
    pageWidth = 80
    pageLength = 66
    layout = {'TitleWidth': pageWidth - 2,
              'TitleLeft': 0,
              'TitleIndent': 8,
              'TitleCenter': (pageWidth - 2) // 2,
              'TitlePrefix': ' ',
              'TitleSuffix': ' ',
              'spacesPerIndent': 2}

    #-----------------------------------------------------------------------

    @staticmethod
    def displayDictionary(level, myDictionary, myFile, myLogger=None):
        '''
        Recursive method to display nested entries in configuration dictionary.
        '''
        def getDictionaryKeyTypeList(myDictionary, myLogger=None):
            '''
            Return a sorted list containing the key type in the
            specified dictionary.
            '''
            # print('***** getDictionaryKeyTypeList *****')
            try:

                myKeyList = list(myDictionary.keys())
                selectedKeyTypes = []
                for aKey in myKeyList:
                    if type(aKey) in selectedKeyTypes:
                        pass
                    else:
                        selectedKeyTypes += [type(aKey)]

            except Exception as e:

##                print('***** ERROR: Exception at "%s"' % e)
##                print('\n***\n' + str(myDictionary) + '\n***\n')

                if myLogger is None:

                    # TBD - Need to find out cause of failure.
                    myLoggerID = open('tsReportUtilities.log', 'w')
                    fmt = '%s - ERROR: Exception at "%s"' % (
                        TsReportUtilities.getDateTimeString(time.time(),
                                                            msec=False), e)
                    myLoggerID.write('\n%s\n' % fmt)
                    myLoggerID.write('\n***\n' + str(myDictionary) + '\n***\n')
                    myLoggerID.flush()
                    myLoggerID.close()

##                else:

##                    myLogger.error('Exception at "%s"' % e)
##                    myLogger.info('\n***\n' + str(myDictionary) + '\n***\n')

            results = selectedKeyTypes
            # print('results=%s' % str(results))
            return (results)

        #-------------------------------------------------------------------

        def getSelectedDictionaryEntries(myDictionary, myType, myLogger=None):
            '''
            Return a dictioanry containing the specified type of entries from
            the specified dictionary.
            '''
            # print('***** getSelectedDictionaryEntries *****')
            # print('myDictionary=%s' % str(myDictionary))
            # print('myType=%s' % str(myType))
            try:

                myKeyList = list(myDictionary.keys())
                # print('myKeyList=%s' % str(myKeyList))
                selectedKeyList = []
                selectedMaximumKeyLength = 0
                selectedDictionary = {}
                for aKey in myKeyList:
                    # print('aKey=%s' % str(aKey))
                    if isinstance(aKey, myType):
                        selectedKeyList += [aKey]
                        selectedKeyText = str(aKey)
                        if isinstance(aKey, int):
                            # Adjust for a leading space
                            selectedKeyLength = len(selectedKeyText) + 1
                        else:
                            selectedKeyLength = len(selectedKeyText)
                        # print('selectedKeyLength=%d' % selectedKeyLength)
                        selectedMaximumKeyLength = max(
                            selectedKeyLength,
                            selectedMaximumKeyLength)
                        selectedDictionary[aKey] = myDictionary[aKey]

            except Exception as e:

##                print('***** ERROR: Exception at "%s"' % e)
##                print('\n***\n' + str(myDictionary) + '\n***\n')

                if myLogger is None:

                    # TBD - Need to find out cause of failure.
                    myLoggerID = open('tsReportUtilities.log', 'w')
                    fmt = '%s - ERROR: Exception at "%s"' % (
                        TsReportUtilities.getDateTimeString(time.time(),
                                                            msec=False), e)
                    myLoggerID.write('\n%s\n' % fmt)
                    myLoggerID.write('\n***\n' + str(myDictionary) + '\n***\n')
                    myLoggerID.flush()
                    myLoggerID.close()

##                else:

##                    myLogger.error('Exception at "%s"' % e)
##                    myLogger.info('\n***\n' + str(myDictionary) + '\n***\n')

            results = (selectedDictionary, selectedMaximumKeyLength)
            # print('results=%s' % str(results))
            return (results)

        #-------------------------------------------------------------------

        indent = '      ' * level
        banner = '-' * 5
        if 'name' in list(myDictionary.keys()):
            theName = myDictionary['name']
        else:
            theName = 'No Name'

        beginBanner = '\n   %s%s Begin "%s" at level %d %s\n' % (
            indent,
            banner,
            theName,
            level,
            banner)

        endBanner = '\n   %s%s End   "%s" at level %d %s\n' % (
            indent,
            banner,
            theName,
            level,
            banner)

        myFile.write(beginBanner + '\n')

        # print('***** displayDictionary *****')
        # print('level=%d' % level)
        # print('myDictionary=%s' % str(myDictionary))
        myTypes = getDictionaryKeyTypeList(myDictionary)
        # print('myTypes=%s' % str(myTypes))
        maximumLength = 0
        for selectedType in myTypes:
            # print('selectedType=%s' % str(selectedType))
            (selectedDictionaryEntries,
             selectedMaximumLength) = \
             getSelectedDictionaryEntries(myDictionary,
                                          selectedType,
                                          myLogger)
            maximumLength = max(maximumLength, selectedMaximumLength)
            # print('maximumLength=%d' % maximumLength)
            # print('selectedDictionaryEntries=%s' % \
            #       str(selectedDictionaryEntries))
            try:
                # Sort alpha-numeric class objects
                # (e.g., int & str)
                keyList = sorted(list(selectedDictionaryEntries))
            except Exception as errorCode:
                # Cannot sort non-alpha-numeric class objects
                # (e.g., dictionary & window)
                if DEBUG:
                    print('***** DEBUG: %s in displayDictionary' % errorCode)
                keyList = list(selectedDictionaryEntries)
            # print('keyList=%s' % str(keyList))
            for theKey in keyList:
                theValue = selectedDictionaryEntries[theKey]
                if isinstance(theValue, dict):
                    sublevel = level + 1
                    subindent = '  ' * sublevel
                    TsReportUtilities.displayDictionary(sublevel,
                                                        theValue,
                                                        myFile,
                                                        myLogger)
                else:
                    # print('%s = %s' % (str(theKey),
                    #                    str(theValue)))
                    if isinstance(theValue, int):
                        # Append hex ASCII value for integer type entries.
                        numericValue = int(theValue)
                        textValue = '%d (0x%X)' % (numericValue, numericValue)
                    else:
                        textValue = str(myDictionary[theKey])
                    text = '   %s %*s = %s\n' % (indent,
                                                 maximumLength,
                                                 theKey,
                                                 textValue)
                    myFile.write(text)

        myFile.write(endBanner + '\n')

    #-----------------------------------------------------------------------

    @staticmethod
    def getByteCountStrings(bytes):
        '''
        Return a tupple with the text representations of a value.
        Labeled     - TB (Terabyte),
                      GB (Gigabyte),
                      MB (Megabyte),
                      KB (Kilobyte) and
                      B (Byte)
        Decimal     - ASCII Numeric
        Hexadecimal - Hex ASCII

        Ref: http://www.answers.com/topic/terabyte?cat=health
        '''
        KILOBYTE = 1024
        MEGABYTE = KILOBYTE * KILOBYTE
        GIGABYTE = MEGABYTE * KILOBYTE
        TERABYTE = GIGABYTE * KILOBYTE
        PETABYTE = TERABYTE * KILOBYTE
        EXABYTE = PETABYTE * KILOBYTE
        ZETTABYTE = EXABYTE * KILOBYTE
        YOTTABYTE = ZETTABYTE * KILOBYTE

        kilobytes = float(bytes)/float(KILOBYTE)
        megabytes = float(kilobytes)/float(KILOBYTE)
        gigabytes = float(megabytes)/float(KILOBYTE)
        terabytes = float(gigabytes)/float(KILOBYTE)
        petabytes = float(terabytes)/float(KILOBYTE)
        exabytes = float(petabytes)/float(KILOBYTE)
        zettabytes = float(exabytes)/float(KILOBYTE)
        yottabytes = float(zettabytes)/float(KILOBYTE)

        if bytes >= YOTTABYTE:
            labeledSize = '%2.2f YBytes' % yottabytes

        elif bytes >= ZETTABYTE:
            labeledSize = '%2.2f ZBytes' % zettabytes

        elif bytes >= EXABYTE:
            labeledSize = '%2.2f EBytes' % exabytes

        elif bytes >= PETABYTE:
            labeledSize = '%2.2f PBytes' % petabytes

        elif bytes >= TERABYTE:
            labeledSize = '%2.2f TBytes' % terabytes

        elif bytes >= GIGABYTE:
            labeledSize = '%2.2f GBytes' % gigabytes

        elif bytes >= MEGABYTE:
            labeledSize = '%2.2f MBytes' % megabytes

        elif bytes >= KILOBYTE:
            labeledSize = '%4.2f KBytes' % kilobytes

        else:
            labeledSize = '%d Bytes' % bytes
 
        decimalSize = '%d' % bytes
        hexadecimalSize = '0x%X' % bytes

        return (labeledSize, decimalSize, hexadecimalSize)

    #-----------------------------------------------------------------------
 
    @staticmethod
    def getDateAndTimeString(seconds):
        '''
        Construct timestamp string (in "Date at Time" format).
        '''
        return time.strftime('%a, %d-%b-%Y at %H:%M:%S',
                             time.localtime(seconds))

    #-----------------------------------------------------------------------
 
    @staticmethod
    def getDateTimeString(seconds,
                          msec=False,
                          filename=False):
        '''
        Construct timestamp string suitable for use as label or alternatively
        for use as filename.

        Label output uses "Year/Month/Day Hour:Minute:Second" format
        with optional ".millisecond" suffix). For example,
        "2010/05/13-04:17:49.123" is returned for 123 milliseconds after
        May 13, 2010 at 04:17:49).

        Filename output uses "Year/Month/Day" and "Hour:Minute:Second" data
        separated by "-at-" and with "-" replacing "/" and ":" separators.
        For example, "2010-05-13-at-04-17-49" is returned for May 13, 2010
        at 04:17:49).

        From: http://www.portfoliofaq.com/pfaq/FAQ00352.htm

                The following list is fairly exhaustive and pulls together
                references from various sources. Although not mentioned
                explicitly, Unix seems to have few - if any - restrictions.
                Compliance with these conventions as assets are added to
                your library will allow widest use of the assets without
                subsequent manual intervention to re-path/name, etc. The
                rules take into account the use of assets on local &
                network hard drives, CD/DVD, removable drives and online
                (web/ftp) using Mac OS9/OSX and Windows OSs:

                1.  Illegal filename characters, (e.g. : or ?). (All OSs).

                2.  Deprecated filename characters (; and ,). (All OSs).

                3.  >31 filename characters including extension.
                    (Mac Classic).

                4.  >64 filename characters including extension.
                    (Windows: ISO9660+Joliet CD or Hybrid CD partition).

                5.  No extension - extensions are mandatory for Windows and
                    the only means for Portfolio to tell file type.
                    (Windows, Mac OS X).

                6.  Filename has >1 period - Portfolio may misinterpret
                    extension. (Windows, Mac OS X).

                7.  Extension may be wrong, i.e. not 3 characters.
                    (Windows, Mac OS X).

                8.  Illegal characters in path to file - same issue
                    as #1 but for path. (All OSs).

                9.  Deprecated characters in path to file - same issue
                    as #2 but for path. (All OSs).

                10. Filename may not begin with a period. (Windows not
                    allowed, Mac treats as a hidden file)

                11.  Filename may not end in a period. (Windows not
                     allowed - OS "throws away" the trailing period
                     when naming/reading so incorrect matching vs.
                     Mac name)

                12. Names conflicting with some of Win OS old DOS
                    functions (Not allowed in either upper or lowercase
                    and with or without a file extension or as a file
                    extension: COM1 to COM9 inclusive, LPT1 to LPT9
                    inclusive, CON, PRN, AUX, CLOCK$ and NUL)

                13. Case sensitivity. Windows OSs (and IIS web servers)
                    are not case sensitive. Most other OSs (and web
                    servers) are.

                14. Filenames ought not to begin with a hyphen (Unix
                    systems my interpret the filename as a flag to a
                    command line call).

        From: http://msdn.microsoft.com/en-us/library/windows/
              desktop/aa365247%28v=vs.85%29.aspx#naming_conventions

                Use any character in the current code page for a name,
                including Unicode characters and characters in the
                extended character set, except for the following:

                    The following reserved characters:
                        < (less than)
                        > (greater than)
                        : (colon)
                        " (double quote)
                        / (forward slash)
                        \ (backslash)
                        | (vertical bar or pipe)
                        ? (question mark)
                        * (asterisk)

        '''
        if filename:

            if FileNameTimeDashFormat:
                timestamp = time.strftime(
                    '%Y-%m-%d-at-%H-%M-%S',
                    time.localtime(seconds))
            else:
                timestamp = time.strftime(
                    '%Y-%m-%d-at-%H_%M_%S',
                    time.localtime(seconds))

        else:
            if msec:
                timestamp1 = time.strftime(
                    '%Y/%m/%d %H:%M:%S',
                    time.localtime(seconds))

                timestamp2 = '%03d' % ((seconds - int(seconds)) * 1000)

                timestamp = '%s%s%s' % (timestamp1, msecDelimiter, timestamp2)
 
            else:
                timestamp = time.strftime(
                    '%Y/%m/%d %H:%M:%S',
                    time.localtime(seconds))

        return timestamp

    #-----------------------------------------------------------------------

    @staticmethod
    def getDayHourMinuteSecondString(inputSeconds=0,
                                     firstDelimiter='-'):
        '''
        Convert time from seconds to string format.
        '''
        secondsLeft = inputSeconds
        days = secondsLeft // (3600 * 24)
        secondsLeft -= days * (3600 * 24)
        hours = secondsLeft // 3600
        secondsLeft -= hours * 3600
        minutes = secondsLeft // 60
        secondsLeft -= minutes * 60
        seconds = secondsLeft

        return '%02d%s%02d:%02d:%02d' % (days,
                                         firstDelimiter,
                                         hours,
                                         minutes,
                                         seconds)

    #-----------------------------------------------------------------------

    @staticmethod
    def getElapsedTimeString(startupTime, currentTime):
        '''
        Construct elapsed time in days, hours, minutes, seconds between
        supplied startup and current time inputs in seconds since the
        UNIX epoch.
        '''
        tsru = TsReportUtilities
        return '%s (days-hrs:min:sec)' % \
               tsru.getDayHourMinuteSecondString(
                   inputSeconds=int(currentTime - \
                                    startupTime),
                   firstDelimiter='-')

    #-----------------------------------------------------------------------

    @staticmethod
    def getHourMinuteSecondString(seconds):
        '''
        Construct time string (in "Hour:Minute:Second" format) from time in
        seconds since UNIX epoch.
        '''
        return time.strftime('%H:%M:%S', time.localtime(seconds))

    #-----------------------------------------------------------------------

    @staticmethod
    def getIndentString(indent):
        '''
        Construct a string of white space appropriate for indenting level.
        '''
        if indent < 1:
            return ''
        else:
            return ' ' * (TsReportUtilities.layout['spacesPerIndent'] * indent)

    #-----------------------------------------------------------------------

    @staticmethod
    def getNextPathName(theDirectory, theName):
        '''
        Construct the path to the next log file.

        Get the next filename
          theName + _ + number + .txt
          log_1.txt, log_2.txt
        theDirectory : path to the directory containing the files
        theName      : string at the beginning of the simple filename
        '''
##        lock = tsfl.TsFileLock(tsfl.TsFileLock.EVENTID)
##        lock.acquire()
        nextNumber = 1
        names = sorted(glob.glob(os.path.join(theDirectory,
                                       theName + '_*' + '.txt')))
        for name in names:
            nameWithoutExtension = os.path.splitext(name)[0]
            currentNumber = nameWithoutExtension[
                nameWithoutExtension.rfind('_') + 1:]
            nextNumber = int(currentNumber) + 1
        pathName = os.path.join(theDirectory,
                                '%s_%04d.txt' % (theName, nextNumber))
##        lock.release()
        return pathName

    #-----------------------------------------------------------------------
 
    @staticmethod
    def getSecondsTimeFromHoursMinutesSecondsString(timeString=None):
        '''
        Convert time from string to seconds format.
        '''
        seconds = 0
        if timeString is not None:
            timeList = timeString.split(':')
            for entry in timeList:
                if not entry.isdigit():
                    raise tse.ProgramException(
                        tse.ARGUMENT_VALUE_NOT_VALID,
                        'time invalid: %s' % timeString)
            timeListLength = len(timeList)
            if timeListLength == 3:
                seconds = (int(timeList[0]) * 60 * 60) + \
                          (int(timeList[1]) * 60) + (int(timeList[2]))
            elif timeListLength == 2:
                seconds = (int(timeList[0]) * 60) + (int(timeList[1]))
            elif timeListLength == 1:
                seconds = int(timeList[0])
            else:
                raise tse.ProgramException(tse.ARGUMENT_VALUE_NOT_VALID,
                                           'time invalid: %s' % timeString)

        return seconds

    #-----------------------------------------------------------------------

    @staticmethod
    def getSeparatorString(title=None,
                           indent=0,
                           position=layout['TitleCenter'],
                           separatorCharacter='-',
                           tab=4):
        '''
        Construct a string of title and white space to separate one section
        of text from another.
        '''
        tsru = TsReportUtilities
        indentOffset = ' ' * (tab * indent)

        if title is None:
            # The title line will consist of a leading blank line, separator
            # characters and atrailing blank line.
            text = '\n' + \
                   indentOffset + \
                   separatorCharacter * \
                   (tsru.layout['TitleWidth'] - indent) + '\n'

        else:
            # The title line will consist of leading blank line and separator
            # characters, the specified title text and trailing separator
            # characters and a blank line.
            #
            # The size of the leader, title and trailer length is the
            # TitleWidth minus the two spaces.
            #
            # The leader length is half of the limit length unless a smaller
            # position has been specified.
            #
            # The trailer length completes the remainder of the TitleWidth.
            theTitle = title
 
            limit = tsru.layout['TitleWidth'] - 2 - (indent * tab)
 
            length = len(tsru.layout['TitlePrefix']) + \
                     len(theTitle) + \
                     len(tsru.layout['TitleSuffix'])
 
            leader = int(min(position, (limit - length) // 2))
            trailer = int(limit - (leader + length))
 
            text = '\n' + \
                   indentOffset + \
                   separatorCharacter * leader + \
                   '%s%s%s' % (tsru.layout['TitlePrefix'],
                               theTitle,
                               tsru.layout['TitleSuffix']) + \
                   separatorCharacter * trailer + \
                   '\n'
 
        return (text.rstrip())

    #-----------------------------------------------------------------------

    @staticmethod
    def getStatisticsList(startupTime,
                          currentTime,
                          numberOfTestRuns,
                          numberOfTestPasses,
                          numberOfTestFailures):
        '''
        Create test summary after elapesed time and statistics details
        on the number of test runs, number of passing test runs, number
        of failing test runs, startup timestamp, shutdown timestamp
        and elapsed timesrtamp.
        '''
        tsru = TsReportUtilities
        if numberOfTestFailures > 0:
            resultsMessage = 'FAILED'
        elif numberOfTestPasses > 0:
            resultsMessage = 'PASSED'
        else:
            resultsMessage = 'UNKNOWN'

        elapsedTime = tsru.getElapsedTimeString(startupTime,
                                                currentTime)

        text = '\nTest Summary: %s after %s' % (resultsMessage,
                                                elapsedTime)

        text += '\n     Details: Runs %d, Passes %d, Failures %d' % \
                (numberOfTestRuns,
                 numberOfTestPasses,
                 numberOfTestFailures)
 
        text += tsru.getTimeStatisticsList(startupTime,
                                           currentTime)
        return text

    #-----------------------------------------------------------------------

    @staticmethod
    def getTimeStatisticsList(startupTime, currentTime):
        '''
        Generate Startup, Current (or Shutdown) and Elapsed Time strings.
        '''
        tsru = TsReportUtilities
        text = '\n'
        text += '              Started %s\n' % \
                tsru.getHourMinuteSecondString(startupTime)
 
        text += '              Ended   %s\n' % \
                tsru.getHourMinuteSecondString(currentTime)
 
        text += '              Elapsed %s\n' % \
                tsru.getElapsedTimeString(startupTime,
                                          currentTime)

        return text

    #-----------------------------------------------------------------------

    @staticmethod
    def getYearMonthDayString(seconds):
        '''
        Construct date string (in "Year-Month-Day" format) from time in seconds
        since UNIX epoch.
        '''
        return time.strftime('%Y-%m-%d', time.localtime(seconds))

#--------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
