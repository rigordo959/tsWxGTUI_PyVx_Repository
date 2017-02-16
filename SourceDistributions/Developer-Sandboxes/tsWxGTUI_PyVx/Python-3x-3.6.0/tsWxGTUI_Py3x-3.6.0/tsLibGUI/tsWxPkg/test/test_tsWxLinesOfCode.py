#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:39:09 AM rsg>"
'''
test_tsWxLinesOfCode.py - Application program to scan a file
directory and produce a report of the number of source code
files, lines of code, blank/comment lines, word count and
character count.
'''
#################################################################
#
# File: test_tsWxLinesOfCode.py
#
# Purpose:
#
#    Application program to scan a file directory and produce a
#    report of the number of source code files, lines of code,
#    blank/comment lines, word count and character count.
#
# Limitations:
#
#    Threading overhead is noticable. TaskBar Clock normally
#    updates, without threading every 1-3 seconds. With threading,
#    clock frequently does NOT update for minutes at a time.
#
#    Scans of extensive collection of files may take many minutes
#    depending on the platform.
#
#       Mac OS X scanned files 18977 of 83569 in  4 minutes.
#       Cygwin-X scanned files 15558 of 74819 in 22 minutes.
#                (Note: Non-xterm Cygwin aborted at GUI startup.)
#
# Notes:
#
#    The blank/comment lines represent a line that contains no
#    executable code. A blank line in one that contains no
#    alpha-numeric characters and is terminated by a new line
#    character(\n).
#
#    A single line comment is one that begins with a programming
#    language specific comment identifier (upper or lower case):
#        .ada          "--"
#        .asm          ";"
#        .bas          "rem"
#        .bash         "#"
#        .bat          "rem"
#        .c            "//"
#        .c++          "//"
#        .cpp          "//"
#        .csh          "#"
#        .f            "c"   "*"   "!"
#        .f77          "c"   "*"   "!"
#        .f90          "c"   "*"   "!"
#        .for          "c"   "*"   "!"
#        .ftn          "c"   "*"   "!"
#        .g77          "c"   "*"   "!"
#        .g90          "c"   "*"   "!"
#        .h            "//"
#        .inc          "c"   "*"   "!"
#        .ksh          "#"
#        .py           "#"
#        .sh           "#"
#
#    A multi-line comment is one that begins and ends with a programming
#    language specific comment identifier (shown as a begin-end pair):
#        .c            ("/*",   "*/")
#        .h            ("/*",   "*/")
#        .c++          ("/*",   "*/")
#        .cpp          ("/*",   "*/")
#        .pas          ("{ *",  " }")
#        .plm          ("/*",   "*/")
#        .py           ("'''", "'''") ('"""', '"""')
#
# Usage (example):
#
#     python test_tsWxLinesOfCode.py
#
# Methods:
#
#   None
#
# Modifications:
#
#   2011/12/15 rsg Added platform-dependent support for argparse
#                  and optparse based on Python version. The
#                  selection criteria is that optparse became
#                  deprecated with Python 2.7.0 or later.
#
# ToDo:
#
#   2011/12/12 rsg Propose elimination of treading overhead by
#                  launching Lines-Of-Code application process
#                  instead of application thread.
#
#   2011/12/12 rsg Troubleshoot IOError that occurs only on
#                  cygwin but not on Cygwin-X or Mac OS X.
#                  Cygwin message tail is:
#
#                  Starting open: name=<>; mode=<w>
#                  Ending open: name=<>; mode=<w>
#                  self.logs=[]
#                  Starting open: name=<>; mode=<w>
#                  Ending open: name=<>; mode=<w>
#                  Starting open: name=<>; mode=<w>
#                  Ending open: name=<>; mode=<w>
#                  Starting open: name=<>; mode=<w>
#                  Ending open: name=<>; mode=<w>
#                  ]0;/cygdrive/d/WR/SoftwareGadgetry-2.x
#                  rsg@eclecticxpvm /cygdrive/d/WR/SoftwareGadgetry-2.x
#
# Modifications:
#
#   2011/12/12 rsg Added threading capability so that GUI will
#                  update while non-time critical director scan
#                  runs in background.
#
#################################################################

__title__     = 'test_tsWxLinesOfCode'
__version__   = '1.3.0'
__date__      = '12/25/2011'
__authors__   = 'Richard S. Gordon, a.k.a. Software Gadgetry'
__copyright__ = 'Copyright (c) 2007-2011 Software Gadgetry. ' + \
                'All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

import math
import os
## import os.path
import platform
import sys
import textwrap
import _thread
import time
import traceback

optParseDeprecated = '2.7.0'
platformVersion = str(platform.python_version())
if (platformVersion < optParseDeprecated):

    from optparse import OptionParser

else:

    import argparse

DEBUG    = False  # Enables log with debugging details
SCAN_LOG = False  # Enables log with line by line scan parsing details
VERBOSE  = False  # Enables log with redirected output details

##if False and DEBUG:
##    # Import wingdbstub only if cygwin platform.
##    import platform
##    hostOS = platform.system().lower()
##    if hostOS.find('cygwin') != -1:
##        try:
##            import wingdbstub
##        except ImportError:
##            pass

try:
    import tsLibGUI
except ImportError:
    pass

import tsApplication as tsAPP
import tsExceptions as tse
import tsLogger as Logger
##from tsLogger import TsLogger as Logger

try:
    import tsLibGUI
except ImportError:
    pass
from tsWxTextCtrl import TextCtrl as wxTextCtrl

#########################################################################
# Begin Test Control Switches

