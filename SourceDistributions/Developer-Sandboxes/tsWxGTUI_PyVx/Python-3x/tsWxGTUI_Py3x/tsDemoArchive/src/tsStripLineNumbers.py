#! /usr/bin/env python
#"Time-stamp: <08/20/2013  7:36:33 AM rsg>"
'''
tsStripLineNumbers.py - Tool to strip line numbers from source code.
'''
#################################################################
#
# File: tsStripLineNumbers.py
#
# Purpose:
#
#    Tool to strip line numbers from source code (such as
#    annotated listings) that do not reference line numbers
#    for conditional branching.
#
# Limitations:
#
#     Output from fixed format Fortran (F77) code is NOT corrected to
#     ensure that each statement first character begins in column 7 and
#     that each ampersand ("&") continuation character is in column 6.
#
# Usage (examples):
#
#     python tsStripLineNumbers.py
#
# Usage:
#
#     python tsStripLineNumbers.py -i SourcePath -o TargetPath
#
# Notes:
#
#     None
#
# Modifications:
#
#    2013/06/09 rsg Updated build __version__ through
#                   __header__.
#
#    2013/06/10 rsg Added support for command line keywords.
#                   Copied both stripped and unstripped files
#                   into target directory.
#
# ToDo:
#
#
#################################################################

__title__     = 'tsStripLineNumbers.py'
__version__   = '2.0.0'
__date__      = '06/10/2013'
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

#--------------------------------------------------------------------------

import os
import os.path
from optparse import OptionParser
import sys

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))


#--------------------------------------------------------------------------

try:

    import tsLogger as Logger

    import tsCommandLineEnv

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

nullCharacter = chr(0x0)
nullString = ''
numericCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
targetPath = '../published/'
lineNumberedExtensions = ['.bas']

#--------------------------------------------------------------------------

def cleanupSourceLine(theSourceName, theTargetName, theLogger):
    '''
    Copy contents of specified source file to target directory after
    removing line numbers and spurious whitespace at end of each line.
    '''
    ## source = './pp20001'
    ## target = '%s.%s' % (source, ext)
    sourceID = open(theSourceName, 'r')
    targetID = open(theTargetName, 'w')
    enableStripping = True
    sequence = 0
    offset = 0
    for line in sourceID:

        if line[0] == '$':

            offset = 0

            targetID.write('%s\n' % line[offset: len(line)].replace(
                nullCharacter, nullString).rstrip())

        elif enableStripping:

            if sequence == 0:

                theLogger.debug(line)

                if len(line.strip()) == 0:

                    continue

            else:

                for i in range(len(line)):

                    if line[i] == '$':

                        offset = 0
                        break

                    elif line[i] in numericCharacters:

                        offset = min(i, len(line))

                    elif line[i] != ' ':

                        offset = min(i, len(line))
                        break

                    elif theSourceName.lower().find('.asm') > -1:

                        offset = min(i + 1, len(line))
                        break

                    else:

                        offset = min(i, len(line))
                        break

                if offset == 0:

                    enableStripping = False

                targetID.write('%s\n' % line[offset: len(line)].replace(
                    nullCharacter, nullString).rstrip())

        else:

            offset = 0
            targetID.write('%s\n' % line[offset: len(line)].replace(
                nullCharacter, nullString).rstrip())

        sequence += 1

    targetID.flush()
    targetID.close()
    sourceID.close()

#--------------------------------------------------------------------------

def copySourceFile(theSourceName, theTargetName, theLogger):
    '''
    Copy line numbered contents of specified source file to target
    directory after removing spurious whitespace at end of each line.
    '''
    ## source = './pp20001'
    ## target = '%s.%s' % (source, ext)
    sourceID = open(theSourceName, 'r')
    targetID = open(theTargetName, 'w')

    offset = 0
    for line in sourceID:

        targetID.write('%s\n' % line[offset: len(line)].replace(
            nullCharacter, nullString).rstrip())

    targetID.flush()
    targetID.close()
    sourceID.close()

#--------------------------------------------------------------------------

def getDirectoryData(source, target, theLogger):
    '''
    Controls the file selection.
    '''
    try:
        os.mkdir(target)
    except Exception as errorCode:
        print('target errorCode="%s"' % str(errorCode))
        sys.exit(255)

    for dirpath, dirnames, filenames in os.walk(source):

        for name in filenames:

            theList = name.split('.')

            if len(theList) < 2:

                theRoot = theList[0]
                theExtension = ''
                theExt = ''

            else:

                theRoot = theList[0]
                theExtension = theList[1]
                theExt = '.%s' % theExtension

            # theLogger.debug(theExt, name)
            # if theExt.lower() in nonLineNumberedExtensions:
            if (theExt.lower() in lineNumberedExtensions):

                theLogger.debug('\tCopying: %s' % name)
                theSourceName = os.path.join(dirpath, name)
                theTargetName = os.path.join(target, name)
                copySourceFile(theSourceName, theTargetName, theLogger)

            if not (theExt.lower() in lineNumberedExtensions):

                theLogger.debug('\tStripping: %s' % name)
                theSourceName = os.path.join(dirpath, name)
                theTargetName = os.path.join(target, name)
                cleanupSourceLine(theSourceName, theTargetName, theLogger)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    def getOptions():
        '''
        Parse the command line and return a list of positional arguments
        and a dictionanary of keyword options.
        '''
        parser = OptionParser(usage='''\
        %prog [options]... -i input -o output

        Copies a directory tree from the specified source to destination.
        ''')

        parser.add_option("-i", "--input",
                            action="store",
                            dest="input",
                            default="./",
                            type="string",
                            help="topLevel directory [default = ./]")

        parser.add_option("-o", "--output",
                            action="store",
                            dest="output",
                            default="../published/",
                            type="string",
                            help="output directory ' + \
                            '[default = ../published]")

        (options, args) = parser.parse_args()
        print('getOptions: args=%s' % str(args))
        print('getOptions: options=%s' % str(options))
        if len(args) != 0:
            parser.print_help()
            sys.exit(1)

        return (args, options)

    #----------------------------------------------------------------------

    def theMainApplication():
        '''
        Display program name, version and date. Receive and validate
        command line options and arguments. Display help, error and
        status information. Initiate the file directory copy.
        '''
        print(__header__)

        (myArgs, myOptions) = getOptions()
        print('theMainApplication: myArgs=%s' % str(myArgs))
        print('theMainApplication: myOptions=%s' % str(myOptions))

        mySource = myOptions.input
        myDestination = myOptions.output

        theLogger = Logger.TsLogger(name='FileScanDetails.log',
                                    threshold=Logger.DEBUG)

        getDirectoryData(mySource,
                         myDestination,
                         theLogger)

##        getDirectoryData('../Sample Source Files',
##                         '../published/',
##                         theLogger)
##        getDirectoryData('../tool ge',
##                         '../published/',
##                         theLogger)
##        getDirectoryData('./',
##                         '../published/',
##                         theLogger)

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

        enableDefaultCommandLineParser=False,

        logs=[],

        runTimeEntryPoint=prototype)

    myApp.Wrapper()
