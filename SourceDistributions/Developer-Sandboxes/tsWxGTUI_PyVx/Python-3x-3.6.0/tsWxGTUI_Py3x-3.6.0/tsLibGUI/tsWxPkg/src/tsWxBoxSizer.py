#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:26:07 AM rsg>"
'''
tsWxBoxSizer.py - Class to lay out its associated GUI objects
in a simple row or column, depending on the orientation parameter
passed to the constructor.
'''
#################################################################
#
# File: tsWxBoxSizer.py
#
# Purpose:
#
#    Class to lay out its associated GUI objects in a simple row
#    or column, depending on the orientation parameter passed to
#    the constructor.
#
# Usage (example):
#
#    # Import
#
#    from tsWxBoxSizer import BoxSizer
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
#    ***** Reference code for wxWidgets 2.9.2 is under development.
#    ***** It compiles with many syntax and undefined variable errors.
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
#    2011/10/12 rsg RecalcSizes probably does not need to support
#                   the alignment flags in manner of the wxWidgets
#                   module renamed herein as RecalcSizes_Orig.
#
#    2011/10/13 rsg AddSpacer does not work. NoneType has no
#                   width or height.
#
#################################################################

__title__     = 'tsWxBoxSizer'
__version__   = '1.2.0'
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

import tsWxGlobals as wx

from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxSizer import Sizer
from tsWxSizerItem import SizerItem as wxSizerItem

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
 
class BoxSizer(Sizer):
    '''
    The basic idea behind a box sizer is that windows will most often be
    laid out in rather simple basic geometry, typically in a row or a
    column or nested hierarchies of either. A wx.BoxSizer will lay out
    its items in a simple row or column, depending on the orientation
    parameter passed to the constructor.

    It is the unique feature of a box sizer, that it can grow in both
    directions (height and width) but can distribute its growth in the
    main direction (horizontal for a row) unevenly among its children.
    This is determined by the proportion parameter give to items when
    they are added to the sizer. It is interpreted as a weight factor,
    i.e. it can be zero, indicating that the window may not be resized
    at all, or above zero. If several windows have a value above zero,
    the value is interpreted relative to the sum of all weight factors
    of the sizer, so when adding two windows with a value of 1, they
    will both get resized equally and each will receive half of the
    available space after the fixed size items have been sized. If the
    items have unequal proportion settings then they will receive a
    coresondingly unequal allotment of the free space.
    '''
    def __init__(self, orient=wx.HORIZONTAL):
        '''
        Constructor for a wx.BoxSizer. orient may be one of wx.VERTICAL
        or wx.HORIZONTAL for creating either a column sizer or a row sizer.
        '''
        theClass = 'BoxSizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Sizer.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        # either wxHORIZONTAL or wxVERTICAL
        self.ts_Orientation = orient

        # the sum of proportion of all of our elements
        self.ts_TotalProportion = 0

        # minimal size needed for this sizer as calculated by
        # the last call to our CalcMin()
        self.ts_MinSize = DEFAULT_SIZE

        # minimal size needed for this sizer as calculated, by
        # calcMin, for the containing window (panel), the parent
        # of those subpanels managed by this BoxSizer instance.
        self.ts_CalcMinArea = []
        self.ts_CalcMinAreaProportion = []
        self.ts_CalcMinKind = []
        self.ts_CalcMinWindow = []
        self.ts_ClientArea = []
        self.ts_ContainingWindow = None
        self.ts_MinSize = wxSize(0, 0)
        self.ts_SizeMinThis = []
        self.ts_TotalFixedSize = wxSize(0, 0)
        self.ts_TotalProportion = 0

