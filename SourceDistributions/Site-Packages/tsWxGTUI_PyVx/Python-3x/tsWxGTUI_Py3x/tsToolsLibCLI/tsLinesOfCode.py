#! /usr/bin/env python
#"Time-stamp: <04/22/2015  7:27:34 AM rsg>"
'''
tsLinesOfCode.py - Class of utility functions, used by the
tsLinesOfCodeProjectMetrics.py tool, to coordinate the
processes of gathering software lines of code metrics and
deriving, analyzing, estimating and reporting software
development project labor, cost, schedule and productivity
metrics.
'''
#################################################################
#
# File: tsLinesOfCode.py
#
# Purpose:
#
#    Class of utility functions to coordinate the processes
#    of gathering software lines of code metrics and deriving,
#    analyzing, estimating and reporting software development
#    project labor, cost, schedule and productivity metrics.
#
# Limitations:
#
#    1. No industry standard file naming convention. Each lines-of-code
#       analysis tool presumes that file name extensions unambiguously
#       distinguish one programming language format from another.
#       Comparing the sample files provided by the "tsLinesOfCode"
#       tool with two other tools reveals that some extensions may be
#       associated with different programming languages. For example:
#
#       a. "tsLinesOfCode-2.0.0" by Richard S. Gordon (rigordo@comcast.net
#          The supplied samples have Fortran include files with the
#         ".inc" extension.
#
#       b. "sloccount-2.26" by David A. Wheller (dwheeler@dwheeler.com)
#          The supplied samples have one PHP file with the ".inc"
#          extension.
#
#       c. "Understand-3.1.646" by Scientific Toolworks (www.scitools.com)
#          The supplied samples have one ZLIB file with the ".inc" extension.
#
#    2. There are advantages and disadvantages associated with each tool.
#
#       a. "tsLinesOfCode-2.0.0" by Richard S. Gordon (rigordo@comcast.net
#          Implementation is in the Python programming language. The
#          optional Pyrex programming language may be used to interface
#          with components implemented in compiled languages such as
#          C/C++. This makes it easier for users to extend and maintain
#          the open source tool.
#
#       b. "sloccount-2.26" by David A. Wheller (dwheeler@dwheeler.com)
#          Implementation is in multiple compiled and scripting languages.
#          This makes it somewhat easier for users to extend and maintain
#          the open source tool.
#
#       c. "Understand-3.1.646" by Scientific Toolworks (www.scitools.com)
#          This is a mult-function, commercial product. Its implementation
#          is proprietary. Users cannot extend and maintain this tool.
#
#          Its manufacturer claims that its metrics can be categorized in
#          the following groups:
#
#              Complexity Metrics (e.g. McCabe Cyclomatic)
#              Volume Metrics (e.g Lines of Code)
#              Object Oriented (e.g. Coupling Between Object Classes)
#
#          Its manufacturer claims that it is very efficient at collect-
#          ing metrics about the code that it analyzes. These metrics
#          can be extracted automatically via command line calls,
#          exported to spreadsheets, viewed graphically, dynamically
#          explored in the GUI, or customized via the Understand Perl
#          API. They can also be reported at the project level, for
#          files, classes, functions or user defined architectures.
#
#    3. "tsLinesOfCode-2.0.0" Analysis Methods.
#
#          Mature
#          (candidates for introduction of new file name extensions)
#          -------------------------------------------------------
#          TsLinesOfCode.CommentSyntax_Ada_Source
#          TsLinesOfCode.CommentSyntax_Bourne_Again_Shell_Script
#          TsLinesOfCode.CommentSyntax_Bourne_Shell_Script
#          TsLinesOfCode.CommentSyntax_C_CPP_H_Source
#          TsLinesOfCode.CommentSyntax_C_Shell_Script
#          TsLinesOfCode.CommentSyntax_Cobol_Source
#          TsLinesOfCode.CommentSyntax_Fortran_Source
#          TsLinesOfCode.CommentSyntax_Intel_Asm80_Source
#          TsLinesOfCode.CommentSyntax_Intel_PLM80_Source
#          TsLinesOfCode.CommentSyntax_Korn_Shell_Script
#          TsLinesOfCode.CommentSyntax_MS_Basic_Source
#          TsLinesOfCode.CommentSyntax_MS_Command_Line_Shell_Script
#          TsLinesOfCode.CommentSyntax_PSF_Python_Extension_Script
#          TsLinesOfCode.CommentSyntax_PSF_Python_Script
#          TsLinesOfCode.CommentSyntax_Pascal_Source
#          TsLinesOfCode.MainLoop
#          TsLinesOfCode.Plain_Text_Document
#
#          Under Construction
#          (candidates for Pyrex interface to sloccount components)
#          -------------------------------------------------------
#          TsLinesOfCode.CommentSyntax_Data_Source
#          TsLinesOfCode.CommentSyntax_Default_Source
#          TsLinesOfCode.CommentSyntax_Haskel_Source
#          TsLinesOfCode.CommentSyntax_Literal_Haskel_Source
#          TsLinesOfCode.CommentSyntax_PHP_Source
#          TsLinesOfCode.CommentSyntax_Ruby_Source
#
# Notes:
#
#    See http://en.wikipedia.org/wiki/Source_lines_of_code.
#    It provides an introduction to software metrics: its foundation,
#    applications, capabilities, limitations and evolution.
#
#    The blank/comment lines represent a line that contains no
#    executable code. A blank line in one that contains no
#    alpha-numeric characters and is terminated by a new line
#    character(\n).
#
#    A single line comment is one that begins with a programming
#    language specific comment identifier (upper or lower case):
#
#        .ada          "--"
#        .adb          "--"
#        .ads          "--"
#        .asm          ";"
#        .asm80        ";"
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
#        .f95          "c"   "*"   "!"
#        .for          "c"   "*"   "!"
#        .ftn          "c"   "*"   "!"
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
#        .plm80        ("/*",   "*/")
#        .plm96        ("/*",   "*/")
#        .py           ("'''", "'''") ('"""', '"""')
#
#    File Extension requirements (for additional source code) inspired by
#    SLOCCount 2.26 utility by David Wheeler (for details see
#    http://www.dwheeler.com/sloccount/).
#
#    Algorithm requirements (for estimating software project development
#    effort, staffing and scheduling) is based on COCOMO(R) 81 publication
#    by Dr, Barry Boehm.
#
# Usage (examples):
#
#   Interpreter   program app.      operator settings
#   -----------   ----------------  -----------------------------
#   python        tsLinesOfCode.py
#
#   python2.7     tsLinesOfCode.py  [-i INPUTDIR] [-o OUTPUTFILE]
#
#   python3.3     tsLinesOfCode.py  [-h] [-v] [-a]
#                                   [-d] [-s] [-V]
#                                   [-p {0,1,2}]
#                                   [-i INPUTDIR] [-o OUTPUTFILE]
#                                   {argparse, optparse, getopt}
#
#       ---------------------------------------------------------
#       Key:
#
#           "python"    - Default interpreter for platform
#
#           "python2.7" - First alternate interpreter for platform
#
#           "python3.3" - Second alternate interpreter for platform
#
#           "[]" - Brackets enclose option keywords and values
#
#           "{}" - Braces enclose option value choices and
#                  positional arguments
#
# Methods:
#
#    TsLinesOfCode - Class to coordinate the processes of
#           gathering software lines of code metrics and
#           deriving, analyzing, estimating and reporting
#           software development project labor, cost,
#           schedule and productivity metrics.
#
#    TsLinesOfCode.__init - Method to initializes the inherited
#           base class.
#
#    TsLinesOfCode.MainLinesOfCodeLoop - Method to sequence through
#           the following processes:
#
#           a) tsOperatorSettings - gather key-word value
#                  pair options and positional arguments
#                  command line used by operator to launch
#                  program
#
#           b) tsSoftwareMetrics - invokes and controls
#                  the tsSoftwareParser class to scan
#                  files in the operator designated directory
#                  and extract the number of lines of code
#                  from the number of comment/blank lines.
#
#           d) tsProject Metrics - derives, from the lines
#                  of code metrics, the software development
#                  project labor, cost, schedule and produc-
#                  tivity metrics using the COCOMO 1981
#                  algorithm
#
# Modifications:
#
#   2011/12/12 rsg Added threading capability so that CLI will
#                  update while non-time critical director scan
#                  runs in background.
#
#   2011/12/15 rsg Added platform-dependent support for argparse
#                  and optparse based on Python version. The
#                  selection criteria is that optparse became
#                  deprecated with Python 2.7.0 or later.
#
#   2013/01/17 rsg Created the syntaxFeatures tabulation to
#                  facilitate standardization of nominclature.
#                  Substituted 'SingleLineComment' for references
#                  to 'Comment' or 'FirstComment'.
#
#   2011/12/19 rsg Added support for Plain_Text_Document (*.txt)
#
#   2013/02/10 rsg Added writeEstimatedDevelopmentEffort method.
#
#   2013/02/14 rsg Modified the design to substitute CLI for GUI
#                  (Graphical User Interface) and substitute
#                  EventLoggingWrapper for _Prototype. The goal
#                  is to use names that were more appropriate.
#
#   2013/05/22 rsg Converted the original monolithic application
#                  design to a multi-class one with enhanced
#                  command line option parsing (descriptive,
#                  built-in help and support for argparse,
#                  optparse and getopt Python library modules).
#                  The design can now apply the debug, scan and
#                  verbose options directly raher than attempt-
#                  ing to clumsily modify global "constants"
#                  DEBUG, SCAN_LOG and VERBOSE.
#
#   2013/07/31 rsg Update the application launch design in the manner of
#                  tsStripMomments (for Command Line Interface mode) and
#                  "TBD" (for Graphical User Interface mode):
#
#                  * Adopt myParser and getSettings as interface to
#                    default and application-specific command line
#                    parsing capabilities. Objective is to apply
#                    consistant operator settings acquisition.
#
#                  * Adopt EntryPoint as interface to default and
#                    application-specific command line user interface
#                    mode launch capabilities. Objective is to apply
#                    consistant user interface launch without
#                    references to various names such as Prototype.
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
#   2013/01/17 rsg Apply syntaxFeatures tabulation in a generic
#                  analyzer method to replace file type specific
#                  methods. Algorithm differences might make
#                  this impractical
#
#   2013/05/22 rsg Eliminate the required positional argument
#                  by which the operator specifies the parser.
#                  Use of keyword option, with default to None
#                  would be more user friendly.
#
#   2013/07/31 rsg Correct report header by replacing reference to
#                  __header__ by self.GetRunTimeHeader().
#
#################################################################

