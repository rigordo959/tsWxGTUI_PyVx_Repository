#! /usr/bin/env python
#"Time-stamp: <05/31/2014  7:14:54 AM rsg>"
'''
test_tsWxWidgets.py - Test application program. It demonstrates
features and operation of the tsWxGTUI toolkit and associated
building block components of tsLibCLI and tsLibGUI.
'''
#################################################################
#
# File: test_tsWxWidgets.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of the tsWxGTUI toolkit and associated
#    building block components of tsLibCLI and tsLibGUI.
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
#     python test_tsWxWidgets.py
#
# Methods:
#
#   None
#
# Modifications:
#
#    2010/xx/xx rsg Added support for redirection for
#                   stdout/stderr to filename.
#
#    2011/03/22 rsg Modified dialogTest to set parent = None.
#
#    2011/12/26 rsg Re-arranged test controls to facilitate
#                   troubleshooting of duplicate main frame
#                   (windows_communicate) buttons (iconize,
#                   maximize and close) which appear during
#                   taskbar focus button initialization.
#
#    2012/01/20 rsg Added DEBUG, Frame and Dialog show logic
#                   to troubleshoot and resolve non-initialized
#                   Dialog PanelLayer instance variable.
#                   Determined that self.Show only creates
#                   Application Frame and children Handles
#                   and PanelLayers. Need self.dlg.Showe to
#                   create Dialog and Children Handles and
#                   PanelLayers,
#
#    2014/04/27 rsg Modified gaugeTest to simulate incrementing
#                   by looping through SetValue and pausing.
#
# ToDo:
#
#   1. Add support for redirection for stdout/stderr to window.
#   2. Show menu help in status bar - works on MS Windows
#   3. Fix minimum size - can resize the Frame too small
#      added fix - doesn't quite work on MacOS, need to check MS Windows
#
#################################################################

__title__     = 'test_tsWxWidgets'
__version__   = '2.4.0'
__date__      = '04/27/2014'
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

#--------------------------------------------------------------------------

import os.path
import sys
import time
import traceback
from optparse import OptionParser

if False and DEBUG:
    # Import wingdbstub only if cygwin platform.
    import platform
    hostOS = platform.system().lower()
    if hostOS.find('cygwin') != -1:
        try:
            import wingdbstub
        except ImportError:
            pass

#--------------------------------------------------------------------------

if True:

    print(__header__)
    time.sleep(5)

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

    import tsWx as wx
    import tsWxMultiFrameEnv

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

except Exception, exceptionCode:

    print('%s: Exception (tsLibGUI); ' % __title__ + \
          'exceptionCode=%s' % str(exceptionCode))

##from tsWxSystemSettings import SystemSettings as wxSystemSettings
##import tsLogger as Logger

#--------------------------------------------------------------------------

#########################################################################
# Begin Test Control Switches

DEBUG = True
VERBOSE = False

centerOnScreenEnabled = False
checkBoxEnabled = True
colorTestEnabled = False
dialogEnabled = True
exceptionHandlingEnabled = True
frameSizingEnabled = True
gaugeEnabled = True
menuBarEnabled = True
panelEnabled = False
radioBoxEnabled = dialogEnabled
radioButtonEnabled = dialogEnabled
redirectEnabled = DEBUG
runTimeTitleEnabled = False
screenTestEnabled = False
scrollBarEnabled = False
statusBarEnabled = True
statusBarTestDrive = True
systemSettingsTestEnabled = False
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

theStatusBar = None

__help__ = '''
This program demonstrates currently supported widgets.

'''

#--------------------------------------------------------------------------

##class CustomSplashScreen(wx.SplashScreen):
##    '''
##    '''
##    def __init__(self,
##                 bitmap,
##                 splashStyle,
##                 milliseconds,
##                 parent,
##                 id,
##                 pos,
##                 size,
##                 style):
##        '''
##        '''
##        wx.SplashScreen.__init__(
##            self,
##            bitmap,
##            splashStyle,
##            milliseconds,
##            parent,
##            id,
##            pos,
##            size,
##            style,
##            ForegroundColour=wx.COLOR_YELLOW,
##            BackgroundColour=wx.COLOR_RED)

