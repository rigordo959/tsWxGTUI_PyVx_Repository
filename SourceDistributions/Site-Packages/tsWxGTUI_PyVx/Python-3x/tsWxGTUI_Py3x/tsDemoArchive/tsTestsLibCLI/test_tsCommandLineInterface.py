#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:00:36 AM rsg>"
__doc__ = '''
test_tsCommandLineInterface.py - Application program to
demonstrate the features of the tsCommandLineInterface class.
'''
#################################################################
#
# File: test_tsCommandLineInterface.py
#
# Purpose:
#
#    Application program to demonstrate the features of the
#    tsCommandLineInterface class.
#
# Usage (example):
#
#     ## Reference Module Methods
#     python test_tsCommandLineInterface.py
#
# Methods:
#
# ToDo:
#   1. TBD.
#
# Modifications:
#
#################################################################

__title__     = 'test_tsCommandLineInterface'
__version__   = '2.0.0'
__date__      = '05/24/2013'
__authors__   = 'Richard S. Gordon & Frederick A. Kier'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.'
 
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

#------------------------------------------------------------------------

from optparse import OptionParser
import os.path
import sys
import traceback

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py3x.tsLibCLI import tsCommandLineInterface as tsCLI
from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
# from tsWxGTUI_Py3x.tsLibCLI import tsLogger as Logger
# from tsWxGTUI_Py3x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

##    def getOptions():
##        '''
##        Parse the command line and return a list of positional arguments
##        and a dictionanary of keyword options.

##        NOTE: Requirement is an inappropriate, oversimplification.
##              Invoking argparse or optparse (deprecated with Python 2.7.0)
##              do not produce equivalent output without substantial post
##              processing that has not yet been created. This may explain
##              inability to migrate use of tsApplication to tsCommandLineEnv
##              or to tsWxMultiFrameEnv.
##        '''
##        parser = OptionParser(usage='''\
##        %prog [options]...

##        Capture current hardware and software information
##        about the run time environment for the user process.
##        ''')

##        (options, args) = parser.parse_args()
##        if len(args) != 0:
##            parser.print_help()
##            sys.exit(1)

##        return (args, options)

    def theMainApplication(*args, **kw):

        print(__header__)

        myCLI = tsCLI.CommandLineInterface()

        answer = myCLI.multiFieldInput(
            'single field; default format? ', indent=4, debug=True)
        print('  answer type = %s; answer= "%s"' % (type(answer), answer))
        print('\n\n')

        fmt = '%s,%f,%d'
        answer = myCLI.multiFieldInput(
            'three fields; format=%s? ' % fmt, fmt, indent=4, debug=True)
        print('  answer type = %s; answer= "%s"' % (type(answer), answer))
        print('\n\n')

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:

        theApplication = tsAPP.TsApplication(
                buildTitle=__title__,
                buildVersion=__version__,
                buildDate=__date__,
                buildAuthors=__authors__,
                buildCopyright=__copyright__,
                buildLicense=__license__,
                buildCredits=__credits__,
                buildTitleVersionDate=mainTitleVersionDate,
                buildHeader=__header__,
                # getOptions=getOptions,
                runTimeTitle='main',
                logs=[],
                runTimeEntryPoint=theMainApplication)

        theApplication.runMainApplication()

    except Exception as applicationError:
        if isinstance(applicationError, tse.TsExceptions):
            msg = str(applicationError).replace("'", "")
            tse.displayError(applicationError)
            exitStatus = applicationError.exitCode
        else:
            msg = None
            sys.stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

    if msg == tse.NO_ERROR:
        sys.stdout.write(msg + '\n')
    elif msg is not None:
        sys.stderr.write(msg + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)
