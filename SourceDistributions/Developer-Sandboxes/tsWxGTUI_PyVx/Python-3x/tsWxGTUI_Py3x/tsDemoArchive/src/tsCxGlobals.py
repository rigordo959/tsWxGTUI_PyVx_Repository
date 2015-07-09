#! /usr/bin/env python
# "Time-stamp: <06/27/2014  7:51:11 AM rsg>"
'''
tsCxGlobals.py - Module to establish configuration constants and
macro-type functions for the Command Line Interface mode of the
"tsWxGTUI" Toolkit.
'''
#################################################################
#
# File: tsCxGlobals.py
#
# Purpose:
#
#     Module to establish configuration constants and macro-type
#     functions for the Command Line Interface mode of the
#     "tsWxGTUI" Toolkit.
#
# Usage (example):
#
#    # Import
#
#    import tsCxGlobals as cx
#
# Capabilities:
#
#    1. Provide a centralized mechanism for modifying/restoring those
#       configuration constants that can be interogated at runtime by
#       those software components having a "need-to-know". The intent
#       being to avoid subsequent searches to locate and modify or
#       restore a constant appropriate to the current configuration.
#
#    2. Provide a theme-based mechanism for modifying/restoring those
#       configuration constants as appropriate for the following
#       users and their activities:
#
#       a. Supervisory Control and Data Acquisition (SCADA) System:
#
#          * System Operator
#          * Software Engineer
#          * System Administrator
#          * Field Service
#
#       b. Application ("tsWxGTUI" CLI/GUI) Development System:
#
#          * Software Engineer
#          * System Administrator
#          * Field Service
#
#       c. Toolkit ("tsWxGTUI") Development System:
#
#          * Software Engineer
#          * System Administrator
#          * Field Service
#
# Limitations:
#
#    1. There are two copies of the tsCxGlobals.py file. The shared
#       one must be just above the tsLibCLI directory. As a backup,
#       it is advisable to also maintain a reference copy of it in
#       tsCxGlobalsPkg/src.
#
#    2. The "tsToolkitCLI" and the "tsCxGlobals" module are designed
#       to launch and support Python executable Command Line Interface
#       (CLI) applications, tools and tests via the "tsCommandLineEnv"
#       module.
#
#    3. The "tsToolkitGUI" and the "tsWxGlobals" module are designed
#       to launch and support Python executable Graphical-style User
#       Interface (GUI) applications, tools and tests via the
#       "tsWxMultiFrameEnv" module. The launch module is a customized
#       version of "tsCommandLineEnv". After launching the Python
#       application, it manages the startup, operation and shutdown
#       of the "wxPython"-style, "nCurses"-based GUI emulation.
#
# Notes:
#
#    1. The "tsToolkitCLI" is designed to be independent of the
#       "tsToolkitGUI". However, its "tsApplication" module, collects
#       and distributes all the keyword-value pair options and posi-
#       tional argumets entered by the operator and those launch
#       parameters established by the application itself. This in-
#       dependence ensures that there is a common launch mechanism
#       ("tsApplication") for both CLI and GUI applications.
#
#    2. This "tsCxGlobals" module establishes a common area for defin-
#       ing system-wide CLI configuration parameters whose values may
#       be then communicated within and across a distributed system.
#
#    3. The "tsWxGlobals" module establishes a common area for defin-
#       ing system-wide GUI configuration parameters whose values may
#       be then communicated within and across a distributed system.
#
#    4. Themes are customized sets of configuration parameters that
#       are appropriate for a desired look and feel.
#
# Classes:
#
#    None.
#
# Methods:
#
#    tsCaselessStringCompare - Return True, only if two text strings are
#        identical except for upper/lower case. Otherwise, return False.
#
#    tsMax - Cast both operands to the same type before comparing them to
#        avoid warnings about signed/unsigned comparisons from some
#        compilers
#
#    tsMin - Cast both operands to the same type before comparing them to
#        avoid warnings about signed/unsigned comparisons from some
#        compilers
#
#    get_terminal_size - Return width and height of console display
#        for Cygwin, Darwin (Mac OS X), Linux platforms
#
#    _get_terminal_size_linux - Return width and height of console
#        display from ioctl and termios info.
#
#    _get_terminal_size_tput - Return width and height of console
#        display from terminal columns and line info.
#
#    _get_terminal_size_windows - Return width and height of console
#        display from Microsoft Windows console screen buffer info.
#
# Modifications:
#
#    2013/10/20 rsg Initial version.
#
#    2013/11/13 rsg Re-assigned Private severity level from 60 to
#                   1 because nothing should be higher than
#                   CRITICAL OR EMERGENCY.
#
#    2014/01/22 rsg Added list of classes and methods..
#
#    2014/04/08 rsg Changed to "ThemeToUse = Theme_SCADA_Operator"
#                   from "ThemeToUse = Theme_Toolkit_Engineer"
#                   in order to reduce verbosity of event logging.
#
# ToDo:
#
#    TBD.
#
#################################################################

