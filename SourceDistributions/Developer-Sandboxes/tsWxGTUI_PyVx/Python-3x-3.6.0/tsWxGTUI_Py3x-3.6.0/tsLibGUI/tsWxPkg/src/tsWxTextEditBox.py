#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:52:07 AM rsg>"
'''
tsWxTextEditBox.py - Class represents that portion of a dialog
that requests and edits a single or multi-line text string from
the user.
'''
#################################################################
#
# File: tsWxTextEditBox.py
#
# Purpose:
#
#    Class represents that portion of a dialog that requests and
#    edits a single or multi-line text string from the user.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTextEditBox import TextEditBox
#
# Requirements:
#
#    Operator Interface:
#
#        Input is entered via terminal keyboard. It is received
#        on an event driven basis. The operator may enter ASCII
#        data via any alphabetic, numeric or punctuation character.
#        Alphabetic characters may be in upper or lower case.
#        The operator may enter editing control commands via
#        selected ASCII control characters or via associated
#        editing keys.
#
#        Output is displayed via terminal display. It is updated
#        on an event driven basis. Text may optionally be masked
#        (i.e., displayed as asterisks) when appropriate for
#        password mode. The editing may automatically wrap text
#        to fit the available display.
#
#        Cursor (caret) is to be displayed as operator prompt.
#        It is to be programmatically positioned at the column
#        and row associated with the next keyboard input.
#
#    Application Interface:
#
#         Operator Input is accumulated in a buffer. The contents
#         of the full or empty buffer is delivered upon receipt of
#         a complete or cancel event notification.
#
# Capabilities:
#
#    Operator input is organized as an editable list of characters.
#    Insertions and deletions may be made before or after any
#    buffered character.
#
#    The editing control characters are those typically associated
#    with the Emacs text editor. The editing keys are mapped to
#    the equivalent editing control characters.
#
#    The text wrapper converts the text associated with a single
#    paragraph so that every line fits within the display. It
#    returns a list of output lines, without final newlines.
#
#    The layout utility organizes a copy of the operator input
#    buffer into a line by line list of character strings to be
#    displayed.
#
#    The offset to cursor map utility provides display column and
#    row coordinates for each operator input character.
#
#    The cursor to offset map utility identifies the insertion or
#    deletion location in the list of operator input characters
#    from the associated display column and row coordinates.
#
# Limitations:
#
#    The design and implementation assumes use of ASCII characters.
#
# Notes:
#
#    None
#
# Methods:
#
#    __init__
#    do_command
#    edit
#    gather
#    tsConvertCursor2CursorDictKey
#    tsConvertCursor2Offset
#    tsConvertCursorDictKey2Cursor
#    tsConvertOffset2Cursor
#    tsGetCompletion
#    tsGetConstrainedAnticipatedNextCursorPosition
#    tsGetConstrainedCursorPosition
#    tsGetConstrainedTextCharacterBufferOffset
#    tsGetLabel
#    tsGetPasswordMode
#    tsGetStripSpaces
#    tsInsertKeystrokeDataKey
#    tsLayoutLineBuffer
#    tsOnControl_A
#    tsOnControl_B
#    tsOnControl_D
#    tsOnControl_E
#    tsOnControl_F
#    tsOnControl_G
#    tsOnControl_H
#    tsOnControl_I
#    tsOnControl_J
#    tsOnControl_K
#    tsOnControl_L
#    tsOnControl_N
#    tsOnControl_O
#    tsOnControl_P
#    tsOnKeyBackSpace
#    tsOnKeyDC
#    tsOnKeyDown
#    tsOnKeyEnd
#    tsOnKeyEnter
#    tsOnKeyHome
#    tsOnKeyLeft
#    tsOnKeyNpage
#    tsOnKeyPpage
#    tsOnKeyRight
#    tsOnKeyUp
#    tsOnReset
#    tsOnTextEntryFromKbd
#    tsSetCompletion
#    tsSetConstrainedAnticipatedNextCursorPosition
#    tsSetConstrainedCursorPosition
#    tsSetConstrainedTextCharacterBufferOffset
#    tsSetLabel
#    tsSetPasswordMode
#    tsSetStripSpaces
#    tsTextCtrlLayout
#    tsUpdateCursor
#    tsUpdateDisplay
#
# Classes:
#
#    TextEditBox
#
# Modifications:
#
#    2012/07/21 rsg Added TextEditBox class and associated
#                   methods.
#
#    2012/07/28 rsg Added evt argument to each tsOn<event>.
#
#    2012/08/01 rsg Started improvement of algorithms,
#                   variable names and parameter passing.
#
#                   Successful with simplest of editing insertions
#                   and deletions associated with character buffer.
#
#                   Revised algorithms to track and apply line buffer
#                   layout changes associated with text wrapping.
#
#                   Added Set and Get methods to change and retrieve:
#                       ts_TextCharacterBufferOffset,
#                       ts_CurrentCursorPosition, and
#                       ts_AnticipatedNextCursorPosition.
#                   These methods eliminate the need for any calling
#                   method to replicate logic to test and constrain
#                   each data value to be within its associated valid
#                   range.
#
#                   Improved built-in diagnostics which eliminated
#                   the need for any calling method to replicate
#                   logic to gather, format and output the "data base"
#                   containing the initial and final state for each
#                   input, editing and output activity.
#
#                   Re-designed tsLayoutLineBuffer, tsOnControl_B,
#                   tsOnControl_D, tsOnControl_F and tsOnControl_K to
#                   use the operator controlled cursor position and
#                   corrected synchronization with the character buffer
#                   offset to achieve the operator expected backward and
#                   forward deletions of one or more characters.
#
#                   Added methods tsConvertCursor2CursorDictKey and
#                   tsConvertCursor2Offset to encode and decode
#                   Cursor into and from CursorDictKey becasue Python's
#                   dictionary keys its dictionary entries by a hash
#                   code. The consequence being that different instances
#                   of wxPoint(0, 0) became individual keys which
#                   screwed up the cursor to offset mapping.
#
#                   Converted the TextCharacterBuffer from an ordinary
#                   list of single character strings to a class with
#                   methods for randomly or sequentially populating,
#                   accessing and de-populating a simple, non-linked
#                   list of user defined objects. The Application
#                   Programming Interface of this NonLinkedList class
#                   emulated that of the DoubleLinkedList class to
#                   facilitate a future enhancement. Initially it was
#                   implemented as an internal class that later became
#                   an external one to facilitate separate maintenance.
#                   The primary limitation of an ordinary list is its
#                   dependency on application-level local logic to
#                   whether insertions take place before or after the
#                   application specified user defined object index.
#
#                   Still need a mechanism to block application until
#                   operator has completed the input and editing.
#
#    2012/10/08 rsg Not Finished improvements of algorithms, parameter
#                   passing, variable names and comments.
#
# ToDo:
#
#    2012/08/06 rsg Investigate why TextEditBox.tsOnLeftClick
#                   fails to be triggered by mouse. Log registers
#                   that TextEditBox received trigger.
#
#    2012/09/18 rsg Resolve why block cursor (wx.caretVeryVisible)
#                   is active and cannot be programmatically changed.
#
#    2012/09/23 rsg Investigate why tsDumpTextEditBoxDataBase
#                   sometimes reports requestor as 'callerName'
#                   instead of real name. This seems to happen
#                   when operator event driven input data is
#                   being processed by tsInsertKeystrokeDataKey.
#                   For example after entering '0123456789').
#                   Other requests work as do all invocations
#                   of tsDumpTextEditBoxCheckPoint which uses
#                   the identical invocation and processing
#                   algorithm.
#
#    2012/09/27 rsg Investigate why trap occurs when
#                   self.ts_AnticipatedNextCursorPosition is
#                   adjusted to beginning of next line after
#                   operator inserted a new line.
#
#################################################################

__title__     = 'tsWxTextEditBox'
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

##import copy
import textwrap

import tsExceptions as tse
##import tsLogger

import tsWxGlobals as wx

# from tsWxBoxSizer import BoxSizer as wxBoxSizer
# from tsWxButton import Button as wxButton
# from tsWxDialog import Dialog
# from tsWxPanel import Panel as wxPanel
# from tsWxStaticLine import StaticLine as wxStaticLine

from tsWxEvent import EVT_CHAR
from tsWxEvent import EVT_COMMAND_LEFT_CLICK   # [Left Mouse]-Button Click
from tsWxEvent import EVT_COMMAND_RIGHT_CLICK  # [Right Mouse]-Button Click
from tsWxEvent import EVT_SET_FOCUS
##from tsWxPanel import Panel as wxPanel
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxTextCtrl import TextCtrl as wxTextCtrl

from tsWxGraphicalTextUserInterface import KeyCodes as wxKeyCodes

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DUMMY_CURSOR = wxPoint(-1, -1)
KEY_NAMES = wxKeyCodes
NEW_LINE_CHARACTER = 0x0a
RESET_CHARACTER = 0 # curses.ascii.NUL
RESET_CHARACTER_NAME = '<Ctrl-Shift-2>'

USE_CONSTRAIN_CURSOR = False # True
USE_CONSTRAIN_OFFSET = False # True
USE_CURSOR_DICT_KEY  = True
USE_DOUBLE_LINKED_LIST = False # True

if USE_DOUBLE_LINKED_LIST:

    from tsWxDoubleLinkedList import DoubleLinkedList as wxLinkedUserDataList

else:

    from tsWxNonLinkedList import NonLinkedList as wxLinkedUserDataList

USE_PYLINT_ATTRIBUTE_WARNINGS = False # True = Initialize via Command Reset

#---------------------------------------------------------------------------

