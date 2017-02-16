#! /usr/bin/env python
# "Time-stamp: <04/08/2015  6:58:16 AM rsg>"
'''
tsWxStaticText.py - Class to establish a static text control
that displays one or more lines of read-only text.

wxStaticText supports the three classic text alignments, label
ellipsization and formatting markup.
'''
#################################################################
#
# File: tsWxStaticText.py
#
# Purpose:
#
#    Class to establish a static text control that displays one
#    or more lines of read-only text.
#
#    wxStaticText supports the three classic text alignments,
#    label ellipsization and formatting markup.
#
# Usage (example):
#
#    # Import
#
#    from tsWxStaticText import StaticText
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
#    2011/12/26 rsg Added logic to tsStaticTextLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxStaticText'
__version__   = '1.2.0'
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

#---------------------------------------------------------------------------

from textwrap import TextWrapper

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx
from tsWxGTUI_Py3x.tsLibGUI import tsWxGraphicalTextUserInterface as tsGTUI

from tsWxGTUI_Py3x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import EVT_SET_FOCUS
from tsWxGTUI_Py3x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py3x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py3x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class StaticText(Control):
    '''
    Class to establish a static text control that displays one or more
    lines of read-only text.

    wxStaticText supports the three classic text alignments, label
    ellipsization and formatting markup.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.StaticTextNameStr):
        '''
        Create a Control. Normally you should only call this from a subclass
        (_init__) as a plain old wx.Control is not very useful.
        '''
        theClass = 'StaticText'

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

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % self.Position)
            self.logger.debug('               size: %s' % self.Size)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('          validator: %s' % validator)
            self.logger.debug('               name: %s' % name)

        self.ts_Name = name
        self.ts_Parent = parent

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
        else:
            self.ts_GrandParent = parent.Parent

        self.ts_BackgroundColour = wx.ThemeToUse['BackgroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse['ForegroundColour'].lower()
        if False:
            # Facilitate differentiation of this panel from its parent by
            # transposing the parent's foreground and background colors.
            self.ts_BackgroundColour = self.ts_Parent.ts_ForegroundColour
            self.ts_ForegroundColour = self.ts_Parent.ts_BackgroundColour
        else:
            self.ts_BackgroundColour = self.ts_Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.ts_Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_TheWrapper = None

        self.ts_Name = name
        self.ts_ButtonText = label

        myRect, myClientRect = self.tsStaticTextLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        if True:
            self.tsShow()

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               label=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               name=wx.StaticTextNameStr,
               pixels=True):
        '''
        Do the 2nd phase and create the GUI Control.
        '''
        myRect, myClientRect = self.tsStaticTextLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Get the default attributes for this class.
        '''
        return (wx.WINDOW_VARIANT_NORMAL)

    #-----------------------------------------------------------------------

    def Wrap(self, width):
        '''
        This function wraps the control label so that each of its lines
        becomes at most width pixels wide if possible (the lines are broken
        at word boundaries so it might not be the case if words are too
        long). If width is negative, no wrapping is done.
        '''
        # TBD - Under Construction. Should this output or just format?
        expandTabs = True
        replaceWhitespace = True
        initialIndent = ''
        subsequentIndent = ''
        fixSentenceEndings = False
        breakLongWords = True

        self.ts_TheWrapper = TextWrapper(
            width = width - len(subsequentIndent),
            expand_tabs = expandTabs,
            replace_whitespace = replaceWhitespace,
            initial_indent = initialIndent,
            subsequent_indent = subsequentIndent,
            fix_sentence_endings = fixSentenceEndings,
            break_long_words = breakLongWords)

        controlLabel = self.GetLabel()

        theLines = self.ts_TheWrapper.wrap(controlLabel)
        maxRow = self.Rect.height // wx.pixelHeightPerCharacter
        maxCol = (self.Rect.width // wx.pixelWidthPerCharacter) - 1
        row = 0 + self.tsIsBorderThickness(style=self.ts_Style, pixels=False)
        col = 0 + self.tsIsBorderThickness(style=self.ts_Style, pixels=False)
        for aLine in theLines:
            if row < maxRow:
                # TBD - Verify the constraints against wxPython.
                self.tsCursesAddStr(
                    col, row, '%s' % aLine[0:min(len(aLine), maxCol - 1)],
                    attr=None, pixels=False)
            row += 1

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsShow(self):
        '''
        Create and update StaticText specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:

                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            label=self.ts_ButtonText,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.Name)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the StaticText.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd(' ', attr=None)
            self.tsCreateBorder()
            self.tsCreateLabel()

    #-----------------------------------------------------------------------

    def tsStaticTextLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of static text based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)
 
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        label = self.ts_Text

        if theSize == theDefaultSize:
            # theDefaultSize

            theLabelSize = theSize
            self.logger.debug(
                '      theLabelSize (begin): %s' % theLabelSize)

            if label is None:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(0, 0)
                self.logger.warning(
                    'theLabelSize: %s for None' % theLabelSize)
            elif label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(wx.pixelWidthPerCharacter,
                                      wx.pixelHeightPerCharacter)
            elif label.find('\n') == -1:
                # TBD - Remove adjustment for extra cursor width
                theLabelSize = wxSize(
                    (len(label) + 0) * wx.pixelWidthPerCharacter,
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
                    (maxWidth + 0) * wx.pixelWidthPerCharacter,
                    maxHeight * wx.pixelHeightPerCharacter)

            self.logger.debug(
                '      theLabelSize (end): %s' % theLabelSize)

            if thePosition == theDefaultPosition:
                # theDefaultPosition

                myRect = wxRect(parent.ClientRect.x,
                                parent.ClientRect.y,
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

                myRect = wxRect(parent.ClientRect.x,
                                parent.ClientRect.y,
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
        msg = 'parent=%s; pos=%s; size=%s; name=%s; label=%s; myRect=%s' % \
              (parent, pos, size, name, label, myRect)

        self.logger.debug('    tsStaticTextLayout: %s' % msg)

        return (myRect, myClientRect)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
