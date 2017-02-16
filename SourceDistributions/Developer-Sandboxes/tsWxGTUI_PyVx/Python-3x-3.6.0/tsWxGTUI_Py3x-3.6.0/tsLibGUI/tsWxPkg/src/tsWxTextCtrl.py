#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:51:26 AM rsg>"
'''
tsWxTextCtrl.py - Class to establish a text control that allows
text to be displayed and edited. It may be single line or
multi-line.

Notice that a lot of methods of the text controls are found in
the base wxTextEntry class which is a common base class for
wxTextCtrl and other controls using a single line text entry
field (e.g. wxComboBox).
'''
#################################################################
#
# File: tsWxTextCtrl.py

#
# Purpose:
#
#    Class to establish a text control that allows text to be
#    displayed and edited. It may be single line or multi-line.
#
#    Notice that a lot of methods of the text controls are found
#    in the base wxTextEntry class which is a common base class
#    for wxTextCtrl and other controls using a single line text
#    entry field (e.g. wxComboBox).
#
# Usage (example):
#
#    # Import
#
#    from tsWxTextCtrl import TextCtrl
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
#    2011/11/17 rsg Enhanced design so as to support a key word
#                   argument for curses-type text markup that
#                   enables the "blink", "bold", "normal",
#                   "reverse", "standout" and "underline"
#                   attributes for individual lines. It also
#                   supports changing each line's foreground
#                   and background color attributes.
#
#    2011/12/26 rsg Added logic to tsTextCtrlLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2011/12/30 rsg Added logic to AppendText to accept
#                   color markup only when terminal reports
#                   that it has colors.
#
#    2012/01/19 rsg Revised logic to restrict use of color
#                   features to those terminals that support
#                   color and exclude color features for
#                   non-color terminals such as vt100 and vt220.
#
#    2012/02/17 rsg Added self._tsLabel to save value parameter
#                   for access by self.tsCreateLabel. Added
#                   missing border thickness adjustments to
#                   AppendText.
#
# ToDo:
#
#    2011/11/18 rsg Enhance design so as to support appending,
#                   inserting and deleting text within a line.
#                   The current design, based on API document-
#                   ation, for wxPython 2.8.9.2, only appends
#                   new lines. This characteristic was only
#                   appropriate and used for the Redirected
#                   output window. There was no notion of
#                   support for the text editor applications
#                   referenced in wxWidgets 2.9.4 TextEntry.
#                   Might want to adopt such wxWidgets classes
#                   wxTextAttr and wxTextEntry instead of the
#                   markup key word argument.
#
#    2012/02/17 rsg Need to fix wrapping in AppendText. Portion
#                   of embedded new line (text1\ntext2' are not
#                   printed or properly indented. Som text also
#                   overwrites side border characters when running
#                   test_tsWxScrolled.py.
#
#################################################################

__title__     = 'tsWxTextCtrl'
__version__   = '1.7.0'
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

from textwrap import TextWrapper

import tsWxGlobals as wx
from tsWxEvent import EVT_COMMAND_LEFT_CLICK   # [Left Mouse]-Button Click
from tsWxEvent import EVT_SET_FOCUS
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

appendTextWrapEnable = True # False

#---------------------------------------------------------------------------

