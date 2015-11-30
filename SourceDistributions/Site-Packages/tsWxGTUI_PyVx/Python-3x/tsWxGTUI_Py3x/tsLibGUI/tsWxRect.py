#! /usr/bin/env python
# "Time-stamp: <04/08/2015  3:52:57 AM rsg>"
'''
tsWxRect.py - Class to represent the position and size of a
graphical object with integer x (horizontal) and y (vertical)
postion and with integer width (horizontal) and height (vertical)
size properties.
'''
#################################################################
#
# File: tsWxRect.py
#
# Purpose:
#
#    Class to represent the position and size of a
#    graphical object with integer x (horizontal) and y (vertical)
#    postion and with integer width (horizontal) and height (vertical)
#    size properties.
#
# Usage (example):
#
#    # Import
#
#    from tsWxRect import wxRect
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
#    1. Finish construction.
#    2. Test Intersect and Intersects..
#
#################################################################

__title__     = 'tsWxRect'
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

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py3x.tsLibGUI import tsWxPoint
from tsWxGTUI_Py3x.tsLibGUI import tsWxSize

wxPoint = tsWxPoint.Point
wxSize = tsWxSize.Size

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Rect(object):
    '''
    A class for representing and manipulating rectangles. It has x, y, width
    and height properties. In wxPython most places that expect a wx.Rect can
    also accept a (x,y,width,height) tuple.
    '''
    def __init__(self, x=0, y=0, width=0, height=0):
        '''
        Create a new Rect object.
        '''
##        theClass = 'Rect'
##        self.tsRegisterClassNameAndMembershipFlag(theClass)

        self.ts_x = x
        self.ts_y = y
        self.ts_width = width
        self.ts_height = height

    #-----------------------------------------------------------------------

    def __add__(self, rect):
        '''
        Add the properties of rect to this rectangle and return the result.
        '''
        temp = Rect.tsGetRectType(rect)
        return (Rect(x=self.ts_x + temp.x,
                     y=self.ts_y + temp.y,
                     width=self.ts_width + temp.width,
                     height=self.ts_height + temp.height))

    #-----------------------------------------------------------------------
 
