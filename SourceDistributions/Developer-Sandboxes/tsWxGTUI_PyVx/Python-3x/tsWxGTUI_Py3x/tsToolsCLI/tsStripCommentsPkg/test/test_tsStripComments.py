#! /usr/bin/env python
#"Time-stamp: <07/27/2013  7:08:19 AM rsg>"
'''
test_tsStripComments.py - Test and demonstrate the application
program which generates a directory of non-commented Python
source files. It strips comments and doc strings by de-tokenizing
a tokenized version of each source file.
'''
#################################################################
#
# File: test_tsStripComments.py
#
# Purpose:
#
#    Test and demonstrate the application program which generates
#    a directory of non-commented Python source files. It strips
#    comments and doc strings by de-tokenizing a tokenized
#    version of each source file.
#
# Limitations:
#
#    1. No industry standard file naming convention. Each lines-of-code
#       analysis tool presumes that file name extensions unambiguously
#       distinguish one programming language format from another.
#       Comparing the sample files provided by the "tsStripComments"
#       tool with two other tools reveals that some extensions may be
#       associated with different programming languages. For example:
#
#       a. "tsStripComments-2.0.0" by Richard S. Gordon (rigordo@comcast.net
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
#       a. "tsStripComments-2.0.0" by Richard S. Gordon (rigordo@comcast.net
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
#    3. "tsStripComments-2.0.0" Analysis Methods.
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
#   python        tsStripComments.py
#
#   python2.7     tsStripComments.py  [-i INPUTDIR] [-o OUTPUTFILE]
#
#   python3.3     tsStripComments.py  [-h] [-v] [-a]
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
# Modifications:
#
# ToDo:
#
#################################################################

__title__     = 'test_tsStripComments'
__version__   = '2.2.0'
__date__      = '05/25/2013'
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

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    ##import tsApplication as tsAPP
    import tsExceptions as tse
    import tsLogger as Logger

    from tsCommandLineEnv import CommandLineEnv

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsToolsCLI

except ImportError as importCode:

    print('%s: ImportError (tsToolsCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    from tsStripComments import TsStripComments

except ImportError as importCode:

    print('%s: ImportError (tsToolsCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

class test_tsStripComments(TsStripComments):
    '''
    Test and demonstrate the application program which scans a file
    directory tree and produces reports of software source code and
    development project    '''
    def __init(self):
        '''
        '''
        TsStripComments.__init__(self)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def exitTest():
        '''
        The part of tsOperatorSettingsParser that initiates
        termination with the appropriate normal or abnormal exit code
        and message.
        '''
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def mainEntryPointTest():
        '''
        The wrapper-based part of "tsOperatorSettingsParser" that initiates
        startup with the appropriate command line parsing method.
        '''
        theApp = test_tsStripComments()
        theApp.MainLoop()

##      print('\n\n\tLineOfCode Startup:')
##      state = dir(theApp)
##      for item in state:
##          if item == 'options':
##              print('\t\t%s=%s' % (item, str(theApp.options)))
##          elif item == 'args':
##              print('\t\t%s=%s' % (item, str(theApp.args)))
##          else:
##              print('\t\t%s' % item)
##      theApp.logger.debug('\n\n\tLineOfCode Startup: %s' % dir(theApp))
##      theApp.MainLoop()

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
        enableDefaultCommandLineParser=False,
        runTimeEntryPoint=mainEntryPointTest)

    myApp.Wrapper()

