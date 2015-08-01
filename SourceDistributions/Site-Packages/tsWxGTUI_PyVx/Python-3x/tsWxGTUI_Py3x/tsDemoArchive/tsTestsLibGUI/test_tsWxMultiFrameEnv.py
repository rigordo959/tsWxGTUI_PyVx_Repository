#! /usr/bin/env python
#"Time-stamp: <04/04/2015  9:33:03 AM rsg>"
'''
test_tsWxMultiFrameEnv.py - Test application for class to
establish environment for a Multi-Frame Graphical User Interface.
It creates a simple Frame and displays "Hello World!" as
StaticText.
'''
#################################################################
#
# File: test_tsWxMultiFrameEnv.py
#
# Purpose:
#
#     Test application for class to establish environment for
#     a Multi-Frame Graphical User Interface. It creates a simple
#     Frame and displays "Hello World!" as StaticText.
#
# Limitations:
#
#    1) The "tsApplication" module can be used to launch only the
#       Command Line Interface portion of an applications. The
#       application designer is responsible for producing Unix-style
#       exit codes and messages, upon application termination.
#
#    2) The "tsCommandLineEnv" module, a derivative of "tsApplication"
#       can be used to launch only the Command Line Interface portion
#       of an applications. It provides a wrapper that produces Unix-
#       style exit codes and messages, upon application termination.
#
#    3) The "tsWxMultiFrameEnv" module, a derivative of "tsCommand
#       LineEnv" can be used to launch both the Command Line Interface
#       and Graphical-style User Interface portions of an applications.
#       It provides a wrapper that produces Unix-style exit codes and
#       messages, upon application termination.
#
#    4) Command line keyword-value pair option and positional argument
#       parsing uses off-the-shelf, Python version appropriate modules.
#       To facilitate portability of this sample run time environment
#       manager from one Python platform to another, it automatically
#       selects and uses latest one of following:
#
#       a) "argparse" module used with Python 2.7.0 or later
#
#       b) "optparse" module used with Python 2.3.0 or later
#
#       c) "getopt" module used with Python 1.6.0 or later
#
# Notes:
#
#    1) "tsApplication" is a base class for launching the appli-
#        cation specified by an operator. It initializes and con-
#        figures the application using the following keyword
#        value pairs and positional arguments:
#
#        a) Input provided on the command line by an operator. The
#           command line uses a Unix-style, free-format to promote
#           future enhancement and on-going maintenance.
#
#        b) Input provided in the parameter list of the applica-
#           tion's invocation of the class instantiation. The par-
#           ameter list uses a Python-style free-format to promote
#           future enhancement and on-going maintenance.
#
#    2) "tsCommandlineEnv" is a convenience package wrapping term-
#       inal keyboard input, video display scrolled text output,
#       "tsLogger" and "tsException" services. It is a base class
#       for "tsWxMultiFrameEnv".
#
#    3) "tsWxMultiFrameEnv" is a convenience package wrapping
#       terminal keyboard & mouse input, video display row and
#       column addressable, field-editable output, "tsLogger"
#       and "tsException" services.
#
#    4) Standardized command line option parsing methods return
#       a dictionary, of keyword value pairs, and a list, of
#       positional arguments in the manner of the "optparse"
#       module. This should facilitate application support for
#       the evolving Python command line option parsing modules.
#       However, this requires that "tsApplication" stubs and
#       application parsing methods include a small amount of
#       extra code for the appropriate "argparse", "optparse"
#       and "getopt" output format conversion.
#
#    5) The various command line parser modules produce usage
#       help. The content and format may vary based on the
#       parser's capabilities and limitations. Considerable
#       care needs to be taken to minimize the difference in
#       order to produce a software product that retains its
#       look and feel for the end-user, regardless of the
#       hardware and software platform being used.
#
# Usage (example):
#
#     ###########################################################
#
#     ## Import Module
#     from tsWxMultiFrameEnv import MultiFrameEnv
#
#     ##  Generalized Form to Instantiate and Launch an application
#     ##  module that uses a Command Line Interface (CLI) to a
#     ##  character-mode terminal with optional logging.
#     ##
#     ##  Configuration options enable the CLI application to launch
#     ##  and use the same character-mode terminal with a Graphical-
#     ##  style User Interface (GUI).
#     ##
#     ##  See this File's header for examples of those application
#     ##  specific source code descriptions associated with
#     ##  parameter identifiers having double-underscore ("__")
#     ##  prefix and suffix.
#     ##
#     ##  See the test_tsWxWidgets.py File's header for examples of
#     ##  the gui application options.
#
#     myApp = MultiFrameEnv(
#         #######################################################
#         # All applications (with Command Line Interface or
#         # Graphical-style User Interface) begin with the following
#         # Command Line Interface Launch configuration item list:
#
#         buildTitle=__title__,
#         buildVersion=__version__,
#         buildDate=__date__,
#         buildAuthors=__authors__,
#         buildCopyright=__copyright__,
#         buildLicense=__license__,
#         buildCredits=__credits__,
#         buildTitleVersionDate=mainTitleVersionDate,
#         buildHeader=__header__,
#         buildPurpose=__doc__,
#
#         #######################################################
#
#         # Python version appropriate Command Line Interface
#         # module(s) may be enabled to obtain non-Application-
#         # specific Keyword-Value pair Options and Positional
#         # Arguments and associated command line help:
#
#         #     "argparse" module - introduced with Python 2.7.0
#         #     "optparse" module - introduced with Python 2.3.0
#         #     "getopt"   module - introduced with Python 1.6.0
#
#         enableDefaultCommandLineParser=False # Disable unless True
#
#         #######################################################
#
#         # When appropriate, some applications also use the following
#         # Graphical-style User Interface Launch configuration item list:
#
#         guiRequired=True,
#         guiTopLevelObjectId=-1,
#         guiMessageRedirect=True,
#         guiMessageFilename=None,
#         guiTopLevelObject=_Communicate,
#         guiTopLevelObjectName='Sample',
#         guiTopLevelObjectTitle='widgets_communicate',
#
#         #######################################################
#
#         # When customized logging is appropriate, some applica-
#         # tions use the following application-specific Launch
#         # configuration item:
#
#         logs=['1st-Non-Default', ..., 'Nth-Non-Default'],
#
#         # When basic logging is appropriate, some applications
#         # use the following non-application-specific Launch
#         # configuration item:
#
#         logs=[],
#
#         #######################################################
#
#         # All applications, with Command Line Interface or with
#         # both Command Line and Graphical-style User Interfaces,
#         # wrapup their Configuration item list as follows:
#
#         runTimeEntryPoint=main)
#
#         #######################################################
#
#     ## Launch via reference to appropriate Module Method
#     myApp.Wrapper()
#
# CLI Methods:
#
#    exitTest - Optional Simulated Input / Output Exception to
#           induce termination with an exit code and message.
#
#    mainTest - Command Line Interface. It gathers and displays
#           operator input as keyword-value pair options and
#           positional arguments.
#
#    EntryPoint - Application Programming Interface, It
#           gathers and displays configuration parameters as
#           keyword-value pair options and positional arguments.
#
# GUI Class & Methods:
#
#    _Prototype            - Class to establish the frame that
#                            contains the application specific
#                            graphical components.
#
#    _Prototype.OnAbout    - Event Handler for Mouse Click on About button
#
#    _Prototype.OnHelp     - Event Handler for Mouse Click on Help button
#
#    _Prototype.OnMove - Unused Event Handler for Window Re-sizing
#
#    _Prototype.OnQuit - Event Handler for Mouse Click on Close button
#
#    _Prototype.__init__ - Class constructor
#
#    _Prototype.tsGetTheId - Return ID associated with class instance
#
#    nextWindowId - Generates a unique GUI object Id
#
# Modifications:
#
#    2013/12/08 rsg Initial version.
#
#    2015/04/04 rsg Replaced "import tsWxGlobals as wx" by
#                   "import tsWx as wx" and made the associated
#                   Toolkit building block references.
#
# ToDo:
#
#     None.
#
#################################################################

