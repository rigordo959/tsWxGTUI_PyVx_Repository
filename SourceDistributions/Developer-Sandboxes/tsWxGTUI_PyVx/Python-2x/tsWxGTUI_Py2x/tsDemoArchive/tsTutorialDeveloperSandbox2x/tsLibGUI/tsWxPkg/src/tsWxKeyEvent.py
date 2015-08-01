#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:37:27 AM rsg>"
'''
tsWxKeyEvent.py - Class to contain information about key press
and release events.
'''
#################################################################
#
# File: tsWxKeyEvent.py
#
# Purpose:
#
#    Class to contain information about key press and release
#    events.
#
# Usage (example):
#
#    # Import
#
#    from tsWxKeyEvent import KeyEvent
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
#    Modify code to interpret event type.
#
#################################################################

__title__     = 'tsWxKeyEvent'
__version__   = '1.0.0'
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

import tsExceptions as tse

import tsWxGlobals as wx
from tsWxEvent import Event
from tsWxKeyboardState import KeyboardState
from tsWxPoint import Point as wxPoint

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

unimplemented = True

#---------------------------------------------------------------------------

class KeyEvent(Event, KeyboardState):
    '''
    This event class contains information about key press and release
    events.

    The main information carried by this event is the key being pressed
    or released. It can be accessed using either GetKeyCode() function
    or GetUnicodeKey(). For the printable characters, the latter should
    be used as it works for any keys, including non-Latin-1 characters
    that can be entered when using national keyboard layouts. GetKeyCode()
    should be used to handle special characters (such as cursor arrows
    keys or HOME or INS and so on) which correspond to wxKeyCode enum
    elements above the WXK_START constant. While GetKeyCode() also
    returns the character code for Latin-1 keys for compatibility, it
    does not work for Unicode characters in general and will return
    WXK_NONE for any non-Latin-1 ones. For this reason, it is recommended
    to always use GetUnicodeKey() and only fall back to GetKeyCode() if
    GetUnicodeKey() returned WXK_NONE meaning that the event corresponds
    to a non-printable special keys.

    While both of these functions can be used with the events of
    wxEVT_KEY_DOWN, wxEVT_KEY_UP and wxEVT_CHAR types, the values
    returned by them are different for the first two events and the
    last one. For the latter, the key returned corresponds to the
    character that would appear in e.g. a text zone if the user
    pressed the key in it. As such, its value depends on the current
    state of the Shift key and, for the letters, on the state of
    Caps Lock modifier. For example, if A key is pressed without
    Shift being held down, wxKeyEvent of type wxEVT_CHAR generated
    for this key press will return (from either GetKeyCode() or
    GetUnicodeKey() as their meanings coincide for ASCII characters)
    key code of 97 corresponding the ASCII value of a. And if the
    same key is pressed but with Shift being held (or Caps Lock
    being active), then the key could would be 65, i.e. ASCII value
    of capital A.

    However for the key down and up events the returned key code will
    instead be A independently of the state of the modifier keys i.e.
    it depends only on physical key being pressed and is not translated
    to its logical representation using the current keyboard state.
    Such untranslated key codes are defined as follows:

    * For the letters they correspond to the upper case value of the letter.

    * For the other alphanumeric keys (e.g. 7 or +), the untranslated
    key code corresponds to the character produced by the key when it
    is pressed without Shift. E.g. in standard US keyboard layout the
    untranslated key code for the key =/+ in the upper right corner
    of the keyboard is 61 which is the ASCII value of =.

    * For the rest of the keys (i.e. special non-printable keys) it
    is the same as the normal key code as no translation is used anyhow.

    Notice that the first rule applies to all Unicode letters, not just
    the usual Latin-1 ones. However for non-Latin-1 letters only
    GetUnicodeKey() can be used to retrieve the key code as GetKeyCode()
    just returns WXK_NONE in this case.

    To summarize: you should handle wxEVT_CHAR if you need the translated
    key and wxEVT_KEY_DOWN if you only need the value of the key itself,
    independent of the current keyboard state.

    Note:

    Not all key down events may be generated by the user. As an example,
    wxEVT_KEY_DOWN with = key code can be generated using the standard
    US keyboard layout but not using the German one because the = key
    corresponds to Shift-0 key combination in this layout and the key
    code for it is 0, not =. Because of this you should avoid requiring
    your users to type key events that might be impossible to enter on
    their keyboard.

    Another difference between key and char events is that another kind
    of translation is done for the latter ones when the Control key is
    pressed: char events for ASCII letters in this case carry codes
    corresponding to the ASCII value of Ctrl-Latter, i.e. 1 for Ctrl-A,
    2 for Ctrl-B and so on until 26 for Ctrl-Z. This is convenient for
    terminal-like applications and can be completely ignored by all the
    other ones (if you need to handle Ctrl-A it is probably a better
    idea to use the key event rather than the char one). Notice that
    currently no translation is done for the presses of [, \, ], ^
    and _ keys which might be mapped to ASCII values from 27 to 31.

    Finally, modifier keys only generate key events but no char events
    at all. The modifiers keys are WXK_SHIFT, WXK_CONTROL, WXK_ALT and
    various WXK_WINDOWS_XXX from wxKeyCode enum.

    Modifier keys events are special in one additional aspect: usually
    the keyboard state associated with a key press is well defined,
    e.g. wxKeyboardState::ShiftDown() returns true only if the Shift
    key was held pressed when the key that generated this event itself
    was pressed. There is an ambiguity for the key press events for
    Shift key itself however. By convention, it is considered to be
    already pressed when it is pressed and already released when it
    is released. In other words, wxEVT_KEY_DOWN event for the Shift
    key itself will have wxMOD_SHIFT in GetModifiers() and ShiftDown()
    will return true while the wxEVT_KEY_UP event for Shift itself
    will not have wxMOD_SHIFT in its modifiers and ShiftDown() will
    return false.

    Tip: You may discover the key codes and modifiers generated by
    all the keys on your system interactively by running the Key
    Event Sample wxWidgets sample and pressing some keys in it.

    Note:

    If a key down (EVT_KEY_DOWN) event is caught and the event handler
    does not call event.Skip() then the corresponding char event
    (EVT_CHAR) will not happen. This is by design and enables the
    programs that handle both types of events to avoid processing
    the same key twice. As a consequence, if you do not want to
    suppress the wxEVT_CHAR events for the keys you handle, always
    call event.Skip() in your wxEVT_KEY_DOWN handler. Not doing may
    also prevent accelerators defined using this key from working.

    If a key is maintained in a pressed state, you will typically
    get a lot of (automatically generated) key down events but only
    one key up one at the end when the key is released so it is
    wrong to assume that there is one up event corresponding to
    each down one.

    For Windows programmers: The key and char events in wxWidgets
    are similar to but slightly different from Windows WM_KEYDOWN
    and WM_CHAR events. In particular, Alt-x combination will
    generate a char event in wxWidgets (unless it is used as an
    accelerator) and almost all keys, including ones without
    ASCII equivalents, generate char events too.
    '''
    # Class variables

    #-----------------------------------------------------------------------

    def __init__(self, keyEventType=wx.EVT_NULL):
        '''
        Constructs a wx.KeyEvent.
        '''
        theClass = 'KeyEvent'

        wx.RegisterFirstCallerClassName(self, theClass)

        Event.__init__(self)
        KeyboardState.__init__(self)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        self.ts_keyEventType = keyEventType
 
        self.ts_keyCode = 0
        self.ts_rawKeyCode = 0
        self.ts_rawKeyFlags = 0
        self.ts_unicodeKey = 0
        self.ts_x = 0
        self.ts_y = 0
 
