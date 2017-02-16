#! /usr/bin/env python
# "Time-stamp: <06/09/2015  8:08:37 AM rsg>"
__doc__ = '''
test_tsCxGlobals.py - Test application for tsCxGlobals module.
'''
#################################################################
#
# File: tsCxGlobals.py
#
# Purpose:
#
#     Test application for tsCxGlobals module.
#
# Usage (example):
#
#    # Execute
#
#    python test_tsCxGlobals.py
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
#       user activities:
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
#    1. The "tsToolkitCLI" and the "tsCxGlobals" module are designed
#       to launch and support Python executable Command Line Interface
#       (CLI) applications, tools and tests via the "tsCommandLineEnv"
#       module.
#
#    2. The "tsToolkitGUI" and the "tsWxGlobals" module are designed
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
# Methods:
#
#    TBD.
#
# Classes:
#
#    TBD.
#
# Modifications:
#
#    2013/10/22 rsg Initial version.
#
# ToDo:
#
#    TBD.
#
#################################################################

__title__     = 'test_tsCxGlobals'
__version__   = '1.0.0'
__date__      = '10/22/2013'
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

import os
import sys

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
    from tsCxGlobals import ThemeToUse

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
	  'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

    #-------------------------------------------------------------------

    print(__header__)

    #-------------------------------------------------------------------

    myLogger = Logger.TsLogger(name='',
                               threshold=Logger.INFO)

    #-------------------------------------------------------------------

    level = 0
    myDictionary = ThemeToUse
    myConsole = sys.stdout
    tsrpu.displayDictionary(level, myDictionary, myConsole)

    myFile = open(os.path.join(myLogger.theLogPath,
                               'tsCxGlobalsDictionaryTest.log'), 'w')

    tsrpu.displayDictionary(level, myDictionary, myFile)
    myFile.close()
