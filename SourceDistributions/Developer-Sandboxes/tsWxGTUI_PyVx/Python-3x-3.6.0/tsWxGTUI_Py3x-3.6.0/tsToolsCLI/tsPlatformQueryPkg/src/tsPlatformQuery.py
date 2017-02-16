#! /usr/bin/env python
#"Time-stamp: <03/22/2015  4:20:16 PM rsg>"
'''
tsPlatformQuery - Tool to capture current hardware and software
information about the run time environment available to computer
programs.
'''
#################################################################
#
# File: tsPlatformQuery.py
#
# Purpose:
#
#     Tool to capture current hardware and software information
#     about the run time environment available to computer
#     programs.
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
# Usage (example):
#
#     tsPlatformQuery.py
#
# Classes:
#
#    TsPRTEOperatorSettingsParser - Class to incorporate features in
#           tsOperatorSettingsParser.
#
# Methods:
#
#    TsPRTEOperatorSettingsParser.__init__
#    TsPRTEOperatorSettingsParser.argsFormatter
#    TsPRTEOperatorSettingsParser.dedentFormatter
#    TsPRTEOperatorSettingsParser.getAbout
#    TsPRTEOperatorSettingsParser.getCommandLineParserModule
#    TsPRTEOperatorSettingsParser.getDebug
#    TsPRTEOperatorSettingsParser.getHelp
#    TsPRTEOperatorSettingsParser.getInput
#    TsPRTEOperatorSettingsParser.getOutput
#    TsPRTEOperatorSettingsParser.getProperties
#    TsPRTEOperatorSettingsParser.getRunTimeTitle
#    TsPRTEOperatorSettingsParser.getRunTimeTitleVersionDate
#    TsPRTEOperatorSettingsParser.getVerbose
#    TsPRTEOperatorSettingsParser.getVersion
#    TsPRTEOperatorSettingsParser.helpAbout
#    TsPRTEOperatorSettingsParser.helpDebug
#    TsPRTEOperatorSettingsParser.helpHelp
#    TsPRTEOperatorSettingsParser.helpPurpose
#    TsPRTEOperatorSettingsParser.helpVerbose
#    TsPRTEOperatorSettingsParser.helpVersion
#    TsPRTEOperatorSettingsParser.optionsFormatter
#    TsPRTEOperatorSettingsParser.parseCommandLineDispatch
#    TsPRTEOperatorSettingsParser.parseCommandLineUsageViaArgParse
#    TsPRTEOperatorSettingsParser.parseCommandLineUsageViaGetOpt
#    TsPRTEOperatorSettingsParser.parseCommandLineUsageViaOptParse
#    TsPRTEOperatorSettingsParser.parseCommandLineViaArgParse
#    TsPRTEOperatorSettingsParser.parseCommandLineViaGetOpt
#    TsPRTEOperatorSettingsParser.parseCommandLineViaOptParse
#    TsPRTEOperatorSettingsParser.setAbout
#    TsPRTEOperatorSettingsParser.setDebug
#    TsPRTEOperatorSettingsParser.setHelp
#    TsPRTEOperatorSettingsParser.setOutput
#    TsPRTEOperatorSettingsParser.setProperties
#    TsPRTEOperatorSettingsParser.setVerbose
#    TsPRTEOperatorSettingsParser.setVersion
#    TsPRTEOperatorSettingsParser.unknown
#
#    theMainApplication - Display program name, version and date.
#          Receive and validate command line options and arguments.
#          Display help, error and status information. Initiate
#          the file directory copy.
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
#    2015/03/22 rsg Removed the optparse-based internal class
#                   OperatorSettingsParser in order to use
#                   the tsPRTEOperatorSettingsParser, which
#                   automatically use the highest-level
#                   available parser (getopt, optparse or
#                   argparse) available on the platform.
#
# ToDo:
#
#################################################################

__title__     = 'tsPlatformQuery'
__version__   = '2.3.0'
__date__      = '03/22/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

#----------------------------------------------------------------------

import os.path
import platform
import sys
import string
import textwrap

try:
    import argparse
    PARSER_ARGPARSE_AVAILABLE = True
except:
    PARSER_ARGPARSE_AVAILABLE = False

try:
    from optparse import OptionParser
    PARSER_OPTPARSE_AVAILABLE = True
except:
    PARSER_OPTPARSE_AVAILABLE = False

try:
    import getopt
    PARSER_GETOPT_AVAILABLE = True
except:
    PARSER_GETOPT_AVAILABLE = False

#----------------------------------------------------------------------

import tsLibCLI

#----------------------------------------------------------------------

import tsCommandLineEnv
import tsExceptions as tse
import tsLogger as Logger
import tsPlatformRunTimeEnvironment as tsquery
import tsReportUtilities

##Logger = tsLogger
##tse = tsExceptions
##tsquery = tsPlatformRunTimeEnvironment

#--------------------------------------------------------------------------

DEBUG = False
VERBOSE = False

EnableEarliestAncestor = True
EnableOptionsGNU = True
EnableArgParsePositionalArguments = False # N/A for OptParse & GetOpt
runTimeTitleEnabled = True
theAssignedLogger = None
tracebackEnabled = False

