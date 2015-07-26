#! /usr/bin/env python
#"Time-stamp: <04/04/2015  9:45:43 AM rsg>"
'''
test_tsWxDisplay.py - Application program to mimic some features
of the Graphical TextUser Interface.
'''
#################################################################
#
# File: test_tsWxDisplay.py
#
# Purpose:
#
#    Application program to report features of wx.Display.
#
# Limitations:
#
#    1) None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxDisplay.py
#
# Methods:
#
#    DummyLogger
#    DummyLogger.critical
#    DummyLogger.debug
#    DummyLogger.error
#    DummyLogger.info
#    DummyLogger.log
#    DummyLogger.warning
#    displayTest
#    displayTest.__init__
#    displayTest.exitTest
#    displayTest.getRunTimeTitle
#    displayTest.getRunTimeTitleVersionDate
#    displayTest.main
#    displayTest.prototype
#
# Modifications:
#
#    2013/12/24 rsg Updated to accomodate changes to tsApplication.
#
#    2013/12/25 rsg Modified displayTest class to examine and log
#                   various attribytes.
#
#    2013/12/27 rsg Modified displayTest class to examine and log
#                   color database.
#
#    2015/04/04 rsg Replaced "import tsWxGlobals as wx" by
#                   "import tsWx as wx" and made the associated
#                   Toolkit building block references.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'test_tsWxDisplay'
__version__   = '1.2.0'
__date__      = '04/01/2015'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

import os.path
import platform
import sys
import time
import traceback

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger
from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWx as wx

#--------------------------------------------------------------------------

WXPYTHON_EMULATION = True

__help__ = '''
This program shows the most basic wxPython application. It reports
information about the display.
'''

DEBUG = False

DebugKeyValueUndefined     = False
DebugSimulatedKeyErrorTrap = False
EnableOptionsGNU = True

theAssignedLogger = None

#---------------------------------------------------------------------------

class DummyLogger(object):
    '''
    The dummy log class. It is not needed when tsApplication establishes
    a fully funtional logger.
    '''
    def log(self, *args, **kw):
        pass
 
    def info(self, *args, **kw):
        pass
 
    def debug(self, *args, **kw):
        pass
 
    def warning(self, *args, **kw):
        pass
 
    def error(self, *args, **kw):
        pass
 
    def critical(self, *args, **kw):
        pass

class displayTest(object):
    '''
    Class to establish the application specific control components.
    '''
    def __init__(self, logger):
        '''
        Add our main entry point to kw
        Init tsApp
        '''
        theClass = 'displayTest'

        self.logger = logger

##        kw['main'] = self.main
##        tsAPP.TsApplication.__init__(self, *args, **kw)

        try:
            print('About to acess logger: %s' % str(self.logger))
##            self.logger = tsAPP.TsApplication.getLog(self)
        except AttributeError, e:
            print('AttributeError: %s' % str(e))
            self.logger = DummyLogger()

        self.logger.debug(
            'Begin %s (0x%X).' % (theClass, id(self)))

        try:
            self.theScreen = wx.GraphicalTextUserInterface(theClass)
            self.Display = wx.Display(self)
        except AttributeError:
            self.theScreen = None
