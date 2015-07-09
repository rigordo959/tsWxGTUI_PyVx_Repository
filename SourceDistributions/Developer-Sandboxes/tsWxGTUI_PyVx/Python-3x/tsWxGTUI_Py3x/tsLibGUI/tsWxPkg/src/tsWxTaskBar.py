#! /usr/bin/env python
# "Time-stamp: <01/01/2015  5:11:36 AM rsg>"
'''
tsWxTaskBar.py - Class to establish a taskbar icon (button) for
each top level window (frame, dialog etc.). A taskbar icon
appears in the "system tray" and responds to mouse clicks,
optionally with a tooltip above it to help provide information.
'''
#################################################################
#
# File: tsWxTaskBar.py
#
# Purpose:
#
#    Class to establish a taskbar icon (button) for each top
#    level window (frame, dialog etc.). A taskbar icon appears
#    in the "system tray" and responds to mouse clicks,
#    optionally with a tooltip above it to help provide
#    information.
#
# Usage (example):
#
#    # Import
#
#    from tsWxTaskBar import TaskBar
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
# Classes:
#
#    TaskBar
#    TaskBarButton
#
# Methods:
#
#    TaskBar.Create
#    TaskBar.CreateStatusBar
#    TaskBar.CreateStatusTitle
#    TaskBar.__init__
#    TaskBar.tsGetClientArea
#    TaskBar.tsGetNetworkIdentification
#    TaskBar.tsGetTaskBarButtonData
#    TaskBar.tsShow
#    TaskBar.tsShowTaskBar
#    TaskBar.tsTaskBarLayout
#    TaskBar.tsTrapIfTooSmall
#    TaskBar.tsUpdate
#    TaskBarButton.__init__
#    TaskBarButton.tsCreateTaskBarButton
#    TaskBarButton.tsCreateTaskBarButtonLine
#    TaskBarButton.tsCreateTaskBarButtonMultiLine
#    TaskBarButton.tsOnLeftClick
#    TaskBarButton.tsTaskBarButtonOnSetFocus
#    TaskBarButton.tsUpdate
#
# Modifications:
#
#    2011/12/26 rsg Added reference to tsTaskBarButtonOnSetFocus
#                   as final operation in TaskBarButton.__init__
#                   so that newest button indicates the one
#                   having focus by default.
#
#    2012/01/06 rsg Added Hot Key visual support to TaskBarButton.
#                   Also added tsCreateTaskBarButton,
#                   tsCreateTaskBarButtonLine,
#                   tsCreateTaskBarButtonMultiLine and tsUpdate.
#
#    2012/01/19 rsg Modified tsTaskBarButtonOnSetFocus to replace
#                   hard coded colors by values taken at run time
#                   from wx.tsWxGlobals.ThemeToUse. This resolved
#                   appearance of black space between buttons
#                   when the theme-based color scheme changed.
#
#    2012/02/21 rsg Modified tsOnLeftClick to invoke
#                   tsProcessEventTables.
#
#    2012/03/29 rsg Applied DISPLAY_STANDOUT font style to
#                   distinguish active from inactive task on
#                   non-color displays (such as vt100 and vt220).
#
#    2012/05/02 rsg Added self.ts_DescendantOrderOfShow to
#                   register the order of show of for this
#                   top level window and its descendants.
#
#    2012/06/30 rsg Modified __init to change handler from
#                   tsTaskBarButtonOnSetFocus ro tsOnLeftClick.
#                   Modified tsOnLeftClick to invoke
#                   tsTaskBarButtonOnSetFocus. This eliminated
#                   redundant invocations of tstsTaskBarTopTask
#                   but did not resolve the failure to bring
#                   top task to foreground.
#
#    2012/07/02 rsg Re-designed logic to track changes in the TopTask
#                   and only change the panel stack when there has
#                   been a change in the TopTask. The previous design
#                   changed the stack multiple times, once for each
#                   task button color update. This eliminated
#                   redundant invocations of tstsTaskBarTopTask
#                   but did not resolve the failure to bring
#                   top task to foreground.
#
#    2012/07/28 rsg Remove triggeringMouseTuple argument from
#                   self.tsProcessEventTables and from
#                   self.tsProcessSelectedEventTable since
#                   event now contains value in its EventData.
#                   Add evt argument to tsOnLeftClick.
#
#    2013/06/21 rsg Referenced high-level self.tsCursesPanelUpdatePanels()
#                   instead of low-level curses.panel.update_panel()
#
#    2013/06/21 rsg Referenced high-level self.tsCursesDoUpdate()
#                   instead of low-level curses.doupdate()
#
#    2013/06/21 rsg Moved tsTaskBarTopTask, tsTaskBarTopChild and
#                   tsTaskBarDumpPanelStack from tsWxTaskBar to
#                   tsWxWindows.
#
#    2014/07/18 rsg Re-engineered use of curses panel stack to reflect
#                   changes made to the main wxPython emulation module,
#                   tsWxGraphicalTextUserInterface. Changes only effect
#                   conditionalizing based on wx.USE_CURSES_PANEL_STACK.
#
#    2015/01/01 rsg Added method tsGetNetworkIdentification and
#                   modified __init_ to append the methods output to
#                   self.ts_Title. This helps to distinguish local from
#                   from remote tasks when there are multiple sessions
#                   active on a single operator's display.
#
# ToDo:
#
#    2012/01/06 rsg TBD - Expand visual Hot Key support with
#                   associated AcceleratorEntries which would
#                   be needed only for mouseless terminals
#                   (such as vt100 and original cygwin console).
#
#    2012/06/30 rsg Resolve failure of leftClick to change focus
#                   to task associated with operator selected
#                   task bar button.
#
#    2012/07/03 rsg Reconcile need for Show with need for Panel Stack.
#                   (http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/
#                   panels.html). Panel Stack eExample doesn't use
#                   Show, but we need Show to delay creation of
#                   windows until distributed layouts have completed.
#
#################################################################