###########################################################################
# The following "Help" messages are used to configure each of the Python
# version specific command line parsers: "argparse", "optparse" and
# "getopt".
#
# This primarily ensures consistancy between user interfaces and second-
# arily eliminates multiple duplications of the "Help" messages.
###########################################################################

#----------------------------------------------------------------------

aboutHelp = textwrap.dedent('''

show a summary of the terms & conditions for users of this
software (including the applicable product identification,
authors, contributors, copyrights, licenses and purpose)
and exit

''')

#----------------------------------------------------------------------

debugHelp = textwrap.dedent('''

log/display application program progress and diagnostic messages
useful in debugging and troubleshooting.
(default = False).

''')

#----------------------------------------------------------------------

descriptionHelp = textwrap.dedent('''

BACKGROUND

This is a multipurpose application program. It explores and
demonstrates the functionality, enhanceability and portability
of evolving user interface technology.

Featuring a character mode, Command Line Interface (CLI), the
application program has been implemented entirely in the Python
programming language, it has been developed for use with evolving
Python 2.x releases (currently 2.7.9). The application extracts
keyword-value pair options and positional arguments via the
appropriate Python library module:

    "argparse" (introduced with Python 2.7.0 and 3.2.0)
    "optparse" (introduced with Python 2.3.0 and 3.0.0;
                subsequently deprecated by argparse)
    "getopt"   (introduced with Python 1.6.0 and 3.0.0)

The Python 2to3 utility has been used to create a baseline Python
3.x release (currently 3.4.2) compatible version which is then
debugged to resolve the few remaining conversion issues (such as
options for: 1) file open mode; 2) curses terminal name byte string
encoding/decoding; and 3) exception handling).

FEATURES

This is a tool to capture current hardware and software information
about the run time environment available to computer programs.

''')

#----------------------------------------------------------------------

examplesHelp = textwrap.dedent('''

Examples:

    Interpreter   program app.      operator settings
    -----------   ----------------  -----------------------------
    python        %prog.py

    python2.7     %prog.py \\
                                    [-h] [-v] [-a] \\
                                    [-o OUTPUTFILE] \\
                                    [-d] [-V]

    python3.3     %prog.py \\
                                    [--help] [--version] [--about] \\
                                    [--output OUTPUTFILE] \\
                                    [--debug] [--Verbose]

        ---------------------------------------------------------
        Key:

            "python"    - Default interpreter for platform

            "python2.7" - First alternate interpreter for platform

            "python3.3" - Second alternate interpreter for platform

            "[]" - Brackets enclose option keywords and values

            "{}" - Braces enclose option value choices and
                   positional arguments

''')

#----------------------------------------------------------------------

outputHelp = textwrap.dedent('''

log/display current hardware and software information
about the run time environment to this output file
(default = "././%s_RunTimeEnvironment")

''')

#----------------------------------------------------------------------

moduleHelp = textwrap.dedent('''

sets default for standard Python parser module.
(To demonstrate the similarity and differences between Optional and
 Positional Arguments, an Optional Argument is used to set the latest
 Python recommendation, "argparse", while a Positional Argument is used
 to override it with a now Python deprecated "optparse" or "getopt")

''')

#----------------------------------------------------------------------

optionsHelp = textwrap.dedent('''

Optional Aguments:
  -h, --help            show this help message and exit
  -v, --version         show the build version of this software (including its
                        title, version and date) and exit
  -a, --about           show a summary of the terms & conditions for users of
                        this software (including the applicable product
                        identification, authors, contributors, copyrights,
                        licenses and purpose) and exit
  -o OUTPUT, --output OUTPUT
                        log/display source file metrics (source type, code
                        lines, comment lines, total lines, words, characters)
                        for each invidual file and for collection of files to
                        this output file (default =
                        "./%s%s" % (%prog, "_RunTimeEnvironment").
  -d, --debug           log/display application program progress and
                        diagnostic messages useful in debugging and
                        troubleshooting. (default = False).
  -V, --Verbose         log/display verbose troubleshooting details for
                        application program activity tracking diagnostic
                        messages (default = False)

''')

#----------------------------------------------------------------------

positionalHelp = textwrap.dedent('''

Positional Arguments:
  None

''')

#----------------------------------------------------------------------

##syntaxHelp = textwrap.dedent('''

##Syntax:

##    <python-interpreter> <program> [Keyword-Value Option(s)] ... \\
##                                   [Positional Argument(s)] ...

##''')

syntaxHelp = textwrap.dedent('''

Syntax:

    <python-interpreter> <program> [Keyword-Value Option(s)] ...

''')

#----------------------------------------------------------------------

usageHelp = textwrap.dedent('''

Usage:

    %prog \\

            [-h] [-v] [-o OUTPUT] \\
            [-d] [-V]

''')

#----------------------------------------------------------------------

verboseHelp = textwrap.dedent('''

log/display verbose troubleshooting details for application
program activity tracking diagnostic messages (default = False)

''')

#----------------------------------------------------------------------

versionHelp = textwrap.dedent('''

show the build version of this software (including its title,
version and date) and exit

''')