#--------------------------------------------------------------------------

class CustomStatusBar(wx.StatusBar):
    '''
    '''
    def __init__(self, parent, log):
        '''
        '''
        wx.StatusBar.__init__(
            self,
            parent,
            id=nextWindowId())

        self.log = log

        if statusBarTestDrive:
 
            # This status bar has three fields
            self.SetFieldsCount(3)
            # Sets the three fields to be relative widths to each other.
            self.SetStatusWidths([-2, -1, -2])
            self.sizeChanged = False
            self.Bind(wx.EVT_SIZE, self.OnSize)
            self.Bind(wx.EVT_IDLE, self.OnIdle)

            # Field 0 ... just text
            self.SetStatusText("1st Customized Field", 0)
    ##        self.ts_Handle.refresh()

            self.SetStatusText("2nd", 1)
    ##        self.ts_Handle.refresh()

            # TBD - Remove Show
    ##        self.ts_Handle.refresh()
    ##        curses.napms(wx.napTimeMilliseconds)

            if True:

                self.SetStatusText("3rd Customized Field", 2)
    ##                self.ts_Handle.refresh()
##                self.Show()
##                self.SetStatusText("4th Customized Field", 2)
##                self.Show()

            else:
                import curses

                t = time.localtime(time.time())
                st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
                self.SetStatusText(st, 2)
                self.ts_Handle.refresh()
                curses.napms(wx.napTimeMilliseconds)

        else:

            if True:
                pass

            else:

                # This will fall into field 1 (the second field)
                self.cb = wx.CheckBox(self, 1001, "toggle clock")
                self.Bind(wx.EVT_CHECKBOX, self.OnToggleClock, self.cb)
                self.cb.SetValue(True)

                # set the initial position of the checkbox
                self.Reposition()

                # We're going to use a timer to drive a 'clock' in the last
                # field.
                self.timer = wx.PyTimer(self.Notify)
                self.timer.Start(1000)
                self.Notify()

    #-----------------------------------------------------------------------

    # Handles events from the timer we started in __init__().
    # We're using it to drive a 'clock' in field 2 (the third field).
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
        self.SetStatusText(st, 2)
        self.log.WriteText("tick...\n")

    #-----------------------------------------------------------------------

    # the checkbox was clicked
    def OnToggleClock(self, event):
        if self.cb.GetValue():
            self.timer.Start(1000)
            self.Notify()
        else:
            self.timer.Stop()

    #-----------------------------------------------------------------------

    def OnSize(self, evt):
        self.Reposition()  # for normal size events

        # Set a flag so the idle time handler will also do the repositioning.
        # It is done this way to get around a buglet where GetFieldRect is not
        # accurate during the EVT_SIZE resulting from a frame maximize.
        self.sizeChanged = True
        print('CustomStatusBar OnSize: Changed=%s' % self.sizeChanged)

    #-----------------------------------------------------------------------

    def OnIdle(self, evt):
        if self.sizeChanged:
            self.Reposition()
            print('CustomStatusBar OnIdle: Changed=%s' % self.sizeChanged)

    #-----------------------------------------------------------------------

    # reposition the checkbox
    def Reposition(self):
        rect = self.GetFieldRect(1)
        self.cb.SetPosition((rect.x+2, rect.y+2))
        self.cb.SetSize((rect.width-4, rect.height-4))
        self.sizeChanged = False

    #-----------------------------------------------------------------------

##class TestCustomStatusBar(wx.Frame):
##    def __init__(self, parent, log):
##        wx.Frame.__init__(self, parent, nextWindowId(), 'Test Custom StatusBar')

##        self.sb = CustomStatusBar(self, log)
##        self.SetStatusBar(self.sb)
##        tc = wx.TextCtrl(self, nextWindowId(), "", style=wx.TE_READONLY|wx.TE_MULTILINE)

