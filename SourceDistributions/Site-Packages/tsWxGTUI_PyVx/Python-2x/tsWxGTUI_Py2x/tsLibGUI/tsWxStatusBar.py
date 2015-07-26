#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:45:12 AM rsg>"
'''
tsWxStatusBar.py - Class to establish a status bar, a narrow
window that can be placed along the bottom of a frame to give
small amounts of status information. It can contain one or
more fields, one or more of which can be variable length
according to the size of the window.

wxStatusBar also maintains an independent stack of status texts
for each field (see PushStatusText() and PopStatusText()).

Note that in wxStatusBar context, the terms pane and field are
synonyms.
'''
#################################################################
#
# File: tsWxStatusBar.py
#
# Purpose:
#
#    Class to establish a status bar, a narrow window that can
#    be placed along the bottom of a frame to give small amounts
#    of status information. It can contain one or more fields,
#    one or more of which can be variable length according to
#    the size of the window.
#
#    wxStatusBar also maintains an independent stack of status
#    texts for each field (see PushStatusText() and
#    PopStatusText()).
#
#    Note that in wxStatusBar context, the terms pane and field
#    are synonyms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxStatusBar import StatusBar
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
#    08/10/2010 rsg - Replaced references to wxStaticText by
#                     wxTextCtrl.
#
#    2011/12/26 rsg - Added logic to tsStatusBarLayout to inhibit
#                     operation once self.ts_Handle has been
#                     assigned a curses window identifier.
#
# ToDo:
#
#    1) Incorrect Fields Text (GetLabel !!= text).
#
#    None.
#
#################################################################

__title__     = 'tsWxStatusBar'
__version__   = '1.2.0'
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

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI

from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxTextCtrl import TextCtrl as wxTextCtrl
from tsWxGTUI_Py2x.tsLibGUI.tsWxWindow import Window

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

callerPositionSizeStyleEnabled = False

#---------------------------------------------------------------------------

