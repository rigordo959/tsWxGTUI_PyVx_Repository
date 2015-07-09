#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:39:58 AM rsg>"
'''
test_tsWxRadioBoxEvent.py - Application program to demonstrates
working with the wx.EvtHandler methods
'''
#################################################################
#
# File: test_tsWxRadioBoxEvent.py.py
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
#     python test_tsWxRadioBoxEvent.py
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

__title__     = 'test_tsWxRadioBoxEvent'
__version__   = '0.0.0'
__date__      = '10/11/2009'
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

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

#---------------------------------------------------------------------------

class RadioBoxEventFrame(wx.Frame):
 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With RadioBox(s)',
                size=(350, 212))
        self.panel = wx.Panel(self)

        self.baseRadioBoxRect = self.panel.ts_ClientRect

        print('Radio Box Test: Rect=%s' % self.baseRadioBoxRect)
        rb1Choices = ['&first\tCtrl-f',
                      '&second\tCtrl-s',
                      '&third\tCtrl-t']
        rb1 = wx.RadioBox(
            self.panel,
            id=nextWindowId(),
            label='Vertical Radio Box',
            pos=(self.baseRadioBoxRect.x + \
                 2 * wx.pixelWidthPerCharacter,
                 self.baseRadioBoxRect.y + \
                 2 * wx.pixelHeightPerCharacter),
            size=(25 * wx.pixelWidthPerCharacter,
                  7 * wx.pixelHeightPerCharacter),
            choices=rb1Choices,
            majorDimension=0,
            style=wx.RA_VERTICAL | wx.BORDER_SIMPLE,
            validator=wx.DefaultValidator,
            name=wx.RadioBoxNameStr)
        rb1.SetSelection(2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, rb1)
        print('Radio Box Test: rb1=%s' % rb1.ts_Rect)

        rb2Choices = ['f&ourth\tCtrl-o',
                      'f&ifth\tCtrl-i']
        rb2 = wx.RadioBox(
            self.panel,
            id=nextWindowId(),
                label='Horizontal Radio Box',
                pos=(self.baseRadioBoxRect.x + \
                     2 * wx.pixelWidthPerCharacter,
                     self.baseRadioBoxRect.y + \
                     10 * wx.pixelHeightPerCharacter),
                size=(38 * wx.pixelWidthPerCharacter,
                      5 * wx.pixelHeightPerCharacter),
                choices=rb2Choices,
                majorDimension=0,
                style=wx.RA_HORIZONTAL | wx.BORDER_SIMPLE,
                validator=wx.DefaultValidator,
                name=wx.RadioBoxNameStr)
        rb2.SetSelection(1)
        rb2.ts_ItemWindow[1].Label = '&Last\tCtrl-L'
        self.Bind(wx.EVT_RADIOBUTTON, self.OnGroup1Select, rb2)
        print('Radio Box Test: rb2=%s' % rb2.ts_Rect)

    #-----------------------------------------------------------------------

    def OnGroup1Select(self, event):
        '''
        '''
        radio_selected = event.GetEventObject()
        print('Group1 %s selected\n' % radio_selected.GetLabel() )

        for radio, text in self.group1_ctrls:
            if radio is radio_selected:
                text.Enable(True)
            else:
                text.Enable(False)

    #-----------------------------------------------------------------------

    def OnGroup2Select(self, event):
        '''
        '''
        radio_selected = event.GetEventObject()
        print('Group2 %s selected\n' % radio_selected.GetLabel() )

        for radio, text in self.group1_ctrls:
            if radio is radio_selected:
                text.Enable(True)
            else:
                text.Enable(False)

    #-----------------------------------------------------------------------

    def EvtRadioBox(self, event):
        '''
        '''
        print('EvtRadioBox: %d\n' % event.IsChecked())
        cb = event.GetEventObject()
        if cb.Is3State():
            print("\t3StateValue: %s\n" % cb.Get3StateValue())
##        pass

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
        frame = RadioBoxEventFrame(parent=None, id=-1)
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
