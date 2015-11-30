#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:55:23 AM rsg>"
'''
tsWxPyOnDemandOutputWindow.py - Class that can be used for
redirecting Python stdout and stderr streams. It will do
nothing until something is wrriten to the stream at which
point it will create a Frame with a text area and write the
text there.
'''
#################################################################
#
# File: tsWxPyOnDemandOutputWindow.py
#
# Purpose:
#
#    Class that can be used for redirecting Python stdout and
#    stderr streams. It will do nothing until something is
#    wrriten to the stream at which point it will create a
#    Frame with a text area and write the text there.
#
# Usage (example):
#
#    # Import
#
#    from tsWxPyOnDemandOutputWindow import PyOnDemandOutputWindow
#    from tsWxPyOnDemandOutputWindow import PyOnDemandStdioWindow
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    2011/11/21 rsg Added StdioMargin and StdioMarkup from the
#                   theme controls.
#
#    2011/12/30 rsg Added logic to write to accept markup only
#                   when terminal reports that it has colors.
#
#    2012/01/15 rsg Added logic to apply default ThemeToUse
#                   markup to increase brightness/contrast in
#                   order to improve readibility.
#
#    2012/01/19 rsg Added logic to CreateOutputWindow that
#                   inhibits color markup for non-color vt100
#                   and vt220 terminal emulators.
#
#    2012/02/21 rsg Modified tsOn... to invoke
#                   tsProcessEventTables.
#
#    2012/05/14 rsg Modified __init__ logic to set
#                   "self.ts_PyOnDemandStdioWindow = True"
#                   and set associated variables when "wx.ThemeToUse[
#                   'StdioTitle'] == wx.StdioRedirectedTitleStr".
#
#    2012/05/14 rsg Modified CreateOutputWindow to proceed only if
#                   self.ts_Frame is None.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event).
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsWxPyOnDemandOutputWindow'
__version__   = '1.6.1'
__date__      = '04/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibGUI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Curses Module API & ' + \
                'Run Time Library Features:' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  wxWidgets (formerly wxWindows) & ' + \
                'wxPython API Features:' + \
                '\n\t  Copyright (c) 1992-2008 Julian Smart, ' + \
                'Robert Roebling,' + \
                '\n\t\t\tVadim Zeitlin and other members of the ' + \
                '\n\t\t\twxWidgets team.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  wxWindows Library License' + \
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'

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

import os
import time

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

tsrpu = tsReportUtilities.TsReportUtilities()

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxEvent

from tsWxGTUI_Py2x.tsLibGUI.tsWxDisplay import Display as wxDisplay
from tsWxGTUI_Py2x.tsLibGUI.tsWxFrame import Frame as wxFrame
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxTextCtrl import TextCtrl as wxTextCtrl

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

printMarkupToIgnore = {' ': '[Print terminated with Comma]',
                       '\n': '[Print terminated with New Line]'}

#---------------------------------------------------------------------------

class PyOnDemandOutputWindow(object):
    '''
    A class that can be used for redirecting Python stdout and stderr streams.
    It will do nothing until something is written to the stream at which point
    it will create a Frame with a text area and write the text there.
    '''
    def __init__(self, title):
        '''
        Construct a wx.PyOnDemandOutputWindow object.
        '''
        theClass = 'PyOnDemandStdioWindow'

        wx.RegisterFirstCallerClassName(self, theClass)

##        applicationId = wx.ID_ANY

