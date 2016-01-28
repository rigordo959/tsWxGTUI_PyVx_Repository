#! /usr/bin/env python
#"Time-stamp: <11/26/2013  9:51:05 PM rsg>"
'''
test_tsWxSplashScreen.py - Test application program. It demonstrates
features and operation of the tsWxSplashScreen class and associated
building block components of tsLibCLI and tsLibGUI.
'''
#################################################################
#
# File: test_tsWxSplashScreen.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of the tsWxSplashScreen class and associated
#    building block components of tsLibCLI and tsLibGUI.
#
# Capabilities:
#
#    Displays "tsWxGTUI" Toolkit Trademark, Copyright Notice,
#    Recipient Rights (License) or referral to Notice file.
#
# Limitations:
#
#    Requires 60+ column x 47+ row display for Trademark,
#    Copyright Notice and Recipient Rights (License).
#
#    Requires 60+ column x 35 row display for Copyright
#    Notice and Recipient Rights (License).
#
#    Requires 60+ column x 14 row display for referral
#    to Notice file.
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxSplashScreen.py
#
# Classes & Methods:
#
#    _Prototype
#    _Prototype.EntryPoint
#    _Prototype.ExitSplashScreen
#    _Prototype.InitPanelSizer
#    _Prototype.InitPanelText
#    _Prototype.InitSplashScreen
#    _Prototype.InitUserInterface
#    _Prototype.LayoutSplashScreen
#    _Prototype.OnAbout
#    _Prototype.OnHelp
#    _Prototype.OnMove
#    _Prototype.OnQuit
#    _Prototype.WrapupSplashScreen
#    _Prototype.__init__
#    _Prototype.exitTest
#    _Prototype.getEntrySettings
#    _Prototype.getOptions
#    _Prototype.tsGetTheId
#
# Methods:
#
#    nextWindowId
#    nextWindowId
#
# Modifications:
#
#   2013/11/26 rsg Re-engineered for available display
#
#                  If space is marginal:
#                      1. See "Notice.txt" file...
#
#                  elif space is acceptable:
#                      1. copyright
#                      2. rights
#
#                  else (space is more than ample):
#                      1. trademark
#                      2. copyright
#                      3. rights
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsWxSplashScreen'
__version__   = '2.1.0'
__date__      = '11/26/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s. All rights reserved.' % __authors__
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
                '\n\t\t\twxxWidgets team.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  wxWindows Library License' + \
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

import curses
import os.path
import string
import sys
import time
import traceback
from optparse import OptionParser

#--------------------------------------------------------------------------

if True:

    print(__header__)
    time.sleep(5)

#--------------------------------------------------------------------------

if False:
    # Import wingdbstub only if cygwin platform.
    import platform
    hostOS = platform.system().lower()
    if hostOS.find('cygwin') != -1:
        try:
            import wingdbstub
        except ImportError:
            pass

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsApplication as tsAPP
    import tsExceptions as tse
    import tsLogger as Logger
    import tsOperatorSettingsParser

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsLibGUI

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsLibGUI

##    import tsApplication as tsAPP
##    import tsExceptions as tse
##    import tsCommandLineEnv
    import tsWx as wx
    import tsWxMultiFrameEnv

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

except Exception, exceptionCode:

    print('%s: Exception (tsLibGUI); ' % __title__ + \
          'exceptionCode=%s' % str(exceptionCode))

#########################################################################
# Begin Test Control Switches

DEBUG = True
VERBOSE = False

centerOnScreenEnabled = False
exceptionHandlingEnabled = True
frameSizingEnabled = True
redirectEnabled = DEBUG
runTimeTitleEnabled = False
splashScreenEnabled = False
splashScreenSeconds = 0
tracebackEnabled = False

splashScreenEnabled = True
splashScreenSizingEnabled = False
##splashScreenFileName = wx.ThemeToUse['SplashScreenFileName']
##splashScreenShowSeconds = wx.ThemeToUse['SplashScreenShowSeconds']
splashScreenFileName = './theSplashScreen.img'
splashScreenShowSeconds = 15
splashScreenMilliseconds = splashScreenShowSeconds * 1000

# End Test Control Switches

#########################################################################