__title__     = 'tsWxTaskBar'
__version__   = '1.11.0'
__date__      = '01/01/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

import socket
import sys

import time
import curses
import curses.panel

import tsExceptions as tse

import tsWxGlobals as wx
import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxEvent import EVT_SET_FOCUS
from tsReportUtilities import TsReportUtilities as tsrpu
from tsWxAcceleratorEntry import AcceleratorEntry as wxAcceleratorEntry
from tsWxAcceleratorTable import AcceleratorTable as wxAcceleratorTable
from tsWxButton import Button as wxButton
from tsWxFrame import Frame
from tsWxObject import Object as wxObject
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxStaticText import StaticText as wxStaticText
from tsWxTextCtrl import TextCtrl as wxTextCtrl
from tsWxEvent import EVT_COMMAND_LEFT_CLICK

tsWxGTUI_DataBase = tsGTUI.GraphicalTextUserInterface

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

RESOLVED_NEW_PANEL_STACK_ISSUE = True

#---------------------------------------------------------------------------

class TaskBarButton(wxButton):
    '''
    '''
    # Class State Variables
    lastTopTask = None
    lastTopButtonTasks = []

    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 validator=wx.DefaultValidator,
                 name=wx.ButtonNameStr,
                 task=None,
                 useClientArea=True):
        '''
        '''
        # Create Hot Key
        if False and label.find('&') == -1:

            prefix = '&'
            character = ''
            suffix = label

            aLine = prefix.strip() + character.strip() + suffix.strip()

            text = aLine.strip()

        else:

            text = label.strip()

            (prefix,
             character,
             suffix,
             flags) = self.tsParseAcceleratorTextLabel(text)

            aLine = prefix.strip() + character.strip() + suffix.strip()

            text = aLine.strip()

        # Automatically Bind mouse event ASAP (now).
        # Will register event in the SystemEventTable
        # if useClientArea=False.
        wxButton.__init__(self,
                          parent,
                          id=id,
                          label=text,
                          pos=pos,
                          name=name,
                          useClientArea=useClientArea)

        button = self
        self.ts_ButtonSavedForegroundColour = button.ts_ForegroundColour
        self.ts_ButtonSavedButtonBackgroundColour = button.ts_BackgroundColour

        self.ts_ParentSavedForegroundColour = parent.ts_ForegroundColour
        self.ts_ParentSavedButtonBackgroundColour = parent.ts_BackgroundColour

        self.ts_Task = task
        self.ts_TaskSavedForegroundColour = self.ts_Task.ts_ForegroundColour
        self.ts_TaskSavedBackgroundColour = self.ts_Task.ts_BackgroundColour

        if False and \
           DEBUG:
            fmt1 = 'assignedId=%d; label="%s" ' % (self.ts_AssignedId, label)
            fmt2 = 'task=%s ' % task
            fmt3 = 'parent=%s ' % parent
            fmt4 = 'self=%s' % self
            msg = fmt1 + fmt2 + fmt3 + fmt4
            print('DEBUG: tsWxTaskBar.TaskBarButton: %s\n' % msg)

        TaskBarButton.lastTopButtonTasks.append(task)

        theEvent = EVT_COMMAND_LEFT_CLICK # EVT_SET_FOCUS
        # theHandler = self.tsTaskBarButtonOnSetFocus
        theHandler = self.tsOnLeftClick

        # Bind mouse event ASAP (now).
        # Will register event in the SystemEventTable
        # if useSystemEventTable=True.
        self.Bind(theEvent,
                  theHandler,
                  button,
                  useSystemEventTable=True)

        button.Show()
        self.tsTaskBarButtonOnSetFocus()

    #-----------------------------------------------------------------------

    def tsOnLeftClick(self, evt):
        '''
        '''
        self.tsTaskBarButtonOnSetFocus()

        triggeringObject = self.ts_Task
        objectId = triggeringObject.ts_AssignedId

        objectCriteria = 'EVT_COMMAND_LEFT_CLICK ' + \
                         'for [%s]-Button' % self.GetLabel()

        triggeringEvent = EVT_COMMAND_LEFT_CLICK

