#! /usr/bin/env python
#"Time-stamp: <02/23/2015  5:37:05 AM rsg>"
__doc__ = '''
test_tsSysCommands.py - Test application for tsSysCommands.
'''
#################################################################
#
# File: test_tsSysCommands.py
#
# Purpose:
#
#     Test application for tsSysCommands
#
# Limitations:
#
# Usage: test_tsSysCommands.py [options]
#
#     Options:
#       -h, --help            show this help message and exit
#       -c COMMAND, --command=COMMAND
#                             command [default = None]
#       -V, --Verbose         print status messages to stdout
#                             [default = False]
#
# Notes:
#
# Modifications:
#
#     2014/04/14 rsg Changed case from -v / --verbose to
#                    -V / --Verbose in order to be somewhat
#                    compatible with tsOperatorSettingsParser.
#
# ToDo:
#
#     2014/04/14 rsg Replace optparse with variant of
#                    tsOperatorSettingsParser. Add support
#                    for -a / --about and -v / --version.
#
#     2014/04/14 rsg Replace tsApplication with tsCommandLineEnv.
#
#################################################################

__title__     = 'test_tsSysCommands.py'

__version__   = '2.1.0'
__date__      = '04/14/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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

#--------------------------------------------------------------------------

import os
import sys
import time
from optparse import OptionParser

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsApplication as tsAPP
    import tsExceptions as tse
    import tsLogger as Logger
    from tsSysCommands import TsSysCommands

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

if __name__ == "__main__":

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
        #global parser

        parser = OptionParser()
        parser.add_option("-c", "--command",
                            action="store",
                            dest="command",
                            default=None,
                            type="string",
                            help="command [default = None]")

        parser.add_option("-V", "--Verbose",
                            action="store_true",
                            dest="verbose",
                            default=False,
                            help="print status messages to stdout [default = False]")

        (args, options) = parser.parse_args()
        return (args, options)
 
    print(__header__)

    (myOptions, myArgs) = getOptions()
 
    exitStatus = 0
    msg = 'No Errors'

    if myOptions.command == 'getstatusoutput':
        TsSysCommands.tsGetStatusOutput(myArgs[0])
    elif myOptions.command == 'getoutput':
        TsSysCommands.tsGetOutput(myArgs[0])
    elif myOptions.command == 'getstatus':
        TsSysCommands.tsGetStatus(myArgs[0])

##    command = 'python tsPlatformQuery.py'
    command = 'stty size' #'ping 10.0.160.100'
##    command = 'tput cols' #'ping 10.0.160.100'
##    command = 'tput lines' #'ping 10.0.160.100'
    print(command)

    ##print TsSysCommands.tsCall(['ls','-la'])
##    TsSysCommands.tsCall(command.split(' '),
##                         bufsize=0,
##                         executable=None,
##                         stdin=None,
##                         stdout=None,
##                         stderr=None,
##                         preexec_fn=None,
##                         close_fds=False,
##                         shell=False,
##                         cwd=None,
##                         env=None,
##                         universal_newlines=True,
##                         startupinfo=None,
##                         creationflags=0)
##    TsSysCommands.tsCheckCall(command.split(' '),
##                              bufsize=0,
##                              executable=None,
##                              stdin=None,
##                              stdout=None,
##                              stderr=None,
##                              preexec_fn=None,
##                              close_fds=False,
##                              shell=False,
##                              cwd=None,
##                              env=None,
##                              universal_newlines=True,
##                              startupinfo=None,
##                              creationflags=0)
    TsSysCommands.tsCheckCall(command.split(' '))

    if msg == 'No Errors':
        sys.stdout.write(msg)
    else:
        sys.stderr.write(msg.replace("'", ""))
 
    sys.exit(exitStatus)
