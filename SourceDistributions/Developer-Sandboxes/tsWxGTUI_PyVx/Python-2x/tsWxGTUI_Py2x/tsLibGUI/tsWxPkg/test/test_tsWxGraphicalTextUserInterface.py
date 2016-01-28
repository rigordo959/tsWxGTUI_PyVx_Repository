#! /usr/bin/env python
#"Time-stamp: <12/02/2014  9:55:04 AM rsg>"
'''
test_tsWxGraphicalTextUserInterface.py - Demonstration and
design verification test of the foreground/background color
pairs provided by the "tsWxGTUI" Toolkit and its character-
mode emulation of the pixel-mode "wxPython" Graphical User
Interface.
'''
#################################################################
#
# File: test_tsWxGraphicalTextUserInterface.py
#
# Purpose:
#
#     Demonstration and design verification test of the
#     foreground/background color pairs provided by
#     the "tsWxGTUI" Toolkit and its character-mode
#     emulation of the pixel-mode "wxPython" Graphical
#     User Interface.
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
#     python test_tsWxGraphicalTextUserInterface.py
#
# Methods:
#
#    sample
#    sample.EntryPoint
#    sample.__init__
#    sample.colorPairTest
#    sample.colorPairTestExtended
#    sample.exitTest
#    sample.getEntrySettings
#    sample.monochromeTest
#    sample.testGetBuiltinPaletteRGB
#    sample.testGetColorDataBase
#    sample.testGetColorDataBaseID
#    sample.testGetColorDataBasePairID
#    sample.testGetColorDataBaseRGB
#    sample.testGetGeometry
#    sample.testSupervisor
#
# Modifications:
#
#    2013/07/17 rsg Redesigned to use tsCommandLineEnv and
#                   tsLogger.
#
#    2013/12/29 rsg Added logic to capture and log the various
#                   color databases in order to properly size
#                   the test annotations.
#
#    2013/12/29 rsg Redesigned to reduce size of color test
#                   area and display annotation in white on
#                   black.
#
#    2014/01/03 rsg Added support for xterm-16color.
#
#    2014/01/17 rsg Added support for xterm-88color and
#                   xterm-256color. Also adopted method
#                   tsGetSetToUseColorCodeFromName,
#                   switched ForegroundColor from inner to
#                   outer loop and BackgroundColor from
#                   outer to inner loop.
#
#    2014/01/27 rsg Re-designed test to identify:
#                   Test Case: Number of Maximum
#                   Color Names: Foreground and Background
#                   Characer Cell Atributes:
#                       Alternate, Blink, Bold, Dim,
#                       Normal, Reverse, Standout, Underline
#
#    2014/10/18 rsg Updated test to ensure that "Built-In" and
#                   "tsWxGTUI" color palette designations
#                   reflect the curses.can_change_color state.
#
#    2014/10/25 rsg Added logic to apply curses.A_REVERSE
#                   attribute to header lines for fmt2 and fmt5.
#
#    2014/10/26 rsg Added logic to apply control switch
#                   USE_256_COLOR_PAIR_LIMIT.
#
#    2014/10/28 rsg Added logic to apply curses.A_REVERSE
#                   to headers associated with fmt2 and fmt5.
#
#    2014/11/21 rsg Modified design to speed up testing and
#                   to resolve undocumented curses limitation
#                   of 256 maximum color pairs.
#
#                   Modified formatting of "TEXT ATTRIBUTE"
#                   line 5 to include "NxN COLOR PAIRS" prefix
#                   in order to clarify the number of cases.
#
#    2014/11/24 rsg Added 'linux' to the supported terminal emulator
#                   types.
#
#    2014/12/02 rsg Fixed Monochrome Test to use white-on-black or
#                   black-on-white based on wxThemeToUse.
#                   Changed color code for white to -1 from 1.
#
#    2014/12/02 rsg Fixed colorPairTest and colorPairTestExtended
#                   to always use white-on-black regardless
#                   of wxThemeToUse.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'test_tsWxGraphicalTextUserInterface'
__version__   = '2.14.1'
__date__      = '12/92/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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
                '\n\t\t\twxWidgets team.' + \
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

#---------------------------------------------------------------------------

import curses
import os.path
import sys
import time
import traceback

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

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

##    import tsApplication as tsAPP
    import tsExceptions as tse
    import tsLogger
    import tsCommandLineEnv
    import tsOperatorSettingsParser
    from tsReportUtilities import TsReportUtilities as tsrpu

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

    import tsWx as wx
##    import tsWxMultiFrameEnv
    from tsWxGlobals import ThemeToUse as wxThemeToUse
    from tsWxGlobals import USE_256_COLOR_PAIR_LIMIT

    from tsWxGraphicalTextUserInterface \
         import GraphicalTextUserInterface as gtui

    from tsWxPythonColor8SubstitutionMap import *
    from tsWxPythonColor16SubstitutionMap import *

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

except Exception, exceptionCode:

    print('%s: Exception (tsLibGUI); ' % __title__ + \
          'exceptionCode=%s' % str(exceptionCode))

#---------------------------------------------------------------------------

#--------------------------------------------------------------------------

# Begin Test Control Switches
DEBUG = True
VERBOSE = False
viewingMilliSeconds = 500

StandardTerminalEmulators = wxThemeToUse['StandardTerminalEmulators'] 

##StandardTerminalEmulators = {
##        'name': 'StandardTerminalEmulators',
##        'BlackOnWhiteDefault': [
##            'linux'],
##        'WhiteOnBlackDefault': [
##            'ansi',
##            'cygwin',
##            'vt100',
##            'vt220',
##            'xterm',
##            'xterm-16color',
##            'xterm-256color',
##            'xterm-88color',
##            'xterm-color'],
##        'nonColorTerminals': [
##            'vt100',
##            'vt220'],
##        'supportedTermCaps': [
##            'cygwin',
##            'linux',
##            'vt100',
##            'vt220',
##            'xterm',
##            'xterm-color',
##            'xterm-16color',
##            'xterm-88color',
##            'xterm-256color'],
##        'unsupportedTermCaps': [
##            'ansi']
##        }