##        self.SetSize((640, 480))
##        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    #-----------------------------------------------------------------------

##    def OnCloseWindow(self, event):
##        self.sb.timer.Stop()
##        del self.sb.timer
##        self.Destroy()

###---------------------------------------------------------------------------

##class TestPanel(wx.Panel):
##    def __init__(self, parent, log):
##        self.log = log
##        wx.Panel.__init__(self, parent, nextWindowId())

##        b = wx.Button(self, nextWindowId(), "Show the StatusBar sample", (50,50))
##        self.Bind(wx.EVT_BUTTON, self.OnButton, b)

##    #-----------------------------------------------------------------------

##    def OnButton(self, evt):
##        win = TestCustomStatusBar(self, self.log)
##        win.Show(True)

###---------------------------------------------------------------------------

##class _LeftPanel(wx.Panel):
##    '''
##    Placed on left side of the Frame.
##    Takes up entire left side.

##    Has two buttons: plus and minus
##    Has one static text area used as a title.
##    '''
##    def __init__(self, parent, id):
##        '''
##        Init the panel
##        Create the title text area
##        Get a reference to the right panel text area
##        Create the two buttons
##        Bind the button events to the methods
##        '''
##        wx.Panel.__init__(self, parent, style=wx.SUNKEN_BORDER, name='Left')
##        wx.StaticText(self, nextWindowId(), 'Left Panel')

##        self.text = parent.GetParent().rightPanel.text
##        # TBD - Simulate event update to value of rightPanel.text
##        wx.StaticText(self,
##                      nextWindowId(),
##                      '%s (OnMinus)' % str(int(self.text.GetLabel()) - 1),
##                      (10, 55))

##        button1 = wx.Button(self, nextWindowId(), '+', (10, 30))
##        button2 = wx.Button(self, nextWindowId(), '-', (10, 80))

##        self.Bind(wx.EVT_BUTTON, self.OnPlus, button1)
##        self.Bind(wx.EVT_BUTTON, self.OnMinus, button2)

##    #-----------------------------------------------------------------------

##    def OnPlus(self, event):
##        '''
##        Get the current value
##        Add 1
##        Set the new value
##        '''
##        value = int(self.text.GetLabel())
##        value += 1
##        self.text.SetLabel(str(value))
##        print('LeftPanel OnPlus: value=%d' % value)

##    #-----------------------------------------------------------------------

##    def OnMinus(self, event):
##        '''
##        Get the current value
##        Subtract 1
##        Set the new value
##        '''
##        value = int(self.text.GetLabel())
##        value -= 1
##        self.text.SetLabel(str(value))
##        print('LeftPanel OnMinus: value=%d' % value)

###--------------------------------------------------------------------------

##class _RightPanel(wx.Panel):
##    '''
##    Placed on right side of the Frame.
##    Takes up entire right side.

##    Has one static text area used as a counter
##    Has one static text area used as a title.
##    '''
##    def __init__(self, parent, id):
##        '''
##        Init the panel
##        Create the title text area
##        Create the counter text area
##        '''
##        wx.Panel.__init__(self,
##                          parent,
##                          id,
##                          style=wx.BORDER_SUNKEN,
##                          name='Right')
##        wx.StaticText(self, nextWindowId(), 'Right Panel')
####        self.text = wx.StaticText(self, nextWindowId(), '0', (40, 60))
##        self.text = wx.StaticText(self, nextWindowId(), '0', (40, 55))

#--------------------------------------------------------------------------

class _Communicate(wx.Frame):
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

##        if splashScreenEnabled:
##            print('Starting CustomSplashScreen')

##            bitmap = None
##            splashStyle = 0
##            milliseconds = 5000
##            parent = None
##            id = wx.ID_ANY
##            pos=wx.DefaultPosition
##            size=wx.DefaultSize
##            style = wx.DEFAULT_SPLASHSCREEN_STYLE

