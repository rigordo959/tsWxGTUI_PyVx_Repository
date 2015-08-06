#! /usr/bin/env python
# "Time-stamp: <04/08/2015  8:51:23 AM rsg>"
'''
tsWxPySimpleApp.py - Base Class for creating a simple application
class. You can just create one of these and then make your top
level windows later, and not have to worry about OnInit.
'''
#################################################################
#
# File: tsWxPySimpleApp.py
#
# Purpose:
#
#    Base Class for creating a simple application class. You
#    can just create one of these and then make your top level
#    windows later, and not have to worry about OnInit.
#
# Usage (example):
#
#    # Import
#
#    from tsWxPySimpleApp import PySimpleApp as App
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Modifications:
#
#    2013/07/03 rsg Added "wxPyDeprecationWarning: Using
#                   deprecated class PySimpleApp."
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxPySimpleApp'
__version__   = '1.1.0'
__date__      = '07/03/2013'
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

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI.tsWxApp import App

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class PySimpleApp(App):
    '''
    A simple application class. You can just create one of these and then
    make your top level windows later, and not have to worry about OnInit.
    For example:

    app = wx.PySimpleApp()
    frame = wx.Frame(None, title='Hello World')
    frame.Show()
    app.MainLoop()
    '''
    def __init__(self,
                 redirect=False,
                 filename=None,
                 useBestVisual=False,
                 clearSigInt=True):
        '''
        Construct a wx.App object.
        '''
        print('wxPyDeprecationWarning: Using deprecated class PySimpleApp.')

        theClass = 'PySimpleApp'

        wx.RegisterFirstCallerClassName(self, theClass)

        App.__init__(self,
                     redirect=redirect,
                     filename=filename,
                     useBestVisual=useBestVisual,
                     clearSigInt=clearSigInt)

        id = wx.ID_ANY

        self.tsBeginClassRegistration(theClass, id)

        self.tsEndClassRegistration(theClass)

    def OnInit(self):
        '''
        '''
        return (True)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
