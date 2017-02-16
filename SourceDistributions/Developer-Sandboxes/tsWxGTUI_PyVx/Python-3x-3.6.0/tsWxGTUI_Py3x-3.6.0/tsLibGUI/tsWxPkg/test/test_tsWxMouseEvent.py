#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:39:36 AM rsg>"
'''
test_tsWxMouseEvent.py - Application program to demonstrates
working with the wx.EvtHandler methods
'''
#################################################################
#
# File: test_tsWxMouseEvent.py.py
#
# Purpose:
#
#    Application program to demonstrates working with the
#    wx.EvtHandler methods.
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxMouseEvent.py
#
# Methods:
#
# ToDo:
#
#    None
#
# Modifications:
#
#    None
#
#################################################################

__title__     = 'test_tsWxMouseEvent'
__version__   = '0.0.0'
__date__      = '10/01/2009'
__authors__   = 'Richard "Dick" S. Gordon & Frederick "Rick" A. Kier'
__copyright__ = 'Copyright (c) 2007-2009 TeamSTARS. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__,
                                         __line2__,
                                         __line3__)

mainTitleVersionDate = __line1__

import sys
import time
import traceback

try:
    import tsLibraries
except:
    pass

import tsApplication as tsAPP
import tsExceptions as tse
import tsLogger as Logger

try:
    import wx
except ImportError as wxImportError:
    import tsWx as wx

WXPYTHON_EMULATION = True

__help__ = '''
This program demonstrates working with the wx.EvtHandler methods.
'''

mainTitleVersionDate = __line1__

simulateEvents = True

#---------------------------------------------------------------------------

class MouseEventFrame(wx.Frame):
 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                size=(300, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel,
                                label="Not Over",
                                pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
###        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
###        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
##        if simulateEvents:
##            event = wx.EVT_BUTTON
##            self.OnButtonClick(event)
##        else:
##            event = wx.EVT_ENTER_WINDOW
##            self.OnButtonClick(event)
 
    def OnButtonClick(self, event):
        print('MouseEventFrame.OnButtonClick')
        self.panel.SetBackgroundColour('Green')
        if not simulateEvents:
            self.panel.Refresh()
        else:
            self.panel.Parent.Show()
 
    def OnEnterWindow(self, event):
        self.button.SetLabel("Over Me!")
        if not simulateEvents:
            self.panel.Refresh()
        else:
            self.panel.Parent.Show()
        event.Skip()
 
    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        if not simulateEvents:
            self.panel.Refresh()
        else:
            self.panel.Parent.Show()
        event.Skip()

#---------------------------------------------------------------------------

class cliAPP(tsAPP.TsApplication):
    '''
    Class to establish the application specific control components.
    '''
    def __init__(self, *args, **kw):
        '''
        Add our main entry point to kw
        Init tsApp
        '''
        kw['main'] = self.main
        tsAPP.TsApplication.__init__(self, *args, **kw)
        self.theWindowLogger = Logger.TsLogger(threshold = Logger.DEBUG,
                                               start = time.time(),
                                               name = 'stdscr')

    def main(self):
        '''
        '''
        app = wx.PySimpleApp(redirect=True,
                             filename=None)
        frame = MouseEventFrame(parent=None, id=-1)
        frame.Show()

        message = 'Started timestamped wxPython: stdout/stderr\n\n' + \
                  'Print statements and other standard output ' + \
                  'will now be directed to this window.'

        self.theWindowLogger.info(message)

        self.theWindowLogger.debug('Before MainLoop')
        print("Before MainLoop")
        app.MainLoop()
        print("After MainLoop")
        self.theWindowLogger.debug('After MainLoop')

#---------------------------------------------------------------------------

if __name__ == '__main__':
    '''
    Create my App
    Run the main entry point
    '''
    # Remember original stdout and stderr
    #  WxPython makes them graphical
    _stdout = sys.stdout
    _stderr = sys.stderr

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:
        theApplication = cliAPP(
            header=__header__,
            mainTitleVersionDate=mainTitleVersionDate,
            title=__title__,
            version=__version__,
            date=__date__,
            logs=[])

        theApplication.runMain()

    except Exception as e:
        if isinstance(e, tse.TsExceptions):
            msg = str(e)
            tse.displayError(e)
            exitStatus = e.exitCode
        else:
            msg = None
            _stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

##    print __header__
#    _stdout.write(__header__)

    if msg == tse.NO_ERROR:
        _stdout.write(msg + '\n')

    elif msg is not None:
        _stderr.write(msg.replace('"', '') + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)
