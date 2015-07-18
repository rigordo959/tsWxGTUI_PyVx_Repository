#! /usr/bin/env python
#"Time-stamp: <07/18/2015  5:50:35 AM rsg>"
'''
tsPlatformRunTimeEnvironment - Class to capture current
hardware, software and network information about the run time
environment for the user process.
'''
#################################################################
#
# File: tsPlatformRunTimeEnvironment.py
#
# Purpose:
#
#     Class to capture current hardware, software and network
#     information about the run time environment for the user
#     process.
#
# Limitations:
#
#     1. Host processor hardware support includes various
#        releases of Pentium, PowerPC, SPARC.
#
#     2. Host operating system software support includes
#        various releases of Cygwin, Linux ('SuSE', 'debian',
#        'redhat', 'mandrake'), Mac OS ('X'), Unix ('Solaris')
#        and Windows ('98', '2000', 'XP', 'Vista').
#
#     3. Host virtual machine software support includes
#        various releases of Java and Python.
#
# Usage (example):
#
#     # Import Example
#     from tsPlatformRunTimeEnvironment import PlatformRunTimeEnvironment
#
#     # Configuration Example
#     myOutputPath = os.path.abspath('./PlatformRunTimeEnvironment.txt')
#
#     # Data Input Example
#     myRunTimeEnvironment = PlatformRunTimeEnvironment()
#
#     # Data Output Example
#     myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)
#
# Classes
#
#     PlatformRunTimeEnvironment
#
# Methods:
#
#     PlatformRunTimeEnvironment.__init__
#     PlatformRunTimeEnvironment.logPlatformInfo
#     PlatformRunTimeEnvironment.tsGetHostCentralProcessingUnit
#     PlatformRunTimeEnvironment.tsGetHostConsoleDisplaySize
#     PlatformRunTimeEnvironment.tsGetHostOperatingSystem
#     PlatformRunTimeEnvironment.tsGetJavaPlatform
#     PlatformRunTimeEnvironment.tsGetLinuxPlatform
#     PlatformRunTimeEnvironment.tsGetMacPlatform
#     PlatformRunTimeEnvironment.tsGetNetworkIdentification
#     PlatformRunTimeEnvironment.tsGetPlatformRunTimeEnvironment
#     PlatformRunTimeEnvironment.tsGetProcessParameters
#     PlatformRunTimeEnvironment.tsGetPythonPlatform
#     PlatformRunTimeEnvironment.tsGetWindowsPlatform
#     PlatformRunTimeEnvironment.tsInterpretMissingPlatformInfo
#
# Notes:
#
#    None
#
# Modifications:
#
#    2013/01/27 rsg Modified tsGetHostCentralProcessingUnit.
#                   Added test of the "64-bitness" of the current
#                   Python interpreter. On Mac OS X (and perhaps
#                   other platforms) executble files may be
#                   universal files containing multiple architectures.
#
#    2013/10/19 rsg Added tsGetHostConsoleDisplaySize method.
#
#    2014/02/14 rsg Modified tsGetProcessParameters to handle
#                   'getlogin = <%s>' % os.getlogin() exception
#                   on Ubuntu linux via
#                   'getlogin = <%s>' % pwd.getpwuid(os.getuid())[0].
#
#    2014/02/19 rsg Updated the list of methods.
#
#    2014/05/12 rsg Conditionalize python.platform dependancies.
#
#    2014/05/12 rsg Conditionalize python.platform.linux_distribution
#                   dependancy.
#
#    2014/05/12 rsg Conditionalize sys.maxsize dependancy.
#
#    2014/05/26 rsg Modified tsGetProcessParameters. Substituted
#                   "try except" for "if self.theSystem != 'Windows'"
#                   in order to support back port to Python 2.4.4.
#
#    2014/07/17 rsg Modified tsGetNetworkIdentification to recover
#                   from socket.gethostname() error first encountered
#                   on newly introduced Linux patform, OpenSUSE 13.1.
#
#    2015/03/21 rsg Added import of tsGistGetTerminalSize to
#                   eliminate need for copying code.
#
# ToDo:
#
#    1. _getNetworkIdentification - Cannot explain missing Mac
#       OS X information.
#
#    2. _getMacOperatingSystem - Cannot explain missing Mac
#       OS X information.
#
#    2014/05/26 rsg Resolve outdated import mechanisms that
#                   preclude back porting to Python 2.3.4.
#
#
#################################################################