class TsPRTEOperatorSettingsParser(object):
    '''
    Class to parse the command line entered by the operator of an
    application program. Parsing extracts the Keyword-Value pair
    Options and Positional Arguments that will configure and
    control the application during its execution.
    '''

    #----------------------------------------------------------------------

    def __init__(self):
        '''
        Class constructor.
        '''

        # self.CommandLineEnv = CommandLineEnv.__App
        self.sysArgs = []
        self.sysOptions = {}
        if False and DEBUG and VERBOSE:
            print('\n\n\tsysArgs="%s"' % str(self.sysArgs))
            print('\n\tsysOptions="%s"\n' % str(self.sysOptions))

        self.parent = tsCommandLineEnv.CommandLineEnv._App

        self.logger = Logger.TsLogger(
            name=Logger.StandardOutputFile,
            threshold=Logger.INFO)

        self.logger.info('dir(self.parent)=%s' % str(dir(self.parent)))

##        self.reportWrapper = textwrap.TextWrapper(
##          width=60,
##            initial_indent' ',
##            subsequent_indent'    ',
##            break_long_words=True)

        # Initialize default state of positional arguments (args)
        # and keyword-value pairs (options) that will
        # be overridden during command line parsing
        self.args = []        # callback preempts return of value
        self.options = {
            'about':   False, # callback preempts return of value
            'debug':   False,
            'help':    False, # callback preempts return of value
            'input':   './',
            'output':  './%s.txt' % self.getRunTimeTitle(),
            'Verbose': False,
            'version': False  # callback preempts return of value
        }

        # self.parseCommandLineViaOptParse()
        # self.parseCommandLineDispatch()
        # print(self.parent.getRunTimeTitle())
        # print(self.getOptions())
        # self.helpHelp()

    #----------------------------------------------------------------------

    def unknown(self, opts, resultsOptions):
        '''
        Troubleshoot unknown optional arguments.
        '''

        if False and DEBUG and VERBOSE:

            print('unknown: opts=%s' % opts)
            print('unknown: resultsOptions=%s' % resultsOptions)

        unsortedOptions = {}
        for entry in opts:
            keyword = entry[0]
            value = entry[1]
            unsortedOptions[keyword] = value

        sortedOptionKeys = sorted(unsortedOptions.keys())

        if False and DEBUG and VERBOSE:

            print('unknown: sortedOptionKeys=%s' % sortedOptionKeys)

        for keyword in sortedOptionKeys:
            value = unsortedOptions[keyword]
            if keyword in ('-h', '--help'):

                self.Help = True
                self.parseCommandLineUsageViaGetOpt()
                print('\nNo Error')
                sys.exit(0)

            elif keyword in ('-v', '--version'):

                self.Version = True
##                print('Version:')
##                print('    %s' % mainTitleVersionDate)
##                print('\nNo Error')
##                sys.exit(0)

            elif keyword in ('-a', '--about'):

                self.About = True
                resultsOptions['about'] = True

            elif keyword in ('-d', '--debug'):

                self.Debug = True
                resultsOptions['debug'] = value

            elif keyword in ('-o', '--output'):

                self.Output = value

            elif keyword in ('-V', '--Verbose'):

                self.Verbose = True

            else:

                # assert False, 'unhandled option'
                fmt1 = '%s.parseCommandLineViaGetOpt: ' % __title__
                fmt2 = 'Unhandled Option ' + \
                    '(Keyword=%s; Value=%s)' % (keyword, value)
                msg = fmt1 + fmt2
                if False and DEBUG and VERBOSE:
                    print(msg)
                self.logger.error(msg)
                sys.exit(2)

    #----------------------------------------------------------------------

    def argsFormatter(self, initialIndent, argsText):
        '''
        Format a list of positional arguments so that each one will be
        displayed on a line by itself.
        '''
        comma = ','
        commaReplacement = comma + initialIndent + '\t\t '
        lines = argsText.replace(comma, commaReplacement)
        text = initialIndent + 'args: %s' % lines
        return (text)

    #----------------------------------------------------------------------

    def dedentFormatter(self, inputBuffer):
        '''
        Unwrap contents of buffer.
        '''
        lines = inputBuffer.split('\n')
        outputBuffer = ''
 
        for line in lines:
            text =  '\n%s' % line.lstrip()
            outputBuffer += text
        return (outputBuffer)

    #----------------------------------------------------------------------

    def getAbout(self):
        '''
        Return False, by default, after initialization and True after
        operator entered "-a"/"--about" key-word option.
        '''
        return (self.options['about'])

    #----------------------------------------------------------------------

    def getDebug(self):
        '''
        Return False, by default, after initialization and True after
        operator entered "-d"/"--debug" key-word option.
        '''
        return (self.options['debug'])

    #----------------------------------------------------------------------

    def getHelp(self):
        '''
        Return False, by default, after initialization and True after
        operator entered "-ha"/"--help" key-word option.
        '''
        return (self.options['help'])

    #----------------------------------------------------------------------

    def getInput(self):
        '''
        Return default value, after initialization and input value after
        operator entered "-i"/"--input" key-word option.
        '''
        return (self.options['input'])

    #----------------------------------------------------------------------

    def getOutput(self):
        '''
        Return default value, after initialization and output value after
        operator entered "-o"/"--output" key-word option.
        '''
        return (self.options['output'])

    #----------------------------------------------------------------------

    def getProperties(self):
        '''
        Return lookup table of keyword-get-property pairs.
        '''
        theGetProperties = {
            'about': self.getAbout(),
            'debug': self.getDebug(),
            'help': self.getHelp(),
            'output': self.getOutput(),
            'Verbose': self.getVerbose(),
            'version': self.getVersion()
            }

        return (theGetProperties)

    #----------------------------------------------------------------------

    def getVerbose(self):
        '''
        Return False, by default, after initialization and True after
        operator entered "-V"/"--Verbose" key-word option.
        '''
        return (self.options['Verbose'])

    #----------------------------------------------------------------------

    def getVersion(self):
        '''
        Return False, by default, after initialization and True after
        operator entered "-v"/"--version" key-word option.
        '''
        return (self.options['version'])

    #----------------------------------------------------------------------

    def setAbout(self, value):
        '''
        Set True after operator entered "-a"/"--about" key-word option.
        '''
        self.options['about'] = value
        self.helpAbout()

        print('\nNo Error')

        sys.exit(0)

    #----------------------------------------------------------------------

    def setDebug(self, value):
        '''
        Set True after operator entered "-d"/"--debug" key-word option.
        '''
        self.options['debug'] = value

    #----------------------------------------------------------------------

    def setHelp(self, value):
        '''
        Set True after operator entered "-h"/"--help" key-word option.

        NOTES:

        1) This function whould only be invoked by "getopt".

        2) "argparse" and "optparse" automatically intercept and
           handle operator requests for help.
        '''
        self.options['help'] = value
        self.helpHelp()

        print('\nNo Error')
        sys.exit(0)

    #----------------------------------------------------------------------

    def setOutput(self, value):
        '''
        Set value after operator entered "-o"/"--output" key-word option.
        '''
        self.options['output'] = value

    #----------------------------------------------------------------------

    def setProperties(
        self,
        about,
        debug,
##      help,
        output,
        version,
        Verbose):
        '''
        Return lookup table of keyword-set-property pairs.
        '''

        # Process action/exit properties (about, help version)
        # before state (flag/value ones)
        if about:
            self.setAbout(about)

