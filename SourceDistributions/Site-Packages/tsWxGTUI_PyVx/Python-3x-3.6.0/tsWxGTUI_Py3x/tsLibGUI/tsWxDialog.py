#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:48:37 AM rsg>"
'''
tsWxDialog.py - Class to create a dialog box, a window with a
title bar and sometimes a system menu, which can be moved around
the screen. It can contain controls and other windows and is
often used to allow the user to make some choice or to answer
a question.
'''
#################################################################
#
# File: tsWxDialog.py
#
# Purpose:
#
#    Class to create a dialog box, a window with a title bar
#    and sometimes a system menu, which can be moved around
#    the screen. It can contain controls and other windows and is
#    often used to allow the user to make some choice or to answer
#    a question.
#
# Usage (example):
#
#    # Import
#
#    from tsWxDialog import Dialog
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
#    2010/08/27 rsg Initiatialized self.ts_SystemEventTable
#                   and self.ts_UserEventTable to
#                   reflect active buttons (HelpButton,
#                   and CloseButton).
#
#    2010/10/03 rsg Moved instance variables for the top-level
#                   buttons (OnClose, OnMaximize, OnMinimize and
#                   OnRestore).
#
#    2011/03/22 rsg Replaced all references to tsWindowlayout
#                   by references to tsDialogWindowLayout.
#
#    2011/03/22 rsg Modified tsDialogWindowLayout to test if
#                   pos and size are both default values.
#
#    2010/10/25 rsg Updated layout in tsGetClientArea to
#                   recognize changes such as post-creation
#                   re-sizing, centering or addition of menu
#                   bar, tool bar and status bar.
#
#    2011/12/26 rsg Added logic to tsDialogWindowLayout to
#                   inhibit operation once self.ts_Handle has
#                   been assigned a curses window identifier.
#
#    2012/05/02 rsg Added self.ts_DescendantOrderOfShow to
#                   register the order of show of for this
#                   top level window and its descendants.
#
#    2012/06/26 rsg Updated description to include both frame
#                   and dialog objects since the top-level
#                   object for at least one wxPython demo is
#                   a dialog rather than a frame.
#
# ToDo:
#
#    2012/06/05 rsg Add logic to ShowModal that creates and
#                   activates the dialog-specific event loop.
#
#    2012/06/05 rsg Add logic to EndModal that de-activates
#                   the dialog-specific event loop.
#
#    2012/07/05 rsg Investigate need for CheckIfCanBeUsedAsParent
#                   and GetParentForModalDialog methods that
#                   are defined in DialogBase class and used in
#                   Dialog class when modal style is applied.
#
#################################################################

__title__     = 'tsWxDialog'
__version__   = '1.7.0'
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

from tsWxGTUI_Py3x.tsLibGUI.tsWxDoubleLinkedList \
     import DoubleLinkedList as wxDoubleLinkedList
from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py3x.tsLibGUI.tsWxAcceleratorEntry \
     import AcceleratorEntry as wxAcceleratorEntry
from tsWxGTUI_Py3x.tsLibGUI.tsWxAcceleratorTable \
     import AcceleratorTable as wxAcceleratorTable
from tsWxGTUI_Py3x.tsLibGUI.tsWxDialogButton import DialogButton as wxButton
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py3x.tsLibGUI.tsWxTopLevelWindow import TopLevelWindow

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

ButtonBar               = wx.ThemeToUse['Dialog']['ButtonBarDefault']
CloseButtonLabel        = wx.ThemeToUse['Dialog']['CloseButtonLabel']
HelpButtonLabel         = wx.ThemeToUse['Dialog']['HelpButtonLabel']
IconizeButtonLabel      = wx.ThemeToUse['Dialog']['IconizeButtonLabel']
MaximizeButtonLabel     = wx.ThemeToUse['Dialog']['MaximizeButtonLabel']
RestoreDownButtonLabel  = wx.ThemeToUse['Dialog']['RestoreDownButtonLabel']

#---------------------------------------------------------------------------

