#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:43:50 AM rsg>"
'''
tsWxRadioButton.py - Class to establish a radio button that is a
labelled box which by default is either on (the checkmark is
visible) or off (no checkmark).
'''
#################################################################
#
# File: tsWxRadioButton.py
#
# Purpose:
#
#    Class to establish a radio button that is a labelled box
#    which by default is either on (the checkmark is visible) or
#    off (no checkmark).
#
# Usage (example):
#
#    # Import
#
#    from tsWxRadioButton import RadioButton
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Modifications:
#
#    2010/07/16 rsg Modified tsCreateRadioButton to support
#                   use of "&" to designate accelerator
#                   character.
#
#    2010/08/31 rsg For consistancy with wxPython and industry
#                   conventions, changed characterCellAccelerator
#                   to "tsGTUI.DISPLAY_UNDERLINE"
#                   from "tsGTUI.DISPLAY_BOLD".
#
#    2011/12/26 rsg Added logic to tsRadioButtonLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/21 rsg Modified tsOnLeftClick to invoke
#                   tsProcessEventTables.
#
#    2012/03/24 rsg Modified tsUpdate to inhibit self.tsCreateBorder()
#                   because it caused border artifacts event when
#                   there was no border around radio button.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to each tsOn<event>.
#
# ToDo:
#
#    2012/03/24 rsg Troubleshoot tsCreateRadioButton for right
#                   aligned.
#
#################################################################

__title__     = 'tsWxRadioButton'
__version__   = '1.2.1'
__date__      = '04/01/2013'
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
import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxEvent import EVT_RADIOBUTTON
from tsWxEvent import EVT_COMMAND_LEFT_CLICK # [Left Mouse]-Button Click
from tsWxControl import Control
from tsWxPoint import Point as wxPoint
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