__title__     = 'tsCxGlobals'
__version__   = '1.2.0'
__date__      = '04/08/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  terminalsize (https://gist.github.com/' + \
                'jtriley/1108174) Features: ' + \
                '\n\t  Copyright (c) 2011 Justin T. Riley.' + \
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

#--------------------------------------------------------------------------

import copy
import os
import platform
import shlex
import struct
import subprocess
import sys

try:
    import syslog
    syslogAvailable = True
except ImportError as e:
    syslogAvailable = False

#---------------------------------------------------------------------------

ProductName   = '"tsWxGTUI" Toolkit'
SubSystemName   = '"tsToolkitCLI"'
VendorName    = 'Richard S. Gordon, a.k.a. Software Gadgetry'
ThemeDate     = __date__

import platform
## import types

DEBUG = True # TBD - Retain True to prevent Unimplemented Traps
VERBOSE = True

#---------------------------------------------------------------------------

System = platform.system()
Platform = '__tsToolkitCLI__'

#---------------------------------------------------------------------------

#
# Events may be assigned a severity level and sent to the
# specified logger in the form of a text string. The message
# can be formatted as appropriate.
#
# Severity levels have pre-assigned priorities typically
# applied as follows:
#
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

# The following defines tsLogger sverity levels which
# may be used as a threshold filter for console output.
NOTSET        = 0            # From Python Logging module
DEBUG         = 10           # From Python Logging module
INFO          = 20           # From Python Logging module
NOTICE        = INFO + 5     # Introduced by tsLogger package
WARNING       = 30           # From Python Logging module
ALERT         = WARNING + 5  # Introduced by tsLogger package
ERROR         = 40           # From Python Logging module
CRITICAL      = 50           # From Python Logging module
EMERGENCY     = CRITICAL + 5 # Introduced by tsLogger package

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
    WARNING: WARNING,
    'name': 'threshold'
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
    WARNING: 'WARNING',
    'name': 'category'
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
        PRIVATE: syslog.LOG_EMERG,
        WARNING: syslog.LOG_WARNING,
        'name': 'syslogMap'
        }

#---------------------------------------------------------------------------

def tsCaselessStringCompare(string1, string2):
    '''
    Return True, only if two text strings are identical except for
    upper/lower case. Otherwise, return False.
    '''
    if string1.lower() == string2.lower():
        match = True
    else:
        match = False

    return (match)

#---------------------------------------------------------------------------

def Max(a, b):
    '''
    Cast both operands to the same type before comparing them to avoid
    warnings about signed/unsigned comparisons from some compilers
    '''
    if ((isinstance(a, float)) or \
        (isinstance(b, float))):

        return (max(float(a), float(b)))

    else:

        return (max(int(a), int(b)))

#---------------------------------------------------------------------------

def Min(a, b):
    '''
    Cast both operands to the same type before comparing them to avoid
    warnings about signed/unsigned comparisons from some compilers
    '''
    if ((isinstance(a, float)) or \
        (isinstance(b, float))):

        return (min(float(a), float(b)))

    else:

        return (min(int(a), int(b)))

#--------------------------------------------------------------------------
 
def get_terminal_size():
    """ getTerminalSize()
     - Return width and height of console display
     - works on linux,os x,windows,cygwin(windows)
     originally retrieved from:
     http://stackoverflow.com/questions/566746/
            how-to-get-console-window-width-in-python
    """
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        print("default")
        tuple_xy = (80, 25)      # default value
    return tuple_xy

#--------------------------------------------------------------------------
 
def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass

#--------------------------------------------------------------------------

def _get_terminal_size_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/
    #             how-do-i-find-the-width-height-of-a-terminal-window
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass

#--------------------------------------------------------------------------
 
def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

#---------------------------------------------------------------------------

# Base-line definitions apply regardless of user activity.

sizex, sizey = get_terminal_size()