##myLevel = 0
##myFile = open('./junk.txt', 'w')
myDictionary = StandardTerminalEmulators

##tsrpu.displayDictionary(myLevel, myDictionary, myFile, myLogger=None)
print('##### myDictionary: %s' % str(myDictionary))

BlackOnWhiteDefault = myDictionary['BlackOnWhiteDefault']
WhiteOnBlackDefault = myDictionary['WhiteOnBlackDefault']
nonColorTerminals   = myDictionary['nonColorTerminals']
supportedTermCaps   = myDictionary['supportedTermCaps']
unsupportedTermCaps = myDictionary['unsupportedTermCaps']

# End Test Control Switches

#--------------------------------------------------------------------------

__help__ = '''
Append " -h" or " --help" to the command line before using the
"ENTER/RETURN" key.
'''

#--------------------------------------------------------------------------

class sample(object):

    def __init__(self):
        '''
        Class constructor.
        '''

        print(__header__)

        self.sample_max_colors = 0
        self.sample_max_color_pairs = 0

    #-------------------------------------------------------------------

    def testGetBuiltinPaletteRGB(self):
        '''
        Return the Red, Green and Blue settings for the built-in color
        palette.
        '''
        self.myLogger.notice(
            'testGetBuiltinPaletteRGB: %s' % str(
                gtui.BuiltinPaletteRGB))
        theKeys = sorted(list(gtui.BuiltinPaletteRGB.keys()))
        maxLength = 0
        for item in theKeys:
            if item != 'name':
                maxLength = max(maxLength, len(item))

        for item in theKeys:
            if item != 'name':
                fill = ' ' * (maxLength - len(item))
                colorName = item
                theValue = gtui.BuiltinPaletteRGB[item]
                red = theValue[0]
                green = theValue[1]
                blue = theValue[2]
                hexRGB = (red << 16) + (green << 8) + (blue)
                self.myLogger.debug(
                    '%s%s rgb=0x%6.6X' % (colorName, fill, hexRGB))

        return (gtui.BuiltinPaletteRGB)

    #-------------------------------------------------------------------

    def testGetColorDataBase(self):
        '''
        Return the Color Data Base dictionary of color names and their
        associated color IDs.
        '''
        self.myLogger.notice(
            'testGetColorDataBase: %s' % str(
                gtui.ColorDataBase))
        theKeys = sorted(gtui.ColorDataBase.keys())
        maxLength = 0
        for item in theKeys:
            if item != 'name':
                maxLength = max(maxLength, len(item))

        for item in theKeys:
            if item != 'name':
                fill = ' ' * (maxLength - len(item))
                colorName = item
                theValue = gtui.ColorDataBase[item]
                self.myLogger.debug(
                    '%s%s colorID=%d' % (colorName, fill, theValue))
        return (gtui.ColorDataBase)

    #-------------------------------------------------------------------

    def testGetColorDataBaseID(self):
        '''
        Return the Color Data Base dictionary of color IDs and their
        associated color names.
        '''
        self.myLogger.notice(
            'testGetColorDataBaseID: %s' % str(
                gtui.ColorDataBaseID))
        theKeys = gtui.ColorDataBaseID.keys()
        theColorID = []
        for item in theKeys:
            if item != 'name':
                theColorID += [item]
        
        theKeys = sorted(theColorID)
        for item in theKeys:
            if item != 'name':
                colorID = item
                colorName = gtui.ColorDataBaseID[item]
                self.myLogger.debug(
                    'colorID=%d; colorName=%s' % (colorID, colorName))
        return (gtui.ColorDataBaseID)

    #-------------------------------------------------------------------

    def testGetColorDataBasePairID(self):
        '''
        Return the Color Data Base dictionary of color pair IDs and their
        associated foreground and background color names.

        Step 1. Get Color Pair from each Color Pair ID.
        Step 2. Get Color Pair ID from each Step 1 Color Pair
        Step 3. Verify match between Step 1 and Step 2 Color Pair IDs.
        '''
        self.myLogger.notice(
            'testGetColorDataBasePairID (two-way comparison): %s' % str(
                gtui.ColorDataBasePairID))

        theKeys = gtui.ColorDataBasePairID[
            'ColorNumbersFromPairNumbers'].keys()
        theColorPairID = []
        for item in theKeys:
            if item != 'name':
                theColorPairID += [item]
        
        theKeys = sorted(theColorPairID)

        for item in theKeys:
            if item != 'name':
                colorPairID = item
                colorPair = gtui.ColorDataBasePairID[
                    'ColorNumbersFromPairNumbers'][item]
                self.myLogger.debug(
                    'colorPairID=%d; colorPair=%s' % (colorPairID,
                                                      str(colorPair)))

                colorPairID_2nd = gtui.ColorDataBasePairID[
                    'PairNumbersFromColorNumbers'][colorPair]
                if colorPairID_2nd != colorPairID:
                    self.myLogger.error(
                        'colorPair=%s; colorPairID=%d' % (str(colorPair),
                                                          colorPairID_2nd))

        return (gtui.ColorDataBasePairID)

    #-------------------------------------------------------------------

    def testGetColorDataBaseRGB(self):
        '''
        Return the Red, Green and Blue settings for all color names
        in the color data base.
        '''
        self.myLogger.notice(
            'testGetColorDataBaseRGB: %s' % str(
                gtui.ColorDataBaseRGB))

        theKeys = sorted(gtui.ColorDataBaseRGB.keys())
        maxLength = 0
        for item in theKeys:
            if item != 'name':
                maxLength = max(maxLength, len(item))

        for item in theKeys:
            if item != 'name':
                fill = ' ' * (maxLength - len(item))
                colorName = item
                theValue = gtui.ColorDataBaseRGB[item]
                red = theValue[0]
                green = theValue[1]
                blue = theValue[2]
                hexRGB = (red << 16) + (green << 8) + (blue)
                self.myLogger.debug(
                    '%s%s rgb=0x%6.6X' % (colorName, fill, hexRGB))

        return (gtui.ColorDataBaseRGB)

    #-------------------------------------------------------------------

    def testGetGeometry(self):
        '''
        Return the console display geometry, in wxPython format
        (stdscrX, stdscrY, stdscrWidth, stdscrHeight) rather
        than in curses format (getbegyx: a tuple (y, x) of co-ordinates
        of upper-left corner; and getmaxyx, a tuple (y, x) of the height
        and width of the window).
        '''
        
        # theRect = wxRect(stdscrX, stdscrY, stdscrWidth, stdscrHeight)
        theRect = gtui.StdscrGeometry

        return (theRect)

    #-------------------------------------------------------------------

    def testSupervisor(self):
        '''
        Initiate, select and control the sequence of tests of the
        tsWxGraphicalTextUserInterface.
        '''
        theCallerClass = self
        self.myLogger = tsLogger.TsLogger(
            threshold=tsLogger.DEBUG,
            start=time.time(),
            name='ColorPairValidation.log')

        self.ts_myGTUI = gtui(theCallerClass)
        if self.ts_myGTUI.HasColors:

            self.testGetBuiltinPaletteRGB()
            self.testGetColorDataBase()
            self.testGetColorDataBaseID()
            self.testGetColorDataBasePairID()
            self.testGetColorDataBaseRGB()

            if (((self.ts_myGTUI.TermName == 'cygwin') or \
                 (self.ts_myGTUI.TermName == 'xterm')) or \
                 (self.ts_myGTUI.TermName == 'xterm-color')):

                self.colorPairTest()
                self.colorPairTestExtended()

            elif (self.ts_myGTUI.TermName == 'xterm-16color'):

                self.colorPairTest()
                self.colorPairTestExtended()

            elif (self.ts_myGTUI.TermName == 'xterm-88color'):

                self.colorPairTest()
                self.colorPairTestExtended()

            elif (self.ts_myGTUI.TermName == 'xterm-256color'):

                self.colorPairTest()
                self.colorPairTestExtended()

            elif (self.ts_myGTUI.TermName == 'linux'):

                self.colorPairTest()
                self.colorPairTestExtended()

            else:

                self.colorPairTest()
                self.colorPairTestExtended()

        else:

            self.monochromeTest()

        self.ts_myGTUI.stop()

