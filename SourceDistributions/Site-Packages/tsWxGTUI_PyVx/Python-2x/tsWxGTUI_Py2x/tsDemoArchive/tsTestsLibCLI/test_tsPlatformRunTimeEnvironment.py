#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:05:55 AM rsg>"
__doc__ = '''
test_tsPlatformRunTimeEnvironment - Tool to capture current
hardware and software information about the run time environment
for the user process.
'''
#################################################################
#
# File: test_tsPlatformRunTimeEnvironment.py
#
# Purpose:
#
#     Tool to capture current hardware and software information
#     about the run time environment for the user process.
#
# Limitations:
#
#     1. Host processor hardware support includes various
#        releases of Pentium, PowerPC, SPARC.
#
#     2. Host operating system software support includes
#        various releases of Cygwin, Linux ('SuSE', 'debian',
#        'redhat', 'mandrake'), Mac OS ('X'), Unix ('Solaris')
#        and Windows ('98', '2000', 'XP', 'Vista').
#
#     3. Host virtual machine software support includes
#        various releases of Java and Python.
#
# Usage (example):
#
#     test_tsPlatformRunTimeEnvironment.py
#
# Methods:
#
# Notes:
#
# Modifications:
#
#     2014/01/25 rsg Replaced tsApplication with tsCommandLineEnv.
#
# ToDo:
#
#################################################################

__title__     = 'test_tsPlatformRunTimeEnvironment'
__version__   = '2.1.0'
__date__      = '01/25/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Platform & Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'
 
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

import os
import string
import sys
from optparse import OptionParser
import textwrap

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsCommandLineEnv
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsPlatformRunTimeEnvironment as tsquery

#--------------------------------------------------------------------------

DEBUG = False

#--------------------------------------------------------------------------

