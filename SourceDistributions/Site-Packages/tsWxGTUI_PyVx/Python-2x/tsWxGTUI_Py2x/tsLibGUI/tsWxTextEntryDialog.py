#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:47:18 AM rsg>"
'''
tsWxTextEntryDialog.py - Class represents a dialog that requests
a one-line text string from the user.
'''
#################################################################
#
# File: tsWxTextEntryDialog.py
#
# Purpose:
#
#    Class represents a dialog that requests a one-line text
#    string from the user.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTextEntryDialog import TextEntryDialog
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
#    2012/07/21 rsg Added TextEntryBox class and associated
#                   methods.
#
#    2012/07/28 rsg Added evt argument to each tsOn<event>.
#
#    2012/08/10 rsg Replaced tsWxTextEntryBox internal class by
#                   import of equivalent tsWxTextEditBox external
#                   class.
#
# ToDo:
#
#    2012/08/11 rsg Investigate corrective actions for
#                   tsWxTextEditBox:
#
#                   nonEventDrivenMode uses curses.textpad.Textbox;
#                   application automatically blocked pending
#                   operator terminating input via control G;
#                   however, operator may enter new string after
#                   terminating input via control G.
#
#                   eventDrivenMode uses TextEditBox.TextBox;
#                   application has no mechanism to block pending
#                   operator terminating input via control G or
#                   mouse button click; however, operator may
#                   enter new string after terminating input via
#                   control G; also, application does not receive
#                   answer string.
#
#################################################################

__title__     = 'tsWxTextEntryDialog'
__version__   = '1.2.0'
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

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py2x.tsLibGUI import tsWxEvtHandler
from tsWxGTUI_Py2x.tsLibGUI import tsWxStaticText

from tsWxGTUI_Py2x.tsLibGUI.tsWxBoxSizer import BoxSizer as wxBoxSizer
from tsWxGTUI_Py2x.tsLibGUI.tsWxButton import Button as wxButton
from tsWxGTUI_Py2x.tsLibGUI.tsWxDialog import Dialog
from tsWxGTUI_Py2x.tsLibGUI.tsWxDoubleLinkedList \
     import DoubleLinkedList as wxDoubleLinkedList
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxPanel import Panel as wxPanel
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxStaticLine import StaticLine as wxStaticLine
from tsWxGTUI_Py2x.tsLibGUI.tsWxTextEditBox import TextEditBox as wxTextEditBox

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class TextEntryDialog(Dialog):
    '''
    Class represents a dialog that requests a one-line text string
    from the user.
    '''
    def __init__(self,
                 parent,                 # Should be None unless modal mode
                 message,                # Alias for user prompt output
                 caption=wx.EmptyString, # Alias for title
                 value=wx.EmptyString,   # Option for default user input
                 style=wx.TEXT_ENTRY_DIALOG_STYLE, # Options for ClientRect
                 size=wx.DefaultSize,    # Extension for application use
                 pos=wx.DefaultPosition  # Option for application use
                 ):
        '''
        Use ShowModal() to show the dialog.

        Parameters:

        parent  Parent window.

        message Message to show on the dialog.

        caption The caption of the dialog.

        value   The default value, which may be the empty string.

        style   A dialog style, specifying the buttons (wxOK, wxCANCEL)
                and an optional wxCENTRE style. Additionally, wxTextCtrl
                styles (such as wxTE_PASSWORD or wxTE_MULTILINE) may be
                specified here.

        pos     Dialog position.
        '''
        theClass = 'TextEntryDialog'

        # Capture initial caller parametsrs before Dialog makes changes
        self.backup_parent = parent
        self.backup_message = message
        self.backup_caption = caption
        self.backup_value = value
        self.backup_style = style
        self.backup_size = size
        self.backup_pos = pos

        name = wx.TextEntryDialogNameStr
        title = caption
        self.backup_name = name
        self.backup_size = size
        self.backup_title = title

        # Capture initial caller parametsrs before they are changed
        self.caller_caption = caption
        self.caller_message = message
        self.caller_name = name
        self.caller_parent = parent
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_title = title
        self.caller_value = value

        wx.RegisterFirstCallerClassName(self, theClass)

        Dialog.__init__(self,
                        parent, # self.GetParentForModalDialog(parent, style),
                        id=wx.ID_ANY,
                        title=title,
                        pos=pos,
                        size=size,
                        # Apply Default Dialog Style to Top-Level Window
                        # (defer TextEntryDialog style for internal layout)
                        style=wx.DEFAULT_DIALOG_STYLE,
                        name=name)

        # Capture parameters.
        self.ts_Caption = self.backup_caption
        self.ts_Message = self.backup_message
        self.ts_Parent = self.backup_parent    # Should be None unless modal mode
        self.ts_Pos = self.backup_pos
        self.ts_Size = self.backup_size
        self.ts_Style = self.backup_style
        self.ts_Title = self.backup_title
        self.ts_Value = self.backup_value

        self.ts_Completion = False
        self.ts_PasswordMode = False
        self.ts_StripSpaces = False

