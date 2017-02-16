#! /usr/bin/env python
#"Time-stamp: <02/24/2015  4:49:51 AM rsg>"
'''
tsLogger.py - Class that emulates a subset of Python logging
API. It defines and handles prioritized, time and date stamped
event message formatting and output to files and devices. Files
are organized in a date and time stamped directory named for the
launched application. Unix-type devices include syslog, stderr,
stdout and stdscr (the ncurses display screen). It also supports
"wxPython"-style logging of assert and check case results.
'''
#################################################################
#
# File: tsLogger.py
#
# Purpose:
#
#    Class that emulates a subset of Python logging API. It
#    defines and handles prioritized, time and date stamped
#    event message formatting and output to files and devices.
#    Files are organized in a date and time stamped directory
#    named for the launched application. Unix-type devices
#    include syslog, stderr, stdout and stdscr (the ncurses
#    display screen). It also supports "wxPython"-style logging
#    of assert and check case results.
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
#     from tsLogger import TsLogger as Logger
#
#     ## Instantiate Module with NO default parameters
#     myLogger = Logger(threshold=Logger.DEBUG,
#                       start=previous_time(from time.time()),
#                       name='./myError.log')
#
#     ## Instantiate Module with all default parameters
#     myLogger = Logger() # with threshold=Logger.INFO
#                         # with start=current_time(from time.time())
#                         # with name=Logger.StandardOutputFile (from argv(0))
#
#     ## Instantiate Module with only default threshold and name parameters
#     myLogger = Logger(start=previous_time(from time.time()))
#
#     ## Instantiate Module with only default start and name parameters
#     myLogger = Logger(threshold=Logger.ERROR)
#
#     ## Instantiate Module for description with NO default parameters
#     myLogger = Logger(threshold=Logger.DEBUG,
#                       start=previous_time(from time.time()),
#                       name='myPlatform.log',
#                       width=132,
#                       break_long_words=True,
#                       expand_tabs=True,
#                       file_footer='End Host OS Features',
#                       file_header='Start Host OS Features',
#                       fix_sentence_endings=True,
#                       initial_indent=20,
#                       replace_whitespace=True,
#                       subsequent_indent=)
#
#     ## Reference Module Methods
#     myLogger.log(Logger.ERROR, 'Timeout. Remote Host not available.')
#     myLogger.error('Timeout. Remote Host not available.')
#
# OVERVIEW
#
# Events may be assigned a severity level and sent to the
# specified logger in the form of a text string. The message
# can be formatted as appropriate.
#
# Severity levels have pre-assigned priorities typically
# applied as follows:
#
# +----------+--------------+-----------------------------------+
# | SEVERITY | PRIORITY     | APPLICATION                       |
# +----------+--------------+-----------------------------------+
# | NOTSET   | 0 (None)     | Indication that severity has not  |
# |          | No           | been specified by application.    |
# |          | Details      | logger.notset is NOT available.   |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'NOT Available'           |
# |          |              |   logger.notset(msg)              |
# +----------+--------------+-----------------------------------+
# | PRIVATE  | 1 (Min)      | Option used to surpress console   |
# |          | Unlimited    | output of data intended only to   |
# |          | Details      | be archived in a file.            |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'memory dump:' + \        |
# |          |              |    '%s' % str(dump)               |
# |          |              |   logger.private(msg)             |
# +----------+--------------+-----------------------------------+
# | DEBUG    | 10           | Option used to communicate        |
# |          | Lowest Usable| troubleshooting information to    |
# |          | Details      | the system operator.              |
# |          |              |                                   |
# |          |              | Detailed information, typically   |
# |          |              | of interest only when diagnosing  |
# |          |              | problems.                         |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Should Water Temp' + \   |
# |          |              |    'erature be over 130 degrees?' |
# |          |              |   logger.debug(msg)               |
# +----------+--------------+-----------------------------------+
# | INFO     | 20           | Option used to communicate        |
# |          | Progress     | progress information to the system|
# |          | Details      | operator.                         |
# |          |              |                                   |
# |          |              | Confirmation that things are      |
# |          |              | working as expected.              |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Water Temperature ' + \  |
# |          |              |    'between 120-129 degrees.'     |
# |          |              |   logger.info(msg)                |
# +----------+--------------+-----------------------------------+
# | NOTICE   | 25           | Option used to communicate        |
# |          | Milestone    | milestone information to the      |
# |          | Details      | system operator.                  |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Water Temperature ' + \  |
# |          |              |    'reached 130 degrees.'         |
# |          |              |   logger.notice(msg)              |
# +----------+--------------+-----------------------------------+
# | WARNING  | 30           | Used by default for anticipated,  |
# |          | Pre-Alarm    | recoverable pre-alarm conditions  |
# |          | Details      | which ought to be brought to the  |
# |          |              | attention of the system operator. |
# |          |              |                                   |
# |          |              | An indication that something      |
# |          |              | unexpected happened, or indica-   |
# |          |              | tive of some problem in the near  |
# |          |              | future (e.g. "disk space low".    |
# |          |              | The software is still working as  |
# |          |              | expected.                         |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Water Temperature ' + \  |
# |          |              |    'over 130 degrees.'            |
# |          |              |   logger.warning(msg)             |
# +----------+--------------+-----------------------------------+
# | ALERT    | 35           | Used by default for anticipated,  |
# |          | Alarm        | recoverable alarm conditions      |
# |          | Details      | which ought to be brought to the  |
# |          |              | attention of the system operator. |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Water Temperature ' + \  |
# |          |              |    'between 131-139 degrees.'     |
# |          |              |   logger.alert(msg)               |
# +----------+--------------+-----------------------------------+
# | ERROR    | 40           | Used for unexpected, non-recover- |
# |          | Failure      | able failures which need to be    |
# |          | Details      | communicated to the system        |
# |          |              | operator.                         |
# |          |              |                                   |
# |          |              | Due to a more serious problem,    |
# |          |              | the software has not been able    |
# |          |              | to perform some function.         |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Sensor Failed. ' + \     |
# |          |              |    'Water Temperature not ' + \   |
# |          |              |    'in range of 32-212 degrees'   |
# |          |              |   logger.error(msg)               |
# +----------+--------------+-----------------------------------+
# | CRITICAL | 50           | Used for urgent, non-recoverable  |
# |          | Damage       | operating situations (coolant     |
# |          | Related      | leak) which need to be commun-    |
# |          | Details      | icated to the system operator.    |
# |          |              |                                   |
# |          |              | A serious error, indicating that  |
# |          |              | the program itself may be unable  |
# |          |              | to continue running.              |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Thermostat failed. ' + \ |
# |          |              |    'Water Temperature over ' + \  |
# |          |              |    '140 degrees.'                 |
# |          |              |   logger.critical(msg)            |
# +----------+--------------+-----------------------------------+
# | EMERGENCY| 55           | Used for urgent, non-recoverable  |
# |          | Safety       | operating situations (primary     |
# |          | Related      | power loss) which need to be com- |
# |          | details      | municated to the system operator. |
# |          |              |                                   |
# |          |              | Example:                          |
# |          |              |   msg = 'Primary AC Power ' + \   |
# |          |              |    'Supply failed. Shut' + \      |
# |          |              |    'down system before  ' + \     |
# |          |              |    'Backup Battery runs out ' + \ |
# |          |              |    'in 10 minutes.'               |
# |          |              |   logger.emergency(msg)           |
# +----------+--------------+-----------------------------------+
#
#################################################################
#
# Assertion handlers: check if the condition is true and call
# assert handler (which will by default notify the user about
# failure) if it is not.
#
# wxASSERT and wxFAIL handlers as well as wxTrap() function do
# nothing at all if wxDEBUG_LEVEL is 0 however they do check
# their conditions at default debug level 1, unlike the previous
# wxWidgets versions.
#
# wxASSERT_LEVEL_2 is meant to be used for "expensive" asserts
# which should normally be disabled because they have a big
# impact on performance and so this macro only does anything if
# wxDEBUG_LEVEL >= 2.
#
# wxCHECK handlers always check their conditions, setting debug
# level to 0 only makes them silent in case of failure, otherwise
# -- including at default debug level 1 -- they call the assert
# handler if the condition is false
#
# They are supposed to be used only in invalid situation: for
# example, an invalid parameter (e.g. a NULL pointer) is passed
# to a function. Instead of dereferencing it and causing core dump
# the function might use:
#
#      wxCHECK_RET( p != NULL, "pointer ca not be NULL" )
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
#   2008/01/23 rsg  Added logic to flush output to log file.
#
#   2010/05/08 rsg  Redesigned for tsWxGraphicalTextUserInterface.
#                   Removed concurrent output to stdout/stderr
#                   when logger dedicated to file output so as
#                   to not corrupt curses stdscr.
#                   Converted some global variables to class
#                   variables to eliminate import dependencies
#                   such as tsWxGlobals and tsApplication.
#
#   2010/05/08 rsg  Added applicationName as prefix to log file
#                   names.
#
#   2010/06/23 rsg  Added 'stdscr' to list of devices to support
#                   wxPython output to redirection window..
#
#   2011/01/25 rsg  Added assert and check result output handlers
#                   to support wxPython.
#
#   2011/11/23 rsg  Clarified description of logger severity
#                   levels. Added examples.
#
#   2011/11/23 rsg  Clarified description of logger severity
#                   levels. Added examples.
#
#   2013/06/26 rsg  Added Vinay Sajip to Python logging copyright.
#
#   2013/06/29 rsg  Re-designed class "TsLogger" to facilitate
#                   maintenance by inheriting features of newly
#                   created "localLogger" and "wxPythonAsserts"
#                   classes and their relocated components.
#
#   2013/08/19 rsg  Clarified description of the TSLogger class.
#
#   2013/11/13 rsg  Re-assigned Private severity level from 60 to
#                   1 because nothing should be higher than
#                   CRITICAL OR EMERGENCY.
#
# ToDo:
#
#   1. Methods should support *args and **kw.
#
#################################################################

