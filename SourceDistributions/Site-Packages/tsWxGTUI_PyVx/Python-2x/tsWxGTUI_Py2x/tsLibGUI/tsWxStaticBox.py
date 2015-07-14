#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:19:22 AM rsg>"
'''
tsWxStaticBox.py - Class to establish a static box, a rectangle
drawn around other windows to denote a logical grouping of items.
'''
#################################################################
#
# File: tsWxStaticBox.py
#
# Purpose:
#
#    Class to establish a static box, a rectangle drawn around
#    other windows to denote a logical grouping of items.
#
# Usage (example):
#
#    # Import
#
#    from tsWxStaticBox import StaticBox
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
#    2011/12/26 rsg Added logic to tsStaticBoxLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2012/02/21 rsg Modified tsOnLeftClick to invoke
#                   tsProcessEventTables.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxStaticBox'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxControl import Control
from tsWxGTUI_Py2x.tsLibGUI.tsWxEvent import *
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class StaticBox(Control):
    '''
    Class to establish a static box,  a rectangle drawn around other windows
    to denote a logical grouping of items.
    '''
##    Note that while the previous versions required that windows appearing
##    inside a static box be created as its siblings (i.e. use the same parent
##    as the static box itself), since wxWidgets 2.9.1 it is also possible to
##    create them as children of wxStaticBox itself and you are actually
##    encouraged to do it like this if compatibility with the previous
##    versions is not important.

##    So the new recommended way to create static box is:

##            void MyFrame::CreateControls()
##            {
##                wxPanel *panel = new wxPanel(this);
##                wxStaticBox *box = new wxStaticBox(
##                                       panel, wxID_ANY, "StaticBox");

##                new wxStaticText(
##                    box, wxID_ANY "This window is a child of the staticbox");
##                ...
##            }

##    While the compatible -- and now deprecated -- way is

##                wxStaticBox *box = new wxStaticBox(
##                                       panel, wxID_ANY, "StaticBox");

##                new wxStaticText(
##                    panel, wxID_ANY "This window is a child of the panel");
##                ...

##    Also note that there is a specialized wxSizer class (wxStaticBoxSizer)
##    which can be used as an easier way to pack items into a static box.

    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.StaticBoxNameStr,
                 useClientArea = True):
        '''
        Create a Control. Normally you should only call this from a subclass
        (_init__) as a plain old wx.Control is not very useful.
        '''
        theClass = 'StaticBox'

        wx.RegisterFirstCallerClassName(self, theClass)

        Control.__init__(self,
                         parent,
                         id=id,
                         pos=pos,
                         size=size,
                         style=style,
                         validator=validator,
                         name=name)

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_validator = validator
        self.caller_name = name

        self.tsBeginClassRegistration(theClass, id)

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

        theTopLevelClass = parent
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
            # Inter-StaticBox spaces have same color as parent background.
            self.ts_BackgroundColour = self.Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.Parent.ts_ForegroundColour

        # Facilitate differentiation of this panel from its parent by
        # transposing the parent's foreground and background colors.
        if style == wx.BORDER_SUNKEN:

            self.ts_BackgroundColour = wx.COLOR_BLACK
            self.ts_ForegroundColour = wx.COLOR_WHITE

        elif style == wx.BORDER_RAISED:

            self.ts_BackgroundColour = wx.COLOR_WHITE
            self.ts_ForegroundColour = wx.COLOR_BLACK

        else:

            self.ts_BackgroundColour = self.ts_Parent.ts_BackgroundColour
            self.ts_ForegroundColour = self.ts_Parent.ts_ForegroundColour

        self.ts_Style = style

        self.ts_Label = label
        self.ts_StaticBoxText = self.tsStripAcceleratorTextLabel(label)

        self.ts_UseClientArea = useClientArea
        self.ts_Validator = validator

        (myRect, myClientRect) = self.tsStaticBoxLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=-1,
##               label=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               validator=wx.DefaultValidator,
               name=wx.ButtonNameStr,
               pixels=True):
        '''
        Create the GUI StaticBox for 2-phase creation.
        '''
