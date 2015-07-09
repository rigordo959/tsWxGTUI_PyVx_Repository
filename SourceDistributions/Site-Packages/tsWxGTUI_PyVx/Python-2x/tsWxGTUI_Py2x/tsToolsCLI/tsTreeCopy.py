#! /usr/bin/env python
#"Time-stamp: <03/10/2015  4:06:42 AM rsg>"
'''
tsTreeCopy.py - Tool to copy the contents of a source directory
to a target directory.
'''
#################################################################
#
# File: tsTreeCopy.py
#
# Purpose:
#
#     Tool to copy the contents of a source directory to a
#     target directory.
#
# Limitations:
#
# Usage (example):
#
#    python tsTreeCopy.py -s -i source -o destination
#
# Modifications:
#
#   07/17/2007 rsg Replaced source and desitination (target)
#                  Options with Positional Arguments. Added
#                  symlink Option. Also output usage help upon
#                  detection of invalid command line.
#
# ToDo:
#
#################################################################

__title__     = 'tsTreeCopy.py'
__version__   = '2.0.0'
__date__      = '06/09/2013'
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

import sys
import os
import os.path
from optparse import OptionParser
import shutil

#--------------------------------------------------------------------------

import tsLibCLI

from tsLibCLI import tsExceptions as tse
from tsLibCLI import tsLogger as Logger
from tsLibCLI import tsCommandLineEnv

CommandLineEnv = tsCommandLineEnv.CommandLineEnv

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
                            default="../published",
                            type="string",
                            help="output directory [default = ../published]")

        parser.add_option("-s", "--symlinks",
                          action="store_true",
                          dest="symlinks",
                          default=False,
                          help="Copy symbolic links, if True, ' + \
                          'or contents of linked files, if False ' + \
                          '[default = False].")

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
        Display program name, version and date. Receive and validate command line
        options and arguments. Display help, error and status information. Initiate
        the file directory copy.
        '''
        print(__header__)

        (myArgs, myOptions) = getOptions()
        print('theMainApplication: myArgs=%s' % str(myArgs))
        print('theMainApplication: myOptions=%s' % str(myOptions))

        mySource = myOptions.input
        myDestination = myOptions.output

        symlinks = myOptions.symlinks

        exitStatus = 0
        exitMsg = 'No Errors'

        if mySource == '':
            exitMsg = 'COMMAND LINE ERROR: ' \
                      'No Source specified.'
            exitStatus = tse.INVALID_ERROR_CODE

        elif myDestination == '':
            exitMsg = 'COMMAND LINE ERROR: ' \
                      'No Destination specified.'
            exitStatus = tse.INVALID_ERROR_CODE

        elif myDestination == mySource:
            exitMsg = 'COMMAND LINE ERROR: ' \
                      'Cannot use Source "%s" also for Destination.' % \
                      mySource
            exitStatus = tse.INVALID_ERROR_CODE

        if exitStatus == 0:
            shutil.copytree(os.path.abspath(mySource),
                            os.path.abspath(myDestination),
                            symlinks)
        else:
            sys.stderr.write(exitMsg.replace("'", ""))
            sys.exit(exitStatus)

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
