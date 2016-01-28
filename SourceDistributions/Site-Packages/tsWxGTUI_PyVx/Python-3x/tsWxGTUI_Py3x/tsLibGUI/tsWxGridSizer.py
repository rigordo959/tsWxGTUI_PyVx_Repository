#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:54:11 AM rsg>"
'''
tsWxGridSizer.py - Class for a sizer which lays out its children
in a two-dimensional table with all table fields having the same
size, i.e. the width of each field is the width of the widest
child, the height of each field is the height of the tallest
child.
'''
#################################################################
#
# File: tsWxGridSizer.py
#
# Purpose:
#
#    Class for a sizer which lays out its children in a
#    two-dimensional table with all table fields having the same
#    size, i.e. the width of each field is the width of the widest
#    child, the height of each field is the height of the tallest
#    child.
#
# Usage (example):
#
#    # Import
#
#    from tsWxGridSizer import GridSizer
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
#    None.
#
# ToDo:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
#################################################################

__title__     = 'tsWxGridSizer'
__version__   = '1.3.2'
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

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizer import Sizer
from tsWxGTUI_Py3x.tsLibGUI.tsWxSizerItem import SizerItem as wxSizerItem

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DEFAULT_POS = wxPoint(wx.DefaultPosition)
DEFAULT_SIZE = wxSize(wx.DefaultSize)

#---------------------------------------------------------------------------
 
class GridSizer(Sizer):
    '''
    A grid sizer is a sizer which lays out its children in a two-dimensional
    table with all cells having the same size. In other words, the width of
    each cell within the grid is the width of the widest item added to the
    sizer and the height of each grid cell is the height of the tallest item.
    An optional vertical and/or horizontal gap between items can also be
    specified (in pixels.)

    Items are placed in the cells of the grid in the order they are added,
    in row-major order. In other words, the first row is filled first, then
    the second, and so on until all items have been added. (If neccessary,
    additional rows will be added as items are added.) If you need to have
    greater control over the cells that items are placed in then use the
    wx.GridBagSizer.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor for a wx.GridSizer. rows and cols determine the number of
        columns and rows in the sizer - if either of the parameters is zero,
        it will be calculated to from the total number of children in the
        sizer, thus making the sizer grow dynamically. vgap and hgap define
        extra space between all children.
        '''
        theClass = 'GridSizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Sizer.__init__(self)

        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        if ((len(args) == 0) and \
            (len(kwargs) == 0)):

            # Instatiate Grid Class without using args or kwargs
            # associated with instantiation variants.

            rows = 0
            cols = 0
            vgap = 0
            hgap = 0

        elif ((len(args) + len(kwargs)) == 2):

            # Instatiate Grid Class without using args or kwargs
            # associated with instantiation variants.

            if ((isinstance(args[0], int)) and \
                (isinstance(args[1], wxSize))):

                # def __init__(self, cols, gap):
                cols = args[0]
                vgap = args[1].height
                hgap = args[1].width

            else:

                # def __init__(self, Cols=0, Gap=wx.DefaultSize):
                cols = kwargs['Col']
                vgap = kwargs['Gap'].height
                hgap = kwargs['Gap'].width

            if cols == 0:
                rows = 1
            else:
                rows = 0

            self.logger.wxASSERT(cols >= 0)

        elif ((len(args) + len(kwargs)) == 3):

            # Instatiate Grid Class without using args or kwargs
            # associated with instantiation variants.

            if ((isinstance(args[0], int)) and \
                (isinstance(args[1], int)) and \
                (isinstance(args[2], int))):

                # def __init__(self, cols, vgap, hgap):
                cols = args[0]
                vgap = args[1]
                hgap = args[2]

                if cols == 0:
                    rows = 1
                else:
                    rows = 0

            elif ((isinstance(args[0], int)) and \
                  (isinstance(args[1], int)) and \
                  (isinstance(args[2], wxSize))):

                # def __init__(self, rows, cols, gap):
                rows = args[0]
                cols = args[1]
                vgap = args[2].height
                hgap = args[2].width

            else:

                # def __init__(self, rows=0, cols=0, gap=wx.DefaultSize):
                rows = kwargs['Rows']
                cols = kwargs['Cols']
                vgap = kwargs['Gap'].height
                hgap = kwargs['Gap'].width

            self.logger.wxASSERT(cols >= 0)

        else:

            # if ((len(args) + len(kwargs)) == 4):

            if (len(args) == 4):

                # Instatiate Grid Class without using args or kwargs
                # associated with instantiation variants.

                # def __init__(self, rows, cols, vgap, hgap):
                rows = args[0]
                cols = args[1]
                vgap = args[2]
                hgap = args[3]

            else:

                # Instatiate Grid Class without using args or kwargs
                # associated with instantiation variants.

                # def __init__(self, rows=1, cols=0, vgap=0, hgap=0):
                rows = kwargs['Rows']
                cols = kwargs['Cols']
                vgap = kwargs['Vgap']
                hgap = kwargs['Hgap']

 
            if ((rows == 0) and \
                (cols == 0)):

                rows = 1

            self.logger.wxASSERT((rows >= 0) and (cols >= 0))

        if ((rows | cols) == 0):
            self.ts_Rows = 1
        else:
            self.ts_Rows = rows

        self.ts_Cols = cols

        self.ts_HGap = hgap

        self.ts_VGap = vgap

