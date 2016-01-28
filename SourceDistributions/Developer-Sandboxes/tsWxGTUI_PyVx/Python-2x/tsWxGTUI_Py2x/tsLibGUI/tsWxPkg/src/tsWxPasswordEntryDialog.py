#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:41:34 AM rsg>"
'''
tsWxPasswordEntryDialog.py - Class represents a dialog that
requests a one-line password string from the user.
'''
#################################################################
#
# File: tsWxPasswordEntryDialog.py
#
# Purpose:
#
#    Class represents a dialog that requests a one-line password
#    string from the user.
#
# Usage (example):
#
#    # Import
#
#    from tsWxPasswordEntryDialog import PasswordEntryDialog
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
#   2012/08/12 rsg Changed tsWxTextEntryDialog and tsWxTextEditBox.
#                  Resolved inability to turn-off the echoing of
#                  input characters and the inability to stop
#                  displaying dialog with a visible password.
#                  Resolution applicable only for event driven mode.
#
# ToDo:
#
#   2012/07/12 rsg Investigate and resolve inability to turn-off
#                  the echoing of input characters and the
#                  inability to stop displaying dialog with
#                  a visible password.
#
#################################################################

__title__     = 'tsWxPasswordEntryDialog'
__version__   = '1.1.0'
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

from tsWxDoubleLinkedList import DoubleLinkedList as wxDoubleLinkedList
from tsWxTextEntryDialog import TextEntryDialog
import tsWxGlobals as wx

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class PasswordEntryDialog(TextEntryDialog):
    '''
    Class represents a dialog that requests a one-line text string
    from the user.
    '''
    def __init__(self,
                 parent,                 # Should be None unless modal mode
                 message,                # Alias for user prompt output
                 caption=wx.EmptyString, # Alias for title
                 value=wx.EmptyString,   # Option for default user input
                 style=wx.TE_PASSWORD,   # Options for ClientRect
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
        theClass = 'PasswordEntryDialog'

        # Capture initial caller parametsrs before Dialog makes changes
        self.backup_parent = parent
        self.backup_message = message
        self.backup_caption = caption
        self.backup_value = value
        self.backup_style = style
        self.backup_size = size
        self.backup_pos = pos

        name = wx.PasswordEntryDialogNameStr
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

        TextEntryDialog.__init__(
            self,
            parent,          # Should be None unless modal mode
            message,         # Alias for user prompt output
            caption=caption, # Alias for title
            value=value,     # Option for default user input
            style=style,     # Options for ClientRect
            size=size,       # Extension for application use
            pos=pos          # Option for application use
            )

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
        self.ts_PasswordMode = True
        self.ts_StripSpaces = True

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
                'PasswordEntryDialog']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'PasswordEntryDialog']['ForegroundColour'].lower()
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

                msg = 'tsWxPasswordEntryDialog.__init__: ' + \
                      'Proceeding with tsDialogFeatureLayout. ' + \
                      'Style contains wx.CENTRE.'
                self.logger.debug(msg)
                print('DEBUG: %s\n' % msg)

            self.Center()

            # curses.noecho()

            self.ts_TextPad = self.tsDialogFeatureLayout()

            # curses.echo()

            self.Show()

        else:

            msg = 'tsWxPasswordEntryDialog.__init__: ' + \
                  'Skipped tsDialogFeatureLayout. ' + \
                  'Style did NOT contain wx.CENTRE.'
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)

        self.ts_ButtonUserPressed = wx.ID_CANCEL

        self.tsEndClassRegistration(theClass)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