##        triggeringObject.ProcessEvent(triggeringEvent)

        if False:

            msg = 'tsWxTaskBar.TaskBarButton.tsOnLeftClick ' + \
                  'task=%s; assignedId=%s; earliestAncestor=%s ' % (
                      self.ts_Task,
                      self.ts_Task.ts_AssignedId,
                      self.ts_Task.ts_EarliestAncestor)
            print('NOTICE: %s\n' % msg)

            results = self.tsProcessEventTables(
                objectCriteria=objectCriteria,
                objectId=objectId,
                triggeringEvent=triggeringEvent,
                triggeringObject=triggeringObject)

        else:

            if wx.USE_CURSES_PANEL_STACK:

                msg = 'tsWxTaskBar.TaskBarButton.tsOnLeftClick ' + \
                      'task=%s; assignedId=%s; earliestAncestor=%s ' % (
                          self.ts_Task,
                          self.ts_Task.ts_AssignedId,
                          self.ts_Task.ts_EarliestAncestor)
                print('NOTICE: %s\n' % msg)

                ## self.tsTaskBarDumpPanelStack()

                if self.ts_Task != TaskBarButton.lastTopTask:

                    if DEBUG:

                        msg = 'tsWxTaskBar.TaskBarButton.tsOnLeftClick ' + \
                              '(new panel stack): ' \
                              'ts_Task=%s; lastTopTask=%s' % (
                                  self.ts_Task, TaskBarButton.lastTopTask)

                        print(msg)

                    self.tsTaskBarTopTask(self.ts_Task)

                    if RESOLVED_NEW_PANEL_STACK_ISSUE:

                        # Resolved new panel stack issue
                        for theTask in TaskBarButton.lastTopButtonTasks:

                            if not (theTask != TaskBarButton.lastTopTask):
                                theTask.Show()

                    TaskBarButton.lastTopTask = self.ts_Task

                    if RESOLVED_NEW_PANEL_STACK_ISSUE:

                        # Resolved new panel stack issue
                        TaskBarButton.lastTopTask.Show()

                self.tsCursesPanelUpdatePanels()
                self.tsCursesDoUpdate()

            else:

                msg = 'tsWxTaskBar.TaskBarButton.tsOnLeftClick ' + \
                      '(tsTaskBarTopTask): ' + \
                      'Unable to change focus because ' + \
                      'wx.USE_CURSES_PANEL_STACK=%s.' % str(
                          wx.USE_CURSES_PANEL_STACK)
                print('NOTICE: %s\n' % msg)

                self.ts_Task.Show()

    #-----------------------------------------------------------------------

    def tsTaskBarButtonOnSetFocus(self):
        '''
        '''
        buttonChild = self
        buttonChildTask = buttonChild.ts_Task
        # buttonChildTask.ts_FocusFromKbd = buttonChildTask

        for buttonSibling in buttonChild.ts_Parent.ts_Children:

            if (isinstance(buttonSibling, TaskBarButton)):

                ##### Begin Update TaskBar Buttons
                BackgroundColour = wx.ThemeToUse[
                    'TaskBar']['InactiveFocusBackgroundColour']

                if (buttonSibling == buttonChild):

                    ForegroundColour = wx.ThemeToUse[
                        'TaskBar']['ActiveFocusForegroundColour']

                    if False and DEBUG and VERBOSE:

                        taskFocus = '  Active'

                        for taskChild in buttonSibling.ts_Task.ts_Children:

                            if isinstance(taskChild, wxButton):

                                taskTitle = buttonSibling.ts_Task.ts_Title
                                taskChildLabel = taskChild.ts_Label
                                taskChildRect = taskChild.ts_Rect
                                taskChildClientRect = taskChild.ts_ClientRect
                                taskChildHandle = taskChild.ts_Handle
                                fmt0 = 'Focus=%s; ' % taskFocus
                                fmt1 = 'TaskTitle=%s; ' % taskTitle
                                fmt2 = 'Label=%s; ' % taskChildLabel
                                fmt3 = 'Rect=%s; ' % str(taskChildRect)
                                fmt4 = 'ClientRect=%s; ' % str(
                                    taskChildClientRect)
                                fmt5 = 'Child=%s; ' % str(taskChild)
                                fmt6 = 'Handle=%s' % str(taskChildHandle)
                                msg = fmt0 + fmt1 + fmt2 + fmt3 + \
                                      fmt4 + fmt5 + fmt6
                                print('DEBUG: %s\n' % msg)

                else:

                    BackgroundColour =  wx.ThemeToUse[
                        'TaskBar']['InactiveFocusBackgroundColour']

                    ForegroundColour =  wx.ThemeToUse[
                        'TaskBar']['InactiveFocusForegroundColour']

                    if False and DEBUG and VERBOSE:

                        taskFocus = 'Inactive'

                        for taskChild in buttonSibling.ts_Task.ts_Children:

                            if isinstance(taskChild, wxButton):

                                taskTitle = buttonSibling.ts_Task.ts_Title
                                taskChildLabel = taskChild.ts_Label
                                taskChildRect = taskChild.ts_Rect
                                taskChildClientRect = taskChild.ts_ClientRect
                                taskChildHandle = taskChild.ts_Handle
                                fmt0 = 'Focus=%s; ' % taskFocus
                                fmt1 = 'TaskTitle=%s; ' % taskTitle
                                fmt2 = 'Label=%s; ' % taskChildLabel
                                fmt3 = 'Rect=%s; ' % str(taskChildRect)
                                fmt4 = 'ClientRect=%s; ' % str(
                                    taskChildClientRect)
                                fmt5 = 'Child=%s; ' % str(taskChild)
                                fmt6 = 'Handle=%s' % str(taskChildHandle)
                                msg = fmt0 + fmt1 + fmt2 + fmt3 + \
                                      fmt4 + fmt5 + fmt6
                                print('DEBUG: %s\n' % msg)

                buttonSibling.ts_BackgroundColour = BackgroundColour
                buttonSibling.ts_ForegroundColour = ForegroundColour
                buttonSibling.tsUpdate()
                buttonSibling.Show()
                ##### End Update TaskBar Buttons

    #-----------------------------------------------------------------------

    def tsCreateTaskBarButton(self):
        '''
        Create single or multi-line buttons.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            text = self.ts_Label
            if text != wx.EmptyString:
                if text.find('\n') == -1:
                    self.tsCreateTaskBarButtonLine(text)
                else:
                    self.tsCreateButtonMultiLine(text)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateTaskBarButtonLine(self, theLabel):
        '''
        Create single line button.
        '''
        self.logger.debug(
            'tsCreateButtonLine: theLabel="%s"; rect=%s' % (
                theLabel, str(self.Rect)))

        if theLabel == wx.EmptyString:

            pass

        elif False:

            # RadioButton Not Applicable
            characterCellAttribute = tsGTUI.DISPLAY_REVERSE
            characterCellAccelerator = (
                characterCellAttribute | tsGTUI.DISPLAY_UNDERLINE)
            window = self.ts_Handle

            (prefix,
             character,
             suffix,
             flags) = self.tsParseAcceleratorTextLabel(theLabel)

            aLine = prefix + character + suffix

            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                       pixels=True)
            col = 0 + 0 * borderThickness.width
            row = 0 + 0 * borderThickness.height

            window.attron(characterCellAttribute)

            if self.tsIsBorderStyle(style=self.ts_Style):
                # Adjust for indent, border and space on left and right sides.
                maxCols = len(aLine)
##                maxCols = min(len(aLine),
##                              (self.Rect.width - 5 * borderThickness.width // \
##                               wx.pixelWidthPerCharacter))
                window.addstr(int(row),
                              int(col),
                              '%s' % prefix)
                window.attron(characterCellAccelerator)
                window.addstr(int(row),
                              int(col) + len(prefix),
                              '%s' % character)
                window.attroff(characterCellAccelerator)
                window.addstr(int(row),
                              int(col) + len(prefix) + len(character),
                              '%s' % suffix)
            else:
                # Adjust for indent on left and right sides.
                maxCols = len(aLine)
##                maxCols = min(len(aLine),
##                              (self.Rect.width - 5 * borderThickness.width // \
##                               wx.pixelWidthPerCharacter))
                window.addstr(int(row),
                              int(col),
                              '[%s' % prefix)
                window.attron(characterCellAccelerator)
                window.addstr(int(row),
                              int(col) + len(prefix) + 1,
                              '%s' % character)
                window.attroff(characterCellAccelerator)
                window.addstr(int(row),
                              int(col) + len(prefix) + 1 + len(character),
                              '%s]' % suffix)

            window.attroff(characterCellAttribute)

        else:

            theLabel = '[&%s]' % theLabel
            # print(tsGTUI.GraphicalTextUserInterface.TermName.lower())

            termName = tsGTUI.GraphicalTextUserInterface.TermName.lower()

            if termName == 'xterm':

                # termName == 'xterm'

                # Prefererred config for xterm.
                # Underline also used for menus, checkboxes and radio buttons,
                # Standout only used for Frame and Dialog
                # help, iconize, maximize/restore and close buttons.
                characterCellAttribute = (
                    tsGTUI.DISPLAY_BOLD | tsGTUI.DISPLAY_STANDOUT)
                characterCellAccelerator = (
                    tsGTUI.DISPLAY_UNDERLINE | characterCellAttribute)

            elif termName == 'cygwin':

                # termName == 'cygwin'

                # Prefererred config for cygwin.
                # Cygwin terminals substitute cyan color for underline
                # Reverse also used for menus, checkboxes and radio buttons,
                # Standout only used for Frame and Dialog
                # help, iconize, maximize/restore and close buttons.
                characterCellAttribute = tsGTUI.DISPLAY_BOLD
                characterCellAccelerator = (
                    tsGTUI.DISPLAY_REVERSE | characterCellAttribute)

            else:

                # termName == 'vt100'

                # Prefererred config for vt100.
                # Underline also used for menus, checkboxes and radio buttons,
                # Standout only used for Frame and Dialog
                # help, iconize, maximize/restore and close buttons.
                if self.ts_ForegroundColour == wx.ThemeToUse[
                    'TaskBar']['ActiveFocusForegroundColour']:

                    characterCellAttribute = (
                        tsGTUI.DISPLAY_BOLD | tsGTUI.DISPLAY_STANDOUT)

                else:

                    characterCellAttribute = (
                        tsGTUI.DISPLAY_BOLD)

                characterCellAccelerator = (
                    tsGTUI.DISPLAY_UNDERLINE | characterCellAttribute)


            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                       pixels=True)
            col = 0 + 0 * borderThickness.width
            row = 0 + 0 * borderThickness.height

            ampersandPosition = theLabel.find('&')

            if ampersandPosition == 0:
                prefix = ''
            else:
                prefix = theLabel[0:ampersandPosition]

            character = theLabel[ampersandPosition+1]
            suffix = theLabel[ampersandPosition+2:len(theLabel)]

            self.tsCursesAddStr(col,
                                row,
                                prefix,
                                attr=characterCellAttribute,
                                pixels=False)

            col += len(prefix)
            self.tsCursesAddStr(col,
                                row,
                                character,
                                attr=characterCellAccelerator,
                                pixels=False)

            col += len(character)
            self.tsCursesAddStr(col,
                                row,
                                suffix,
                                attr=characterCellAttribute,
                                pixels=False)

##            col += len(suffix)
##            self.tsCursesAddStr(col, row, separator, attr=None, pixels=False)

    #-----------------------------------------------------------------------

    def tsCreateTaskBarButtonMultiLine(self, text):
        '''
        Create multi-line button.
        '''
        # TBD - Under Construction. Should surround text with border.
        #       Should also support hot key.
        msg = 'NotImplementedError: %s' % \
              'tsCreateButtonMultiLine in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
 
        aLine = text
        borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                   pixels=True)
        col = 1 + 0 * borderThickness.width
        row = 0 + 0 * borderThickness.height

        if aLine != wx.EmptyString:
            characterCellAttribute = tsGTUI.DISPLAY_STANDOUT
            window = self.ts_Handle

            window.attron(characterCellAttribute)
            if self.tsIsBorderStyle(style=self.ts_Style):
                # Adjust for indent, border and space on left and right sides.
                maxCols = min(len(aLine),
                              (self.Rect.width - 4 * borderThickness.width // \
                               wx.pixelWidthPerCharacter))
                window.addstr(int(row), int(col), ' %s ' % aLine[0:maxCols])
            else:
                # Adjust for indent on left and right sides.
                maxCols = min(len(aLine),
                              (self.Rect.width - 4 * borderThickness.width // \
                               wx.pixelWidthPerCharacter))
                window.addstr(int(row), int(col), '[%s]' % aLine[0:maxCols])
            window.attroff(characterCellAttribute)

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Draw the actual features of the Button.
        '''
        if self.tsIsShowPermitted:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            self.tsCreateBorder()
            self.tsCreateTaskBarButton()