##        self.Help = help

        if version:
            self.setVersion(version)

        # Process state (flag/value) properties
        # after action/exit ones (about, help, version)

        self.setDebug(debug)
        self.setOutput(output)
        self.setVerbose(Verbose)

##        return (theSetProperties)

    #----------------------------------------------------------------------

    def setVerbose(self, value):
        '''
        Set True after operator entered "-V"/"--Verbose" key-word option.
        '''
        self.options['Verbose'] = value

    #----------------------------------------------------------------------

    def setVersion(self, value):
        '''
        Set True after operator entered "-v"/"--version" key-word option.
        '''
        self.options['version'] = value
        self.helpVersion()

        print('\nNo Error')
        sys.exit(0)

    #----------------------------------------------------------------------

    def optionsFormatter(self, initialIndent, optionsText):
        '''
        Format a dictionary of keyword-value pair options so that each
        pair will be displayed on a line by itself.
        '''
        comma = ','
        commaReplacement = comma + initialIndent + '\t '

        lines = optionsText.replace(comma, commaReplacement)

        text = initialIndent + 'options: %s' % lines

        return (text)

    #----------------------------------------------------------------------

    def helpAbout(self):
        '''
        helpAbout
        '''
        print('\n\nAbout:')

        lines = self.parent.buildHeader.split('\n')

        for line in lines:
            print('\t%s' % line)

        print('\nPurpose:\n')

        lines = self.parent.buildPurpose.split('\n')

        for line in lines:
            print('\t%s' % string.lstrip(line))

        print('\nDescription:')

        lines = descriptionHelp.split('\n')
        for line in lines:

            print('\t%s' % line)

        try:

            sampleOutput = './tsToolsCLI/tsPlatformQueryPkg' + \
                           '/sampleHelp' + \
                           '/%s%s'  % (self.getRunTimeTitle(),
                                       '_RunTimeEnvironment.txt')

            fileID = open(sampleOutput, 'r')

            print('\nSample Output:')

            # wrappedlines = self.reportWrapper(aboutSampleOutput)
            #lines = wrappedLines.split('\n')

            for line in fileID:

                print('%s' % line.strip('\n'))

        except Exception as errorCode:

            fmt1 = '%s' % self.getRunTimeTitle()
            fmt2 = '.tsPRTEOperatorSettingsParser: ' + \
                   'errorCode="%s"\n' % str(errorCode)
            msg = fmt1 + fmt2
            self.logger.warning(msg)

    #----------------------------------------------------------------------

    def helpDebug(self):
        '''
        helpDebug
        '''
        print(self.helpDebug.__doc__)

    #----------------------------------------------------------------------

    def helpHelp(self):
        '''
        '''
        print(syntaxHelp.__doc__.replace(
        '%prog', '%s.py' % self.getRunTimeTitle()))

        print('\nHelp')
        lines = syntaxHelp.split('\n')
        for line in lines:
            print('%s' % line.replace('%prog',
            self.getRunTimeTitle() + '.py'))

        print('\nUsage:')
        lines = usageHelp.split('\n')
        for line in lines:
            print('  %s' % line.replace('%prog',
            self.getRunTimeTitle() + '.py'))

    #----------------------------------------------------------------------

    def helpPurpose(self):
        '''
        helpPurpose
        '''
        print('\nPurpose:\n')

    #----------------------------------------------------------------------

    def helpVerbose(self):
        '''
        helpVerbose
        '''
        print(self.helpVerbose.__doc__)

    #----------------------------------------------------------------------

    def helpVersion(self):
        '''
        helpVersion
        '''
        print('\nVersion:')
        print('\n    %s' % self.parent.buildTitleVersionDate)

    #------------------------------------------------------------------

    def getCommandLineParserModule(self, rawArgsOptions):
        '''
        Return the lower case module name of the Command Line Parser as
        appropriate to the Python version unless specified by the operator
        via a case-insensitive positional argument (e.g. "argparse",
        "OptParse" or "GETOPT").
        '''
        if PARSER_ARGPARSE_AVAILABLE:

            theParserModule = 'argparse'

        elif PARSER_OPTPARSE_AVAILABLE:

            theParserModule = 'optarse'

        else:

            theParserModule = 'getopt'

        print('\n\tCommand Line Parser Module = "%s"' % theParserModule)
        msg = 'Command Line Parser Module = "%s"' % theParserModule
        self.logger.info(msg)

        return (theParserModule)

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

    #----------------------------------------------------------------------

    def parseCommandLineDispatch(self):
        '''
        Stub to substitute for non-existant parseCommandLine. Returns
        non-application specific behavior and results appropriate for
        the latest Python parser module ("argparse", "optparse" or
        "getopt") available to the application.
        '''
        rawArgsOptions = sys.argv[1:]
        if False and DEBUG and VERBOSE:
            print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        CommandLineParserModule = self.getCommandLineParserModule(
            rawArgsOptions)

        if CommandLineParserModule == 'argparse':

            (args, options) = self.parseCommandLineViaArgParse()

        elif CommandLineParserModule == 'optparse':

            (args, options) = self.parseCommandLineViaOptParse()

        else:

            (args, options) = self.parseCommandLineViaGetOpt()

        if False and DEBUG and VERBOSE:

            print('\n\t%s.parseCommandLineDispatch: ' % __title__)
            print(self.argsFormatter('\n\t', str(args)))
            print(self.optionsFormatter('\n\t', str(options)))