# For a minimal splashscreen with two nested borders,
# it is presumed that the:
#
#    1. Minimum Display size is 60+ columns x 14+ rows
#
#    2. Minimum Client Area is 56+ columns x 3+ rows
#
#    3. Displays referral to NOTICES.txt file..
##
theNotices = '''Copies of the Copyright, License and Contract agreements
which permit YOUR use, modification & redistribution of
the "tsWxGTUI" Toolkit are in the "NOTICES.txt" file.'''

#########################################################################

# For a usable splashscreen with two nested borders,
# it is presumed that the:
#
#    1. Usable Display size is 60+ columns x 35+ rows
#
#    2. Usable Client Area is 56+ columns x 31+ rows
#
#    3. Displays Copyright and Rights (License).
#

theCopyright = '''tsWxGTUI, v0.0.0 (build 11/25/2013)

  Author(s): Richard S. Gordon
  Copyright (c) 2010-2013 Richard S. Gordon,
                          a.k.a Software Gadgetry
                          (formerly TeamSTARS),
                All rights reserved.
  GNU General Public License, Version 3, 29 June 2007

  Third-party components are subject to their author`s
  designated copyright and license notices.'''

theRights = '''This is free and open source software. You can redistri-
bute and modify it only under the terms and conditions
set forth in the accompanying files, "COPYRIGHT.txt" and
"LICENSE.txt".

The "tswxGTUI" Toolkit and third-party components are
distributed in the hope that they will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.'''

#########################################################################

# For an ample splashscreen with two nested borders,
# it is presumed that the:
#
#    1. Ample Display size exceeds 60+ columns x 47+ rows
#
#    2. Ample Client Area exceeds 56+ columns x 43+ rows
#
#    3. Displays Trademark, Copyright and Rights (License).
#

theTrademark = '''+----+----+  TeamSTARS "tsWxGTUI" Toolkit
| ts | Wx |      with Python-based
+----+----+         Command Line Interface (CLI)
| G T U I |      and "wxPython"-style, "nCurses"-based
+---------+         Graphical-Text User Interface (GUI)

Get that cross-platform, pixel-mode "wxPython" feeling
on character-mode, "xterm" & "vt100" terminals.'''

#--------------------------------------------------------------------------

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

centerOnScreenEnabled = False
tracebackEnabled = False

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

# End Test Control Switches
#########################################################################

#--------------------------------------------------------------------------

