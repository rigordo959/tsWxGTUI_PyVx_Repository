#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:38:54 AM rsg>"
'''
test_tsWxFieldMarkup.py - Application program to demonstrate the
text field markup features of the Graphical Text User Interface.
'''
#################################################################
#
# File: test_tsWxFieldMarkup.py
#
# Purpose:
#
#    Application program to demonstrate the text field markup
#    features of the Graphical Text User Interface.
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
#     python test_tsWxFieldMarkup.py
#
# Methods:
#
#   None
#
# ToDo:
#
#   None
#
# Modifications:
#
#   None
#
#################################################################

__title__     = 'test_tsWxFieldMarkup'
__version__   = '1.0.0'
__date__      = '06/11/2012'
__authors__   = 'Richard S. Gordon, a.k.a. Software Gadgetry'
__copyright__ = 'Copyright (c) 2012 Software Gadgetry. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

import os.path
import sys
import time
import traceback
from optparse import OptionParser

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
##import tsLogger as Logger

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

runTimeTitleEnabled = False
exceptionHandlingEnabled = True
frameSizingEnabled = True
splashScreenSeconds = 0

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

theStatusBar = None

__help__ = '''
This program demonstrates currently supported features.

'''

#--------------------------------------------------------------------------

if not exceptionHandlingEnabled:

    try:
        import wx
    except ImportError as wxImportError:
        import tsWx as wx

else:

    try:

        import tsWx as wx

    except Exception as theTsWxImportError:

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

        if frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=((83 * wx.pixelWidthPerCharacter),
                                    (70 * wx.pixelHeightPerCharacter)),
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

        # The following tests depend on Showing final Frame position.
##        if splashScreenEnabled:
##            self.theSplashScreen.tsShow()
##            time.sleep(splashScreenSeconds)

##        self.myframe = wx.Frame(None, title='FieldMarkup')

        #-------------------------------------------------------------------
        # Begin Frame Relocation
        #-------------------------------------------------------------------

        # TBD - Menu Bar Client Area Change in Frame did not
        # reduce height of panel.
        theFrame = self
##        menubar = wx.MenuBar(theFrame)
##        fileMenu = wx.Menu()
##        menubar.Append(fileMenu, '&File')
##        self.SetMenuBar(menubar)

##        self.Centre()
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

        parent = self
        self.InitUI(parent,
                    id=wx.ID_ANY,
                    title=wx.EmptyString,
                    pos=wx.DefaultPosition,
                    size=wx.DefaultSize,
                    style=wx.DEFAULT_FRAME_STYLE,
                    name=wx.FrameNameStr)
        self.Show()

        theMarkupKeys = list(wx.ThemeToUse['StdioMarkup'].keys())
        for theKey in sorted(theMarkupKeys):
##        for theKey in theMarkupKeys:

            theMarkup = wx.ThemeToUse['StdioMarkup'][theKey]
            theMarkupText = 'Logger Key is %s: with %s.\n' % (
                theKey, str(theMarkup))

            print(theMarkupText)

        self.logger.debug(
            'End %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

    #-----------------------------------------------------------------------
 
    def InitUI(self,
               parent,
               id=wx.ID_ANY,
               title=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.DEFAULT_FRAME_STYLE,
               name=wx.FrameNameStr):
        '''
        Init the Panels
        Show the Panels
        '''
        parent = self

        print('Automatic Positioning & Sizing for expected layout.')

##        parentForegroundColour = parent.GetForegroundColour()
##        parentBackgroundColour = parent.GetBackgroundColour()

##        titleForegroundColour = parentBackgroundColour
##        titleBackgroundColour = parentForegroundColour

##        headerForegroundColour = parentForegroundColour
##        headerBackgroundColour = parentBackgroundColour

##        subHeaderForegroundColour = parentForegroundColour
##        subHeaderBackgroundColour = parentBackgroundColour

##        dataForegroundColour = parentForegroundColour
##        dataBackgroundColour = parentBackgroundColour

##        markupTitle = {
##            'Foreground':wx.COLOR_YELLOW,
##            'Background':parentBackgroundColour,
##            'Attributes':[wx.DISPLAY_STANDOUT, wx.DISPLAY_UNDERLINE]
##            }

        panelContents1 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        panelContents2 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        panelContents3 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        panelContents4 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        panelContents5 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        panelContents6 = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ']

        boxVerticalFlag = wx.EXPAND
        boxVertical = wx.BoxSizer(wx.VERTICAL)

        panel1 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="WHITE",
            contents=panelContents1,
            flag=boxVerticalFlag,
            name="TEST_INFO_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        markup1 = {"Background":"BLACK",
                   "Foreground":"WHITE",
                   "Attributes":[wx.DISPLAY_NORMAL]}

        panel2 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="YELLOW",
            colorForeground="BLACK",
            contents=panelContents2,
            flag=boxVerticalFlag,
            name="CE_INFO_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        markup2 = {"Background":"BLACK",
                   "Foreground":"YELLOW",
                   "Attributes":[wx.DISPLAY_NORMAL]}