__title__     = 'tsPlatformRunTimeEnvironment.py'
__version__   = '2.6.0'
__date__      = '03/21/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007' + \
                '\n\n\t  terminalsize (https://gist.github.com/' + \
                'jtriley/1108174) Features: ' + \
                '\n\t  Copyright (c) 2011 Justin T. Riley.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007' + \
                '\n\n\t  Python Platform & Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' + \
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

import os
import os.path

try:

    # Platform introduced with Python 2.3
    import platform
    platformAvailable = True

except Exception as errorCode:

    # Platform NOT introduced until Python 2.3
    platformAvailable = False

import socket
import sys
import textwrap as TextWrapper
import time
import traceback
from optparse import OptionParser

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    import tsLogger as Logger
    from tsGistGetTerminalSize import * 
    from tsReportUtilities import TsReportUtilities as tsrpu

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#-----------------------------------------------------------------------

class PlatformRunTimeEnvironment(object):
    '''
    Class to capture current hardware, software and network
    information about the run time environment for the user
    process.
    '''

    def __init__(self):
        '''
        Initialize the class. Return standard runtime environment.
        '''

        self.theArchitecture = platform.architecture(executable=sys.executable,
                                                     bits='',
                                                     linkage='')
        self.theMachine = platform.machine()
        self.theNode = platform.node()

        if platformAvailable:
            # Introduced with Python 2.3
            self.thePlatform = platform.platform(aliased=1, terse=0)
        else:
            # NOT Introduced until Python 2.3
            self.thePlatform = ''

        if platformAvailable:
            try:
                # Introduced with Python 2.6
                self.thePython_branch = platform.python_branch()
                self.thePython_implementation = \
                                              platform.python_implementation()
                self.thePython_revision = platform.python_revision()
            except Exception as errorCode:
                # NOT Introduced until Python 2.6
                self.thePython_branch = ''
                self.thePython_implementation = ''
                self.thePython_revision = ''
        else:
            # NOT Introduced until Python 2.6
            self.thePython_branch = ''
            self.thePython_implementation = ''
            self.thePython_revision = ''

        self.theProcessor = platform.processor()
        self.thePython_build = platform.python_build()
        self.thePython_compiler = platform.python_compiler()
        self.thePython_version = platform.python_version()
        self.thePython_version_tuple = platform.python_version_tuple()
        self.theRelease = platform.release()
        self.theSystem = platform.system()
        self.theUname = platform.uname()
        self.theVersion = platform.version()

        self.theSystem_alias = platform.system_alias(self.theSystem,
                                                     self.theRelease,
                                                     self.theVersion)

    #-------------------------------------------------------------------

    def tsGetNetworkIdentification(self, theInfo):
        '''
        Return network host information including hostname, list of aliases
        and list of IP addresses.
        '''
        try:
            (socketHostname,
             socketAliaslist,
             socketIpaddrlist) = socket.gethostbyaddr(socket.gethostname())
        except socket.herror:
            socketHostname = socket.gethostname()
            socketAliaslist = []
            socketIpaddrlist = []
        except Exception as errorCode:
            socketHostname = ''
            socketAliaslist = []
            socketIpaddrlist = []
            fmt1 = 'tsPlatformRunTimeEnvironment.' + \
                   'tsGetNetworkIdentification: '
            fmt2 = 'errorCode=%s; ' % str(errorCode)
            fmt3 = 'socketHostname=<%s>; ' % socketHostname
            fmt4 = 'socketAliaslist=<%s>; ' % socketAliaslist
            fmt5 = 'socketIpaddrlist=<%s>' % socketIpaddrlist
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            print('ERROR:' + msg) 

        theInfo += ['\n']
        theInfo += ['  Network Identification']
        theInfo += ['  ----------------------']
        theInfo += ['         hostname = <%s>' % socketHostname]
        theInfo += ['        aliaslist = <%s>' % socketAliaslist]
        theInfo += ['       ipaddrlist = <%s>' % socketIpaddrlist]

    #-------------------------------------------------------------------

    def tsGetHostCentralProcessingUnit(self, theInfo):
        '''
        Return host CPU information.
        '''
        bits, linkage = self.theArchitecture
        try:
            # Introduced with Python 2.6
            self.is_64bits = sys.maxsize > 2**32
        except Exception as errorCode:
            # NOT Introduced until Python 2.6
            self.is_64bits = False

        theInfo += ['\n']
        theInfo += ['  Host Central Processing Unit']
        theInfo += ['  ----------------------------']
        theInfo += ['          machine = <%s>' % self.theMachine]
        theInfo += ['        processor = <%s>' % self.theProcessor]
        if self.is_64bits:
            theInfo += [
                '     architecture = <%s> bits (sys.maxsize); <%s> linkage' % \
                (64, linkage)]
        else:
            theInfo += [
                '     architecture = <%s> bits; <%s> linkage' % \
                (bits.replace('bit', ''), linkage)]
        theInfo += ['        byteorder = <%s>' % sys.byteorder]

    #-------------------------------------------------------------------

    def tsGetHostConsoleDisplaySize(self, theInfo):
        '''
        Return console window size:
            - width  = number of characters / line
            - height = number of lines / display
        '''
        try:

            sizex, sizey = get_terminal_size()

        except Exception as tsGetHostConsoleDisplaySizeErrorCode:

            sizex = 80
            sizey = 25

            fmt1 = 'Assuming tsGetHostConsoleDisplaySize: '
            fmt2 = '\n\tsizex=%d; \n' % sizex
            fmt3 = '\n\tsizey=%d; \n' % sizey
            fmt4 = '\n\terrorCode: %s' % tsGetHostConsoleDisplaySizeErrorCode
            msg = fmt1 + fmt2 + fmt3 + fmt4
            print(msg)

        theInfo += ['\n']
        theInfo += ['  Host Console Display Size']
        theInfo += ['  -------------------------']
        theInfo += ['  characters/line = <%s>' % sizex]
        theInfo += ['    lines/display = <%s>' % sizey]

    #-------------------------------------------------------------------

    def tsGetHostOperatingSystem(self, theInfo):
        '''
        Return host OS information
        '''
        theInfo += ['\n']
        theInfo += ['  Host Operating System']
        theInfo += ['  ---------------------']
        theInfo += ['              api = <%s>' % os.name]
        theInfo += ['           system = <%s>' % self.theSystem]
        theInfo += ['          release = <%s>' % self.theRelease]
        theInfo += ['          version = <%s>' % self.theVersion]

    #-------------------------------------------------------------------

    def tsGetPythonPlatform(self, theInfo):
        '''
        Return Python VM information.
        '''
        theInfo += ['\n']
        theInfo += ['  Python Platform']
        theInfo += ['  ---------------']
        theInfo += ['           branch = <%s>' % self.thePython_branch]
        theInfo += ['            build = <%s> number; <%s> date' % \
                    self.thePython_build]
        theInfo += ['         compiler = <%s>' % self.thePython_compiler]
        theInfo += ['   implementation = <%s>' % self.thePython_implementation]
        theInfo += ['         revision = <%s>' % self.thePython_revision]
        theInfo += ['          version = <%s>' % self.thePython_version]