ThemeCxPython = {
    'ProductName': ProductName,
    'SubSystemName': SubSystemName,
    'VendorName': VendorName,
    'ThemeName': 'ThemeCxPython',
    'ThemeDate': ThemeDate,

    'name': __title__,

    'tsLoggerLevels': {
        'NotSet': NOTSET,       # From Python Logging module
        'Private': PRIVATE,     # Introduced by tsLogger package
        'Debug': DEBUG,         # From Python Logging module
        'Info': INFO,           # From Python Logging module
        'Notice': NOTICE,       # Introduced by tsLogger package
        'Warning': WARNING,     # From Python Logging module
        'Alert': ALERT,         # Introduced by tsLogger package
        'Error': ERROR,         # From Python Logging module
        'Critical': CRITICAL,   # From Python Logging module
        'Emergency': EMERGENCY, # Introduced by tsLogger package
        'name': 'tsLoggerLevels'
        },

    'tsLoggerStandardTargets': {
        'StandardOutputFile': '',
        'StandardOutputDevice': 'stdout',
        'StandardErrorDevice': 'stderr',
        'StandardScreenDevice': 'stdscr',
        'SystemLogDevice': 'syslog',
        'name': 'tsLoggerStandardTargets'
        },

    'tsConsoleDisplaySize': {
        'Cols': sizex,
        'Rows': sizey,
        'name': 'tsConsoleDisplaySize'
        }

    }

#---------------------------------------------------------------------------

# Themes for Supervisory Control and Data Acquisition (SCADA) System Users
# operating equipment for automation, communication, control, diagnostic,
# instrumentation and simulation applications
Theme_SCADA_Operator = copy.copy(ThemeCxPython)
Theme_SCADA_Operator['ThemeUser'] = 'Theme_SCADA_Operator'
Theme_SCADA_Operator['Troubleshooting'] = {
    'Debug_CLI_Configuration': False, # True,
    'Debug_CLI_Exceptions': False, # True,
    'Debug_CLI_Launch': False, # True,
    'Debug_CLI_Progress': False, # True,
    'Debug_CLI_Termination': False, # True,
    'Debug_GUI_Configuration': False, # True,
    'Debug_GUI_Exceptions': False, # True,
    'Debug_GUI_Launch': False, # True,
    'Debug_GUI_Progress': False, # True,
    'Debug_GUI_Termination': False, # True,
    'name': 'Troubleshooting'
    }
