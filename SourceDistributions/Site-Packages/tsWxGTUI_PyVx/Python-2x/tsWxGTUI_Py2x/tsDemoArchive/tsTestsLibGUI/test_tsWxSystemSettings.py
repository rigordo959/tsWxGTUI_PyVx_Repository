#! /usr/bin/env python
#"Time-stamp: <05/08/2015  3:28:56 PM rsg>"
'''
test_tsWxSystemSettings.py - Application program to unit test the
features of the tsWxSystemSettings module.
'''
#################################################################
#
# File: test_tsWxSystemSettings.py
#
# Purpose:
#
#    Application program to unit test the features of the
#    tsWxSystemSettings module.
#
# Limitations:
#
#    The TeamSTARS "tsWxGTUI" Toolkit's tsWxSystem-
#    Settings module and this test/demonstration
#    module emulate many but not all features of
#    their "wxPython" counterparts.
#
#    It also adds tests/demonstrations of internal
#    features associated with "character-mode".    
#
# Notes:
#
#    The C++ programming language based "tsWxWidgets"
#    Graphical User Interface (GUI) Toolkit has evolved
#    over many years. It can be used to develop and
#    operate user friendly "pixel-mode" application pro-
#    grams on a variety of computer hardware (32-bit/
#    64-bit) and software (Linux, Mac OS X, Microsoft
#    Windows and unix) platforms. It is a broadly sup-
#    ported, field proven and very popular cross-platform
#    software package. It also provides wrappers that
#    enable applications to be written in Python and
#    other programming languages.
#    
#    The TeamSTARS "tsWxGTUI" Toolkit provides a Python
#    programming language based character-mode emulation
#    of the Application Programming Interface (API) for
#    the pixel-mode "wxPython" wrapper. The emulation
#    facilitates the porting of "wxPython" applications
#    to low cost embedded computer systems having limited
#    processing, memory, network and input/output resources.
#
#    The TeamSTARS "tsWxGTUI" Toolkit provides a Python
#    programming language based character-mode emulation of
#    the Application Programming Interface (API) for the
#    pixel-mode "wxPython" wrapper to the c++ programming
#    language based "tsWxWidgets" Graphical User Interface
#    (GUI) Toolkit.
#
# Usage (example):
#
#     python test_tsWxSystemSettings.py
#
# Methods:
#
#     _Prototype
#     _Prototype.EntryPoint
#     _Prototype.OnAbout
#     _Prototype.OnHelp
#     _Prototype.OnMove
#     _Prototype.OnQuit
#     _Prototype.TestScrolled
#     _Prototype.__init__
#     _Prototype.exitTest
#     _Prototype.getEntrySettings
#     _Prototype.getOptions
#     _Prototype.tsGetTheId
#     _Prototype_three_panels
#     _Prototype_three_panels.OnAbout
#     _Prototype_three_panels.OnHelp
#     _Prototype_three_panels.OnMove
#     _Prototype_three_panels.OnQuit
#     _Prototype_three_panels.TestScrolled
#     _Prototype_three_panels.__init__
#     _Prototype_three_panels.getOptions
#     _Prototype_three_panels.tsGetTheId
#     nextWindowId
#     testCases
#     testCases.MainLoop
#     testCases.__init__
#     testCases.standardCase
#     testCases.verboseCase
#
# Modifications:
#
#    2014/12/12 rsg Incorporated GUI-style functionality from
#                   test_tsWxScrolledWindowDual.py.
#
#    2015/04/05 rsg Replaced "import tsWxGlobals as wx" by
#                   "import tsWx as wx" and made the associated
#                   references.
#
# ToDo:
#
#    2014/12/14 rsg Implement missing features of the metrics
#                   capability.
#
#    2014/12/14 rsg Resolve malfunctioning of Python 3x internal
#                   features of GetColour capability that other-
#                   wise operate normally under Python 2x.
#
#                   Only the first three of of the eight xterm
#                   keys are printed.
#
#################################################################

