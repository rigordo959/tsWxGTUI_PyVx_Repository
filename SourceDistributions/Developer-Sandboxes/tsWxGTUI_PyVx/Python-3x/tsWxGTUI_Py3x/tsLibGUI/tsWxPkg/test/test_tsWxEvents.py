#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:38:48 AM rsg>"
'''
test_tsWxEvents.py - Application program to test some events.
'''
#################################################################
#
# File: test_tsWxEvents.py.py
#
# Purpose:
#
#    Application program to test some events.
#
#
#    1. Frame
#    2. one main panel added to Frame
#    3. two panels, one left and one right, added to main panel
#    4. two buttons in the left panel (plus and minus)
#    5. one text widget in the right panel used as a counter
#    6. the plus button will add one to the counter
#    7. the minus button will subtract one from the counter
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
#     python test_tsWxEvents.py
#
# Methods:
#
# ToDo:
#
# Modifications:
#
#
#################################################################

import sys
import time
import traceback

DEBUG = True

if False and DEBUG:
    # Import wingdbstub only if cygwin platform.
    import platform
    hostOS = platform.system().lower()
    if hostOS.find('cygwin') != -1:
        try:
            import wingdbstub
        except ImportError:
            pass

try:
    import tsLibraries
except ImportError:
    pass

import tsApplication as tsAPP
import tsExceptions as tse

__title__     = 'test_tsWxEvents'
__version__   = '0.0.1'
__date__      = '05/29/2009'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2009 TeamSTARS. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

#########################################################################
# Begin Test Control Switches
DEBUG = True
VERBOSE = False

redirectEnabled = DEBUG
if redirectEnabled:
    if VERBOSE:
        redirectedFileName = 'redirectedFile.log'
    else:
        redirectedFileName = None
else:
    redirectedFileName = None

exceptionHandlingEnabled = True
frameSizingEnabled = True
splashScreenSeconds = 0

centerOnScreenEnabled = True
checkBoxEnabled = True
dialogEnabled = False
gaugeEnabled = True
menuBarEnabled = True
panelEnabled = False
scrollBarEnabled = True
statusBarEnabled = True
statusBarTestDrive = True
tracebackEnabled = False
# End Test Control Switches
#########################################################################

theStatusBar = None

__help__ = '''
This program shows communications between widgets

The buttons in the LEFT PANEL cause the counter in the
RIGHT PANEL to increment and decrement.

The Graphical Interface is composed:

               Screen
               Frame
               Panel
  Left Panel          Right Panel
  Button (+)          Text
  Button (-)

'''

#--------------------------------------------------------------------------

print(__header__)
print('  wxPython Emulation')
print('      exceptionHandlingEnabled: %s' % exceptionHandlingEnabled)
print('                menuBarEnabled: %s' % menuBarEnabled)
print('                  panelEnabled: %s' % panelEnabled)
print('              statusBarEnabled: %s' % statusBarEnabled)
print('            statusBarTestDrive: %s' % statusBarTestDrive)
print('         centerOnScreenEnabled: %s' % centerOnScreenEnabled)
print('               checkBoxEnabled: %s' % checkBoxEnabled)
print('                 dialogEnabled: %s' % dialogEnabled)
print('            frameSizingEnabled: %s' % frameSizingEnabled)
print('                  gaugeEnabled: %s' % gaugeEnabled)
print('               redirectEnabled: %s' % redirectEnabled)
print('            redirectedFileName: %s' % redirectedFileName)
print('              scrollBarEnabled: %s' % scrollBarEnabled)
print('           splashScreenSeconds: %s' % splashScreenSeconds)
print('              tracebackEnabled: %s' % tracebackEnabled)

print(__help__)
time.sleep(splashScreenSeconds)

if not exceptionHandlingEnabled:

    import tsWx as wx

