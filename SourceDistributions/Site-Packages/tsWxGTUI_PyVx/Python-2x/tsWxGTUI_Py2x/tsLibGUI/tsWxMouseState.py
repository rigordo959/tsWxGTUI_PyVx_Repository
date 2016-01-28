#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:10:11 AM rsg>"
'''
tsWxMouseState.py - Class to hold information about mouse button and
modifier key states and is what is returned from wx.GetMouseState.
'''
#################################################################
#
# File: tsWxMouseState.py
#
# Purpose:
#
#    Class to hold information about mouse button and modifier key
#    states and is what is returned from wx.GetMouseState.
#
# Usage (example):
#
#    # Import
#
#    from tsWxMouseState import MouseState
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
#                   class variables so that the MouseState is
#                   global across all referencing modules.
#
#    2010/11/06 rsg Reverted to class instance variables.
#
#    2010/11/08 rsg Removed properties to conform with wxWidgets API.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxMouseState'
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

from tsWxGTUI_Py2x.tsLibCLI import tsCxGlobals as cx

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI.tsWxKeyboardState import KeyboardState

#---------------------------------------------------------------------------

class MouseState(KeyboardState):
    '''
    This class s used to hold information about mouse button and modifier
    key states and is what is returned from wx.GetMouseState.
    '''
    # Class variables

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        Constructs a wx.MouseState.
        '''
##        theClass = 'MouseState'
##        # Create class membership flag self.thisown
##        self.tsRegisterClassNameAndMembershipFlag(theClass)

        KeyboardState.__init__(self)

        self.ts_LeftIsDown = False
        self.ts_MiddleIsDown = False
        self.ts_RightIsDown = False
        self.ts_Aux1IsDown = False
        self.ts_Aux2IsDown = False
        self.ts_X = 0
        self.ts_Y = 0

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        del self

    #-----------------------------------------------------------------------
 
    def GetX(self):
        '''
        Returns X coordinate of the physical mouse event position.
        '''
        return (self.ts_X)

    #-----------------------------------------------------------------------

    def GetY(self):
        '''
        Returns Y coordinate of the physical mouse event position.
        '''
        return (self.ts_Y)

    #-----------------------------------------------------------------------
 
    def LeftIsDown(self):
        '''
        Returns true if the left mouse button is currently down.
        '''
        return (self.ts_LeftIsDown)

    #-----------------------------------------------------------------------
 
    def MiddleIsDown(self):
        '''
        Returns true if the middle mouse button is currently down.
        '''
        return (self.ts_MiddleIsDown)

    #-----------------------------------------------------------------------
 
    def RightIsDown(self):
        '''
        Returns true if the right mouse button is currently down.
        '''
        return (self.ts_RightIsDown)

    #-----------------------------------------------------------------------
 
    def Aux1IsDown(self):
        '''
        Returns true if the first extra mouse button is currently down.
        '''
        return (self.ts_Aux1IsDown)

    #-----------------------------------------------------------------------
 
    def Aux2IsDown(self):
        '''
        Returns true if the second extra mouse button is currently down.
        '''
        return (self.ts_Aux2IsDown)

    #-----------------------------------------------------------------------
 
    def SetLeftIsDown(self, down):
        '''
        Sets the Left mouse button state at the time of the event.
        '''
        self.ts_LeftIsDown = down

    #-----------------------------------------------------------------------
 
    def SetMiddleIsDown(self, down):
        '''
        Sets the Middle mouse button state at the time of the event.
        '''
        self.ts_MiddleIsDown = down

    #-----------------------------------------------------------------------
 
    def SetRightIsDown(self, down):
        '''
        Sets the Right mouse button state at the time of the event.
        '''
        self.ts_RightIsDown = down

    #-----------------------------------------------------------------------
 
    def SetAux1IsDown(self, down):
        '''
        Sets the first extra mouse button state at the time of the event.
        '''
        self.ts_Aux1IsDown = down

    #-----------------------------------------------------------------------
 
    def SetAux2IsDown(self, down):
        '''
        Sets the second extra mouse button state at the time of the event.
        '''
        self.ts_Aux2IsDown = down

    #-----------------------------------------------------------------------
 
    def SetX(self, x):
        '''
        Sets the X coordinate of the physical mouse event position.
        '''
        self.ts_X = x

    #-----------------------------------------------------------------------

    def SetY(self, y):
        '''
        Sets the Y coordinate of the physical mouse event position.
        '''
        self.ts_Y = y

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)

    myState = MouseState()

    print('***** Initialized Modifier Key State ***')
    print('AltDown = %s' % myState.AltDown())
    print('CmdDown = %s' % myState.CmdDown())
    print('ControlDown = %s' % myState.ControlDown())
    print('MetaDown = %s' % myState.MetaDown())
    print('ShiftDown = %s' % myState.ShiftDown())

    print('***** Initialized Mouse Button State ***')
    print('LeftIsDown = %s' % myState.LeftIsDown)
    print('MiddleIsDown = %s' % myState.MiddleIsDown)
    print('RightIsDown = %s' % myState.RightIsDown)
    print('Aux1IsDown = %s' % myState.Aux1IsDown)
    print('Aux2IsDown = %s' % myState.Aux2IsDown)

    print('***** Initialized Mouse Position State ***')
    print('GetX = %d' % myState.GetX())
    print('GetY = %d' % myState.GetY())

    downStates = [True, False]
    for state in downStates:
        print('\n')

        print('***** Modifier Key States Set %s ***' % state)
        myState.SetAltDown(state)
        myState.SetCmdDown(state)
        myState.SetControlDown(state)
        myState.SetMetaDown(state)
        myState.SetShiftDown(state)

        print('***** Mouse Button States Set %s ***' % state)
        myState.SetLeftIsDown(state)
        myState.SetMiddleIsDown(state)
        myState.SetRightIsDown(state)
        myState.SetAux1IsDown(state)
        myState.SetAux2IsDown(state)

        print('***** Mouse Position States Set %s ***' % state)
        myState.SetX(myState.GetX() + 1234)
        myState.SetY(myState.GetY() + 5678)

        print('***** Updated Modifier Key States Set %s ***' % state)
        print('AltDown = %s' % myState.AltDown())
        print('CmdDown = %s' % myState.CmdDown())
        print('ControlDown = %s' % myState.ControlDown())
        print('MetaDown = %s' % myState.MetaDown())
        print('ShiftDown = %s' % myState.ShiftDown())

        print('***** Updated Mouse Button States Set %s ***' % state)
        print('LeftIsDown = %s' % myState.LeftIsDown())
        print('MiddleIsDown = %s' % myState.MiddleIsDown())
        print('RightIsDown = %s' % myState.RightIsDown())
        print('Aux1IsDown = %s' % myState.Aux1IsDown())
        print('Aux2IsDown = %s' % myState.Aux2IsDown())

        print('***** Updated Mouse Position States Set %s ***' % state)
        print('GetX = %d' % myState.GetX())
        print('GetY = %d' % myState.GetY())