##        (self.ts_Rect,
##         self.ts_ClientRect) = self.tsTextEntryDialogLayout(
##             parent, pos, size, style, caption)

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

        if True:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'TextEntryDialog']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'TextEntryDialog']['ForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'Dialog']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'Dialog']['ForegroundColour'].lower()

        self.ts_ButtonSeparatorLine = wx.ThemeToUse[
            'TextEntryDialog']['ButtonSeparatorLine']

        self.ts_TextEntryStripSpaces = wx.ThemeToUse[
            'TextEntryDialog']['StripSpaces']

        self.ts_TextPad = None
        self.ts_IdleTimeQueue = wxDoubleLinkedList(lifoMode=False)
        self.ts_RealTimeQueue = wxDoubleLinkedList(lifoMode=False)

        self.ts_DescendantOrderOfShow = [self.ts_AssignedId]

        # The following redefines the usage of the style wx.CENTRE.
        # Intended only to govern the alignment of the buttons within
        # the dialog, we also apply it the centering of the dialog
        # itself within the desktop because the layout process cannot
        # wait for the application to initiate centering.
        if (self.ts_Style & wx.CENTRE) == wx.CENTRE:

            if DEBUG:

                msg = 'tsWxTextEntryDialog.__init__: ' + \
                      'Proceeding with tsDialogFeatureLayout. ' + \
                      'Style contains wx.CENTRE.'
                self.logger.debug(msg)
                print('DEBUG: %s\n' % msg)

            self.Center()

            self.theButtons = None
            self.theCancelButton = None
            self.theLine = None
            self.theMessage = None
            self.theOkButton = None
            self.theSpacer = None
            self.theTextBox = None
            self.theValue = None

            self.ts_TextPad = self.tsDialogFeatureLayout()

            self.Show()

        else:

            msg = 'tsWxTextEntryDialog.__init__: ' + \
                  'Skipped tsDialogFeatureLayout. ' + \
                  'Style did NOT contain wx.CENTRE.'
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)

        self.ts_ButtonUserPressed = wx.ID_CANCEL

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def GetValue(self):
        '''
        Returns the text that the user has entered if the user has pressed
        OK, or the original value if the user has pressed Cancel.
        '''
        self.ts_ButtonUserPressed = wx.ID_CANCEL

        # Wait for input terminated by Enter or by OkButtonClick
        ## self.tsRegisterKeyboardInputOrder()

        response = self.tsCursesTextpadEdit(self.ts_TextPad, None)

        ## self.tsUnRegisterKeyboardInputOrder()

        if wx.ThemeToUse['TextEntryDialog']['StripSpaces']:

            self.ts_Value = response.strip()

        else:

            self.ts_Value = response

        if False and DEBUG:

            msg = 'tsWxTextEntryDialog.GetValue: ' + \
                  'response="%s"; self.ts_Value="%s"' % (
                      str(response), self.ts_Value)
            print('NOTICE: %s\n' % msg)

        return (self.ts_Value)

    #-----------------------------------------------------------------------

    def tsOnCancelButtonClick(self, evt):
        '''
        '''
        self.ts_ButtonUserPressed = wx.ID_CANCEL

        if False and DEBUG:

            msg = 'tsWxTextEntryDialog.tsOnCancelButtonClick: ' + \
                  'self.ts_Value="%s"' % self.ts_Value
            print('NOTICE: %s\n' % msg)

        return (self.ts_Value)

    #-----------------------------------------------------------------------

    def tsOnOkButtonClick(self, evt):
        '''
        '''
        self.ts_ButtonUserPressed = wx.ID_OK

        if wx.ThemeToUse['TextEntryDialog']['StripSpaces']:

            self.ts_Value = self.tsCursesTextpadGather(self.ts_TextPad).strip()

        else:

            self.ts_Value = self.tsCursesTextpadGather(self.ts_TextPad)

        if False and DEBUG:

            msg = 'tsWxTextEntryDialog.tsOnOkButtonClick: ' + \
                  'self.ts_Value="%s"' % self.ts_Value
            print('NOTICE: %s\n' % msg)

        return (self.ts_Value)

    #-----------------------------------------------------------------------

    def SetValue(self, value):
        '''
        Sets the default text value.
        '''
        self.ts_Value = value

        if False and DEBUG:

            msg = 'tsWxTextEntryDialog.SetValue: ' + \
                  'self.ts_Value="%s"' % self.ts_Value
            print('NOTICE: %s\n' % msg)

    #-----------------------------------------------------------------------

    def ShowModal(self):
        '''
        Shows the dialog, returning wx.ID_OK if the user pressed OK,
        and wx.ID_CANCEL otherwise.
        '''
