#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:33:37 AM rsg>"
'''
tsWxStaticLine.py - Class to establish a static line, which may
be used in a dialog to separate the groups of controls.

The line may be only vertical or horizontal. Moreover, not all
ports (notably not wxGTK) support specifying the transversal
direction of the line (e.g. height for a horizontal line) so
for maximal portability you should specify it as wxDefaultCoord.
'''
#################################################################
#
# File: tsWxStaticLine.py
#
# Purpose:
#
#     Class to establish a static line, which may be used in a
#     dialog to separate the groups of controls.
#
#     The line may be only vertical or horizontal. Moreover,
#     not all ports (notably not wxGTK) support specifying the
#     transversal direction of the line (e.g. height for a
#     horizontal line) so for maximal portability you should
#     specify it as wxDefaultCoord.
#
# Usage (example):
#
#    # Import
#
#    from tsWxStaticLine import StaticLine
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    While a vertical line can fill its parent's client area height,
#    a horizontal line can fill its parent's client area width except
#    for right-most column which must be reserved for cursor in order
#    to not wrap into next row. To ensure symetry, the design blank
#    fills the left-most horizontal column. For consistancy, the
#    design blank fills the top-most and bottom-most vertical rows.
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    2012/07/04 rsg Derived design from tsWxGauge.
#
#    2012/07/30 rsg Removed the unused tsSetStaticLine which
#                   had been superceded by tsCreateStaticLine.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsWxStaticLine'
__version__   = '1.1.0'
__date__      = '07/18/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class StaticLine(Control):
    '''
    Class to establish a static line, which may be used in a dialog to
    separate the groups of controls.
    '''
 
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.LI_VERTICAL,
                 validator=wx.DefaultValidator,
                 name=wx.StaticLineNameStr):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        theClass = 'StaticLine'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         validator=validator,
                         name=name)

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Default = False

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        if False:
            # Leaves artifacts of different color than parent background.
            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_Validator = validator

        self.ts_StaticLinePos = 0

        myRect, myClientRect = self.tsStaticLineLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.LI_VERTICAL,
               validator=wx.DefaultValidator,
               name=wx.StaticLineNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        myRect, myClientRect = self.tsStaticLineLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignored under other platforms. Under Mac, it will change the size of
        the returned font. See wx.Window.SetWindowVariant for more about this.
        '''
        return (variant)

    #-----------------------------------------------------------------------
 
    def IsVertical(self):
        '''
        '''
        if self.ts_Style & wx.LI_VERTICAL:
            results = True
        else:
            results = False
        return (results)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsCreateStaticLine(self):
        '''
        '''
        horizontalLineToken = curses.ACS_HLINE
        verticalLineToken = curses.ACS_VLINE

        if self.ts_Style & wx.LI_HORIZONTAL:

            # Align Horizontal
            maxCols = self.Rect.width // wx.pixelWidthPerCharacter
            minCol =  0
            row = 0
            for col in range(minCol, maxCols, 1):
                if col < 1:
                    fill = ' '
                else:
                    fill = horizontalLineToken

                self.tsCursesAddCh(
                    col, row, fill,
                    attr=None, pixels=False)

        else:
            # Align Vertical
            maxRows = self.Rect.height // wx.pixelHeightPerCharacter
            minRow = 0
            col = 0
            for row in range(minRow, maxRows, 1):

                reversedRow = (maxRows - 1) - row

                if ((row < 1) or \
                    (row > (maxRows - 2))):
                    fill = ' '
                else:
                    fill = verticalLineToken

                self.tsCursesAddCh(
                    col, reversedRow, fill,
                    attr=None, pixels=False)

    #-----------------------------------------------------------------------

    def tsStaticLineLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of StaticLine based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)
 
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        if theSize == theDefaultSize:
            # theDefaultSize

            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            parent.ClientArea.width,
                            parent.ClientArea.height)

        else:
            # Not theDefaultSize

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

##        theDisplayRect = self.Display.GetClientArea()
##        if not theDisplayRect.InsideRect(myRect):
##            myRect = wxRect(
##                max(thePosition.x, theDisplayRect.x),
##                max(thePosition.y, theDisplayRect.y),
##                min(theSize.width, theDisplayRect.width),
##                min(theSize.height, theDisplayRect.height - 1))

##        if not theDisplayRect.InsideRect(myRect):
##            myRect = theDisplayRect

        myClientRect = wxRect(myRect.x,
                              myRect.y,
                              myRect.width,
                              myRect.height)

        self.tsTrapIfTooSmall(name, myRect)
        fmt = 'parent=%s; pos=%s; size=%s; ' + \
              'name="%s"; label="%s"; myRect=%s'
        msg = fmt % (
            parent, str(pos), str(size), name, self.GetLabel(), str(myRect))

        self.logger.debug('    tsStaticLineLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update StaticLine specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            pos=self.ts_Rect.Position,
                            size=self.ts_Rect.Size,
                            style=self.ts_Style,
                            validator=self.ts_Validator,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Button.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            # self.tsCreateBorder()
            self.tsCreateStaticLine()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