class _Prototype(wx.Frame):
    '''
    Class to establish the frame that contains the application specific
    graphical components.
    '''
    def tsGetTheId(self):
        '''
        Return the ID associated with this class instance.
        '''
        return id(self)

    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id=nextWindowId(),
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.FrameNameStr):
        '''
        Init the Frame
        Show the Frame
        '''
        myApp = self.InitUserInterface(parent,
                 id=wx.ID_ANY,
                 title=title,
                 pos=pos,
                 size=size,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name=name)

        if splashScreenEnabled:
            mySplash = self.InitSplashScreen(
                parent,
                id=wx.ID_ANY,
                title='Splash Screen',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.DEFAULT_FRAME_STYLE,
                name=wx.SplashScreenNameStr)

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

    #-----------------------------------------------------------------------

    def ExitSplashScreen(self):
        '''
        Exit the SplashScreen
        Hide the SplashScreen
        '''
        pass

    #-----------------------------------------------------------------------

    def InitSplashScreen(self,
                         parent,
                         id=nextWindowId(),
                         title=wx.EmptyString,
                         pos=wx.DefaultPosition,
                         size=wx.DefaultSize,
                         style=wx.DEFAULT_FRAME_STYLE,
                         name=wx.FrameNameStr):
        '''
        Init the SplashScreen
        Show the SplashScreen
        '''
        splashScreenParent = None
        msg = 'Sample Bitmap'
        theSplashScreen = wx.SplashScreen(
            splashScreenParent,
            id=wx.ID_ANY,
            bitmap=msg,
            milliseconds=splashScreenMilliseconds,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            splashStyle=0,
            style=0)

        theSplashScreenRect = theSplashScreen.Rect
        print('theSplashScreen.Rect=%s' % str(theSplashScreen.Rect))

        # Vertical Sizers currently only take client width
        # of parent frame and then proportion height.
        borderWidth  = wx.pixelWidthPerCharacter  # left+right
        borderHeight = wx.pixelHeightPerCharacter # top+bottom

        # Cannot log before GUI started via Frame.
        self.logger = theSplashScreen.logger
        self.logger.debug(
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        availablePixelWidth = theSplashScreenRect.width

        availablePixelHeight = theSplashScreenRect.height

        availableWidth, availableHeight = wx.tsGetCharacterValues(
            availablePixelWidth, availablePixelHeight)

        print('availableSplashScreen: width=%d; height=%d' % (
            availableWidth, availableHeight))

        copyrightVerticalFlag = wx.EXPAND
        copyrightVertical = wx.BoxSizer(wx.VERTICAL)

        splashScreenNotices = []
        linesNotices = theNotices.split('\n')
        maxNoticesWidth = 0
        maxNoticesHeight = 0
        for aLine in linesNotices:
            maxNoticesWidth = max(
                maxNoticesWidth, len(aLine))
            maxNoticesHeight += 1
            splashScreenNotices += [aLine]
        print(
            'maxNoticesWidth=%d; maxNoticesHeight=%d' % (
                maxNoticesWidth, maxNoticesHeight))

        splashScreenTrademark = []
        linesTrademark = theTrademark.split('\n')
        maxTrademarkWidth = 0
        maxTrademarkHeight = 0
        for aLine in linesTrademark:
            maxTrademarkWidth = max(
                maxTrademarkWidth, len(aLine))
            maxTrademarkHeight += 1
            splashScreenTrademark += [aLine]
        print(
            'maxTrademarkWidth=%d; maxTrademarkHeight=%d' % (
                maxTrademarkWidth, maxTrademarkHeight))

        splashScreenCopyright = []
        linesCopyright = theCopyright.split('\n')
        maxCopyrightWidth = 0
        maxCopyrightHeight = 0
        for aLine in linesCopyright:
            maxCopyrightWidth = max(
                maxCopyrightWidth, len(aLine))
            maxCopyrightHeight += 1
            splashScreenCopyright += [aLine]
        print(
            'maxCopyrightWidth=%d; maxCopyrightHeight=%d' % (
                maxCopyrightWidth, maxCopyrightHeight))

        splashScreenRights = []
        linesRights = theRights.split('\n')
        maxRightsWidth = 0
        maxRightsHeight = 0
        for aLine in linesRights:
            maxRightsWidth = max(
                maxRightsWidth, len(aLine))
            maxRightsHeight += 1
            splashScreenRights += [aLine]
        print(
            'maxRightsWidth=%d; maxRightsHeight=%d' % (
                maxRightsWidth, maxRightsHeight))

        maxWidth = max(maxNoticesWidth,
                       maxTrademarkWidth,
                       maxCopyrightWidth,
                       maxRightsWidth)
##        theParts = {
##            'Trademark': {
##                'Content': splashScreenTrademark,
##                'Size': len(linesTrademark)},
##            'Copyright': {
##                'Content': splashScreenCopyright,
##                'Size': len(linesCopyright)},
##            'Rights': {
##                'Content': splashScreenRights,
##                'Size': len(linesRights)}
##            }

        parent = theSplashScreen

        copyrightVerticalFlag = wx.EXPAND
        copyrightVertical = wx.BoxSizer(wx.VERTICAL)
        copyrightVerticalPanel = wx.Panel(parent,
                                          wx.ID_ANY,
                                          style=wx.BORDER_SIMPLE)
        copyrightVerticalPanel.SetBackgroundColour("MAGENTA")
        copyrightVertical.Add(
            copyrightVerticalPanel, proportion=1, flag=copyrightVerticalFlag)
        copyrightVerticalPanel.SetAutoLayout(True)
        copyrightVerticalPanel.SetSizer(copyrightVertical)
        copyrightVerticalPanel.Layout()

        self.Show(show=True)

        copyrightVerticalFlag = wx.EXPAND
        copyrightVertical = wx.BoxSizer(wx.VERTICAL)

        #
        # if (space is more than ample):
        #    1. trademark
        #    2. copyright
        #    3. rights
        #
        # elif space is usable:
        #    1. copyright
        #    2. rights
        #
        # elif space is marginal:
        #    1. See "Notice.txt" file...
        #
        # else space is unusable:
        #    1. Report operator configuration error

        if (availableWidth >= maxWidth) and \
           (availableHeight >= (
            maxTrademarkHeight + maxCopyrightHeight + maxRightsHeight + 8)):

            isAmpleSpace = True
            isUsableSpace = False
            isMinimalSpace = False
            isUnusableSpace = False
        else:
            isAmpleSpace = False

            if (availableWidth >= (maxWidth) and \
               (availableHeight >= (
                   maxCopyrightHeight + maxRightsHeight + 6))):

                isUsableSpace = True
                isMinimalSpace = False
                isUnusableSpace = False
            else:
                isUsableSpace = False

                if (availableWidth >= maxWidth) and \
                   (availableHeight >= (maxNoticesHeight + 4)):
                    isMinimalSpace = True
                    isUnusableSpace = False
                else:
                    isMinimalSpace = False

                    if (availableWidth < maxWidth - 4) and (availableHeight < (
                        maxNoticesHeight + 4)):
                        isUnusableSpace = True
                    else:
                        isUnusableSpace = False

        fmt1 = 'isAmpleSpace (%s); ' % str(isAmpleSpace)
        fmt2 = 'isUsableSpace (%s); ' % str(isUsableSpace)
        fmt3 = 'isMinimalSpace (%s); ' % str(isMinimalSpace)
        fmt4 = 'isUnusableSpace (%s)' % str(isUnusableSpace)
        msg = fmt1 + fmt2 + fmt3 + fmt4
        print(msg)

        if isAmpleSpace:

        #
        #    1. Ample Display size exceeds 64 columns x 48 rows
        #
        #    2. Ample Client Area exceeds 60 columns x 34 rows
        #

            copyright1 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="CYAN",
                colorForeground="BLUE",
                contents=splashScreenTrademark,
                flag=copyrightVerticalFlag,
                name="Heading",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            copyright2 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="BLUE",
                colorForeground="YELLOW",
                contents=splashScreenCopyright,
                flag=copyrightVerticalFlag,
                name="TeamStars",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            copyright3 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="BLACK",
                colorForeground="YELLOW",
                contents=splashScreenRights,
                flag=copyrightVerticalFlag,
                name="wxWidgets & wxPython",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            self.InitPanelText(copyright1,
                               splashScreenTrademark,
                               makeBitMap=True)

            self.InitPanelText(copyright2,
                               splashScreenCopyright)

            self.InitPanelText(copyright3,
                               splashScreenRights)

            self.Show(show=True)

        elif isUsableSpace:

            # For a usable splashscreen with two nested borders,
            # it is presumed that the:
            #
            #    1. Usable Display size is 64 columns x 40 rows
            #
            #    2. Usable Client Area is 60 columns x 36 rows

            copyright2 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="BLUE",
                colorForeground="YELLOW",
                contents=splashScreenCopyright,
                flag=copyrightVerticalFlag,
                name="TeamStars",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            copyright3 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="BLACK",
                colorForeground="YELLOW",
                contents=splashScreenRights,
                flag=copyrightVerticalFlag,
                name="wxWidgets & wxPython",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            self.InitPanelText(copyright2,
                               splashScreenCopyright,
                               makeBitMap=True)

            self.InitPanelText(copyright3,
                               splashScreenRights)

            self.Show(show=True)

        elif isMinimalSpace:

            # For a minimal splashscreen with two nested borders,
            # it is presumed that the:
            #
            #    1. Minimum Display size is 60 columns x 14 rows
            #
            #    2. Minimum Client Area is 56 columns x 3 rows
            #

            copyright1 = self.InitPanelSizer(
                parent,
    ##            id=wx.ID_ANY,
                colorBackground="BLACK",
                colorForeground="YELLOW",
                contents=splashScreenNotices,
                flag=copyrightVerticalFlag,
                name="wxWidgets & wxPython",
    ##            pos=wx.DefaultPosition,
    ##            size=wx.DefaultSize,
                sizer=copyrightVertical,
                style=wx.BORDER_SIMPLE
                )

            self.InitPanelText(copyright1,
                               splashScreenNotices,
                               makeBitMap=True)

            self.Show(show=True)

        else:

            # if ((availableWidth < 60) or \
            #     (availableHeight < 14)):

            # For an unusable splashscreen with two nested borders,
            # it is presumed that the:
            #
            #    1. Unusable Display size is less than 60 columns x 14 rows
            #
            #    2. Unusable Client Area is less than 56 columns x 3 rows
            #

            fmt1 = 'InitSplashScreen: '
            fmt2 = 'maxNoticesHeight (%d) > ' % (maxNoticesHeight + 4)
            fmt3 = 'availableHeight (%d).' % availableHeight
            msg = fmt1 + fmt2 + fmt3
            print('ERROR NOTICE: %s' % msg)

            # self.Show(show=True)

            raise tse.UserInterfaceException(
            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE, msg)

    #-----------------------------------------------------------------------

    def InitUserInterface(self,
                          parent,
                          id=nextWindowId(),
                          title=wx.EmptyString,
                          pos=wx.DefaultPosition,
                          size=wx.DefaultSize,
                          style=wx.DEFAULT_FRAME_STYLE,
                          name=wx.FrameNameStr):
        '''
        Init the User Interface
        Show the User Interface
        '''

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=((280 * 3) / 3, (200 * 3) / 3),
                              style=style,
                              name=name)

            # TBD - This should NOT change Frame color.
            # It should only change Panel color.