##        msg = 'tsWxTextEntryDialog.ShowModal: ' + \
##              'NotImplementedErro'
##        print(msg)

        self.GetValue()

        return (wx.ID_OK)

##        self.Show()

##        return (self.ts_ButtonUserPressed)

##        msg = 'NotImplementedError: %s' % \
##              'ShowModal in tsWxDialog'
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

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

    #-----------------------------------------------------------------------

    def tsTextEntryDialogLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of dialog based upon arguments.
        '''
        # Example Layout (wxPython TextEntryDialog)
        #
        #   Key:
        #       Caption = "Eh?"
        #       Message = "What is your favorite programming language?"
        #       Value   = "Python is the best!"
        #       Buttons = "OK" and "Cancel"
        #
        #   Layout:
        #       Title    = Caption
        #       VSizer1  = Message Line(s)
        #       VSizer2  = Value Line(s)
        #       VSizer3  = Horizontal Separator (TextLine)
        #       VSizer4  = Button(s)
        #       HSizer1  = Spacer (variable size)
        #       HSizer2  = OK Button (fixed size)
        #       HSizer3  = Cancel Button (fixed size)
        #
        # wxPython-Style (pixel-mode)
        #
        # +---------------------------------------------------------+
        # | Caption                                              [X]|
        # +---------------------------------------------------------+
        # | What is your favorite programming language?             |
        # |  +---------------------------------------------------+  |
        # |  |Python is the best!                                |  |
        # |  +---------------------------------------------------+  |
        # | ------------------------------------------------------- |
        # |                              +----------+ +----------+  |
        # |                              [    OK    ] [  Cancel  ]  |
        # |                              +----------+ +----------+  |
        # +---------------------------------------------------------+
        #
        # tsWxGTUI-Style (character-mode)
        #
        # +- Caption -------------------------------------- [?][X] -+
        # +---------------------------------------------------------+
        # | What is your favorite programming language?             |
        # |  +---------------------------------------------------+  |
        # |  |Python is the best!                                |  |
        # |  +---------------------------------------------------+  |
        # | ------------------------------------------------------- |
        # |                              [    OK    ] [  Cancel  ]  |
        # +---------------------------------------------------------+
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

                myRect = wxRect(self.display.ClientArea.x,
                                self.display.ClientArea.y,
                                self.display.ClientArea.width,
                                self.display.ClientArea.height)
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

        self.logger.debug('tsTextEntryDialog.' + \
                          'tsTextEntryDialogLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsDialogFeatureLayout(self):
        '''
        '''
        # Example Layout (wxPython TextEntryDialog)
        #
        #   Key:
        #       Caption = "Eh?"
        #       Message = "What is your favorite programming language?"
        #       Value   = "Python is the best!"
        #       Buttons = "OK" and "Cancel"
        #
        #   Layout:
        #       Title    = Caption
        #       VSizer1  = Message Line(s)
        #       VSizer2  = Value Line(s)
        #       VSizer3  = Horizontal Separator (TextLine)
        #       VSizer4  = Button(s)
        #       HSizer1  = Spacer (variable size)
        #       HSizer2  = OK Button (fixed size)
        #       HSizer3  = Cancel Button (fixed size)
        #
        # wxPython-Style (12-row pixel-mode)
        #
        # +---------------------------------------------------------+
        # | Caption                                              [X]|
        # +---------------------------------------------------------+
        # | What is your favorite programming language?             |
        # |  +---------------------------------------------------+  |
        # |  |Python is the best!                                |  |
        # |  +---------------------------------------------------+  |
        # | ------------------------------------------------------- |
        # |                              +----------+ +----------+  |
        # |                              [    OK    ] [  Cancel  ]  |
        # |                              +----------+ +----------+  |
        # +---------------------------------------------------------+
        #
        # tsWxGTUI-Style (9-row, ButtonSeparatorLine character-mode)
        #
        # +- Caption -------------------------------------- [?][X] -+
        # +---------------------------------------------------------+
        # | What is your favorite programming language?             |
        # |  +---------------------------------------------------+  |
        # |  |Python is the best!                                |  |
        # |  +---------------------------------------------------+  |
        # | ------------------------------------------------------- |
        # |                              [    OK    ] [  Cancel  ]  |
        # +---------------------------------------------------------+
        #
        # tsWxGTUI-Style (8-row, non-ButtonSeparatorLine character-mode)
        #
        # +- Caption -------------------------------------- [?][X] -+
        # +---------------------------------------------------------+
        # | What is your favorite programming language?             |
        # |  +---------------------------------------------------+  |
        # |  |Python is the best!                                |  |
        # |  +---------------------------------------------------+  |
        # |                              [    OK    ] [  Cancel  ]  |
        # +---------------------------------------------------------+
##        wxBeginBusyCursor();

        theDialog = self

        theContainer = wxPanel(
            theDialog,
            id=wx.ID_ANY,
            label=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.BORDER_NONE,
##            style=0,
            name=wx.PanelNameStr)

        #-------------------------------------------------------------------

        theVerticalSizer = wxBoxSizer(wx.VERTICAL)

        self.theMessage = wxPanel(
            theContainer,
            wx.ID_ANY,
            label=self.ts_Message,
            style=0)

        self.theValue = wxPanel(
            theContainer,
            wx.ID_ANY,
            style=wx.BORDER_SIMPLE)

        if True:
            self.theValue.ts_BackgroundColour = wx.ThemeToUse[
                'TextEntryDialog']['TextBoxBackgroundColour'].lower()
            self.theValue.ts_ForegroundColour = wx.ThemeToUse[
                'TextEntryDialog']['TextBoxForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'Dialog']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'Dialog']['ForegroundColour'].lower()

        if False and self.ts_ButtonSeparatorLine:

            self.theLine = wxStaticLine(
                theContainer,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.LI_HORIZONTAL,
                validator=wx.DefaultValidator,
                name=wx.StaticLineNameStr)

        self.theButtons = wxPanel(
            theContainer,
            wx.ID_ANY,
            style=0)

        answerProportion = max(1, theContainer.ClientRect.height // (
            wx.pixelHeightPerCharacter))
        theVerticalSizer.Add(self.theMessage, proportion=1)
        theVerticalSizer.Add(self.theValue, proportion=answerProportion)

        if False and self.ts_ButtonSeparatorLine:

            theVerticalSizer.Add(self.theLine, proportion=1)

        theVerticalSizer.Add(self.theButtons, proportion=1)

        self.SetAutoLayout(True)
        self.SetSizer(theVerticalSizer)
        self.Layout()

        self.Show(show=True)

        #-------------------------------------------------------------------

        theHorizontalSizer = wxBoxSizer(wx.HORIZONTAL)

        self.theSpacer = wxPanel(
            self.theButtons,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=0)

        if (self.ts_Style & wx.OK) == wx.OK:

            self.theOkButton = wxButton(
                self.theButtons,
                id=wx.ID_ANY,
                label='   OK   ',
                # label='OK', # '   OK   ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                useClientArea=True)

            # Automatically Bind all mouse events ASAP (now).
            # Will register event in the SystemEventTable.
            event = EVT_COMMAND_LEFT_CLICK
            handler = self.tsOnOkButtonClick
            source = self.theOkButton
            self.Bind(event,
                      handler,
                      source,
                      useSystemEventTable=True)

        else:

            self.theOkButton = None

        if (self.ts_Style & wx.CANCEL) == wx.CANCEL:

            self.theCancelButton = wxButton(
                self.theButtons,
                id=wx.ID_ANY,
                label=' Cancel ',
                # label='Cancel', # ' Cancel ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                useClientArea=True)

            # Automatically Bind all mouse events ASAP (now).
            # Will register event in the SystemEventTable.
            event = EVT_COMMAND_LEFT_CLICK
            handler = self.tsOnCancelButtonClick
            source = self.theCancelButton
            self.Bind(event,
                      handler,
                      source,
                      useSystemEventTable=True)

        else:

            self.theCancelButton = None

        theHorizontalSizer.Add(self.theSpacer, proportion=2)
        theHorizontalSizer.Add(self.theOkButton,
                               proportion=1)
        theHorizontalSizer.Add(self.theCancelButton,
                               proportion=1)

        self.theButtons.SetAutoLayout(True)
        self.theButtons.SetSizer(theHorizontalSizer)
        self.theButtons.Layout()

        self.theButtons.Show(show=True)

        self.theTextBox = wxTextEditBox(
            self.theValue,
            wx.ID_ANY,
            style=0)

        self.theTextBox.tsSetCompletion(self.ts_Completion)
        self.theTextBox.tsSetPasswordMode(self.ts_PasswordMode)
        self.theTextBox.tsSetStripSpaces(self.ts_StripSpaces)

        self.theTextBox.Show()
        theTextPad = self.theTextBox

        return (theTextPad)

        #-------------------------------------------------------------------

##    #if wxUSE_STATTEXT
##        // 1) text message
##        topsizer.Add(self.CreateTextSizer(message), flagsBorder);
##    #endif

##        // 2) text ctrl
##        self.ts_textctrl = wx.TextCtrl(
##            wx.ID_TEXT, value,
##            wxDefaultPosition,
##            Size(300, wx.DefaultCoord),
##            style & ~wx.TextEntryDialogStyle)

##        topsizer.Add(self.ts_textctrl,
##                     wx.SizerFlags(style & wx.TE_MULTILINE ? 1 : 0).
##                     Expand().
##                     TripleBorder(wxLEFT | wxRIGHT))

##    #if wxUSE_VALIDATORS
##        wxTextValidator validator( wxFILTER_NONE, &m_value );
##        m_textctrl->SetValidator( validator );
##    #endif // wxUSE_VALIDATORS

##        // 3) buttons if any
##        wxSizer *buttonSizer = CreateSeparatedButtonSizer(style & (wxOK | wxCANCEL));
##        if ( buttonSizer )
##        {
##            topsizer->Add(buttonSizer, wxSizerFlags(flagsBorder2).Expand());
##        }

##        SetAutoLayout( true );
##        SetSizer( topsizer );

##        topsizer->SetSizeHints( this );
##        topsizer->Fit( this );

##        if ( style & wxCENTRE )
##            Centre( wxBOTH );

##        m_textctrl->SetSelection(-1, -1);
##        m_textctrl->SetFocus();

##        wxEndBusyCursor();
##    }
##        self.Center()

##        if (self.ts_Style & wx.OK) == wx.OK:

##            self.ts_OnOKButton = wxButton(
##                self,
##                id=wx.ID_ANY,
##                label='OK',
##                pos=(10,10))

##            print('self.ts_OnOKButton = "%s"' % str(
##                self.ts_OnOKButton))
####            self.Bind(wx.EVT_BUTTON, self.OnButton, self.ts_OnOKButton))

##        if (self.ts_Style & wx.CANCEL) == wx.CANCEL:

##            self.ts_OnCancelButton = wxButton(
##                self,
##                id=wx.ID_ANY,
##                label='Cancel',
##                pos=(30,30))
##            print('self.ts_ts_OnCancelButton = "%s"' % str(
##                self.ts_OnCancelButton))
##            self.Bind(wx.EVT_BUTTON, self.OnButton, self.ts_OnOKButton))

##    #-----------------------------------------------------------------------

##    def tsTrapIfTooSmall(self, name, myRect):
##        '''
##        '''
##        # TBD - Under Construction.
##        if True:
##            return

