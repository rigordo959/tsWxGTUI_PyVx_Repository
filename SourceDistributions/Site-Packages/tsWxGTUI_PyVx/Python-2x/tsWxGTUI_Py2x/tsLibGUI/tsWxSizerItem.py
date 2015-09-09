#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:18:29 AM rsg>"
'''
tsWxSizerItem.py - Class used to track the position, size and other
attributes of each item managed by a wx.Sizer.
'''
#################################################################
#
# File: tsWxSizerItem.py
#
# Purpose:
#
#    Class used to track the position, size and other attributes
#    of each item managed by a wx.Sizer.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSizerItem import SizerItem
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

__title__     = 'tsWxSizerItem'
__version__   = '1.3.0'
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

from tsWxGTUI_Py2x.tsLibGUI.tsWxObject import Object
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxSizerFlags import SizerFlags as wxSizerFlags
from tsWxGTUI_Py2x.tsLibGUI.tsWxSizerSpacer import SizerSpacer as wxSizerSpacer
from tsWxGTUI_Py2x.tsLibGUI.tsWxWindow import Window as wxWindow

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class SizerItem(Object):
    '''
    The wx.SizerItem class is used to track the position, size and other
    attributes of each item managed by a wx.Sizer. It is not usually
    necessary to use this class because the sizer elements can also be
    identified by their positions or window or sizer references but
    sometimes it may be more convenient to use wx.SizerItem directly.
    Also, custom classes derived from wx.PySizer will probably need to
    use the collection of wx.SizerItems held by wx.Sizer when calculating
    layout.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor for Sizer, Spacer and Window variants of SizerItem.

        Design for wxPython 2.8.12 supported no arguments and no key word
        arguments. The application first had to instantiate the SizerItem
        Class and then use various Set methods to configure the kind of
        SizerItem.

        Design for wxWidgets 2.9.2.2 supported optional arguments and key
        word arguments. The application could instantiate the SizerItem
        Class in the manner of wxPython 2.8.12 or optionally instantiate
        the Sizer, Spacer or Window variant via the appropriate args and
        kwargs.

        Since there is no wxPython 2.9.2.2, the following implementation
        attempts to cover all wxWidgets 2.9.2.2 instantiation forms.
        '''
        theClass = 'SizerItem'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        # Begin setup to avoid triggering pylint errors and warnings.
        # Set Default Values

        # ***** Begin Default Attributes
        self.ts_Border = 0
        self.ts_Flag = 0
        self.ts_ID = self.ts_LastSizerItemId = wx.ID_NONE
        self.ts_Kind = wx.Item_None
        self.ts_MinSize = wxSize(0, 0)
        self.ts_MinSizeWithBorder = wxSize(0, 0)
        self.ts_Proportion = 0
        self.ts_Ratio = 0.0
        self.ts_Rect = wxRect(0, 0, 0, 0)
        self.ts_Show = False
        self.ts_Size = wxSize(0, 0)
        self.ts_Sizer = None
        self.ts_Spacer = None
        self.ts_UserData = None
        self.ts_Window = None
        # ***** End Default Attributes

        # End setup to avoid triggering pylint errors and warnings.

        if (len(args) == 0) and \
           (len(kwargs) == 0):

            # Instatiate SizerItem Class without using args or kwargs
            # associated with Sizer, Spacer or Window variants.
            self.__init_No_Args_No_KwArgs__()

        elif (len(args) > 0) and \
             (isinstance(args[0], wxWindow)):

            # Instatiate SizerItem Class using args or kwargs
            # associated with Window variant.

            self.__init_Item_Window__(args, kwargs)

        elif (len(args) > 0) and \
             (isinstance(args[0], wxSizerSpacer)):

            # Instatiate SizerItem Class using args or kwargs
            # associated with Spacer variants.

            self.__init_Item_Spacer__(args, kwargs)

        else:

            # Instatiate SizerItem Class using args or kwargs
            # associated with Sizer variants.

            self.__init_Item_Sizer__(args, kwargs)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __init_No_Args_No_KwArgs__(self):
        '''
        '''
        # Instatiate SizerItem Class without using args or kwargs
        # associated with Sizer, Spacer or Window variants.

        self.ts_Proportion = 0
        self.ts_Border = 0
        self.ts_Flag = 0
        self.ts_ID = wx.ID_NONE

    #-----------------------------------------------------------------------

    def __init_Item_Sizer__(self, *args, **kwargs):
        '''
        '''
        # Instatiate SizerItem Class using args or kwargs
        # associated with Sizer variants.

        # Apply arguments, key word arguments or defaults
        try:
            sizer = args[0]
        except IndexError:
            try:
                sizer = kwargs['Sizer']
            except KeyError:
                sizer = None

        try:
            proportion = args[1]
        except IndexError:
            try:
                proportion = kwargs['Proportion']
            except KeyError:
                proportion = 0

        try:
            flag = args[2]
        except IndexError:
            try:
                flag = kwargs['Flag']
            except KeyError:
                flag = 0

        try:
            border = args[3]
        except IndexError:
            try:
                border = kwargs['Border']
            except KeyError:
                border = 0

        try:
            userData = args[4]
        except IndexError:
            try:
                userData = kwargs['UserData']
            except KeyError:
                userData = None

        self.ts_Kind = wx.Item_None
        self.ts_Sizer = None
        self.ts_Proportion = proportion
        self.ts_Border = border
        self.ts_Flag = flag
        self.ts_Ratio = 0.0
        self.ts_ID = wx.ID_NONE
        self.ts_UserData = userData

        wxSizerFlags.ASSERT_VALID_SIZER_FLAGS( self.ts_Flag )

        self.DoSetSizer(sizer)

        # self.ts_MinSize is set later

    #-----------------------------------------------------------------------

    def __init_Item_Spacer__(self, *args, **kwargs):
        '''
        '''
        # Instatiate SizerItem Class using args or kwargs
        # associated with Spacer variants.

