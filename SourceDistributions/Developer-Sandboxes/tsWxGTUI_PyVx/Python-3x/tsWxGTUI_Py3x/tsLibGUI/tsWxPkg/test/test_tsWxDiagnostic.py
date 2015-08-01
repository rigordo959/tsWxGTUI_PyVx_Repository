#! /usr/bin/env python
#"Time-stamp: <06/04/2013  2:10:12 AM rsg>"
'''
test_tsWxDiagnostic.py -Test application program. It demonstrates
features and operation of the tsWxWindows class and associated
building block components of tsLibCLI and tsLibGUI.
'''
#################################################################
#
# File: test_tsWxDiagnostic.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of the tsWxWindows class and associated
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
#     python test_tsWxDiagnostic.py
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

__title__     = 'test_tsWxDiagnostic'
__version__   = '2.0.0'
__date__      = '06/04/2013'
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

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsApplication as tsAPP
    import tsExceptions as tse
    import tsLogger as Logger
    import tsOperatorSettingsParser

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsLibGUI

except ImportError as importCode:

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

except ImportError as importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

except Exception as exceptionCode:

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
                              size=((85 * wx.pixelWidthPerCharacter),
                                    (63 * wx.pixelHeightPerCharacter)),
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

##        self.myframe = wx.Frame(None, title='Diagnostic')

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

        panelContents1 = [
            'OS 6.2.0    \  SLEUTH 0.4.2 Ad Mfg/Sleuth_LITE.stg     pc-sw1    D 02-16:15:45',
            ' 11/07/05 14:05:44 11/10/05 06:22:29                                          ']

        panelContents2 = [
            '               CE INFO DISPLAY (0/0)                                          ',
            '             Memory         Exec Heap K    Cluster K     Procs   Imgs         ',
            '  CE  TP Size  FreeK HwtrK Size Free Hwtr Size Free Hwtr Cnt Max Cnt Max Reg  ',
            '    1 H   -1M     -1    -1   -1   -1   -1   -1   -1   -1  -1  -1  -1  -1 0/0  ',
            '    2 p  256M 245071     0  448  106  429   32   27    6   7  65   7  10 2/5  ',
            '    3 p  256M 246811     0  448  236  414   32   28    6   4  65   4  10 1/5  ',
            '    4 p  256M 252879     0  448  297  410   32   29    6   2  65   2  10 0/5  ',
            '    5 p  256M 255223     0  448  320  401   32   30    6   2  65   2  10 1/5  ']

        panelContents3 = [
            '               PROCESS INFO DISPLAY                                           ',
            '                     Stack               Heap            RunTime              ',
            '  PID       Index  Size   Hwtr    Size    Free    Hwtr   Secs  Usecs Rc       ',
            ' 0x   2a481    0  20480     -1 1064928  529040  535888     92.750000 0x0      ',
            ' 0x   49a01    1  20480     -1 1064928  529040  535888      0.175000 0x0      ',
            ' 0x   29c02    2  20480     -1    8160    2480    5680      0.025000 0x0      ',
            ' 0x   27f03    3  20480     -1 1064928  529040  535888      2.025000 0x0      ',
            ' 0x   56702    4  20480     -1    8160    2320    5840      0.000000 0x0      ',
            ' 0x   26e04    5  16384     -1    8160    2624    5600      0.000000 0x0      ',
            ' 0x   39b81    6  20480     -1 4325344 4256736   68608     20.125000 0x0      ',
            ' 0x   22d05    7  20480     -1    8160    2320    5840      0.000000 0x0      ',
            ' 0x   20206    8  20480     -1 4325344 4316032  245024    148.400000 0x0      ',
            ' 0x   37082    9  20480     -1    8160    2480    5680      0.000000 0x0      ',
            ' 0x   34d83   10  20480     -1 1064928  529040  535888      0.250000 0x0      ']

        panelContents4 = [
            ' Type      Host   C80  I860   PPC SHARC TLoops   Sp  Errors Pid/Stuck         ',
            ' monitor      1     0     0     0     0                   0 0x17800/0x21c     ',
            ' dx           0     0     0     4     0     10     0      0       0           ',
            ' isr timer    0     0     0     2     0     38     0      0       0           ',
            ' mailbox      0     0     0     2     0    145     0      0       0           ',
            ' quick        0     0     0     1     0    471     0      0       0           ',
            ' sal          0     0     0     2     0    141     0      0       0           ',
            '                                                                              ',
            '            <------- Max Count -------->  Total  Bcst   Sgnl    No   CE:5/0   ',
            ' Type       Host   C80  I860   PPC SHARC  Kills  Kills  Kills  Rsrce DEV:0/0  ',
            ' Monitor       0     0     0     0     0  14623      0      0      0   Stuck  ',
            ' dx            0     0     0    11     0   2640      0      0      0       0  ',
            ' isr timer     0     0     0     4     0   1748      0      0      0       0  ',
            ' mailbox       0     0     0    14     0   4244      0      0      0       0  ',
            ' quick         0     0     0    13     0   3361      0      0      0       0  ',
            ' sal           0     0     0    10     0   2630      0      0      0       0  ']

        panelContents5 = [
            ' E10 Tests:  11 Tgt:  11 Kills:14623 Pause: 0 Term-r Err:  0 Arun   Pg:1/1    ']

        panelContents6 = [
            '        GENERAL                    TESTING                    DISPLAY      ',
            '                                                                           ',
            '   Help       Stop                                       NextPg    PrevPg  ',
            '   Cluster    Tests           Options     Kill           Clear     ToFile  ',
            '   Edit                       Limits      Modes          GoToPg    Display ']

        boxVerticalFlag = wx.EXPAND
        boxVertical = wx.BoxSizer(wx.VERTICAL)

        panel1 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="CYAN",
            colorForeground="BLACK",
            contents=panelContents1,
            flag=boxVerticalFlag,
            name="SLEUTH",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        panel2 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="YELLOW",
            contents=panelContents2,
            flag=boxVerticalFlag,
            name="CE_INFO_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        panel3 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="YELLOW",
            contents=panelContents3,
            flag=boxVerticalFlag,
            name="PROCESS_INFO_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        panel4 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="WHITE",
            contents=panelContents4,
            flag=boxVerticalFlag,
            name="TEST_INFO_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

        panel5 = self.InitPanelSizer(
            parent,
##            id=wx.ID_ANY,
            colorBackground="BLACK",
            colorForeground="MAGENTA",
            contents=panelContents5,
            flag=boxVerticalFlag,
            name="TEST_SUMMARY_DISPLAY",
##            pos=wx.DefaultPosition,
##            size=wx.DefaultSize,
            sizer=boxVertical,
            style=wx.BORDER_SIMPLE
            )

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

##        self.Show(show=True)

        self.InitPanelText(panel1, panelContents1)

        self.InitPanelText(panel2, panelContents2)

        self.InitPanelText(panel3, panelContents3)

        self.InitPanelText(panel4, panelContents4)

        self.InitPanelText(panel5, panelContents5)

        self.InitPanelText(panel6, panelContents6)

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
 
    def InitPanelText(self, panel, contents=[], style=0):
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
                except Exception as errorCode:
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

