#! /usr/bin/env python
#"Time-stamp: <06/04/2013  4:22:08 AM rsg>"
'''
test_tsWxStaticBoxSizer.py - Test application program. It demonstrates
features and operation of the tsWxStaticBoxSizer class and associated
building block components of tsLibCLI and tsLibGUI.
'''
#################################################################
#
# File: test_tsWxStaticBoxSizer.py
#
# Purpose:
#
#    Test application program. It demonstrates features and
#    operation of the tsWxStaticBoxSizer class and associated
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
#     python test_tsWxStaticBoxSizer.py
#
# Methods:
#
#   None
#
# Modifications:
#
#   2012/05/15 rsg Added logic to BlockWindow that supportd mouse
#                  Left-Click on individual BlockWindows.
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsWxStaticBoxSizer'
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
    from tsWxEvent import EVT_COMMAND_LEFT_CLICK # [Left Mouse]-Button Click

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

labels = "one two three four five six seven eight nine".split()

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

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self):
        '''
        '''
        triggeringObject = self
        objectId = triggeringObject.ts_AssignedId
 
        objectCriteria = 'EVT_COMMAND_LEFT_CLICK for ' + \
                         '[%s]-Button' % self.GetLabel()
        triggeringEvent = EVT_COMMAND_LEFT_CLICK

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

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

        self.TestStaticBoxSizer(theFrame)

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

    def TestStaticBoxSizer(self, theFrame):
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

        boxSizer1 = self.MakeStaticBoxSizer(
            boxPanel=boxPanel1, itemLabels=labels[0:3])
        boxPanel1.Layout()
        print('boxPanel2: clientArea=%s' % str(boxPanel1.ClientArea))

        boxSizer2 = self.MakeStaticBoxSizer(
            boxPanel=boxPanel2, itemLabels=labels[3:6])
        boxPanel2.Layout()
        print('boxPanel1: clientArea=%s' % str(boxPanel2.ClientArea))

        boxSizer3 = self.MakeStaticBoxSizer(
            boxPanel=boxPanel3, itemLabels=labels[6:9])
        boxPanel3.Layout()
        print('boxPane3: clientArea=%s' % str(boxPanel3.ClientArea))

    #-----------------------------------------------------------------------

    def MakeStaticBoxSizer(self,
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

            # Automatically Bind all mouse events ASAP (now).
            # Will register event in the SystemEventTable.
            event = EVT_COMMAND_LEFT_CLICK
            handler = bw.tsOnLeftClick
            source = bw
            self.Bind(event,
                      handler,
                      source,
                      useSystemEventTable=True)

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