##            wxSizerItem::wxSizerItem(int width,
##                                     int height,
##                                     int proportion,
##                                     int flag,
##                                     int border,
##                                     wxObject* userData)
##                       : m_kind(Item_None),
##                         m_sizer(NULL),
##                         m_minSize(width, height), // minimal size is the initial size
##                         m_proportion(proportion),
##                         m_border(border),
##                         m_flag(flag),
##                         m_id(wxID_NONE),
##                         m_userData(userData)
##            {
##                ASSERT_VALID_SIZER_FLAGS( m_flag );

##                DoSetSpacer(wxSize(width, height));
##            }

        # Apply arguments, key word arguments or defaults
        try:
            width = args[0]
        except IndexError:
            try:
                width = kwargs['Width']
            except KeyError:
                width = 0

        try:
            height = args[1]
        except IndexError:
            try:
                height = kwargs['Height']
            except KeyError:
                height = 0

        try:
            proportion = args[2]
        except IndexError:
            try:
                proportion = kwargs['Proportion']
            except KeyError:
                proportion = 0

        try:
            flag = args[3]
        except IndexError:
            try:
                flag = kwargs['Flag']
            except KeyError:
                flag = 0

        try:
            border = args[4]
        except IndexError:
            try:
                border = kwargs['Border']
            except KeyError:
                border = 0

        try:
            userData = args[5]
        except IndexError:
            try:
                userData = kwargs['UserData']
            except KeyError:
                userData = None

        self.ts_Kind = wx.Item_None
        self.ts_Sizer = None
        self.ts_Proportion = proportion
        self.ts_Border = border
        self.ts_Flag = flag
        self.ts_ID = wx.ID_NONE
        self.ts_UserData = userData

        # minimal size is the initial size
        self.ts_MinSize = wxSize(width, height)

        wxSizerFlags.ASSERT_VALID_SIZER_FLAGS( self.ts_Flag )

        self.DoSetSpacer(wxSize(width, height))

        # self.ts_MinSize is set later

    #-----------------------------------------------------------------------

    def __init_Item_Window__(self, *args, **kwargs):
        '''
        '''
        # Instatiate SizerItem Class using args or kwargs
        # associated with Window variant.

        # Apply arguments, key word arguments or defaults
        try:
            window = args[0]
        except IndexError:
            try:
                window = kwargs['Window']
            except KeyError:
                window = None

        try:
            proportion = args[1]
        except IndexError:
            try:
                proportion = kwargs['Proportion']
            except KeyError:
                proportion = 0

        try:
            flag = args[2]
        except IndexError:
            try:
                flag = kwargs['Flag']
            except KeyError:
                flag = 0

        try:
            border = args[3]
        except IndexError:
            try:
                border = kwargs['Border']
            except KeyError:
                border = 0

        try:
            userData = args[4]
        except IndexError:
            try:
                userData = kwargs['UserData']
            except KeyError:
                userData = None

        self.ts_Kind = wx.Item_None
        self.ts_Proportion = proportion
        self.ts_Border = border
        self.ts_Flag = flag
        self.ts_ID = wx.ID_NONE
        self.ts_UserData = userData

        wxSizerFlags.ASSERT_VALID_SIZER_FLAGS( self.ts_Flag )

        self.DoSetWindow(window)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''

        Modeled after ~wxSizerItem in sizer.cpp file of wxWidgets.
        '''
        del self.ts_UserData
        self.Free()

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        Calculates the minimum desired size for the item, including any space
        needed by borders.

        Modeled after CalcMin in sizer.cpp file of wxWidgets.
        '''
        if self.IsSizer():

            self.ts_MinSize = self.ts_Sizer.GetMinSize()

            # if we have to preserve aspect ratio _AND_ this is
            # the first-time calculation, consider ret to be initial size
            if (self.ts_Flag & wx.SHAPED) and \
               self.IsNullDouble(self.ts_Ratio):
 
                self.SetRatio(self.ts_MinSize)

        elif self.IsWindow():

            # Since the size of the window may change during runtime, we
            # should use the current minimal/best size.
            self.ts_MinSize = self.ts_Window.GetEffectiveMinSize()

        return (self.GetMinSizeWithBorder())

    #-----------------------------------------------------------------------
 
    def DeleteWindows(self):
        '''
        Destroy the window or the windows in a subsizer, depending on the type
        of item.

        Modeled after DeleteWindows in sizer.cpp file of wxWidgets.
        '''
        if self.ts_Kind == wx.Item_None or \
           self.ts_Kind == wx.Item_Spacer:
 
            pass

        elif self.ts_Kind == wx.Item_Window:
 
            # We are deleting the window from this sizer - normally
            # the window destroys the sizer associated with it,
            # which might destroy this, which we don't want
            self.ts_Window.SetContainingSizer(None)
            self.ts_Window.Destroy()
            # Putting this after the switch will result in a spacer
            # not being deleted properly on destruction
            self.ts_Kind = wx.Item_None

        elif self.ts_Kind == wx.Item_Sizer:

            self.ts_Sizer.DeleteWindows()

        else:

            self.logger.wxFAIL_MSG(
                'DeleteWindows unexpected ts_Kind %s.' % self.ts_Kind)

    #-----------------------------------------------------------------------
 
    def DetachSizer(self):
        '''
        Enable deleting the SizerItem without destroying the contained sizer.

        Modeled after DetachSizer in sizer.h file of wxWidgets.
        '''
        self.ts_Sizer = None

    #-----------------------------------------------------------------------
 
    def DoSetSizer(self, sizer):
        '''

        Modeled after DoSetSizer in sizer.cpp file of wxWidgets.
        '''
        self.ts_Kind = wx.Item_Sizer
        self.ts_Sizer = sizer

    #-----------------------------------------------------------------------
 
    def DoSetSpacer(self, size):
        '''

        Modeled after DoSetSpacer in sizer.cpp file of wxWidgets.
        '''
        self.ts_Kind = wx.Item_Spacer
        self.ts_Spacer = wxSizerSpacer(size)
        self.ts_MinSize = size
        self.SetRatio(size)

    #-----------------------------------------------------------------------
 
    def DoSetWindow(self, window):
        '''

        Modeled after DoSetWindow in sizer.cpp file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (window is not None),
            'SizerItem.DoSetWindow window cannot be =%s' % str(window))

        self.ts_Kind = wx.Item_Window
        self.ts_Window = window

        # window does not become smaller than its initial size,
        # whatever happens
        self.ts_MinSize = window.GetSize()

        if (self.ts_Flag & wx.FIXED_MINSIZE):
            window.SetMinSize(self.ts_MinSize)

        # aspect ratio calculated from initial size
        self.SetRatio(self.ts_MinSize)

    #-----------------------------------------------------------------------

    def Free(self):
        '''

        Modeled after Free in sizer.cpp file of wxWidgets.
        '''
        if self.ts_Kind == wx.Item_None:
            pass

        elif self.ts_Kind == wx.Item_Window:
            self.ts_Window.SetContainingSizer(None)

        elif self.ts_Kind == wx.Item_Sizer:
            del self.ts_Sizer

        elif self.ts_Kind == wx.Item_Spacer:
            del self.ts_Spacer

        else:
            self.logger.wxFAIL_MSG(
                'Free Item_Max (%s) cannot be %s' % (wx.Item_Max,
                                                     self.ts_Kind))

        self.ts_Kind = wx.Item_None

    #-----------------------------------------------------------------------
 
    def GetBorder(self):
        '''
        Get the border value for this item.

        Modeled after GetBorder in sizer.h file of wxWidgets.
        '''
        return (self.ts_Border)

    #-----------------------------------------------------------------------
 
    def GetFlag(self):
        '''
        Get the flag value for this item.

        Modeled after GetFlag in sizer.h file of wxWidgets.
        '''
        return (self.ts_Flag)

    #-----------------------------------------------------------------------
 
##    def GetHGrow(self):
##        '''
##        TBD
##        '''
##        return (False)

    #-----------------------------------------------------------------------
 
    def GetMinSize(self):
        '''
        Get the minimum size needed for the item.

        Modeled after GetMinSize in sizer.h file of wxWidgets.
        '''
        return (self.ts_MinSize)

    #-----------------------------------------------------------------------
 
    def GetMinSizeWithBorder(self):
        '''
        Get the minimum size needed for the item with space for the borders
        added, if needed.

        Modeled after GetMinSizeWithBorder in sizer.cpp file of wxWidgets.
        '''
        ret = self.ts_MinSize

        border = self.tsGetBorderCharacterDimensions(thickness=self.ts_Border)

        if self.ts_Flag & wx.WEST:
            ret.x += border.width
 
        if self.ts_Flag & wx.EAST:
            ret.x += border.width
 
        if self.ts_Flag & wx.NORTH:
            ret.y += border.height
 
        if self.ts_Flag & wx.SOUTH:
            ret.y += border.height

        return (ret)

    #-----------------------------------------------------------------------
 
    def GetOption(self, *args, **kwargs):
        '''
        Please use GetProportion instead.
        # Deprecated in 2.6, use {G,S}etProportion instead.

        Modeled after GetOption in sizer.h file of wxWidgets.
        '''
        if True or args is None or kwargs is None:
            self.GetProportion()
        else:
            msg = 'NotImplementedError: %s' % 'GetOption in tsWxSizerItem'
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def GetPosition(self):
        '''
        Returns the current position of the item, as set in the last Layout.

        Modeled after GetPosition in sizer.h file of wxWidgets.
        '''
        return (wxPoint(self.ts_Rect.x, self.ts_Rect.y))

    #-----------------------------------------------------------------------

    def GetProportion(self):
        '''
        Get the proportion value for this item.

        Modeled after GetProportion in sizer.h file of wxWidgets.
        '''
        return (self.ts_Proportion)

    #-----------------------------------------------------------------------
 
    def GetRatio(self):
        '''
        Get the ratio item attribute.

        Modeled after GetRatio in sizer.h file of wxWidgets.
        '''
        return (self.ts_Ratio)

    #-----------------------------------------------------------------------
 
    def GetRect(self):
        '''
        Returns the rectangle that the sizer item should occupy

        Modeled after GetRect in sizer.h file of wxWidgets.
        '''
        return (self.ts_Rect)

    #-----------------------------------------------------------------------
 
    def GetSize(self):
        '''
        Get the current size of the item, as set in the last Layout.

        Modeled after GetSize in sizer.cpp file of wxWidgets.
        '''
        if self.ts_Kind == wx.Item_None:
            ret = wxSize(0, 0)

        elif self.ts_Kind == wx.Item_Window:
            ret = self.ts_Window.GetSize()

        elif self.ts_Kind == wx.Item_Sizer:
            ret = self.ts_Sizer.GetSize()

        elif self.ts_Kind == wx.Item_Spacer:
            ret = self.ts_Spacer.GetSize()

        else:
            # elif self.ts_Kind == wx.Item_Max:
            self.logger.wxFAIL_MSG(
                'Unexpected wxSizerItem.GetSize ts_Kind == wx.Item_Max.')

        border = self.tsGetBorderCharacterDimensions(
            thickness=self.ts_Border)

        if self.ts_Flag & wx.WEST:
            ret.x += border.width

        if self.ts_Flag & wx.EAST:
            ret.x += border.width

        if self.ts_Flag & wx.NORTH:
            ret.y += border.height

        if self.ts_Flag & wx.SOUTH:
            ret.y += border.height

        return (ret)

    #-----------------------------------------------------------------------
 
    def GetSizer(self):
        '''
        Get the subsizer (if any) that is managed by this sizer item.

        Modeled after GetSizer in sizer.h file of wxWidgets.
        '''
        return (self.ts_Sizer)

    #-----------------------------------------------------------------------
 
    def GetSpacer(self):
        '''
        Get the size of the spacer managed by this sizer item.

        Modeled after GetSpacer in sizer.h file of wxWidgets.
        '''
        if (self.ts_Kind == wx.Item_Spacer):

            size = self.ts_Spacer.GetSize()

        return (size)

    #-----------------------------------------------------------------------
 
    def GetUserData(self):
        '''
        Returns the userData associated with this sizer item, or None if
        there is not any.

        Modeled after GetUserData in sizer.h file of wxWidgets.
        '''
        return (self.ts_UserData)

    #-----------------------------------------------------------------------
 