#---------------------------------------------------------------------------

class TaskBar(Frame):
    '''
    Class to establish a taskbar icon (button) for each top level
    window (frame, dialog etc.). A taskbar icon appears in the "system
    tray" and responds to mouse clicks, optionally with a tooltip above
    it to help provide information.
    '''
    # Class variables

    baton = ['|', '/', '-', '\\']
    batonID = 0

    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_TASK_STYLE,
                 name=wx.TaskBarNameStr):
        '''
        Construct class.
        '''
        theClass = 'TaskBar'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_title = title
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        Frame.__init__(self,
                       parent,
                       id=id,
                       title=title,
                       pos=pos,
                       size=size,
                       style=style,
                       name=name)

        self.tsBeginClassRegistration(theClass, id)

        (myRect, myClientRect) = self.tsTaskBarLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        self.ts_applicationName = self.logger.applicationName

        self.ts_applicationLabel = None

        self.ts_applicationTime = ' %s %28s' % (
            TaskBar.baton[TaskBar.batonID],
            tsrpu.getDateAndTimeString(time.time()))

        self.ts_applicationProgress = None

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % self.ts_Id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('              title: %s' % title)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)
            self.logger.debug('              stdio: %s' % \
                              self.FindWindowByName(wx.StdioNameStr))

        self.ts_Name = name
        self.ts_Parent = parent

        self.ts_DescendantOrderOfShow = [self.ts_AssignedId]

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
            self.ts_ReserveTaskBarArea == False
            self.ts_ReserveRedirectArea = False
        else:
            self.ts_GrandParent = parent.Parent
            self.ts_ReserveTaskBarArea == parent.ts_ReserveTaskBarArea
            self.ts_ReserveRedirectArea = parent.ts_ReserveRedirectArea

        if name == wx.TaskBarNameStr:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'TaskBar']['BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'TaskBar']['ForegroundColour'].lower()
            self.ts_ReserveTaskBarArea == True

        else:
            self.ts_BackgroundColour = wx.ThemeToUse[
                'BackgroundColour'].lower()
            self.ts_ForegroundColour = wx.ThemeToUse[
                'ForegroundColour'].lower()

##        self.ts_FocusEnabled = True
        self.SetFocus()

        self.ts_ButtonNames = []
        self.ts_Buttons = []
        self.ts_Label = title
        self.ts_Style = style
        self.ts_Host = self.tsGetNetworkIdentification()
        self.ts_Title = '%s @ %s' % (
            title, self.ts_Host) # [0:min(15, len(self.ts_Host))])

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

    def Create(
        self,
        parent,
        id=wx.ID_ANY,
        title=wx.EmptyString,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE,
        name=wx.FrameNameStr,
        pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        (myRect, myClientRect) = self.tsTaskBarLayout(
            parent, pos, size, style, name)
        self.ts_Rect = myRect
        self.ts_ClientRect = myClientRect

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=pixels)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def CreateStatusTitle(self, taskBarRect):
        '''
        Create a status title for the TaskBar that identifies the run-time
        name of the top-level executable module. Right justify it on the
        title line of the TaskBar.
        '''
        if self.ts_applicationLabel is None:

            self.ts_applicationLabel = '%s ' % self.ts_applicationName[0: min(
                len(self.ts_applicationName),
                (taskBarRect.width // \
                 wx.pixelWidthPerCharacter) - (len(self.ts_Title) + 5))]

            parent = self

            baseLabel = self.ts_applicationLabel
            baseStyle = 0 # wx.BORDER_SIMPLE
            baseCol = ((taskBarRect.x + taskBarRect.width) // \
                       wx.pixelWidthPerCharacter) - \
                       (len(self.ts_applicationLabel) + 1) - 1
            baseRow = self.ts_Rect.Top / wx.pixelHeightPerCharacter
            basePos = wx.tsGetPixelValues(baseCol, baseRow)
            if baseStyle == 0:
                baseSize = wx.tsGetPixelValues(len(baseLabel) + 1, 1)
            else:
                baseSize = wx.tsGetPixelValues(len(baseLabel) + 4, 1 + 2)
            self.ts_applicationLabel = wxStaticText(
                parent,
                id=wx.ID_ANY,
                label=baseLabel,
                pos=basePos,
                size=baseSize,
                style=baseStyle,
                validator=wx.DefaultValidator,
                name=wx.StaticTextNameStr)
            self.ts_applicationLabel.Show()

    #-----------------------------------------------------------------------

    def CreateStatusBar(self, taskBarRect):
        '''
        Create a status bar that indicates run-time activity of the
        top-level executable module. When idle, it updates a twirling
        baton and the current date and time of day. An unexpectedly
        long interval between updates indicate that the program is
        too busy or that it has become hung in an infinite loop.
        '''
        TaskBar.batonID = (TaskBar.batonID + 1) % len(TaskBar.baton)

        self.ts_applicationTime = '%s %28s ' % (
            TaskBar.baton[TaskBar.batonID],
            tsrpu.getDateAndTimeString(time.time()))

        if self.ts_applicationProgress is None:
            if False:

                col = ((taskBarRect.x + taskBarRect.width) // \
                       wx.pixelWidthPerCharacter) - \
                       (len(self.ts_applicationTime) + 1)

                row = (wx.ThemeToUse['TaskBar']['WindowHeight'] // \
                       wx.pixelHeightPerCharacter) - 1

                self.tsCursesAddStr(
                    col,
                    row,
                    self.ts_applicationTime,
                    attr=tsGTUI.DISPLAY_NORMAL,
                    pixels=False)

            else:

                parent = self

                baseLabel = self.ts_applicationTime
                baseStyle = 0 # wx.BORDER_SIMPLE
                baseCol = ((taskBarRect.x + taskBarRect.width) // \
                           wx.pixelWidthPerCharacter) - \
                           (len(self.ts_applicationTime) + 1) - 1
                baseRow = self.ts_Rect.Bottom // wx.pixelHeightPerCharacter
                basePos = wx.tsGetPixelValues(baseCol, baseRow)
                if baseStyle == 0:
                    baseSize = wx.tsGetPixelValues(len(baseLabel) + 1, 1)
                else:
                    baseSize = wx.tsGetPixelValues(len(baseLabel) + 4, 1 + 2)
                self.ts_applicationProgress = wxTextCtrl(
                    parent,
                    id=wx.ID_ANY,
                    value=baseLabel,
                    pos=basePos,
                    size=baseSize,
                    style=baseStyle,
                    validator=wx.DefaultValidator,
                    name=wx.TextCtrlNameStr)
                self.ts_applicationProgress.tsShow()
        else:
            self.ts_applicationProgress.SetLabel(self.ts_applicationTime)
            self.ts_applicationProgress.tsShow()

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsGetTaskBarButtonData(self):
        '''
        Create button, for newly activated task, and remov button for newly
        inactivated task. Also need to set and clear focus as appropriate
        to task activity and event notification.

        Define the label and handler for the buttons associated with the
        top-level window "tasks" appearing the TaskBar frame.

        Based on "wxPython In Action" by Noel Rappin and Robin Dunn,
        Manning Publications Co. (See downloaded source code located in
        Chapter-05, goodExampple.py.)
        '''
        #
        # Template = ('~',
        #             tsWxEvent.EVT_SET_FOCUS,
        #             self.OnTaskSetFocus,
        #             'SetTaskFocusButton(%s)' %self.ts_Name)

        try:
            self.tsRegisterShowOrder()
        except Exception as e:
            self.logger.error('%s; %s' % (__title__, e))
 
        theTaskBarTitle = wx.TaskBarTitleStr.split(' ', 1)
        theTaskBarName = theTaskBarTitle[0].strip('_').title()
        col = 1
        row = 1
        msg = ''
        for item in tsWxGTUI_DataBase.WindowTopLevelTasks:
            # TBD - Construct nickname for item using first word.
            # (NOTE: Titles are derived from item.GetLabel()).
            theTitle = item.GetLabel().split(' ', 1)
            theName = theTitle[0].strip('_').title()
            if theName == theTaskBarName:
                # Do not inlude Task Bar in displayed list.
                pass
            elif theName == 'Screen':
                # Do not inlude Console Screen in displayed list.
                pass
            else:
                col += len(msg) + 1
                if theName not in self.ts_ButtonNames:
                    # TBD - Buttons must not be repeated.
                    self.ts_ButtonNames.append(theName)
                    msg = '[%s]' % theName

                    # Automatically Bind mouse event ASAP (now).
                    # Will register event in the SystemEventTable
                    # if useClientArea=False.
                    button = TaskBarButton(
                        self,
                        -1,
                        label=theName,
                        pos=(self.Rect.x + \
                             col * wx.pixelWidthPerCharacter,
                             self.Rect.y + \
                             row * wx.pixelHeightPerCharacter),
                        name='%sButton(%s)' % (theName,
                                               self.Name),
                        task=item,
                        useClientArea=True)

                    # Automatically Bind all mouse events ASAP (now).
                    # Will register event in the SystemEventTable.
                    event = EVT_COMMAND_LEFT_CLICK
                    handler = button.tsOnLeftClick
                    source = button
                    button.Bind(event,
                                handler,
                                source,
                                useSystemEventTable=True)

##                    theEvent = EVT_SET_FOCUS
##                    theHandler = self.tsTaskBarOnSetFocus

##                    # Bind mouse event ASAP (now).
##                    # Will register event in the SystemEventTable
##                    # if useSystemEventTable=True.
##                    self.Bind(theEvent,
##                              theHandler,
##                              button,
##                              useSystemEventTable=True)

                    button.Show()

                    self.ts_Buttons.append(button)

            item.Show()

    #-----------------------------------------------------------------------

    def tsGetClientArea(self, pixels=True):
        '''
        Returns the bounding rectangle the client area of the Frame,
        i.e., without menu bars, tool bars, status bars and such.
        '''
        return (self.ts_ClientRect)

    #-------------------------------------------------------------------

    def tsGetNetworkIdentification(self):
        '''
        Return network hostname.
        '''
        try:
            (socketHostname,
             socketAliaslist,
             socketIpaddrlist) = socket.gethostbyaddr(socket.gethostname())
        except socket.herror:
            socketHostname = socket.gethostname()
            socketAliaslist = []
            socketIpaddrlist = []
        except Exception as errorCode:
            socketHostname = ''
            socketAliaslist = []
            socketIpaddrlist = []
            fmt1 = 'tsWxTaskBar.' + \
                   'tsGetNetworkIdentification: '
            fmt2 = 'errorCode=%s; ' % str(errorCode)
            fmt3 = 'socketHostname=<%s>; ' % socketHostname
            fmt4 = 'socketAliaslist=<%s>; ' % socketAliaslist
            fmt5 = 'socketIpaddrlist=<%s>' % socketIpaddrlist
            msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
            self.logger.error(msg)

        return (socketHostname)

    #-----------------------------------------------------------------------

    def tsTaskBarLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of frame based upon arguments.
        '''
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)
 
        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        if name == wx.TaskBarNameStr:

            myRect = wxObject.TheDisplay.tsGetTaskArea(pixels=True)

        elif thePosition == theDefaultPosition and theSize == theDefaultSize:

            myRect = wxObject.TheDisplay.GetClientArea(pixels=True)

        elif thePosition == theDefaultPosition:

            myRect = wxRect(wxObject.TheDisplay.ClientArea.x,
                            wxObject.TheDisplay.ClientArea.y,
                            theSize.width,
                            theSize.height)

        elif theSize == theDefaultSize:

            theDisplaySize = wxSize(
                wxObject.TheDisplay.ClientArea.width,
                wxObject.TheDisplay.ClientArea.height)

            myRect = wxRect(
                thePosition.x,
                thePosition.y,
                theDisplaySize.width - thePosition.x,
                theDisplaySize.height - thePosition.y)

        else:

            myRect = wxRect(thePosition.x,
                            thePosition.y,
                            theSize.width,
                            theSize.height)

            theDisplayRect = wxObject.TheDisplay.GetClientArea()
            if not theDisplayRect.InsideRect(myRect):
                myRect = wxRect(
                    max(thePosition.x, theDisplayRect.x),
                    max(thePosition.y, theDisplayRect.y),
                    min(theSize.width, theDisplayRect.width),
                    min(theSize.height, theDisplayRect.height - 1))

            if not theDisplayRect.InsideRect(myRect):
                myRect = theDisplayRect

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + theBorder.height,
                              myRect.width - 2 * theBorder.width,
                              myRect.height - 2 * theBorder.height)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; title=%s; myRect=%s' % \
              (parent, pos, size, name, self.Title, myRect)

        self.logger.debug('    tsTaskBarLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def tsTrapIfTooSmall(self, name, myRect):
        '''
        '''
        # TBD - Under Construction.
        if True:
            return

        minScreenDimensions = wx.ThemeToUse['MinScreenDimensions']
        minScreenWidth = minScreenDimensions['FrameWidth']
        minScreenHeight = minScreenDimensions['FrameHeight'] + \
                          minScreenDimensions['MenuBarHeight'] + \
                          minScreenDimensions['ToolBarHeight'] + \
                          minScreenDimensions['StatusBarHeight'] + \
                          minScreenDimensions['RedirectionHeight'] + \
                          minScreenDimensions['TaskBar']['Height']

        minClientHeight = minScreenDimensions['FrameHeight'] + \
                          minScreenDimensions['MenuBarHeight'] + \
                          minScreenDimensions['ToolBarHeight'] + \
                          minScreenDimensions['StatusBarHeight']

        minWidth = minScreenWidth

        if name == wx.TaskBarNameStr:
            minHeight = minScreenDimensions['TaskBar']['Height']

        elif name == wx.StdioNameStr:
            minHeight = minScreenDimensions['RedirectionHeight']

        else:

            minHeight = minClientHeight

        minScreenSize = wxSize(minScreenWidth // wx.pixelWidthPerCharacter,
                               minScreenHeight // wx.pixelHeightPerCharacter)

        mySize = wxSize(myRect.width // wx.pixelWidthPerCharacter,
                        myRect.height // wx.pixelHeightPerCharacter)

        minSize = wxSize(minWidth // wx.pixelWidthPerCharacter,
                         minHeight // wx.pixelHeightPerCharacter)

        actualScreen = wxObject.TheDisplay.GetGeometry(pixels=True)
 
        actualScreenWidth = actualScreen.width
        actualScreenHeight = actualScreen.height
        actualScreenSize = wxSize(actualScreenWidth, actualScreenHeight)

        if actualScreenSize.width < minScreenSize.width:

            fmt = '  Screen "%s" width (%d) is too small.' + \
                  ' Please make screen at least (%d) columns'
            abortMsg = fmt % (wxObject.TheDisplay.Name,
                              actualScreenSize.width,
                              minScreenSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if actualScreenSize.height < minScreenSize.height:

            fmt = '  Screen "%s" height (%d) is too small.' + \
                  ' Please make screen at least (%d) lines'
            abortMsg = fmt % (wxObject.TheDisplay.Name,
                              actualScreenSize.height,
                              minScreenSize.height)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if mySize.width < minSize.width:

            fmt = '  Window "%s" width (%d) is too small.' + \
                  ' Please make screen at least (%d) columns'
            abortMsg = fmt % (name, mySize.width, minSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if mySize.height < minSize.height:

            fmt = '  Window "%s" height (%d) is too small.' + \
                  ' Please make screen at least (%d) lines'
            abortMsg = fmt % (name, mySize.height, minSize.height)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update Frame specific native GUI.
        '''
        if self.ts_Handle is None:
            self.Create(self.ts_Parent,
                        id=self.ts_AssignedId,
                        pos=(self.Position.x, self.Position.y),
                        size=(self.Size.width, self.Size.height),
                        style=self.ts_Style,
                        name=self.ts_Name,
                        pixels=True)

        try:
            self.tsRegisterShowOrder()
        except Exception as e:
            self.logger.error('%s; %s' % (__title__, e))

        self.tsUpdate()

    #-----------------------------------------------------------------------
 
    def tsUpdate(self):
        '''
        Draw the actual features of the Frame.
        '''
        if self.ts_Handle is not None:

            self.tsCursesScrollOk(0)
            self.tsCursesBkgd()
            self.tsCreateBorder()

            if self.ts_Style & wx.CAPTION:
                self.tsCreateTitleLine(self.ts_Title)

            self.tsShowTaskBar()

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def tsShowTaskBar(self):
        '''
        Display the list of top level tasks.
        '''
        # TBD - Replace text output with creation/deletion of the
        # buttons associated with each task.
        try:
            self.tsRegisterShowOrder()
        except Exception as e:
            self.logger.error('%s; %s' % (__title__, e))

        self.tsGetTaskBarButtonData()

        taskBarRect = self.Rect

        self.CreateStatusTitle(taskBarRect)

        self.CreateStatusBar(taskBarRect)

    #-----------------------------------------------------------------------

##    def tsTaskBarOnSetFocus(self):
##        '''
##        '''
##        msg = 'tsWxTaskBar.tsTaskBarOnSetFocus: Event not handled.'
##        print('DEBUG: %s\n' % msg)

##        self.ts_BackgroundColour = 'Black'
##        self.ts_ForegroundColour = 'Red'
##        if True:

##            self.tsUpdate()
##            self.Show()

    #-----------------------------------------------------------------------

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    ClientArea = property(tsGetClientArea)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
