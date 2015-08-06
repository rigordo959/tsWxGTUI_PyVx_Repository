#! /usr/bin/env python
#"Time-stamp: <12/23/2013  7:29:31 AM rsg>"
'''
test_tsWxCurses.py - Class to define and handle text-based user interfaces, TUIs.
'''
#################################################################
#
# File: test_tsWxCurses.py
#
# Purpose:
#
#    Class to define and handle text-based user interfaces, TUIs.
#
# Limitations:
#
#    1. Assumes that operator has logged into the computer from
#       a VT-100 or XTerm compatible console.
#
#    2. Assumes availability of Ncurses, a programming library
#       providing an API, allowing the programmer to write
#       text-based user interfaces, TUIs, in a terminal-
#       independent manner. It also optimizes screen changes,
#       in order to reduce the latency experienced when using
#       remote shells.
#
# Usage (example):
#
#     ## Import Module
#     import test_tsCurses as tsui
#
#     ## Instantiate Module
#     myUserInterface = tsui.TsCurses(threshold=Logger.ERROR,
#                                     start=time.time(),
#                                     logger='./myError.log')
#
#     ## Reference Module Methods
#     myLogger.log(Logger.ERROR, 'Timeout. Remote Host not available.')
#     myLogger.error('Timeout. Remote Host not available.')
#
# Methods:
#
#    None
#
# Modifications:
#
#    2013/02/28 rsg Added import tsCommandLineInterfaceLibrary.
#
#    2013/02/28 rsg Added import tsGraphicalUserInterfaceLibrary.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'test_tsWxCurses'
__version__   = '1.0.0'
__date__      = '02/28/2013'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2013 TeamSTARS. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

import curses
import curses.ascii
import curses.panel
import curses.textpad
import curses.wrapper
import os
import os.path
import sys
import time

try:

    import tsLibCLI

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

try:

    import tsExceptions as tse
    import tsLogger as Logger
    import tsOperatorSettingsParser
    # import tsCommandLineInterfaceLibrary
    from tsReportUtilities import TsReportUtilities as tsrpu

except ImportError, importCode:

    print('%s: ImportError (tsLibGUI); ' % __title__ + \
          'importCode=%s' % str(importCode))

class TsCurses(object):
    '''
    Define features of non-graphical, text mode console user interface.
    '''
    expectedSize = {'rows': 63, 'cols': 82}
 
    COLOR_BLACK = curses.COLOR_BLACK
    COLOR_RED = curses.COLOR_RED
    COLOR_GREEN = curses.COLOR_GREEN
    COLOR_YELLOW = curses.COLOR_YELLOW
    COLOR_BLUE = curses.COLOR_BLUE
    COLOR_MAGENTA = curses.COLOR_MAGENTA
    COLOR_CYAN = curses.COLOR_CYAN
    COLOR_WHITE = curses.COLOR_WHITE

    # Dictionary of available colors in numeric order.
    colors = {COLOR_BLACK: 0,
              COLOR_RED: 1,
              COLOR_GREEN: 2,
              COLOR_YELLOW: 3,
              COLOR_BLUE: 4,
              COLOR_MAGENTA: 5,
              COLOR_CYAN: 6,
              COLOR_WHITE: 7}

    ALIGN_TO_TOP = 'top'
    ALIGN_TO_MIDDLE = 'middle'
    ALIGN_TO_BOTTOM = 'botttom'

    ALIGN_TO_LEFT = 'left'
    ALIGN_TO_CENTER = 'center'
    ALIGN_TO_RIGHT = 'right'
    ALIGN_TO_JUSTIFIED = 'justified'

    verticalAlignment = [ALIGN_TO_TOP,
                         ALIGN_TO_MIDDLE,
                         ALIGN_TO_BOTTOM]

    horizontalAlignment = [ALIGN_TO_LEFT,
                           ALIGN_TO_CENTER,
                           ALIGN_TO_RIGHT,
                           ALIGN_TO_JUSTIFIED]

    def __init__(self, **kw):
        '''
        Initialze the class.
        '''
        self.theStartTime = time.time()
        try:
            self.console = Logger.TsLogger(threshold=Logger.DEBUG,
                                           start=self.theStartTime,
                                           name=Logger.StandardErrorDevice)
        except:
            self.console = None

        for arg in sys.argv:
            self.ourName, self.ourExt = arg.split('.')
            if self.ourExt == 'py':
                break

        for key in list(kw.keys()):

            if key == 'name':
                self.name = kw[key]
                self.ts_open(kw[key], TRUNCATE)

            elif key == 'length':
                self.length = kw[key]

            elif key == 'width':
                self.width = kw[key]

            elif key == 'start':
                self.theStartTime = float(kw[key])

            elif key == 'logger':
                self.logger = kw[key]

        if 'logger' not in list(kw.keys()):
            try:
                self.logger = Logger.TsLogger(
                    threshold=Logger.DEBUG,
                    start=self.theStartTime,
                    name=os.path.join(os.getcwd(),
                                      '%s.log' % __title__))
            except:
                self.bomb('Unable to establish working logger.')

        self.windows = {}

    def tsBomb(self, msg):
        '''
        Output messagte to command line interface when non-graphical,
        text mode console user interface is unavailable.
        '''
        try:
            self.console.error(msg)
        except:
            print('No console available. ERROR: %s' % msg)

        sys.exit(1)

    def tsCreateColorPairs(self):
        '''
        Activate available foreground and background color combinations.
        Identifier (0-63) = <forground id (0-7)><background id (0-7)>
        '''
        for foreground in range(len(self.colors)):
            for background in range(len(self.colors)):
                if foreground != background:
                    # Skip unusable combinations.
                    curses.init_pair(
                        self.tsWhichColorPair(self.colors[foreground],
                                              self.colors[background]),
                        self.colors[foreground],
                        self.colors[background])

    def tsWhichColorPair(self, foreground, background):
        return (self.colors[foreground] << 3) + self.colors[background]

    def tsActivatedColorPair(self, foreground, background):
        return curses.color_pair(
            self.tsWhichColorPair(self.colors[foreground],
                                  self.colors[background]))

    def tsCreateWindow(self,
                       parentName,
                       childName,
                       nrows,
                       ncols,
                       begin_y,
                       begin_x,
                       parentVerticalAlignment=ALIGN_TO_TOP,
                       parentHorizontalAlignment=ALIGN_TO_LEFT,
                       background=None,
                       border=None,
                       title=None,
                       titleColorPair=None,
                       titleVerticalAlignment=ALIGN_TO_TOP,
                       titleHorizontalAlignment=ALIGN_TO_LEFT,
                       contents=None,
                       contentsColorPair=None,
                       contentsVerticalAlignment=ALIGN_TO_TOP,
                       contentsHorizontalAlignment=ALIGN_TO_LEFT):
        '''
        '''