##        minScreenDimensions = wx.ThemeToUse['MinScreenDimensions']
##        minScreenWidth = minScreenDimensions['FrameWidth']
##        minScreenHeight = minScreenDimensions['FrameHeight'] + \
##                          minScreenDimensions['MenuBarHeight'] + \
##                          minScreenDimensions['ToolBarHeight'] + \
##                          minScreenDimensions['StatusBarHeight'] + \
##                          minScreenDimensions['RedirectionHeight'] + \
##                          minScreenDimensions['TaskBarHeight']

##        minClientHeight = minScreenDimensions['FrameHeight'] + \
##                          minScreenDimensions['MenuBarHeight'] + \
##                          minScreenDimensions['ToolBarHeight'] + \
##                          minScreenDimensions['StatusBarHeight']

##        minWidth = minScreenWidth

##        if name == wx.TaskBarNameStr:
##            minHeight = minScreenDimensions['TaskBarHeight']

##        elif name == wx.StdioNameStr:
##            minHeight = minScreenDimensions['RedirectionHeight']

##        else:

##            minHeight = minClientHeight

##        minScreenSize = wxSize(minScreenWidth // wx.pixelWidthPerCharacter,
##                               minScreenHeight // wx.pixelHeightPerCharacter)

##        mySize = wxSize(myRect.width // wx.pixelWidthPerCharacter,
##                        myRect.height // wx.pixelHeightPerCharacter)