class TextCtrl(Control):
    '''
    Class to establish a text control that allows text to be displayed and
    edited. It may be single line or multi-line.

    Notice that a lot of methods of the text controls are found in the
    base wxTextEntry class which is a common base class for wxTextCtrl and
    other controls using a single line text entry field (e.g. wxComboBox).
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 value=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.TextCtrlNameStr):
        '''
        Create a Control. Normally you should only call this from a subclass
        (_init__) as a plain old wx.Control is not very useful.
        '''
        theClass = 'TextCtrl'

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
        self.caller_value = value
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
            self.logger.debug('              value: %s' % value)
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

        if False:

            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()

            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()

        elif  (self.tsCursesHasColors):

            self.ts_BackgroundColour = self.ts_Parent.ts_BackgroundColour

            self.ts_ForegroundColour = self.ts_Parent.ts_ForegroundColour

        else:

            self.ts_BackgroundColour = None

            self.ts_ForegroundColour = None

        self.ts_Style = style

        self.ts_Name = name
        self.ts_Label = value
        self.ts_Text = value
        self.ts_Row = 0
        self.ts_Col = 0
        self.ts_LineNumber = 0

        myRect, myClientRect = self.tsTextCtrlLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        if True:
            self.tsShow()

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_COMMAND_LEFT_CLICK
        handler = self.tsOnLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Create(self,
               parent,
               id=wx.ID_ANY,
               value=wx.EmptyString,
               pos=wx.DefaultPosition,
               size=wx.DefaultSize,
               style=0,
               name=wx.TextCtrlNameStr,
               pixels=True):
        '''
        Actually create the GUI TextCtrl for 2-phase creation.
        '''
        myRect, myClientRect = self.tsTextCtrlLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect
        myRect = self.tsGetRectangle(pos, size)

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def AppendText(self,
                   text,
                   breakLongWords=True,
                   expandTabs=True,
                   fixSentenceEndings=False,
                   initialIndent='',
                   markup=None,
                   newLine=True,
                   replaceWhitespace=False,
                   subsequentIndent='',
                   theLineNumberWidth=0,
                   topOfForm=False,
                   wrap=False):
        '''
        Appends the text argument to the end of the text in the control.
        The insertion point also moves to the end of the control.
        '''
        if topOfForm:

            self.ts_Col = 0 + \
                          self.tsIsBorderThickness(self.ts_Style,
                                                   pixels=False).width

            self.ts_Row = 0 + \
                          self.tsIsBorderThickness(self.ts_Style,
                                                   pixels=False).height
##            self.tsCursesAddStr(self.ts_Col,
##                                self.ts_Row,
##                                '',
##                                attr=None,
##                                pixels=False)
        elif newLine:

            self.ts_Col = 0 + \
                          self.tsIsBorderThickness(self.ts_Style,
                                                   pixels=False).width
##            self.tsCursesAddStr(self.ts_Col,
##                                self.ts_Row,
##                                '',
##                                attr=None,
##                                pixels=False)

        maxCols = (self.Rect.width // wx.pixelWidthPerCharacter) - 1
        maxRows = (self.Rect.height // wx.pixelHeightPerCharacter) - 1

        if wrap:

            theWidth = maxCols - theLineNumberWidth - \
                       2 * self.tsIsBorderThickness(self.ts_Style,
                                                    pixels=False).width

            theWrapper = TextWrapper(
                width=theWidth - len(subsequentIndent),
                expand_tabs=expandTabs,
                replace_whitespace=replaceWhitespace,
                initial_indent=initialIndent,
                subsequent_indent=subsequentIndent,
                fix_sentence_endings=fixSentenceEndings,
                break_long_words=breakLongWords)

            theLines = theWrapper.wrap(text)

        else:

            theLines = text.split('\n')

##        self.ts_Col = 0
        self.ts_Handle.scrollok(True)

        if (self.tsCursesHasColors):

            # Markup may have colors

            if (markup is None):

                # No Markup
                restoreBackgroundColour = self.GetBackgroundColour()
                restoreForegroundColour = self.GetForegroundColour()
                restoreAttributes = []
                setupAttributes = []

            else:

                restoreBackgroundColour = self.GetBackgroundColour()
                restoreForegroundColour = self.GetForegroundColour()

                attrRestoreColorPair = self.GetAttributeValueFromColorPair(
                    restoreForegroundColour,
                    restoreBackgroundColour)

                restoreAttributes = []
                setupAttributes = []

                try:
                    setupBackgroundColour = markup['Background']
                except KeyError:
                    setupBackgroundColour = restoreBackgroundColour

                try:
                    setupForegroundColour = markup['Foreground']
                except KeyError:
                    setupForegroundColour = restoreForegroundColour

                try:
                    setupAttributes = markup['Attributes']
                    restoreAttributes = setupAttributes
                    restoreAttributes.reverse()
                except KeyError:
                    restoreAttributes = []
                    setupAttributes = []

        else:

            # Markup maynot have colors
            restoreAttributes = []
            setupAttributes = []

            try:
                setupAttributes = markup['Attributes']
                restoreAttributes = setupAttributes
                restoreAttributes.reverse()
            except KeyError:
                restoreAttributes = []
                setupAttributes = []

        for aLine in theLines:
            self.ts_LineNumber += 1
            if False and DEBUG:
                msg = '%d %s' % (self.ts_LineNumber, aLine)
            else:
                msg = aLine

            self.logger.debug('AppendText: %s' % msg)

            if markup is None:

                # No Markup
                if newLine:

                    self.ts_Col = 0 + len(initialIndent) + \
                                  self.tsIsBorderThickness(self.ts_Style,
                                                           pixels=False).width

                if self.ts_Row < maxRows:
                    if newLine:
                        self.ts_Row += 1
                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=None,
                                        pixels=False)
                else:
                    if newLine:
                        self.tsCursesScroll()

                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=None,
                                        pixels=False)

                if not newLine:
                    self.ts_Col += len(msg)

            elif (self.tsCursesHasColors):

                # Markup may have colors
                if newLine:

                    self.ts_Col = 0 + len(initialIndent) + \
                                  self.tsIsBorderThickness(self.ts_Style,
                                                           pixels=False).width

                attrColorPair = self.GetAttributeValueFromColorPair(
                    setupForegroundColour,
                    setupBackgroundColour)

                attrMarkup = attrColorPair
                for attr in setupAttributes:
                    attrMarkup = attrMarkup | attr

                if self.ts_Row < maxRows:
                    if newLine:
                        self.ts_Row += 1

                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=attrMarkup,
                                        pixels=False)
                else:
                    if newLine:
                        self.tsCursesScroll()

                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=attrMarkup,
                                        pixels=False)

                if not newLine:
                    self.ts_Col += len(msg)

            else:

                # Markup maynot have colors
                if newLine:

                    self.ts_Col = 0 + len(initialIndent) + \
                                  self.tsIsBorderThickness(self.ts_Style,
                                                           pixels=False).width

                attrMarkup = 0
                for attr in setupAttributes:
                    attrMarkup = attrMarkup | attr

                if self.ts_Row < maxRows:
                    if newLine:
                        self.ts_Row += 1

                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=attrMarkup,
                                        pixels=False)
                else:
                    if newLine:
                        self.tsCursesScroll()

                    self.tsCursesAddStr(self.ts_Col,
                                        self.ts_Row,
                                        msg,
                                        attr=attrMarkup,
                                        pixels=False)

                if not newLine:
                    self.ts_Col += len(msg)

    #-----------------------------------------------------------------------

##bool  CanCopy(self)
##bool  CanCut(self)
##bool  CanPaste(self)
##bool  CanRedo(self)
##bool  CanUndo(self)
##      ChangeValue(self, value)

##    def Clear(self):
##        '''
##        Resets the text value of the control to "". Also generates a text
##        updated event.
##        '''
##        pass