##        self.parentName = parentName
##        self.childName = childName
##        self.nrows = nrows
##        self.ncols = ncols
##        self.begin_y = begin_y
##        self.begin_x = begin_x
##        self.parentVerticalAlignment = parentVerticalAlignment
##        self.parentHorizontalAlignment = parentHorizontalAlignment
##        self.background = background
##        self.border = border
##        self.title = title
##        self.titleColorPair = titleColorPair
##        self.titleVerticalAlignment = titleVerticalAlignment
##        self.titleHorizontalAlignment = titleHorizontalAlignment
##        self.contents = contents
##        self.contentsColorPair = contentsColorPair
##        self.contentsVerticalAlignment = contentsVerticalAlignment
##        self.contentsHorizontalAlignment = contentsHorizontalAlignment
 
##        maxRows, maxCols = self.windows[parentName].getmaxyx()
##        if parentName == 'stdscr':
##            if maxRows < self.expectedSize['rows']:
##                self.tsBomb('Screen needs %d lines; Only have %d.' %
##                          (self.expectedSize['rows'], maxRows))
##            if maxCols < self.expectedSize['cols']:
##                self.tsBomb('Screen needs %d columns.; Only have %d.' %
##                          (self.expectedSize['cols'], maxCols))

        names = list(self.windows.keys())
        if childName not in names:
            if border is True:
                offset = 1
            else:
                offset = 0

            if parentVerticalAlignment == self.ALIGN_TO_TOP:
                row = begin_y
            elif parentVerticalAlignment == self.ALIGN_TO_MIDDLE:
                row = (maxRows - nrows) / 2
            elif parentVerticalAlignment == self.ALIGN_TO_BOTTOM:
                row = maxRows - nrows - offset
            else:
                row = begin_y

            if parentHorizontalAlignment == self.ALIGN_TO_LEFT:
                col = begin_x
            elif parentHorizontalAlignment == self.ALIGN_TO_CENTER:
                col = ((maxCols - ncols - offset) / 2)
            elif parentHorizontalAlignment == self.ALIGN_TO_RIGHT:
                col = maxCols - ncols - offset
            else:
                col = begin_x

            childWindow = curses.newwin(nrows, ncols, row, col)
            self.logger.debug('Window Size (%d/%d) at (%d/%d)' %(nrows,
                                                                 ncols,
                                                                 row,
                                                                 col))
            self.windows[childName] = childWindow
            if background is not None:
                childWindow.bkgd(background)
            if border is True:
                childWindow.border()
                self.logger.debug('Window Border')

            if title is not None:
                if titleColorPair is not None:
                    childWindow.attron(titleColorPair)
                childWindow.attron(curses.A_STANDOUT)

                if titleVerticalAlignment == self.ALIGN_TO_TOP:
                    row = 0
                elif titleVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - 0) / 2
                elif titleVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - 1
                else:
                    row = 0

                if titleHorizontalAlignment == self.ALIGN_TO_LEFT:
                    col = offset
                elif titleHorizontalAlignment == self.ALIGN_TO_CENTER:
                    col = ((ncols - (len(title) + 2)) / 2)
                elif titleHorizontalAlignment == self.ALIGN_TO_RIGHT:
                    col = ncols - (len(title) + 2) - offset
                else:
                    col = offset
 
                childWindow.addstr(int(row), int(col), ' %s ' % title)
                self.logger.debug('Title: (%d/%d) "%s"' %(row, col, title))
                childWindow.attroff(curses.A_STANDOUT)
                if titleColorPair is not None:
                    childWindow.attroff(titleColorPair)

            if contents is not None:
                if contentsColorPair is not None:
                    childWindow.attron(contentsColorPair)
                childWindow.attron(curses.A_NORMAL)

                if contentsVerticalAlignment == self.ALIGN_TO_TOP:
                    row = offset
                elif contentsVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - len(contents)) / 2
                elif contentsVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - len(contents) - offset + 1
                else:
                    row = offset

##                localContents = \
##                              [tsrpu.getDateAndTimeString(time.time())] + contents
                localContents = contents
                for theText in localContents:

                    if contentsHorizontalAlignment == self.ALIGN_TO_LEFT:
                        col = offset
                    elif contentsHorizontalAlignment == self.ALIGN_TO_CENTER:
                        col = (ncols - len(theText) - offset) / 2
                    elif contentsHorizontalAlignment == self.ALIGN_TO_RIGHT:
                        col = (ncols - len(theText)) - offset
                    else:
                        col = offset

                    childWindow.addstr(int(row), int(col), '%s' % theText)
                    self.logger.debug('Text: (%d/%d) "%s"' %(row, col, theText))
                    row += 1
 
                childWindow.attroff(curses.A_NORMAL)
                if contentsColorPair is not None:
                    childWindow.attroff(contentsColorPair)

                if background is not None:
                    childWindow.bkgd(curses.A_NORMAL)

            childWindow.refresh()
            self.logger.debug('Window Refresh')
            if 0:
                childWindow.getch()
            else:
                curses.napms(5000)

        else:

            childWindow = self.windows[childName]
            offset = 2
            if contents is not None:
                childWindow.attron(curses.A_NORMAL)

                if contentsVerticalAlignment == self.ALIGN_TO_TOP:
                    row = offset
                elif contentsVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - len(contents)) / 2
                elif contentsVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - len(contents) - offset + 1
                else:
                    row = offset

                localContents = \
                              [tsrpu.getDateAndTimeString(time.time())] + contents
                for theText in localContents:

                    if contentsHorizontalAlignment == self.ALIGN_TO_LEFT:
                        col = offset
                    elif contentsHorizontalAlignment == self.ALIGN_TO_CENTER:
                        col = (ncols - len(theText) - offset) / 2
                    elif contentsHorizontalAlignment == self.ALIGN_TO_RIGHT:
                        col = (ncols - len(theText)) - offset
                    else:
                        col = offset

                    childWindow.addstr(int(row), int(col), '%s' % theText)
                    self.logger.debug('Text: (%d/%d) "%s"' %(row, col, theText))
                    row += 1
 
                childWindow.attroff(curses.A_NORMAL)