##        self.tsBeginClassRegistration(theClass, applicationId)

        indent = '--' * 5
        self.logger = tsLogger.TsLogger(
            threshold=tsLogger.DEBUG,
            start=time.time(),
            name=tsLogger.StandardOutputFile)

        self.logger.debug(
            '%s Begin %s (0x%X) after logger import.' % (
                indent, theClass, id(self)))

        # Establish defaults until attributes finalized
        self.ts_ClassName = theClass
        self.ts_Frame = None
        self.ts_Parent = None
        self.ts_Text = None
        self.ts_Title = title

        if wx.ThemeToUse['Stdio']['Title'] == wx.StdioRedirectedTitleStr:

            self.ts_PyOnDemandStdioWindow = True

            self.ts_Name = wx.StdioNameStr
            self.ts_Style = wx.DEFAULT_STDIO_STYLE
            self.ts_logFile = self.tsCreateScrollableRedirectionLog()
            self.ts_Margin = wx.tsGetClassInstanceFromTuple(
                wx.ThemeToUse['Stdio']['Margin'], wxSize)

        else:

            self.ts_PyOnDemandStdioWindow = False

            self.ts_Name = wx.FrameNameStr
            self.ts_Style = wx.DEFAULT_FRAME_STYLE
            self.ts_logFile = None
            self.ts_Margin = wx.tsGetClassInstanceFromTuple(
                wx.ThemeToUse['Stdio']['Margin'], wxSize)

        (thePosition, theSize) = self.tsGetStdioPositionAndSize()
        self.ts_Rect = wxRect(thePosition.x,
                              thePosition.y,
                              theSize.width,
                              theSize.height)

        self.ts_ClientRect = wxRect(
            thePosition.x + wx.pixelWidthPerCharacter,
            thePosition.y + wx.pixelHeightPerCharacter,
            theSize.width - 2 * wx.pixelWidthPerCharacter,
            theSize.height - 2 * wx.pixelHeightPerCharacter)

        self.ts_Cache = wx.EmptyString

        #self.OnCloseClicked = None
        #self.OnHelpClicked = None
        #self.OnMaximizeClicked = None
        #self.OnMinimizeClicked = None
        #self.OnRestoreDownClicked = None
        self.OnClose = None
        self.OnHelp = None
        self.OnMaximize = None
        self.OnMinimize = None
        self.OnRestoreDown = None

##        self.tsEndClassRegistration(theClass)
##        self.logger.debug(
##            '%s End %s (0x%X).' % (
##                indent, theClass, id(self)))

    #-----------------------------------------------------------------------

    def close(self):
        '''
        '''
        if self.ts_Frame is not None:
            self.ts_Frame.Close()

    #-----------------------------------------------------------------------
 
    def CreateOutputWindow(self, st):
        '''
        Create frame and text control. Append st (text) to output. Show the
        frame and bind the frame OnCloseButtton to the event.
        '''
        # TBD - Under Construction. The class wxTextCtrl is not available.
        if not (self.ts_Frame is None):
            return
 
        try:
            self.ts_Frame = wxFrame(
                self.ts_Parent,
                id=-1,
                title=self.ts_Title,
                pos=wxPoint(self.ts_Rect.x, self.ts_Rect.y),
                size=wxSize(self.ts_Rect.width, self.ts_Rect.height),
                style=self.ts_Style,
                name=self.ts_Name)
        except Exception, frameError:
            self.logger.error(
                '  CreateOutputWindow: frameError. %s' % frameError)
            msg = 'CreateOutputWindow Frame Error: %s' % str(frameError)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if self.ts_Frame.display.HasColors:
            self.ts_Markup = wx.ThemeToUse['Stdio']['Markup']['DEFAULT']
        else:
            self.ts_Markup = None

        try:
            self.ts_Text  = wxTextCtrl(
                self.ts_Frame,
                id=-1,
                value=wx.EmptyString,
                pos=wxPoint(
                    self.ts_ClientRect.x + self.ts_Margin.width,
                    self.ts_ClientRect.y + self.ts_Margin.height),
                size=wxSize(
                    self.ts_ClientRect.width - 2 * self.ts_Margin.width,
                    self.ts_ClientRect.height - 2 * self.ts_Margin.height),
                style=0, # wx.TE_MULTILINE |wx.TE_READONLY,
                validator=wx.DefaultValidator,
                name=wx.TextCtrlNameStr)
        except Exception, textCtrError:
            self.logger.error(
                '  CreateOutputWindow: textCtlError. %s' % textCtrError)
            msg = 'CreateOutputWindow textCtr Error: %s' % str(textCtrError)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Skip this since text has been pre-cached in self.write
        # before invocation of self.CreateOutputWindow.
        if False:
            self.ts_Text.AppendText(st)

        self.ts_Frame.Show(True)
