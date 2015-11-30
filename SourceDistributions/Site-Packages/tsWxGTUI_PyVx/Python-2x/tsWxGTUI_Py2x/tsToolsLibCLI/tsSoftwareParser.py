#! /usr/bin/env python
#"Time-stamp: <04/22/2015  7:29:57 AM rsg>"
'''
tsSoftwareParser.py - Class of utiltity functions, used by the
tsLinesOfCodeProjectMetrics.py tool, to parse
source code and accumulate the number of source lines of code,
blank/comment lines, word count and character count.
'''
#################################################################
#
# File: tsSoftwareParser.py
#
# Purpose:
#
#     Class of utiltity functions to parse source code and
#     accumulate the number of source lines of code,
#     blank/comment lines, word count and character count.
#
# Limitations:
#
#    1. No industry standard file naming convention. Each lines-of-code
#       analysis tool presumes that file name extensions unambiguously
#       distinguish one programming language format from another.
#       Comparing the sample files provided by the "tsSoftwareParser"
#       tool with two other tools reveals that some extensions may be
#       associated with different programming languages. For example:
#
#       a. "tsSoftwareParser-2.0.0" by Richard S. Gordon (rigordo@comcast.net
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
#       a. "tsSoftwareParser-2.0.0" by Richard S. Gordon (rigordo@comcast.net
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
#    3. "tsSoftwareParser-2.0.0" Analysis Methods.
#
#          Mature
#          (candidates for introduction of new file name extensions)
#          -------------------------------------------------------
#          SoftwareParser.CommentSyntax_Ada_Source
#          SoftwareParser.CommentSyntax_Bourne_Again_Shell_Script
#          SoftwareParser.CommentSyntax_Bourne_Shell_Script
#          SoftwareParser.CommentSyntax_C_CPP_H_Source
#          SoftwareParser.CommentSyntax_C_Shell_Script
#          SoftwareParser.CommentSyntax_Cobol_Source
#          SoftwareParser.CommentSyntax_Fortran_Source
#          SoftwareParser.CommentSyntax_Intel_Asm80_Source
#          SoftwareParser.CommentSyntax_Intel_PLM80_Source
#          SoftwareParser.CommentSyntax_Korn_Shell_Script
#          SoftwareParser.CommentSyntax_MS_Basic_Source
#          SoftwareParser.CommentSyntax_MS_Command_Line_Shell_Script
#          SoftwareParser.CommentSyntax_PSF_Python_Extension_Script
#          SoftwareParser.CommentSyntax_PSF_Python_Script
#          SoftwareParser.CommentSyntax_Pascal_Source
#          SoftwareParser.MainLoop
#          SoftwareParser.Plain_Text_Document
#
#          Under Construction
#          (candidates for Pyrex interface to sloccount components)
#          -------------------------------------------------------
#          SoftwareParser.CommentSyntax_Data_Source
#          SoftwareParser.CommentSyntax_Default_Source
#          SoftwareParser.CommentSyntax_Haskel_Source
#          SoftwareParser.CommentSyntax_Literal_Haskel_Source
#          SoftwareParser.CommentSyntax_PHP_Source
#          SoftwareParser.CommentSyntax_Ruby_Source
#
#    4. Threading overhead is noticable. TaskBar Clock normally
#       updates, without threading every 1-3 seconds. With threading,
#       clock frequently does NOT update for minutes at a time.
#
#       Scans of extensive collection of files may take many minutes
#       depending on the platform.
#
#          Mac OS X scanned files 18977 of 83569 in  4 minutes.
#          Cygwin-X scanned files 15558 of 74819 in 22 minutes.
#                   (Note: Non-xterm Cygwin aborted at GUI startup.)
#
# Notes:
#
#    See http://www.lehigh.edu/~inimr/computer-basics-tutorial/
#        filextentions.htm
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
# Usage (example):
#
#   python tsSoftwareParser.py --ScanDetails -i ./
#
# Methods:
#
#   TsSoftwareParser
#   TsSoftwareParser.CommentSyntax_Ada_Source
#   TsSoftwareParser.CommentSyntax_Bourne_Again_Shell_Script
#   TsSoftwareParser.CommentSyntax_Bourne_Shell_Script
#   TsSoftwareParser.CommentSyntax_C_CPP_H_Source
#   TsSoftwareParser.CommentSyntax_C_Shell_Script
#   TsSoftwareParser.CommentSyntax_Cobol_Source
#   TsSoftwareParser.CommentSyntax_Data_Source
#   TsSoftwareParser.CommentSyntax_Default_Source
#   TsSoftwareParser.CommentSyntax_Fortran_Source
#   TsSoftwareParser.CommentSyntax_Haskel_Source
#   TsSoftwareParser.CommentSyntax_Intel_Asm80_Source
#   TsSoftwareParser.CommentSyntax_Intel_PLM80_Source
#   TsSoftwareParser.CommentSyntax_Korn_Shell_Script
#   TsSoftwareParser.CommentSyntax_Literal_Haskel_Source
#   TsSoftwareParser.CommentSyntax_MS_Basic_Source
#   TsSoftwareParser.CommentSyntax_MS_Command_Line_Shell_Script
#   TsSoftwareParser.CommentSyntax_PHP_Source
#   TsSoftwareParser.CommentSyntax_PSF_Python_Extension_Script
#   TsSoftwareParser.CommentSyntax_PSF_Python_Script
#   TsSoftwareParser.CommentSyntax_Pascal_Source
#   TsSoftwareParser.CommentSyntax_Ruby_Source
#   TsSoftwareParser.Plain_Text_Document
#   TsSoftwareParser.__init__
#   TsSoftwareParser.tsLocSPGetDirectoryData
#   TsSoftwareParser.tsLocSPGetSyntaxFeatures
#   TsSoftwareParser.tsLocSPGetSyntaxList
#   TsSoftwareParser.tsLocSPReportResults
#   TsSoftwareParser.tsLocSPWriteDistribution
#   TsSoftwareParser.tsLocSPWriteRecognizedFileReport
#   TsSoftwareParser.tsLocSPWriteResults
#   TsSoftwareParser.tsLocSPWriteSkippedFileReport
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
#                  OptionWrapper for _Prototype. The goal
#                  is to use names that were more appropriate.
#
#   2013/04/14 rsg Modified the design to use the updated
#                  tsApplication module.
#
#   2013/04/17 rsg Removed, by commenting-out, getOptions from
#                  tsApplication argument list. This did not change
#                  the command line parsing code for argparse
#                  and optparse.
#
#   2013/11/14 rsg Commented-out unsupported code extenstions.
#
#   2013/11/15 rsg Re-organized and added language attribute to
#                  self.tsLocSPSyntaxList. Commented-out those
#                  file extensions that are not yet supported.
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
#   2013/01/17 rsg Resolve inability to launch via tsCommandLineEnv
#                  instead of via tsApplication. Does not offer
#                  appropriate coupling between external option
#                  definition and internal option handling, as
#                  exemplified by OptionWrapper.
#
#   2013/07/31 rsg Correct report header by replacing reference to
#                  __header__ by self.GetRunTimeHeader().
#
#################################################################