##        theInfo += ['    version_tuple = <%s>' % str(
##            self.thePython_version_tuple)]


    #-------------------------------------------------------------------

    def tsGetJavaPlatform(self, theInfo):
        '''
        Return Java specific runtime environment.
        '''
        (release,
         vendor,
         vminfo,
         osinfo) = platform.java_ver(release='',
                                     vendor='',
                                     vminfo=('','',''),
                                     osinfo=('','',''))
 
        (vm_name, vm_release, vm_vendor) = vminfo

        (os_name, os_version, os_arch)= osinfo

        if release != '' or \
           vendor != '' or \
           vm_name != '' or \
           vm_release != '' or \
           vm_vendor != '' or \
           os_name != '' or \
           os_version != '' or \
           os_arch != '':

            dataAvailable = True
        else:
            dataAvailable = False

        if dataAvailable:
            theInfo += ['\n']
            theInfo += ['  Java Platform']
            theInfo += ['  -------------']
            theInfo += ['          release = <%s>' % release]
            theInfo += ['           vendor = <%s>' % vendor]
            theInfo += ['          vm_name = <%s>' % vm_name]
            theInfo += ['        vm_vendor = <%s>' % vm_vendor]
            theInfo += ['       vm_release = <%s>' % vm_release]
            theInfo += ['          os_arch = <%s>' % os_arch]
            theInfo += ['          os_name = <%s>' % os_name]
            theInfo += ['       os_version = <%s>' % os_version]

    #-------------------------------------------------------------------

    def tsGetMacPlatform(self,
                         theInfo):
        '''
        Return Mac OS specific runtime environment.
        '''
        (release,
         versioninfo,
         machine) = platform.mac_ver(release='',
                                     versioninfo=('','',''),
                                     machine='')

        (version, dev_stage, non_release_version) = versioninfo

        if release != '' or \
            version != '' or \
            dev_stage != '' or \
            non_release_version != '' or \
            machine != '':
 
            dataAvailable = True
        else:
            dataAvailable = False

        if dataAvailable:
            theInfo += ['\n']
            theInfo += ['  Mac Platform']
            theInfo += ['  ------------']
            theInfo += ['          release = <%s>' % release]
            theInfo += ['          version = <%s>' % version]
            theInfo += ['        dev_stage = <%s>' % dev_stage]
            theInfo += ['  non-release ver = <%s>' % non_release_version]
            theInfo += ['          machine = <%s>' % machine]

    #-------------------------------------------------------------------

    def tsGetLinuxPlatform(self,
                           theInfo):
        '''
        Return Linux specific runtime environment.
        '''
        try:
            # Introduced with Python 2.6
            (distname,
             version,
             unixId) = platform.linux_distribution(
                 distname='',
                 version='',
                 id='',
                 supported_dists=('SuSE',
                                  'debian',
                                  'redhat',
                                  'mandrake'),
                 full_distribution_name=1)
        except Exception as errorCode:
            # NOT Introduced until Python 2.6
            (distname,
             version,
             unixId) = platform.dist(
                 distname='',
                 version='',
                 id='',
                 supported_dists=('SuSE',
                                  'debian',
                                  'redhat',
                                  'mandrake'))
        try:
            (lib,
             libVersion) = platform.libc_ver(executable=sys.executable,
                                             lib='',
                                             version='',
                                             chunksize=2048)
        except IOError:
            lib = ''
            libVersion = ''

        if distname != '' or \
           version != '' or \
           unixId != '' or \
           lib != '' or \
           libVersion != '':

            dataAvailable = True
        else:
            dataAvailable = False

        if dataAvailable:
            theInfo += ['\n']
            theInfo += ['  Unix Operating System']
            theInfo += ['  ---------------------']
            theInfo += ['         distname = <%s>' % distname]
            theInfo += ['          version = <%s>' % version]
            theInfo += ['               id = <%s>' % unixId]
            theInfo += ['              lib = <%s>' % lib]
            theInfo += ['      lib version = <%s>' % libVersion]

    #-------------------------------------------------------------------

    def tsGetWindowsPlatform(self,
                                    theInfo):
        '''
        Return Microsoft Windows specific runtime environment.
        '''
        (release,
         version,
         csd,
         ptype) = platform.win32_ver(release='',
                                     version='',
                                     csd='',
                                     ptype='')

        if release != '' or \
           version != '' or \
           csd != '' or \
           ptype != '':
 
            dataAvailable = True
        else:
            dataAvailable = False

        if dataAvailable:
            theInfo += ['\n']
            theInfo += ['  Windows Platform']
            theInfo += ['  ----------------']
            theInfo += ['          release = <%s>' % release]
            theInfo += ['          version = <%s>' % version]
            theInfo += [' csd service pack = <%s>' % csd]
            theInfo += ['core & build type = <%s>' % ptype]

    #-------------------------------------------------------------------

    def tsGetProcessParameters(self, theInfo):
        '''
        '''
        pid = os.getpid()

        theInfo += ['\n']
        theInfo += ['  Process Parameters']
        theInfo += ['  ------------------']
        theInfo += ['              pid = <%d> / <0x%X>' % (pid, pid)]

