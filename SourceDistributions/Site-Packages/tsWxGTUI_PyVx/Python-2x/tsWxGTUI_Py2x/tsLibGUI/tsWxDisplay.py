#! /usr/bin/env python
# "Time-stamp: <04/08/2015  5:51:51 AM rsg>"
'''
tsWxDisplay.py - Class to represent the features of a
display/monitor attached to the system.
'''
#################################################################
#
# File: tsWxDisplay.py
#
# Purpose:
#
#    Class to represent the features of a display/monitor attached
#    to the system.
#
# Usage (example):
#
#    # Import
#
#    from tsWxDisplay import Display
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
#    None.
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
#    2011/04/01 rsg Used wxPoint, wxSize and wxRect instead of
#                   tuples for StdScreenGeometry.
#
#    2013/12/26 rsg Corrected format of returned values:
#                   Incorrect Tuple: ((0, 0),)
#                   Corrected Tuple: (0, 0)
#
#    2013/12/27 rsg Corrected GetMame so as to use:
#                   Display.TheTerminal.TermName
#
#    2014/02/09 rsg Re-designed __init__, tsInstallLoggerAccess
#                   and tsPrivateLogger. Converted the private
#                   log file DisplayConfiguration.txt to a
#                   tsLogger managed log file and co-located it
#                   with the other run-time log files. This
#                   avoided clutteringthe application launch
#                   directory with diagnostic files needed only
#                   during troubleshooting.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxDisplay'
__version__   = '1.1.0'
__date__      = '02/09/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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

#---------------------------------------------------------------------------

import time

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger
from tsWxGTUI_Py2x.tsLibCLI import tsReportUtilities

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Display(object):
    '''
    Represents a display/monitor attached to the system.
    '''

    # Display geometry provided for static method references.
    EnableRedirectArea = None
    EnableTaskBarArea = None
    Parent = None
    TerminalPixelRectangle = None
    TheLogger = None
    TheTerminal = None
    TheTerminalScreen = None
    VideoMode = None

    PrivateLogger = None

    def __init__(self, parent, reservedAreaFlags=None):
        '''
        Construct class
        '''

        theClass = 'Display'

        wx.RegisterFirstCallerClassName(self, theClass)
 