__title__     = 'tsSoftwareParser'
__version__   = '2.5.0'
__date__      = '11/15/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.' + \
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

import math
import os
import os.path

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger

#--------------------------------------------------------------------------

class TsSoftwareParser(object):
    '''
    Class of utiltity functions to parse source code and accumulate
    the number of source lines of code, blank/comment lines, word
    count and character count.
    '''

    #-----------------------------------------------------------------------

    def __init__(self,
                 logger,
                 debug_log,
                 input_dir,
                 output_file,
                 scan_log,
                 verbose_log,
                 fileID):
        '''
        Initialize the class and its variables.
        '''
        self.logger = logger
        self.debug_log = debug_log
        self.input_dir = input_dir
        self.output_file = output_file
        self.scan_log = scan_log
        self.verbose_log = verbose_log
        self.fileID = fileID

        self.processedFileCount = 0
        self.skippedFiles = []

        #-------------------------------------------------------------------

        self.tsLocSPSyntaxFeatures = {

            # Supported source code file extensions (lower case only)
            # and associated comment syntax method.
            #
            # NOTES:
            #
            #     1. Added extensions used by David Wheeler's SLOC Tool.
            #     2. Pending implementation, each new extension is
            #        associated with self.Plain_Text_Document.

            # Is NOT david_wheeler_sloc_emulation

            'Ada_Source': {
                'SingleLineComment': ['-- ']
                },

            'Bourne_Shell_Script': {
                'SingleLineComment': ['#']
                },

            'Bourne_Again_Shell_Script': {
                'SingleLineComment': ['#']
                },

            'C_CPP_H_Source': {
                'SingleLineComment': ['//'],
                'OpeningQuote': ['/*'],
                'ClosingQuote': ['*/'],
                },

            'C_Shell_Script': {
                'SingleLineComment': ['#']
                },

            'Data_Source': {
                'SingleLineComment': ['#'],
                'FirstTripleQuote': ['"""', "'''"]
                },

            'Default_Source': {
                'SingleLineComment': ['#'],
                'FirstTripleQuote': ['"""', "'''"]
                },

            'Fortran_Source': {
                'SingleLineComment': ['c', '*', '!'],
                'LeftJustifiedLine': ['!']
                },

            'Intel_Asm80_Source': {
                'SingleLineComment': [';']
                },

            'Intel_PLM80_Source': {
                'Directive': ['$'],
                'OpeningQuote': ['/*'],
                'ClosingQuote': ['*/'],
                },

            'Korn_Shell_Script': {
                'SingleLineComment': ['#']
                },

            'MS_Basic_Source': {
                'SingleLineComment': ['rem ', 'REM ']
                },

            'MS_Command_Line_Shell_Script': {
                'SingleLineComment': ['rem ', 'REM ']
                },

            'Pascal_Source': {
                'Directive': ['{$'],
                'OpeningQuote': ['{ '],
                'ClosingQuote': [' }'],
                },

            'PSF_Python_Script': {
                'SingleLineComment': ['#'],
                'FirstTripleQuote': ['"""', "'''"]
                },

            'PSF_Python_Extension_Script': {
                'SingleLineComment': ['#'],
                'FirstTripleQuote': ['"""', "'''"]
                }

            }

        self.tsLocSPSyntaxList = {

            '.ada': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Ada Source (95 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Ada_Source, # ADA
                'words': 0},

            '.adb': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Ada Source (95 standard, Body)',
                'lines': 0,
                'method': self.CommentSyntax_Ada_Source, # ADA
                'words': 0},

            '.ads': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Ada Source (95 standard, Specifications)',
                'lines': 0,
                'method': self.CommentSyntax_Ada_Source, # ADA
                'words': 0},

            '.asm': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Assembler Source (Intel ASM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_Asm80_Source, #ASM
                'words': 0},

            '.asm80': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Assembler Source (Intel ASM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_Asm80_Source, #ASM
                'words': 0},

            '.bas': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'BASIC Source',
                'lines': 0,
                'method': self.CommentSyntax_MS_Basic_Source, #BASIC
                'words': 0},

            '.bash': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'BASH Script (Bourne Again Shell)',
                'lines': 0,
                'method': self.CommentSyntax_Bourne_Again_Shell_Script, #BASH
                'words': 0},

            '.bat': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'BATCH Script (Microsoft Command Line Shell)',
                'lines': 0,
                'method': self.CommentSyntax_MS_Command_Line_Shell_Script, #BAT
                'words': 0},

            '.c': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C Source',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, #C
                'words': 0},

            '.c++': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C++ Source',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, #C++
                'words': 0},

            '.cbl': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'COBOL Source',
                'lines': 0,
                'method': self.CommentSyntax_Cobol_Source, # COBOL
                'words': 0},

            '.cc': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C++ Source',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, # C++
                'words': 0},

            '.cob': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'COBOL Source',
                'lines': 0,
                'method': self.CommentSyntax_Cobol_Source, # COBOL
                'words': 0},

            '.cpp': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C++ Source',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, #C++
                'words': 0},

            '.cs': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C\# Source (Microsoft)',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, # C#
                'words': 0},

            '.csh': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C Shell Script',
                'lines': 0,
                'method': self.CommentSyntax_C_Shell_Script, #CSH
                'words': 0},

            '.cxx': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C++ Source',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, # C++
                'words': 0},

            '.f': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.f77': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source (77 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.f90': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source (90 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.f95': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source (95 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.for': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.ftn': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.h': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'C Source (Header)',
                'lines': 0,
                'method': self.CommentSyntax_C_CPP_H_Source, #C
                'words': 0},

            '.inc': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'FORTRAN Source (Include)',
                'lines': 0,
                'method': self.CommentSyntax_Fortran_Source, #FORTRAN
                'words': 0},

            '.ksh': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'KSH Script (Korn Shell)',
                'lines': 0,
                'method': self.CommentSyntax_Korn_Shell_Script, #KSH
                'words': 0},

            '.p': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Pascal Source',
                'lines': 0,
                'method': self.CommentSyntax_Pascal_Source, #PASCAL
                'words': 0},

            '.pas': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Pascal Source',
                'lines': 0,
                'method': self.CommentSyntax_Pascal_Source, # PASCAL
                'words': 0},

            '.plm': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'PL/M Source (Intel PLM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_PLM80_Source, # PLM
                'words': 0},

            '.plm80': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'PL/M Source (Intel PLM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_PLM80_Source, # PLM
                'words': 0},

            '.plm96': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'PL/M Source (Intel PLM96 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_PLM80_Source, # PLM
                'words': 0},

            '.plmext': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'PL/M Extension Source (Intel PLM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_PLM80_Source, # PLM
                'words': 0},

            '.py': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Python Script Source',
                'lines': 0,
                'method': self.CommentSyntax_PSF_Python_Script, # PYTHON
                'words': 0},

            '.rb': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Ruby Source',
                'lines': 0,
                'method': self.CommentSyntax_Ruby_Source, # RUBY
                'words': 0},

            '.s': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Assembler Source (Intel ASM80 standard)',
                'lines': 0,
                'method': self.CommentSyntax_Intel_Asm80_Source, # ASSEMBLER
                'words': 0},

            '.sh': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'SH Script (Bourne Shell)',
                'lines': 0,
                'method': self.CommentSyntax_Bourne_Shell_Script,
                'words': 0},

            '.txt': {
                'chars': 0,
                'codeLines': 0,
                'commentLines': 0,
                'files': 0,
                'language': 'Plain Text (ASCII)',
                'lines': 0,
                'method': self.Plain_Text_Document, # ASCII TEXT
                'words': 0}

            }