##        if self.theSystem != 'Windows':
        try:
            # The following code supports Cygwin, Linux, Mac OS X and Unix.
            #
            # The platform.windows function only works if Mark Hammond's
            # win32all package is installed and (obviously) only runs
            # on Win32 compatible platforms.
            theInfo += ['          getppid = <%d> / <0x%X>' % (os.getppid(),
                                                               os.getppid())]
            theInfo += ['          getegid = <%s>' % os.getegid()]
            theInfo += ['          geteuid = <%s>' % os.geteuid()]
            theInfo += ['           getgid = <%s>' % os.getgid()]
            theInfo += ['        getgroups = <%s>' % os.getgroups()]
            theInfo += ['          getpgid = <%s>' % os.getpgid(pid)]
            theInfo += ['           getuid = <%s>' % os.getuid()]
            try:
                theInfo += ['         getlogin = <%s>' % os.getlogin()]
            except Exception as errorCode:
                self.logger.warning(
                    'tsPlatformRunTimeEnvironment.' + \
                    'tsGetProcessParameters: errorCode=%s' % str(errorCode))
                theInfo += ['         getlogin = <%s>' % (
                    pwd.getpwuid(os.getuid())[0])]
            theInfo += ['          ctermid = <%s>' % os.ctermid()]
        except Exception as errorCode:
            # Neither print function nor "from tsLogger import TsLogger"
            # are available in Python 2.3.4.
            pass

        theInfo += ['              cwd = <%s>' % os.getcwd()]

        environ = os.environ

        theInfo += ['\n']
        theInfo += ['  Environment Variables']
        theInfo += ['  ---------------------']
        keys = list(environ.keys())
        keyList = sorted(keys)
 
        keyWidth = 0
        for key in keyList:
            if len(key) > keyWidth:
                keyWidth = len(key)

        if len(keyList) == 0:
            theInfo += ['      environment = <>']
        else:
            for key in sorted(keys):
                theInfo += ['  %s = <%s>' % \
                            (key.rjust(keyWidth), environ[key])]


    #-------------------------------------------------------------------

    def tsGetPlatformRunTimeEnvironment(self):
        '''
        Build list of strings that describe the following standard runtime
        enviroment features: "Network Host", "Python Virtual Machine",
        "Host Operating System", "Host Central Processing Unit",
        "Process Parameters" with associated platform specific details.
        '''
        theInfo = []

        lines = __header__.split('\n')
        for line in lines:
            theInfo += [line]

        theBeginTitle = 'Begin Platform Run Time Environment'
        theEndTitle = 'End Platform Run Time Environment'
        theInfo += ['%s' % \
                    tsrpu.getSeparatorString(title=theBeginTitle,
                                             separatorCharacter='=',
                                             position=tsrpu.layout[
                                                 'TitleCenter'])]
 
        theInfo += ['\n']
        theInfo += ['  Reported %s' % \
                    tsrpu.getDateAndTimeString(time.time())]

        self.tsGetNetworkIdentification(theInfo)
        self.tsGetHostCentralProcessingUnit(theInfo)
        self.tsGetHostOperatingSystem(theInfo)
        self.tsGetHostConsoleDisplaySize(theInfo)
        self.tsGetPythonPlatform(theInfo)
        self.tsGetJavaPlatform(theInfo)
        self.tsGetMacPlatform(theInfo)
        self.tsGetLinuxPlatform(theInfo)
        self.tsGetWindowsPlatform(theInfo)
        self.tsGetProcessParameters(theInfo)

        theInfo += ['%s' % \
                    tsrpu.getSeparatorString(title=theEndTitle,
                                             separatorCharacter='=',
                                             position=tsrpu.layout[
                                                 'TitleCenter'])]

        return theInfo

    #-------------------------------------------------------------------

    def tsInterpretMissingPlatformInfo(self, platformInfo):
        '''
        Insert and return explanation of any empty platform information.
        '''
        interpretation = {
            "<''>": "<''> # NOTE: Value NOT available.", \
            \
            '<"">': '<""> # NOTE: Value NOT available.', \
            \
            '<>': '<> # NOTE: Value NOT available.', \
            \
            '<[]>': '<[]> # NOTE: List of Values NOT available.', \
            \
            '<{}>': '<{}> # NOTE: Dictionary of Key & Values NOT available.'}
        keys = list(interpretation.keys())
        for key in keys:
            platformInfo = platformInfo.replace(key, interpretation[key])
        return platformInfo

    #-------------------------------------------------------------------

    def logPlatformInfo(self, fileName='./PlatformRunTimeEnvironment.log'):
        '''
        Display list of strings that describe the runtime enviroment features.
        '''
        width = tsrpu.pageWidth - 2
 