##    def GetVGrow(self):
##        '''

##        Modeled after TBD in sizer.cpp file of wxWidgets.
##        '''
##        return (False)

    #-----------------------------------------------------------------------
 
    def GetWindow(self):
        '''
        Get the window (if any) that is managed by this sizer item.

        Modeled after GetWindow in sizer.h file of wxWidgets.
        '''
        if (self.ts_Kind == wx.Item_Window):
            return (self.ts_Window)
        else:
            return (None)

    #-----------------------------------------------------------------------

    def InformFirstDirection(self,
                             direction,
                             size,
                             availableOtherDir):
        '''

        Modeled after InformFirstDirection in sizer.cpp file of wxWidgets.
        '''

        # The size that come here will be including borders.
        # Child items should get it without borders.
        border = self.tsGetBorderCharacterDimensions(
            thickness=self.ts_Border)

        if size > 0:

            if (direction == wx.HORIZONTAL):

                if (self.ts_Flag & wx.WEST):
                    size -= border.width

                if (self.ts_Flag & wx.EAST):
                    size -= border.width

            elif (direction == wx.VERTICAL):

                if (self.ts_Flag & wx.NORTH):
                    size -= border.height

                if (self.ts_Flag & wx.SOUTH):
                    size -= border.height

        didUse = False
        # Pass the information along to the held object
        if (self.IsSizer()):

            didUse = self.GetSizer().InformFirstDirection(
                direction,
                size,
                availableOtherDir)

            if (didUse):
                self.ts_MinSize = self.GetSizer().CalcMin()

        elif (self.IsWindow()):

            didUse =  self.GetWindow().InformFirstDirection(
                direction,
                size,
                availableOtherDir)

            if (didUse):
                self.ts_MinSize = self.ts_Window.GetEffectiveMinSize()

            # This information is useful for items with wxSHAPED flag, since
            # we can request an optimal min size for such an item. Even if
            # we overwrite the m_minSize member here, we can read it back from
            # the owned window (happens automatically).
            if ((self.ts_Flag & wx.SHAPED) and \
                (self.ts_Flag & wx.EXPAND) and \
                direction):

                if (not self.IsNullDouble(self.ts_Ratio)):

                    fmt1 = 'Shaped item, non-zero '
                    fmt2 = 'proportion in wxSizerItem.'
                    fmt3 = 'InformFirstDirection()'
                    self.logger.wxCHECK_MSG((self.ts_Proportion == 0),
                                            False,
                                            (fmt1 + fmt2 + fmt3))

                    if (direction == wx.HORIZONTAL and \
                        (not self.IsNullDouble(self.ts_Ratio))):

                        # Clip size so that we do not take too much
                        if ((availableOtherDir >= 0) and \
                            (int(size/self.ts_Ratio) - \
                             self.ts_MinSize.y) > availableOtherDir):

                            size = int((availableOtherDir + \
                                        self.ts_MinSize.y) * self.ts_Ratio)

                        self.ts_MinSize = wxSize(size,
                                                 int(size/self.ts_Ratio))

                    elif (direction == wx.VERTICAL):

                        # Clip size so that we do not take too much
                        if ((availableOtherDir >= 0) and \
                            (int(size * self.ts_Ratio) - (
                                self.ts_MinSize.x)) > availableOtherDir):

                            size = int((availableOtherDir + \
                                        self.ts_MinSize.x) / self.ts_Ratio)

                        self.ts_MinSize = wxSize(int(size * self.ts_Ratio),
                                                 size)

                    didUse = True

        return (didUse)

    #-----------------------------------------------------------------------

    def IsNullDouble(self, x):
        '''
        Compare a double precision floating point value with zero.

        Modeled after IsNullDouble in sizer.cpp file of wxWidgets.
        '''
        return (self.IsSameDouble(x, float(0.0)))

    #-----------------------------------------------------------------------

    def IsSameDouble(self, x, y):
        '''
        Compare two double precision floating point values for equality.

        Modeled after IsSameDouble in sizer.cpp file of wxWidgets.
        '''
        return (x == y)

    #-----------------------------------------------------------------------
 
    def IsShown(self):
        '''
        Is the item to be shown in the layout?

        This function behaves obviously for the windows and spacers but for the
        sizers it returns true if any sizer element is shown and only returns
        false if all of them are hidden.

        Modeled after IsShown in sizer.cpp file of wxWidgets.
        '''
        if (self.ts_Flag & wx.RESERVE_SPACE_EVEN_IF_HIDDEN):
            return (True)

        self.logger.wxASSERT_MSG(
           (self.ts_Kind != wx.Item_Max),
           'SizerItem.IsShown cannot have Item_Max (%s) be ts_Kind (%s)' % (
               wx.Item_Max, self.ts_Kind))

        if (self.ts_Kind == wx.Item_None):

            # we may be called from CalcMin(), just return false so that we're
            # not used
            return (False)

        elif (self.ts_Kind == wx.Item_Window):

            return (self.ts_Window.IsShown())

        elif (self.ts_Kind == wx.Item_Sizer):

            # arbitrarily decide that if at least one of our elements is
            # shown, so are we (this arbitrariness is the reason for
            # deprecating this function)

            # Some apps (such as dialog editors) depend on an empty sizer
            # still being laid out correctly and reporting the correct size
            # and position.

            theChildCount = self.ts_Sizer.GetChildren().GetCount()
            if theChildCount == 0:

                return (True)

            else:
