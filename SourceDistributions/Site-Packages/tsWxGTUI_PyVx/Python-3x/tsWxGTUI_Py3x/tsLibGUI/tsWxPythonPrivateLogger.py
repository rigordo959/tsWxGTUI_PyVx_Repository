#! /usr/bin/env python
# "Time-stamp: <03/09/2015  3:29:52 AM rsg>"
'''
tsWxPythonPrivateLogger.py - Refactored portion of the
tsWxGraphicalTextUserInterface that provides a class and
associated methods which emulate a subset of Python logging
API. It defines and handles prioritized, time and date
stamped event message formatting and output to files and
devices. Files are organized in a date and time stamped
directory named for the launched application. Unix-type
devices include stderr and stdout.
'''
#################################################################
#
# File: tsWxPythonPrivateLogger.py
#
# Purpose:
#
#     Refactored portion of the tsWxGraphicalTextUserInterface
#     that provides a class and associated methods which emulate
#     a subset of Python logging API. It defines and handles
#     prioritized, time and date stamped event message formatting
#     and output to files and devices. Files are organized in a
#     date and time stamped directory named for the launched
#     application. Unix-type devices include stderr and stdout.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonPrivateLogger import *
#
# Requirements:
#
#     The PrivateLogger class and associated methods emulate
#     a subset of Python logging API. It defines and handles
#     prioritized, time and date stamped event message formatting
#     and output to files and devices.
#
# Capabilities:
#
#
# Limitations:
#
#    The PrivateLogger class should only be used when the
#    tsWxGraphicalTextUserInterface module is itself the main
#    program. It will not be needed when the tsApplication
#    module establishes a fully funtional logger.
#
# Notes:
#
#
# Classes:
#
#    PrivateLogger
#
# Methods:
#
#    PrivateLogger.__init__
#    PrivateLogger._log
#    PrivateLogger._output
#    PrivateLogger.alert
#    PrivateLogger.critical
#    PrivateLogger.debug
#    PrivateLogger.emergency
#    PrivateLogger.error
#    PrivateLogger.exception
#    PrivateLogger.info
#    PrivateLogger.log
#    PrivateLogger.notice
#    PrivateLogger.warning
#
# Modifications:
#
#    2014/07/03 rsg Added the following modules:
#			tsWxPythonColor16DataBase
#			tsWxPythonColor16SubstitutionMap
#			tsWxPythonColor256DataBase
#			tsWxPythonColor88DataBase
#			tsWxPythonColor8DataBase
#			tsWxPythonColor8SubstitutionMap
#			tsWxPythonColorDataBaseRGB
#			tsWxPythonColorNames
#			tsWxPythonColorRGBNames
#			tsWxPythonColorRGBValues
#			tsWxPythonMonochromeDataBase
#			tsWxPythonPrivateLogger
#
# ToDo:
#
#
#################################################################

__title__     = 'tsWxPythonPrivateLogger'
__version__   = '1.0.0'
__date__      = '07/03/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t\t\tfor Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 Free Software ' + \
                '\n\t\t\tFoundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  nCurses README,v 1.23 2006/04/22'

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

class PrivateLogger(object):
    '''
    The PrivateLogger class.

    It should only be needed when this module is itself the main program.
    It will not be needed when tsApplication establishes a fully funtional
    logger.
    '''

    # The following defines sverity levels which may be used as
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
    PRIVATE       = CRITICAL + 10
    PRIVATENAME   = 'PRIVATE'

    LOG_PATH      = "./"
    LOG_NAME      = "message"
    LOG_EXTENSION = ".log"
    APPEND        = "a"
    TRUNCATE      = "w"
    DEFAULT_LOG_FILE_MODE = TRUNCATE

    threshold = {NOTSET: NOTSET,
                 DEBUG: DEBUG,
                 INFO: INFO,
                 NOTICE: NOTICE,
                 WARNING: WARNING,
                 ALERT: ALERT,
                 ERROR: ERROR,
                 CRITICAL: CRITICAL,
                 EMERGENCY: EMERGENCY,
                 PRIVATE: PRIVATE}

    category = {NOTSET: 'NOTSET',
                DEBUG: 'DEBUG',
                INFO: 'INFO',
                NOTICE: 'NOTICE',
                WARNING: 'WARNING',
                ALERT: 'ALERT',
                ERROR: 'ERROR',
                CRITICAL: 'CRITICAL',
                EMERGENCY: 'EMERGENCY',
                PRIVATE: 'PRIVATE'}

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        '''
        self.theThreshold = DEBUG
        timestamp = tsrpu.getDateTimeString(time.time(), msec=True)
        ts_logFile = '%s/%s' % (
            tsLogger.TsLogger.defaultStandardOutputPath,
            defaultLogFileName)
        self.theFile = open(ts_logFile, defaultLogFileMode, 0)
        self.theFile.write('%s - %s\n' % (
            timestamp, 'Started logging to file "%s"' % ts_logFile))

        self.theFile.flush()

    #-----------------------------------------------------------------------

    def alert(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ALERT'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.ALERT, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def critical(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
 
        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.CRITICAL, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def debug(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.DEBUG, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def emergency(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'EMERGENCY'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
 
        logger.critical("Houston, we have a %s", "major disaster",
        exc_info = 1)
        '''
        self._log(*(PrivateLogger.EMERGENCY, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def error(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.ERROR, msg, args), **kwargs)

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
        self._log(*(PrivateLogger.INFO, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def _log(self, level, msg, args, exc_info = None, extra = None):
        '''
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        '''
        if self.theThreshold <= level:
            timestamp = tsrpu.getDateTimeString(time.time(), msec = True)

            record = '%s %9.9s: %s' % (timestamp,
                                       PrivateLogger.category[level],
                                       msg)
            self._output(record, level = level)

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
        self._log(*(PrivateLogger.NOTICE, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def warning(self, msg, *args, **kwargs):
        '''
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info = 1)
        '''
        self._log(*(PrivateLogger.WARNING, msg, args), **kwargs)

    #-----------------------------------------------------------------------

    def _output(self, text, level = NOTSET, newline = True):
        '''
        Output message to console and/or file.
        '''
        if newline:
            message = text + '\n'
        else:
            message = text

        if PrivateLogger.NOTSET < level and \
           level >= self.theThreshold and \
           level < PrivateLogger.PRIVATE:
            if level >= PrivateLogger.WARNING:
                # Send to stderr
                sys.stderr.write(message)
            else:
                # Send to stdout
                sys.stdout.write(message)

        if PrivateLogger.NOTSET < level and \
           level >= self.theThreshold and \
           level <= PrivateLogger.PRIVATE:
            if self.theFile is not None:
                # Send to file
                self.theFile.write(message)
                self.theFile.flush()