class OperatorSettingsParser(object):
    '''
    Class to incorporate features in tsOperatorSettingsParser.
    '''
    def __init__(self):
        '''
        Class constructor.
        '''

        #------------------------------------------------------------------

        ###################################################################
        # The following "Help" messages are used to configure each of the
        # Python version specific command line parser.
        ###################################################################

        #------------------------------------------------------------------

        self.aboutHelp = textwrap.dedent('''

        show a summary of the terms & conditions for users of this
        software (including the applicable product identification,
        authors, contributors, copyrights, licenses and purpose)
        and exit

        ''')

        #------------------------------------------------------------------

        self.debugHelp = textwrap.dedent('''

        log/display application program progress and diagnostic messages
        useful in debugging and troubleshooting.
        (default = False).

        ''')

        #------------------------------------------------------------------

        self.descriptionHelp = textwrap.dedent('''

        BACKGROUND

        This is a tool to capture current hardware and software information
        about the run time environment available to computer programs.

        ''')

        #------------------------------------------------------------------

        self.outputHelp = textwrap.dedent('''

        log/display current hardware and software information
        about the run time environment to this output file
        (default = "./%s.txt")

        ''') % self.getRunTimeTitle()

        #------------------------------------------------------------------

        self.syntaxHelp = textwrap.dedent('''

        Syntax:

            <python-interpreter> %prog [Option(s)]

        Examples:

            Python     application & option(s)
            ---------  ------------------------------------------------
            python     %prog

            python2.7  %prog  [-h] [-v] [-a] [-o] [-d] [-V]

            python3.3  %prog  [--help] [--version] \\
                                [--about] [--output]
                                [--debug] [--Verbose]

            -----------------------------------------------------------
            Key:

                "python"    - Default interpreter for platform

                "python2.7" - First alternate interpreter for platform

                "python3.3" - Second alternate interpreter for platform

                "[]" - Brackets enclose option keywords and values

                "{}" - Braces enclose option value choices, if any, and
                       positional arguments, if any

        ''').replace('%prog', self.getRunTimeTitle())

        #------------------------------------------------------------------

        self.usageHelp = textwrap.dedent('''

            %prog [Option(s)]

        Examples:

            %prog

            %prog  [-h] [-v] [-a] \\
                                [-o] \\
                                [-d] [-V]

            %prog  [--help] [--version] [--about] \\
                                [-output] \\
                                [--debug] [--Verbose]

        Purpose:

             Capture current hardware and software information about
             the run time environment available to computer programs.
        ''').replace('%prog', self.getRunTimeTitle())

        #------------------------------------------------------------------

        self.verboseHelp = textwrap.dedent('''

        log/display verbose troubleshooting details for application
        program activity tracking diagnostic messages (default = False)

        ''')

        #------------------------------------------------------------------

        self.versionHelp = textwrap.dedent('''

        show the build version of this software (including its title,
        version and date) and exit

        ''')

    #----------------------------------------------------------------------

    def getOptions(self):
        '''
        Parse the command line and return a list of positional arguments
        and a dictionanary of keyword options.
        '''
        parser = OptionParser(usage=self.usageHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-v', '--version',
            action='store_true',
            dest='version',
            default=False,
            help=self.versionHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-a', '--about',
            action='store_true',
            dest='about',
            default=False,
            help=self.aboutHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-o', '--output',
            action='store',
            dest='output',
            default='./%s.txt' % self.getRunTimeTitle(),
            type=str,
            help=self.outputHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-d', '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help=self.debugHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-V', '--Verbose',
            action='store_true',
            dest='Verbose',
            default=False,
            help=self.verboseHelp)

        (optionsOptParse, argsOptParse) = parser.parse_args()
        if len(argsOptParse) != 0:
            parser.print_help()
            sys.exit(1)

        maxArgs = min(0, len(argsOptParse))
        if len(argsOptParse) > maxArgs:
            # parser.error("wrong number of arguments")
            extraArgs = []
            for index in range(maxArgs, len(argsOptParse)):
                extraArgs += argsOptParse[index]
            parser.error("\n\n\tinvalid argument(s) = %s" % str(extraArgs))

        args = argsOptParse
        options = {}
        options['about'] = optionsOptParse.about
        options['debug'] = optionsOptParse.debug
        # options['help'] = optionsOptParse.help
        options['output'] = optionsOptParse.output
        options['version'] = optionsOptParse.version
        options['Verbose'] = optionsOptParse.Verbose

        if optionsOptParse.about:
            print('About:\n')
 
            buildHeader = __header__
            for line in buildHeader.split('\n'):
                print('\t%s' % line)

            print('Purpose:\n')
            for line in __doc__.split('\n'):
                print('\t%s' % string.lstrip(line))

            print('No Error')
            sys.exit(0)

        if optionsOptParse.version:
            print('Version:')
            for line in textwrap.wrap(mainTitleVersionDate):
                print('\n\t%s\n' % string.lstrip(line))
            print('No Error')
            sys.exit(0)

        return (args, options)

    #----------------------------------------------------------------------

    def getRunTimeTitle(self):
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        # Capture Command Line Arguments.
        argv = sys.argv

        # Separate File Path from its associated File Name and Extension
        (filePath, fileNameExt) = os.path.split(argv[0])

        # Separate File Name from its associated Extension
        (fileName, fileExt) = os.path.splitext(fileNameExt)

        if DEBUG:

            fmt1 = 'tsApplication.getRunTimeTitle:'
            fmt2 = '(filePath, fileNameExt)) = %s' % (
                str((filePath, fileNameExt)))
            fmt3 = '(fileName, fileExt) = %s' % (
                str(((fileName, fileExt))))
            msg = '\n\t%s\n\n\t\t%s\n\n\t\t%s' % (fmt1, fmt2, fmt3)
            self.logger.debug(msg)

        runTimeTitle = fileName
        return (runTimeTitle)

    #----------------------------------------------------------------------

    def getRunTimeTitleVersionDate(self):
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        runTimeTitle = self.getRunTimeTitle()
        if runTimeTitle == __title__:

            runTimeTitleVersionDate = mainTitleVersionDate

        else:

            runTimeTitleVersionDate = '%s, v%s (build %s)' % (
                runTimeTitle, __version__, __date__)

        return (runTimeTitleVersionDate)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def theMainApplication(*args, **kw):
        '''
        Display program name, version and date. Receive and validate
        command line options and arguments. Display help, error and
        status information. Initiate the file directory copy.
        '''
        theOperatorSettingsParser = OperatorSettingsParser()
        print('\n%s\n' % (
            theOperatorSettingsParser.getRunTimeTitleVersionDate()))

        (myArgs, myOptions) = theOperatorSettingsParser.getOptions()

        myOutputPath = myOptions['output']
        myRunTimeEnvironment = tsquery.PlatformRunTimeEnvironment()
        myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

        sys.stdout.write('\tResults are available in "%s".\n\n' % \
                         myOutputPath)

    prototype = theMainApplication
    myApp = tsCommandLineEnv.CommandLineEnv(

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

        enableDefaultCommandLineParser=True,

        logs=[],

        runTimeEntryPoint=prototype)

    myApp.Wrapper()