__title__     = 'tsLogger.py'
__version__   = '2.2.0'
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

import errno as Errno
import os.path
import sys
import time
from textwrap import TextWrapper

try:
    import thread
    import threading
except ImportError:
    thread = None

try:

    import logging
    import logging.handlers
    import logging.config
    _PythonLogging = True

except ImportError, importCode:

    _PythonLogging = False
    print('%s: ImportError (PythonLogging); ' % __title__ + \
          'importCode=%s' % str(importCode))

try:
    import syslog
    syslogAvailable = True
except ImportError, e:
    syslogAvailable = False
##    msg = 'Import Error: %s' % str(e)
##    raise tse.ProgramException(
##        tse.OS_ERROR, msg)

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    from tsReportUtilities import TsReportUtilities as tsru

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

__all__ = [
    'ALERT',
    'CRITICAL',
    'DEBUG',
    'DEBUG_TRACE_LEVEL',
    'DummyLogger',
    'EMERGENCY',
    'ERROR',
    'INFO',
    'NOTICE',
    'NOTSET',
    'PRIVATE',
    'StandardErrorDevice',
    'StandardOutputDevice',
    'StandardOutputFile',
    'SystemLogDevice',
    'TsLogger',
    'WARNING',
    'alert',
    'critical',
    'debug',
    'description',
    'emergency',
    'error',
    'event',
    'exception',
    'info',
    'log',
    'notice',
    'progress',
    'warning']

StandardOutputFile   = ''
StandardOutputDevice = 'stdout'
StandardErrorDevice  = 'stderr'
StandardScreenDevice = 'stdscr'
SystemLogDevice      = 'syslog'