##            self.myLogger.close()

    #-------------------------------------------------------------------

    def monochromeTest(self):
        '''
        Conduct the tsWxGraphicalTextUserInterface tests of the
        non-color vt100/vt220 terminals and associated terminal
        emulators. The background color is always black. The
        foreground color is that of the single color phosphor
        (green, orange or white).
        #
        #    2014/01/25 rsg Re-designed test to identify:
        #                   Test Case: Number of Maximum
        #                   Color Names: Foreground and Background
        #                   Characer Cell Atributes:
        #                       Alternate, Blink, Bold, Dim,
        #                       Normal, Reverse, Standout, Underline
        #
        '''
        termName = self.ts_myGTUI.TermName.upper()
        template = '''
                     1         2         3         4         5
           0123456789012345678901234567890123456789012345678901234567
         0 +--------------------------------------------------------+
         1 | CASE nnnnn of MMMMM for TermName:                      |
         2 |             COLOR NAME             ( ID) [ SAMPLE    ] |
         3 | FOREGROUND:                  white ( -1) [           ] |
         4 | BACKGROUND:                  black (  0) [           ] |
         5 |                           TEXT ATTRIBUTE [ SAMPLE    ] |
         6 |                           ALTCHARSET     [ ALTCHARSET] |
         7 |                           Blink          [ Blink     ] |
         8 |                           Bold           [ Bold      ] |
         9 |                           Dim            [ Dim       ] |
        10 |                           Normal         [ Normal    ] |
        11 |                           Reverse        [ Reverse   ] |
        12 |                           Standout       [ Standout  ] |
        13 |                           Underline      [ Underline ] |
        14 +--------------------------------------------------------+
        '''
        theRect = self.testGetGeometry()
        self.myLogger.debug('monochromeTest: theRect=%s' % str(theRect))

        # Non-Color terminals are always white on black
        sampleWindowForeground = 'white'
        sampleWindowBackground = 'black'

        set_to_use = {
            0: sampleWindowBackground,
            -1: sampleWindowForeground}

        self.myLogger.debug(
            'monochromeTest:  foreground=%s; background=%s' % (
                sampleWindowForeground, sampleWindowBackground))

        theText = template.split('\n')

        textLines = len(theText) - 4
        textCols = 0
        for aLine in theText:
            textCols = max(textCols, len(aLine))
        nlines = textLines
        ncols = textCols - 8
        begin_y = 0
        begin_x = 0
        sampleWindow = {}

        maxColors = 1
        maxCases = 1
        attribute = curses.A_NORMAL

        sampleWindow = curses.newwin(nlines,
                                     ncols,
                                     begin_y,
                                     begin_x)

        maxIdLength = len(' (%d)' % len(set_to_use))
        maxColorLength = 0
        for id in sorted(list(set_to_use.keys())):
            maxColorLength = max(maxColorLength, len(set_to_use[id]))

        ID = 1
        # Non-Color terminals are always white on black
        bg = 0
        fg = -1
        background = set_to_use[bg]
        foreground = set_to_use[fg]

        sampleWindow.border()

