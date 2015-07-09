#! /usr/bin/env python
#"Time-stamp: <04/04/2015  9:41:09 AM rsg>"
'''
test_tsWxRSM.py - Test application program. It demonstrates
features and operation of tsLibCLI and tsLibGUI as applicable
for the Rotor Stress Monitor.
'''
#################################################################
#
# File: test_tsWxRSM.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of tsLibCLI and tsLibGUI as applicable
#    for the Rotor Stress Monitor.
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxRSM.py
#
# Methods:
#
#   None
#
# Modifications:
#
#    2012/07/01 rsg Replaced Dialog by Frame in DiagnosticsTest.
#                   This seeks to demonstrate that application
#                   can create other frames and not just dialogs.
#
#    2015/04/04 rsg Replaced "import tsWxGlobals as wx" by
#                   "import tsWx as wx" and made the associated
#                   Toolkit building block references.
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsWxRSM'
__version__   = '2.1.0'
__date__      = '04/04/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

import os.path
import string
import sys
import time
import traceback

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

from tsWxGTUI_Py2x.tsLibCLI import tsApplication as tsAPP
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWx as wx

#########################################################################
# Begin Test Control Switches

DEBUG = True
VERBOSE = False

centerOnScreenEnabled = False
dialogEnabled = True
exceptionHandlingEnabled = True
frameSizingEnabled = True
redirectEnabled = DEBUG
runTimeTitleEnabled = False
splashScreenEnabled = False
splashScreenSeconds = 0
tracebackEnabled = False

# End Test Control Switches
#########################################################################

#--------------------------------------------------------------------------

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

#--------------------------------------------------------------------------

