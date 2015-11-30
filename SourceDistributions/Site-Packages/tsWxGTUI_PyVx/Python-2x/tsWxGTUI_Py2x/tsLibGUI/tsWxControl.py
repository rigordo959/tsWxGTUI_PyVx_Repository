#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:37:00 AM rsg>"
'''
tsWxControl.py - Base Class for a control or "widget".
A control is generally a small window which processes user
input and/or displays one or more item of data.
'''
#################################################################
#
# File: tsWxControl.py
#
# Purpose:
#
#    Base Class for a control or "widget". A control is
#    generally a small window which processes user
#    input and/or displays one or more item of data.
#
# Usage (example):
#
#    # Import
#
#    from tsWxControl import Control
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
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxControl'
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

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxWindow import Window

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class Control(Window):
    '''
    This is the base class for a control or 'widget'.

    A control is generally a small window which processes user input and/or
    displays one or more item of data.
    '''
    def __init__(self,
                 parent,
                 id=-1,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.ControlNameStr):
        '''
        Default class constructor.
        '''
        theClass = 'Control'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
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

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        self.ts_Rect = wxRect(
            thePosition.x, thePosition.y, theSize.width, theSize.height)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('                pos: %s' % self.Position)
            self.logger.debug('               size: %s' % self.Size)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('          validator: %s' % validator)
            self.logger.debug('               name: %s' % name)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        self.ts_Validator = validator

        # Facilitate differentiation of this panel from its parent by
        # transposing the parent's foreground and background colors.
        self.ts_BackgroundColour = wx.ThemeToUse[
            'ForegroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse[
            'BackgroundColour'].lower()

        self.ts_Style = style

        self.tsEndClassRegistration(theClass)

    def Command(self, event):
        '''
        Simulates the effect of the user issuing a command to the item.
        '''
        self.logger.debug(
            '      Command Event (Unimplemented): %s.' % event)
 
    def Create(self,
               parent,
               id=-1,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               validator=wx.DefaultValidator,
               name=wx.ControlNameStr,
               pixels=True):
        '''
        Do the 2nd phase and create the GUI control.
        '''
        myRect = self.tsGetRectangle(pos, size)

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    def GetAlignment(self):
        '''
        Get the control alignment (left/right/centre, top/bottom/centre)
        '''
        alignmentMask = wx.ALIGN_BOTTOM or \
                        wx.ALIGN_CENTER_HORIZONTAL or \
                        wx.ALIGN_CENTER_VERTICAL or \
                        wx.ALIGN_LEFT or \
                        wx.ALIGN_MASK or \
                        wx.ALIGN_NOT or \
                        wx.ALIGN_RIGHT or \
                        wx.ALIGN_TOP or \
                        wx.ALIGN_CENTER

        return (self.ts_Style & alignmentMask)

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class.
        '''
        return (wx.WINDOW_VARIANT_NORMAL)

    def GetLabelText(self):
        '''
        Get just the text of the label, without mnemonic characters ("&")
        '''
        return (self.ts_Name.replace('&', ''))

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsUpdate(self):
        '''
        Draw the actual features of the Control.
        '''
        if self.tsIsShowPermitted:

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s.tsUpdate; %s' % (__title__, e))

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd(' ', attr=None)
            self.tsCreateBorder()
            self.tsCursesAddStr(
                1, 0, ' %s ' % self.GetLabel(), attr=None, pixels=False)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Alignment = property(GetAlignment)
    LabelText = property(GetLabelText)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
