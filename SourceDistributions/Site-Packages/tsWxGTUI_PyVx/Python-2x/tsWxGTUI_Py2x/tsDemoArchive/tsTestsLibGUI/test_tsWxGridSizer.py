#! /usr/bin/env python
#"Time-stamp: <04/04/2015  9:38:32 AM rsg>"
'''
test_tsWxGridSizer.py - Test application program. It demonstrates
features and operation of the tsWxGridSizer class and associated
building block components of tsLibCLI and tsLibGUI.
'''
#################################################################
#
# File: test_tsWxGridSizer.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of the tsWxGridSizer class and associated
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
#     python test_tsWxGridSizer.py
#
# Methods:
#
#   None
#
# Modifications:
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

__title__     = 'test_tsWxGridSizer'
__version__   = '1.1.0'
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

#--------------------------------------------------------------------------

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

        # The following tests depend on Showing final Frame position.
##        if splashScreenEnabled:
##            self.theSplashScreen.tsShow()
##            time.sleep(splashScreenSeconds)

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

        #-------------------------------------------------------------------
        # End Prototype
        #-------------------------------------------------------------------

    #-----------------------------------------------------------------------
 
    def InitUI(self):

        boxVertical = wx.BoxSizer(wx.VERTICAL)
        boxVerticalPanel = wx.Panel(
            theFrame, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        boxVerticalPanel.SetBackgroundColour("MAGENTA")
        boxVertical.Add(boxVerticalPanel, proportion=1, flag=wx.EXPAND)
        self.SetAutoLayout(True)
        self.SetSizer(boxVertical)
        self.Layout()

        self.Show(show=True)

        panel3 = wx.Panel(boxVerticalPanel,
                          wx.ID_ANY,
                          (8, 12),
                          (32, 36),
                          style=wx.BORDER_SIMPLE)
        panel4 = wx.Panel(boxVerticalPanel,
                          wx.ID_ANY,
                          (48, 12),
                          (32, 36),
                          style=wx.BORDER_SIMPLE)

        panel5 = wx.Panel(boxVerticalPanel,
                          wx.ID_ANY,
                          (88, 56),
                          (32, 36),
                          style=wx.BORDER_SIMPLE)

        panel3.SetBackgroundColour("CYAN")
        panel4.SetBackgroundColour("GREEN")
        panel5.SetBackgroundColour("YELLOW")

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