##            self.theSplashScreen = CustomSplashScreen(
##                bitmap,
##                splashStyle,
##                milliseconds,
##                parent,
##                id,
##                pos,
##                size,
##                style)

##            self.theSplashScreen.CenterOnScreen()

##            try:
##                bitmapID = file('./tsLibraries/tsWxPkg/src/tsWxPython.txt',
##                                'r+')
##                theText = ''
##                for theLine in bitmapID:
##                    # print(theLine)
##                    theText += theLine
##                self.theSplashScreen.ts_Text.AppendText(theText)
##                bitmapID.close()
##            except Exception, e:
##                print('bitmapID: Exception: %s' % e)

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=(280, 200),
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
            'Begin %s (0x%X).' % ('Communicate', self.tsGetTheId()))

        # The following tests do NOT depend on Showing final Frame position.
        self.menuBarTest()
        self.panelTest()
        self.statusBarTest()
        self.centeringTest()
        self.scrollBarTest()

        if True:
            parentHandle = self.ts_Handle
            parentPanelLayer = self.ts_PanelLayer

        # The following tests depend on Showing final Frame position.

        self.Show(show=True) # Create Application Handle; Show Frame/Children

        self.dialogTest()

        if False:
            if (parentHandle != self.ts_Handle):
                fmt1 = 'dialogTest: post-dialog creation '
                fmt2 = 'parentHandle=%s ' % parentHandle
                fmt3 = 'changed to self.ts_Handle=%s' % self.ts_Handle
                msg = fmt1 + fmt2 + fmt3
                print('DEBUG: %s\n' % msg)

            if (parentPanelLayer != self.ts_PanelLayer):
                fmt1 = 'dialogTest: post-dialog creation '
                fmt2 = 'parentPanelLayer=%s ' % parentPanelLayer
                fmt3 = 'changed to self.ts_PanelLayer=%s' % \
                       self.ts_PanelLayer
                msg = fmt1 + fmt2 + fmt3
                print('DEBUG: %s\n' % msg)

        self.screenTest()

        self.gaugeTest()
        self.checkBoxTest()

        self.Show(show=True) # Update Application Frame/Children

        # self.radioBoxTest()
        self.radioButtonTest()
        self.redirectionTest()

        self.dlg1.Show(show=True)# Create Dialog Handle; Show Dialog/Children


        self.colorTest()
        self.systemSettingsTest()

        self.Show(show=True) # Update Application Frame/Children

        if DEBUG:
            if (self.dlg1.ts_Handle is None):
                fmt1 = 'dialogTest: post-dialog creation '
                fmt2 = 'self.dlg1.ts_Handle=%s' % \
                       self.dlg1.ts_Handle
                msg = fmt1 + fmt2
                print('ERROR: %s\n' % msg)

            if (self.dlg1.ts_PanelLayer is None):
                fmt1 = 'dialogTest: post-dialog creation '
                fmt2 = 'self.dlg1.ts_PanelLayer=%s' % \
                       self.dlg1.ts_PanelLayer
                msg = fmt1 + fmt2
                print('ERROR: %s\n' % msg)

        # TBD - This should NOT change Frame color.
        # It should only change Panel color.
