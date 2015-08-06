#!/usr/bin/env python
# "Time-stamp: <06/09/2015  7:30:14 AM rsg>"
'''
Tutorial_CLI_4_Command_Line_PlatformQuery_Application.py - Tool
to capture current hardware and software information about the
run time environment available to computer programs.
'''
#################################################################
#
# File: Tutorial_CLI_4_Command_Line_PlatformQuery_Application.py
#
# Purpose:
#
#     Demonstrate tool to capture current hardware and software
#     information about the run time environment available to
#     computer programs.
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
# Notes:
#
# Usage:
#
#     python Tutorial_CLI_4_Command_Line_PlatformQuery_Application.py \
#            [Option(s)]
#
# Examples:
#
#     python Tutorial_CLI_4_Command_Line_PlatformQuery_Application
#
#     python Tutorial_CLI_4_Command_Line_PlatformQuery_Application \
#                         [-h] [-v] [-a] \
#                         [-o] \
#                         [-d] [-V]
#
#     python Tutorial_CLI_4_Command_Line_PlatformQuery_Application \
#                         [--help] [--version] [--about] \
#                         [-output] \
#                         [--debug] [--Verbose]
#
# Options:
#   -h, --help            show this help message and exit
#   -v, --version         show the build version of this software (including
#                         its title, version and date) and exit
#   -a, --about           show a summary of the terms & conditions for users
#                         of this software (including the applicable product
#                         identification, authors, contributors, copyrights,
#                         licenses and purpose) and exit
#   -o OUTPUT, --output=OUTPUT
#                         log/display current hardware and software
#                         information about the run time environment to this
#                         output file (default = "./tsPlatformQuery.txt")
#   -d, --debug           log/display application program progress and
#                         diagnostic messages useful in debugging and
#                         troubleshooting. (default = False).
#   -V, --Verbose         log/display verbose troubleshooting details for
#                         application program activity tracking diagnostic
#                         messages (default = False)
#
# Classes:
#
#    OperatorSettingsParser - Class to incorporate features in
#           tsOperatorSettingsParser.
#
# Methods:
#
#    theMainApplication - Display program name, version and date.
#          Receive and validate command line options and arguments.
#          Display help, error and status information. Initiate
#          the file directory copy.
#
#    OperatorSettingsParser.__init__ - Class constructor.
#
#    OperatorSettingsParser.getOptions - Parse the command line and
#          return a list of positional arguments and a dictionanary
#          of keyword options.
#
#    OperatorSettingsParser.getRunTimeTitle -  Method to return
#           Run Time Title, or Build Title, whichever was actually
#           used in command line, stripping it of any file path.
#
#    OperatorSettingsParser.getRunTimeTitleVersionDate - Method to
#           return the Build Title, Version and Date (with any
#           Run Time update) for use in command line parsing help
#           and error display output.
#
#    OperatorSettingsParser.theMainApplication - Display program name,
#           version and date. Receive and validate command line
#           options and arguments. Display help, error and
#           status information. Initiate the file directory copy.
#
# Modifications:
#
#    2013/06/10 rsg Derived this version from:
#                   "test_tsPlatformRunTimeEnvironment.py".
#
#    2013/06/10 rsg Re-engineered getOptions to incorporate
#                   features of tsOperatorSettingsParser:
#                   getRunTimeTitle, getRunTimeTitleVersionDate
#                   and textwrap.
#
#    2013/06/10 rsg Added option for setting output file
#                   name and location.
#
#    2013/06/10 rsg Revised out generated in response to options
#                   "-a", "-v" and "-h".
#
#    2014/02/13 rsg Re-organized code as an application rather
#                   than as a building block module. This makes it
#                   reasonable to display the file's header upon
#                   launch (needed when help, about and version
#                   information must be displayed in context).
#
# ToDo:
#
#################################################################

__title__     = 'Tutorial_CLI_4_Command_Line_PlatformQuery_Application'
__version__   = '2.1.0'
__date__      = '02/12/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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

import tsLibCLI

#--------------------------------------------------------------------------

from tsCommandLineEnv import CommandLineEnv

import tsPlatformRunTimeEnvironment as tsquery

#--------------------------------------------------------------------------

DEBUG = False

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    class OperatorSettingsParser(object):
        '''
        Class to incorporate features in tsOperatorSettingsParser.
        '''
        def __init__(self):
            '''
            Class constructor.
            '''

            #--------------------------------------------------------------

            ###############################################################
            # The following "Help" messages are used to configure each of
            # the Python version specific command line parser.
            ###############################################################

            #--------------------------------------------------------------

            self.aboutHelp = textwrap.dedent('''

            show a summary of the terms & conditions for users of this
            software (including the applicable product identification,
            authors, contributors, copyrights, licenses and purpose)
            and exit

            ''')

            #--------------------------------------------------------------

            self.debugHelp = textwrap.dedent('''

            log/display application program progress and diagnostic messages
            useful in debugging and troubleshooting.
            (default = False).

            ''')

            #--------------------------------------------------------------

            self.descriptionHelp = textwrap.dedent('''

            BACKGROUND

            This is a tool to capture current hardware and software information
            about the run time environment available to computer programs.

            ''')

            #--------------------------------------------------------------

            self.outputHelp = textwrap.dedent('''

            log/display current hardware and software information
            about the run time environment to this output file
            (default = "./%s.txt")

            ''') % self.getRunTimeTitle()

            #--------------------------------------------------------------

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

            #--------------------------------------------------------------

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

            #--------------------------------------------------------------

            self.verboseHelp = textwrap.dedent('''

            log/display verbose troubleshooting details for application
            program activity tracking diagnostic messages (default = False)

            ''')

            #--------------------------------------------------------------

            self.versionHelp = textwrap.dedent('''

            show the build version of this software (including its title,
            version and date) and exit

            ''')

        #------------------------------------------------------------------

        def getOptions(self):
            '''
            Parse the command line and return a list of positional arguments
            and a dictionanary of keyword options.
            '''
            parser = OptionParser(usage=self.usageHelp)

            #--------------------------------------------------------------

            parser.add_option(
                '-v', '--version',
                action='store_true',
                dest='version',
                default=False,
                help=self.versionHelp)

            #--------------------------------------------------------------

            parser.add_option(
                '-a', '--about',
                action='store_true',
                dest='about',
                default=False,
                help=self.aboutHelp)

            #--------------------------------------------------------------

            parser.add_option(
                '-o', '--output',
                action='store',
                dest='output',
                default='./%s.txt' % self.getRunTimeTitle(),
                type=str,
                help=self.outputHelp)

            #--------------------------------------------------------------

            parser.add_option(
                '-d', '--debug',
                action='store_true',
                dest='debug',
                default=False,
                help=self.debugHelp)

            #--------------------------------------------------------------

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

        #------------------------------------------------------------------

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

        #------------------------------------------------------------------

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

        enableDefaultCommandLineParser=True,

        logs=[],

        runTimeEntryPoint=prototype)

    myApp.Wrapper()

