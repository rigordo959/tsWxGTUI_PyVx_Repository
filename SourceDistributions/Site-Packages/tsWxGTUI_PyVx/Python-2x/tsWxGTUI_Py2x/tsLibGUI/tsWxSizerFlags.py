#! /usr/bin/env python
# "Time-stamp: <04/09/2015  4:31:44 AM rsg>"
'''
tsWxSizerFlags.py - Container Class for sizer item flags that
provides readable names for them. Normally, when you add an
item to a sizer via wxSizer.Add, you have to specify a lot of
flags and parameters which can be unwieldy. This is where
wxSizerFlags comes in: it allows you to specify all parameters
using the named methods instead.
'''
#################################################################
#
# File: tsWxSizerFlags.py
#
# Purpose:
#
#    Container Class for sizer item flags that provides readable
#    names for them. Normally, when you add an item to a sizer
#    via wxSizer.Add, you have to specify a lot of flags and
#    parameters which can be unwieldy. This is where wxSizerFlags
#    comes in: it allows you to specify all parameters using the
#    named methods instead.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSizerFlags import SizerFlags
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
#    1) Character-mode displays only support 8 (width) x 12 (height)
#       pixel borders. This applies whether or not wxALL direction
#       has been specified and whether or not wxWidgets 1, 2, 3
#       or other pixel thickness has been specified.
#
#    2) The "tsGetBorderCharacterDimensions" method must be
#       invoked, as appropriate, during all sizer.Layout operations.
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    2011/01/03 rsg Added "tsGetBorderCharacterDimensions" method
#                   to accomodate character-mode rather than
#                   pixel-mode displays.
#
# ToDo:
#
#    2011/01/25 rsg TBD investigate replacing print statements by
#                   logger assert and check statements. This may
#                   require replacement of "object" base class
#                   type by "Object" type.
#
#################################################################

__title__     = 'tsWxSizerFlags'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxDisplay import Display as wxDisplay
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

SIZER_FLAGS_MASK = (
    0 | \
    wx.CENTER | \
    wx.RESERVE_SPACE_EVEN_IF_HIDDEN | \
    wx.HORIZONTAL | \
    wx.VERTICAL | \
    wx.LEFT | \
    wx.RIGHT | \
    wx.UP | \
    wx.DOWN | \
    wx.ALIGN_NOT | \
    wx.ALIGN_CENTER_HORIZONTAL | \
    wx.ALIGN_RIGHT | \
    wx.ALIGN_BOTTOM | \
    wx.ALIGN_CENTER_VERTICAL | \
    wx.STRETCH_NOT | \
    wx.SHRINK | \
    wx.GROW | \
    wx.SHAPED | \
    wx.FIXED_MINSIZE
    )

#---------------------------------------------------------------------------
 
class SizerFlags(object):
    '''
    Normally, when you add an item to a sizer via wx.Sizer.Add, you have to
    specify a lot of flags and parameters which can be unwieldy. This is
    where wx.SizerFlags comes in: it allows you to specify all parameters
    using the named methods instead. For example, instead of:

    sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL, 10)

    you can now write:

    sizer.AddF(ctrl, wx.SizerFlags().Expand().Border(wx.ALL, 10))

    This is more readable and also allows you to create wx.SizerFlags objects
    which can be reused for several sizer items.:

    flagsExpand = wx.SizerFlags(1)
    flagsExpand.Expand().Border(wx.ALL, 10)
    sizer.AddF(ctrl1, flagsExpand)
    sizer.AddF(ctrl2, flagsExpand)

    Note that by specification, all methods of wx.SizerFlags return the
    wx.SizerFlags object itself allowing chaining multiple method calls
    like in the examples above.
    '''
    def __init__(self, proportion=0):
        '''
        Construct the flags object initialized with the given proportion
        (0 by default).

        Modeled after wxSizerFlags in sizer.h file of wxWidgets.
        '''
        ## theClass = 'SizerFlags'

        ## wx.RegisterFirstCallerClassName(self, theClass)

        ## Object.__init__(self)

        ## self.tsBeginClassRegistration(theClass, wx.ID_ANY)


        try:
            self.logger = wxDisplay.TheLogger
            if self.logger is None:
                self.logger = tsLogger.TsLogger()
        except AttributeError, errorCode:
            msg = 'Display.TheLogger not available (%s)' % errorCode
            print(' DEBUG: %s' % msg)
            self.logger = tsLogger.TsLogger()
            self.logger.debug(msg)

        # Set Default Values
        self.ts_BorderInPixels = 0 # -1
        self.ts_Flags = 0
        self.ts_Proportion = proportion

        ## self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##        def __del__(self):
