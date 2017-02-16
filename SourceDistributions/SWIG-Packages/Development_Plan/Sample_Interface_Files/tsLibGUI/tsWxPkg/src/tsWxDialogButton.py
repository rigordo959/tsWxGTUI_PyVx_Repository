#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:30:01 AM rsg>"
'''
tsWxDialogButton.py - Class to establish a button that
controls the closing, help, iconizing, maximizing and restoring
the previous size of a Dialog type window.
'''
#################################################################
#
# File: tsWxDialogButton.py
#
# Purpose:
#
#     Class to establish a button that controls the closing,
#     help, iconizing, maximizing and restoring the previous size
#     of a Dialog type window.
#
# Usage (example):
#
#    # Import
#
#    from tsWxDialogButton import TopLevelWindowButton
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
#    2011/12/26 rsg Added logic to tsButtonLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/21 rsg Modified tsOnLeftClick to invoke
#                   tsProcessEventTable.
#
#    2012/03/09 rsg Added missing objectId assignment to
#                   tsOnLeftClick.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to tsOnLeftClick.
#
#    2013/07/06 rsg Modified tsOnLeftClick to disable logic for
#                   mapping EVT_COMMAND_LEFT_CLICK into:
#
#                   EVT_CLOSE       # [X]-Button Click (Dialog)
#                   EVT_HELP        # [?]-Button Click (Dialog)
#                   EVT_ICONIZE     # [_]-Button Click (Dialog)
#                   EVT_MAXIMIZE    # [Z]-Button Click (Dialog)
#                   EVT_RESTOREDOWN # [z]-Button Click (Dialog)
#
#                   Also, disabled imports of unused events.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxDialogButton'
__version__   = '1.5.0'
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
import curses.panel

import tsWxGlobals as wx
##from tsWxEvent import EVT_CLOSE              # [X]-Button Click (Dialog)
##from tsWxEvent import EVT_HELP               # [?]-Button Click (Dialog)
##from tsWxEvent import EVT_ICONIZE            # [_]-Button Click (Dialog)
##from tsWxEvent import EVT_MAXIMIZE           # [Z]-Button Click (Dialog)
##from tsWxEvent import EVT_RESTOREDOWN        # [z]-Button Click (Dialog)
from tsWxEvent import EVT_COMMAND_LEFT_CLICK # [Left Mouse]-Button Click
from tsWxButton import Button
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

ButtonBar              = wx.ThemeToUse['Dialog']['ButtonBarDefault']
CloseButtonLabel       = wx.ThemeToUse['Dialog']['CloseButtonLabel']
HelpButtonLabel        = wx.ThemeToUse['Dialog']['HelpButtonLabel']
IconizeButtonLabel     = wx.ThemeToUse['Dialog']['IconizeButtonLabel']
MaximizeButtonLabel    = wx.ThemeToUse['Dialog']['MaximizeButtonLabel']
RestoreDownButtonLabel = wx.ThemeToUse['Dialog']['RestoreDownButtonLabel']

#---------------------------------------------------------------------------