##        fmt01 = 'Case %d of %d for %s:' % (ID, maxCases, termName)
##        fmt02 = '            [ COLOR NAME             ( ID) ] '  \
##               '[   Sample  ]'

        palette = gtui.TermName
        fmt01 = 'Case %d of %d for %s:' % (ID, maxCases, termName)
        fmt02 = '            [             COLOR NAME ( ID) ] '  \
               '[   %-5s  ]' % palette.upper()

        fmt03 = 'Foreground: [ %22s (%3d) ] [   Sample  ]' % (
            foreground, fg)
        fmt04 = 'Background: [ %22s (%3d) ] [   Sample  ]' % (
            background, bg)
        fmt05 = '%44s [   Sample  ]' % 'TEXT ATTRIBUTE'
        fmt06 = '%44s [   Sample  ]' % 'Altcharset'
        fmt07 = '%44s [   Sample  ]' % 'Blink'
        fmt08 = '%44s [   Sample  ]' % 'Bold'
        fmt09 = '%44s [   Sample  ]' % 'Dim'
        fmt10 = '%44s [   Sample  ]' % 'Normal'
        fmt11 = '%44s [   Sample  ]' % 'Reverse'
        fmt12 = '%44s [   Sample  ]' % 'Standout'
        fmt13 = '%44s [   Sample  ]' % 'Underline'

        msg = fmt01 + fmt02 + fmt03 # + fmt4
        sampleWindow.addstr(begin_y + 1,
                            begin_x + 1,
                            fmt01)

        sampleWindow.attron(curses.A_REVERSE)
        sampleWindow.addstr(begin_y + 2,
                            begin_x + 1,
                            fmt02)
        sampleWindow.attroff(curses.A_REVERSE)

        sampleWindow.addstr(begin_y + 3,
                            begin_x + 1,
                            fmt03)
        sampleWindow.addstr(begin_y + 4,
                            begin_x + 1,
                            fmt04)

        sampleWindow.attron(curses.A_REVERSE)
        sampleWindow.addstr(begin_y + 5,
                            begin_x + 1,
                            fmt05)
        sampleWindow.attroff(curses.A_REVERSE)

        sampleWindow.addstr(begin_y + 6,
                            begin_x + 1,
                            fmt06)
        sampleWindow.addstr(begin_y + 7,
                            begin_x + 1,
                            fmt07)
        sampleWindow.addstr(begin_y + 8,
                            begin_x + 1,
                            fmt08)
        sampleWindow.addstr(begin_y + 9,
                            begin_x + 1,
                            fmt09)
        sampleWindow.addstr(begin_y + 10,
                            begin_x + 1,
                            fmt10)
        sampleWindow.addstr(begin_y + 11,
                            begin_x + 1,
                            fmt11)
        sampleWindow.addstr(begin_y + 12,
                            begin_x + 1,
                            fmt12)
        sampleWindow.addstr(begin_y + 13,
                            begin_x + 1,
                            fmt13)

        sampleWindow.attron(curses.A_REVERSE)
        sampleWindow.addstr(begin_y + 3,
                            begin_x + 48,
                            '        ')
        sampleWindow.attroff(curses.A_REVERSE)

        sampleWindow.attron(curses.A_NORMAL)
        sampleWindow.addstr(begin_y + 4,
                            begin_x + 48,
                            '        ')
        sampleWindow.attroff(curses.A_NORMAL)

##      sampleWindow.attron(curses.A_NORMAL)
##      sampleWindow.addstr(begin_y + 5,
##                          begin_x + 48,
##                          '   Sample  ')
##      sampleWindow.attroff(curses.A_NORMAL)

        sampleWindow.attron(curses.A_NORMAL)
        sampleWindow.addstr(begin_y + 6,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_ALTCHARSET)

        sampleWindow.attron(curses.A_BLINK)
        sampleWindow.addstr(begin_y + 7,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_BLINK)

        sampleWindow.attron(curses.A_BOLD)
        sampleWindow.addstr(begin_y + 8,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_BOLD)

        sampleWindow.attron(curses.A_DIM)
        sampleWindow.addstr(begin_y + 9,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_DIM)

        sampleWindow.attron(curses.A_NORMAL)
        sampleWindow.addstr(begin_y + 10,
                            begin_x + 48,
                            '  Sample  ')
        sampleWindow.attroff(curses.A_NORMAL)

        sampleWindow.attron(curses.A_REVERSE)
        sampleWindow.addstr(begin_y + 11,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_REVERSE)

        sampleWindow.attron(curses.A_STANDOUT)
        sampleWindow.addstr(begin_y + 12,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_STANDOUT)

        sampleWindow.attron(curses.A_UNDERLINE)
        sampleWindow.addstr(begin_y + 13,
                            begin_x + 48,
                            '  Sample ')
        sampleWindow.attroff(curses.A_UNDERLINE)

        self.myLogger.debug('%s\n' % msg)

        sampleWindow.refresh()

        curses.doupdate()
        curses.napms(viewingMilliSeconds * 5)
        sampleWindow.clear()

    #-------------------------------------------------------------------

    def colorPairTest(self):
        '''
        Conduct the tsWxGraphicalTextUserInterface tests of the
        xterm, xterm-color and xterm-16color terminal emulators.
        #
        #    2014/01/25 rsg Re-designed test to identify:
        #                   Test Case: Number of Maximum
        #                   Color Names: Foreground and Background
        #                   Characer Cell Atributes:
        #                       Alternate, Blink, Bold, Dim,
        #                       Normal, Reverse, Standout, Underline
        #
        '''
        termName = self.ts_myGTUI.TermName.upper()
        template = '''
                     1         2         3         4         5
           0123456789012345678901234567890123456789012345678901234567
         0 +--------------------------------------------------------+
         1 | CASE nnnnn of MMMMM for TermName:                      |
         2 |             COLOR NAME             ( ID) [ SAMPLE    ] |
         3 | FOREGROUND: light goldenrod yellow (255) [           ] |
         4 | BACKGROUND:                  black (  0) [           ] |
         5 |                           TEXT ATTRIBUTE [ SAMPLE    ] |
         6 |                           ALTCHARSET     [ ALTCHARSET] |
         7 |                           Blink          [ Blink     ] |
         8 |                           Bold           [ Bold      ] |
         9 |                           Dim            [ Dim       ] |
        10 |                           Normal         [ Normal    ] |
        11 |                           Reverse        [ Reverse   ] |
        12 |                           Standout       [ Standout  ] |
        13 |                           Underline      [ Underline ] |
        14 +--------------------------------------------------------+
        '''
        theRect = self.testGetGeometry()
        self.myLogger.debug('colorPairTest: theRect=%s' % str(theRect))

        theText = template.split('\n')

        textLines = len(theText) - 4
        textCols = 0
        for aLine in theText:
            textCols = max(textCols, len(aLine))
        nlines = textLines
        ncols = textCols - 8
        begin_y = 0
        begin_x = 0
        sampleWindow = {}