##            '''
##            '''
##            pass

    #-----------------------------------------------------------------------

    def Align(self, alignment):
        '''
        Sets the item alignment

        Modeled after Align in sizer.h file of wxWidgets.
        '''
        # notice that Align() replaces the current alignment flags, use
        # specific methods below such as Top(), Left() &c if you want
        # to set just the vertical or horizontal alignment

        self.ts_Flags &= ~wx.ALIGN_MASK
        self.ts_Flags |= alignment

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Align Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------

    @staticmethod
    def ASSERT_VALID_SIZER_FLAGS(f):
        '''
        Checks if flags value (f) is within the mask of allowed values.

        Return True is specified flag bits (f) represents a combination
        of valid sizer flag bits.
        '''
        if (f == (f & SIZER_FLAGS_MASK)) :

            valid = True

        else:

            valid = False

        return (valid)

    #-----------------------------------------------------------------------

    def Border(self,
               direction=wx.ALL,
               borderInPixels=-1):
        '''
        Sets the border of the item in the direction(s) or sides given
        by the direction parameter. If the borderInPixels value is not
        given then the default border size (see GetDefaultBorder) will
        be used.

        Modeled after Border in sizer.h file of wxWidgets.
        '''
        self.ts_Flags &= ~wx.ALL
        self.ts_Flags |= direction

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Border Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        self.ts_BorderInPixels = borderInPixels

        return (self)

    #-----------------------------------------------------------------------

    def Bottom(self):
        '''
        Aligns the object to the bottom of the available space, a shortcut
        for calling Align(wx.ALIGN_BOTTOM)

        Modeled after Bottom in sizer.h file of wxWidgets.
        '''
        self.ts_Flags = (
            self.ts_Flags & ~wx.ALIGN_CENTER_VERTICAL) | wx.ALIGN_BOTTOM

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Bottom Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------

    def Center(self):
        '''
        Sets the centering alignment flags.

        Modeled after Center in sizer.h file of wxWidgets.
        '''
        return (self.Centre())

    #-----------------------------------------------------------------------

    def Centre(self):
        '''
        Same as Center for those with an alternate dialect of English.

        Modeled after Centre in sizer.h file of wxWidgets.
        '''
        return (self.Align(wx.ALIGN_CENTER))

    #-----------------------------------------------------------------------
 
    def DoubleBorder(self,
                     direction=wx.ALL):
        '''
        Sets the border in the given direction to twice the default border
        size.

        Modeled after DoubleBorder in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (direction == wx.ALL),
            'DoubleBorder direction 0x%X != 0x%X.' % (
                direction,
                wx.ALL))

        if wx.USE_BORDER_BY_DEFAULT:

            # Can only support one border character
            return (self.Border(direction,
                                self.GetDefaultBorder()))

        else:

            return (self)

    #-----------------------------------------------------------------------
 
    def DoubleHorzBorder(self):
        '''
        Sets the left and right borders to twice the default border size.

        Modeled after DoubleHorzBorder in sizer.h file of wxWidgets.
        '''
        if wx.USE_BORDER_BY_DEFAULT:

            # Can only support one border character
            return (self.Border(wx.LEFT | wx.RIGHT,
                                SizerFlags.GetDefaultBorder()))

        else:

            return (self)

    #-----------------------------------------------------------------------
 
    def Expand(self):
        '''
        Sets the wx.EXPAND flag, which will cause the item to be expanded
        to fill as much space as it is given by the sizer.

        Modeled after Expand in sizer.h file of wxWidgets.
        '''
        self.ts_Flags |= wx.EXPAND

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Expand Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------

    def FixedMinSize(self):
        '''
        Sets the wx.FIXED_MINSIZE flag.

        Modeled after FixedMinSize in sizer.h file of wxWidgets.
        '''
        self.ts_Flags |= wx.FIXED_MINSIZE

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'FixedMinSize Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def GetBorderInPixels(self):
        '''
        Returns the border value in pixels to be used in the sizer item.

        Modeled after GetBorderInPixels in sizer.h file of wxWidgets.
        '''
        return (self.ts_BorderInPixels)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetDefaultBorder():
        '''
        Returns the default border size used by the other border methods

        Modeled after GetDefaultBorder in sizer.h file of wxWidgets.
        '''
        if wx.USE_BORDER_BY_DEFAULT:

            return (-1)

        else:

            return (0)

    #-----------------------------------------------------------------------
 
    def GetFlags(self):
        '''
        Returns the flags value to be used in the sizer item.

        Modeled after GetFlags in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'GetFlags Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self.ts_Flags)

    #-----------------------------------------------------------------------
 
    def GetProportion(self):
        '''
        Returns the proportion value to be used in the sizer item.

        Modeled after GetProportion in sizer.h file of wxWidgets.
        '''
        return (self.ts_Proportion)

    #-----------------------------------------------------------------------
 
    def HorzBorder(self):
        '''
        Sets the left and right borders to the default border size.

        Modeled after HorzBorder in sizer.h file of wxWidgets.
        '''
        if wx.USE_BORDER_BY_DEFAULT:

            return (self.Border(wx.LEFT | wx.RIGHT,
                                SizerFlags.GetDefaultBorder()))

        else:

            return (self)

    #-----------------------------------------------------------------------
 
    def Left(self):
        '''
        Aligns the object to the left, a shortcut for calling
        Align(wx.ALIGN_LEFT)

        Modeled after Left in sizer.h file of wxWidgets.
        '''
        self.ts_Flags &= ~(wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL)

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Left Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def Proportion(self, proportion):
        '''
        Sets the items proportion value.

        Modeled after Proportion in sizer.h file of wxWidgets.
        '''
        self.ts_Proportion = proportion
 
        return (self)

    #-----------------------------------------------------------------------

    def ReserveSpaceEvenIfHidden(self):
        '''
        Makes the item ignore windows visibility status

        Modeled after ReserveSpaceEvenIfHidden in sizer.h file of wxWidgets.
        '''
        self.ts_Flags |= wx.RESERVE_SPACE_EVEN_IF_HIDDEN

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'ReserveSpaceEvenIfHidden Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def Right(self):
        '''
        Aligns the object to the right, a shortcut for calling
        Align(wx.ALIGN_RIGHT)

        Modeled after Right in sizer.h file of wxWidgets.
        '''
        self.ts_Flags = (
            self.ts_Flags & ~wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_RIGHT)

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Right Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def Shaped(self):
        '''
        Sets the wx.SHAPED flag.

        Modeled after Shaped in sizer.h file of wxWidgets.
        '''
        self.ts_Flags |= wx.SHAPED

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Shaped Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def Top(self):
        '''
        Aligns the object to the top of the available space, a shortcut
        for calling Align(wx.ALIGN_TOP)

        Modeled after Top in sizer.h file of wxWidgets.
        '''
        self.ts_Flags &= ~(wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_VERTICAL)

        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'Top Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        return (self)

    #-----------------------------------------------------------------------
 
    def TripleBorder(self, direction=wx.ALL):
        '''
        Sets the border in the given direction to three times the default
        border size.

        Modeled after TripleBorder in sizer.h file of wxWidgets.
        '''
        self.logger.wxASSERT_MSG(
            (self.ts_Flags == (self.ts_Flags & SIZER_FLAGS_MASK)),
            'TripleBorder Flags 0x%X != 0x%X.' % (
                self.ts_Flags,
                self.ts_Flags & SIZER_FLAGS_MASK))

        if wx.USE_BORDER_BY_DEFAULT:

            # Can only support one border character
            return (self.Border(direction,
                                SizerFlags.GetDefaultBorder()))

        else:

            return (self)

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

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    myLogger = tsLogger.TsLogger(threshold=tsLogger.DEBUG,
                                 name='./test_tsWxSizerFlags.log')

    SIZER_FLAGS = [
        0,                               # 0x00000000
        wx.CENTER,                       # 0x00000001
        wx.RESERVE_SPACE_EVEN_IF_HIDDEN, # 0x00000002
        wx.HORIZONTAL,                   # 0x00000004
        wx.VERTICAL,                     # 0x00000008
        wx.LEFT,                         # 0x00000010
        wx.RIGHT,                        # 0x00000020
        wx.UP,                           # 0x00000040
        wx.DOWN,                         # 0x00000080
        wx.ALIGN_NOT,                    # 0x00000000
        wx.ALIGN_CENTER_HORIZONTAL,      # 0x00000100
        wx.ALIGN_RIGHT,                  # 0x00000200
        wx.ALIGN_BOTTOM,                 # 0x00000400
        wx.ALIGN_CENTER_VERTICAL,        # 0x00000800
        wx.STRETCH_NOT,                  # 0x00000000
        wx.SHRINK,                       # 0x00001000
        wx.GROW,                         # 0x00002000
        wx.SHAPED,                       # 0x00004000
        wx.FIXED_MINSIZE,                # 0x00008000
        0xFFFFFFFF                       # 0xFFFFFFFF
        ]

