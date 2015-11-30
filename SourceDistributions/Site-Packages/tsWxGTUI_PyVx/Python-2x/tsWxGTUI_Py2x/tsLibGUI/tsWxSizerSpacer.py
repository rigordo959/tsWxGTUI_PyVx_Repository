#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:16:07 AM rsg>"
'''
tsWxSizerSpacer.py - Class used by wx.SizerItem to represent a
spacer.
'''
#################################################################
#
# File: tsWxSizerSpacer.py
#
# Purpose:
#
#    Class used by wx.SizerItem to represent a spacer.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSizerSpacer import SizerSpacer
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

__title__     = 'tsWxSizerSpacer'
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

from tsWxGTUI_Py2x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class SizerSpacer(Object):
    '''
    Used by wx.SizerItem to represent a spacer.
    '''
    def __init__(self, size, isShown=True):
        '''
        Constructs an empty wx.SizerSpacer.
        '''
        theClass = 'SizerSpacer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        # Set Default Values
        self.ts_Size = self.SetSize(size)
        self.ts_IsShown = isShown
##        self.ts_Children = []

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##        def __del__(self):
##            '''
##            '''
##            pass

    #-----------------------------------------------------------------------

    def GetIsShown(self):
        '''
        '''
        return (self.ts_IsShown)

    #-----------------------------------------------------------------------

    def GetSize(self):
        '''
        '''
        return (self.ts_Size)

    #-----------------------------------------------------------------------

    def SetSize(self, size):
        '''
        '''
        self.ts_Size = wx.tsGetClassInstanceFromTuple(size, wxSize)

    #-----------------------------------------------------------------------

    def Show(self, show=True):
        '''
        '''
        self.ts_IsShown = show

    #-----------------------------------------------------------------------

    IsShown = property(GetIsShown)
    Size = property(GetSize, SetSize)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
