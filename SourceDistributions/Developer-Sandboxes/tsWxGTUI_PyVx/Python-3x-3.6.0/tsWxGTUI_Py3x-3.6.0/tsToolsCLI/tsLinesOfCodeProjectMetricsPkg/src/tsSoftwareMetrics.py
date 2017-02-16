#! /usr/bin/env python
#"Time-stamp: <09/14/2013  5:35:53 PM rsg>"
'''
tsSoftwareMetrics.py - Class to scan a file directory tree
and produce a report of the number of source code files,
lines of code, blank/comment lines, word count and
character count.
'''
#################################################################
#
# File: tsSoftwareMetrics.py
#
# Purpose:
#
#    Class to scan a file directory tree and produce a report
#    of the number of source code files, lines of code, blank/
#    comment lines, word count and character count.
#
# Limitations:
#
# Notes:
#
# Usage (example):
#
#   python tsSoftwareMetrics.py
#
# Methods:
#
#   TsSoftwareMetrics
#   TsSoftwareMetrics.reportResults
#   TsSoftwareMetrics.writeDistribution
#   TsSoftwareMetrics.writeResults
#   TsSoftwareMetrics.writeSkippedFileReport
#
# Modifications:
#
# ToDo:
#
#################################################################

__title__     = 'tsSoftwareMetrics'
__version__   = '2.3.0'
__date__      = '07/31/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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

##try:

##    import tsLibCLI

##except ImportError, importCode:

##    print('%s: ImportError (tsLibCLI); ' % __title__ + \
##          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

##    import tsToolsCLI
    from tsSoftwareParser import TsSoftwareParser

except ImportError as importCode:

    print('%s: ImportError (tsToolsCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

class TsSoftwareMetrics(object):
    '''
    Class to scan a file directory and produce a report of
    the number of source code files, lines of code, blank/comment lines,
    word count and character count.
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

        self.softwareParser = TsSoftwareParser(
            self.logger,
            debug_log,
            input_dir,
            output_file,
            scan_log,
            verbose_log,
            fileID)

    #-----------------------------------------------------------------------

    def tsLocSMGetDirectoryData(self):
        '''
        Controls the file selection and display of software devemopment
        metrics.
        '''
        (myFileCount,
         myCodeLineCount,
         myCommentLineCount,
         myLineCount,
         myWordCount,
         myCharacterCount,
         myValues) = self.softwareParser.tsLocSPGetDirectoryData()

        return (myFileCount,
                myCodeLineCount,
                myCommentLineCount,
                myLineCount,
                myWordCount,
                myCharacterCount,
                myValues)
 
    #-----------------------------------------------------------------------

    def tsLocSMReportResults(self,
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
        self.softwareParser.tsLocSPReportResults(
            fileCount,
            codeLineCount,
            commentLineCount,
            lineCount,
            wordCount,
            characterCount,
            values)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    pass