##        if (termName in WhiteOnBlackDefault):
##            # This configuration cannot display black
##            sampleWindowForeground = 'white'
##            sampleWindowBackground = 'black'
##        else:
##            sampleWindowForeground = 'black'
##            sampleWindowBackground = 'white'

        sampleWindowForeground = 'white'
        sampleWindowBackground = 'black'

        set_to_use = self.ts_myGTUI.tsGetSetToUseForColorCodeFromName()
        maxColors = len(set_to_use)
        maxCases = maxColors**2

##        attribute = curses.A_STANDOUT | curses.A_BOLD
        attribute = curses.A_NORMAL

        sampleWindow = curses.newwin(nlines,
                                     ncols,
                                     begin_y,
                                     begin_x)

##        begin_y = -1
##        begin_x = 1
        
##        for aLine in theText:
##            begin_y +=1
##            sampleWindow.addstr(begin_y,
##                                begin_x,
##                                aLine)
##      sampleWindow.refresh()

##      curses.doupdate()
##      curses.napms(viewingMilliSeconds)
##      sampleWindow.clear()

        set_to_use = self.ts_myGTUI.tsGetSetToUseForColorNameFromCode()
        maxIdLength = len(' (%d)' % len(set_to_use))
        maxColorLength = 0
        for id in sorted(list(set_to_use.keys())):
            maxColorLength = max(maxColorLength, len(set_to_use[id]))

        color_pair_content = self.ts_myGTUI.tsGetCursesPairContent
        color_pair_number = self.ts_myGTUI.tsGetColorPairNumber
        color_attribute = self.ts_myGTUI.tsGetAttributeValueFromColorPair

        self.sample_max_colors = len(set_to_use)
        self.sample_max_color_pairs = int(
            self.sample_max_colors**2)

        ID = 0
        for bg in sorted(list(set_to_use.keys())):
            background = set_to_use[bg]
            for fg in sorted(list(set_to_use.keys())):
                foreground = set_to_use[fg]
                ID += 1
##                color_pair = color_pair_number(
##                    foreground,
##                    background)

                sampleWindow.border()
                sampleWindow.bkgd(
                    ' ',
                    color_attribute(sampleWindowForeground,
                                    sampleWindowBackground))

##                fmt01 = 'Case %d of %d for %s:' % (ID, maxCases, termName)

##                fmt02 = '            [ COLOR NAME             ( ID) ] '  \
##                       '[   Sample  ]'

                if gtui.CanChangeColor:
                    palette = 'tsWxGTUI'
                else:
                    palette = 'Built-In'
                fmt01 = 'Case %d of %d for %s:' % (ID, maxCases, termName)
                fmt02 = '            [             COLOR NAME ( ID) ] '  \
                       '[ %-8s  ]' % palette
                fmt03 = 'Foreground: [ %22s (%3d) ] [   Sample  ]' % (
                    foreground, fg)
                fmt04 = 'Background: [ %22s (%3d) ] [   Sample  ]' % (
                    background, bg)

                if ((self.ts_myGTUI.TermName == 'cygwin') or \
                    (self.ts_myGTUI.TermName == 'xterm') or \
                    (self.ts_myGTUI.TermName == 'xterm-color')):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                elif (self.ts_myGTUI.TermName == 'xterm-16color'):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                        
                    fmt05 = '%44s [   Sample  ]' % prefix

                elif (((self.ts_myGTUI.TermName == 'xterm-88color') or \
                       (self.ts_myGTUI.TermName == 'xterm-256color')) and \
                      (maxCases == 256)):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                elif (self.ts_myGTUI.TermName == 'xterm-88color'):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                else:

                    # (self.ts_myGTUI.TermName == 'xterm-256color'):
                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                fmt06 = '%44s [   Sample  ]' % 'Altcharset'
                fmt07 = '%44s [   Sample  ]' % 'Blink'
                fmt08 = '%44s [   Sample  ]' % 'Bold'
                fmt09 = '%44s [   Sample  ]' % 'Dim'
                fmt10 = '%44s [   Sample  ]' % 'Normal'
                fmt11 = '%44s [   Sample  ]' % 'Reverse'
                fmt12 = '%44s [   Sample  ]' % 'Standout'
                fmt13 = '%44s [   Sample  ]' % 'Underline'

##                fmt1 = 'Case %d; "%s" (%d) on "%s" (%d); ' % (
##                    ID, foreground, fg, background, bg)
##                fmt2 = 'Color Pair %d; Pair Content %s' % (
##                    color_pair, str(color_pair_content(color_pair)))
                msg = fmt01 + fmt02 + fmt03 # + fmt4
                sampleWindow.addstr(begin_y + 1,
                                    begin_x + 1,
                                    fmt01)

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(sampleWindowForeground,
                                                    sampleWindowBackground))
                sampleWindow.addstr(begin_y + 2,
                                    begin_x + 1,
                                    fmt02)
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(sampleWindowForeground,
                                                     sampleWindowBackground))

                sampleWindow.addstr(begin_y + 3,
                                    begin_x + 1,
                                    fmt03)
                sampleWindow.addstr(begin_y + 4,
                                    begin_x + 1,
                                    fmt04)

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(sampleWindowForeground,
                                                    sampleWindowBackground))
                sampleWindow.addstr(begin_y + 5,
                                    begin_x + 1,
                                    fmt05)
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(sampleWindowForeground,
                                                     sampleWindowBackground))

                sampleWindow.addstr(begin_y + 6,
                                    begin_x + 1,
                                    fmt06)
                sampleWindow.addstr(begin_y + 7,
                                    begin_x + 1,
                                    fmt07)
                sampleWindow.addstr(begin_y + 8,
                                    begin_x + 1,
                                    fmt08)
                sampleWindow.addstr(begin_y + 9,
                                    begin_x + 1,
                                    fmt09)
                sampleWindow.addstr(begin_y + 10,
                                    begin_x + 1,
                                    fmt10)
                sampleWindow.addstr(begin_y + 11,
                                    begin_x + 1,
                                    fmt11)
                sampleWindow.addstr(begin_y + 12,
                                    begin_x + 1,
                                    fmt12)
                sampleWindow.addstr(begin_y + 13,
                                    begin_x + 1,
                                    fmt13)

                sampleWindow.attron(attribute | \
                                    color_attribute(foreground,
                                                    foreground))
                sampleWindow.addstr(begin_y + 3,
                                    begin_x + 48,
                                    '         ')
                sampleWindow.attroff(attribute | \
                                     color_attribute(foreground,
                                                     foreground))

                sampleWindow.attron(attribute | \
                                    color_attribute(background,
                                                    background))
                sampleWindow.addstr(begin_y + 4,
                                    begin_x + 48,
                                    '         ')
                sampleWindow.attroff(attribute | \
                                     color_attribute(background,
                                                     background))