##        theWrapper = TextWrapper(width=width - len(subsequent_indent),
##                                 expand_tabs=expand_tabs,
##                                 replace_whitespace=replace_whitespace,
##                                 initial_indent=initial_indent,
##                                 subsequent_indent=subsequent_indent,
##                                 fix_sentence_endings=fix_sentence_endings,
##                                 break_long_words=break_long_words)

        myInfo = self.tsGetPlatformRunTimeEnvironment()
        myLogger = open(fileName, 'w')

        for text in myInfo:
            newText = self.tsInterpretMissingPlatformInfo(text)
            paragraphs = newText.split('\n\n')
            for paragraph in paragraphs:
                if paragraph == '':
                    myLogger.write('\n')
                elif len(paragraph) < width:
                    myLogger.write(paragraph + '\n')
                else:
                    expand_tabs = False
                    replace_whitespace = True
                    fix_sentence_endings = False
                    break_long_words = True

                    initial_indent = ''
                    myIndent = paragraph.find('<')
                    if myIndent == -1:
                        subsequent_indent = ''
                    else:
                        subsequent_indent = ' ' * (myIndent + 1)
                    for aLine in TextWrapper.wrap(
                        paragraph,
                        width=width,
                        expand_tabs=expand_tabs,
                        replace_whitespace=replace_whitespace,
                        initial_indent=initial_indent,
                        subsequent_indent=subsequent_indent,
                        fix_sentence_endings=fix_sentence_endings,
                        break_long_words=break_long_words):
                        myLogger.write(aLine + '\n')

#-----------------------------------------------------------------------

if __name__ == '__main__':
    # Main program to demonstrate the expected operating scenario.

    print(__header__)

    exitStatus = 0
    msg = 'No Errors'
 
    try:
        myOutputPath = os.path.abspath('./PlatformRunTimeEnvironment.txt')
        myRunTimeEnvironment = PlatformRunTimeEnvironment()
        myRunTimeEnvironment.logPlatformInfo(fileName= myOutputPath)

        sys.stdout.write('Results are available in "%s".\n\n' % \
                         os.path.abspath(myOutputPath))

    except tse.InputOutputException as e:
        msg = str(e)
        exitStatus = e.exitCode
 
    except tse.ProgramException as e:
        msg = str(e)
        exitStatus = e.exitCode
 
    except Exception as e:
        msg = str(e)
        exitStatus = tse.INVALID_ERROR_CODE

    if msg == 'No Errors':
        sys.stdout.write(msg)
    else:
        sys.stderr.write(msg.replace("'", ""))
 
    sys.exit(exitStatus)
 
