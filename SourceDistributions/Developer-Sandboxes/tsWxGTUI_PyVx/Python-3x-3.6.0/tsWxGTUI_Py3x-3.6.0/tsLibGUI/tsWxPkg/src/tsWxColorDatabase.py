#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:28:02 AM rsg>"
'''
tsWxColorDatabase.py - Class to establish a database of standard
RGB colours for a predefined set of named colours (such as
"BLACK'', "LIGHT GREY"). The application may add to this set
if desired by using AddColour and may use it to look up colours
by names using Find or find the names for the standard colour
using FindName.
'''
#################################################################
#
# File: tsWxColorDatabase.py
#
# Purpose:
#
#    Class to establish a database of standard RGB colours for
#    a predefined set of named colours (such as "BLACK'',
#    "LIGHT GREY"). The application may add to this set if
#    desired by using AddColour and may use it to look up colours
#    by names using Find or find the names for the standard colour
#    using FindName.
#
# Usage (example):
#
#    # Import
#
#    from tsWxColorDatabase import ColorDatabase
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

__title__     = 'tsWxColorDatabase'
__version__   = '0.1.0'
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

##import tsExceptions as tse
##from tsReportUtilities import TsReportUtilities as tsru

import tsWxGlobals as wx
import tsWxColor as wxColor

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class ColorDatabase(object):
    '''
    wxPython maintains a database of standard RGB colours for a predefined
    set of named colours (such as "BLACK'', "LIGHT GREY"). The application
    may add to this set if desired by using AddColour and may use it to look
    up colours by names using Find or find the names for the standard colour
    using FindName.

    There is one predefined instance of this class called wxTheColourDatabase.

    The standard database contains at least the following colours:

    AQUAMARINE, BLACK, BLUE, BLUE VIOLET, BROWN, CADET BLUE, CORAL, CORNFLOWER
    BLUE, CYAN, DARK GREY, DARK GREEN, DARK OLIVE GREEN, DARK ORCHID, DARK
    SLATE BLUE, DARK SLATE GREY DARK TURQUOISE, DIM GREY, FIREBRICK, FOREST
    GREEN, GOLD, GOLDENROD, GREY, GREEN, GREEN YELLOW, INDIAN RED, KHAKI,
    LIGHT BLUE, LIGHT GREY, LIGHT STEEL BLUE, LIME GREEN, MAGENTA, MAROON,
    MEDIUM AQUAMARINE, MEDIUM BLUE, MEDIUM FOREST GREEN, MEDIUM GOLDENROD,
    MEDIUM ORCHID, MEDIUM SEA GREEN, MEDIUM SLATE BLUE, MEDIUM SPRING GREEN,
    MEDIUM TURQUOISE, MEDIUM VIOLET RED, MIDNIGHT BLUE, NAVY, ORANGE, ORANGE
    RED, ORCHID, PALE GREEN, PINK, PLUM, PURPLE, RED, SALMON, SEA GREEN,
    SIENNA, SKY BLUE, SLATE BLUE, SPRING GREEN, STEEL BLUE, TAN, THISTLE,
    TURQUOISE, VIOLET, VIOLET RED, WHEAT, WHITE, YELLOW, YELLOW GREEN.
    '''

    def __init__(self):
        '''
        Constructs the colour database. It will be initialized at the first
        use.
        '''
        theClass = 'ColorDatabase'

        wx.RegisterFirstCallerClassName(self, theClass)

##        Object.__init__(self)
##        try:
##            self.theFirstCallerName != theClass
##        except AttributeError:
##            self.theFirstCallerName = theClass

##        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        wxColor.TheUniqueDatabaseID = []
        theKeys = sorted(wxColor.ColorMapCurses.keys())
        for aKey in theKeys:
            aColor = wxColor.ColorMapCurses[aKey]
            try:
                (red, green, blue) = wxColor.ColorListRGB[aColor]
                theValues = '(%d, %d, %d)' % (red, green, blue)
                if aColor.find('9') == -1 and \
                   aColor.find('8') == -1 and \
                   aColor.find('7') == -1 and \
                   aColor.find('6') == -1 and \
                   aColor.find('5') == -1 and \
                   aColor.find('4') == -1 and \
                   aColor.find('3') == -1 and \
                   aColor.find('2') == -1 and \
                   aColor.find('1') == -1 and \
                   aColor.find('0') == -1 and \
                   not (aColor in wxColor.TheUniqueDatabaseID):
                    wxColor.TheUniqueDatabaseID += [aColor]
                    uniqueId = len(wxColor.TheUniqueDatabaseID)
                    theSymbol = aColor
                    theName = theSymbol.lower()
                    wxColor.TheCursesDataBase[theName] = uniqueId
                    wxColor.TheColourDatabase[theName] = (red, green, blue)
                    print('%30.30s = %15.15s # %3d "%s"' % (aColor,
                                                            theValues,
                                                            uniqueId,
                                                            theName))
            except Exception as e:
                msg = 'Exception %s' % e
                print(msg)

        theColors = sorted(wxColor.ColorListRGB.keys())
        for aColor in theColors:
            try:
                (red, green, blue) = wxColor.ColorListRGB[aColor]
                theValues = '(%d, %d, %d)' % (red, green, blue)
                if aColor.find('9') == -1 and \
                   aColor.find('8') == -1 and \
                   aColor.find('7') == -1 and \
                   aColor.find('6') == -1 and \
                   aColor.find('5') == -1 and \
                   aColor.find('4') == -1 and \
                   aColor.find('3') == -1 and \
                   aColor.find('2') == -1 and \
                   aColor.find('1') == -1 and \
                   aColor.find('0') == -1 and \
                   not (aColor in wxColor.TheUniqueDatabaseID):
                    wxColor.TheUniqueDatabaseID += [aColor]
                    uniqueId = len(wxColor.TheUniqueDatabaseID)
                    theSymbol = aColor
                    theName = theSymbol.lower()
                    wxColor.TheCursesDataBase[theName] = uniqueId
                    wxColor.TheColourDatabase[theName] = (red, green, blue)
                    print('%30.30s = %15.15s # %3d "%s"' % (aColor,
                                                            theValues,
                                                            uniqueId,
                                                            theName))
            except Exception as e:
                msg = 'Exception %s' % e
                print(msg)
 