class StatusBar(Window):
    '''
    Class to establish a status bar, a narrow window that can be placed
    along the bottom of a frame to give small amounts of status information.
    It can contain one or more fields, one or more of which can be variable
    length according to the size of the window.

    wxStatusBar also maintains an independent stack of status texts for
    each field (see PushStatusText() and PopStatusText()).

    Note that in wxStatusBar context, the terms pane and field are synonyms.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_STATUSBAR_STYLE,
                 name=wx.StatusLineNameStr):
        '''
        Create a Control. Normally you should only call this from a subclass
        (_init__) as a plain old wx.Control is not very useful.
        '''
        theClass = 'StatusBar'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Window.__init__(self,
                        parent,
                        id=id,
                        pos=pos,
                        size=size,
                        style=style,
                        name=name)

        self.tsBeginClassRegistration(theClass, id)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        # Initialize StatusBar Contents
        self.ts_minHeight = wx.ThemeToUse['StatusBar']['WindowHeight']

        self.ts_nFields = 0
        self.ts_FieldRect = []
        self.ts_Fields = []
        self.ts_StatusStacks = []
        self.ts_StatusStyles = []
        self.ts_StatusText = []
        self.ts_StatusTextStacks = []
        self.ts_StatusWidths = []

        if callerPositionSizeStyleEnabled:
            self.ts_Style = style
        else:
            self.ts_Style = wx.DEFAULT_STATUSBAR_STYLE

        self.ts_Rect = self.tsStatusBarLayout(parent, pos, size, style, name)

        if DEBUG:
            print('__init__: self.ts_Rect = %s' % self.ts_Rect)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
##            self.logger.debug('              title: %s' % title)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)
            self.logger.debug('rect (see pos/size): %s' % self.ts_Rect)

        self.ts_BackgroundColour = wx.ThemeToUse['BackgroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse['ForegroundColour'].lower()

        self.tsEndClassRegistration(theClass)

    def Create(self,
               parent,
               id=wx.ID_ANY,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
##               style=wx.ST_SIZEGRIP,
               style=wx.BORDER_SIMPLE,
               name=wx.StatusLineNameStr,
               pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        if DEBUG:
            self.logger.debug('StatusBar.Create')
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % id)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)
            self.logger.debug('             pixels: %s' % pixels)

        self.ts_Rect = self.tsStatusBarLayout(parent, pos, size, style, name)

        if DEBUG:
            print('Create: self.ts_Rect = %s' % self.ts_Rect)

        self.ts_Handle = self.tsCursesNewWindow(self.ts_Rect, pixels=pixels)

        self._tsCalculateAbsWidths()
        self._tsCreateStatusText()

        return (self.ts_Handle is not None)

    def GetBorderX(self):
        '''
        '''
        return (self.ts_Rect.x)

    def GetBorderY(self):
        '''
        '''
        return (self.ts_Rect.y)

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class.
        '''
        return (wx.WINDOW_VARIANT_NORMAL)

    def GetFieldRect(self, i=0):
        '''
        '''
        return (self.ts_FieldRect[i])

    def GetFields(self):
        '''
        Return a list of field values in the status bar.
        '''
        return (self.ts_Fields)

    def GetFieldsCount(self):
        '''
        Return the number of field values in the status bar.
        '''
        return (self.ts_nFields)

    def GetStatusText(self, number=0):
        '''
        '''
        assert number < self.ts_nFields

        return (self.ts_Fields[number].Label)

    def PopStatusText(self, number=0):
        '''
        Restore the previous text associated with a specified field.
        '''
        assert number < self.ts_nFields
        assert len(self.ts_StatusTextStacks[number]) > 0

        top = len(self.ts_StatusTextStacks[number]) - 1
        self.SetStatusText(self.ts_StatusTextStacks[number][top], number)
        self.ts_StatusTextStacks[number].remove[top]

    def PushStatusText(self, text, number=0):
        '''
        Change the text associated with a specified field after saving
        the previous value for later use.
        '''
        assert number < self.ts_nFields
 
        self.ts_StatusTextStacks[number].append(self.GetStatusText(number))
        self.SetStatusText(text, number)

    def SetFields(self, items):
        '''
        Set the values of the StatusBar fields from a list of strings.
        '''
        assert len(items) <= self.ts_nFields

        for index in range(len(items)):
            try:
                self.ts_Fields[index].Label = items[index]
            except IndexError, e:
##                self.ts_Fields[index].Label = items[index]
                self.logger.error('Exception %s.' % e)