##    Normally, when you add an item to a sizer via wx.Sizer.Add, you have to
##    specify a lot of flags and parameters which can be unwieldy. This is
##    where wx.SizerFlags comes in: it allows you to specify all parameters
##    using the named methods instead. For example, instead of:
 
    ctrlX = SizerFlags()
    ctrlX.ts_BorderInPixels = 10
    ctrlX.ts_Proportion = 1.0
    ctrlX.ts_Flags = 0

    ctrlX.ts_Flags = ctrlX.ts_Flags | wx.EXPAND | wx.ALL
    fmt1X = 'ctrlX.ts_Flags=0x%X; ' % ctrlX.ts_Flags
    fmt2X = 'ctrlX.ts_Proportion=%s; ' % ctrlX.ts_Proportion
    fmt3X = 'ctrlX.ts_BorderInPixels=%s' % ctrlX.ts_BorderInPixels
    msgX = fmt1X + fmt2X + fmt3X
    myLogger.info(msgX)

##    you can now write:

    ctrlY = SizerFlags()
    ctrlY.ts_Flags = 0
    ctrlY.ts_BorderInPixels = 0
    ctrlY.ts_Proportion = 1.0
    ctrlY.Expand().Border(wx.ALL, 10)
    fmt1Y = 'ctrlY.ts_Flags=0x%X; ' % ctrlY.GetFlags()
    fmt2Y = 'ctrlY.ts_Proportion=%s; ' % ctrlY.GetProportion()
    fmt3Y = 'ctrlY.ts_BorderInPixels=%s' % ctrlY.GetBorderInPixels()
    msgY = fmt1Y + fmt2Y + fmt3Y
    myLogger.info(msgY)

    if ((ctrlX.ts_Flags == ctrlY.ts_Flags) and \
        (ctrlX.ts_BorderInPixels == ctrlY.ts_BorderInPixels) and \
        (ctrlX.ts_Proportion == ctrlY.ts_Proportion)):

        match = True

    else:

        match = False

    myLogger.info(' Match (%s)' % match)

##    This is more readable and also allows you to create wx.SizerFlags objects
##    which can be reused for several sizer items.:

    ctrlZ = SizerFlags(wx.EXPAND)
    ctrlZ.Expand().Border(wx.ALL, 10)
    ctrlZ.ts_Proportion = 1.0
##    ctrlZ_sizer.AddF(ctrl1, flagsExpand)
##    ctrlZ_sizer.AddF(ctrl2, flagsExpand)

    if ((ctrlX.ts_Flags == ctrlZ.ts_Flags) and \
        (ctrlX.ts_BorderInPixels == ctrlZ.ts_BorderInPixels) and \
        (ctrlX.ts_Proportion == ctrlZ.ts_Proportion)):

        match = True

    else:

        match = False

##    myLogger.info('ctrlX.ts_Flags == ctrlZ_flagsExpand Match: %s' % match)

    myLogger.info(' Match (%s)' % match)

    theMask = 0
    theFlags = SizerFlags()
    i = 0
    for flag in SIZER_FLAGS:
        theMask = theMask | flag
        myLogger.info(
            '%2.2d (0x%8.8X); mask (0x%8.8X)' % (i, flag, theMask))
        theFlags.ASSERT_VALID_SIZER_FLAGS(flag)
        i += 1
