#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:38:08 AM rsg>"
'''
test_tsWxCheckBoxEvent.py - Application program to demonstrates
working with the wx.EvtHandler methods
'''
#################################################################
#
# File: test_tsWxCheckBoxEvent.py.py
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
#     python test_tsWxCheckBoxEvent.py
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

__title__     = 'test_tsWxCheckBoxEvent'
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

class CheckBoxEventFrame(wx.Frame):
 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With CheckBox(s)',
                size=(280, 168))
        self.panel = wx.Panel(self)

        self.baseCheckBoxRect = self.panel.ts_ClientRect

        cb1 = wx.CheckBox(
            self.panel,
            nextWindowId(),
            "&R-Align\tCtrl-R",
            (self.baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
            (15 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            style=wx.ALIGN_RIGHT | wx.NO_BORDER)
        cb1.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb1)

        cb2 = wx.CheckBox(
            self,
            nextWindowId(),
            "&L-Align\tCtrl-L",
            (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 4 * wx.pixelHeightPerCharacter),
            (12 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb2)

        cb3 = wx.CheckBox(
            self,
            nextWindowId(),
            "&Apples\tCtrl-A",
            (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 5 * wx.pixelHeightPerCharacter),
            (12 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            wx.NO_BORDER)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb3)

        cb4 = wx.CheckBox(
            self,
            nextWindowId(),
            "&Oranges\tCtrl-O",
            (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 6 * wx.pixelHeightPerCharacter),
            (12 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            wx.NO_BORDER)
        cb4.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb4)

        cb5 = wx.CheckBox(
            self,
            nextWindowId(),
            "&Tristate\tCtrl-T",
            (self.baseCheckBoxRect.x + 2 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
            (15 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            style=(wx.ALIGN_RIGHT | \
                   wx.NO_BORDER | \
                   wx.CHK_3STATE | \
                   wx.CHK_ALLOW_3RD_STATE_FOR_USER))
        cb5.Set3StateValue(2)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb5)

        cb6 = wx.CheckBox(
            self,
            nextWindowId(),
            "&Pears\tCtrl-P",
            (self.baseCheckBoxRect.x + 16 * wx.pixelWidthPerCharacter,
             self.baseCheckBoxRect.y + 7 * wx.pixelHeightPerCharacter),
            (15 * wx.pixelWidthPerCharacter,
             1 * wx.pixelHeightPerCharacter),
            wx.NO_BORDER)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb6)

    #-----------------------------------------------------------------------

    def EvtCheckBox(self, event):
        '''
        '''
        print('EvtCheckBox: %d\n' % event.IsChecked())
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
        frame = CheckBoxEventFrame(parent=None, id=-1)
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
