#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:37:16 AM rsg>"
'''
tsWxControlWithItems.py - Convenience Class that derives from
both wxControl and wxItemContainer. It is used as basis for
some controls (wxChoice and wxListBox).
'''
#################################################################
#
# File: tsWxControlWithItems.py
#
# Purpose:
#
#    Convenience Class that derives from both wxControl and
#    wxItemContainer. It is used as basis for some controls
#    (wxChoice and wxListBox).
#
# Usage (example):
#
#    # Import
#
#    from tsWxControlWithItems import ControlWithItems as wxControlWithItems
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

__title__     = 'tsWxControlWithItems'
__version__   = '0.1.0'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py3x.tsLibGUI.tsWxItemContainer import ItemContainer

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class ControlWithItems(Control, ItemContainer):
    '''
    wx.ControlWithItems combines the wx.ItemContainer class with the
    wx.Control class, and is used for the base class of various controls
    that have items.
    '''
    def __init__(self):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        theClass = 'ControlWithItems'

##        # Capture initial caller parametsrs before they are changed
##        self.caller_parent = parent
##        self.caller_id = id
##        self.caller_label = label
##        self.caller_pos = pos
##        self.caller_size = size
##        self.caller_style = style
##        self.caller_validator = validator
##        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         self.ts_parent,
                         id=self.ts_Id,
                         pos=self.ts_pos,
                         size=self.ts_size,
                         style=self.ts_style,
                         validator=self.ts_validator,
                         name=self.ts_name)

        ItemContainer.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % self.ts_parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
##            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % str(self.ts_pos))
            self.logger.debug('               size: %s' % str(self.ts_size))
            self.logger.debug('              style: 0x%X' % self.ts_style)
            self.logger.debug('          validator: %s' % self.ts_validator)
            self.logger.debug('               name: %s' % self.ts_name)

##        self.ts_Default = False

##        self.ts_Name = name
##        self.ts_Parent = parent
##        if parent is None:
##            self.ts_GrandParent = None
##        else:
##            self.ts_GrandParent = parent.Parent

##        if False:
##            # Leaves artifacts of different color than parent background.
##            self.ts_BackgroundColour = wx.ThemeToUse[
##                'BackgroundColour'].lower()
##            self.ts_ForegroundColour = wx.ThemeToUse[
##                'ForegroundColour'].lower()
##        else:
##            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
##            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

##        self.ts_Style = style

##        self.ts_ButtonText = label
##        self.ts_Label = label
##        self.ts_Validator = validator
##        self.ts_Value = False

##        myRect, myClientRect = self.tsButtonLayout(
##            parent, pos, size, style, name)
##        self.ts_Rect = myRect
##        self.ts_ClientRect = myClientRect

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