class DialogButton(Button):
    '''
    Class to establish a button that controls the closing, help,
    iconizing, maximizing and restoring the previous size of a
    Dialog type window.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.DialogButtonNameStr,
                 useClientArea=True):
        '''
        Create and show a button. The preferred way to create standard buttons
        is to use a standard ID and an empty label. In this case wxWigets will
        automatically use a stock label that corresponds to the ID given.
        These labels may vary across platforms as the platform itself will
        provide the label if possible. In addition, the button will be
        decorated with stock icons under GTK+ 2.
        '''
        theClass = 'DialogButton'

        wx.RegisterFirstCallerClassName(self, theClass)

        Button.__init__(self,
                        parent=parent,
                        id=id,
                        label=label,
                        pos=pos,
                        size=size,
                        style=style,
                        validator=validator,
                        name=name,
                        useClientArea=useClientArea)

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

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
            # Inter-button spaces have same color as parent background.
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_Label = label
        self.ts_ButtonText = self.tsStripAcceleratorTextLabel(label)

        self.ts_UseClientArea = useClientArea
        self.ts_Validator = validator

        (myRect, myClientRect) = self.tsButtonLayout(
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
    # Begin tsWx API Extensions

    def tsButtonLayout(self, parent, pos, size, style, name):
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

        # Ignore UseClientArea because cursor wraps beyond bottom
        # when last character has been output.
        if self.ts_UseClientArea:
            offset = wxPoint(0, 0)
        else:
            offset = wxPoint(0, 0)

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

            if thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theLabelSize.width,
                                theLabelSize.height)

            else:
                # Not theDefaultPosition

                myRect = wxRect(offset.x + thePosition.x,
                                offset.y + thePosition.y,
                                theLabelSize.width,
                                theLabelSize.height)

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

                myRect = wxRect(offset.x + thePosition.x,
                                offset.y + thePosition.y,
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

        self.logger.debug('    tsButtonLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsOnClose(self, evt):
        '''
        '''
        theEarliestAncestor = self.tsFindWindowByAssignedId(
            self.ts_EarliestAncestor)
        theEarliestAncestor.Closed = True
        print('%s: Closed=%s' % (self.ts_EarliestAncestor,
                                 theEarliestAncestor.Closed))
        theEarliestAncestor.ts_PanelLayer.hide()
        self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsOnHelp(self, evt):
        '''
        '''
##      self.tsCursesDoUpdate()
        if self.ts_BackgroundColour == wx.COLOR_BLUE:
            self.ts_BackgroundColour = wx.COLOR_YELLOW
        elif self.ts_BackgroundColour == wx.COLOR_YELLOW:
            self.ts_BackgroundColour = wx.COLOR_MAGENTA
        elif self.ts_BackgroundColour == wx.COLOR_MAGENTA:
            self.ts_BackgroundColour = wx.COLOR_GREEN
        elif self.ts_BackgroundColour == wx.COLOR_GREEN:
            self.ts_BackgroundColour = wx.COLOR_RED
        elif self.ts_BackgroundColour == wx.COLOR_RED:
            self.ts_BackgroundColour = wx.COLOR_BLACK
        else:
            self.ts_BackgroundColour = wx.COLOR_BLUE
        self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsOnIconize(self, evt):
        '''
        '''
        def hideChildren(self, parent):
            '''
            '''
            for child in parent.ts_Children:
                self.hideChildren(child)
                child.ts_PanelLayer.hide()

        theEarliestAncestor = self.tsFindWindowByAssignedId(
            self.ts_EarliestAncestor)
        print('%s: Iconized=%s' % (self.ts_EarliestAncestor,
                                   theEarliestAncestor.Closed))
        theEarliestAncestor.ts_PanelLayer.hide()
        theEarliestAncestor.Iconized = True
        self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsOnMaximize(self, evt):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def tsOnRestoreDown(self, evt):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def tsOnUnknown(self, evt):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        theLabel = self.GetLabel()
        print('NOTICE: %s: received "%s" from "%s"' %
              ('tsWxDialogButton',
               str(EVT_COMMAND_LEFT_CLICK),
               '[%s]-Button' % theLabel))

        if theLabel == CloseButtonLabel:   

            self.tsOnClose(evt)

        elif theLabel == HelpButtonLabel:

            self.tsOnHelp(evt)

        elif theLabel == IconizeButtonLabel:

            self.tsOnIconize(evt)

        elif theLabel == MaximizeButtonLabel:

            self.tsOnMaximize(evt)

        elif theLabel == RestoreDownButtonLabel:

            self.tsOnRestoreDown(evt)

        else:

            self.tsOnUnknown(evt)

        theEarliestAncestor = self.tsFindWindowByAssignedId(
            self.ts_EarliestAncestor)
        theEarliestAncestor.ts_PanelLayer.hide()
##      self.tsCursesDoUpdate()
##      if self.ts_BackgroundColour == wx.COLOR_BLUE:
##          self.ts_BackgroundColour = wx.COLOR_YELLOW
##      elif self.ts_BackgroundColour == wx.COLOR_YELLOW:
##          self.ts_BackgroundColour = wx.COLOR_MAGENTA
##      elif self.ts_BackgroundColour == wx.COLOR_MAGENTA:
##          self.ts_BackgroundColour = wx.COLOR_GREEN
##      elif self.ts_BackgroundColour == wx.COLOR_GREEN:
##          self.ts_BackgroundColour = wx.COLOR_RED
##      elif self.ts_BackgroundColour == wx.COLOR_RED:
##          self.ts_BackgroundColour = wx.COLOR_BLACK
##      else:
##          self.ts_BackgroundColour = wx.COLOR_BLUE
        self.tsUpdate()

        return (True)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'EVT_COMMAND_LEFT_CLICK for ' + \
##                         '[%s]-Button' % self.GetLabel()
##        triggeringEvent = EVT_COMMAND_LEFT_CLICK
        
##        if self.GetLabel().find('CloseButton') > -1:

##            objectCriteria = 'EVT_CLOSE for [X]-Button'
##            triggeringEvent = EVT_CLOSE

##        elif self.GetLabel().find('HelpButton') > -1:

##            objectCriteria = 'EVT_HELP for [?]-Button'
##            triggeringEvent = EVT_HELP

##        elif self.GetLabel().find('MaximizeButton') > -1:

##            objectCriteria = 'EVT_MAXIMIZE for [Z]-Button'
##            triggeringEvent = EVT_MAXIMIZE

##        elif self.GetLabel().find('IconizeButton') > -1:

##            objectCriteria = 'EVT_ICONIZE for [_]-Button'
##            triggeringEvent = EVT_ICONIZE

##        elif self.GetLabel().find('RestoreDownButton') > -1:

##            objectCriteria = 'EVT_RESTOREDOWN for [z]-Button'
##            triggeringEvent = EVT_RESTOREDOWN

##        else:

##            objectCriteria = 'EVT_COMMAND_LEFT_CLICK for ' + \
##                             '[%s]-Button' % self.GetLabel()
##            triggeringEvent = EVT_COMMAND_LEFT_CLICK

####        triggeringObject.ProcessEvent(triggeringEvent)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

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
            except Exception, e:
                self.logger.error('%s.tsShow; %s' % (__title__, e))

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
            self.tsCreateButton()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