##        self.ForegroundColour = wx.COLOR_YELLOW
##        self.BackgroundColour = wx.COLOR_MAGENTA

        self.logger.debug(
            'End %s (0x%X).' % ('Communicate', self.tsGetTheId()))

    #-----------------------------------------------------------------------

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))
        print('Communicate OnMove: value=%s' % str(pos))

    #-----------------------------------------------------------------------

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        print('Communicate OnQuit: value=%d' % -1)
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
        print('Communicate OnHelp: value=%d' % -1)

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
        print('Communicate OnAbout: value=%d' % -1)

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

        if False and checkBoxEnabled:

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
                # "&R-Align\tCtrl-R",
                "R-Align",
                (self.baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                 self.baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                (12 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=wx.ALIGN_RIGHT | wx.NO_BORDER)
            cb1.SetValue(True)
##            self.tsUpdateEventAndAcceleratorTables(
##                wx.EVT_CHECKBOX, self.EvtCheckBox, cb1)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb1)

        elif checkBoxEnabled:

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
                style=wx.ALIGN_LEFT | wx.NO_BORDER)
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
                style=wx.ALIGN_LEFT | wx.NO_BORDER)
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
                style=wx.ALIGN_LEFT | wx.NO_BORDER)
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
                style=wx.ALIGN_LEFT | wx.NO_BORDER)
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

    def dialogTest(self):
        '''
        '''
        theParent = None

        modal = False
        if modal:
            theTitle = "Dialog Modal"
        else:
            theTitle = "Dialog Non-Modal"

        if dialogEnabled:
            self.dlg1 = wx.Dialog(
                theParent,
                nextWindowId(),
                title=theTitle,
##                pos=(0, 0),
                size=(350, 200),
                #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
##                useMetal=useMetal,
                )
            self.dlg1.CenterOnScreen()

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
            range1 = 7
            g1.SetRange(range1)
            for value1 in range(range1):
                g1.SetValue(value1)
                self.Show(show=True)
                time.sleep(1)
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
            range2 = 27
            g2.SetRange(range2)
            for value2 in range(range2):
                g2.SetValue(value2)
                self.Show(show=True)
                time.sleep(1)
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
            except Exception, e:
                text.append('screenTest: exception=%s' % str(e))

            row = 32
            col = 1
            for aline in text:
                try:
                    myScreen.tsCursesAddStr(
                        col, row, aline, attr=None, pixels=False)
                    self.stdscr.refresh()
                except Exception, e:
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

    def MainLoopSystemSettingsTest(self):
        '''
        '''
        print('MainLoopSystemSettingsTest')
        self.standardCase()
        self.verboseCase()

    #----------------------------------------------------------------------

    def standardCase(self):
        '''
        '''

        #------------------------------------------------------------------

        print('\n%s Begin Standard Cases %s' % ('-' * 10, '-' * 30))

        #------------------------------------------------------------------

        print('\n\n***** Case of GetColour *****')
        keyList = sorted(wxSystemSettings.wxSystemColour.keys())
        for theKey in keyList:
            theValue = self.settings.GetColour(theKey)
            print('\t%3d %s' % (theKey, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Case of GetFont *****')
        keyList = sorted(wxSystemSettings.wxSystemFont.keys())
        for theKey in keyList:
            theValue = self.settings.GetFont(theKey)
            print('\t%3d %s' % (theKey, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Case of GetMetric *****')
        keyList = sorted(wxSystemSettings.wxSystemMetric.keys())
        for theKey in keyList:
            theValue = self.settings.GetMetric(theKey,
                                               win=None)
            print('\t%3d %s' % (theKey, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Case of HasFeature *****')
        keyList = sorted(wxSystemSettings.wxSystemFeature.keys())
        for theKey in keyList:
            theValue = self.settings.HasFeature(theKey)
            print('\t%3d %s' % (theKey, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Case of GetScreenType *****')
        theValue = self.settings.GetScreenType()
        print('\t    %s' % theValue)

        #------------------------------------------------------------------

        print('\n\n***** Case of SetScreenType *****')
        for screen in self.settings.wxSystemScreenType:
            self.settings.SetScreenType(screen)
##            theValue = self.settings.GetScreenType()
            x = self.settings.wxSystemScreenType[screen]
            theName = x[0]
            theValue = x[1]
            print('\t    %s for %s (No Change Allowed)' % \
                  (theValue, screen))

        #------------------------------------------------------------------
        print('\n%s End   Standard Cases %s' % ('-' * 10, '-' * 30))

    #----------------------------------------------------------------------

    def verboseCase(self):
        '''
        '''

        #------------------------------------------------------------------

        print('\n%s Begin Verbose  Cases %s' % ('-' * 10, '-' * 30))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of GetColour *****')
        keyList = sorted(wxSystemSettings.wxSystemColour.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.GetColour(theKey, verbose=True)
            print('\t%3d %40s %s' % (theKey, theName, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of GetFont *****')
        keyList = sorted(wxSystemSettings.wxSystemFont.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.GetFont(theKey, verbose=True)
            print('\t%3d %40s %s' % (theKey, theName, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of GetMetric *****')
        keyList = sorted(wxSystemSettings.wxSystemMetric.keys())
        parent = None
        winFrame = wx.Frame(
            parent,
            id=wx.ID_ANY,
            title='Get_Metric',
            pos=wx.Point(380, 232),
            size=wx.Size(240, 100),
            style=wx.DEFAULT_FRAME_STYLE,
            name=wx.FrameNameStr)
        winFrame.ForegroundColour = wx.COLOR_WHITE
        winFrame.BackgroundColour = wx.COLOR_RED
        for theKey in keyList:
            (theName, theValue) = self.settings.GetMetric(theKey,
                                                          win=winFrame,
                                                          verbose=True)
            print('\t%3d %40s %s' % (theKey, theName, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of HasFeature *****')
        keyList = sorted(wxSystemSettings.wxSystemFeature.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.HasFeature(theKey, verbose=True)
            print('\t%3d %40s %s' % (theKey, theName, theValue))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of GetScreenType *****')
        (theName, theValue) = self.settings.GetScreenType(verbose=True)
        print('\t    %40s %s' % (theName,theValue))

        #------------------------------------------------------------------

        print('\n\n***** Verbose Case of SetScreenType *****')
        for screen in self.settings.wxSystemScreenType:
            self.settings.SetScreenType(screen)
##            (theName, theValue) = self.settings.GetScreenType(verbose=True)
            x = self.settings.wxSystemScreenType[screen]
            theName = x[0]
            theValue = x[1]
            print('\t    %40s %s for %s (No Change Allowed)' % \
                  (theName, theValue, screen))

        #------------------------------------------------------------------

        print('\n%s End   Verbose  Cases %s' % ('-' * 10, '-' * 30))

    #----------------------------------------------------------------------

    def systemSettingsTest(self):
        '''
        '''
        if systemSettingsTestEnabled:
            self.settings = wxSystemSettings()
            self.MainLoopSystemSettingsTest()
##            dbase = wx.SystemSettings
##            dbase.tsSetTerminalPixelRectangle()
##            systemLogger = dbase.tsGetTheLogger()
##            systemTerminal = dbase.tsGetTheTerminal()
##            systemTerminalPixelRectangle = dbase.tsGetTerminalPixelRectangle()
##            systemTerminalPixelWidth = systemTerminalPixelRectangle.width
##            systemTerminalPixelHeight = systemTerminalPixelRectangle.height
##            systemTerminalScreen = dbase.tsGetTheTerminalScreen()
##            print('systemTerminalPixelRectangle=%s; x=%s; y=%s' % (
##                str(systemTerminalPixelRectangle),
##                str(dbase.wxSystemMetric[dbase.wxSYS_SCREEN_X]),
##                str(dbase.wxSystemMetric[dbase.wxSYS_SCREEN_Y])))

##            for item in dbase.wxSystemColour.keys():
##                print('wxSystemColour[%s]=%s' % (
##                    str(item), str(dbase.wxSystemColour[item])))

##            for item in dbase.wxSystemFeature.keys():
##                print('wxSystemFeature[%s]=%s' % (
##                    str(item), str(dbase.wxSystemFeature[item])))

##            for item in dbase.wxSystemFont.keys():
##                print('wxSystemFont[%s]=%s' % (
##                    str(item), str(dbase.wxSystemFont[item])))

##            for item in dbase.wxSystemMetric.keys():
##                print('wxSystemMetric[%s]=%s' % (
##                    str(item), str(dbase.wxSystemMetric[item])))

##            for item in dbase.wxSystemScreenType.keys():
##                print('wxSystemScreenType[%s]=%s' % (
##                    str(item), str(dbase.wxSystemScreenType[item])))

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
        guiTopLevelObject=_Communicate,
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