_deviceList = [
    StandardOutputFile,
    StandardOutputDevice,
    StandardErrorDevice,
    StandardScreenDevice,
    SystemLogDevice]

_consoleList = [StandardOutputDevice,
                StandardErrorDevice,
                StandardScreenDevice]

TROUBLE_SHOOTING_DEBUG = False # Note: DEBUG reserved for severity level.

# The following defines severity levels which may be used as
# a threshold filter for console output.
NOTSET        = 0
DEBUG         = 10
INFO          = 20
NOTICE        = INFO + 5
WARNING       = 30
ALERT         = WARNING + 5
ERROR         = 40
CRITICAL      = 50
EMERGENCY     = CRITICAL + 5

# The following defines a pseudo level which may be used to add stack
# backtrace to console output.
DEBUG_TRACE_LEVEL = DEBUG - 5

# The following defines a pseudo level which may be used to surpress
# console output.
PRIVATE       = NOTSET + 1
PRIVATENAME   = 'PRIVATE'

LOG_PATH      = "./"
LOG_NAME      = "message"
LOG_EXTENSION = ".log"
APPEND        = "a"
TRUNCATE      = "w"
DEFAULT_LOG_FILE_MODE = TRUNCATE

# The following dictionary is alphabetical
threshold = {
    ALERT: ALERT,
    CRITICAL: CRITICAL,
    DEBUG: DEBUG,
    EMERGENCY: EMERGENCY,
    ERROR: ERROR,
    INFO: INFO,
    NOTICE: NOTICE,
    NOTSET: NOTSET,
    PRIVATE: PRIVATE,
    WARNING: WARNING
    }

# The following dictionary is alphabetical
category = {
    ALERT: 'ALERT',
    CRITICAL: 'CRITICAL',
    DEBUG: 'DEBUG',
    EMERGENCY: 'EMERGENCY',
    ERROR: 'ERROR',
    INFO: 'INFO',
    NOTICE: 'NOTICE',
    NOTSET: 'NOTSET',
    PRIVATE: 'PRIVATE',
    WARNING: 'WARNING'
    }

# The following dictionary is alphabetical
if syslogAvailable:
    # The following definitions support syslog
    syslogMap = {
        ALERT: syslog.LOG_ALERT,
        CRITICAL: syslog.LOG_CRIT,
        DEBUG: syslog.LOG_DEBUG,
        EMERGENCY: syslog.LOG_EMERG,
        ERROR: syslog.LOG_ERR,
        INFO: syslog.LOG_INFO,
        NOTICE: syslog.LOG_NOTICE,
        NOTSET: syslog.LOG_INFO,
        PRIVATE: syslog.LOG_INFO,
        WARNING: syslog.LOG_WARNING
        }

#---------------------------------------------------------------------------
#   Level-related stuff (from: Python logging module.
#---------------------------------------------------------------------------

# The following defines the textual representation of logging level 'level'.
# If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
# INFO, DEBUG) then you get the corresponding string. If you have
# associated levels with names using addLevelName then the name you have
# associated with 'level' is returned.
#
# If a numeric value corresponding to one of the defined levels is passed
# in, the corresponding string representation is returned.
_levelNames = {
    ALERT: 'ALERT',
    CRITICAL: 'CRITICAL',
    DEBUG: 'DEBUG',
    DEBUG_TRACE_LEVEL: 'DEBUG_TRACE_LEVEL',
    EMERGENCY: 'EMERGENCY',
    ERROR: 'ERROR',
    INFO: 'INFO',
    NOTICE: 'NOTICE',
    NOTSET: 'NOTSET',
    PRIVATE: 'PRIVATE',
    WARNING: 'WARNING',
    'ALERT': ALERT,
    'CRITICAL': CRITICAL,
    'DEBUG': DEBUG,
    'DEBUG_TRACE_LEVEL': DEBUG_TRACE_LEVEL,
    'EMERGENCY': EMERGENCY,
    'ERROR': ERROR,
    'INFO': INFO,
    'NOTICE': NOTICE,
    'NOTSET': NOTSET,
    'PRIVATE': PRIVATE,
    'WARNING': WARNING}

#---------------------------------------------------------------------------

def getLevelName(level):
    '''
    Return the textual representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    Otherwise, the string "Level %s" % level is returned.
    '''
    return _levelNames.get(level, ("Level %s" % level))

#---------------------------------------------------------------------------

def addLevelName(level, levelName):
    '''
    Associate "levelName" with "level".

    This is used when converting levels to text during message formatting.
    '''
    _acquireLock()
    try:    #unlikely to cause an exception, but you never know...
        _levelNames[level] = levelName
        _levelNames[levelName] = level
    finally:
        _releaseLock()

#---------------------------------------------------------------------------

def _checkLevel(level):
    if isinstance(level, int):
        rv = level
    elif str(level) == level:
        if level not in _levelNames:
            raise ValueError("Unknown level: %r" % level)
        rv = _levelNames[level]
    else:
        raise TypeError(
            "Level not an integer or a valid string: %r" % level)
    return rv

#---------------------------------------------------------------------------
#   Thread-related stuff (from: Python logging module.
#---------------------------------------------------------------------------

#
#_lock is used to serialize access to shared data structures in this
# module.
#
# This needs to be an RLock because fileConfig() creates and configures
# Handlers, and so might arbitrary user threads. Since Handler code
# updates the shared dictionary _handlers, it needs to acquire the lock.
# But if configuring, the lock would already have been acquired - so we
# need an RLock.
# The same argument applies to Loggers and Manager.loggerDict.
#
if thread:
    _lock = threading.RLock()
else:
    _lock = None

#---------------------------------------------------------------------------

def _acquireLock():
    """
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    """
    if _lock:
        _lock.acquire()

#---------------------------------------------------------------------------

def _releaseLock():
    """
    Release the module-level lock acquired by calling _acquireLock().
    """
    if _lock:
        _lock.release()

