#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:01:10 AM rsg>"
'''
tsWxGauge.py - Class to establish a gauge, a horizontal or
vertical bar which shows a quantity (often time). wxGauge
supports two working modes: determinate and indeterminate
progress.
'''
#################################################################
#
# File: tsWxGauge.py
#
# Purpose:
#
#    Class to establish a gauge, a horizontal or vertical bar
#    which shows a quantity (often time). wxGauge supports two
#    working modes: determinate and indeterminate progress.
#
# Usage (example):
#
#    # Import
#
#    from tsWxGauge import Gauge as wxGauge
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
#    2011/12/26 rsg Added logic to tsGaugeLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/03/22 rsg Added logic to tsCreateGauge to apply
#                   the wx.DISPLAY_NORMAL attribut only when
#                   bar graph cell contains a blank (" "). The
#                   the wx.DISPLAY_REVERSE attribute is applied
#                   to the remaining cells. This will accomodate
#                   bar graph characters such as the standard
#                   "#" character or an alternate one for future
#                   pulsing (such as "/", ":" etc.).
#
#    2012/07/04 rsg Added dashed separator lines between methods.
#
# ToDo:
#
#    2012/03/22 rsg Add support for self.Pulse. Replace sequence
#                   of consecutive "##" by sequence of "#/" or
#                   "/#" that alternate upon each pulse tick.
#
#################################################################

__title__     = 'tsWxGauge'
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

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

# BarGraph Tokens
blankToken = ' '
standardToken = '#'
pulseToken = 'Z'

#---------------------------------------------------------------------------

