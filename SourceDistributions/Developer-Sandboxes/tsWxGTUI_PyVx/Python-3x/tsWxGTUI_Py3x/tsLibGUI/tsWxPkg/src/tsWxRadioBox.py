#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:43:37 AM rsg>"
'''
tsWxRadioBox.py - Class to establish a RadioBox that is used to
select one of a number of mutually exclusive choices. It is
displayed as a vertical column or horizontal row of labelled
buttons, surrounded by a box that can optionally have a label.
'''
#################################################################
#
# File: tsWxRadioBox.py
#
# Purpose:
#
#    Class to establish a RadioBox that is used to select one of
#    a number of mutually exclusive choices. It is displayed as
#    a vertical column or horizontal row of labelled buttons,
#    surrounded by a box that can optionally have a label.
#
# Usage (example):
#
#    # Import
#
#    from tsWxRadioBox import RadioBox as wxRadioBox
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
#    2011/12/26 rsg Added logic to tsRadioBoxLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/21 rsg Modified tsOnLeftClick and ts_OnRadioButtonClick
#                   to invoke tsProcessEventTables.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event>.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxRadioBox'
__version__   = '1.3.0'
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

import tsWxGlobals as wx
from tsWxEvent import EVT_RADIOBOX
from tsWxEvent import EVT_RADIOBUTTON
from tsWxEvent import EVT_COMMAND_LEFT_CLICK # [Left Mouse]-Button Click
from tsWxControl import Control
from tsWxPoint import Point as wxPoint
from tsWxRadioButton import RadioButton as wxRadioButton
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class RadioBox(Control):
    '''
    A RadioBox is used to select one of a number of mutually exclusive
    choices. It is displayed as a vertical column or horizontal row of
    labelled buttons, surrounded by a box that can optionally have a
    label.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 choices=wx.PyEmptyStringArray,
                 majorDimension=0,
                 style=wx.RA_HORIZONTAL,
                 validator=wx.DefaultValidator,
                 name=wx.RadioBoxNameStr):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        # Also, remember that wx.RA_SPECIFY_COLS means that we arrange buttons
        # in left to right order and GetMajorDim() is the number of columns
        # while wx.RA_SPECIFY_ROWS means that the buttons are arranged top to
        # bottom and GetMajorDim() is the number of rows.
        theClass = 'RadioBox'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_choices = choices
        self.caller_majorDimension = majorDimension
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
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('            choices: %s' % choices)
            self.logger.debug('     majorDimension: %s' % majorDimension)
            self.logger.debug('              style: 0x%X' % style)
#            self.logger.debug('          validator: 0x%X' % validator)
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

        self.ts_Choices = choices
        self.ts_Count = len(choices)
        self.ts_Label = label
        self.ts_MajorDimension = max(majorDimension, self.ts_Count)
        self.ts_Style = style
        self.ts_Validator = validator

        myRect, myClientRect = self.tsRadioBoxLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        bestSize = self.tsBestSize()
##        style = 0

        self.ts_ItemLabel = []
        self.ts_ItemEnabled = []
        self.ts_ItemHelpText = []
        self.ts_ItemToolTip = []
        self.ts_ItemShown = []
        self.ts_ItemWindow = []

        # TBD - Verify scaling.
        if self.ts_Style & wx.RA_HORIZONTAL:
            itemWidth = bestSize.width // (self.ts_MajorDimension + 1)
        else:
            itemWidth = bestSize.width

        for item in range(self.ts_Count):
            self.ts_ItemLabel.append(self.ts_Choices[item])
            self.ts_ItemHelpText.append(self.ts_ItemLabel[item])
            self.ts_ItemToolTip.append(self.ts_ItemLabel[item])
            self.ts_ItemShown.append(True)

            if item == 0:
                self.ts_ItemEnabled.append(True)
            else:
                self.ts_ItemEnabled.append(False)

            # TBD - Under Construction.
            if self.ts_Style & wx.RA_HORIZONTAL:
                # Horizontal layout
                posTBD = wxPoint(
                    self.Rect.x + (item * itemWidth + 2) * wx.pixelWidthPerCharacter,
                    self.Rect.y + (2) * wx.pixelHeightPerCharacter)
            else:
                # Vertical layout
                posTBD = wxPoint(
                    self.Rect.x + (2) * wx.pixelWidthPerCharacter,
                    self.Rect.y + (item + 2) * wx.pixelHeightPerCharacter)

##            sizeTBD = wxSize(
##                (len('(*)  ') + len(
##                    self.ts_ItemLabel[item])) * wx.pixelWidthPerCharacter,
##                wx.pixelHeightPerCharacter)

            sizeTBD = wxSize(
                (len('(*)  ') + len(self.tsStripAcceleratorTextLabel(
                    self.ts_ItemLabel[item]))) * wx.pixelWidthPerCharacter,
                wx.pixelHeightPerCharacter)

            self.ts_ItemWindow.append(wxRadioButton(
                self,
                id=wx.ID_ANY,
                label=self.ts_ItemLabel[item],
                pos=posTBD,
                size=sizeTBD,
                style=(self.ts_Style & wx.ALIGN_LEFT | \
                       self.ts_Style & wx.ALIGN_RIGHT | \
                       wx.NO_BORDER),
                validator=wx.DefaultValidator,
                name=self.ts_ItemLabel[item]))

            self.ts_ItemWindow[item].SetValue(self.ts_ItemEnabled[item])

        if self.ts_Style & wx.RA_HORIZONTAL:
            self.ts_ColumnCount = self.ts_MajorDimension
            self.ts_RowCount = 1

        elif self.ts_Style & wx.RA_VERTICAL:
            self.ts_ColumnCount = 1
            self.ts_RowCount = self.ts_MajorDimension

        else:
            # TBD - Temporary dimension
            self.ts_ColumnCount = self.ts_MajorDimension
            rows, cols = divmod(self.ts_Count, self.ts_MajorDimension)
            if cols == 0:
                self.ts_RowCount = rows
            else:
                self.ts_RowCount = rows + 1

        self.ts_Selection = 0
        self.ts_StringSelection = 0

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        # Automatically Bind all Radio Button events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_RADIOBUTTON
        handler = self.tsOnRadioButtonClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=-1,
               label=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               validator=wx.DefaultValidator,
               name=wx.RadioBoxNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        if label == wx.EmptyString:
            # Prevent pylint warning.
            pass

        myRect, myClientRect = self.tsRadioBoxLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def EnableItem(self, n, enable=True):
        '''
        # def EnableItem(*args, **kwargs):
        EnableItem(self, unsigned int n, bool enable=True)
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemEnabled[n] = enable

    #-----------------------------------------------------------------------

    def FindString(self, s):
        '''
        '''
        n = -1
        for i in range(self.ts_Count):
            if s == self.ts_ItemLabel[i]:
                n = i
        return (n)

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
        pass

    #-----------------------------------------------------------------------

    def GetColumnCount(self):
        '''
        '''
        return (self.ts_ColumnCount)

    #-----------------------------------------------------------------------

    def GetCount(self):
        '''
        '''
        return (self.ts_Count)

    #-----------------------------------------------------------------------

    def GetItemHelpText(self, n):
        '''
        # def GetItemHelpText(*args, **kwargs):

        GetItemHelpText(self, unsigned int n) -> String
        '''
        assert -1 < n and n < self.ts_Count

        return (self.ts_ItemHelpText[n])

    #-----------------------------------------------------------------------

    def GetItemLabel(self, n):
        '''
        '''
        assert -1 < n and n < self.ts_Count

        return (self.ts_ItemLabel[n])

    #-----------------------------------------------------------------------

    def GetItemToolTip(self, n):
        '''
        # def GetItemToolTip(*args, **kwargs):

        GetItemToolTip(self, unsigned int item) -> ToolTip
        '''
        assert -1 < n and n < self.ts_Count

        return (self.ts_ItemToolTip[n])

    #-----------------------------------------------------------------------

    def GetNextItem(self, item, dir, style):
        '''
        '''
        if dir is None:
            # Prevent pylint warning.
            pass

        if style is None:
            # Prevent pylint warning.
            pass

        assert -1 < item and item < self.ts_Count

        oldItem = item
        newItem = (oldItem + 1) % self.ts_Count

        return (newItem)

    #-----------------------------------------------------------------------
 
    def GetRowCount(self):
        '''
        '''
        return (self.ts_RowCount)

    #-----------------------------------------------------------------------
 
    def GetSelection(self):
        '''
        '''
        return (self.ts_Selection)

    #-----------------------------------------------------------------------

    def GetString(self, n):
        '''
        '''
        assert -1 < n and n < self.ts_Count

        assert self.ts_ItemWindow[n].Label == self.ts_ItemLabel[n]

        return (self.ts_ItemLabel[n])

    #-----------------------------------------------------------------------

    def GetStringSelection(self):
        '''
        '''
        return (self.ts_ItemLabel[self.ts_Selection])

    #-----------------------------------------------------------------------

    def IsItemEnabled(self, n):
        '''
        # def IsItemEnabled(*args, **kwargs):
        IsItemEnabled(self, unsigned int n) -> bool
        '''
        assert -1 < n and n < self.ts_Count

        assert self.ts_ItemWindow[n].Value == self.ts_ItemEnabled[n]

        return (self.ts_ItemEnabled[n])

    #-----------------------------------------------------------------------

    def IsItemShown(self, n):
        '''
        # def IsItemShown(*args, **kwargs):
 
        IsItemShown(self, unsigned int n) -> bool
        '''
        assert -1 < n and n < self.ts_Count

        return (self.ts_ItemShown[n])

    #-----------------------------------------------------------------------

    def SetItemHelpText(self, n, helpText):
        '''
        # def SetItemHelpText(*args, **kwargs):
 
        SetItemHelpText(self, unsigned int n, String helpText)
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemHelpText[n] = helpText

    #-----------------------------------------------------------------------

    def SetItemLabel(self, n, label):
        '''
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemLabel[n] = label
        self.ts_ItemWindow[n].Label = label

    #-----------------------------------------------------------------------

    def SetItemToolTip(self, n, text):
        '''
        # def SetItemToolTip(*args, **kwargs):
        SetItemToolTip(self, unsigned int item, String text)
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemToolTip[n] = text

    #-----------------------------------------------------------------------

    def SetSelection(self, n):
        '''
        '''
        assert -1 < n and n < self.ts_Count

        for i in range(self.ts_Count):
            if i == n:
                self.ts_ItemEnabled[i] = True
                self.ts_Selection = i
            else:
                self.ts_ItemEnabled[i] = False
 
            self.ts_ItemWindow[i].SetValue(self.ts_ItemEnabled[i])

    #-----------------------------------------------------------------------

    def SetString(self, n, label):
        '''
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemLabel[n] = label
        self.ts_ItemWindow[n].Label = label

    #-----------------------------------------------------------------------

    def SetStringSelection(self, s):
        '''
        '''
        for n in range(self.ts_Count):
            if s == self.ts_ItemLabel[n]:
                self.SetSelection(n)
                status = True
                break
        else:
            status = False

        return (status)

    #-----------------------------------------------------------------------

    def ShowItem(self, n, show=True):
        '''
        # def ShowItem(*args, **kwargs):
        ShowItem(self, unsigned int n, bool show=True):
        '''
        assert -1 < n and n < self.ts_Count

        self.ts_ItemShown[n] = show
        self.ts_ItemWindow[n].Show()

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsBestSize(self):
        '''
        '''
        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=True)

        maxWidth = 0
        maxHeight = 0
        for choice in self.ts_Choices:
            buttonText = self.tsStripAcceleratorTextLabel(choice)
            if len(buttonText) > maxWidth:
                maxWidth = len(buttonText)
                maxHeight += 1
 
        if self.ts_Style & wx.RA_VERTICAL:
            # Vertical
            best = wxSize(
                (maxWidth * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (maxHeight * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))

        elif self.ts_Style & wx.RA_HORIZONTAL:
            # Horizontal
            best = wxSize(
                (maxWidth * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (maxHeight * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))

        else:
            # TBD - Should this be allowed?
            best = wxSize(
                (maxWidth * wx.pixelWidthPerCharacter + \
                 2 * borderThickness.width),
                (maxHeight * wx.pixelHeightPerCharacter + \
                 2 * borderThickness.height))
 

        return (best)

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        triggeringObject = self
 
        objectCriteria = 'EVT_COMMAND_LEFT_CLICK for ' + \
                         '[%s]-Button' % self.GetLabel()
        triggeringEvent = EVT_COMMAND_LEFT_CLICK

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=triggeringObject.ts_AssignedId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsOnRadioButtonClick(self, evt):
        '''
        '''
##        for selection in self.ts_Choices:
##            if selection is None:
##                selection.SetValue(wx.CHK_CHECKED)
##            else:
##                selection.SetValue(wx.CHK_UNCHECKED)

##            selection.tsCreateRadioButton()
##            selection.tsShow()
 
        triggeringObject = self
 
        objectCriteria = 'EVT_RADIOBOX for [%s]-Button' % self.GetLabel()
        triggeringEvent = EVT_RADIOBOX

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=triggeringObject.ts_AssignedId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsRadioBoxLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of RadioBox based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)
 
        if style is None:
            # Prevent pylint warning.
            pass

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        theBestSize = self.tsBestSize()

        if theSize == theDefaultSize:
            # theDefaultSize

            theBoxSize = theBestSize

            if thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theBoxSize.width,
                                theBoxSize.height)

            else:
                # Not theDefaultPosition

                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theBoxSize.width,
                                theBoxSize.height)

        else:
            # Not theDefaultSize

            if thePosition == theDefaultPosition:
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
              'name="%s"; myRect=%s'
        msg = fmt % (parent, str(pos), str(size), name, str(myRect))

        self.logger.debug('    tsRadioBoxLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update RadioBox specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            label=self.ts_Label,
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
        Draw the actual features of the Box.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            self.tsCreateBorder()
            self.tsCreateTitleLine(self.ts_Label)
            for index in range(self.ts_Count):
                self.ts_ItemWindow[index].tsUpdate()
    ##        self.tsCreateRadioBox()

    #-----------------------------------------------------------------------

##    def tsCreateRadioBox(self, n):
##        '''
##        '''
##        if self.ts_Value == wx.CHK_UNCHECKED:
##            checkMark = ' '
##        else:
##            checkMark = '*'

##        row = 0
##        col = 0
##        maxCols = (self.Rect.width // wx.pixelWidthPerCharacter) - col - 1
##        minCols = len(self.ts_Label) + len('[ ]')
##        if self.ts_Style & wx.ALIGN_RIGHT:
##            # Align Right
##            if minCols <= maxCols:
##                fill = ' ' * (maxCols - minCols - 2)
##                string = '%s%s (%s)' % (fill, self.ts_Label, checkMark)
##            else:
##                string = '%s (%s)' % (self.ts_Label,
##                                      checkMark)
##        else:
##            # Align Left
##            if minCols <= maxCols:
##                fill = ' ' * (maxCols - minCols)
##                string = '(%s) %s%s' % (checkMark, self.ts_Label, fill)
##            else:
##                string = '(%s) %s' % (checkMark,
##                                      self.ts_Label)

##        self.tsCursesAddStr(
##            col, row, string[0:maxCols], attr=None, pixels=False)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ColumnCount = property(GetColumnCount)
    Count = property(GetCount)
    RowCount = property(GetRowCount)
    Selection = property(GetSelection, SetSelection)
    StringSelection = property(GetStringSelection, SetStringSelection)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