__title__     = 'tsLinesOfCode'
__version__   = '2.4.0'
__date__      = '07/31/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  File Extension Features of SLOCCount 2.26: ' + \
                '\n\t  Copyright (c) 2001-2004 David A. Wheeler. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Algorithm Features of COCOMO(R) 81: ' + \
                '\n\t  Copyright (c) 1981 Dr. Barry W. Boehm. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Logging Module API Features: ' + \
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

import os.path
import sys

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsLogger as Logger

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsToolsLibCLI import tsLOCPMOperatorSettingsParser
from tsWxGTUI_Py3x.tsToolsLibCLI import tsProjectMetrics
from tsWxGTUI_Py3x.tsToolsLibCLI import tsSoftwareMetrics

from tsLOCPMOperatorSettingsParser import TsLOCPMOperatorSettingsParser
from tsProjectMetrics import TsProjectMetrics
from tsSoftwareMetrics import TsSoftwareMetrics

#--------------------------------------------------------------------------

# Enables startup message when both True
DEBUG = False
VERBOSE = False

#--------------------------------------------------------------------------

class TsLinesOfCode(TsLOCPMOperatorSettingsParser):
    '''
    Class to coordinate the processes of gathering software lines of
    code metrics and deriving, analyzing, estimating and reporting
    software development project labor, cost, schedule and productivity
    metrics.
    '''
    def __init(self, applicationSettings=None):
        '''
        Class constructor. Initializes the inherited base class.
        '''

        if True or DEBUG:
            print('\n\ntsLinesOfCode\n')
            print('applicationSettings=\n\t%s\n' % str(applicationSettings))
