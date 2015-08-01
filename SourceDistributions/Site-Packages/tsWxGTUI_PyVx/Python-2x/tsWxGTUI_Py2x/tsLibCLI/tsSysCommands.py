#! /usr/bin/env python
#"Time-stamp: <03/28/2015  2:16:46 AM rsg>"
'''
tsSysCommands.py - Class definition and methods for issuing
shell commands to and receiving responses from the host
operating system.
'''
#################################################################
#
# File: tsSysCommands.py
#
# Purpose:
#
#     Class definition and methods for issuing shell commands
#     to and receiving responses from the host operating system.
#
# Limitations:
#
#     None
#
# Usage (examples):
#
#     python tsSysCommands
#
# Notes:
#
#     None
#
# Modifications:
#
#     2013/09/18 rsg Removed references to the now deprecated
#                    command module. Substituted the code from
#                    the Python-3.x version which had already
#                    substituted the appropriate subprocess
#                    module references.
#
# ToDo:
#
#     None
#
#################################################################

__title__     = 'tsSysCommands.py'

__version__   = '2.1.0'
__date__      = '09/18/2013'
__authors__   = 'Richard S. Gordon'
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

#--------------------------------------------------------------------------

from optparse import OptionParser
import os
import os.path
import subprocess
import sys

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

CommandLineEnvWrapperEnable = True

tsrpu = tsReportUtilities.TsReportUtilities

#---------------------------------------------------------------------------

class TsSysCommands(object):
    '''
    This class wraps the Python subprocess module which allows you to spawn
    new processes, connect to their input/output/error pipes, and obtain
    their return codes.
    '''

    #----------------------------------------------------------------------

    @staticmethod
    def tsGetStatusOutput(cmd):
        '''
        Execute the string cmd in a shell with os.popen() and return a
        2-tuple (status, output). cmd is actually run as { cmd ; } 2>&1,
        so that the returned output will contain output or error messages.
        A trailing newline is stripped from the output. The exit status
        for the command can be interpreted according to the rules for
        the C function wait().
        '''
        try:
            return subprocess.getstatusoutput(cmd)
        except:
            return None
##            raise tse.UserInterfaceException(
##                tse.COMMAND_LINE_OPERATION_NOT_VALID,
##                'Command: "%s"' % cmd)

    #----------------------------------------------------------------------

    @staticmethod
    def tsGetOutput(theCmd):
        '''
        Like getstatusoutput(), except the exit status is ignored and the
        return value is a string containing the command output.
        '''
        try:
            return subprocess.getoutput(theCmd)
        except:
            return None
##            raise tse.UserInterfaceException(
##                tse.COMMAND_LINE_OPERATION_NOT_VALID,
##                'Command: "%s"' % theCmd)

    #----------------------------------------------------------------------

    @staticmethod
    def tsGetStatus(theFile):
        '''
        Return the output of "ls -ld theFile" as a string. This
        function uses the getoutput() function, and properly
        escapes backslashes and dollar signs in the argument.
        '''
        try:
            return subprocess.getstatus(theFile)
        except:
            return None
##            raise tse.UserInterfaceException(
##                tse.COMMAND_LINE_OPERATION_NOT_VALID,
##                'Command: "ls -ld %s"' % theFile)

    #----------------------------------------------------------------------

    @staticmethod
    def tsCall(args,
               bufsize=0,
               executable=None,
               stdin=None,
               stdout=None,
               stderr=None,
               preexec_fn=None,
               close_fds=False,
               shell=False,
               cwd=None,
               env=None,
               universal_newlines=False,
               startupinfo=None,
               creationflags=0):
        '''
        Run command with arguments. Wait for command to complete,
        then return the returncode attribute.

        The arguments are the same as for the Popen constructor.

        Example: retcode = call(["ls", "-l"])
        '''
 
        try:
            print('tsCall')
            return subprocess.call(args,
                                   bufsize=bufsize,
                                   executable=executable,
                                   stdin=stdin,
                                   stdout=stdout,
                                   stderr=stderr,
                                   preexec_fn=preexec_fn,
                                   close_fds=close_fds,
                                   shell=shell,
                                   cwd=cwd,
                                   env=env,
                                   universal_newlines=universal_newlines,
                                   startupinfo=startupinfo,
                                   creationflags=creationflags)
        except OSError, e:
            raise tse.ProgramException(tse.OS_ERROR,
                                       'Command: "%s"' % e)
        except ValueError, e:
            raise tse.UserInterfaceException(
                tse.COMMAND_LINE_OPERATION_NOT_VALID,
                'Command: "%s"' % e)

    #----------------------------------------------------------------------

    @staticmethod
    def tsCheckCall(args,
                    bufsize=0,
                    executable=None,
                    stdin=None,
                    stdout=None,
                    stderr=None,
                    preexec_fn=None,
                    close_fds=False,
                    shell=False,
                    cwd=None,
                    env=None,
                    universal_newlines=False,
                    startupinfo=None,
                    creationflags=0):
        '''
        Run command with arguments. Wait for command to complete.
        If the exit code was zero then return, otherwise raise
        CalledProcessError. The CalledProcessError object will
        have the return code in the returncode attribute.

        The arguments are the same as for the Popen constructor.

        Example: check_call(["ls", "-l"])
        '''
        try:
            print('tsCheckCall')
            subprocess.check_call(args,
                                  bufsize=bufsize,
                                  executable=executable,
                                  stdin=stdin,
                                  stdout=stdout,
                                  stderr=stderr,
                                  preexec_fn=preexec_fn,
                                  close_fds=close_fds,
                                  shell=shell,
                                  cwd=cwd,
                                  env=env,
                                  universal_newlines=universal_newlines,
                                  startupinfo=startupinfo,
                                  creationflags=creationflags)
        except TypeError, e:
            raise tse.UserInterfaceException(
                tse.COMMAND_LINE_OPERATION_NOT_VALID,
                'Command: "%s"' % e)
        except subprocess.CalledProcessError, e:
            raise tse.UserInterfaceException(
                tse.COMMAND_LINE_OPERATION_NOT_VALID,
                'Command: "%s"' % e)
        except KeyboardInterrupt:
            raise tse.UserInterfaceException(
                tse.ABORT_BY_OPERATOR,
                '')

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