##            self.ForegroundColour = wx.COLOR_YELLOW
##            self.BackgroundColour = wx.COLOR_MAGENTA

        else:

            # Establish character and pixel position of this canvas
            # Set at top left row and column of area to be centered, by
            # default, in the user terminal screen.
            begin_y = -1
            begin_x = -1
            thePos = wx.tsGetPixelValues(begin_x, begin_y)

            # Establish character and pixel size of this canvas
            # for the wxPython application "tsWxGUI_test1.py".
            #
            # VGA Display (640 x 480 pixels) with Courier (8 x 12 pixels)
            # monospaced font characters contains (80 Cols x 40 Rows).

            # Set typical console area
            max_x = -1 # 300
            max_y = -1 # 250
            theSize = wx.tsGetPixelValues(max_x, max_y)

            wx.Frame.__init__(
                self,
                parent,
                id,
                name='Frame',
                title=title,
                pos=thePos,
                size=theSize,
                style=wx.DEFAULT_FRAME_STYLE)

        # Cannot log before GUI started via Frame.
        self.logger.debug(
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

##        self.Center()

##        self.myframe = wx.Frame(None, title='GridSizer')

        #-------------------------------------------------------------------
        # Begin Frame Relocation
        #-------------------------------------------------------------------

        # TBD - Menu Bar Client Area Change in Frame did not
        # reduce height of panel.
        theFrame = self
        menubar = wx.MenuBar(theFrame)
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Centre()
        self.Show()

        theRect = theFrame.Rect
        theClientArea = theFrame.ClientArea
        print('Frame: Rect=%s; ClientArea=%s' % (str(theRect),
                                                 str(theClientArea)))

        #-------------------------------------------------------------------
        # End Frame Relocation
        #-------------------------------------------------------------------

        #-------------------------------------------------------------------
        # Begin Prototype
        #-------------------------------------------------------------------

        # TBD - Menu Bar Client Area Change in Frame did not
        # reduce height of panel.

##         self.Show()

        # panel = wxPanel(
        #             parent,
        #             id=wx.ID_ANY,
        #             pos=wx.DefaultPosition,
        #             size=wx.DefaultSize,
        #             style=wx.DEFAULT_PANEL_STYLE,
        #             name=wx.PanelNameStr)

        parent = self

        print('Automatic Positioning & Sizing for expected layout.')

##        self.LayoutSplashScreen()

        boxVerticalFlag = wx.EXPAND
        boxVertical = wx.BoxSizer(wx.VERTICAL)
        boxVerticalPanel = wx.Panel(parent, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        boxVerticalPanel.SetBackgroundColour("MAGENTA")
        boxVertical.Add(boxVerticalPanel, proportion=1, flag=boxVerticalFlag)
        boxVerticalPanel.SetAutoLayout(True)
        boxVerticalPanel.SetSizer(boxVertical)
        boxVerticalPanel.Layout()

        self.Show(show=True)

        nRows =  5 # 5
        nCols =  4 # 4
        vGap  =  5 # 5
        hGap  =  5 # 5
        gsFlag = wx.ALIGN_CENTER_HORIZONTAL | \
                 wx.ALIGN_CENTER_VERTICAL # wx.EXPAND
        gs = wx.GridSizer(nRows, nCols, vGap, hGap)
        gs.AddMany( [
##            (wx.Button(boxVerticalPanel, label='Cls'),   0, gsFlag),
##            (wx.Button(boxVerticalPanel, label='Bck'),   0, gsFlag),
##            (wx.StaticText(boxVerticalPanel),            0, gsFlag),
##            (wx.Button(boxVerticalPanel, label='Close'), 0, gsFlag),
            (wx.Button(boxVerticalPanel, label='7'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='8'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='9'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='/'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='4'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='5'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='6'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='*'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='1'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='2'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='3'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='-'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='0'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='.'),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='='),     0, gsFlag),
            (wx.Button(boxVerticalPanel, label='+'),     0, gsFlag) ])

        boxVertical.Add(gs, proportion=1, flag=gsFlag)
        boxVerticalPanel.SetSizer(gs)
        gs.Layout()
        theFrame.Show(show=True)

        self.Show(show=True)

        self.logger.debug(
            'End %s (0x%X).' % ('Prototype', self.tsGetTheId()))

    #-----------------------------------------------------------------------
 
    def InitPanelSizer(self,
                       parent,
                       id=wx.ID_ANY,
                       ##                  title=wx.EmptyString,
                       colorBackground=None,
                       colorForeground=None,
                       contents=[],
                       flag=0,
                       name=wx.PanelNameStr,
                       pos=wx.DefaultPosition,
                       size=wx.DefaultSize,
                       sizer=None,
                       style=wx.DEFAULT_PANEL_STYLE):
        '''
        Init the Panel
        Show the Panel
        '''
        if id == wx.ID_ANY:
            id = nextWindowId()

        if colorBackground is None:
            colorBackground = parent.GetBackgroundColour()

        if colorForeground is None:
            colorForeground = parent.GetForegroundColour()
 
        thePanel = wx.Panel(parent, wx.ID_ANY, style=style)
        thePanel.SetForegroundColour(colorForeground)
        thePanel.SetBackgroundColour(colorBackground)
        sizer.Add(thePanel,
                  proportion=2 + len(contents),
                  flag=flag)
        thePanel.SetAutoLayout(True)
        thePanel.SetSizer(sizer)
        thePanel.Layout()

        return (thePanel)

    #-----------------------------------------------------------------------
 
    def InitPanelText(self,
                      panel,
                      contents=[],
                      style=0,
                      makeBitMap=False):
        '''
        Init the Panel Text
        Show the Panel Text
        '''
        theText = wx.TextCtrl(
                panel,
                id=-1,
                value=wx.EmptyString,
                pos=wx.Point(
                    panel.ts_Rect.x + wx.pixelWidthPerCharacter,
                    panel.ts_Rect.y + wx.pixelHeightPerCharacter),
                size=wx.Size(
                    panel.ts_Rect.width - 2 * wx.pixelWidthPerCharacter,
                    panel.ts_Rect.height - 2 * wx.pixelHeightPerCharacter),
                style=0, # wx.TE_MULTILINE |wx.TE_READONLY,
                validator=wx.DefaultValidator,
                name=wx.TextCtrlNameStr)
        for text in contents:
            theText.AppendText(text)
        theText.Show()

        if makeBitMap:
            try:

                mode = 'w'
                bitmapID = open(splashScreenFileName, mode)
    ##            self.ts_Handle.putwin(bitmapID)
                theText.ts_Handle.putwin(bitmapID)
                bitmapID.close()

            except IOError, ioErrorCode:

                print('ERROR: ioErrorCode: %s' % str(ioErrorCode))

            except curses.error, cursesErrorCode:

                print('ERROR: cursesErrorCode: %s' % str(cursesErrorCode))

    #-----------------------------------------------------------------------

    def LayoutSplashScreen(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))
        print('Prototype OnMove: value=%s' % str(pos))

    #-----------------------------------------------------------------------

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        print('Prototype OnQuit: value=%d' % -1)
        self.Close()

    #-----------------------------------------------------------------------
 
    def OnHelp(self, event):
        '''
        Show the help dialog.
        '''
        dlg = wx.MessageDialog(
            self,
            __help__,
            "%s Help" % __title__,
            wx.OK | wx.ICON_INFORMATION)

        dlg.ShowModal()
        dlg.Destroy()
        print('Prototype OnHelp: value=%d' % -1)

    #-----------------------------------------------------------------------

    def OnAbout(self, event):
        '''
        Show the about dialog.
        '''
        dlg = wx.MessageDialog(
            self,
            __header__,
            'About %s' % __title__,
            wx.OK | wx.ICON_INFORMATION)

        dlg.ShowModal()
        dlg.Destroy()
        print('Prototype OnAbout: value=%d' % -1)

    #-----------------------------------------------------------------------

    def WrapupSplashScreen(self):
        '''
        '''
        pass

    #----------------------------------------------------------------------

    # @staticmethod
    def getOptions(self):
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

        parser = OptionParser()

        parser = OptionParser(usage='''%prog [options]...

        Application program to demonstrate various features of the
        Graphical Text User Interface.
        '''
        )

        parser.add_option(
            '-d', '--directory',
            action='store',
            dest='directory',
            default='./',
            type='string',
            help='Directory of source code file(s) [default = ./]')

        parser.add_option(
            '-o', '--outputFileName',
            action='store',
            dest='outputFileName',
            default='tsLinesOfCodeStatistics.txt',
            type='string',
            help='Output statistics file name [default = ' + \
            'tsLinesOfCodeStatistics.txt]')

        (args, options) = parser.parse_args()
        print('ARgs: %s; Options: %s' % (args, options))
        if len(args) != 0:
            parser.print_help()
            sys.exit(1)

        return (args, options)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def exitTest():
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def getEntrySettings(*args, **kw):
        '''
        Return entry point command line keyword-value pair options
        and positional arguments.
        '''
        if False and DEBUG:

            print('\n%s\n' % myParser.getRunTimeTitleVersionDate())

        myParser =  tsOperatorSettingsParser.TsOperatorSettingsParser()

        rawArgsOptions = sys.argv[1:]
        maxArgs = len(rawArgsOptions)
        if False and DEBUG:

            print('\trawArgsOptions=%s' % str(rawArgsOptions))

        (args, options) = myParser.parseCommandLineDispatch()

        if False and DEBUG:

            print('type(args=%s)=%s' % (str(args), type(args)))
            print('type(options=%s)=%s' % (str(options), type(options)))

        if False and DEBUG:

            label = myParser.getRunTimeTitle()

            fmt1 = '%s.getEntrySettings (parameter list): ' % label
            fmt2 = 'args=%s;\n\t\tkw=%s' % (str(args), str(kw))
            print('\n\t%s\n\t\t%s' % (fmt1, fmt2))

            fmt1 = '%s.getEntrySettings (command line argv): ' % label
            fmt2 = 'args=%s' % str(args)
            fmt3 = 'options (unsorted)=%s' % str(options)
            print('\n\t%s\n\t\t%s;\n\t\t%s' % (fmt1, fmt2, fmt3))

            fmt1 = '\n\t%s.getEntrySettings (command line argv): ' % label
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                try:
                    value = '"%s"' % options[key]
                except Exception, errorCode:
                    value = ''
                if text == '':
                    text = '{\n\t\t\t%s: %s' % (str(key), str(value))
                else:
                    text += ', \n\t\t\t%s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        return (args, options)

    #----------------------------------------------------------------------

    def EntryPoint(*args, **kw):
        '''
        '''
        if True and DEBUG:

            print('\n\n\tEntryPoint (parameters:' + \
                  '\n\t\tArgs=%s;\n\t\tOptions=%s' % (
                      str(args), str(kw)))

        if True:
            (args, options) = getEntrySettings(*args, **kw)
        else:
            getEntrySettings(*args, **kw)
            args = myApp.args
            options = myApp.options

        if True and DEBUG:
            print('\n\n\tResults:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
                str(args), str(options)))

    Instance =  tsWxMultiFrameEnv.MultiFrameEnv(

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
#
        enableDefaultCommandLineParser=False, # Disable unless True
#
        guiMessageFilename=None,
        guiMessageRedirect=True,
        guiRequired=True,
        guiTopLevelObject=_Prototype,
        guiTopLevelObjectId=wx.ID_ANY,
        guiTopLevelObjectName=wx.FrameNameStr,
        guiTopLevelObjectParent=None,
        guiTopLevelObjectPosition=wx.DefaultPosition,
        guiTopLevelObjectSize=wx.DefaultSize,
        guiTopLevelObjectStatusBar=None,              # TBD - Implementation
        guiTopLevelObjectStyle=wx.DEFAULT_FRAME_STYLE,
        guiTopLevelObjectTitle='Gui_Test_Units', # __title__,
#
        runTimeEntryPoint=EntryPoint)

    Instance.Wrapper()