##            print('\n\n\tproperties:')
##            print('\t\tabout=%s' % str(self.About))
##            print('\t\thelp=%s' % str(self.Help))
##            print('\t\tversion=%s' % str(self.Version))
##            print('\t\tDebug=%s' % str(self.Debug))
##            print('\t\tOutput=%s' % str(self.Output))
##            print('\t\tVerbose=%s' % str(self.Verbose))

##      self.logger.info(
##          'parseCommandLineDispatch = %s' % CommandLineParserModule)

        return (args, options)

    #----------------------------------------------------------------------

    def parseCommandLineUsageViaArgParse(self):
        '''
        Create the default help display for this application using
        standardized components. Disable use of unwanted optional
        features and those features that are supplied by the standard
        Python parser module (argparse, optparse and getopt).
        '''
        theCommandLineHelp = '\n'

        ShowPurposeHelp = True
        ShowSyntaxHelp = True
        ShowExamplesHelp = True
        ShowUsageHelp = False
        ShowOptionsHelp = False
        ShowPositionalHelp = False

        if ShowPurposeHelp:

            theCommandLineHelp += '\nPurpose:\n'
            lines = self.parent.buildPurpose.split('\n')
            for line in lines:
                theCommandLineHelp += '\n\t%s' % line

        if ShowSyntaxHelp:

            theCommandLineHelp += syntaxHelp

        if ShowExamplesHelp:

            theCommandLineHelp += examplesHelp

        if ShowUsageHelp:

            theCommandLineHelp += usageHelp

        if ShowOptionsHelp:

            theCommandLineHelp += optionsHelp

        if ShowPositionalHelp:

            theCommandLineHelp += positionalHelp

        return (theCommandLineHelp)

    #----------------------------------------------------------------------

    def parseCommandLineUsageViaGetOpt(self):
        '''
        Create the default help display for this application using
        standardized components. Disable use of unwanted optional
        features and those features that are supplied by the standard
        Python parser module (argparse, optparse and getopt).
        '''
        theCommandLineHelp = '\n'

        ShowPurposeHelp = True
        ShowSyntaxHelp = True
        ShowExamplesHelp = True
        ShowUsageHelp = True
        ShowOptionsHelp = True
        ShowPositionalHelp = True

        if ShowUsageHelp:

            theCommandLineHelp += usageHelp

        if ShowPurposeHelp:

            theCommandLineHelp += '\nPurpose:\n'
            lines = self.parent.buildPurpose.split('\n')
            for line in lines:
                theCommandLineHelp += '\n\t%s' % line

        if ShowSyntaxHelp:

            theCommandLineHelp += syntaxHelp

        if ShowExamplesHelp:

            theCommandLineHelp += examplesHelp

        if ShowOptionsHelp:

            theCommandLineHelp += optionsHelp

        if ShowPositionalHelp:

            theCommandLineHelp += positionalHelp

        return (theCommandLineHelp)

    #----------------------------------------------------------------------

    def parseCommandLineUsageViaOptParse(self):
        '''
        Create the default help display for this application using
        standardized components. Disable use of unwanted optional
        features and those features that are supplied by the standard
        Python parser module (argparse, optparse and getopt).
        '''
        theCommandLineHelp = '\n'

        ShowPurposeHelp = True
        ShowSyntaxHelp = True
        ShowExamplesHelp = True
        ShowUsageHelp = True
        ShowOptionsHelp = False
        ShowPositionalHelp = True

        if ShowUsageHelp:

            theCommandLineHelp += usageHelp.replace('\nUsage:\n', '')

        if ShowPurposeHelp:

            theCommandLineHelp += '\nPurpose:\n'
            lines = self.parent.buildPurpose.split('\n')
            for line in lines:
                theCommandLineHelp += '\n\t%s' % line

        if ShowSyntaxHelp:

            theCommandLineHelp += syntaxHelp

        if ShowExamplesHelp:

            theCommandLineHelp += examplesHelp

        if ShowOptionsHelp:

            theCommandLineHelp += optionsHelp

        if ShowPositionalHelp:

            theCommandLineHelp += positionalHelp

        return (theCommandLineHelp)

    #----------------------------------------------------------------------

    def parseCommandLineViaArgParse(self):
        '''
        Parse the command line and extract any keyword-value pair and
        positional arguments.
        '''