##                node = []

##                for i in range(theChildCount):
##                    if i == 0:
##                        node.append(self.ts_Sizer.GetChildren().GetFirst())
##                    else:
##                        node.append(node.GetNext())
                node = self.ts_Sizer.GetChildren()

                for i in range(theChildCount):
                    if node[i].GetData().IsShown():
                        return (True)

                return (False)

        elif (self.ts_Kind == wx.Item_Spacer):

            return (self.ts_Spacer.IsShown())

        else:

            # Item_Max
            self.logger.wxFAIL_MSG(
                'Unexpected wxSizerItem: ts_Kind %s' % self.ts_Kind)

        return (False)

    #-----------------------------------------------------------------------

##    # This is a helper to support wxRESERVE_SPACE_EVEN_IF_HIDDEN. In wx 2.9+,
##    # this flag is respected by IsShown(), but not in wx 2.8.
##    bool wxSizerItem::ShouldAccountFor() const
##
##        if ( m_flag & wxRESERVE_SPACE_EVEN_IF_HIDDEN )
##            return true;

##        if ( IsSizer() )
##
##            # this mirrors wxSizerItem::IsShown() code above
##            const wxSizerItemList& children = m_sizer->GetChildren();
##            if ( children.GetCount() == 0 )
##                return true;

##            for ( wxSizerItemList::compatibility_iterator
##                  node = children.GetFirst();
##                  node;
##                  node = node->GetNext() )
##
##                if ( node->GetData()->ShouldAccountFor() )
##                    return true;
##
##            return false;
##
##        else
##
##            return IsShown();
##
##

    #-----------------------------------------------------------------------
 
    def IsSizer(self):
        '''
        Is this sizer item a subsizer?

        Modeled after IsSizer in sizer.h file of wxWidgets.
        '''
        if  ((self.ts_Kind == wx.Item_None) or \
             (self.ts_Kind == wx.Item_Spacer) or \
             (self.ts_Kind == wx.Item_Window)):

            return (False)

        else:

            return (True)

    #-----------------------------------------------------------------------
 
    def IsSpacer(self):
        '''
        Is this sizer item a spacer?

        Modeled after IsSpacer in sizer.h file of wxWidgets.
        '''
        return (self.ts_Kind == wx.Item_Spacer)

    #-----------------------------------------------------------------------
 
    def IsWindow(self):
        '''
        Is this sizer item a window?

        Modeled after IsWindow in sizer.h file of wxWidgets.
        '''
        return (self.ts_Kind == wx.Item_Window)

    #-----------------------------------------------------------------------
 
    def SetBorder(self, border):
        '''
        Set the border value for this item.

        Modeled after SetBorder in sizer.h file of wxWidgets.
        '''
        self.ts_Border = border

    #-----------------------------------------------------------------------
 
    def SetDimension(self, *args):
        '''
        Set the position and size of the space allocated for this item by
        the sizer, and adjust the position and size of the item (window or
        subsizer) to be within that space taking alignment and borders into
        account.

        Modeled after SetDimension in sizer.cpp file of wxWidgets.
        '''