##            self.theGeometry = wxRect(-1, -1, -1, -1)
##        self.logger.debug(
##            '  theGeometry: %s.' % str(self.theGeometry))

        self.main()

        self.logger.debug(
            'End %s (0x%X).' % (theClass, id(self)))

    def main(self):
        '''
        Get a wx App
        Build the communicate Frame
        Enter wx main loop
        '''
        print(__header__)

        myDisplay = wx.Display(self)

        try:
            theDisplayChangeMode = myDisplay.ChangeMode()
            self.logger.debug(
                'ChangeMode: %s' % str(theDisplayChangeMode))

            theDisplayClientArea = myDisplay.GetClientArea()
            self.logger.debug(
                'GetClientArea: %s' % str(theDisplayClientArea))

            theDisplayCount = myDisplay.GetCount()
            self.logger.debug(
                'GetCount: %s' % str(theDisplayCount))

            theDisplayCurrentMode = myDisplay.GetCurrentMode()
            self.logger.debug(
                'GetCurrentMode: %s' % str(theDisplayCurrentMode))

            theTopLeftPoint = (theDisplayClientArea.x,
                               theDisplayClientArea.y)
            theDisplayGetFromTopLeftPoint = myDisplay.GetFromPoint(
                theTopLeftPoint)
            self.logger.debug(
                'GetFromPoint (Top Left %s: 0 expected): %s' % (
                    str(theTopLeftPoint),
                    str(theDisplayGetFromTopLeftPoint)))

            theCenterPoint = (
                (theDisplayClientArea.x + theDisplayClientArea.width) // 2,
                (theDisplayClientArea.y + theDisplayClientArea.height) // 2)
            theDisplayGetFromCenterPoint = myDisplay.GetFromPoint(
                theCenterPoint)
            self.logger.debug(
                'GetFromPoint (Center %s: 0 expected): %s' % (
                    str(theCenterPoint),
                    str(theDisplayGetFromCenterPoint)))

            theBottomRightPoint = (
                (theDisplayClientArea.x + theDisplayClientArea.width),
                (theDisplayClientArea.y + theDisplayClientArea.height))
            theDisplayGetFromBottomRightPoint = myDisplay.GetFromPoint(
                theBottomRightPoint)
            self.logger.debug(
                'GetFromPoint (Bottom Right %s: 0 expected): %s' % (
                    str(theBottomRightPoint),
                    str(theDisplayGetFromBottomRightPoint)))

            theBeyondBottomRightPoint = (
                (theDisplayClientArea.x + theDisplayClientArea.width) + 1,
                (theDisplayClientArea.y + theDisplayClientArea.height) + 1)
            theDisplayGetFromBeyondBottomRightPoint = myDisplay.GetFromPoint(
                theBeyondBottomRightPoint)
            self.logger.debug(
                'GetFromPoint (Beyond Bottom Right %s: -1 expected): %s' % (
                    str(theBeyondBottomRightPoint),
                    str(theDisplayGetFromBeyondBottomRightPoint)))

            theBeyondTopLeftPoint = (
                (theDisplayClientArea.x - 1),
                (theDisplayClientArea.y - 1))
            theDisplayGetFromBeyondTopLeftPoint = myDisplay.GetFromPoint(
                theBeyondTopLeftPoint)
            self.logger.debug(
                'GetFromPoint (Beyond Top Left %s: -1 expected): %s' % (
                    str(theBeyondTopLeftPoint),
                    str(theDisplayGetFromBeyondTopLeftPoint)))

            theWindow = myDisplay
            self.logger.debug(
                'GetFromWindow (window %s: 0 expected) %s' % (
                    str(theWindow),
                    str(myDisplay.GetFromWindow(theWindow))))

            theNonWindow = None
            self.logger.debug(
                'GetFromWindow (window %s: %s expected) %s' % (
                    str(theNonWindow),
                    str(wx.NOT_FOUND),
                    str(myDisplay.GetFromWindow(theNonWindow))))

            self.logger.debug(
                'GetGeometry: %s' % myDisplay.GetGeometry())

            self.logger.debug(
                'GetModes (DefaultVideoMode: %s expected) %s' % (
                    wx.DefaultVideoMode,
                    myDisplay.GetModes(wx.DefaultVideoMode)))

            self.logger.debug(
                'GetName: %s' % myDisplay.GetName())

            self.logger.debug(
                'IsOk: %s' % myDisplay.IsOk())

            self.logger.debug(
                'IsPrimary: %s' % myDisplay.IsPrimary())

            self.logger.debug(
                'ResetMode: %s' % myDisplay.ResetMode())

            self.logger.debug(
                'Children: %s' % str(myDisplay.Children))

            self.logger.debug(
                'stdscr: %s' % str(myDisplay.stdscr))

            self.logger.debug(
                'theRedirectedStdioArea: %s' % str(
                myDisplay.theRedirectedStdioArea))

            self.logger.debug(
                'theScreen: %s' % str(myDisplay.theScreen))

            self.logger.debug(
                'theTaskArea: %s' % str(myDisplay.theTaskArea))

            self.logger.debug(
                'theTasks: %s' % str(myDisplay.theTasks))

            self.logger.debug(
                'ClientArea: %s' % str(myDisplay.ClientArea))

            self.logger.debug(
                'CurrentMode: %s' % str(myDisplay.CurrentMode))

            self.logger.debug(
                'Geometry: %s' % str(myDisplay.Geometry))

            self.logger.debug(
                'HasColors: %s' % str(myDisplay.HasColors))

            self.logger.debug(
                'Modes: %s' % str(myDisplay.Modes))

            self.logger.debug(
                'Name: %s' % str(myDisplay.Name))

##            self.logger.debug(
##                'ColorDatabase: %s' % dir(ColorDatabase))

            self.logger.debug(
                'ColorDataBaseID: %s' % str(
		    tsGTUI.GraphicalTextUserInterface.ColorDataBaseID))

        except Exception, errorCode:
            self.logger.error('testDisplay.main: errorCode=%s' % \
                              str(errorCode))

#---------------------------------------------------------------------------

if __name__ == '__main__':

##    # Create my App
##    # Run the main entry point

##    # Remember original stdout and stderr
##    #  WxPython makes them graphical
##    _stdout = sys.stdout
##    _stderr = sys.stderr

##    exitStatus = tse.NONERROR_ERROR_CODE
##    msg = tse.NO_ERROR

##    try:
##        theApplication = displayTest(
##            header=__header__,
##            mainTitleVersionDate=mainTitleVersionDate,
##            title=__title__,
##            version=__version__,
##            date=__date__,
##            logs=[])

##        theApplication.runMain()

##    except Exception, e:
##        if isinstance(e, tse.TsExceptions):
##            msg = str(e)
##            tse.displayError(e)
##            exitStatus = e.exitCode
##        else:
##            msg = None
##            _stderr.write(traceback.format_exc())
##            exitStatus = tse.INVALID_ERROR_CODE

####    print __header__
###    _stdout.write(__header__)

##    if msg == tse.NO_ERROR:
##        _stdout.write(msg + '\n')

##    elif msg is not None:
##        _stderr.write(msg.replace('"', '') + '\n')

##    # Return (exitStatus)
##    sys.exit(exitStatus)


    #----------------------------------------------------------------------

    def exitTest():
        '''
        Simulated Input / Output Exception to induce termination
        with an exit code and message.
        '''
 
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = tsLogger.TsLogger(threshold=tsLogger.DEBUG,
                                     name='exitTest')

        message = 'ExitTest'

        myLogger.debug('***** ExitTest %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def getRunTimeTitle():
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        # Capture Command Line Arguments.
        argv = sys.argv

        # Separate File Path from its associated File Name and Extension
        (filePath, fileNameExt) = os.path.split(argv[0])

        # Separate File Name from its associated Extension
        (fileName, fileExt) = os.path.splitext(fileNameExt)

        return (fileName)

    #----------------------------------------------------------------------

    def getRunTimeTitleVersionDate():
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        runTimeTitle = getRunTimeTitle()
        if runTimeTitle == __title__:

            runTimeTitleVersionDate = mainTitleVersionDate

        else:

            runTimeTitleVersionDate = '%s, v%s (build %s)' % (
                runTimeTitle, __version__, __date__)

        return (runTimeTitleVersionDate)

    #----------------------------------------------------------------------

    def prototype(*args, **kw):
        '''
        Simulated main program entry point with simulated exception
        inducing exit test.
        '''
        print('\n%s\n' % getRunTimeTitleVersionDate())

        rawArgsOptions = sys.argv[1:]
        print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        theModule = tsOperatorSettingsParser
        theClass = theModule.TsOperatorSettingsParser()
        (args, options) = theClass.parseCommandLineDispatch()

        if True or DEBUG:

            print('\n\ttsCommandLineEnv.prototype (parameter list): ' + \
                  '\n\t\targs=%s;\n\t\tkw=%s' % (str(args),
                                                 str(kw)))

            print('\n\ttsCommandLineEnv.prototype (command line argv): ' + \
                  '\n\t\targs=%s;\n\t\toptions (unsorted)=%s' % (
                      str(args),
                      str(options)))

            fmt1 = '\n\ttsCommandLineEnv.prototype (command line argv): '
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                value = '"%s"' % options[key]
                if text == '':
                    text = '{%s: %s' % (str(key), str(value))
                else:
                    text += ', %s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        try:
            myLogger = tsLogger.TsLogger(
                threshold = tsLogger.DEBUG,
                start = time.time(),
                name = 'testDisplay.log') 
##          myLogger = tsLogger.TsLogger(
##              threshold = tsLogger.DEBUG,
##              name = ' ')
            myLogger.notice('About to invoke displayTest')
            testApplication = displayTest(myLogger)

        except Exception, e:
            if isinstance(e, tse.TsExceptions):
                msg = str(e)
                tse.displayError(e)
                exitStatus = e.exitCode
            else:
                msg = None
                sys.stderr.write(traceback.format_exc())
                exitStatus = tse.INVALID_ERROR_CODE

        # exitTest()

    #----------------------------------------------------------------------

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
            buildPurpose=__doc__,

            enableDefaultCommandLineParser=False,

##          guiMessageFilename=None,
##          guiMessageRedirect=False,
##          guiRedirects=False,
##          guiRequired=False,
##          guiTopLevelObject=None,
##          guiTopLevelObjectId=None,
##          guiTopLevelObjectName=None,
##          guiTopLevelObjectParent=None,
##          guiTopLevelObjectTitle=None,

            logs=[tsLogger.StandardOutputFile, 'Dummy#2', 'Dummy#3'],

            runTimeEntryPoint=prototype)

        results = (theApplication.args, theApplication.options)
        print('results="%s"' % str(results))
        theAssignedLogger = theApplication.logger
        theApplication.runMainApplication()

    except Exception, applicationError:

        if isinstance(applicationError, tse.TsExceptions):
            msg = str(applicationError).replace("'", "")
            tse.displayError(applicationError)
            exitStatus = applicationError.exitCode
        else:
            msg = None
            sys.stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

    if msg == tse.NO_ERROR:
        sys.stdout.write(msg)
    elif msg is not None:
        sys.stderr.write(msg)

    # Return (exitStatus)
    sys.exit(exitStatus)
