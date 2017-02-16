#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:39:01 AM rsg>"
'''
test_tsWxFileCommander.py - Application program to mimic some features of
the Graphical Text User Interface.
'''
#################################################################
#
# File: test_tsWxFileCommander.py
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
#     python test_tsWxFileCommander.py
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

__title__     = 'test_tsWxFileCommander'
__version__   = '1.0.0'
__date__      = '12/07/2011'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2011 TeamSTARS. All rights reserved.'
 
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

labels = "one two three four five six seven eight nine".split()

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

class BlockWindow(wx.Panel):

    def __init__(self,
                 blockParent,
                 blockText):
        '''
        '''
        blockPos = (-1, -1)
        blockSize = (100, 25)

        wx.Panel.__init__(
            self,
            blockParent,
            id=wx.ID_ANY,
            label=blockText,
            pos=blockPos,
            size=blockSize,
            style=wx.BORDER_SIMPLE,
            name='BlockWindow')

        self.SetBackgroundColour("RED")
        self.SetForegroundColour("WHITE")
        self.SetMinSize(blockSize)

##        x = 2
##        y = 2
##        string = blockText
##        self.tsCursesAddStr(x, y, string, attr=None, pixels=False)
##        self.Show()

##        self.Bind(wx.EVT_PAINT, self.OnPaint)

##    def OnPaint(self, evt):
##        sz = self.GetSize()
##        dc = wx.PaintDC(self)
##        dc.SetFont(self.GetFont())
##        w,h = dc.GetTextExtent(self.label)
##        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)

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

        self.TestFileCommander(theFrame)

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

    def TestFileCommander(self, theFrame):
        '''
        '''
        print('Automatic Positioning & Sizing for expected layout.')

        thePanel = wx.Panel(
            theFrame,
            id=wx.ID_ANY,
            label='MyPanel',
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.BORDER_SIMPLE,
            name=wx.StaticBoxNameStr)

        thePanel.SetBackgroundColour('WHITE')
        thePanel.SetForegroundColour('BLUE')

        # make three static boxes with windows positioned inside them
        boxPanel1 = wx.StaticBox(
            thePanel,
            id=wx.ID_ANY,
            label='Box 1',
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.BORDER_SIMPLE,
            validator=wx.DefaultValidator,
            name=wx.StaticBoxNameStr,
            useClientArea = True)

        boxPanel2 = wx.StaticBox(
            thePanel,
            id=wx.ID_ANY,
            label='Box 2',
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.BORDER_SIMPLE,
            validator=wx.DefaultValidator,
            name=wx.StaticBoxNameStr,
            useClientArea = True)

        boxPanel3 = wx.StaticBox(
            thePanel,
            id=wx.ID_ANY,
            label='Box 3',
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.BORDER_SIMPLE,
            validator=wx.DefaultValidator,
            name=wx.StaticBoxNameStr,
            useClientArea = True)

        boxPanel1.SetBackgroundColour('cyan')
        boxPanel1.SetForegroundColour('white')

        boxPanel2.SetBackgroundColour('green')
        boxPanel2.SetForegroundColour('white')

        boxPanel3.SetBackgroundColour('yellow')
        boxPanel3.SetForegroundColour('white')

        # We can also use a sizer to manage the placement of other
        # sizers (and therefore the windows and sub-sizers that they
        # manage as well.)
        theSizer = wx.BoxSizer(wx.HORIZONTAL)
        theSizer.Add(boxPanel1, proportion=1, flag=wx.ALL, border=1)
        theSizer.Add(boxPanel2, proportion=1, flag=wx.ALL, border=1)
        theSizer.Add(boxPanel3, proportion=1, flag=wx.ALL, border=1)

        thePanel.SetSizer(theSizer)
        thePanel.Layout()
        objects = [theFrame, thePanel, boxPanel1, boxPanel2, boxPanel3]
        names = ['theFrame', 'thePanel', 'boxPanel1', 'boxPanel2', 'boxPanel3']
        for i in range(0, len(objects)):
            fmt1 = 'thePanels: '
            fmt2 = '%s[%d]; ' % (names[i], i)
            fmt3 = 'rect=%s; ' % str(objects[i].ts_Rect)
            fmt4 = 'clientrect=%s' % str(objects[i].ts_ClientRect)
            print (fmt1 + fmt2 + fmt3 + fmt4)

        boxSizer1 = self.MakeFileCommander(
            boxPanel=boxPanel1, itemLabels=labels[0:3])
        boxPanel1.Layout()
        print('boxPanel2: clientArea=%s' % str(boxPanel1.ClientArea))

        boxSizer2 = self.MakeFileCommander(
            boxPanel=boxPanel2, itemLabels=labels[3:6])
        boxPanel2.Layout()
        print('boxPanel1: clientArea=%s' % str(boxPanel2.ClientArea))

        boxSizer3 = self.MakeFileCommander(
            boxPanel=boxPanel3, itemLabels=labels[6:9])
        boxPanel3.Layout()
        print('boxPane3: clientArea=%s' % str(boxPanel3.ClientArea))

    #-----------------------------------------------------------------------

    def MakeFileCommander(self,
                           boxPanel=None,
                           itemLabels=None):
        '''
        '''
        # first the static box
        # then the sizer
        boxSizer = wx.StaticBoxSizer(boxPanel, orient=wx.VERTICAL)

        # then add items to it like normal
        for label in itemLabels:
            bw = BlockWindow(boxPanel, label)
            ## sizer.Add(bw, 0, wx.ALL, 2)
            if True:
                # Add expects one Positional with Keyword arguments,
                # This form worked with Box and Grid Sizers.
                boxSizer.Add(bw, proportion=1, flag=wx.ALL, border=1)
            else:
                # AddF expects Positional arguments,
                # This form never tried but ought to work
                boxSizer.AddF(bw, 1, wx.ALL, 1)

        boxPanel.SetSizer(boxSizer)

        return (boxSizer)

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