##        panel3 = self.InitPanelSizer(
##            parent,
####            id=wx.ID_ANY,
##            colorBackground="BLACK",
##            colorForeground="YELLOW",
##            contents=panelContents3,
##            flag=boxVerticalFlag,
##            name="PROCESS_INFO_DISPLAY",
####            pos=wx.DefaultPosition,
####            size=wx.DefaultSize,
##            sizer=boxVertical,
##            style=wx.BORDER_SIMPLE
##            )

##        markup3 = {"Background":"BLACK",
##                   "Foreground":"YELLOW",
##                   "Attributes":[wx.DISPLAY_NORMAL]}

        panel4 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="CYAN",
            contents=panelContents4,
            flag=boxVerticalFlag,
            name="SLEUTH",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        markup4 = {"Background":"CYAN",
                   "Foreground":"BLACK",
                   "Attributes":[wx.DISPLAY_NORMAL]}


        panel5 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="RED",
            contents=panelContents5,
            flag=boxVerticalFlag,
            name="TEST_SUMMARY_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        markup5 = {"Background":"BLACK",
                   "Foreground":"RED",
                   "Attributes":[wx.DISPLAY_NORMAL]}

        panel6 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="GREEN",
            contents=panelContents6,
            flag=boxVerticalFlag,
            name="GENERAL_TESTING_DISPLAY_MENU",
##            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        markup6 = {"Background":"BLACK",
                   "Foreground":"GREEN",
                   "Attributes":[wx.DISPLAY_NORMAL]}

##        self.Show(show=True)

        self.InitPanelText(panel1, panelContents1, markup=markup1)

        self.InitPanelText(panel2, panelContents2, markup=markup2)

