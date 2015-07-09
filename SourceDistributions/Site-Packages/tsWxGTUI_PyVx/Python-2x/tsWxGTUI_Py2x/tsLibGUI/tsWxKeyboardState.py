#! /usr/bin/env python
# "Time-stamp: <03/28/2015 10:43:48 AM rsg>"
'''
tsWxKeyboardState.py - Class to hold information about keyboard
modifier keys and is what is returned from wx.GetModifiers.
'''
#################################################################
#
# File: tsWxKeyboardState.py
#
# Purpose:
#
#    Class to hold information about keyboard modifier keys
#    and is what is returned from wx.GetModifiers.
#
# Usage (example):
#
#    # Import
#
#    from tsWxKeyboardState import KeyboardState
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
#    2010/09/18 rsg Converted the class instance variables to
#                   class variables so that the KeyboardState is
#                   global across all referencing modules.
#
#    2010/11/08 rsg Reverted to class instance variables so that
#                   the KeyboardState is NOT global across all
#                   referencing modules.
#
#    2010/11/08 rsg Removed properties so as to conform with
#                   wxWidgets API.
#
#    2010/11/09 rsg Added tsWx API Extensions for use by
#                   tsWxEventLoop: SetAltDown, SetCmdDown,
#                   SetControlDown, SetMetaDown and SetShiftDown.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxKeyboardState'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class KeyboardState(object):
    '''
    Provides methods for testing the state of the keyboard modifier keys.

    This class is used as a base class of wxKeyEvent and wxMouseState and,
    hence, indirectly, of wxMouseEvent, so its methods may be used to get
    information about the modifier keys which were pressed when the event
    occurred.
    '''
    # Class variables

    #-----------------------------------------------------------------------

    def __init__(self,
                 controlDown = False,
                 shiftDown = False,
                 altDown = False,
                 metaDown = False):
        '''
        Constructor initializes the modifier key settings.

        By default, no modifiers are active.
        '''