##        self.ts_ContainingWindowClientArea = DEFAULT_SIZE

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Add(self, item, proportion=0, flag=0, border=0, userData=None):
        '''
        Appends a child to the sizer.

        wxSizer itself is an abstract class, but the parameters are
        equivalent in the derived classes that you will instantiate to
        use it so they are described here:

        Parameters:
        window  The window to be added to the sizer. Its initial size
        (either set explicitly by the user or calculated internally when
        using wxDefaultSize) is interpreted as the minimal and in many
        cases also the initial size.

        proportion      Although the meaning of this parameter is
        undefined in wxSizer, it is used in wxBoxSizer to indicate if a
        child of a sizer can change its size in the main orientation of
        the wxBoxSizer - where 0 stands for not changeable and a value
        of more than zero is interpreted relative to the value of other
        children of the same wxBoxSizer. For example, you might have a
        horizontal wxBoxSizer with three children, two of which are
        supposed to change their size with the sizer. Then the two
        stretchable windows would get a value of 1 each to make them
        grow and shrink equally with the sizers horizontal dimension.

        flag OR-combination of flags affecting sizers behaviour.
        See wxSizer flags list for details.

        border Determines the border width, if the flag parameter is
        set to include any border flag.

        userData Allows an extra object to be attached to the
        sizer item, for use in derived classes when sizing information
        is more complex than the proportion and flag will allow for.
        '''
        # Create new SizerItem with default addributes
        child = wxSizerItem()

        if isinstance(item, tuple) or \
           isinstance(item, wxSize):

            # Overload the child's wxSizerSpacer attribute
            child.ts_Size = wx.tsGetClassInstanceFromTuple(item, wxSize)
            child.ts_Kind = wx.Item_Spacer
            self.ts_Size = child.ts_Size
            self.logger.debug('Sizer.Add: Tuple=%s' % str(self.ts_Size))

        elif isinstance(item, GridSizer):
 
            # Overload the child's wxSizer attribute
            child.Sizer = item
            child.ts_Kind = wx.Item_Sizer
            self.ts_Size = None
            self.logger.debug('Sizer.Add: Sizer=%s' % str(self.ts_Size))

        else:

            # Overload the child's window attribute
            # Supports Top Level Windows (i.e., Dialogs and Frames)
            # Supports Lower Level Windows (i.e., Buttons, Check Boxes,
            # Gauges, Panels, Radio Boxes, Radio Buttons etc.).
            child.Window = item
            child.ts_Kind = wx.Item_Window
            try:
                self.ts_Size = item.ts_Size
            except AttributeError:
                self.ts_Size = DEFAULT_SIZE
            self.logger.debug('Sizer.Add: Window=%s' % str(self.ts_Size))

        # Overload the child's other attributes
        child.Proportion = proportion
        child.Flag = flag
        child.Border = border
        child.UserData = userData

        # Register the child in the wxSizerItemList
        self.ts_Children.Add(child)
 
        return (child)

    #-----------------------------------------------------------------------

    def CalcCols(self):
        '''
        Returns the number of columns needed for the current total number
        of children (and the fixed number of rows).
        '''

        self.logger.wxCHECK_MSG(
            self.ts_Rows == 0,
            'Cannot calculate number of cols ' + \
            'if number of rows is not specified')

        return (self.GetCount() + self.ts_Rows - 1) / self.ts_Rows

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        This method is where the sizer will do the actual calculation of its
        childrens minimal sizes. You should not need to call this directly
        as it is called by Layout

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        nitems = self.CalcRowsCols()
        if DEBUG:
            print(
                'GridSizes.CalcMin: nitems=%d; Rows=%d; Cols=%d' % (
                    nitems, self.ts_Rows, self.ts_Cols))

        if (nitems == 0):
            return (wxSize(0, 0))

        sizerClientArea = self.FindSizerClientArea()
        self.ts_Rect = sizerClientArea
        self.ts_Position = wxPoint(sizerClientArea.x, sizerClientArea.y)
        self.ts_Size = wxSize(sizerClientArea.width, sizerClientArea.height)
        if DEBUG:
            print(
                'GridSizer.CalcMin: sizerClientArea=%s' % str(sizerClientArea))

        sz = wxSize(
            ((sizerClientArea.width - (
                (self.ts_Cols - 1) * self.ts_HGap)) / self.ts_Cols),
            ((sizerClientArea.height - (
                (self.ts_Rows - 1) * self.ts_VGap)) / self.ts_Rows))

        if DEBUG:
            print(
                'GridSizer.CalcMin: sz=%s; sizerClientArea=%s' % (
                    str(sz),
                    str(sizerClientArea)))

        # Find the max width and height for any component
        w = 0
        h = 0
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item =  node.GetUserData()
            if DEBUG:
                msg = 'GridSizer.CalcMin: item[%d]=%s' % (i, str(item))
                print(msg)

            if (item.ts_Kind == wx.Item_Sizer):
                item.ts_Sizer.Layout()