##        self.InitPanelText(panel3, panelContents3, markup=markup3)

        self.InitPanelText(panel4, panelContents4, markup=markup4)

        self.InitPanelText(panel5, panelContents5, markup=markup5)

        self.InitPanelText(panel6, panelContents6, markup=markup6)

        self.Show(show=True)

    #-----------------------------------------------------------------------
 
    def InitPanelSizer(
        self,
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
 
    def InitPanelText(self, panel, contents=[], style=0, markup=None):
        '''
        Init the Panel Text
        Show the Panel Text

        Inputs are panel, the window to display the contents which may be:
            1) a simple text string with or without embeded new lines (\n)
            2) a list of simple text strings
            3) a list of text markup dictionaries

                contents = [
                {
                "Foreground":wx.COLOR_YELLOW,
                "Background":wx.COLOR_BLUE,
                "Attributes":[wx.DISPLAY_STANDOUT],
                "Text":["Header Text"]},
                {
                "Foreground":wx.COLOR_YELLOW,
                "Background":wx.COLOR_BLUE,
                "Attributes":[wx.DISPLAY_UNDERLINE, wx.DISPLAY_REVERSE],
                "Text":["Sub-Header Text"]}
                ]

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
            theText.AppendText(text, markup=None)

        testCases = [(" [ BLINK     ] ", wx.DISPLAY_BLINK),
                     (" [ BOLD      ] ", wx.DISPLAY_BOLD),
                     (" [ DIM       ] ", wx.DISPLAY_DIM),
                     (" [ NORMAL    ] ", wx.DISPLAY_NORMAL),
                     (" [ STANDOUT  ] ", wx.DISPLAY_STANDOUT),
                     (" [ REVERSE   ] ", wx.DISPLAY_REVERSE),
                     (" [ UNDERLINE ] ", wx.DISPLAY_UNDERLINE)]

        foreground = theText.GetForegroundColour() # wx.COLOR_CYAN
        background = theText.GetBackgroundColour()# wx.COLOR_MAGENTA

        attrColor = theText.GetAttributeValueFromColorPair(
            foreground, background)

##        attrMarkupColor = theText.GetAttributeValueFromColorPair(
##            wx.COLOR_RED, wx.COLOR_BLACK)
        attrMarkupColor = theText.GetAttributeValueFromColorPair(
            foreground, background)

        i = 0
        for (msg, attr) in testCases:

            if foreground == wx.COLOR_WHITE and \
               background == wx.COLOR_BLACK:

                markup = {"Foreground": foreground,
                          "Background": background,
                          "Attributes": [attr]}

            else:

                markup = {"Foreground": background,
                          "Background": foreground,
                          "Attributes": [attr]}
 
##            markup = {"Foreground":wx.COLOR_RED,
##                      "Background":wx.COLOR_BLACK,
##                      "Attributes": [attr]}

            comment = 'markup[%d]: msg=%s; attr=0x%X; attrColor=0x%X' % (
                i, msg, attr, attrMarkupColor)

            print(comment)

##        theText.AppendText(' 1st phrase ', newLine=False, markup=markup)
##        theText.AppendText(' 2nd phrase ', newLine=False, markup=markup)
##        theText.AppendText(' 3rd phrase ', newLine=True, markup=markup)

            if (msg == " [ BLINK     ] "):
                theText.AppendText("", topOfForm=True, markup=markup)
                theText.AppendText(msg, newLine=False, markup=markup)
##            elif (msg == " [ BLINK     ] "):
##                theText.AppendText(msg, newLine=True, markup=markup)
            elif (msg == " [ STANDOUT  ] "):
                theText.AppendText("", newLine=True, markup=markup)
                theText.AppendText("", newLine=True, markup=markup)
                theText.AppendText(msg, newLine=False, markup=markup)
            else:
                theText.AppendText(msg, newLine=False, markup=markup)

            i += 1

        if False:
            fileName = './tsPlatformQuery.py'
            fileMode = 'r'
            fileId = open(fileName, fileMode)
            cache = ''
            for aLine in fileId:
                cache += aLine
            theText.AppendText(cache, wrap=False, markup=None)
            print(cache)
            fileId.close()

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

    # Build Information (Top Level Executable Module)
    buildTitle     = __title__
    buildVersion   = __version__
    buildDate      = __date__
    buildAuthors   = __authors__
    buildCopyright = __copyright__

    # User Information (Command Line Interface)
    # TBD - May need to derive class from tsWxMultiFrameEnv
    # inorder to override cliAPP.getOptions.
    cliOptions = None # _Prototype.getOptions

    # Application Program Information (Graphical User Interface)
    guiTopLevelObjectId = wx.ID_ANY
    guiMessageRedirect = True
    guiMessageFilename = None
    guiTopLevelObject = _Prototype
    guiTopLevelObjectName = 'Prototype'
    guiTopLevelObjectTitle = 'Prototype_Feature'
 
    Instance =  wx.MultiFrameEnv(
        cliOptions=cliOptions,
        sourceTitle=buildTitle,
        sourceVersion=buildVersion,
        sourceDate=buildDate,
        sourceAuthors=buildAuthors,
        sourceCopyright=buildCopyright,
        # wrapperHeader=__header__,
        wrapperRedirect=guiMessageRedirect,
        wrapperFilename=guiMessageFilename,
        wrapperTopLevelObject=guiTopLevelObject,
        wrapperId=guiTopLevelObjectId,
        # wrapperMainTitleVersionDate=mainTitleVersionDate,
        wrapperName=guiTopLevelObjectName,
        wrapperTitle=guiTopLevelObjectTitle
        )
    Instance.Wrapper()