##            '.ec': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'GEOS error-checking version ',
##                'lines': 0,
##                'method': self.CommentSyntax_C_CPP_H_Source, #C++
##                'words': 0},

##            '.ecp': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.CommentSyntax_C_CPP_H_Source, #C++
##                'words': 0},

##            ## '.dat': {
##              'chars': 0,
##              'codeLines': 0,
##              'commentLines': 0,
##              'files': 0,
##              'language': 'Data Source',
##              'lines': 0,
##              'method': self.CommentSyntax_DAT_Source,
##              'words': 0},self.CommentSyntax_Data_Source,
##            ## '.pyx': {
##              'chars': 0,
##              'codeLines': 0,
##              'commentLines': 0,
##              'files': 0,
##              'language': 'Python Extension Script',
##              'lines': 0,
##              'method': self.CommentSyntax_PYX_Source,
##              'words': 0},self.CommentSyntax_PSF_Python_Extension_Script,
##            ## '.src': {
##              'chars': 0,
##              'codeLines': 0,
##              'commentLines': 0,
##              'files': 0,
##              'language': 'Default Source',
##              'lines': 0,
##              'method': self.CommentSyntax_SRC_Source,
##              'words': 0},self.CommentSyntax_Default_Source,

##            '.awk': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'AWK Script',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # AWK
##                'words': 0},

