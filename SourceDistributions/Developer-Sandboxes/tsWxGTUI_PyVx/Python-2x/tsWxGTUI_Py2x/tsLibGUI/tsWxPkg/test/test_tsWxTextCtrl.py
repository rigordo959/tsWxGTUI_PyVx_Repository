#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:17:29 AM rsg>"
'''
test_tsWxTextCtrl.py - Application program to mimic some
features of the Graphical TextUser Interface.
'''
#################################################################
#
# File: test_tsWxTextCtrl.py.py
#
# Purpose:
#
#    Application program to mimic some features of the
#    Graphical Text User Interface.
#
#
#    1. Frame
#    2. one main panel added to Frame
#    3. two panels, one left and one right, added to main panel
#    4. two buttons in the left panel (plus and minus)
#    5. one text widget in the right panel used as a counter
#    6. the plus button will add one to the counter
#    7. the minus button will subtract one from the counter
#
# Limitations:
#
#    1) None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxTextCtrl.py
#
# Methods:
#
# ToDo:
#   1. Show menu help in status bar - works on MS Windows
#   2. Fix minimum size - can resize the Frame too small
#      added fix - doesn't quite work on MacOS, need to check MS Windows
#
# Modifications:
#
#################################################################

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
import tsWx as wx

##import wx

__title__     = 'test_tsWxTextCtrl'
__version__   = '1.0.0'
__date__      = '08/29/2011'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2011 Software Gadgetry. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__,
                                         __line2__,
                                         __line3__)

WXPYTHON_EMULATION = True

__help__ = '''
This program shows the most basic wxPython application. It creates a frame
and displays "GE TURBINE AUTOMATIC CONTROL".
'''

mainTitleVersionDate = __line1__

description = '''
                      1         2         3         4         5         6         7
Row/Col     0123456789012345678901234567890123456789012345678901234567890123456789012345
      0     ----------------------------------------------------------------------------
      1     1987/05/15  15:42:00    GE TURBINE AUTOMATIC CONTROL          plant: TAC-OFF
      2     ------------------------------+-----------------------------+---------------
      3     generator: OFF-LINE at    0mw | turbine: TRIPPED at    0rpm |   tac: MONITOR
      4     accel. rate:     HOLD rpm/min | admission: to-?? rate: SLOW |   cle:     LOW
      5     ------------------------------+-----------------------------+---------------
      6     Turbine Location   Temperature  --Stress--  Pred  --Total Life Expenditure--
      7                        Shell  Bore  Surf  Bore  Bore  CLE (%)  Zone1 Zone2 Zone3
      8     HP 1st Stage (HP)   ****  ****  ****  ****  ****    0.000      0     0     0
      9     RH Bowl      (RH)   ****  ****  ****  ****  ****    0.000      0     0     0
     10     Crossover    (XO)   ****  ****  ****  ****  ****    0.000      0     0     0
      1                         Stabilization Until 16:42:20
      2     position (%)        pressure (psi)  temperature (^F)     temperature (^F)
      3     sv bypass   0  ***  main stm     0  main stm    68   68  rht  stm  **** ****
      4     cv          0       chest        0  hp shell    68   68  rh bowl     68   68
      5     load lim  ***       rht stm   ****  cv inner    68   68  xo shell    68   68
      6     load set  ***                       cv outer    68   68  tc ref      85
      7     speed set ***   speed meter:    0rpm   load meter: ****mw  valve meter:   0%
      8     ----------------------------------------------------------------------------
      9        Manual Hold: OFF | Computer Hold:  ON | MODE Hold: Turbine Tripped
     20     ----------------------------------------------------------------------------

'''
descriptionTopLeft = wx.Point(12, 2)
descriptionBottomRight = wx.Point(88, 23)

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

    def main(self):
        '''
        Get a wx App
        Build the Frame
        Enter wx main loop
        '''
        app = wx.PySimpleApp(redirect=True,
                             filename=None)
        self.myframe = wx.Frame(None, title='BasicFrame')

        parent = self.myframe
        print('ClientArea: %s' % str(parent.ClientArea))
        tcPosition = (parent.ClientArea.x, parent.ClientArea.y)
        tcSize = (parent.ClientArea.width, parent.ClientArea.height)
        print('tcPosition: %s; tcSize: %s' % (tcPosition, tcSize))
        self.myframe.tc = wx.TextCtrl(
            parent,
            id=wx.ID_ANY,
            value=wx.EmptyString,
            pos=tcPosition,
            size=tcSize,
            style=0,
            validator=wx.DefaultValidator,
            name=wx.TextCtrlNameStr)

        self.myframe.tc.AppendText(description)

        line = -1
        for aline in description.split('\n'):
            line += 1
##            print('line: %d; aline: %s' % (line, aline))
            if (line > descriptionTopLeft.y) and \
               (line <= descriptionBottomRight.y):

                self.myframe.tc.AppendText(aline[descriptionTopLeft.x - 1:len(aline)])
##        print(description)

        self.myframe.Show()
        # print("Before MainLoop")
        app.MainLoop()
        # print("After MainLoop")

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

    except Exception, e:
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