__title__     = 'test_tsWxSystemSettings'
__version__   = '1.3.0'
__date__      = '04/04/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2011-2015 Software Gadgetry. ' + \
                'All rights reserved.'
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = ''
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__,
                                         __line2__,
                                         __line3__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

from optparse import OptionParser

import curses
import os
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

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWx as wx

#--------------------------------------------------------------------------

class testCases(object):
    '''
    Conduct standard (wxPython/wxWidgets compliant) and verbose (non-standard)
    unit test of SystemSettings user callable methods:

        GetScreenType()
        SetScreenType(screen)
        GetFont(index)
        GetMetric(index)
        HasFeature(index)
        GetColour(index)
    '''

    #----------------------------------------------------------------------

    def __init__(self):
        '''
        '''
        self.logger = Logger.TsLogger(name='testCases_tsWxSystemSettings.txt',
                                      threshold=Logger.DEBUG)
        self.settings = wx.SystemSettings()
        self.testCaseSettings = []

    #----------------------------------------------------------------------

    def MainLoop(self):
        '''
        '''
        self.verboseCase()
        self.standardCase()
        return (self.testCaseSettings)

    #----------------------------------------------------------------------

    def standardCase(self):
        '''
        '''

        #------------------------------------------------------------------

        self.logger.debug(
            '\n%s Begin Standard Cases %s' % ('-' * 10, '-' * 30))
        self.testCaseSettings += [
            '\n%s Begin Standard Cases %s' % ('-' * 10, '-' * 30)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of GetScreenType *****')
        self.testCaseSettings += [
            '\n\n***** Case of GetScreenType *****']

        theValue = self.settings.GetScreenType()
        if (theValue == 4):

            self.logger.debug(
                '    %s for %s' % \
                (theValue, 'Screen Size >= 800x600 (100cols x 50rows)'))
            self.testCaseSettings += [
                '    %s for %s' % \
                (theValue, 'Screen Size >= 800x600 (100cols x 50rows)')]

        elif (theValue == 3):

            self.logger.debug(
                '    %s for %s' % \
                (theValue, '640x480 <= Screen Size < 800x600'))
            self.testCaseSettings += [
                '    %s for %s' % \
                (theValue, '640x480 <= Screen Size < 800x600')]

        elif (theValue == 2):

            self.logger.debug(
                '    %s for %s' % \
                (theValue, '320x240 <= Screen Size < 640x480'))
            self.testCaseSettings += [
                '    %s for %s' % \
                (theValue, '320x240 <= Screen Size < 640x480')]

        elif (theValue == 1):

            self.logger.debug(
                '    %s for %s' % \
                (theValue, '80x60 <= Screen Size < 320x240'))
            self.testCaseSettings += [
                '    %s for %s' % \
                (theValue, '80x60 <= Screen Size < 320x240')]

        else:

            self.logger.debug(
                '    %s for %s' % \
                (theValue, 'Screen Size < 80x60 (10cols x 5rows)'))
            self.testCaseSettings += [
                '    %s for %s' % \
                (theValue, 'Screen Size < 80x60 (10cols x 5rows)')]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of SetScreenType *****')
        self.testCaseSettings += [
            '\n\n***** Case of SetScreenType *****']

        for screen in sorted(self.settings.wxSystemScreenType, reverse=True):
            self.settings.SetScreenType(screen)
##            theValue = self.settings.GetScreenType()
            x = self.settings.wxSystemScreenType[screen]
            theName = x[0]
            theValue = x[1]

            if (screen == 4):

                self.logger.debug(
                    '    %s for %s' % \
                    (theValue, 'Screen Size >= 800x600 (100cols x 50rows)'))
                self.testCaseSettings += [
                    '    %s for %s' % \
                    (theValue, 'Screen Size >= 800x600 (100cols x 50rows)')]

            elif (screen == 3):

                self.logger.debug(
                    '    %s for %s' % \
                    (theValue, '640x480 <= Screen Size < 800x600'))
                self.testCaseSettings += [
                    '    %s for %s' % \
                    (theValue, '640x480 <= Screen Size < 800x600')]

            elif (screen == 2):

                self.logger.debug(
                    '    %s for %s' % \
                    (theValue, '320x240 <= Screen Size < 640x480'))
                self.testCaseSettings += [
                    '    %s for %s' % \
                    (theValue, '320x240 <= Screen Size < 640x480')]

            elif (screen == 1):

                self.logger.debug(
                    '    %s for %s' % \
                    (theValue, '80x60 <= Screen Size < 320x240'))
                self.testCaseSettings += [
                    '    %s for %s' % \
                    (theValue, '80x60 <= Screen Size < 320x240')]

            else:

                self.logger.debug(
                    '    %s for %s' % \
                    (theValue, 'Screen Size < 80x60 (10cols x 5rows)'))
                self.testCaseSettings += [
                    '    %s for %s' % \
                    (theValue, 'Screen Size < 80x60 (10cols x 5rows)')]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of GetFont *****')
        self.testCaseSettings += [
            '\n\n***** Case of GetFont *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemFont.keys())
        for theKey in keyList:
            theValue = self.settings.GetFont(theKey)
            self.logger.debug(
                '    %d %s' % (theKey, theValue))
            self.testCaseSettings += [
                '    %d %s' % (theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of GetMetric *****')
        self.testCaseSettings += [
            '\n\n***** Case of GetMetric *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemMetric.keys())
        for theKey in keyList:
            theValue = self.settings.GetMetric(theKey)
            self.logger.debug(
                '   %2d %s' % (theKey, theValue))
            self.testCaseSettings += [
                '   %2d %s' % (theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of HasFeature *****')
        self.testCaseSettings += [
            '\n\n***** Case of HasFeature *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemFeature.keys())
        for theKey in keyList:
            theValue = self.settings.HasFeature(theKey)
            self.logger.debug(
                '%3d %s' % (theKey, theValue))
            self.testCaseSettings += [
                '%3d %s' % (theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Case of GetColour *****')
        self.testCaseSettings += [
            '\n\n***** Case of GetColour *****']

##        if curses.has_colors():
##            if curses.COLOR_PAIRS >= 256:
##                theDataBase = tsWxGTUI16
##            else:
##                theDataBase = tsWxGTUI8
##        else:
##            theDataBase = tsWxGTUIMonochrome

####        keyList = sorted(
####            theDataBase.keys())
##        keyList = theDataBase.keys()

##        fmt1 = '\n  Available from "%s" ' % theDataBase['name']
##        fmt2 = 'via GetColour'
##        msg = fmt1 + fmt2
##        self.logger.debug(msg)
##        self.testCaseSettings += [msg]

##        for theKey in keyList:
##            if theKey != 'Name':
##                (theName, theValue) = self.settings.GetColour(
##                    theKey, verbose=True, internal=True)
##                if (not (theValue is None)):
##                    self.logger.debug(
##                        '  %3s %s' % (theKey, theValue))
##                    self.testCaseSettings += [
##                        '  %3s %s' % (theKey, theValue)]
##                else:
##                    pass
##            else:
##                pass

        keyList = sorted(
            wx.SystemSettings.wxSystemColour.keys())

        self.logger.debug(
            '\n  Available from "tsWxGlobals.py" via GetColour')
        self.testCaseSettings += [
            '\n  Available from "tsWxGlobals.py" via GetColour']

        for theKey in keyList:
            theValue = self.settings.GetColour(theKey)
            if (not (theValue is None)):
                self.logger.debug('%3d %s' % (theKey, theValue))
                self.testCaseSettings += ['%3d %s' % (theKey, theValue)]

        self.logger.debug(
            '\n  Unavailable from "tsWxGlobals.py" via GetColour')
        self.testCaseSettings += [
            '\n  Unavailable from "tsWxGlobals.py" via GetColour']

        for theKey in keyList:
            theValue = self.settings.GetColour(theKey)
            if (theValue is None):
                self.logger.debug('%3d %s' % (theKey, theValue))
                self.testCaseSettings += ['%3d %s' % (theKey, theValue)]

        #------------------------------------------------------------------
        self.logger.debug(
            '\n%s End   Standard Cases %s' % ('-' * 10, '-' * 30))
        self.testCaseSettings += [
            '\n%s End   Standard Cases %s' % ('-' * 10, '-' * 30)]

    #----------------------------------------------------------------------

    def verboseCase(self):
        '''
        '''

        #------------------------------------------------------------------

        self.logger.debug(
            '\n%s Begin Verbose  Cases %s' % ('-' * 10, '-' * 30))
        self.testCaseSettings += [
            '\n%s Begin Verbose  Cases %s' % ('-' * 10, '-' * 30)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of GetScreenType *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of GetScreenType *****']

        (theName, theValue) = self.settings.GetScreenType(verbose=True)
        if (theValue == 4):

            self.logger.debug(
                '%16s %s for %s' % \
                (theName, theValue,
                 'Screen Size >= 800x600 (100cols x 50rows)'))
            self.testCaseSettings += [
                '%16s %s for %s' % \
                (theName, theValue,
                 'Screen Size >= 800x600 (100cols x 50rows)')]

        elif (theValue == 3):

            self.logger.debug(
                '%16s %s for %s' % \
                (theName, theValue,
                 '640x480 <= Screen Size < 800x600'))
            self.testCaseSettings += [
                '%16s %s for %s' % \
                (theName, theValue,
                 '640x480 <= Screen Size < 800x600')]

        elif (theValue == 2):

            self.logger.debug(
                '%16s %s for %s' % \
                (theName, theValue,
                 '320x240 <= Screen Size < 640x480'))
            self.testCaseSettings += [
                '%16s %s for %s' % \
                (theName, theValue,
                 '320x240 <= Screen Size < 640x480')]

        elif (theValue == 1):

            self.logger.debug(
                '%16s %s for %s' % \
                (theName, theValue,
                 '80x60 <= Screen Size < 320x240'))
            self.testCaseSettings += [
                '%16s %s for %s' % \
                (theName, theValue,
                 '80x60 <= Screen Size < 320x240')]

        else:

            self.logger.debug(
                '%16s %s for %s' % \
                (theName, theValue,
                 'Screen Size < 80x60 (10cols x 5rows)'))
            self.testCaseSettings += [
                '%16s %s for %s' % \
                (theName, theValue,
                 'Screen Size < 80x60 (10cols x 5rows)')]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of SetScreenType *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of SetScreenType *****']

        for screen in sorted(self.settings.wxSystemScreenType, reverse=True):
            self.settings.SetScreenType(screen)
##            (theName, theValue) = self.settings.GetScreenType(verbose=True)
            x = self.settings.wxSystemScreenType[screen]
            theName = x[0]
            theValue = x[1]

            if (screen == 4):

                self.logger.debug(
                    '%16s %s for %s' % \
                    (theName, theValue,
                     'Screen Size >= 800x600 (100cols x 50rows)'))
                self.testCaseSettings += [
                    '%16s %s for %s' % \
                    (theName, theValue,
                     'Screen Size >= 800x600 (100cols x 50rows)')]

            elif (screen == 3):

                self.logger.debug(
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '640x480 <= Screen Size < 800x600'))
                self.testCaseSettings += [
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '640x480 <= Screen Size < 800x600')]

            elif (screen == 2):

                self.logger.debug(
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '320x240 <= Screen Size < 640x480'))
                self.testCaseSettings += [
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '320x240 <= Screen Size < 640x480')]

            elif (screen == 1):

                self.logger.debug(
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '80x60 <= Screen Size < 320x240'))
                self.testCaseSettings += [
                    '%16s %s for %s' % \
                    (theName, theValue,
                     '80x60 <= Screen Size < 320x240')]

            else:

                self.logger.debug(
                    '%16s %s for %s' % \
                    (theName, theValue,
                     'Screen Size < 80x60 (10cols x 5rows)'))
                self.testCaseSettings += [
                    '%16s %s for %s' % \
                    (theName, theValue,
                     'Screen Size < 80x60 (10cols x 5rows)')]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of GetFont *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of GetFont *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemFont.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.GetFont(
                theKey, verbose=True)
            self.logger.debug(
                '%27s %d %s' % (theName, theKey, theValue))
            self.testCaseSettings += [
                '%27s %d %s' % (theName, theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of GetMetric *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of GetMetric *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemMetric.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.GetMetric(
                theKey, verbose=True)
            self.logger.debug(
                '%26s %2d %s' % (theName, theKey, theValue))
            self.testCaseSettings += [
                '%26s %2d %s' % (theName, theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of HasFeature *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of HasFeature *****']

        keyList = sorted(
            wx.SystemSettings.wxSystemFeature.keys())
        for theKey in keyList:
            (theName, theValue) = self.settings.HasFeature(
                theKey, verbose=True)
            self.logger.debug(
                '%40s %3d %s' % (theName, theKey, theValue))
            self.testCaseSettings += [
                '%40s %3d %s' % (theName, theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n\n***** Verbose Case of GetColour *****')
        self.testCaseSettings += [
            '\n\n***** Verbose Case of GetColour *****']

##        if curses.has_colors():
##            if curses.COLOR_PAIRS >= 256:
##                theDataBase = tsWxGTUI16
##            else:
##                theDataBase = tsWxGTUI8
##        else:
##            theDataBase = tsWxGTUIMonochrome

##       ## keyListUnsorted = list(theDataBase.keys())
####        print('***** keyListUnsorted=%s' % str(keyListUnsorted))
####        keyListEdited = keyListUnsorted.remove('name')       
####        print('***** keyListEdited=%s' % str(keyListEdited))
##        ketList = theDataBase.keys() # sorted(keyListEdited)

##        fmt1 = '\n  Available from "%s" ' % theDataBase['name']
##        fmt2 = 'via GetColour'
##        msg = fmt1 + fmt2
##        self.logger.debug(msg)
##        self.testCaseSettings += [msg]

##        for theKey in keyList:
##            if theKey != 'Name':
##                (theName, theValue) = self.settings.GetColour(
##                    theKey, verbose=True, internal=True)
##                if (not (theValue is None)):
##                    self.logger.debug(
##                        '%40s %3s %s' % (theName, theKey, theValue))
##                    self.testCaseSettings += [
##                        '%40s %3s %s' % (theName, theKey, theValue)]
##                else:
##                    pass
##            else:
##                pass

        keyList = sorted(
            wx.SystemSettings.wxSystemColour.keys())

        self.logger.debug(
            '\n  Available from "tsWxGlobals.py" via GetColour')
        self.testCaseSettings += [
            '\n  Available from "tsWxGlobals.py" via GetColour']

        for theKey in keyList:
            (theName, theValue) = self.settings.GetColour(
                theKey, verbose=True)
            if (not (theValue is None)):
                self.logger.debug(
                    '%40s %3d %s' % (theName, theKey, theValue))
                self.testCaseSettings += [
                    '%40s %3d %s' % (theName, theKey, theValue)]

        self.logger.debug(
            '\n  Unavailable from "tsWxGlobals.py" via GetColour')
        self.testCaseSettings += [
            '\n  Unavailable from "tsWxGlobals.py" via GetColour']

        for theKey in keyList:
            (theName, theValue) = self.settings.GetColour(
                theKey, verbose=True)
            if (theValue is None):
                self.logger.debug(
                    '%40s %3d %s' % (theName, theKey, theValue))
                self.testCaseSettings += [
                    '%40s %3d %s' % (theName, theKey, theValue)]

        #------------------------------------------------------------------

        self.logger.debug(
            '\n%s End   Verbose  Cases %s' % ('-' * 10, '-' * 30))
        self.testCaseSettings += [
            '\n%s End   Verbose  Cases %s' % ('-' * 10, '-' * 30)]

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

class _Prototype_three_panels(wx.Frame):
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

        #-------------------------------------------------------------------

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

        self.panelT = wx.Panel(self.theFrame,
                               wx.ID_ANY,
                               label='Dual ScrollBars',
                               style=boxHorizontalPanelStyle)

        self.panelT.SetBackgroundColour("YELLOW")
        self.panelT.SetForegroundColour("BLACK")

        self.boxHorizontal.Add(self.panelT, proportion=1, flag=wx.EXPAND)

        #-------------------------------------------------------------------

        self.theFrame.SetAutoLayout(True)
        self.theFrame.SetSizer(self.boxHorizontal)
        self.theFrame.Layout()

        #-------------------------------------------------------------------

        theBorder = self.panelT.tsIsBorderThickness(
            self.panelT.ts_Style, pixels=True)

        self.theScrolledPanelT = wx.Scrolled(
            self.panelT,
            id=wx.ID_ANY,
            label='Peep Hole View',
            pos=(self.panelT.Rect.x + wx.pixelWidthPerCharacter,
                 self.panelT.Rect.y + wx.pixelHeightPerCharacter),
            size=(self.panelT.Rect.width - 2 * theBorder.width,
                  self.panelT.Rect.height - 2 * theBorder.height),
            # style=0,
            # style=wx.HSCROLL,
            # style=wx.VSCROLL,
            style=wx.HSCROLL | wx.VSCROLL,
            name=wx.ScrolledNameStr)

        self.theScrolledPanelT.Show(show=True)

        #-------------------------------------------------------------------

        app = testCases()

        self.testCaseSettings = app.MainLoop()

        #-------------------------------------------------------------------

        theCount = 0
        for item in self.testCaseSettings:
            lines = item.split('\n')
            for theLine in lines:
                self.theScrolledPanelT.tsAppendText(
                    '%3d %s' % (theCount, theLine))
                theCount += 1

##        attr = wx.DISPLAY_BOLD # wx.DISPLAY_REVERSE
##        attrColorPair = self.GetAttributeValueFromColorPair(
##                'black',
##                'red')

##        self.theScrolledPanelT.tsAppendText(
##            '         1         2         3         4         5' + \
##            '         6         7         8',
##            wx.DISPLAY_BOLD)

##        self.theScrolledPanelT.tsAppendText(
##            '12345678901234567890123456789012345678901234567890' + \
##            '123456789012345678901234567890',
##            wx.DISPLAY_BOLD | wx.DISPLAY_UNDERLINE)

##        self.theScrolledPanelT.tsAppendText(
##            'Peep Hole View Wider Text' + \
####            '\nLine #2' + \
####            '\nLine #3' + \
##            '\nLine #4')

##        self.theScrolledPanelT.tsAppendText(
##            'Another Peep Hole View Wider Text\nLine #6\nLine #7\nLine #8',
##            markup=attr)

##        self.theScrolledPanelT.tsAppendText(
##            'Another Peep Hole View Wider Text\nLine #10\nLine #11\nLine #12',
##            markup=attrColorPair)

##        attr = wx.DISPLAY_REVERSE
##        attrColorPair = self.GetAttributeValueFromColorPair(
##                'black',
##                'red')

##        self.theScrolledPanelT.tsAppendText(
##            'Another Peep Hole View Wider Text\nLine #14\nLine #15\nLine #16',
##            markup=attr | attrColorPair)

##        self.theScrolledPanelT.tsAppendText(
##            'Another Peep Hole View Wider Text\nLine #18\nLine #19\nLine #20')

##        self.theScrolledPanelT.tsAppendText(
##            'Another Peep Hole View Wider Text\nLine #22\nLine #23\nLine #24')

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