##            childWindow.touchwin()
            childWindow.refresh()
            self.logger.debug('Window Refresh')
            curses.napms(5000)

        return childWindow

    def tsCreateScrollableWindow(self,
                                 parentName,
                                 childName,
                                 nrows,
                                 ncols,
                                 begin_y,
                                 begin_x,
                                 parentVerticalAlignment=ALIGN_TO_TOP,
                                 parentHorizontalAlignment=ALIGN_TO_LEFT,
                                 background=None,
                                 border=None,
                                 title=None,
                                 titleColorPair=None,
                                 titleVerticalAlignment=ALIGN_TO_TOP,
                                 titleHorizontalAlignment=ALIGN_TO_LEFT,
                                 contents=None,
                                 contentsColorPair=None,
                                 contentsVerticalAlignment=ALIGN_TO_TOP,
                                 contentsHorizontalAlignment=ALIGN_TO_LEFT):
        '''
        '''
##        self.parentName = parentName
##        self.childName = childName
##        self.nrows = nrows
##        self.ncols = ncols
##        self.begin_y = begin_y
##        self.begin_x = begin_x
##        self.parentVerticalAlignment = parentVerticalAlignment
##        self.parentHorizontalAlignment = parentHorizontalAlignment
##        self.background = background
##        self.border = border
##        self.title = title
##        self.titleColorPair = titleColorPair
##        self.titleVerticalAlignment = titleVerticalAlignment
##        self.titleHorizontalAlignment = titleHorizontalAlignment
##        self.contents = contents
##        self.contentsColorPair = contentsColorPair
##        self.contentsVerticalAlignment = contentsVerticalAlignment
##        self.contentsHorizontalAlignment = contentsHorizontalAlignment
 
##        maxRows, maxCols = self.windows[parentName].getmaxyx()
##        if parentName == 'stdscr':
##            if maxRows < self.expectedSize['rows']:
##                self.tsBomb('Screen needs %d lines; Only have %d.' %
##                          (self.expectedSize['rows'], maxRows))
##            if maxCols < self.expectedSize['cols']:
##                self.tsBomb('Screen needs %d columns.; Only have %d.' %
##                          (self.expectedSize['cols'], maxCols))

        names = list(self.windows.keys())
        if childName not in names:
            if border is True:
                offset = 1
            else:
                offset = 0

            if parentVerticalAlignment == self.ALIGN_TO_TOP:
                row = begin_y
            elif parentVerticalAlignment == self.ALIGN_TO_MIDDLE:
                row = (maxRows - nrows) / 2
            elif parentVerticalAlignment == self.ALIGN_TO_BOTTOM:
                row = maxRows - nrows - offset
            else:
                row = begin_y

            if parentHorizontalAlignment == self.ALIGN_TO_LEFT:
                col = begin_x
            elif parentHorizontalAlignment == self.ALIGN_TO_CENTER:
                col = ((maxCols - ncols - offset) / 2)
            elif parentHorizontalAlignment == self.ALIGN_TO_RIGHT:
                col = maxCols - ncols - offset
            else:
                col = begin_x