##        self.ts_SizeMinThis = None
##        self.ts_CalcMinArea = None
##        self.ts_CalcMinAreaProportion = None
##        self.ts_CalcMinKind = None
##        self.ts_CalcMinWindow = None
##        self.ts_ClientArea = None
##        self.ts_ContainingWindow = None
        self.ts_RecalcArea = None

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

        elif isinstance(item, BoxSizer):
 
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

    def AddSpacer(self, size):
        '''
        '''
        if self.IsVertical():
            item = wxSize(0, size)
        else:
            item = wxSize(size, 0)

        child = self.Add(item, proportion=0, flag=0, border=0, userData=None)

        # Register the child in the wxSizerItemList
        self.ts_Children.Add(child)

        return (child)

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        Calculate the total minimum width and height needed by all items
        in the sizer according to this sizer layout algorithm.
        '''
        # The minimal size for the sizer should be big enough to allocate
        # its element at least its minimal size but also, and this is the
        # non-trivial part, to respect the children proportion. To satisfy
        # the latter condition we must find the greatest min-size-to-
        # proportion ratio for all elements with non-zero proportion.

        # This sizer instance only manages a single parent's client area.
        # Unlike wxWidgets, a parent's client area depends on size of
        # Top Level Window (Frame or Dialog) that depends on initial size
        # of Display Screen which was manually set by a System Operator.

        sizerClientArea = self.FindSizerClientArea()
        self.logger.debug(
            'BoxSizer.CalcMin: sizerClientArea=%s' % str(sizerClientArea))

        self.ts_CalcMinArea = []
        self.ts_CalcMinAreaProportion = []
        self.ts_CalcMinKind = []
        self.ts_CalcMinWindow = []
        self.ts_ClientArea = []
        self.ts_ContainingWindow = None
        self.ts_MinSize = wxSize(0, 0)
        self.ts_SizeMinThis = []
        self.ts_TotalFixedSize = wxSize(0, 0)
        self.ts_TotalProportion = 0

        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item =  node.GetUserData()
            msg = 'BoxSizer.CalcMin: item[%d]=%s' % (i, str(item))
##            print(msg)
            self.logger.debug(msg)

            if (True or item.IsShown()):

                # sizeMinThis = item.CalcMin()
                # TBD - Not sure if the following is equivalent.

                if (item.ts_Kind == wx.Item_None):

                    msg = 'Kind: %s' % 'Item_None'
                    sizeMinThis = wxSize(0, 0)
                    self.ts_CalcMinWindow += [None]

                elif (item.ts_Kind == wx.Item_Sizer):

                    msg = 'Kind: %s' % 'Item_Sizer'
                    self.ts_Sizer.Layout()
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = item.ts_Sizer.Size

                elif (item.ts_Kind == wx.Item_Spacer):

                    msg = 'Kind: %s' % 'Item_Spacer'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = item.ts_Spacer.Size

                elif (item.ts_Kind == wx.Item_Window):

                    msg = 'Kind: %s' % 'Item_Window'
                    self.ts_CalcMinWindow += [item.ts_Window]
                    parent = item.ts_Window.ts_Parent
                    clientArea = parent.ClientArea

                    if (clientArea == sizerClientArea):

                        theRect = parent.Rect
                        theClientArea = parent.ClientArea
                        if DEBUG:
                            print(
                                'BoxSizer.CalcMin: Rect=%s; ClientArea=%s' % (
                                str(theRect),
                                str(theClientArea)))

                    else:

                        theRect = parent.Rect
                        theClientArea = parent.ClientArea
                        if DEBUG:
                            print(
                                'BoxSizer.CalcMin: Rect=%s; ClientArea=%s' % (
                                str(theRect),
                                str(theClientArea)))
                        self.logger.error(
                            'BoxSizer.CalcMin: Rect=%s; ClientArea=%s' % (
                            str(theRect),
                            str(theClientArea)))

                    msg = '%s; Parent.clientArea=%s' % (msg, str(clientArea))
                    sizeMinThis = wxSize(clientArea.width, clientArea.height)

                    if (self.ts_ContainingWindow is None):

                        self.ts_ContainingWindow = parent
                        self.ts_ClientArea = clientArea

                    elif (self.ts_ContainingWindow == parent):

                        pass

                    else:

                        fmt1 = 'BoxSizer.CalcMin: '
                        fmt2 = 'Rejected Parent=%s' % str(parent)
                        fmt3 = 'Previous Parent=%s' % str(
                            self.ts_ContainingWindow)
                        msgError = fmt1 + fmt2 + fmt3
                        if DEBUG:
                            print(msgError)
                        self.logger.error(msgError)

                elif (item.ts_Kind == wx.Item_Max):

                    msg = 'Kind: %s' % 'Item_Max'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = wxSize(0, 0)

                else:

                    msg = 'Kind: %s' % 'Item_Unknown'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = wxSize(0, 0)

                self.logger.debug(msg)

                propThis = item.GetProportion()

                self.ts_CalcMinArea += [sizeMinThis]
                self.ts_CalcMinAreaProportion += [propThis]
                self.ts_CalcMinKind += [item.ts_Kind]
                self.ts_SizeMinThis += [sizeMinThis]

                if (propThis != 0):

                    # Adjustable size item

                    self.ts_TotalProportion += propThis

                    msg = 'BoxSizer.CalcMin: item[%d]=%s; totalProp= %s' % (
                        i, str(item), str(self.ts_TotalProportion))
                    self.logger.debug(msg)

                else:

                    # Fixed size item

                    self.ts_TotalFixedSize += sizeMinThis

                    msg = 'BoxSizer.CalcMin: item[%d]=%s; totalFixed= %s' % (
                        i, str(item), str(self.ts_TotalFixedSize))
                    self.logger.debug(msg)

        for i in range(0, self.ts_Children.GetCount()):

            if (self.ts_Orientation == wx.HORIZONTAL):

                orientation = 'HORIZONTAL'
                self.ts_CalcMinArea[i].height = self.ts_ClientArea.height

                if (self.ts_CalcMinAreaProportion[i] == 0):

                    self.ts_CalcMinArea[
                        i].width = self.ts_SizeMinThis[i].width

                else:

                    scalableWidth = self.ts_ClientArea.width - \
                                    self.ts_TotalFixedSize.width

                    self.ts_CalcMinArea[i].width = int(0.5 + (
                        scalableWidth * (
                            float(self.ts_CalcMinAreaProportion[i]) /
                            float(self.ts_TotalProportion))))

            else:

                orientation = '  VERTICAL'
                self.ts_CalcMinArea[i].width = self.ts_ClientArea.width

                if (self.ts_CalcMinAreaProportion[i] == 0):

                    self.ts_CalcMinArea[
                        i].height = self.ts_SizeMinThis[i].height

                else:

                    scalableHeight = self.ts_ClientArea.height - \
                                     self.ts_TotalFixedSize.height

                    self.ts_CalcMinArea[i].height = int(0.5 + (
                        scalableHeight * (
                            float(self.ts_CalcMinAreaProportion[i]) /
                            float(self.ts_TotalProportion))))

            fmt1 = '%s CalcMinArea[%d]: width=%3d; height=%3d; ' % (
                orientation,
                i,
                int(self.ts_CalcMinArea[i].width),
                int(self.ts_CalcMinArea[i].height))

            fmt2 = 'totalProportion=%3d' % int(self.ts_TotalProportion)

            self.logger.debug(fmt1 + fmt2)

        theCalcMinSize = self.GetSizeInMajorDir(self.ts_ClientArea)
        self.logger.debug('theCalcMinSize=%d' % theCalcMinSize)
        return (theCalcMinSize)

    #-----------------------------------------------------------------------

    def GetMinOrRemainingSize(self,
                              orient,
                              item,
                              remainingSpace):
        '''
        Helper of RecalcSizes(): checks if there is enough remaining space
        for the min size of the given item and returns its min size or the
        entire remaining space depending on which one is greater.

        This function updates the remaining space parameter to account for
        the size effectively allocated to the item.
        '''
        if (remainingSpace > 0):

            sizeMin = item.GetMinSizeWithBorder()
            if (orient == wx.HORIZONTAL):
                size = sizeMin.width
            else:
                size = sizeMin.height

            if (size >= remainingSpace):

                # truncate the item to fit in the remaining space,
                # this is better than showing it only partially in
                # general, even if both choices are bad -- but there
                # is nothing else we can do
                size = remainingSpace

            remainingSpace -= size

        else:

            # no remaining space, no space at all left, no need to even
            # query the item for its min size as we can't give it to it
            # anyhow
            size = 0

        return (size)

    #-----------------------------------------------------------------------

    def GetOrientation(self):
        '''
        Returns the current orientation of the sizer.
        '''
        return (self.ts_Orientation)

    #-----------------------------------------------------------------------

    def GetSizeInMajorDir(self, sz):
        '''
        Helper for our code: this returns the component of the given
        wxSize in the direction of the sizer and in the other direction,
        respectively
        '''
        if self.ts_Orientation == wx.HORIZONTAL:
            return (sz.width)
        else:
            return (sz.height)

    #-----------------------------------------------------------------------

    def GetSizeInMinorDir(self, sz):
        '''
        Helper for our code: this returns the component of the given
        wxSize in the direction of the sizer and in the other direction,
        respectively
        '''
        if self.ts_Orientation == wx.HORIZONTAL:
            return (sz.height)
        else:
            return (sz.width)

    #-----------------------------------------------------------------------

    def IsVertical(self):
        '''
        '''
        # either wxHORIZONTAL or wxVERTICAL
        if self.ts_Orientation == wx.VERTICAL:
            return (True)

        else:
            return (False)

    #-----------------------------------------------------------------------

##    def Layout(self):
##        '''
##        Call this to force layout of the children anew, e.g.
##        after having added a child to or removed a child (window, other
##        sizer or space) from the sizer while keeping the current dimension.
##        '''
##        self.logger.debug('BoxSizer.Layout: self.ts_Children=%s (%d)' % (
##            str(self.ts_Children), self.ts_Children.GetCount()))

