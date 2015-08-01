#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:07:46 AM rsg>"
'''
test_tsWxBoxLogo.py - Application program to mimic some features of
the Graphical Text User Interface.
'''
#################################################################
#
# File: test_tsWxBoxLogo.py
#
# Purpose:
#
#    Application program to mimic some features of the
#    Graphical Text User Interface.
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
#     python test_tsWxBoxLogo.py
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

__title__     = 'test_tsWxBoxLogo'
__version__   = '1.0.0'
__date__      = '06/13/2012'
__authors__   = 'Richard S. Gordon, a.k.a. Software Gadgetry'
__copyright__ = 'Copyright (c) 2021 Software Gadgetry. All rights reserved.'
 
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
    except ImportError, wxImportError:
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
                              size=((280 * 3) / 2, (200 * 3) / 2),
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
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        # The following tests depend on Showing final Frame position.
##        if splashScreenEnabled:
##            self.theSplashScreen.tsShow()
##            time.sleep(splashScreenSeconds)

##        self.myframe = wx.Frame(None, title='BoxSizer')

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

##         self.Show()

        # panel = wxPanel(
        #             parent,
        #             id=wx.ID_ANY,
        #             pos=wx.DefaultPosition,
        #             size=wx.DefaultSize,
        #             style=wx.DEFAULT_PANEL_STYLE,
        #             name=wx.PanelNameStr)

        parent = self
        logoPanel = wx.Panel(
            parent,
            id=wx.ID_ANY,
##            pos=wx.Point(5 * wx.pixelWidthPerCharacter,
##                         5 * wx.pixelHeightPerCharacter),
##            size=wx.Size(10 * wx.pixelWidthPerCharacter,
##                         10 * wx.pixelHeightPerCharacter),
            style=wx.DEFAULT_PANEL_STYLE,
            name=wx.PanelNameStr)

        print('Automatic Positioning & Sizing for expected layout.')

        boxVertical = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(logoPanel,
                          wx.ID_ANY,
                          # label=' t s ',
                          style=wx.BORDER_DEFAULT)

        panel2 = wx.Panel(logoPanel,
                        wx.ID_ANY,
                        label=' G T U I ',
                        style=wx.BORDER_DEFAULT)

        panel1.SetBackgroundColour("RED")
        panel1.SetForegroundColour("YELLOW")
        panel2.SetBackgroundColour("BLUE")
        panel2.SetForegroundColour("WHITE")

        boxVertical.Add(panel1, proportion=1, flag=wx.EXPAND)

        # TBD - Resolve why the following disrupt boxHorizontal display
##        boxHorizontal.AddSpacer(8)
##        boxHorizontal.AddSpacer(wx.SizerSpacer((wx.pixelWidthPerCharacter,
##                                                wx.pixelHeightPerCharacter))

        boxVertical.Add(panel2, proportion=1, flag=wx.EXPAND)

        self.SetAutoLayout(True)
        self.SetSizer(boxVertical)
        self.Layout()

        self.Show(show=True)

        boxHorizontal = wx.BoxSizer(wx.HORIZONTAL)

        panel3 = wx.Panel(panel1,
                          wx.ID_ANY,
                          label=' t s ',
                          style=wx.BORDER_DEFAULT)

        panel4 = wx.Panel(panel1,
                          wx.ID_ANY,
                          label=' W x ',
                          style=wx.BORDER_DEFAULT)

##        panel5 = wx.Panel(panel2,
##                        wx.ID_ANY,
##                        label='GTUI ',
##                        style=wx.BORDER_DEFAULT)

        panel3.SetBackgroundColour("RED")
        panel3.SetForegroundColour("YELLOW")
        panel4.SetBackgroundColour("GREEN")
        panel4.SetForegroundColour("BLUE")
##        panel5.SetBackgroundColour("BLUE")
##        panel5.SetForegroundColour("WHITE")

        boxHorizontal.Add(panel3, proportion=1, flag=wx.EXPAND)

        boxHorizontal.Add(panel4, proportion=1, flag=wx.EXPAND)

        panel1.SetAutoLayout(True)
        panel1.SetSizer(boxHorizontal)
        panel1.Layout()

        self.Show(show=True)

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

        # TBD - This should NOT change Frame color.
        # It should only change Panel color.
##        self.ForegroundColour = wx.COLOR_YELLOW
##        self.BackgroundColour = wx.COLOR_MAGENTA

        self.logger.debug(
            'End %s (0x%X).' % ('Prototype', self.tsGetTheId()))

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