##            childWindow = curses.newwin(nrows, ncols, row, col)
            containerName = childName + '-container'
            containerWindow = \
                            self.tsCreateWindow(parentName=childName,
                                                childName=containerName,
                                                nrows=nrows,
                                                ncols=ncols,
                                                begin_y=begin_y,
                                                begin_x=begin_x,
                                                parentVerticalAlignment=ALIGN_TO_TOP,
                                                parentHorizontalAlignment=ALIGN_TO_LEFT,
                                                background=background,
                                                border=border,
                                                title=title,
                                                titleColorPair=titleColorPair,
                                                titleVerticalAlignment=ALIGN_TO_TOP,
                                                titleHorizontalAlignment=ALIGN_TO_LEFT,
                                                contents=None,
                                                contentsColorPair=None,
                                                contentsVerticalAlignment=ALIGN_TO_TOP,
                                                contentsHorizontalAlignment=ALIGN_TO_LEFT)
            self.logger.debug('Scrollable Window Size (%d/%d) at (%d/%d)' %(nrows,
                                                                            ncols,
                                                                            row,
                                                                            col))
            self.windows[containerName] = containerWindow

            horizontalScrollBarName = childName + '-hscrollbar'
            horizontalScrollBarWindow = \
                            self.tsCreateWindow(parentName=containerName,
                                                childName=horizontalScrollBarName,
                                                nrows=1,
                                                ncols=ncols - (offset * 2) - 1,
                                                begin_y=0 + nrows - offset,
                                                begin_x=0 + offset,
                                                parentVerticalAlignment=ALIGN_TO_TOP,
                                                parentHorizontalAlignment=ALIGN_TO_LEFT,
                                                background=background,
                                                border=None,
                                                title=None,
                                                titleColorPair=None,
                                                titleVerticalAlignment=ALIGN_TO_TOP,
                                                titleHorizontalAlignment=ALIGN_TO_LEFT,
                                                contents=None,
                                                contentsColorPair=None,
                                                contentsVerticalAlignment=ALIGN_TO_TOP,
                                                contentsHorizontalAlignment=ALIGN_TO_LEFT)
            self.logger.debug('Horizontal Scroll Bar Size (%d/%d) at (%d/%d)' %(nrows,
                                                                            ncols,
                                                                            row,
                                                                            col))
            self.windows[containerName] = containerWindow

            if background is not None:
                childWindow.bkgd(background)
            if border is True:
                childWindow.border()
                self.logger.debug('Window Border')

            if title is not None:
                if titleColorPair is not None:
                    childWindow.attron(titleColorPair)
                childWindow.attron(curses.A_STANDOUT)

                if titleVerticalAlignment == self.ALIGN_TO_TOP:
                    row = 0
                elif titleVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - 0) / 2
                elif titleVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - 1
                else:
                    row = 0

                if titleHorizontalAlignment == self.ALIGN_TO_LEFT:
                    col = offset
                elif titleHorizontalAlignment == self.ALIGN_TO_CENTER:
                    col = ((ncols - (len(title) + 2)) / 2)
                elif titleHorizontalAlignment == self.ALIGN_TO_RIGHT:
                    col = ncols - (len(title) + 2) - offset
                else:
                    col = offset
 
                childWindow.addstr(row, col, ' %s ' % title)
                self.logger.debug('Title: (%d/%d) "%s"' %(row, col, title))
                childWindow.attroff(curses.A_STANDOUT)
                if titleColorPair is not None:
                    childWindow.attroff(titleColorPair)

            if contents is not None:
                if contentsColorPair is not None:
                    childWindow.attron(contentsColorPair)
                childWindow.attron(curses.A_NORMAL)

                if contentsVerticalAlignment == self.ALIGN_TO_TOP:
                    row = offset
                elif contentsVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - len(contents)) / 2
                elif contentsVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - len(contents) - offset + 1
                else:
                    row = offset

##                localContents = \
##                              [tsrpu.getDateAndTimeString(time.time())] + contents
                localContents = contents
                for theText in localContents:

                    if contentsHorizontalAlignment == self.ALIGN_TO_LEFT:
                        col = offset
                    elif contentsHorizontalAlignment == self.ALIGN_TO_CENTER:
                        col = (ncols - len(theText) - offset) / 2
                    elif contentsHorizontalAlignment == self.ALIGN_TO_RIGHT:
                        col = (ncols - len(theText)) - offset
                    else:
                        col = offset

                    childWindow.addstr(row, col, '%s' % theText)
                    self.logger.debug('Text: (%d/%d) "%s"' %(row, col, theText))
                    row += 1
 
                childWindow.attroff(curses.A_NORMAL)
                if contentsColorPair is not None:
                    childWindow.attroff(contentsColorPair)

                if background is not None:
                    childWindow.bkgd(curses.A_NORMAL)

            childWindow.refresh()
            self.logger.debug('Window Refresh')
            if 0:
                childWindow.getch()
            else:
                curses.napms(5000)

        else:

            childWindow = self.windows[childName]
            offset = 2
            if contents is not None:
                childWindow.attron(curses.A_NORMAL)

                if contentsVerticalAlignment == self.ALIGN_TO_TOP:
                    row = offset
                elif contentsVerticalAlignment == self.ALIGN_TO_MIDDLE:
                    row = (nrows - len(contents)) / 2
                elif contentsVerticalAlignment == self.ALIGN_TO_BOTTOM:
                    row = nrows - len(contents) - offset + 1
                else:
                    row = offset

                localContents = \
                              [tsrpu.getDateAndTimeString(time.time())] + contents
                for theText in localContents:

                    if contentsHorizontalAlignment == self.ALIGN_TO_LEFT:
                        col = offset
                    elif contentsHorizontalAlignment == self.ALIGN_TO_CENTER:
                        col = (ncols - len(theText) - offset) / 2
                    elif contentsHorizontalAlignment == self.ALIGN_TO_RIGHT:
                        col = (ncols - len(theText)) - offset
                    else:
                        col = offset

                    childWindow.addstr(row, col, '%s' % theText)
                    self.logger.debug('Text: (%d/%d) "%s"' %(row, col, theText))
                    row += 1
 
                childWindow.attroff(curses.A_NORMAL)