##                sampleWindow.attron(curses.A_NORMAL | \
##                                    color_attribute(foreground,
##                                                    background))
##                sampleWindow.addstr(begin_y + 5,
##                                    begin_x + 48,
##                                    ' Sample    ')
##                sampleWindow.attroff(curses.A_NORMAL | \
##                                   color_attribute(foreground,
##                                                   background))

                sampleWindow.attron(curses.A_NORMAL | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 6,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_ALTCHARSET | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_BLINK | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 7,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_BLINK | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_BOLD | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 8,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_BOLD | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_DIM | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 9,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_DIM | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_NORMAL | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 10,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_NORMAL | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 11,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_STANDOUT | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 12,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_STANDOUT | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_UNDERLINE | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 13,
                                    begin_x + 48,
                                    '  Sample ')
                sampleWindow.attroff(curses.A_UNDERLINE | \
                                     color_attribute(foreground,
                                                     background))

                self.myLogger.debug('%s\n' % msg)
##                self.myLogger.write('%s\n' % msg)
##                self.myLogger.flush()
##                sampleWindow.attron(attribute | \
##                                    color_attribute(foreground,
##                                                    background))
##                sampleWindow.addstr(begin_y + 5,
##                                    begin_x + 1,
##                                    fmt1)
##                sampleWindow.addstr(begin_y + 6,
##                                    begin_x + 1,
##                                    fmt2)
##                sampleWindow.addstr(begin_y + 7,
##                                    begin_x + 1,
##                                    fmt3)
##                sampleWindow.addstr(begin_y + 8,
##                                    begin_x + 1,
##                                    fmt4)
##                sampleWindow.attroff(attribute | \
##                                     color_attribute(foreground,
##                                                     background))
                sampleWindow.refresh()

                curses.doupdate()
                curses.napms(viewingMilliSeconds)
                sampleWindow.clear()

    #-------------------------------------------------------------------

    def colorPairTestExtended(self):
        '''
        Conduct the tsWxGraphicalTextUserInterface tests of available
        color substituion mapping for cygwin, xterm, xterm-color,
        xterm-16color, xterm-88color and xterm-256color terminal
        emulators.
        #
        #    2014/01/25 rsg Re-designed test to identify:
        #                   Test Case: Number of Maximum
        #                   Color Names: Foreground and Background
        #                   Characer Cell Atributes:
        #                       Alternate, Blink, Bold, Dim,
        #                       Normal, Reverse, Standout, Underline
        #
        '''
        termName = self.ts_myGTUI.TermName.upper()
        template = '''
                     1         2         3         4         5
           0123456789012345678901234567890123456789012345678901234567
         0 +--------------------------------------------------------+
         1 | CASE nnnnn of MMMMM for TermName & Color Substitution: |
         2 |             COLOR NAME             ( ID) [ SAMPLE    ] |
         3 | FOREGROUND: light goldenrod yellow (255) [ MAPPED    ] |
         4 | BACKGROUND:                  black (  0) [ BUILT-IN  ] |
         5 |                           TEXT ATTRIBUTE [ SAMPLE    ] |
         5 | USE_256_COLOR_PAIR_LIMIT  TEXT ATTRIBUTE [ SAMPLE    ] |
         6 |                           ALTCHARSET     [ ALTCHARSET] |
         7 |                           Blink          [ Blink     ] |
         8 |                           Bold           [ Bold      ] |
         9 |                           Dim            [ Dim       ] |
        10 |                           Normal         [ Normal    ] |
        11 |                           Reverse        [ Reverse   ] |
        12 |                           Standout       [ Standout  ] |
        13 |                           Underline      [ Underline ] |
        14 +--------------------------------------------------------+
        '''
        theRect = self.testGetGeometry()
        self.myLogger.debug('colorPairTestExtended: theRect=%s' % str(theRect))

        theText = template.split('\n')

        textLines = len(theText) - 4
        textCols = 0
        for aLine in theText:
            textCols = max(textCols, len(aLine))
        nlines = textLines
        ncols = textCols - 8
        begin_y = 0
        begin_x = 0
        sampleWindow = {}