class Dialog(TopLevelWindow):
    '''
    Class to create a dialog box, a window with a title bar and
    sometimes a system menu, which can be moved around the screen.
    It can contain controls and other windows and is often used
    to allow the user to make some choice or to answer a question.

    Dialogs can be made scrollable, automatically, for computers
    with low resolution screens: please see Automatic scrolling
    dialogs for further details.

    Dialogs usually contains either a single button allowing to
    close the dialog or two buttons, one accepting the changes and
    the other one discarding them (such button, if present, is
    automatically activated if the user presses the "Esc" key).
    By default, buttons with the standard wxID_OK and wxID_CANCEL
    identifiers behave as expected. Starting with wxWidgets 2.7
    it is also possible to use a button with a different identifier
    instead, see SetAffirmativeId() and SetEscapeId().

    Also notice that the CreateButtonSizer() should be used to create
    the buttons appropriate for the current platform and positioned
    correctly (including their order which is platform-dependent).
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_DIALOG_STYLE,
                 name=wx.DialogNameStr):
        '''
        '''
        theClass = 'Dialog'

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

        self.ts_oldFocus = None
        self.ts_isShown = False
        self.ts_modalData = None
        self.ts_endModalCalled = False
        self.ts_dialogToolBar = None

        self.ts_ButtonSizerFlags = 32926
        self.ts_returnCode = 0
        self.ts_sizeSet = False
        self.ts_modalShowing = False
        self.ts_themeEnabled = True

        myRect, myClientRect = self.tsDialogWindowLayout(
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

        self.ts_Name = name
        self.ts_Parent = parent

        self.ts_IdleTimeQueue = wxDoubleLinkedList(lifoMode=False)
        self.ts_RealTimeQueue = wxDoubleLinkedList(lifoMode=False)

        self.ts_DescendantOrderOfShow = [self.ts_AssignedId]

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        if True:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'Dialog']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'Dialog']['ForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()

##        self.ts_FocusEnabled = True
        self.SetFocus()

        self.ts_Label = title
        self.ts_Style = style
        self.ts_Title = title

        self.ts_defaultDialogAcceleratorEntries = {
            '?': {'name': 'OnHelp',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('?'),
                  'cmdID': wx.ID_ANY},
            'X': {'name': 'OnClose',
                  'flags': wx.ACCEL_ALT,
                  'keyCode': ord('X'),
                  'cmdID': wx.ID_ANY}
            }

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
               id=wx.ID_ANY,
               title=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.DEFAULT_DIALOG_STYLE,
               name=wx.DialogNameStr,
               pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        # self.SetExtraStyle(self.GetExtraStyle() | wx.TOPLEVEL_EX_DIALOG

        # Save focus before doing anything which can potentially change it
##        self.ts_oldFocus = self.FindFocus()

        # All dialogs should really have this style
        style |= wx.TAB_TRAVERSAL

##        if !wx.TopLevelWindow.Create(parent,
##                                     id,
##                                     title,
##                                     pos,
##                                     size,
##                                     style,
##                                     name):
##            return False;

##        if self.ts_hasFont:
##            self.SetFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))

        # if defined(__SMARTPHONE__) && defined(__WXWINCE__)
        #     SetLeftMenu(wxID_OK, _("OK"));
        #
        # if wxUSE_TOOLBAR && defined(__POCKETPC__)
        #     self.CreateToolBar()
        #

        (myRect, myClientRect) = self.tsDialogWindowLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def CreateButtonSizer(self, flags, *ignored):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'CreateButtonSizer in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def CreateSeparatedButtonSizer(self, flags):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'CreateSeparatedButtonSizer in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        Sizer = None
##        return Sizer

    #-----------------------------------------------------------------------

    def CreateStdDialogButtonSizer(self, flags):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'CreateStdDialogButtonSizer in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        StdDialogButtonSizer = None
##        return StdDialogButtonSizer

    #-----------------------------------------------------------------------
 
    def CreateTextSizer(self, message):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'CreateTextSizer in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        Sizer = None
##        return Sizer

    #-----------------------------------------------------------------------

    def EndModal(self, retCode):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'EndModal in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##{
##    SetReturnCode( retCode );

##    if (!IsModal())
##    {
##        wxFAIL_MSG( wxT("wxDialog:EndModal called twice") );
##        return;
##    }

##    m_modalShowing = False;

##    gtk_main_quit();

##    Show( False );
##}

##        pass

    #-----------------------------------------------------------------------

    def GetAffirmativeId(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'GetAffirmativeId in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return int

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        users system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See wx.Window.SetWindowVariant for more about this.
        '''
        msg = 'NotImplementedError: %s' % \
              'GetClassDefaultAttributes in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (0)

    #-----------------------------------------------------------------------

    def GetEscapeId(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'GetEscapeId in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return int

    #-----------------------------------------------------------------------

##    # class DialogBase(TopLevelWindow):
##    def CheckIfCanBeUsedAsParent(self, parent):
##        '''
##        '''
##        if (parent is None):
##            return (None)

##        extern WXDLLIMPEXP_DATA_BASE(wxList) wxPendingDelete;
##        if ( wxPendingDelete.Member(parent) || parent->IsBeingDeleted() )
##        {
##            // this window is being deleted and we shouldn't create any children
##            // under it
##            return NULL;
##        }

##        if ( parent->HasExtraStyle(wxWS_EX_TRANSIENT) )
##        {
##            // this window is not being deleted yet but it's going to disappear
##            // soon so still don't parent this window under it
##            return NULL;
##        }

##        if ( !parent->IsShownOnScreen() )
##        {
##            // using hidden parent won't work correctly neither
##            return NULL;
##        }

##        // FIXME-VC6: this compiler requires an explicit const cast or it fails
##        //            with error C2446
##        if ( const_cast<const wxWindow *>(parent) == this )
##        {
##            // not sure if this can really happen but it doesn't hurt to guard
##            // against this clearly invalid situation
##            return NULL;
##        }

##        return parent;
##    }

    #-----------------------------------------------------------------------
    # class DialogBase(TopLevelWindow):
##    def GetParentForModalDialog(self, parent, style):
##        '''
##        Creating a parent-less modal dialog will result (under e.g. wxGTK2)
##        in an unfocused dialog, so try to find a valid parent for it unless
##        we were explicitly asked not to.
##        '''
##        if (style & wx.DIALOG_NO_PARENT):
##            return (None)

##        # first try the given parent
##        if (not (parent is None)):
##            parent = self.CheckIfCanBeUsedAsParent(
##                self.GetTopLevelParent(parent))

##        # then the currently active window
##        if (parent is None):
##            parent = self.CheckIfCanBeUsedAsParent(
##                self.GetTopLevelParent(self.GetActiveWindow()))

##        # and finally the application main window
##        if (parent is None)
##            parent = CheckIfCanBeUsedAsParent(wxTheApp.GetTopWindow())

##        return (parent)

    #-----------------------------------------------------------------------

    def GetReturnCode(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'GetReturnCode in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return int

    #-----------------------------------------------------------------------

    def IsModal(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'IsModal in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##        return (self.ts_modalShowing)

    #-----------------------------------------------------------------------

    def SetAffirmativeId(self, affirmativeId):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'SetAffirmativeId in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def SetEscapeId(self, escapeId):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'SetEscapeId in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetReturnCode(self, returnCode):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'SetReturnCode in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ShowModal(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxDialog'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
##      if self.IsModal():

##           self.logger.wxFAIL_MSG('tsWxDialog.ShowModal called twice')
##           return self.GetReturnCode()

##    // use the apps top level window as parent if none given unless explicitly
##    // forbidden
##    if ( !GetParent() && !(GetWindowStyleFlag() & wxDIALOG_NO_PARENT) )
##    {
##        extern WXDLLIMPEXP_DATA_CORE(wxList) wxPendingDelete;

##        wxWindow * const parent = wxTheApp->GetTopWindow();

##        if ( parent &&
##                parent != this &&
##                    parent->IsShownOnScreen() &&
##                        !parent->IsBeingDeleted() &&
##                            !wxPendingDelete.Member(parent) &&
##                                !(parent->GetExtraStyle() & wxWS_EX_TRANSIENT) )
##        {
##            m_parent = parent;
##            gtk_window_set_transient_for( GTK_WINDOW(m_widget),
##                                          GTK_WINDOW(parent->m_widget) );
##        }
##    }

##    wxBusyCursorSuspender cs; // temporarily suppress the busy cursor

##    Show( True );

##    m_modalShowing = True;

##    g_openDialogs++;

##    // NOTE: gtk_window_set_modal internally calls gtk_grab_add() !
##    gtk_window_set_modal(GTK_WINDOW(m_widget), True);

##    wxEventLoop().Run();

##    gtk_window_set_modal(GTK_WINDOW(m_widget), False);

##    g_openDialogs--;

##    return GetReturnCode();
##}
##        return int

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsButtonData(self):
        '''
        Define the label and handler for the Iconize, Maximize and Close
        Buttons on the Frame Title Line.

        Based on "wxPython In Action" by Noel Rappin and Robin Dunn,
        Manning Publications Co. (See downloaded source code located in
        Chapter-05, goodExampple.py.)
        '''
        if self.ts_Rect.TopLeft == self.display.ClientArea.TopLeft and \
           self.ts_Rect.BottomRight == self.display.ClientArea.BottomRight:
            # Full Screen; Show "RestoreDown" instead of "Maximize" Button
            return (('&?\tCtrl-?',
                     EVT_COMMAND_LEFT_CLICK, # EVT_HELP,
                     None, # self.tsOnHelpClick,
                     'HelpButton(%s)' %self.ts_Name),
                    ('&X\tCtrl-X',
                     EVT_COMMAND_LEFT_CLICK, # EVT_CLOSE,
                     None, # self.tsOnCloseClick,
                     'CloseButton(%s)' %self.ts_Name))
        else:
            # Not Full Screen; Show "Maximize" Button
            return (('&?\tCtrl-?',
                     EVT_COMMAND_LEFT_CLICK, # EVT_HELP,
                     None, # self.tsOnHelpClick,
                     'HelpButton(%s)' %self.ts_Name),
                    ('&X\tCtrl-X',
                     EVT_COMMAND_LEFT_CLICK, # EVT_CLOSE,
                     None, # self.tsOnCloseClick,
                     'CloseButton(%s)' %self.ts_Name))

    #-----------------------------------------------------------------------

    def tsBuildOneButton(self,
                         parent,
                         label=None,
                         event=None,
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

        return (button)

    #-----------------------------------------------------------------------

    def tsCreateButtonBar(self, panel, xPos=0, yPos=0):
        '''
        Create the collection of Dialog Buttons located on the Dialog Title
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

##            # Bind mouse event ASAP (now).
##            # Will register event in the SystemEventTable
##            # if useSystemEventTable=True.
##            self.Bind(theEvent,
##                      theHandler,
##                      button,
##                      useSystemEventTable=True)

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

            theButtons += [button]

##            myRect = button.Rect
##            xPos += myRect.width - 1 * wx.pixelWidthPerCharacter
##            self.logger.debug('tsCreateButtonBar: myRect=%s' % str(myRect))
            xPos += button.GetSize().width - 1 * wx.pixelWidthPerCharacter

    #-----------------------------------------------------------------------

    def tsGetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the Dialog.
        '''
        parent = self.ts_Parent
        pos = wxPoint(self.ts_Rect.x, self.ts_Rect.y)
        size = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        style = self.ts_Style
        name = self.ts_Name

        (myRect, myClientRect) = self.tsDialogWindowLayout(
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

    def tsDialogWindowLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of dialog based upon arguments.
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

        if thePosition == theDefaultPosition and \
           theSize == theDefaultSize:

            if parent is None:

##                myRect = wxRect(self.display.ClientArea.x,
##                                self.display.ClientArea.y,
##                                self.display.ClientArea.width,
##                                self.display.ClientArea.height)
                myRect = self.display.ClientArea

            else:

                myRect = parent.GetClientArea(pixels=True)

        elif thePosition == theDefaultPosition:

            myRect = wxRect(self.display.ClientArea.x,
                            self.display.ClientArea.y,
                            theSize.width,
                            theSize.height)

        elif theSize == theDefaultSize:

            theDisplaySize = wxSize(
                self.display.ClientArea.width,
                self.display.ClientArea.height)

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

            theDisplayRect = self.display.GetClientArea()
            if not theDisplayRect.InsideRect(myRect):
                myRect = wxRect(
                    max(thePosition.x, theDisplayRect.x),
                    max(thePosition.y, theDisplayRect.y),
                    min(theSize.width, theDisplayRect.width),
                    min(theSize.height, theDisplayRect.height - 1))

            if not theDisplayRect.InsideRect(myRect):
                myRect = theDisplayRect

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + theBorder.height,
                              myRect.width - 2 * theBorder.width,
                              myRect.height - 2 * theBorder.height)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; title=%s; myRect=%s' % \
              (parent, pos, size, name, self.Title, myRect)

        self.logger.debug('    tsDialogWindowLayout: %s' % msg)

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

        actualScreen = self.display.GetGeometry(pixels=True)
 
        actualScreenWidth = actualScreen.width
        actualScreenHeight = actualScreen.height
        actualScreenSize = wxSize(actualScreenWidth, actualScreenHeight)

        if actualScreenSize.width < minScreenSize.width:

            fmt = '  Screen "%s" width (%d) is too small.' + \
                  ' Please make screen at least (%d) columns'
            abortMsg = fmt % (self.display.Name,
                              actualScreenSize.width,
                              minScreenSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if actualScreenSize.height < minScreenSize.height:

            fmt = '  Screen "%s" height (%d) is too small.' + \
                  ' Please make screen at least (%d) lines'
            abortMsg = fmt % (self.display.Name,
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
 
    def tsUpdate(self):
        '''
        Draw the actual features of the Dialog.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()

                if self.ts_Style & wx.CAPTION:
                    self.tsCreateTitleLine(self.ts_Title)

                panel = self
                # Blinking cursor must not erase top right corner.
                buttonBarIndent = (
                    len(ButtonBar) + 2) * wx.pixelWidthPerCharacter

                # TBD - Why assume that all resizing buttons should be displayed?
                if self.ts_Style & (
                    wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.CLOSE_BOX):
                    self.tsCreateButtonBar(
                        panel,
                        xPos=self.ts_Rect.Right - buttonBarIndent,
                        yPos=self.ts_Rect.Top)

        return (self.ts_Handle is not None)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    AffirmativeId = property(GetAffirmativeId, SetAffirmativeId)
    ClientArea = property(tsGetClientArea)
    EscapeId = property(GetEscapeId, SetEscapeId)
    ReturnCode = property(GetReturnCode, SetReturnCode)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