##        theClass = 'KeyboardState'
##        # Create class membership flag self.thisown
##        self.tsRegisterClassNameAndMembershipFlag(theClass)

        # TBD - Presume that each event should retain association with
        # its own instance variables?
        self.ts_AltDown = altDown
        self.ts_ControlDown = controlDown
        self.ts_MetaDown = metaDown
        self.ts_ShiftDown = shiftDown

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        del self

    #-----------------------------------------------------------------------

    def AltDown(self):
        '''
        Returns true if the Alt key is pressed.

        Notice that GetModifiers() should usually be used instead of this one.
        '''
        return (self.ts_AltDown)
 
    #-----------------------------------------------------------------------

    def CmdDown(self):
        '''
        Returns true if the key used for command accelerators is pressed.

        Cmd is a pseudo key which is Control for PC and Unix platforms but
        Apple (or Command) key under Macs: it makes often sense to use it
        instead of ControlDown() because Command key is used for the same
        thing under Mac as Control elsewhere (even though Control still
        exists, it is usually not used for the same purpose under Mac).

        Notice that GetModifiers() should usually be used instead of this
        one. However, the Apple "Cmd" (Command) is Not supported, by
        Ncurses, on computer platforms running Mac OS X, Linux or Windows.
        '''
        return (self.ControlDown())

    #-----------------------------------------------------------------------
 
    def ControlDown(self):
        '''
        Returns true if the Control key is pressed.

        This function does not distinguish between right and left control
        keys.

        In portable code you usually want to use CmdDown() to automatically
        test for the more frequently used Command key (and not the rarely
        used Control one) under Mac.

        Notice that GetModifiers() should usually be used instead of this one.
        '''
        return (self.ts_ControlDown)

    #-----------------------------------------------------------------------

    def GetModifiers(self):
        '''
        Return the bit mask of all pressed modifier keys.

        The return value is a combination of wxMOD_ALT, wxMOD_CONTROL,
        wxMOD_SHIFT and wxMOD_META bit masks. Additionally, wxMOD_NONE
        is defined as 0, i.e. corresponds to no modifiers
        (see HasModifiers()) and wxMOD_CMD is either wxMOD_CONTROL
        (MSW and Unix) or wxMOD_META (Mac), see CmdDown().
        See wxKeyModifier for the full list of modifiers.

        Notice that this function is easier to use correctly than, for
        example, ControlDown() because when using the latter you also
        have to remember to test that none of the other modifiers is pressed:

        if ( ControlDown() && !AltDown() && !ShiftDown() && !MetaDown() )
            ... handle Ctrl-XXX ...

        and forgetting to do it can result in serious program bugs (e.g.
        program not working with European keyboard layout where AltGr key
        which is seen by the program as combination of CTRL and ALT is used).
        On the other hand, you can simply write:

        if ( GetModifiers() == wxMOD_CONTROL )
            ... handle Ctrl-XXX ...

        with this function.
        '''
        mask = wx.wxMOD_NONE

        if (self.ts_ControlDown):

            mask = mask | wx.wxMOD_CONTROL

        if (self.ts_ShiftDown):

            mask = mask | wx.wxMOD_SHIFT

        if (self.ts_AltDown):

            mask = mask | wx.wxMOD_ALT

        if (self.ts_MetaDown):

            mask = mask | wx.wxMOD_META

        if (mask == (wx.wxMOD_CONTROL | \
                     wx.wxMOD_SHIFT | \
                     wx.wxMOD_ALT | \
                     wx.wxMOD_META)):

            mask = wx.wxMOD_ALL

        return (mask)

    #-----------------------------------------------------------------------
 
    def HasModifiers(self):
        '''
        Returns true if any modifiers at all are pressed.

        This is equivalent to GetModifiers() != wxMOD_NONE.
        '''
        return (self.GetModifiers() != wx.wxMOD_NONE)

    #-----------------------------------------------------------------------
 
    def MetaDown(self):
        '''
        Returns true if the Meta/Windows/Apple key is pressed.

        This function tests the state of the key traditionally called Meta
        under Unix systems, Windows keys under MSW and Apple, or Command,
        key under Mac.

        Notice that GetModifiers() should usually be used instead of this one.

        See also:

        CmdDown()

        Reimplemented in wxMouseEvent.

        Notice: Apple "Cmd" (Command) Not supported, by Ncurses, on computer
        platforms running Mac OS X, Linux or Windows.
        '''
        return (self.ts_MetaDown)

    #-----------------------------------------------------------------------
 
    def ShiftDown(self):
        '''
        Returns true if the Shift key is pressed.

        This function does not distinguish between right and left shift keys.

        Notice that GetModifiers() should usually be used instead of this one.
        '''
        return (self.ts_ShiftDown)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def SetAltDown(self, down):
        '''
        Sets the Alt key down state at the time of the event.
        '''
        self.ts_AltDown = down
 
    #-----------------------------------------------------------------------

    def SetCmdDown(self, down):
        '''
        Sets the Cmd key down state at the time of the event.
        "Cmd" is a pseudo key which is the same as Control for PC and Unix
        platforms but the special "Apple" (a.k.a as "Command") key on Macs.

        Notice: Apple "Cmd" (Command) Not supported, by Ncurses, on computer
        platforms running Mac OS X, Linux or Windows.
        '''
        self.SetControlDown(down)

    #-----------------------------------------------------------------------
 
    def SetControlDown(self, down):
        '''
        Sets the Control key down state at the time of the event.
        '''
        self.ts_ControlDown = down

    #-----------------------------------------------------------------------
 
    def SetMetaDown(self, down):
        '''
        Sets the Meta key down state at the time of the event.

        Notice: Apple "Cmd" (Command) Not supported, by Ncurses, on computer
        platforms running Mac OS X, Linux or Windows.
        '''
        self.ts_MetaDown = down

    #-----------------------------------------------------------------------
 
    def SetShiftDown(self, down):
        '''
        Sets the Shift key down state at the time of the event.
        '''
        self.ts_ShiftDown = down

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)

    myState = KeyboardState()

    print('***** Initialized State ***')
    print('AltDown = %s' % myState.AltDown())
    print('CmdDown = %s' % myState.CmdDown())
    print('ControlDown = %s' % myState.ControlDown())
    print('MetaDown = %s' % myState.MetaDown())
    print('ShiftDown = %s' % myState.ShiftDown())
    print('GetModifiers = 0x%X' % myState.GetModifiers())
    print('HasModifiers = %s' % myState.HasModifiers())

    downStates = [True, False]
    for state in downStates:
        print('\n')

        print('***** State Set %s ***' % state)
        myState.SetAltDown(state)
        myState.SetCmdDown(state)
        myState.SetControlDown(state)
        myState.SetMetaDown(state)
        myState.SetShiftDown(state)

        print('AltDown = %s' % myState.AltDown())
        print('CmdDown = %s' % myState.CmdDown())
        print('ControlDown = %s' % myState.ControlDown())
        print('MetaDown = %s' % myState.MetaDown())
        print('ShiftDown = %s' % myState.ShiftDown())
        print('GetModifiers = 0x%X' % myState.GetModifiers())
        print('HasModifiers = %s' % myState.HasModifiers())
