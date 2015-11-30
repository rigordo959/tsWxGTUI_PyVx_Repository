#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:41:19 AM rsg>"
'''
tsWxPanel.py - Class to establish a panel that is a window on
which controls are placed. It is usually placed within a frame.
Its main feature over its parent class wxWindow is code for
handling child windows and TAB traversal. Since wxWidgets 2.9,
there is support both for TAB traversal implemented by wxWidgets
itself as well as native TAB traversal (such as for GTK 2.0).
'''
#################################################################
#
# File: tsWxPanel.py
#
# Purpose:
#
#    Class to establish a panel that is a window on which controls
#    are placed. It is usually placed within a frame. Its main
#    feature over its parent class wxWindow is code for handling
#    child windows and TAB traversal. Since wxWidgets 2.9, there
#    is support both for TAB traversal implemented by wxWidgets
#    itself as well as native TAB traversal (such as for GTK 2.0).
#
# Usage (example):
#
#    # Import
#
#    from tsWxPanel import Panel
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
#    2011/10/01 rsg Modified __init__ to replace defaultPosition
#                   and defaultSize with values fromparent client
#                   area when parent is NOT a Top Level Window.
#                   NOTE: This modification is intended to support
#                   the application programmer's use of sizers to
#                   automatically layout panel position and size.
#
#    2011/12/04 rsg Added label to constructor argument list.
#
#    2011/12/26 rsg Added logic to tsPanelLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxPanel'
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

import tsWxGlobals as wx
from tsWxEvent import EVT_SET_FOCUS
from tsWxWindow import Window
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

class Panel(Window):
    '''
    A panel is a window on which controls are placed. It is usually placed
    within a frame. Its main feature over its parent class wxWindow is code
    for handling child windows and TAB traversal. Since wxWidgets 2.9,
    there is support both for TAB traversal implemented by wxWidgets itself
    as well as native TAB traversal (such as for GTK 2.0).

    Note:

    Tab traversal is implemented through an otherwise undocumented
    intermediate wxControlContainer class from which any class can derive
    in addition to the normal wxWindow base class. Please see wx/containr.h
    and wx/panel.h to find out how this is achieved.
 
    If not all characters are being intercepted by your OnKeyDown or
    OnChar handler, it may be because you are using the wxTAB_TRAVERSAL
    style, which grabs some keypresses for use by child controls.

    Remarks:

    By default, a panel has the same colouring as a dialog.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_PANEL_STYLE,
                 name=wx.PanelNameStr):
        '''
        Construct and show a generic Window.
        '''
        theClass = 'Panel'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        if parent is None:

            # Top Level Windows (Frames & Dialogs) have no parent
            panelPos = pos
            panelSize = size

        else:

            parentClientArea = parent.ClientArea
            if pos == wx.DefaultPosition:
                panelPos = wxPoint(parentClientArea.x,
                                   parentClientArea.y)
            else:
                panelPos = pos

            if size == wx.DefaultSize:
                panelSize = wxSize(parentClientArea.width,
                                   parentClientArea.height)
            else:
                panelSize = size

        Window.__init__(self,
                        parent,
                        id=id,
                        pos=panelPos,
                        size=panelSize,
                        style=style,
                        name=name)

        self.tsBeginClassRegistration(theClass, id)

        if False:
            self.ts_Rect = wxRect(-1, -1, -1, -1)
            self.ts_ClientRect = self.ts_Rect
        else:
            (myRect, myClientRect) = self.tsPanelLayout(
                parent, panelPos, panelSize, style, name)
            self.ts_Rect = myRect
            self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Label = label
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

        # Facilitate differentiation of this panel from its parent by
        # transposing the parent's foreground and background colors.
        if style == wx.BORDER_SUNKEN:

            self.ts_BackgroundColour = wx.COLOR_BLACK
            self.ts_ForegroundColour = wx.COLOR_WHITE

        elif style == wx.BORDER_RAISED:

            self.ts_BackgroundColour = wx.COLOR_WHITE
            self.ts_ForegroundColour = wx.COLOR_BLACK

        else:

            self.ts_BackgroundColour = self.ts_Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.ts_Parent.ts_ForegroundColour

        self.ts_Style = style

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
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
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.DEFAULT_PANEL_STYLE,
               name=wx.PanelNameStr,
               pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        (myRect, myClientRect) = self.tsPanelLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(self.ts_Rect, pixels=pixels)

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
        ignore under other platforms. Under Mac, it will change the size
        of the returned font. See wx.Window.SetWindowVariant for more about
        this.
        '''
        return (0)

    #-----------------------------------------------------------------------

    def SetFocusIgnoringChildren(self):
        '''
        In contrast to SetFocus (see above) this will set the focus to
        the panel even of there are child windows in the panel.
        '''
        pass

    #----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the Panel.
        '''
        return (self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def tsPanelLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of panel based upon arguments.
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

        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        # Ignore UseClientArea because cursor wraps beyond bottom
        # when last character has been output.
        offset = wxPoint(theBorder.width, theBorder.height)

        if thePosition == theDefaultPosition and \
             theSize == theDefaultSize:

            # The Default Position and the Parent's Default Client Size
            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            parent.ClientArea.width,
                            parent.ClientArea.height)

        elif thePosition == theDefaultPosition:

            # Parent's Default Client Position and the Specified Size
            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            theSize.width,
                            theSize.height)

        else:

            # The Specified Position and the Specified Size

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

        myClientRect = wxRect((myRect.x + offset.x),
                              (myRect.y + offset.y),
                              (myRect.width - (2 * offset.x)),
                              (myRect.height - (2 * offset.y)))

        msg = 'parent=%s; pos=%s; size=%s; name=%s; myRect=%s' % \
              (parent, pos, size, name, myRect)

        self.logger.debug('    tsPanelLayout: %s' % msg)

        return (myRect, myClientRect)

    #----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Panel specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.ts_Parent,
                            id=self.ts_AssignedId,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.ts_Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Panel.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()
                self.tsCreateLabel()

        return (self.ts_Handle is not None)

    # End tsWx API Extensions
    #----------------------------------------------------------------------
    ClientArea = property(tsGetClientArea)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