##        for i in range(len(args)):
##            print('txWxSizerItem.SetDimension:args[%d]= %s' % (
##                i, str(args[i])))
        if len(args) == 4:
            # len(args) == 4; Invoked via SetDimension(x, y, w, h)
            myPosition = wxPoint(args[0], args[1])
            mySize = wxSize(args[2], args[3])

        else:

            # len(args) == 2; Invoked via SetDimension(pos, size)
            myPosition = args[0]
            mySize = args[1]


        if self.ts_Flag & wx.SHAPED:
 
            # adjust aspect ratio
            rwidth = int(mySize.height * self.ts_Ratio)
            if rwidth > mySize.width:
 
                # fit horizontally
                rheight = int(mySize.width / self.ts_Ratio)
                # add vertical space
                if self.ts_Flag & wx.ALIGN_CENTER_VERTICAL:
                    myPosition.y += (mySize.height - rheight) / 2

                elif self.ts_Flag & wx.ALIGN_BOTTOM:
                    myPosition.y += (mySize.height - rheight)
                # use reduced dimensions
                mySize.height = rheight
 
            elif rwidth < mySize.width:
 
                # add horizontal space
                if self.ts_Flag & wx.ALIGN_CENTER_HORIZONTAL:
                    myPosition.x += (mySize.width - rwidth) / 2

                elif self.ts_Flag & wx.ALIGN_RIGHT:
                    myPosition.x += (mySize.width - rwidth)
                mySize.width = rwidth
 
        # This is what GetPosition() returns. Since we calculate
        # borders afterwards, GetPosition() will be the left/top
        # corner of the surrounding border.
        myBorder = self.tsGetBorderCharacterDimensions(
            thickness=self.ts_Border)

        if (self.ts_Flag & wx.WEST):
 
            myPosition.x += myBorder.width
            mySize.width -= myBorder.width
 
        if (self.ts_Flag & wx.EAST):
 
            mySize.width -= myBorder.width
 
        if (self.ts_Flag & wx.NORTH):
 
            myPosition.y += myBorder.height
            mySize.height -= myBorder.height
 
        if (self.ts_Flag & wx.SOUTH):
 
            mySize.height -= myBorder.height

        if (mySize.width < 0):
            mySize.width = 0

        if (mySize.height < 0):
            mySize.height = 0

        self.ts_Rect = wxRect(myPosition.x,
                              myPosition.y,
                              mySize.width,
                              mySize.height)

        if (self.ts_Kind == wx.Item_None):

            self.logger.wxFAIL_MSG(
                'Cannot set size of uninitialized sizer item in ' + \
                'wx.SizerItem.SetDimension')

        elif (self.ts_Kind == wx.Item_Window):
            # Use wxSIZE_FORCE_EVENT here since a sizer item might
            # have changed alignment or some other property which would
            # not change the size of the window. In such a case, no
            # wxSizeEvent would normally be generated and thus the
            # control wouldn't get layed out correctly here.
            if True:
                self.ts_Window.SetSize(mySize)
