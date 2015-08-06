#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:36:24 AM rsg>"
'''
tsWxItemContainer.py - Class to emulate the wxPython API for non-graphical,
curses-based platforms.
'''
#################################################################
#
# File: tsWxItemContainer.py
#
# Purpose:
#
#    Class to emulate the wxPython API for non-graphical,
#    curses-based platforms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxItemContainer import ItemContainer as wxItemContainer
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

__title__     = 'tsWxItemContainer'
__version__   = '0.1.1'
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

class ItemContainer(object):
    '''
    The wx.ItemContainer class defines an interface which is implemented by
    all controls which have string subitems, each of which may be selected,
    such as wx.ListBox, wx.CheckListBox, wx.Choice as well as wx.ComboBox
    which implements an extended interface deriving from this one.

    It defines the methods for accessing the controls items and although
    each of the derived classes implements them differently, they still all
    conform to the same interface.

    The items in a wx.ItemContainer have (non empty) string labels and,
    optionally, client data associated with them.
    '''
    def __init__(self):
        '''
        Construct an instance.
        '''
        theClass = 'ItemContainer'

        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

##        self.tsEndClassRegistration(theClass)

##int   Append(self, item, clientData)
##Adds the item to the control, associating the given data with the item if not None.
##      AppendItems(self, strings)
##Apend several items at once to the control.
##      Clear(self)
##Removes all items from the control.
##      Delete(self, n)
##Deletes the item at the zero-based index 'n' from the control.
##int   FindString(self, s)
##Finds an item whose label matches the given string.
##PyObject      GetClientData(self, n)
##Returns the client data associated with the given item, (if any.)
##int   GetCount(self)
##Returns the number of items in the control.
##      GetItems(self)
##Return a list of the strings in the control
##int   GetSelection(self)
##Returns the index of the selected item or wx.NOT_FOUND if no item is selected.
##String        GetString(self, n)
##Returns the label of the item with the given index.
##wxArrayString         GetStrings(self)
##String        GetStringSelection(self)
##Returns the label of the selected item or an empty string if no item is selected.
##int   Insert(self, item, pos, clientData)
##Insert an item into the control before the item at the pos index, optionally associating some data object with the item.
##bool  IsEmpty(self)
##Returns True if the control is empty or False if it has some items.
##      Select(self, n)
##This is the same as SetSelection and exists only because it is slightly more natural for controls which support multiple selection.
##      SetClientData(self, n, clientData)
##Associate the given client data with the item at position n.
##      SetItems(self, items)
##Clear and set the strings in the control from a list
##      SetSelection(self, n)
##Sets the item at index 'n' to be the selected item.
##      SetString(self, n, s)
##Sets the label for the given item.
##bool  SetStringSelection(self, s)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

##    Count = property(GetCount)
##    Items = property(GetItems, SetItems)
##    Selection = property(GetSelection, SetSelection)
##    Strings = property(GetStrings)
##    StringSelection = property(GetStringSelection, SetStringSelection)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
