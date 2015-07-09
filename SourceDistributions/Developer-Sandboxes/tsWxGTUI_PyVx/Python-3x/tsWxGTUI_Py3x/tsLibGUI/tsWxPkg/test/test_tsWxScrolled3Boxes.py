#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:40:24 AM rsg>"
'''
test_tsWxScrolled.py - Application program to demonstrate
the tsWxScrolled, tsWxScrolledText, tsWxScrollBar,
tsWxScrolBarButtons and tsWxScrollBarGauge features of the
Graphical Text User Interface.
'''
#################################################################
#
# File: test_tsWxScrolled.py
#
# Purpose:
#
#    Application program to demonstrate the tsWxScrolled,
#    tsWxScrolledText, tsWxScrollBar, tsWxScrolBarButtons and
#    tsWxScrollBarGauge features of the Graphical Text User
#    Interface.
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
#     python test_tsWxScrolled.py
#
# Methods:
#
#   None
#
# Modifications:
#
#   2012/02/10 rsg Re-organized ScrollBar test code by panel
#                  association rather than operation. Revised
#                  panel colors to improve contrast and hence
#                  readability.
#
#   2012/02/18 rsg Added logic to TestScrolled code to invoke
#                  the following:
#                      tsAppendText
#                      tsUpdateScrolledText
#
#   2012/02/18 rsg Added logic to TestScrolled code to invoke
#                  the following pending implementation of
#                  event processing:
#                      tsOnHScrollWinBottom
#                      tsOnHScrollWinBottom
#                      tsOnHScrollWinLineDown
#                      tsOnHScrollWinLineUp
#                      tsOnHScrollWinPageDown
#                      tsOnHScrollWinPageUp
#                      tsOnHScrollWinTop
#                      tsOnVScrollWinLineDown
#                      tsOnVScrollWinLineUp
#                      tsOnVScrollWinPageDown
#                      tsOnVScrollWinPageUp
#                      tsOnVScrollWinTop
#
#    2012/02/29 rsg Simplified interface to Scrolled.tsAppendText
#                   and to Scrolled.tsUpdateScrolledText.
#
#    2012/03/04 rsg Added logic to link horizontal and vertical
#                   scrolling with associated tsWxScrolled
#                   methods.
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsWxScrolled'
__version__   = '1.1.0'
__date__      = '03/04/2012'
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

        if False and frameSizingEnabled:

            wx.Frame.__init__(self,
                              parent,
                              id=nextWindowId(),
                              title=title,
                              pos=pos,
                              size=((280 * 4) / 2, (200 * 4) / 2),
                              style=style,
                              name=name)

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
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        #-------------------------------------------------------------------
        # Begin Prototype
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

        self.TestScrolled(theFrame)
        self.Show()

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

        self.logger.debug(
            'End %s (0x%X).' % ('Prototype', self.tsGetTheId()))

    #-----------------------------------------------------------------------

    def TestScrolled(self, theFrame):
        '''
        '''
        self.theFrame = theFrame
        print('Automatic Positioning & Sizing for expected layout.')

        #-------------------------------------------------------------------

        self.boxHorizontal = wx.BoxSizer(wx.HORIZONTAL)

        # Sized panels may overlap but panel borders prevent
        # overlap of associated scroll bars and text area contents.
        boxHorizontalPanelStyle = wx.BORDER_SIMPLE

        #-------------------------------------------------------------------

        self.panel1 = wx.Panel(self.theFrame,
                               wx.ID_ANY,
                               label='Horizontal ScrollBar',
                               style=boxHorizontalPanelStyle)

        self.panel1.SetBackgroundColour("CYAN")
        self.panel1.SetForegroundColour("BLACK")

        self.boxHorizontal.Add(self.panel1, proportion=1, flag=wx.EXPAND)

        #-------------------------------------------------------------------

        self.panel2 = wx.Panel(self.theFrame,
                               wx.ID_ANY,
                               label='Vertical ScrollBar',
                               style=boxHorizontalPanelStyle)

        self.panel2.SetBackgroundColour("GREEN")
        self.panel2.SetForegroundColour("BLACK")

        self.boxHorizontal.Add(self.panel2, proportion=1, flag=wx.EXPAND)

        #-------------------------------------------------------------------

        self.panel3 = wx.Panel(self.theFrame,
                               wx.ID_ANY,
                               label='Dual ScrollBars',
                               style=boxHorizontalPanelStyle)

        self.panel3.SetBackgroundColour("YELLOW")
        self.panel3.SetForegroundColour("BLACK")

        self.boxHorizontal.Add(self.panel3, proportion=1, flag=wx.EXPAND)

        #-------------------------------------------------------------------

        self.theFrame.SetAutoLayout(True)
        self.theFrame.SetSizer(self.boxHorizontal)
        self.theFrame.Layout()

        #-------------------------------------------------------------------

        try:

            theBorder = self.panel1.tsIsBorderThickness(
                self.panel1.ts_Style, pixels=True)

            self.theScrolledPanel1 = wx.Scrolled(
                self.panel1,
                id=wx.ID_ANY,
                label='Narrow View',
                pos=(self.panel1.Rect.x + wx.pixelWidthPerCharacter,
                     self.panel1.Rect.y + wx.pixelHeightPerCharacter),
                size=(self.panel1.Rect.width - 2 * theBorder.width,
                      self.panel1.Rect.height - 2 * theBorder.height),
                # style=0,
                style=wx.HSCROLL,
                # style=wx.VSCROLL,
                # style=wx.HSCROLL | wx.VSCROLL,
                name=wx.ScrolledNameStr)

            self.theScrolledPanel1.Show(show=True)

        except Exception as errorCode:

            msg ='TestScrolled:  wx.Scrolled errorCode=%s' % str(errorCode)
            print('DEBUG: %s\n' % msg)

        #-------------------------------------------------------------------

        try:

            theBorder = self.panel2.tsIsBorderThickness(
                self.panel2.ts_Style, pixels=True)

            self.theScrolledPanel2 = wx.Scrolled(
                self.panel2,
                id=wx.ID_ANY,
                label='Short View',
                pos=(self.panel2.Rect.x + wx.pixelWidthPerCharacter,
                     self.panel2.Rect.y + wx.pixelHeightPerCharacter),
                size=(self.panel2.Rect.width - 2 * theBorder.width,
                      self.panel2.Rect.height - 2 * theBorder.height),
                # style=0,
                # style=wx.HSCROLL,
                style=wx.VSCROLL,
                # style=wx.HSCROLL | wx.VSCROLL,
                name=wx.ScrolledNameStr)

            self.theScrolledPanel2.Show(show=True)

        except Exception as errorCode:

            msg ='TestScrolled:  wx.Scrolled errorCode=%s' % str(errorCode)
            print('DEBUG: %s\n' % msg)

        #-------------------------------------------------------------------

        try:

            theBorder = self.panel3.tsIsBorderThickness(
                self.panel3.ts_Style, pixels=True)

            self.theScrolledPanel3 = wx.Scrolled(
                self.panel3,
                id=wx.ID_ANY,
                label='Peep Hole View',
                pos=(self.panel3.Rect.x + wx.pixelWidthPerCharacter,
                     self.panel3.Rect.y + wx.pixelHeightPerCharacter),
                size=(self.panel3.Rect.width - 2 * theBorder.width,
                      self.panel3.Rect.height - 2 * theBorder.height),
                # style=0,
                # style=wx.HSCROLL,
                # style=wx.VSCROLL,
                style=wx.HSCROLL | wx.VSCROLL,
                name=wx.ScrolledNameStr)

            self.theScrolledPanel3.Show(show=True)

        except Exception as errorCode:

            msg = 'TestScrolled:  wx.Scrolled errorCode=%s' % str(errorCode)
            print('DEBUG: %s\n' % msg)

        #-------------------------------------------------------------------

