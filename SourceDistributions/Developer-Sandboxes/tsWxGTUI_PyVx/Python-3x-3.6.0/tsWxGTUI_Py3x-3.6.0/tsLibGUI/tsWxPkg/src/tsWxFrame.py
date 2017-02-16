#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:34:24 AM rsg>"
'''
tsWxFrame.py - Class to emulate the wxPython API for
non-graphical, curses-based platforms.
'''
#################################################################
#
# File: tsWxFrame.py
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
#    from tsWxFrame import Frame
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
#    1. The operator must use/create a separate desktop for each GUI
#       application.
#
#    2. Each operator desktop supports only one application frame (such
#       as the GNU "Midnight Commander" File Manager).
#
#    3. Each operator desktop also supports one optional frame (identified
#       by the reserved name "stdio") for the display of redirected output
#       from "stdout" and "stderr".
#
#    The above limitations are a consequence of the curses implimentation.
#    Curses handles child positioning and child contents in a different
#    manner than wxPython:
#
#    a. Segmentation faults occur when curses attempts to create a child
#       object that extends beyond the upper or lower border of the frame.
#
#    b. No exception is raised when curses attempts to create a child object
#       that extends beyond the right border of the frame. Instead, the
#       contents of the child are clipped.
#
#    c. No exception is raised when curses attempts to create a child object
#       that extends beyond the left border of the frame. Instead, the
#       left border of the child and the contents of the child will be
#       created at the left border of the frame.
#
# Notes:
#
#    A Frame is a window whose size and position can (usually) be changed by
#    the user. It usually has thick borders and a title bar, and can
#    optionally contain a menu bar, toolbar and status bar. A frame can
#    contain any window that is not a Frame or Dialog. It is one of the most
#    fundamental of the wxWindows components.
#
#    A Frame that has a status bar and toolbar created via the
#    CreateStatusBar / CreateToolBar functions manages these windows, and
#    adjusts the value returned by GetClientSize to reflect the remaining
#    size available to application windows.
#
#    By itself, a Frame is not too useful, but with the addition of Panels
#    and other child objects, it encompasses the framework around which most
#    user interfaces are constructed.
#
#    If you plan on using Sizers and auto-layout features, be aware that the
#    Frame class lacks the ability to handle these features unless it contains
#    a Panel. The Panel has all the necessary functionality to both control
#    the size of child components, and also communicate that information in a
#    useful way to the Frame itself.
#
#    As is typical of child objects, buttons may be positioned within or beyond
#    the border of the frame. Children whose contents or borders are located
#    beyond the border of the frame are silently clipped, without the raising
#    of any error exception.
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
#    2010/07/02 rsg Set self.ts_FrameAcceleratorTable to
#                   reflect active buttons (OnMinimize,
#                   OnRestoreDown, OnMaximize and OnClose).
#
#    2010/08/27 rsg Initiatialized self.ts_SystemEventTable
#                   and self.ts_UserEventTable to
#                   reflect active buttons (OnMinimize,
#                   OnRestoreDown, OnMaximize and OnClose).
#
#    2010/10/03 rsg Moved instance variables for the top-level
#                   buttons (OnClose, OnMaximize, OnMinimize and
#                   OnRestore).
#
#    2010/10/25 rsg Updated layout in tsGetClientArea to
#                   recognize changes such as post-creation
#                   re-sizing, centering or addition of menu
#                   bar, tool bar and status bar.
#
#    2011/12/25 rsg Instrumented tsCreateButtonBar to detect
#                   and unexpected changes in position of
#                   buttons relative to title that showed
#                   up in TaskBar.tsTaskBarOnSetFocus.
#
#    2011/12/27 rsg Added logic to tsFrameWindowLayout to
#                   inhibit operation once self.ts_Handle has
#                   been assigned a curses window identifier.
#
#    2012/01/15 rsg Disabled conditional logic in tsShow that
#                   set self.ts_FocusFromKbd = self.
#
#    2012/05/02 rsg Added self.ts_DescendantOrderOfShow to
#                   register the order of show of for this
#                   top level window and its descendants.
#
#    2013/07/04 rsg Re-designed tsCreateButtonBar in effort
#                   to fix handling of mouse clicks.
#
# ToDo:
#
#    2010/03/20 rsg Replace cmdID value when supporting
#                   accelerators.
#
#    2011/12/25 rsg Remove Instrumented tsCreateButtonBar
#                   if nothing found.
#
#################################################################

