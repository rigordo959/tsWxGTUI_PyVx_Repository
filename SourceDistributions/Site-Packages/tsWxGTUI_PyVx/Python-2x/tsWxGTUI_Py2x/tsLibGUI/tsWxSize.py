#! /usr/bin/env python
# "Time-stamp: <03/28/2015  7:27:35 PM rsg>"
'''
tsWxSize.py - Class to represent the size of a graphical object
with integer width (horizontal) and height (vertical) properties.
'''
#################################################################
#
# File: tsWxSize.py
#
# Purpose:
#
#    Class to represent the size of a graphical object with
#    integer width (horizontal) and height (vertical) properties.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSize import Size
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

__title__     = 'tsWxSize'
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

class Size(object):
    '''
    wx.Size is a useful data structure used to represent the size of
    something. It simply contains integer width and height properties.
    In most places in wxPython where a wx.Size is expected a (width,
    height) tuple can be used instead.
    '''
    def __init__(self, w=0, h=0):
        '''
        Constructor. Creates a size object.
        '''
##        theClass = 'Size'
##        self.tsRegisterClassNameAndMembershipFlag(theClass)

        self.ts_width = w
        self.ts_height = h

    #-----------------------------------------------------------------------

    def __add__(self, sz):
        '''
        Add sz properties to this and return the result.
        '''
        temp = Size.tsGetSizeType(sz)
        return (Size(self.ts_width + sz.width,
                     self.ts_height + sz.height))

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        Under Construction.
        '''
        del self.ts_width
        del self.ts_height
        del self

    #-----------------------------------------------------------------------

    def __eq__(self, other):
        '''
        Test for equality of wx.Size objects.
        '''
        temp = Size.tsGetSizeType(other)
        return ((self.ts_width == other.width) and \
                (self.ts_height == other.height))

    #-----------------------------------------------------------------------

    def __getitem__(self, index):
        '''
        Under Construction.
        '''
        values = [self.ts_width, self.ts_height]
        try:

            return (self[index])

        except Exception, errorCode:

            return (None)
##            msg = 'NotImplementedError: (%s) index (%s) for %s' % \
##                  (errorCode, index, '__getitem__ in tsWxSize')
##            print(msg)
##            # self.logger.error(msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __len__(self):
        '''
        Return length of object.
        '''
        return (len(self))

    #-----------------------------------------------------------------------

    def __ne__(self, other):
        '''
        Test for inequality of wx.Size objects.
        '''
        temp = Size.tsGetSizeType(other)
        return ((self.ts_width != other.width) or \
                (self.ts_height != other.height))

    #-----------------------------------------------------------------------

    def __nonzero__(self):
        '''
        Return True if not zero.
        '''
        return (self.ts_width != 0 and \
                self.ts_height != 0)

    #-----------------------------------------------------------------------

    def __reduce__(self):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__reduce__ in tsWxSize'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __repr__(self):
        '''
        Return text representation.
        '''
        text = str((self.ts_width, self.ts_height))
        return (text)

    #-----------------------------------------------------------------------

    def __setitem__(self, index, val):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__setitem__ in tsWxSize'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __str__(self):
        '''
        Return text representation.
        '''
        return ('(%d, %d)' % (self.ts_width, self.ts_height))

    #-----------------------------------------------------------------------

    def __sub__(self, sz):
        '''
        Subtract sz proprties from this and return the result
        '''
        temp = Size.tsGetSizeType(sz)
        return (Size(self.ts_width - temp.width,
                     self.ts_height - temp.height))

    #-----------------------------------------------------------------------

    def DecBy(self, dx, dy):
        '''
        Scales the dimensions of this object by the given factors.
        '''
        self.ts_width -= dx
        self.ts_height -= dy

    #-----------------------------------------------------------------------

    def DecTo(self, sz):
        '''
        Decrements this object so that both of its dimensions are
        not greater than the corresponding dimensions of the size.
        '''
        temp = Size.tsGetSizeType(sz)
        if self.ts_width > temp.width:
            self.ts_width = temp.width

        if self.ts_height > temp.height:
            self.ts_height = temp.height

    #-----------------------------------------------------------------------

    def Get(self):
        '''
        Return the x and y properties as a tuple.
        '''
        return (self.ts_width, self.ts_height)

    #-----------------------------------------------------------------------

    def GetHeight(self):
        '''
        Return the y properties.
        '''
        return (self.ts_height)

    #-----------------------------------------------------------------------

    def GetWidth(self):
        '''
        Return the x properties.
        '''
        return (self.ts_width)

    #-----------------------------------------------------------------------

    def IncBy(self, dx, dy):
        '''
        Scales the dimensions of this object by the given factors.
        '''
        self.ts_width += dx
        self.ts_height += dy

    #-----------------------------------------------------------------------

    def IncTo(self, sz):
        '''
        Increments this object so that both of its dimensions are
        not less than the corresponding dimensions of the size.
        '''
        temp = Size.tsGetSizeType(sz)

        if self.ts_width < temp.width:
            self.ts_width = temp.width

        if self.ts_height < temp.height:
            self.ts_height = temp.height

    #-----------------------------------------------------------------------

    def IsFullySpecified(self):
        '''
        Returns True if both components of the size are non-default
        values.
        '''
        return (self.ts_width != -1 and self.ts_height != -1)

    #-----------------------------------------------------------------------

    def Scale(self, xscale, yscale):
        '''
        Scales the dimensions of this object by the given factors.
        '''
        self.ts_width = self.ts_width * xscale
        self.ts_height = self.ts_height * yscale

    #-----------------------------------------------------------------------

    def Set(self, w, h):
        '''
        Set both the w and h properties.
        '''
        self.ts_width = w
        self.ts_height = h

    #-----------------------------------------------------------------------

    def SetDefaults(self, size):
        '''
        Combine this size with the other one replacing the default
        components of this object (i.e..
        '''
        temp = Size.tsGetSizeType(size)

        if self.ts_width == -1:
            self.ts_width = temp.width

        if self.ts_height == -1:
            self.ts_height = temp.height

    #-----------------------------------------------------------------------

    def SetHeight(self, h):
        '''
        Set both the h properties.
        '''
        self.ts_height = h

    #-----------------------------------------------------------------------

    def SetWidth(self, w):
        '''
        Set both the w properties.
        '''
        self.ts_width = w

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetSizeType(*args):
        '''
        Generate the specified class instance from the specified tuple.
        '''
        if ((len(args) == 2) and \
            (isinstance(args[0], int)) and \
            (isinstance(args[1], int))):

            return (Size(args[0], args[1]))

        elif ((len(args) == 1) and \
              (isinstance(args[0], Size))):

            return (args[0])

        elif ((len(args) == 1) and \
              (isinstance(args[0], tuple)) and \
              (len(args[0]) == 2)):

            theTuple = args[0]
            return (Size(theTuple[0], theTuple[1]))

        else:

##            fmt1 = 'Invalid data "%s" ' % str(theData)
##            fmt2 = 'with type "%s".' % str(type(theData))
##            msg = fmt1 + fmt2
##            print('***** ', msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            return (None)

    #-----------------------------------------------------------------------

    width = property(GetWidth, SetWidth)
    height = property(GetHeight, SetHeight)
    x = property(GetWidth, SetWidth)
    y = property(GetHeight, SetHeight)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    wxSize = Size

    theSize = wxSize(100, 200)
    print('theSize: %s; x: %d; y: %d' % (
        theSize, theSize.x, theSize.y))

    print('theSize: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))
 
    theSize.Set(theSize.width * 3, theSize.height * 4)
    print('theSize: %s; x: %d; y: %d' % (
        theSize, theSize.x, theSize.y))

    print('theSize: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))


    sz = wxSize(w=10, h=20)
    print('pt: %s; width: %d; height: %d' % (
        sz, sz.width, sz.height))

    theSum = theSize.__add__(sz)
    print('__add__: %s; width: %d; height: %d' % (
        theSum, theSum.width, theSum.height))

    theEq = theSize.__eq__(theSize)
    print('__eq__: %s; theSize: %s; theSize: %s' % (
        theEq, str(theSize), str(theSize)))

    theEq = theSize.__eq__(sz)
    print('__eq__: %s; theSize: %s; sz: %s' % (
        theEq, str(theSize), str(sz)))

    theNe = theSize.__ne__(theSize)
    print('__ne__: %s; theSize: %s; theSize: %s' % (
        theNe, str(theSize), str(theSize)))

    theNe = theSize.__ne__(sz)
    print('__ne__: %s; theSize: %s; sz: %s' % (
        theNe, str(theSize), str(sz)))

    theSum = theSize.__sub__(sz)
    print('__sub__: %s; width: %d; height: %d' % (
        theSum, theSum.width, theSum.height))

    theSize.DecTo(sz)
    print('DecTo: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))

    print('Get: %s; x: %d; y: %d' % (theSize.Get(), theSize.x, theSize.y))

    theSize.Set(w=500, h=600)
    print('Set: %s; x: %d; y: %d' % (theSize.Get(), theSize.x, theSize.y))

    sz = wxSize(w=10, h=20)
    theSize = wxSize(100, 200)
    theSize.DecTo(sz)
    print('DecTo: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))

    theSize = wxSize(w=10, h=20)
    sz = wxSize(100, 200)
    theSize.IncTo(sz)
    print('IncTo: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))

    theSize = wxSize(w=100, h=200)
    theSize.Scale(0.25, 1.5)
    print('Scale: %s; width: %d; height: %d' % (
        theSize, theSize.width, theSize.height))

    theInput = [1, 2]
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(1, 2)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = wxSize(2, 3)
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (3, 4)
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = [4, 5]
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (5, 6, 7)
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (6)
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (7.0)
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = 8
    theInputType = str(type(theInput))
    theOutput = wxSize.tsGetSizeType(theInput)
    print('\n\ntsGetSizeType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))