##        import argparse

        print('\n')

        ShowEnhancedArgParseHelp = True
        ShowExamplesHelp = True
        ShowSyntaxHelp = False

        if ShowEnhancedArgParseHelp:

            parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent(
                    self.parseCommandLineUsageViaArgParse()).replace(
                    '%prog', '%s.py' % self.getRunTimeTitle()))

        elif ShowExamplesHelp:

            parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent(
                    examplesHelp).replace(
                    '%prog', '%s.py' % self.getRunTimeTitle()))

        elif ShowSyntaxHelp:

            parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent(
                    syntaxHelp).replace(
                    '%prog', '%s.py' % self.getRunTimeTitle()))

        else:

            # Show only Usage and description of Keyword Optiona
            # and Positional Agruments
            parser = argparse.ArgumentParser()

        #------------------------------------------------------------------

        parser.add_argument(
            '-v', '--version',
            action='store_true',
            dest='version',
            help=textwrap.dedent(versionHelp).replace(
                '%prog', '%s.py' % self.getRunTimeTitle()))

        #------------------------------------------------------------------

        parser.add_argument(
            '-a', '--about',
            action='store_true',
            dest='about',
            default=False,
            help=textwrap.dedent(aboutHelp).replace(
                '%prog', '%s.py' % self.getRunTimeTitle()))

        #------------------------------------------------------------------

        parser.add_argument(
            '-o', '--output',
            action='store',
            dest='output',
            default='./%s_%s' % (self.getRunTimeTitle(),
                                 '_RunTimeEnvironment.txt'), 
            help=textwrap.dedent(outputHelp).replace(
                '%prog', '%s.py' % self.getRunTimeTitle()))

        #------------------------------------------------------------------

        parser.add_argument(
            '-d', '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help=textwrap.dedent(debugHelp).replace(
                '%prog', '%s.py' % self.getRunTimeTitle()))

        #------------------------------------------------------------------

        parser.add_argument(
            '-V', '--Verbose',
            action='store_true',
            dest='Verbose',
            default=False,
            help=textwrap.dedent(verboseHelp).replace(
                '%prog', '%s.py' % self.getRunTimeTitle()))

        #------------------------------------------------------------------

##        if EnableArgParsePositionalArguments:

##            parser.add_argument(
##                'module',
##                choices=['argparse', 'optparse', 'getopt'],
##                help=textwrap.dedent(moduleHelp).replace(
##                    '%prog', '%s.py' % self.getRunTimeTitle()))

##        else:

##            parser.add_argument(
##                '-m', '--module',
##                action='store',
##                dest='module',
##                default='argparse',
##                choices=['argparse'],
##                help=textwrap.dedent(moduleHelp).replace(
##                    '%prog', '%s.py' % self.getRunTimeTitle()))

        # The parser returns a keyword-value pair for each command line
        # option. Each returned keyword is the attribute name specified
        # for the option dest parameter. Each returned attribute value
        # is the parsed commmand line value.
        results = parser.parse_args()

##        if EnableArgParsePositionalArguments:

##            try:

##                if False and DEBUG and VERBOSE:
##                    print('\tresults (before remove module)=' + \
##                          '"%s"' % str(results))

##                delattr(results, 'module')

##                if False and DEBUG and VERBOSE:
##                    print('\n\tresults (after remove module)=' + \
##                          '"%s"' % str(results))

##            except Exception as optionsError:

##                print('\t\toptionsError="%s"' % str(optionsError))

        try:
            options = vars(results)
        except AttributeError:
            options = {}


        if not EnableArgParsePositionalArguments:

            try:
                args = [results.module]
            except AttributeError:
                args = ['argparse']

        if False and DEBUG and VERBOSE:

            print('>>>>> options: %s; type: %s' %(
                str(options),
                str(type(options))))
            print('>>>>> options.about: %s; type: %s' %(
                str(options['about']),
                str(type(options['about']))))

        self.setProperties(
            options['about'],
            options['debug'],
##          options['help'],
            options['output'],
            options['version'],
            options['Verbose'])

        return (args, options)

    #----------------------------------------------------------------------

    def parseCommandLineViaGetOpt(self):
        '''
        Parse the command line and extract any keyword-value pair and
        positional arguments.
        '''
