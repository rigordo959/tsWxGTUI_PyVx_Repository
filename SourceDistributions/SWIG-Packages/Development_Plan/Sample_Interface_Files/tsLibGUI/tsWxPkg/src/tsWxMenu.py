#! /usr/bin/env python
# "Time-stamp: <04/08/2014  6:07:51 PM rsg>"
'''
tsWxMenu.py - Class to establish a menu which is a popup (or
pull down) list of items, one of which may be selected before
the menu goes away (clicking elsewhere dismisses the menu).
Menus may be used to construct either menu bars or popup menus.
'''
#################################################################
#
# File: tsWxMenu.py
#
# Purpose:
#
#    Class to establish a menu which is a popup (or pull down)
#    list of items, one of which may be selected before the menu
#    goes away (clicking elsewhere dismisses the menu). Menus
#    may be used to construct either menu bars or popup menus.
#
# Usage (example):
#
#    # Import
#
#    from tsWxMenu import Menu
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
#    2014/04/08 rsg Modified Append method to add True to
#                   inhibit trap even when DEBUG is False.
#
# ToDo:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
#################################################################

__title__     = 'tsWxMenu'
__version__   = '0.1.2'
__date__      = '04/08/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
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

import tsExceptions as tse
import tsWxGlobals as wx
from tsWxEvtHandler import EvtHandler

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class Menu(EvtHandler):
    '''
    A menu is a popup (or pull down) list of items, one of which may be
    selected before the menu goes away (clicking elsewhere dismisses the
    menu). Menus may be used to construct either menu bars or popup menus.

    A menu item has an integer ID associated with it which can be used to
    identify the selection, or to change the menu item in some way. A menu
    item with a special identifier -1 is a separator item and does not have
    an associated command but just makes a separator line appear in the menu.

    Note:

    Please note that wxID_ABOUT and wxID_EXIT are predefined by wxWidgets
    and have a special meaning since entries using these IDs will be taken
    out of the normal menus under MacOS X and will be inserted into the
    system menu (following the appropriate MacOS X interface guideline).
    On PalmOS wxID_EXIT is disabled according to Palm OS Companion guidelines.

    Menu items may be either normal items, check items or radio items. Normal
    items do not have any special properties while the check items have a
    boolean flag associated to them and they show a checkmark in the menu
    when the flag is set. wxWidgets automatically toggles the flag value
    when the item is clicked and its value may be retrieved using either
    wxMenu::IsChecked method of wxMenu or wxMenuBar itself or by using
    wxEvent::IsChecked when you get the menu notification for the item in
    question.

    The radio items are similar to the check items except that all the other
    items in the same radio group are unchecked when a radio item is checked.
    The radio group is formed by a contiguous range of radio items, i.e. it
    starts at the first item of this kind and ends with the first item of
    a different kind (or the end of the menu). Notice that because the radio
    groups are defined in terms of the item positions inserting or removing
    the items in the menu containing the radio items risks to not work
    correctly.
    '''
    def __init__(self, title=wx.EmptyString, style=0):
        '''
        '''
        theClass = 'Menu'

        wx.RegisterFirstCallerClassName(self, theClass)

        EvtHandler.__init__(self)

        id = wx.ID_ANY

        self.tsBeginClassRegistration(theClass, id)

        if DEBUG:
            self.logger.debug('              title: %s' % title)
            self.logger.debug('              style: 0x%X' % style)

        self.tsEndClassRegistration(theClass)

    def Append(self,
               id=-1,
               text=wx.EmptyString,
               help=wx.EmptyString,
               kind=0):
        '''
        '''
        if True or DEBUG:
	    # True inhibits trap even when DEBUG is False.
            msg = 'Text="%s"; Help="%s"' % (text, help)
            self.logger.error(
                'raise NotImplementedError: %s (%s)' % (
                    'Append in tsWxMenu', msg))
        else:
            msg = 'NotImplementedError: %s' % 'Append'
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##MenuItem      AppendCheckItem(self, id, text, help)
##MenuItem      AppendItem(self, item)
##MenuItem      AppendMenu(self, id, text, submenu, help)
##MenuItem      AppendRadioItem(self, id, text, help)
##MenuItem      AppendSeparator(self)
##MenuItem      AppendSubMenu(self, submenu, text, help)
##      Attach(self, menubar)
##      Break(self)
##      Check(self, id, check)
##bool  Delete(self, id)
##bool  DeleteItem(self, item)
##      Destroy(self)
##Deletes the C++ object this Python object is a proxy for.
##bool  DestroyId(self, id)
##bool  DestroyItem(self, item)
##      Detach(self)
##      Enable(self, id, enable)
##int   FindItem(self, item)
##MenuItem      FindItemById(self, id)
##MenuItem      FindItemByPosition(self, position)
##EvtHandler    GetEventHandler(self)
##String        GetHelpString(self, id)
##Window        GetInvokingWindow(self)
##String        GetLabel(self, id)
##String        GetLabelText(self, itemid)
##MenuBar       GetMenuBar(self)
##size_t        GetMenuItemCount(self)
##MenuItemList  GetMenuItems(self)
##Menu  GetParent(self)
##long  GetStyle(self)
##String        GetTitle(self)
##MenuItem      Insert(self, pos, id, text, help, kind)
##MenuItem      InsertCheckItem(self, pos, id, text, help)
##MenuItem      InsertItem(self, pos, item)
##MenuItem      InsertMenu(self, pos, id, text, submenu, help)
##MenuItem      InsertRadioItem(self, pos, id, text, help)
##MenuItem      InsertSeparator(self, pos)
##bool  IsAttached(self)
##bool  IsChecked(self, id)
##bool  IsEnabled(self, id)
##MenuItem      Prepend(self, id, text, help, kind)
##MenuItem      PrependCheckItem(self, id, text, help)
##MenuItem      PrependItem(self, item)
##MenuItem      PrependMenu(self, id, text, submenu, help)
##MenuItem      PrependRadioItem(self, id, text, help)
##MenuItem      PrependSeparator(self)
##MenuItem      Remove(self, id)
##MenuItem      RemoveItem(self, item)
##      SetEventHandler(self, handler)
##      SetHelpString(self, id, helpString)
##      SetInvokingWindow(self, win)
##      SetLabel(self, id, label)
##      SetParent(self, parent)
##      SetTitle(self, title)
##      UpdateUI(self, source)
 
##    EventHandler = property(GetEventHandler, SetEventHandler)
##    HelpString = property(GetHelpString, SetHelpString)
##    InvokingWindow = property(GetInvokingWindow, SetInvokingWindow)
##    MenuBar = property(GetMenuBar)
##    MenuItemCount = property(GetMenuItemCount)
##    MenuItems = property(GetMenuItems)
##    Parent = property(GetParent, SetParent)
##    Style = property(GetStyle)
##    Title = property(GetTitle, SetTitle)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
