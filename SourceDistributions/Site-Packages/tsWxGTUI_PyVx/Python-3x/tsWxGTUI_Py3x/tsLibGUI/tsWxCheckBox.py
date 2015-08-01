#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:32:20 AM rsg>"
'''
tsWxCheckBox.py - Class to establish a checkbox which is a
labelled box that by default is either on (the checkmark
is visible) or off (no checkmark). Optionally (When the
wx.CHK_3STATE style flag is set) it can have a third state,
called the mixed or undetermined state. Often this is used
as a "Does Not Apply" state.
'''
#################################################################
#
# File: tsWxCheckBox.py
#
# Purpose:
#
#    Class to establish a checkbox which is a labelled box that
#    by default is either on (the checkmark is visible) or off
#    (no checkmark). Optionally (When the wx.CHK_3STATE style
#    flag is set) it can have a third state, called the mixed
#    or undetermined state. Often this is used as a "Does Not
#    Apply" state.
#
# Usage (example):
#
#    # Import
#
#    from tsWxCheckBox import CheckBox
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
#    2010/07/16 rsg - Modified tsCreateCheckBox to support
#                     use of "&" to designate accelerator
#
#    2010/08/31 rsg - For consistancy with wxPython and industry
#                     conventions, changed characterCellAccelerator
#                     to "tsGTUI.DISPLAY_UNDERLINE"
#                     from "tsGTUI.DISPLAY_BOLD".
#
#    2011/12/26 rsg Added logic to tsCheckBoxLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/21 rsg Modified tsOnLeftClick to invoke
#                   tsProcessEventTables.
#
#    2012/03/21 rsg Modified tsCreateCheckBox to replace erroneous
#                   parentheses "()" by brackets "[]"..
#
#    2012/03/24 rsg Modified tsUpdate to inhibit self.tsCreateBorder()
#                   because it caused border artifacts event when
#                   there was no border around checkbox.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to tsOnLeftClick.
#
# ToDo:
#
#    Validate tsCreateCheckBox for truncated right justified
#    case.
#
#################################################################

__title__     = 'tsWxCheckBox'
__version__   = '1.4.0'
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

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI

from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import *
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

