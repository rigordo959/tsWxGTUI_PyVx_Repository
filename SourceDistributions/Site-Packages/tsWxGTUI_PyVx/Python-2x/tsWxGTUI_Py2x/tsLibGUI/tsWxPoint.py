#! /usr/bin/env python
# "Time-stamp: <03/28/2015  4:08:07 PM rsg>"
'''
tsWxPoint.py - Class to represent a point or position of a graphical
object with integer x (horizontal) and y (vertical) properties.
'''
#################################################################
#
# File: tsWxPoint.py
#
# Purpose:
#
#    Class to represent a point or position of a graphical object
#    with integer x (horizontal) and y (vertical) properties.
#
# Usage (example):
#
#    # Import
#
#    from tsWxPoint import Point
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

__title__     = 'tsWxPoint'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse

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

class Point(object):
    '''
    A data structure for representing a point or position with integer x
    and y properties. Most places in wxPython that expect a wx.Point can
    also accept a (x,y) tuple.
    '''
    def __init__(self, x=0, y=0):
        '''
        Constructor. Create a wx.Point object.
        '''
##        theClass = 'Point'
##        # Create class membership flag self.thisown
##        self.tsRegisterClassNameAndMembershipFlag(theClass)
        self.ts_x = x
        self.ts_y = y

    #-----------------------------------------------------------------------

    def __add__(self, pt):
        '''
        Add pt properties to this and return the result.
        '''
        temp = Point.tsGetPointType(pt)
        return (Point(self.ts_x + temp.x, self.ts_y + temp.y))



    #-----------------------------------------------------------------------

##    def __del__(self):
##        '''
##        '''
##        del self.ts_x
##        del self.ts_y
##        del self

    #-----------------------------------------------------------------------

    def __eq__(self, other):
        '''
        Test for equality of wx.Point objects.
        '''
        temp = Point.tsGetPointType(other)
        return ((self.ts_x == temp.x) and \
                (self.ts_y == temp.y))
    #-----------------------------------------------------------------------

    def __getitem__(self, index):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__getitem__ in tsWxPoint'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __iadd__(self, pt):
        '''
        Add pt to this object.
        '''
        return (Point(self.ts_x + pt.x, self.ts_y + pt.y))

    #-----------------------------------------------------------------------

    def __isub__(self, pt):
        '''
        Subtract pt from this object.
        '''
        return (Point(self.ts_x - pt.x, self.ts_y - pt.y))

    #-----------------------------------------------------------------------

    def __len__(self):
        '''
        Return length of object.
        '''
        return (len(self))

    #-----------------------------------------------------------------------

    def __ne__(self, other):
        '''
        Test for inequality of wx.Point objects.
        '''
        temp = Point.tsGetPointType(other)
        return ((self.ts_x != temp.x) or \
                (self.ts_y != temp.y))

    #-----------------------------------------------------------------------

    def __nonzero__(self):
        '''
        Return True if not zero.
        '''
        return (self.ts_x != 0 and \
                self.ts_y != 0)

    #-----------------------------------------------------------------------

    def __reduce__(self):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__reduce__ in tsWxPoint'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __repr__(self):
        '''
        Return text representation.
        '''
        text = str((self.ts_x, self.ts_y))
        return (text)

    #-----------------------------------------------------------------------

    def __setitem__(self, index, val):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__setitem__ in tsWxPoint'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __str__(self):
        '''
        Return text representation.
        '''
        return ('(%d, %d)' % (self.ts_x, self.ts_y))

    #-----------------------------------------------------------------------

    def __sub__(self, pt):
        '''
        Subtract pt properties from this and return the result
        '''
        temp = Point.tsGetPointType(pt)
        return (Point(self.ts_x - temp.x, self.ts_y - temp.y))

    #-----------------------------------------------------------------------

    def Get(self):
        '''
        Return the x and y properties as a tuple.
        '''
        return (self.ts_x, self.ts_y)

    #-----------------------------------------------------------------------

    def Set(self, x, y):
        '''
        Set both the x and y properties.
        '''
        self.ts_x = x
        self.ts_y = y

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetPointType(*args):
        '''
        Generate the specified class instance from the specified tuple.
        '''
        if ((len(args) == 2) and \
            (isinstance(args[0], int)) and \
            (isinstance(args[1], int))):

            return (Point(args[0], args[1]))

        elif ((len(args) == 1) and \
              (isinstance(args[0], Point))):

            return (args[0])

        elif ((len(args) == 1) and \
              (isinstance(args[0], tuple)) and \
              (len(args[0]) == 2)):

            theTuple = args[0]
            return (Point(theTuple[0], theTuple[1]))

        else:

##            fmt1 = 'Invalid data "%s" ' % str(theData)
##            fmt2 = 'with type "%s".' % str(type(theData))
##            msg = fmt1 + fmt2
##            print('***** ', msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            return (None)

    #-----------------------------------------------------------------------

    def tsGet_x(self): return self.ts_x
    def tsSet_x(self, value): self.ts_x = value
    def tsDel_x(self): del self.ts_x
    x = property(tsGet_x, tsSet_x, tsDel_x)

    #-----------------------------------------------------------------------

    def tsGet_y(self): return self.ts_y
    def tsSet_y(self, value): self.ts_y = value
    def tsDel_y(self): del self.ts_y
    y = property(tsGet_y, tsSet_y, tsDel_y)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    wxPoint = Point

    thePoint = wxPoint(x=100, y=200)
    print('thePoint: %s; x: %d; y: %d' % (thePoint, thePoint.x, thePoint.y))
    thePoint.Set(thePoint.x * 3, thePoint.y * 4)
    print('thePoint: %s; x: %d; y: %d' % (thePoint, thePoint.x, thePoint.y))

    pt = wxPoint(x=10, y=20)
    print('pt: %s; x: %d; y: %d' % (pt, pt.x, pt.y))

    theSum = thePoint.__add__(pt)
    print('__add__: %s; x: %d; y: %d' % (theSum, theSum.x, theSum.y))

    theEq = thePoint.__eq__(thePoint)
    print('__eq__: %s; thePoint: %s; thePoint: %s' % (
        theEq, str(thePoint), str(thePoint)))

    theEq = thePoint.__eq__(pt)
    print('__eq__: %s; thePoint: %s; pt: %s' % (
        theEq, str(thePoint), str(pt)))

    theSum = thePoint.__iadd__(pt)
    print('__iadd__: %s; x: %d; y: %d' % (theSum, theSum.x, theSum.y))

    theNe = thePoint.__ne__(thePoint)
    print('__ne__: %s; thePoint: %s; thePoint: %s' % (
        theNe, str(thePoint), str(thePoint)))

    theNe = thePoint.__ne__(pt)
    print('__ne__: %s; thePoint: %s; pt: %s' % (
        theNe, str(thePoint), str(pt)))

    theSum = thePoint.__sub__(pt)
    print('__sub__: %s; x: %d; y: %d' % (theSum, theSum.x, theSum.y))

    theSum = thePoint.__isub__(pt)
    print('__isub__: %s; x: %d; y: %d' % (theSum, theSum.x, theSum.y))

    print('Get: %s; x: %d; y: %d' % (thePoint.Get(), thePoint.x, thePoint.y))

    thePoint.Set(x=500, y=600)
    print('Set: %s; x: %d; y: %d' % (thePoint.Get(), thePoint.x, thePoint.y))

    theInput = [1, 2]
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(1, 2)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = wxPoint(2, 3)
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (3, 4)
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = [4, 5]
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (5, 6, 7)
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (6)
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (7.0)
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = 8
    theInputType = str(type(theInput))
    theOutput = wxPoint.tsGetPointType(theInput)
    print('\n\ntsGetPointType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))