##        # (re)calculates minimums needed for each item and other preparations
##        # for layout
##        self.CalcMin()

##        # Applies the layout and repositions/resizes the items
##        self.RecalcSizes()

    #-----------------------------------------------------------------------

    def PosInMajorDir(self, pt):
        '''
        Helper for our code: this returns the component of the given
        wxPoint in the direction of the sizer and in the other direction,
        respectively
        '''
        if self.ts_Orientation == wx.HORIZONTAL:
            return (pt.x)
        else:
            return (pt.y)

    #-----------------------------------------------------------------------

    def PosInMinorDir(self, pt):
        '''
        Helper for our code: this returns the component of the given
        wxPoint in the direction of the sizer and in the other direction,
        respectively
        '''
        if self.ts_Orientation == wx.HORIZONTAL:
            return (pt.y)
        else:
            return (pt.x)

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        Recalculate (if necessary) the position and size of each item and
        then call item.SetDimension to do the actual positioning and sizing
        of the items within the space alloted to this sizer.
        '''
        self.ts_RecalcArea = []

        for i in range(0, self.ts_Children.GetCount()):

            if (self.ts_Orientation == wx.HORIZONTAL):

                # Horizontal Layout
                orientation = 'HORIZONTAL'
                if (i == 0):

                    self.ts_RecalcArea += [wxRect(
                        self.ts_ClientArea.x,
                        self.ts_ClientArea.y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

                else:

                    self.ts_RecalcArea += [wxRect(
                        (self.ts_RecalcArea[i - 1].x + \
                         self.ts_RecalcArea[i - 1].width),
                        self.ts_RecalcArea[i - 1].y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

            else:

                # Vertical Layout
                orientation = '  VERTICAL'

                if (i == 0):

                    self.ts_RecalcArea += [wxRect(
                        self.ts_ClientArea.x,
                        self.ts_ClientArea.y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

                else:

                    self.ts_RecalcArea += [wxRect(
                        self.ts_RecalcArea[i - 1].x,
                        (self.ts_RecalcArea[i - 1].y + \
                         self.ts_RecalcArea[i - 1].height),
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

            if DEBUG:

                msg = '%s RecalcSizes[%d]: Rect=%s; ' % (
                    orientation,
                    i,
                    self.ts_RecalcArea[i])
                print(msg)

            self.ts_CalcMinWindow[i].ts_Rect = self.ts_RecalcArea[i]

    #-----------------------------------------------------------------------

    def RecalcSizes_Orig(self):
        '''
        Recalculate (if necessary) the position and size of each item and
        then call item.SetDimension to do the actual positioning and sizing
        of the items within the space alloted to this sizer.
        '''
        if True or (self.ts_Children.GetCount() == 0):
            return

        totalMinorSize = self.GetSizeInMinorDir(self.ts_Size)
        totalMajorSize = self.GetSizeInMajorDir(self.ts_Size)

        # the amount of free space which we should redistribute among the
        # stretchable items (i.e. those with non zero proportion)
        delta = totalMajorSize - self.GetSizeInMajorDir(self.ts_MinSize)

        # declare loop variables used below:
        # i   # iterator in self.ts_Children list
        # n = 0 # item index in majorSizes array

        # First, inform item about the available size in minor direction
        # as this can change their size in the major direction. Also
        # compute the number of visible items and sum of their min sizes
        # in major direction.

        minMajorSize = 0
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item = node.GetUserData()

            if (True or item.IsShown()):

##                # sizeMinThis = item.CalcMin()
##                # TBD - Not sure if the following is equivalent.
##                if (item.ts_Kind == wx.Item_None):

##                    msg = 'Kind: %s' % 'Item_None'
##                    sizeMinThis = wxSize(0, 0)

##                elif (item.ts_Kind == wx.Item_Window):

##                    msg = 'Kind: %s' % 'Item_Window'
##                    parent = item.ts_Window.ts_Parent
##                    clientArea = parent.ClientArea
##                    msg = '%s; Parent.clientArea=%s' % (msg, str(clientArea))
##                    sizeMinThis = wxSize(clientArea.width, clientArea.height)
##                    # Take immediate exit. This sizer instance
##                    # only manages a single parent's client area.
##                    # Unlike wxWidgets, a parent's client area
##                    # depends on size of Top Level Window (Frame
##                    # or Dialog) that depends on initial size of
##                    # Display Screen which was manuall set by a
##                    # System Operator.
##                    return (sizeMinThis)

##                elif (item.ts_Kind == wx.Item_Sizer):

##                    msg = 'Kind: %s' % 'Item_Sizer'
##                    sizeMinThis = item.ts_Sizer.Size

##                elif (item.ts_Kind == wx.Item_Spacer):

##                    msg = 'Kind: %s' % 'Item_Spacer'
##                    sizeMinThis = item.ts_Spacer.Size

##                elif (item.ts_Kind == wx.Item_Max):

##                    msg = 'Kind: %s' % 'Item_Max'
##                    sizeMinThis = wxSize(0, 0)

##                else:

##                    msg = 'Kind: %s' % 'Item_Unknown'
##                    sizeMinThis = wxSize(0, 0)

                szMinPrev = item.GetMinSizeWithBorder()
                item.InformFirstDirection(self.ts_Orientation^wx.BOTH,
                                          totalMinorSize,
                                          delta)
                szMin = item.GetMinSizeWithBorder()
                deltaChange = self.GetSizeInMajorDir(szMin - szMinPrev)
                if (deltaChange != 0):

                    # Since we passed available space along to the item, it
                    # should not take too much, so delta should not become
                    # negative.
                    delta -= deltaChange

                minMajorSize += self.GetSizeInMajorDir(
                    item.GetMinSizeWithBorder())

        # update our min size and delta which may have changed
        # self.SizeInMajorDir(self.ts_MinSize) = minMajorSize
        self.ts_MinSize = minMajorSize
        delta = totalMajorSize - minMajorSize

        # space and sum of proportions for the remaining items, both
        # may change below
        remaining = totalMajorSize
        totalProportion = self.ts_TotalProportion

        # size of the (visible) items in major direction, -1 means
        # "not fixed yet"
        majorSizes = [wx.DefaultCoord] * self.ts_Children.GetCount()

        # Check for the degenerated case when we don't have enough space
        # for even the min sizes of all the items: in this case we really
        # can't do much more than to to allocate the min size to as many
        # of fixed size items as possible (on the assumption that variable
        # size items such as text zones or list boxes may use scrollbars
        # to show their content even if their size is less than min size
        # but that fixed size items such as buttons will suffer even more
        # if we don't give them their min size)
        if (totalMajorSize < minMajorSize):

            # Second degenerated case pass: allocate min size to all fixed
            # size items.
            n = -1
            for i in range(0, self.ts_Children.GetCount()):
                node = self.ts_Children.GetIndex(i)

                n += 1

                item = node.GetUserData()

                if (True or item.IsShown()):

                    # deal with fixed size items only during this pass
                    if (item.GetProportion() == 0):

                        majorSizes[n] = self.GetMinOrRemainingSize(
                            self.ts_Orientation, item, remaining)

            # Third degenerated case pass: allocate min size to all the
            # remaining, i.e. non-fixed size, items.
            n = -1
            for i in range(0, self.ts_Children.GetCount()):
                node = self.ts_Children.GetIndex(i)

                n += 1

                item = node.GetUserData()

                if (True or item.IsShown()):

                    # we've already dealt with fixed size items above
                    if ((item.GetProportion() != 0)):

                        majorSizes[n] = self.GetMinOrRemainingSize(
                            self.ts_Orientation, item, remaining)

        else:

            # we do have enough space to give at least min sizes to all items

            # Second and maybe more passes in the non-degenerated case: deal
            # with fixed size items and items whose min size is greater than
            # what we would allocate to them taking their proportion into
            # account. For both of them, we will just use their min size, but
            # for the latter we also need to reexamine all the items as the
            # items which fitted before we adjusted their size upwards might
            # not fit any more. This does make for a quadratic algorithm but
            # it's not obvious how to avoid it and hopefully it's not a huge
            # problem in practice as the sizers don't have many items usually
            # (and, of course, the algorithm still reduces into a linear one
            # if there is enough space for all the min sizes).
            nonFixedSpaceChanged = False
            i = -1
            n = -1
            for j in range(0, self.ts_Children.GetCount()):
                node = self.ts_Children.GetIndex(j)

                i += 1
                n += 1

                item = node.GetUserData()

                if (nonFixedSpaceChanged):

                    i = 0
                    n = 0
                    nonFixedSpaceChanged = False

                # check for the end of the loop only after the check above
                # as otherwise we wouldn't do another pass if the last child
                # resulted in non fixed space reduction
                if (i == self.GetCount() - 1):
                    break

                itemInner = self.ts_Children[i].GetUserData()

                if (True or itemInner.IsShown()):

                    # don't check the item which we had already dealt with during a
                    # previous pass (this is more than an optimization, the code
                    # wouldn't work correctly if we kept adjusting for the same item
                    # over and over again)
                    if (majorSizes[n] == wx.DefaultCoord):

                        minMajor = self.GetSizeInMajorDir(
                            itemInner.GetMinSizeWithBorder())

                        # it doesn't make sense for min size to be negative but
                        # right now it's possible to create e.g. a spacer with
                        # (-1, 10) as size and people do it in their code
                        # apparently (see #11842) so ensure that we don't use
                        # this -1 as real min size as it conflicts with the
                        # meaning we use for it here and negative min sizes
                        # just don't make sense anyhow (which is why it might
                        # be a better idea to deal with them at wxSizerItem
                        # level in the future but for now this is the minimal
                        # fix for the bug)
                        if (minMajor < 0 ):
                            minMajor = 0

                        propItem = itemInner.GetProportion()
                        if (propItem != 0):

                            # is the desired size of this item big enough?
                            if (((remaining * propItem) / totalProportion) >= \
                                minMajor):

                                # yes, it is, we'll determine the real size of
                                # this item later, for now just leave it as
                                # wxDefaultCoord
                                pass

                            # the proportion of this item won't count, it has
                            # effectively become fixed
                            totalProportion -= propItem

                        # we can already allocate space for this item
                        majorSizes[n] = minMajor

                        # change the amount of the space remaining to the other items,
                        # as this can result in not being able to satisfy their
                        # proportions any more we will need to redo another loop
                        # iteration
                        remaining -= minMajor

                        nonFixedSpaceChanged = True

            # Last by one pass: distribute the remaining space among the
            # non-fixed items whose size weren't fixed yet according to their
            # proportions.
            i = -1
            n = -1
            for j in range(0, self.ts_Children.GetCount()):
                node = self.ts_Children.GetIndex(j)

                i += 1
                n += 1

                itemInner = self.ts_Children.GetIndex(i).GetUserData()

                if (True or itemInner.IsShown()):

                    if (majorSizes[n] == wx.DefaultCoord):

                        propItem = itemInner.GetProportion()
                        majorSizes[n] = (
                            remaining * propItem) / totalProportion

                        remaining -= majorSizes[n]
                        totalProportion -= propItem

        # the position at which we put the next child
        pt = self.ts_Position


        # Final pass: finally do position the items correctly using their
        # sizes as determined above.
        i = -1
        n = -1
        for j in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(j)

            i += 1
            n += 1

            itemInner = self.ts_Children.GetIndex(i).GetUserData()

            if (True or itemInner.IsShown()):

                majorSize = majorSizes[n]

                sizeThis = itemInner.GetMinSizeWithBorder()

                # apply the alignment in the minor direction
                posChild = pt

                minorSize = self.GetSizeInMinorDir(sizeThis)
                flag = itemInner.GetFlag()
                if ((flag & (wx.EXPAND | wx.SHAPED)) or \
                    (minorSize > totalMinorSize)):

                    # occupy all the available space if wxEXPAND was given and
                    # also if the item is too big to fit -- in this case we
                    # truncate it below its minimal size which is bad but better
                    # than not showing parts of the window at all
                    minorSize = totalMinorSize

                elif (flag & self.tsChoose(self.IsVertical(),
                                           wx.ALIGN_RIGHT,
                                           wx.ALIGN_BOTTOM)):


                    self.logger.wxASSERT_MSG(
                        False,
                        'Invalid code for RecalcSizes in sizer.cpp')
    ##                PosInMinorDir(posChild) += totalMinorSize - minorSize

                # NB: wxCENTRE is used here only for backwards compatibility,
                #     wxALIGN_CENTRE should be used in new code
                elif (flag & self.tsChoose((wx.CENTER | (self.IsVertical())),
                                            wx.ALIGN_CENTER_HORIZONTAL,
                                            wx.ALIGN_CENTER_VERTICAL)):

                    self.logger.wxASSERT_MSG(
                        False,
                        'Invalid code for RecalcSizes in sizer.cpp')

    ##                PosInMinorDir(posChild) += (totalMinorSize - minorSize) / 2

                # apply RTL adjustment for horizontal sizers:
                if ((not self.IsVertical()) and \
                    (self.ts_ContainingWindow is not None)):

                    posChild.x = \
                    self.ts_ContainingWindow.AdjustForLayoutDirection(
                        posChild.x,
                        majorSize,
                        self.ts_Size.x
                        )

                # finally set size of this child and advance to the next one
                item.SetDimension(posChild,
                                  self.SizeFromMajorMinor(majorSize,
                                                          minorSize))


##                self.logger.wxASSERT_MSG(
##                    False,
##                    'Invalid code for RecalcSizes in sizer.cpp')
    ##            PosInMajorDir(pt) += majorSize

    #-----------------------------------------------------------------------

    def SetOrientation(self, orient):
        '''
        Resets the orientation of the sizer.
        '''
        self.ts_Orientation = orient

    #-----------------------------------------------------------------------

    # another helper: creates wxSize from major and minor components
    def SizeFromMajorMinor(self, major, minor):
        '''
        '''
        if self.ts_Orientation == wx.HORIZONTAL:

            return (wxSize(major, minor))

        else: # wxVERTICAL

            return (wxSize(minor, major))

    #-----------------------------------------------------------------------

    def SizeInMajorDir(self, sz):
        '''
        Helper for our code: this returns the component of the given
        wxSize in the direction of the sizer and in the other direction,
        respectively
        '''
        if (self.ts_Orientation == wx.HORIZONTAL):
            return (sz.width)
        else:
            return (sz.height)

    #-----------------------------------------------------------------------

    def SizeInMinorDir(self, sz):
        '''
        Helper for our code: this returns the component of the given
        wxSize in the direction of the sizer and in the other direction,
        respectively
        '''
        if (self.ts_Orientation == wx.HORIZONTAL):
            return (sz.height)
        else:
            return (sz.width)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsChoose(self, condition, choiceIfTrue, choiceIfFalse):
        '''
        '''
        if condition:

            return (choiceIfTrue)

        else:

            return (choiceIfFalse)
 
    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Orientation = property(GetOrientation, SetOrientation)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
