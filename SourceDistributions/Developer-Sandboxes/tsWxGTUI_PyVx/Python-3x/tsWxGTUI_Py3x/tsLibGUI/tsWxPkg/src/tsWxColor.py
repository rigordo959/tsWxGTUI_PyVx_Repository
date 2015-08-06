#! /usr/bin/env python
# "Time-stamp: <01/14/2014  5:04:50 AM rsg>"
'''
tsWxColor.py - Class to establish a colour object representing
a combination of Red, Green, and Blue (RGB) intensity values that
is used to determine drawing colours, window colours, etc.
Valid RGB values are in the range 0 to 255.
'''
#################################################################
#
# File: tsWxColor.py
#
# Purpose:
#
#    Class to establish a colour object representing a combination
#    of Red, Green, and Blue (RGB) intensity values that is used
#    to determine drawing colours, window colours, etc. Valid RGB
#    values are in the range 0 to 255.
#
# Usage (example):
#
#    # Import
#
#    from tsWxColor import Color
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
#    Under Construction.
#
#################################################################

__title__     = 'tsWxColor'
__version__   = '0.2.0'
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

import binascii
import curses

import tsExceptions as tse
##from tsReportUtilities import TsReportUtilities as tsru

import tsWxGlobals as wx
import tsWxGraphicalTextUserInterface as tsGTUI

from tsWxObject import Object

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Color(Object):
    '''
    A colour is an object representing a combination of Red, Green, and
    Blue (RGB) intensity values, and is used to determine drawing colours,
    window colours, etc.  Valid RGB values are in the range 0 to 255.

    In wxPython there are typemaps that will automatically convert from a
    colour name, from a #RRGGBB colour hex value string, or from a 3 or 4
    integer tuple to a wx.Colour object when calling C++ methods that
    expect a wxColour.  This means that the following are all
    equivallent:

    win.SetBackgroundColour(wxColour(0,0,255))
    win.SetBackgroundColour("BLUE")
    win.SetBackgroundColour("#0000FF")
    win.SetBackgroundColour((0,0,255))

    In addition to the RGB values, the alpha transparency can optionally
    be set.  This is supported by the typemaps as well as the wx.Colour
    constructors and setters.  (The alpha value is ignored in many places
    that take a wx.Colour object, but it is honored in things like wx.GCDC
    or wx.GraphicsContext.)  Adding an alpha value of 0xC0 (192) to the
    above samples looks like this:

    win.SetBackgroundColour(wxColour(0,0,255,192))
    win.SetBackgroundColour("BLUE:C0")
    win.SetBackgroundColour("#0000FFC0")
    win.SetBackgroundColour((0,0,255,192))

    Additional colour names and their coresponding values can be added
    using wx.ColourDatabase. Also see wx.lib.colourdb for a large set
    of colour names and values.  Various system colours (as set in the
    user system preferences or control panel) can be retrieved with
    wx.SystemSettings.GetColour.
    '''

    #-----------------------------------------------------------------------

    def __init__(self, red, green, blue, alpha):
        '''
        Constructs a colour from red, green, blue and alpha values.
        '''
        theClass = 'Color'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)
        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        self.ts_Alpha = alpha
        self.ts_Blue = blue
        self.ts_Green = green
        self.ts_Red = red