##            parent = item.ts_Window.ts_Parent
##            clientArea = parent.ClientArea

##            theRect = parent.Rect
##            theClientArea = parent.ClientArea
##            print('GridSizer.CalcMin: Rect=%s; ClientArea=%s' % (
##                str(theRect),
##                str(theClientArea)))

##            tempSize = item.CalcMin()
##            sz = tempSize
##            sz = wxSize((min(tempSize.width,
##                            ((self.ts_ContainingWindowClientArea.width /
##                              self.ts_Cols) - self.ts_Hgap))),
##                        (min(tempSize.width,
##                             ((self.ts_ContainingWindowClientArea.height /
##                               self.ts_Rows) - self.ts_Vgap))))

            w = wx.Max( w, sz.x )
            h = wx.Max( h, sz.y )

        # In case we have a nested sizer with a two step algo , give it
        # a chance to adjust to that (we give it width component)
        didChangeMinSize = False
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item =  node.GetUserData()
            didChangeMinSize |= item.InformFirstDirection(
                wx.HORIZONTAL, w, -1 )

        # And redo iteration in case min size changed
        if(didChangeMinSize):

            w = h = 0
            for i in range(0, self.ts_Children.GetCount()):
                node = self.ts_Children.GetIndex(i)

                item =  node.GetUserData()
                sz = item.GetMinSizeWithBorder()

                w = wx.Max( w, sz.x )
                h = wx.Max( h, sz.y )

        return (wxSize(self.ts_Cols * w + (self.ts_Cols-1) * self.ts_HGap,
                       self.ts_Rows * h + (self.ts_Rows-1) * self.ts_VGap))

    #-----------------------------------------------------------------------

    def CalcRows(self):
        '''
        Returns the number of rows needed for the current total number
        of children (and the fixed number of columns).
        '''

        self.logger.wxCHECK_MSG(
            self.ts_Cols == 0,
            'Cannot calculate number of rows ' + \
            'if number of cols is not specified')

        return (self.GetCount() + self.ts_Cols - 1) / self.ts_Cols

    #-----------------------------------------------------------------------

    def CalcRowsCols(self):
        '''
        Calculates how many rows and columns will be in the sizer based on
        the current number of items and also the rows, cols specified in the
        constructor.
        '''
        nitems = self.ts_Children.GetCount()

        ncols = self.GetEffectiveColsCount()
        nrows = self.GetEffectiveRowsCount()

        # Since Insert() checks for overpopulation, the following
        # should only assert if the grid was shrunk via SetRows() / SetCols()
        self.logger.wxASSERT_MSG(
            (nitems <= (ncols * nrows)),
            'GridSizer.CalcRowsCols logic error')

        return (nitems)

    #-----------------------------------------------------------------------

    def DoInsert(self, index, item):
        '''
        '''
        # if only the number of columns or the number of rows is
        # specified for a sizer, arbitrarily many items can be added
        # to it but if both of them are fixed, then the sizer cannot
        # have more than that many items -- check for this here to
        # ensure that we detect errors as soon as possible
        if ((self.ts_Cols & self.ts_Rows) > 0):

            nitems = len(self.ts_Children)
            if (nitems == self.ts_Cols * self.ts_Rows):

                fmt1 = 'Too many items (%d > %d*%d) ' % (nitems + 1,
                                                         self.ts_Cols,
                                                         self.ts_Rows)
                fmt2 = 'in grid sizer '
                fmt3 = '(maybe you should omit the number of either '
                fmt4 = 'rows or columns?)'
                msg = fmt1 + fmt2 + fmt3 + fmt4
                self.logger.wxFAIL_MSG(msg)

                # additionally, continuing to use the specified number
                # of columns and rows is not a good idea as callers of
                # CalcRowsCols() expect that all sizer items can fit into
                # self.ts_Cols-/self.ts_Rows-sized arrays which is not
                # the case if there are too many items and results in
                # crashes, so let it compute the number of rows automatically
                # by forgetting the (wrong) number of rows specified (this
                # also has a nice side effect of giving only one assert
                # even if there are many more items than allowed in this
                # sizer)
                self.ts_Rows = 0

        return (wxSizer.DoInsert(self, index, item))

    #-----------------------------------------------------------------------

    def GetCols(self):
        '''
        Returns the number of columns in the sizer.
        '''
        return (self.ts_Cols)

    #-----------------------------------------------------------------------

    def GetEffectiveColsCount(self):
        '''
        '''
        if self.ts_Cols > 0:
            return (self.ts_Cols)
        else:
            return (self.CalcCols())

    #-----------------------------------------------------------------------

    def GetEffectiveRowsCount(self):
        '''
        '''
        if self.ts_Rows > 0:
            return (self.ts_Rows)
        else:
            return (self.CalcRows())

    #-----------------------------------------------------------------------
 
    def GetHGap(self):
        '''
        Returns the horizontal gap (in pixels) between cells in the sizer.
        '''
        return (self.ts_HGap)

    #-----------------------------------------------------------------------
 
    def GetRows(self):
        '''
        Returns the number of rows in the sizer.
        '''
        return (self.ts_Rows)

    #-----------------------------------------------------------------------
 
    def GetVGap(self):
        '''
        Returns the vertical gap (in pixels) between the cells in the sizer.
        '''
        return (self.ts_VGap)

    #-----------------------------------------------------------------------