##    def __del__(self):
##        '''
##        Under Construction.
##        '''
##        del self.ts_x
##        del self.ts_y
##        del self.ts_width
##        del self.ts_height
##        del self

    #-----------------------------------------------------------------------

    def __eq__(self, other):
        '''
        Test for equality of wx.Rect objects.
        '''
        temp = Rect.tsGetRectType(other)
        return ((self.ts_x == temp.x) and \
                (self.ts_y == temp.y) and \
                (self.ts_width == temp.width) and \
                (self.ts_height == temp.height))

    #-----------------------------------------------------------------------

    def __getitem__(self, index):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__getitem__ in tsWxRect'
        #self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __iadd__(self, rect):
        '''
        Add the properties of rect to this rectangle, updating this rectangle.
        '''
        self.ts_x += rect.x
        self.ts_y += rect.y
        self.ts_width += rect.width
        self.ts_height += rect.height
        return (Rect(self.ts_x, self.ts_y, self.ts_width, self.ts_height))

    #-----------------------------------------------------------------------

    def __len__(self):
        '''
        Return length of this object.
        '''
        return (len(self))

    #-----------------------------------------------------------------------

    def __ne__(self, other):
        '''
        Test for inequality of wx.Rect objects.
        '''
        temp = Rect.tsGetRectType(other)
        return ((self.ts_x != temp.x) or \
                (self.ts_y != temp.y) or \
                (self.ts_width != temp.width) or \
                (self.ts_height != temp.height))

    #-----------------------------------------------------------------------

    def __bool__(self):
        '''
        Return True if this object is not zero.
        '''
        return (self.ts_x != 0 and \
                self.ts_y !=0 and \
                self.ts_width != 0 and \
                self.ts_height != 0)

    #-----------------------------------------------------------------------

    def __reduce__(self):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__reduce__ in tsWxRect'
        #self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __repr__(self):
        '''
        Return text representation.
        '''
        text = str((self.ts_x, self.ts_y, self.ts_width, self.ts_height))
        return (text)

    #-----------------------------------------------------------------------

    def __setitem__(self, index, val):
        '''
        Under Construction.
        '''
        msg = 'NotImplementedError: %s' % '__setitem__ in tsWxRect'
        #self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def __str__(self):
        '''
        Return text representation.
        '''
        text = '(%d, %d, %d, %d)'  % (
            self.ts_x, self.ts_y, self.ts_width, self.ts_height)
        return (text)

    #-----------------------------------------------------------------------

    def CenterIn(self, r, dir=wx.BOTH):
        '''
        Center this rectangle within the one passed to the method, which
        is usually, but not necessarily, the larger one.
        '''
        temp = Rect.tsGetRectType(r)

        containerX = temp.x
        containerY = temp.y
        containerWidth = temp.width
        containerHeight = temp.height

        # centerX = self.ts_x
        # centerY = self.ts_y
        centerWidth = self.ts_width
        centerHeight = self.ts_height

        if dir == wx.HORIZONTAL:

            centerDeltaX = (containerWidth - centerWidth) // 2
            centerDeltaY = 0

        elif dir == wx.VERTICAL:

            centerDeltaX = 0
            centerDeltaY = (containerHeight - centerHeight) // 2

        else:

            centerDeltaX = (containerWidth - centerWidth) // 2
            centerDeltaY = (containerHeight - centerHeight) // 2

        return (Rect(containerX + centerDeltaX,
                     containerY + centerDeltaY,
                     centerWidth,
                     centerHeight))

    #-----------------------------------------------------------------------

    def CentreIn(self, r, dir=wx.BOTH):
        '''
        Center this rectangle within the one passed to the method, which
        is usually, but not necessarily, the larger one.
        '''
        self.CenterIn(r, dir)

    #-----------------------------------------------------------------------

    def Contains(self, pt):
        '''
        Return True if the point is inside the rect.
        '''
        return (self.ContainsXY(pt.x, pt.y))

    #-----------------------------------------------------------------------

    def ContainsRect(self, rect):
        '''
        Returns True if the given rectangle is completely inside this
        rectangle or touches its boundary.
        '''
        temp = Rect.tsGetRectType(rect)

        return (
            ((self.ts_x <= temp.x) and \

             ((temp.x + temp.width - 1) <= \
              (self.ts_x + self.ts_width - 1)) and \

             (self.ts_y <= temp.y) and \

              ((temp.y + temp.height - 1) <= \
               (self.ts_y + self.ts_height - 1))))

    #-----------------------------------------------------------------------

    def ContainsXY(self, x, y):
        '''
        Return True if the point is inside the rect.
        '''
        return ((self.ts_x <= x and \
                 x < self.ts_x + self.ts_width) and \
                (self.ts_y <= y and \
                 y < self.ts_y + self.ts_height))

    #-----------------------------------------------------------------------

    def Deflate(self, dx, dy):
        '''
        Decrease the rectangle size. This method is the opposite of Inflate
        in that Deflate(a,b) is equivalent to Inflate(-a,-b). Please refer
        to Inflate for a full description.
        '''
        self.ts_x += dx
        self.ts_y += dy
        self.ts_width -= dx * 2
        self.ts_height -= dy * 2

    #-----------------------------------------------------------------------

    def Get(self):
        '''
        Return the rectangle properties as a tuple.
        '''
        return (self.GetX(),
                self.GetY(),
                self.GetWidth(),
                self.GetHeight())

    #-----------------------------------------------------------------------

    def GetBottom(self):
        '''
        '''
        return (self.ts_y + self.ts_height - 1)

    #-----------------------------------------------------------------------

    def GetBottomLeft(self):
        '''
        '''
        return (wxPoint(self.ts_x, self.ts_y + self.ts_height - 1))

    #-----------------------------------------------------------------------

    def GetBottomRight(self):
        '''
        '''
        return (wxPoint(self.ts_x + self.ts_width - 1,
                        self.ts_y + self.ts_height - 1))

    #-----------------------------------------------------------------------

    def GetHeight(self):
        '''
        '''
        return (self.ts_height)

    #-----------------------------------------------------------------------

    def GetLeft(self):
        '''
        '''
        return (self.ts_x)

    #-----------------------------------------------------------------------

    def GetPosition(self):
        '''
        '''
        return (wxPoint(self.ts_x, self.ts_y))

    #-----------------------------------------------------------------------

    def GetRight(self):
        '''
        '''
        return (self.ts_x + self.ts_width - 1)

    #-----------------------------------------------------------------------

    def GetSize(self):
        '''
        '''
        return (wxSize(w=self.ts_width, h=self.ts_height))

    #-----------------------------------------------------------------------

    def GetTop(self):
        '''
        '''
        return (self.ts_y)

    #-----------------------------------------------------------------------

    def GetTopLeft(self):
        '''
        '''
        return (wxPoint(self.ts_x, self.ts_y))

    #-----------------------------------------------------------------------

    def GetTopRight(self):
        '''
        '''
        return (wxPoint(self.ts_x + self.ts_width - 1, self.ts_y))

    #-----------------------------------------------------------------------

    def GetWidth(self):
        '''
        '''
        return (self.ts_width)

    #-----------------------------------------------------------------------

    def GetX(self):
        '''
        '''
        return (self.ts_x)

    #-----------------------------------------------------------------------

    def GetY(self):
        '''
        '''
        return (self.ts_y)

    #-----------------------------------------------------------------------

    def Inflate(self, dx, dy):
        '''
        Increases the size of the rectangle.

        The left border is moved farther left and the right border is moved
        farther right by dx. The upper border is moved farther up and the
        bottom border is moved farther down by dy. (Note the the width and
        height of the rectangle thus change by 2*dx and 2*dy, respectively.)
        If one or both of dx and dy are negative, the opposite happens: the
        rectangle size decreases in the respective direction.

        The change is made to the rectangle inplace, if instead you need a
        copy that is inflated, preserving the original then make the copy
        first:

        copy = wx.Rect(*original)
        copy.Inflate(10,15)

        Inflating and deflating behaves naturally. Defined more precisely,
        that means:

        * Real inflates (that is, dx and/or dy >= 0) are not constrained.
        Thus inflating a rectangle can cause its upper left corner to move
        into the negative numbers. (The versions prior to 2.5.4 forced the
        top left coordinate to not fall below (0, 0), which implied a forced
        move of the rectangle.)
 
        * Deflates are clamped to not reduce the width or height of the
        rectangle below zero. In such cases, the top-left corner is
        nonetheless handled properly. For example, a rectangle at (10, 10)
        with size (20, 40) that is inflated by (-15, -15) will become located
        at (20, 25) at size (0, 10). Finally, observe that the width and
        height are treated independently. In the above example, the width is
        reduced by 20, whereas the height is reduced by the full 30 (rather
        than also stopping at 20, when the width reached zero).
        '''
        self.ts_x -= dx
        self.ts_y -= dy
        self.ts_width += dx * 2
        self.ts_height += dy * 2

    #-----------------------------------------------------------------------

    def Inside(self, pt):
        '''
        Return True if the point is inside the rect.
        '''
        temp = wxPoint.tsGetPointType(pt)
        return ((self.x <= temp.x) and \

                (temp.x <= self.x + self.width) and \

                (self.y <= temp.y) and \

                (temp.y <= self.y + self.height))

    #-----------------------------------------------------------------------

    def InsideRect(self, rect):
        '''
        Returns True if the given rectangle is completely inside this
        rectangle or touches its boundary.
        '''
        temp = Rect.tsGetRectType(rect)
        return (self.Inside(temp.GetTopLeft()) and \
                self.Inside(temp.GetTopRight()) and \
                self.Inside(temp.GetBottomLeft()) and \
                self.Inside(temp.GetBottomRight()))

    #-----------------------------------------------------------------------

    def InsideXY(self, x, y):
        '''
        Return True if the point is inside the rect.
        '''
        return (self.Inside(wxPoint(x, y)))

    #-----------------------------------------------------------------------

    def Intersect(self, rect):
        '''
        Returns the intersectsion of this rectangle and rect.
        TBD - Under Construction.
        '''
        temp = Rect.tsGetRectType(rect)

        if self.x <= temp.x:
            aRect = self
            bRect = temp
        else:
            aRect = temp
            bRect = self

        if (aRect.InsideXY(bRect.x,
                           bRect.y) and \
            aRect.InsideXY(bRect.x + bRect.width,
                           bRect.y) and \
            aRect.InsideXY(bRect.x,
                           bRect.y + bRect.height) and \
            aRect.InsideXY(bRect.x + bRect.width,
                           bRect.y + bRect.height)):
            if DEBUG:
                print('\n\n***** Enclosed: %s %s' % (aRect, bRect))

            # Rectangle A encloses B.
            # +-----------+
            # |      A    |
            # |  O-----O  |
            # |  |     |  |
            # |  |   B |  |
            # |  |     |  |
            # |  O-----O  |
            # |           |
            # +-----------+
            return (bRect)

        elif ((aRect.InsideXY(bRect.x,
                              bRect.y + bRect.height) and \
               aRect.InsideXY(bRect.x + bRect.width,
                              bRect.y + bRect.height)) and \
              not (aRect.InsideXY(bRect.x,
                                  bRect.y) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y))):
            # Rectangle A encloses bottom side of B.
            #    +-----+
            #    |  B  |
            # +--O-----O--+
            # |  |     |  |
            # |  O-----O  |
            # |     A     |
            # +-----------+
            if DEBUG:
                print('\n\n***** Above: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           aRect.y,
                           bRect.width,
                           bRect.height - (aRect.y - bRect.y)))

        elif (aRect.InsideXY(bRect.x,
                             bRect.y + bRect.height) and \
              not (aRect.InsideXY(bRect.x,
                                  bRect.y) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y + bRect.height))):
            # Rectangle A encloses lower left corner of B.
            #    +-----------+
            #    |   B       |
            # +--O--------O  |
            # |  |        |  |
            # |  O--------O--+
            # |      A    |
            # +-----------+
            if DEBUG:
                print('\n\n***** TopRight: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           aRect.y,
                           aRect.width - (bRect.x - aRect.x),
                           aRect.height - (aRect.y - bRect.y)))

        elif (bRect.InsideXY(aRect.x + aRect.width,
                             aRect.y) and \
              (bRect.InsideXY(aRect.x + aRect.width,
                              aRect.y + aRect.height))):
            # Rectangle A inserted into left side of B.
            #    +-----------+
            #    |   B       |
            # +--O--------O  |
            # |  |        |  |
            # |  |   A    |  |
            # |  |        |  |
            # +--O--------O  |
            #    |           |
            #    +-----------+
            if DEBUG:
                print('\n\n***** RightHalf: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           aRect.y,
                           aRect.width - (bRect.x - aRect.x),
                           aRect.height))

        elif (aRect.InsideXY(bRect.x,
                             bRect.y) and \
              not (aRect.InsideXY(bRect.x,
                                  bRect.y + bRect.height) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y + bRect.height))):
            # Rectangle A encloses top left corner of B.
            # +-----------+
            # |      A    |
            # |  O--------O--+
            # |  |        |  |
            # +--O--------O  |
            #    |   B       |
            #    +-----------+
            if DEBUG:
                print('\n\n***** BottomRight: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           bRect.y,
                           aRect.width - (bRect.x - aRect.x),
                           aRect.height - (bRect.y - aRect.y)))

        elif ((aRect.InsideXY(bRect.x,
                              bRect.y) and \
               aRect.InsideXY(bRect.x + bRect.width,
                              bRect.y)) and \
              not (aRect.InsideXY(bRect.x,
                                  bRect.y + bRect.height) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y + bRect.height))):
            # Rectangle A encloses top side of B.
            # +-----------+
            # |      A    |
            # |  O-----O  |
            # |  |     |  |
            # +--O-----O--+
            #    |   B |
            #    +-----+
            if DEBUG:
                print('\n\n***** Below: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           bRect.y,
                           bRect.width,
                           aRect.height - (bRect.y - aRect.y)))

        elif ((aRect.InsideXY(bRect.x,
                              bRect.y) and \
               aRect.InsideXY(bRect.x,
                              bRect.y + bRect.height)) and \
              not (aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y) and \
                   aRect.InsideXY(bRect.x + bRect.width,
                                  bRect.y + bRect.height))):
            # Rectangle A encloses left side of B.
            # +-----------+
            # |      A    |
            # |  O--------O---+
            # |  |        |   |
            # |  |        | B |
            # |  |        |   |
            # |  O--------O---+
            # |           |
            # +-----------+
            if DEBUG:
                print('\n\n***** LeftSide: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           bRect.y,
                           aRect.width - bRect.x,
                           bRect.height))

        elif (aRect.InsideXY(bRect.x,
                             aRect.y) and \
              aRect.InsideXY(bRect.x + bRect.width,
                             aRect.y) and \
              aRect.InsideXY(bRect.x,
                             aRect.y + aRect.height) and \
              aRect.InsideXY(bRect.x + bRect.width,
                             aRect.y + aRect.height)):
            # Rectangle A encloses center of B.
            #    O-----O
            #    |   B |
            # +--+-----+--+
            # |  |     |A |
            # |  |     |  |
            # +--+-----+--+
            #    |     |
            #    O-----O
            if DEBUG:
                print('\n\n***** MidSection: %s %s' % (aRect, bRect))

            return (wxRect(bRect.x,
                           aRect.y,
                           bRect.width,
                           aRect.height))

        else:
            # No intersection.
            if DEBUG:
                print('\n\n***** NonIntersecting: %s %s' % (aRect, bRect))

            return (wxRect(0, 0, 0, 0))

    #-----------------------------------------------------------------------

    def Intersects(self, rect):
        '''
        Returns True if the rectangles have a non empty intersection.
        TBD - Under Construction; Do NOT Use.
        '''
        temp = Rect.tsGetRectType(rect)
        return (self.Intersect(temp) != wxRect(0, 0, 0, 0))

    #-----------------------------------------------------------------------

    def IsEmpty(self):
        '''
        Under Construction.
        '''
        return (self.ts_width == 0 and self.ts_height == 0)

    #-----------------------------------------------------------------------

    def Offset(self, pt):
        '''
        Same as OffsetXY but uses dx, dy from Point.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.OffsetXY(temp.x, temp.y)

    #-----------------------------------------------------------------------

    def OffsetXY(self, dx, dy):
        '''
        Moves the rectangle by the specified offset. If dx is positive, the
        rectangle is moved to the right, if dy is positive, it is moved to
        the bottom, otherwise it is moved to the left or top respectively.
        '''
        self.ts_x += dx
        self.ts_y += dy

    #-----------------------------------------------------------------------

    def Set(self, x=0, y=0, width=0, height=0):
        '''
        Set all rectangle properties.
        '''
        self.ts_x = x
        self.ts_y = y
        self.ts_width = width
        self.ts_height = height

    #-----------------------------------------------------------------------

    def SetBottom(self, bottom):
        '''
        Under Construction.
        '''
        self.ts_height = bottom + 1 - self.ts_y

    #-----------------------------------------------------------------------

    def SetBottomLeft(self, pt):
        '''
        Under Construction.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.ts_x = temp.x
        self.ts_height = temp.y + 1 - self.ts_y

    #-----------------------------------------------------------------------

    def SetBottomRight(self, pt):
        '''
        Under Construction.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.ts_width = temp.x + 1 - self.ts_x
        self.ts_height = temp.y + 1 - self.ts_y

    #-----------------------------------------------------------------------

    def SetHeight(self, h):
        '''
        Under Construction.
        '''
        self.ts_height = h

    #-----------------------------------------------------------------------

    def SetLeft(self, left):
        '''
        Under Construction.
        '''
        self.ts_x = left

    #-----------------------------------------------------------------------

    def SetPosition(self, pt):
        '''
        Under Construction.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.ts_x = temp.x
        self.ts_y = temp.y

    #-----------------------------------------------------------------------

    def SetRight(self, right):
        '''
        Under Construction.
        '''
        self.ts_width = right + 1 - self.ts_x

    #-----------------------------------------------------------------------

    def SetSize(self, sz):
        '''
        Under Construction.
        '''
        temp = wxSize.tsGetSizeType(sz)
        self.ts_width = temp.width
        self.ts_height = temp.height

    #-----------------------------------------------------------------------

    def SetTop(self, top):
        '''
        Under Construction.
        '''
        self.ts_y = top

    #-----------------------------------------------------------------------

    def SetTopLeft(self, pt):
        '''
        Under Construction.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.ts_x = temp.x
        self.ts_y = temp.y

    #-----------------------------------------------------------------------

    def SetTopRight(self, pt):
        '''
        Under Construction.
        '''
        temp = wxPoint.tsGetPointType(pt)
        self.ts_width = temp.y + 1 - self.ts_x
        self.ts_y = temp.y

    #-----------------------------------------------------------------------

    def SetWidth(self, w):
        '''
        Under Construction.
        '''
        self.ts_width = w

    #-----------------------------------------------------------------------

    def SetX(self, x):
        '''
        Under Construction.
        '''
        self.ts_x = x

    #-----------------------------------------------------------------------

    def SetY(self, y):
        '''
        Under Construction.
        '''
        self.ts_y = y

    #-----------------------------------------------------------------------

    def Union(self, rect):
        '''
        Under Construction.
 
        Returns the rectangle containing the bounding box of this rectangle
        and the one passed in as parameter.
        '''
        temp = Rect.tsGetRectType(rect)

        left = min(self.Left,
                   temp.Left)

        right = max(self.Left + self.Width,
                    temp.Left + temp.Width)

        width = right - left

        top = min(self.Top,
                  temp.Top)

        bottom = max(self.Top + self.Height,
                     temp.Top + temp.Height)

        height = bottom - top

        return (wxRect(left, top, width, height))

    #-----------------------------------------------------------------------

    @staticmethod
    def tsGetRectType(*args):
        '''
        Generate the specified class instance from the specified tuple.
        '''
        if ((len(args) == 4) and \
            (isinstance(args[0], int)) and \
            (isinstance(args[1], int)) and \
            (isinstance(args[2], int)) and \
            (isinstance(args[3], int))):

            return (Rect(args[0], args[1], args[2], args[3]))

        elif ((len(args) == 1) and \
              (isinstance(args[0], Rect))):

            return (args[0])

        elif ((len(args) == 1) and \
              (isinstance(args[0], tuple)) and \
              (len(args[0]) == 4)):

            theTuple = args[0]
            return (Rect(theTuple[0], theTuple[1], theTuple[2], theTuple[3]))

        else:

##            fmt1 = 'Invalid data "%s" ' % str(theData)
##            fmt2 = 'with type "%s".' % str(type(theData))
##            msg = fmt1 + fmt2
##            print('***** ', msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
            return (None)

    #-----------------------------------------------------------------------

    Bottom = property(GetBottom, SetBottom)
    BottomLeft = property(GetBottomLeft, SetBottomLeft)
    BottomRight = property(GetBottomRight, SetBottomRight)
    Empty = property(IsEmpty)
    Height = property(GetHeight, SetHeight)
    Left = property(GetLeft, SetLeft)
    Position = property(GetPosition, SetPosition)
    Right = property(GetRight, SetRight)
    Size = property(GetSize, SetSize)
    Top = property(GetTop, SetTop)
    TopLeft = property(GetTopLeft, SetTopLeft)
    TopRight = property(GetTopRight, SetTopRight)
    Width = property(GetWidth, SetWidth)
    X = property(GetX, SetX)
    Y = property(GetY, SetY)
    height = property(GetHeight, SetHeight)
    width = property(GetWidth, SetWidth)
    x = property(GetLeft, SetLeft)
    y = property(GetTop, SetTop)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    wxRect = Rect

    theRect = wxRect(x=100, y=200, width=300, height=400)
    print('theRect: %s; x: %d; y: %d; width: %d; height: %d' % \
          (theRect, theRect.x, theRect.y, theRect.width, theRect.height))

    print('Bottom: %s' % theRect.Bottom)
    print('BottomLeft: %s' % theRect.BottomLeft)
    print('BottomRight %s' % theRect.BottomRight)
    print('Empty: %s' % theRect.Empty)
    print('Height: %s' % theRect.Height)
    print('Left: %s' % theRect.Left)
    print('Position: %s' % theRect.Position)
    print('Right: %s' % theRect.Right)
    print('Size: %s' % theRect.Size)
    print('Top: %s' % theRect.Top)
    print('TopLeft: %s' % theRect.TopLeft)
    print('TopRight: %s' % theRect.TopRight)
    print('Width: %s' % theRect.Width)
    print('X: %s' % theRect.X)
    print('Y: %s' % theRect.Y)
    print('x: %s' % theRect.x)
    print('y: %s' % theRect.y)

    smallRect = wxRect(x=10, y=20, width=30, height=40)
    print('smallRect: %s; x: %d; y: %d; width: %d; height: %d' % \
          (smallRect, smallRect.x, smallRect.y,
           smallRect.width, smallRect.height))

    print('__add__:',theRect.__add__(smallRect))

    print('__eq__ (True):',theRect.__eq__(theRect))
    print('__eq__ (False):',theRect.__eq__(smallRect))

    print('__ne__ (False):',theRect.__ne__(theRect))
    print('__ne__ (True):',theRect.__ne__(smallRect))

    print('__add__:',theRect.__add__(smallRect))

    zeroRect = wxRect(x=0, y=0, width=0, height=0)
    print('__nonzero__ (True):',theRect.__nonzero__())
    print('__nonzero__ (False):',zeroRect.__nonzero__())

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.Top()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.TopLeft()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.TopRight()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.Bottom()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.BottomLeft()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.BottomRight()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.Left()

##    zeroRect = wxRect(x=0, y=0, width=0, height=0)
##    zeroRect.Right()

    theRect.Set(x=theRect.x * 3,
                y=theRect.y * 4,
                width=theRect.width * 5,
                height=theRect.height * 6)

    print('Set: %s; x: %d; y: %d; width: %d; height: %d' % \
          (theRect, theRect.x, theRect.y, theRect.width, theRect.height))

    contents = wxRect(x=10, y=20, width=30, height=40)
    package = wxRect(x=100, y=200, width=300, height=400)
    cutout = contents.CenterIn(package, dir=wx.BOTH)
    print('CenterIn       (Both): %s; x: %d; y: %d; width: %d; height: %d' % \
          (cutout,
           cutout.x, cutout.y,
           cutout.width, cutout.height))

    contents = wxRect(x=10, y=20, width=30, height=40)
    package = wxRect(x=100, y=200, width=300, height=400)
    cutout = contents.CenterIn(package, dir=wx.HORIZONTAL)
    print('CenterIn (Horizontal): %s; x: %d; y: %d; width: %d; height: %d' % \
          (cutout,
           cutout.x, cutout.y,
           cutout.width, cutout.height))

    contents = wxRect(x=10, y=20, width=30, height=40)
    package = wxRect(x=100, y=200, width=300, height=400)
    cutout = contents.CenterIn(package, dir=wx.VERTICAL)
    print('CenterIn   (Vertical): %s; x: %d; y: %d; width: %d; height: %d' % \
          (cutout,
           cutout.x, cutout.y,
           cutout.width, cutout.height))

    # Under Construction.
    #    Test cases use inappropriate input values.
    theRect = wxRect(x=100, y=100, width=100, height=100)
    theNonIntersectingRect = wxRect(x=100+200,
                                    y=100+200,
                                    width=25,
                                    height=50)
    theAboveRect = wxRect(x=150, y=100 - 10, width=25, height=50)
    theBelowRect = wxRect(x=150, y=200 - 10, width=25, height=50)
    theRightSideRect = wxRect(x=200 - 10, y=100 + 10, width=25, height=50)
    theLeftSideRect = wxRect(x=100 + 10, y=100 + 10, width=25, height=50)
    theTopRightCornerRect = wxRect(x=200 - 10, y=100 - 10, width=25, height=50)
    theBottomRightCornerRect = wxRect(x=200 - 10, y=200 + 10, width=25, height=50)
    theRightHalfRect = wxRect(x=200 - 10, y=100 - 10, width=25, height=800)
    theLeftHalfRect = wxRect(x=100 - 10, y=100 - 10, width=25, height=800)
    theMidSectionRect = wxRect(x=100 + 10, y=100 - 10, width=25, height=800)

    # Intersection of theRect and itself
    print('\nIntersect theNonIntersectingRect: %s' % theRect.Intersect(theNonIntersectingRect))
    print('Intersects theNonIntersectingRect=(False): %s' % theRect.Intersects(theNonIntersectingRect))

    print('\nIntersect self: %s' % theRect.Intersect(theRect))
    print('Intersects self=(True): %s' % theRect.Intersects(theRect))

    print('\nIntersect above: %s' % theRect.Intersect(theAboveRect))
    print('Intersects above=(True): %s' % theRect.Intersects(theAboveRect))

    print('\nIntersect below: %s' % theRect.Intersect(theBelowRect))
    print('Intersects below=(True): %s' % theRect.Intersects(theBelowRect))

    print('\nIntersect RightSide: %s' % theRect.Intersect(theRightSideRect))
    print('Intersects RightSide=(True): %s' % theRect.Intersects(theRightSideRect))

    print('\nIntersect LeftSide: %s' % theRect.Intersect(theLeftSideRect))
    print('Intersects LeftSide=(True): %s' % theRect.Intersects(theLeftSideRect))

    print('\nIntersect TopRight: %s' % theRect.Intersect(theTopRightCornerRect))
    print('Intersects TopRight=(True): %s' % theRect.Intersects(theTopRightCornerRect))

    print('\nIntersect BottomRight: %s' % theRect.Intersect(theBottomRightCornerRect))
    print('Intersects BottomRight=(True): %s' % theRect.Intersects(theBottomRightCornerRect))

    print('\nIntersect RightHalf: %s' % theRect.Intersect(theRightHalfRect))
    print('Intersects RightHalf=(True): %s' % theRect.Intersects(theRightHalfRect))

    print('\nIntersect LeftHalf: %s' % theRect.Intersect(theLeftHalfRect))
    print('Intersects LeftHalf=(True): %s' % theRect.Intersects(theLeftHalfRect))

    print('\nIntersect MidSection: %s' % theRect.Intersect(theMidSectionRect))
    print('Intersects MidSection=(True): %s' % theRect.Intersects(theMidSectionRect))

    # Union of theRect and itself
    print('\nUnion theRect: %s; theRect: %s' % \
          (theRect, theRect))
    print('Union just theRect: %s' % theRect.Union(theRect))

    print('\nUnion theNonIntersectingRect: %s; theNonIntersectingRect: %s' % \
          (theNonIntersectingRect, theNonIntersectingRect))
    print('Union just theNonIntersectingRect: %s' % \
          theNonIntersectingRect.Union(theNonIntersectingRect))

    print('\nUnion theRect: %s; theNonIntersectingRect: %s' % \
          (theRect, theNonIntersectingRect))
    print('Union theRect & theNonIntersectingRect: %s' % theRect.Union(
        theNonIntersectingRect))

    theInput = [1, 2, 3, 4]
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(1, 2, 3, 4)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = wxRect(2, 3, 4, 5)
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s; %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (3, 4, 5, 6)
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = [4, 5, 6, 7]
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (5, 6, 7, 8, 9)
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (6)
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = (7.0)
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))

    theInput = 8
    theInputType = str(type(theInput))
    theOutput = wxRect.tsGetRectType(theInput)
    print('\n\ntsGetRectType (%s): \n\ttheOutput=%s; theInput:=%s %s' % (
        type(theOutput), theOutput, theInput, theInputType))