##          print('buildTitle=\n\t%s\n' % kw['buildTitle'])
##          print('buildVersion=\n\t%s\n' % kw['buildVersion'])
##          print('buildDate=\n\t%s\n' % kw['buildDate'])
##          print('buildAuthors=\n\t%s\n' % kw['buildAuthors'])
##          print('buildCopyright=\n\t%s\n' % kw['buildCopyright'])
##          print('buildLicense=\n\t%s\n' % kw['buildLicense'])
##          print('buildCredits=\n\t%s\n' % kw['buildCredits'])
##          print('buildTitleVersionDate=\n\t%s\n' % \
##                kw['buildTitleVersionDate'])
##          print('buildHeader=\n\t%s\n' % kw['buildHeader'])
##          print('buildPurpose=\n\t%s\n' % kw['buildPurpose'])
        TsLOCPMOperatorSettingsParser.__init__(
            self,
            applicationSettings=applicationSettings)

        self.projectMetrics = None

        self.softwareMetrics = None

    #-----------------------------------------------------------------------

    def MainLinesOfCodeLoop(self):
        '''
        Method to sequence through the following processes:

        a) tsOperatorSettings - gather key-word value pair options and
           positional arguments command line used by operator to launch
           program

        b) tsSoftwareMetrics - invokes and controls the tsSoftwareParser
           class to scan files in the operator designated directory and
           extract the number of lines of code from the number of comment/
           blank lines.

        d) tsProject Metrics - derives, from the lines of code metrics,
           the software development project labor, cost, schedule and
           productivity metrics using the COCOMO 1981 algorithm
        '''
        if DEBUG and VERBOSE:
            print('\n\n\tTsLinesOfCode.MainLinesOfCodeLoop Startup:')

        (args, options) = self.parseCommandLineDispatch()

        if DEBUG and VERBOSE:
            state = dir(self)
            for item in state:
                if item == 'options':
                    print('\t\t%s=%s' % (item, str(self.options)))
                elif item == 'args':
                    print('\t\t%s=%s' % (item, str(self.args)))
                else:
                    print('\t\t%s' % item)

        try:

            debug_log    = options['debug']
            input = options['input']
            output = options['output']
            scan_log = options['scan']
            verbose_log  = options['Verbose']

            if DEBUG and VERBOSE:
                print('\tdebug_log = "%s"' % str(debug_log))
                print('\tinput = "%s"' % str(input))
                print('\toutput = "%s"' % str(output))
                print('\tscan_log = "%s"' % str(scan_log))
                print('\tverbose_log = "%s"' % str(verbose_log))

        except Exception as errorCode:

            print('\tErrorCode (args, options) = "%s"' % str(errorCode))
            print('\t\targs = "%s"' % str(args))
            print('\t\toptions = "%s"' % str(options))
            sys.exit(2)

        if output is None:
            print('  No Output File: <%s>.' % output)
            fileID = sys.stdout
        else:
            if DEBUG and VERBOSE:
                print('  Output File:    <%s>.' % output)
            mode = 'w'
            fileID = open(output, mode)
            hline = '-' * 78
            fileID.write('\n%s' % hline)
            fileID.write('%s' % __header__)
            fileID.write('\n%s\n' % hline)

        print('\n')

        self.softwareMetrics = TsSoftwareMetrics(
            self.logger,
            debug_log,
            input,
            output,
            scan_log,
            verbose_log,
            fileID)

        (myFileCount,
         myCodeLineCount,
         myCommentLineCount,
         myLineCount,
         myWordCount,
         myCharacterCount,
         myValues) = self.softwareMetrics.tsLocSMGetDirectoryData()

        self.softwareMetrics.tsLocSMReportResults(
            myFileCount,
            myCodeLineCount,
            myCommentLineCount,
            myLineCount,
            myWordCount,
            myCharacterCount,
            myValues)

        self.projectMetrics = TsProjectMetrics(
            self.logger,
            debug_log,
            input,
            output,
            scan_log,
            verbose_log,
            fileID)

        self.projectMetrics.tsLocPMReportResults(myCodeLineCount)

##      print('Breakpoint exit.')
##      exit(0)

        fileID.close()

        if output is not None:
            print('\n  Results are available in "%s".\n' % \
                  os.path.abspath(output))

#--------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