threadingEnabled = True # True runs non-time critical code in a thread.

redirectEnabled = DEBUG
if redirectEnabled:
    if VERBOSE:
        redirectedFileName = 'redirectedFile.log'
    else:
        redirectedFileName = None
else:
    redirectedFileName = None

runTimeTitleEnabled = False
exceptionHandlingEnabled = True
frameSizingEnabled = False

centerOnScreenEnabled = False
tracebackEnabled = False

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

# End Test Control Switches
#########################################################################

theStatusBar = None

__help__ = '''
This program scans a file directory and produce a report of the number of source code files, lines of code, blank/comment lines, word count and character count.
'''

#--------------------------------------------------------------------------

if not exceptionHandlingEnabled:

    try:
        import wx
    except ImportError as wxImportError:
        import tsWx as wx

else:

    try:

        import tsWx as wx

    except Exception as theTsWxImportError:

        _stdout = sys.stdout
        _stderr = sys.stderr

        _stderr.write('%s' % __header__)

        exitStatus = tse.NONERROR_ERROR_CODE
        msg = tse.NO_ERROR

        if isinstance(theTsWxImportError, tse.TsExceptions):

            exitStatus = theTsWxImportError.exitCode
            msg = '%s. [ExitCode #%d]' % (
                str(theTsWxImportError).replace("'", ""), exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                tse.displayError(theTsWxImportError)

        elif isinstance(theTsWxImportError, ImportError):

            exitStatus = 128 # TBD - tse.INVALID_ERROR_CODE
            msg = '%s. %s. %s. [ExitCode #%d]' % (
                tse.USER_INTERFACE_EXCEPTION,
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE,
                theTsWxImportError,
                exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        else:

            exitStatus = tse.INVALID_ERROR_CODE
            msg = "Unexpected error: %s [ExitCode #%d]" % (
                sys.exc_info()[0], exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        _stderr.write('\n%s\n' % msg)

        # Return (exitStatus)
        sys.exit(exitStatus)

#--------------------------------------------------------------------------

def getArgParseOptions():
    '''
    Parse the command line and return a list of positional arguments
    and a dictionanary of keyword options.

    NOTE: Requirement is an inappropriate, oversimplification.
          Invoking argparse or optparse (deprecated with Python 2.7.0)
          do not produce equivalent output without substantial post
          processing that has not yet been created. This may explain
          inability to migrate use of tsApplication to tsCommandLineEnv
          or to tsWxMultiFrameEnv.
    '''
    #########################################################
    # Begin declarations required to convert global constants
    # into command line option variables.
    global DEBUG
    global SCAN_LOG
    global VERBOSE
    # End declarations required to convert global constants
    #########################################################
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''

    %prog [Positional Arguments] [Keyword Arguments] ...

Syntax:

    python    %prog [-i=<input directory path>] [-o=<output file path>]
    python2.7 %prog [-i=<input directory path>] [-o=<output file path>]
    python3.2 %prog [-i=<input directory path>] [-o=<output file path>]

Description:

    "%prog" is an application program with a character
    mode, Graphical-style User Interface (GUI). Implemented entirely
    in the Python programming language, it is compatible with python
    versions 2.6 through 3.2.

    The application scans an input file directory and produces an output
    file that reports, for each source file, the number of lines of code,
    blank/comment lines, word count and character count. The output file
    also reports any files that were skipped because of an unrecognized
    "name.ext".

    The output file also includes a summary of the total, standard
    deviation, average and relative percentage of code and comment lines.
    The summary is also output to the GUI display.

Examples (default case):

    python %prog
    python %prog -i=./ -o=./tsWxLinesOfCodeStatistics.txt
    python %prog -i ./ -o ./tsWxLinesOfCodeStatistics.txt
    '''))

    #-----------------------------------------------------------------------

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s, v1.0.0')

    #-----------------------------------------------------------------------

    parser.add_argument(
        '-i', '--inputDirectoryPath',
        action='store',
        dest='input_Directory_Path',
        default='./',
        type=str,
        help='Directory of source code file(s) [default = ./]')

    #-----------------------------------------------------------------------

    parser.add_argument(
        '-o', '--outputFilePath',
            action='store',
            dest='output_File_Path',
            default='./tsWxLinesOfCodeStatistics.txt',
            type=str,
            help='Output file path/name [default = ' + \
            './tsLinesOfCodeStatistics.txt]')

    #-----------------------------------------------------------------------

    parser.add_argument(
        '--DebugDetails',
            action='store_true',
            dest='DEBUG',
            default=False,
            help='Log debugging details [default = False]')

    #-----------------------------------------------------------------------

    parser.add_argument(
        '--ScanDetails',
            action='store_true',
            dest='SCAN_LOG',
            default=False,
            help='Log line-by-line scan parsing details [default = False]')

    #-----------------------------------------------------------------------

    parser.add_argument(
        '--VerboseDetails',
            action='store_true',
            dest='VERBOSE',
            default=False,
            help='Log redirected output details [default = False]')

    # The parser returns a keyword-value pair for each command line
    # option. Each returned keyword is the attribute name specified
    # for the option dest parameter. Each returned attribute value
    # is the parsed commmand line value.
    options = parser.parse_args()
    args = []

    DEBUG = options.DEBUG
    SCAN_LOG = options.SCAN_LOG
    VERBOSE = options.VERBOSE

    if DEBUG and VERBOSE:
        print('  getArgParseOptions:\n')
        print('         Args: %s\n' % str(args))
        ## print('      Options: %s\n' % str(options))
        print('        DEBUG: %s\n' % str(DEBUG))
        print('     SCAN_LOG: %s\n' % str(SCAN_LOG))
        print('      VERBOSE: %s\n' % str(VERBOSE))

    return (args, options)

#--------------------------------------------------------------------------

def getOptParseOptions():
    '''
    Parse the command line and return a list of positional arguments
    and a dictionanary of keyword options.

    NOTE: Requirement is an inappropriate, oversimplification.
          Invoking argparse or optparse (deprecated with Python 2.7.0)
          do not produce equivalent output without substantial post
          processing that has not yet been created. This may explain
          inability to migrate use of tsApplication to tsCommandLineEnv
          or to tsWxMultiFrameEnv.
    '''
    #########################################################
    # Begin declarations required to convert global constants
    # into command line option variables.
    global DEBUG
    global SCAN_LOG
    global VERBOSE
    # End declarations required to convert global constants
    #########################################################
    parser = OptionParser(
        usage='''

    %prog [Positional Arguments] [Keyword Arguments] ...

Syntax:

    python    %prog [-i=<input directory path>] [-o=<output file path>]
    python2.7 %prog [-i=<input directory path>] [-o=<output file path>]
    python3.2 %prog [-i=<input directory path>] [-o=<output file path>]

Description:

    "%prog" is an application program with a character
    mode, Graphical-style User Interface (GUI). Implemented entirely
    in the Python programming language, it is compatible with python
    versions 2.6 through 3.2.

    The application scans an input file directory and produces an output
    file that reports, for each source file, the number of lines of code,
    blank/comment lines, word count and character count. The output file
    also reports any files that were skipped because of an unrecognized
    "name.ext".

    The output file also includes a summary of the total, standard
    deviation, average and relative percentage of code and comment lines.
    The summary is also output to the GUI display.

Examples (default case):

    python %prog
    python %prog -i=./ -o=./tsWxLinesOfCodeStatistics.txt
    python %prog -i ./ -o ./tsWxLinesOfCodeStatistics.txt
    ''', version="%prog, v1.0.0")

    #-----------------------------------------------------------------------

    parser.add_option(
        '-i', '--inputDirectoryPath',
        action='store',
        dest='input_Directory_Path',
        default='./',
        type='string',
        help='Directory of source code file(s) [default = ./]')

    #-----------------------------------------------------------------------

    parser.add_option(
        '-o', '--outputFilePath',
            action='store',
            dest='output_File_Path',
            default='./tsWxLinesOfCodeStatistics.txt',
            type='string',
            help='Output file path/name [default = ' + \
            './tsLinesOfCodeStatistics.txt]')

    #-----------------------------------------------------------------------

    parser.add_option(
        '--DebugDetails',
            action='store_true',
            dest='DEBUG',
            default=False,
            help='Log debugging details [default = False]')

    #-----------------------------------------------------------------------

    parser.add_option(
        '--ScanDetails',
            action='store_true',
            dest='SCAN_LOG',
            default=False,
            help='Log line-by-line scan parsing details [default = False]')

    #-----------------------------------------------------------------------

    parser.add_option(
        '--VerboseDetails',
            action='store_true',
            dest='VERBOSE',
            default=False,
            help='Log redirected output details [default = False]')

    # The parser returns a keyword-value pair for each command line
    # option. Each returned keyword is the attribute name specified
    # for the option dest parameter. Each returned attribute value
    # is the parsed commmand line value.
    (args, options) = parser.parse_args()

    DEBUG = options.DEBUG
    SCAN_LOG = options.SCAN_LOG
    VERBOSE = options.VERBOSE

    if DEBUG and VERBOSE:
        print('  getOptParseOptions:\n')
        print('         Args: %s\n' % str(args))
        print('      Options: %s\n' % str(options))
        print('        DEBUG: %s\n' % str(DEBUG))
        print('     SCAN_LOG: %s\n' % str(SCAN_LOG))
        print('      VERBOSE: %s\n' % str(VERBOSE))

    return (args, options)

#--------------------------------------------------------------------------

def getOptions():
    '''
    Parse the command line and return a list of positional arguments
    and a dictionanary of keyword options.

    NOTE: Requirement is an inappropriate, oversimplification.
          Invoking argparse or optparse (deprecated with Python 2.7.0)
          do not produce equivalent output without substantial post
          processing that has not yet been created. This may explain
          inability to migrate use of tsApplication to tsCommandLineEnv
          or to tsWxMultiFrameEnv.
    '''
    if (platformVersion < optParseDeprecated):

        parser = 'getOptParseOptions'

        (args, options) = getOptParseOptions()

    else:

        parser = 'getArgParseOptions'

        (args, options) = getArgParseOptions()

    if DEBUG and VERBOSE:
        print('  getOptions using %s\n' % parser)
        print('      Options: %s\n' % str(options))
        print('         Args: %s\n' % str(args))
        print('        DEBUG: %s\n' % str(DEBUG))
        print('     SCAN_LOG: %s\n' % str(SCAN_LOG))
        print('      VERBOSE: %s\n' % str(VERBOSE))

    return (args, options)

#--------------------------------------------------------------------------

class TsWxLinesOfCode(object):
    '''
    Class to scan a file directory and produce a report of
    the number of source code files, lines of code, blank/comment lines,
    word count and character count.
    '''

    #-----------------------------------------------------------------------

    def __init__(self, myLogger, myPanel, myTextCtrl):
        '''
        Initialize the class and its variables.
        '''
        self.logger = myLogger
        self.panel = myPanel
        self.textCtrl = myTextCtrl

        self.processedFileCount = 0
        self.skippedFiles = []

        # Supported source code file extensions (lower case only)
        # and associated comment syntax method.
        self.syntaxList = {
            '.ada': self.CommentSyntax_Ada_Source,
            '.asm': self.CommentSyntax_Intel_Asm80_Source,
            '.bas': self.CommentSyntax_MS_Basic_Source,
            '.bash': self.CommentSyntax_Bourne_Again_Shell_Script,
            '.bat': self.CommentSyntax_MS_Command_Line_Shell_Script,
            '.c': self.CommentSyntax_C_CPP_H_Source,
            '.c++': self.CommentSyntax_C_CPP_H_Source,
            '.cpp': self.CommentSyntax_C_CPP_H_Source,
            '.csh': self.CommentSyntax_C_Shell_Script,
##            '.dat': self.CommentSyntax_Data_Source,
            '.f': self.CommentSyntax_Fortran_Source,
            '.f77': self.CommentSyntax_Fortran_Source,
            '.f90': self.CommentSyntax_Fortran_Source,
            '.for': self.CommentSyntax_Fortran_Source,
            '.ftn': self.CommentSyntax_Fortran_Source,
            '.g77': self.CommentSyntax_Fortran_Source,
            '.g90': self.CommentSyntax_Fortran_Source,
            '.h': self.CommentSyntax_C_CPP_H_Source,
            '.inc': self.CommentSyntax_Fortran_Source,
            '.ksh': self.CommentSyntax_Korn_Shell_Script,
            '.pas': self.CommentSyntax_Pascal_Source,
            '.plm': self.CommentSyntax_Intel_PLM80_Source,
            '.py': self.CommentSyntax_PSF_Python_Script,
##            '.pyx': self.CommentSyntax_PSF_Python_Extension_Script,
            '.sh': self.CommentSyntax_Bourne_Shell_Script
##            '.src': self.CommentSyntax_Default_Source
            }
##        for theKey in self.syntaxList.keys():
##            self.textCtrl.AppendText('%s\n' % theKey)
##        for i in range(0, 10):
##            self.textCtrl.AppendText('ERROR: %d\n' % i)
##            self.textCtrl.Show()
 

    #-----------------------------------------------------------------------

    def CommentSyntax_Ada_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = strippedLine.find('-- ')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Intel_Asm80_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                comment = strippedLine.find(';')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif comment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Bourne_Again_Shell_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                comment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif comment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_MS_Basic_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = max(strippedLine.find('rem '),
                                   strippedLine.find('REM '))

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_MS_Command_Line_Shell_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = max(strippedLine.find('rem '),
                                   strippedLine.find('REM '))

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_C_CPP_H_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            codeStringActive = False
            docStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                singleLineComment = strippedLine.find('//')
                openingQuote = strippedLine.find('/*')
                if openingQuote != -1:
                    try:
                        closingQuote = strippedLine.find(
                            '*/', openingQuote + 2)

                    except Exception as e:
                        closingQuote = -1
                else:
                    closingQuote = strippedLine.find('*/')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we an singleLine comment
                elif singleLineComment == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote == -1:
                        # Started documatation string block
                        docStringActive = True
                    else:
                        # Ended documatation string block
                        docStringActive = False

                # Have we started or ended a string block?
                elif openingQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote == -1:
                        # Started documatation string block
                        codeStringActive = True
                    else:
                        # Ended documatation string block
                        codeStringActive = False

                # Have we previously started a code string block?
                elif codeStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote != -1:
                        # Ended documatation string block
                        codeStringActive = False

                # Have we previously started a documentation string block?
                elif docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote != -1:
                        # Ended documatation string block
                        docStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_C_Shell_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                comment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif comment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Data_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception as e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        if nextTripleQuote == -1:
                            # Started documatation string block
                            docStringActive = True
                        else:
                            # Ended documatation string block
                            docStringActive = False

                    elif docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          firstTripleQuote,
                                          nextTripleQuote))

                    if nextTripleQuote == -1:
                        # Started code string block
                        codeStringActive = True
                    else:
                        # Started and Ended code string block
                        codeStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Fortran_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                leftJustifiedLine = line.ljust(len(line))
                strippedLine = line.strip()

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif line[0].lower() == 'c' or \
                     line[0] == '*' or \
                     line[0] == '!' or \
                     leftJustifiedLine[0] == '!':

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Korn_Shell_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                comment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif comment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Pascal_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                directive = strippedLine.find('{$')
                openingQuote = strippedLine.find('{ ')
                if openingQuote != -1:
                    try:
                        closingQuote = strippedLine.find(
                            ' }', openingQuote + 2)

                    except Exception as e:
                        closingQuote = -1
                else:
                    closingQuote = strippedLine.find(' }')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a directive line?
                elif directive == 0:

                    # Started a directive line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote == -1:
                        # Started documatation string block
                        docStringActive = True
                    else:
                        # Ended documatation string block
                        docStringActive = False

                # Have we started or ended a string block?
                elif openingQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote == -1:
                        # Started documatation string block
                        docStringActive = True
                    else:
                        # Ended documatation string block
                        docStringActive = False

                # Have we previously started a documentation string block?
                elif docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingQuote,
                                          closingQuote))

                    if closingQuote != -1:
                        # Ended documatation string block
                        docStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Intel_PLM80_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                directive = strippedLine.find('$')
                openingQuote = strippedLine.find('/*')
                closingQuote = strippedLine.find('*/')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a directive line?
                elif directive == 0:

                    # Started a directive line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' %  strippedLine)

                    docStringActive = True

                elif closingQuote == 0:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                    docStringActive = False

                # Have we previously started a documentation string block?
                elif docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_PSF_Python_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception as e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        if nextTripleQuote == -1:
                            # Started documatation string block
                            docStringActive = True
                        else:
                            # Ended documatation string block
                            docStringActive = False

                    elif docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          firstTripleQuote,
                                          nextTripleQuote))

                    if nextTripleQuote == -1:
                        # Started code string block
                        codeStringActive = True
                    else:
                        # Started and Ended code string block
                        codeStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_PSF_Python_Extension_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception as e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        if nextTripleQuote == -1:
                            # Started documatation string block
                            docStringActive = True
                        else:
                            # Ended documatation string block
                            docStringActive = False

                    elif docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          firstTripleQuote,
                                          nextTripleQuote))

                    if nextTripleQuote == -1:
                        # Started code string block
                        codeStringActive = True
                    else:
                        # Started and Ended code string block
                        codeStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Bourne_Shell_Script(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                comment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif comment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def CommentSyntax_Default_Source(self, name):
        '''
        Method to gather software development metrics. It gathers
        lines of code, word and character count statistics for the
        selected file.
        '''

        chars = 0
        codeLines = 0
        commentLines = 0
        lines = 0
        words = 0

        try:
            source = open(name)

            docStringActive = False
            codeStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                firstComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception as e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif firstComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if SCAN_LOG:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if SCAN_LOG:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        if nextTripleQuote == -1:
                            # Started documatation string block
                            docStringActive = True
                        else:
                            # Ended documatation string block
                            docStringActive = False

                    elif docStringActive:

                        commentLines += 1

                        if SCAN_LOG:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          firstTripleQuote,
                                          nextTripleQuote))

                    if nextTripleQuote == -1:
                        # Started code string block
                        codeStringActive = True
                    else:
                        # Started and Ended code string block
                        codeStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if SCAN_LOG:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception as e:
            self.logger.warning('Exception = %s' % e)
            if os.path.islink(name):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(name)
                msg = 'Broken Link Issue with\n    %s->%s\n' % (name, link)
            else:
                # Report Unknown Access Issue to Named File.
                msg = 'Unknown Access Issue with\n    %s\n' % name

            self.logger.warning(msg)
            print('  *** WARNING: %s' % msg)

        if lines != codeLines + commentLines:
            self.logger.error(
                'wc: Lines (%d) != codeLines (%d) + commentLine (%d)' % (
                    lines, codeLines, commentLines))

        return (codeLines, commentLines, lines, words, chars)

    #-----------------------------------------------------------------------

    def getDirectoryData(self, top, fileID):
        '''
        Controls the file selection and display of software devemopment
        metrics.
        '''
        characterCount = 0
        codeLineCount = 0
        commentLineCount = 0
        fileCount = 0
        lineCount = 0
        values = []
        wordCount = 0

        fileID.write('\n')
        fileID.write('%8.8s %8.8s %8.8s %8.8s %8.8s %s\n' % (
            'CODE',
            'CMNTS',
            'LINES',
            'WORDS',
            'CHARS',
            'PATH/FILE'))

        for dirpath, dirnames, filenames in os.walk(top):
            for name in filenames:
                skipped = True
                for sourceCodeExtension in list(self.syntaxList.keys()):
                    wcMethod = self.syntaxList[sourceCodeExtension]
                    theName = os.path.abspath(os.path.join(dirpath, name))
                    if name.lower().endswith(sourceCodeExtension.lower()):
                        skipped = False
                        self.processedFileCount += 1
                        if SCAN_LOG:
                            self.logger.debug(
                                '\n\n\twcMethod: <%s>\n' % theName)
                        elif DEBUG:
                            self.logger.debug('wcMethod: <%s>' % theName)

                        (codeLines,
                         commentLines,
                         lines,
                         words,
                         chars) = wcMethod(theName)

                        fileID.write('%8d %8d %8d %8d %8d %s\n' % (
                            codeLines,
                            commentLines,
                            lines,
                            words,
                            chars,
                            theName))

                        codeLineCount += codeLines
                        commentLineCount += commentLines
                        lineCount += lines
                        wordCount += words
                        characterCount += chars
                        values += [(
                            codeLines, commentLines, lines, words, chars)]
                        fileCount += 1

                if skipped:
                    self.skippedFiles.append(theName)
                    self.logger.warning('Skipped: <%s>' % theName)

        if lineCount != codeLineCount + commentLineCount:
            fmt1 = 'getDirectoryData: LineCount (%d) != ' % lineCount
            fmt2 = 'codeLineCount (%d) + commentLineCount (%d)' % (
                    codeLineCount, commentLineCount)
            self.logger.error(fmt1 + fmt2)

        return (fileCount,
                codeLineCount,
                commentLineCount,
                lineCount,
                wordCount,
                characterCount,
                values)

    #-----------------------------------------------------------------------

    def MainLoop(self):
        '''
        Display program name, version and date. Receive and validate
        command line options and arguments. Display help, error and status
        information. Initiate the file directory copy.
        '''
        #########################################################
        # Begin declarations required to convert global constants
        # into command line option variables.
        global DEBUG
        global SCAN_LOG
        global VERBOSE
        # End declarations required to convert global constants
        #########################################################

        print(__header__)

        # Must get command line positional and keyword arguments
        # before redirection of stdout and stderr to GUI display.
        (myOptions, myArgs) = getOptions()

        try:

            DEBUG    = myOptions.DEBUG
            SCAN_LOG = myOptions.SCAN_LOG
            VERBOSE  = myOptions.VERBOSE

        except Exception as errorCode:

            print('getOptions myOptions = %s' % str(myOptions))
            print('getOptions    myArgs = %s' % str(myArgs))
            print('Skipped (myOptions, myArgs) = %s' % str(errorCode))

        if False:
            self.myInputPath = myOptions.input_Directory_Path
            self.myOutputPath = myOptions.output_File_Path
        else:
            try:
                self.myInputPath = myArgs[0]
            except:
                self.myInputPath = myOptions.input_Directory_Path

            try:
                self.myOutputPath = myArgs[1]
            except:
                self.myOutputPath = myOptions.output_File_Path

        if self.myInputPath is None:
            print('  No Input Path:  <%s>.' % self.myInputPath)
            exit(1)
        else:
            print('  Input Path:     <%s>.' % self.myInputPath)

        if self.myOutputPath is None:
            print('  No Output File: <%s>.' % self.myOutputPath)
            myFileID = sys.stdout
        else:
            print('  Output File:    <%s>.' % self.myOutputPath)
            myFileID = open(self.myOutputPath, 'w')
            hline = '-' * 78
            myFileID.write('\n%s' % hline)
            myFileID.write(__header__)
            myFileID.write('\n%s\n' % hline)

        print('\n')

        (myFileCount,
         myCodeLineCount,
         myCommentLineCount,
         myLineCount,
         myWordCount,
         myCharacterCount,
         myValues) = self.getDirectoryData(self.myInputPath, myFileID)

        self.reportResults(myFileID,
                           myFileCount,
                           myCodeLineCount,
                           myCommentLineCount,
                           myLineCount,
                           myWordCount,
                           myCharacterCount,
                           myValues)

        myFileID.close()

        if self.myOutputPath is not None:
            print('  Results are available in "%s".\n' % \
                  os.path.abspath(self.myOutputPath))
 
    #-----------------------------------------------------------------------

    def reportResults(self,
                      fileID,
                      fileCount,
                      codeLineCount,
                      commentLineCount,
                      lineCount,
                      wordCount,
                      characterCount,
                      values):
        '''
        Analyze and display software development metrics.
        '''
        self.fileCtrl = fileID
        hline = '-' * 78

        self.textCtrl.AppendText('%s\n' % __header__,
                                 markup={'Attributes': [wx.DISPLAY_BOLD],
                                         'Foreground': 'cyan'})

        self.writeResults('%s' % hline)

        self.writeResults('\n  Input Path:     <%s>.' % self.myInputPath)
        self.writeResults('  Results are available in "%s".' % \
                          os.path.abspath(self.myOutputPath))

        self.writeResults('\n%s\n' % hline)

        indentText = ' ' * 7
        self.writeResults(
            '%s %8.8s %8.8s %8.8s %8.8s %8.8s %10.10s' % (
            indentText,
            'FILES',
            'CODE',
            'CMNTS',
            'LINES',
            'WORDS',
            'CHARS'))

##        hline = '-' * 78
##        self.writeResults('%s' % hline)

        if lineCount != codeLineCount + commentLineCount:
            fmt1 = 'reportResults: LineCount (%d) != ' % lineCount
            fmt2 = 'codeLineCount (%d) + commentLineCount (%d)' % (
                    codeLineCount, commentLineCount)
            self.logger.error(fmt1 + fmt2)

        # self.writeResults('\n')

        if lineCount > 0:
            self.writeResults(
                '   Pct:            %6.2f%s  %6.2f%s  %6.2f%s' % (
                    (100.0 * (
                        float(codeLineCount) /  float(lineCount))), '%',
                    (100.0 * (
                        float(commentLineCount) /  float(lineCount))), '%',
                    (100.0 * (
                        float(lineCount) / float(lineCount))), '%'))

        self.writeResults('Totals: %8d %8d %8d %8d %8d %10d' % (
            fileCount,
            codeLineCount,
            commentLineCount,
            lineCount,
            wordCount,
            characterCount))

        if fileCount == 0:
            avgFileCount = fileCount
            avgCodeCount = codeLineCount
            avgCmntCount = commentLineCount
            avgLineCount = lineCount
            avgWordCount = wordCount
            avgCharacterCount = characterCount
        else:
            avgFileCount = 1
            avgCodeCount = int(round(float(codeLineCount) / float(fileCount)))
            avgCmntCount = int(round(float(commentLineCount) / \
                                     float(fileCount)))
            avgLineCount = max(avgCodeCount + avgCmntCount,
                               int(round(float(lineCount) / float(fileCount))))
            avgWordCount = int(round(float(wordCount) / float(fileCount)))
            avgCharacterCount = int(round(float(characterCount) / \
                                          float(fileCount)))

        sumOfCodeDeviationsSquared = 0
        sumOfCmntDeviationsSquared = 0
        sumOfLineDeviationsSquared = 0
        sumOfWordDeviationsSquared = 0
        sumOfCharDeviationsSquared = 0

        for i in range(fileCount):
            (codeLines, commentLines, lines, words, chars) = values[i]
            codeDeviation = codeLines - avgCodeCount
            cmntDeviation = commentLines - avgCmntCount
            lineDeviation = lines - avgLineCount
            wordDeviation = words - avgWordCount
            charDeviation = chars - avgCharacterCount
            sumOfCodeDeviationsSquared += codeDeviation**2
            sumOfCmntDeviationsSquared += cmntDeviation**2
            sumOfLineDeviationsSquared += lineDeviation**2
            sumOfWordDeviationsSquared += wordDeviation**2
            sumOfCharDeviationsSquared += charDeviation**2

        if fileCount <= 1:
            avgOfCodeDeviationsSquared = sumOfCodeDeviationsSquared
            avgOfCmntDeviationsSquared = sumOfCmntDeviationsSquared
            avgOfLineDeviationsSquared = sumOfLineDeviationsSquared
            avgOfWordDeviationsSquared = sumOfWordDeviationsSquared
            avgOfCharDeviationsSquared = sumOfCharDeviationsSquared
        else:
            avgOfCodeDeviationsSquared = sumOfCodeDeviationsSquared / \
                                         float(fileCount - 1)

            avgOfCmntDeviationsSquared = sumOfCmntDeviationsSquared / \
                                         float(fileCount - 1)

            avgOfLineDeviationsSquared = sumOfLineDeviationsSquared / \
                                         float(fileCount - 1)

            avgOfWordDeviationsSquared = sumOfWordDeviationsSquared / \
                                         float(fileCount - 1)

            avgOfCharDeviationsSquared = sumOfCharDeviationsSquared / \
                                         float(fileCount - 1)

        stdCodeCount = 0
        stdCmntCount = 0
        stdLineCount = 0
        stdWordCount = 0
        stdCharCount = 0
        for i in range(fileCount):
            (codeLines, commentLines, lines, words, chars) = values[i]
            codeAbsDelta = abs(codeLines - avgCodeCount)
            cmntAbsDelta = abs(commentLines - avgCmntCount)
            lineAbsDelta = abs(lines - avgLineCount)
            wordAbsDelta = abs(words - avgWordCount)
            charAbsDelta = abs(chars - avgCharacterCount)
            if codeAbsDelta <= math.sqrt(avgOfCodeDeviationsSquared):
                stdCodeCount += 1
            if cmntAbsDelta <= math.sqrt(avgOfCmntDeviationsSquared):
                stdCmntCount += 1
            if lineAbsDelta <= math.sqrt(avgOfLineDeviationsSquared):
                stdLineCount += 1
            if wordAbsDelta <= math.sqrt(avgOfWordDeviationsSquared):
                stdWordCount += 1
            if charAbsDelta <= math.sqrt(avgOfCharDeviationsSquared):
                stdCharCount += 1

        self.writeResults('   Std: %8d %8d %8d %8d %8d %10d' % (
            stdLineCount,
            math.sqrt(avgOfCodeDeviationsSquared),
            math.sqrt(avgOfCmntDeviationsSquared),
            math.sqrt(avgOfLineDeviationsSquared),
            math.sqrt(avgOfWordDeviationsSquared),
            math.sqrt(avgOfCharDeviationsSquared)))

        self.writeResults('   Avg: %8d %8d %8d %8d %8d %10d' % (
            avgFileCount,
            avgCodeCount,
            avgCmntCount,
            avgLineCount,
            avgWordCount,
            avgCharacterCount))

        skippedFileCount = len(self.skippedFiles)
        if skippedFileCount > 0:
            hline = '-' * 78
            self.writeResults('\n%s' % hline)
            fmt = 'Skipped %d of %d file(s) for having invalid "name.ext"' % \
                  (skippedFileCount,
                   skippedFileCount + self.processedFileCount)

            print('  %s.\n' % fmt)
            self.writeResults('\n%s:' % fmt)

            recognizedKeys = ''
            i = -1
            for key in sorted(self.syntaxList.keys()):
                i += 1
                if recognizedKeys == '':
                    recognizedKeys += 'Valid file "name.ext" ' + \
                                      '(Upper or Lower case):' + \
                                      '\n\n    %5s' % key
                elif i < 8:
                    recognizedKeys += ', %5s' % key
                else:
                    i = 0
                    recognizedKeys += ',\n    %5s' % key
 
            self.writeResults('\n   %s' % recognizedKeys)

            i = -1
            for item in self.skippedFiles:
##                self.writeResults('   %s\n' % item)
                i += 1
                if (i == 0):
                    fileID.write('\n   %s\n' % item)
                else:
                    fileID.write('   %s\n' % item)

        self.writeResults('\n%s\n' % hline)

    #-----------------------------------------------------------------------

    def writeResults(self, buffer):
        '''
        '''
        self.fileCtrl.write('%s\n' % buffer)
        self.textCtrl.AppendText(buffer)

#--------------------------------------------------------------------------

class _Prototype(wx.Frame):
    '''
    Class to establish the frame that contains the application specific
    graphical components.
    '''
    def tsGetTheId(self):
        '''
        Return the ID associated with this class instance.
        '''
        return id(self)

    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id=nextWindowId(),
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.FrameNameStr):
        '''
        Init the Frame
        Show the Frame
        '''

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=((280 * 3) / 2, (200 * 3) / 2),
                              style=style,
                              name=name)

            # TBD - This should NOT change Frame color.
            # It should only change Panel color.
##            self.ForegroundColour = wx.COLOR_YELLOW
##            self.BackgroundColour = wx.COLOR_MAGENTA

        else:

            # Establish character and pixel position of this canvas
            # Set at top left row and column of area to be centered, by
            # default, in the user terminal screen.
            begin_y = -1
            begin_x = -1
            thePos = wx.tsGetPixelValues(begin_x, begin_y)

            # Establish character and pixel size of this canvas
            # for the wxPython application "tsWxGUI_test1.py".
            #
            # VGA Display (640 x 480 pixels) with Courier (8 x 12 pixels)
            # monospaced font characters contains (80 Cols x 40 Rows).

            # Set typical console area
            max_x = -1 # 80
            max_y = -1 # 30
            theSize = wx.tsGetPixelValues(max_x, max_y)

            wx.Frame.__init__(
                self,
                parent,
                id,
                name='Frame',
                title=title,
                pos=thePos,
                size=theSize,
                style=wx.DEFAULT_FRAME_STYLE)

        # Cannot log before GUI started via Frame.
        self.logger.debug(
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        # The following tests depend on Showing final Frame position.
##        if splashScreenEnabled:
##            self.theSplashScreen.tsShow()
##            time.sleep(splashScreenSeconds)

##        self.myframe = wx.Frame(None, title='BoxSizer')

        #-------------------------------------------------------------------
        # Begin Prototype
        #-------------------------------------------------------------------

        # TBD - Menu Bar Client Area Change in Frame did not
        # reduce height of panel.
        theFrame = self
        menubar = wx.MenuBar(theFrame)
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Centre()
        self.Show()

        theRect = theFrame.Rect
        theClientArea = theFrame.ClientArea
        print('Frame: Rect=%s; ClientArea=%s' % (str(theRect),
                                                 str(theClientArea)))

        tcPosition = (theFrame.ClientArea.x, theFrame.ClientArea.y)
        tcSize = (theFrame.ClientArea.width, theFrame.ClientArea.height)
        theTextCtrl = wx.TextCtrl(
            theFrame,
            id=wx.ID_ANY,
            value=wx.EmptyString,
            pos=tcPosition,
            size=tcSize,
            style=0,
            validator=wx.DefaultValidator,
            name=wx.TextCtrlNameStr)

##        for i in range(0, 10):
##            msg = 'ERROR: %d\n' % i
##            print(msg)
##            theTextCtrl.AppendText(msg)

        theFrame.Show()
        thePanel = None
        if SCAN_LOG:
            theLogger = Logger.TsLogger(name='ScanDetails.log',
                                        threshold=Logger.DEBUG)
        else:
            theLogger = Logger.TsLogger(name='',
                                        threshold=Logger.DEBUG)
        LinesOfCode = TsWxLinesOfCode(theLogger, thePanel, theTextCtrl)
        if threadingEnabled:
            # thread.start_new_thread ( thread, ( 'Argument' ) )
            _thread.start_new_thread(LinesOfCode.MainLoop, ())
        else:
            LinesOfCode.MainLoop()

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

        # TBD - This should NOT change Frame color.
        # It should only change Panel color.
##        self.ForegroundColour = wx.COLOR_YELLOW
##        self.BackgroundColour = wx.COLOR_MAGENTA

        self.logger.debug(
            'End %s (0x%X).' % ('Prototype', self.tsGetTheId()))

    #-----------------------------------------------------------------------

##    def OnMove(self, event):
##        pos = event.GetPosition()
##        self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))
##        print('Prototype OnMove: value=%s' % str(pos))

    #-----------------------------------------------------------------------

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        print('Prototype OnQuit: value=%d' % -1)
        self.Close()

    #-----------------------------------------------------------------------
 
##    def OnHelp(self, event):
##        '''
##        Show the help dialog.
##        '''
##        dlg = wx.MessageDialog(
##            self,
##            __help__,
##            "%s Help" % __title__,
##            wx.OK | wx.ICON_INFORMATION)

##        dlg.ShowModal()
##        dlg.Destroy()
##        print('Prototype OnHelp: value=%d' % -1)

    #-----------------------------------------------------------------------

##    def OnAbout(self, event):
##        '''
##        Show the about dialog.
##        '''
##        dlg = wx.MessageDialog(
##            self,
##            __header__,
##            'About %s' % __title__,
##            wx.OK | wx.ICON_INFORMATION)

##        dlg.ShowModal()
##        dlg.Destroy()
##        print('Prototype OnAbout: value=%d' % -1)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    # Build Information (Top Level Executable Module)
    buildTitle     = __title__
    buildVersion   = __version__
    buildDate      = __date__
    buildAuthors   = __authors__
    buildCopyright = __copyright__

    # User Information (Command Line Interface)
    # TBD - May need to derive class from tsWxMultiFrameEnv
    # inorder to override cliAPP.getOptions.
    cliOptions = getOptions()

    # Application Program Information (Graphical User Interface)
    guiTopLevelObjectId = wx.ID_ANY
    guiMessageRedirect = True
    guiMessageFilename = None
    guiTopLevelObject = _Prototype
    guiTopLevelObjectName = 'Prototype'
    guiTopLevelObjectTitle = 'Prototype_Feature'
 
    Instance =  wx.MultiFrameEnv(
        cliOptions=cliOptions,
        sourceTitle=buildTitle,
        sourceVersion=buildVersion,
        sourceDate=buildDate,
        sourceAuthors=buildAuthors,
        sourceCopyright=buildCopyright,
        # wrapperHeader=__header__,
        wrapperRedirect=guiMessageRedirect,
        wrapperFilename=guiMessageFilename,
        wrapperTopLevelObject=guiTopLevelObject,
        wrapperId=guiTopLevelObjectId,
        # wrapperMainTitleVersionDate=mainTitleVersionDate,
        wrapperName=guiTopLevelObjectName,
        wrapperTitle=guiTopLevelObjectTitle
        )
    Instance.Wrapper()
