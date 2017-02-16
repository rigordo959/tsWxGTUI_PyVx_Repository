#! /usr/bin/env python
# "Time-stamp: <10/25/2013  7:29:13 AM rsg>"
'''
tsWxDebugHandlers.py - Class that provides assert and check
handlers for debugging.
'''
#################################################################
#
# File: tsWxDebugHandlers.py
#
# Purpose:
#
#    Class that provides assert and check handlers for debugging.
#
# Usage (example):
#
#    # Import
#
#    from tsWxDebugHandlers import DebugHandlers
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxDebugHandlers'
__version__   = '1.0.1'
__date__      = '04/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
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

##import tsWxGlobals as wx # Invalid import because of circular dependency.
import tsCxGlobals as cx

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

class DebugHandlers(object):
    '''
    Assertion handlers: check if the condition is true and call assert handler
    (which will by default notify the user about failure) if it is not.

    wxASSERT and wxFAIL handlers as well as wxTrap() function do nothing at all
    if wxDEBUG_LEVEL is 0 however they do check their conditions at default
    debug level 1, unlike the previous wxWidgets versions.

    wxASSERT_LEVEL_2 is meant to be used for "expensive" asserts which should
    normally be disabled because they have a big impact on performance and so
    this macro only does anything if wxDEBUG_LEVEL >= 2.

    wxCHECK handlers always check their conditions, setting debug level to 0
    only makes them silent in case of failure, otherwise -- including at
    default debug level 1 -- they call the assert handler if the condition
    is false

    They are supposed to be used only in invalid situation: for example, an
    invalid parameter (e.g. a NULL pointer) is passed to a function. Instead
    of dereferencing it and causing core dump the function might use

    wxCHECK_RET( p != NULL, "pointer ca not be NULL" )
    '''
    def __init__(self):
        '''
        Constructor
        '''
        try:
            self.logger.debug(
                'Global logger available for DebugHandlers.')
        except AttributeError as errorCode:

            import tsLogger

            self.logger = tsLogger.TsLogger(
                threshold=tsLogger.DEBUG,
                # start=previous_time(from time.time()),
                name='./myAsserts.log')
            self.logger.debug(
                'Local logger available for DebugHandlers; rc=%s.' % str(
                    errorCode))

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
            msg = '***** ASSERT: cond (%s).' % cond
            self.logger.debug(msg)
            print(msg)

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
            self.logger.debug(msg)
            print('***** ASSERT_MSG: cond (%s). %s' % (cond, msg))

    #-----------------------------------------------------------------------
    def wxCHECK(self, cond, rc):
        '''
        check which returns with the specified return code if the condition
        fails
        '''
        if (cond == True):
            pass
        else:
            fmt = '***** CHECK: cond (%s); rc (%s).' % (cond, rc)
            self.logger.debug(fmt)
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
            fmt = '***** CHECK_MSG: cond (%s); rc (%s); msg=%s.' % (
                cond, rc, msg)
            self.logger.debug(fmt)
            self.wxFAIL_COND_MSG(cond, msg)
            return (rc)

    #-----------------------------------------------------------------------

    def wxCHECK2(self, cond, op=None):
        '''
        check that expression is true, perform op if not
        '''
        if (cond == True):
            pass
        elif (op is not None):
            fmt = '***** CHECK2: cond (%s); op (%s).' % (
                cond, op)
            self.logger.debug(fmt)
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
            fmt = '***** CHECK2_MSG: cond (%s); op (%s); msg (%s).' % (
                cond, op, msg)
            self.logger.debug(fmt)
            self.wxFAIL_COND_MSG(cond, msg)
            op()

    #-----------------------------------------------------------------------

    def wxFAIL(self):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        msg = '***** FAIL: Unreachable Code.'
        self.logger.debug(msg)
        print(msg)

    #-----------------------------------------------------------------------

    def wxFAIL_COND_MSG(self, cond, msg=None):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        fmt = '***** FAIL_COND_MSG: cond (%s). %s' % (cond, msg)
        self.logger.debug(fmt)
        print(fmt)

    #-----------------------------------------------------------------------

    def wxFAIL_MSG(self, msg=None):
        '''
        wxFAIL is a special form of assert: it always triggers (and so is
        usually used in normally unreachable code
        '''
        fmt = '***** FAIL_MSG: Unreachable Code. %s' % msg
        self.logger.debug(fmt)
        print(fmt)

    #-----------------------------------------------------------------------

    def wxTRAP(self):
        '''
        wxTRAP is a special form of assert: it always triggers (and so is
        usually used in application trap handler code
        '''
        fmt = '***** TRAP: Application Code.'
        self.logger.debug(fmt)
        print(fmt)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    def pseudoOp(number):
        print(number)

    print(__header__)

    myDebugHandlers = DebugHandlers()

    conditions = [True, False]
    line = 0
    for cond in conditions:

        print('#################### cond=%s ####################' % cond)
        line += 1
        text = 'Sample #%d' % line
        rc = 123 + line
        # op = pseudoOp(line)

        print('line= %d; rc=%s' % (line, myDebugHandlers.wxASSERT(
            cond)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxASSERT_MSG(
            cond, msg='Sample #%d' % line)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxCHECK(
            cond, rc)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxCHECK_MSG(
            cond, rc, msg='Sample #%d' % line)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxCHECK2(
            cond,
            op=pseudoOp(line))))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxCHECK2_MSG(
            cond,
            op=pseudoOp(line),
            msg='Sample #%d' % line)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxFAIL()))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxFAIL_COND_MSG(
            cond, msg='Sample #%d' % line)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxFAIL_MSG(
            msg='Sample #%d' % line)))

        line += 1
        print('line= %d; rc=%s' % (line, myDebugHandlers.wxTRAP()))
