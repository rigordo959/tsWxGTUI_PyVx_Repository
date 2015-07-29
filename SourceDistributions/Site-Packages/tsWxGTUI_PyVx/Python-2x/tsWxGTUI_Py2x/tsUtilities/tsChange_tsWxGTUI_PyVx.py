#! /usr/bin/env python
#"Time-stamp: <03/29/2015  6:05:47 AM rsg>"
'''
tsChange_tsWxGTUI_PyVx.py - Tool to generate a directory of
installable source files. It transforms the tsWxGTUI_PyVx
import identifier created by merging tsWxGTUI_Py2x changes
into a previous tsWxGTUI_Py3x.
'''
#################################################################
#
# File: tsChange_tsWxGTUI_PyVx.py
#
# Purpose:
#
#     Tool to generate a directory of installable source files.
#     It transforms the tsWxGTUI_PyVx import identifier created by
#     merging tsWxGTUI_Py2x changes into a previous tsWxGTUI_Py3x.
#
# Limitations:
#
#    Transforms only files who's name ends with '.py'.
#
# Notes:
#
#    None
#
# Usage (examples):
#
#    python tsChange_tsWxGTUI_PyVx.py \
#           -d sourcePath -o targetPath -n noticePath
#
# Methods:
#
#    None
#
# ToDo:
#
#    None
#
# Modifications:
#
#    2015/03/29 rsg Initial version.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsChange_tsWxGTUI_PyVx.py'

__version__   = '0/0.0'
__date__      = '03/29/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2015 ' + \
                '%s. All rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = ''
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

import os
from optparse import OptionParser
import sys

try:
    import tsLibraries
except:
    pass

import tsApplication as tsAPP
import tsExceptions as tse

#--------------------------------------------------------------------------

myOptions = None
 
if __name__ == '__main__':

    def replaceMacros(inputName, outputName, noticeDirectory):
        '''
        It transforms the tsWxGTUI_PyVx import identifier created by
	merging tsWxGTUI_Py2x changes into a previous tsWxGTUI_Py3x.
        '''
        oldVersion = 'from tsWxGTUI_Py2x.'
        newVersion = 'from tsWxGTUI_Py3x.'
        try:
            inputFile = open(inputName, 'r')
            outputFile = open(outputName, 'w')
        except:
            if os.path.islink(inputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
		    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' \
		    % (inputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
		    '  *** WARNING: Unknown Access Issue with\n    %s\n' \
		    % inputName)

        changed = False
        try:
            for line in inputFile:
            ##    print line
                if str(line).find(oldVersion) > -1:
                    changed = True
                    outputFile.write('%s' % line.replace(oldVersion,
                                                         newVersion))
                else:
                    outputFile.write('%s' % line)
        except:
            if os.path.islink(inputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
		    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' \
		    % (inputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
		    '  *** WARNING: Unknown Access Issue with\n    %s\n' \
		    % inputName)

        return changed

    def getOptions():
        '''
        Create class variables for each command line option.
        '''
        #global parser
        parser = OptionParser(usage='''\
        %prog [options]...

        It transforms the tsWxGTUI_PyVx import identifier created by
	merging tsWxGTUI_Py2x changes into a previous tsWxGTUI_Py3x.
        '''
        )

        parser.add_option("-d", "--directory",
                            action="store",
                            dest="inputDirectory",
                            default="./",
                            type="string",
                            help="topLevel directory [default = ./]")

        parser.add_option("-o", "--output",
                            action="store",
                            dest="outputDirectory",
                            default="../published",
                            type="string",
                            help="output directory [default = ../published]")

        parser.add_option("-n", "--notices",
                            action="store",
                            dest="noticeDirectory",
                            default="../notices",
                            type="string",
                            help="notice directory [default = ../notices]")

        parser.add_option("-v", "--verbose",
                            action="store_true",
                            dest="verbose",
                            default=False,
                            help="print status messages to stdout [default = False]")

        (options, args) = parser.parse_args()
        if len(args) != 0:
            parser.print_help()
            sys.exit(1)

        return (options, args)

    def getDirectoryData(inputDirectory, outputDirectory, noticeDirectory):
        '''
        Scan directory for files to be published.
        '''
        try:
            os.mkdir(outputDirectory)
        except OSError:
            pass

        sourceCodeExtension = '.py'
        for dirpath, dirnames, filenames in os.walk(inputDirectory):
            if dirnames is None:
                pass
            indent = dirpath.count(os.sep)
            header = 'Directory: %s' % dirpath
            print('\n%s%s' % ('    ' * indent, header))
            print('%s%s\n' % ('    ' * indent, '-' * len(header)))
            for name in filenames:
                if name.lower().endswith(sourceCodeExtension.lower()):
                    inputName = os.path.join(dirpath, name)
                    outputName = os.path.join(dirpath, outputDirectory, name)
                    changed = replaceMacros(inputName,
                                            outputName,
                                            noticeDirectory)
                    if changed:
                        print(' CHANGED', name)
                    else:
                        print('        ', name)

    def theMainApplication():
        '''
        Display program name, version and date.

	Receive and validate command line options and arguments.

	Display help, error and status information. Initiate
        the file directory copy.
        '''
        print(__header__)

        (myOptions, myArgs) = getOptions()

        getDirectoryData(myOptions.inputDirectory,
                         myOptions.outputDirectory,
                         myOptions.noticeDirectory)

 
    theApplication = tsAPP.TsApplication(
        header=__header__,
        main=theMainApplication,
        mainTitleVersionDate=mainTitleVersionDate,
        title=__title__,
        version=__version__,
        date=__date__)

    theApplication.runMain()