#                    mySize,
#                    wx.SIZE_ALLOW_MINUS_ONE | wx.SIZE_FORCE_EVENT)
            else:
                self.ts_Window.SetSize(mySize)
#                    mySize,
#                    wx.SIZE_ALLOW_MINUS_ONE)

        elif (self.ts_Kind == wx.Item_Sizer):

            self.ts_Sizer.SetDimension(myPosition, mySize)

        elif (self.ts_Kind == wx.Item_Spacer):

            self.ts_Spacer.SetSize(mySize)

        else: # Item_Max

            self.logger.wxFAIL_MSG('Unexpected wxSizerItem.ts_Kind=Item_Max')

    #-----------------------------------------------------------------------
 
    def SetFlag(self, flag):
        '''
        Set the flag value for this item.

        Modeled after SetFlag in sizer.h file of wxWidgets.
        '''
        self.ts_Flag = flag

    #-----------------------------------------------------------------------
 
##    def SetHGrow(self):
##        '''

##        Modeled after TBD in sizer.cpp file of wxWidgets.
##        '''
##        return (False)

    #-----------------------------------------------------------------------
 
    def SetInitSize(self, size):
        '''

        Modeled after SetInitSize in sizer.h file of wxWidgets.
        '''
        if (self.IsWindow()):
            self.ts_Window.SetMinSize(size)
        else:
            self.ts_MinSize = size

    #-----------------------------------------------------------------------
 
    def SetInitSizeXY(self, x, y):
        '''

        Modeled after SetInitSize in sizer.h file of wxWidgets.
        '''
        size = wxSize(x, y)
        if (self.IsWindow()):
            self.ts_Window.SetMinSize(size)
        else:
            self.ts_MinSize = size

    #-----------------------------------------------------------------------
 
    def SetMinSize(self, size):
        '''

        Modeled after SetMinSize in sizer.h file of wxWidgets.
        '''
        if (self.IsWindow()):
            self.ts_Window.SetMinSize(size)
        else:
            self.ts_MinSize = size

    #-----------------------------------------------------------------------
 
    def SetMinSizeXY(self, x, y):
        '''

        Modeled after SetMinSize in sizer.h file of wxWidgets.
        '''
        size = wxSize(x, y)
        if (self.IsWindow()):
            self.ts_Window.SetMinSize(size)
        else:
            self.ts_MinSize = size

    #-----------------------------------------------------------------------

    def SetOption(self, *args, **kwargs):
        '''
        Please use SetProportion instead.
        # Deprecated in 2.6, use {G,S}etProportion instead.

        Modeled after SetOption in sizer.h file of wxWidgets.
        '''
        if True or kwargs is None:
            proportion = args[0]
            self.SetProportion(proportion)
        else:
            msg = 'NotImplementedError: %s' % 'SetOption in tsWxSizerItem'
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
 
    def SetProportion(self, proportion):
        '''
        Set the proportion value for this item.

        Modeled after SetProportion in sizer.h file of wxWidgets.
        '''
        self.ts_Proportion = proportion

    #-----------------------------------------------------------------------
 
    def SetRatio(self, ratio):
        '''
        Set the ratio item attribute.

        Modeled after SetRatio in sizer.h file of wxWidgets.
        '''
        self.ts_Ratio = float(ratio)

    #-----------------------------------------------------------------------
 
    def SetRatioSize(self, size):
        '''
        Set the ratio item attribute.

        Modeled after SetRatioSize in sizer.cpp file of wxWidgets.
        '''
        mySize = wx.tsGetClassInstanceFromTuple(size, wxSize)
        if mySize.height > 0:
            self.SetRatio(float(mySize.width) / float(mySize.height))
        else:
            self.SetRatio(float(1.0))

    #-----------------------------------------------------------------------
 
    def SetRatioWH(self, width, height):
        '''
        Set the ratio item attribute.

        Modeled after SetRatioWH in sizer.h file of wxWidgets.
        '''
        if height > 0:
            self.SetRatio(float(width) / float(height))
        else:
            self.SetRatio(float(1.0))

    #-----------------------------------------------------------------------
 
    def SetSizer(self, sizer):
        '''
        Set the subsizer to be managed by this sizer item.

        Modeled after SetSizer in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
           (sizer is not None),
           'SizerItem.SetSizer sizer cannot be %s.' % sizer)

        self.logger.wxASSERT_MSG(
           (not (isinstance(sizer, tuple))),
           'SizerItem.SetSizer sizer instance cannot be %s.' % str(sizer))

        self.ts_Kind = wx.Item_Sizer
        self.ts_Sizer = sizer

    #-----------------------------------------------------------------------
 
    def SetSpacer(self, size):
        '''
        Set the size of the spacer to be managed by this sizer item.

        Modeled after SetSpacer in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
           (size is None),
           'SizerItem.SetSpacer size cannot be %s.' % size)

        self.ts_Kind = wx.Item_Spacer

        theSize = wx.tsGetClassInstanceFromTuple(size, wxSize)
        self.ts_Spacer = wxSizerSpacer(theSize)
        self.ts_MinSize = theSize
        self.SetRatio(theSize)

    #-----------------------------------------------------------------------
 
    def SetUserData(self, userData):
        '''
        Associate a Python object with this sizer item.

        Modeled after SetUserData in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
           (userData is None),
           'SetUserData cannot have userData be %s.' % userData)

        self.ts_UserData = userData

    #-----------------------------------------------------------------------
 
    def SetWindow(self, window):
        '''
        Set the window to be managed by this sizer item.

        Modeled after SetWindow in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
           (window is not None),
           'SetWindow cannot have window be %s.' % str(window))

        self.ts_Kind = wx.Item_Window
        self.ts_Window = window

        # window doesn't become smaller than its initial size, whatever happens
        if True:
            self.ts_MinSize = window.Size
        else:
            if window.Size is None:
                # TBD - What should size be when curses handle not yet created.
                self.ts_MinSize = wxSize(10 * wx.pixelWidthPerCharacter,
                                         3 * wx.pixelHeightPerCharacter)
            else:
                self.ts_MinSize = window.Size