else:

    try:

        import tsWx as wx

    except Exception, theTsWxImportError:

        _stdout = sys.stdout
        _stderr = sys.stderr

        _stderr.write('%s' % __header__)

        exitStatus = tse.NONERROR_ERROR_CODE
        msg = tse.NO_ERROR

        if isinstance(theTsWxImportError, tse.TsExceptions):

            exitStatus = theTsWxImportError.exitCode
            msg = '%s. [ExitCode #%d]' % (
                str(theTsWxImportError).replace("'", ""), exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                tse.displayError(theTsWxImportError)

        elif isinstance(theTsWxImportError, ImportError):

            exitStatus = 128 # TBD - tse.INVALID_ERROR_CODE
            msg = '%s. %s. %s. [ExitCode #%d]' % (
                tse.USER_INTERFACE_EXCEPTION,
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE,
                theTsWxImportError,
                exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        else:

            exitStatus = tse.INVALID_ERROR_CODE
            msg = "Unexpected error: %s [ExitCode #%d]" % (
                sys.exc_info()[0], exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        _stderr.write('\n%s\n' % msg)

        # Return (exitStatus)
        sys.exit(exitStatus)
# Event enabler
useEvents = wx.useEvents

#--------------------------------------------------------------------------
class myTimer(wx.Timer):

    def __init__(self):
        '''
        TBD - is owner = None right, needed?
        '''
        wx.Timer.__init__(self, None)
 
    def Notify(self):
        print('Hello from myTimer')
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
            id=-1)

        self.log = log

        if statusBarTestDrive:
 
            # This status bar has three fields
            self.SetFieldsCount(3)
            # Sets the three fields to be relative widths to each other.
            self.SetStatusWidths([-2, -1, -2])
            self.sizeChanged = False
            if useEvents:
                self.Bind(wx.EVT_SIZE, self.OnSize)
                self.Unbind(wx.EVT_SIZE)
                self.Bind(wx.EVT_IDLE, self.OnIdle)
 
                timer = myTimer()
                timerOwner = timer.Owner
                timerId = timer.Id
                timer.Start(1000)
 
                timerx = wx.Timer(self)
                self.Bind(wx.EVT_TIMER, self.OnTimer, timerx)
                timerx.Start(1000)

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

    # Handles events from the timer we started in __init__().
    # We're using it to drive a 'clock' in field 2 (the third field).
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
        self.SetStatusText(st, 2)
        self.log.WriteText("tick...\n")


    def OnTimer(self, evt):
        print('Hello from OnTimer')
 
        # the checkbox was clicked
    def OnToggleClock(self, event):
        if self.cb.GetValue():
            self.timer.Start(1000)
            self.Notify()
        else:
            self.timer.Stop()


    def OnSize(self, evt):
        self.Reposition()  # for normal size events

        # Set a flag so the idle time handler will also do the repositioning.
        # It is done this way to get around a buglet where GetFieldRect is not
        # accurate during the EVT_SIZE resulting from a frame maximize.
        self.sizeChanged = True


    def OnIdle(self, evt):
        if self.sizeChanged:
            self.Reposition()


    # reposition the checkbox
    def Reposition(self):
        rect = self.GetFieldRect(1)
        self.cb.SetPosition((rect.x+2, rect.y+2))
        self.cb.SetSize((rect.width-4, rect.height-4))
        self.sizeChanged = False



##class TestCustomStatusBar(wx.Frame):
##    def __init__(self, parent, log):
##        wx.Frame.__init__(self, parent, -1, 'Test Custom StatusBar')

##        self.sb = CustomStatusBar(self, log)
##        self.SetStatusBar(self.sb)
##        tc = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_MULTILINE)

##        self.SetSize((640, 480))
##        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

##    def OnCloseWindow(self, event):
##        self.sb.timer.Stop()
##        del self.sb.timer
##        self.Destroy()

###---------------------------------------------------------------------------

##class TestPanel(wx.Panel):
##    def __init__(self, parent, log):
##        self.log = log
##        wx.Panel.__init__(self, parent, -1)

##        b = wx.Button(self, -1, "Show the StatusBar sample", (50,50))
##        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


##    def OnButton(self, evt):
##        win = TestCustomStatusBar(self, self.log)
##        win.Show(True)

#---------------------------------------------------------------------------

class _LeftPanel(wx.Panel):
    '''
    Placed on left side of the Frame.
    Takes up entire left side.

    Has two buttons: plus and minus
    Has one static text area used as a title.
    '''
    def __init__(self, parent, id):
        '''
        Init the panel
        Create the title text area
        Get a reference to the right panel text area
        Create the two buttons
        Bind the button events to the methods
        '''
        wx.Panel.__init__(self, parent, style=wx.SUNKEN_BORDER, name='Left')
        wx.StaticText(self, -1, 'Left Panel')

        self.text = parent.GetParent().rightPanel.text
        # TBD - Simulate event update to value of rightPanel.text
        wx.StaticText(self,
                      -1,
                      '%s (OnMinus)' % str(int(self.text.GetLabel()) - 1),
                      (10, 55))

        button1 = wx.Button(self, -1, '+', (10, 30))
        button2 = wx.Button(self, -1, '-', (10, 80))

##        self.Bind(wx.EVT_BUTTON, self.OnPlus, button1)
##        self.Bind(wx.EVT_BUTTON, self.OnMinus, button2)

    def OnPlus(self, event):
        '''
        Get the current value
        Add 1
        Set the new value
        '''
        value = int(self.text.GetLabel())
        value += 1
        self.text.SetLabel(str(value))

    def OnMinus(self, event):
        '''
        Get the current value
        Subtract 1
        Set the new value
        '''
        value = int(self.text.GetLabel())
        value -= 1
        self.text.SetLabel(str(value))

#--------------------------------------------------------------------------

class _RightPanel(wx.Panel):
    '''
    Placed on right side of the Frame.
    Takes up entire right side.

    Has one static text area used as a counter
    Has one static text area used as a title.
    '''
    def __init__(self, parent, id):
        '''
        Init the panel
        Create the title text area
        Create the counter text area
        '''
        wx.Panel.__init__(self,
                          parent,
                          id,
                          style=wx.BORDER_SUNKEN,
                          name='Right')
        wx.StaticText(self, -1, 'Right Panel')
##        self.text = wx.StaticText(self, -1, '0', (40, 60))
        self.text = wx.StaticText(self, -1, '0', (40, 55))

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

    def __init__(self,
                 parent,
                 id=-1,
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

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=-1,
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

        if panelEnabled:

            panel = wx.Panel(self, -1)
            self.rightPanel = _RightPanel(panel, -1)

            leftPanel = _LeftPanel(panel, -1)

            hbox = wx.BoxSizer()
            hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
            hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)

####        panel.SetSizer(hbox)
####        self.SetMinSize(hbox.GetMinSize())

        if statusBarEnabled:
            theStatusBarParent = self
            if statusBarTestDrive:

##            self.sb = CustomStatusBar(self, log)
##            self.SetStatusBar(self.sb)
##            tc = wx.TextCtrl(self,
##                             -1,
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

        if centerOnScreenEnabled:
            self.Centre()

        if scrollBarEnabled:
            theScrollBarParent = self
            horizontalScrollBar = wx.ScrollBar(
                theScrollBarParent,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.SB_HORIZONTAL)
            verticalScrollBar = wx.ScrollBar(
                theScrollBarParent,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.SB_VERTICAL)
#            scrollBar.CenterOnScreen()

        if dialogEnabled:
            dlg = wx.Dialog(
                self,
                -1,
                "Sample Dialog",
                size=(350, 200),
                #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
##                useMetal=useMetal,
                )
            dlg.CenterOnScreen()

        self.Show(show=True)

        baseGaugeRect = self.Rect
        if gaugeEnabled:

            # TBD - Remove temporty adjustment for smallest screens.
            if frameSizingEnabled:
                baseGaugeRect.x += 1 * wx.pixelWidthPerCharacter
                baseGaugeRect.y += 4 * wx.pixelHeightPerCharacter
            else:
                baseGaugeRect.x += 2 * wx.pixelWidthPerCharacter
                baseGaugeRect.y += 4 * wx.pixelHeightPerCharacter

            g1 = wx.Gauge(self,
                          -1,
                          range=100,
##                          pos=(110, 50),
##                          size=(250, 25),
                          pos=((baseGaugeRect.x + \
                                0 * wx.pixelWidthPerCharacter),
                               baseGaugeRect.y),
                          size=(3 * wx.pixelWidthPerCharacter,
                                9 * wx.pixelHeightPerCharacter),
                          style=wx.GA_VERTICAL | wx.BORDER_SIMPLE)
            g1.SetRange(7)
            g1.SetValue(5)

            g2 = wx.Gauge(self,
                          -1,
                          range=100,
##                          pos=(110, 50),
##                          size=(250, 25),
                          pos=((baseGaugeRect.x + \
                                3 * wx.pixelWidthPerCharacter),
                               (baseGaugeRect.y + \
                                0 * wx.pixelHeightPerCharacter)),
                          size=(29 * wx.pixelWidthPerCharacter,
                                3 * wx.pixelHeightPerCharacter),
                          style=wx.GA_HORIZONTAL | wx.BORDER_SIMPLE)
            g2.SetRange(27)
            g2.SetValue(25)

        self.Show(show=True)

        baseCheckBoxRect = baseGaugeRect
        if checkBoxEnabled:

            if frameSizingEnabled:
                baseCheckBoxRect.x += 1 * wx.pixelWidthPerCharacter
                baseCheckBoxRect.y -= 1 * wx.pixelHeightPerCharacter
            else:
                baseCheckBoxRect.x += 2 * wx.pixelWidthPerCharacter
                baseCheckBoxRect.y += 0 * wx.pixelHeightPerCharacter

##            st = wx.StaticText(self,
##                               -1,
##                               "This example demonstrates the wx.CheckBox control.",
##                               (10, 10))

            cb1 = wx.CheckBox(
                self,
                -1,
                "R-Align",
                (baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=wx.ALIGN_RIGHT | wx.NO_BORDER)
            cb1.SetValue(True)
 
            cb2 = wx.CheckBox(
                self,
                -1,
                "L-Align",
                (baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=wx.ALIGN_LEFT)

            cb3 = wx.CheckBox(
                self,
                -1,
                "Apples",
                (baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 5 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)
 
            cb4 = wx.CheckBox(
                self,
                -1,
                "Oranges",
                (baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 6 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)
            cb4.SetValue(True)

            cb5 = wx.CheckBox(
                self,
                -1,
                "Tristate",
                (baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                style=(wx.ALIGN_RIGHT | \
                       wx.NO_BORDER | \
                       wx.CHK_3STATE | \
                       wx.CHK_ALLOW_3RD_STATE_FOR_USER))
            cb5.Set3StateValue(2)

            cb6 = wx.CheckBox(
                self,
                -1,
                "Pears",
                (baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
                 baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
                (15 * wx.pixelWidthPerCharacter,
                 1 * wx.pixelHeightPerCharacter),
                wx.NO_BORDER)

        self.Show(show=True)

        if statusBarEnabled and not statusBarTestDrive:
            for i in range(5):
                msg = 'Update #%d to status.' % i
                print(msg)
                theStatusBar = self.GetStatusBar()
                theStatusBar.SetStatusText(msg)

                # TBD - Perform as part of theStatusBar.Show.
                theStatusBar._tsUpdateStatusText()
                time.sleep(1)

        # TBD - This should NOT change Frame color.
        # It should only change Panel color.
##        self.ForegroundColour = wx.COLOR_YELLOW
##        self.BackgroundColour = wx.COLOR_MAGENTA

        self.logger.debug(
            'End %s (0x%X).' % ('Communicate', self.tsGetTheId()))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        self.Close()
 
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

#--------------------------------------------------------------------------

class guiAPP(wx.App):
    '''
    '''
    def __init__(self, redirect=True, filename=None):
        '''
        Used.
        '''
        print("App __init__")
        wx.App.__init__(self, redirect=redirect, filename=filename)

        # TBD - The next two lines enable the statusBarTestDrive simulation.
        self.theFrame = None
        self.theStatusBar = None

    def OnInit(self):
        '''
        This must be provided by the application, and will usually create the
        application main window, optionally calling {wxApp::SetTopWindow}.
        You may use {OnExit} to clean up anything initialized here, provided
        that the function returns true.

        Notice that if you want to to use the command line processing provided
        by wxWidgets you have to call the base class version in the derived
        class OnInit().

        Return true to continue processing, false to exit the application
        immediately.
        '''
        print(__header__)
        print('OnInit')
        print('OnInit #2')

        self.theFrame = _Communicate(None,
                                     id=-1,
                                     title='widgets communicate',
                                     name='_Communicate')
##        self.theFrame.Show()
        self.SetTopWindow(self.theFrame)
 
        print('A pretend error message', file=sys.stderr)

        return True

    def OnExit(self):
        '''
        Override this member function for any processing which needs to be
        done as the application is about to exit. OnExit is called after
        destroying all application windows and controls, but before wxWidgets
        cleanup. Note that it is not called at all if {OnInit} failed.

        The return value of this function is currently ignored, return the
        same value as returned by the base class method if you override it.
        '''
        print('OnExit')

#--------------------------------------------------------------------------

class cliAPP(tsAPP.TsApplication):
    '''
    Class to establish the application specific control components.
    '''
    def __init__(self, *args, **kw):
        '''
        Add our main entry point to kw
        Init tsApp
        '''
        kw['main'] = self.main
        tsAPP.TsApplication.__init__(self, *args, **kw)

    def main(self):
        '''
        Get a wx App
        Build the communicate Frame
        Enter wx main loop
        '''
        # TBD - Enable redirection
        app = guiAPP(redirect=redirectEnabled,
                     filename=redirectedFileName)
 
        if statusBarTestDrive:
            app.theStatusBar = theStatusBar

        print("Before MainLoop")
        app.MainLoop()
        print("After MainLoop")

#--------------------------------------------------------------------------

if __name__ == '__main__':
    # Create my App
    # Run the main entry point
    #
    # Remember original stdout and stderr
    #  WxPython makes them graphical
    _stdout = sys.stdout
    _stderr = sys.stderr

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:
        theApplication = cliAPP(
            header=__header__,
            mainTitleVersionDate=mainTitleVersionDate,
            title=__title__,
            version=__version__,
            date=__date__,
            logs=[])
##            logs=[wx.cliLoggerNameStr, wx.guiLoggerNameStr])

        theApplication.runMain()

    except Exception, e:
        if isinstance(e, tse.TsExceptions):
            msg = str(e).replace("'", "")
            tse.displayError(e)
            exitStatus = e.exitCode
        else:
            msg = None
            _stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

##    print __header__
#    _stdout.write(__header__)

    if msg == tse.NO_ERROR:
        _stdout.write(msg + '\n')

    elif msg is not None:
        _stderr.write(msg + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)