__title__     = 'test_tsWxMultiFrameEnv'
__version__   = '1.1.0'
__date__      = '04/04/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

#------------------------------------------------------------------------

import os.path
import sys
import time
import traceback

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py3x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWx as wx

#------------------------------------------------------------------------

DEBUG = True # Set True to log run time parameters and exit.
VERBOSE = False

DebugSimulatedKeyErrorTrap = True

PySimpleAppMode = False # Set True only for Redirection, TaskBar and
                        # Single The Frame with no Dialogs

debugExitEnabled = False # True
frameSizingEnabled = True
redirectEnabled = True
runTimeTitleEnabled = True
splashScreenSeconds = 0
tracebackEnabled = False

#------------------------------------------------------------------------

__help__ = '''
This program demonstrates an environment for a multi-frame
and multi-dialog Graphical-style User Interface.

'''
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
                              size=(40 * wx.pixelWidthPerCharacter,
                                    10 * wx.pixelHeightPerCharacter),
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
        self.logger.notice(
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))
        print(
            'Begin %s (0x%X).' % ('Prototype', self.tsGetTheId()))

        #-------------------------------------------------------------------
        # Begin Prototype
        #-------------------------------------------------------------------

        self.Centre()
        self.Show()

        theFrame = self

        theRect = theFrame.Rect
        theClientArea = theFrame.ClientArea
        print('Frame: Rect=%s; ClientArea=%s' % (str(theRect),
                                                 str(theClientArea)))

        theText = "Hello, World! "
        print("theText=%s" % theText)

        # Allow additional width for cursor
        theTextWidth = (len(theText) + 1) * wx.pixelWidthPerCharacter
        theTextHeight = 1 * wx.pixelHeightPerCharacter

        theTextOffset = wx.Point(
            (theClientArea.x + (
                (theClientArea.width - theTextWidth) // 2)),
            (theClientArea.y + (
                (theClientArea.height - theTextHeight) // 2)))
        print("theTextOffset=%s" % str(theTextOffset))

        theTextSize = wx.Size(theTextWidth, theTextHeight)
        print("theTextSize=%s" % str(theTextSize))

        text = wx.StaticText(
            theFrame,
            pos=theTextOffset,
            size=theTextSize,
            label=theText)

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

#------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def exitTest():
        '''
        Simulated Input / Output Exception to induce termination
        with an exit code and message.
        '''
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def mainTest(*args, **kw):
        '''
        Command Line Interface. It gathers and displays operator
        input as keyword-value pair options and positional arguments.
        '''
        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='mainTest')
        myParser =  tsOperatorSettingsParser.TsOperatorSettingsParser()
        msg = '\n%s\n' % myParser.getRunTimeTitleVersionDate()
        print(msg)
        myLogger.debug(msg)

        rawArgsOptions = sys.argv[1:]
        msg = '\trawArgsOptions=%s' % str(rawArgsOptions)
        print(msg)
        myLogger.debug(msg)
        maxArgs = len(rawArgsOptions)

        (args, options) = myParser.parseCommandLineDispatch()
        msg = 'type(args=%s)=%s' % (str(args), type(args))
        print(msg)
        myLogger.debug(msg)

        msg = 'type(options=%s)=%s' % (str(options), type(options))
        print(msg)
        myLogger.debug(msg)

        if True or DEBUG:
            label = myParser.getRunTimeTitle()

            fmt1 = '%s.mainTest (parameter list): ' % label
            fmt2 = 'args=%s;\n\t\tkw=%s' % (str(args), str(kw))
            msg = '\n\t%s\n\t\t%s' % (fmt1, fmt2)
            print(msg)
            myLogger.debug(msg)

            fmt1 = '%s.mainTest (command line argv): ' % label
            fmt2 = 'args=%s' % str(args)
            fmt3 = 'options (unsorted)=%s' % str(options)
            msg = '\n\t%s\n\t\t%s;\n\t\t%s' % (fmt1, fmt2, fmt3)
            print(msg)
            myLogger.debug(msg)

            fmt1 = '\n\t%s.mainTest (command line argv): ' % label
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
            myLogger.debug(msg)

        return (args, options)

    #----------------------------------------------------------------------

    def EntryPoint(*args, **kw):
        '''
        Application Programming Interface, It gathers and displays
        configuration parameters as keyword-value pair options and
        positional arguments.
        '''
        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='EntryPoint')
        fmt1 = '\n\n  EntryPoint:'
        fmt2 = '\n\n    myLogger=%s' % myLogger
        fmt3 = '\n\n    appLogger=%s' % myLogger.appLogger
        fmt4 = '\n\n    theLogName=%s' % myLogger.theLogName
        fmt5 = '\n\n    theLogPath=%s' % myLogger.theLogPath
        fmt6 = '\n\n    theLogThreshold=%s\n\n' % myLogger.theLogThreshold
        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6
        print(msg)
        myLogger.debug(msg)

        msg = '\n\n\tEntryPoint (parameters:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
            str(args), str(kw))
        print(msg)
        myLogger.debug(msg)

        if True:
            (args, options) = mainTest(*args, **kw)
        else:
            mainTest(*args, **kw)
            args = myApp.args
            options = myApp.options

        msg = '\n\n\tResults:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
            str(args), str(options))
        print(msg)
        myLogger.debug(msg)

    #----------------------------------------------------------------------

    myApp = wx.MultiFrameEnv(

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
        guiTopLevelObjectTitle= __title__,
#
        runTimeEntryPoint=EntryPoint)

    myApp.Wrapper()

