#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:52:20 AM rsg>"
'''

***** Do NOT Use. Under Conbstruction. *****
*****       Base class not known.      *****

tsWxTextEntry.py - Common base class for single line text entry
fields.

This class is not a control itself, as it does not derive from
wxWindow. Instead it is used as a base class by other controls,
notably wxTextCtrl and wxComboBox and gathers the methods common
to both of them.
'''
#################################################################
#
# File: tsWxTextEntry.py
#
# Purpose:
#
#    Common base class for single line text entry fields.
#
#    This class is not a control itself, as it does not derive
#    from wxWindow. Instead it is used as a base class by other
#    controls, notably wxTextCtrl and wxComboBox and gathers the
#    methods common to both of them.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTextEntry import TextEntry
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

__title__     = 'tsWxTextEntry'
__version__   = '1.0.0'
__date__      = '09/16/2013'
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

import tsWxGlobals as wx
from tsWxAcceleratorEntry import AcceleratorEntry as wxAcceleratorEntry
from tsWxAcceleratorTable import AcceleratorTable as wxAcceleratorTable
from tsWxBoxSizer import BoxSizer as wxBoxSizer
from tsWxButton import Button as wxButton
from tsWxDialog import Dialog
from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
from tsWxEvent import EVT_CLOSE
from tsWxEvent import EVT_HELP
from tsWxEvent import EVT_SET_FOCUS
from tsWxEvent import EVT_COMMAND_LEFT_CLICK   # [Left Mouse]-Button Click
from tsWxPanel import Panel as wxPanel
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxSizerSpacer import SizerSpacer as wxSizerSpacer
from tsWxStaticLine import StaticLine as wxStaticLine
from tsWxStaticText import StaticText as wxStaticText
from tsWxTextCtrl import TextCtrl as wxTextCtrl
from tsWxTopLevelWindow import TopLevelWindow

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class TextEntry(EvtHandler):
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
        '''
        theClass = 'TextEntry'

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

##        wx.RegisterFirstCallerClassName(self, theClass)

##        Dialog.__init__(self,
##                        parent, # self.GetParentForModalDialog(parent, style),
##                        id=wx.ID_ANY,
##                        title=title,
##                        pos=pos,
##                        size=size,
##                        # Apply Default Dialog Style to Top-Level Window
##                        # (defer TextEntryDialog style for internal layout)
##                        style=wx.DEFAULT_DIALOG_STYLE,
##                        name=name)

        # Capture parameters.
        self.ts_Caption = self.backup_caption
        self.ts_Message = self.backup_message
        self.ts_Parent = self.backup_parent    # Should be None unless modal mode
        self.ts_Pos = self.backup_pos
        self.ts_Size = self.backup_size
        self.ts_Style = self.backup_style
        self.ts_Title = self.backup_title
        self.ts_Value = self.backup_value

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

    def AppendText(self, text):
        '''
        Appends the text to the end of the text control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def AutoComplete(self, choices):
        '''
        Call this function to enable auto-completion of the text typed
        in a single-line text control using the given choices.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def AutoComplete(self, completer):
        '''
        Enable auto-completion using the provided completer object.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def AutoCompleteFileNames(self):
        '''
        Call this function to enable auto-completion of the text typed
        in a single-line text control using all valid file system paths.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def AutoCompleteDirectories(self):
        '''
        Call this function to enable auto-completion of the text using
        the file system directories.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def CanCopy(self):
        '''
        Returns true if the selection can be copied to the clipboard.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def CanCut(self):
        '''
        Returns true if the selection can be cut to the clipboard.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def CanPaste(self):
        '''
        Returns true if the contents of the clipboard can be pasted into
        the text control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def CanRedo(self):
        '''
        Returns true if there is a redo facility available and the last
        operation can be redone.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def CanUndo(self):
        '''
        Returns true if there is an undo facility available and the
        last operation can be undone.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def ChangeValue(self, value):
        '''
        Sets the new text control value.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Clear(self):
        '''
        Clears the text in the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Copy(self):
        '''
        Copies the selected text to the clipboard.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def GetHint(self):
        '''
        Returns the current hint string.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxString =''

        return (wxString)

    #-----------------------------------------------------------------------

    def GetInsertionPoint(self):
        '''
        Returns the insertion point, or cursor, position.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        int = 0

        return (int)

    #-----------------------------------------------------------------------

    def GetLastPosition(self):
        '''
        Returns the zero based index of the last position in the text
        control, which is equal to the number of characters in the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxTextPos = (0, 0)

        return (wxTextPos)

    #-----------------------------------------------------------------------

    def GetMargins(self):
        '''
        Returns the margins used by the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxPoint = (0, 0)

        return (wxPoint)

    #-----------------------------------------------------------------------

    def GetRange(self, dataFrom, dataTo):
        '''
        Returns the string containing the text starting in the positions
        from and up to to in the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxString = ''

        return (wxString)

    #-----------------------------------------------------------------------

    def GetSelection(self, dataFrom, dataTo):
        '''
        Gets the current selection span.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def GetStringSelection(self):
        '''
        Gets the text currently selected in the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxString = ''

        return (wxString)

    #-----------------------------------------------------------------------

    def GetValue(self):
        '''
        Gets the contents of the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        wxString = ''

        return (wxString)

    #-----------------------------------------------------------------------

    def IsEditable(self):
        '''
        Returns true if the controls contents may be edited by user
        (note that it always can be changed by the program).
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def IsEmpty(self):
        '''
        Returns true if the control is currently empty.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def Paste(self):
        '''
        Pastes text from the clipboard to the text item.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Redo(self):
        '''
        If there is a redo facility and the last operation can be redone,
        redoes the last operation.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Remove(self, dataFrom, dataTo):
        '''
        Removes the text starting at the first given position up to
        (but not including) the character at the last position.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Replace(self, dataFrom, dataTo, value):
        '''
        Replaces the text starting at the first position up to
        (but not including) the character at the last position
        with the given text.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SelectAll(self):
        '''
        Selects all text in the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetEditable(self, editable):
        '''
        Makes the text item editable or read-only, overriding the
        wxTE_READONLY flag.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetHint(self, hint):
        '''
        Sets a hint shown in an empty unfocused text control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def SetInsertionPoint(self, pos):
        '''
        Sets the insertion point at the given position.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetInsertionPointEnd(self):
        '''
        Sets the insertion point at the end of the text control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetMargins(self, pt):
        '''
        Attempts to set the control margins.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def SetMargins(self, left, top=-1):
        '''
        Attempts to set the control margins.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

        bool = False

        return (bool)

    #-----------------------------------------------------------------------

    def SetMaxLength(self, len):
        '''
        This function sets the maximum number of characters the user
        can enter into the control.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetSelection(self, dataFrom, dataTo):
        '''
        Selects the text starting at the first position up to
        (but not including) the character at the last position.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def SetValue(self, value):
        '''
        Sets the new text control value.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def Undo(self):
        '''
        If there is an undo facility and the last operation can be
        undone, undoes the last operation.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------

    def WriteText(self, text):
        '''
        Writes the text into the text control at the current insertion
        position.
        '''
        msg = 'NotImplementedError: %s' % \
              'ShowModal in tsWxTextEntry'
        self.logger.error(msg)
        print('ERROR: %s\n' % msg)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions


    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