##        import getopt

        print('\n')

        rawArgsOptions = sys.argv[1:]
        lenRawArgsOptions = len(rawArgsOptions)

        if True:

            # TBD - Workaround to ensure operator gets response
            #       to request for help.

            for rawArg in rawArgsOptions:
                if ((rawArg == '-h') or \
                    (rawArg == '-h')):

                    lines = self.parseCommandLineUsageViaGetOpt().split('\n')
                    print('\n')
                    for line in lines:
                        print('%s' % line.replace(
                            '%prog', self.getRunTimeTitle()))
                    print('\nNo Error')
                    sys.exit(0)

        if False and DEBUG and VERBOSE:
            print(
                '\n\n\t\tlenRawArgsOptions=%d; rawArgsOptions=%s' % (
                    lenRawArgsOptions, str(rawArgsOptions)))

        if lenRawArgsOptions == 0:

            availableArgsOptions = []
            self.logger.debug('parseCommandLineViaGetOpt: ' + \
                              'availableArgsOptions = "%s"' % str(
                                  availableArgsOptions))

        elif rawArgsOptions[lenRawArgsOptions - 1].lower() in [
            'argparse', 'optparse', 'getopt']:

            availableArgsOptions = rawArgsOptions[0:lenRawArgsOptions - 1]

        else:

            availableArgsOptions = rawArgsOptions

        if False and DEBUG and VERBOSE:
            print(
                '\n\n\t\tavailableArgsOptions=%s' % str(availableArgsOptions))

        resultsOptions = {
            "about": False,
            "help": False,
            "version": False,
            "debug": False,
            "output": "./%prog_RunTimeEnvironment.txt",
            "Verbose": False}

        resultsArgs = []

        try:

            if EnableOptionsGNU:

                rawArgsOptions = sys.argv[1:]
                shortOptionList = "ahvdo:V"
                longOptionList = ["about",
                                  "help",
                                  "version",
                                  "debug",
                                  "output=",
                                  "Verbose"]
                opts, args = getopt.gnu_getopt(
                    rawArgsOptions,
                    shortOptionList,
                    longOptionList)

            else:

                rawArgsOptions = sys.argv[1:]
                shortOptionList = "ahvdo:V"
                longOptionList = ["about",
                                  "help",
                                  "version",
                                  "debug",
                                  "output=",
                                  "Verbose"]

                opts, args = getopt.getopt(
                    rawArgsOptions,
                    shortOptionList,
                    longOptionList)

            if False and DEBUG and VERBOSE:

                fmt1 = '\n\t%s.parseCommandLineViaGetOpt: ' % __title__
                fmt2 = '\n\t\trawArgsOptions = "%s"; EnableOptionsGNU="%s"' % (
                    str(rawArgsOptions), str(EnableOptionsGNU))
                msg = fmt1 + fmt2
                print(msg)

        except getopt.GetoptError as errorCode:

            # print something like "option -a not recognized"
            print('%s' % str(errorCode))
            # parseCommandLineUsageViaGetOpt()
            sys.exit(2)

        except Exception as errorCode:

            # print help information and exit:
            fmt1 = '%s.parseCommandLineViaGetOpt: ' % __title__
            fmt2 = 'errorCode = "%s"; EnableOptionsGNU="%s"' % (
                str(errorCode), str(EnableOptionsGNU))
            msg = fmt1 + fmt2
            print(msg)

            self.logger.error(msg)
            sys.exit(2)

##          raise tse.ProgramException(
##              tse.APPLICATION_TRAP,
##              msg)

        maxArgs = min(1, len(args))

        extraArgs = []
        for index in range(len(args)):

            if index < maxArgs:

                pass

            else:

                extraArgs += [args[index]]

        if len(extraArgs) > 0:

            print('argument(s) %s not recognized' % str(
                extraArgs))
            self.parseCommandLineUsageViaGetOpt()
            sys.exit(2)

        if False and DEBUG:

            self.unknown(opts, resultsOptions)

        else:

            unsortedOptions = {}
            for entry in opts:
                keyword = entry[0]
                value = entry[1]
                unsortedOptions[keyword] = value

            sortedOptionKeys = sorted(unsortedOptions.keys())

            if False and DEBUG and VERBOSE:

                print('***** sortedOptionKeys=%s' % sortedOptionKeys)

            for keyword in sortedOptionKeys:
                value = unsortedOptions[keyword]
                if keyword in ('-h', '--help'):

                    self.Help = True
                    lines = self.parseCommandLineUsageViaGetOpt().split('\n')
                    for line in lines:
                        print('%s' % line.replace(
                            '%prog', self.getRunTimeTitle))
                    print('\nNo Error')
                    sys.exit(0)

                elif keyword in ('-v', '--version'):

                    self.Version = True
    ##                print('Version:')
    ##                print('    %s' % mainTitleVersionDate)
    ##                print('\nNo Error')
    ##                sys.exit(0)

                elif keyword in ('-a', '--about'):

                    self.About = True
                    resultsOptions['about'] = True

                elif keyword in ('-d', '--debug'):

                    self.Debug = True
                    resultsOptions['debug'] = value

                elif keyword in ('-o', '--output'):

                    self.Output = value

                elif keyword in ('-V', '--Verbose'):

                    self.Verbose = True

                else:

                    # assert False, 'unhandled option'
                    fmt1 = '%s.parseCommandLineViaGetOpt: ' % \
                           '%s' % self.getRunTimeTitle()
                    fmt2 = 'Unhandled Option ' + \
                        '(Keyword=%s; Value=%s)' % (keyword, value)
                    msg = fmt1 + fmt2
                    print(msg)
                    self.logger.error(msg)
                    sys.exit(2)

    ##                raise tse.OperatorSettingsParserException(
    ##                    tse.COMMAND_LINE_OPTION_DOES_NOT_EXIST,
    ##                    msg)

        resultsOptions = self.getProperties()

        for index in range(maxArgs):

            if index == 0:

                resultsArgs += [args[index]]

            elif index == 1:

                resultsArgs += [args[index]]

            else:

                print('argument[%d]="%s" is not recognized' % (
                    index, str(args[index])))
                self.parseCommandLineUsageViaGetOpt()
                sys.exit(2)