##            childWindow.touchwin()
            childWindow.refresh()
            self.logger.debug('Window Refresh')
            curses.napms(5000)

        return ChildWindow
 
    def windowTest(self, stdscr):

        offset = 2

        content = __header__.split('\n')
        nrows = len(content) + (offset * 2)
        ncols = 0
        for theText in content:
            if ncols < len(theText):
                ncols = len(theText)
        ncols += (offset * 2)

        contentsTitles = ['Align window to Top Left',
                          'Align window to Middle Center',
                          'Align window to Bottom Right',]

        verticalAlignments = [self.ALIGN_TO_TOP,
                              self.ALIGN_TO_MIDDLE,
                              self.ALIGN_TO_BOTTOM]

        horizontalAlignments = [self.ALIGN_TO_LEFT,
                                self.ALIGN_TO_CENTER,
                                self.ALIGN_TO_RIGHT]
        for i in range(3):
            self.tsCreateWindow('stdscr',
                              'Child %d' % i,
                              nrows,
                              ncols,
                              0 + (i * (nrows + 3)),
                              0 + (i * 4),
                              parentVerticalAlignment=verticalAlignments[i],
                              parentHorizontalAlignment=horizontalAlignments[i],
    ##                          background=None,
                              border=True,
                              title='%s' % contentsTitles[i],
    ##                          titleColorPair=None,
                              titleVerticalAlignment=self.ALIGN_TO_TOP,
                              titleHorizontalAlignment=self.ALIGN_TO_LEFT,
                              contents=content,
    ##                          contentsColorPair=None,
                              contentsVerticalAlignment=self.ALIGN_TO_TOP,
                              contentsHorizontalAlignment=self.ALIGN_TO_LEFT
                              )

        stdscr.getch()

    def borderlessTitleTest(self, stdscr):

        offset = 2

        content = __header__.split('\n')
        nrows = len(content) + (offset * 4)
        ncols = 0
        for theText in content:
            if ncols < len(theText):
                ncols = len(theText)
        ncols += (offset * 2)

        contentsTitles = ['Align title to Top Left',
                          'Align title to Middle Center',
                          'Align title to Bottom Right',]

        verticalAlignments = [self.ALIGN_TO_TOP,
                              self.ALIGN_TO_MIDDLE,
                              self.ALIGN_TO_BOTTOM]

        horizontalAlignments = [self.ALIGN_TO_LEFT,
                                self.ALIGN_TO_CENTER,
                                self.ALIGN_TO_RIGHT]
        for i in range(3):
            self.tsCreateWindow('stdscr',
                              'Child %d' % i,
                              nrows,
                              ncols,
                              0 + (i * (nrows + 3)),
                              0 + (i * 4),
                              parentVerticalAlignment=self.ALIGN_TO_TOP,
                              parentHorizontalAlignment=self.ALIGN_TO_LEFT,
    ##                          background=None,
    ##                          border=False,
                              title='%s' % contentsTitles[i],
    ##                          titleColorPair=None,
                              titleVerticalAlignment=verticalAlignments[i],
                              titleHorizontalAlignment=horizontalAlignments[i],
                              contents=content,
    ##                          contentsColorPair=None,
                              contentsVerticalAlignment=self.ALIGN_TO_TOP,
                              contentsHorizontalAlignment=self.ALIGN_TO_LEFT
                              )

        stdscr.getch()

    def titleTest(self, stdscr):

        offset = 2

        content = __header__.split('\n')
        nrows = len(content) + (offset * 4)
        ncols = 0
        for theText in content:
            if ncols < len(theText):
                ncols = len(theText)
        ncols += (offset * 2)

        contentsTitles = ['Align title to Top Left',
                          'Align title to Middle Center',
                          'Align title to Bottom Right',]

        verticalAlignments = [self.ALIGN_TO_TOP,
                              self.ALIGN_TO_MIDDLE,
                              self.ALIGN_TO_BOTTOM]

        horizontalAlignments = [self.ALIGN_TO_LEFT,
                                self.ALIGN_TO_CENTER,
                                self.ALIGN_TO_RIGHT]
        for i in range(3):
            self.tsCreateWindow('stdscr',
                              'Child %d' % i,
                              nrows,
                              ncols,
                              0 + (i * (nrows + 3)),
                              0 + (i * 4),
                              parentVerticalAlignment=self.ALIGN_TO_TOP,
                              parentHorizontalAlignment=self.ALIGN_TO_LEFT,
    ##                          background=None,
                              border=True,
                              title='%s' % contentsTitles[i],
    ##                          titleColorPair=None,
                              titleVerticalAlignment=verticalAlignments[i],
                              titleHorizontalAlignment=horizontalAlignments[i],
                              contents=content,
    ##                          contentsColorPair=None,
                              contentsVerticalAlignment=self.ALIGN_TO_TOP,
                              contentsHorizontalAlignment=self.ALIGN_TO_LEFT
                              )

        stdscr.getch()

    def contentTest(self, stdscr):

        offset = 2

        content = __header__.split('\n')
        nrows = len(content) + (offset * 6)
        ncols = 0
        for theText in content:
            if ncols < len(theText):
                ncols = len(theText)
        ncols += (offset * 2)

        contentsTitles = ['Align contents to Top Left',
                          'Align contents to Middle Center',
                          'Align contents to Bottom Right',]

        verticalAlignments = [self.ALIGN_TO_TOP,
 
                              self.ALIGN_TO_MIDDLE,
                              self.ALIGN_TO_BOTTOM]

        horizontalAlignments = [self.ALIGN_TO_LEFT,
                                self.ALIGN_TO_CENTER,
                                self.ALIGN_TO_RIGHT]
        for i in range(3):
            self.tsCreateWindow('stdscr',
                              'Child %d' % i,
                              nrows,
                              ncols,
                              0 + (i * (nrows + 3)),
                              0 + (i * 4),
                              parentVerticalAlignment=self.ALIGN_TO_TOP,
                              parentHorizontalAlignment=self.ALIGN_TO_LEFT,
    ##                          background=None,
                              border=True,
                              title='%s' % contentsTitles[i],
    ##                          titleColorPair=None,
                              titleVerticalAlignment=self.ALIGN_TO_TOP,
                              titleHorizontalAlignment=self.ALIGN_TO_CENTER,
                              contents=content,
    ##                          contentsColorPair=None,
                              contentsVerticalAlignment=verticalAlignments[i],
                              contentsHorizontalAlignment=horizontalAlignments[i]
                              )
        for i in range(3):
            self.tsCreateWindow('stdscr',
                              'Child %d' % i,
                              nrows,
                              ncols,
                              0 + (i * (nrows + 3)),
                              0 + (i * 4),
                              parentVerticalAlignment=self.ALIGN_TO_TOP,
                              parentHorizontalAlignment=self.ALIGN_TO_LEFT,
    ##                          background=None,
                              border=True,
                              title='%s' % contentsTitles[i],
    ##                          titleColorPair=None,
                              titleVerticalAlignment=self.ALIGN_TO_TOP,
                              titleHorizontalAlignment=self.ALIGN_TO_CENTER,
                              contents=content,
    ##                          contentsColorPair=None,
                              contentsVerticalAlignment=verticalAlignments[i],
                              contentsHorizontalAlignment=horizontalAlignments[i]
                              )

        stdscr.getch()