##        if label == wx.EmptyString:
##            # Prevent pylint warning.
##            pass

        (myRect, myClientRect) = self.tsStaticBoxLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(self.ts_Rect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

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
        return (0)

    #-----------------------------------------------------------------------

##    TBD - Should be staticmethod
##    @staticmethod
    def GetDefaultSize(self):
        '''
        Returns the default StaticBox size for this platform.
        '''
        thickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=False)

        if False:
            width = (len(self.ts_StaticBoxText) + 1) * \
                    wx.pixelWidthPerCharacter

            height = (1) * wx.pixelHeightPerCharacter
        else:
            width = (thickness.width + \
                     len(self.ts_StaticBoxText) + 1) * \
                     wx.pixelWidthPerCharacter

            height = (thickness.height + 1) * wx.pixelHeightPerCharacter

        return (wxSize(width, height))

    #-----------------------------------------------------------------------

    def SetDefault(self):
        '''
        This sets the StaticBox to be the default item for the panel or
        dialog box.
        '''
        self.ts_Default = False

    #-----------------------------------------------------------------------

    def SetFocusIgnoringChildren(self):
        '''
        In contrast to SetFocus (see above) this will set the focus to
        the panel even of there are child windows in the panel.
        '''
        pass

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the StaticBox.
        '''
        myRect = self.ts_Rect

        (x, y, width, height) = (myRect.x,
                                 myRect.y,
                                 myRect.width,
                                 myRect.height)

        thickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=pixels)

        myClientRect = wxRect(
            (x + thickness.width),
            (y + thickness.height),
            (width - (2 * thickness.width)),
            (height - (2 * thickness.height)))

        self.ts_ClientRect = myClientRect

        if pixels:

            return (myClientRect)

        else:

            return (wxRect(
                (myClientRect.x // wx.pixelWidthPerCharacter),
                (myClientRect.y // wx.pixelWidthPerCharacter),
                (myClientRect.width // wx.pixelWidthPerCharacter),
                (myClientRect.height // wx.pixelWidthPerCharacter)))

    #-----------------------------------------------------------------------

    def tsStaticBoxLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
        '''
        if (not (self.ts_Handle is None)):

            # Inhibit operation once self.ts_Handle has been
            # assigned a curses window identifier.
            return (self.ts_Rect, self.ts_ClientRect)
 
        if style is None:
            # Prevent pylint warning.
            pass

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        # Ignore UseClientArea because cursor wraps beyond bottom
        # when last character has been output.
        offset = wxPoint(theBorder.width, theBorder.height)

        if thePosition == theDefaultPosition and \
             theSize == theDefaultSize:

            # The Default Position and the Parent's Default Client Size
            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            parent.ClientArea.width,
                            parent.ClientArea.height)

        elif thePosition == theDefaultPosition:

            # Parent's Default Client Position and the Specified Size
            myRect = wxRect(parent.ClientArea.x,
                            parent.ClientArea.y,
                            theSize.width,
                            theSize.height)

        else:

            # The Specified Position and the Specified Size

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

        myClientRect = wxRect((myRect.x + offset.x),
                              (myRect.y + offset.y),
                              (myRect.width - (2 * offset.x)),
                              (myRect.height - (2 * offset.y)))

        msg = 'parent=%s; pos=%s; size=%s; name=%s; myRect=%s' % \
              (parent, pos, size, name, myRect)

        self.logger.debug('    tsStaticBoxLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxScrolledWindow.' +\
              'tsOnLeftClick'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        triggeringObject = self
 
##        if self.GetLabel().find('CloseButton') > -1:

##            print('EVT_CLOSE for [X]-Button')
##            triggeringEvent = EVT_CLOSE

##        elif self.GetLabel().find('HelpButton') > -1:

##            print('EVT_HELP for [?]-Button')
##            triggeringEvent = EVT_HELP

##        elif self.GetLabel().find('MaximizeButton') > -1:

##            print('EVT_MAXIMIZE for [Z]-Button')
##            triggeringEvent = EVT_MAXIMIZE

##        elif self.GetLabel().find('MinimizeButton') > -1:

##            print('EVT_ICONIZE for [_]-Button')
##            triggeringEvent = EVT_ICONIZE

##        elif self.GetLabel().find('RestoreButton') > -1:

##            print('EVT_MAXIMIZE for [z]-Button')
##            triggeringEvent = EVT_MAXIMIZE

##        else:

##            print('EVT_COMMAND_LEFT_CLICK for [%s]-Button' % self.GetLabel())
##            triggeringEvent = EVT_COMMAND_LEFT_CLICK

##        triggeringEvent = EVT_COMMAND_LEFT_CLICK

##        triggeringObject.ProcessEvent(triggeringEvent)

##        results = self.tsProcessEventTables(
##            objectCriteria=objectCriteria,
##            objectId=objectId,
##            triggeringEvent=triggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update StaticBox specific native GUI.
        '''
        if self.tsIsShowPermitted:

            print('tsWxStaticBox.tsShow: Handle=%s' % str(self.ts_Handle))
            if self.ts_Handle is None:

                self.Create(self.ts_Parent,
                            id=self.ts_AssignedId,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.ts_Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception, e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the StaticBox.
        '''
        if self.tsIsShowPermitted:

            print('tsWxStaticBox.tsUpdate: Handle=%s' % str(self.ts_Handle))
            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()
                self.tsCreateLabel()

        return (self.ts_Handle is not None)

    # End tsWx API Extensions
    #-----------------------------------------------------------------------
    ClientArea = property(tsGetClientArea)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