#---------------------------------------------------------------------------

class localLogger(object):
    '''
    Class, that emulates a subset of Python logging API, to define and
    handle prioritized, time and date stamped event message formatting
    and output to files, syslog, stderr, stdout and stdscr (ncurses
    display screen). It also supports "wxPython"-style logging of
    assert and check case results.
    '''
##    activeLoggerIDs = {}
##    activeLoggerIDs['name'] = 'activeLoggerIDs'
##    argv = sys.argv

##    fileLabel = tsru.getDateTimeString(time.time(),
##                                       msec=False,
##                                       filename=True)

##    (head, tail) = os.path.split(argv[0])
##    if head == '':
##        mkdirsHead = './logs/%s' % fileLabel
##        mkdirsMode = 0777
##    else:
##        mkdirsHead = '%s/logs/%s' % (head, fileLabel)
##        mkdirsMode = 0777

##    try:
##        os.makedirs(mkdirsHead, mkdirsMode)
##    except Exception, e:
##        sys.stderr.write('EXCEPTION: <%s>' % str(e))

##    msg = ['Unable to create default log file.']

##    (fileName, fileExt) = os.path.splitext(tail)
##    applicationName = fileName

##    for path in [mkdirsHead, head]:

##        defaultStandardOutputFileName = '%s/%s.log' % (mkdirsHead, fileName)

##        defaultStandardOutputFileID = None

##      try:

##          defaultStandardOutputFileID = open(
##              defaultStandardOutputFileName,
##              DEFAULT_LOG_FILE_MODE)

##          defaultStandardOutputPath = path
##          print(str(defaultStandardOutputFileID))
##          break

##      except Exception, e:

##          if True or TROUBLE_SHOOTING_DEBUG:
##              fmt1 = '\nFailed : head=<%s>; ' % mkdirsHead
##              fmt2 = 'tail=<%s>; ' % tail
##              fmt3 = 'fileName=<%s>; ' % defaultStandardOutputFileName
##              fmt4 = 'e=<%s>' % str(e)
##              msg += [fmt1 + fmt2 + fmt3 + fmt4]
##              print(msg)

##          defaultStandardOutputFileID = None

##    if defaultStandardOutputFileID is None:

##      sys.stderr.write(str(msg))
##      raise tse.InputOutputException(
##          tse.IO_ERROR, str(msg))