__title__     = 'tsWxFrame'
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

import tsExceptions as tse

import tsWxGlobals as wx
from tsWxEvent import EVT_COMMAND_LEFT_CLICK
from tsWxEvent import EVT_CLOSE
from tsWxEvent import EVT_ICONIZE
from tsWxEvent import EVT_MINIMIZE
from tsWxEvent import EVT_MAXIMIZE
from tsWxEvent import EVT_RESTOREDOWN
from tsWxEvent import EVT_SET_FOCUS
from tsWxAcceleratorEntry import AcceleratorEntry as wxAcceleratorEntry
from tsWxAcceleratorTable import AcceleratorTable as wxAcceleratorTable
from tsWxFrameButton import FrameButton as wxButton
from tsWxObject import Object as wxObject
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxStatusBar import StatusBar as wxStatusBar
from tsWxTopLevelWindow import TopLevelWindow

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

ButtonBar               = wx.ThemeToUse['Frame']['ButtonBarDefault']
CloseButtonLabel        = wx.ThemeToUse['Frame']['CloseButtonLabel']
MaximizeButtonLabel     = wx.ThemeToUse['Frame']['MaximizeButtonLabel']
IconizeButtonLabel      = wx.ThemeToUse['Frame']['IconizeButtonLabel']
RestoreDownButtonLabel  = wx.ThemeToUse['Frame']['RestoreDownButtonLabel']

#---------------------------------------------------------------------------

