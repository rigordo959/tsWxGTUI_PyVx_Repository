#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:08:12 AM rsg>"
'''
test_tsStripSettingsParser.py - Test application for the
default command line interface system used to parse and extract
keyword-value pair options and positional arguments. Depending
on the Python version or overriding operator selection, it can
test parsing via the standard Python modules "argparse",
"optparse" and "getopt".
'''
#################################################################
#
# File: test_tsStripSettingsParser.py
#
# Purpose:
#
#    Test application for the default command line interface
#    system used to parse and extract keyword-value pair
#    options and positional arguments. Depending on the Python
#    version or overriding operator selection, it can test
#    parsing via the standard Python modules "argparse",
#    "optparse" and "getopt".
#
# Limitations:
#
#     Requires one or more of the parser module(s) available
#     in the Python version(s) supported by the application.
#
#     "argparse" (introduced with Python 2.7.0)
#     "optparse" (introduced with Python 2.3.0)
#     "getopt"   (introduced with Python 1.6.0)
#
# Notes:
#
#     2013/06/16 rsg "argparse" is the primary parser module.
#                    It is therefore the default value for the
#                    "module" keyword option.
#
#     2013/06/16 rsg "optparse" and "getopt" are the secondary
#                    tertiary parser modules respectively. In
#                    order to demonstrate positional arguments,
#                    they require that the operator specify the
#                    desired one as a positional argument.
#
# Methods:
#
#    exitTest - Method to initiate either a normal or abnormal
#           termination of the application program.
#
#    mainTest - Top-level method to control application-specific
#           functions. It prints the header text containing the
#           title, version, date, authors, copyright, license and
#           credits. It demonstrates exception handling.
#
# Modifications:
#
#
# ToDo:
#
#################################################################

__title__     = 'test_tsStripSettingsParser'
__version__   = '1.0.0'
__date__      = '07/27/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'

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

DEBUG = False

DebugKeyValueUndefined     = False
DebugSimulatedKeyErrorTrap = False
EnableOptionsGNU = True

theAssignedLogger = None

runTimeTitleEnabled = True
tracebackEnabled = False

#------------------------------------------------------------------------

__help__ = '''
This program demonstrates an environment for a Command Line User Interface.

'''

import os.path
import sys

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsCommandLineEnv

from tsCommandLineEnv import CommandLineEnv

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsToolsLibCLI import tsStripSettingsParser

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

##    print(__header__)

    #----------------------------------------------------------------------

    def exitTest():
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def mainTest(*args, **kw):
        '''
        Main program entry point test.
        '''
        myParser =  tsStripSettingsParser.TsStripSettingsParser()
        print('\n%s\n' % myParser.getRunTimeTitleVersionDate())

        rawArgsOptions = sys.argv[1:]
        print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        (args, options) = myParser.parseCommandLineDispatch()

        print('type(args=%s)=%s' % (str(args), type(args)))
        print('type(options=%s)=%s' % (str(options), type(options)))

        if True or DEBUG:
            label = myParser.getRunTimeTitle()

            fmt1 = '%s.mainTest (parameter list): ' % label
            fmt2 = 'args=%s;\n\t\tkw=%s' % (str(args), str(kw))
            print('\n\t%s\n\t\t%s' % (fmt1, fmt2))

            fmt1 = '%s.mainTest (command line argv): ' % label
            fmt2 = 'args=%s' % str(args)
            fmt3 = 'options (unsorted)=%s' % str(options)
            print('\n\t%s\n\t\t%s;\n\t\t%s' % (fmt1, fmt2, fmt3))

            fmt1 = '\n\t%s.mainTest (command line argv): ' % label
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                try:
                    value = '"%s"' % options[key]
                except Exception, errorCode:
                    value = ''
                if text == '':
                    text = '{\n\t\t\t%s: %s' % (str(key), str(value))
                else:
                    text += ', \n\t\t\t%s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        return (args, options)

    #----------------------------------------------------------------------

    def EntryPoint(*args, **kw):
        '''
        '''

        print('\n\n\tEntryPoint (parameters:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
            str(args), str(kw)))

        if True:
            (args, options) = mainTest(*args, **kw)
        else:
            mainTest(*args, **kw)
            args = myApp.args
            options = myApp.options

        print('\n\n\tResults:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
            str(args), str(options)))

        print('\n')

    #----------------------------------------------------------------------

    myApp = CommandLineEnv(
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
        logs=[Logger.StandardOutputFile, 'Dummy#2', 'Dummy#3'],
        enableDefaultCommandLineParser=True,
        runTimeEntryPoint=EntryPoint)

    myApp.Wrapper()