##        minSize = wxSize(minWidth // wx.pixelWidthPerCharacter,
##                         minHeight // wx.pixelHeightPerCharacter)

##        actualScreen = self.display.GetGeometry(pixels=True)
 
##        actualScreenWidth = actualScreen.width
##        actualScreenHeight = actualScreen.height
##        actualScreenSize = wxSize(actualScreenWidth, actualScreenHeight)

##        if actualScreenSize.width < minScreenSize.width:

##            fmt = '  Screen "%s" width (%d) is too small.' + \
##                  ' Please make screen at least (%d) columns'
##            abortMsg = fmt % (self.display.Name,
##                              actualScreenSize.width,
##                              minScreenSize.width)

##            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

##            raise tse.UserInterfaceException(
##                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

##        if actualScreenSize.height < minScreenSize.height:

##            fmt = '  Screen "%s" height (%d) is too small.' + \
##                  ' Please make screen at least (%d) lines'
##            abortMsg = fmt % (self.display.Name,
##                              actualScreenSize.height,
##                              minScreenSize.height)

##            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

##            raise tse.UserInterfaceException(
##                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

##        if mySize.width < minSize.width:

##            fmt = '  Window "%s" width (%d) is too small.' + \
##                  ' Please make screen at least (%d) columns'
##            abortMsg = fmt % (name, mySize.width, minSize.width)