##        self.tsBeginClassRegistration(theClass, id)

        self.ts_Name = theClass

        if Display.TheLogger is None:

            Display.TheLogger = self.tsInstallTheLoggerAccess()

        if Display.TheTerminal is None:

            try:

                Display.TheTerminal = tsGTUI.GraphicalTextUserInterface(
                    theClass)

                Display.TheTerminalScreen = Display.TheTerminal.Stdscr

                theGeometryPixels = Display.TheTerminal.StdscrGeometryPixels
                Display.TerminalPixelRectangle = theGeometryPixels

                Display.VideoMode = wx.DefaultVideoMode

                (theTaskBarAreaFlag,
                 theRedirectAreaFlag) = self.tsIsNowOkToEnableReservedArea(
                     reservedAreaFlags)

                Display.EnableRedirectArea = theRedirectAreaFlag
                Display.EnableTaskBarArea = theTaskBarAreaFlag

                Display.Parent = parent

                if DEBUG and VERBOSE:

                    self.tsPrivateLogger(
                        'EnableRedirectArea=%s' % str(
                            Display.EnableRedirectArea))

                    self.tsPrivateLogger(
                        'EnableTaskBarArea=%s' % str(
                            Display.EnableTaskBarArea))

                    self.tsPrivateLogger(
                        'Parent=%s' % Display.Parent)

                    self.tsPrivateLogger(
                        'TerminalPixelRectangle=%s' % str(
                            Display.TerminalPixelRectangle))

                    self.tsPrivateLogger(
                        'TheTerminal=%s' % str(
                            Display.TheTerminal))

                    self.tsPrivateLogger(
                        'TheTerminalScreen=%s' % str(
                            Display.TheTerminalScreen))

                    self.tsPrivateLogger(
                        'VideoMode=%s' % str(
                            Display.VideoMode))

            except AttributeError, e:

                msg = '%s.__init__: Exception = %s' % (__title__, str(e))
                self.tsPrivateLogger(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
 
            self.tsPrivateLogger('End %s (ts_FirstCaller=%s)' % (
                theClass, self.theFirstCallerClassName))

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def __del__(self):
##        '''
##        '''
##        pass

    #-----------------------------------------------------------------------

    def __nonzero__(self):
        '''
        Return True if and initialized display exists; else return False.
        '''
        if Display.TheTerminal is None:
            result = False

        elif Display.TerminalPixelRectangle == wxRect(0, 0, 0, 0):
            result = False

        else:
            result = True

        return (result)

    #-----------------------------------------------------------------------

    def ChangeMode(self, mode=wx.DefaultVideoMode):
        '''
        Changes the video mode of this display to the mode specified in
        the mode parameter.
        '''
        if (Display.VideoMode != mode) and \
           (mode == wx.DefaultVideoMode):

            Display.VideoMode = mode
            return (True)

        else:

            return (False)

    #-----------------------------------------------------------------------

    def GetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the display,
        i.e., without taskbars and such.
        '''
        ###############################################################
        #      X=0         1         2         3   X=W-1
        #        01234567890123456789012345678901234
        # Y=0    +---------------------------------+ Frame Border Top
        #   1    |Client Area                      |
        #   2    |   (ex. 35 cols x 6 rows)        |
        #   3    |                                 |
        #   4    |                                 |
        #   5    +---------------------------------+ Frame Border Bottom
        #   H-9  +---------------------------------+ Stdio Border Top
        #   H-8  |Stdio Output (Optionl)           |
        #   H-7  |   (ex. 35 cols x 5 rows)        |
        #   H-6  |                                 |
        #   H-5  +---------------------------------+ Stdio Border Bottom
        #   H-4  +---------------------------------+ Task Border Top
        #   H-3  |Task Bar Output (Optional)       |
        #   H-2  |   (ex. 35 cols x 4 rows)        |
        # Y=H-1  +---------------------------------+ Task Border Bottom
        ###############################################################
        if DEBUG and VERBOSE:
            self.tsPrivateLogger(
                '  GetClientArea:Display.EnableRedirectArea=%s' % \
                Display.EnableRedirectArea)
 
            self.tsPrivateLogger(
                '  GetClientArea:Display.EnableTaskBarArea=%s' % \
                Display.EnableTaskBarArea)

        theCharacterArea = self.GetGeometry(pixels=False)

        if Display.EnableTaskBarArea:

            theTaskArea = self.tsGetTaskArea(pixels=False)

            theCharacterArea.height -= theTaskArea.height

        if Display.EnableRedirectArea:

            theRedirectedStdioArea = self.tsGetRedirectedStdioArea(
                pixels=False)

            theCharacterArea.height -= theRedirectedStdioArea.height


        thePixelArea = wxRect(
            theCharacterArea.x * wx.pixelWidthPerCharacter,
            theCharacterArea.y * wx.pixelHeightPerCharacter,
            theCharacterArea.width * wx.pixelWidthPerCharacter,
            theCharacterArea.height * wx.pixelHeightPerCharacter)
 
        if pixels:
            theArea = thePixelArea
        else:
            theArea = theCharacterArea

        if DEBUG and VERBOSE:
            self.tsPrivateLogger(
                'GetClientArea: %s pixels = %s characters' % (
                    thePixelArea, theCharacterArea))

        return (theArea)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetCount():
        '''
        Return the number of available displays.
        '''
        if Display.TheTerminal is None:

            return (0)

        else:

            # There should be only one display
            return (1)

    #-----------------------------------------------------------------------

    def GetCurrentMode(self):
        '''
        Get the current video mode.
        '''
        return (Display.VideoMode)

    #-----------------------------------------------------------------------
 
    @staticmethod
    def GetFromPoint(pt):
        '''
        Find the display where the given point lies, return wx.NOT_FOUND
        if it does not belong to any display.
        '''
        if Display.TheTerminal is None:

            return (wx.NOT_FOUND)

        elif Display.TerminalPixelRectangle.Inside(pt):

            # There should be only one display
            return (0)

        else:

            return (wx.NOT_FOUND)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetFromWindow(window):
        '''
        Find the display where the given window lies, return wx.NOT_FOUND
        if it is not shown at all.
        '''
        if Display.TheTerminal is None:

            return (wx.NOT_FOUND)

        elif window is None:

            return (wx.NOT_FOUND)

        else:

            # There should be only one display
            return (0)

    #-----------------------------------------------------------------------

    def GetGeometry(self, pixels=True):
        '''
        Returns the bounding rectangle of the display whose index was
        passed to the constructor.
        '''
        if Display.TheTerminal is None:

            (displayX,
             displayY,
             displayWidth,
             displayHeight) = (0, 0, 0, 0)

        else:

            if True:
                geometry = Display.TheTerminal.ts_stdscrGeometry
                (displayX,
                 displayY,
                 displayWidth,
                 displayHeight) = (geometry.x,
                                   geometry.y,
                                   geometry.width,
                                   geometry.height)
            else:
                (displayX,
                 displayY,
                 displayWidth,
                 displayHeight) = Display.TheTerminal.ts_stdscrGeometry


        theCharacterArea = wxRect(
            displayX,
            displayY,
            displayWidth,
            displayHeight)

        thePixelArea = wxRect(
            displayX * wx.pixelWidthPerCharacter,
            displayY * wx.pixelHeightPerCharacter,
            displayWidth * wx.pixelWidthPerCharacter,
            displayHeight * wx.pixelHeightPerCharacter)
 
        if pixels:
            theArea = thePixelArea
        else:
            theArea = theCharacterArea

        if DEBUG and VERBOSE:
            self.tsPrivateLogger(
                'GetGeometry: %s pixels = %s characters' % (
                    thePixelArea, theCharacterArea))

        return (theArea)

    #-----------------------------------------------------------------------

    def GetModes(self, mode=wx.DefaultVideoMode):
        '''
        Enumerate all video modes supported by this display matching the
        given one (in the sense of VideoMode.Match()).
        '''
        if mode == wx.DefaultVideoMode:
            return ([wx.DefaultVideoMode])
        else:
            return ([])

    #-----------------------------------------------------------------------
 
    def GetName(self):
        '''
        Returns the display name.
        '''
        return (Display.TheTerminal.TermName)

    #-----------------------------------------------------------------------
 
    def IsOk(self):
        '''
        Return true if the object was initialized successfully.
        '''
        try:

            ok = Display.TheTerminal.ts_stdscrGeometry != wxRect(0, 0, 0, 0)

        except AttributeError:

            ok = False

        return (ok)

    #-----------------------------------------------------------------------

    def IsPrimary(self):
        '''
        Returns True if the display is the primary display.
        '''
        return (True)

    #-----------------------------------------------------------------------

    def ResetMode(self):
        '''
        Restore the default video mode (just a more readable synonym)
        '''
        Display.VideoMode = wx.DefaultVideoMode

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetRedirectedStdioArea(self, pixels=True):
        '''
        Return rectangle position and size of window used for redirected
        output from print, stdout and stderr.

        NOTE: Area includes top, bottom, left and right borders. It must
        support at least one message. Messages may optionally include a
        timestamp. The assumed length of a typical message, without its
        timestamp, but with the left and right borders, is 80 characters.
        The minimum height must therefore provide sufficient lines to
        display the full message and its timestamp.
        '''
        ###############################################################
        #      X=0         1         2         3   X=W-1
        #        01234567890123456789012345678901234
        # Y=0    +---------------------------------+ Frame Border Top
        #   1    |Client Area                      |
        #   2    |   (ex. 35 cols x 6 rows)        |
        #   3    |                                 |
        #   4    |                                 |
        #   5    +---------------------------------+ Frame Border Bottom
        #   H-9  +---------------------------------+ Stdio Border Top
        #   H-8  |Stdio Output (Optionl)           |
        #   H-7  |   (ex. 35 cols x 5 rows)        |
        #   H-6  |                                 |
        #   H-5  +---------------------------------+ Stdio Border Bottom
        #   H-4  +---------------------------------+ Task Border Top
        #   H-3  |Task Bar Output (Optional)       |
        #   H-2  |   (ex. 35 cols x 4 rows)        |
        # Y=H-1  +---------------------------------+ Task Border Bottom
        ###############################################################
        if Display.EnableRedirectArea:

            theTotalArea = self.GetGeometry(pixels=False)

            borderRows = 2
            # borderCols = 2

            if wx.ThemeToUse['Stdio']['Timestamp']:
                minLineWidth = wx.pageWidth + len('2008/07/04 05:44:52.486 -')
            else:
                minLineWidth = wx.pageWidth

            (minDisplayPixelWidth, minDisplayPixelHeight) = \
                                   wx.RedirectedWindowHeight['minDisplay']

            (minDisplayWidth, minDisplayHeight) = (
                 minDisplayPixelWidth // wx.pixelWidthPerCharacter,
                 minDisplayPixelHeight // wx.pixelHeightPerCharacter)

            minHeightPercent = int(
                wx.RedirectedWindowHeight['minHeightPercent'])

            maxHeightPercent = int(
                wx.RedirectedWindowHeight['maxHeightPercent'])

            maxRedirectedWidth = theTotalArea.width

            theTaskArea = self.tsGetTaskArea(pixels=False)

            # thePosition = wxPoint(theTotalArea.x, theTotalArea.y)
            theSize = wxSize(theTotalArea.width, theTotalArea.height)

            theRedirectedAreaOffset = - 1
            if theSize.width < minDisplayWidth:

                if theSize.height < minDisplayHeight:

                    maxRedirectedHeight = max(
                        (borderRows + int(
                            1 + minLineWidth // maxRedirectedWidth)),
                        ((theSize.height *  minHeightPercent) // 100) * \
                        int(1 + minLineWidth // maxRedirectedWidth) + \
                        theRedirectedAreaOffset)

                else:

                    maxRedirectedHeight = max(
                        (borderRows + int(
                            1 + minLineWidth // maxRedirectedWidth)),
                        ((theSize.height *  minHeightPercent) // 100) + \
                        theRedirectedAreaOffset)

            elif theSize.height < minDisplayHeight:

                maxRedirectedHeight = max(
                    (borderRows + int(
                        1 + minLineWidth // maxRedirectedWidth)),
                    ((theSize.height *  minHeightPercent) // 100) + \
                    theRedirectedAreaOffset)

            else:

                maxRedirectedHeight = max(
                    (borderRows + int(
                        1 + minLineWidth // maxRedirectedWidth)),
                    ((theSize.height *  maxHeightPercent) // 100) + \
                    theRedirectedAreaOffset)

            theRedirectedSize = wxSize(maxRedirectedWidth,
                                       maxRedirectedHeight)

            theRedirectedPos = wxPoint(
                theTaskArea.x,
                theTaskArea.y - (theRedirectedSize.height + 0))

            theCharacterArea = wxRect(theRedirectedPos.x,
                                      theRedirectedPos.y,
                                      theRedirectedSize.width,
                                      theRedirectedSize.height)

            thePixelArea = wxRect(
                theCharacterArea.x * wx.pixelWidthPerCharacter,
                theCharacterArea.y * wx.pixelHeightPerCharacter,
                theCharacterArea.width * wx.pixelWidthPerCharacter,
                theCharacterArea.height * wx.pixelHeightPerCharacter)

            if pixels:
                theArea = thePixelArea
            else:
                theArea = theCharacterArea

            if DEBUG and VERBOSE:
                self.tsPrivateLogger(
                    'tsGetRedirectedStdioArea: %s pixels = %s characters' % (
                        thePixelArea, theCharacterArea))

        else:
 
            theArea = None

            if DEBUG and VERBOSE:
                self.tsPrivateLogger(
                    'tsGetRedirectedStdioArea: %s' % theArea)
 
        return (theArea)

    #-----------------------------------------------------------------------

    def tsGetTaskArea(self, pixels=True):
        '''
        Return rectangle position and size of window used for task bar.
        '''
        ###############################################################
        #      X=0         1         2         3   X=W-1
        #        01234567890123456789012345678901234
        # Y=0    +---------------------------------+ Frame Border Top
        #   1    |Client Area                      |
        #   2    |   (ex. 35 cols x 6 rows)        |
        #   3    |                                 |
        #   4    |                                 |
        #   5    +---------------------------------+ Frame Border Bottom
        #   H-9  +---------------------------------+ Stdio Border Top
        #   H-8  |Stdio Output (Optionl)           |
        #   H-7  |   (ex. 35 cols x 5 rows)        |
        #   H-6  |                                 |
        #   H-5  +---------------------------------+ Stdio Border Bottom
        #   H-4  +---------------------------------+ Task Border Top
        #   H-3  |Task Bar Output (Optional)       |
        #   H-2  |   (ex. 35 cols x 4 rows)        |
        # Y=H-1  +---------------------------------+ Task Border Bottom
        ###############################################################
        if Display.EnableTaskBarArea:
 
            theTaskAreaHeight = wx.ThemeToUse['TaskBar']['WindowHeight'] // \
                                wx.pixelHeightPerCharacter

            theTotalArea = self.GetGeometry(pixels=False)

            theTaskAreaOffset = theTaskAreaHeight
            theCharacterArea = wxRect(
                theTotalArea.x,
                theTotalArea.y + theTotalArea.height - theTaskAreaOffset,
                theTotalArea.width,
                theTaskAreaHeight)

            thePixelArea = wxRect(
                theCharacterArea.x * wx.pixelWidthPerCharacter,
                theCharacterArea.y * wx.pixelHeightPerCharacter,
                theCharacterArea.width * wx.pixelWidthPerCharacter,
                theCharacterArea.height * wx.pixelHeightPerCharacter)

            if pixels:
                theArea = thePixelArea
            else:
                theArea = theCharacterArea

            if DEBUG and VERBOSE:
                self.tsPrivateLogger(
                    'tsGetTaskArea: %s pixels = %s characters' % (
                        thePixelArea, theCharacterArea))

        else:
 
            theArea = None

            if DEBUG and VERBOSE:
                self.tsPrivateLogger(
                    'tsGetTaskArea: %s' % theArea)

        return (theArea)

    #-----------------------------------------------------------------------

    def tsGetTheLogger(self):
        '''
        Return the logger instance.
        '''
        return (Display.TheLogger)

    #-----------------------------------------------------------------------

    def tsInstallTheLoggerAccess(self):
        '''
        Return the logger instance.
        '''
        try:

            self.logger = tsLogger.TsLogger(
                threshold=tsLogger.ERROR,
                start=time.time(),
                name=tsLogger.StandardOutputFile)

            Display.PrivateLogger = tsLogger.TsLogger(
                threshold=tsLogger.DEBUG,
                start=time.time(),
                name='DisplayConfiguration.log')

            fmt1 = '%s.tsInstallTheLoggerAccess: '  % __title__
            fmt2 = 'Started diagnostic PrivateLogger'
            msg = fmt1 + fmt2
            Display.PrivateLogger.debug(msg)

        except AttributeError, e:

            self.logger = None
            msg = 'tsInstallTheLoggerAccess: Exception = %s' % e
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (self.logger)

    #-----------------------------------------------------------------------

    def tsGetTheTerminal(self):
        '''
        Return the native (curses) screen.
        '''
        return (Display.TheTerminal)

    #-----------------------------------------------------------------------

    def tsGetTheTerminalScreen(self):
        '''
        Return the native (curses) screen.
        '''
        return (Display.TheTerminalScreen)

    #-----------------------------------------------------------------------

    def tsPrivateLogger(self, text):
        '''
        Output text to Private Logger.
        '''
        Display.PrivateLogger.debug('%s' % text)

    #-----------------------------------------------------------------------

    def tsIsNowOkToEnableReservedArea(self, reservedAreaFlags):
        '''
        Enable reserved area the first time its Flag is ON.
        '''

        if reservedAreaFlags is None:

            enableTaskBarArea = False
            enableRedirectArea = False

        else:

            if reservedAreaFlags['ReserveTaskBarArea']:
                enableTaskBarArea = True
            else:
                enableTaskBarArea = False

            if reservedAreaFlags['ReserveRedirectArea']:
                enableRedirectArea = True
            else:
                enableRedirectArea = False

        return (enableTaskBarArea, enableRedirectArea)

    #-----------------------------------------------------------------------

    def tsGetTheChildren(self):
        '''
        '''
        return (Display.TheTerminal.WindowTopLevelTasks)

    #-----------------------------------------------------------------------

    def tsGetHasColors(self):
        '''
        '''
        return (Display.TheTerminal.HasColors)

    #-----------------------------------------------------------------------

    def tsGetTheTasks(self):
        '''
        '''
        return (Display.TheTerminal.WindowTopLevelTasks)

    #-----------------------------------------------------------------------

    stdscr = property(tsGetTheTerminalScreen)
    theRedirectedStdioArea = property(tsGetRedirectedStdioArea)
    theTaskArea = property(tsGetTaskArea)
    theTerminal = property(tsGetTheTerminal)

    Children = property(tsGetTheChildren)
    HasColors = property(tsGetHasColors)
    theScreen = property(tsGetTheTerminalScreen)
    theTasks = property(tsGetTheTasks)
    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ClientArea = property(GetClientArea)
    CurrentMode = property(GetCurrentMode)
    Geometry = property(GetGeometry)
    Modes = property(GetModes)
    Name = property(GetName)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