##    print('\nNo Error')
##    sys.exit(0)

    #-----------------------------------------------------------------------

    def __init__(self, **kw):
        '''
        Initialze the class.
        '''
        self.applicationName = TsLogger.applicationName
        self.break_long_words = True
        self.expand_tabs = True
        self.fix_sentence_endings = False
        self.initial_indent = ''
        self.name = StandardOutputFile
        self.replace_whitespace = True
        self.subsequent_indent = ''
        self.theFileFooter = ''
        self.theFileHeader = ''
        self.theStartTime = time.time()
        self.theThreshold = INFO
        self.thisLogID = None
        self.thisLogName = None
        self.thisRegisteredName = None
        self.width = 80 - 2

        for key in list(kw.keys()):

            if key == 'name':
                self.thisLogName = kw[key]
                self.name = self.thisLogName
                if self.thisLogName in list(TsLogger.activeLoggerIDs.keys()):
                    self.thisLogID = TsLogger.activeLoggerIDs[
                        self.thisLogName]

                elif self.thisLogName == StandardOutputDevice:
                    self.thisLogID = sys.stdout
                    self.thisLogID.flush()
                    TsLogger.activeLoggerIDs[
                            self.thisLogName] = self.thisLogID

                elif self.thisLogName == StandardErrorDevice:
                    self.thisLogID = sys.stderr
                    self.thisLogID.flush()
                    TsLogger.activeLoggerIDs[
                            self.thisLogName] = self.thisLogID

                elif self.thisLogName == StandardScreenDevice:
                    self.thisLogID = None
                    TsLogger.activeLoggerIDs[
                            self.thisLogName] = self.thisLogID

                else:
                    try:
                        (self.thisLogName, self.thisLogID) = self.open(
                            self.thisLogName, DEFAULT_LOG_FILE_MODE)
                        TsLogger.activeLoggerIDs[
                            self.thisLogName] = self.thisLogID
                    except Exception, e:
                        self.thisLogID = None
                        fmt1 = 'Exception: thisLogName=<%s>; ' % \
                               self.thisLogName
                        fmt2 = 'thisLogID=<%s>; e=<%s>' % \
                               (self.thisLogID, str(e))
                        print(fmt2 + fmt2)
                        self.thisLogName = StandardOutputDevice
                        self.thisLogID = sys.stdout
                        TsLogger.activeLoggerIDs[
                            self.thisLogName] = self.thisLogID

                if self.thisLogName == StandardOutputFile:
                    theLogName = TsLogger.defaultStandardOutputFileName
                else:
                    theLogName = self.thisLogName
                self.thisRegisteredName = theLogName

            elif key == 'width':
                self.width = kw[key]

            elif key == 'expand_tabs':
                self.expand_tabs = kw[key]

            elif key == 'replace_whitespace':
                self.replace_whitespace = kw[key]

            elif key == 'initial_indent':
                self.initial_indent = kw[key]

            elif key == 'subsequent_indent':
                self.subsequent_indent = kw[key]

            elif key == 'fix_sentence_endings':
                self.fix_sentence_endings = kw[key]

            elif key == 'break_long_words':
                self.break_long_words = kw[key]

            elif key == 'threshold':
                self.theThreshold = threshold[kw[key]]

            elif key == 'start':
                self.theStartTime = float(kw[key])

            elif key == 'file_header':
                self.theFileHeader = kw[key]

            elif key == 'file_footer':
                self.theFileFooter = kw[key]

        self.theWrapper = TextWrapper(width = \
                                      self.width - \
                                      len(self.subsequent_indent),
 
                                      expand_tabs = self.expand_tabs,
 
                                      replace_whitespace = \
                                      self.replace_whitespace,
 
                                      initial_indent = \
                                      self.initial_indent,
 
                                      subsequent_indent = \
                                      self.subsequent_indent,
                                      
                                      fix_sentence_endings = \
                                      self.fix_sentence_endings,
                                      
                                      break_long_words = \
                                      self.break_long_words)

    #-----------------------------------------------------------------------

    def alert(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ALERT'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem",
        exc_info = 1)
        '''
        self._log(*(ALERT, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def critical(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(CRITICAL, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def debug(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem",
        exc_info = 1)
        '''
        self._log(*(DEBUG, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def description(self,
                    message,
                    title=None,
                    level=NOTSET,
                    width=80,
                    initial_indent='',
                    subsequent_indent='',
                    indent=0,
                    tab=4):
        '''
        Output timestamped message on new line.
        '''
        if (self.theThreshold <= level) or \
           (level == NOTSET):
            self._output(tsru.getSeparatorString(title = self.theFileHeader,
                                                 separatorCharacter = '=',
                                                 position = 4,
                                                 indent = 0,
                                                 tab = 4),
                         level = level)

            timestamp = tsru.getDateTimeString(time.time())
            record = '%s %9.9s' % (timestamp, category[level])

            theBeginTitle = 'Begin "%s"' % title
            theEndTitle = 'End "%s"' % title
            theHeader = '%s\n' % \
                        tsru.getSeparatorString(title = theBeginTitle,

                                                separatorCharacter = '-',

                                                position = \
                                                tsru.layout['TitleCenter'],

                                                indent = indent,

                                                tab = tab)
            theFooter = '%s\n' % \
                        tsru.getSeparatorString(title = theEndTitle,

                                                separatorCharacter = '-',

                                                position = \
                                                tsru.layout['TitleCenter'],

                                                indent = indent,

                                                tab = tab)

            self._output(record, level = level)

            self._output(theHeader, level = level)

            for theLine in message:
                paragraphs = theLine.split('\n\n')
                for paragraph in paragraphs:
                    if paragraph == '':
                        self._output('', level = level)
                    else:
                        for aLine in self.theWrapper.wrap(paragraph):
                            self._output(aLine, level = level)

            self._output(theFooter, level = level)

            self._output(tsru.getSeparatorString(title = self.theFileFooter,
                                                 separatorCharacter = '=',
                                                 position = 4,
                                                 indent = 0,
                                                 tab = 4),
                         level = level)

    #-----------------------------------------------------------------------

    def emergency(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'EMERGENCY'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(EMERGENCY, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def error(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info = 1)
        '''
        self._log(*(ERROR, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def event(self, message, level=NOTSET):
        '''
        Output timestamped message on new line.
        '''
        if (self.theThreshold <= level) or \
           (level == NOTSET):
            timestamp = tsru.getDateTimeString(time.time(), msec = True)
            record = '%s %9.9s %s' % (timestamp, category[level], message)
            self._output(record, level = level)
            time.sleep(1.0-0.002)

    #-----------------------------------------------------------------------

    def exception(self, msg, *args):
        '''
        Convenience method for logging an ERROR with exception information.
        '''
        self.error(*(msg,) + args, **{'exc_info': 1})

    #-----------------------------------------------------------------------

    def info(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem",
        exc_info = 1)
        '''
        self._log(*(INFO, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def _log(self, level, msg, args, exc_info = None, extra = None):
        '''
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        '''
        if self.theThreshold <= level:
            timestamp = tsru.getDateTimeString(time.time(), msec=True)

            try:
                theCategory = category[level]
            except Exception, e:
                theCategory = 'NOTSET'

            record = '%s %9.9s: %s' % (timestamp, theCategory, msg)
            self._output(record, level=level)

    #-----------------------------------------------------------------------

    def log(self, level, msg, *args, **kwargs):
        '''
        Log 'msg % args' with the integer severity 'level'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.log(level, "We have a %s", "mysterious problem", exc_info = 1)
        '''
        if not isinstance(level, int):
            raise tse.ProgramException(tse.ARGUMENT_TYPE_NOT_VALID,
                                       'Expected=%s; Actual=%s.' % \
                                       (int, type(level)))

        if level >= self.theThreshold:
            self._log(*(level, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def notice(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'NOTICE'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem",
        exc_info = 1)
        '''
        self._log(*(NOTICE, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def warning(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem",
        exc_info = 1)
        '''
        self._log(*(WARNING, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def close(self):
        '''
        Close access with self named device or file.
        '''
        if (self.thisLogName != TsLogger.defaultStandardOutputFileName) and \
           (self.thisLogName not in _deviceList):

            if TROUBLE_SHOOTING_DEBUG:
                print('Starting close: name=<%s>' % self.thisLogName)

            self.thisLogID.close()

            if TROUBLE_SHOOTING_DEBUG:
                print('Ending close: name=<%s>' % self.thisLogName)

    #-----------------------------------------------------------------------

    def open(self, name, mode):
        '''
        Create access with named device or file. NOTE: Must not be
        used for StandardScreenDevice.
        '''
        if TROUBLE_SHOOTING_DEBUG:
            print('Starting open: name=<%s>; mode=<%s>' % (name, mode))

        try:
            if name == StandardOutputDevice:
                deviceName = name
                deviceID = sys.stdout

            elif name == StandardErrorDevice:
                deviceName = name
                deviceID = sys.stderr

            elif name == SystemLogDevice and syslogAvailable:

                # Logging options other than the defaults can be set by
                # explicitly opening the log file with openlog() prior to
                # calling syslog(). The defaults are (usually) ident = 'syslog',
                # logopt = 0, facility = LOG_USER. The ident argument is a
                # string which is prepended to every message. The optional
                # logopt argument is a bit field - see below for possible
                # values to combine. The optional facility argument sets
                # the default facility for messages which do not have a
                # facility explicitly encoded.

                if False:
                    ident = 'syslog'
                    logopt = 0
                    facility = syslog.LOG_USER
                    syslog.openlog(ident, logopt, facility)

                deviceName = name
                deviceID = syslog.syslog

            elif name == StandardOutputFile:

                deviceName = TsLogger.defaultStandardOutputFileName
                deviceID = TsLogger.defaultStandardOutputFileID

            else:

                head = TsLogger.defaultStandardOutputPath
                (pseudoHead, tail) = os.path.split(name)
                if True:
                    deviceName = '%s/%s' % (
                        head,
                        tail)
                else:
                    deviceName = '%s/%s-%s' % (
                        head,
                        TsLogger.applicationName,
                        tail)
                deviceID = open(deviceName, mode)

        except OSError, (errno, strerror):
            # Substitute stdout.
            deviceName = StandardOutputDevice
            deviceID = sys.stdout
            if errno != Errno.EEXIST:
                msg = 'open: Name=<%s>; Errno=<%s>: Strerror=<%s>.' % \
                      (name, str(errno), str(strerror))
                if TROUBLE_SHOOTING_DEBUG:
                    print('EXCEPTION: %s' % msg)
                else:
                    raise tse.ProgramException(tse.OS_ERROR, msg)

        except IOError, (errno, strerror):
            # Substitute stdout.
            deviceName = StandardOutputDevice
            deviceID = sys.stdout
            if errno != Errno.ENOENT:
                msg = 'open: Name=<%s>; Errno=<%s>: Strerror=<%s>.' % \
                      (name, str(errno), str(strerror))
                if TROUBLE_SHOOTING_DEBUG:
                    print('EXCEPTION: %s' % msg)
                else:
                    raise tse.InputOutputException(tse.IO_ERROR, msg)

        if TROUBLE_SHOOTING_DEBUG:
            print('Ending open: name=<%s>; mode=<%s>' % (name, mode))

        return (deviceName, deviceID)

    #-----------------------------------------------------------------------

    def _output(self, text, level=NOTSET, newline=True):
        '''
        Output message to console and/or file.
        '''
        if newline:
            message = text + '\n'
        else:
            message = text

        if NOTSET < level and \
           level >= self.theThreshold and \
           level <= EMERGENCY:

            if self.thisLogName == SystemLogDevice:
                self.thisLogID(syslogMap[level] | syslog.LOG_USER, message)

            elif self.thisLogID is not None:
                # Send to file
                self.thisLogID.write(message)
                self.thisLogID.flush()

            else:
                # Use print function, with timestamp, when tsWxPkg
                # or wxPython redirects output to window on screen
                print(message)

    #-----------------------------------------------------------------------

    def progress(self, message, level=NOTSET):
        '''
        Output timestamped message on same line.
        NOTE: Only outputs to same line.
        '''
        timestamp = tsru.getDateTimeString(time.time())
        record = '\r%s %9.9s %s' % (timestamp, category[level], message)
        self._output(record, level = level, newline = False)

    #-----------------------------------------------------------------------

    def getLogger(self, name):
        """
        Get a logger with the specified name (channel name), creating it
        if it doesn't yet exist. This name is a dot-separated hierarchical
        name, such as "a", "a.b", "a.b.c" or similar.

        If a PlaceHolder existed for the specified name [i.e. the logger
        didn't exist but a child of it did], replace it with the created
        logger and fix up the parent/child references which pointed to the
        placeholder to now point to the logger.
        """
        rv = None
        if not isinstance(name, basestring):
            raise TypeError('A logger name must be string or Unicode')
        if isinstance(name, unicode):
            name = name.encode('utf-8')
        _acquireLock()
        try:
            if name in self.loggerDict:
                rv = self.loggerDict[name]
                if isinstance(rv, PlaceHolder):
                    ph = rv
                    rv = (self.loggerClass or _loggerClass)(name)
                    rv.manager = self
                    self.loggerDict[name] = rv
                    self._fixupChildren(ph, rv)
                    self._fixupParents(rv)
            else:
                rv = (self.loggerClass or _loggerClass)(name)
                rv.manager = self
                self.loggerDict[name] = rv
                self._fixupParents(rv)
        finally:
            _releaseLock()
        return rv

#---------------------------------------------------------------------------

class wxPythonAsserts(object):
    '''
    Provides wxPython style asserts.
    '''
    def __init__(self):
        '''
        Class constructor.
        '''
        pass

    #-----------------------------------------------------------------------

    def wxASSERT(self, cond):
        '''
        assert checks if the condition is true and calls the assert handler
        with a default message if it is not

        NB: the macro is defined like this to ensure that nested if/else
        statements containing it are compiled in the same way whether
        it is defined as empty or not
        '''
        if (cond == True):
            pass
        else:
            msg = 'wxASSERT for cond (%s)' % cond
            self.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def wxASSERT_MSG(self, cond, msg=None):
        '''
        assert checks if the condition is true and calls the assert handler
        with the provided message if it is not

        NB: the macro is defined like this to ensure that nested if/else
        statements containing it are compiled in the same way whether
        it is defined as empty or not
        '''
        if (cond == True):
            pass
        else:
            self.error(msg)
            raise tse.ProgramException(
                tse.APPLICATION_TRAP,
                'wxASSERT_MSG for cond (%s); msg (%s)' % (cond, msg))

    #-----------------------------------------------------------------------
    def wxCHECK(self, cond, rc):
        '''
        check which returns with the specified return code if the condition
        fails
        '''
        if (cond == True):
            pass
        else:
            msg = 'wxCHECK for cond (%s); rc (%s)' % (cond, rc)
            self.warning(msg)
            return (rc)

    #-----------------------------------------------------------------------

    def wxCHECK_MSG(self, cond, rc, msg=None):
        '''
        check which returns with the specified return code if the condition
        fails
        '''
        if (cond == True):
            pass
        else:
            fmt = 'wxCHECK_MSG for cond (%s); rc (%s); msg=%s' % (
                cond, rc, msg)
            self.warning(fmt)
            return (rc)

    #-----------------------------------------------------------------------

    def wxCHECK_RET(self, cond, msg=None):
        '''
        special form of wxCHECK2: as wxCHECK, but for use in void functions

        NB: there is only one form (with msg parameter) and it is intentional:
        there is no other way to tell the caller what exactly went wrong
        from the void function (of course, the function should not be void
        to begin with...)
        '''
        if (cond == True):
            pass
        else:
            fmt = 'wxCHECK_RET for cond (%s); msg (%s)' % (
                cond, msg)
            self.error(fmt)

    #-----------------------------------------------------------------------

    def wxCHECK2(self, cond, op=None):
        '''
        check that expression is true, perform op if not
        '''
        if (cond == True):
            pass
        elif (op is not None):
            msg = 'wxCHECK2 for cond (%s); op (%s)' % (
                cond, op)
            self.error(msg)
            op()

    #-----------------------------------------------------------------------

    def wxCHECK2_MSG(self, cond, op=None, msg=None):
        '''
        the generic macro: takes the condition to check, the statement to
        be execute in case the condition is false and the message to pass
        to the assert handler
        '''
        if (cond == True):
            pass
        elif (op is not None):
            fmt = 'wxCHECK2_MSG for cond (%s); op (%s); msg (%s)' % (
                cond, op, msg)
            self.error(fmt)
            op()

    #-----------------------------------------------------------------------

    def wxFAIL(self):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        msg = 'wxFAIL for Normally Unreachable Code'
        self.error(msg)
        raise tse.ProgramException(
            tse.APPLICATION_TRAP,
            msg)

    #-----------------------------------------------------------------------

    def wxFAIL_COND_MSG(self, cond, msg=None):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        msg = 'wxFAIL_COND_MSG for Normally Unreachable Code; ' + \
              'cond (%s); msg (%s)' % (cond, msg)
        self.error(msg)
        raise tse.ProgramException(
            tse.APPLICATION_TRAP,
            msg)

    #-----------------------------------------------------------------------

    def wxFAIL_MSG(self, msg=None):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        msg = 'wxFAIL_MSG for Normally Unreachable Code; ' + \
              'msg (%s)' % msg
        self.error(msg)
        raise tse.ProgramException(
            tse.APPLICATION_TRAP,
            msg)

    #-----------------------------------------------------------------------

    def wxTRAP(self):
        '''
        wxTRAP is a special form of assert: it always triggers (and so is
        usually used in application trap handler code
        '''
        msg = 'wxTRAP for Application Code'
        self.error(msg)
        raise tse.ProgramException(
            tse.APPLICATION_TRAP,
            msg)

#---------------------------------------------------------------------------

class TsLogger(localLogger, wxPythonAsserts):
    '''
    Class that emulates a subset of Python logging API. It defines and
    handles prioritized, time and date stamped event message formatting
    and output to files and devices. Files are organized in a date and
    time stamped directory named for the launched application. Unix-type
    devices include syslog, stderr, stdout and stdscr (the ncurses display
    screen). It also supports "wxPython"-style logging of assert and
    check case results.
    '''
    activeLoggerIDs = {}
    activeLoggerIDs['name'] = 'activeLoggerIDs'
    argv = sys.argv

    fileLabel = tsru.getDateTimeString(time.time(),
                                       msec=False,
                                       filename=True)

    (head, tail) = os.path.split(argv[0])
    if head == '':
        mkdirsHead = './logs/%s' % fileLabel
        mkdirsMode = 0777
    else:
        mkdirsHead = '%s/logs/%s' % (head, fileLabel)
        mkdirsMode = 0777

    try:
        os.makedirs(mkdirsHead, mkdirsMode)
    except Exception, e:
        sys.stderr.write('EXCEPTION: <%s>' % str(e))

    msg = ['Unable to create default log file.']

    (fileName, fileExt) = os.path.splitext(tail)
    applicationName = fileName

    for path in [mkdirsHead, head]:

        defaultStandardOutputFileName = '%s/%s.log' % (mkdirsHead, fileName)

        defaultStandardOutputFileID = None

        try:

            defaultStandardOutputFileID = open(
                defaultStandardOutputFileName,
                DEFAULT_LOG_FILE_MODE)

            defaultStandardOutputPath = path
            print(str(defaultStandardOutputFileID))
            break

        except Exception, e:

            if True or TROUBLE_SHOOTING_DEBUG:
                fmt1 = '\nFailed : head=<%s>; ' % mkdirsHead
                fmt2 = 'tail=<%s>; ' % tail
                fmt3 = 'fileName=<%s>; ' % defaultStandardOutputFileName
                fmt4 = 'e=<%s>' % str(e)
                msg += [fmt1 + fmt2 + fmt3 + fmt4]
                for line in msg:
                    print(line)
            defaultStandardOutputPath = None
            defaultStandardOutputFileID = None

    if defaultStandardOutputFileID is None:

        msg = ['Unable to create default log file.']

        sys.stderr.write(str(msg))
        raise tse.InputOutputException(
            tse.IO_ERROR, str(msg))

##    print('\nNo Error')
##    sys.exit(0)

    #-----------------------------------------------------------------------

##    def __init__(self, **kw): # name, level=NOTSET):
    def __init__(self, **kw):
        '''
        Initialze the class.
        '''
        localLogger.__init__(self, **kw)

        wxPythonAsserts.__init__(self)

    #-----------------------------------------------------------------------

    def tsGetDefaultStandardOutputFileID(self):
        '''
        '''
        try:

            reply = TsLogger.defaultStandardOutputFileID

        except Exception, e:

            try:

                reply = TsLogger(threshold=ERROR,
                                 start=time.time(),
                                 name=StandardOutputFile)

            except Exception, e:

                msg = 'tsGetDefaultStandardOutputFileID: e=<%s>.' % \
                      str(e)
                if TROUBLE_SHOOTING_DEBUG:
                    print('EXCEPTION: %s' % msg)
                else:
                    raise tse.InputOutputException(tse.IO_ERROR, msg)

                reply = None

        return (reply)

    #-----------------------------------------------------------------------

    def tsGetLoggerPath(self):
        '''
        '''
        try:

            reply = TsLogger.defaultStandardOutputPath

        except Exception, e:

            msg = 'tsGetLoggerPath: e=<%s>.' % \
                  str(e)

            reply = None

            if TROUBLE_SHOOTING_DEBUG:
                print('EXCEPTION: %s' % msg)
            else:
                raise tse.InputOutputException(tse.IO_ERROR, msg)

        if reply is None:

            reply = './'

        return (reply)

    #-----------------------------------------------------------------------

    def tsGetLoggerName(self):
        '''
        '''
        return (self.thisLogName)

    #-----------------------------------------------------------------------

    def tsGetLoggerThreshold(self):
        '''
        '''
        return (self.theThreshold)

    #-----------------------------------------------------------------------
    # Properties

    appLogger = property(tsGetDefaultStandardOutputFileID)
    theLogName = property(tsGetLoggerName)
    theLogPath = property(tsGetLoggerPath)
    theLogThreshold = property(tsGetLoggerThreshold)

#---------------------------------------------------------------------------

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
            except Exception, propertyErrorCode:
                myLogger.error(
                    'propertyErrorCode="%s"' % propertyErrorCode)

        #-------------------------------------------------------------------

        def levelTest(myLogger):
            '''
            Verify logging for each level.
            '''
            availableLevels = [
                NOTSET,
                PRIVATE,
                # DEBUG_TRACE_LEVEL,
                DEBUG,
                INFO,
                NOTICE,
                WARNING,
                ALERT,
                ERROR,
                CRITICAL,
                EMERGENCY]

            if TROUBLE_SHOOTING_DEBUG:

                print('begin levelTest on <%s>' % myLogger.thisLogName)

            for level in availableLevels:

                levelName = getLevelName(level)

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
            for device in _deviceList:
                print('\n\t%s' % separator)
                myLogger = TsLogger(threshold=INFO,
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
                myLogger = TsLogger(threshold = NOTSET,
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
            myLogger = TsLogger(threshold = ERROR,
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
                                 level = ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #1')

            message = ['2nd line;\tone tab']
            myLogger.description(message,
                                 level = ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #2')

            message = ['3rd line;\t\ttwo tabs',
                       '',
                       paragraph]
            myLogger.description(message,
                                 level = ERROR,
                                 indent = 1,
                                 tab = 4,
                                 title = 'Data Corruption #3')
            myLogger.close()

        #-------------------------------------------------------------------

        def rewriteTest():
            '''
            '''
            myLogger = TsLogger(threshold = WARNING,
                                start = time.time(),
                                name = 'myProgress.log')
            print('\tName: %s' % myLogger.thisRegisteredName)
            print('\tID: %s' % myLogger.thisLogID)
            myLogger.progress('No Level update', level = NOTSET)
            myLogger.progress('Debug Level update', level = DEBUG)
            myLogger.progress('Info Level update', level = INFO)
            myLogger.progress('Warning Level update', level = WARNING)
            myLogger.progress('Error Level update', level = ERROR)
            myLogger.progress('Critical Level update', level = CRITICAL)

            myLogger.event('\n\nFinished New Logging Tests\n\n')
            myLogger.close()

        #-------------------------------------------------------------------

        def assertTest():
            '''
            '''

            def pseudoOp(number):
                print(number)

            myDebugHandlers = TsLogger(threshold = DEBUG,
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
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 2
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxASSERT_MSG(
                            cond,
                            msg='Sample #%d' % line)))
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 3
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK(
                            cond,
                            rc=123 + line)))
                except Exception, errorCode:
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
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 5
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxCHECK2(
                            cond,
                            op=pseudoOp(line))))
                except Exception, errorCode:
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
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 7
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxFAIL()))
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 8
                try:
                    print('line= %d; rc=%s' % (
                        line, myDebugHandlers.wxFAIL_COND_MSG(
                            cond, msg='Sample #%d' % line)))
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 9
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxFAIL_MSG(
                            msg='Sample #%d' % line)))
                except Exception, errorCode:
                    print('Handled Trap for line= %d; errorCode=%s' % (
                        line, errorCode))

                line += 1 # 10
                try:
                    print('line= %d; rc=%s' % (
                        line,
                        myDebugHandlers.wxTRAP()))
                except Exception, errorCode:
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

        myLogger = TsLogger(threshold = DEBUG,
                            start = time.time(),
                            name = 'myProperties.log')

        level=0
        head = myLogger.tsGetLoggerPath()
        tail = 'tsLogger-Dict.txt'
        deviceName = '%s/%s' % (head, tail)
        myFile = open(deviceName, 'w+')
        myDictionary = TsLogger.activeLoggerIDs
        tsru.displayDictionary(level, myDictionary, myFile, myLogger=None)
        myFile.close()

        propertyTest(myLogger)

    #-----------------------------------------------------------------------

    print(__header__)

    exitStatus = 0
    exitMsg = 'No Errors'
 
    try:

        wrapperTest()
 
    except tse.ProgramException, e1:
        exitMsg = str(e1)
        exitStatus = e1.exitCode
 
    except tse.InputOutputException, e1:
        exitMsg = str(e1)
        exitStatus = e1.exitCode
 
    if exitMsg == 'No Errors':
        sys.stdout.write(exitMsg)
    else:
        sys.stderr.write(exitMsg.replace("'", ""))

    sys.exit(exitStatus)
