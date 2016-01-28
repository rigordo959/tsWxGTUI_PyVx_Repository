#! /usr/bin/env python
#"Time-stamp: <05/31/2014  7:13:47 AM rsg>"
'''
test_tsWxScrolledWindow.py - Test application program. It
demonstrates features and operation of the tsWxScrolled,
tsWxScrolledText, tsWxScrollBar, tsWxScrolBarButtons and
tsWxScrollBarGauge and associated building block components
of tsLibCLI and tsLibGUI..
'''
#################################################################
#
# File: test_tsWxScrolledWindow.py
#
# Purpose:
#
#     Test application program. It demonstrates features and
#     operation of the tsWxScrolled, tsWxScrolledText,
#     tsWxScrollBar, tsWxScrolBarButtons and tsWxScrollBarGauge
#     and associated building block components of tsLibCLI and
#     tsLibGUI.
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
#     python test_tsWxScrolledWindow.py
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
#    2012/03/08 rsg Modified tsAppendText case to support text style
#                   (e.g. wx.DISPLAY_REVERSE) and/or foreground/
#                   background color pair attribute markup.
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsWxScrolledWindow'
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

##    import tsApplication as tsAPP
##    import tsExceptions as tse
##    import tsCommandLineEnv
    import tsWx as wx
    import tsWxMultiFrameEnv

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

except Exception, exceptionCode:

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

        except Exception, errorCode:

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

        except Exception, errorCode:

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

        except Exception, errorCode:

            msg = 'TestScrolledWindow:  ' + \
                  'wx.ScrolledWindow errorCode=%s' % str(errorCode)
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

        attr = wx.DISPLAY_BOLD # wx.DISPLAY_REVERSE
        attrColorPair = self.GetAttributeValueFromColorPair(
                'black',
                'red')

        self.theScrolledPanel3.tsAppendText(
            '         1         2         3         4         5' + \
            '         6         7         8',
            wx.DISPLAY_BOLD)

        self.theScrolledPanel3.tsAppendText(
            '12345678901234567890123456789012345678901234567890' + \
            '123456789012345678901234567890',
            wx.DISPLAY_BOLD | wx.DISPLAY_UNDERLINE)

        self.theScrolledPanel3.tsAppendText(
            'Peep Hole View Wider Text' + \
##            '\nLine #2' + \
##            '\nLine #3' + \
            '\nLine #4')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #6\nLine #7\nLine #8',
            markup=attr)

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #10\nLine #11\nLine #12',
            markup=attrColorPair)

        attr = wx.DISPLAY_REVERSE
        attrColorPair = self.GetAttributeValueFromColorPair(
                'black',
                'red')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #14\nLine #15\nLine #16',
            markup=attr | attrColorPair)

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #18\nLine #19\nLine #20')

        self.theScrolledPanel3.tsAppendText(
            'Another Peep Hole View Wider Text\nLine #22\nLine #23\nLine #24')

        #self.theScrolledPanel3.Scroll(-1, -1)
        #self.theScrolledPanel3.Scroll(0, 0)
        #self.theScrolledPanel3.Scroll(1, 1)
        #self.theScrolledPanel3.Scroll(10, 4)
        #self.theScrolledPanel3.tsOnHScrollWinTop()

        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()
        #self.theScrolledPanel3.tsOnHScrollWinLineDown()

        #self.theScrolledPanel3.tsOnHScrollWinPageDown()

##        self.theScrolledPanel3.tsOnHScrollWinPageDown()

##        self.theScrolledPanel3.tsOnHScrollWinBottom()

##        self.theScrolledPanel3.tsOnVScrollWinTop()

        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()
        #self.theScrolledPanel3.tsOnVScrollWinLineDown()

        #self.theScrolledPanel3.tsOnVScrollWinPageDown()
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