class CheckBox(Control):
    '''
    A checkbox is a labelled box which by default is either on (the checkmark
    is visible) or off (no checkmark). Optionally (When the wx.CHK_3STATE
    style flag is set) it can have a third state, called the mixed or
    undetermined state. Often this is used as a "Does Not Apply" state.

    Window Styles

    wx.CHK_2STATE       Create a 2-state checkbox. This is the default.

    wx.CHK_3STATE       Create a 3-state checkbox.

    wx.CHK_ALLOW_3RD_STATE_FOR_USER     By default a user cannot set a 3-state
    checkbox to the third state. It can only be done from code. Using this
    flags allows the user to set the checkbox to the third state by clicking.

    wx.ALIGN_RIGHT Makes the text appear on the left of the checkbox.

    Events

    EVT_CHECKBOX        Sent when checkbox is clicked.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.CheckBoxNameStr):
        '''
        '''
        theClass = 'CheckBox'

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

        self.ts_Style = style

        self.ts_Label = label
        self.ts_ButtonText = self.tsStripAcceleratorTextLabel(label)

        self.ts_Validator = validator
        self.ts_Value = wx.CHK_UNCHECKED

        myRect, myClientRect = self.tsCheckBoxLayout(
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
               name=wx.CheckBoxNameStr,
               pixels=True):
        '''
        Actually create the GUI CheckBox for 2-phase creation.
        '''
        if label == wx.EmptyString:
            # Prevent pylint warning.
            pass

        myRect, myClientRect = self.tsCheckBoxLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def Get3StateValue(self):
        '''
        Returns wx.CHK_UNCHECKED when the CheckBox is unchecked,
        wx.CHK_CHECKED when it is checked and wx.CHK_UNDETERMINED
        when it is in the undetermined state.
        '''
        return (self.ts_Value)

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
        Gets the state of a 2-state CheckBox.

        Returns wx.CHK_UNCHECKED when the CheckBox is unchecked and
        wx.CHK_CHECKED when it is checked.
        '''
        return (self.Get3StateValue() != wx.CHK_UNCHECKED)

    #-----------------------------------------------------------------------

    def Is3rdStateAllowedForUser(self):
        '''
        Returns whether or not the user can set the CheckBox to the third
        state.
        '''
        return (self.ts_Style & wx.CHK_ALLOW_3RD_STATE_FOR_USER)

    #-----------------------------------------------------------------------
 
    def Is3State(self):
        '''
        Returns whether or not the CheckBox is a 3-state CheckBox.
        '''
        return (self.ts_Style & wx.CHK_3STATE)

    #-----------------------------------------------------------------------
 
    def IsChecked(self):
        '''
        Similar to GetValue, but raises an exception if it is not a 2-state
        CheckBox.
        '''
        if self.ts_Style & wx.CHK_2STATE:
            # Is 2-state CheckBox
            return (self.GetValue())
        else:
            # is 3-state CheckBox
            msg = 'Needs to be a 2-state CheckBox: %s' % \
                  'IsChecked in tsWxCheckBox'
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Set3StateValue(self, state):
        '''
        Sets the CheckBox to the given state.
        '''
        if self.ts_Style & wx.CHK_3STATE or \
           self.ts_Style & wx.CHK_ALLOW_3RD_STATE_FOR_USER:

            # 3-state CheckBox
            if state == wx.CHK_UNCHECKED:

                self.ts_Value = wx.CHK_UNCHECKED

            elif state == wx.CHK_CHECKED:

                self.ts_Value = wx.CHK_CHECKED

            else:

                self.ts_Value = wx.CHK_UNDETERMINED

        else:

            # 2-state CheckBox
            if state == wx.CHK_UNCHECKED:

                self.ts_Value = wx.CHK_UNCHECKED

            else:

                self.ts_Value = wx.CHK_CHECKED

    #-----------------------------------------------------------------------

    def SetValue(self, state):
        '''
        Set the state of a 2-state CheckBox.
        '''
        if state:

            self.ts_Value = wx.CHK_CHECKED

        else:

            self.ts_Value = wx.CHK_UNCHECKED

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsCheckBoxLayout(self, parent, pos, size, style, name):
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

        self.logger.debug('    tsCheckBoxLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        if self.Is3State() and \
           self.Is3rdStateAllowedForUser():

            # 3-state CheckBox
            if self.Get3StateValue() == wx.CHK_UNCHECKED:

                self.Set3StateValue(wx.CHK_CHECKED)

            elif self.Get3StateValue() == wx.CHK_CHECKED:

                self.Set3StateValue(wx.CHK_UNDETERMINED)

            else:

                self.Set3StateValue(wx.CHK_UNCHECKED)

        else:

            # 2-state CheckBox
            if self.GetValue() == wx.CHK_UNCHECKED:

                self.SetValue(wx.CHK_CHECKED)

            else:

                self.SetValue(wx.CHK_UNCHECKED)

        self.tsCreateCheckBox()
        self.tsShow()

        triggeringObject = self
        objectId = triggeringObject.ts_AssignedId

        objectCriteria = 'EVT_CHECKBOX for [%s]-Button' % self.GetLabel()
        triggeringEvent = EVT_CHECKBOX

##        triggeringObject.ProcessEvent(triggeringEvent)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Button specific native GUI.
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
        Draw the actual features of the Button.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            # self.tsCreateBorder()
            self.tsCreateCheckBox()

    #-----------------------------------------------------------------------

    def tsCreateCheckBox(self):
        '''
        '''
        if self.ts_Value == wx.CHK_UNCHECKED:
            checkMark = ' '
        elif self.ts_Value == wx.CHK_CHECKED:
            checkMark = 'X'
        else:
            checkMark = '-'

        useAccelerator = True
        if useAccelerator:
            characterCellAttribute = tsGTUI.DISPLAY_STANDOUT
            characterCellAccelerator = tsGTUI.DISPLAY_UNDERLINE
        else:
            characterCellAttribute = tsGTUI.DISPLAY_NORMAL
            characterCellAccelerator = characterCellAttribute

        window =  self

        text = self.ts_ButtonText

        (prefix,
         character,
         suffix,
         flags) = self.tsParseAcceleratorTextLabel(self.ts_Label)

        if flags is None:
            # Prevent pylint warning.
            pass

        aLine = prefix + character + suffix

        if aLine is None:
            # Prevent pylint warning.
            pass

        row = 0
        col = 0
        # TBD - Truncate to leave space for cursor beyond last character
        truncate = 1
        maxCols = (self.Rect.width // wx.pixelWidthPerCharacter) - \
                  col - truncate
        minCols = len(text) + len('[ ]')
        if self.ts_Style & wx.ALIGN_RIGHT:

            # Align Right
            if minCols <= maxCols:
                fill = ' ' * (maxCols - minCols - 2)
##                string = '%s%s [%s]' % (fill, text, checkMark)
##                print('%s; ("%s"; "%s"; "%s"' % \
##                      (string, prefix, character, suffix))

                window.tsCursesAddStr(
                    int(col),
                    int(row),
                    '%s%s' % (fill[0:len(fill)], prefix),
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
                    '%s [%s]' % (suffix, checkMark),
                    attr=None,
                    pixels=False)

            else:
##                string = '%s [%s]' % (text, checkMark)
##                print('%s; ("%s"; "%s"; "%s"' % \
##                      (string, prefix, character, suffix))

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
                    '%s [%s]' % (suffix, checkMark),
                    attr=None,
                    pixels=False)

        else:
            # Align Left
            if minCols <= maxCols:
                fill = ' ' * (maxCols - minCols)
##                string = '[%s] %s%s' % (checkMark, text, fill)
##                print('%s; ("%s"; "%s"; "%s"' % \
##                      (string, prefix, character, suffix))

                window.tsCursesAddStr(
                    int(col),
                    int(row),
                    '[%s] %s' % (checkMark, prefix),
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
##                string = '[%s] %s' % (checkMark, text)
##                print('%s; ("%s"; "%s"; "%s"' % \
##                      (string, prefix, character, suffix))

                window.tsCursesAddStr(
                    int(col),
                    int(row),
                    '[%s] %s' % (checkMark, prefix),
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

##        self.tsCursesAddStr(
##            col, row, string[0:maxCols], attr=None, pixels=False)
 
    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ThreeStateValue = property(Get3StateValue, Set3StateValue)
    Value = property(GetValue, SetValue)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