class _SCADA(wx.Frame):
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
        Get a menubar
        Get a menu for the "file" menu
        Get a menu item for "Quit"
        Bind the "Quit" menu item to the method
        Add "Quit" to the "File" menu
        Add the "File" menu to the menubar
        Get a panel to cover the Frame TBD Needed?
        Create the "Right" panel
        Create the "Left" panel
        Get a box sizer - horizontal
        Add "Left" panel to box sizer
        Add "Right" panel to box sizer
        Set box sizer as sizer for the Frame panel
        Create Status bar
        Center the Frame
        Show the Frame
        '''
        global theStatusBar

        if splashScreenEnabled:
            print('Starting CustomSplashScreen')

            bitmap = None
            splashStyle = 0
            milliseconds = 5000
            parent = None
            id = wx.ID_ANY
            pos=wx.DefaultPosition
            size=wx.DefaultSize
            style = wx.DEFAULT_SPLASHSCREEN_STYLE

            self.theSplashScreen = CustomSplashScreen(
                bitmap,
                splashStyle,
                milliseconds,
                parent,
                id,
                pos,
                size,
                style)

            self.theSplashScreen.CenterOnScreen()

            try:
                bitmapID = file('./tsLibraries/tsWxPkg/src/tsWxPython.txt',
                                'r+')
                theText = ''
                for theLine in bitmapID:
                    # print(theLine)
                    theText += theLine
                self.theSplashScreen.ts_Text.AppendText(theText)
                bitmapID.close()
            except Exception as e:
                print('bitmapID: Exception: %s' % e)

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=(640, 300),
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
            max_x = -1 # 80
            max_y = -1 # 30
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
            'Begin %s (0x%X).' % ('SCADA', self.tsGetTheId()))

        # The following tests do NOT depend on Showing final Frame position.
##        self.menuBarTest()
##        self.panelTest()
##        self.statusBarTest()
##        self.centeringTest()
##        self.scrollBarTest()
        self.DiagnosticsTest()

        # The following tests depend on Showing final Frame position.
##        if splashScreenEnabled:
##            self.theSplashScreen.tsShow()
##            time.sleep(splashScreenSeconds)

        self.Show(show=True)

        self.scada_rsm_display()
##        self.screenTest()

##        self.gaugeTest()
##        self.checkBoxTest()
##        # self.radioBoxTest()
##        self.radioButtonTest()
##        self.redirectionTest()
##        self.colorTest()
##        self.systemSettingsTest()

        # TBD - This should NOT change Frame color.
        # It should only change Panel color.
##        self.ForegroundColour = wx.COLOR_YELLOW
##        self.BackgroundColour = wx.COLOR_MAGENTA

        self.logger.debug(
            'End %s (0x%X).' % ('SCADA', self.tsGetTheId()))

    #-----------------------------------------------------------------------

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))
        print('SCADA OnMove: value=%s' % str(pos))

    #-----------------------------------------------------------------------

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        print('SCADA OnQuit: value=%d' % -1)
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
        print('SCADA OnHelp: value=%d' % -1)

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
        print('SCADA OnAbout: value=%d' % -1)

    #----------------------------------------------------------------------

    def centeringTest(self):
        '''
        '''
        if centerOnScreenEnabled:
            self.Centre()

    #-----------------------------------------------------------------------

    def checkBoxTest(self):
        '''
        '''
        self.baseCheckBoxRect = self.baseGaugeRect

        if checkBoxEnabled:

            if frameSizingEnabled:
                self.baseCheckBoxRect.x += 1 * wx.pixelWidthPerCharacter
                self.baseCheckBoxRect.y -= 1 * wx.pixelHeightPerCharacter
            else:
                self.baseCheckBoxRect.x += 2 * wx.pixelWidthPerCharacter
                self.baseCheckBoxRect.y += 0 * wx.pixelHeightPerCharacter

##            st = wx.StaticText(self,
##                               nextWindowId(),
##                               "This example demonstrates the wx.CheckBox control.",
##                               (10, 10))

            cb1 = wx.CheckBox(
                self,
                nextWindowId(),
                "&R-Align\tCtrl-R",
                (self.baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=wx.ALIGN_RIGHT | wx.NO_BORDER)
            cb1.SetValue(True)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb1)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb1)
 
            cb2 = wx.CheckBox(
                self,
                nextWindowId(),
                "&L-Align\tCtrl-L",
                (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                (12 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=wx.ALIGN_LEFT)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb2)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb2)

            cb3 = wx.CheckBox(
                self,
                nextWindowId(),
                "&Apples\tCtrl-A",
                (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 5 * wx.pixelHeightPerCharacter),
                (12 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb3)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb3)
 
            cb4 = wx.CheckBox(
                self,
                nextWindowId(),
                "&Oranges\tCtrl-O",
                (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 6 * wx.pixelHeightPerCharacter),
                (12 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)
            cb4.SetValue(True)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb4)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb4)

            cb5 = wx.CheckBox(
                self,
                nextWindowId(),
                "&Tristate\tCtrl-T",
                (self.baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=(wx.ALIGN_RIGHT | \
                       wx.NO_BORDER | \
                       wx.CHK_3STATE | \
                       wx.CHK_ALLOW_3RD_STATE_FOR_USER))
            cb5.Set3StateValue(2)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb5)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb5)

            cb6 = wx.CheckBox(
                self,
                nextWindowId(),
                "&Pears\tCtrl-P",
                (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb6)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb6)

        ## self.Show(show=True)

    #-----------------------------------------------------------------------

    def EvtCheckBox(self, event):
        '''
        '''
        self.log.write('EvtCheckBox: %d\n' % event.IsChecked())
        cb = event.GetEventObject()
        if cb.Is3State():
            self.logger.info("\t3StateValue: %s\n" % cb.Get3StateValue())
##        pass

    #-----------------------------------------------------------------------

    def colorTest(self):
        '''
        '''
        if colorTestEnabled:
            print('ColorPairMapCurses' % type(ColorPairMapCurses))

            print('TheColourDatabase' % type(TheColourDatabase))

            print('TheCursesDataBase' % type(TheCursesDataBase))

            print('TheUniqueDatabaseID' % type(TheUniqueDatabaseID))

    #-----------------------------------------------------------------------

    def DiagnosticsTest(self):
        '''
        '''
        theParent = None

        modal = False
        if modal:
            theTitle = "Diagnostics"
        else:
            theTitle = "Diagnostics"

        if dialogEnabled:
            self.dlg1 = wx.Frame(
                theParent,
                nextWindowId(),
                title=theTitle,
##                pos=(0, 0),
                size=(80 * 8, 25 * 12),
                #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                style=wx.DEFAULT_FRAME_STYLE, # & ~wx.CLOSE_BOX,
##                useMetal=useMetal,
                )
            self.dlg1.CenterOnScreen()
            # Setup Dialog-style colors
            newBackgroundColour = self.dlg1.GetForegroundColour()
            newForegroundColour = self.dlg1.GetBackgroundColour()
            self.dlg1.SetBackgroundColour(newBackgroundColour)
            self.dlg1.SetForegroundColour(newForegroundColour)

        text = []

        if True:

            # Graphical User Interface-Style (mouse click is input)
            text += ["                                                                            "]
            text += ["                                                                            "]
##          text += ["On-Line Diagnostic & Maintenance Report Commands                            "]
            text += ["                                                                            "]
            text += ["         On-Line Diagnostic & Maintenance Report Commands                   "]
            text += ["         ------------------------------------------------                   "]
            text += ["         [ ] EXIT On-Line Diagnostic & Maintenance                          "]
            text += ["         [ ] PAUSE CRT Display Update                                       "]
            text += ["         [ ] STOP Logs & RESUME normal operation                            "]
            text += ["         [X] RUN Rotor Stress/Cyclic Life     Log                           "]
            text += ["         [ ] RUN Analog Input    (IN01-IN08)  Log                           "]
            text += ["         [ ] RUN Analog Output   (CV01-CV80)  Log                           "]
            text += ["         [ ] RUN Digital Input   (DCD I/O)    Log                           "]
            text += ["         [ ] RUN Digital Output  (MV01-MV12)  Log                           "]
            text += ["         [ ] RUN Data Base Print              Log                           "]
            text += ["         [ ] RUN Analog Input    (IN01-IN08)  Setup                         "]
            text += ["         [ ] RUN Analog Output   (CV01-CV80)  Setup                         "]
            text += ["         [ ] RUN Digital Input   (DCD I/O)    Setup                         "]
            text += ["         [ ] RUN Digital Output  (MV01-MV12)  Setup                         "]
            text += ["                                                                            "]

        else:

            # Command Line Interface-Style (numeric code is input)
            text += ["                                                                            "]
            text += ["On-Line Diagnostic & Maintenance Report Commands                            "]
            text += ["                                                                            "]
            text += ["         CODE       FUNCTION                                                "]
            text += ["         ------     ----------------------------------------                "]
            text += ["         [  1 ]      STOP On-Line Diagnostic & Maintenance                  "]
            text += ["         [  2 ]     PAUSE CRT Display Update ['CONTINUE']                   "]
            text += ["         [  3 ]      STOP Logs & RESUME normal operation                    "]
            text += ["         [  4 ]     START Rotor Stress/Cyclic Life     Log                  "]
            text += ["         [  5 ]     START Analog Input    (IN01-IN08)  Log                  "]
            text += ["         [  6 ]     START Analog Output   (CV01-CV80)  Log                  "]
            text += ["         [  7 ]     START Digital Input   (DCD I/O)    Log                  "]
            text += ["         [  8 ]     START Digital Output  (MV01-MV12)  Log                  "]
            text += ["         [  9 ]     START Data Base Print              Log                  "]
            text += ["         [ 10 ]     START Analog Input    (IN01-IN08)  Setup                "]
            text += ["         [ 11 ]     START Analog Output   (CV01-CV80)  Setup                "]
            text += ["         [ 12 ]     START Digital Input   (DCD I/O)    Setup                "]
            text += ["         [ 13 ]     START Digital Output  (MV01-MV12)  Setup                "]
            text += ["                                                                            "]

        self.baseDlgRect = self.dlg1.Rect
        print('baseDlgRect=%s' % str(self.baseDlgRect))
        maxRows = (self.baseDlgRect.height / wx.pixelHeightPerCharacter) - 1
        maxCols = (self.baseDlgRect.width / wx.pixelWidthPerCharacter) - 1
        row = 2
        col = 2
        for aline in text:
            if (row < maxRows):
                try:
                    self.dlg1.tsCursesAddStr(
                        col, row, aline[0: min(len(aline), maxCols)], attr=None, pixels=False)
                    self.dlg1.Show()
                except Exception as e:
                    print('Exception: %s; aline: %s' % (e, aline))
                row += 1

    #-----------------------------------------------------------------------

    def gaugeTest(self):
        '''
        '''
        self.baseGaugeRect = self.Rect

        if gaugeEnabled:

            # TBD - Remove temporty adjustment for smallest screens.
            if frameSizingEnabled:
                self.baseGaugeRect.x += 1 * wx.pixelWidthPerCharacter
                self.baseGaugeRect.y += 4 * wx.pixelHeightPerCharacter
            else:
                self.baseGaugeRect.x += 2 * wx.pixelWidthPerCharacter
                self.baseGaugeRect.y += 4 * wx.pixelHeightPerCharacter

            g1 = wx.Gauge(self,
                          nextWindowId(),
                          range=100,
##                          pos=(110, 50),
##                          size=(250, 25),
                          pos=((self.baseGaugeRect.x + \
                                0 * wx.pixelWidthPerCharacter),
                               self.baseGaugeRect.y),
                          size=(3 * wx.pixelWidthPerCharacter,
                                9 * wx.pixelHeightPerCharacter),
                          style=wx.GA_VERTICAL | wx.BORDER_SIMPLE)
            g1.SetRange(7)
            g1.SetValue(5)
            # g1.Pulse()
            # g1.Pulse()

            g2 = wx.Gauge(self,
                          nextWindowId(),
                          range=100,
##                          pos=(110, 50),
##                          size=(250, 25),
                          pos=((self.baseGaugeRect.x + \
                                3 * wx.pixelWidthPerCharacter),
                               (self.baseGaugeRect.y + \
                                0 * wx.pixelHeightPerCharacter)),
                          size=(29 * wx.pixelWidthPerCharacter,
                                3 * wx.pixelHeightPerCharacter),
                          style=wx.GA_HORIZONTAL | wx.BORDER_SIMPLE)
            g2.SetRange(27)
            g2.SetValue(25)
            # g2.Pulse()
            # g2.Pulse()

        ## self.Show(show=True)

    #-----------------------------------------------------------------------

    def menuBarTest(self):
        '''
        '''
        if menuBarEnabled:
            menubar = wx.MenuBar(self)

            # File menu
            theFileMenu = wx.Menu()
            item = theFileMenu.Append(
                wx.ID_ANY,
                text='&Quit\tCtrl+Q',
                help='Exit program')
    ####        self.Bind(wx.EVT_MENU, self.OnQuit, item)

            menubar.Append(theFileMenu, '&File')

            # Help menu
            theHelpMenu = wx.Menu()
            item = theHelpMenu.Append(
                wx.ID_HELP,
                text='&Help\tCtrl+?',
                help='Help for this test')
    ####        self.Bind(wx.EVT_MENU, self.OnHelp, item)

            ## this gets put in the App menu on OS-X
            item = theHelpMenu.Append(
                wx.ID_ABOUT,
                text="&About",
                help="More information About this program")
    ####        self.Bind(wx.EVT_MENU, self.OnAbout, item)
            menubar.Append(theHelpMenu, '&Help')

            self.SetMenuBar(menubar)

    #-----------------------------------------------------------------------

    def panelTest(self):
        '''
        '''
        if panelEnabled:

            panel = wx.Panel(self, nextWindowId())
            self.rightPanel = _RightPanel(panel, nextWindowId())

            leftPanel = _LeftPanel(panel, nextWindowId())

            hbox = wx.BoxSizer()
            hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
            hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)

####        panel.SetSizer(hbox)
####        self.SetMinSize(hbox.GetMinSize())

    #-----------------------------------------------------------------------

    def radioBoxTest(self):
        '''
        '''
        self.baseRadioBoxRect = self.baseGaugeRect

        if radioBoxEnabled:

            if frameSizingEnabled:
                self.baseRadioBoxRect.x += 1 * wx.pixelWidthPerCharacter
                self.baseRadioBoxRect.y -= 1 * wx.pixelHeightPerCharacter
            else:
                self.baseRadioBoxRect.x += 2 * wx.pixelWidthPerCharacter
                self.baseRadioBoxRect.y += 0 * wx.pixelHeightPerCharacter

##            st = wx.StaticText(self,
##                               nextWindowId(),
##                               "This example demonstrates the wx.RadioBox control.",
##                               (10, 10))

            rb1 = wx.RadioBox(
                self,
                nextWindowId(),
                label='Choices',
                pos=(self.baseRadioBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                     self.baseRadioBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                size=(15 * wx.pixelWidthPerCharacter,
                      1 * wx.pixelHeightPerCharacter),
                choices=['am', 'fm', 'cd', 'satelite'],
                majorDimension=0,
                style=wx.ALIGN_RIGHT | wx.NO_BORDER)
 

        ## self.Show(show=True)

    #-----------------------------------------------------------------------

    def radioButtonTest(self):
        '''
        '''
        if False:
            self.baseRadioButtonRect = self.dlg1.Rect
        else:
            self.baseRadioButtonRect = wx.Rect(
                38 * wx.pixelWidthPerCharacter,
                1 * wx.pixelHeightPerCharacter,
                15 * wx.pixelWidthPerCharacter,
                1 * wx.pixelHeightPerCharacter)

        if radioButtonEnabled:

            if frameSizingEnabled:
                self.baseRadioButtonRect.x += 1 * wx.pixelWidthPerCharacter
                self.baseRadioButtonRect.y -= 1 * wx.pixelHeightPerCharacter
            else:
                self.baseRadioButtonRect.x += 2 * wx.pixelWidthPerCharacter
                self.baseRadioButtonRect.y += 0 * wx.pixelHeightPerCharacter

##            st = wx.StaticText(self,
##                               nextWindowId(),
##                               "This example demonstrates the wx.RadioButton control.",
##                               (10, 10))
            if radioBoxEnabled:

                print('Radio Box Test: Rect=%s' % self.baseRadioButtonRect)
                rb1Choices = ['&first\tCtrl-f',
                              '&second\tCtrl-s',
                              '&third\tCtrl-t']
                rb1 = wx.RadioBox(
                    self.dlg1,
                    id=nextWindowId(),
                    label='Vertical Radio Box',
                    pos=(self.dlg1.Rect.x + \
                         2 * wx.pixelWidthPerCharacter,
                         self.dlg1.Rect.y + \
                         2 * wx.pixelHeightPerCharacter),
                    size=(25 * wx.pixelWidthPerCharacter,
                          7 * wx.pixelHeightPerCharacter),
                    choices=rb1Choices,
                    majorDimension=0,
                    style=wx.RA_VERTICAL | wx.BORDER_SIMPLE,
                    validator=wx.DefaultValidator,
                    name=wx.RadioBoxNameStr)
                rb1.SetSelection(2)
##                rb1.Show(True)
##                self.tsUpdateEventAndAcceleratorTables(
##                    wx.EVT_CHECKBOX, self.EvtCheckBox, rb1)
                self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, rb1)
                print('Radio Box Test: rb1=%s' % rb1.ts_Rect)

                rb2Choices = ['f&ourth\tCtrl-o',
                              'f&ifth\tCtrl-i']
                rb2 = wx.RadioBox(
                    self.dlg1,
                    id=nextWindowId(),
                    label='Horizontal Radio Box',
                    pos=(self.dlg1.Rect.x + \
                         2 * wx.pixelWidthPerCharacter,
                         self.dlg1.Rect.y + \
                         10 * wx.pixelHeightPerCharacter),
                    size=(38 * wx.pixelWidthPerCharacter,
                          5 * wx.pixelHeightPerCharacter),
                    choices=rb2Choices,
                    majorDimension=0,
                    style=wx.RA_HORIZONTAL | wx.BORDER_SIMPLE,
                    validator=wx.DefaultValidator,
                    name=wx.RadioBoxNameStr)
                rb2.SetSelection(1)
                rb2.ts_ItemWindow[1].Label = '&Last\tCtrl-L'
##                rb2.Show(True)
##                self.tsUpdateEventAndAcceleratorTables(
##                    wx.EVT_CHECKBOX, self.EvtCheckBox, rb2)
                self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, rb2)
                print('Radio Box Test: rb2=%s' % rb2.ts_Rect)

            else:
                print('Radio Button Test: Rect=%s' % self.baseRadioButtonRect)
                rb1 = wx.RadioButton(
                    self,
                    nextWindowId(),
                    label='Tuner',
                    pos=(self.baseRadioButtonRect.x + \
                         2 * wx.pixelWidthPerCharacter,
                         self.baseRadioButtonRect.y + \
                         4 * wx.pixelHeightPerCharacter),
                    size=(10 * wx.pixelWidthPerCharacter,
                          1 * wx.pixelHeightPerCharacter),
                    style=wx.ALIGN_LEFT | wx.NO_BORDER,
                    validator=wx.DefaultValidator,
                    name='TunerButton')
                rb1.SetValue(True)
##                rb1.Show(True)
                print('Radio Button Test: rb1=%s' % rb1.ts_Rect)
 

##        self.Show(show=True)

    #-----------------------------------------------------------------------

    def scada_rsm_display(self):
        '''
        '''
        text = []

        text += ["----------------------------------------------------------------------------"]
        text += ["1986/02/12  11:30:00       TURBINE AUTOMATIC CONTROL          plant:  TAC-ON"]
        text += ["------------------------------+-----------------------------+---------------"]
        text += ["generator:  ON-LINE at   35mw | turbine:   RESET at 3602rpm |   tac: MONITOR"]
        text += ["loading rate:          MEDIUM | admission: in-PA rate: FAST |   cle:  MEDIUM"]
        text += ["------------------------------+-----------------------------+---------------"]
        text += ["Turbine Location   Temperature  --Stress--  Pred  --Total Life Expenditure--"]
        text += ["                   Shell  Bore  Surf  Bore  Bore  CLE (%)  Zone1 Zone2 Zone3"]
        text += ["HP 1st Stage (HP)   ****  ****  ****  ****  ****    0.000      0     0     0"]
        text += ["RH Bowl      (RH)   ****  ****  ****  ****  ****    0.000      0     0     0"]
        text += ["Crossover    (XO)   ****  ****  ****  ****  ****    0.000      0     0     0"]
        text += ["                   Stabilization until HP 1st Stage TCs Repaired            "]
        text += ["position (%)        pressure (psi)  temperature (^F)     temperature (^F)   "]
        text += ["sv bypass 150  ***  main stm   600  main stm   300  305  rht  stm  **** ****"]
        text += ["cv         35       chest      600  hp shell  **** ****  rh bowl    250  260"]
        text += ["load lim  ***       rht stm   ****  cv inner   305  315  xo shell   190  200"]
        text += ["load set  ***                       cv outer   270  285  tc ref      85     "]
        text += ["speed set ***   speed meter: 3602rpm   load meter:   35mw  valve meter:  35%"]
        text += ["----------------------------------------------------------------------------"]
        text += ["   Operator Hold: OFF | Computer Hold: OFF | OK-to-Select MANUAL Mode       "]
        text += ["----------------------------------------------------------------------------"]

        self.baseRSMRect = self.Rect
        print('baseRSMRect=%s' % str(self.baseRSMRect))
        maxRows = (self.baseRSMRect.height / wx.pixelHeightPerCharacter) - 1
        maxCols = (self.baseRSMRect.width / wx.pixelWidthPerCharacter) - 1
        row = 2
        col = 2
        for aline in text:
            if (row < maxRows):
                try:
                    self.tsCursesAddStr(
                        col, row, aline[0: min(len(aline), maxCols)], attr=None, pixels=False)
                    # self.stdscr.refresh()
                except Exception as e:
                    print('Exception: %s; aline: %s' % (e, aline))
                row += 1
 

    #-----------------------------------------------------------------------

    def OnGroup1Select(self, event):
        '''
        '''
        radio_selected = event.GetEventObject()
        self.logger.info('Group1 %s selected\n' % radio_selected.GetLabel() )

##        for radio, text in self.group1_ctrls:
##            if radio is radio_selected:
##                text.Enable(True)
##            else:
##                text.Enable(False)

    #-----------------------------------------------------------------------

    def OnGroup2Select(self, event):
        '''
        '''
        radio_selected = event.GetEventObject()
        self.logger.info('Group2 %s selected\n' % radio_selected.GetLabel() )

##        for radio, text in self.group1_ctrls:
##            if radio is radio_selected:
##                text.Enable(True)
##            else:
##                text.Enable(False)

    #-----------------------------------------------------------------------

    def screenTest(self):
        '''
        '''
        if screenTestEnabled:
            text = []
            text.append('screenTest: enabled=%s' % screenTestEnabled)
            try:
                from tsWxScreen import Screen as wxScreen
                myScreen = wxScreen(
                    None,
                    id=nextWindowId(),
                    title='ScreenTest',
                    pos=wx.DefaultPosition,
                    size=wx.DefaultSize,
                    style=wx.DEFAULT_FRAME_STYLE,
                    name='My Screen')
                text.append(
                    'screenTest: name="%s"; rect=%s; clientRect=%s' % (
                    myScreen.TermName, myScreen.Rect, myScreen.ClientRect))
                for child in myScreen.Children:
                    text.append(
                        'screenTest: child="%s"; rect=%s; clientRect=%s' % (
                        child.GetLabel(), child.Rect, child.ClientRect))
            except Exception as e:
                text.append('screenTest: exception=%s' % str(e))

            row = 32
            col = 1
            for aline in text:
                try:
                    myScreen.tsCursesAddStr(
                        col, row, aline, attr=None, pixels=False)
                    self.stdscr.refresh()
                except Exception as e:
                    print(aline)
                row += 1

    #-----------------------------------------------------------------------
 
    def redirectionTest(self):
        '''
        '''
        if statusBarEnabled and not statusBarTestDrive:
            for i in range(5):
                msg = 'Update #%d to status.' % i
                print(msg)
                theStatusBar = self.GetStatusBar()
                theStatusBar.SetStatusText(msg)

                # TBD - Perform as part of theStatusBar.Show.
                theStatusBar._tsUpdateStatusText()
                time.sleep(1)

    #-----------------------------------------------------------------------

    def scrollBarTest(self):
        '''
        '''
        if scrollBarEnabled:
            theScrollBarParent = self
            horizontalScrollBar = wx.ScrollBar(
                theScrollBarParent,
                id=nextWindowId(),
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.SB_HORIZONTAL,
                name='Horizontal Scrollbar')
            verticalScrollBar = wx.ScrollBar(
                theScrollBarParent,
                id=nextWindowId(),
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.SB_VERTICAL,
                name='Vertical Scrollbar')
#            scrollBar.CenterOnScreen()

    #-----------------------------------------------------------------------

    def statusBarTest(self):
        '''
        '''
        if statusBarEnabled:
            theStatusBarParent = self
            if statusBarTestDrive:

##            self.sb = CustomStatusBar(self, log)
##            self.SetStatusBar(self.sb)
##            tc = wx.TextCtrl(self,
##                             nextWindowId(),
##                             "",
##                             style=wx.TE_READONLY|wx.TE_MULTILINE)

##            self.SetSize((640, 480))
##            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

                self.sb = CustomStatusBar(theStatusBarParent, None)
                self.SetStatusBar(self.sb)
                theStatusBar = self.sb
            else:
                self.CreateStatusBar()
                theStatusBar = self.GetStatusBar()
                theStatusBar.SetStatusText('Single status statement.')
            self.logger.debug(
                '  theStatusBar: %s.' % theStatusBar)

    #-----------------------------------------------------------------------

    def systemSettingsTest(self):
        '''
        '''
        if systemSettingsTestEnabled:
            dbase = wx.SystemSettings
            dbase.tsSetTerminalPixelRectangle()
            systemLogger = dbase.tsGetTheLogger()
            systemTerminal = dbase.tsGetTheTerminal()
            systemTerminalPixelRectangle = dbase.tsGetTerminalPixelRectangle()
            systemTerminalPixelWidth = systemTerminalPixelRectangle.width
            systemTerminalPixelHeight = systemTerminalPixelRectangle.height
            systemTerminalScreen = dbase.tsGetTheTerminalScreen()
            print('systemTerminalPixelRectangle=%s; x=%s; y=%s' % (
                str(systemTerminalPixelRectangle),
                str(dbase.wxSystemMetric[dbase.wxSYS_SCREEN_X]),
                str(dbase.wxSystemMetric[dbase.wxSYS_SCREEN_Y])))

            for item in dbase.wxSystemColour.keys():
                print('wxSystemColour[%s]=%s' % (
                    str(item), str(dbase.wxSystemColour[item])))

            for item in dbase.wxSystemFeature.keys():
                print('wxSystemFeature[%s]=%s' % (
                    str(item), str(dbase.wxSystemFeature[item])))

            for item in dbase.wxSystemFont.keys():
                print('wxSystemFont[%s]=%s' % (
                    str(item), str(dbase.wxSystemFont[item])))

            for item in dbase.wxSystemMetric.keys():
                print('wxSystemMetric[%s]=%s' % (
                    str(item), str(dbase.wxSystemMetric[item])))

            for item in dbase.wxSystemScreenType.keys():
                print('wxSystemScreenType[%s]=%s' % (
                    str(item), str(dbase.wxSystemScreenType[item])))

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
        print('Args: %s; Options: %s' % (args, options))
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

    Instance =  wx.MultiFrameEnv(

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
        guiTopLevelObject=_SCADA,
        guiTopLevelObjectId=wx.ID_ANY,
        guiTopLevelObjectName=wx.FrameNameStr,
        guiTopLevelObjectParent=None,
        guiTopLevelObjectPosition=wx.DefaultPosition,
        guiTopLevelObjectSize=wx.DefaultSize,
        guiTopLevelObjectStatusBar=None,              # TBD - Implementation
        guiTopLevelObjectStyle=wx.DEFAULT_FRAME_STYLE,
        guiTopLevelObjectTitle='Rotor_Stress_Monitor', # __title__,
#
        runTimeEntryPoint=EntryPoint)

    Instance.Wrapper()

