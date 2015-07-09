#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:49:26 AM rsg>"
'''
tsWxSlider.py - Class to establish a control with a handle which
can be pulled back and forth to change the value.
'''
#################################################################
#
# File: tsWxSlider.py
#
# Purpose:
#
#    Class to establish a control with a handle which can be
#    pulled back and forth to change the value.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSlider import Slider as wxSlider
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
#    2011/12/26 rsg Added logic to tsSliderLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxSlider'
__version__   = '1.1.0'
__date__      = '07/18/2013'
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
from tsWxControl import Control
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Slider(Control):
    '''
    Class to establish a control with a handle which can be pulled back
    and forth to change the value. On Windows, the track bar control is used.

    Slider events are handled in the same way as a scrollbar.
 
    Create a Control. Normally you should only call this from a subclass
    __init__ as a plain old wx.Control is not very useful.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 value=0,
                 minValue=0,
                 maxValue=100,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.SL_HORIZONTAL,
                 validator=wx.DefaultValidator,
                 name=wx.SliderNameStr):
        '''
        Create a Control. Normally you should only call this from a
        subclass __init__ as a plain old wx.Control is not very useful.
        '''
        theClass = 'Slider'

        # TBD - Set default label
        label = None

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         validator=validator,
                         name=name)

        self.tsBeginClassRegistration(theClass, id)

        # TBD - Set default label
        label = None

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % str(pos))
            self.logger.debug('               size: %s' % str(size))
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Default = False

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        if False:
            # Leaves artifacts of different color than parent background.
            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()
        else:
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_ButtonText = label
        self.ts_Label = label
        self.ts_Validator = validator
        self.ts_Value = False

        myRect, myClientRect = self.tsSliderLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.tsEndClassRegistration(theClass)

    def Create(self,
               parent,
               id=wx.ID_ANY,
               value=0,
               minValue=0,
               maxValue=100,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=wx.SL_HORIZONTAL,
               validator=wx.DefaultValidator,
               name=wx.SliderNameStr,
               pixels=True):
        '''
        Create the GUI Button for 2-phase creation.
        '''
        myRect, myClientRect = self.tsSliderLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class. This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignored under other platforms. Under Mac, it will change the size of
        the returned font. See wx.Window.SetWindowVariant for more about this.
        '''
        pass

    def GetValue(self):
        '''
        TBD - Under Construction.
        '''
        return (self.ts_Value)

    def SetValue(self, value):
        '''
        TBD - Under Construction.
        '''
        if self.ts_Value == value:
            self.ts_Value = value

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsSliderLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        label = self.ts_Label

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[]')) * wx.pixelWidthPerCharacter,
                    wx.pixelHeightPerCharacter)

            elif label.find('\n') == -1:
                # TBD - Remove adjustment for extra cursor width
                theLabelSize = wxSize(
                    (len(label) + len('[ ]')) * wx.pixelWidthPerCharacter,
                    wx.pixelHeightPerCharacter)
            else:
                # TBD - Remove adjustment for extra cursor width
                theLines = label.split('\n')
                maxWidth = 0
                maxHeight = len(theLines)
                for aLine in theLines:
                    if len(aLine) > maxWidth:
                        maxWidth = len(aLine)
                theLabelSize = wxSize(
                    (maxWidth + len('[ ]')) * wx.pixelWidthPerCharacter,
                    maxHeight * wx.pixelHeightPerCharacter)

            self.logger.debug(
                '      theLabelSize (end): %s' % theLabelSize)

            if thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theLabelSize.width,
                                theLabelSize.height)

            else:
                # Not theDefaultPosition

                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theLabelSize.width,
                                theLabelSize.height)

        else:
            # Not theDefaultSize

            if thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theSize.width,
                                theSize.height)

            else:
                # Not theDefaultPosition

                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theSize.width,
                                theSize.height)

##        theDisplayRect = self.Display.GetClientArea()
##        if not theDisplayRect.InsideRect(myRect):
##            myRect = wxRect(
##                max(thePosition.x, theDisplayRect.x),
##                max(thePosition.y, theDisplayRect.y),
##                min(theSize.width, theDisplayRect.width),
##                min(theSize.height, theDisplayRect.height - 1))

##        if not theDisplayRect.InsideRect(myRect):
##            myRect = theDisplayRect

        myClientRect = wxRect(myRect.x,
                              myRect.y,
                              myRect.width,
                              myRect.height)

        self.tsTrapIfTooSmall(name, myRect)
        fmt = 'parent=%s; pos=%s; size=%s; ' + \
              'name="%s"; label="%s"; myRect=%s'
        msg = fmt % (parent, str(pos), str(size), name, label, str(myRect))

        self.logger.debug('    tsSliderLayout: %s' % msg)

        return (myRect, myClientRect)

    def tsShow(self):
        '''
        Create and update Button specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            label=self.ts_Label,
                            pos=self.ts_Rect.Position,
                            size=self.ts_Rect.Size,
                            style=self.ts_Style,
                            validator=self.ts_Validator,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    def tsUpdate(self):
        '''
        Draw the actual features of the Button.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            self.tsCreateBorder()
            self.tsCreateButton()

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    Value = property(GetValue, SetValue)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