##      Copy(self)
##bool  Create(self, parent, id, pos, size, style, validator, name)
##Do the 2nd phase and create the GUI control.
##      Cut(self)
##      DiscardEdits(self)

##    def EmulateKeyPress(self, event):
##        '''
##        Given a keypress event, inserts into the control the character
##        associated with the event, just as if the actual keypress had
##        occured
##        '''
##        return (False)

##VisualAttributes      GetClassDefaultAttributes(variant)
##Get the default attributes for this class. (Static method)

##    def GetDefaultStyle(self):
##        '''
##        '''
##        return (self.ts_Style)

##    def GetInsertionPoint(self):
##        '''
##        The position is the integer index of the current insertion point,
##        or to put it another way, the index where the next inserted
##        character would be placed. The beginning of the control is 0.
##        '''
##        return (-1)

##long  GetLastPosition(self)
##int   GetLineLength(self, lineNo)
##String        GetLineText(self, lineNo)
##int   GetNumberOfLines(self)

##    def GetRange(self, from, to):
##        '''
##        Return the string between the given integer positions of the output.
##        '''
##        return (text)

##    def GetSelection():
##        '''
##        Return a tuple (start, end) with the indexes of the currently
##        selected text. If the return values from and to are the same,
##        there is no selection.
##        '''
##        return (from, to)


##String        GetString(self, from, to)

##    def GetStringSelection(self):
##        '''
##        The position is the integer index of the current insertion point,
##        or to put it another way, the index where the next inserted
##        character would be placed. The beginning of the control is 0.
##        '''
##        return ('None')

##bool  GetStyle(self, position, style)

    #-----------------------------------------------------------------------

    def GetValue(self):
        '''
        '''
        if self.ts_Text is None:
            value = ''
        else:
            value = self.ts_Text
        return (value)

    #-----------------------------------------------------------------------

##(result, col, row)    HitTest(pt)
##Find the row, col coresponding to the character at the point given in pixels.
##(result, position)    HitTestPos(pt)
##Find the character position in the text coresponding to the point given in pixels.
##bool  IsEditable(self)
##bool  IsEmpty(self)
##bool  IsModified(self)
##bool  IsMultiLine(self)
##bool  IsSingleLine(self)
##bool  LoadFile(self, file, fileType)
##      MacCheckSpelling(self, check)
##      MarkDirty(self)
##      Paste(self)
##(x, y)        PositionToXY(pos)
##      Redo(self)
##      Remove(self, from, to)
##      Replace(self, from, to, value)
##bool  SaveFile(self, file, fileType)
##      SelectAll(self)
##      SendTextUpdatedEvent(self)

    #-----------------------------------------------------------------------

    def SetDefaultStyle(self, style):
        '''
        '''
        self.ts_Style = style
        return (True)

    #-----------------------------------------------------------------------
 