##        print('tsWxSizerItem.SetWindow: MinSize=%s' % self.ts_MinSize)

        if self.ts_Flag & wx.FIXED_MINSIZE:
            window.SetMinSize(self.ts_MinSize)

        # aspect ratio calculated from initial size
        self.SetRatioSize(self.ts_MinSize)

    #-----------------------------------------------------------------------
 
    def Show(self, show):
        '''
        Set the show item attribute, which sizers use to determine if the
        item is to be made part of the layout or not. If the item is tracking
        a window then it is shown or hidden as needed.

        Modeled after Show in sizer.cpp file of wxWidgets.
        '''
        if (self.ts_Kind == wx.Item_None):

            self.logger.wxFAIL_MSG(
                'Cannot show uninitialized sizer item in ' \
                'wxSizerItem.Show')

        elif (self.ts_Kind == wx.Item_Window):

            self.ts_Window.Show(show)

        elif (self.ts_Kind == wx.Item_Sizer):

            self.ts_Sizer.Show(show)

        elif (self.ts_Kind == wx.Item_Spacer):
            self.ts_Spacer.Show(show)

        else:

            self.logger.wxFAIL_MSG(
                'Unexpected wxSizerItem.Show ts_Kind %s' % self.ts_Kind)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetBorderCharacterDimensions(self, thickness):
        '''
        Return width and height of border character in pixels.

        Parameter:

        thickness --- Border line thickness in pixels.
        '''
        if thickness == -1:

            if wx.USE_BORDER_BY_DEFAULT:

                # Default (1-pixel) border required.
                dimensions = wxSize(wx.pixelWidthPerCharacter,
                                    wx.pixelHeightPerCharacter)
            else:

                # No border required.
                dimensions = wxSize(0, 0)

        elif thickness == 0:

            # No border required.
            dimensions = wxSize(0, 0)

        else:

            # Override thickness and apply default (1-pixel) border.
            dimensions = wxSize(min(1, thickness) * wx.pixelWidthPerCharacter,
                                min(1, thickness) * wx.pixelHeightPerCharacter)

        return (dimensions)

    #-----------------------------------------------------------------------

    def SetItemBounds(self, item, x, y, w, h):
        '''

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        pt = wxPoint(x, y)
        sz = wxSize(item.GetMinSizeWithBorder())
        flag = int(item.GetFlag())

        if flag & wx.EXPAND or \
           flag & wx.SHAPED:
 
            sz = wxSize(w, h)
 
        else:
 
            if flag & wx.ALIGN_CENTER_HORIZONTAL:
 
                pt.x = x + (w - sz.x) // 2
 
            elif flag & wx.ALIGN_RIGHT:
 
                pt.x = x + (w - sz.x)
 

            if flag & wx.ALIGN_CENTER_VERTICAL:
 
                pt.y = y + (h - sz.y) // 2
 
            elif flag & wx.ALIGN_BOTTOM:
 
                pt.y = y + (h - sz.y)

        item.SetDimension(pt, sz)

    #-----------------------------------------------------------------------

    def nextSizerItemId(self):
        '''
        Generate next in sequence of unique IDs upon request of the application
        program. NOTE: This is independent of internal assignedID generation.
        '''
        if self.ts_LastSizerItemId == wx.ID_NONE:

            self.ts_LastSizerItemId = 0

        else:

            self.ts_LastSizerItemId += 1

        return (self.ts_LastSizerItemId)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
 
    Border = property(GetBorder, SetBorder)
    Flag = property(GetFlag, SetFlag)
    MinSize = property(GetMinSize)
    MinSizeWithBorder = property(GetMinSizeWithBorder)
    Position = property(GetPosition)
    Proportion = property(GetProportion, SetProportion)
    Ratio = property(GetRatio, SetRatio)
    Rect = property(GetRect)
    Size = property(GetSize)
    Sizer = property(GetSizer, SetSizer)
    Spacer = property(GetSpacer, SetSpacer)
    UserData = property(GetUserData, SetUserData)
    Window = property(GetWindow, SetWindow)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
