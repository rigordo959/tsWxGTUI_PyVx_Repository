#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:09:14 AM rsg>"
'''
tsWxMenuBar.py - Class to establish a menu bar, a series of menus
accessible from the top of a frame.
'''
#################################################################
#
# File: tsWxMenuBar.py
#
# Purpose:
#
#    Class to establish a menu bar, a series of menus accessible
#    from the top of a frame.
#
# Usage (example):
#
#    # Import
#
#    from tsWxMenuBar import MenuBar
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
#    2010/08/31 rsg - For consistancy with wxPython and industry
#                     conventions, changed characterCellAccelerator
#                     to "tsGTUI.DISPLAY_UNDERLINE"
#                     from "tsGTUI.DISPLAY_BOLD".
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxMenuBar'
__version__   = '0.2.0'
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

from textwrap import TextWrapper

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI

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

class MenuBar(Window):
    '''
    Class to establish a menu bar, a series of menus accessible from the
    top of a frame.

    Remarks: To respond to a menu selection, provide a handler for
    EVT_MENU, in the frame that contains the menu bar.

    If you have a toolbar which uses the same identifiers as your
    EVT_MENU entries, events from the toolbar will also be processed by
    your EVT_MENU event handlers.

    Tip: under Windows, if you discover that menu shortcuts (for example,
    Alt-F to show the file menu) are not working, check any EVT_CHAR events
    you are handling in child windows. If you are not calling event.Skip()
    for events that you do not process in these event handlers, menu
    shortcuts may cease to work.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_MENUBAR_STYLE,
                 name=wx.MenuBarNameStr):
        '''
        Construct and show a generic Window.
        '''
        theClass = 'MenuBar'

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

        myRect = wxRect(parent.Rect.x + wx.pixelWidthPerCharacter,
                        parent.Rect.y + wx.pixelHeightPerCharacter,
                        parent.Rect.width - 2* wx.pixelWidthPerCharacter,
                        wx.ThemeToUse['MenuBar']['WindowHeight'])
        self.ts_Rect = myRect

        self.ts_theEntry = []
        self.ts_theEntryCount = wx.ID_ANY
        self.ts_MenuCount = 0
        self.ts_Menus = None

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
##            self.logger.debug('              title: %s' % title)
            self.logger.debug('                pos: %s' % self.Position)
            self.logger.debug('               size: %s' % self.Size)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        self.ts_BackgroundColour = wx.ThemeToUse['BackgroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse['ForegroundColour'].lower()

        self.ts_Style = style

        self.ts_TheWrapper = None

        self.ts_UserInputEnable = False

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Append(self, menu, title):
        '''
        '''
        pos = self.ts_theEntryCount + 1
        self.Insert(self.ts_theEntryCount, menu, title)
        return (True)

    #-----------------------------------------------------------------------

    def Attach(self, frame):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'Attach in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def Check(self, id, check):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'Check in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def Detach(self):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'Detach in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def Enable(self, enable):
        '''
        Enable or disable the window for user input.
        '''
        if self.ts_UserInputEnable == enable:
            return (False)
        else:
            self.ts_UserInputEnable = enable
            return (True)

    #-----------------------------------------------------------------------

    def EnableTop(self, pos, enable):
        '''
        '''
        self.ts_theEntry[pos]['enabled'] = enable

    #-----------------------------------------------------------------------

    def FindItemById(self, id):
        '''
        '''
        MenuItem = self.ts_theEntry[id]
        return (MenuItem)

    #-----------------------------------------------------------------------

    def FindMenu(self, title):
        '''
        '''
        pos = wx.ID_ANY
        for i in range(len(self.ts_theEntry)):
            if self.ts_theEntry[i]['title'] == title:
                pos = i
                break
        return pos

    #-----------------------------------------------------------------------

    def FindMenuItem(self, menu, item):
        '''
        '''
        return (0)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetAutoWindowMenu():
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def GetFrame(self):
        '''
        '''
        return (self.ts_Parent)

    #-----------------------------------------------------------------------

    def GetHelpString(self, id):
        '''
        '''
        return (None)

    #-----------------------------------------------------------------------

    def GetLabel(self):
        '''
        Generic way of getting a label from any window, for identification
        purposes.
        '''
        return (self.ts_Label)

    #-----------------------------------------------------------------------

    def GetLabelTop(self, pos):
        '''
        '''
        return (None)

    #-----------------------------------------------------------------------

    def GetMenu(self, pos):
        '''
        '''
        return (self.ts_theEntry[pos])

    #-----------------------------------------------------------------------

    def GetMenuCount(self):
        '''
        '''
        return (len(self.ts_theEntry))

    #-----------------------------------------------------------------------

    def GetMenuLabel(self, pos):
        '''
        '''
        try:
            label = self.ts_theEntry[pos]['title']
        except IndexError:
            label = None
 
        return (label)

    #-----------------------------------------------------------------------

    def GetMenuLabelText(self, pos):
        '''
        '''
        label = self.GetMenuLabel(pos)
        text = label.replace('&', '')
        return (text)

    #-----------------------------------------------------------------------

    def GetMenus(self):
        '''
        Return a list of (menu, label) items for the menus in the MenuBar.
        '''
        return ([])

    #-----------------------------------------------------------------------

    def Insert(self, pos, menu, title):
        '''
        '''
        self.ts_theEntryCount += 1
        self.ts_theEntry.insert(
            pos,
            {'enabled': False,
             'menu': menu,
             'name': pos,
             'title': title})
        # TBD - Remove _ShowMenuBarHorizontalEntries
##        self.ts_ShowMenuBarHorizontalEntries()

    #-----------------------------------------------------------------------

    def IsAttached(self):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsChecked(self, id):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsEnabled(self):
        '''
        turns true if the window is enabled for input, false otherwise.
        '''
        return (False)

    #-----------------------------------------------------------------------

    def IsEnabledTop(self, pos):
        '''
        '''
        return (False)

    #-----------------------------------------------------------------------
 
    def Remove(self, pos):
        '''
        '''
        self.ts_theEntryCount -= 1
        x = self.ts_theEntry[pos]
        self.ts_theEntry.remove(x)

    #-----------------------------------------------------------------------

    def Replace(self, pos, menu, title):
        '''
        '''
        self.ts_theEntry[pos] = {'enabled': False,
                               'menu': menu,
                               'name': pos,
                               'title': title}

    #-----------------------------------------------------------------------

    @staticmethod
    def SetAutoWindowMenu(enable):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'SetAutoWindowMenu'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetHelpString(self, id, helpString):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'SetHelpString in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def SetLabel(self, label):
        '''
        Set the text which the window shows in its label if applicable.
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'SetLabel in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def SetLabelTop(self, pos, label):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'SetLabelTop in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def SetMenuLabel(self, pos, label):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'SetMenuLabel in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def SetMenus(self, items):
        '''
        Clear and add new menus to the MenuBar from a list of (menu, label)
        items.
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'SetMenus in tsWxMenuBar')

    #-----------------------------------------------------------------------

    def UpdateMenus(self):
        '''
        '''
        self.logger.error(
            'raise NotImplementedError: %s' % 'UpdateMenus in tsWxMenuBar')

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetMenuBarSize(self):
        '''
        '''
        menubar = self

        # Begin text wrapper setup
        width = (self.Rect.width // wx.pixelWidthPerCharacter) - 2
        expand_tabs = True
        replace_whitespace = True
        initial_indent = ''
        subsequent_indent = ''
        fix_sentence_endings = False
        break_long_words = False
        self.ts_TheWrapper = TextWrapper(
            width=width - len(subsequent_indent),
            expand_tabs=expand_tabs,
            replace_whitespace=replace_whitespace,
            initial_indent=initial_indent,
            subsequent_indent=subsequent_indent,
            fix_sentence_endings=fix_sentence_endings,
            break_long_words=break_long_words)
        # End text wrapper setup

##        self.ts_Rect = parent._frameMenuBarRect
##        self.theLayoutAlgorithm = wxLayoutAlgorithm()
##        window = self
##        theTitle = parent._Rect
##        MenuBar = self.theLayoutAlgorithm._LayoutMenuBar(window, theTitle)

        text = ''
        separator = '  '
        for i in range(len(menubar.ts_theEntry)):
            item = str(menubar.ts_theEntry[i]['title'])
            ampersandPosition = item.find('&')

            if ampersandPosition == 0:
                prefix = ''
            else:
                prefix = item[0:ampersandPosition]

            character = item[ampersandPosition+1]
            suffix = item[ampersandPosition+2:len(item)]

            text += prefix
            text += character
            text += separator

        theLines = self.ts_TheWrapper.wrap(text)
        theCols = width
        theRows = len(theLines) + 2

        return (self.tsGetPixelValues(theCols, theRows))

    #-----------------------------------------------------------------------

    def tsShowMenuBarHorizontalEntries(self):
        '''
        '''
        menubar = self

        text = ''
##        (row, col, width, height) = self.ts_getCharacterRectangle(
##            self.ts_Rect.x, self.ts_Rect.y, self.ts_Rect.width, self.ts_Rect.height)
        row = (self.Rect.x // wx.pixelWidthPerCharacter) + 0
        col = (self.Rect.y // wx.pixelHeightPerCharacter) + 0
        separator = '  '

        useAccelerator = True
        if useAccelerator:
            characterCellAttribute = None # tsGTUI.DISPLAY_STANDOUT
            characterCellAccelerator = tsGTUI.DISPLAY_UNDERLINE
        else:
            characterCellAttribute = tsGTUI.DISPLAY_NORMAL
            characterCellAccelerator = characterCellAttribute

        for i in range(len(menubar.ts_theEntry)):
            item = str(menubar.ts_theEntry[i]['title'])
            ampersandPosition = item.find('&')

            if ampersandPosition == 0:
                prefix = ''
            else:
                prefix = item[0:ampersandPosition]

            character = item[ampersandPosition+1]
            suffix = item[ampersandPosition+2:len(item)]

            self.tsCursesAddStr(col,
                                row,
                                prefix,
                                attr=characterCellAttribute,
                                pixels=False)

            col += len(prefix)
            self.tsCursesAddStr(col,
                                row,
                                character,
                                attr=characterCellAccelerator,
                                pixels=False)

            col += len(character)
            self.tsCursesAddStr(col,
                                row,
                                suffix,
                                attr=characterCellAttribute,
                                pixels=False)

            col += len(suffix)
            self.tsCursesAddStr(col, row, separator, attr=None, pixels=False)

            col += len(separator)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update MenuBar specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                myRect = wxRect(
                    self.ts_Parent.Rect.x + wx.pixelWidthPerCharacter,
                    self.ts_Parent.Rect.y + wx.pixelHeightPerCharacter,
                    self.ts_Parent.Rect.width - 2* wx.pixelWidthPerCharacter,
                    wx.ThemeToUse['MenuBar']['WindowHeight'])

                thePosition = wxPoint(myRect.x, myRect.y)
                theSize = wxSize(myRect.width, myRect.height)

                # TBD - Update Class geometry.
    ##            self.ts_Rect = myRect
    ##            self.logger.debug(
    ##                '_show: myRect=%s; Rect = %s' % (myRect, self.ts_Rect))

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

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the MenuBar.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd(' ', attr=None)

                self.tsCreateMenuBar()

                self.tsShowMenuBarHorizontalEntries()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Frame = property(GetFrame)
    MenuCount = property(GetMenuCount)
    Menus = property(GetMenus, SetMenus)

#--------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