class titleWidget(TsCurses):
    def __init__(self,
                 container,
                 title=None,
                 style=curses.A_STANDOUT,
                 foregroundColor=TsCurses.COLOR_WHITE,
                 backgroundColor=TsCurses.COLOR_BLACK,
                 verticalPlacement=TsCurses.ALIGN_TO_TOP,
                 horizontalPlacement=TsCurses.ALIGN_TO_LEFT):
        self.container = container
        self.title = title
        self.style = style
        self.verticalPlacement = verticalPlacement
        self.horizontalPlacement = horizontalPlacement
        self.offset = 2

    def setup(self):
        if self.title is not None:
            nrows, ncols = container.getmaxyx()
            container.attron(self.style)

            if self.verticalPlacement == self.ALIGN_TO_TOP:
                row = 0
            elif self.verticalPlacement == self.ALIGN_TO_MIDDLE:
                row = (nrows - 0) / 2
            elif self.verticalPlacement == self.ALIGN_TO_BOTTOM:
                row = nrows - 1
            else:
                row = 0

            if self.horizontalPlacement == self.ALIGN_TO_LEFT:
                col = self.offset
            elif self.horizontalPlacement == self.ALIGN_TO_CENTER:
                col = ((ncols - (len(title) + 2)) / 2)
            elif self.horizontalPlacement == self.ALIGN_TO_RIGHT:
                col = ncols - (len(title) + 2) - self.offset
            else:
                col = self.offset

            container.addstr(row, col, ' %s ' % self.title)
            container.attroff(self.style)

class textWidget(TsCurses):
    def __init__(self,
                 container,
                 text=None,
                 style=curses.A_NORMAL,
                 foregroundColor=TsCurses.COLOR_WHITE,
                 backgroundColor=TsCurses.COLOR_BLACK,
                 verticalPlacement=TsCurses.ALIGN_TO_TOP,
                 horizontalPlacement=TsCurses.ALIGN_TO_LEFT):
        self.container = container
        self.text = text
        self.style = style
        self.verticalPlacement = verticalPlacement
        self.horizontalPlacement = horizontalPlacement
        self.offset = 2

    def setup(self):
        if self.text is not None:
            nrows, ncols = container.getmaxyx()
            container.attron(self.style)

            if verticalPlacement == self.ALIGN_TO_TOP:
                row = self.offset
            elif verticalPlacement == self.ALIGN_TO_MIDDLE:
                row = (nrows - len(contents)) / 2
            elif verticalPlacement == self.ALIGN_TO_BOTTOM:
                row = nrows - len(contents) - self.offset + 1
            else:
                row = self.offset

            for theText in contents:

                if self.horizontalPlacement == self.ALIGN_TO_LEFT:
                    col = self.offset
                elif self.horizontalPlacement == self.ALIGN_TO_CENTER:
                    col = (ncols - len(theText) - self.offset) / 2
                elif self.horizontalPlacement == self.ALIGN_TO_RIGHT:
                    col = (ncols - len(theText)) - self.offset
                else:
                    col = self.offset

                container.addstr(row, col, '%s' % theText)
                row += 1

            container.attroff(self.style)

        container.refresh()
        if 0:
            container.getch()
        else:
            curses.napms(5000)

##class windowWidget(TsCurses):

##    def __init__(self,
##                 parentName,
##                 childName,
##                 nrows,
##                 ncols,
##                 begin_y,
##                 begin_x,
##                 parentVerticalAlignment=ALIGN_TO_TOP,
##                 parentHorizontalAlignment=ALIGN_TO_LEFT,
##                 background=None,
##                 border=None,
##                 title=None,
##                 titleColorPair=None,
##                 titleVerticalAlignment=ALIGN_TO_TOP,
##                 titleHorizontalAlignment=ALIGN_TO_LEFT,
##                 contents=None,
##                 contentsColorPair=None,
##                 contentsVerticalAlignment=ALIGN_TO_TOP,
##                 contentsHorizontalAlignment=ALIGN_TO_LEFT):
##        '''
##        '''
##        maxRows, maxCols = self.windows[parentName].getmaxyx()
##        if parentName == 'stdscr':
##            if maxRows < self.expectedSize['rows']:
##                self.tsBomb('Screen needs %d lines; Only have %d.' %
##                          (self.expectedSize['rows'], maxRows))
##            if maxCols < self.expectedSize['cols']:
##                self.tsBomb('Screen needs %d columns.; Only have %d.' %
##                          (self.expectedSize['cols'], maxCols))
##        names = self.windows.keys()
##        if childName not in names:
##            if border is True:
##                offset = 2
##            else:
##                offset = 2

##            if parentVerticalAlignment == self.ALIGN_TO_TOP:
##                row = begin_y
##            elif parentVerticalAlignment == self.ALIGN_TO_MIDDLE:
##                row = (maxRows - nrows) / 2
##            elif parentVerticalAlignment == self.ALIGN_TO_BOTTOM:
##                row = maxRows - nrows - offset
##            else:
##                row = begin_y

##            if parentHorizontalAlignment == self.ALIGN_TO_LEFT:
##                col = begin_x
##            elif parentHorizontalAlignment == self.ALIGN_TO_CENTER:
##                col = ((maxCols - ncols - offset) / 2)
##            elif parentHorizontalAlignment == self.ALIGN_TO_RIGHT:
##                col = maxCols - ncols - offset
##            else:
##                col = begin_x

##            childWindow = curses.newwin(nrows, ncols, row, col)
##            self.windows[childName] = childWindow
##            if border is True:
##                childWindow.border()

##            if title is not None:
##                childWindow.attron(curses.A_STANDOUT)

##                if titleVerticalAlignment == self.ALIGN_TO_TOP:
##                    row = 0
##                elif titleVerticalAlignment == self.ALIGN_TO_MIDDLE:
##                    row = (nrows - 0) / 2
##                elif titleVerticalAlignment == self.ALIGN_TO_BOTTOM:
##                    row = nrows - 1
##                else:
##                    row = 0