##        if TheColourDatabase == {}:
##            TheColourDatabase = ColorListRGB
 
        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def __eq__(self, other):
        '''
        Compare colours for equality.
        '''
        return (self.ts_Alpha == other.ts_Alpha and \
                self.ts_Blue == other.ts_Blue and \
                self.ts_Green == other.ts_Green and \
                self.ts_Red == other.ts_Red)

    #-----------------------------------------------------------------------

    def __getitem__(self, index):
        '''
        Under Construction.
        '''
        set_to_use = []
        for item in list(tsGTUI.colorSubstitutionMap.keys()):
            if item == 'name':
                pass
            else:
                set_to_use += [item]

        if 0 <= index and index < len(set_to_use):
            return (tsGTUI.xterm256ColorNamesFromCodes[index])
        else:
            return (-1)

    #-----------------------------------------------------------------------

    def __len__(self):
        '''
        Return length of this object.
        '''
        return (len(self))

    #-----------------------------------------------------------------------

    def __ne__(self, other):
        '''
        Compare colours for inequality.
        '''
        return (self.ts_Alpha != other.Alpha and \
                self.ts_Blue != other.ts_Blue and \
                self.ts_Green != other.ts_Green and \
                self.ts_Red != other.ts_Red)

    #-----------------------------------------------------------------------

    def __bool__(self):
        '''
        Return True if this object is not zero.
        '''
        return (self.ts_Alpha != 0 and \
                self.ts_Blue !=0 and \
                self.ts_Green != 0 and \
                self.ts_Red != 0)

    #-----------------------------------------------------------------------
 
    def __reduce__(self):
        '''
        Under construction.
        '''
        pass

    #-----------------------------------------------------------------------

    def __repr__(self):
        '''
        Return text representation.
        '''
        text = '#%2.2X%2.2X%2.2X:%2.2X'  % (
            self.ts_Red, self.ts_Green, self.ts_Blue, self.ts_Alpha)
        return (text)

    #-----------------------------------------------------------------------

    def __str__(self):
        '''
        Return text representation.
        '''
        text = '#%2.2X%2.2X%2.2X:%2.2X'  % (
            self.ts_Red, self.ts_Green, self.ts_Blue, self.ts_Alpha)
        return (text)

    #-----------------------------------------------------------------------

    def Alpha(self):
        '''
        Returns the Alpha value.
        '''
        return (self.ts_Alpha)

    #-----------------------------------------------------------------------

    @staticmethod
    def asTuple(*args, **kwargs):
        '''
        asTuple is deprecated, use Get instead
        '''
        if len(args) > 0 or \
           len(list(kwargs.keys())) > 0:
            msg = 'NotImplementedError: %s' % 'asTuple in tsWxColor'
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Blue(self):
        '''
        Returns the blue intensity.
        '''
        return (self.ts_Blue)

    #-----------------------------------------------------------------------

    def Get(self, includeAlpha=False):
        '''
        Returns the RGB intensity values as a tuple, optionally the alpha
        value as well.
        '''
        if includeAlpha:
            return (self.ts_Red, self.ts_Green, self.ts_Blue, self.ts_Alpha)
        else:
            return (self.ts_Red, self.ts_Green, self.ts_Blue)

    #-----------------------------------------------------------------------

    def GetAsString(self, flags):
        '''
        Return the colour as a string.
        '''
        myFlags = flags
        if myFlags == flags:
            text = '#%2.2X%2.2X%2.2X:%2.2X'  % (
                self.ts_Red, self.ts_Green, self.ts_Blue, self.ts_Alpha)
            return (text)

    #-----------------------------------------------------------------------

    def GetPixel(self):
        '''
        Returns a pixel value which is platform-dependent.
        '''
        text = '#%2.2X%2.2X%2.2X'  % (
            self.ts_Red, self.ts_Green, self.ts_Blue)
        return (text)

    #-----------------------------------------------------------------------

    def GetRGB(self):
        '''
        Return the colour as a packed RGB value
        '''
        text = '#%2.2X%2.2X%2.2X:%2.2X'  % (
            self.ts_Red, self.ts_Green, self.ts_Blue, self.ts_Alpha)
        return (text)

    #-----------------------------------------------------------------------

    def Green(self):
        '''
        Returns the green intensity.
        '''
        return (self.ts_Green)

    #-----------------------------------------------------------------------

    def IsOk(self):
        '''
        Returns True if the colour object is valid (the colour has been
        initialised with RGB values).
        '''
        return ((0 <= self.ts_Alpha) and (self.ts_Alpha <= 255) and \
                (0 <= self.ts_Blue) and (self.ts_Blue <= 255) and \
                (0 <= self.ts_Green) and (self.ts_Green <= 255) and \
                (0 <= self.ts_Red) and (self.ts_Red <= 255))

    #-----------------------------------------------------------------------

    def Ok(self):
        '''
        Returns True if the colour object is valid (the colour has been
        initialised with RGB values).
        '''
        return ((0 <= self.ts_Alpha) and (self.ts_Alpha <= 255) and \
                (0 <= self.ts_Blue) and (self.ts_Blue <= 255) and \
                (0 <= self.ts_Green) and (self.ts_Green <= 255) and \
                (0 <= self.ts_Red) and (self.ts_Red <= 255))

    #-----------------------------------------------------------------------

    def Red(self):
        '''
        Returns the red intensity.
        '''
        return (self.ts_Red)

    #-----------------------------------------------------------------------

    def Set(self, red, green, blue, alpha):
        '''
        Sets the RGB intensity values.
        '''
        self.ts_Alpha = alpha
        self.ts_Blue = blue
        self.ts_Green = green
        self.ts_Red = red

    #-----------------------------------------------------------------------

    def SetFromName(self, colourName):
        '''
        Sets the RGB intensity values using a colour name listed in
        wx.TheColourDatabase.
        '''
        theSymbol = colourName.lower()
        if theSymbol in list(tsGTUI.ExtendedColorDataBaseRGB.keys()):
            (red, green, blue) = tsGTUI.ExtendedColorDataBaseRGB[theSymbol]
        else:
            (red, green, blue) = (-1, -1, -1)

        self.ts_Alpha = wx.ALPHA_OPAQUE
        self.ts_Blue = blue
        self.ts_Green = green
        self.ts_Red = red

    #-----------------------------------------------------------------------

    @staticmethod
    def SetRGB(*args, **kwargs):
        '''
        SetRGB(self, unsigned long colRGB)
        '''
        if len(args) >= 2:
            self = args[0]

            try:
                # colRGB = '#RRGGBB
                colRGB = args[1]
                red = binascii.unhexlify(colRGB[1:2])
                green = binascii.unhexlify(colRGB[3:4])
                blue = binascii.unhexlify(colRGB[5:6])
                if 'alpha' in list(kwargs.keys()):
                    alpha = binascii.unhexlify(kwargs['alpha'])
                else:
                    alpha = wx.ALPHA_OPAQUE
            except Exception as e:
                self.logger.error('SetRGB in tsWxColor: %s' % e)
                (red, green, blue) = (-1, -1, -1)

            self.ts_Alpha = alpha
            self.ts_Blue = blue
            self.ts_Green = green
            self.ts_Red = red

    #-----------------------------------------------------------------------

    Pixel = property(GetPixel)
    RGB = property(GetRGB, SetRGB)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

##    nameFile = open('./namefile.py', 'w')
##    rgbFile = open('./rgbFile.py', 'w')
##    myColors = Color(0,0,0,0)
##    colorKeys = ColorListRGB.keys()
##    colorNames = sorted(colorKeys)
##    for color in colorNames:
##        name = color.lower()
##        rgb = ColorListRGB[color]
##        print("'%s' = %s" % (constant, name, rgb))
##        nameFile.write("%s = '%s',\n" % (constant, name))
##        rgbFile.write("%s = '%s',\n" % (constant, rgb))
##    nameFile.close()
##    rgbFile.close()