##            '.cl': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'LISP Cursor Library View Source',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LISP
##                'words': 0},

##            '.el': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'LISP Source',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LISP
##                'words': 0},

##            '.exp': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'EXPECT Source',
##                'lines': 0,
##                'method':self.Plain_Text_Document, # EXPECT
##                'words': 0},

##            '.hs': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'HASKELL Source',
##                'lines': 0,
##                'method': self.CommentSyntax_Haskel_Source, # HASKELL
##                'words': 0},

##            '.i3': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'MODULA-3 Source',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # MODULA-3
##                'words': 0},

##            '.ig': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'MODULA-3 Source',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # MODULA-3
##                'words': 0},

##            '.itk': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # TCL
##                'words': 0},

##            '.java': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Java Source',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # JAVA
##                'words': 0},

##            '.jl': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LISP
##                'words': 0},

##            '.l': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LEX/FLEX
##                'words': 0},

                ## Under Construction: Literal Haskel
##          '.lhs': self.CommentSyntax_Literal_Haskel_Source, # Literal Haskell
##            '.lhs': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LITERAL HASKELL
##                'words': 0},

##            '.lsp': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method':self.Plain_Text_Document, # LISP
##                'words': 0},

##            '.m': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # OBJECTIVE-C
##                'words': 0},

##            '.m3': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # MODULA-3
##                'words': 0},

##            '.mg': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # MODULA-3
##                'words': 0},

##            '.ml': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # ML
##                'words': 0},

##            '.ml3': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # ML
##                'words': 0},

##            '.pad': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Ada-Data Source',
##                'lines': 0,
##                'method': self.CommentSyntax_Ada_Source, # ADA
##                'words': 0},

##            '.pc': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.CommentSyntax_C_CPP_H_Source, # C
##                'words': 0},

##            '.pcc': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.CommentSyntax_C_CPP_H_Source, # C
##                'words': 0},

##            '.perl': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PERL
##                'words': 0},

                ## Under Construction: Literal Haskel
##          '.php': self.CommentSyntax_PHP_Source, # PHP
##            '.php': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PHP
##                'words': 0},

##            '.php3': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PHP
##                'words': 0},

##            '.php4': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PHP
##                'words': 0},

##            '.php5': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PHP
##                'words': 0},

##            '.php6': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PHP
##                'words': 0},

##            '.pl': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PERL
##                'words': 0},

##            '.pm': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # PERL
##                'words': 0},

##            '.scm': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # LISP
##                'words': 0},

##            '.sed': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # SED
##                'words': 0},

##            '.sql': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # SQL
##                'words': 0},

##            '.tcl': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # TCL
##                'words': 0},

##            '.tk': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # TCL
##                'words': 0},