##                if titleHorizontalAlignment == self.ALIGN_TO_LEFT:
##                    col = offset
##                elif titleHorizontalAlignment == self.ALIGN_TO_CENTER:
##                    col = ((ncols - (len(title) + 2)) / 2)
##                elif titleHorizontalAlignment == self.ALIGN_TO_RIGHT:
##                    col = ncols - (len(title) + 2) - offset
##                else:
##                    col = offset
 
##                childWindow.addstr(row, col, ' %s ' % title)
##                childWindow.attroff(curses.A_STANDOUT)

##            if contents is not None:
##                childWindow.attron(curses.A_NORMAL)

##                if contentsVerticalAlignment == self.ALIGN_TO_TOP:
##                    row = offset
##                elif contentsVerticalAlignment == self.ALIGN_TO_MIDDLE:
##                    row = (nrows - len(contents)) / 2
##                elif contentsVerticalAlignment == self.ALIGN_TO_BOTTOM:
##                    row = nrows - len(contents) - offset
##                else:
##                    row = offset

##                for theText in contents:

##                    if contentsHorizontalAlignment == self.ALIGN_TO_LEFT:
##                        col = offset
##                    elif contentsHorizontalAlignment == self.ALIGN_TO_CENTER:
##                        col = (ncols - len(theText) - offset) / 2
##                    elif contentsHorizontalAlignment == self.ALIGN_TO_RIGHT:
##                        col = (ncols - len(theText)) - offset
##                    else:
##                        col = offset

##                    childWindow.addstr(row, col, '%s' % theText)
##                    row += 1
 
##                childWindow.attroff(curses.A_NORMAL)

##            childWindow.refresh()
##            if 0:
##                childWindow.getch()
##            else:
##                curses.napms(5000)
##        pass


 
##    def __init__(self,
##                 container,
##                 text=None,
##                 style=curses.A_NORMAL,
##                 foregroundColor=TsCurses.COLOR_WHITE,
##                 backgroundColor=TsCurses.COLOR_BLACK,
##                 verticalPlacement=TsCurses.ALIGN_TO_TOP,
##                 horizontalPlacement=TsCurses.ALIGN_TO_LEFT):
##        self.container = container
##        self.text = text
##        self.style = style
##        self.verticalPlacement = verticalPlacement
##        self.horizontalPlacement = horizontalPlacement
##        self.offset = 2

##    def setup(self):
##        if self.text is not None:
##            nrows, ncols = container.getmaxyx()
##            container.attron(self.style)

##            if verticalPlacement == self.ALIGN_TO_TOP:
##                row = self.offset
##            elif verticalPlacement == self.ALIGN_TO_MIDDLE:
##                row = (nrows - len(contents)) / 2
##            elif verticalPlacement == self.ALIGN_TO_BOTTOM:
##                row = nrows - len(contents) - self.offset
##            else:
##                row = self.offset

##            for theText in contents:

##                if self.horizontalPlacement == self.ALIGN_TO_LEFT:
##                    col = self.offset
##                elif self.horizontalPlacement == self.ALIGN_TO_CENTER:
##                    col = (ncols - len(theText) - self.offset) / 2
##                elif self.horizontalPlacement == self.ALIGN_TO_RIGHT:
##                    col = (ncols - len(theText)) - self.offset
##                else:
##                    col = self.offset

##                container.addstr(row, col, '%s' % theText)
##                row += 1

##            container.attroff(self.style)

##        container.refresh()
##        if 0:
##            container.getch()
##        else:
##            curses.napms(5000)

if __name__ == '__main__':

    def tsMain(stdscr):
        xself = TsCurses()

        try:
            maxRows, maxCols = stdscr.getmaxyx()
            if maxRows < xself.expectedSize['rows']:
                xself.tsBomb('Screen needs %d lines; Only have %d.' %
                            (xself.expectedSize['rows'], maxRows))
            if maxCols < xself.expectedSize['cols']:
                xself.tsBomb('Screen needs %d columns.; Only have %d.' %
                            (xself.expectedSize['cols'], maxCols))
        except:
            xself.tsBomb('Unable to detect screen size.')

        xself.windows['stdscr'] = stdscr

        curses.start_color()
        curses.use_default_colors()
        stdscr.attrset(0)
        stdscr.box()
        stdscr.refresh()
        xself.tsCreateColorPairs()

        theContents = [
            'OS 6.2.0    \  SLEUTH 0.4.2 Ad Mfg/Sleuth_LITE.stg     pc-sw1    D 02-16:15:45',
            ' 11/07/05 14:05:44 11/10/05 06:22:29                                          ']
        begin_y = 1
        begin_x = 1
        nrows = len(theContents) + 2 # maxRows
        xself.logger.debug('nrows = %d' % nrows)
        ncols = maxCols - 2

        xself.tsCreateWindow('stdscr',
                            'frame1',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            background=None,
                            border=True,
                            title='Frame #1',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_BLACK, xself.COLOR_CYAN),