##        self.thisown = theClass

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------
 
    def GetKeyCode(self):
        '''
        Returns the key code of the key that generated this event.

        ASCII symbols return normal ASCII values, while events from
        special keys such as "left cursor arrow" (WXK_LEFT) return
        values outside of the ASCII range. See wxKeyCode for a full
        list of the virtual key codes.

        Note that this method returns a meaningful value only for
        special non-alphanumeric keys or if the user entered a
        character that can be represented in current locale default
        charset. Otherwise, e.g. if the user enters a Japanese
        character in a program not using Japanese locale, this
        method returns WXK_NONE and GetUnicodeKey() should be used
        to obtain the corresponding Unicode character.

        Using GetUnicodeKey() is in general the right thing to do
        if you are interested in the characters typed by the user,
        GetKeyCode() should be only used for special keys (for
        which GetUnicodeKey() returns WXK_NONE).
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'GetKeyCode in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            return (self.ts_keyCode)

    #-----------------------------------------------------------------------
 
    def GetPosition(self):
        '''
        Obtains the position (in client coordinates) at which the key
        was pressed.
        '''
        return (wxPoint(self.ts_x, self.ts_y))

    #-----------------------------------------------------------------------
 
    def GetPositionTuple(self):
        '''
        Obtains the position (in client coordinates) at which the key
        was pressed.
        '''
        return (self.ts_x, self.ts_y)

    #-----------------------------------------------------------------------
 
    def GetRawKeyCode(self):
        '''
        Returns the raw key code for this event.

        The flags are platform-dependent and should only be used
        if the functionality provided by other wxKeyEvent methods
        is insufficient.

        Under MSW, the raw key code is the value of wParam parameter
        of the corresponding message.

        Under GTK, the raw key code is the keyval field of the
        corresponding GDK event.

        Under OS X, the raw key code is the keyCode field of the
        corresponding NSEvent.

        Note:

        Currently the raw key codes are not supported by all ports,
        use #ifdef wxHAS_RAW_KEY_CODES to determine if this feature
        is available.
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'GetRawKeyCode in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            # TBD - May need to inspect self.ts_keyEventType.
            return (self.ts_rawKeyCode)

    #-----------------------------------------------------------------------
 
    def GetRawKeyFlags(self):
        '''
        Returns the low level key flags for this event.

        The flags are platform-dependent and should only be used
        if the functionality provided by other wxKeyEvent methods
        is insufficient.

        Under MSW, the raw flags are just the value of lParam
        parameter of the corresponding message.

        Under GTK, the raw flags contain the hardware_keycode
        field of the corresponding GDK event.

        Under OS X, the raw flags contain the modifiers state.

        Note:

        Currently the raw key flags are not supported by all
        ports, use #ifdef wxHAS_RAW_KEY_CODES to determine
        if this feature is available.
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'GetRawKeyFlags in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            # TBD - May need to inspect self.ts_keyEventType.
            return (self.ts_rawKeyFlags)

    #-----------------------------------------------------------------------
 
    def GetUnicodeKey(self):
        '''
        Returns the Unicode character corresponding to this key event.

        If the key pressed does not have any character value
        (e.g. a cursor key) this method will return WXK_NONE.
        In this case you should use GetKeyCode() to retrieve
        the value of the key.

        This function is only available in Unicode build,
        i.e. when wxUSE_UNICODE is 1.
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'GetUnicodeKey in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            # TBD - May need to inspect self.ts_keyEventType.
            return (self.ts_unicodeKey)

    #-----------------------------------------------------------------------
 
    def GetX(self):
        '''
        Returns the X position (in client coordinates) of the event.
        '''
        return (self.ts_x)

    #-----------------------------------------------------------------------

    def GetY(self):
        '''
        Returns the Y position (in client coordinates) of the event.
        '''
        return (self.ts_y)

    #-----------------------------------------------------------------------

    def IsKeyInCategory(self, category):
        '''
        Returns true if the key is in the given key category.

        Parameters:

        category - A bitwise combination of named wxKeyCategoryFlags
        constants.

        Since:
        2.9.1
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'IsKeyInCategory in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            # TBD - May need to inspect self.ts_keyEventType.
            return (self.ts_keyCode in category)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def SetUnicodeKey(self, uniChar):
        '''
        Set the Unicode value of the key event, but only if this is a
        Unicode build of wxPython.
        '''
        if unimplemented:
            msg = 'NotImplementedError: %s' % 'SetUnicodeKey in tsWxKeyEvent'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        elif uniChar is None:
            pass
        else:
            # TBD - May need to inspect self.ts_keyEventType.
            pass

    #-----------------------------------------------------------------------
 
    def SetX(self, x):
        '''
        Sets the X coordinate of the physical mouse event position.
        '''
        self.ts_x = x

    #-----------------------------------------------------------------------

    def SetY(self, y):
        '''
        Sets the Y coordinate of the physical mouse event position.
        '''
        self.ts_y = y

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