##                raise IndexError

    def SetFieldsCount(self, number):
        '''
        Subdivide the StatusBar into the specified number of fieilds.
        '''
        assert number > 0

        if number > self.ts_nFields:

            for index in range(self.ts_nFields, number):
                self.ts_FieldRect.append(None)
                self.ts_Fields.append(None)
                self.ts_StatusStacks.append([])
                self.ts_StatusStyles.append(wx.DEFAULT_STATUSBAR_STYLE)
                self.ts_StatusText.append(wx.EmptyString)
                self.ts_StatusTextStacks.append([])
                self.ts_StatusWidths.append(-1)

        elif number < self.ts_nFields:

            for index in range(number, self.ts_nFields):
                self.ts_FieldRect.remove(index)
                self.ts_Fields.remove(index)
                self.ts_StatusStacks.remove(index)
                self.ts_StatusStyles.remove(index)
                self.ts_StatusText.remove(index)
                self.ts_StatusTextStacks.remove(index)
                self.ts_StatusWidths.remove(index)

        self.ts_nFields = number

        # Reinitialize Widths
        widths = []
        for index in range(number):
            widths.append(-1)

        self.SetStatusWidths(widths)

    def SetMinHeight(self, height):
        '''
        Change the minimum height of the StatusBar.
        '''
        self.ts_minHeight = height

    def SetStatusStyles(self, styles):
        '''
        Change the style of StatusBar field(s).
        '''
        assert len(styles) == self.ts_nFields

        for index in range(len(styles)):
            try:
                self.ts_StatusStyles[index] = styles[index]
            except IndexError:
                self.ts_StatusStyles.append(styles[index])
                self.logger.error(
                    'SetStatusStyles IndexError: %d' % index)

    def SetStatusText(self, text, number=0):
        '''
        Change the label text associated with the specified StatusBar field.
        '''
        assert number < self.ts_nFields

        theLabel = text
        index = number

        try:
            self.ts_StatusText[index] = theLabel
        except IndexError:
            self.ts_StatusText.append(theLabel)
            self.logger.debug(
                'SetStatusText IndexError: %d' % index)

    def SetStatusWidths(self, widths):
        '''
        Change the width of StatusBar field(s).
        '''
        assert len(widths) == self.ts_nFields

        self.ts_StatusWidths = widths

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def _tsCalculateAbsWidths(self):
        '''
        '''
        widths = self.ts_StatusWidths

        number = self.ts_nFields

        baseRect = self.ts_Rect

        maxFixed = 0
        maxProportional = 0
        for index in range(number):
            if widths[index] < 0:
                maxProportional += widths[index]
            else:
                maxFixed += widths[index]
            fmt = '_tsCalculateAbsWidths: widths[%d]; ' + \
                  'MaxProportional=%d; maxFixed=%d'
            self.logger.debug(fmt % (index, maxProportional, maxFixed))

        for index in range(number):
            if widths[index] < 0:
                myWidth = int(float(baseRect.width - maxFixed) * float(
                    widths[index]) / float(maxProportional))
            else:
                myWidth = widths[index]
            widths[index] = myWidth

        # Adjust to match parent width.
        # TBD - Resolve need for subtracting one character width?
        theRemainingWidth = min(
            baseRect.width,
            self.ts_Parent.ts_Rect.width - wx.pixelWidthPerCharacter)
        for index in range(number):
            theRemainingWidth -= widths[index]
 
        widths[0] += theRemainingWidth

        self._tsCreateFields()

    def _tsCreateFields(self):
        '''
        '''
        widths = self.ts_StatusWidths

        number = self.ts_nFields

        baseRect = self.Rect

        # RSG - 07/31/2008
        if True:
            # TBD - Why did change to tsWxTextCtrl introduce need for this.
            baseRect.x -= wx.pixelWidthPerCharacter
            baseRect.y -= wx.pixelHeightPerCharacter
        else:
            # TBD - Why round up?
            # Compensates for centering that splits a single character
            baseRect.x += wx.pixelWidthPerCharacter // 2
        # RSG - 07/31/2008
 
        remainderWidth = 0

        overlay = wx.ThemeToUse['StatusBar']['Overlay']
        if overlay and number > 1:
            overlayAdjustment = wx.pixelWidthPerCharacter
        else:
            overlayAdjustment = 0

        cells = []
        for index in range(number):
            characterWidth, pixelRemainder = divmod(
                widths[index], wx.pixelWidthPerCharacter)
            remainderWidth += pixelRemainder
            cells.append(characterWidth * wx.pixelWidthPerCharacter)
            if index < number - 1:
                cells[index] += overlayAdjustment
                if overlay:
                    remainderWidth += (wx.pixelWidthPerCharacter // 2) - 1
            else:
                cells[index] += remainderWidth
            if DEBUG:
                fmt = '_tsCreateFields: ' + \
                      'widths(%d)=%3d; ' + \
                      'cells=%3d; ' + \
                      'remainderWidth=%3d'
                self.logger.debug(fmt % (
                    index, widths[index], cells[index], remainderWidth))

        self.ts_FieldRect = []
        self.ts_Fields = []
        self.ts_StatusStyles = []
        self.ts_StatusWidths = []
        for index in range(number):
            self.ts_Fields.append(None)
            self.ts_StatusStyles.append(self.ts_Style)
            self.ts_StatusWidths.append(cells[index])
            if index == 0:
                self.ts_FieldRect.append(
                    wxRect(baseRect.x,
                           baseRect.y,
                           self.ts_StatusWidths[index],
                           baseRect.height))

##            elif index == 1:
##                if True or overlay:
##                    self.ts_FieldRect.append(
##                        wxRect(self.ts_FieldRect[index - 1].x + \
##                               self.ts_StatusWidths[index - 1],
##                               self.ts_FieldRect[index - 1].y,
##                               self.ts_StatusWidths[index],
##                               self.ts_FieldRect[index - 1].height))

##                else:
##                    self.ts_FieldRect.append(
##                        wxRect(self.ts_FieldRect[index - 1].x + \
##                               self.ts_StatusWidths[index - 1] + remainderWidth,
##                               self.ts_FieldRect[index - 1].y,
##                               self.ts_StatusWidths[index],
##                               self.ts_FieldRect[index - 1].height))

            else:
                if overlay:
                    self.ts_FieldRect.append(
                        wxRect(self.ts_FieldRect[index - 1].x + \
                               self.ts_StatusWidths[index - 1] - overlayAdjustment,
                               self.ts_FieldRect[index - 1].y,
                               self.ts_StatusWidths[index],
                               self.ts_FieldRect[index - 1].height))
                else:
                    self.ts_FieldRect.append(
                        wxRect(self.ts_FieldRect[index - 1].x + \
                           self.ts_StatusWidths[index - 1] - overlayAdjustment,
                           self.ts_FieldRect[index - 1].y,
                           self.ts_StatusWidths[index],
                           self.ts_FieldRect[index - 1].height))
 
            if DEBUG:
                fmt = '_tsCreateFields: ' + \
                      'ts_FieldRect(%d)=%s; '
                self.logger.debug(fmt % (
                    index, str(self.ts_FieldRect[index])))

        # TBD - Can creating TextCtrl be deferred until Show?
        if True:
            self._tsCreateStatusText()

    def _tsCreateStatusText(self):
        '''
        Create each Status Bar Field. Set label to empty string until
        application defines a real value..
        '''
        number = self.ts_nFields # self.GetFieldsCount()

        parent = self
        for index in range(number):
            theText = wxTextCtrl(
                parent,
 
                id=wx.ID_ANY,
 
                value=wx.EmptyString,

                pos=(self.ts_FieldRect[index].x + \
                     wx.pixelWidthPerCharacter,
 
                     self.ts_FieldRect[index].y + \
                     wx.pixelHeightPerCharacter),
 
                size=(self.ts_FieldRect[index].width - \
                      0 * wx.pixelWidthPerCharacter,
 
                      self.ts_FieldRect[index].height - \
                      0 * wx.pixelHeightPerCharacter),
 
                style=wx.DEFAULT_STATUSBAR_STYLE,
 
                validator=wx.DefaultValidator,
 
                name='%s(%d)' % (self.ts_Name, index))

            if DEBUG:
                print('_tsCreateStatusText: index=%s; rect=%s' % (
                    index, self.ts_FieldRect[index]))

            try:

                self.ts_Fields[index] = theText

            except IndexError:

                self.ts_Fields.append(theText)

                self.logger.debug(
                    '_tsCreateStatusText: self.ts_Fields[%d]: %s' % (
                        index,
                        self.ts_Fields[index]))

    def tsStatusBarLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of status bar. Ignore based upon arguments.
        '''
        ###############################################################
        #      X=0         1         2         3   X=W-1
        #        01234567890123456789012345678901234
        # Y=0    +- Frame Title ---------[-][=][X]-+ Frame Border Top
        #   1    +---------------------------------+ Menu Bar Border Top
        #   2    |Menu Bar (Optional)              |
        #   3    |   (ex. 35 cols x 4 rows)        |
        #   4    +- - - - - - - - - - - - - - - - -+ Menu Bar Border Bottom
        #   4    + - - - - - - - - - - - - - - - - + Tool Bar Border Top
        #   5    |Tool Bar (Optional)              |
        #   6    |   (ex. 35 cols x 4 rows)        |
        #   7    +- - - - - - - - - - - - - - - - -+ Tool Bar Border Bottom
        #   7    + - - - - - - - - - - - - - - - - + Client Border Top
        #   8    |Client Area                      |
        #   9    |   (ex. 35 cols x 5 rows)        |
        #   H-5  |                                 |
        #   H-4  +- - - - - - - - - - - - - - - - -+ Client Border Bottom
        #   H-4  + - - - - - - - - - - - - - - - - + Status Border Top
        #   H-3  |Status Line (Optional)           |
        #   H-2  |   (ex. 35 cols x 4 rows)        |
        # Y=H-1  +---------------------------------| Status Border Bottom
        #
        # NOTE: Overlapping rows denoted by "- - - -" and " - - - ".
        ###############################################################
        # Apply override of parental StatusBar position.
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            ## return (self.ts_Rect, self.ts_ClientRect)
            return (self.ts_Rect)

        thePixelSize = parent.Rect.Size
        thePixelSize.height = self.ts_minHeight

        if parent.Rect.Size != self.display.ClientArea.Size:
            offset = thePixelSize.height - 1 * wx.pixelHeightPerCharacter
        else:
            offset = thePixelSize.height - 2 * wx.pixelHeightPerCharacter

        myRect = wxRect(parent.Rect.x,
                        parent.Rect.y + parent.Rect.height - offset,
                        thePixelSize.width,
                        thePixelSize.height)

        return (myRect)

    def tsShow(self):
        '''
        Shows or hides the window. You may need to call Raise for a top
        level window if you want to bring it to top, although this is not
        needed if Show is called immediately after the frame creation.
        Returns True if the window has been shown or hidden or False if
        nothing was done because it already was in the requested state.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                myRect = wxRect(
                    self.ts_Parent.Rect.Left,
                    (self.ts_Parent.Rect.Bottom - \
                     wx.ThemeToUse['StatusBar']['WindowHeight'] - \
                     wx.pixelHeightPerCharacter),
                    self.ts_Parent.Rect.width,
                    wx.ThemeToUse['StatusBar']['WindowHeight'])

                thePosition = wxPoint(myRect.x, myRect.y)
                theSize = wxSize(myRect.width, myRect.height)

                # TBD - Update Class geometry.
                self.ts_Rect = myRect
                self.logger.debug(
                    'tsShow: myRect=%s; Rect = %s' % (myRect, self.ts_Rect))

                self.ts_BaseRect = self.ts_Rect
                if DEBUG:
                    print('tsShow: myRect=%s; Rect = %s' % (myRect, self.ts_Rect))

                self.Create(self,
                            id=-1,
                            pos=thePosition,
                            size=theSize,
                            style=self.ts_Style,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()
 
    def tsUpdate(self):
        '''
        Draw the actual features of the StatusBar.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd(' ', attr=None)

            if self.tsIsBorderStyle(style=self.ts_Style):
                self.tsCursesBox()

            self.tsCreateLabel()

            self._tsUpdateStatusText()

    def _tsUpdateStatusText(self):
        '''
        '''
        for index in range(self.GetFieldsCount()):
            theLabel = self.ts_StatusText[index]

            if DEBUG:
                oldLabel = self.ts_Fields[index].GetLabel()
                msg1 = '_tsUpdateStatusText:'
                msg2 = 'index=%d;' % index
                msg3 = 'GetLabel="%s";' % oldLabel
                msg4 = 'SetLabel="%s"' % theLabel

                print('%s %s %s %s' % (msg1, msg2, msg3, msg4))

            self.ts_Fields[index].SetLabel(theLabel)
            self.ts_Fields[index].tsCreateStatusLabel()
            self.ts_Fields[index].Show()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
#---------------------------------------------------------------------------

    BorderX = property(GetBorderX)
    BorderY = property(GetBorderY)
    FieldRect = property(GetFieldRect)
    Fields = property(GetFields, SetFields)
    FieldsCount = property(GetFieldsCount, SetFieldsCount)
    StatusText = property(GetStatusText, SetStatusText)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