##        self.theFrame.Show()

        self.theScrolledPanel1.tsAppendText(
            '         1         2         3         4         5' + \
            '         6         7         8' + \
            '\n12345678901234567890123456789012345678901234567890' + \
            '123456789012345678901234567890' + \
            '\nNarrow View Text' + \
##            '\nLine #2' + \
##            '\nLine #3' + \
            '\nLine #4')

        self.theScrolledPanel1.tsAppendText(
            'Another Narrow View Wider Text\nLine #6\nLine #7\nLine #8')

##        self.theScrolledPanel1.tsUpdateScrolledText()

        #-------------------------------------------------------------------

        self.theScrolledPanel2.tsAppendText(
            '         1         2         3         4         5' + \
            '         6         7         8' + \
            '\n12345678901234567890123456789012345678901234567890' + \
            '123456789012345678901234567890' + \
            '\nShort View Text' + \
##            '\nLine #2' + \
##            '\nLine #3' + \
            '\nLine #4')

        self.theScrolledPanel2.tsAppendText(
            'Another Short View Wider Text\nLine #6\nLine #7\nLine #8')

        self.theScrolledPanel2.tsAppendText(
            'Another Short View Wider Text\nLine #10\nLine #11\nLine #12')

        self.theScrolledPanel2.tsAppendText(
            'Another Short View Wider Text\nLine #14\nLine #15\nLine #16')