##        self.ts_Frame.Bind(tsWxEvent.EVT_CLOSE, self.OnCloseWindow)

    #-----------------------------------------------------------------------

    def flush(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def OnCloseWindow(self, event):
        '''
        '''
        if self.ts_Frame is not None:
            self.ts_Frame.Destroy()

        self.ts_Frame = None
        self.ts_Text  = None

    #-----------------------------------------------------------------------
 
    def SetParent(self, parent):
        '''
        Set the window to be used as the popup Frame parent.
        '''
        self.ts_Parent = parent

    #-----------------------------------------------------------------------

    def write(self, text):
        '''
        Create the output window if needed and write the string to it.
        If not called in the context of the gui thread then uses CallAfter
        to do the work there.

        NOTE: In accordance with Python convention, this method supports the
        formating of a single line of output across multiple print statements.
        '''
        if self.ts_Frame is None:
 
            msg1 = 'Print statements and other standard output '
            msg2 = 'will now be directed to this window.'

            if wx.ThemeToUse['Stdio']['Timestamp']:
                theStartupText = '\n\n%s\n' % (msg1 + msg2)
            else:
                theStartupText = '%s\n' % (msg1 + msg2)

            if wx.ThemeToUse['Stdio']['Timestamp']:
                # Begin the new record with a timestamp.
                timestamp = tsrpu.getDateTimeString(time.time(), msec=True)
                self.ts_Cache += '%s - %s' % (timestamp, theStartupText)
            else:
                # Append the text to the existing record.
                self.ts_Cache += theStartupText

            self.CreateOutputWindow(theStartupText)

        if self.ts_logFile is None and \
           wx.ThemeToUse['Stdio']['ScrollableLogFile']:
            self.ts_logFile = self.tsCreateScrollableRedirectionLog()

        theMarkup = None
        if self.ts_Frame.display.HasColors:
            # TBD - Fix so that we pass Attributes without colors.
            for theKey in wx.ThemeToUse['Stdio']['Markup'].keys():

                thePriorityKey = '%s:' % theKey
                theKeyPosition = text.find(thePriorityKey)
                ## print('theKeyPosition[%s] = %d' % (theKey, theKeyPosition))
                if (theKeyPosition > -1):
                    theMarkup = wx.ThemeToUse['Stdio']['Markup'][theKey]
                    ## print('theKeyPosition[%s] = %d' % (
                    ##     theKey, theKeyPosition))

                    break

        # Original design based on wxPyOnDemandOutputWindow
        # without markup

        if theMarkup is None:

            # Apply default markup to increase brightness/conrtrast
            # in order to improve readability
            theKey = 'DEFAULT'
            theMarkup = wx.ThemeToUse['Stdio']['Markup'][theKey]

        if self.ts_Text is not None:

            terminalCharacter = len(text)
            terminalNewLine = text[
                terminalCharacter - 1:terminalCharacter] == '\n'

            if text not in list(printMarkupToIgnore.keys()):

                if (self.ts_Cache == wx.EmptyString):

                    # Begin the new record with a timestamp.
                    timestamp = tsrpu.getDateTimeString(time.time(),
                                                        msec=True)
                    self.ts_Cache += '%s - %s' % (timestamp, text)

                else:

                    # Append the text to the existing record.
##                    timestamp = wx.EmptyString
##                    theMarkup = None
                    self.ts_Cache += text

                if terminalNewLine:

                    # End and output those existing records that
                    # contain a new line.
                    self.ts_Text.AppendText(self.ts_Cache,
                                            markup=theMarkup)
                    self.tsUpdateScrollableRedirectionLog(self.ts_Cache)
                    self.ts_Cache = wx.EmptyString

            elif terminalNewLine:

                # End and output those existing records that
                # would now contain a new line.
                self.ts_Text.AppendText(self.ts_Cache, markup=theMarkup)
                self.tsUpdateScrollableRedirectionLog(self.ts_Cache)
                self.ts_Cache = wx.EmptyString

            else:

                # Append the text to the existing record.
                self.ts_Cache += text

        self.ts_Frame.Show(True)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetStdioPositionAndSize(self):
        '''
        Return position and size of window used for redirected output.
        '''
        if not self.ts_PyOnDemandStdioWindow:
 
            # Establish defaults until attributes finalized
            theRedirectedPos = wxPoint(-1, -1)
            theRedirectedSize = wxSize(450, 300)

        else:

            try:
                self.Display = wxDisplay(self)
                theClientArea = self.Display.theRedirectedStdioArea

                theRedirectedSize = wxSize(theClientArea.width,
                                           theClientArea.height)

                theRedirectedPos = wxPoint(
                    theClientArea.x,
                    theClientArea.y)
            except Exception, getError:
                theRedirectedPos = wxPoint(-1, -1)
                theRedirectedSize = wxSize(450, 300)
                self.logger.debug(
                    '  GetStdioPositionAndSize Exception. %s' % getError)
                msg = 'GetStdioPositionAndSize Exception: %s' % str(getError)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (theRedirectedPos, theRedirectedSize)

    #-----------------------------------------------------------------------

    def tsCreateScrollableRedirectionLog(self):
        '''
        Return file instance used for scrollable redirected output.
        '''
        # TBD - Begin prototype for Scrollable Redirection Window
        # Will need an application instance specific file name.
        theDirectory = os.getcwd()
        theWindowTitle = self.ts_Title
        theKeyWord = theWindowTitle.split(' ', 1)
        theNickName = theKeyWord[0].strip('_').title()
        theFileName = '%s-stdout' % theNickName

        if True:
            thePathName = os.path.join(
                tsLogger.TsLogger.defaultStandardOutputPath,
                '%s.log' % theFileName)
        else:
            thePathName = tsrpu.getNextPathName(theDirectory, theFileName)
 
        theLogFile = open(thePathName, 'w')

        theLogFileHeader = tsrpu.getSeparatorString(
            title='Begin %s on %s' % (
                'PRINT/STDOUT/STDERR log',
                tsrpu.getDateAndTimeString(time.time())),
            indent=0,
            position=tsrpu.layout['TitleIndent'],
            separatorCharacter='$',
            tab=4)

        theLogFile.write('%s\n\n' % theLogFileHeader)
        theLogFile.write('%s - Started logging to file "%s".\n\n' % (
            tsrpu.getDateTimeString(time.time(), msec=True),
            thePathName))
        # TBD - End prototype for Scrollable Redirection Window
        return (theLogFile)

    #-----------------------------------------------------------------------

    def tsOnCloseClick(self, evt):
        '''
        '''
        objectCriteria = 'DEBUG: tsOnCloseClick: EVT_CLOSE ' + \
                         'for [X]-Button ' + \
                         'of "%s" window is NOT handled.\n' % self.ts_Title

        triggerentEvent = EVT_CLOSE
        triggeringObject = self.OnClose
        objectId = self.OnClose.ts_AssignedId

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnHelpClick(self, evt):
        '''
        '''
        objectCriteria = 'tsOnHelpClick: EVT_HELP ' + \
                         'for [?]-Button not handled.'

        triggerentEvent = EVT_HELP
        triggeringObject = self.OnHelp
        objectId = self.OnHelp.ts_AssignedId

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnMaximizeClick(self, evt):
        '''
        '''
        objectCriteria = 'tsOnMaximizeClick: EVT_MAXIMIZE ' + \
                         'for [Z]-Button not handled.'


        triggerentEvent = EVT_MAXIMIZE
        triggeringObject = self.OnMaximize
        objectId = self.OnMaximize.ts_AssignedId

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnMinimizeClick(self, evt):
        '''
        '''
        objectCriteria = 'tsOnMinimizeClick: EVT_ICONIZE ' + \
                         'for [_]-Button not handled.'

        triggerentEvent = EVT_ICONIZE
        triggeringObject = self.OnMinimize
        objectId = self.OnMinimizee.ts_AssignedId

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnRestoreDownClick(self, evt):
        '''
        '''
        objectCriteria = 'tsOnRestoreDownClick: EVT_RESTOREDOWN ' + \
                         'for [z]-Button not handled.'

        triggerentEvent = EVT_RESTOREDOWN
        triggeringObject = self.OnRestoreDown
        objectId = self.OnRestoreDown.ts_AssignedId

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    def tsUpdateScrollableRedirectionLog(self, theRecord):
        '''
        Append the record to the scrollable redirected output.
        '''
        self.ts_logFile.write(theRecord + '\n')
        self.ts_logFile.flush()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