##   def Layout(self):
##        '''
##        Call this to force layout of the children anew, e.g.
##        after having added a child to or removed a child (window, other
##        sizer or space) from the sizer while keeping the current dimension.
##        '''
##        self.logger.debug('GridSizer.Layout: self.ts_Children=%s (%d)' % (
##            str(self.ts_Children), self.ts_Children.GetCount()))

##        # (re)calculates minimums needed for each item and other preparations
##        # for layout
##        self.CalcMin()

##        # Applies the layout and repositions/resizes the items
##        self.RecalcSizes()

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        Using the sizes calculated by CalcMin reposition and resize all the
        items managed by this sizer. You should not need to call this
        directly as it is called by Layout.

        Modeled after RecalcSizes in sizer.cpp file of wxWidgets.
        '''
        nitems = self.CalcRowsCols()
        self.logger.debug(
            'GridSizes.RecalcSizes: nitems=%d; Rows=%d; Cols=%d' % (
            nitems, self.ts_Rows, self.ts_Cols))

        if (nitems == 0):
            return

        # find the space allotted to this sizer

        if True:

            # Use CalcMin Output and Integer Arithmetic
            pt = self.GetPosition()
            sz = self.GetSize()

            w = (sz.width - (
                (self.ts_Cols - 1) * self.ts_HGap)) / self.ts_Cols

            h = (sz.height - (
                (self.ts_Rows - 1) * self.ts_VGap)) / self.ts_Rows

        else:

            # TBD - Use CalcMin Output and Floating Point Arithmetic
            pt = self.GetPosition()
            sz = self.GetSize()

            w = (sz.width - (
                (self.ts_Cols - 1) * self.ts_HGap)) / self.ts_Cols

            h = (sz.height - (
                (self.ts_Rows - 1) * self.ts_VGap)) / self.ts_Rows

##            ptOrig = self.GetPosition()
##            xOrig = ptOrig.x
##            yOrig = ptOrig.y

##            szOrig = self.GetSize()
##            widthOrig = szOrig.width
##            heightOrig = szOrig.height

##            hGapOrig = self.ts_HGap
##            vGapOrig = self.ts_VGap
##            x = int(float(szOrig.x) + (float(wx.pixelWidthPerCharacter) / 2.0))
##            sz = wxSize(szOrig.x +
##            pt = ptOrig

##            w = (sz.width - ((self.ts_Cols - 1) * self.ts_HGap)) / self.ts_Cols

##            h = (sz.height - ((self.ts_Rows - 1) * self.ts_VGap)) / self.ts_Rows

        y = pt.y
        for r in range(self.ts_Rows):

            x = pt.x
            for c in range(self.ts_Cols):

                i = (r * self.ts_Cols) + c
                if (i < nitems):

                    node = self.ts_Children.indexedNodeList[i]

                    self.logger.wxASSERT_MSG(
                        (node is not None),
                        'GridSizer.RecalcSizes Failed to find node')

                    if True:
                        theItem = node.GetUserData()
                        thePoint = wxPoint(x, y)
                        theSize = wxSize(w, h)
                        theItem.SetDimension(thePoint, theSize)
                        theLabel = theItem.ts_Window.ts_Label
                        if DEBUG:
                            print(
                                'r=%d; c=%d; i=%d; pt=%s; sz=%s; label=%s' % (
                                    r, c, i, str(thePoint),
                                    str(theSize), theLabel))
                    self.SetItemBounds(node.GetUserData(), x, y, w, h)

                x = x + w + self.ts_HGap

            y = y + h + self.ts_VGap

    #-----------------------------------------------------------------------
 
    def SetCols(self, cols):
        '''
        Sets the number of columns in the sizer.
        '''
        self.logger.wxASSERT_MSG(
            cols >= 0, 'Number of columns must be non-negative')
        self.ts_Cols = max(0, cols)

    #-----------------------------------------------------------------------
 
    def SetHGap(self, gap):
        '''
        Sets the horizontal gap (in pixels) between cells in the sizer
        '''
        self.logger.wxASSERT_MSG(
            gap >= 0, 'Horizontal pixels gap must be non-negative')
        self.ts_HGap = max(0, gap)

    #-----------------------------------------------------------------------

    def SetItemBounds(self, item, x, y, w, h ):
        '''
        '''
        pt = wxPoint(x, y)
        sz = item.GetMinSizeWithBorder()
        flag = item.GetFlag()

        if ((flag & wx.EXPAND) or \
            (flag & wx.SHAPED)):

            sz = wxSize(w, h)

        else:

            if (flag & wx.ALIGN_CENTER_HORIZONTAL):

                pt.x = x + (w - sz.width) / 2

            elif (flag & wx.ALIGN_RIGHT):

                pt.x = x + (w - sz.width)

            if (flag & wx.ALIGN_CENTER_VERTICAL):

                pt.y = y + (h - sz.height) / 2

            elif (flag & wx.ALIGN_BOTTOM):

                pt.y = y + (h - sz.height)

        msg = 'GridSizer.SetItemBounds: '  + \
              'item (%s); pt (%s); sz (%s)' % (
                  str(item),
                  str(pt),
                  str(sz))
        if DEBUG:
            print(msg)
        self.logger.debug(msg)

##        item.SetDimension(pt, sz)
        item.ts_Window.ts_Rect = wxRect(pt.x, pt.y, sz.width, sz.height)

    #-----------------------------------------------------------------------

    def SetRows(self, rows):
        '''
        Sets the number of rows in the sizer.
        '''
        self.logger.wxASSERT_MSG(
            rows >= 0,
            'Number of rows must be non-negative')
        self.ts_Rows = max(0, rows)

    #-----------------------------------------------------------------------
 
    def SetVGap(self, gap):
        '''
        Sets the vertical gap (in pixels) between cells in the sizer
        '''
        self.logger.wxASSERT_MSG(
            gap >= 0, 'Vertical pixels gap must be non-negative')
        self.ts_VGap = max(0, gap)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Cols = property(GetCols, SetCols)
    HGap = property(GetHGap, SetHGap)
    Rows = property(GetRows, SetRows)
    VGap = property(GetVGap, SetVGap)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