Theme_SCADA_Operator['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': WARNING,
    'StandardErrorDevice': ERROR,
    'StandardScreenDevice': INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_SCADA_Engineer = copy.copy(ThemeCxPython)
Theme_SCADA_Engineer['ThemeUser'] = 'Theme_SCADA_Engineer'
Theme_SCADA_Engineer['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_SCADA_Engineer['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_SCADA_Administrator = copy.copy(ThemeCxPython)
Theme_SCADA_Administrator['ThemeUser'] = 'Theme_SCADA_Administrator'
Theme_SCADA_Administrator['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_SCADA_Administrator['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': WARNING,
    'StandardErrorDevice': ERROR,
    'StandardScreenDevice': INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_SCADA_Service = copy.copy(ThemeCxPython)
Theme_SCADA_Service['ThemeUser'] = 'Theme_SCADA_Service'
Theme_SCADA_Service['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_SCADA_Service['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

#---------------------------------------------------------------------------

# Themes for "tsWxGTUI" Toolkit CLI/GUI Application Development System Users
# developing, enhancing, maintaining and troubleshooting computer software
# for automation, communication, control, diagnostic, instrumentation and
# simulation applications.
#
#    1. "tsToolkitCLI" - Command Line Interface Applications
#
#    2. "tsToolkitGUI" - Graphical-style User Interface Applications
#

Theme_Application_Engineer = copy.copy(ThemeCxPython)
Theme_Application_Engineer['ThemeUser'] = 'Theme_Application_Engineer'
Theme_Application_Engineer['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Application_Engineer['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_Application_Administrator = copy.copy(ThemeCxPython)
Theme_Application_Administrator['ThemeUser'] = 'Theme_Application_Administrator'
Theme_Application_Administrator['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Application_Administrator['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': WARNING,
    'StandardErrorDevice': ERROR,
    'StandardScreenDevice': INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_Application_Service = copy.copy(ThemeCxPython)
Theme_Application_Service['ThemeUser'] = 'Theme_Application_Service'
Theme_Application_Service['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Application_Service['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

#---------------------------------------------------------------------------

# Themes for "tsWxGTUI" Toolkit Development System Users developing, enhanc-
# ing, maintaining and troubleshooting general-purpose, re-usable computer
# software.
#
#    1. "tsToolkitCLI" - Command Line Interface buildong blocks
#
#       a. "tsLibCLI"
#       b. "tsToolsCLI"
#       c. "tsUtilities"
#       d. "tsTestsCLI"
#
#    2. "tsToolkitGUI" - Graphical-style User Interface buildong blocks
#
#       a. "tsLibGUI"
#       b. "tsToolsGUI"
#       c. "tsTestsGUI"
#

Theme_Toolkit_Engineer = copy.copy(ThemeCxPython)
Theme_Toolkit_Engineer['ThemeUser'] = 'Theme_Toolkit_Engineer'
Theme_Toolkit_Engineer['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Toolkit_Engineer['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_Toolkit_Administrator = copy.copy(ThemeCxPython)
Theme_Toolkit_Administrator['ThemeUser'] = 'Theme_Toolkit_Administrator'
Theme_Toolkit_Administrator['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Toolkit_Administrator['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': WARNING,
    'StandardErrorDevice': ERROR,
    'StandardScreenDevice': INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

Theme_Toolkit_Service = copy.copy(ThemeCxPython)
Theme_Toolkit_Service['ThemeUser'] = 'Theme_Toolkit_Service'
Theme_Toolkit_Service['Troubleshooting'] = {
    'Debug_CLI_Configuration': True,
    'Debug_CLI_Exceptions': True,
    'Debug_CLI_Launch': True,
    'Debug_CLI_Progress': True,
    'Debug_CLI_Termination': True,
    'Debug_GUI_Configuration': True,
    'Debug_GUI_Exceptions': True,
    'Debug_GUI_Launch': True,
    'Debug_GUI_Progress': True,
    'Debug_GUI_Termination': True,
    'name': 'Troubleshooting'
    }
Theme_Toolkit_Service['tsLoggerThresholds'] = {
    'StandardOutputFile': DEBUG,
    'StandardOutputDevice': DEBUG, # WARNING,
    'StandardErrorDevice': DEBUG, # ERROR,
    'StandardScreenDevice': DEBUG, # INFO,
    'SystemLogDevice':  ERROR,
    'name': 'tsLoggerThresholds'
    }

#---------------------------------------------------------------------------

##ThemeToUse = Theme_SCADA_Operator
##ThemeToUse = Theme_SCADA_Engineer
##ThemeToUse = Theme_SCADA_Administrator
##ThemeToUse = Theme_SCADA_Service
##ThemeToUse = Theme_Application_Engineer
##ThemeToUse = Theme_Application_Administrator
##ThemeToUse = Theme_Application_Service
##ThemeToUse = Theme_Toolkit_Engineer
##ThemeToUse = Theme_Toolkit_Administrator
##ThemeToUse = Theme_Toolkit_Service

# ThemeToUse = Theme_SCADA_Operator   # Minimum debug verbosity
ThemeToUse = Theme_Toolkit_Engineer # Maximum debug verbosity

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

    #--------------------------------------------------------------------------

    try:

        import tsLibCLI

    except ImportError as importCode:

        print('%s: ImportError (tsLibCLI); ' % __title__ + \
              'importCode=%s' % str(importCode))

    #--------------------------------------------------------------------------

    try:

        import tsExceptions as tse
        import tsLogger as Logger
        from tsReportUtilities import TsReportUtilities as tsrpu

    except ImportError as importCode:

        print('%s: ImportError (tsLibCLI); ' % __title__ + \
              'importCode=%s' % str(importCode))

    #-------------------------------------------------------------------

    print(__header__)

    #-------------------------------------------------------------------

    myLogger = Logger.TsLogger(name='',
                               threshold=Logger.INFO)

    #-------------------------------------------------------------------

    sizex, sizey = get_terminal_size()
    print('\n  width = %d; height = %d' % (sizex, sizey))

    current_os = platform.system()
    print('\n  current_os = %s' % current_os)

    #-------------------------------------------------------------------

    level = 0
    myDictionary = ThemeToUse
    myConsole = sys.stdout
    tsrpu.displayDictionary(level, myDictionary, myConsole)

    myFile = open(os.path.join(myLogger.theLogPath,
                               'tsCxGlobalsDictionaryTest.log'), 'w')

    tsrpu.displayDictionary(level, myDictionary, myFile)
    myFile.close()