##      SetEditable(self, editable)

    #-----------------------------------------------------------------------

##    def SetInsertionPoint(self, pos):
##        '''
##        The position is the integer index of the current insertion point,
##        or to put it another way, the index where the next inserted
##        character would be placed. The beginning of the control is 0.
##        '''
##        pass

##    def SetInsertionPointEnd(self):
##        '''
##        The position is the integer index of the current insertion point,
##        or to put it another way, the index where the next inserted
##        character would be placed. The beginning of the control is 0.
##        '''
##        pass

##      SetMaxLength(*args, **kwargs)
##SetMaxLength(self, unsigned long len)
##      SetModified(self, modified)

##    def SetSelection(self, from, to
##bool  SetStyle(self, start, end, style)

    #-----------------------------------------------------------------------

    def SetValue(self, value):
        '''
        '''
        if self.ts_Text is None:
            self.ts_Text = ''
        else:
            self.ts_Text = value
        self.ts_Label = self.ts_Text

    #-----------------------------------------------------------------------

##      ShowPosition(self, pos)
##      Undo(self)

##    def write(self, text):
##        '''
##        '''
##        if True or text != wx.EmptyString:
##            self.WriteText(text)

##    def WriteText(self, text):
##        '''
##        Similar toAppendText() except that the new text is placed at the
##        current insertion point.
##        '''
##        self.logger.debug(
##            'WriteText: %s' % text)
##        self.tsCursesAddStr(2, 1, text)
##        self.Show()

##long  XYToPosition(self, x, y)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        if True or DEBUG:
            fmt1 = 'tsWxTextCtrl.tsOnLeftClick: '
            fmt2 = 'evt=%s' % str(evt)
            msg = fmt1 + fmt2

            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        targetObject = self.ts_Parent

##        results = self.tsProcessEventTables(
##            objectCriteria=self.ts_TriggeringCriteria,
##            objectId=objectId,
##            triggeringEvent=self.ts_TriggeringEvent,
##            triggeringObject=triggeringObject)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update TextCtrl specific native GUI.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is None:
                self.Create(self.Parent,
                            id=self.ts_AssignedId,
                            value=self.ts_Text,
                            pos=self.Position,
                            size=self.Size,
                            style=self.ts_Style,
                            name=self.Name,
                            pixels=True)

            try:
                self.tsRegisterShowOrder()
            except Exception as e:
                self.logger.error('%s; %s' % (__title__, e))

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsTextCtrlLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of button based upon arguments.
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

            if label is wx.EmptyString:
                # TBD - Adjust for cursor width
                theLabelSize = wxSize(wx.pixelWidthPerCharacter,
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

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + theBorder.height,
                              myRect.width - 2 * theBorder.width,
                              myRect.height - 2 * theBorder.height)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; label=%s; myRect=%s' % \
              (parent, pos, size, name, label, myRect)

        self.logger.debug('    tsTextCtrlLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the TextCtl.
        '''
        if self.tsIsShowPermitted:

            if self.ts_Handle is not None:

                self.tsCursesScrollOk(0)
                self.tsCursesBkgd()
                self.tsCreateBorder()
                self.tsCreateLabel()

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def Wrap(self, width):
        '''
        This function wraps the control value so that each of its lines
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

        theWrapper = TextWrapper(
            width = width - len(subsequentIndent),
            expand_tabs = expandTabs,
            replace_whitespace = replaceWhitespace,
            initial_indent = initialIndent,
            subsequent_indent = subsequentIndent,
            fix_sentence_endings = fixSentenceEndings,
            break_long_words = breakLongWords)

        controlLabel = self.GetLabel()

        theLines = theWrapper.wrap(controlLabel)
        maxRow = self.Rect.height // wx.pixelHeightPerCharacter
        maxCol = (self.Rect.width // wx.pixelWidthPerCharacter) - 1
        row = 0 + self.tsIsBorderThickness(style=self.ts_Style, pixels=False)
        col = 0 + self.tsIsBorderThickness(style=self.ts_Style, pixels=False)
        for aLine in theLines:
            if row < maxRow:
                # TBD - Verify the constraints against wxPython.
                self.tsCursesAddStr(
                    col, row, '%s' % aLine[0:min(len(aLine), maxCol - 1)])
            row += 1

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

##    DefaultStyle = property(GetDefaultStyle, SetDefaultStyle)
##    InsertionPoint = property(GetInsertionPoint, SetInsertionPoint)
##    LastPosition = property(GetLastPosition)
##    NumberOfLines = property(GetNumberOfLines)
##    Selection = property(GetSelection, SetSelection)
##    StringSelection = property(GetStringSelection)
##    Value = property(GetValue, SetValue)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