##            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

##            raise tse.UserInterfaceException(
##                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

##        if mySize.height < minSize.height:

##            fmt = '  Window "%s" height (%d) is too small.' + \
##                  ' Please make screen at least (%d) lines'
##            abortMsg = fmt % (name, mySize.height, minSize.height)

##            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

##            raise tse.UserInterfaceException(
##                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

##    #-----------------------------------------------------------------------

##    def tsShow(self):
##        '''
##        Create and update Frame specific native GUI.
##        '''
##        if self.ts_Handle is None:
##            self.Create(self.ts_Parent,
##                        id=self.ts_AssignedId,
##                        pos=(self.Position.x, self.Position.y),
##                        size=(self.Size.width, self.Size.height),
##                        style=self.ts_Style,
##                        name=self.ts_Name,
##                        pixels=True)

##        try:
##            self.tsRegisterShowOrder()
##        except Exception, e:
##            self.logger.error('%s; %s' % (__title__, e))

##        self.tsUpdate()

##        if False:
##            # TBD - Remove
##            try:
##                self.ts_FocusFromKbd = self
##                self.SetFocusFromKbd()
##            except Exception, e:
##                msg = 'tsShow: Exception=%s' % str(e)
##                self.logger.error(msg)

##    #-----------------------------------------------------------------------
 
##    def tsUpdate(self):
##        '''
##        Draw the actual features of the Frame.
##        '''
##        tempRect = self.ts_Rect
##        if self.ts_Handle is not None:

##            self.tsCursesScrollOk(0)
##            self.tsCursesBkgd()
##            self.tsCreateBorder()

##            if self.ts_Style & wx.CAPTION:
##                self.tsCreateTitleLine(self.ts_Title)

##            panel = self
##            panelRect = panel.ts_Rect
##            self.logger.wxASSERT_MSG(
##                (panelRect == tempRect),
##                '%s != %s' % (str(panelRect), str(tempRect)))
##            # Blinking cursor must not erase top right corner.
##            buttonBarIndent = (
##                len('[_][Z][X]') + 2) * wx.pixelWidthPerCharacter

##            # TBD - Why assume that all resizing buttons should be displayed?
##            if self.ts_Style & (
##                wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.CLOSE_BOX):

##                self.logger.wxASSERT_MSG(
##                    (panelRect.y == tempRect.y),
##                    '%s != %s' % (str(panelRect.y), str(tempRect.y)))

##                self.tsCreateButtonBar(
##                    panel,
##                    xPos=self.ts_Rect.Right - buttonBarIndent,
##                    yPos=self.ts_Rect.Top)

##            # TBD - How can fields be updated?
####            theStatusBar = self.GetStatusBar()
####            if theStatusBar is not None:
####                theStatusBar._tsUpdateStatusText()

##        return (self.ts_Handle is not None)

##    # End tsWx API Extensions
##    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