class Gauge(Control):
    '''
    A gauge is a horizontal or vertical bar which shows a quantity
    (often time). wxGauge supports two working modes: determinate and
    indeterminate progress.

    The first is the usual working mode (see SetValue() and SetRange())
    while the second can be used when the program is doing some processing
    but you do not know how much progress is being done. In this case,
    you can periodically call the Pulse() function to make the progress
    bar switch to indeterminate mode (graphically it is usually a set of
    blocks which move or bounce in the bar control).

    wxGauge supports dynamic switch between these two work modes.

    There are no user commands for the gauge.
    '''
 
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 range=100,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.GA_HORIZONTAL,
                 validator=wx.DefaultValidator,
                 name=wx.GaugeNameStr):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        theClass = 'Gauge'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_range = range
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
            self.logger.debug('              range: %s' % range)
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

        self.ts_Range = range
        self.ts_Validator = validator
        self.ts_Value = False
        self.ts_BarGraph = []

        self.ts_GaugePos = 0

        myRect, myClientRect = self.tsGaugeLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               range=100,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.GA_HORIZONTAL,
               validator=wx.DefaultValidator,
               name=wx.GaugeNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        myRect, myClientRect = self.tsGaugeLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def GetBezelFace(self):
        '''
        '''
        # GA_HORIZONTAL             = 0x00000004
        # GA_VERTICAL               = 0x00000008
        # BORDER                    = 0x02000000
        # BORDER_DOUBLE             = 0x10000000
        # BORDER_MASK               = 0x1F200000
        # BORDER_NONE               = 0x00200000
        # BORDER_RAISED             = 0x04000000
        # BORDER_SIMPLE             = 0x02000000
        # BORDER_STATIC             = 0x01000000
        # BORDER_SUNKEN             = 0x08000000
        # BORDER_THEME              = 0x10000000
        if (self.ts_Style & wx.BORDER) == wx.BORDER:
            theBezelFace = wx.BORDER

        elif (self.ts_Style & wx.BORDER_DOUBLE) == wx.BORDER_DOUBLE:
            theBezelFace = wx.BORDER_DOUBLE

        elif (self.ts_Style & wx.BORDER_MASK) == wx.BORDER_MASK:
            theBezelFace = wx.BORDER_MASK

        elif (self.ts_Style & wx.BORDER_NONE) == wx.BORDER_NONE:
            theBezelFace = wx.BORDER_NONE

        elif (self.ts_Style & wx.BORDER_RAISED) == wx.BORDER_RAISED:
            theBezelFace = wx.BORDER_RAISED

        elif (self.ts_Style & wx.BORDER_SIMPLE) == wx.BORDER_SIMPLE:
            theBezelFace = wx.BORDER_SIMPLE

        elif (self.ts_Style & wx.BORDER_STATIC) == wx.BORDER_STATIC:
            theBezelFace = wx.BORDER_STATIC

        elif (self.ts_Style & wx.BORDER_SUNKEN) == wx.BORDER_SUNKEN:
            theBezelFace = wx.BORDER_SUNKEN

        elif (self.ts_Style & wx.BORDER_THEME) == wx.BORDER_THEME:
            theBezelFace = wx.BORDER_THEME

        else:
            msg = 'NotImplementedError: %s' % 'GetBezelFace in tsWxGauge'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (theBezelFace)

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

    def GetRange(self):
        '''
        '''
        return (self.ts_Range)

    #-----------------------------------------------------------------------
 
    def GetShadowWidth(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'GetShadowWidth in tsWxGauge'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def GetValue(self):
        '''
        '''
        return (self.ts_GaugePos)

    #-----------------------------------------------------------------------
 
    def IsVertical(self):
        '''
        '''
        return (not (self.ts_Style & wx.GA_HORIZONTAL))

    #-----------------------------------------------------------------------
 
    def Pulse(self):
        '''
        '''
        barGraphOrig = self.ts_BarGraph
        if len(self.ts_BarGraph) > 1:
            if barGraphOrig[0] == standardToken and \
               barGraphOrig[1] == standardToken:

                for i in range(0, len(self.ts_BarGraph), 2):
                    if barGraphOrig[i] == standardToken:
                        self.ts_BarGraph[i] = pulseToken

                for i in range(1, len(self.ts_BarGraph), 2):
                    if barGraphOrig[i] == pulseToken:
                        self.ts_BarGraph[i] = standardToken

            else:

                # TBD - Will this operate properly after initial SetValue?

                for i in range(0, len(self.ts_BarGraph), 2):
                    if barGraphOrig[i] == standardToken:
                        self.ts_BarGraph[i] = pulseToken
                    elif barGraphOrig[i] == pulseToken:
                        self.ts_BarGraph[i] = standardToken

                for i in range(1, len(self.ts_BarGraph), 2):
                    if barGraphOrig[i] == standardToken:
                        self.ts_BarGraph[i] = pulseToken
                    elif barGraphOrig[i] == pulseToken:
                        self.ts_BarGraph[i] = standardToken
        self.tsShow()

    #-----------------------------------------------------------------------
 
    def SetBezelFace(self, w):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetBezelFace in tsWxGauge'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def SetRange(self, range):
        '''
        '''
        self.ts_Range = range
        if self.ts_GaugePos > self.ts_Range:
            self.ts_GaugePos = self.ts_Range

        self.tsSetGauge()

    #-----------------------------------------------------------------------
 
    def SetShadowWidth(self, w):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetShadowWidth in tsWxGauge'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def SetValue(self, pos):
        '''
        '''
        assert (pos <= self.ts_Range)

        self.ts_GaugePos = pos
        self.tsSetGauge()

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsBestSize(self):
        '''
        '''
        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=True)

        gaugeThickness = 1
        gaugeLength = 10
 
        if self.ts_Style & wx.GA_VERTICAL:
            # Vertical
            best = wxSize(
                (gaugeThickness * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (gaugeLength * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))
        else:
            # Horizontal
            best = wxSize(
                (gaugeLength * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (gaugeThickness * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))

        return (best)

    #-----------------------------------------------------------------------

    def tsCreateGauge(self):
        '''
        '''
        barGraph = self.ts_BarGraph

        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=False)

        if self.ts_Style & wx.GA_HORIZONTAL:

            # Align Horizontal
            maxCols = self.Rect.width // wx.pixelWidthPerCharacter
            minCol =  borderThickness.width
            row = borderThickness.height
            for col in range(minCol, maxCols - minCol, 1):
                fill = barGraph[col - 1]
                if fill == ' ':
                    self.tsCursesAddCh(
                        col, row, fill,
                        attr=None, pixels=False)
                else:
                    self.tsCursesAddCh(
                        col, row, fill,
                        attr=wx.DISPLAY_REVERSE, pixels=False)

        else:
            # Align Vertical
            maxRows = self.Rect.height // wx.pixelHeightPerCharacter
            minRow = borderThickness.height
            col = borderThickness.width
            for row in range(minRow, maxRows - minRow, 1):
                reversedRow = maxRows - row - 1
                fill = barGraph[row - 1]
                if fill == ' ':
                    self.tsCursesAddCh(
                        col, reversedRow, fill,
                        attr=None, pixels=False)
                else:
                    self.tsCursesAddCh(
                        col, reversedRow, fill,
                        attr=wx.DISPLAY_REVERSE, pixels=False)

    #-----------------------------------------------------------------------

    def tsSetGauge(self):
        '''
        '''
        assert (0 <= self.ts_GaugePos and \
                self.ts_GaugePos <= self.ts_Range)

        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=False)

        self.ts_BarGraph = []
        if self.ts_Style & wx.GA_HORIZONTAL:
            # Align Horizontal
            maxCols = self.Rect.width // wx.pixelWidthPerCharacter
            minCol =  borderThickness.width
            row = borderThickness.height
            slope = float(self.ts_Range) / float(maxCols - 2 * minCol)
            intercept = float(0)
            # col = 1
            for col in range(minCol, maxCols - minCol, 1):
                y = slope * float(col - minCol) + intercept
 
                if y < float(self.GetValue()):
                    fill = standardToken
                else:
                    fill = blankToken

                self.ts_BarGraph.append(fill)
        else:
            # Align Vertical
            maxRows = self.Rect.height // wx.pixelHeightPerCharacter
            minRow = borderThickness.height
            col = borderThickness.width
            slope = float(self.ts_Range) / float(maxRows - 2 * minRow)
            intercept = float(0)
            for row in range(minRow, maxRows - minRow, 1):
                reversedRow = maxRows - row - 1
                y = slope * float(row - minRow) + intercept

                if y < float(self.GetValue()):
                    fill = standardToken
                else:
                    fill = blankToken

                self.ts_BarGraph.append(fill)

        self.tsShow()

    #-----------------------------------------------------------------------

    def tsGaugeLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of gauge based upon arguments.
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

        label = self.ts_Name

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[]')) * wx.pixelWidthPerCharacter,
                    wx.pixelHeightPerCharacter)

            elif label.find('\n') == -1:
                # TBD - Remove adjustment for extra cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[ ]')) * wx.pixelWidthPerCharacter,
                    wx.pixelHeightPerCharacter)
            else:
                # TBD - Remove adjustment for extra cursor width
                theLines = label.split('\n')
                maxWidth = 0
                maxHeight = len(theLines)
                for aLine in theLines:
                    if len(aLine) > maxWidth:
                        maxWidth = len(aLine)
                theLabelSize = wxSize(
                    (maxWidth + len('[ ]')) * wx.pixelWidthPerCharacter,
                    maxHeight * wx.pixelHeightPerCharacter)

            self.logger.debug(
                '      theLabelSize (end): %s' % theLabelSize)

            if False and thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theLabelSize.width,
                                theLabelSize.height)

            else:
                # Not theDefaultPosition

                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theLabelSize.width,
                                theLabelSize.height)

        else:
            # Not theDefaultSize

            if False and thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theSize.width,
                                theSize.height)

            else:
                # Not theDefaultPosition

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
        msg = fmt % (parent, str(pos), str(size), name, label, str(myRect))

        self.logger.debug('    tsGaugeLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Gauge specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            range=self.ts_Range,
                            pos=self.ts_Rect.Position,
                            size=self.ts_Rect.Size,
                            style=self.ts_Style,
                            validator=self.ts_Validator,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
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
            self.tsCreateBorder()
            self.tsCreateGauge()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    BezelFace = property(GetBezelFace, SetBezelFace)
    Range = property(GetRange, SetRange)
    ShadowWidth = property(GetShadowWidth, SetShadowWidth)
    Value = property(GetValue, SetValue)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