##        self.theScrolledPanel2.tsUpdateScrolledText()

        #-------------------------------------------------------------------

        self.theScrolledPanel3.tsAppendText(
            '         1         2         3         4         5' + \
            '         6         7         8' + \
            '\n12345678901234567890123456789012345678901234567890' + \
            '123456789012345678901234567890' + \
            '\nPeep Hole View Wider Text' + \
##            '\nLine #2' + \
##            '\nLine #3' + \
            '\nLine #4')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #6\nLine #7\nLine #8')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #10\nLine #11\nLine #12')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #14\nLine #15\nLine #16')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #18\nLine #19\nLine #20')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #22\nLine #23\nLine #24')

        #self.theScrolledPanel3.tsOnHScrollWinTop()

        self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()

        self.theScrolledPanel3.tsOnHScrollWinPageDown()

##        self.theScrolledPanel3.tsOnHScrollWinPageDown()

##        self.theScrolledPanel3.tsOnHScrollWinBottom()

##        self.theScrolledPanel3.tsOnVScrollWinTop()

        self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()

        self.theScrolledPanel3.tsOnVScrollWinPageDown()
##        self.theScrolledPanel3.tsOnVScrollWinPageUp()

##        self.theScrolledPanel3.tsOnVScrollWinBottom()

##        self.theScrolledPanel3.tsUpdateScrolledText()

##        self.theScrolledPanel3.tsOnVScrollWinLineDown()

        self.theFrame.Show()

    #-----------------------------------------------------------------------

    def OnMove(self, event):
        #pos = event.GetPosition()
        #self.posCtrl.SetValues('%s, %s' % (pos.x, pos.y))
        print('Prototype OnMove: event=%s' % str(event))

    #-----------------------------------------------------------------------

    def OnQuit(self, event):
        '''
        Close the Frame
        '''
        print('Prototype OnQuit: event=%s' % str(event))
##        self.Close()

    #-----------------------------------------------------------------------
 
    def OnHelp(self, event):
        '''
        Show the help dialog.
        '''
##       dlg = wx.MessageDialog(
##            self,
##            __help__,
##            "%s Help" % __title__,
##            wx.OK | wx.ICON_INFORMATION)

##        dlg.ShowModal()
##        dlg.Destroy()
        print('Prototype OnHelp: event=%s' % str(event))

    #-----------------------------------------------------------------------

    def OnAbout(self, event):
        '''
        Show the about dialog.
        '''
##        dlg = wx.MessageDialog(
##            self,
##            __header__,
##            'About %s' % __title__,
##            wx.OK | wx.ICON_INFORMATION)

##        dlg.ShowModal()
##        dlg.Destroy()
        print('Prototype OnAbout: event=%s' % str(event))

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