##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def AddColour(self, name, colour):
        '''
        Adds a colour to the database. If a colour with the same name already
        exists, it is replaced.

        Please note that the overload taking a pointer is deprecated and will
        be removed in the next wxWidgets version, please do not use it.
        '''
        theSymbol = self.tsGetStandardizedColorName(name)
        (red, green, blue) = colour
        if theSymbol in wxColor.TheUniqueDatabaseID:
            # Replace red, green, blue intensities
            wxColor.TheColourDatabase[theSymbol] = (red, green, blue)
        else:
            # Append new name and red, green, blue intensities
            wxColor.TheUniqueDatabaseID += [theSymbol]
            wxColor.TheColourDatabase[theSymbol] = (red, green, blue)
            uniqueId = len(wxColor.TheColourDatabase)
            wxColor.TheCursesDataBase[theSymbol] = uniqueId

    #-----------------------------------------------------------------------

    def Append(self, name, red, green, blue):
        '''
        '''
        theSymbol = self.tsGetStandardizedColorName(name)
        if theSymbol in wxColor.TheUniqueDatabaseID:
            # Replace red, green, blue intensities
            wxColor.TheColourDatabase[theSymbol] = (red, green, blue)
        else:
            # Append new name and red, green, blue intensities
            wxColor.TheUniqueDatabaseID += [theSymbol]
            wxColor.TheColourDatabase[theSymbol] = (red, green, blue)
            uniqueId = len(wxColor.TheColourDatabase)
            wxColor.TheCursesDataBase[theSymbol] = uniqueId

    #-----------------------------------------------------------------------

    def Find(self, name):
        '''
        Finds a colour given the name. Returns an invalid colour object (that
        is, such that its Ok() method returns false) if the colour was not
        found in the database.
        '''
        theSymbol = self.tsGetStandardizedColorName(name)
        if theSymbol in wxColor.TheUniqueDatabaseID:
            # Prepare to return red, green, blue intensities
            (red, green, blue) = wxColor.TheColourDatabase[theSymbol]
            alpha = wx.ALPHA_OPAQUE
        else:
            # Prepare to return invalid red, green, blue intensities
            (red, green, blue) = (-1, -1, -1)
            alpha = -1
        return (wxColor.Color(red, green, blue, alpha))

    #-----------------------------------------------------------------------

    def FindColour(self, name):
        '''
        Finds a colour given the name. Returns an invalid colour object (that
        is, such that its Ok() method returns false) if the colour was not
        found in the database.
        '''
        theSymbol = self.tsGetStandardizedColorName(name)
        if theSymbol in wxColor.TheUniqueDatabaseID:
            # Prepare to return red, green, blue intensities
            (red, green, blue) = wxColor.TheColourDatabase[theSymbol]
            alpha = wx.ALPHA_OPAQUE
        else:
            # Prepare to return invalid red, green, blue intensities
            (red, green, blue) = (-1, -1, -1)
            alpha = -1
        return (wxColor.Color(red, green, blue, alpha))

    #-----------------------------------------------------------------------

    @staticmethod
    def FindName(colour):
        '''
        Finds a colour name given the colour. Returns an empty string if the
        colour is not found in the database.
        '''
        theName = ''
        for aColor in list(wxColor.TheColourDatabase.keys()):
            if wxColor.TheColourDatabase[aColor] == colour:
                theName = aColor
                msg = 'FindName in %s: theName = %s' % (__title__, theName)
                print('WARNING: %s' % msg)
                break
            else:
                pass
        return (theName)

    #----------------------------------------------------------------------
    # Begin tsWx API Extensions

    @staticmethod
    def tsGetStandardizedColorName(freeFormatName):
        '''
        '''
        done = False
        standardizedName = freeFormatName.lower()
        while not done:
            if standardizedName.find('  ') == -1:
                done = True
            else:
                standardizedName = standardizedName.replace('  ', ' ')
                msg1 = 'tsGetStandardizedColorName in %s: ' % __title__
                msg2 = 'freeFormatName = %s' % freeFormatName
                msg = msg1 + msg2
                print('WARNING: %s' % msg)
 
        return (standardizedName)

    # End tsWx API Extensions
    #----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

##    nameFile = open('./namefile.py', 'w')
##    rgbFile = open('./rgbFile.py', 'w')
##    colorKeys = RGB_Colors_wxPython.keys()
##    colorNames = sorted(colorKeys)
##    for color in colorNames:
##        constant = 'COLOR_' + color.replace(' ', '_')
##        name = color.lower()
##        rgb = RGB_Colors_wxPython[color]
##        print("%s = '%s'; %s" % (constant, name, rgb))
##        nameFile.write("%s = '%s',\n" % (constant, name))
##        rgbFile.write("%s = '%s',\n" % (constant, rgb))
##    nameFile.close()
##    rgbFile.close()