class TextEditBox(wxTextCtrl):
    '''
    A TextEditBox is a window on which controls are placed. It is usually
    placed within a dialog. Its main feature over its parent class TextCtrl
    is code for handling text input and editing.

    # TextEditBox objects have the following methods:

    #-----------------------------------------------------------------------
    #
    #     edit([validator])
    #
    #     This is the entry point you will normally use. It accepts editing
    #     keystrokes until one of the termination keystrokes is entered. If
    #     validator is supplied, it must be a function. It will be called for
    #     each keystroke entered with the keystroke as a parameter; command
    #     dispatch is done on the result. This method returns the window
    #     contents as a string; whether blanks in the window are included
    #     is affected by the stripspaces member.
    #
    #-----------------------------------------------------------------------
    #
    #     do_command(ch)
    #
    #     Process a single command keystroke. Here are the supported special
    #     keystrokes:
    #
    #         Keystroke Action
    #         ========= ===================================================
    #         Control-@ Cancel (Erase) Input upon Control-Shift-2
    #         Control-A Move cursor to left edge of window.
    #         Control-B Cursor left, wrapping to previous line if appropriate.
    #         Control-D Delete character under cursor.
    #         Control-E Move cursor to right edge (stripspaces off) or end
    #                   of line (stripspaces on).
    #         Control-F Cursor right, wrapping to next line when appropriate.
    #         Control-G Terminate, returning the window contents.
    #         Control-H Delete character backward.
    #         Control-I Horizontal Tab.
    #         Control-J Terminate if the window is 1 line, otherwise insert
    #                   newline.
    #         Control-K If line is blank, delete it, otherwise clear to end
    #                   of line.
    #         Control-L Refresh screen.
    #         Control-N Cursor down; move down one line.
    #         Control-O Insert a blank line at cursor location.
    #         Control-P Cursor up; move up one line.
    #
    #     Move operations do nothing if the cursor is at an edge where the
    #     movement is not possible.
    #
    #     The following synonyms are supported  where possible:
    #
    #         Constant      Keystroke
    #         ============= =========
    #         KEY_BACKSPACE Control-H
    #         KEY_DOWN      Control-N
    #         KEY_ENTER     Control-J
    #         KEY_LEFT      Control-B
    #         KEY_RIGHT     Control-F
    #         KEY_HTAB      Control-I
    #         KEY_UP        Control-P
    #         KEY_NPAGE     Control-N
    #         KEY_PPAGE     Control-P
    #
    #     All other keystrokes are treated as a command to insert the given
    #     character and move right (with line wrapping).
    #
    #-----------------------------------------------------------------------
    #
    #     gather()
    #
    #     This method returns the window contents as a string; whether blanks
    #     in the window are included is affected by the stripspaces member.
    #
    #-----------------------------------------------------------------------
    #
    #     stripspaces
    #
    #     This data member is a flag which controls the interpretation of
    #     blanks in the window. When it is on, trailing blanks on each line
    #     are ignored; any cursor motion that would land the cursor on a
    #     trailing blank goes to the end of that line instead, and trailing
    #     blanks are stripped when the window contents are gathered.
    #
    #-----------------------------------------------------------------------
    #
    # Until event drive features are perfected, design provides option to
    # use non-event driven nCurses textpad feature:
    #
    #     Return a textbox widget object. The win argument should be a curses
    #     WindowObject in which the textbox is to be contained. The edit
    #     cursor of the textbox is initially located at the upper left hand
    #     corner of the containing window, with coordinates (0, 0). The
    #     instances stripspaces flag is initially on.
    #
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_TEXTEDITBOX_STYLE,
                 name=wx.TextEditBoxNameStr):
        '''
        Construct and show a generic TextEditBox.
        '''
        theClass = 'TextEditBox'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_label = None # label
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        if parent is None:

            # Top Level Windows (Frames & Dialogs) have no parent
            panelPos = pos
            panelSize = size

        else:

            parentClientArea = parent.ClientArea
            if pos == wx.DefaultPosition:
                panelPos = wxPoint(parentClientArea.x,
                                   parentClientArea.y)
            else:
                panelPos = pos

            if size == wx.DefaultSize:
                panelSize = wxSize(parentClientArea.width,
                                   parentClientArea.height)
            else:
                panelSize = size

        wxTextCtrl.__init__(
            self,
            parent,
            id=id,
            pos=panelPos,
            size=panelSize,
            style=style,
            name=name)

        self.tsBeginClassRegistration(theClass, id)

        (myRect, myClientRect) = self.tsTextCtrlLayout(
            parent, panelPos, panelSize, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        if DEBUG and VERBOSE:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              label: %s' % label)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Label = label
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

        #-------------------------------------------------------------------

        self.ts_Style = style

        self.ts_Completion = False

        self.ts_CursorMode = True

        self.ts_PasswordMode = False

        self.ts_StripSpaces = False

        self.ts_Validator = None

        #-------------------------------------------------------------------
        # Ord Keystroke Action

        self.KeystrokeAction = {
            0: self.tsOnReset,          # Cancel (Erase) Input for Control_@
            1: self.tsOnControl_A,      # Move Cursor Left Side (<- Backward)
            2: self.tsOnControl_B,      # Move Cursor Left (<- Backward)
            4: self.tsOnControl_D,      # Delete Next Character (-> Forward)
            5: self.tsOnControl_E,      # Move Cursor Right Side (-> Forward)
            6: self.tsOnControl_F,      # Move Cursor Right (-> Forward)
            7: self.tsOnControl_G,      # Terminate, return contents
            8: self.tsOnControl_H,      # Delete Prev. Character (<- Backward)
            9: self.tsOnControl_I,      # Horizontal Tab Character (-> Tab)
            10: self.tsOnControl_J,     # Terminate or Insert New Line
            11: self.tsOnControl_K,     # Delete Line or String to End of Line
            12: self.tsOnControl_L,     # Refresh Screen
            14: self.tsOnControl_N,     # Move Cursor Down (v Downward)
            15: self.tsOnControl_O,     # Insert Blank Line
            16: self.tsOnControl_P,     # Move Cursor Up (^ Upward)
            258: self.tsOnKeyDown,      # Move Cursor Down (v Downward)
            259: self.tsOnKeyUp,        # Move Cursor Up (^ Upward)
            260: self.tsOnKeyLeft,      # Move Cursor Left (<- Backward)
            261: self.tsOnKeyRight,     # Move Cursor Right (-> Forward)
            262: self.tsOnKeyHome,      # Move Cursor Left Side (<- Backward)
            263: self.tsOnKeyBackSpace, # Delete Prev. Character (<- Backward)
            330: self.tsOnKeyDC,        # Delete Next Character (-> Forward)
            338: self.tsOnKeyNpage,     # Move Cursor Down (v Downward)
            339: self.tsOnKeyPpage,     # Move Cursor Up (^ Upward)
            343: self.tsOnKeyEnter,     # Terminate or Insert New Line
            360: self.tsOnKeyEnd        # Move Cursor Right Side (-> Forward)
            }

        self.KeystrokeActionKeys = list(self.KeystrokeAction.keys())

        #-------------------------------------------------------------------
        # Two-dimensional (Operator/Application) view of Edit Buffer

        # Convert dimension from pixel to character cell units
        (self.ts_MaxCols, self.ts_MaxRows) = wx.tsGetCharacterValues(
            self.ts_ClientRect.width, self.ts_ClientRect.height)

        self.ts_MaxCapacity = (self.ts_MaxCols * self.ts_MaxRows)

        self.ts_TextCharacterBufferLimit = wxPoint(self.ts_MaxCols - 1,
                                                   self.ts_MaxRows - 1)

        if DEBUG and VERBOSE:
            fmt1 = 'tsWxTextEditBox.__init__: ' + \
                   'myRect=%s; myClientRect=%s; ' % (
                       str(myRect), str(myClientRect))
            fmt2 = 'maxCols=%d; maxRows=%d; maxCapacity=%d' % (
                self.ts_MaxCols, self.ts_MaxRows, self.ts_MaxCapacity)
            msg = fmt1 + fmt2
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)
 
        #-------------------------------------------------------------------
        # Configure Text Wrapper Instance

        if self.ts_PasswordMode:

            # PasswordMode = True
            #
            # These parameters force self.tsLayoutLineBuffer to
            # represent the contents of self.ts_TextCharacterBuffer
            # in the Offset2CursorMap and in self.ts_Cursor2OffsetMap.
            thisWidth = self.ts_MaxCols
            thisInitialIndent = ''         # Changes break mapping
            thisSubsequentIndent = ''      # Changes break mapping
            thisExpandTabs = False         # Changes break mapping
            thisReplaceWhitespace = False  # Changes break mapping
            thisFixSentenceEndings = False # Changes break mapping
            thisBreakLongWords = True      # Changes break mapping
            thisDropWhiteSpace = False     # Changes break mapping
            thisBreakOnHyphens = False     # Changes break mapping

        elif self.ts_CursorMode:

            # CursorMode = True.
            #
            # These parameters force self.tsLayoutLineBuffer to
            # represent the contents of self.ts_TextCharacterBuffer
            # in the Offset2CursorMap and in self.ts_Cursor2OffsetMap.
            thisWidth = self.ts_MaxCols
            thisInitialIndent = ''         # Changes break mapping
            thisSubsequentIndent = ''      # Changes break mapping
            thisExpandTabs = False         # Changes break mapping
            thisReplaceWhitespace = False  # Changes break mapping
            thisFixSentenceEndings = False # Changes break mapping
            thisBreakLongWords = True      # Changes break mapping
            thisDropWhiteSpace = False     # Changes break mapping
            thisBreakOnHyphens = False     # Changes break mapping

        else:

            # Experimental Mode
            #
            # These parameters do NOT force self.tsLayoutLineBuffer to
            # represent the contents of self.ts_TextCharacterBuffer
            # in the Offset2CursorMap and in self.ts_Cursor2OffsetMap.
            # This leaves gaps in the mapping that precipitate Traps.
            thisWidth = self.ts_MaxCols
            thisInitialIndent = ''
            thisSubsequentIndent = ''
            thisExpandTabs = True
            thisReplaceWhitespace = True
            thisFixSentenceEndings = True
            thisBreakLongWords = True
            thisDropWhiteSpace = True
            thisBreakOnHyphens = True

        self.tsTextWrapper = textwrap.TextWrapper(
            width=thisWidth,
            initial_indent=thisInitialIndent,
            subsequent_indent=thisSubsequentIndent,
            expand_tabs=thisExpandTabs,
            replace_whitespace=thisReplaceWhitespace,
            fix_sentence_endings=thisFixSentenceEndings,
            break_long_words=thisBreakLongWords,
            drop_whitespace=thisDropWhiteSpace,
            break_on_hyphens=thisBreakOnHyphens)

        self.tsTextWrap = self.tsTextWrapper.wrap

        if USE_PYLINT_ATTRIBUTE_WARNINGS:

            # Identify those state variable attributes used by the text
            # editor that trigger pylint warning that their initial values
            # have been defined outside the __init__ method, by the
            # tsOnReset method.

            # Pre-define state variable attributes as if operator issued
            # the Reset Command.
            self.tsOnReset(RESET_CHARACTER)

        else:

            # Pre-define state variable attributes used by the text editor
            # to avoid the pylint warning that their initial values have
            # been defined outside the __init__ method, by the tsOnReset
            # method.

            # Editable list of characters
            self.ts_TextCharacterBuffer = wxLinkedUserDataList()

            # Character insert/delete index
            self.ts_TextCharacterBufferOffset = 0

            # Displayable list of text strings
            self.ts_TextLineBuffer = []

            # Line insert/delete index
            self.ts_TextLineBufferIndex = []

            # Maps Cursor to Offset
            self.ts_TextBufferCursor2OffsetMap = {}

            # Maps Offset to Cursor
            self.ts_TextBufferOffset2CursorMap = {}

            # Anticipated Next Cursor Position
            self.ts_AnticipatedNextCursorPosition = wxPoint(0, 0)

            # Cursor Position
            self.ts_CursorPosition = wxPoint(0, 0)

        #-------------------------------------------------------------------
        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        #
        # TBD - Investigate why enabling this code is ineffective
        # in triggering tsTexEntryBox receipt of mouse LeftClicks.
        # The mouse LeftClicks are recognized by parent (such as
        # tsWxTextEntryDialog or tsWxPasswordEntryDialog) not only
        # for the TextEditBox but for the parent's surrounding
        # rectanglular area.
        #
        if True:
            event = EVT_COMMAND_LEFT_CLICK
        else:
            event = EVT_COMMAND_RIGHT_CLICK

        handler = self.tsOnEditBoxLeftClick
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        # Automatically Bind all keyboard events ASAP (now).
        # Will register event in the SystemEventTable.
        event = EVT_CHAR
        handler = self.tsOnTextEntryFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        event = EVT_SET_FOCUS
        handler = self.SetFocusFromKbd
        source = self
        self.Bind(event,
                  handler,
                  source,
                  useSystemEventTable=True)

        #-------------------------------------------------------------------
        self.tsRegisterKeyboardInputOrder()

        # TBD - Resolve why wx.caretVeryVisible is unchangeable.
        self.ts_CursorVisibility = self.tsCursesCaretVisibility(
            visibility=wx.caretVeryVisible)

        self.tsUpdateDisplay(RESET_CHARACTER,
                             self.ts_TextCharacterBufferOffset)

        self.tsEndClassRegistration(theClass)

    #----------------------------------------------------------------------

    def do_command(self, evt):
        '''
        Process a single command keystroke. Here are the supported special
        keystrokes:

            Keystroke Action
            ========= =====================================================
            Control-A Move cursor to left edge of window.
            Control-B Cursor left, wrapping to previous line if appropriate.
            Control-D Delete character under cursor.
            Control-E Move cursor to right edge (stripspaces off) or end
                      of line (stripspaces on).
            Control-F Cursor right, wrapping to next line when appropriate.
            Control-G Terminate, returning the window contents.
            Control-H Delete character backward.
            Control-I Horizontal Tab.
            Control-J Terminate if the window is 1 line, otherwise insert
                      newline.
            Control-K If line is blank, delete it, otherwise clear to end
                      of line.
            Control-L Refresh screen.
            Control-N Cursor down; move down one line.
            Control-O Insert a blank line at cursor location.
            Control-P Cursor up; move up one line.

            Move operations do nothing if the cursor is at an edge where the
            movement is not possible.
 
        The following keystroke synonyms are supported where possible:

            Keystroke     Synonym
            ============= =========
            KEY_BACKSPACE Control-H
            KEY_DOWN      Control-N
            KEY_END       Control-E
            KEY_ENTER     Control-J
            KEY_HOME      Control-A
            KEY_HTAB      Control-I
            KEY_LEFT      Control-B
            KEY_RIGHT     Control-F
            KEY_UP        Control-P

        All other keystrokes are treated as a command to insert the given
        character and move right (with line wrapping).
        '''
        inputTuple = evt.EventData
        (ch, theCharacter, theKeyname, theFlags) = inputTuple

        if ch in self.KeystrokeActionKeys:

            try:

                if DEBUG and VERBOSE:

                    fmt1 = 'tsWxTextEditBox.do_command (editActionKey): '
                    fmt2 = 'ch="%s" (0x%x); ' % (str(ch), int(ch))
                    fmt3 = 'theCharacter="%s"; ' % str(theCharacter)
                    fmt4 = 'theKeyname="%s"; ' % str(theKeyname)
                    fmt5 = 'theFlags="%s"' % str(theFlags)
                    msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                    self.logger.debug(msg)
                    print('DEBUG: %s\n' % msg)

                # Apply Keystroke Edit Action Key
                editActionKey = self.KeystrokeAction[ch]
                editActionKey(ch)

            except KeyError as errorCode:

                fmt1 = 'tsWxTextEditBox.do_command (editActionKey): '
                fmt2 = 'ch="%s" (0x%x); ' % (str(ch), int(ch))
                fmt3 = 'theCharacter="%s"; ' % str(theCharacter)
                fmt4 = 'theKeyname="%s"; ' % str(theKeyname)
                fmt5 = 'theFlags="%s"; ' % str(theFlags)
                fmt6 = 'errorCode="%s"' % str(errorCode)
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6
                self.logger.error(msg)
                print('ERROR: %s\n' % msg)
                # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            try:

                if DEBUG and VERBOSE:

                    fmt1 = 'tsWxTextEditBox.do_command (editDataKey): '
                    fmt2 = 'ch="%s" (0x%x); ' % (str(ch), int(ch))
                    fmt3 = 'theCharacter="%s"; ' % str(theCharacter)
                    fmt4 = 'theKeyname="%s"; ' % str(theKeyname)
                    fmt5 = 'theFlags="%s"' % str(theFlags)
                    msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                    self.logger.debug(msg)
                    print('DEBUG: %s\n' % msg)

                # Apply Keystroke Data Key
                self.tsInsertKeystrokeDataKey(ch)

            except KeyError as errorCode:

                fmt1 = 'tsWxTextEditBox.do_command (editDataKey): '
                fmt2 = 'ch="%s" (0x%x); ' % (str(ch), int(ch))
                fmt3 = 'errorCode="%s"' % str(errorCode)
                msg = fmt1 + fmt2 + fmt3
                self.logger.error(msg)
                print('ERROR: %s\n' % msg)
                # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #----------------------------------------------------------------------

    def edit(self, validator=None):
        '''
        This is the entry point you will normally use.

        It accepts editing keystrokes until one of the termination
        keystrokes is entered.

        If validator is supplied, it must be a function. It will be
        called for each keystroke entered with the keystroke as a
        parameter; command dispatch is done on the result.

        This method returns the window contents as a string; whether
        blanks in the window are included is affected by the stripspaces
        member.
        '''
        self.ts_Validator = validator

        self.ts_CursorVisibility = self.tsCursesCaretVisibility(
            visibility=wx.caretVeryVisible)
 
        if wx.ThemeToUse['TextEditBox']['EventDriven']:

            # Event driven
            msg = 'tsWxTextEditBox.edit (Event Driven): ' + \
                  'TextBox setup option will support ' + \
                  'tsWxEventLoop mouse handling. ' + \
                  'Operator must terminate text with "ctrl-G" or ' + \
                  'Mouse clicks on "OK" or "Cancel" buttons.'
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

            # Loop, gathering input pending completion.

            # TextCharacterBuffer is a list of single character strings.
            #
            # This permits entries to be inserted or deleted in an order
            # that establishes their relative position on the display.
            # One can insert a new line (^J) after some preceding text
            # in order to move the succeeding text to the beginning of
            # a new line. By deleting a new line, one can concatenate the
            # formerly preceding and succeeding text on the same line.
            self.ts_TextCharacterBuffer = wxLinkedUserDataList(
                ) # editable list of characters

            results = ''
            for index in range(self.ts_TextCharacterBuffer.GetCount()):

                results += self.ts_TextCharacterBuffer.GetIndex(index)

        else:

            # Non-event driven
            msg = 'tsWxTextEditBox.edit (Non-event Driven): ' + \
                  'TextBox setup option will preempt ' + \
                  'tsWxEventLoop mouse handling. ' + \
                  'Operator must terminate text with "enter". ' + \
                  'Mouse clicks on "OK" or "Cancel" buttons ' + \
                  'will be ignored.'
            self.logger.warning(msg)
            print('WARNING: %s\n' % msg)

            # Loop, gathering input pending completion.
            theTextPad = self.tsCursesTextpad(self.ts_Handle)
            results = theTextPad.edit()

        return (results)

    #----------------------------------------------------------------------

    def gather(self):
        '''
        Terminate, returning the edit window contents.

        This method returns the window contents as a string; whether blanks
        in the window are included is affected by the stripspaces member.
        '''
        if self.Completion:

            self.ts_CursorVisibility = self.tsCursesCaretVisibility(
            visibility=self.ts_CursorVisibility)

            results = ''
            for aRow in range(len(self.ts_TextLineBuffer)):
                results += self.ts_TextLineBuffer[aRow]

        if self.ts_StripSpaces:

            # Return a copy of the string with the leading and trailing
            # characters removed. The chars argument is a string specifying
            # the set of characters to be removed. If omitted or None, the
            # chars argument defaults to removing whitespace. The chars
            # argument is not a prefix or suffix; rather, all combinations
            # of its values are stripped.
            # return results.strip([chars])
            return (results.strip())

        else:

            return (results)

    #----------------------------------------------------------------------
    # Begin tsWx API Extensions

    #-----------------------------------------------------------------------

    def tsConvertCursorDictKey2Cursor(self, theDictKey):
        '''
        Return the Cursor Position associated with the Dictionary Key
        encoding the specified cursor column and row.
        '''
        theRow = int(theDictKey) / int(self.ts_MaxCols)
        theCol = theDictKey - (theRow * self.ts_MaxCols)

        theCursorPosition = wxPoint(theCol, theRow)

        return (theCursorPosition)

    #-----------------------------------------------------------------------

    def tsConvertCursor2CursorDictKey(self, theCursorPosition):
        '''
        Return the Dictionary Key encoding the specified cursor
        column and row.
        '''
        theCol = min(max(0, theCursorPosition.x), self.ts_MaxCols - 1)
        theRow = min(max(0, theCursorPosition.y), self.ts_MaxRows - 1)

        theDictKey = theCol + (theRow * self.ts_MaxCols)

        return (theDictKey)

    #-----------------------------------------------------------------------

    def tsConvertCursor2Offset(self, newCursorPosition):
        '''
        Return the text character buffer offset for the specified cursor
        column and row.
        '''
        newCol = min(max(0, newCursorPosition.x), self.ts_MaxCols -1)
        newRow = min(max(0, newCursorPosition.y), self.ts_MaxRows -1)

        try:

            if wxPoint(newCol, newRow) == wxPoint(0, 0):

                newCharacterBufferOffset = 0

            elif ((newRow < len(self.ts_TextLineBuffer)) and \
                  (newCol < len(self.ts_TextLineBuffer[newRow]))):

                newCharacterBufferOffset = self.ts_TextBufferCursor2OffsetMap[
                    self.tsConvertCursor2CursorDictKey(wxPoint(
                        newCol, newRow))]

            else:

                newCharacterBufferOffset = (
                    self.ts_TextCharacterBuffer.GetCount())

        except Exception as errorCode:

            if (((newCursorPosition.x >= 0) and \
                 (newCursorPosition.x <  self.ts_MaxCols)) and \
                ((newCursorPosition.y >= 0) and \
                 (newCursorPosition.y <  self.ts_MaxRows))):

                newCol = newCursorPosition.x
                newRow = newCursorPosition.y

                if ((newCol == 0) and \
                    (newRow < len(self.ts_TextLineBuffer))):

                    newCharacterBufferOffset = (
                        self.ts_TextLineBufferIndex[newRow])

                else:

                    newCharacterBufferOffset = (
                        self.ts_TextBufferCursor2OffsetMap[
                            self.tsConvertCursor2CursorDictKey(
                                wxPoint(newCol, newRow))])

            else:

                newCharacterBufferOffset = (
                    self.ts_TextCharacterBuffer.GetCount())

        return (newCharacterBufferOffset)

    #-----------------------------------------------------------------------

    def tsConvertOffset2Cursor(self, newTextCharacterBufferOffset):
        '''
        Return the displayed cursor position (column and row coordinated)
        for the specified text character buffer offset.
        '''
        if newTextCharacterBufferOffset <= 0:

            # newTextCharacterBufferOffset <= 0
            newCursorPosition = wxPoint(0, 0)

        elif newTextCharacterBufferOffset >= (
            self.ts_TextCharacterBuffer.GetCount()):

            # newTextCharacterBufferOffset >= (
            # self.ts_TextCharacterBuffer.GetCount())
            # Get last location within TextCharacterBuffer
            if DEBUG and VERBOSE:
                fmt1 = 'tsWxTextEditBox.tsConvertOffset2Cursor: '
                fmt2 = 'TextBufferOffset2CursorMap="%s"' % str(
                    self.ts_TextBufferOffset2CursorMap)
                msg = fmt1 + fmt2
                self.logger.notice(msg)
                print('NOTICE: %s\n' % msg)

            lastCursorPosition = self.ts_TextBufferOffset2CursorMap[
                max(0, (self.ts_TextCharacterBuffer.GetCount()) - 1)]

            lastCol = lastCursorPosition.x
            lastRow = lastCursorPosition.y

            if ((lastCol + 1) < self.ts_MaxCols):

                # (lastCol + 1) < self.ts_MaxCols
                # Set last location just beyond last character in last row
                newCursorPosition = wxPoint(lastCol + 1, lastRow)

            elif ((lastRow + 1) < self.ts_MaxRows):

                # (lastCol + 1) = self.ts_MaxCols
                # (lastRow + 1) < self.ts_MaxRows
                # Set last location just before first character in next row
                newCursorPosition = wxPoint(0, lastRow + 1)

            else:

                # (lastCol + 1) = self.ts_MaxCols
                # (lastRow + 1) = self.ts_MaxRows
                # Set unusable location beyond last character in last row
                newCursorPosition = lastCursorPosition

        else:

            # newTextCharacterBufferOffset < (
            # self.ts_TextCharacterBuffer.GetCount())
            # Set location within TextCharacterBuffer
            try:

                newCursorPosition = self.ts_TextBufferOffset2CursorMap[
                    newTextCharacterBufferOffset]

            except KeyError as errorCode:

                oldCursorPosition = self.ts_TextBufferOffset2CursorMap[
                    max(0, newTextCharacterBufferOffset - 1)]

                newCursorPosition = wxPoint(0, oldCursorPosition.y + 1)

                fmt1 = 'tsWxTextEditBox.tsConvertOffset2Cursor: '
                fmt2 = 'KeyError="%s"; ' % str(errorCode)
                fmt3 = 'offset=%s; ' % str(newTextCharacterBufferOffset)
                fmt4 = 'cursor (old)=%s; ' % str(oldCursorPosition)
                fmt5 = 'cursor (new)=%s' % str(newCursorPosition)
                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                self.logger.warning(msg)
                print('WARNING: %s\n' % msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (newCursorPosition)

    #-----------------------------------------------------------------------

    def tsDumpTextEditBoxCheckPoint(self,
                                    character,
                                    oldAnticipatedNextCursor,
                                    callerName=None):
        '''
        Gather, format and output a Text Edit Box CheckPoint.
        '''
        fmt1 = '***** tsWxTextEditBox.%s: ' % callerName

        if int(character) in list(KEY_NAMES.keys()):

            if character == RESET_CHARACTER:

                fmt2a = '\n\n\tKeyboard Input (ch) was ' + \
                        'ScanCode=%d (0x%x) ' % (character, character)
                fmt2b = 'for %s="%s"; ' % (
                    RESET_CHARACTER_NAME,
                    KEY_NAMES[character])
                fmt2 = fmt2a + fmt2b

            else:

                fmt2 = '\n\n\tKeyboard Input (ch) was ' + \
                       'ScanCode=%d (0x%x) for Curses Name="%s"; ' % (
                           character, character, KEY_NAMES[character])

        else:

            fmt2 = '\n\n\tKeyboard Input (ch) was ' + \
                   'ScanCode=%d (0x%x) for Character="%s"; ' % (
                       character, character, chr(character))

        fmt3 = '\n\n\tAnticipatedNextCursorPosition=%s was %s; ' % (
            str(self.ts_AnticipatedNextCursorPosition),
            str(oldAnticipatedNextCursor))

        msg = fmt1 + fmt2 + fmt3
        self.logger.debug(msg)
        print('DEBUG: %s\n' % msg)

    #-----------------------------------------------------------------------

    def tsDumpTextEditBoxDataBase(self,
                                  character,
                                  oldOffset,
                                  oldCursor,
                                  oldAnticipatedNextCursor,
                                  callerName=None):
        '''
        Gather, format and output contents of the Text Edit Box DataBase.
        '''
        fmt1 = '***** tsWxTextEditBox.%s: ' % callerName

        if int(character) in list(KEY_NAMES.keys()):

            if character == RESET_CHARACTER:

                fmt2a = '\n\n\tKeyboard Input (ch) was ' + \
                        'ScanCode=%d (0x%x) ' % (character, character)
                fmt2b = 'for %s="%s"; ' % (
                    RESET_CHARACTER_NAME,
                    KEY_NAMES[character])
                fmt2 = fmt2a + fmt2b

            else:

                fmt2 = '\n\n\tKeyboard Input (ch) was ' + \
                       'ScanCode=%d (0x%x) for Curses Name="%s"; ' % (
                           character, character, KEY_NAMES[character])

        else:

            fmt2 = '\n\n\tKeyboard Input (ch) was ' + \
                   'ScanCode=%d (0x%x) for Character="%s"; ' % (
                       character, character, chr(character))

        fmt3 = '\n\n\tTextCharacterBuffer="%s"; ' % str(
            self.tsGetTextCharacterBufferString())

        fmt4 = '\n\n\tTextCharacterBufferOffset=%s was %s; ' % (
            str(self.ts_TextCharacterBufferOffset),
            oldOffset)

        fmt5 = '\n\n\tCursorPosition=%s was %s; ' % (
            str(self.ts_CursorPosition),
            str(oldCursor))

        fmt6 = '\n\n\tAnticipatedNextCursorPosition=%s was %s; ' % (
            str(self.ts_AnticipatedNextCursorPosition),
            str(oldAnticipatedNextCursor))

        fmt7 = '\n\n\tTextLineBuffer="%s"; ' % str(
            self.ts_TextLineBuffer)

        fmt8 = '\n\n\tTextLineBufferIndex="%s"; ' % str(
            self.ts_TextLineBufferIndex)

        if USE_CURSOR_DICT_KEY:

            cursor2OffsetMap = ''
            cursorDictKeys = list(self.ts_TextBufferCursor2OffsetMap.keys())

            for cursorDictKey in cursorDictKeys:

                cursor = self.tsConvertCursorDictKey2Cursor(cursorDictKey)
                offset = self.ts_TextBufferCursor2OffsetMap[cursorDictKey]
                if cursorDictKey == cursorDictKeys[0]:

                    cursor2OffsetMap += '{%s: %s' % (str(cursor),
                                                     str(offset))

                elif cursorDictKey == cursorDictKeys[len(cursorDictKeys) - 1]:

                    cursor2OffsetMap += ', %s: %s}' % (str(cursor),
                                                       str(offset))

                else:

                    cursor2OffsetMap += ', %s: %s' % (str(cursor),
                                                      str(offset))

            fmt9 = '\n\n\tCursor2OffsetMap="%s"; ' % str(
                cursor2OffsetMap)

        else:

            fmt9 = '\n\n\tCursor2OffsetMap="%s"; ' % str(
                self.ts_TextBufferCursor2OffsetMap)

        if USE_CURSOR_DICT_KEY:

            offset2CursorMap = ''
            offsetDictKeys = list(self.ts_TextBufferOffset2CursorMap.keys())

            for offsetDictKey in offsetDictKeys:

                offset = offsetDictKey
                if USE_CURSOR_DICT_KEY:

                    # cursorDictKey NOT actually used
                    cursorDictKey = self.ts_TextBufferOffset2CursorMap[
                        offset]
                    cursor = cursorDictKey

                else:

                    # cursorDictKey actually used
                    cursorDictKey = self.ts_TextBufferOffset2CursorMap[
                        offset]
                    cursor = self.tsConvertCursorDictKey2Cursor(
                        cursorDictKey)

                if offsetDictKey == offsetDictKeys[0]:

                    offset2CursorMap += '{%s: %s' % (str(offset),
                                                     str(cursor))

                elif offsetDictKey == offsetDictKeys[len(offsetDictKeys) - 1]:

                    offset2CursorMap += ', %s: %s}' % (str(offset),
                                                       str(cursor))

                else:

                    offset2CursorMap += ', %s: %s' % (str(offset),
                                                      str(cursor))

            fmt10 = '\n\n\tOffset2CursorMap="%s"' % str(
                offset2CursorMap)

        else:

            fmt10 = '\n\n\tOffset2CursorMap="%s"' % str(
                self.ts_TextBufferOffset2CursorMap)

        msg = (fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + \
               fmt6 + fmt7 + fmt8 + fmt9 + fmt10)
        self.logger.debug(msg)
        print('DEBUG: %s\n' % msg)

    #-----------------------------------------------------------------------

    def tsGetCompletion(self):
        '''
        Return the Completion.
        '''
        return (self.ts_Completion)

    #-----------------------------------------------------------------------

    def tsGetConstrainedAnticipatedNextCursorPosition(self):
        '''
        Return a constrained Anticipated Next CursorPosition. The value
        must be within the range of wxPoint(0, 0) to wxPoint(maxCols - 1,
        maxRows - 1).
        '''
        oldCursor = self.ts_AnticipatedNextCursorPosition

        if USE_CONSTRAIN_CURSOR:

            oldCol = max(0, oldCursor.x)
            oldRow = max(0, oldCursor.y)
            constrainedCursor = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                        min(oldRow, self.ts_MaxRows - 1))

        else:

            oldCol = oldCursor.x
            oldRow = oldCursor.y
            constrainedCursor = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                        min(oldRow, self.ts_MaxRows - 1))

        return (constrainedCursor)

    #-----------------------------------------------------------------------

    def tsGetConstrainedCursorPosition(self):
        '''
        Return a constrained Cursor Position. The value must be within the
        range of wxPoint(0, 0) to wxPoint(maxCols - 1, maxRows - 1).
        '''
        oldCursor = self.ts_CursorPosition

        if USE_CONSTRAIN_CURSOR:

            oldCol = max(0, oldCursor.x)
            oldRow = max(0, oldCursor.y)
            constrainedCursor = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                        min(oldRow, self.ts_MaxRows - 1))

        else:

            oldCol = oldCursor.x
            oldRow = oldCursor.y
            constrainedCursor = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                        min(oldRow, self.ts_MaxRows - 1))

        return (constrainedCursor)

    #-----------------------------------------------------------------------

    def tsGetConstrainedTextCharacterBufferOffset(self):
        '''
        Return a constrained Text Character Buffer Offset. The value must be
        within the range of 0 to MaxCapacity - 1.
        '''
        oldOffset = self.ts_TextCharacterBufferOffset

        if USE_CONSTRAIN_OFFSET:

            constrainedOffset = max(0, min(oldOffset,
                                           self.ts_MaxCapacity - 1))

        else:

            constrainedOffset = oldOffset

        return (constrainedOffset)

    #-----------------------------------------------------------------------

    def tsGetLabel(self):
        '''
        Return the label.
        '''
        return (self.ts_Label)

    #-----------------------------------------------------------------------

    def tsGetPasswordMode(self):
        '''
        Return the PasswordMode.
        '''
        return (self.ts_PasswordMode)

    #-----------------------------------------------------------------------

    def tsGetStripSpaces(self):
        '''
        Return the StripSpaces.
        '''
        return (self.ts_StripSpaces)

    #-----------------------------------------------------------------------

    def tsGetTextCharacterBufferString(self):
        '''
        Return the text string.
        '''
        string = ''
        for index in range(self.ts_TextCharacterBuffer.GetCount()):
            string += chr(self.ts_TextCharacterBuffer.GetIndex(index))
        return (string)

    #-----------------------------------------------------------------------

    def tsInsertKeystrokeDataKey(self, ch):
        '''
        Insert
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsInsertKeystrokeDataKey'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        if ((oldOffset + 1) < self.ts_MaxCapacity):

            if (oldOffset >= self.ts_TextCharacterBuffer.GetCount()):

                # Insert character at end of input list.
                self.ts_TextCharacterBuffer.InsertAsTail(ch)

            else:

                # Insert character before or between start and end
                # of input list.
                self.ts_TextCharacterBuffer.InsertBefore(oldOffset, ch)

            newOffset = oldOffset + 1

        else:

            newOffset = oldOffset

            fmt1 = 'tsWxTextEditBox.tsInsertKeystrokeDataKey ' + \
                   '(rejected 0x%x): ' % ch
            fmt2 = 'No More Room! buffer="%s"' % str(
                self.ts_TextCharacterBuffer)
            fmt3 = 'offset=%s; ' % str(self.ts_TextCharacterBufferOffset)
            fmt4 = 'cursor=%s' % str(self.ts_CursorPosition)
            msg = fmt1 + fmt2 + fmt3 + fmt4
            self.logger.warning(msg)
            print('WARNING: %s\n' % msg)
            # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        if True or (DEBUG and VERBOSE):

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #-----------------------------------------------------------------------

    def tsLayoutLineBuffer(self, ch, newOffset, callerName=None):
        '''
        Allocate contents of line buffer.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        requestor = 'tsLayoutLineBuffer'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        #-------------------------------------------------------------------

        # Allocate TextCharacterBuffer to ParagraphBuffer.
        paragraphBuffer = []
        paragraphBufferIndex = [0]
        string = ''
        for item in range(self.ts_TextCharacterBuffer.GetCount()):

            data = chr(self.ts_TextCharacterBuffer.GetIndex(item))

            if data == chr(10):

                string += chr(10)
                paragraphBuffer.append(string)
                paragraphBufferIndex.append(item + 1)
                string = wx.EmptyString

            else:

                if string == wx.EmptyString:

                    string = data

                else:

                    string += data

                if item == (self.ts_TextCharacterBuffer.GetCount() - 1):

                    paragraphBuffer.append(string)

            if DEBUG and VERBOSE:

                fmt1 = 'TextEditBox.tsLayoutLineBuffer ' + \
                       '(paragraphBuffer Layout Detail): '

                fmt2 = '\n\n\titem=%d; ' % item

                fmt3 = '\n\n\tTextCharacterBuffer[%d]="%s" (0x%x); ' % (
                    item, data, ord(data))

                fmt4 = '\n\n\tTextCharacterBuffer="%s"; ' % str(
                    self.tsGetTextCharacterBufferString())

                fmt5 = '\n\n\tparagraphBuffer="%s"; ' % str(
                    paragraphBuffer)

                fmt6 = '\n\n\tparagraphBufferIndex="%s"' % str(
                    paragraphBufferIndex)

                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6
                self.logger.debug(msg)
                print('DEBUG: %s\n' % msg)

        #-------------------------------------------------------------------

        # Allocate ParagraphBuffer to TextLineBuffer.
        self.ts_TextLineBuffer = []
        self.ts_TextLineBufferIndex = [0]

        for item in range(len(paragraphBuffer)):

            paragraph = paragraphBuffer[item]
            strings = self.tsTextWrap(paragraph)

            for string in strings:

                previousIndex = len(self.ts_TextLineBufferIndex) - 1
                previousOffset = self.ts_TextLineBufferIndex[previousIndex]
                self.ts_TextLineBuffer.append(string)
                self.ts_TextLineBufferIndex.append(
                    previousOffset + len(string))

            if DEBUG and VERBOSE:

                fmt1 = 'TextEditBox.tsLayoutLineBuffer ' + \
                       '(TextLineBuffer Layout Detail): '

                fmt2 = '\n\n\titem=%d; ' % item

                fmt3 = '\n\n\tparagraph[%d]="%s"; ' % (
                    item, str(paragraph))

                fmt4 = '\n\n\tparagraphBuffer="%s"; ' % str(
                    paragraphBuffer)

                fmt5 = '\n\n\tstrings="%s"; ' % str(
                    strings)

                fmt6 = '\n\n\tTextLineBuffer="%s"; ' % str(
                    self.ts_TextLineBuffer)

                fmt7 = '\n\n\tTextLineBufferIndex="%s"; ' % str(
                    self.ts_TextLineBufferIndex)

                msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6 + fmt7
                self.logger.debug(msg)
                print('DEBUG: %s\n' % msg)

        if DEBUG and VERBOSE:

            fmt1 = 'TextEditBox.tsLayoutLineBuffer ' + \
                   '(TextLineBuffer Layout Summary): '

            fmt2 = '\n\n\tparagraphBuffer="%s"; ' % str(
                paragraphBuffer)

            fmt3 = '\n\n\tTextLineBuffer="%s"; ' % str(
                self.ts_TextLineBuffer)

            fmt4 = '\n\n\tTextLineBufferIndex="%s"; ' % str(
                self.ts_TextLineBufferIndex)

            msg = fmt1 + fmt2 + fmt3 + fmt4
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

        #-------------------------------------------------------------------

        # Allocate TextLineBuffer to the Cursor to Offset Map and to the
        # Offset to Cursor Map.
        self.ts_TextBufferCursor2OffsetMap = {} # maps Cursor to Offset
        self.ts_TextBufferCursor2OffsetMap[
            self.tsConvertCursor2CursorDictKey(wxPoint(0, 0))] = 0
        self.ts_TextBufferOffset2CursorMap = {} # maps Offset to Cursor
        self.ts_TextBufferOffset2CursorMap[0] = wxPoint(0, 0)

        # New Algorithm (Under Construction)
        if (self.ts_TextCharacterBuffer.GetCount() == 0):

            # Empty Buffers
            offset = 0
            cursor = wxPoint(0, 0)

            self.ts_TextBufferCursor2OffsetMap[
                self.tsConvertCursor2CursorDictKey(cursor)] = offset
            self.ts_TextBufferOffset2CursorMap[offset] = cursor

        else:

            offset = 0
            for row in range(len(self.ts_TextLineBuffer)):

                theLine = list(self.ts_TextLineBuffer[row])

                for col in range(len(theLine)):

                    theCharacter = theLine[col]

                    inSync = False
                    while (not inSync):

                        data = chr(self.ts_TextCharacterBuffer.GetIndex(
                            offset))

                        if theCharacter == data:

                            inSync = True

                            # Printable Character; Inserted by Operator
                            cursor = wxPoint(col, row)

                            self.ts_TextBufferCursor2OffsetMap[
                                self.tsConvertCursor2CursorDictKey(cursor)] = (
                                    offset)
                            self.ts_TextBufferOffset2CursorMap[
                                offset] = cursor

##                        elif (data == NEW_LINE_CHARACTER) and \
##                             (theCharacter == ' '):

##                            inSync = True

##                            # Printable Character; Inserted by Operator
##                            cursor = wxPoint(col, row)

##                            self.ts_TextBufferCursor2OffsetMap[cursor] = offset
##                            self.ts_TextBufferOffset2CursorMap[offset] = cursor

                        else:

                            if DEBUG:

                                fmt1 = 'TextEditBox.tsLayoutLineBuffer: ' + \
                                       'Ignored unexpected ' +\
                                       'data="%s" != string="%s"; ' % (
                                           data,
                                           self.ts_TextLineBuffer[
                                               row][col:col+1])
                                fmt2 = 'LineBuffer[%d]="%s"; ' % (
                                    row, str(self.ts_TextLineBuffer))
                                fmt3 = 'LineBufferIndex="%s"' % str(
                                    self.ts_TextLineBufferIndex)
                                msg = fmt1 + fmt2 + fmt3
                                self.logger.warning(msg)
                                print('WARNING: %s\n' % msg)

                        if ((offset + 1) < (
                            self.ts_TextCharacterBuffer.GetCount())):

                            offset += 1

                        else:

                            break

                    if DEBUG and VERBOSE:

                        fmt1 = 'TextEditBox.tsLayoutLineBuffer ' + \
                               '(Cursor Map Layout Details): '
                        fmt2 = '\n\n\toffset=%s; ' % str(offset)
                        fmt3 = '\n\n\tdata="%s" (0x%x) vs ' % (data, ord(data))
                        fmt4 = '\n\n\tcol' + \
                               '[%d]="%s" (0x%x); line[%d]="%s" ; ' % (
                                   col,
                                   theCharacter,
                                   ord(theCharacter),
                                   row,
                                   self.ts_TextLineBuffer[row])
                        fmt5 = '\n\n\tLineBuffer[%d]="%s"; ' % (
                            row, str(self.ts_TextLineBuffer))
                        fmt6 = '\n\n\tLineBufferIndex="%s"' % str(
                            self.ts_TextLineBufferIndex)
                        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5 + fmt6
                        self.logger.debug(msg)
                        print('DEBUG: %s\n' % msg)

##        if (checkmaps) or (DEBUG and VERBOSE):

##            fmt1 = 'TextEditBox.tsLayoutLineBuffer (checkmaps): '
##            fmt2 = '\n\n\tLineBuffer="%s"; ' % str(
##                self.ts_TextLineBuffer)
##            fmt3 = '\n\n\tLineBufferIndex="%s"' % str(
##                self.ts_TextLineBufferIndex)
##            fmt4 = '\n\n\tCursor2OffsetMap="%s"' % str(
##                self.ts_TextBufferCursor2OffsetMap)
##            fmt5 = '\n\n\tOffset2CursorMap="%s"' % str(
##                self.ts_TextBufferOffset2CursorMap)
##            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
##            self.logger.debug(msg)
##            print('DEBUG: %s\n' % msg)

        # Update terminal display to reflect line buffer changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_A(self, ch):
        '''
        Move cursor to left edge of window.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldCursor.x
        oldRow = oldCursor.y

        requestor = 'tsOnControl_A'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldCursor, callerName=requestor)

        newCol = 0
        newRow = oldRow
        newCursor = wxPoint(newCol, newRow)
        newOffset = self.tsConvertCursor2Offset(newCursor)

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if True or (DEBUG and VERBOSE):

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_B(self, ch):
        '''
        Move cursor left, wrapping to previous line if appropriate.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        requestor = 'tsOnControl_B'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newOffset = max(0, oldOffset - 1)

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_D(self, ch):
        '''
        Delete character under cursor.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_D'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        if ((0 <= oldOffset) and \
            (oldOffset < (self.ts_TextCharacterBuffer.GetCount()))):

            self.ts_TextCharacterBuffer.Remove(oldOffset)

            newOffset = max(0, oldOffset - 1)

        else:

            if (oldOffset < 0):

                newOffset = 0

            else:

                newOffset = (self.ts_TextCharacterBuffer.GetCount())


        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        # Move cursor right, wrapping to next line when appropriate.
        self.tsOnControl_F(ch)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_E(self, ch):
        '''
        Move cursor to right edge (stripspaces off) or end of line
        (stripspaces on).
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        # oldCol = oldCursor.x
        oldRow = oldCursor.y

        requestor = 'tsOnControl_E'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newCol = max(0, len(self.ts_TextLineBuffer[oldRow]))
        newRow = oldRow
        newCursor = wxPoint(0, newRow) # TBD - Fix Map Trap on newCol
        newOffset = self.tsConvertCursor2Offset(newCursor) + newCol

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_F(self, ch):
        '''
        Move cursor right, wrapping to next line when appropriate.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        requestor = 'tsOnControl_F'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newOffset = min(oldOffset + 1, self.ts_MaxCols -1)

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_G(self, ch):
        '''
        Terminate, returning the edit window contents.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_G'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        self.Completion = True

        results = self.gather()

        if DEBUG and VERBOSE:

            print('##### tsWxTextEditBox.tsOnControl_G: Begin Report.')
            print('TextCharacterBuffer="%s"' % str(self.ts_TextCharacterBuffer))
            print('lineBuffer="%s"' % str(self.ts_TextLineBuffer))
            print('lineBufferIndex="%s"' % str(
                self.ts_TextLineBufferIndex))

            if VERBOSE:
                for offset in range((self.ts_TextCharacterBuffer.GetCount())):
                    theData = self.ts_TextCharacterBuffer.GetIndex(offset)
                    theCursor = self.tsConvertOffset2Cursor(offset)
                    theOffset = self.tsConvertCursor2Offset(theCursor)
                    if theData == 10:
                        fmt1 = 'tsWxTextEditBox.tsOnControl_G: '
                        fmt2 = '%3.3d: 0x%2.2X; %s; %s' % (offset,
                                                           theData,
                                                           str(theCursor),
                                                           str(theOffset))
                        msg = fmt1 + fmt2
                    else:
                        fmt1 = 'tsWxTextEditBox.tsOnControl_G: '
                        fmt2 = '%3.3d: "%s"; %s; %s' % (offset,
                                                        chr(theData),
                                                        str(theCursor),
                                                        str(theOffset))
                        msg = fmt1 + fmt2

                    self.logger.debug(msg)
                    print('DEBUG: %s\n' % msg)

            fmt1 = 'tsWxTextEditBox.tsOnControl_G (0x%x): ' % ch
            fmt2 = 'buffer="%s"' % str(self.tsGetTextCharacterBufferString())
            fmt3 = 'offset=%s' % str(self.ts_TextCharacterBufferOffset)
            msg = fmt1 + fmt2 + fmt3
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)
            print('##### tsWxTextEditBox.tsOnControl_G: End Report.')

        return (results)

    #----------------------------------------------------------------------

    def tsOnControl_H(self, ch):
        '''
        Delete character under cursor after moving cursor backwards.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_H'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        # Move cursor left, wrapping to previous line if appropriate.
        self.tsOnControl_B(ch)

        # Delete character under cursor.
        self.tsOnControl_D(ch)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_I(self, ch):
        '''
        Move to the right to the next Horizontal Tab position.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_I'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newOffset = oldOffset

        for i in range(8):

            ## self.tsInsertKeystrokeDataKey(ch)
            oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
            self.ts_TextCharacterBuffer.InsertAfter(oldOffset, ch)
            newOffset = min(
                oldOffset + 1, self.ts_MaxCapacity - 1)
            self.tsSetConstrainedTextCharacterBufferOffset(newOffset)

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_J(self, ch):
        '''
        Terminate if the window is 1 line, otherwise insert newline.

        NOTE: If we terminate on first line, how could we accept
        additional lines unless we terminate if first line is empty?
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_J'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        # Insert new line
        try:

            self.tsInsertKeystrokeDataKey(ch)

        except KeyError as errorCode:

            fmt1 = 'tsWxTextEditBox.tsOnControl_J (insert new line): '
            fmt2 = 'ch=%s; errorCode="%s"' % (
                str(ch), str(errorCode))
            msg = fmt1 + fmt2
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        newOffset = self.tsGetConstrainedTextCharacterBufferOffset()

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_K(self, ch):
        '''
        If line is blank, delete it, otherwise clear to end of line.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_K'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        theKillRow = self.tsGetConstrainedCursorPosition().y

        theKillOffset = oldOffset

        firstKillCol = max(0, self.ts_CursorPosition.x)

        lastKillCol = max(0, len(self.ts_TextLineBuffer[theKillRow]))

        if lastKillCol == 0:

            del self.ts_TextLineBuffer[theKillRow]

        else:

            # Clear to end of line.
            for theKillCol in range(firstKillCol,
                                    lastKillCol):

                self.tsOnKeyDC(ch)

                if DEBUG and VERBOSE:

                    fmt1 = 'TBD - tsWxTextEditBox.tsOnControl_K (0x%x): ' % ch
                    fmt2 = 'buffer="%s"' % str(
                        self.tsGetTextCharacterBufferString())
                    fmt3 = 'theKillOffset=%s' % str(theKillOffset)
                    msg = fmt1 + fmt2 + fmt3
                    self.logger.debug(msg)
##                    print('DEBUG: %s\n' % msg)

        newOffset = self.tsGetConstrainedTextCharacterBufferOffset()

        self.tsSetConstrainedTextCharacterBufferOffset(newOffset)

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_L(self, ch):
        '''
        Refresh screen.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_L'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newOffset = oldOffset

        # Update terminal display to reflect line buffer/cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_N(self, ch):
        '''
        Move cursor down one line.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldCursor.x
        oldRow = oldCursor.y

        requestor = 'tsOnControl_N'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        newCol = oldCol
        newRow = oldRow

        newCursor = wxPoint(newCol, newRow)

        try:

            newOffset = oldOffset - 3 #self.tsConvertCursor2Offset(newCursor)

        except KeyError as errorCode:

            newOffset =  oldOffset + (
                len(self.ts_TextLineBuffer[oldRow]) - oldCol) + 3

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_O(self, ch):
        '''
        Insert a blank line at cursor location.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnControl_O'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        # Insert new line into TextCharacterBuffer.
        # Update the following:
        #     text line buffer to reflect character buffer changes
        #     cursor position to reflect line buffer changes
        #     terminal display to reflect line buffer changes
        self.tsInsertKeystrokeDataKey(NEW_LINE_CHARACTER)

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, oldOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnControl_P(self, ch):
        '''
        Move cursor up one line.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldCursor.x
        oldRow = oldCursor.y

        requestor = 'tsOnControl_P'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

##        try:

##            newOffset = self.tsConvertCursor2Offset(newCursor)

##        except KeyError, errorCode:

##            newOffset =  oldOffset + (
##                len(self.ts_TextLineBuffer[oldRow]) - oldCol) + 3

        if oldRow > 0:

            newRow = oldRow # - 1

        else:

            newRow = oldRow

####        newLength = len(self.ts_TextLineBuffer[newRow])
####        newLastCol = newLength - 1
##        if oldCol < newLength:

##            newCol = oldOffset - self.ts_TextLineBufferIndex[newRow]

##        else:

##            string = self.ts_TextLineBuffer[newRow]
##            lastCharacter = string[newLastCol, newLastCol + 1]
##            if lastCharacter == 10:

##                newCol = newLastCol - 1

##            else:

##                newCol = newLastCol

        newOffset = oldOffset - 5 #self.ts_TextLineBufferIndex[newRow] + newCol

        # Update terminal display to reflect cursor changes
        self.tsUpdateDisplay(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #-----------------------------------------------------------------------

    def tsOnEditBoxLeftClick(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'tsWxTextEditBox.' + \
              'tsOnEditBoxLeftClick'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if True or DEBUG:
##            fmt1 = 'tsWxTextEditBox.tsOnEditBoxLeftClick: '
##            fmt2 = 'evt=%s' % str(evt)
##            msg = fmt1 + fmt2

##            self.logger.debug(msg)
##            print('NOTICE: %s\n' % msg)

##        triggeringObject = self
##        objectId = triggeringObject.ts_AssignedId

##        targetObject = self.ts_ScrolledText

##        results = self.tsProcessEventTables(
##            objectCriteria=self.ts_TriggeringCriteria,
##            objectId=objectId,
##            triggeringEvent=self.ts_TriggeringEvent,
##            triggeringObject=triggeringObject)

    #----------------------------------------------------------------------

    def tsOnKeyBackSpace(self, ch):
        '''
        Delete character under cursor after moving cursor backwards.
        '''
        self.tsOnControl_H(ch)

    #----------------------------------------------------------------------

    def tsOnKeyDC(self, ch):
        '''
        Delete character under cursor.
        '''
        # Move cursor left, wrapping to previous line if appropriate.
        self.tsOnControl_B(ch)

        # Delete character under cursor.
        self.tsOnControl_D(ch)

        # Move cursor right, wrapping to next line when appropriate.
        self.tsOnControl_F(ch)

    #----------------------------------------------------------------------

    def tsOnKeyDown(self, ch):
        '''
        Move cursor down one line.
        '''
        self.tsOnControl_N(ch)

    #----------------------------------------------------------------------

    def tsOnKeyEnd(self, ch):
        '''
        Move cursor to right edge (stripspaces off) or end of line
        (stripspaces on).
        '''
        self.tsOnControl_E(ch)

    #----------------------------------------------------------------------

    def tsOnKeyEnter(self, ch):
        '''
        Terminate if the window is 1 line, otherwise insert newline.

        NOTE: If we terminate on first line, how could we accept
        additional lines unless we terminate if first line is empty?
        '''
        self.tsOnControl_J(ch)

    #----------------------------------------------------------------------

    def tsOnKeyHome(self, ch):
        '''
        Move cursor to left edge of window.
        '''
        self.tsOnControl_A(ch)

    #----------------------------------------------------------------------

    def tsOnKeyLeft(self, ch):
        '''
        Move cursor left, wrapping to previous line if appropriate.
        '''
        self.tsOnControl_B(ch)

    #----------------------------------------------------------------------

    def tsOnKeyNpage(self, ch):
        '''
        Move cursor down one line.
        '''
        self.tsOnControl_N(ch)

    #----------------------------------------------------------------------

    def tsOnKeyPpage(self, ch):
        '''
        Move cursor up one line.
        '''
        self.tsOnControl_P(ch)

    #----------------------------------------------------------------------

    def tsOnKeyRight(self, ch):
        '''
        Move cursor right, wrapping to next line when appropriate.
        '''
        self.tsOnControl_F(ch)

    #----------------------------------------------------------------------

    def tsOnKeyUp(self, ch):
        '''
        Move cursor up one line.
        '''
        self.tsOnControl_P(ch)

    #-----------------------------------------------------------------------

    def tsOnReset(self, ch):
        '''
        Cancel (erase) input upon Control-@ (Control-Shift-2).
        '''
        self.ts_Completion = False
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        oldCol = oldAnticipatedNextCursor.x
        oldRow = oldAnticipatedNextCursor.y

        requestor = 'tsOnReset'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, callerName=requestor)

        #-------------------------------------------------------------------
        # Sequential (Internal) character/line views of Edit Buffer

        # TextCharacterBuffer is a list of single character strings.
        #
        # This permits entries to be inserted or deleted in an order
        # that establishes their relative position on the display.
        # One can insert a new line (^J) after some preceding text
        # in order to move the succeeding text to the beginning of
        # a new line. By deleting a new line, one can concatenate the
        # formerly preceding and succeeding text on the same line.
        self.ts_TextCharacterBuffer = wxLinkedUserDataList(
            ) # editable list of characters

        self.ts_TextCharacterBufferOffset = 0 # character insert/delete index

        # TextLineBuffer is a list of multi-character strings.
        #
        # List entries are indexed by row. The list is updated
        # after each character has been inserted into or deleted
        # from the TextCharacterBuffer. The operator input cursor
        # and display of edited operator input are then updated.
        self.ts_TextLineBuffer = [] # displayable list of text strings

        self.ts_TextLineBufferIndex = [] # line insert/delete index

        # TextBufferCursor2OffsetMap and TextBufferOffset2CursorMap are
        # dictionaries used to traslate between TextBufferOffset and
        # the currently associated TextLineBuffer CursorPosition.
        self.ts_TextBufferCursor2OffsetMap = {} # maps Cursor to Offset
##        self.ts_TextBufferCursor2OffsetMap[self.tsConvertCursor2CursorDictKey(
##            wxPoint(0, 0))] = 0
        self.ts_TextBufferOffset2CursorMap = {} # maps Offset to Cursor
##        self.ts_TextBufferOffset2CursorMap[0] = (
##            self.tsConvertCursor2CursorDictKey(wxPoint(0, 0)))

        if False:

            # This level of initialization should NOT be needed.
            for row in range(self.ts_MaxRows):
                self.ts_TextLineBuffer.append(wx.EmptyString)
                self.ts_TextLineBufferIndex.append(0)

        # The Cursor Position contains the display screen column and row
        # (line) co-ordinates of the operator input cursor.
        self.ts_AnticipatedNextCursorPosition = wxPoint(0, 0)
        self.ts_CursorPosition = wxPoint(0, 0)

        newOffset = 0

        # Update text line buffer to reflect character buffer changes
        self.tsLayoutLineBuffer(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    #----------------------------------------------------------------------

    def tsOnTextEntryFromKbd(self, evt):
        '''
        Receive and process event driven keyboard input from operator.
        '''
        # Receive operator input
        inputTuple = evt.EventData
        (ch, theCharacter, theKeyname, theFlags) = inputTuple

        if DEBUG and VERBOSE:

            fmt1 = 'tsWxTextEditBox.tsOnTextEntryFromKbd (Start 0x%x): ' % ch
            fmt2 = 'inputTuple="%s"; ' % str(inputTuple)
            fmt3 = 'offset=%s' % str(self.ts_TextCharacterBufferOffset)
            msg = fmt1 + fmt2 + fmt3
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

        # Edit contents of text character buffer:
        #     Delete selected contents of buffer
        #     Insert new component into buffer
        # Layout contents of new display and cursor (caret) position
        # Update display
        self.do_command(evt)

        if DEBUG and VERBOSE:

            fmt1 = 'tsWxTextEditBox.tsOnTextEntryFromKbd (End 0x%x): ' % ch
            fmt2 = 'buffer="%s"; ' % str(self.ts_TextCharacterBuffer)
            fmt3 = 'offset=%s; ' % str(self.ts_TextCharacterBufferOffset)
            fmt4 = 'cursor=%s' % str(self.ts_CursorPosition)
            msg = fmt1 + fmt2 + fmt3 + fmt4
            self.logger.debug(msg)
            print('DEBUG: %s\n' % msg)

    #-----------------------------------------------------------------------

    def tsSetCompletion(self, completion):
        '''
        Return the completion.
        '''
        self.ts_Completion = completion

    #-----------------------------------------------------------------------

    def tsSetConstrainedAnticipatedNextCursorPosition(self, oldCursor):
        '''
        Set a constrained Anticipated Next Cursor Position. The value
        must be within the range of wxPoint(0, 0) to wxPoint(maxCols - 1,
        maxRows - 1).
        '''
        oldCol = max(0, oldCursor.x)
        oldRow = max(0, oldCursor.y)

        constrainedCursor = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                    min(oldRow, self.ts_MaxRows - 1))

        self.ts_AnticipatedNextCursorPosition = constrainedCursor

    #-----------------------------------------------------------------------

    def tsSetConstrainedCursorPosition(self, oldCursor):
        '''
        Set a constrained Cursor Position. The value must be within the
        range of wxPoint(0, 0) to wxPoint(maxCols - 1, maxRows - 1).
        '''
        oldCol = max(0, oldCursor.x)
        oldRow = max(0, oldCursor.y)

        self.ts_CursorPosition = wxPoint(min(oldCol, self.ts_MaxCols - 1),
                                         min(oldRow, self.ts_MaxRows - 1))

    #-----------------------------------------------------------------------

    def tsSetConstrainedTextCharacterBufferOffset(self, oldOffset):
        '''
        Set a constrained Text Character Buffer Offset. The value must be
        within the range of 0 to MaxCapacity - 1.
        '''
        constrainedOffset = max(0, min(oldOffset,
                                       self.ts_MaxCapacity - 1))

        self.ts_TextCharacterBufferOffset = constrainedOffset

    #-----------------------------------------------------------------------

    def tsSetLabel(self, label):
        '''
        Set the label.
        '''
        self.ts_Label = label

    #-----------------------------------------------------------------------

    def tsSetPasswordMode(self, PasswordMode):
        '''
        Set the PasswordMode.
        '''
        self.ts_PasswordMode = PasswordMode

    #-----------------------------------------------------------------------

    def tsSetStripSpaces(self, StripSpaces):
        '''
        Set the StripSpaces.
        '''
        self.ts_StripSpaces = StripSpaces

    #-----------------------------------------------------------------------

    def tsTextCtrlLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of panel based upon arguments.
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

        self.logger.debug('    tsTextCtrlLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsUpdateCursor(self, ch, newOffset):
        '''
        Update the cursor to reflect the recent editing commands.
        Establish Gnu Emacs-style new cursor prompt position at
        left of insertion point (at left margin or on top of
        the most recently inserted character).
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        requestor = 'tsUpdateCursor'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor,requestor)

        newCursor = self.tsConvertOffset2Cursor(newOffset)

        if newOffset == 0:

            # Re-Initiale Cursor to beginning of terminal screen
            nextCursor = wxPoint(newCursor.x, newCursor.y)

        else:

            # Move cursor to terminal screen location of last keyboard input
            if (newCursor.y == oldCursor.y):

                # Remain on same line
                nextCursor = newCursor

            elif (newCursor.y < oldCursor.y):

                # Switch to a line above
                nextCursor = wxPoint(
                    len(self.ts_TextLineBuffer[newCursor.y]) - 1, newCursor.y)

            else:

                # Switch to a line below
                nextCursor = wxPoint(
                    len(self.ts_TextLineBuffer[newCursor.y]) - 1, newCursor.y)

        self.tsSetConstrainedCursorPosition(nextCursor)

        if False and \
           self.ts_TextCharacterBuffer[oldOffset] == NEW_LINE_CHARACTER:

            anticipatedNextCursor = wxPoint(0, nextCursor.y + 1)

        else:

            anticipatedNextCursor = nextCursor

        self.tsSetConstrainedAnticipatedNextCursorPosition(
            anticipatedNextCursor)

        # Update the caret as operator prompt for input
        try:

            if True:

                self.tsCursesChgAt(
                    x=self.ts_AnticipatedNextCursorPosition.x,
                    y=self.ts_AnticipatedNextCursorPosition.y,
                    num=1,
                    attr=wx.DISPLAY_UNDERLINE,
                    pixels=False)

            else:

                self.tsCursesChgAt(
                    x=self.ts_CursorPosition.x,
                    y=self.ts_CursorPosition.y,
                    num=1,
                    attr=wx.DISPLAY_UNDERLINE,
                    pixels=False)

        except Exception as errorCode:

            fmt1 = 'tsWxTextEditBox.tsUpdateCursor (tsCursesChgAt): '
            fmt2 = 'errorCode="%s"' % str(errorCode)
            msg = fmt1 + fmt2
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName='callerName')


    #-----------------------------------------------------------------------

    def tsUpdateDisplay(self, ch, newOffset):
        '''
        Update the display to reflect the recent editing commands.
        Display the new cursor prompt position and contents of the
        edit line buffer.

        NOTE: Each event driven keyboard input handler is responsible
        for registering the new keyboard input in the EditBoxBuffer
        and calculating and reportin the associated change to the
        TextCharacterBufferOffset.
        '''
        oldOffset = self.tsGetConstrainedTextCharacterBufferOffset()
        oldCursor = self.tsGetConstrainedCursorPosition()
        oldAnticipatedNextCursor = (
            self.tsGetConstrainedAnticipatedNextCursorPosition())

        requestor = 'tsUpdateDisplay'

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxCheckPoint(
                ch, oldAnticipatedNextCursor, requestor)

        self.tsSetConstrainedTextCharacterBufferOffset(newOffset)

        # Update terminal display to reflect line buffer changes
        try:

            self.tsCursesClear()

            for row in range(len(self.ts_TextLineBuffer)):
                try:
                    results = self.ts_TextLineBuffer[row]
                except Exception as errorCode:
                    results = wx.EmptyString
                x = 0
                y = row
                self.tsCursesAddStr(
                    x, y, results, attr=wx.DISPLAY_NORMAL, pixels=False)
##                self.tsCursesClrToEol()

        except Exception as errorCode:

            fmt1 = 'tsWxTextEditBox.tsUpdateDisplay (tsCursesAddStr): '
            fmt2 = 'errorCode="%s"' % str(errorCode)
            msg = fmt1 + fmt2
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        # Update cursor position to reflect line buffer changes
        self.tsUpdateCursor(ch, newOffset)

        if DEBUG and VERBOSE:

            self.tsDumpTextEditBoxDataBase(
                ch,
                oldOffset,
                oldCursor,
                oldAnticipatedNextCursor,
                callerName=requestor)

    # End tsWx API Extensions
    #----------------------------------------------------------------------
    Completion = property(tsGetCompletion, tsSetCompletion)
    Label = property(tsGetLabel, tsSetLabel)
    PasswordMode = property(tsGetPasswordMode, tsSetPasswordMode)
    StripSpaces = property(tsGetStripSpaces, tsSetStripSpaces)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
