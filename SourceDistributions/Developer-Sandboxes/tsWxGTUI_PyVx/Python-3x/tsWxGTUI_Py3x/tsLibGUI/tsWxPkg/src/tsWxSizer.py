#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:48:08 AM rsg>"
'''
tsWxSizer.py - Abstract base class used for laying out subwindows
in a window.
'''
#################################################################
#
# File: tsWxSizer.py
#
# Purpose:
#
#    Abstract base class used for laying out subwindows
#    in a window.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSizer import Sizer
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
#    2011/01/26 rsg Resolved definition of wxSizerItemList.
#
#    2011/12/11 rsg Added "GetSubdividedUnitSize".
#
#    2011/12/11 rsg Added "GetProportionedUnitSize".
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxSizer'
__version__   = '1.4.0'
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

import tsExceptions as tse

import tsWxGlobals as wx
from tsWxDisplay import Display as wxDisplay
from tsWxObject import Object
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxSizerItem import SizerItem as wxSizerItem
from tsWxSizerItemList import SizerItemList as wxSizerItemList
from tsWxWindow import Window as wxWindow

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

class Sizer(Object):
    '''
    You cannot use wxSizer directly; instead, you will have to use one of
    the sizer classes derived from it. Currently there are wxBoxSizer,
    wxStaticBoxSizer, wxGridSizer, wxFlexGridSizer, wxWrapSizer and
    wxGridBagSizer.

    The layout algorithm used by sizers in wxWidgets is closely related
    to layout in other GUI toolkits, such as Javas AWT, the GTK toolkit
    or the Qt toolkit. It is based upon the idea of the individual
    subwindows reporting their minimal required size and their ability to
    get stretched if the size of the parent window has changed.

    This will most often mean that the programmer does not set the original
    size of a dialog in the beginning, rather the dialog will be assigned
    a sizer and this sizer will be queried about the recommended size. The
    sizer in turn will query its children, which can be normal windows,
    empty space or other sizers, so that a hierarchy of sizers can be
    constructed. Note that wxSizer does not derive from wxWindow and thus
    does not interfere with tab ordering and requires very little resources
    compared to a real window on screen.

    What makes sizers so well fitted for use in wxWidgets is the fact that
    every control reports its own minimal size and the algorithm can handle
    differences in font sizes or different window (dialog item) sizes on
    different platforms without problems. If e.g. the standard font as well
    as the overall design of Motif widgets requires more space than on
    Windows, the initial dialog size will automatically be bigger on
    Motif than on Windows.

    Sizers may also be used to control the layout of custom drawn items
    on the window. The wxSizer::Add(), wxSizer::Insert(), and
    wxSizer::Prepend() functions return a pointer to the newly added
    wxSizerItem. Just add empty space of the desired size and attributes,
    and then use the wxSizerItem::GetRect() method to determine where
    the drawing operations should take place.

    Please notice that sizers, like child windows, are owned by the
    library and will be deleted by it which implies that they must be
    allocated on the heap. However if you create a sizer and do not add
    it to another sizer or window, the library would not be able to
    delete such an orphan sizer and in this, and only this, case it
    should be deleted explicitly.

    wxPython Note: If you wish to create a sizer class in wxPython you
    should derive the class from wxPySizer in order to get Python-aware
    capabilities for the various virtual methods.
    '''

    def __init__(self):
        '''
        The constructor.

        Note that wxSizer is an abstract base class and may not be
        instantiated.
        '''
        theClass = 'Sizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)
 
        self.ts_Children = wxSizerItemList()
        self.ts_ContainingWindow = None
        self.ts_ContainingWindowClientArea = None
        self.ts_MinSize = None
        self.ts_Position = DEFAULT_POS
        self.ts_Rect = wxRect(0, 0, 0, 0)
        self.ts_Size = DEFAULT_SIZE
        self.ts_Sizer = None

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        The destructor.
        '''
        self.WX_CLEAR_LIST(self.ts_Children)
        del self

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

        elif isinstance(item, Sizer):
 
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

    def AddF(self, *args, **kwargs):
        '''
        AddF(self, item, wx.SizerFlags flags) -> wx.SizerItem

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        try:

            theItem = args[0]

        except IndexError as itemErrorCode:

            theItem = None

            msg = 'Sizer.AddF: itemErrorCode=%s' % str(
                itemErrorCode)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        try:

            theProportion = args[1]

        except IndexError:

            try:

                theProportion = kwargs['proportion']

            except KeyError:

                theProportion = 0

        try:

            theFlag = args[2]

        except IndexError:

            try:

                theFlag = kwargs['flag']

            except KeyError:

                theFlag = 0

        try:

            theBorder = args[3]

        except IndexError:

            try:

                theBorder = kwargs['border']

            except KeyError:

                theBorder = 0

        try:

            theUserData = args[4]

        except IndexError:

            try:

                theUserData = kwargs['userData']

            except KeyError:

                theUserData = None

        self.Add(theItem,
                 proportion=theProportion,
                 flag=theFlag,
                 border=theBorder,
                 userData=theUserData)

    #-----------------------------------------------------------------------

    def AddItem(self, item):
        '''
        Adds a wx.SizerItem to the sizer.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        return (self.Add(item))

    #-----------------------------------------------------------------------

    def AddMany(self, items):
        '''
        AddMany is a convenience method for adding several items to a sizer
        at one time. Simply pass it a list of tuples, where each tuple
        consists of the parameters that you would normally pass to the
        Add method.

        Convenience method not in sizer.h or sizer.cpp file of wxWidgets.
        '''
        for entry in items:

            if isinstance(entry, tuple):

                try:

                    theItem = entry[0]

                except IndexError as itemErrorCode:

                    theItem = None

                    msg = 'Sizer.AddMany: itemErrorCode=%s' % str(
                        itemErrorCode)
                    raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

                try:

                    theProportion = entry[1]

                except IndexError:

                    theProportion = 0

                try:

                    theFlag = entry[2]

                except IndexError:

                    theFlag = 0

                try:

                    theBorder = entry[3]

                except IndexError:

                    theBorder = 0

                try:

                    theUserData = entry[4]

                except IndexError:

                    theUserData = None

                self.Add(theItem,
                         proportion=theProportion,
                         flag=theFlag,
                         border=theBorder,
                         userData=theUserData)

    #-----------------------------------------------------------------------

    def AddSizer(self, *args, **kwargs):
        '''
        Compatibility alias for Add.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        try:

            theItem = args[0]

        except IndexError as itemErrorCode:

            theItem = None

            msg = 'Sizer.AddSizer: itemErrorCode=%s' % str(
                itemErrorCode)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        try:

            theProportion = args[1]

        except IndexError:

            try:

                theProportion = kwargs['proportion']

            except KeyError:

                theProportion = 0

        try:

            theFlag = args[2]

        except IndexError:

            try:

                theFlag = kwargs['flag']

            except KeyError:

                theFlag = 0

        try:

            theBorder = args[3]

        except IndexError:

            try:

                theBorder = kwargs['border']

            except KeyError:

                theBorder = 0

        try:

            theUserData = args[4]

        except IndexError:

            try:

                theUserData = kwargs['userData']

            except KeyError:

                theUserData = None

        self.Add(theItem,
                 proportion=theProportion,
                 flag=theFlag,
                 border=theBorder,
                 userData=theUserData)

    #-----------------------------------------------------------------------

    def AddSpacer(self, size):
        '''
        This base function adds non-stretchable space to both the horizontal
        and vertical orientation of the sizer.

        More readable way of calling:
        wxSizer::Add(size, size, 0).
        '''
        self.AddF(size, size, 0)

    #-----------------------------------------------------------------------

    def AddStretchSpacer(self, prop=1):
        '''
        Adds stretchable space to the sizer.

        More readable way of calling:
        wxSizer::Add(0, 0, prop).
        '''
        self.AddF(0, 0, prop)

    #-----------------------------------------------------------------------

    def AddWindow(self, window, flags):
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

        flags   A wxSizerFlags object that enables you to specify most
        of the above parameters more conveniently.
        '''
        self.Add(window, flag=flags)

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        Calculate the total minimum width and height needed by all items
        in the sizer according to this sizer layout algorithm.

        This method is abstract and has to be overwritten by any derived
        class.

        Here, the sizer will do the actual calculation of its childrens
        minimal sizes.

        Implemented in wxGridBagSizer, and wxBoxSizer.
        '''
        self.logger.debug(
            'Sizer.CalcMin: %s' % str(self.FindSizerClientArea()))

        width = 0
        height = 0
        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            # calculate the total minimum width and height needed
            # by all items in the sizer according to this sizer's
            # layout algorithm.
            item = node.GetUserData()

            minSize = item.MinSize
            width += minSize.width
            height += minSize.height

            self.logger.debug(
                'Sizer.CalcMin: item=%s; minSize=%s; width=%s; height=%s' % (
                str(item), str(minSize), str(width), str(height)))

        size = wxSize(width, height)
        self.logger.debug('Sizer.CalcMin: size=%s' % size)

        return (size)

    #-----------------------------------------------------------------------

    def Clear(self, delete_windows=False):
        '''
        Detaches all children from the sizer.

        If delete_windows is true then child windows will also be deleted.
        '''
        # First clear the ContainingSizer pointers
        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.IsWindow()):

                item.GetWindow().SetContainingSizer(None)

            node = self.ts_Children.GetNext()

        # Destroy the windows if needed
        if (delete_windows):

            self.DeleteWindows()

        # Now empty the list
        self.WX_CLEAR_LIST(self.ts_Children)

    #-----------------------------------------------------------------------

    def ComputeFittingClientSize(self, window):
        '''
        Computes client area size for window so that it matches the sizers
        minimal size.

        Unlike GetMinSize(), this method accounts for other constraints
        imposed on window, namely displays size (returned size will never
        be too large for the display) and maximum window size if previously
        set by wxWindow::SetMaxSize().

        The returned value is suitable for passing to
        wxWindow::SetClientSize() or wxWindow::SetMinClientSize().
        '''
        self.logger.wxCHECK_MSG(
            (not (window is None)),
            wx.DefaultSize,
            'ComputeFittingClientSize window cannot be %s.' % window)

        # take the min size by default and limit it by max size
        size = window.GetMinClientSize() # TBD - Fix for TypeError with (window)

        tlw = window
        if (not (tlw is None)):
 
            # hack for small screen devices where TLWs are always full screen
            if tlw.IsAlwaysMaximized():
 
                return (tlw.GetClientSize())

            # limit the window to the size of the display it is on
            disp = wxDisplay.GetFromWindow(window)
            self.logger.wxASSERT_MSG(
                (disp != wx.NOT_FOUND),
                msg='Unexpected loss of display (%s)' % disp)

            #####
            ## File "test_tsWxStaticBoxSizer.py", line 340, in __init__
            ## theSizer.Fit(theWindow)
            ## File "/cygdrive/d/WR/SoftwareGadgetry-2.x/tsLibraries/tsWxPkg/src/tsWxSizer.py", line 650, in ComputeFittingClientSize
            ## sizeMax = wxDisplay.GetClientArea(self).Size
            ## TypeError: unbound method GetClientArea() must be called with Display instance as first argument (got BoxSizer instance instead)
            #####
            try:
                sizeMax = wxDisplay.GetClientArea(self).Size
            except TypeError:
                sizeMax = wxSize(tlw.ClientRect.width,
                                 tlw.ClientRect.height)

            # space for decorations and toolbars etc.
            sizeMax = tlw.WindowToClientSize(sizeMax)

        else:

            sizeMax = window.GetMaxClientSize(window)

        if (sizeMax.width != wx.DefaultCoord and \
            size.x > sizeMax.width ):

            size.x = sizeMax.width

        if (sizeMax.height != wx.DefaultCoord and \
            size.y > sizeMax.height ):

            size.y = sizeMax.height

        return (size)

    #-----------------------------------------------------------------------

    def ComputeFittingWindowSize(self, window):
        '''
        Like ComputeFittingClientSize(), but converts the result into
        window size.

        The returned value is suitable for passing to wxWindow::SetSize()
        or wxWindow::SetMinSize().
        '''
        self.logger.wxASSERT_MSG(
            (window is not None),
            msg='ComputeFittingWindowSize window cannot be %s.' % window)

        return (window.ClientToWindowSize(
            self.ComputeFittingClientSize(window)))

    #-----------------------------------------------------------------------

    def DeleteWindows(self):
        '''
        Destroy all windows managed by the sizer.

        Modeled after DeleteWindows in sizer.cpp file of wxWidgets.
        '''
        node = self.ts_Children.GetFirst()
        while (node is not None):

            item = node.GetUserData()

            if (isinstance(item, wxWindow)):

                item.DeleteWindows()

            node = self.ts_Children.GetNext()

    #-----------------------------------------------------------------------

    def Detach(self, item):
        '''
        Detaches an item from the sizer without destroying it. This method
        does not cause any layout or resizing to take place, call Layout
        to do so. The item parameter can be either a window, a sizer, or
        the zero-based index of the item to be detached. Returns True if
        the child item was found and detached.

        Modeled after Detach in sizer.cpp file of wxWidgets.
        '''
        if isinstance(item, int):

            index = item
            return (self.DetachIndex(index))

        elif isinstance(item, Sizer):

            sizer = item
            return (self.DetachSizer(sizer))

        else:

            # Window
            window = item
            return (self.DetachWindow(window))

    #-----------------------------------------------------------------------

    def DetachIndex(self, index):
        '''
        Detach a item at position index from the sizer without destroying
        it.

        This method does not cause any layout or resizing to take place,
        call Layout() to update the layout "on screen" after detaching a
        child from the sizer. Returns true if the child item was found
        and detached, false otherwise.
        '''
        self.logger.wxCHECK_MSG(
            ((index >= 0) and \
             (index < self.ts_Children.GetCount())),
            False,
            'DetachIndex index (%s) is out of range.' % index)

        node = self.ts_Children[index]
        self.logger.wxCHECK_MSG(
            (node is not None),
            False,
            'DetachIndex failed to find ' + \
            'child node (%s) for index (%s).' % (node, index))

        item = node.GetUserData()

        if (item.IsSizer()):

            item.DetachSizer()

        del item
        self.ts_Children.Remove(node)

        return (True)

    #-----------------------------------------------------------------------

    def DetachSizer(self, sizer):
        '''
        Detach the child sizer from the sizer without destroying it.

        This method does not cause any layout or resizing to take place,
        call Layout() to update the layout "on screen" after detaching a
        child from the sizer.

        Returns true if the child item was found and detached, false otherwise.
        '''
        self.logger.wxASSERT_MSG(
            (sizer is not None),
            msg='DetachSizer sizer cannot be (%s)' % sizer)

        node = self.ts_Children.GetFirst()
        while (node is not None):

            item = node.GetUserData()

            if (item.GetSizer() == sizer):

                item.DetachSizer()
                del item
                self.ts_Children.Remove(node)
                return (True)

            node = node.GetNext()

        return (False)

    #-----------------------------------------------------------------------

    def DetachWindow(self, window):
        '''
        Detach the child window from the sizer without destroying it.

        This method does not cause any layout or resizing to take place,
        call Layout() to update the layout "on screen" after detaching a
        child from the sizer.

        Returns true if the child item was found and detached, false
        otherwise.
        '''
        self.logger.wxASSERT_MSG(
            (window is not None),
            msg='DetachWindow failed. Window cannot be (%s)' % window)

        node = self.ts_Children.GetFirst()
        while (node is not None):

            item = node.GetUserData()

            if (item.GetWindow() == window):

                del item
                self.ts_Children.Remove(node)

                return (True)

            node = self.ts_Children.GetNext()

        return (False)

    #-----------------------------------------------------------------------

    def DoInsert(self, index, item):
        '''
        Adds a wx.SizerItem to the sizer.

        Modeled after DoInsert in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            ((index < 0) or (index >= self.ts_Children.GetCount())),
            msg='DoInsert index (%s) is out of range.' % index)

        self.ts_Children.InsertBefore(index, item)

        if (not (item.GetWindow() is None)):

            item.GetWindow().SetContainingSizer()

        if (not (item.GetSizer() is None)):

            item.GetSizer().SetContainingWindow(self.ts_ContainingWindow)

        return (item)

    #-----------------------------------------------------------------------

    def DoSetItemMinSize(self, item, width, height):
        '''
        Set the minimum width and height of to the sizer item.

        Modeled after DoSetItemMinSize in sizer.cpp file of wxWidgets.
        '''
        if isinstance(item, wxWindow):

            return (self.DoSetItemMinSizeWindow(item, width, height))

        elif isinstance(item, Sizer):

            return (self.DoSetItemMinSizeSizer(item, width, height))

        elif isinstance(item, int):

            return (self.DoSetItemMinSizeIndex(item, width, height))

        else:

            self.logger.wxFAIL_MSG(
                msg='DoSetItemMinSize invalid item type %s' % type(item))

    #-----------------------------------------------------------------------

    def DoSetItemMinSizeIndex(self, index, width, height):
        '''
        Set the minimum width and height of to the idexed item.

        Modeled after DoSetItemMinSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxCHECK_MSG(
            ((index >= 0) and \
             (index < self.ts_Children.GetCount())),
            False,
            'DoSetItemMinSizeIndex index (%s) is out of range.' % index)

        node = self.ts_Children[index]

        self.logger.wxCHECK_MSG(
            (not (node is None)),
            False,
            msg='DoSetItemMinSizeIndex failed to find child[%d] node' % index)

        item = node.GetUserData()

        if (item.GetSizer()):

            # Sizers contains the minimal size in them, if not calculated ...
            item.GetSizer().DoSetMinSize(width, height)

        else:

            # ... but the minimal size of spacers and windows is
            # stored via the item
            item.SetMinSize(width, height)

        return (True)

    #-----------------------------------------------------------------------

    def DoSetItemMinSizeSizer(self, sizer, width, height):
        '''
        Set the minimum width and height of to the sizer item.

        Modeled after DoSetItemMinSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not (sizer is None)),
            msg='DoSetItemMinSizeSizer sizer cannot be %s' % sizer)

        # Is it our immediate child?
        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetSizer() == sizer):

                item.GetSizer().DoSetMinSize(width, height)

                return (True)

            node = self.ts_Children.GetNext()

        # No?  Search any subsizers we own then

        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetSizer() and \
                item.GetSizer().DoSetItemMinSize(sizer, width, height)):
 
                # A child sizer found the requested windw, exit.
                return (True)

            node = self.ts_Children.GetNext()

        return (False)

    #-----------------------------------------------------------------------

    def DoSetItemMinSizeWindow(self, window, width, height):
        '''
        Set the minimum width and height of to the sizer item.

        Modeled after DoSetItemMinSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not (window is None)),
            msg='DoSetItemMinSizeWindow window cannot be %s' % window)

        # Is it our immediate child?
        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetWindow() == window):
 
                item.SetMinSize(width, height)
                return (True)

            node = self.ts_Children.GetNext()

        # No?  Search any subsizers we own then

        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetSizer() and \
                item.GetSizer().DoSetItemMinSize(window, width, height)):
 
                # A child sizer found the requested windw, exit.
                return (True)

            node = self.ts_Children.GetNext()

        return (False)

    #-----------------------------------------------------------------------

    def DoSetMinSize(self, width, height):
        '''
        Set the minimum width and height of to the sizer.

        Modeled after DoSetMinSize in sizer.cpp file of wxWidgets.
        '''
        self.ts_MinSize.width = width
        self.ts_MinSize.height = height

    #-----------------------------------------------------------------------

    def FindSizerClientArea(self):
        '''
        Return the client area of the window object that contains this
        sizer and all of its descendant children.

        To accomplish this, scan the list of children for the first window
        object (e.g. panel, button, checkbox, radiobutton, textctrl etc.)
        whose parent would be considered the one containing this sizer.
        '''
        for i in range(0, self.ts_Children.GetCount()):

            node = self.ts_Children.GetIndex(i)

            item =  node.GetUserData()

            if (True or item.IsShown()):

                if (item.ts_Kind == wx.Item_Window):

                    try:
                        theWindow = item.ts_Window
                        theParent = theWindow.ts_Parent
                        theClientArea = theParent.ClientArea
                        if DEBUG:
                            fmt1 = 'Sizer.FindSizerClientArea: '
                            fmt2 = 'Found [%d] ' % i
                            fmt3 = 'ClientArea=%s ' % str(theClientArea)
                            fmt4 = 'Window=%s; Rect=%s ' % (
                                str(theWindow),
                                str(theWindow.Rect))
                            fmt5 = 'Parent=%s; Rect=%s ' % (
                                str(theParent),
                                str(theParent.Rect))
                            print(fmt1 + fmt2 + fmt3 + fmt4 + fmt5)
                        return (theClientArea)
 
                    except Exception as errorCode:
                        if DEBUG:
                            print('Sizer.FindSizerClientArea: ' + \
                                  'Skipped [%d]; %s' % (i, str(errorCode)))
                        pass

        theWindow = None
        theParent = None
        theClientArea = None
        if DEBUG:
            fmt1 = 'Sizer.FindSizerClientArea: '
            fmt2 = 'Failed '
            fmt3 = 'ClientArea=%s ' % str(theClientArea)
            fmt4 = 'Window=%s ' % str(theWindow)
            fmt5 = 'Parent=%s ' % str(theParent)
            print(fmt1 + fmt2 + fmt3 + fmt4 + fmt5)
        return (theClientArea)

    #-----------------------------------------------------------------------

    def Fit(self, window):
        '''
        Tell the sizer to resize the window so that its client area matches
        the sizers minimal size (ComputeFittingClientSize() is called to
        determine it).

        This is commonly done in the constructor of the window itself, see
        sample in the description of wxBoxSizer.

        Returns:
        The new window size.
        '''
        self.logger.wxASSERT_MSG(
            (not (window is None)),
            msg='Fit window cannot be %s.' % window)

        # set client size
        window.SetClientSize(self.ComputeFittingClientSize(window))

        # return entire size
        return (window.GetSize())

    #-----------------------------------------------------------------------

    def FitInside(self, window):
        '''
        Tell the sizer to resize the virtual size of the window to match
        the sizers minimal size.

        This will not alter the on screen size of the window, but may
        cause the addition/removal/alteration of scrollbars required to
        view the virtual area in windows which manage it.
        '''
        self.logger.wxASSERT_MSG(
            (window is not None),
            msg='FitInside window cannot be %s.' % window)

        if window.IsTopLevel():
            # Fit window to display screen's client area
            size = self.VirtualFitSize(window)
        else:
            # Fit window to parent's client area
            size = window.GetMinClientSize(window)

        window.SetVirtualSize(size)

    #-----------------------------------------------------------------------

    def GetChildren(self):
        '''
        Returns the list of the items in this sizer.

        The elements of type-safe wxList wxSizerItemList are pointers to
        objects of type wxSizerItem.
        '''
        return (self.ts_Children)

    #-----------------------------------------------------------------------

    def GetContainingWindow(self):
        '''
        Returns the window this sizer is used in or NULL if none.
        '''
        return (self.ts_ContainingWindow)

    #-----------------------------------------------------------------------

    def GetCount(self):
        '''
        Return the number of children for this sizer
        '''
        return (self.ts_Children.GetCount())

    #-----------------------------------------------------------------------

    def GetItem(self, item, Recursive=False):
        '''
        Returns the wx.SizerItem which holds the item given. The item
        parameter can be either a window, a sizer, or the zero-based
        index of the item to be found.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        if isinstance(item, int):

            index = item
            return (self.GetItemIndex(index, Recursive=Recursive))

        elif isinstance(item, Sizer):

            sizer = item
            return (self.GetItemSizer(sizer, Recursive=Recursive))

        elif isinstance(item, wxWindow):

            window = item
            return (self.GetItemWindow(window, Recursive=Recursive))

        else:

            self.logger.wxFAIL_MSG(
                msg='GetItem invalid item type %s' % type(item))

    #-----------------------------------------------------------------------

    def GetItemById(self, id, Recursive=False):
        '''
        Finds item of the sizer which has the given id.

        This id is not the window id but the id of the wxSizerItem itself.
        This is mainly useful for retrieving the sizers created from XRC
        resources. Use parameter recursive to search in subsizers too.
        Returns pointer to item or NULL.
        '''
        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetId() == id):

                return (item)

            elif (Recursive and \
                  item.IsSizer()):

                subitem = item.GetSizer().GetItemById(id, Recursive=True)
                if (not (subitem is None)):
                    return (subitem)

            node = self.ts_Children.GetNext()

        return (None)

    #-----------------------------------------------------------------------

    def GetItemCount(self):
        '''
        Returns the number of items in the sizer.

        If you just need to test whether the sizer is empty or not you can
        also use IsEmpty() function.
        '''
        return (len(self.ts_Children))

    #-----------------------------------------------------------------------

    def GetItemIndex(self, index, Recursive=False):
        '''
        Finds wxSizerItem which is located in the sizer at position index.

        Use parameter recursive to search in subsizers too. Returns pointer
        to item or NULL.
        '''
        self.logger.wxCHECK_MSG(
            (index < self.ts_Children.GetCount()),
            msg='GetItemIndex index (%d) is out of range' % index)

        return (self.ts_Children.GetIndex(index))

    #-----------------------------------------------------------------------

    def GetItemSizer(self, sizer, Recursive=False):
        '''
        Returns the wx.SizerItem which holds the item given. The item
        parameter can be either a window, a sizer, or the zero-based
        index of the item to be found.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not (sizer is None)),
            msg='GetItemSizer sizer cannot be (%s)' % sizer)

        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetSizer() == sizer):

                return (item)

            elif (Recursive and item.IsSizer()):

                subitem = item.GetSizer().GetItem(sizer, Recursive=True)
                if (not (subitem is None)):
                    return (subitem)

            node = self.ts_Children.GetNext()

        return (None)

    #-----------------------------------------------------------------------

    def GetItemWindow(self, window, Recursive=False):
        '''
        Finds wxSizerItem which holds the given window.

        Use parameter recursive to search in subsizers too. Returns
        pointer to item or NULL.
        '''
        self.logger.wxASSERT_MSG(
            (not (window is None)),
            msg='GetItemWindow window cannot be (%s)' % window)

        node = self.ts_Children.GetFirst()
        while (not (node is None)):

            item = node.GetUserData()

            if (item.GetWindow() == window):

                return (item)

            elif (Recursive and item.IsSizer()):

                subitem = item.GetSizer().GetItem(window, Recursive=True)
                if (not (subitem is None)):
                    return (subitem)

            node = self.ts_Children.GetNext()

        return (None)

    #-----------------------------------------------------------------------

    def GetMaxClientSize(self, window):
        '''
        Returns the minimal size of the sizer. This is either the combined
        minimal size of all the children and their borders or the minimal
        size set by SetMinSize, depending on which is bigger.

        Modeled after GetMaxClientSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT(not (window is None))

        return (window.WindowToClientSize(window.GetMaxSize()))

    #-----------------------------------------------------------------------

    def GetMinClientSize(self, window):
        '''
        Returns the minimal size of the sizer. This is either the combined
        minimal size of all the children and their borders or the minimal
        size set by SetMinSize, depending on which is bigger.

        Modeled after GetMinClientSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT(not (window is None))

        return (self.GetMinSize()) # Already returns client size.

    #-----------------------------------------------------------------------

    def GetMinSize(self):
        '''
        Returns the minimal size of the sizer.

        This is either the combined minimal size of all the children and
        their borders or the minimal size set by SetMinSize(), depending
        on which is bigger. Note that the returned value is client size,
        not window size. In particular, if you use the value to set
        toplevel windows minimal or actual size, use
        wxWindow::SetMinClientSize() or wxWindow::SetClientSize(),
        not wxWindow::SetMinSize() or wxWindow::SetSize().
        '''
        ret = self.CalcMin()

        if (ret.width < self.ts_MinSize.width):

            ret.width = self.ts_MinSize.width

        if (ret.height < self.ts_MinSize.height):

            ret.height = self.ts_MinSize.height

        return (ret)

    #-----------------------------------------------------------------------

    def GetMinSizeTuple(self):
        '''
        Returns the minimal size of the sizer.

        This is either the combined minimal size of all the children and
        their borders or the minimal size set by SetMinSize(), depending
        on which is bigger. Note that the returned value is client size,
        not window size. In particular, if you use the value to set
        toplevel windows minimal or actual size, use
        wxWindow::SetMinClientSize() or wxWindow::SetClientSize(),
        not wxWindow::SetMinSize() or wxWindow::SetSize().
        '''
        # TBD - Under Construction.
        return (self.ts_MinSize.width, self.ts_MinSize.height)

    #-----------------------------------------------------------------------

    def GetPosition(self):
        '''
        Returns the current position of the sizer.
        '''
        return (self.ts_Position)

    #-----------------------------------------------------------------------

    def GetPositionTuple(self):
        '''
        Returns the current position of the sizer.
        '''
        return (self.ts_Position.x, self.ts_Position.y)

    #-----------------------------------------------------------------------

    def GetSize(self):
        '''
        Returns the current size of the sizer.
        '''
        return (self.ts_Size)

    #-----------------------------------------------------------------------

    def GetSizeTuple(self):
        '''
        Returns the current size of the sizer.
        '''
        return (self.ts_Size.width, self.ts_Size.height)

    #-----------------------------------------------------------------------

    def GetProportionedUnitSize(self,
                                guiItem,
                                unitProportion=1,
                                totalProportion=1,
                                tiled=True,
                                orientation=wx.HORIZONTAL,
                                pixels=True):
        '''
        Return the size of each unit when a GUI item has been subdivided
        into the specified column or row orientation proportion.

        When pixels is True, the returned size will be in pixel units and
        character units when pixels is False..

        When tiled is True, the unit size is constrained to be in integer
        multiples of the standard fixed-width font character. As a
        consequence, none of the borders of each unit will overlap.

        However, when tiled is False,  the unit size may be fractional
        multiples of the standard fixed-width font character. As a
        consequence, some the units may share an overlapping border.
        '''
        self.logger.wxASSERT_MSG(
            (unitProportion >= 0),
            msg='GetProportionedUnitSize: ' + \
            'Invalid unitProportion=%d' % unitProportion)

        self.logger.wxASSERT_MSG(
            (totalProportion >= 0),
            msg='GetProportionedUnitSize: ' + \
            'Invalid totalProportion=%d' % totalProportion)

        guiItemRect = guiItem.Rect

        if tiled:

            # Non-overlapping Tiled units
            if orientation == wx.HORIZONTAL:

                colChars = (guiItemRect.width * unitProportion) // (
                    totalProportion * wx.pixelWidthPerCharacter)

                rowChars = (guiItemRect.height) // (
                    wx.pixelHeightPerCharacter)

            else:

                colChars = (guiItemRect.width) // (
                    wx.pixelWidthPerCharacter)

                rowChars = (guiItemRect.height * unitProportion) // (
                    totalProportion * wx.pixelHeightPerCharacter)

            if pixels:

                theSize = wxSize(
                    (colChars * wx.pixelWidthPerCharacter),
                    (rowChars * wx.pixelHeightPerCharacter))

            else:

                theSize = wxSize(colChars, rowChars)

        else:

            # Overlapping Tiled units
            if orientation == wx.HORIZONTAL:

                colChars = (guiItemRect.width * unitProportion) // (
                    totalProportion * wx.pixelWidthPerCharacter)

                rowChars = (guiItemRect.height) // (
                    wx.pixelHeightPerCharacter)

            else:

                colChars = (guiItemRect.width) // (
                    wx.pixelWidthPerCharacter)

                rowChars = (guiItemRect.height * unitProportion) // (
                    totalProportion * wx.pixelHeightPerCharacter)

            if pixels:

                theSize = wxSize(
                    (colChars * wx.pixelWidthPerCharacter),
                    (rowChars * wx.pixelHeightPerCharacter))

            else:

                theSize = wxSize(colChars, rowChars)

        return (theSize)

    #-----------------------------------------------------------------------

    def GetSubdividedUnitSize(self,
                              guiItem,
                              colUnits=1,
                              rowUnits=1,
                              tiled=True,
                              pixels=True):
        '''
        Return the size of each unit when a GUI item has been subdivided
        into the specified number of columns and rows.

        When pixels is True, the returned size will be in pixel units and
        character units when pixels is False..

        When tiled is True, the unit size is constrained to be in integer
        multiples of the standard fixed-width font character. As a
        consequence, none of the borders of each unit will overlap.

        However, when tiled is False,  the unit size may be fractional
        multiples of the standard fixed-width font character. As a
        consequence, some the units may share an overlapping border.
        '''
        self.logger.wxASSERT_MSG(
            (colUnits > 0),
            msg='GetSubdividedUnitSize: Invalid colUnits=%d' % colUnits)

        self.logger.wxASSERT_MSG(
            (rowUnits > 0),
            msg='GetSubdividedUnitSize: Invalid rowUnits=%d' % rowUnits)

        guiItemRect = guiItem.Rect

        if tiled:

            # Non-overlapping Tiled units
            colChars = guiItemRect.width // (
                colUnits * wx.pixelWidthPerCharacter)

            rowChars = guiItemRect.height // (
                rowUnits * wx.pixelHeightPerCharacter)

            if pixels:

                theSize = wxSize(
                    (colChars * wx.pixelWidthPerCharacter),
                    (rowChars * wx.pixelHeightPerCharacter))
            else:

                theSize = wxSize(colChars, rowChars)

        else:

            # Overlapping Tiled units
            colPixels = guiItemRect.width // colUnits

            rowPixels = guiItemRect.height // rowUnits

            if pixels:
 
                theSize = wxSize(colPixels, rowPixels)

            else:

                theSize = wxSize(
                    (colPixels // wx.pixelWidthPerCharacter),
                    (rowPixels // wx.pixelHeightPerCharacter))

        return (theSize)

    #-----------------------------------------------------------------------

    def Hide(self, item, Recursive=False):
        '''
        Hides the child sizer.

        To make a sizer item disappear, use Hide() followed by Layout().

        Use parameter recursive to hide elements found in subsizers.
        Returns true if the child item was found, false otherwise.
        '''
        if isinstance(item, int):

            index = item
            return (self.HideIndex(index, Recursive=Recursive))

        elif isinstance(item, Sizer):

            sizer = item
            return (self.HideSizer(sizer, Recursive=Recursive))

        elif isinstance(item, wxWindow):

            window = item
            return (self.HideWindow(window, Recursive=Recursive))

    #-----------------------------------------------------------------------

    def HideIndex(self, index, Recursive=False):
        '''
        Hides the item at position index.

        To make a sizer item disappear, use Hide() followed by Layout().

        Use parameter recursive to hide elements found in subsizers. Returns
        true if the child item was found, false otherwise.
        '''
        self.Show(index, False, Recursive)

    #-----------------------------------------------------------------------

    def HideSizer(self, sizer, Recursive=False):
        '''
        Hides the child sizer.

        To make a sizer item disappear, use Hide() followed by Layout().

        Use parameter recursive to hide elements found in subsizers.
        Returns true if the child item was found, false otherwise.
        '''
        self.Show(sizer, False, Recursive)

    #-----------------------------------------------------------------------

    def HideWindow(self, window, Recursive=False):
        '''
        Hides the child window.

        To make a sizer item disappear, use Hide() followed by Layout().

        Use parameter recursive to hide elements found in subsizers.
        Returns true if the child item was found, false otherwise.
        '''
        self.Show(window, False, Recursive)

    #-----------------------------------------------------------------------

    def Insert(self,
               before,
               item,
               proportion=0,
               flag=0,
               border=0,
               userData=None):
        '''
        Inserts a new item into the list of items managed by this sizer before
        the item at index before. See Add for a description of the parameters.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        child = wxSizerItem()

        if isinstance(item, tuple) or \
           isinstance(item, wxSize):
 
            child.MinSize = item

        elif isinstance(item, wxWindow):
 
            child.Window = item

        else:
 
            child.Sizer = item

        child.Proportion = proportion
        child.Flag = flag
        child.Border = border
        child.UserData = userData

        self.ts_Children.InsertBefore(before, child)

        return (child)

    #-----------------------------------------------------------------------

    def InsertF(self, *args, **kwargs):
        '''
        InsertF(self, int before, item, wx.SizerFlags flags) -> wx.SizerItem.

        Similar to Insert, but uses the wx.SizerFlags convenience class for
        setting the various flags, options and borders.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'InsertF in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InsertItem(self, index, item):
        '''
        Inserts a wx.SizerItem to the sizer at the position given by index.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        self.ts_Children.InsertBefore(index, item)

    #-----------------------------------------------------------------------

    def InsertSizer(self, *args, **kw):
        '''
        Compatibility alias for Insert.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'InsertSizer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InsertSpacer(self, index, size):
        '''
        Inserts stretchable space to the sizer.

        More readable way of calling wxSizer::Insert(0, 0, prop).
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'InsertSpacer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InsertStretchSpacer(self, index, prop):
        '''
        Inserts stretchable space to the sizer.

        More readable way of calling wxSizer::Insert(0, 0, prop).
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'InsertStretchSpacer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InsertWindow(self, *args, **kw):
        '''
        Compatibility alias for Insert.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'InsertWindow in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsEmpty(self):
        '''
        Return true if the sizer has no elements.
        '''
        return (self.GetItemCount() == 0)

    #-----------------------------------------------------------------------

    def IsShown(self, item):
        '''
        Returns true if the item at index is shown.
        '''
        if isinstance(item, int):

            index = item
            return (self.IsShownIndex(index))

        elif isinstance(item, Sizer):

            sizer = item
            return (self.IsShownSizer(sizer))

        elif isinstance(item, wxWindow):

            window = item
            return (self.IsShownWindow(window))

    #-----------------------------------------------------------------------

    def IsShownIndex(self, index):
        '''
        Returns true if the item at index is shown.
        '''
        self.logger.wxCHECK_MSG(
            (index < len(self.ts_Children)),
            False,
            msg='IsShownIndex index (%d) is out of range' % index)

        return (self.ts_Children[index].IsShown())

    #-----------------------------------------------------------------------

    def IsShownSizer(self, sizer):
        '''
        Returns true if the sizer is shown.
        '''
        for node in self.ts_Children:

            item = node.GetData()

            if (item.GetSizer() == sizer):

                return (item.IsShown())

        self.logger.wxFAIL_MSG(
            msg='IsShownSizer failed to find sizer item (%s)' % sizer)

        return (False)

    #-----------------------------------------------------------------------

    def IsShownWindow(self, window):
        '''
        Returns true if the window is shown.
        '''
        for node in self.ts_Children:

            item = node.GetData()

            if (item.GetWindow() == window):

                return (item.IsShown())

        self.logger.wxFAIL_MSG(
            msg='IsShownWindow failed to find sizer item (%s)' % window)

        return (False)

    #-----------------------------------------------------------------------

    def Layout(self):
        '''
        Call this to force layout of the children anew, e.g. after
        having added a child to or removed a child (window, other sizer
        or space) from the sizer while keeping the current dimension.
        '''
        self.logger.debug(
            'Sizer.Layout: self.ts_Children=%s (%d)' % (
            str(self.ts_Children), self.ts_Children.GetCount()))

        # (re)calculates minimums needed for each item and other preparations
        # for layout
        self.CalcMin()

        # Applies the layout and repositions/resizes the items
        self.RecalcSizes()

    #-----------------------------------------------------------------------

    def Prepend(self, item, proportion=0, flag=0, border=0, userData=None):
        '''
        Same as Add(), but prepends the items to the beginning of the list
        of items (windows, subsizers or spaces) owned by this sizer.
        '''
        return (self.ts_Children.InsertBefore(0, item))

    #-----------------------------------------------------------------------

    def PrependF(self, *args, **kwargs):
        '''
        PrependF(self, item, wx.SizerFlags flags) -> wx.SizerItem

        Similar to Prepend but uses the wx.SizerFlags convenience class for
        setting the various flags, options and borders.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        msg = 'NotImplementedError: %s' % 'PrependF in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrependItem(self, item):
        '''
        Prepends a wx.SizerItem to the sizer.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        msg = 'NotImplementedError: %s' % 'PrependItem in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrependSizer(self, *args, **kw):
        '''
        Compatibility alias for Prepend.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        msg = 'NotImplementedError: %s' % 'PrependSizer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrependSpacer(self, size):
        '''
        Prepends non-stretchable space to the sizer.
        '''
        msg = 'NotImplementedError: %s' % 'PrependSpacer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrependStretchSpacer(self, prop=1):
        '''
        Prepends stretchable space to the sizer.
        '''
        msg = 'NotImplementedError: %s' % 'PrependStretchSpacer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrependWindow(self, *args, **kw):
        '''
        Compatibility alias for Prepend.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        msg = 'NotImplementedError: %s' % 'PrependWindow in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        Recalculate (if necessary) the position and size of each item and
        then call item.SetDimension to do the actual positioning and sizing
        of the items within the space alloted to this sizer.

        This method is abstract and has to be overwritten by any derived
        class.
        '''
        msg = 'NotImplementedError: %s' % 'RecalcSizes in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Remove(self, item):
        '''
        Removes an item from the sizer and destroys it. This method does
        not cause any layout or resizing to take place, call Layout to
        update the layout on screen after removing a child from the sizer.
        The item parameter can be either a window, a sizer, or the zero-based
        index of an item to remove. Returns True if the child item was found
        and removed.

        Note:

        For historical reasons calling this method with a wx.Window parameter
        is deprecated, as it will not be able to destroy the window since it
        is owned by its parent. You should use Detach instead.

        Modeled after Remove in sizer.cpp file of wxWidgets.
        '''
        if isinstance(item, int):

            # Removes a child from the sizer and destroys it if it is a
            # sizer or a spacer, but not if it is a window (because
            # windows are owned by their parent window, not the sizer).
            index = item

            self.logger.wxCHECK_MSG(
                ((index >= 0) and \
                 (index < self.GetCount())),
                False,
                'Remove index (%s) is out of range.' % index)

            node = self.ts_Children[index]

            self.logger.wxASSERT_MSG(
                (node is not None),
                msg='Remove failed to find child node for index (%s)' % index)

            image = node.GetUserData()
            del image
            self.ts_Children.Remove(index)

            return (True)

        elif isinstance(item, Sizer):

            # Removes a sizer child from the sizer and destroys it.
            sizer = item

            self.logger.wxASSERT_MSG(
                (sizer is not None),
                msg='Remove cannot find sizer (%s)' % sizer)

            node = self.ts_Children.GetFirst()
            while (node is not None):

                item = node.GetData()

                if (item.GetSizer() == sizer):

                    del item
                    self.ts_Children.Remove(node)
                    return (True)

                node = self.ts_Children.GetNext()

            return (False)

        else:

            # Removes a child window from the sizer, but does not destroy
            # it (because windows are owned by their parent window, not
            # the sizer).
            window = item
 
            return (self.Detach(window))

    #-----------------------------------------------------------------------

    def RemovePos(self, *args, **kw):
        '''
        Compatibility alias for Remove.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'RemovePos in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RemoveSizer(self, *args, **kw):
        '''
        Compatibility alias for Remove.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'RemoveSizer in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RemoveWindow(self, *args, **kw):
        '''
        Compatibility alias for Remove.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # TBD - Under Construction.
        msg = 'NotImplementedError: %s' % 'RemoveWindow in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Replace(self, olditem, item, Recursive=False):
        '''
        Detaches the given olditem from the sizer and replaces it with item
        which can be a window, sizer, or wx.SizerItem.  The detached child
        is destroyed only if it is not a window, (because windows are owned
        by their parent, not the sizer.) The recursive parameter can be used
        to search for the given element recursivly in subsizers.

        This method does not cause any layout or resizing to take place,
        call Layout to do so.

        Returns True if the child item was found and removed.

        Modeled after Replace in sizer.cpp file of wxWidgets.
        '''
        if isinstance(olditem, Sizer):

            return (self.ReplaceSizer(olditem, item, Recursive))

        elif isinstance(olditem, wxWindow):

            return (self.ReplaceWindow(olditem, item, Recursive))

        else: # isinstance(olditem, int)

            return (self.ReplaceIndex(olditem, item, Recursive))

    #-----------------------------------------------------------------------

    def ReplaceIndex(self, old, newitem, Recursive=False):
        '''
        Detaches the given olditem from the sizer and replaces it with item
        which can be a window, sizer, or wx.SizerItem.  The detached child
        is destroyed only if it is not a window, (because windows are owned
        by their parent, not the sizer.) The recursive parameter can be used
        to search for the given element recursivly in subsizers.

        This method does not cause any layout or resizing to take place,
        call Layout to do so.

        Returns True if the child item was found and removed.

        Modeled after Replace in sizer.cpp file of wxWidgets.
        '''
        return (False)
##    {
##        wxCHECK_MSG( old < m_children.GetCount(), false, wxT("Replace index is out of range") );
##        wxASSERT_MSG( newitem, wxT("Replacing with NULL item") );

##        wxSizerItemList::compatibility_iterator node = m_children.Item( old );

##        wxCHECK_MSG( node, false, wxT("Failed to find child node") );

##        wxSizerItem *item = node->GetData();
##        node->SetData(newitem);

##        if (item->IsWindow() && item->GetWindow())
##            item->GetWindow()->SetContainingSizer(NULL);

##        delete item;

##        return true;
##    }

    #-----------------------------------------------------------------------

    def ReplaceSizer(self, oldsz, newsz, Recursive=False):
        '''
        Detaches the given olditem from the sizer and replaces it with item
        which can be a window, sizer, or wx.SizerItem.  The detached child
        is destroyed only if it is not a window, (because windows are owned
        by their parent, not the sizer.) The recursive parameter can be used
        to search for the given element recursivly in subsizers.

        This method does not cause any layout or resizing to take place,
        call Layout to do so.

        Returns True if the child item was found and removed.

        Modeled after Replace in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not(oldsz is None)),
            msg='Cannot replace old sizer (%s)' % oldsz)

        self.logger.wxASSERT_MSG(
            (not(newsz is None)),
            msg='Cannot replace with new sizer (%s)' % newsz)

        for node in self.ts_Children:

            if (not (node is None)):

                item = node.GetData()

                if (item.GetSizer() == oldsz):

                    item.AssignSizer(newsz)
                    return (True)

                elif (Recursive and item.IsSizer()):

                    if (item.GetSizer().Replace(oldsz, newsz, Recursive=True)):
                        return (True)

                node = node.GetNext()

        return (False)

    #-----------------------------------------------------------------------

    def ReplaceWindow(self, oldwin, newwin, Recursive=False):
        '''
        Detaches the given olditem from the sizer and replaces it with item
        which can be a window, sizer, or wx.SizerItem.  The detached child
        is destroyed only if it is not a window, (because windows are owned
        by their parent, not the sizer.) The recursive parameter can be used
        to search for the given element recursivly in subsizers.

        This method does not cause any layout or resizing to take place,
        call Layout to do so.

        Returns True if the child item was found and removed.

        Modeled after Replace in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not (oldwin is None)),
            msg='Unable to replace old window (%s)' % oldwin)

        self.logger.wxASSERT_MSG(
            (not (newwin is None)),
            msg='Unable to replace with new window (%s)' % newwin)

        for node in self.ts_Children:

            if (not (node is None)):

                item = node.GetUserData()

                if (item.GetWindow() == oldwin):

                    item.AssignWindow(newwin)
                    newwin.SetContainingSizer()
                    return (True)

                elif (Recursive and \
                      item.IsSizer()):

                    if (item.GetSizer().Replace(oldwin,
                                                newwin,
                                                Recursive=True)):
                        return (True)

        return (False)

    #-----------------------------------------------------------------------

    def SetContainingWindow(self, window):
        '''
        Set (or unset) the window this sizer is used in.

        Modeled after SetContainingWindow in sizer.cpp file of wxWidgets.
        '''
        if (window == self.ts_ContainingWindow):

            return

        self.ts_ContainingWindow = window

        # set the same window for all nested sizers as well,
        # they also are in the same window
        node = self.ts_Children.GetFirst()
        while not (node is None):

            item = node.GetData()

            sizer = item.GetSizer()
            if (not (sizer is None)):

                sizer.SetContainingWindow(window)

            node = self.ts_Children.GetNext()

    #-----------------------------------------------------------------------

    def SetDimension(self, *args):
        '''
        Call this to force the sizer to take the given dimension and thus force
        the items owned by the sizer to resize themselves according to the
        rules defined by the parameter in the Add, Insert or Prepend methods.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
##        for i in range(len(args)):
##            print('txWxSizer.SetDimension:args[%d]= %s' % (
##                i, str(args[i])))
        if len(args) == 4:

            # len(args) == 4; Invoked via SetDimension(x, y, w, h)
            pos = wxPoint(args[0], args[1])
            size = wxSize(args[2], args[3])

        elif len(args) == 2:

            # len(args) == 2; Invoked via SetDimension(pos, size)
            pos = args[0]
            size = args[1]

        else:

            # len(args) == 0; Invoked via SetDimension()
            pos = DEFAULT_POS # wxPoint(self.ts_Rect.x, self.ts_Rect.y)
            size = DEFAULT_SIZE # wxSize(self.ts_Rect.width, self.ts_Rect.height)

        # Under Construction.
        self.ts_Rect = wxRect(pos.x, pos.y, size.width, size.height)

    #-----------------------------------------------------------------------

    def SetItemMinSize(self, item, size):
        '''
        Sets the minimum size that will be allocated for an item in the sizer.
        The item parameter can be either a window, a sizer, or the zero-based
        index of the item. If a window or sizer is given then it will be
        searched for recursivly in subsizers if neccessary.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        # Under Construction.
        msg = 'NotImplementedError: %s' % 'SetItemMinSize in tsWxSizer'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetMinSize(self, size):
        '''
        Call this to give the sizer a minimal size. Normally, the sizer will
        calculate its minimal size based purely on how much space its children
        need. After calling this method GetMinSize will return either the
        minimal size as requested by its children or the minimal size set
        here, depending on which is bigger.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        self.ts_MinSize = size

    #-----------------------------------------------------------------------

    def SetSizeHints(self, window):
        '''
        This method first calls Fit() and then
        wxTopLevelWindow::SetSizeHints() on the window passed to it.

        Tell the sizer to set (and Fit) the minimal size of the window to match
        the sizers minimal size. This is commonly done in the constructor of
        the window itself if the window is resizable (as are many dialogs
        under Unix and frames on probably all platforms) in order to prevent
        the window from being sized smaller than the minimal size required by
        the sizer.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        clientSize = self.ComputeFittingClientSize(window)

        window.SetMinClientSize(clientSize)
        window.SetClientSize(clientSize)

    #-----------------------------------------------------------------------

    def SetVirtualSizeHints(self, window):
        '''
        Tell the sizer to set the minimal size of the window virtual area to
        match the sizers minimal size. For windows with managed scrollbars
        this will set them appropriately.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT(not (window is None))

        self.FitInside(window)

    #-----------------------------------------------------------------------

    def Show(self, item, show=True, Recursive=False):
        '''
        Shows or hides an item managed by the sizer. To make a sizer item
        disappear or reappear, use Show followed by Layout. The item
        parameter can be either a window, a sizer, or the zero-based index
        of the item. Use the recursive parameter to show or hide an item
        in a subsizer. Returns True if the item was found.

        Modeled after Show in sizer.h file of wxWidgets.
        '''
        if isinstance(item, int):

            index = item
            return (self.ShowIndex(index, Recursive=Recursive))

        elif isinstance(item, Sizer):

            sizer = item
            return (self.ShowSizer(sizer, Recursive=Recursive))

        elif isinstance(item, wxWindow):

            window = item
            return (self.ShowWindow(window, Recursive=Recursive))

        else:

            self.logger.wxFAIL_MSG(
                msg='Show invalid item type %s' % type(item))

    #-----------------------------------------------------------------------

    def ShowIndex(self, index, show=True, Recursive=False):
        '''
        Shows or hides an item managed by the sizer. To make a sizer item
        disappear or reappear, use Show followed by Layout. The item
        parameter can be either a window, a sizer, or the zero-based index
        of the item. Use the recursive parameter to show or hide an item
        in a subsizer. Returns True if the item was found.

        Modeled after Show in sizer.h file of wxWidgets.
        '''
        item = self.ts_Children[index]

        if (not (item is None)):

            item.Show(show)
            return (True)

        return (False)

    #-----------------------------------------------------------------------

    def ShowItems(self, show):
        '''
        Recursively call wxWindow.Show on all sizer items.

        Modeled after ShowItems in sizer.h file of wxWidgets.
        '''
        for node in self.Children:

            node.GetData().Show(show)

    #-----------------------------------------------------------------------

    def ShowSizer(self, sizer, show=True, Recursive=False):
        '''
        Shows or hides an item managed by the sizer. To make a sizer item
        disappear or reappear, use Show followed by Layout. The item
        parameter can be either a window, a sizer, or the zero-based index
        of the item. Use the recursive parameter to show or hide an item
        in a subsizer. Returns True if the item was found.

        Modeled after Show in sizer.h file of wxWidgets.
        '''
        item = self.GetItem(sizer, Recursive=Recursive)

        if (not (item is None)):

            item.Show(show)
            return (True)

        return (False)

    #-----------------------------------------------------------------------

    def ShowWindow(self, window, show=True, Recursive=False):
        '''
        Shows or hides an item managed by the sizer. To make a sizer item
        disappear or reappear, use Show followed by Layout. The item
        parameter can be either a window, a sizer, or the zero-based index
        of the item. Use the recursive parameter to show or hide an item
        in a subsizer. Returns True if the item was found.

        Modeled after Show in sizer.h file of wxWidgets.
        '''
        item = self.GetItem(window, Recursive=Recursive)

        if (not (item is None)):

            item.Show(show)
            return (True)

        return (False)

    #-----------------------------------------------------------------------

    def VirtualFitSize(self, window):
        '''
        Return the size that can contain virtually all of the displayable
        window object.

        Modeled after VirtualFitSize in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (not (window is None)),
            msg='VirtualFitSize window cannot be %s' % window)

        size = self.GetMinClientSize(window)
        sizeMax = self.GetMaxClientSize(window)

        # Limit the size if sizeMax != wxDefaultSize

        if ((size.width > sizeMax.width) and \
            (sizeMax.width != DEFAULT_SIZE.width)):

            size.width = sizeMax.width

        if ((size.height > sizeMax.height) and \
            (sizeMax.height != DEFAULT_SIZE.height)):

            size.height = sizeMax.height

        return (size)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def WX_CLEAR_LIST(self, what):
        '''
        Sequentially remove each item from the specified list.
        '''
        self.logger.wxASSERT_MSG(
            isinstance(what, list),
            msg='WX_CLEAR_LIST input type %s cannot be %s' % (
                list, type(what)))

        for item in what:
            # self.logger.debug('item=%s' % item)
            what.remove(item)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
    # Properties

    Children = property(GetChildren)
    ContainingWindow = property(GetContainingWindow, SetContainingWindow)
    MinSize = property(GetMinSize, SetMinSize)
    Position = property(GetPosition)
    Size = property(GetSize)
    SizerItemList = property(GetChildren)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    def wxSizerItemListTest():
        '''
        '''
        print('\n%s\n' % '***** wxSizerItemListTest *****')
        emptyList = wxSizerItemList()
        print('\temptyList.GetCount=%s' % emptyList.GetCount())
        print('\temptyList.GetFirst=%s' % emptyList.GetFirst())
        print('\temptyList.GetLast=%s' % emptyList.GetLast())

        nonemptyList = wxSizerItemList()
        nonemptyList.Add(100)
        nonemptyList.Add(200)
        nonemptyList.Add(300)
        nonemptyList.Add(400)
        print('\n\tnonemptyList.GetCount=%d' % nonemptyList.GetCount())
        print('\tnonemptyList.GetFirst.GetUserData=%s' % \
              nonemptyList.GetFirst().GetUserData())
        print('\tnonemptyList.GetLast.GetUserData=%s' % \
              nonemptyList.GetLast().GetUserData())
        node = nonemptyList.GetFirst()
        while (not (node is None)):
            i = nonemptyList.FindIndexByNode(node)
##            print('\t\ti=[%d]; userData="%s"; node=%s' % (
##                    i, node.GetUserData(), node))
            print('\t\ti=[%d]; userData="%s"' % (
                    i, node.GetUserData()))
            node = nonemptyList.GetNext()

    print(__header__)

    wxSizerItemListTest()