class RadioButton(Control):
    '''
    A radio button is a labelled box which by default is either on (the
    checkmark is visible) or off (no checkmark).

    Window Styles

    wx.CHK_2STATE       Create a 2-state radio button.

    wx.ALIGN_LEFT Makes the text appear on the right of the radio button.

    wx.ALIGN_RIGHT Makes the text appear on the left of the radio button.

    Events

    EVT_RADIOBUTTON     Sent when radio button is clicked.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.RadioButtonNameStr):
        '''
        '''
        theClass = 'RadioButton'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
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
            self.logger.debug('              label: %s' % label)
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

        self.ts_Style = (style & wx.ALIGN_LEFT) | (style & wx.ALIGN_RIGHT)

        self.ts_Label = label
        self.ts_ButtonText = self.tsStripAcceleratorTextLabel(label)

        self.ts_Validator = validator
        self.ts_Value = wx.CHK_UNCHECKED

        myRect, myClientRect = self.tsRadioButtonLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
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
               name=wx.RadioButtonNameStr,
               pixels=True):
        '''
        Actually create the GUI RadioButton for 2-phase creation.
        '''
        if label == wx.EmptyString:
            # Prevent pylint warning.
            pass

        myRect, myClientRect = self.tsRadioButtonLayout(
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
        pass

    #-----------------------------------------------------------------------

    def GetValue(self):
        '''
        Gets the state of a 2-state RadioButton.

        Returns wx.CHK_UNCHECKED when the RadioButton is unchecked and
        wx.CHK_CHECKED when it is checked.
        '''
        return (self.ts_Value != wx.CHK_UNCHECKED)

    #-----------------------------------------------------------------------

    def SetValue(self, state):
        '''
        Set the state of a 2-state RadioButton.
        '''
        if state:

            self.ts_Value = wx.CHK_CHECKED

        else:

            self.ts_Value = wx.CHK_UNCHECKED

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsRadioButtonLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
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


        label = self.ts_ButtonText

        if theSize == theDefaultSize:
            # theDefaultSize
##            print('default size layout label="%s"; pos=%s size=%s' % (
##                label, pos, size))

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            maxWidth = self.ts_Parent.ts_ClientRect.width - (
                2 * wx.pixelWidthPerCharacter)

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(maxWidth, wx.pixelHeightPerCharacter)

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
##            print('not default size layout label="%s"; pos=%s size=%s' % (
##                label, pos, size))

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

        self.logger.debug('    tsRadioButtonLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Button specific native GUI.
        '''
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
        Draw the actual features of the Button.
        '''
        self.tsCursesScrollOk(0)
        self.tsCursesBkgd()
        # self.tsCreateBorder()
        self.tsCreateRadioButton()

    #-----------------------------------------------------------------------

    def tsCreateRadioButton(self):
        '''
        '''
        if self.ts_Value == wx.CHK_CHECKED:
            checkMark = '*'
        else:
            checkMark = ' '

        useAccelerator = True
        if useAccelerator:
            characterCellAttribute = tsGTUI.DISPLAY_STANDOUT
            characterCellAccelerator = tsGTUI.DISPLAY_UNDERLINE
        else:
            characterCellAttribute = tsGTUI.DISPLAY_NORMAL
            characterCellAccelerator = characterCellAttribute

        window =  self

        text = self.ts_ButtonText.strip()
        print('tsWxRadioButton: text="%s"' % text)

        (prefix,
         character,
         suffix,
         flags) = self.tsParseAcceleratorTextLabel(self.ts_Label)

        aLine = prefix.strip() + character.strip() + suffix.strip()
        print('tsWxRadioButton: aLine="%s"' % aLine)

        if flags is None:
            # Prevent pylint warning.
            pass

        # window.attron(characterCellAttribute)

        row = 0
        col = 0
        # TBD - Truncate to leave space for cursor beyond last character
        truncate = 1
        maxCols = (self.Rect.width // wx.pixelWidthPerCharacter) - truncate
        minCols = len(text) + len('( )') + truncate

        if useAccelerator:

            # Display Accelerator Style Text

            if self.ts_Style & wx.ALIGN_RIGHT:

                # Align Right

                if minCols <= maxCols:

                    # Pad short test

                    fill = ' ' * (maxCols - minCols)

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '%s%s' % (fill, prefix),
                        attr=None,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + len(fill) + len(prefix),
                        int(row),
                        '%s' % character,
                        attr=characterCellAccelerator,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + (
                            len(fill)) + len(prefix) + len(character),
                        int(row),
                        '%s (%s)' % (suffix, checkMark),
                        attr=None,
                        pixels=False)

                else:

                    # Truncate long text

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '%s' % prefix,
                        attr=None,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + len(prefix),
                        int(row),
                        '%s' % character,
                        attr=characterCellAccelerator,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + len(prefix) + len(character),
                        int(row),
                        '%s (%s)' % (suffix, checkMark),
                        attr=None,
                        pixels=False)

            else:

                # Align Left

                if minCols <= maxCols:

                    # Pad short text

                    fill = ' ' * (maxCols - minCols)

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '(%s) %s' % (checkMark, prefix),
                        attr=None,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + len(checkMark) + len(prefix) + 3,
                        int(row),
                        '%s' % character,
                        attr=characterCellAccelerator,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + (
                            len(checkMark) + len(prefix) + 3) + len(character),
                        int(row),
                        '%s%s' % (suffix, fill[0:len(fill) - truncate]),
                        attr=None,
                        pixels=False)

                else:

                    # Truncate long text

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '(%s) %s' % (checkMark, prefix),
                        attr=None,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + len(checkMark) + len(prefix) + 3,
                        int(row),
                        '%s' % character,
                        attr=characterCellAccelerator,
                        pixels=False)

                    window.tsCursesAddStr(
                        int(col) + (
                            len(checkMark) + len(prefix) + 3) + len(character),
                        int(row),
                        '%s' % suffix[0:len(suffix) - truncate],
                        attr=None,
                        pixels=False)

        else:

            # Display Non-Accelerator Style Text

            if self.ts_Style & wx.ALIGN_RIGHT:

                # Align Right
                if minCols <= maxCols:

                    # Pad short text

                    fill = ' ' * (maxCols - minCols - truncate)

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '%s %s (%s)' % (fill, aLine, checkMark),
                        attr=None,
                        pixels=False)

                else:

                    # Truncate long text

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        '%s (%s)' % (aLine, checkMark),
                        attr=None,
                        pixels=False)

            else:

                # Align Left

                if minCols <= maxCols:

                    # Pad short text

                    fill = ' ' * (maxCols - minCols - truncate)
                    buffer = '(%s) %s %s' % (checkMark,
                                             aLine[0:len(aLine)],
                                             fill)

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        buffer,
                        attr=None,
                        pixels=False)

                else:

                    # Truncate long text

                    buffer = '(%s) %s' % (checkMark,
                                          aLine[0:len(aLine)])

                    window.tsCursesAddStr(
                        int(col),
                        int(row),
                        buffer,
                        attr=wx.DISPLAY_NORMAL,
                        pixels=False)

##        self.tsCursesAddStr(
##            col, row, string[0:maxCols], attr=None, pixels=False)

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        parent = self.ts_Parent
        siblings = parent.ts_Children
        for sibling in siblings:

            if sibling == self:

                self.SetValue(wx.CHK_CHECKED)

                self.tsCreateRadioButton()
                self.tsShow()

            else:

                sibling.SetValue(wx.CHK_UNCHECKED)

                sibling.tsCreateRadioButton()
                sibling.tsShow()

        triggeringObject = self
        objectId = triggeringObject.ts_AssignedId
 
        objectCriteria = 'EVT_RADIOBUTTON for [%s]-Button' % self.GetLabel()
        triggeringEvent = EVT_RADIOBUTTON

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Value = property(GetValue, SetValue)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