##                raise tse.OperatorSettingsParserException(
##                    tse.COMMAND_LINE_ARGUMENT_DOES_NOT_EXIST,
##                    msg)

        return (resultsArgs, resultsOptions)

    #----------------------------------------------------------------------

    def parseCommandLineViaOptParse(self):
        '''
        Parse the command line and extract any keyword-value pair and
        positional arguments.
        '''

##        from optparse import OptionParser

        print('\n')

        parser = OptionParser()

        applicationUsage = textwrap.dedent(
            self.parseCommandLineUsageViaOptParse())

        parser = OptionParser(usage=applicationUsage)

        #------------------------------------------------------------------

        parser.add_option(
            '-v', '--version',
            action='store_true',
            dest='version',
            default=False,
            help=versionHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-a', '--about',
            action='store_true',
            dest='about',
            default=False,
            help=aboutHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-o', '--output',
            action='store',
            dest='output',
            default='./%s%s' % (self.getRunTimeTitle(),
                                '_RunTimeEnvironment.txt'), 
            help=outputHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-d', '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help=debugHelp)

        #------------------------------------------------------------------

        parser.add_option(
            '-V', '--Verbose',
            action='store_true',
            dest='Verbose',
            default=False,
            help=verboseHelp)

        #------------------------------------------------------------------

##        parser.add_option('module',
##                        help=moduleHelp)

        #------------------------------------------------------------------

        results = parser.parse_args()

        (optionsOptParse, argsOptParse) = results

        maxArgs = min(1, len(argsOptParse))
        if len(argsOptParse) > maxArgs:
            # parser.error("wrong number of arguments")
            extraArgs = []
            for index in range(maxArgs, len(argsOptParse)):
                extraArgs += argsOptParse[index]
            parser.error("\n\n\tinvalid argument(s) = %s" % str(extraArgs))

        maxArgs = min(2, len(argsOptParse))
        if len(argsOptParse) > maxArgs:
            # parser.error("wrong number of arguments")
            extraArgs = []
            for index in range(maxArgs, len(argsOptParse)):
                extraArgs += argsOptParse[index]
            parser.error("\n\n\tinvalid argument(s) = %s" % str(extraArgs))
 
##        for key in options.keys():
##          theGetProperty = self.getProperties[key]
##            value = theGetProperty()

        args = argsOptParse
        options = {}
        options['about'] = optionsOptParse.about
        options['debug'] = optionsOptParse.debug
##        options['help'] = optionsOptParse.help
        options['output'] =  optionsOptParse.output
        options['version'] = optionsOptParse.version
        options['Verbose'] = optionsOptParse.Verbose

        if DEBUG and VERBOSE:

            print('>>>>> options: %s; type: %s' %(
                str(options),
                str(type(options))))

            print('>>>>> options: %s; type: %s' %(
                str(options['about']),
                str(type(options['about']))))

        self.setProperties(
            options['about'],
            options['debug'],
##          options['help'],
            options['output'],
            options['version'],
            options['Verbose'])

        if DEBUG and VERBOSE:

            print('\n\ttsApplication.parseCommandLineViaOptParse: ' + \
                  '\n\t\tresults = %s;\n\t\ttype=%s' % (str(results),
                                                        type(results)))

            print('\n\ttsApplication.parseCommandLineViaOptParse: ' + \
                  'Args: %s' % str(args))

            print('\n\ttsApplication.parseCommandLineViaOptParse: ' + \
                  'Options: %s' % str(options))

        return (args, options)

    #----------------------------------------------------------------------

    About   = property(getAbout, setAbout)
    Debug   = property(getDebug, setDebug)
    Help    = property(getHelp, setHelp)
    Output  = property(getOutput, setOutput)
    Verbose = property(getVerbose, setVerbose)
    Version = property(getVersion, setVersion)

#--------------------------------------------------------------------------

def theMainApplication(*args, **kw):
    '''
    Display program name, version and date. Receive and validate
    command line options and arguments. Display help, error and
    status information. Initiate the file directory copy.
    '''
    # myParser = OperatorSettingsParser()
    myParser = TsPRTEOperatorSettingsParser()
    print('\n%s\n' % (
        myParser.getRunTimeTitleVersionDate()))

    (myArgs, myOptions) = myParser.parseCommandLineDispatch()

    myOutputPath = myOptions['output']
    myRunTimeEnvironment = tsquery.PlatformRunTimeEnvironment()
    myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

    sys.stdout.write('\tResults are available in "%s".\n\n' % \
                     myOutputPath)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

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