##                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
##                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_BLACK, xself.COLOR_CYAN),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        theContents = ['               CE INFO DISPLAY (0/0)                                          ',
                       '             Memory         Exec Heap K    Cluster K     Procs   Imgs         ',
                       '  CE  TP Size  FreeK HwtrK Size Free Hwtr Size Free Hwtr Cnt Max Cnt Max Reg  ',
                       '    1 H   -1M     -1    -1   -1   -1   -1   -1   -1   -1  -1  -1  -1  -1 0/0  ',
                       '    2 p  256M 245071     0  448  106  429   32   27    6   7  65   7  10 2/5  ',
                       '    3 p  256M 246811     0  448  236  414   32   28    6   4  65   4  10 1/5  ',
                       '    4 p  256M 252879     0  448  297  410   32   29    6   2  65   2  10 0/5  ',
                       '    5 p  256M 255223     0  448  320  401   32   30    6   2  65   2  10 1/5  ']

        begin_y = begin_y + nrows
        begin_x = 1
        nrows = len(theContents) + 2 # maxRows
        ncols = maxCols -2
        xself.tsCreateWindow('stdscr',
                            'frame2',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            background=None,
                            border=True,
                            title='Frame #2',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
##                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
##                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        theContents = ['               PROCESS INFO DISPLAY                                           ',
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

        begin_y = begin_y + nrows
        begin_x = 1
        nrows = len(theContents) + 2 # maxRows
        ncols = maxCols - 2
        xself.tsCreateWindow('stdscr',
                            'frame3',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            background=None,
                            border=True,
                            title='Frame #3',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
##                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
##                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        theContents = [' Type      Host   C80  I860   PPC SHARC TLoops   Sp  Errors Pid/Stuck         ',
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


        begin_y = begin_y + nrows
        begin_x = 1
        nrows = len(theContents) + 2 # maxRows
        ncols = maxCols - 2
        xself.tsCreateWindow('stdscr',
                            'frame4',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            background=None,
                            border=True,
                            title='Frame #4',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_WHITE, xself.COLOR_BLACK),
##                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
##                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_WHITE, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        theContents = [' E10 Tests:  11 Tgt:  11 Kills:14623 Pause: 0 Term-r Err:  0 Arun   Pg:1/1    ']

        begin_y = begin_y + nrows
        begin_x = 1
        nrows = len(theContents) + 2 # maxRows
        ncols = maxCols - 2
        xself.tsCreateWindow('stdscr',
                            'frame6',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            background=None,
                            border=True,
                            title='Frame #6',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_MAGENTA, xself.COLOR_BLACK),
##                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
##                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_MAGENTA, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        begin_y = begin_y + nrows
        begin_x = 1
        nrows = 7 + 2 #maxRows
        ncols = maxCols - 2
        xself.tsCreateWindow('stdscr',
                            'frame7',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            background=None,
                            border=True,
                            title='Frame #7',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
                            contents=None,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_YELLOW, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )

        theContents = ['        GENERAL                    TESTING                    DISPLAY      ',
                       '                                                                           ',
                       '   Help       Stop                                       NextPg    PrevPg  ',
                       '   Cluster    Tests           Options     Kill           Clear     ToFile  ',
                       '   Edit                       Limits      Modes          GoToPg    Display ']


        begin_y = begin_y + 1 #nrows
        begin_x = 2 #1
        nrows = len(theContents) + 2 # maxRows
        ncols = maxCols - 4
        xself.tsCreateWindow('frame7',
                            'frame8',
                            nrows,
                            ncols,
                            begin_y,
                            begin_x,
##                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
##                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            background=None,
                            border=True,
                            title='Automatic Menu',
                            titleColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_GREEN, xself.COLOR_BLACK),
                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
                            titleHorizontalAlignment=xself.ALIGN_TO_CENTER,
                            contents=theContents,
                            contentsColorPair=xself.tsActivatedColorPair(
                                xself.COLOR_GREEN, xself.COLOR_BLACK),
                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
                            )
        row = 62
        col = 70
        text = 'Now is the time to come to the aid of the party.'
##        stdscr.addstr(row, col - len(text), text)
        stdscr.addstr(row, 10, text)
        for row in range(62, 70):
            if row == 62:
                stdscr.attron(curses.A_STANDOUT)
                stdscr.addch(row, col, curses.ACS_UARROW)
                stdscr.attroff(curses.A_STANDOUT)
            elif row == 70 - 1:
                stdscr.attron(curses.A_STANDOUT)
                stdscr.addch(row, col, curses.ACS_DARROW)
                stdscr.attroff(curses.A_STANDOUT)
            else:
                stdscr.addch(row, col, curses.ACS_CKBOARD)

        row = 70
        text = 'Four score and seven years ago, our forefathers brought'
        stdscr.addstr(row - 1, col - len(text), text)
        for col in range(10, 70):
            if col == 10:
                stdscr.attron(curses.A_STANDOUT)
                stdscr.addch(row, col, curses.ACS_LARROW)
                stdscr.attroff(curses.A_STANDOUT)
            elif col == 70 - 1:
                stdscr.attron(curses.A_STANDOUT)
                stdscr.addch(row, col, curses.ACS_RARROW)
                stdscr.attroff(curses.A_STANDOUT)
            else:
                stdscr.addch(row, col, curses.ACS_CKBOARD)
##        begin_y = begin_y + 1
##        begin_x = 2
##        nrows = nrows - 2 #maxRows
##        ncols = (ncols/2) - 1
##        xself.tsCreateWindow('frame4',
##                            'frame5left',
##                            nrows,
##                            ncols,
##                            begin_y,
##                            begin_x,
####                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
####                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
####                            background=None,
##                            border=True,
##                            title='Frame #5left',
####                            titleColorPair=None,
####                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
####                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            contents=None,
####                            contentsColorPair=None,
####                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
####                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
##                            )
##        begin_x = ncols + 2
###        nrows = nrows - 2 #maxRows
###        ncols = (ncols/2) - 2
##        xself.tsCreateWindow('frame4',
##                            'frame5right',
##                            nrows,
##                            ncols,
##                            begin_y,
##                            begin_x,
####                            parentVerticalAlignment=xself.ALIGN_TO_TOP,
####                            parentHorizontalAlignment=xself.ALIGN_TO_LEFT,
####                            background=None,
##                            border=True,
##                            title='Frame #5right',
####                            titleColorPair=None,
####                            titleVerticalAlignment=xself.ALIGN_TO_TOP,
####                            titleHorizontalAlignment=xself.ALIGN_TO_LEFT,
##                            contents=None,
####                            contentsColorPair=None,
####                            contentsVerticalAlignment=xself.ALIGN_TO_TOP,
####                            contentsHorizontalAlignment=xself.ALIGN_TO_LEFT
##                            )

#        xself.titleTest(stdscr)
#        xself.borderlessTitleTest(stdscr)
#        xself.contentTest(stdscr)
#        xself.windowTest(stdscr)

        stdscr.getch()

    curses.wrapper(tsMain)