class Frame(TopLevelWindow):
    '''
    Proxy of C++ Frame class.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name=wx.FrameNameStr):
        '''
        Construct class.
        '''
        theClass = 'Frame'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_title = title
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        TopLevelWindow.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        (myRect, myClientRect) = self.tsFrameWindowLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              title: %s' % title)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)
            self.logger.debug('              stdio: %s' % \
                              self.FindWindowByName(wx.StdioNameStr))

        self.ts_Name = name
        self.ts_Parent = parent

        self.ts_DescendantOrderOfShow = [self.ts_AssignedId]

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
            self.ts_ReserveTaskBarArea == False
            self.ts_ReserveRedirectArea = False
        else:
            self.ts_GrandParent = parent.Parent
            self.ts_ReserveTaskBarArea == parent.ts_ReserveTaskBarArea
            self.ts_ReserveRedirectArea = parent.ts_ReserveRedirectArea

        if name == wx.TaskBarNameStr:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'TaskBar']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'TaskBar']['ForegroundColour'].lower()
            self.ts_ReserveTaskBarArea == True

        elif name == wx.StdioNameStr:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'Stdio']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'Stdio']['ForegroundColour'].lower()
            self.ts_ReserveRedirectArea = True

        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()

##        self.ts_FocusEnabled = True
        self.SetFocus()

        self.ts_Label = title
        self.ts_MenuBar = None
        self.ts_StatusBar = None
        self.ts_StatusBarPane = None
        self.ts_Style = style
        self.ts_Title = title
        self.ts_ToolBar = None

        self.ts_defaultFrameAcceleratorEntries = {
            '_': {'name': 'OnIconize',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('_'),
                  'cmdID': wx.ID_ANY},
            'z': {'name': 'OnRestoreDown',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('z'),
                  'cmdID': wx.ID_ANY},
            'Z': {'name': 'OnMaximize',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('Z'),
                  'cmdID': wx.ID_ANY},
            'X': {'name': 'OnClose',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('X'),
                  'cmdID': wx.ID_ANY}
        }

        self.ts_OnFrameCloseButton = None
        self.ts_OnFrameMaximizeButton = None
        self.ts_OnFrameIconizeButton = None
        self.ts_OnFrameRestoreDownButton = None

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

##        if self.ts_OnFrameCloseButton is None:

##            pass

##        else:

##            event = EVT_COMMAND_LEFT_CLICK # EVT_CLOSE
##            handler = self.tsFrameOnClose
##            source = self.ts_OnFrameCloseButton
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##        if self.ts_OnFrameMaximizeButton is None:

##            pass

##        else:

##            event = EVT_COMMAND_LEFT_CLICK # EVT_MAXIMIZE
##            handler = self.tsFrameOnMaximize
##            source = self.ts_OnFrameMaximizeButton
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##        if self.ts_OnFrameIconizeButton is None:

##            pass

##        else:

##            event = EVT_COMMAND_LEFT_CLICK # EVT_ICONIZE
##            handler = self.tsFrameOnIconize
##            source = self.ts_OnFrameIconizeButton
##            self.Bind(event,
##                      handler,
##                      source,
##                      useSystemEventTable=True)

##        if self.ts_OnFrameRestoreDownButton is None:

##            pass

##        else:

##            event = EVT_COMMAND_LEFT_CLICK # EVT_RESTOREDOWN
##            handler = self.tsFrameOnRestoreDown
##            source = self.ts_OnFrameRestoreDownButton
##            self.Bind(event,
##                      handler,
##                      source,
##                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Command(self, winid):
        '''
        TBD
        '''
        msg = 'tsWxFrame.Command: ' + \
            'NOT Implemented for winid=%s.' % str(winid)
        print('DEBUG: %s\n' % msg)
        self.logger.error('raise NotImplementedError: %s' % msg)

        return (False)

    #-----------------------------------------------------------------------

    def Create(
        self,
        parent,
        id=wx.ID_ANY,
        title=wx.EmptyString,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE,
        name=wx.FrameNameStr,
        pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        (myRect, myClientRect) = self.tsFrameWindowLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def CreateStatusBar(self,
                        number=1,
                        style=wx.DEFAULT_STATUSBAR_STYLE,
                        winid=wx.ID_ANY,
                        name=wx.StatusBarNameStr):
        '''
        Create a default Status Bar with the specified number of panels.
        '''
        # TBD - CreateStatusBar is Under Construction.
        parent = self
        theStatusBar = wxStatusBar(parent,
                                   id=winid)

        theStatusBar.SetFieldsCount(number)

        self.SetStatusBar(theStatusBar)

        return (theStatusBar)

    #-----------------------------------------------------------------------

    def CreateToolBar(self, style, winid, name):
        '''
        Create a default Tool Bar
        '''
        return (None) # (wxToolBar())

    #-----------------------------------------------------------------------

    def DoGiveHelp(self, text, show):
        '''
        '''
        self.logger.error('raise NotImplementedError: %s' % 'DoGiveHelp')

    #-----------------------------------------------------------------------

    def DoMenuUpdates(self, menu):
        '''
        '''
        self.logger.error('raise NotImplementedError: %s' % 'DoMenuUpdates')

    #-----------------------------------------------------------------------

    def FindItemInMenuBar(self, menuId):
        '''
        '''
        menuBar = self.ts_MenuBar
        if (not (menuBar is None)):

            return (menuBar.FindItem(menuId))

        else:

            return (None)

##        self.logger.error('raise NotImplementedError: %s' % \
##                          'FindItemInMenuBar')

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

    def GetMenuBar(self):
        '''
        Return the MenuBar object, when one has been defined, or None.
        '''
        return (self.ts_MenuBar)

    #-----------------------------------------------------------------------

    def GetStatusBar(self):
        '''
        Return the StatusBar object, when one has been defined, or None.
        '''
        return (self.ts_StatusBar)

    #-----------------------------------------------------------------------

    def GetStatusBarPane(self):
        '''
        Return the StatusBar Pane ID, when one has been defined, or None.
        '''
        return (self.ts_StatusBarPane)

    #-----------------------------------------------------------------------

    def GetToolBar(self):
        '''
        Return the ToolBar object, when one has been defined, or None.
        '''
        return (self.ts_ToolBar)

    #-----------------------------------------------------------------------

    def PopStatusText(self, number):
        '''
        '''
        self.logger.error('raise NotImplementedError: %s' % 'PopStatusText')

    #-----------------------------------------------------------------------

    def ProcessCommand(self, winid):
        '''
        '''
        msg = 'tsWxFrame.ProcessCommand: ' + \
            'NOT Implemented for winid=%s.' % str(winid)
        print('DEBUG: %s\n' % msg)
        self.logger.error('raise NotImplementedError: %s' % msg)

        self.Command(winid)

        return (False)

    #-----------------------------------------------------------------------

    def PushStatusText(self, text, number):
        '''
        '''
        self.logger.error('raise NotImplementedError: %s' % 'PushStatusText')

    #-----------------------------------------------------------------------

    def SendSizeEvent(self):
        '''
        '''
        self.logger.error('raise NotImplementedError: %s' % 'SendSizeEvent')

    #-----------------------------------------------------------------------

    def SetMenuBar(self, menubar):
        '''
        Record the MenuBar object, when one has been defined.
        '''
##        self.ts_ClientRect.y += (menubar.ts_Rect.y + (
##            2 * wx.pixelHeightPerCharacter))
##        self.ts_ClientRect.height -= (menubar.ts_Rect.height + (
##            2 * wx.pixelHeightPerCharacter))

        self.ts_MenuBar = menubar
        self.logger.debug(
            '         SetMenuBar: %s; Handle=%s; Children=%s' % (
                menubar, self.ts_MenuBar.ts_Handle, self.ts_Children))

    #-----------------------------------------------------------------------

    def SetStatusBar(self, statBar):
        '''
        Record the StatusBar object, when one has been defined.
        '''
        # TBD - Only needed if StatusBar relocated from just below bottom
        # of Frame to inside, just above bottom of Frame.
##        self.ts_ClientRect.height -= (statBar.ts_Rect.height + (
##            0 * wx.pixelHeightPerCharacter))

        self.ts_StatusBar = statBar
        self.logger.debug(
            '         SetStatusBar: %s; Handle=%s; Children=%s' % (
                statBar, self.ts_StatusBar.ts_Handle, self.ts_Children))

    #-----------------------------------------------------------------------

    def SetStatusBarPane(self, n):
        '''
        Record the StatusBar Pane ID, when one has been defined.
        '''
        self.ts_StatusBarPane = n
        self.logger.debug(
            '         SetStatusBarPane: %d' % n)

    #-----------------------------------------------------------------------

    def SetStatusText(self, text, number):
        '''
        Record the StatusBar Text, when one has been defined.
        '''
        self.ts_StatusBar.SetStatusText(text, number)
        self.logger.debug(
            '         SetStatusBarText: %d = %s' % (number, text))

    #-----------------------------------------------------------------------

    def SetStatusWidths(self, widths):
        '''
        Record the StatusBar Width(s), when one has been defined.
        '''
        self.ts_StatusBar.SetStatusWidths(widths)
        self.logger.debug(
            '         SetStatusBarWidths: %s' % widths)

    #-----------------------------------------------------------------------

    def SetToolBar(self, toolbar):
        '''
        Record the ToolBar, when one has been defined.
        '''
##        self.ts_ClientRect.y += (toolbar.ts_Rect.y + (
##            2 * wx.pixelHeightPerCharacter))
##        self.ts_ClientRect.height -= (toolbar.ts_Rect.height + (
##            0 * wx.pixelHeightPerCharacter))

        self.ts_ToolBar = toolbar
        self.logger.debug(
            '         SetToolBar: %s' % toolbar)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsButtonData(self):
        '''
        Define the label and handler for the Iconize, Maximize and Close
        Buttons on the Frame Title Line.

        Based on "wxPython In Action" by Noel Rappin and Robin Dunn,
        Manning Publications Co. (See downloaded source code located in
        Chapter-05, goodExample.py.)
        '''
        if ((self.ts_Rect.TopLeft == \
             wxObject.TheDisplay.ClientArea.TopLeft) and \
            (self.ts_Rect.BottomRight == \
             wxObject.TheDisplay.ClientArea.BottomRight)):

            # Full Screen; Show "RestoreDown" instead of "Maximize" Button
            return ((IconizeButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_ICONIZE,
                     None, # self.tsFrameOnIconizeClick,
                     'IconizeButton(%s)' % self.ts_Name),

                    (RestoreDownButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_RESTOREDOWN,
                     None, # self.tsFrameOnRestoreDownClick,
                     'RestoreDownButton(%s)' % self.ts_Name),

                    (CloseButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_CLOSE,
                     None, # self.tsFrameOnCloseClick,
                     'CloseButton(%s)' % self.ts_Name))
        else:

            # Not Full Screen; Show "Maximize" Button
            return ((IconizeButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_ICONIZE,
                     None, # self.tsFrameOnIconizeClick,
                     'IconizeButton(%s)' %self.ts_Name),

                    (MaximizeButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_MAXIMIZE,
                     None, # self.tsFrameOnMaximizeClick,
                     'MaximizeButton(%s)' % self.ts_Name),

                    (CloseButtonLabel,
                     EVT_COMMAND_LEFT_CLICK, # EVT_CLOSE,
                     None, # self.tsFrameOnCloseClick,
                     'CloseButton(%s)' % self.ts_Name))

    #-----------------------------------------------------------------------

    def tsBuildOneButton(self,
                         parent,
                         label=None,
                         event=None,
                         button=None,
                         handler=None,
                         pos=(0,0),
                         name=wx.ButtonNameStr):
        '''
        Create the specified Frame Button located on the Frame Title
        Line.

        Based on "wxPython In Action" by Noel Rappin and Robin Dunn,
        Manning Publications Co. (See downloaded source code located in
        Chapter-05, goodExampple.py.)
        '''
        button = wxButton(parent,
                          wx.ID_ANY,
                          label=label,
                          pos=pos,
##                          size=(len(label) + len('[ ]')),
                          name=name,
                          useClientArea=True)

##        # Bind mouse event ASAP (now).
##        # Will register event in the SystemEventTable
##        # if useSystemEventTable=True.
##        self.Bind(event,
##                  handler,
##                  button,
##                  useSystemEventTable=True)

        return (button)

    #-----------------------------------------------------------------------

    def tsCreateButtonBar(self, panel, xPos=0, yPos=0):
        '''
        Create the collection of Frame Buttons located on the Frame Title
        Line.

        Based on "wxPython In Action" by Noel Rappin and Robin Dunn,
        Manning Publications Co. (See downloaded source code located in
        Chapter-05, goodExampple.py.)
        '''
        theLabels = []
        theButtons = []
        uninstalledAcceleratorEntries = []
        for theLabel, theEvent, theHandler, theName in self.tsButtonData():
            theLabels += [theLabel]
            pos = wxPoint(xPos, yPos)
            button = self.tsBuildOneButton(panel,
                                           label=theLabel,
                                           event=theEvent,
                                           handler=theHandler,
                                           pos=pos,
                                           name=theName)

##            if theLabel == CloseButtonLabel:

##                theButton = self.ts_OnFrameCloseButton = button

##              event = EVT_COMMAND_LEFT_CLICK # EVT_CLOSE
##              handler = self.tsFrameOnCloseClick
##              source = self.ts_OnFrameCloseButton
##              button.Bind(event,
##                          handler,
##                          source,
##                          useSystemEventTable=True)

##            elif theLabel == MaximizeButtonLabel:

##                theButton = self.ts_OnFrameMaximizeButton = button

##              event = EVT_COMMAND_LEFT_CLICK # EVT_MAXIMIZE
##              handler = self.tsFrameOnMaximizeClick
##              source = self.ts_OnFrameMaximizeButton
##              button.Bind(event,
##                          handler,
##                          source,
##                          useSystemEventTable=True)

##            elif theLabel == IconizeButtonLabel:

##                theButton = self.ts_OnFrameIconizeButton = button

##              event = EVT_COMMAND_LEFT_CLICK # EVT_ICONIZE
##              handler = self.tsFrameOnIconizeClick
##              source = self.ts_OnFrameIconizeButton
##              button.Bind(event,
##                          handler,
##                          source,
##                          useSystemEventTable=True)

##            elif theLabel == RestoreDownButtonLabel:

##                theButton = self.ts_OnFrameRestoreDownButton = button

##              event = EVT_COMMAND_LEFT_CLICK # EVT_RESTOREDOWN
##              handler = self.tsFrameOnRestoreDownClick
##              source = self.ts_OnFrameRestoreDownButton
##              button.Bind(event,
##                          handler,
##                          source,
##                          useSystemEventTable=True)

##            else:

##              msg = 'Invalid value for theLabel="%s"' % theLabel
##              print('ERROR: %s' % msg)

            try:
                fmt1 = '\n\n tsCreateButtonBar: '
                fmt2 = '\n\t self.GetLabel="%s"; ' % self.GetLabel()
                fmt3 = '\n\t self="%s"; ' % str(self)
                fmt4 = '\n\t theLabel="%s"; ' % str(theLabel)
                fmt5 = '\n\t theEvent="%s"; ' % str(theEvent)
                fmt6 = '\n\t theButton="%s"; ' % str(theButton)
                fmt7 = '\n\t theHandler="%s"; ' % str(theHandler)
                fmt8 = '\n\t theName="%s"; ' % str(theName)
                fmt9 = '\n\t theButton="%s"' % str(button)
                msg = fmt1 + fmt2 + fmt3 + fmt4 + \
                    fmt5 + fmt6 + fmt7 + fmt8 + fmt9
                print(msg)
            except Exception as errorCode:
                fmt1 = 'tsCreateButtonBar: '
                fmt2 = 'errorCode="%s"' % str(errorCode)
                print('ERROR: "%s"' % errorCode)

##            # Bind mouse event ASAP (now).
##            # Will register event in the SystemEventTable
##            # if useSystemEventTable=True.
##            self.Bind(theEvent,
##                      theHandler,
##                      button,
##                      useSystemEventTable=True)

            theButtons += [button]

##            myRect = button.Rect
##            xPos += myRect.width - 1 * wx.pixelWidthPerCharacter
##            self.logger.debug('tsCreateButtonBar: myRect=%s' % str(myRect))
            xPos += button.GetSize().width - 1 * wx.pixelWidthPerCharacter

        self.theFrameButtons = theButtons

    #-----------------------------------------------------------------------

    def tsGetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the Frame,
        i.e., without menu bars, tool bars, status bars and such.
        '''
        parent = self.ts_Parent
        pos = wxPoint(self.ts_Rect.x, self.ts_Rect.y)
        size = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        style = self.ts_Style
        name = self.ts_Name

        (myRect, myClientRect) = self.tsFrameWindowLayout(
            parent, pos, size, style, name)

        if self.ts_Rect != myRect:

            # My Area changed after by new feature
            fmt1 = 'Wrong layout. myRect (%s) ' % str(myRect)
            fmt2 = 'changed from self.ts_Rect (%s) ' % str(self.ts_Rect)
            fmt3 = 'in tsWxFrame.tsGetClientArea'
            msg = fmt1 + fmt2 + fmt3
            self.logger.wxASSERT_MSG(
                (self.ts_Rect == myRect),
                msg)

            self.ts_Rect = myRect

        if self.ts_ClientRect != myClientRect:

            # Client Area changed after by new feature
            self.ts_ClientRect = myClientRect

        return (self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def tsFrameOnCloseClick(self, evt):
        '''
        '''
        msg = 'tsFrameOnCloseClick Received "%s"' % str(evt)
        print(msg)
        self.logger.debug(msg)

##        triggeringObject = self.ts_ScrolledText
##        objectId = triggeringObject.ts_AssignedId

##        objectCriteria = 'EVT_VSCROLLWIN_LINEUP for [^]-Button'
##        triggeringEvent = EVT_VSCROLLWIN_LINEUP

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsFrameOnIconizeClick(self, evt):
        '''
        '''
        msg = 'tsFrameOnIconizeClick Received "%s"' % str(evt)
        print(msg)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsFrameOnMaximizeClick(self, evt):
        '''
        '''
        msg = 'tsFrameOnMaximizeClick Received "%s"' % str(evt)
        print(msg)
        self.logger.debug(msg)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsFrameOnRestoreDownClick(self, evt):
        '''
        '''
        msg = 'tsFrameOnRestoreDownClick Received "%s"' % str(evt)
        print(msg)
        self.logger.debug(msg)

        results = self.tsProcessEventTables(
            objectCriteria=objectCriteria,
            objectId=objectId,
            triggeringEvent=triggeringEvent,
            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsFrameWindowLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of frame based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)

        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        if name == wx.TaskBarNameStr:

            myRect = wxObject.TheDisplay.tsGetTaskArea(pixels=True)

        elif name == wx.StdioNameStr:

            myRect = wxObject.TheDisplay.tsGetRedirectedStdioArea(pixels=True)

        elif thePosition == theDefaultPosition and theSize == theDefaultSize:

            myRect = wxObject.TheDisplay.GetClientArea(pixels=True)

        elif thePosition == theDefaultPosition:

            myRect = wxRect(wxObject.TheDisplay.ClientArea.x,
                            wxObject.TheDisplay.ClientArea.y,
                            theSize.width,
                            theSize.height)

        elif theSize == theDefaultSize:

            theDisplaySize = wxSize(
                wxObject.TheDisplay.ClientArea.width,
                wxObject.TheDisplay.ClientArea.height)

            myRect = wxRect(
                thePosition.x,
                thePosition.y,
                theDisplaySize.width - thePosition.x,
                theDisplaySize.height - thePosition.y)

        else:

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

            theDisplayRect = wxObject.TheDisplay.GetClientArea()
            if not theDisplayRect.InsideRect(myRect):
                myRect = wxRect(
                    max(thePosition.x, theDisplayRect.x),
                    max(thePosition.y, theDisplayRect.y),
                    min(theSize.width, theDisplayRect.width),
                    min(theSize.height, theDisplayRect.height - 1))

            if not theDisplayRect.InsideRect(myRect):
                myRect = theDisplayRect

        try:
            if self.ts_MenuBar is None:
                offsetMenuBar = 0
            else:
                offsetMenuBar = (self.ts_MenuBar.Rect.height // \
                                 wx.pixelHeightPerCharacter) * \
                    wx.pixelHeightPerCharacter
        except AttributeError:
            offsetMenuBar = 0

        try:
            if self.ts_StatusBar is None:
                offsetStatusBar = 0
            else:
                offsetStatusBar = ((self.ts_StatusBar.Rect.height // \
                                    wx.pixelHeightPerCharacter) - 1) * \
                    wx.pixelHeightPerCharacter
        except AttributeError:
            offsetStatusBar = 0

        try:
            if self.ts_ToolBar is None:
                offsetToolBar = 0
            else:
                offsetToolBar = (self.ts_ToolBar.Rect.height // \
                                 wx.pixelHeightPerCharacter) * \
                    wx.pixelHeightPerCharacter
        except AttributeError:
            offsetToolBar = 0

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + (theBorder.height + \
                                          offsetMenuBar + \
                                          offsetToolBar),
                              myRect.width - 2 * theBorder.width,
                              myRect.height - (
                                  (2 * theBorder.height) + \
                                  offsetMenuBar + \
                                  offsetToolBar) - \
                              offsetStatusBar)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; title=%s; myRect=%s' % \
            (parent, pos, size, name, self.Title, myRect)

        self.logger.debug('    tsFrameWindowLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsTrapIfTooSmall(self, name, myRect):
        '''
        '''
        # TBD - Under Construction.
        if True:
            return

        minScreenDimensions = wx.ThemeToUse['MinScreenDimensions']
        minScreenWidth = minScreenDimensions['FrameWidth']
        minScreenHeight = minScreenDimensions['FrameHeight'] + \
            minScreenDimensions['MenuBarHeight'] + \
            minScreenDimensions['ToolBarHeight'] + \
            minScreenDimensions['StatusBarHeight'] + \
            minScreenDimensions['RedirectionHeight'] + \
            minScreenDimensions['TaskBarHeight']

        minClientHeight = minScreenDimensions['FrameHeight'] + \
            minScreenDimensions['MenuBarHeight'] + \
            minScreenDimensions['ToolBarHeight'] + \
            minScreenDimensions['StatusBarHeight']

        minWidth = minScreenWidth

        if name == wx.TaskBarNameStr:
            minHeight = minScreenDimensions['TaskBarHeight']

        elif name == wx.StdioNameStr:
            minHeight = minScreenDimensions['RedirectionHeight']

        else:

            minHeight = minClientHeight

        minScreenSize = wxSize(minScreenWidth // wx.pixelWidthPerCharacter,
                               minScreenHeight // wx.pixelHeightPerCharacter)

        mySize = wxSize(myRect.width // wx.pixelWidthPerCharacter,
                        myRect.height // wx.pixelHeightPerCharacter)

        minSize = wxSize(minWidth // wx.pixelWidthPerCharacter,
                         minHeight // wx.pixelHeightPerCharacter)

        actualScreen = wxObject.TheDisplay.GetGeometry(pixels=True)

        actualScreenWidth = actualScreen.width
        actualScreenHeight = actualScreen.height
        actualScreenSize = wxSize(actualScreenWidth, actualScreenHeight)

        if actualScreenSize.width < minScreenSize.width:

            fmt = '  Screen "%s" width (%d) is too small.' + \
                ' Please make screen at least (%d) columns'
            abortMsg = fmt % (wxObject.TheDisplay.Name,
                              actualScreenSize.width,
                              minScreenSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if actualScreenSize.height < minScreenSize.height:

            fmt = '  Screen "%s" height (%d) is too small.' + \
                ' Please make screen at least (%d) lines'
            abortMsg = fmt % (wxObject.TheDisplay.Name,
                              actualScreenSize.height,
                              minScreenSize.height)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if mySize.width < minSize.width:

            fmt = '  Window "%s" width (%d) is too small.' + \
                ' Please make screen at least (%d) columns'
            abortMsg = fmt % (name, mySize.width, minSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if mySize.height < minSize.height:

            fmt = '  Window "%s" height (%d) is too small.' + \
                ' Please make screen at least (%d) lines'
            abortMsg = fmt % (name, mySize.height, minSize.height)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Frame specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:
                self.Create(self.ts_Parent,
                            id=self.ts_AssignedId,
                            pos=(self.Position.x, self.Position.y),
                            size=(self.Size.width, self.Size.height),
                            style=self.ts_Style,
                            name=self.ts_Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

            if False:
                # TBD - Remove
                try:
                    self.ts_FocusFromKbd = self
                    self.SetFocusFromKbd()
                except Exception as e:
                    msg = 'tsShow: Exception=%s' % str(e)
                    self.logger.error(msg)

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Frame.
        '''
        if self.tsIsShowPermitted:

            tempRect = self.ts_Rect
            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()

                if self.ts_Style & wx.CAPTION:
                    self.tsCreateTitleLine(self.ts_Title)

                panel = self
                panelRect = panel.ts_Rect
                self.logger.wxASSERT_MSG(
                    (panelRect == tempRect),
                    '%s != %s' % (str(panelRect), str(tempRect)))
                # Blinking cursor must not erase top right corner.
                buttonBarIndent = (
                    len(ButtonBar) + 2) * wx.pixelWidthPerCharacter

                # TBD - Why assume that all resizing buttons should be displayed?
                if self.ts_Style & (
                    wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.CLOSE_BOX):

                    self.logger.wxASSERT_MSG(
                        (panelRect.y == tempRect.y),
                        '%s != %s' % (str(panelRect.y), str(tempRect.y)))

                    self.tsCreateButtonBar(
                        panel,
                        xPos=self.ts_Rect.Right - buttonBarIndent,
                        yPos=self.ts_Rect.Top)

                # TBD - How can fields be updated?
    ##            theStatusBar = self.GetStatusBar()
    ##            if theStatusBar is not None:
    ##                theStatusBar._tsUpdateStatusText()

        return (self.ts_Handle is not None)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ClientArea = property(tsGetClientArea)
    MenuBar = property(GetMenuBar, SetMenuBar)
    StatusBar = property(GetStatusBar, SetStatusBar)
    StatusBarPane = property(GetStatusBarPane, SetStatusBarPane)
    ToolBar = property(GetToolBar, SetToolBar)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