##        if (termName in WhiteOnBlackDefault):
##            # This configuration cannot display black
##            sampleWindowForeground = 'white'
##            sampleWindowBackground = 'black'
##        else:
##            sampleWindowForeground = 'black'
##            sampleWindowBackground = 'white'

        sampleWindowForeground = 'white'
        sampleWindowBackground = 'black'

        set_to_use = self.ts_myGTUI.tsGetSetToUseForColorCodeFromName()
        map_to_use = self.ts_myGTUI.ColorSubstitutionDataBase
        self.myLogger.debug(
            'colorPairTestExtended: map_to_use=%s' % str(map_to_use))

        if (map_to_use is None):

            if ((self.ts_myGTUI.TermName == 'cygwin') or \
                (self.ts_myGTUI.TermName == 'xterm') or \
                (self.ts_myGTUI.TermName == 'xterm-color')):

                map_to_use = Color8SubstitutionMap

            elif (self.ts_myGTUI.TermName == 'xterm-16color'):

                map_to_use = Color16SubstitutionMap

            elif ((self.ts_myGTUI.TermName == 'xterm-88color') and \
                  (USE_256_COLOR_PAIR_LIMIT)):

                map_to_use = Color16SubstitutionMap

            elif ((self.ts_myGTUI.TermName == 'xterm-256color') and \
                  (USE_256_COLOR_PAIR_LIMIT)):

                map_to_use = Color16SubstitutionMap

            elif ((self.ts_myGTUI.TermName == 'linux') and \
                  ((self.ts_Colors == 8) or \
                   (self.ts_Color_Pairs == 64))):

                map_to_use = Color8SubstitutionMap

            elif ((self.ts_myGTUI.TermName == 'linux') and \
                  ((self.ts_Colors == 16) or \
                   (self.ts_Color_Pairs == 256))):

                map_to_use = Color16SubstitutionMap

            else:

                map_to_use = None

            if (map_to_use is None):

                maxColors = min(1, len(sorted(list(set_to_use.keys()))))

            else:

                maxColors = len(map_to_use) - 1

        else:

            maxColors = len(map_to_use) - 1

        maxCases = maxColors**2
##        attribute = curses.A_STANDOUT | curses.A_BOLD
        attribute = curses.A_NORMAL

        sampleWindow = curses.newwin(nlines,
                                     ncols,
                                     begin_y,
                                     begin_x)

##        begin_y = -1
##        begin_x = 1
        
##        for aLine in theText:
##            begin_y +=1
##            sampleWindow.addstr(begin_y,
##                                begin_x,
##                                aLine)
##      sampleWindow.refresh()

##      curses.doupdate()
##      curses.napms(viewingMilliSeconds)
##      sampleWindow.clear()

        maxIdLength = len(' (%d)' % len(map_to_use))
        maxColorLength = 0
        for id in sorted(list(map_to_use.keys())):
            maxColorLength = max(maxColorLength, len(map_to_use[id]))

        color_pair_content = self.ts_myGTUI.tsGetCursesPairContent
        color_pair_number = self.ts_myGTUI.tsGetColorPairNumber
        color_attribute = self.ts_myGTUI.tsGetAttributeValueFromColorPair

        self.sample_max_colors = len(map_to_use) - 1
        self.sample_max_color_pairs = int(
            self.sample_max_colors**2)

        ID = 0
        for background in sorted(list(map_to_use.keys())):
            if background == 'name':
                continue
            # background = set_to_use[bg]
            backgroundMapColor = map_to_use[background]
            bg = set_to_use[backgroundMapColor]
            for foreground in sorted(list(map_to_use.keys())):
                if foreground == 'name':
                    continue
                # foreground = set_to_use[fg]
                foregroundMapColor = map_to_use[foreground]
                fg = set_to_use[foregroundMapColor]
                ID += 1
##                color_pair = color_pair_number(
##                    sampleWindowForeground,
##                    sampleWindowBackground)

                sampleWindow.border()
                sampleWindow.bkgd(
                    ' ',
                    color_attribute(sampleWindowForeground,
                                    sampleWindowBackground))

##                fmt01 = 'Case %d of %d for %s %s:' % (
##                    ID, maxCases, termName, '& Color Substitution' )
##                fmt02 = '            [ COLOR NAME             ( ID) ] '  \
##                       '[   Sample   ]'

                if gtui.CanChangeColor:
                    palette = 'tsWxGTUI'
                else:
                    palette = 'Built-In'

                fmt01 = 'Case %d of %d for %s %s:' % (
                    ID, maxCases, termName, '& Color Substitution' )
                fmt02 = '            [             COLOR NAME ( ID) ] '  \
                       '[ %-8s  ]' % palette

                fmt03 = 'Foreground: [ %23s (%2d) ] [   Sample  ]' % (
                    foreground + '->' + foregroundMapColor, fg)
                fmt04 = 'Background: [ %23s (%2d) ] [   Sample  ]' % (
                    background + '->' + backgroundMapColor, bg)

                if ((self.ts_myGTUI.TermName == 'cygwin') or \
                    (self.ts_myGTUI.TermName == 'xterm') or \
                    (self.ts_myGTUI.TermName == 'xterm-color')):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                elif (self.ts_myGTUI.TermName == 'xterm-16color'):

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                elif (self.ts_myGTUI.TermName == 'xterm-88color'):

                    # (self.ts_myGTUI.TermName == 'xterm-88color')
                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                else:

                    #  (self.ts_myGTUI.TermName == 'xterm-256color')

                    prefix = '%dx%d COLOR PAIRS    TEXT ATTRIBUTE' %(
                        self.sample_max_colors, self.sample_max_colors)
                    fmt05 = '%44s [   Sample  ]' % prefix

                fmt06 = '%44s [   Sample  ]' % 'Altcharset'
                fmt07 = '%44s [   Sample  ]' % 'Blink'
                fmt08 = '%44s [   Sample  ]' % 'Bold'
                fmt09 = '%44s [   Sample  ]' % 'Dim'
                fmt10 = '%44s [   Sample  ]' % 'Normal'
                fmt11 = '%44s [   Sample  ]' % 'Reverse'
                fmt12 = '%44s [   Sample  ]' % 'Standout'
                fmt13 = '%44s [   Sample  ]' % 'Underline'