##            '.y': {
##                'chars': 0,
##                'codeLines': 0,
##                'commentLines': 0,
##                'files': 0,
##                'language': 'Unknown',
##                'lines': 0,
##                'method': self.Plain_Text_Document, # YACC/BISON
##                'words': 0}
##            }

    #-----------------------------------------------------------------------

    def tsLocSPGetSyntaxFeatures(self):
        '''
        '''
        return (self.tsLocSPSyntaxFeatures)

    #-----------------------------------------------------------------------

    def tsLocSPGetSyntaxList(self):
        '''
        '''
        return (self.tsLocSPSyntaxList)

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
                singleLineComment = strippedLine.find('-- ')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = max(strippedLine.find('rem '),
                                        strippedLine.find('REM '))

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = max(strippedLine.find('rem '),
                                        strippedLine.find('REM '))

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

                    except Exception, e:
                        closingQuote = -1
                else:
                    closingQuote = strippedLine.find('*/')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we an singleLine comment
                elif singleLineComment == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def CommentSyntax_Cobol_Source(self, name):
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
                leftJustifiedLine = line.lstrip()
                strippedLine = line.strip()

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started a comment line?
                elif leftJustifiedLine[0].lower() == '*':

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started an indented directive line?
                elif leftJustifiedLine[0] == '$':

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('DIRCODE: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception, e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if self.scan_log:
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

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                leftJustifiedLine = line.lstrip()
                strippedLine = line.strip()

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started a High Performance Fortran or
                # Open Multi-Programming directive line?
                elif ((line[0].lower() == 'c' or \
                       line[0] == '*' or \
                       line[0] == '!') and \
                      (line.lower().find('hpf$') == 1 or \
                       line.lower().find('omp$') == 1)):

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('DIRCODE: <%s>' % line)
 
                # Have we started a comment line?
                elif line[0].lower() == 'c' or \
                     line[0] == '*' or \
                     line[0] == '!':

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started an indented comment line?
                elif leftJustifiedLine[0] == '!':

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def CommentSyntax_Haskel_Source(self, name):
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
                singleLineComment = strippedLine.find('-- ')
                openingQuote = strippedLine.find('{- ')
                if openingQuote != -1:
                    try:
                        closingQuote = strippedLine.find(
                            '-}', openingQuote + 2)

                    except Exception, e:
                        closingQuote = -1
                else:
                    closingQuote = strippedLine.find('-}')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we an singleLine comment
                elif singleLineComment == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find(';')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a directive line?
                elif directive == 0:

                    # Started a directive line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' %  strippedLine)

                    docStringActive = True

                elif closingQuote == 0:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                    docStringActive = False

                # Have we previously started a documentation string block?
                elif docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def CommentSyntax_Literal_Haskel_Source(self, name):
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
                singleLineComment = strippedLine.find('\\')
                openingCode = strippedLine.find('\\begin{code}')
                if openingCode != -1:
                    try:
                        closingCode = strippedLine.find(
                            '\\end{code}')

                    except Exception, e:
                        closingCode = -1
                else:
                    closingCode = strippedLine.find(
                            '\\end{code}')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we an singleLine comment
                elif singleLineComment == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started or ended a code block?
                elif openingCode > -1:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCode,
                                          closingCode))

                    if closingCode == -1:
                        # Started documatation string block
                        docStringActive = True
                    else:
                        # Ended documatation string block
                        docStringActive = False

                # Have we started or ended a string block?
                elif openingCode > 0:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCode,
                                          closingCode))

                    if closingCode == -1:
                        # Started documatation string block
                        codeStringActive = True
                    else:
                        # Ended documatation string block
                        codeStringActive = False

                # Have we previously started a code string block?
                elif codeStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCode,
                                          closingCode))

                    if closingCode != -1:
                        # Ended documatation string block
                        codeStringActive = False

                # Have we previously started a documentation string block?
                elif docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCode,
                                          closingCode))

                    if closingCode != -1:
                        # Ended documatation string block
                        codeStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
        docCurlyBraceStringActive = False
        docParenthesesStringActive = False

        try:
            source = open(name)

            docStringActive = False
            for line in source:
                lines = lines + 1
                strippedLine = line.strip()
                directive = strippedLine.find('{$')
                openingCurlyBraceQuote = strippedLine.find('{ ')
                if openingCurlyBraceQuote != -1:
                    try:
                        closingCurlyBraceQuote = strippedLine.find(
                            ' }', openingCurlyBraceQuote + 2)

                    except Exception, e:
                        closingCurlyBraceQuote = -1
                else:
                    closingCurlyBraceQuote = strippedLine.find(' }')
                openingParenthesesQuote = strippedLine.find('(* ')
                if openingParenthesesQuote != -1:
                    try:
                        closingParenthesesQuote = strippedLine.find(
                            ' *)', openingParenthesesQuote + 2)

                    except Exception, e:
                        closingParenthesesQuote = -1
                else:
                    closingParenthesesQuote = strippedLine.find(' *)')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a directive line?
                elif directive == 0:

                    # Started a directive line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingParenthesesQuote == 0:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingParenthesesQuote,
                                          closingParenthesesQuote))

                    if closingParenthesesQuote == -1:
                        # Started documatation string block
                        docParenthesesStringActive = True
                    else:
                        # Ended documatation string block
                        docParenthesesStringActive = False

                # Have we started or ended a string block?
                elif openingParenthesesQuote > 0:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingParenthesesQuote,
                                          closingParenthesesQuote))

                    if closingParenthesesQuote == -1:
                        # Started documatation string block
                        docParenthesesStringActive = True
                    else:
                        # Ended documatation string block
                        docParenthesesStringActive = False

                # Have we previously started a documentation string block?
                elif docParenthesesStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingParenthesesQuote,
                                          closingParenthesesQuote))

                    if closingParenthesesQuote != -1:
                        # Ended documatation string block
                        docParenthesesStringActive = False

                # Have we started or ended a string block?
                elif openingCurlyBraceQuote == 0:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCurlyBraceQuote,
                                          closingCurlyBraceQuote))

                    if closingCurlyBraceQuote == -1:
                        # Started documatation string block
                        docCurlyBraceStringActive = True
                    else:
                        # Ended documatation string block
                        docCurlyBraceStringActive = False

                # Have we started or ended a string block?
                elif openingCurlyBraceQuote > 0:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCurlyBraceQuote,
                                          closingCurlyBraceQuote))

                    if closingCurlyBraceQuote == -1:
                        # Started documatation string block
                        docCurlyBraceStringActive = True
                    else:
                        # Ended documatation string block
                        docCurlyBraceStringActive = False

                # Have we previously started a documentation string block?
                elif docCurlyBraceStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s> at %d / %d' % \
                                         (strippedLine,
                                          openingCurlyBraceQuote,
                                          closingCurlyBraceQuote))

                    if closingCurlyBraceQuote != -1:
                        # Ended documatation string block
                        docCurlyBraceStringActive = False

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def CommentSyntax_PHP_Source(self, name):
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
                shellStyleSingleLineComment = strippedLine.find('#')
                cppStyleSingleLineComment = strippedLine.find('//')
                openingQuote = strippedLine.find('/*')
                if shellStyleSingleLineComment == 0:

                    singleLineComment = shellStyleSingleLineComment

                elif cppStyleSingleLineComment == 0:

                    singleLineComment = cppStyleSingleLineComment

                else:

                    singleLineComment = -1

                if openingQuote != -1:
                    try:
                        closingQuote = strippedLine.find(
                            '*/', openingQuote + 2)

                    except Exception, e:
                        closingQuote = -1
                else:
                    closingQuote = strippedLine.find('*/')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we an singleLine comment
                elif singleLineComment == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif openingQuote == 0:

                    commentLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def CommentSyntax_Ruby_Source(self, name):
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception, e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if self.scan_log:
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

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception, e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if self.scan_log:
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

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                else:

                    # Started a code line.
                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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
                singleLineComment = strippedLine.find('#')
                firstTripleQuote = max(strippedLine.find('"""'),
                                       strippedLine.find("'''"))
                if firstTripleQuote != -1:
                    try:
                        nextTripleQuote = max(
                            strippedLine.find('"""',
                                              firstTripleQuote + 3),
                            strippedLine.find("'''",
                                              firstTripleQuote + 3))

                    except Exception, e:
                        nextTripleQuote = -1

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    if codeStringActive:

                        # Started a blank code line.
                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s>' % strippedLine)

                    else:

                        # Started a blank comment line.
                        commentLines += 1

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                elif singleLineComment == 0:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a documentation string block?
                elif (firstTripleQuote == -1) and \
                     docStringActive:

                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                # Have we previously started a code string block?
                elif (firstTripleQuote == -1) and \
                     codeStringActive:

                    codeLines += 1

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                # Have we started or ended a string block?
                elif firstTripleQuote == 0:

                    if codeStringActive:

                        codeLines += 1

                        if self.scan_log:
                            self.logger.info('   CODE: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        codeStringActive = False

                    elif not docStringActive:

                        commentLines += 1

                        if self.scan_log:
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

                        if self.scan_log:
                            self.logger.info('COMMENT: <%s> at %d / %d' % \
                                             (strippedLine,
                                              firstTripleQuote,
                                              nextTripleQuote))

                        # Ended documentation string block
                        docStringActive = False

                # Have we started or ended a code string block?
                elif firstTripleQuote > 0:

                    codeLines += 1

                    if self.scan_log:
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

                    if self.scan_log:
                        self.logger.info('   CODE: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def Plain_Text_Document(self, name):
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
                singleLineComment = strippedLine.find('#')

                # Have we a line of whitespace
                if len(strippedLine) == 0:

                    # Started a blank comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)
 
                # Have we started a comment line?
                else:

                    # Started a comment line.
                    commentLines += 1

                    if self.scan_log:
                        self.logger.info('COMMENT: <%s>' % strippedLine)

                chars = chars + len(line)
                words = words + len(line.split())

            source.close()

        except Exception, e:
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

    def tsLocSPGetDirectoryData(self):
        '''
        Controls the file selection and display of software devemopment
        metrics.
        '''
        top = self.input_dir

        characterCount = 0
        codeLineCount = 0
        commentLineCount = 0
        fileCount = 0
        lineCount = 0
        values = []
        wordCount = 0

        self.fileID.write('\n\t\t' + \
                          'Individual Source Code Feature Statistics' + \
                          '\n')

        self.fileID.write('\n')
        self.fileID.write('%8.8s %8.8s %8.8s %8.8s %8.8s %s\n' % (
            'CODE',
            'CMNTS',
            'LINES',
            'WORDS',
            'CHARS',
            'PATH/FILE'))

        syntaxList = self.tsLocSPGetSyntaxList()

        for dirpath, dirnames, filenames in os.walk(top, topdown=True):
            for name in filenames:
                skipped = True
                for sourceCodeExtension in list(syntaxList.keys()):
                    theName = os.path.abspath(os.path.join(dirpath, name))
                    if name.lower().endswith(sourceCodeExtension.lower()):
                        skipped = False
                        self.processedFileCount += 1
                        if self.scan_log:
                            self.logger.debug(
                                '\n\n\twcMethod: <%s>\n' % theName)
                        elif self.debug_log:
                            self.logger.debug('wcMethod: <%s>' % theName)

                        try:

                            wcDataBase = syntaxList[sourceCodeExtension]

                            wcMethod = wcDataBase['method']

                            (codeLines,
                             commentLines,
                             lines,
                             words,
                             chars) = wcMethod(theName)

                            wcDataBase['chars'] += chars

                            wcDataBase['codeLines'] += codeLines

                            wcDataBase['commentLines'] += commentLines

                            wcDataBase['files'] += 1

                            wcDataBase['lines'] += lines

                            wcDataBase['words'] += words

                            self.fileID.write('%8d %8d %8d %8d %8d %s\n' % (
                                codeLines,
                                commentLines,
                                lines,
                                words,
                                chars,
                                theName))

                        except Exception, e:

                            self.logger.error('getDirectoryData: %s' % e)

##                        self.fileID.write('%8d %8d %8d %8d %8d %s\n' % (
##                            wcDataBase['codeLines'],
##                            wcDataBase['commentLines'],
##                            wcDataBase['lines'],
##                            wcDataBase['words'],
##                            wcDataBase['chars'],
##                            sourceCodeExtension))

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

    def tsLocSPReportResults(self,
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
        hline = '-' * 78

        print('%s' % __header__)

        self.tsLocSPWriteResults(
            '%s\n' % hline)

        self.tsLocSPWriteResults(
            '  Input Path:     <%s>.' % self.input_dir)
        self.tsLocSPWriteResults(
            '  Results are available in "%s".' % \
            os.path.abspath(self.output_file))

        self.tsLocSPWriteResults('\n%s\n' % hline)

        indentText = ' ' * 7
        self.tsLocSPWriteResults(
            '\t\tOverall Source Code Feature Statistics' + \
            '\n\n' + \
            '%s %8.8s %8.8s %8.8s %8.8s %8.8s %10.10s' % (
            indentText,
            'FILES',
            'CODE',
            'CMNTS',
            'LINES',
            'WORDS',
            'CHARS'))

##        hline = '-' * 78
##        self.tsLocSPWriteResults('\n%s' % hline)

        if lineCount != codeLineCount + commentLineCount:
            fmt1 = 'reportResults: LineCount (%d) != ' % lineCount
            fmt2 = 'codeLineCount (%d) + commentLineCount (%d)' % (
                    codeLineCount, commentLineCount)
            self.logger.error(fmt1 + fmt2)

##        self.writeResults('\n')

        if lineCount > 0:
            self.tsLocSPWriteResults(
                '   Pct:            %6.2f%s  %6.2f%s  %6.2f%s' % (
                    (100.0 * (
                        float(codeLineCount) /  float(lineCount))), '%',
                    (100.0 * (
                        float(commentLineCount) /  float(lineCount))), '%',
                    (100.0 * (
                        float(lineCount) / float(lineCount))), '%'))

        self.tsLocSPWriteResults(
            'Totals: %8d %8d %8d %8d %8d %10d' % (
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

        self.tsLocSPWriteResults(
            '   Std: %8d %8d %8d %8d %8d %10d' % (
            stdLineCount,
            math.sqrt(avgOfCodeDeviationsSquared),
            math.sqrt(avgOfCmntDeviationsSquared),
            math.sqrt(avgOfLineDeviationsSquared),
            math.sqrt(avgOfWordDeviationsSquared),
            math.sqrt(avgOfCharDeviationsSquared)))

        self.tsLocSPWriteResults(
            '   Avg: %8d %8d %8d %8d %8d %10d' % (
            avgFileCount,
            avgCodeCount,
            avgCmntCount,
            avgLineCount,
            avgWordCount,
            avgCharacterCount))

        self.tsLocSPWriteResults(
            '\n%s\n' % hline)

##        self.tsLocSPWriteEstimatedDevelopmentEffort(
##            codeLineCount)

##        self.tsLocSPWriteResults(
##            '\n%s\n' % hline)

        self.tsLocSPWriteDistribution(
            fileCount,
            codeLineCount,
            commentLineCount,
            lineCount,
            wordCount,
            characterCount)

        self.tsLocSPWriteRecognizedFileReport()

        self.tsLocSPWriteSkippedFileReport()

        self.tsLocSPWriteResults('\n%s\n' % hline)

    #-----------------------------------------------------------------------

    def tsLocSPWriteDistribution(self,
                                 fileCount,
                                 codeLineCount,
                                 commentLineCount,
                                 lineCount,
                                 wordCount,
                                 characterCount):
        '''
        '''
        indentText = ' ' * 1
        self.tsLocSPWriteResults(
            '\tDistribution of Source Code Feature Statistics ' + \
            'by File Types' + \
            '\n\n' + \
            '%s%7.7s   %8.8s %8.8s %8.8s %8.8s %8.8s %10.10s %8s' % (
                indentText,
                'TYPES',
                'FILES',
                'CODE',
                'CMNTS',
                'LINES',
                'WORDS',
                'CHARS',
                '%-LINES'))

        syntaxList = self.tsLocSPGetSyntaxList()
        for sourceCodeExtension in sorted(list(syntaxList.keys())):

            try:

                wcDataBase = syntaxList[sourceCodeExtension]

                codeLines = wcDataBase['codeLines']
                commentLines = wcDataBase['commentLines']
                files = wcDataBase['files']
                lines = wcDataBase['lines']
                words = wcDataBase['words']
                chars = wcDataBase['chars']

##              self.fileID.write('%8d %8d %8d %8d %8d %s\n' % (
##                  wcDataBase['codeLines'],
##                  wcDataBase['commentLines'],
##                  wcDataBase['lines'],
##                  wcDataBase['words'],
##                  wcDataBase['chars'],
##                  sourceCodeExtension))

                if lines > 0:

                    percentage = '%6.2f%s' % (
                        100.0 * (float(lines) / float(lineCount)), '%')

    ##          self.fileID.write('%8d %8d %8d %s %8d %8d %s\n' % (

                    indentText = ' ' * 3
                    self.tsLocSPWriteResults(
                        '%s%-7s %8s %8d %8d %8d %8d %10d %8s' % (
                            indentText,
                            sourceCodeExtension,
                            files,
                            codeLines,
                            commentLines,
                            lines,
                            words,
                            chars,
                            percentage))

##                  self.tsLocSPWriteResults('%d %8d %8d %8d %s %8d %8d %s\n' % (
##                      files,
##                      codeLines,
##                      commentLines,
##                      lines,
##                      percentage,
##                      words,
##                      chars,
##                      sourceCodeExtension))

            except Exception, e:

                self.logger.error('writeDistribution: %s' % e)

##                        self.fileID.write('%8d %8d %8d %8d %8d %s\n' % (
##                            wcDataBase['codeLines'],
##                            wcDataBase['commentLines'],
##                            wcDataBase['lines'],
##                            wcDataBase['words'],
##                            wcDataBase['chars'],
##                            sourceCodeExtension))
##        self.fileID.write('%s\n' % buffer)
##        self.tsLocSPWriteResults(buffer)

    #-----------------------------------------------------------------------

    def tsLocSPWriteResults(self, buffer):
        '''
        '''
        self.fileID.write('%s\n' % buffer)
        print(buffer)

    #-----------------------------------------------------------------------

    def tsLocSPWriteSkippedFileReport(self):
        '''
        '''
        syntaxList = self.tsLocSPGetSyntaxList()
 
        skippedFileCount = len(self.skippedFiles)
        if skippedFileCount > 0:
            hline = '-' * 78
            self.tsLocSPWriteResults('\n%s' % hline)
            fmt = 'Skipped %d of %d file(s) for having invalid "name.ext"' % \
                  (skippedFileCount,
                   skippedFileCount + self.processedFileCount)

            ## print('  %s.\n' % fmt)
            self.tsLocSPWriteResults('\n%s:' % fmt)

            recognizedKeys = ''
            i = -1
            for key in sorted(syntaxList.keys()):
                i += 1
                if recognizedKeys == '':
                    recognizedKeys += 'Valid file "name.ext" ' + \
                                      '(Upper or Lower case):' + \
                                      '\n\n      %-8s' % key
                elif i < 8:
                    recognizedKeys += '%-8s' % key
                else:
                    i = 0
                    recognizedKeys += '\n      %-8s' % key
 
            self.tsLocSPWriteResults('\n   %s\n' % recognizedKeys)

            i = -1
            for item in self.skippedFiles:
                i += 1
                if (i == 0):
                    self.fileID.write('\n   %s\n' % item)
                else:
                    self.fileID.write('   %s\n' % item)

    #-----------------------------------------------------------------------

    def tsLocSPWriteRecognizedFileReport(self):
        '''
        '''
        hline = '-' * 78

        self.tsLocSPWriteResults(
            '\n%s\n' % hline)

        indentText = ' ' * 1
        self.tsLocSPWriteResults(
            '\tDefinition of Source Code by File Types' + \
            '\n\n' + \
            '%s %8.8s  %s' % (
                indentText,
                'TYPES',
                'DEFINITION'))

        syntaxList = self.tsLocSPGetSyntaxList()
        for key in sorted(syntaxList.keys()):
            lines = syntaxList[key]['lines']
            if lines > 0:

                language = syntaxList[key]['language']

                self.tsLocSPWriteResults(
                    '%s %8.8s  %s' % (indentText, key, language))

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    pass