##                fmt1 = 'Case %d; "%s" (%d) on "%s" (%d); ' % (
##                    ID, foreground, fg, background, bg)
##                fmt2 = 'Color Pair %d; Pair Content %s' % (
##                    color_pair, str(color_pair_content(color_pair)))
                msg = fmt01 + fmt02 + fmt03 # + fmt4
                sampleWindow.addstr(begin_y + 1,
                                    begin_x + 1,
                                    fmt01)

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(sampleWindowForeground,
                                                    sampleWindowBackground))
                sampleWindow.addstr(begin_y + 2,
                                    begin_x + 1,
                                    fmt02)
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(sampleWindowForeground,
                                                     sampleWindowBackground))

                sampleWindow.addstr(begin_y + 3,
                                    begin_x + 1,
                                    fmt03)
                sampleWindow.addstr(begin_y + 4,
                                    begin_x + 1,
                                    fmt04)

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(sampleWindowForeground,
                                                    sampleWindowBackground))
                sampleWindow.addstr(begin_y + 5,
                                    begin_x + 1,
                                    fmt05)
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(sampleWindowForeground,
                                                     sampleWindowBackground))

                sampleWindow.addstr(begin_y + 6,
                                    begin_x + 1,
                                    fmt06)
                sampleWindow.addstr(begin_y + 7,
                                    begin_x + 1,
                                    fmt07)
                sampleWindow.addstr(begin_y + 8,
                                    begin_x + 1,
                                    fmt08)
                sampleWindow.addstr(begin_y + 9,
                                    begin_x + 1,
                                    fmt09)
                sampleWindow.addstr(begin_y + 10,
                                    begin_x + 1,
                                    fmt10)
                sampleWindow.addstr(begin_y + 11,
                                    begin_x + 1,
                                    fmt11)
                sampleWindow.addstr(begin_y + 12,
                                    begin_x + 1,
                                    fmt12)
                sampleWindow.addstr(begin_y + 13,
                                    begin_x + 1,
                                    fmt13)

                sampleWindow.attron(attribute | \
                                    color_attribute(foreground,
                                                    foreground))
                sampleWindow.addstr(begin_y + 3,
                                    begin_x + 48,
                                    '          ')
                sampleWindow.attroff(attribute | \
                                     color_attribute(foreground,
                                                     foreground))

                sampleWindow.attron(attribute | \
                                    color_attribute(background,
                                                    background))
                sampleWindow.addstr(begin_y + 4,
                                    begin_x + 48,
                                    '          ')
                sampleWindow.attroff(attribute | \
                                     color_attribute(background,
                                                     background))

##                sampleWindow.attron(curses.A_NORMAL | \
##                                    color_attribute(foreground,
##                                                    background))
##                sampleWindow.addstr(begin_y + 5,
##                                    begin_x + 48,
##                                    ' Sample    ')
##                sampleWindow.attroff(curses.A_NORMAL | \
##                                   color_attribute(foreground,
##                                                   background))

                sampleWindow.attron(curses.A_NORMAL | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 6,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_ALTCHARSET | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_BLINK | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 7,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_BLINK | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_BOLD | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 8,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_BOLD | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_DIM | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 9,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_DIM | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_NORMAL | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 10,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_NORMAL | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_REVERSE | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 11,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_REVERSE | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_STANDOUT | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 12,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_STANDOUT | \
                                     color_attribute(foreground,
                                                     background))

                sampleWindow.attron(curses.A_UNDERLINE | \
                                    color_attribute(foreground,
                                                    background))
                sampleWindow.addstr(begin_y + 13,
                                    begin_x + 48,
                                    '  Sample  ')
                sampleWindow.attroff(curses.A_UNDERLINE | \
                                     color_attribute(foreground,
                                                     background))

                self.myLogger.debug('%s\n' % msg)
##                self.myLogger.write('%s\n' % msg)
##                self.myLogger.flush()
##                sampleWindow.attron(attribute | \
##                                    color_attribute(foreground,
##                                                    background))
##                sampleWindow.addstr(begin_y + 5,
##                                    begin_x + 1,
##                                    fmt1)
##                sampleWindow.addstr(begin_y + 6,
##                                    begin_x + 1,
##                                    fmt2)
##                sampleWindow.addstr(begin_y + 7,
##                                    begin_x + 1,
##                                    fmt3)
##                sampleWindow.addstr(begin_y + 8,
##                                    begin_x + 1,
##                                    fmt4)
##                sampleWindow.attroff(attribute | \
##                                     color_attribute(foreground,
##                                                     background))
                sampleWindow.refresh()

                curses.doupdate()
                curses.napms(viewingMilliSeconds)
                sampleWindow.clear()

    #-------------------------------------------------------------------

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def exitTest():
        exceptionName = tse.PROGRAM_EXCEPTION
        errorName = 'No Error'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.PROGRAM_EXCEPTION(errorName, message)

    #----------------------------------------------------------------------

    def getEntrySettings(*args, **kw):
        '''
        Return entry point command line keyword-value pair options
        and positional arguments.
        '''
        if False and DEBUG:

            print('\n%s\n' % myParser.getRunTimeTitleVersionDate())

        myParser =  tsOperatorSettingsParser.TsOperatorSettingsParser(
            *args, **kw)

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

##        myGTUI = gtui('cliAPP')
##        print dir(myGTUI)
##        myGTUI.stop()

        myGraphicalUserInterfaceTest = sample()
        myGraphicalUserInterfaceTest.testSupervisor()

    Instance =  tsCommandLineEnv.CommandLineEnv(

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
##        guiMessageFilename=None,
##        guiMessageRedirect=True,
##        guiRequired=True,
##        guiTopLevelObject=_Communicate,
##        guiTopLevelObjectId=wx.ID_ANY,
##        guiTopLevelObjectName=wx.FrameNameStr,
##        guiTopLevelObjectParent=None,
##        guiTopLevelObjectPosition=wx.DefaultPosition,
##        guiTopLevelObjectSize=wx.DefaultSize,
##        guiTopLevelObjectStatusBar=None,              # TBD - Implementation
##        guiTopLevelObjectStyle=wx.DEFAULT_FRAME_STYLE,
##        guiTopLevelObjectTitle='Gui_Test_Units', # __title__,
#
        runTimeEntryPoint=EntryPoint)

    Instance.Wrapper()

