#! /usr/bin/env python
# "Time-stamp: <01/25/2015  6:56:36 AM rsg>"
'''
tsWxWindow.py - Base class for all windows and represents any
visible object on the screen. All controls, top level windows
and so on are wx.Windows. Sizers and device contexts are not
however, as they do not appear on screen themselves.
'''
#################################################################
#
# File: tsWxWindow.py
#
# Purpose:
#
#    Base class for all windows and represents any visible object
#    on the screen. All controls, top level windows and so on are
#    wx.Windows. Sizers and device contexts are not however, as
#    they do not appear on screen themselves.
#
# Usage (example):
#
#    # Import
#
#    from tsWxWindow import Window
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
#    The wxPython emulator introduces the concept of the Earliest
#    Ancestor for each Top-Level Window and decendent child window.
#    The intent is to facilitate visibility determination when
#    windows are fully or partially overlaid by windows associated
#    with another Top-Level Window. Unless the application developer
#    or user has designted the Top-Level Window to have focus, the
#    emulator will assume that components of newer Top-Level Windows
#    should overlay components of older Top-Level Windows.
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
#    Window
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#    Window.AcceptsFocus
#    Window.AcceptsFocusFromKeyboard
#    Window.AcceptsFocusRecursively
#    Window.AddChild
#    Window.AddPendingEvent
#    Window.AdjustForLayoutDirection
#    Window.AdjustForParentClientOriginXY
#    Window.AlwaysShowScrollbars
#    Window.AssociateHandle
#    Window.CacheBestSize
#    Window.CanScroll
#    Window.CanSetTransparent
#    Window.CaptureMouse
#    Window.Center
#    Window.CenterOnParent
#    Window.CenterOnScreen
#    Window.Centre
#    Window.CentreOnParent
#    Window.CentreOnScreen
#    Window.ClearBackground
#    Window.ClientToScreen
#    Window.ClientToScreenXY
#    Window.ClientToWindowSize
#    Window.Close
#    Window.ConvertDialogPixels
#    Window.ConvertDialogPointToPixels
#    Window.ConvertDialogSizeToPixels
#    Window.ConvertPixelPointToDialog
#    Window.ConvertPixelSizeToDialog
#    Window.ConvertPixelsToDialog
#    Window.Create
#    Window.DLG_PNT
#    Window.DLG_SZE
#    Window.Destroy
#    Window.DestroyChildren
#    Window.Disable
#    Window.DissociateHandle
#    Window.DoCaptureMouse
#    Window.DoCentre
#    Window.DoFindFocus
#    Window.DoGetBestClientSize
#    Window.DoGetBestSize
#    Window.DoGetBorderSize
#    Window.DoGetScreenPosition
#    Window.DoGetSibling
#    Window.DoGetVirtualSize
#    Window.DoPhase
#    Window.DoReleaseMouse
#    Window.DoSetSizeHints
#    Window.DoSetVirtualSize
#    Window.DoSetWindowVariant
#    Window.DoUpdateWindowUI
#    Window.DragAcceptFiles
#    Window.Enable
#    Window.FindFocus
#    Window.FindWindowById
#    Window.FindWindowByLabel
#    Window.FindWindowByName
#    Window.Fit
#    Window.FitInside
#    Window.Freeze
#    Window.GetAcceleratorTable
#    Window.GetAccessible
#    Window.GetAdjustedBestSize
#    Window.GetAttributeValueFromColorPair
#    Window.GetAutoLayout
#    Window.GetBackgroundColour
#    Window.GetBackgroundStyle
#    Window.GetBestFittingSize
#    Window.GetBestSize
#    Window.GetBestSizeTuple
#    Window.GetBestVirtualSize
#    Window.GetBorder
#    Window.GetCapture
#    Window.GetCaret
#    Window.GetCharHeight
#    Window.GetCharWidth
#    Window.GetChildren
#    Window.GetClassDefaultAttributes
#    Window.GetClientAreaOrigin
#    Window.GetClientRect
#    Window.GetClientSize
#    Window.GetClientSizeConstraintWH
#    Window.GetClientSizeTuple
#    Window.GetConstraints
#    Window.GetContainingSizer
#    Window.GetCursor
#    Window.GetDefaultAttributes
#    Window.GetDefaultBorder
#    Window.GetDefaultBorderForControl
#    Window.GetDlgUnitBase
#    Window.GetDropTarget
#    Window.GetEffectiveMinSize
#    Window.GetEventHandler
#    Window.GetExtraStyle
#    Window.GetFont
#    Window.GetForegroundColour
#    Window.GetFullTextExtent
#    Window.GetGrandParent
#    Window.GetGtkWidget
#    Window.GetHandle
#    Window.GetHelpText
#    Window.GetHelpTextAtPoint
#    Window.GetId
#    Window.GetLabel
#    Window.GetLayoutDirection
#    Window.GetMainWindowOfCompositeControl
#    Window.GetMaxClientSize
#    Window.GetMaxHeight
#    Window.GetMaxSize
#    Window.GetMaxWidth
#    Window.GetMinClientSize
#    Window.GetMinHeight
#    Window.GetMinSize
#    Window.GetMinWidth
#    Window.GetName
#    Window.GetNextSibling
#    Window.GetParent
#    Window.GetPopupMenuSelectionFromUser
#    Window.GetPopupMenuSelectionFromUserXY
#    Window.GetPosition
#    Window.GetPositionConstraintXY
#    Window.GetPositionTuple
#    Window.GetPrevSibling
#    Window.GetRect
#    Window.GetScreenPosition
#    Window.GetScreenPositionTuple
#    Window.GetScreenRect
#    Window.GetScrollPos
#    Window.GetScrollRange
#    Window.GetScrollThumb
#    Window.GetSize
#    Window.GetSizeConstraintWH
#    Window.GetSizeTuple
#    Window.GetSizer
#    Window.GetStyle
#    Window.GetTextExtent
#    Window.GetThemeEnabled
#    Window.GetToolTip
#    Window.GetToolTipText
#    Window.GetTopLevelAncestor
#    Window.GetTopLevelParent
#    Window.GetTopLevelSiblings
#    Window.GetUpdateClientRect
#    Window.GetUpdateRegion
#    Window.GetValidator
#    Window.GetVirtualSize
#    Window.GetVirtualSizeTuple
#    Window.GetWindowBorderSize
#    Window.GetWindowStyle
#    Window.GetWindowStyleFlag
#    Window.GetWindowVariant
#    Window.HandleAsNavigationKey
#    Window.HandleWindowEvent
#    Window.HasCapture
#    Window.HasExtraStyle
#    Window.HasFlag
#    Window.HasFocus
#    Window.HasMultiplePages
#    Window.HasScrollbar
#    Window.HasTransparentBackground
#    Window.Hide
#    Window.HideWithEffect
#    Window.HitTest
#    Window.HitTestXY
#    Window.InformFirstDirection
#    Window.InheritAttributes
#    Window.InheritsBackgroundColour
#    Window.InitDialog
#    Window.InternalOnSize
#    Window.InvalidateBestSize
#    Window.IsBeingDeleted
#    Window.IsDoubleBuffered
#    Window.IsEnabled
#    Window.IsExposed
#    Window.IsExposedPoint
#    Window.IsExposedRect
#    Window.IsFrozen
#    Window.IsRetained
#    Window.IsScrollbarAlwaysShown
#    Window.IsShown
#    Window.IsShownOnScreen
#    Window.IsThisEnabled
#    Window.IsTopLevel
#    Window.Layout
#    Window.LayoutPhase1
#    Window.LayoutPhase2
#    Window.LineDown
#    Window.LineUp
#    Window.Lower
#    Window.MakeModal
#    Window.Move
#    Window.MoveAfterInTabOrder
#    Window.MoveBeforeInTabOrder
#    Window.MoveConstraint
#    Window.MoveXY
#    Window.Navigate
#    Window.NavigateIn
#    Window.NewControlId
#    Window.NextControlId
#    Window.NotifyWindowOnEnableChange
#    Window.OnClose
#    Window.OnHelp
#    Window.OnInitDialog
#    Window.OnInternalIdle
#    Window.OnMaximize
#    Window.OnMinimize
#    Window.OnRestoreDown
#    Window.PageDown
#    Window.PageUp
#    Window.PopEventHandler
#    Window.PopupMenu
#    Window.PopupMenuXY
#    Window.PostCreate
#    Window.PostSizeEvent
#    Window.PostSizeEventToParent
#    Window.PrepareDC
#    Window.PrevControlId
#    Window.ProcessEvent
#    Window.ProcessPendingEvents
#    Window.ProcessThreadEvent
#    Window.ProcessWindowEvent
#    Window.ProcessWindowEventLocally
#    Window.PushEventHandler
#    Window.QueueEvent
#    Window.Raise
#    Window.Refresh
#    Window.RefreshRect
#    Window.RegisterHotKey
#    Window.ReleaseMouse
#    Window.RemoveChild
#    Window.RemoveEventHandler
#    Window.Reparent
#    Window.ResetConstraints
#    Window.SafelyProcessEvent
#    Window.SatisfyConstraints
#    Window.ScreenToClient
#    Window.ScreenToClientXY
#    Window.ScrollLines
#    Window.ScrollPages
#    Window.ScrollWindow
#    Window.SendDestroyEvent
#    Window.SendIdleEvents
#    Window.SendSizeEvent
#    Window.SendSizeEventToParent
#    Window.SetAcceleratorTable
#    Window.SetAccessible
#    Window.SetAutoLayout
#    Window.SetBackgroundColour
#    Window.SetBackgroundStyle
#    Window.SetBestSize
#    Window.SetBestVirtualSize
#    Window.SetBorder
#    Window.SetCanFocus
#    Window.SetCaret
#    Window.SetClientAreaOrigin
#    Window.SetClientRect
#    Window.SetClientSize
#    Window.SetClientSizeWH
#    Window.SetConstraintSizes
#    Window.SetConstraints
#    Window.SetContainingSizer
#    Window.SetCursor
#    Window.SetDimensions
#    Window.SetDoubleBuffered
#    Window.SetDropTarget
#    Window.SetEventHandler
#    Window.SetExtraStyle
#    Window.SetFocus
#    Window.SetFocusFromKbd
#    Window.SetFont
#    Window.SetForegroundColour
#    Window.SetHelpText
#    Window.SetHelpTextForId
#    Window.SetId
#    Window.SetInitialBestSize
#    Window.SetInitialSize
#    Window.SetLabel
#    Window.SetLayoutDirection
#    Window.SetMaxClientSize
#    Window.SetMaxSize
#    Window.SetMinClientSize
#    Window.SetMinSize
#    Window.SetName
#    Window.SetNextHandler
#    Window.SetOwnBackgroundColour
#    Window.SetOwnFont
#    Window.SetOwnForegroundColour
#    Window.SetPalette
#    Window.SetParent
#    Window.SetPosition
#    Window.SetPreviousHandler
#    Window.SetRect
#    Window.SetScrollPos
#    Window.SetScrollbar
#    Window.SetSize
#    Window.SetSizeConstraint
#    Window.SetSizeHints
#    Window.SetSizeWH
#    Window.SetSizer
#    Window.SetSizerAndFit
#    Window.SetStyle
#    Window.SetThemeEnabled
#    Window.SetToolTip
#    Window.SetToolTipString
#    Window.SetTopLevelAncestor
#    Window.SetTopLevelSiblings
#    Window.SetTransparent
#    Window.SetValidator
#    Window.SetVirtualSize
#    Window.SetVirtualSizeHints
#    Window.SetVirtualSizeHintsSz
#    Window.SetVirtualSizeWH
#    Window.SetWindowStyle
#    Window.SetWindowStyleFlag
#    Window.SetWindowVariant
#    Window.ShouldInheritColours
#    Window.Show
#    Window.ShowWithEffect
#    Window.Thaw
#    Window.ToggleWindowStyle
#    Window.TransferDataFromWindow
#    Window.TransferDataToWindow
#    Window.UnregisterHotKey
#    Window.UnreserveControlId
#    Window.UnsetConstraints
#    Window.UnsetToolTip
#    Window.Update
#    Window.UpdateWindowUI
#    Window.UseBgCol
#    Window.Validate
#    Window.WarpPointer
#    Window.WindowToClientSize
#    Window.__del__
#    Window.__init__
#    Window.theMainApplication
#    Window.tsBuildCursesNewWindowGenealogy
#    Window.tsCreateBorder
#    Window.tsCreateButton
#    Window.tsCreateButtonLine
#    Window.tsCreateButtonMultiLine
#    Window.tsCreateLabel
#    Window.tsCreateLabelLine
#    Window.tsCreateLabelMultiLine
#    Window.tsCreateMenuBar
#    Window.tsCreateScrollBarButton
#    Window.tsCreateScrollBarButtonLine
#    Window.tsCreateScrollBarButtonMultiLine
#    Window.tsCreateStatusLabel
#    Window.tsCreateStatusLabelLine
#    Window.tsCreateStatusLabelMultiLine
#    Window.tsCreateTitleLine
#    Window.tsFindWindowByAssignedId
#    Window.tsGetCharacterRectangle
#    Window.tsGetCharacterSize
#    Window.tsGetCharacterValues
#    Window.tsGetClassInstanceFromTuple
#    Window.tsGetParentCharacterRectangleData
#    Window.tsGetParentPosition
#    Window.tsGetParentSize
#    Window.tsGetPixelSize
#    Window.tsGetPixelValues
#    Window.tsGetRectangle
#    Window.tsGetTheId
#    Window.tsInternalOnSize
#    Window.tsIsBorderStyle
#    Window.tsIsBorderThickness
#    Window.tsIsShowPermitted
#    Window.tsOnHelp
#    Window.tsOnInitDialog
#    Window.tsOnMiddleDown
#    Window.tsOnSysColourChanged
#    Window.tsParseAcceleratorTextLabel
#    Window.tsRegisterClassWindow
#    Window.tsRegisterKeyboardInputOrder
#    Window.tsRegisterShowOrder
#    Window.tsResetShowOrder
#    Window.tsRoundHorizontal
#    Window.tsRoundVertical
#    Window.tsRoundXY
#    Window.tsSetCharHeight
#    Window.tsSetCharWidth
#    Window.tsShow
#    Window.tsStripAcceleratorTextLabel
#    Window.tsTaskBarDumpPanelStack
#    Window.tsTaskBarTopChild
#    Window.tsTaskBarTopTask
#    Window.tsTrapIfTooSmall
#    Window.tsUnRegisterKeyboardInputOrder
#    Window.tsUpdate
#    Window.tsWindowLayout
#    Window.wxGetMetricOrDefault
#    Window.wxHasRealChildren
#
# Modifications:
#
#    2010/03/07 rsg Added event handlers for OnClose, OnMaximize and
#                   OnMinimize.
#
#    2010/03/19 rsg Enabled SetAcceleratorTable. Needed because
#                   cygwin terminal does not support mouse.
#
#    2010/07/16 rsg Modified tsCreateButtonLine to support
#                   use of "&" to designate accelerator
#                   character.
#
#    2010/08/10 rsg Added ts_HotKeyData to retain location of "&"
#                   which designates the accelerator character and
#                   the applicable Alt-Ctrl-Shift key combination.
#
#    2010/08/27 rsg Modified tsBuildCursesNewWindowGenealogy to
#                   capture data from self.ts_SystemEventTable
#                   and self.ts_UserEventTable.
#
#    2010/08/31 rsg For consistancy with wxPython and industry
#                   conventions, changed characterCellAccelerator
#                   to "tsGTUI.DISPLAY_UNDERLINE"
#                   from "tsGTUI.DISPLAY_BOLD".
#
#    2010/10/20 rsg Simplify Window.Layout method's access to
#                   Sizer.Layout.
#
#    2011/12/04 rsg Corrected tsIsBorderStyle. Return False when
#                   style == 0 or style == wx.BORDER_NONE.
#
#    2011/12/05 rsg Applied bold attribute to tsCreateLabelLine.
#
#    2011/12/17 rsg Added self.ts_PanelLayer invocation in
#                   tsRegisterClassWindow in order to track
#                   curses.panel type objects.
#
#    2011/12/26 rsg Added logic to tsWindowLayout to inhibit
#                   operation once self.ts_Handle has been
#                   assigned a curses window identifier.
#
#    2011/12/28 rsg Modified SetFocusFromKbd by adding
#                   curses.doupdate() after
#                   curses.panel.update_panels().
#
#    2011/12/29 rsg Added tsCursesHasColors to prevent
#                   application from trapping if terminal
#                   (such as vt100) only supports black on
#                   white or white on black.
#
#    2012/01/15 rsg Removed code for unused originalAlgorothm
#                   from tsBuildCursesNewWindowGenealogy method.
#
#    2012/01/17 rsg Added conditional logic to RegisterClassWindow
#                   that creates and registers a curses panel
#                   layer only when a new windows has an
#                   associated handle. The conditional logic also
#                   was moved ahead of the data base update logic
#                   to correct the erroneous PanelLayer = None.
#
#    2012/01/19 rsg Revert back to Show without any ShowTiled and
#                   ShowOverlayed special cases.
#
#    2012/01/20 rsg Modified tsRegisterShowOrder to register
#                   PanelLayer in addition to AssignedId.
#
#    2012/01/20 rsg Modified tsRegisterShowOrder to register
#                   AssignedIdByPanelLayer.
#
#    2012/01/25 rsg Added OrderOfShowPanelStack to tsRegisterShowOrder.
#
#    2012/01/25 rsg Substituted "tsWxGTUI_DataBase" in references
#                   to "tsGTUI.GraphicalTextUserInterface".
#
#    2012/01/31 rsg Revised tsIsBorderStyle to apply BORDER_MASK
#                   to ignore non-border styles.

#    2012/02/04 rsg Added tsRoundHorizontal and tsRoundVertical
#                   methods.
#
#    2012/02/16 rsg Modified tsOn... to invoke
#                   tsProcessSelectedEventTable.
#
#    2012/02/21 rsg Removed tsProcessSelectedEventTable because it
#                   and its controller, tsProcessEventTable, are
#                   provided by tsWxEvtHandler.
#
#    2012/03/05 rsg Added split option to tsRoundHorizontal and
#                   tsRoundVertical methods.
#
#    2012/03/05 rsg Added tsRoundXY method which combines the
#                   actions of methods tsRoundHorizontal and
#                   tsRoundVertical.
#
#    2012/03/12 rsg Added tsCursesInch and tsCursesInstr methods.
#
#    2012/03/29 rsg Applied wx.DISPLAY_NON_COLOR_ATTRIBUTE_MASK
#                   to ensure that only font style attributes are
#                   passed to curses for non-color displays (such
#                   as vt100 and vt220).
#
#    2012/05/01 rsg Added logic to tsBuildCursesNewWindowGenealogy
#                   for including DescendantOrderOfShow.
#
#    2012/05/05 rsg Modified tsCursesInch to return attribute
#                   in addition to the character.
#
#    2012/06/08 rsg Replaced references to EventObject by ones
#                   to EventSource so as to conform to
#                   class definition for tsWxEvent.
#
#    2012/07/01 rsg Added registration of WindowsByHandle, WindowsByPad
#                   and WindowsByPanelLayer in GraphicalTextUserInterface
#                   class.
#
#    2012/07/03 rsg Added tsCursesDoUpdate, tsCursesPanelUpdatePanels,
#                   tsCursesWindowNoutRefresh and
#                   tsCursesWindowRedrawWin.
#
#    2012/07/07 rsg Imported curses.textpad. Added tsCursesBeep,
#                   tsCursesTextPad and its associated methods.
#
#    2012/07/19 rsg Added class variable TheKeyboardInputRecipient.
#
#    2012/07/21 rsg Added the following curses interface modules, in
#                   support of tsWxTextEntryDialog:
#                   tsCursesEcho, tsCursesFlash, tsCursesFlushInp,
#                   tsCursesMoveCursor and tsCursesNoEcho.
#
#    2012/08/15 rsg Added methods to erase or clear the various
#                   portions of the windows associated with curses
#                   handles.
#
#    2012/09/18 rsg Added logic to tsCursesCaretVisibility that
#                   returns the previous or default visibility level.
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
#    2013/07/10 rsg Various updates associated with panel layer
#                   hiding when closing and iconizing a window.
#
#    2013/07/18 rsg Added method tsIsShowPermitted to facilitate
#                   the imposition of a permanent CLOSE or temporary
#                   ICONIZE override to the permission for showing of
#                   a window, ita children and its ancestors.
#
#    2013/10/25 rsg Added Troubleshooting definitions and applied
#                   them to definition of DEBUG.
#
#    2014/01/03 rsg Updated Copyright.
#
#    2014/01/13 rsg Replaced references to tsGTUI.color256 by references
#                   to tsGTUI.xterm256Color for compatibility with the
#                   re-designed tsWxGraphicalTextUserInterface module.
#
#    2014/05/11 rsg Resolved compatibility with Python 3.3 and 3.4 by
#                   replacing "import curses." by "from curses import ".
#                   This resulted in the followin:
#
#                   "import curses"
#                   "from curses import ascii"
#                   "from curses import error" as cursesErrorMethod
#                   "from curses import panel"
#                   "from curses import textpad"
#                   "from curses import wrapper"
#
#                   "import _curses"
#                   "from _curses import error" as _cursesErrorMethod
#
#    2014/05/19 rsg Interchanged position of boilerplate for Classes
#                   and Methods and added alphabetical list of methods.
#
#    2014/05/22 rsg Added tsCursesPflush method in attempt to apply
#                   wx.USE_CURSES_PANEL_STACK.
#
#    2014/06/09 rsg Modified tsCursesInch to use mask 0xFFFFFF00 instead
#                   of 0xFF00 to extract character attribute.
#
#    2014/06/28 rsg Added tsWindowCurses import and reference to
#                   faciltate introduction of additional curses services.
#
#    2014/07/10 rsg Added attribute 'WindowsByCursesPanel' to
#                   'GraphicalTextUserInterface' and modified
#                   'start' to facilitate use of curses panel object
#                   id for anticipated use, by 'tsWxEventLoop',
#                   to determine the associated wxPython object
#                   id and curses panel stacking order.
#
#    2014/07/13 rsg Modified tsRegisterClassWindow to add a curses
#                   panel layer for the curses "stdscr" so that the
#                   panel mechanism will include new output during
#                   panel type updates.
#
#    2015/01/25 rsg Modified tsRegisterClassWindow to include
#                   'WindowAssignedIdByCursesPanelLayer' in the
#                   TerminalRunTimeEnvironment.log database. The
#                   intent is to facilitate task bar initiated focus
#                   changes when wx.USE_CURSES_PALEL_STACK is True.
#
# ToDo:
#
#    2011/12/26 rsg Troubleshoot tsWindowLayout. Resolve why
#                   Window based Controls do not initialize via
#                   self.ts_Handle = None. Thought I did that for:
#                   Button, CheckBox, Gauge, RadioBox, RadioButton,
#                   StaticText, TaskBarButton and TextCtrl.
#
#    2011/12/28 rsg Research SetFocusFromKbd. Need to discover
#                   what new information needs to be set and what
#                   old information needs to be cleared.
#                   NOTE: SetFocusFromKbd actions need to be
#                   coordinated with those of TaskBar.
#
#################################################################

__title__     = 'tsWxWindow'
__version__   = '1.28.0'
__date__      = '01/25/2015'
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

import curses
##from curses import ascii
from curses import panel
from curses import textpad
##from curses import wrapper
#
import _curses

import os
import sys
import types
import traceback

from textwrap import TextWrapper

import tsExceptions as tse
import tsLogger

from tsApplication import TsApplication as TsApplication
from tsReportUtilities import TsReportUtilities as tsrpu

import tsWxGlobals as wx
import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxWindowCurses import WindowCurses
from tsWxEvent import EVT_CLOSE
from tsWxEvent import EVT_HELP
from tsWxEvent import EVT_INIT_DIALOG
from tsWxEvent import EVT_MIDDLE_DOWN
from tsWxEvent import EVT_SIZE
from tsWxEvent import EVT_SYS_COLOUR_CHANGED
from tsWxEvent import Event
from tsWxEvent import wxEVT_DESTROY
from tsWxEvtHandler import EvtHandler
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxSystemSettings import SystemSettings as wxSystemSettings

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

tsWxGTUI_DataBase = tsGTUI.GraphicalTextUserInterface

DEFAULT_POS = wxPoint(wx.DefaultPosition)
DEFAULT_SIZE = wxSize(wx.DefaultSize)

#--------------------------------------------------------------------------

class Window(WindowCurses, EvtHandler):
    '''
    wx.Window is the base class for all windows and represents any visible
    object on the screen. All controls, top level windows and so on are
    wx.Windows. Sizers and device contexts are not however, as they do not
    appear on screen themselves.
    '''
    #
    # Styles
    #
    # wx.BORDER_SIMPLE  Displays a thin border around the window.
    #
    # wx.BORDER_DOUBLE  Displays a double border. Windows and Mac only.
    #
    # wx.BORDER_SUNKEN  Displays a sunken border.
    #
    # wx.BORDER_RAISED  Displays a raised border.
    #
    # wx.BORDER_STATIC  Displays a border suitable for a static control.
    #                   Windows only.
    #
    # wx.BORDER_NONE    Displays no border, overriding the default border
    #                   style for the window.
    #
    # wx.TRANSPARENT_WINDOW The window is transparent, that is, it will
    #                   not receive paint events. Windows only.
    #
    # wx.TAB_TRAVERSAL  Use this to enable tab traversal for non-dialog
    #                   windows.
    #
    # wx.WANTS_CHARS    Use this to indicate that the window wants to get
    #                   all char/key events for all keys - even for keys
    #                   like TAB or ENTER which are usually used for dialog
    #                   navigation and which wouldn't be generated without
    #                   this style. If you need to use this style in order
    #                   to get the arrows or etc., but would still like to
    #                   have normal keyboard navigation take place, you
    #                   should create and send a wxNavigationKeyEvent in
    #                   response to the key events for Tab and Shift-Tab.
    #
    # wx.NO_FULL_REPAINT_ON_RESIZE Disables repainting the window
    #                   completely when its size is changed. You will have
    #                   to repaint the new window area manually if you use
    #                   this style. As of version 2.5.1 this style is on by
    #                   default. Use wx.FULL_REPAINT_ON_RESIZE to deactivate
    #                   it.
    #
    # wx.VSCROLL        Use this style to enable a vertical scrollbar. Notice
    #                   that this style cannot be used with native controls
    #                   which don't support scrollbars nor with top-level
    #                   windows in most ports.
    #
    # wx.HSCROLL        Use this style to enable a horizontal scrollbar. The
    #                   same limitations as for wx.VSCROLL apply to this style.
    #
    # wx.ALWAYS_SHOW_SB If a window has scrollbars, disable them
    #                   instead of hiding them when they are not needed
    #                   (i.e. when the size of the window is big enough
    #                   to not require the scrollbars to navigate it). This
    #                   style is currently only implemented for wxMSW and
    #                   wxUniversal and does nothing on the other platforms.
    #
    # wx.CLIP_CHILDREN  Use this style to eliminate flicker caused by the
    #                   background being repainted, then children being
    #                   painted over them. Windows only.
    #
    # wx.FULL_REPAINT_ON_RESIZE Use this style to force a complete
    #                   redraw of the window whenever it is resized instead
    #                   of redrawing just the part of the window affected
    #                   by resizing. Note that this was the behaviour by
    #                   default before 2.5.1 release and that if you
    #                   experience redraw problems with the code which
    #                   previously used to work you may want to try this.
    #
    # Extra Styles
    #
    # wx.WS_EX_VALIDATE_RECURSIVELY By default,
    #                   Validate/TransferDataTo/FromWindow() only work on
    #                   direct children of the window (compatible behaviour).
    #                   Set this flag to make them recursively descend into
    #                   all subwindows.
    #
    # wx.WS_EX_BLOCK_EVENTS wx.CommandEvents and the objects of the
    #                   derived classes are forwarded to the parent window
    #                   and so on recursively by default. Using this flag
    #                   for the given window allows to block this propagation
    #                   at this window, i.e. prevent the events from being
    #                   propagated further upwards. Dialogs have this flag
    #                   on by default.
    #
    # wx.WS_EX_TRANSIENT Don't use this window as an implicit parent
    #                   for the other windows: this must be used with
    #                   transient windows as otherwise there is the risk
    #                   of creating a dialog/frame with this window as a
    #                   parent which would lead to a crash if the parent
    #                   is destroyed before the child.
    #
    # wx.WS_EX_PROCESS_IDLE This window should always process idle
    #                   events, even if the mode set by wx.IdleEvent.SetMode
    #                   is wx.IDLE_PROCESS_SPECIFIED.
    #
    # wx.WS_EX_PROCESS_UI_UPDATES This window should always process UI
    #                   update events, even if the mode set by
    #                   wx.UpdateUIEvent.SetMode is
    #                   wxUPDATE_UI_PROCESS_SPECIFIED.
    #
    # Events emitted by this class
    #
    #   Event macros for events emitted by this class:
    #
    #   EVT_ACTIVATE(id, func):
    #     Process a wxEVT_ACTIVATE event. See wxActivateEvent.
    #
    #   EVT_CHILD_FOCUS(func):
    #     Process a wxEVT_CHILD_FOCUS event. See wxChildFocusEvent.
    #
    #   EVT_CONTEXT_MENU(func):
    #     A right click (or other context menu command depending on
    #     platform) has been detected. See wxContextMenuEvent.
    #
    #   EVT_HELP(id, func):
    #     Process a wxEVT_HELP event. See wxHelpEvent.
    #
    #   EVT_HELP_RANGE(id1, id2, func):
    #     Process a wxEVT_HELP event for a range of ids. See wxHelpEvent.
    #
    #   EVT_DROP_FILES(func):
    #     Process a wxEVT_DROP_FILES event. See wxDropFilesEvent.
    #
    #   EVT_ERASE_BACKGROUND(func):
    #     Process a wxEVT_ERASE_BACKGROUND event. See wxEraseEvent.
    #
    #   EVT_SET_FOCUS(func):
    #     Process a wxEVT_SET_FOCUS event. See wxFocusEvent.
    #
    #   EVT_KILL_FOCUS(func):
    #     Process a wxEVT_KILL_FOCUS event. See wxFocusEvent.
    #
    #   EVT_IDLE(func):
    #     Process a wxEVT_IDLE event. See wxIdleEvent.
    #
    #   EVT_JOY_*(func):
    #     Processes joystick events. See wxJoystickEvent.
    #
    #   EVT_KEY_DOWN(func):
    #     Process a wxEVT_KEY_DOWN event (any key has been pressed).
    #     See wxKeyEvent.
    #
    #   EVT_KEY_UP(func):
    #     Process a wxEVT_KEY_UP event (any key has been released).
    #
    #   EVT_CHAR(func):
    #     Process a wxEVT_CHAR event. See wxKeyEvent.
    #
    #   EVT_MOUSE_CAPTURE_LOST(func):
    #     Process a wxEVT_MOUSE_CAPTURE_LOST event.
    #     See wxMouseCaptureLostEvent.
    #
    #   EVT_MOUSE_CAPTURE_CHANGED(func):
    #     Process a wxEVT_MOUSE_CAPTURE_CHANGED event.
    #     See wxMouseCaptureChangedEvent.
    #
    #   EVT_MOUSE_*(func):
    #     See wxMouseEvent.
    #
    #   EVT_PAINT(func):
    #     Process a wxEVT_PAINT event. See wxPaintEvent.
    #
    #   EVT_POWER_*(func):
    #     The system power state changed. See wxPowerEvent.
    #
    #   EVT_SCROLLWIN_*(func):
    #     Process scroll events. See wxScrollWinEvent.
    #
    #   EVT_SET_CURSOR(func):
    #     Process a wxEVT_SET_CURSOR event. See wxSetCursorEvent.
    #
    #   EVT_SIZE(func):
    #     Process a wxEVT_SIZE event. See wxSizeEvent.
    #
    #   EVT_SYS_COLOUR_CHANGED(func):
    #     Process a wxEVT_SYS_COLOUR_CHANGED event.
    #     See wxSysColourChangedEvent.

    # Window Sizing Overview

    #   It can sometimes be confusing to keep track of the various
    #   size-related attributes of a wxWindow, how they relate to each
    #   other, and how they interact with sizers.
    #
    #   This section will attempt to clear the fog a little, and give
    #   some simple explanations of things.

    # Glossary
    #
    #    "Best Size": the best size of a widget depends on what kind of
    #    widget it is, and usually also on the contents of the widget.
    #    For example a wxListBox's best size will be calculated based
    #    on how many items it has, up to a certain limit, or a wxButtons
    #    best size will be calculated based on its label size, but
    #    normally won't be smaller than the platform default button
    #    size (unless a style flag overrides that). There is a special
    #    virtual method in the C++ window classes called
    #    wxWindow::DoGetBestSize() that a class needs to override if
    #    it wants to calculate its own best size based on its content.
    #
    #    "Minimal Size": the minimal size of a widget is a size that is
    #    normally explicitly set by the programmer either with the
    #    wxWindow::SetMinSize() method or with the
    #    wxWindow::SetSizeHints() method. Most controls will also set
    #    the minimal size to the size given in the controls constructor
    #    if a non-default value is passed. Top-level windows such as
    #    wxFrame will not allow the user to resize the frame below the
    #    minimal size.
    #
    #    "Maximum Size": just like for the minimal size, the maximum
    #    size is normally explicitely set by the programmer with the
    #    wxWindow::SetMaxSize() method or with wxWindow::SetSizeHints().
    #    Top-level windows such as wxFrame will not allow the user to
    #    resize the frame above the maximum size.
    #
    #    "Size": the size of a widget can be explicitly set or fetched
    #    with the wxWindow::SetSize() or wxWindow::GetSize() methods.
    #    This size value is the size that the widget is currently using
    #    on screen and is the way to change the size of something that
    #    is not being managed by a sizer.
    #
    #    "Client Size": the client size represents the widgets area
    #    inside of any borders belonging to the widget and is the area
    #    that can be drawn upon in a EVT_PAINT event. If a widget does
    #    not have a border then its client size is the same as its size.
    #
    #    "Initial Size": the initial size of a widget is the size given
    #    to the constructor of the widget, if any. As mentioned above
    #    most controls will also set this size value as the controls
    #    minimal size. If the size passed to the constructor is the
    #    default wxDefaultSize, or if the size is not fully specified
    #    (such as wxSize(150,-1)) then most controls will fill in the
    #    missing size components using the best size and will set the
    #    initial size of the control to the resulting size.
    #
    #    "Virtual Size": the virtual size is the size of the potentially
    #    viewable area of the widget. The virtual size of a widget may
    #    be larger than its actual size and in this case scrollbars will
    #    appear to the let the user 'explore' the full contents of the
    #    widget. See wxScrolled for more info.

    #-----------------------------------------------------------------------
    # Class Variables
    TheKeyboardInputRecipients = []

    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id=-1,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 name=wx.PanelNameStr):
        '''
        Constructs a window, which can be a child of a frame, dialog
        or any other non-control window.
        '''
        theClass = 'Window'

        # Capture initial caller parametsrs before they are changed
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style
        self.caller_name = name

        wx.RegisterFirstCallerClassName(self, theClass)

        WindowCurses.__init__(self)
        EvtHandler.__init__(self)

        #-------------------------------------------------------------------
        # Begin WindowBase.__init__(self)

        # no window yet, no parent nor children
        self.ts_Parent = None
        self.ts_WindowId = wx.ID_ANY
        self.ts_WindowObjectState = None

        # no constraints on the minimal window size
        self.ts_MaxHeight = wx.DefaultCoord
        self.ts_MaxWidth = wx.DefaultCoord
        self.ts_MinHeight = wx.DefaultCoord
        self.ts_MinWidth = wx.DefaultCoord

        # invalidiated cache value
        self.ts_BestSizeCache = DEFAULT_SIZE

        # window are created enabled and visible by default
        self.ts_IsShown = True
        self.ts_IsEnabled = True

        # the default event handler is just this window
        self.ts_EventHandler = self

        if wx.USE_VALIDATORS:
            # no validators
            self.ts_WindowValidator = None

        # the colours/fonts are default for now, so leave m_font,
        # m_backgroundColour and m_foregroundColour uninitialized
        # and set those
        self.ts_HasBgCol = False
        self.ts_HasFgCol = False
        self.ts_HasFont = False
        self.ts_InheritBgCol = False
        self.ts_InheritFgCol = False
        self.ts_InheritFont = False

        # no style bits
        self.ts_ExStyle = 0
        self.ts_WindowStyle = 0

        self.ts_BackgroundStyle = wx.BG_STYLE_ERASE

        # no constraints whatsoever
        if wx.USE_CONSTRAINTS:
            self.ts_Constraints = None
            self.ts_ConstraintsInvolvedIn = None

        if wx.USE_DRAG_AND_DROP:
            self.ts_DropTarget = None

        if wx.USE_TOOLTIPS:
            self.ts_ToolTip = None

        if wx.USE_CARET:
            self.ts_Caret = None

        if wx.USE_PALETTE:
            self.ts_HasCustomPalette = False

        if wx.USE_ACCESSIBILITY:
            self.ts_Accessible = False

        self.ts_WindowSizer = None
        self.ts_ContainingSizer = None
        self.ts_AutoLayout = False

        self.ts_VirtualSize = DEFAULT_SIZE

        self.ts_ScrollHelper = None

        self.ts_WindowVariant = wx.WINDOW_VARIANT_NORMAL

##        if wx.USE_SYSTEM_OPTIONS:
##            if ( wxSystemOptions.HasOption(wxWINDOW_DEFAULT_VARIANT) ):

##                self.ts_WindowVariant = wxSystemOptions.GetOptionInt(
##                    wxWINDOW_DEFAULT_VARIANT)

        # Whether we're using the current theme for this window (wxGTK
        # only for now)
        self.ts_ThemeEnabled = False

        # This is set to true by SendDestroyEvent() which should be
        # called by the most derived class to ensure that the destruction
        # event is sent as soon as possible to allow its handlers to
        # still see the undestroyed window
        self.ts_IsBeingDeleted = False

        self.ts_FreezeCount = 0

        # End WindowBase.__init__(self)
        #-------------------------------------------------------------------

        self.tsBeginClassRegistration(theClass, id)

        if ((pos == (wx.DefaultCoord, wx.DefaultCoord)) and \
            (size == ((wx.DefaultCoord, wx.DefaultCoord)))):

            self.ts_Rect = wxRect(-1, -1, -1, -1)
            self.ts_ClientRect = self.ts_Rect

        else:

            (myRect, myClientRect) = self.tsWindowLayout(
                parent, pos, size, style, name)
            self.ts_Rect = myRect
            self.ts_ClientRect = myClientRect

        thePosition = self.Position
        theSize = self.Size

        tsWxGTUI_DataBase.WindowsByAssignedId[
            self.ts_AssignedId] = self
        tsWxGTUI_DataBase.WindowsById[self.ts_Id] = self
        tsWxGTUI_DataBase.WindowsByName[name] = self

        if DEBUG:
            self.logger.debug('               self: %s' % self)
            self.logger.debug('             parent: %s' % parent)
            self.logger.debug('                 id: %s' % id)
            self.logger.debug('         AssignedId: %s' % self.ts_AssignedId)
            self.logger.debug('                pos: %s' % thePosition)
            self.logger.debug('               size: %s' % theSize)
            self.logger.debug('              style: 0x%X' % style)
            self.logger.debug('               name: %s' % name)

        self.ts_Name = name
        self.ts_Parent = parent

        self.ts_HotKeyData = None

        theTopLevelClass = self
        self.SetTopLevelAncestor(theTopLevelClass)

        if parent is None:
            self.ts_GrandParent = None
            tsWxGTUI_DataBase.WindowTopLevelTasks += [self]
            self.logger.debug(
                '           theTasks: %s' % \
                tsWxGTUI_DataBase.WindowTopLevelTasks)
        else:
            self.ts_GrandParent = parent.Parent
            parent.AddChild(self)

        self.ts_BackgroundColour = wx.ThemeToUse['BackgroundColour'].lower()
        self.ts_ForegroundColour = wx.ThemeToUse['ForegroundColour'].lower()

        self.ts_BestSize = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        self.ts_BestVirtualSize = wxSize(self.ts_Rect.width,
                                         self.ts_Rect.height)
        self.ts_BestSizeCache = self.ts_BestSize
        self.ts_CaptureMouse = False
##        self.ts_ClientAreaOrigin = wxPoint(self.ts_Rect.x, self.ts_Rect.y)
        self.ts_ClientRect = self.ts_Rect
##        self.ts_ClientSize = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        self.ts_Cursor = self.ClientAreaOrigin
        self.ts_DoubledBuffered = False
        self.ts_EffectiveMinSize = wxSize(self.ts_Rect.width,
                                          self.ts_Rect.height)

        self.ts_Freeze = False
        self.ts_MaxHeight = self.ts_Rect.height
        self.ts_MaxSize = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        self.ts_MaxWidth = self.ts_Rect.width
        self.ts_MinHeight = self.ts_Rect.height
        self.ts_MinSize = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        self.ts_MinWidth = self.ts_Rect.width
        self.ts_ScreenPosition = wxPoint(0, 0)
        self.ts_Size = wxSize(self.ts_Rect.width, self.ts_Rect.height)
        self.ts_VirtualSize = wxSize(self.ts_Rect.width, self.ts_Rect.height)

        # Create _StandardScreen window if not previously done.
        self.ts_AcceleratorTable = wx.NullAcceleratorTable
        self.ts_AcceptFiles = False
        self.ts_AutoLayout = False
        self.ts_BackgroundColour = wx.COLOR_WHITE
        self.ts_BackgroundStyle = wx.BG_STYLE_SYSTEM
        self.ts_BestSizeCache = None
        self.ts_Border = wx.BORDER_SIMPLE
        self.ts_ButtonText = None
        self.ts_Caret = None
        self.ts_CharHeight = wx.pixelHeightPerCharacter
        self.ts_CharWidth = wx.pixelWidthPerCharacter
        self.ts_Children = []
        self.ts_Constraints = None
        self.ts_ContainingSizer = None
        self.ts_DefaultAttributes = None
        self.ts_DropTarget = None
        self.ts_Enabled = False # Set True when window accepts user input
        self.ts_EventHandler = None
        self.ts_ExtraStyle = None
        self.ts_FocusFromKbd = None
        self.ts_Font = 'courier'
        self.ts_ForegroundColour = wx.COLOR_BLACK
        self.ts_GtkWidget = None
        self.ts_Handle = None
        self.ts_HasFocus = False
        self.ts_HelpText = None
        self.ts_Label = wx.EmptyString
        self.ts_LayoutDirection = None
        self.ts_RefreshWindowAndChildren = False
        self.ts_RefreshOnlyThisRect = None
        self.ts_RefreshEraseBackground = False
        self.ts_Shown = False
        self.ts_Sizer = None
        self.ts_Style = style
        self.ts_Text = None
        self.ts_ThemeEnabled = False
        self.ts_Title = None
        self.ts_ToolTip = None
        self.ts_TopLevel = None
        self.ts_TopLevelParent = None
        self.ts_UpdateClientRect = None
        self.ts_UpdateRegion = None
        self.ts_Validator = None
        self.ts_Virtual_Size = None

##        self.ts_WindowAssignedIdByCursesPanelLayer = {}
##        self.ts_WindowAssignedIdByCursesPanelLayer[
##            'name'] = 'WindowAssignedIdByCursesPanelLayer'

        self.ts_WindowSizer = None
        self.ts_WindowStyle = None
        self.ts_WindowStyleFlag = None
        self.ts_WindowVariant = None

        self.ts_WinCaptureChanging = False
        self.ts_WinCaptureCurrent = None
        self.ts_WinCaptureNext = []

        self.ts_FocusEnabled = False

        self.ts_SystemSettings = wxSystemSettings()

        self.ts_PanelLayer = None
        self.ts_PanelLayerIsHidden = False # Set True to disable update/show

        # Automatically Bind all mouse events ASAP (now).
        # Will register event in the SystemEventTable.
        localEventHandlers = [
            (EVT_HELP, self.tsOnHelp),
            (EVT_INIT_DIALOG, self.tsOnInitDialog),
            (EVT_MIDDLE_DOWN, self.tsOnMiddleDown),
            (EVT_SIZE, self.tsInternalOnSize),
            (EVT_SYS_COLOUR_CHANGED, self.tsOnSysColourChanged)
        ]

        if wx.USE_HELP:
            if parent is None:
                # Top Level Window is responsible for creating the
                # HELP Push Button and associated event handler.
                pass
            else:
                # SubWindow is responsible for creating the
                # HELP Push Button and associated event handler.
                localEventHandlers.append((EVT_HELP, self.tsOnHelp))

        for (event, handler) in localEventHandlers:
            source = self
            self.Bind(event,
                      handler,
                      source,
                      useSystemEventTable=True)

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        Destructor.

        Deletes all sub-windows, then deletes itself. Instead of using the
        delete operator explicitly, you should normally use Destroy() so
        that wxWidgets can delete a window only when it is safe to do so,
        in idle time.
        '''
        msg = 'NotImplementedError: %s' % '__del__ in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        self.logger.wxASSERT_MSG(
##            self.GetCapture() != self,
##            'attempt to destroy window with mouse capture')

##        # FIXME: if these 2 cases result from programming errors in the
##        #        user code we should probably assert here instead of
##        #        silently fixing them

##        # Just in case the window has been Closed, but we're then deleting
##        # immediately: don't leave dangling pointers.
##        wxPendingDelete.DeleteObject(self)

##        # Just in case we've loaded a top-level window via LoadNativeDialog but
##        # we weren't a dialog class
##        wxTopLevelWindows.DeleteObject((wxWindow*)this)

##        # Any additional event handlers should be popped before the window is
##        # deleted as otherwise the last handler will be left with a dangling
##        # pointer to this window result in a difficult to diagnose crash later on.
##        wxASSERT_MSG( GetEventHandler() == this,
##                        wxT("any pushed event handlers must have been removed") )

##    #if wx.USE_MENUS
##        # The associated popup menu can still be alive, disassociate from it in
##        # this case
##        if ( wxCurrentPopupMenu && wxCurrentPopupMenu->GetInvokingWindow() == this )
##            wxCurrentPopupMenu->SetInvokingWindow(NULL)
##    #endif # wx.USE_MENUS

##        wxASSERT_MSG( GetChildren().GetCount() == 0, wxT("children not destroyed") )

##        # notify the parent about this window destruction
##        if ( m_parent )
##            m_parent->RemoveChild(this)

##    #if wx.USE_CARET
##        delete m_caret
##    #endif # wx.USE_CARET

##    #if wx.USE_VALIDATORS
##        delete m_windowValidator
##    #endif # wx.USE_VALIDATORS

##    #if wx.USE_CONSTRAINTS
##        # Have to delete constraints/sizer FIRST otherwise sizers may try to look
##        # at deleted windows as they delete themselves.
##        DeleteRelatedConstraints()

##        if ( m_constraints )
##        {
##            # This removes any dangling pointers to this window in other windows'
##            # constraintsInvolvedIn lists.
##            UnsetConstraints(m_constraints)
##            wxDELETE(m_constraints)
##        }
##    #endif # wx.USE_CONSTRAINTS

##        if ( m_containingSizer )
##            m_containingSizer->Detach( (wxWindow*)this )

##        delete m_windowSizer

##    #if wx.USE_DRAG_AND_DROP
##        delete m_dropTarget
##    #endif # wx.USE_DRAG_AND_DROP

##    #if wx.USE_TOOLTIPS
##        delete m_tooltip
##    #endif # wx.USE_TOOLTIPS

##    #if wx.USE_ACCESSIBILITY
##        delete m_accessible
##    #endif

##    #if wx.USE_HELP
##        # NB: this has to be called unconditionally, because we don't know
##        #     whether this window has associated help text or not
##        wxHelpProvider *helpProvider = wxHelpProvider::Get()
##        if ( helpProvider )
##            helpProvider->RemoveHelp(this)
##    #endif
##    }

    #-----------------------------------------------------------------------

    def AcceptsFocus(self):
        '''
        This method may be overridden in the derived classes to return false
        to indicate that this control does not accept input at all
        '''
        return (True)

    #-----------------------------------------------------------------------

    def AcceptsFocusFromKeyboard(self):
        '''
        This method may be overridden in the derived classes to return false
        to indicate that while this control can, in principle, have focus if
        the user clicks it with the mouse, it should not be included in the
        TAB traversal chain when using the keyboard.
        '''
        return (True)

    #-----------------------------------------------------------------------

    def AcceptsFocusRecursively(self):
        '''
        Overridden to indicate whether this window or one of its children
        accepts focus.
        '''
        return (True)

    #-----------------------------------------------------------------------

    def AddChild(self, child):
        '''
        Adds a child window. This is called automatically by window creation
        functions so should not be required by the application programmer.
        '''
        self.logger.wxCHECK_RET(
            (not (child is None)),
            'Window.AddChild: cannot add a NULL child')

        # this should never happen and it will lead to a crash later if it
        # does because RemoveChild() will remove only one node from the
        # children list and the other(s) one(s) will be left with dangling
        # pointers in them
        self.logger.wxASSERT_MSG(
            (not (child in self.GetChildren())),
            'Window.AddChild: called twice')

        self.GetChildren().append(child)
        child.SetParent(self)

        # adding a child while frozen will assert when thawed, so freeze it
        # as if it had been already present when we were frozen
        if ((self.IsFrozen()) and \
            (not (child.IsTopLevel()))):

            child.Freeze()

    #-----------------------------------------------------------------------

    def AddPendingEvent(self, event):
        '''
        See ProcessEvent() for more info about why you should not use
        this function and the reason for making this function protected
        in wxWindow.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'AddPendingEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def AdjustForLayoutDirection(self, x, width, widthTotal):
        '''
        Mirror coordinates for RTL layout if this window uses it and
        if the mirroring is not done automatically like Win32.
        '''
        if (self.GetLayoutDirection() == wx.Layout_RightToLeft):
            return (widthTotal - x - width)
        else:
            return (x)

    #-----------------------------------------------------------------------

    def AdjustForParentClientOriginXY(self, x, y, sizeFlags):
        '''
        '''
        # don't do it for the dialogs/frames - they float independently
        # of their parent
        if (not (self.IsTopLevel())):

            parent = self.GetParent()
            if ((not (sizeFlags & wx.SIZE_NO_ADJUSTMENTS)) and \
                (not (parent is None))):

                pt = parent.GetClientAreaOrigin()
                x += pt.x
                y += pt.y

        return (wxPoint(x, y))

    #-----------------------------------------------------------------------

    def AlwaysShowScrollbars(self):
        '''
        Call this function to force one or both scrollbars to be always
        shown, even if the window is big enough to show its entire contents
        without scrolling.
        '''
        msg = 'NotImplementedError: %s' % 'AlwaysShowScrollbars in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def AssociateHandle(self, handle):
        '''
        Associate the window with a new native handle.
        '''
        self.ts_Handle = handle

    #-----------------------------------------------------------------------

    def CacheBestSize(self, size):
        '''
        Sets the cached best size value.
        '''
        self.ts_BestSizeCache = size

    #-----------------------------------------------------------------------

    def CanScroll(self, orient):
        '''
        Returns True if this window can have a scroll bar in this
        orientation.
        '''
        msg = 'NotImplementedError: %s' % 'CanScroll in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def CanSetTransparent(self):
        '''
        Returns true if the system supports transparent windows and
        calling SetTransparent() may succeed.

        If this function returns false, transparent windows are definitely
        not supported by the current system.

        Reimplemented in wxTopLevelWindow.

        NOTE: On X-windows systems the X server must have the composite
        extension loaded, and there must be a composite manager program
        (such as xcompmgr) running.
        '''
        return (False)

    #-----------------------------------------------------------------------

    def CaptureMouse(self):
        '''
        Directs all mouse input to this window.

        Call ReleaseMouse() to release the capture.

        Note that wxWindows maintains the stack of windows having captured
        the mouse and when the mouse is released the capture returns to the
        window which had had captured it previously and it is only really
        released if there were no previous window. In particular, this means
        that you must release the mouse as many times as you capture it,
        unless the window receives the wx.MouseCaptureLostEvent event.

        Any application which captures the mouse in the beginning of some
        operation must handle wx.MouseCaptureLostEvent and cancel this
        operation when it receives the event. The event handler must not
        recapture mouse.
        '''
        if True:
            self.ts_CaptureMouse = True
        else:
            msg = 'NotImplementedError: %s' % 'CaptureMouse in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        self.ts_CaptureMouse = True

##        wxLogTrace(wxT("mousecapture"),
##                   wxT("CaptureMouse(%p)"),
##                   static_cast<void*>(this));

##        self.logger.wxASSERT_MSG(
##            not self.ts_WinCaptureChanging,
##            'recursive CaptureMouse call?')

##        self.ts_WinCaptureChanging = True

##        winOld = self.GetCapture()
##        if (not (winOld is None)):

##            winOld.DoReleaseMouse()

##            # save it on stack
##            item = new wxWindowNext
##            item.win = winOld
##            item.next = self.ts_WinCaptureNext
##            self.ts_WinCaptureNext = item

##        # else: no mouse capture to save

##        self.DoCaptureMouse()
##        self.ts_WinCaptureCurrent = self

##        self.ts_WinCaptureChanging = False

    #-----------------------------------------------------------------------

    def Center(self, direction=wx.BOTH):
        '''
        Centers the window. The parameter specifies the direction for
        cetering, and may be wx.HORIZONTAL, wx.VERTICAL or wx.BOTH. It may
        also include wx.CENTER_ON_SCREEN flag if you want to center the
        window on the entire screen and not on its parent window. If it is
        a top-level window and has no parent then it will always be centered
        relative to the screen.
        '''
        self.Centre(direction=direction)

    #-----------------------------------------------------------------------

    def CenterOnParent(self, dir=wx.BOTH):
        '''
        Center with respect to the the parent window.
        '''
        self.CentreOnParent(dir=dir)

    #-----------------------------------------------------------------------

    def CenterOnScreen(self, direction=wx.BOTH):
        '''
        Center the window on screen.
        '''
        self.CentreOnScreen(direction=direction)

    #-----------------------------------------------------------------------

    def Centre(self, direction=wx.BOTH):
        '''
        Centers the window. The parameter specifies the direction for
        cetering, and may be wx.HORIZONTAL, wx.VERTICAL or wx.BOTH. It may
        also include wx.CENTER_ON_SCREEN flag if you want to center the
        window on the entire screen and not on its parent window. If it is
        a top-level window and has no parent then it will always be centered
        relative to the screen.
        '''
        if self.Parent is None or \
           direction == wx.CENTER_ON_SCREEN:
            # Center within Screen
            self.CentreOnScreen(direction)
        else:
            self.CentreOnParent(direction)

    #-----------------------------------------------------------------------

    def CentreOnParent(self, dir=wx.BOTH):
        '''
        Center with respect to the the parent window.
        '''
        if self.Parent is None:
            # Center within Screen
            self.CentreOnScreen(direction=dir)
        else:
            parent = self.Parent
            (parentX, parentY) = (self.Parent.Position.x,
                                  self.Parent.Position.y)
            (parentWidth, parentHeight) = (self.Parent.Size.width,
                                           self.Parent.Size.height)

            (childX, childY) = (self.Position.x,
                                self.Position.y)

            (childWidth, childHeight) = (self.Size.width,
                                         self.Size.height)
            theChildSize = wxSize(childWidth, childHeight)

            if dir == wx.HORIZONTAL:
                # Horizontally center within Parent
                # Retain Parent vertical position
                theChildPosition = wxPoint(
                    parentX + ((parentWidth - childWidth) // 2),
                    parentY)

            elif dir == wx.VERTICAL:
                # Vertically center within Parent
                # Retain Parent horizontal position
                theChildPosition = wxPoint(
                    parentX,
                    parentY + ((parentHeight - childHeight) // 2))

            else:
                # Center within Parent
                theChildPosition = wxPoint(
                    parentX + ((parentWidth - childWidth) // 2),
                    parentY + ((parentHeight - childHeight) // 2))

            baseX, offsetX = divmod(theChildPosition.x,
                                    wx.pixelWidthPerCharacter)
            baseY, offsetY = divmod(theChildPosition.y,
                                    wx.pixelHeightPerCharacter)

            self.Rect = wxRect(theChildPosition.x - offsetX,
                               theChildPosition.y - offsetY,
                               theChildSize.width,
                               theChildSize.height)

            self.logger.debug(
                '     CentreOnParent: %s.' % (str(self.Rect)))

        # Report information equivalent to that of tsFrameLayout.
        try:
            pos = wxPoint(self.Position.x, self.Position.y)
            size = wxSize(self.Size.width, self.Size.height)
            name = self.Name
            msg = 'parent=%s; pos=%s; size=%s; name=%s; Rect=%s' % \
                (parent, pos, size, name, self.Rect)
        except AttributeError:
            msg = 'Rect=%s' % self.Rect

        self.logger.debug('    CentreOnParen: %s' % msg)

    #-----------------------------------------------------------------------

    def CentreOnScreen(self, direction=wx.BOTH):
        '''
        Center the window on screen.
        '''
        parent = None
        theDisplay = self.display
        theParentArea = theDisplay.GetClientArea(pixels=True)

        (parentX, parentY) = (
            theParentArea.x, theParentArea.y)

        (parentWidth, parentHeight) = (
            theParentArea.width,
            theParentArea.height)

        theChildPos = wxPoint(self.Position.x, self.Position.y)

        theChildSize = wxSize(self.Size.width, self.Size.height)

        (childX, childY) = (theChildPos.x, theChildPos.y)

        (childWidth, childHeight) = (theChildSize.width, theChildSize.height)

        # Adjust theChildPosition for specified centering.
        if direction == wx.HORIZONTAL:
            # Adjust for parent top horizontal center
            theChildPosition = wxPoint(
                ((parentWidth - childWidth) // 2),
                parentY)

        elif direction == wx.VERTICAL:
            # Adjust for parent left vertical center
            theChildPosition = wxPoint(
                parentX,
                ((parentHeight - childHeight) // 2))

        else:
            # Adjust for parent horizontal and vertical center
            theChildPosition = wxPoint(
                ((parentWidth - childWidth) // 2),
                ((parentHeight - childHeight) // 2))

        baseX, offsetX = divmod(theChildPosition.x, wx.pixelWidthPerCharacter)
        baseY, offsetY = divmod(theChildPosition.y, wx.pixelHeightPerCharacter)

        myRect = wxRect(theChildPosition.x - offsetX,
                        theChildPosition.y - offsetY,
                        theChildSize.width,
                        theChildSize.height)

        # Report information equivalent to that of tsFrameLayout.
        try:
            pos = wxPoint(theChildPos.x,
                          theChildPos.y)
            size = wxSize(theChildSize.width,
                          theChildSize.height)
            name = self.Name
            msg = 'parent=%s; pos=%s; size=%s; name=%s; myRect=%s' % \
                (parent, pos, size, name, myRect)

        except AttributeError:
            msg = 'myRect=%s' % myRect

        self.logger.debug('    CenterOnScreen: %s' % msg)

        self.Rect = myRect

        # TBD - Trial
##        if self.ts_MenuBar is not None:
##            self.ts_MenuBar.Rect.Offset(offset)
##        for child in self.Children:
##            child.Rect.Offset(offset)

    #-----------------------------------------------------------------------

    def ClearBackground(self):
        '''
        Clears the window by filling it with the current background colour.

        Does not cause an erase background event to be generated.

        Notice that this uses wxClientDC to draw on the window and the
        results of doing it while also drawing on wxPaintDC for this
        window are undefined. Hence this method should not be used
        from EVT_PAINT handlers, just use wxDC::Clear() on the wxPaintDC
        you already use there instead.
        '''
        self.ts_Handle.bkgd(
            ' ',
            self.stdscr.tsGetAttributeValueFromColorPair(
                self.GetForegroundColour(),
                self.GetBackgroundColour()))

    #-----------------------------------------------------------------------

    def ClientToScreen(self, pt):
        '''
        Converts to screen coordinates from coordinates relative to this
        window.
        '''
        if self.Parent is None:
            return (pt)
        else:
            return (self.Parent.ClientToScreen(
                wxPoint(pt.x + self.Parent.Position.x,
                        pt.y + self.Parent.Position.y)))

    #-----------------------------------------------------------------------

    def ClientToScreenXY(self, x, y):
        '''
        Converts to screen coordinates from coordinates relative to this
        window.
        '''
        return (self.ClientToScreen((x, y)))

    #-----------------------------------------------------------------------

    def ClientToWindowSize(self, size):
        '''
        Converts client area size size to corresponding window size.
        '''
        # const wxSize diff(GetSize() - GetClientSize());
        #
        # return wxSize(size.x == -1 ? -1 : size.x + diff.x,
        #               size.y == -1 ? -1 : size.y + diff.y);

        diff = self.GetSize() - self.GetClientSize()
        result = wxSize(0, 0)

        if (size.x == -1):
            result.x = -1
        else:
            result.x =  size.x + diff.x

        if (size.y == -1):
            result.y = -1
        else:
            result.y =  size.y + diff.y

        return (result)

    #-----------------------------------------------------------------------

    def Close(self, force=True):
        '''
        This function simply generates a wxCloseEvent whose handler usually
        tries to close the window.

        It does not close the window itself, however.

        Parameters:
        force   false if the windows close handler should be able to veto
        the destruction of this window, true if it cannot.

        Remarks:
        Close calls the close handler for the window, providing an
        opportunity for the window to choose whether to destroy the window.
        Usually it is only used with the top level windows (wxFrame and
        wxDialog classes) as the others are not supposed to have any special
        OnClose() logic. The close handler should check whether the window
        is being deleted forcibly, using wxCloseEvent::CanVeto, in which
        case it should destroy the window using wxWindow::Destroy. Note
        that calling Close does not guarantee that the window will be
        destroyed; but it provides a way to simulate a manual close of
        a window, which may or may not be implemented by destroying the
        window. The default implementation of wxDialog::OnCloseWindow
        does not necessarily delete the dialog, since it will simply
        simulate an wxID_CANCEL event which is handled by the appropriate
        button event handler and may do anything at all. To guarantee
        that the window will be destroyed, call wxWindow::Destroy instead.
        '''
        if True:

            msg = 'NotImplementedError: %s' % 'Close in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            event = Event(EVT_CLOSE, self.ts_WindowId)
            event.SetEventSource(self)
            event.SetCanVeto(not force)

            # return false if window wasn't closed because the application
            # vetoed the close event
            return (self.HandleWindowEvent(event) and \
                    (not event.GetVeto()))

    #-----------------------------------------------------------------------

    def ConvertDialogPixels(self, pt):
        '''
        Converts a point or size from dialog units to pixels.

        For the x dimension, the dialog units are multiplied by the
        fixed point character width. For the y dimension, the dialog
        units are multiplied by the fixed point character height.

        Remarks:
        Dialog units are used for maintaining a dialogs proportions
        even if the font changes. You can also use these functions
        programmatically. A convenience macro is defined:
        define wxDLG_UNIT(parent, pt) parent->ConvertDialogToPixels(pt)
        '''
        if isinstance(pt, wxPoint):
            return (self.ConvertDialogPointToPixels(pt))
        else:
            return (self.ConvertDialogSizeToPixels(pt))

    #-----------------------------------------------------------------------

    def ConvertDialogPointToPixels(self, pt):
        '''
        Converts a point or size from dialog units to pixels.
        '''
        return (self.tsGetPixelValues(pt.x, pt.y))

    #-----------------------------------------------------------------------

    def ConvertDialogSizeToPixels(self, sz):
        '''
        Converts a point or size from dialog units to pixels.
        '''
        return (self.tsGetPixelValues(sz.width, sz.height))

    #-----------------------------------------------------------------------

    def ConvertPixelPointToDialog(self, pt):
        '''
        Converts a point or size from pixel units to dialog units.
        '''
        return (self.tsGetCharacterValues(pt.x, pt.y))

    #-----------------------------------------------------------------------

    def ConvertPixelsToDialog(self, pt):
        '''
        Converts a point or size from pixels to dialog units.

        For the x dimension, the pixels are divided by the fixed point
        character width. For the y dimension, the pixels are divided
        by the fixed point character height.

        Remarks:
        Dialog units are used for maintaining a dialogs proportions even
        if the font changes.
        '''
        if isinstance(pt, wxPoint):
            return (self.ConvertPixelPointToDialog(pt))
        else:
            return (self.ConvertPixelSizeToDialog(pt))

    #-----------------------------------------------------------------------

    def ConvertPixelSizeToDialog(self, sz):
        '''
        Converts a point or size from pixel units to dialog units.
        '''
        return (self.tsGetCharacterValues(sz.width, sz.height))

    #-----------------------------------------------------------------------

    def Create(
        self,
        parent,
        id=-1,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=0,
        name=wx.PanelNameStr,
        pixels=True):
        '''
        Create the GUI part of the Window for 2-phase creation mode.
        '''
        if parent is None:
            myParent = self.stdscr
        else:
            myParent = parent
            if size != DEFAULT_SIZE:
                self.SetMinSize(size)

        if wx.USE_VALIDATORS:
            if (not (self.ts_Parent is None)) and \
               ((self.ts_Parent.GetExtraStyle() & \
                 wx.WS_EX_VALIDATE_RECURSIVELY) != 0):

                self.SetExtraStyle(
                    self.GetExtraStyle() | wx.WS_EX_VALIDATE_RECURSIVELY)

        myRect = self.tsGetRectangle(pos, size)

        self.ts_Handle = self.tsCursesNewWindow(myRect, pixels=True)

        return (self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def DLG_PNT(self, pt):
        '''
        Converts a point or size from dialog units to pixels. Dialog units
        are used for maintaining a dialog proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        '''
        return (self.ConvertDialogPointToPixels(pt))

    #-----------------------------------------------------------------------

    def DLG_SZE(self, sz):
        '''
        Converts a point or size from dialog units to pixels. Dialog units
        are used for maintaining a dialog proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        '''
        return (self.ConvertPixelPointToDialog(sz))

    #-----------------------------------------------------------------------

    def Destroy(self):
        '''
        Destroys the window safely.

        Use this function instead of the delete operator, since different
        window classes can be destroyed differently. Frames and dialogs
        are not destroyed immediately when this function is called -- they
        are added to a list of windows to be deleted on idle time, when
        all the windows events have been processed. This prevents problems
        with events being sent to non-existent windows.

        Returns:
        true if the window has either been successfully deleted, or it has
        been added to the list of windows pending real deletion.
        '''
        try:

            self.logger.debug(
                '  Destroy %s.' % self.ts_Handle)
            # TBD - Python does not include the "delwin" method.
            # curses.delwin(self.ts_Handle)
            self.SendDestroyEvent()

            del self

            return (True)

        except AttributeError as e:

            msg = '  Destroy Failed: %s.' % str(e)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            return (False)

    #-----------------------------------------------------------------------

    def DestroyChildren(self):
        '''
        Destroys all children of a window.
        '''
        for child in self.ts_Children:

            try:

                self.logger.debug(
                    '  DestroyChildren %s.' % child)
                # TBD - Would like to use curses.delwin(Child._Handle)
                del child
                self.ts_Children.remove(child)

            except Exception as errorCode:

                msg = '  DestroyChildren Failed: %s.' % str(errorCode)
                self.logger.debug(msg)

        return (self.Children == [])

    #-----------------------------------------------------------------------

    def Disable(self):
        '''
        Disables the window for user input, same as Enable(False).
        '''
        if self.Enabled:
            self.Enabled = False
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def DissociateHandle(self):
        '''
        Dissociate the current native handle from the window.
        '''
        self.ts_Handle = None

    #-----------------------------------------------------------------------

    def DoCaptureMouse(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'DoCaptureMouse in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        self.logger.wxCHECK_RET(
##            m_widget != NULL,
##            'invalid window')

##        GdkWindow *window = NULL;
##        if (m_wxwindow)
##            window = GTKGetDrawingWindow();
##        else
##            window = GetConnectWidget()->window;

##        wxCHECK_RET( window, wxT("CaptureMouse() failed") );

##        const wxCursor* cursor = &m_cursor;
##        if (!cursor->Ok())
##            cursor = wxSTANDARD_CURSOR;

##        gdk_pointer_grab( window, FALSE,
##                          (GdkEventMask)
##                             (GDK_BUTTON_PRESS_MASK |
##                              GDK_BUTTON_RELEASE_MASK |
##                              GDK_POINTER_MOTION_HINT_MASK |
##                              GDK_POINTER_MOTION_MASK),
##                          NULL,
##                          cursor->GetCursor(),
##                          (guint32)GDK_CURRENT_TIME );
##        g_captureWindow = this;
##        g_captureWindowHasMouse = true;

    #-----------------------------------------------------------------------

    def DoCentre(self, dir):
        '''
        Centres the window.

        Parameters:
        direction  Specifies the direction for the centring. May be
        wxHORIZONTAL, wxVERTICAL or wxBOTH. It may also include the
        wxCENTRE_ON_SCREEN flag.

        Remarks:
        This function is not meant to be called directly by user code,
        but via Centre, Center, CentreOnParent, or CenterOnParent. This
        function can be overriden to fine-tune centring behaviour.
        '''
        if True:

            # centre the window with respect to its parent or screen
            self.Centre(dir)

        else:

            # centre the window with respect to its parent
            self.logger.wxCHECK_RET(
                ((not (dir & wx.CENTRE_ON_SCREEN)) and \
                 (not (self.GetParent() is None))),
                'this method only implements centering child windows')

            self.SetSize(
                self.GetRect().CentreIn(self.GetParent().GetClientSize(), dir))

    #-----------------------------------------------------------------------

    def DoFindFocus(self):
        '''
        Finds the window or control which currently has the keyboard focus.

        Remarks:

        Note that this should have been a static function, so it can be
        called without needing a wxWindow pointer.
        '''
        for theKey in list(wx.WindowsByAssignedId.keys()):
            theWindow = wx.WindowsByAssignedId[theKey]
            if theWindow.ts_FocusEnabled:
                self.logger.debug(
                    'DoFindFocus: %s; name: %s' % (theKey, theWindow.Name))
                return (theWindow)

        return (None)

    #-----------------------------------------------------------------------

    def DoGetBestClientSize(self):
        '''
        '''
        bestClientSize = self.ClientSize
        msg = 'Simulated DoGetBestClientSize=%s in tsWxWindow.' % str(
            bestClientSize)
        self.logger.error(msg)
        return (bestClientSize)

    #-----------------------------------------------------------------------

    def DoGetBestSize(self):
        '''
        Gets the size which best suits the window: for a control, it
        would be the minimal size which does not truncate the control,
        for a panel - the same size as it would have after a call to Fit().
        The default implementation of this function is designed for use
        in container windows, such as wxPanel, and works something like
        this:

        1) If the window has a sizer then it is used to calculate the
        best size.

        2) Otherwise if the window has layout constraints then those are
        used to calculate the best size.

        3) Otherwise if the window has children then the best size is set
        to be large enough to show all the children.

        4) Otherwise if there are no children then the windows minimal
        size will be used as its best size.

        5) Otherwise if there is no minimal size set, then the current
        size is used for the best size.
        '''
        if (not (self.ts_WindowSizer is None)):

            best = self.ts_WindowSizer.GetMinSize()

        elif (wx.USE_CONSTRAINTS and \
              (not (self.ts_Constraints is None))):

            self.SatisfyConstraints()

            # our minimal acceptable size is such that all our windows
            # fit inside
            maxX = 0
            maxY = 0

            for child in self.ts_Children:

                c = child.GetConstraints()
                if (not (c == 0)):

                    # it's not normal that we have an unconstrained child, but
                    # what can we do about it?
                    continue

                x = c.right.GetValue()
                y = c.bottom.GetValue()

                if (x > maxX):
                    maxX = x

                if (y > maxY):
                    maxY = y

                # TODO: we must calculate the overlaps somehow, otherwise we
                #       will never return a size bigger than the current
                #       one :-(

            best = wxSize(maxX, maxY)

        elif (not ((self.ts_Children is None) or \
                   ((self.ts_Children == []))) and \
              (self.wxHasRealChildren(self))):

            # our minimal acceptable size is such that all our visible child
            # windows fit inside
            maxX = 0
            maxY = 0

            for child in self.ts_Children:

                win = child
                if (win.IsTopLevel() or \
                    (not (win.IsShown()))):
                    # dialogs and frames lie in different top level windows -
                    # don't deal with them here as for the status bars, they
                    # don't lie in the client area at all
                    continue

                winPosition = win.Position
                winX = winPosition.x
                winY = winPosition.y

                # if the window hadn't been positioned yet, assume that it
                # is in the origin
                if (winX == wx.DefaultCoord):
                    winX = 0
                if (winY == wx.DefaultCoord):
                    winY = 0

                winSize = win.Size
                winW = winSize.width
                winH = winSize.height
                if ((winX + winW) > maxX):
                    maxX = winX + winW
                if ((winY + winH) > maxY):
                    maxY = winY + winH

            best = wxSize(maxX, maxY)

        else:
            # has no children

            size = self.GetMinSize()
            if (not size.IsFullySpecified()):

                # if the window does not define its best size we assume
                # that it can be arbitrarily small -- usually this is
                # not the case, of course, but we have no way to know
                # what the limit is, it should really override
                # DoGetBestClientSize() itself to tell us
                size.SetDefaults(wxSize(1, 1))

            # return as-is, unadjusted by the client size difference.
            return (size)

        # Add any difference between size and client size
        diff = self.GetSize() - self.GetClientSize()
        best.x += max(0, diff.x)
        best.y += max(0, diff.y)

        return (best)

    #-----------------------------------------------------------------------

    def DoGetBorderSize(self):
        '''
        Return the thickness (width and height) of the display
        occupied by the top, bottom, left and right border
        '''
        if (self.GetBorder() == wx.BORDER_NONE):

            # this is one case in which we can implement it
            # for all ports easily
            border_Size = wxSize(0, 0)

        else:

            # otherwise use the difference between the real size
            # and the client size as a fallback: notice that this
            # would be incorrect, in general for wxWidgets, as client
            # size also doesn't take the scrollbars into account
            borderSize = self.GetSize() - self.GetClientSize()

        return (borderSize)

    #-----------------------------------------------------------------------

    def DoGetScreenPosition(self, x, y):
        '''
        '''
        # screen position is the same as (0, 0) in client coords for non
        # TLWs (and TLWs override this method)
        if (x != 0):
            x = 0

        if (y != 0):
            y = 0

        self.ClientToScreenXY(x, y)

    #-----------------------------------------------------------------------

    def DoGetSibling(self, order):
        '''
        Return the sibling of the window that is in the specified order.
        '''
        self.logger.wxCHECK_MSG(
            (not (self.GetParent() is None)),
            None,
            'GetPrev/NextSibling() does not work for TLWs!')

        theSiblings = self.GetParent().GetChildren()

        self.logger.wxCHECK_MSG(
            (not (self in theSiblings)),
            None,
            "Window.DoGetSibling: window not a child of its parent?")

        i = -1
        for aSibling in theSiblings:
            i += 1
            if (aSibling == self):
                if (order == wx.OrderBefore ):
                    theSibling = self.GetPrevSibling()
                else: # OrderAfter
                    theSibling = self.GetNextSibling()
                break

        if theSibling is None:
            return (None)
        else:
            return (theSibling)

    #-----------------------------------------------------------------------

    def DoGetVirtualSize(self):
        '''
        '''
        # we should use the entire client area so if it is greater than our
        # virtual size, expand it to fit (otherwise if the window is big
        # enough we wouldn't be using parts of it)

        size = self.GetClientSize()
        if (self.ts_VirtualSize.width > size.width):
            size.width = self.ts_VirtualSize.width

        if (self.ts_VirtualSize.height >= size.height):
            size.height = self.ts_VirtualSize.height

        return (size)

    #-----------------------------------------------------------------------

    def DoPhase(self, phase):
        '''
        Do a phase of evaluating child constraints
        '''
        if wx.USE_CONSTRAINTS:

            # the list containing the children for which the constraints are
            # already set correctly
            succeeded = []

            # the max number of iterations we loop before concluding that we
            # can't set the constraints
            maxIterations = 500

            for noIterations in range(0, maxIterations):

                noChanges = 0

                # loop over all children setting their constraints
                for child in self.ts_Children:

                    if (child.IsTopLevel()):

                        # top level children are not inside our client area
                        continue

                    if ((not (child.GetConstraints() is None)) or \
                        (child in succeeded)):

                        # this one is either already ok or
                        # nothing we can do about it
                        continue

                    tempNoChanges = 0
                    if (phase == 1):
                        success = True
                        child.LayoutPhase1(tempNoChanges)
                    else:
                        child.LayoutPhase2(tempNoChanges)
                    noChanges += tempNoChanges

                    if (success):

                        succeeded.append(child)

                if (not (noChanges)):

                    # constraints are set
                    break

            return (True)

        else:

            return (False)

    #-----------------------------------------------------------------------

    def DoReleaseMouse(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'DoReleaseMouse in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##{
##    wxCHECK_RET( m_widget != NULL, wxT("invalid window") );

##    wxCHECK_RET( g_captureWindow, wxT("can't release mouse - not captured") );

##    g_captureWindow = NULL;

##    GdkWindow *window = NULL;
##    if (m_wxwindow)
##        window = GTKGetDrawingWindow();
##    else
##        window = GetConnectWidget()->window;

##    if (!window)
##        return;

##    gdk_pointer_ungrab ( (guint32)GDK_CURRENT_TIME );

    #-----------------------------------------------------------------------

    def DoSetSizeHints(self,
                       minW,
                       minH,
                       maxW,
                       maxH,
                       incW=None,
                       incH=None):
        '''
        '''
        self.logger.wxCHECK_RET(
            ((minW == wx.DefaultCoord) or \
             (maxW == wx.DefaultCoord) or \
             (minW <= maxW) and \
             ((minH == wx.DefaultCoord) or \
              (maxH == wx.DefaultCoord) or \
              (minH <= maxH))
             ),
            'min width/height must be less than max width/height!')

        self.ts_MinWidth = minW
        self.ts_MaxWidth = maxW
        self.ts_MinHeight = minH
        self.ts_MaxHeight = maxH

    #-----------------------------------------------------------------------

    def DoSetVirtualSize(self, x, y):
        '''
        '''
        self.ts_VirtualSize = wxSize(x, y)

    #-----------------------------------------------------------------------

    def DoSetWindowVariant(self, variant=None):
        '''
        Adjust the font height to correspond to our new variant (notice that
        we are only called if something really changed)
        '''
        msg = 'NotImplementedError: %s' % 'DoSetWindowVariant in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        font = self.GetFont()
        size = font.GetPointSize()

##        if (variant is None):
##            pass

##        elif (variant == wx.WINDOW_VARIANT_NORMAL):
##            pass

##        elif (variant == wx.WINDOW_VARIANT_SMALL):
##            size = wxRound(size * 3.0 / 4.0)

##        elif (variant == wx.WINDOW_VARIANT_MINI):
##            size = wxRound(size * 2.0 / 3.0)

##        elif (variant == wx.WINDOW_VARIANT_LARGE):
##            size = wxRound(size * 5.0 / 4.0);

##        else:
##            self.logger.wxFAIL_MSG('unexpected window variant')

##        self.font.SetPointSize(size)
##        self.SetFont(font)

    #-----------------------------------------------------------------------

    def DoUpdateWindowUI(self, event):
        '''
        Does the window-specific updating after processing the update event.

        This function is called by UpdateWindowUI() in order to check
        return values in the wxUpdateUIEvent and act appropriately.
        For example, to allow frame and dialog title updating, wxWidgets
        implements this function as follows:

        // do the window-specific processing after processing the update event
        void wxTopLevelWindowBase::DoUpdateWindowUI(wxUpdateUIEvent& event)
        {
            if ( event.GetSetEnabled() )
                Enable(event.GetEnabled());

            if ( event.GetSetText() )
            {
                if ( event.GetText() != GetTitle() )
                    SetTitle(event.GetText());
            }
        }
        '''
        if ( event.GetSetEnabled() ):
            self.Enable(event.GetEnabled())

        if ( event.GetSetShown() ):
            self.Show(event.GetShown())

    #-----------------------------------------------------------------------

    def DragAcceptFiles(self, accept):
        '''
        Enables or disables eligibility for drop file events (OnDropFiles).

        Parameters:
        accept  If true, the window is eligible for drop file events. If
        false, the window will not accept drop file events.

        Remarks:
        Windows only until version 2.8.9, available on all platforms since
        2.8.10. Cannot be used together with SetDropTarget() on non-Windows
        platforms.
        '''
        self.ts_AcceptFiles = accept

    #-----------------------------------------------------------------------

    def Enable(self, enable=True):
        '''
        Enable or disable the window for user input.

        Note that when a parent window is disabled, all of its children
        are disabled as well and they are reenabled again when the parent is.

        Parameters:
        enable  If true, enables the window for input. If false, disables
        the window.

        Returns:
        Returns true if the window has been enabled or disabled, false if
        nothing was done, i.e. if the window had already been in the
        specified state.
        '''
##        if ( enable == IsThisEnabled() )
##            return false;

##        m_isEnabled = enable;

##        // If we call DoEnable() from NotifyWindowOnEnableChange(), we don't need
##        // to do it from here.
##    #ifdef wxHAS_NATIVE_ENABLED_MANAGEMENT
##        DoEnable(enable);
##    #endif // !defined(wxHAS_NATIVE_ENABLED_MANAGEMENT)

##        NotifyWindowOnEnableChange(enable);

##        return true;

        if self.Enabled != enable:

            self.Enabled = enable
            return (True)

        else:

            return (False)

    #-----------------------------------------------------------------------

    # @staticmethod
    def FindFocus(self):
        '''
        Finds the window or control which currently has the keyboard focus.

        Remarks:

        Note that this should have been a static function, so it can be
        called without needing a wxWindow pointer.
        '''
        win = self.DoFindFocus()
        if (not (win is None)):
            return (win.GetMainWindowOfCompositeControl())
        else:
            return (None)

    #-----------------------------------------------------------------------

    # @staticmethod
    def FindWindowById(self, winid, parent=None):
        '''
        Find the first window with the given id.

        If parent is NULL, the search will start from all top-level frames
        and dialog boxes; if non-NULL, the search will be limited to the
        given window hierarchy. The search is recursive in both cases.
        '''
        if parent is None:

            try:
                win = tsWxGTUI_DataBase.WindowsById[winid]
            except KeyError:
                win = None
                self.logger.debug(
                    'FindWindowById KeyError: %d' % winid)

            return (win)

        else:

            msg = 'NotImplementedError (parent): %s' % \
                'FindWindowById in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def FindWindowByLabel(self, label, parent=None):
        '''
        Find a window by its label.

        Depending on the type of window, the label may be a window title
        or panel item label. If parent is NULL, the search will start from
        all top-level frames and dialog boxes; if non-NULL, the search will
        be limited to the given window hierarchy. The search is recursive
        in both cases.
        '''
        if parent is None:

            msg = 'NotImplementedError: %s' % 'FindWindowByLabel in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            msg = 'NotImplementedError (parent): %s' % \
                'FindWindowByLabel in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def FindWindowByName(self, name, parent=None):
        '''
        Find a window by its name (as given in a window constructor or
        Create() function call).

        If parent is NULL, the search will start from all top-level frames
        and dialog boxes; if non-NULL, the search will be limited to the
        given window hierarchy.

        The search is recursive in both cases. If no window with such name
        is found, FindWindowByLabel() is called.
        '''
        if parent is None:

            try:
                win = tsWxGTUI_DataBase.WindowsByName[name]
            except KeyError:
                win = None
                self.logger.debug(
                    'FindWindowByName KeyError: %s' % name)

            return (win)

        else:

            msg = 'NotImplementedError (parent): %s' % \
                'FindWindowByName in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Fit(self):
        '''
        Sizes the window so that it fits around its subwindows. This function
        will not do anything if there are no subwindows and will only really
        work correctly if sizers are used for the subwindows layout.

        Also, if the window has exactly one subwindow it is better (faster
        and the result is more precise as Fit adds some margin to account for
        fuzziness of its calculations) to call
        window.SetClientSize(child.GetSize()) instead of calling Fit.
        '''
        if (self.Children is None) or (self.Children == {}):

            # do nothing if we have no children
            pass

        else:

            self.SetSize(self.GetBestSize())

    #-----------------------------------------------------------------------

    def FitInside(self):
        '''
        Similar to Fit(), but sizes the interior (virtual) size of a
        window.

        Mainly useful with scrolled windows to reset scrollbars after
        sizing changes that do not trigger a size event, and/or scrolled
        windows without an interior sizer. This function similarly will
        not do anything if there are no subwindows.
        '''
        # if (self.GetChildren().GetCount() > 0):
        if (self.Children is None) or (self.Children == {}):

            # do nothing if we have no children
            pass

        else:

            self.SetVirtualSize(self.GetBestVirtualSize())

    #-----------------------------------------------------------------------

    def Freeze(self):
        '''
        Freezes the window or, in other words, prevents any updates from
        taking place on screen, the window is not redrawn at all.

        Thaw() must be called to reenable window redrawing. Calls to these
        two functions may be nested but to ensure that the window is
        properly repainted again, you must thaw it exactly as many times
        as you froze it.

        If the window has any children, they are recursively frozen too.

        This method is useful for visual appearance optimization (for
        example, it is a good idea to use it before doing many large
        text insertions in a row into a wxTextCtrl under wxGTK) but
        is not implemented on all platforms nor for all controls so
        it is mostly just a hint to wxWidgets and not a mandatory
        directive.
        '''
##        if ( !m_freezeCount++ )
##        {
##            // physically freeze this window:
##            DoFreeze();

##            // and recursively freeze all children:
##            for ( wxWindowList::iterator i = GetChildren().begin();
##                  i != GetChildren().end(); ++i )
##            {
##                wxWindow *child = *i;
##                if ( child->IsTopLevel() )
##                    continue;

##                child->Freeze();
##            }
##        }

        self.ts_Freeze = True

        for child in self.ts_Children:
            child.Freeze()

    #-----------------------------------------------------------------------

    def GetAcceleratorTable(self):
        '''
        Gets the accelerator table for this window.
        '''
        assignedId = self.ts_AssignedId
        dbase = tsWxGTUI_DataBase
        try:
            acceleratorTable = dbase.AcceleratorTableByAssignedId[assignedId]
        except Exception as keyError:
            acceleratorTable = wx.NullAcceleratorTable

        return (acceleratorTable)

    #-----------------------------------------------------------------------

    def GetAccessible(self):
        '''
        Returns the accessible object for this window, if any.
        '''
        msg = 'NotImplementedError: %s' % 'GetAccessible in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetAdjustedBestSize(self, *args, **kwargs):
        '''
        Use GetEffectiveMinSize instead.
        '''
        return (self.GetEffectiveMinSize())

    #-----------------------------------------------------------------------

    def GetAttributeValueFromColorPair(self, foreground, background):
        '''
        Use Get Curses Attribute from Color Pair.
        '''
        return (
            self.TheTerminalScreen.tsGetAttributeValueFromColorPair(
                foreground,
                background))

    #-----------------------------------------------------------------------

    def GetAutoLayout(self):
        '''
        Returns the sizer of which this window is a member, if any,
        otherwise NULL.
        '''
        return (self.ts_AutoLayout)

    #-----------------------------------------------------------------------

    def GetBackgroundColour(self):
        '''
        Returns the background colour of the window.
        '''
        return (self.ts_BackgroundColour)

    #-----------------------------------------------------------------------

    def GetBackgroundStyle(self):
        '''
        Returns the background style of the window.
        '''
        return (self.ts_BackgroundStyle)

    #-----------------------------------------------------------------------

    def GetBestFittingSize(self, *args, **kwargs):
        '''
        Use GetEffectiveMinSize instead.
        '''
        return (self.GetEffectiveMinSize())

    #-----------------------------------------------------------------------

    def GetBestSize(self):
        '''
        This function returns the best acceptable minimal size for the
        window, if applicable.

        For example, for a static text control, it will be the minimal
        size such that the control label is not truncated. For windows
        containing subwindows (such as wx.Panel), the size returned by
        this function will be the same as the size the window would have
        had after calling Fit.

        Note that when you write your own widget you need to override
        the DoGetBestSize() function instead of this (non-virtual!)
        function.
        '''
        if (not (self.ts_WindowSizer is None) and \
            (self.ts_BestSizeCache.IsFullySpecified())):

            return (self.ts_BestSizeCache)

        # call DoGetBestClientSize() first, if a derived class
        # overrides it ad wants it to be used
        size = self.DoGetBestClientSize()
        if (size != DEFAULT_SIZE):

            size += self.DoGetBorderSize()

            self.CacheBestSize(size)
            return (size)

        return (self.DoGetBestSize())

    #-----------------------------------------------------------------------

    def GetBestSizeTuple(self):
        '''
        This function returns the best acceptable minimal size for the window,
        if applicable. For example, for a static text control, it will be the
        minimal size such that the control label is not truncated. For windows
        containing subwindows (suzh as wx.Panel), the size returned by this
        function will be the same as the size the window would have had after
        calling Fit.
        '''
        temp = self.GetBestSize()
        return (temp.width, temp.height)

    #-----------------------------------------------------------------------

    def GetBestVirtualSize(self):
        '''
        Return the largest of ClientSize and BestSize (as determined by a
        sizer, interior children, or other means)
        '''
        temp1 = self.GetClientSize()
        temp2 = self.GetBestSize()

        if temp1.width >= temp2.width and \
           temp1.height >= temp2.height:

            return (temp1)

        elif temp2.width >= temp1.width and \
             temp2.height >= temp1.height:

            return (temp2)

        elif (temp1.width * temp1.height) >= \
             (temp2.width * temp2.height):

            return (temp1)

        else:

            return (temp2)

    #-----------------------------------------------------------------------

    def GetBorder(self, flags=None):
        '''
        Get the window border style from the given flags: this is different
        from simply doing flags & wxBORDER_MASK because it uses
        GetDefaultBorder() to translate wxBORDER_DEFAULT to something
        reasonable.
        '''
        if flags is None:
            border = self.ts_Style & wx.BORDER_MASK
        else:
            border = flags & wx.BORDER_MASK

        if border == wx.BORDER_DEFAULT:

            border = self.GetDefaultBorder()

        elif border == wx.BORDER_THEME:

            border = self.GetDefaultBorderForControl()

        return (border)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetCapture():
        '''
        Returns the currently captured window.
        '''
        if True:

            msg = 'NotImplementedError: %s' % 'GetCapture in tsWxWindow'
            # self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (None)

    #-----------------------------------------------------------------------

    def GetCaret(self):
        '''
        Returns the caret() associated with the window.
        '''
        return (self.ts_Caret)

    #-----------------------------------------------------------------------

    def GetCharHeight(self):
        '''
        Returns the character height for this window.
        '''
        return (self.ts_CharHeight)

    #-----------------------------------------------------------------------

    def GetCharWidth(self):
        '''
        Returns the character width for this window.
        '''
        return (self.ts_CharWidth)

    #-----------------------------------------------------------------------

    def GetChildren(self):
        '''
        Returns an object containing a list of the window children.
        '''
        return (self.ts_Children)

    #-----------------------------------------------------------------------

    @staticmethod
    def GetClassDefaultAttributes(variant=wx.WINDOW_VARIANT_NORMAL):
        '''
        Returns the default font and colours which are used by the control.

        This is useful if you want to use the same font or colour in your
        own control as in a standard control -- which is a much better idea
        than hard coding specific colours or fonts which might look
        completely out of place on the users system, especially if it uses
        themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size
        of the returned font. See SetWindowVariant() for more about this.

        This static method is "overridden" in many derived classes and
        so calling, for example, wxButton::GetClassDefaultAttributes()
        will typically return the values appropriate for a button which
        will be normally different from those returned by, say,
        wxListCtrl::GetClassDefaultAttributes().

        The wxVisualAttributes structure has at least the fields font,
        colFg and colBg. All of them may be invalid if it was not possible
        to determine the default control appearance or, especially for the
        background colour, if the field does not make sense as is the case
        for colBg for the controls with themed background.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetClassDefaultAttributes in tsWxWindow'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetClientAreaOrigin(self):
        '''
        Get the origin of the client area of the window relative to the
        window top left corner (the client area may be shifted because
        of the borders, scrollbars, other decorations...).
        '''
        return (wxPoint(self.ts_ClientRect.x, self.ts_ClientRect.y))

    #-----------------------------------------------------------------------

    def GetClientRect(self):
        '''
        Get the client area position and size as a wx.Rect object.
        '''
        return (self.ts_ClientRect)

    #-----------------------------------------------------------------------

    def GetClientSize(self):
        '''
        This gets the size of the window client area in pixels.

        The client area is the area which may be drawn on by the programmer,
        excluding title bar, border, scrollbars, etc. Note that if this
        window is a top-level one and it is currently minimized, the return
        size is empty (both width and height are 0).
        '''
        return (wxSize(self.ts_ClientRect.width, self.ts_ClientRect.height))

    #-----------------------------------------------------------------------

    def GetClientSizeConstraintWH(self):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            w = constr.width.GetValue()
            h = constr.height.GetValue()

        else:

            (w, h) = self.GetClientSize()

        return (wxSize(w, h))

    #-----------------------------------------------------------------------

    def GetClientSizeTuple(self):
        '''
        This gets the size of the window client area in pixels.
        '''
        return (self.ts_ClientRect.width, self.ts_ClientRect.height)

    #-----------------------------------------------------------------------

    def GetConstraints(self):
        '''
        Returns a pointer to the window layout constraints, or None if
        there are none.
        '''
        msg = 'NotImplementedError: %s' % 'GetConstraints in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetContainingSizer(self):
        '''
        Return the sizer that this window is a member of, if any,
        otherwise None.
        '''
        return (self.ts_ContainingSizer)

    #-----------------------------------------------------------------------

    def GetCursor(self):
        '''
        Return the cursor associated with this window.
        '''
        msg = 'NotImplementedError: %s' % 'GetCursor in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetDefaultAttributes(self):
        '''
        Currently this is the same as calling
        wxWindow::GetClassDefaultAttributes(wxWindow::GetWindowVariant()).

        One advantage of using this function compared to the static
        version is that the call is automatically dispatched to the
        correct class (as usual with virtual functions) and you do not
        have to specify the class name explicitly.

        The other one is that in the future this function could return
        different results, for example it might return a different font
        for an "Ok" button than for a generic button if the users GUI
        is configured to show such buttons in bold font. Of course, the
        down side is that it is impossible to call this function without
        actually having an object to apply it to whereas the static
        version can be used without having to create an object first.
        '''
        msg = 'NotImplementedError: %s' % 'GetDefaultAttributes in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetDefaultBorder(self):
        '''
        Get default border for this window.
        '''
        return (wx.BORDER_NONE)

    #-----------------------------------------------------------------------

    def GetDefaultBorderForControl(self):
        '''
        Get default border for this control.
        '''
        return (wx.BORDER_THEME)

    #-----------------------------------------------------------------------

    def GetDlgUnitBase(self):
        '''
        Windows computes dialog units using average character width over
        upper- and lower-case ASCII alphabet and not using the average
        character width metadata stored in the font; see
        http://support.microsoft.com/default.aspx/kb/145994 for detailed
        discussion.

        It is important that we perform the conversion in identical way,
        because dialog units natively exist only on Windows and Windows
        HIG is expressed using them.
        '''
##        parent = self.GetTopLevelParent(self)

##        if (not (parent.ts_Font.IsOk())):

##            # Default GUI font is used. This is the most common case, so
##            # cache the results.
##            static_defFontSize = wxSize(wx.pixelWidthPerCharacter,
##                                        wx.PixelHeightPerCharacter)
##            if (static_defFontSize.x == 0 ):
##                static_defFontSize = self.GetAverageASCIILetterSize(parent)
##            return (static_defFontSize)

##        else:

##            # Custom font, we always need to compute the result
##            return self.GetAverageASCIILetterSize(parent)

        return (wxSize(wx.pixelWidthPerCharacter,
                       wx.pixelHeightPerCharacter))


    #-----------------------------------------------------------------------

    def GetDropTarget(self):
        '''
        Returns the associated drop target, which may be None.
        '''
        msg = 'NotImplementedError: %s' % 'GetDropTarget in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetEffectiveMinSize(self):
        '''
        Merges the windows best size into the min size and returns the
        result.

        This is the value used by sizers to determine the appropriate
        amount of space to allocate for the widget.

        This is the method called by a wxSizer when it queries the size
        of a window or control.
        '''
        # merge the best size with the min size, giving priority to the
        # min size
        theMin = self.GetMinSize()

        if ((theMin.x == wx.DefaultCoord) or \
            (theMin.y == wx.DefaultCoord)):

            theBest = self.GetBestSize()

            if (theMin.x == wx.DefaultCoord):

                theMin.x =  theBest.x

            if (theMin.y == wx.DefaultCoord):

                theMin.y =  theBest.y

        return (theMin)

    #-----------------------------------------------------------------------

    def GetEventHandler(self):
        '''
        Returns the event handler for this window.

        By default, the window is its own event handler.
        '''
        msg = 'NotImplementedError: %s' % 'GetEventHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetExtraStyle(self):
        '''
        Returns the extra style bits for the window.
        '''
        msg = 'NotImplementedError: %s' % 'GetExtraStyle in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetFont(self):
        '''
        Returns the font for this window.
        '''
        msg = 'NotImplementedError: %s' % 'GetFont in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetForegroundColour(self):
        '''
        Returns the foreground colour of the window.

        Remarks:
        The meaning of foreground colour varies according to the window
        class; it may be the text colour or other colour, or it may not
        be used at all.
        '''
        return (self.ts_ForegroundColour)

    #-----------------------------------------------------------------------

    def GetFullTextExtent(self, string, font):
        '''
        Get the width, height, decent and leading of the text using the
        current or specified font.
        '''
        msg = 'NotImplementedError: %s' % 'GetFullTextExtent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetGrandParent(self):
        '''
        Returns the parent of the parent of this window, or None if there
        is not one.
        '''
        parent = self.GetParent()
        if parent is None:
            return (parent)
        else:
            return (parent.GetParent())

    #-----------------------------------------------------------------------

    def GetGtkWidget(self):
        '''
        On wxGTK returns a pointer to the GtkWidget for this window as a
        long integer.
        '''
        msg = 'NotImplementedError: %s' % 'GetGtkWidget in tsWxWindow'
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetHandle(self):
        '''
        Returns the platform-specific handle of the physical window.

        Cast it to an appropriate handle, such as HWND for Windows,
        Widget for Motif, GtkWidget for GTK or WinHandle for PalmOS.
        '''
        return (self.ts_Handle)

    #-----------------------------------------------------------------------

    def GetHelpText(self):
        '''
        Gets the help text to be used as context-sensitive help for this
        window.

        Note that the text is actually stored by the current wxHelpProvider
        implementation, and not in the window object itself.
        '''
        msg = 'NotImplementedError: %s' % 'GetHelpText in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (None)

    #-----------------------------------------------------------------------

    def GetHelpTextAtPoint(self, point, origin):
        '''
        Gets the help text to be used as context-sensitive help for this
        window.

        This method should be overridden if the help message depends on
        the position inside the window, otherwise GetHelpText() can be
        used.

        Parameters:
        point   Coordinates of the mouse at the moment of help event emission.

        origin  Help event origin, see also wxHelpEvent::GetOrigin.
        '''
        msg = 'NotImplementedError: %s' % 'GetHelpTextAtPoint in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (None)

    #-----------------------------------------------------------------------

    def GetId(self):
        '''
        Returns the identifier of the window.

        Remarks:
        Each window has an integer identifier. If the application has
        not provided one (or the default wxID_ANY) a unique identifier
        with a negative value will be generated.
        '''
        return (self.ts_Id)

    #-----------------------------------------------------------------------

    def GetLabel(self):
        '''
        Generic way of getting a label from any window, for identification
        purposes.

        Remarks:
        The interpretation of this function differs from class to class.
        For frames and dialogs, the value returned is the title.
        For buttons or static text controls, it is the button text. This
        function can be useful for meta-programs such as testing tools or
        special-needs access programs)which need to identify windows by name.
        '''
        if self.ClassName == 'Frame' or \
           self.ClassName == 'Dialog' or \
           self.ClassName == 'Screen' or \
           self.ClassName == 'Stdio':
            try:
                theLabel = self.ts_Title
            except AttributeError:
                theLabel = (self.ts_Name)
                self.logger.debug(
                    'GetLabel AttributeError: %s' % self.ClassName)

        elif self.ClassName == 'Button':
            try:
                theLabel = (self.ts_ButtonText)
            except AttributeError:
                theLabel = (self.ts_Name)
                self.logger.debug(
                    'GetLabel AttributeError: %s' % self.ClassName)

        elif self.ClassName == 'StaticText':
            try:
                theLabel = (self.ts_ButtonText)
            except AttributeError:
                theLabel = (self.ts_Name)
                self.logger.debug(
                    'GetLabel AttributeError: %s' % self.ClassName)

        else:
            theLabel = self.ts_Label

        if DEBUG:
            self.logger.debug('GetLabel: theLabel="%s" for className=%s' % (
                theLabel, self.ClassName))

        return (theLabel)

    #-----------------------------------------------------------------------

    def GetLayoutDirection(self):
        '''
        Returns the layout direction for this window, Note that
        wxLayout_Default is returned if layout direction is not
        supported.
        '''
        return (wx.Layout_Default)

    #-----------------------------------------------------------------------

    def GetMainWindowOfCompositeControl(self):
        '''
        Returns the main window of composite control; this is the window
        that FindFocus returns if the focus is in one of composite
        control windows
        '''
        try:

            # TBD - Not sure if this is appropriate.
            # Is this too far up the ancestor hierarchy
            return (self.ts_EarliestAncestor)

        except AttributeError:

            msg = 'NotImplementedError: %s' % \
                'GetMainWindowOfCompositeControl in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMaxClientSize(self):
        '''
        Returns the maximum size of windows client area.

        This is an indication to the sizer layout mechanism that this is
        the maximum possible size as well as the upper bound on windows
        size settable using SetClientSize().
        '''
        return (wxSize(self.ts_ClientRect.width, self.ts_ClientRect.height))
##        msg = 'NotImplementedError: %s' % 'GetMaxClientSize in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMaxHeight(self):
        '''
        '''
        return (self.ts_Rect.height)
##        msg = 'NotImplementedError: %s' % 'GetMaxHeight in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMaxSize(self):
        '''
        Returns the maximum size of the window.

        This is an indication to the sizer layout mechanism that this is
        the maximum possible size as well as the upper bound on windows
        size settable using SetSize().
        '''
        return (wxSize(self.ts_Rect.width, self.ts_Rect.height))
##        msg = 'NotImplementedError: %s' % 'GetMaxSize in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMaxWidth(self):
        '''
        '''
        return (self.ts_Rect.width)
##        msg = 'NotImplementedError: %s' % 'GetMaxWidth in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMinClientSize(self):
        '''
        Returns the minimum size of windows client area, an indication
        to the sizer layout mechanism that this is the minimum required
        size of its client area.

        It normally just returns the value set by SetMinClientSize(),
        but it can be overridden to do the calculation on demand.
        '''
        return (wxSize(self.ts_ClientRect.width, self.ts_ClientRect.height))
##        msg = 'NotImplementedError: %s' % 'GetMinClientSize in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMinHeight(self):
        '''
        '''
        return (self.ts_Rect.height)
##        msg = 'NotImplementedError: %s' % 'GetMinHeight in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMinSize(self):
        '''
        Returns the minimum size of the window, an indication to the sizer
        layout mechanism that this is the minimum required size.

        This method normally just returns the value set by SetMinSize(),
        but it can be overridden to do the calculation on demand.
        '''
        return (wxSize(self.ts_Rect.width, self.ts_Rect.height))
##        msg = 'NotImplementedError: %s' % 'GetMinSize in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetMinWidth(self):
        '''
        '''
        return (len(self.GetLabel()))

    #-----------------------------------------------------------------------

    def GetName(self):
        '''
        Returns the windows name.

        Remarks:
        This name is not guaranteed to be unique; it is up to the
        programmer to supply an appropriate name in the window
        constructor or via SetName().
        '''
        return (self.ts_Name)

    #-----------------------------------------------------------------------

    def GetNextSibling(self):
        '''
        Returns the next window after this one among the parents
        children or None if this window is the last child
        '''
        parent = self.ts_Parent
        if ((self.IsTopLevel()) or \
            (parent is None)):

            # In wxWidgets/wxPython Top Level Windows (Frames and Dialogs)
            # have no parent and thus no siblings
            return (None)

        else:

            theSiblings = parent.ts_Children
            i = -1
            for aSibling in theSiblings:

                i += 1
                # Find position of self in theSiblings
                if (aSibling == self):

                    if ((0 <= i ) and \
                        (i < (len(theSiblings) - 1))):

                        # Self is not the last child of parent;
                        # can have a next sibling
                        return (theSiblings[i + 1])

                    else:

                        # Self is last child of parent;
                        # cannot have a next sibling
                        return (None)

    #-----------------------------------------------------------------------

    def GetParent(self):
        '''
        Returns the parent window of this window, or None if there is not one.
        '''
        try:
            return (self.ts_Parent)

        except AttributeError:
            self.logger.debug(
                'GetParent AttributeError: %s' % self)
            return (None)

    #-----------------------------------------------------------------------

    def GetPopupMenuSelectionFromUser(self, menu, pos=wx.DefaultPosition):
        '''
        This function shows a popup menu at the given position in this
        window and returns the selected id.

        It can be more convenient than the general purpose PopupMenu()
        function for simple menus proposing a choice in a list of strings
        to the user.

        Notice that to avoid unexpected conflicts between the (usually
        consecutive range of) ids used by the menu passed to this function
        and the existing EVT_UPDATE_UI() handlers, this function
        temporarily disables UI updates for the window, so you need to
        manually disable (or toggle or ...) any items which should be
        disabled in the menu before showing it.

        The parameter menu is the menu to show. The parameter pos (or the
        parameters x and y) is the position at which to show the menu in
        client coordinates. It is recommended to not explicitly specify
        coordinates when calling this method in response to mouse click,
        because some of the ports (namely, wxGTK) can do a better job of
        positioning the menu in that case.

        Returns:
        The selected menu item id or wxID_NONE if none selected or an
        error occurred.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetPopupMenuSelectionFromUser in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetPopupMenuSelectionFromUserXY(self, menu, x, y):
        '''
        This is an overloaded member function, provided for convenience.
        It differs from the above function only in what argument(s) it
        accepts.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetPopupMenuSelectionFromUser in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.GetPopupMenuSelectionFromUser(menu, wxPoint(x, y))

    #-----------------------------------------------------------------------

    def GetPosition(self):
        '''
        Get the window position. Notice that the position is in client
        coordinates for child windows and screen coordinates for the top
        level ones, use GetScreenPosition if you need screen coordinates
        for all kinds of windows.
        '''
        myRect = self.tsGetClassInstanceFromTuple(self.ts_Rect, wxRect)
        return (wxPoint(myRect.x, myRect.y))

    #-----------------------------------------------------------------------

    def GetPositionConstraintXY(self):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            x = constr.left.GetValue()
            y = constr.top.GetValue()

        else:

            (x, y) = self.GetPosition()

        return (wxPoint(x,y))

    #-----------------------------------------------------------------------

    def GetPositionTuple(self):
        '''
        Get the window position. Notice that the position is in client
        coordinates for child windows and screen coordinates for the top
        level ones, use GetScreenPosition if you need screen coordinates
        for all kinds of windows.
        '''
        myRect = self.tsGetClassInstanceFromTuple(self.ts_Rect, wxRect)
        return (myRect.x, myRect.y)

    #-----------------------------------------------------------------------

    def GetPrevSibling(self):
        '''
        Returns the previous window before this one among the parents
        children or None if this window is the first child
        '''
        parent = self.ts_Parent
        if ((self.IsTopLevel()) or \
            (parent is None)):

            # In wxWidgets/wxPython Top Level Windows (Frames and Dialogs)
            # have no parent and thus no siblings
            return (None)

        else:

            theSiblings = parent.ts_Children
            i = -1
            for aSibling in theSiblings:

                i += 1
                # Find position of self in theSiblings
                if (aSibling == self):

                    if (i == 0):

                        # Self is first child of parent;
                        # cannot have a previous sibling
                        return (None)

                    else:

                        # Self is not the first child of parent;
                        # can have a previous sibling
                        return (theSiblings[i - 1])

    #-----------------------------------------------------------------------

    def GetRect(self):
        '''
        Returns the position and size of the window as a wxRect object.
        '''
        return (self.ts_Rect)

    #-----------------------------------------------------------------------

    def GetScreenPosition(self):
        '''
        Returns the window position in screen coordinates, whether the
        window is a child window or a top level one.
        '''
        msg = 'NotImplementedError: %s' % 'GetScreenPosition in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetScreenPositionTuple(self):
        '''
        Get the position of the window in screen coordinantes.
        '''
        msg = 'NotImplementedError: %s' % \
            'GetScreenPositionTuple in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetScreenRect(self):
        '''
        Returns the position and size of the window on the screen as a
        wxRect object.
        '''
        msg = 'NotImplementedError: %s' % 'GetScreenRect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetScrollPos(self, orientation):
        '''
        Returns the built-in scrollbar position.
        '''
        msg = 'NotImplementedError: %s' % 'GetScrollPos in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetScrollRange(self, orientation):
        '''
        Returns the built-in scrollbar range.
        '''
        msg = 'NotImplementedError: %s' % 'GetScrollRange in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetScrollThumb(self, orientation):
        '''
        Returns the built-in scrollbar thumb size.
        '''
        msg = 'NotImplementedError: %s' % 'GetScrollThumb in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetSize(self):
        '''
        Returns the size of the entire window in pixels, including title
        bar, border, scrollbars, etc.

        Note that if this window is a top-level one and it is currently
        minimized, the returned size is the restored window size, not
        the size of the window icon.
        '''
        return (wxSize(self.ts_Rect.width, self.ts_Rect.height))

    #-----------------------------------------------------------------------

    def GetSizeConstraintWH(self):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            w = constr.width.GetValue()
            h = constr.height.GetValue()

        else:

            (w, h) = self.GetSize()

        return (wxSize(w, h))

    #-----------------------------------------------------------------------

    def GetSizeTuple(self):
        '''
        Get the window size.
        '''
        return (self.ts_Rect.width, self.ts_Rect.height)

    #-----------------------------------------------------------------------

    def GetSizer(self):
        '''
        Return the sizer associated with the window by a previous call to
        SetSizer or None if there is not one.
        '''
        return (self.ts_Sizer)

    #-----------------------------------------------------------------------

    def GetStyle(self):
        '''
        Get the window syle.
        '''
        return (self.ts_Style)

    #-----------------------------------------------------------------------

    def GetTextExtent(self, string):
        '''
        Gets the dimensions of the string as it would be drawn on the
        window with the currently selected font.
        '''
        return (self.tsGetPixelValues(len(string), 1))

    #-----------------------------------------------------------------------

    def GetThemeEnabled(self):
        '''
        Return the themeEnabled flag.
        '''
        return (self.ts_ThemeEnabled)

    #-----------------------------------------------------------------------

    def GetToolTip(self):
        '''
        Get the associated tooltip or NULL if none.
        '''
        msg = 'NotImplementedError: %s' % 'GetToolTip in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetToolTipText(self):
        '''
        Get the text of the associated tooltip or empty string if none.
        '''
        msg = 'NotImplementedError: %s' % 'GetToolTipText in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetTopLevelAncestor(self):
        '''
        Return top-level GUI object of our earliest ancestor.
        '''
        self.logger.debug(
            '      GetTopLevelAncestor: %s.' % self.ts_EarliestAncestor)
        return (self.ts_EarliestAncestor)

    #-----------------------------------------------------------------------

    def GetTopLevelParent(self):
        '''
        Returns the first frame or dialog in this window parental hierarchy.
        '''
        msg = 'NotImplementedError: %s' % 'GetTopLevelParent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetTopLevelSiblings(self):
        '''
        '''
        theData = tsWxGTUI_DataBase
        topLevelSiblings = theData.WindowsByShowOrder['OrderOfShow']
        self.logger.debug(
            'GetTopLevelSiblings: %s.' % topLevelSiblings)
        return (topLevelSiblings)

    #-----------------------------------------------------------------------

    def GetUpdateClientRect(self):
        '''
        Get the update rectangle region bounding box in client coords.
        '''
        msg = 'NotImplementedError: %s' % 'GetUpdateClientRect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetUpdateRegion(self):
        '''
        Returns the region specifying which parts of the window have
        been damaged.

        Should only be called within an wxPaintEvent handler.
        '''
        msg = 'NotImplementedError: %s' % 'GetUpdateRegion in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetValidator(self):
        '''
        Returns a pointer to the current validator for the window,
        or NULL if there is none.
        '''
        msg = 'NotImplementedError: %s' % 'GetValidator in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetVirtualSize(self):
        '''
        This gets the virtual size of the window in pixels.

        By default it returns the client size of the window, but after
        a call to SetVirtualSize() it will return the size set with that
        method.
        '''
        self.SetVirtualSize(self.DoGetVirtualSize())
        return (self.ts_VirtualSize)

    #-----------------------------------------------------------------------

    def GetVirtualSizeTuple(self):
        '''
        Get the the virtual size of the window in pixels.
        '''
        self.SetVirtualSize(self.DoGetVirtualSize())
        return (self.ts_VirtualSize.width, self.ts_VirtualSize.height)

    #-----------------------------------------------------------------------

    def GetWindowBorderSize(self):
        '''
        Returns the size of the left/right and top/bottom borders of
        this window in x and y components of the result respectively.
        '''

        border = self.GetBorder()

        if (border == wx.BORDER_NONE):
            # nothing to do, size is already (0, 0)
            size = wxSize(0, 0)

        elif ((border == wx.BORDER_SIMPLE) or \
              (border == wx.BORDER_STATIC)):

            # size.x = wxGetMetricOrDefault(wx.SYS_BORDER_X, self)
            # size.y = wxGetMetricOrDefault(wx.SYS_BORDER_Y, self)
            size = wxSize(wx.pixelWidthPerCharacter,
                          wx.pixelHeightPerCharacter)

        elif ((border == wx.BORDER_SUNKEN) or \
              (border == wx.BORDER_RAISED)):

            # size.x = wxMax(wxGetMetricOrDefault(wxSYS_EDGE_X, self),
            #                wxGetMetricOrDefault(wxSYS_BORDER_X, self))
            # size.y = wxMax(wxGetMetricOrDefault(wxSYS_EDGE_Y, self),
            #                wxGetMetricOrDefault(wxSYS_BORDER_Y, self))
            size = wxSize(wx.pixelWidthPerCharacter,
                          wx.pixelHeightPerCharacter)

        elif (border == wx.BORDER_DOUBLE):

            # size.x = wxGetMetricOrDefault(wxSYS_EDGE_X, self) +
            #          wxGetMetricOrDefault(wxSYS_BORDER_X, self)
            # size.y = wxGetMetricOrDefault(wxSYS_EDGE_Y, self) +
            #          wxGetMetricOrDefault(wxSYS_BORDER_Y, self)

            size = wxSize(wx.pixelWidthPerCharacter,
                          wx.pixelHeightPerCharacter)

        else:

            self.logger.wxFAIL_MSG(
                'tsWxWindow.GetWindowBorderSize: Unknown border style.')

        # we have borders on both sides
        return (wxSize(size.width * 2, size.height * 2))

    #-----------------------------------------------------------------------

    def GetWindowStyle(self):
        '''
        See GetWindowStyleFlag() for more info.
        '''
        msg = 'NotImplementedError: %s' % 'GetWindowStyle in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetWindowStyleFlag(self):
        '''
        Gets the window style that was passed to the constructor or
        Create() method.

        GetWindowStyle() is another name for the same function.

        Reimplemented in wxAuiToolBar.
        '''
        msg = 'NotImplementedError: %s' % 'GetWindowStyleFlag in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def GetWindowVariant(self):
        '''
        Returns the value previously passed to SetWindowVariant().
        '''
        msg = 'NotImplementedError: %s' % 'GetWindowVariant in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HandleAsNavigationKey(self, event):
        '''
        This function will generate the appropriate call to Navigate()
        if the key event is one normally used for keyboard navigation
        and return true in this case.

        Returns:
        Returns true if the key pressed was for navigation and was
        handled, false otherwise.
        '''
        msg = 'NotImplementedError: %s' % 'HandleAsNavigationKey in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HandleWindowEvent(self, event):
        '''
        Shorthand for:
        GetEventHandler()->SafelyProcessEvent(event)
        '''
        return self.GetEventHandler().SafelyProcessEvent(event)

    #-----------------------------------------------------------------------

    def HasCapture(self):
        '''
        Returns true if this window has the current mouse capture.
        '''
        msg = 'NotImplementedError: %s' % 'HasCapture in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HasExtraStyle(self, exFlag):
        '''
        Returns true if the window has the given exFlag bit set in
        its extra styles.
        '''
        msg = 'NotImplementedError: %s' % 'HasExtraStyle in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HasFlag(self, flag):
        '''
        Returns true if the window has the given flag bit set.
        '''
        msg = 'NotImplementedError: %s' % 'HasFlag in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HasFocus(self):
        '''
        Returns true if the window (or in case of composite controls,
        its main child window) has focus.
        '''
        win = self.DoFindFocus()
        return ((win == self) or \
                (win == self.GetMainWindowOfCompositeControl()))

    #-----------------------------------------------------------------------

    def HasMultiplePages(self):
        '''
        This method should be overridden to return true if this window
        has multiple pages.

        All standard class with multiple pages such as wxNotebook,
        wxListbook and wxTreebook already override it to return true
        and user-defined classes with similar behaviour should also
        do so, to allow the library to handle such windows appropriately.
        '''
        msg = 'NotImplementedError: %s' % 'HasMultiplePages in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HasScrollbar(self, orient):
        '''
        Returns true if this window currently has a scroll bar for
        this orientation.
        '''
        msg = 'NotImplementedError: %s' % 'HasScrollbar in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        // if scrolling in the given direction is disabled, we can't have the
##        // corresponding scrollbar no matter what
##        if ( !CanScroll(orient) )
##            return false;

##        const wxSize sizeVirt = GetVirtualSize();
##        const wxSize sizeClient = GetClientSize();

##        return orient == wxHORIZONTAL ? sizeVirt.x > sizeClient.x
##                                      : sizeVirt.y > sizeClient.y;


    #-----------------------------------------------------------------------

    def HasTransparentBackground(self):
        '''
        Returns true if this window background is transparent (as, for
        example, for wxStaticText) and should show the parent window
        background.

        This method is mostly used internally by the library itself and
        you normally should not have to call it. You may, however, have
        to override it in your wxWindow-derived class to ensure that
        background is painted correctly.
        '''
        msg = 'NotImplementedError: %s' % \
            'HasTransparentBackground in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Hide(self):
        '''
        Equivalent to calling Show(False).
        '''
        self.ts_Shown = False
##        msg = 'NotImplementedError: %s' % 'Hide in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HideWithEffect(self, effect, timeout=0):
        '''
        This function hides a window, like Hide(), but using a special
        visual effect if possible.

        The parameters of this function are the same as for ShowWithEffect(),
        please see their description there.
        '''
        self.ts_Shown = False
        msg = 'NotImplementedError: %s' % 'HideWithEffect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HitTest(self, pt):
        '''
        Get the window border style from the given flags: this is different
        from simply doing flags & wxBORDER_MASK because it uses
        GetDefaultBorder() to translate wxBORDER_DEFAULT to something
        reasonable.
        '''
        msg = 'NotImplementedError: %s' % 'HitTest in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def HitTestXY(self, x, y):
        '''
        Get the window border style from the given flags: this is different
        from simply doing flags & wxBORDER_MASK because it uses
        GetDefaultBorder() to translate wxBORDER_DEFAULT to something
        reasonable.
        '''
        msg = 'NotImplementedError: %s' % 'HitTestXY in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InformFirstDirection(self, direction, size, availableOtherDir):
        '''
        '''
        if (not (self.GetSizer() is None)):
            return (self.GetSizer().InformFirstDirection(
                direction,
                size,
                availableOtherDir))
        else:
            return (False)

    #-----------------------------------------------------------------------

    def InheritAttributes(self):
        '''
        This function is (or should be, in case of custom controls) called
        during window creation to intelligently set up the window visual
        attributes, that is the font and the foreground and background
        colours.

        By "intelligently" the following is meant: by default, all
        windows use their own GetClassDefaultAttributes() default
        attributes. However if some of the parents attributes are
        explicitly (that is, using SetFont() and not wxWindow::SetOwnFont)
        changed and if the corresponding attribute had not been explicitly
        set for this window itself, then this window takes the same value
        as used by the parent. In addition, if the window overrides
        ShouldInheritColours() to return false, the colours will not
        be changed no matter what and only the font might.

        This rather complicated logic is necessary in order to accommodate
        the different usage scenarios. The most common one is when all
        default attributes are used and in this case, nothing should be
        inherited as in modern GUIs different controls use different fonts
        (and colours) than their siblings so they cannot inherit the same
        value from the parent. However it was also deemed desirable to
        allow to simply change the attributes of all children at once
        by just changing the font or colour of their common parent,
        hence in this case we do inherit the parents attributes.
        '''
        msg = 'NotImplementedError: %s' % 'InheritAttributes in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InheritsBackgroundColour(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
            'InheritsBackgroundColour in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def InternalOnSize(self, event):
        '''
        '''

        if (not (self.GetAutoLayout() is None)):

            self.Layout()

        event.Skip()

    #-----------------------------------------------------------------------

    def InitDialog(self):
        '''
        Sends an EVT_INIT_DIALOG event, whose handler usually transfers data
        to the dialog via validators.

        Reimplemented in wxPanel.
        '''
        if False:
            msg = 'NotImplementedError: %s' % 'InitDialog in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            event = Event()
            event.SetEventSource(self)
            self.GetEventHandler().ProcessEvent(event)


    #-----------------------------------------------------------------------

    def InvalidateBestSize(self):
        '''
        Reset the cached best size value so it will be recalculated the next
        time it is needed.
        '''
        if False:

            msg = 'NotImplementedError: InvalidateBestSize in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            self.ts_BestSizeCache = DEFAULT_SIZE

            # parent's best size calculation may depend on its children's
            # as long as child window we are in is not top level window itself
            # (because the TLW size is never resized automatically)
            # so let's invalidate it as well to be safe:
            if (not (self.ts_Parent is None) and \
                (not (self.ts_Parent.IsTopLevel()))):

                self.ts_Parent.InvalidateBestSize()

    #-----------------------------------------------------------------------

    def IsBeingDeleted(self):
        '''
        Returns true if this window is in process of being destroyed.

        Top level windows are not deleted immediately but are rather
        scheduled for later destruction to give them time to process
        any pending messages; see Destroy() description.

        This function returns true if this window, or one of its parent
        windows, is scheduled for destruction and can be useful to avoid
        manipulating it as it is usually useless to do something with
        a window which is on the point of disappearing anyhow.
        '''
        if False:

            msg = 'NotImplementedError: %s' % 'IsBeingDeleted in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            status = (self.ts_IsBeingDeleted) or \
                ((not self.IsTopLevel()) and \
                 (not (self.ts_Parent is None)) and \
                 (self.ts_Parent.IsBeingDeleted()))
            return (status)

    #-----------------------------------------------------------------------

    def IsDoubleBuffered(self):
        '''
        Returns true if the window contents is double-buffered by the
        system, i.e. if any drawing done on the window is really done
        on a temporary backing surface and transferred to the screen
        all at once later.
        '''
        msg = 'NotImplementedError: %s' % 'IsDoubleBuffered in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsEnabled(self):
        '''
        Returns true if the window is enabled, i.e. if it accepts user
        input, false otherwise.

        Notice that this method can return false even if this window itself
        had not been explicitly disabled when one of its parent windows is
        disabled. To get the intrinsic status of this window, use
        IsThisEnabled().
        '''
##        return IsThisEnabled() && (
##            IsTopLevel() || !GetParent() || GetParent()->IsEnabled()
##            )

        return ((self.IsThisEnabled()) and \
                ((self.IsTopLevel()) or \
                 (self.GetParent() is None) or \
                  (self.GetParent().IsEnabled())))

    #-----------------------------------------------------------------------

    def IsExposed(self, x, y, w=0, h=0):
        '''
        Returns true if the given point or rectangle area has been exposed
        since the last repaint.

        Call this in an paint event handler to optimize redrawing by only
        redrawing those areas, which have been exposed.
        '''
        if (w == 0) and \
           (h == 0):

            return (self.IsExposedPoint(wxPoint(x, y)))

        else:

            return (self.IsExposedRect(wxRect(x, y, w, h)))

    #-----------------------------------------------------------------------

    def IsExposedPoint(self, pt):
        '''
        Returns true if the given point or rectangle area has been exposed
        since the last repaint.
        '''
        msg = 'NotImplementedError: %s' % 'IsExposedPoint in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsExposedRect(self, rect):
        '''
        Returns true if the given point or rectangle area has been exposed
        since the last repaint.
        '''
        msg = 'NotImplementedError: %s' % 'IsExposedRect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsFrozen(self):
        '''
        Returns true if the window is currently frozen by a call to Freeze().
        '''
        return (self.ts_Freeze)

    #-----------------------------------------------------------------------

    def IsRetained(self):
        '''
        Returns true if the window is retained, false otherwise.

        Remarks:
        Retained windows are only available on X platforms.

        Reimplemented in wxScrolled< wxPanel >.
        '''
        msg = 'NotImplementedError: %s' % 'IsRetained in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsScrollbarAlwaysShown(self, orient):
        '''
        Return whether a scrollbar is always shown.
        '''
        msg = 'NotImplementedError: %s' % \
            'IsScrollbarAlwaysShown in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def IsShown(self):
        '''
        Returns true if the window is shown, false if it has been hidden.
        '''
##        msg = 'NotImplementedError: %s' % 'IsShown in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (self.ts_Shown and self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def IsShownOnScreen(self):
        '''
        Returns true if the window is physically visible on the screen,
        i.e. it is shown and all its parents up to the toplevel window
        are shown as well.
        '''
##        // A window is shown on screen if it itself is shown and so are all its
##        // parents. But if a window is toplevel one, then its always visible on
##        // screen if IsShown() returns true, even if it has a hidden parent.
##        return IsShown() &&
##               (IsTopLevel() || GetParent() == NULL || GetParent()->IsShownOnScreen());

##        msg = 'NotImplementedError: %s' % 'IsShownOnScreen in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (self.ts_Shown and self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def IsThisEnabled(self):
        '''
        Returns true if this window is intrinsically enabled for user input,
        false otherwise, i.e. if Enable() Enable(false) had been called.
        This method is mostly used for wxWidgets itself, user code
        should normally use IsEnabled() instead.
        '''
        theEarliestAncestor = self.tsFindWindowByAssignedId(
            self.ts_EarliestAncestor)
        if theEarliestAncestor.ts_Enabled:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def ShowWithEffect(self, effect, timeout=0):
        '''
        This function shows a window, like Show(), but using a special
        visual effect if possible.

        Parameters:
        effect  The effect to use.

        timeout         The timeout parameter specifies the time of the

        animation, in milliseconds. If the default value of 0 is used, the
        default animation time for the current platform is used.

        Note:
        Currently this function is only implemented in wxMSW and wxOSX
        (for wxTopLevelWindows only in Carbon version and for any kind of
        windows in Cocoa) and does the same thing as Show() in the other
        ports.
        '''
        msg = 'NotImplementedError: %s' % 'ShowWithEffect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        return (self.ts_Shown and self.ts_Handle is not None)

    #-----------------------------------------------------------------------

    def IsTopLevel(self):
        '''
        Returns true if the given window is a top-level one.

        Currently all frames and dialogs are considered to be top-level
        windows (even if they have a parent window).
        '''
        if self in tsWxGTUI_DataBase.WindowTopLevelTasks:
            return (True)
        else:
            return (False)

    #-----------------------------------------------------------------------

    def Layout(self):
        '''
        Invokes the constraint-based layout algorithm or the sizer-based
        algorithm for this window.

        This function does not get called automatically when the window
        is resized because lots of windows deriving from wxWindow do
        not need this functionality. If you want to have Layout() called
        automatically, you should derive from wxPanel (see wxPanel::Layout).

        See also:
        Window Sizing Overview

        Reimplemented in wxPanel, and wxTopLevelWindow.
        '''
        # If there is a sizer, use it instead of the constraints
        if (not (self.GetSizer() is None)):

            try:

                #Use Sizer Layout
                self.logger.debug(
                    'Window.Layout: self.GetSizer()=%s' % str(
                        self.GetSizer()))
                self.GetSizer().Layout()

            except Exception as errorCode:

                self.logger.debug(
                    'Window.Layout: errorCode=%s' % str(errorCode))

                # Use Sizer Virtual Size
                w = 0
                h = 0
                (w, h) = self.GetVirtualSizeTuple()
                self.GetSizer().SetDimension(0, 0, w, h)

            if DEBUG:
                self.logger.debug(
                    'Window.Layout (with Sizer) %s; ClientRect=%s' % (
                        str(self.GetVirtualSizeTuple()),
                        str(self.ClientRect)))

        elif wx.USE_CONSTRAINTS:

            # Find the right constraints values
            self.SatisfyConstraints()

            # Recursively set the real window sizes
            self.SetConstraintSizes()

        return (True)

    #-----------------------------------------------------------------------

    def LayoutPhase1(self, noChanges):
        '''
        First phase of the constraints evaluation: set our own constraints.
        '''
        if wx.USE_CONSTRAINTS:

            constr = self.GetConstraints()

            status = (not constr) or \
                (constr.SatisfyConstraints(self, noChanges))

        else:

            status = False

        return (status)

    #-----------------------------------------------------------------------

    def LayoutPhase2(self, noChanges):
        '''
        Second phase: set the constraints for our children.
        '''
        if wx.USE_CONSTRAINTS:

            noChanges = 0

            # Layout children
            self.DoPhase(1)

            # Layout grand children
            self.DoPhase(2)

            status = True

        else:

            status = False

        return (status)

    #-----------------------------------------------------------------------

    def LineDown(self):
        '''
        This is just a wrapper for ScrollLines(1).
        '''
        msg = 'NotImplementedError: %s' % 'LineDown in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def LineUp(self):
        '''
        This is just a wrapper for ScrollLines(-1).
        '''
        msg = 'NotImplementedError: %s' % 'LineUp in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Lower(self):
        '''
        Lowers the window to the bottom of the window hierarchy (Z-order).
        '''
        msg = 'NotImplementedError: %s' % 'Lower in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def MakeModal(self, modal):
        '''
        Disables all other windows in the application so that the user can
        only interact with this window.

        Parameters:
        modal   If true, this call disables all other windows in the
        application so that the user can only interact with this window.
        If false, the effect is reversed.
        '''
        msg = 'NotImplementedError: %s' % 'MakeModal in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Move(self, pt, flags):
        '''
        Moves the window to the given position.

        Parameters:
        pt      wxPoint object representing the position.
        flags   See SetSize() for more info about this parameter.

        Remarks:
        Implementations of SetSize() can also implicitly implement the Move()
        function, which is defined in the base wxWindow class as the call:
        SetSize(x, y, wxDefaultCoord, wxDefaultCoord, wxSIZE_USE_EXISTING)
        '''
        msg = 'NotImplementedError: %s' % 'Move in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def MoveAfterInTabOrder(self, win):
        '''
        Moves this window in the tab navigation order after the specified
        win.

        This means that when the user presses TAB key on that other window,
        the focus switches to this window.

        Default tab order is the same as creation order, this function and
        MoveBeforeInTabOrder() allow to change it after creating all the
        windows.

        Parameters:
        win     A sibling of this window which should precede it in tab
        order, must not be NULL
        '''
        msg = 'NotImplementedError: %s' % 'MoveAfterInTabOrder in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def MoveBeforeInTabOrder(self, win):
        '''
        Same as MoveAfterInTabOrder() except that it inserts this window
        just before win instead of putting it right after it.
        '''
        msg = 'NotImplementedError: %s' % 'MoveBeforeInTabOrder in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def MoveConstraint(self, x, y):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            if (x != wx.DefaultCoord):

                constr.left.SetValue(x)
                constr.left.SetDone(True)

            if (y != wx.DefaultCoord):

                constr.top.SetValue(y)
                constr.top.SetDone(True)

    #-----------------------------------------------------------------------

    def MoveXY(self, x, y, flags):
        '''
        Moves the window to the given position.
        '''
        msg = 'NotImplementedError: %s' % 'MoveXY in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Navigate(self, flags):
        '''
        Performs a keyboard navigation action starting from this window.

        This method is equivalent to calling NavigateIn() method on the
        parent window.

        Parameters:
        flags   A combination of wxNavigationKeyEvent::IsForward and
        wxNavigationKeyEvent::WinChange.

        Returns:
        Returns true if the focus was moved to another window or false if
        nothing changed.

        Remarks:
        You may wish to call this from a text control custom keypress
        handler to do the default navigation behaviour for the tab key,
        since the standard default behaviour for a multiline text control
        with the wxTE_PROCESS_TAB style is to insert a tab and not navigate
        to the next control. See also wxNavigationKeyEvent and
        HandleAsNavigationKey.
        '''
        msg = 'NotImplementedError: %s' % 'Navigate in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def NavigateIn(self, flags):
        '''
        Performs a keyboard navigation action inside this window.

        See Navigate() for more information.
        '''
##            eventNav = wxNavigationKeyEvent
##            focused = self.FindFocus()
##            eventNav.SetCurrentFocus(focused)
##            eventNav.SetEventSource(focused)
##            eventNav.SetFlags(flags)
##            return (GetEventHandler().ProcessEvent(eventNav))

        msg = 'NotImplementedError: %s' % 'NavigateIn in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def NewControlId(count=1):
        '''
        Create a new ID or range of IDs that are not currently in use.

        The IDs will be reserved until assigned to a wxWindow ID or
        unreserved with UnreserveControlId().

        See Window IDs for more information.

        Parameters:
        count   The number of sequential IDs to reserve.

        Returns:
        Returns the ID or the first ID of the range (i.e. the most negative),
        or wxID_NONE if the specified number of identifiers could not be
        allocated.

        Remarks:
        The Ncurses-based tsWx implementation creates new control Ids via
        a non-static method (See Object.tsNewId()). It currently does not
        support the reference count feature.
        '''
        msg = 'NotImplementedError: %s' % 'NewControlId in tsWxWindow'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def NextControlId(winid):
        '''
        Get the id of the control following the one with the given
        autogenerated) id.
        '''
        msg = 'NotImplementedError: %s' % 'NextControlId in tsWxWindow'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def NotifyWindowOnEnableChange(self, enabled):
        '''
        '''
        msg = 'NotImplementedError: %s' % \
            'NotifyWindowOnEnableChange in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        // Under some platforms there is no need to update the window state
##        // explicitly, it will become disabled when its parent is. On other ones we
##        // do need to disable all windows recursively though.
##    #ifndef wxHAS_NATIVE_ENABLED_MANAGEMENT
##        DoEnable(enabled);
##    #endif // !defined(wxHAS_NATIVE_ENABLED_MANAGEMENT)

##        OnEnabled(enabled);

##        // Disabling a top level window is typically done when showing a modal
##        // dialog and we don't need to disable its children in this case, they will
##        // be logically disabled anyhow (i.e. their IsEnabled() will return false)
##        // and the TLW won't accept any input for them. Moreover, explicitly
##        // disabling them would look ugly as the entire TLW would be greyed out
##        // whenever a modal dialog is shown and no native applications under any
##        // platform behave like this.
##        if ( IsTopLevel() && !enabled )
##            return;

##        // When disabling (or enabling back) a non-TLW window we need to
##        // recursively propagate the change of the state to its children, otherwise
##        // they would still show as enabled even though they wouldn't actually
##        // accept any input (at least under MSW where children don't accept input
##        // if any of the windows in their parent chain is enabled).
##        //
##        // Notice that we must do this even for wxHAS_NATIVE_ENABLED_MANAGEMENT
##        // platforms as we still need to call the children OnEnabled() recursively.
##        for ( wxWindowList::compatibility_iterator node = GetChildren().GetFirst();
##              node;
##              node = node->GetNext() )
##        {
##            wxWindowBase * const child = node->GetData();
##            if ( !child->IsTopLevel() && child->IsThisEnabled() )
##                child->NotifyWindowOnEnableChange(enabled);
##        }

    #-----------------------------------------------------------------------

    def PageDown(self):
        '''
        This is just a wrapper for ScrollPages(1).
        '''
        msg = 'NotImplementedError: %s' % 'PageDown in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PageUp(self):
        '''
        This is just a wrapper for ScrollPages(-1).
        '''
        msg = 'NotImplementedError: %s' % 'PageUp in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PopEventHandler(self, deleteHandler):
        '''
        Removes and returns the top-most event handler on the event handler
        stack.
        ...
        when calling W->PopEventHandler(), the event handler A will be
        removed and B will be the first handler of the stack.

        Note that it is an error to call this function when no event
        handlers were pushed on this window (i.e. when the window itself
        is its only event handler).

        Parameters:
        deleteHandler   If this is true, the handler will be deleted
        after it is removed (and the returned value will be NULL).
        '''
        msg = 'NotImplementedError: %s' % 'PopEventHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PopupMenu(self, menu, pos=wx.DefaultPosition):
        '''
        Pops up the given menu at the specified coordinates, relative to
        this window, and returns control when the user has dismissed the
        menu.

        If a menu item is selected, the corresponding menu event is
        generated and will be processed as usual. If coordinates are not
        specified, the current mouse cursor position is used.

        Parameters:
        menu is the menu to pop up.

        The position where the menu will appear can be specified either as
        a wxPoint pos or by two integers (x and y).

        Remarks:
        Just before the menu is popped up, wxMenu::UpdateUI is called to
        ensure that the menu items are in the correct state. The menu does
        not get deleted by the window. It is recommended to not explicitly
        specify coordinates when calling PopupMenu in response to mouse
        click, because some of the ports (namely, wxGTK) can do a better
        job of positioning the menu in that case.
        '''
        msg = 'NotImplementedError: %s' % 'PopupMenu in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PopupMenuXY(self, menu, x, y):
        '''
        Pops up the given menu at the specified coordinates, relative to
        this window, and returns control when the user has dismissed the
        menu.

        If a menu item is selected, the corresponding menu event is
        generated and will be processed as usual. If coordinates are not
        specified, the current mouse cursor position is used.

        Parameters:
        menu is the menu to pop up.

        The position where the menu will appear can be specified either as
        a wxPoint pos or by two integers (x and y).

        Remarks:
        Just before the menu is popped up, wxMenu::UpdateUI is called to
        ensure that the menu items are in the correct state. The menu does
        not get deleted by the window. It is recommended to not explicitly
        specify coordinates when calling PopupMenu in response to mouse
        click, because some of the ports (namely, wxGTK) can do a better
        job of positioning the menu in that case.
        '''
        msg = 'NotImplementedError: %s' % 'PopupMenuXY in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PostCreate(self, pre):
        '''
        Phase 3 of the 2-phase create <wink!> Call this method after
        precreating the window with the 2-phase create method.
        '''
        msg = 'NotImplementedError: %s' % 'PostCreate in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PostSizeEvent(self):
        '''
        Posts a size event to the window.

        This is the same as SendSizeEvent() with wxSEND_EVENT_POST argument.
        '''
        msg = 'NotImplementedError: %s' % 'PostSizeEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PostSizeEventToParent(self):
        '''
        Posts a size event to the parent of this window.

        This is the same as SendSizeEventToParent() with wxSEND_EVENT_POST
        argument.
        '''
        msg = 'NotImplementedError: %s' % 'PostSizeEventToParent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def PrepareDC(self, dc):
        '''
        Call this function to prepare the device context for drawing a
        scrolled image.
        '''
        msg = 'NotImplementedError: %s' % 'PrepareDC in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def PrevControlId(winid):
        '''
        Get the id of the control preceding the one with the given
        autogenerated) id.
        '''
        msg = 'NotImplementedError: %s' % 'PrevControlId in tsWxWindow'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessEvent(self, event):
        '''
        This function is public in wxEvtHandler but protected in wxWindow
        because for wxWindows you should always call ProcessEvent() on
        the pointer returned by GetEventHandler() and not on the wxWindow
        object itself.

        For convenience, a ProcessWindowEvent() method is provided as a
        synonym for GetEventHandler()->ProcessEvent()

        Note that it is still possible to call these functions directly on
        the wxWindow object (e.g. casting it to wxEvtHandler) but doing
        that will create subtle bugs when windows with event handlers
        pushed on them are involved.

        This holds also for all other wxEvtHandler functions.

        Reimplemented from wxEvtHandler.
        '''
        try:

            # Attempt internal processing of wxEvtHandler.ProcessEvent(event).
            return (self.tsProcessPyEventBinderEvent(event))

        except Exception as e:
            msg = 'NotImplementedError: %s' % 'ProcessEvent in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessPendingEvents(self):
        '''
        See ProcessEvent() for more info about why you should not use
        this function and the reason for making this function protected
        in wxWindow.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'ProcessPendingEvents in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessThreadEvent(self, event):
        '''
        See ProcessEvent() for more info about why you should not use
        this function and the reason for making this function protected
        in wxWindow.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'ProcessThreadEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ProcessWindowEvent(self, event):
        '''
        Convenient wrapper for ProcessEvent().

        This is the same as writing:
        GetEventHandler()->ProcessEvent(event)
        but more convenient. Notice that ProcessEvent() itself cannot be
        called for wxWindow objects as it ignores the event handlers
        associated with the window; use this function instead.
        '''
        self.GetEventHandler().ProcessEvent(event)

    #-----------------------------------------------------------------------

    def ProcessWindowEventLocally(self, event):
        '''
        Wrapper for wxEvtHandler::ProcessEventLocally().

        This method is similar to ProcessWindowEvent() but can be used
        to search for the event handler only in this window and any event
        handlers pushed on top of it. Unlike ProcessWindowEvent() it
        will not propagate the event upwards. But it will use the
        validator and event handlers associated with this window, if any.
        '''
        self.GetEventHandler().ProcessEventLocally(event)

    #-----------------------------------------------------------------------

    def PushEventHandler(self, handler):
        '''
        Pushes this event handler onto the event stack for the window.

        An event handler is an object that is capable of processing the
        events sent to a window. By default, the window is its own event
        handler, but an application may wish to substitute another,
        for example to allow central implementation of event-handling
        for a variety of different window classes.

        wxWindow::PushEventHandler allows an application to set up a
        stack of event handlers, where an event not handled by one event
        handler is handed to the next one in the chain.

        E.g. if you have two event handlers A and B and a wxWindow
        instance W and you call:
        W->PushEventHandler(A);
        W->PushEventHandler(B);
        you will end up with the following situation: ....

        Note that you can use wxWindow::PopEventHandler to remove
        the event handler.

        Parameters:
        handler         Specifies the handler to be pushed. It must
        not be part of a wxEvtHandler chain; an assert will fail if
        it is not unlinked (see wxEvtHandler::IsUnlinked).
        '''
        msg = 'NotImplementedError: %s' % 'PushEventHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def QueueEvent(self, event):
        '''
        See ProcessEvent() for more info about why you should not use
        this function and the reason for making this function protected
        in wxWindow.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'QueueEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Raise(self):
        '''
        Raises the window to the top of the window hierarchy (Z-order).
        '''
        msg = 'NotImplementedError: %s' % 'Raise in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Refresh(self, eraseBackground=True, rect=None):
        '''
        Causes this window, and all of its children recursively
        (except under wxGTK1 where this is not implemented), to be
        repainted.

        Note that repainting does not happen immediately but only
        during the next event loop iteration, if you need to update
        the window immediately you should use Update() instead.

        Parameters:
        eraseBackground         If true, the background will be erased.

        rect                    If non-NULL, only the given rectangle
                                will be treated as damaged.

        See also:
        RefreshRect()

        Reimplemented in wxMenuBar.
        '''
##        {
##            HWND hWnd = GetHwnd();
##            if ( hWnd )
##            {
##                RECT mswRect;
##                const RECT *pRect;
##                if ( rect )
##                {
##                    mswRect.left = rect->x;
##                    mswRect.top = rect->y;
##                    mswRect.right = rect->x + rect->width;
##                    mswRect.bottom = rect->y + rect->height;

##                    pRect = &mswRect;
##                }
##                else
##                {
##                    pRect = NULL;
##                }

##                # RedrawWindow not available on SmartPhone or eVC++ 3
##        #if !defined(__SMARTPHONE__) && !(defined(_WIN32_WCE) && _WIN32_WCE < 400)
##                UINT flags = RDW_INVALIDATE | RDW_ALLCHILDREN;
##                if ( eraseBack )
##                    flags |= RDW_ERASE;

##                ::RedrawWindow(hWnd, pRect, NULL, flags);
##        #else
##                ::InvalidateRect(hWnd, pRect, eraseBack);
##        #endif
##            }
##        }
        if rect is None:
            self.ts_RefreshWindowAndChildren = True
            self.ts_RefreshEraseBackground = eraseBackground
        else:
            self.ts_RefreshOnlyThisRect = rect

    #-----------------------------------------------------------------------

    def RefreshRect(self, rect, eraseBackground=True):
        '''
        Redraws the contents of the given rectangle: the area inside it
        will be repainted.

        This is the same as Refresh() but has a nicer syntax as it can be
        called with a temporary wxRect object as argument like this
        RefreshRect(wxRect(x, y, w, h)).
        '''
        msg = 'NotImplementedError: %s' % 'RefreshRect in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RegisterHotKey(self, hotkeyId, modifiers, virtualKeyCode):
        '''
        Registers a system wide hotkey.

        Every time the user presses the hotkey registered here, this
        window will receive a hotkey event.

        It will receive the event even if the application is in the
        background and does not have the input focus because the user
        is working with some other application.

        Parameters:
        hotkeyId        Numeric identifier of the hotkey. For applications
        this must be between 0 and 0xBFFF. If this function is called from
        a shared DLL, it must be a system wide unique identifier between
        0xC000 and 0xFFFF. This is a MSW specific detail.

        modifiers       A bitwise combination of wxMOD_SHIFT, wxMOD_CONTROL,
        wxMOD_ALT or wxMOD_WIN specifying the modifier keys that have to be
        pressed along with the key.

        virtualKeyCode  The virtual key code of the hotkey.

        Returns:
        true if the hotkey was registered successfully. false if some other
        application already registered a hotkey with this modifier/
        virtualKeyCode combination.

        Remarks:
        Use EVT_HOTKEY(hotkeyId, fnc) in the event table to capture the
        event. This function is currently only implemented under Windows.
        It is used in the Windows CE port for detecting hardware button
        presses.
        '''
        msg = 'NotImplementedError: %s' % 'RegisterHotKey in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ReleaseMouse(self):
        '''
        Releases mouse input captured with CaptureMouse().
        '''
        msg = 'NotImplementedError: %s' % 'ReleaseMouse in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        self.ts_CaptureMouse = False

##        wxLogTrace(wxT("mousecapture"), wxT("ReleaseMouse(%p)"), static_cast<void*>(this))

##        self.logger.wxASSERT_MSG(
##           not self.ts_WinCaptureChanging,
##            'recursive ReleaseMouse call?')

##        self.logger.wxASSERT_MSG(
##            self.GetCapture() == self,
##            'attempt to release mouse, but this window has not captured it')

##        self.logger.wxASSERT_MSG(
##            self.ts_WinCaptureCurrent == self,
##            'attempt to release mouse, but this window has not captured it')

##        self.ts_WinCaptureChanging = True

##        self.DoReleaseMouse()
##        self.ts_WinCaptureCurrent = None

##        if ( self.ts_WinCaptureNext ):

##            ((wxWindowBase*)self.ts_WinCaptureNext->win)->DoCaptureMouse()
##            self.ts_WinCaptureCurrent = self.ts_WinCaptureNext->win

##            wxWindowNext *item = self.ts_WinCaptureNext
##            self.ts_WinCaptureNext = item->next
##            delete item

##        # else: stack is empty, no previous capture

##        self.ts_WinCaptureChanging = False

####        wxLogTrace(wxT("mousecapture"),
####            (const wxChar *) wxT("After ReleaseMouse() mouse is captured by %p"),
####            static_cast<void*>(GetCapture()))


    #-----------------------------------------------------------------------

    def RemoveChild(self, child):
        '''
        Removes a child window.
        '''
##        wxCHECK_RET( child, wxT("can't remove a NULL child") );

##        // removing a child while frozen may result in permanently frozen window
##        // if used e.g. from Reparent(), so thaw it
##        //
##        // NB: IsTopLevel() doesn't return true any more when a TLW child is being
##        //     removed from its ~wxWindowBase, so check for IsBeingDeleted() too
##        if ( IsFrozen() && !child->IsBeingDeleted() && !child->IsTopLevel() )
##            child->Thaw();

##        GetChildren().DeleteObject((wxWindow *)child);
##        child->SetParent(NULL);

        msg = 'NotImplementedError: %s' % 'RemoveChild in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def RemoveEventHandler(self, handler):
        '''
        Find the given handler in the windows event handler stack and
        removes (but does not delete) it from the stack.

        See wxEvtHandler::Unlink() for more info.

        Parameters:
        handler         The event handler to remove, must be non-NULL
        and must be present in this windows event handlers stack.

        Returns:
        Returns true if it was found and false otherwise (this also
        results in an assert failure so this function should only be
        called when the handler is supposed to be there).
        '''
        msg = 'NotImplementedError: %s' % 'RemoveEventHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Reparent(self, newParent):
        '''
        Reparents the window, i.e the window will be removed from its current
        parent window (e.g.
        '''
        msg = 'NotImplementedError: %s' % 'Reparent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        wxWindow *oldParent = GetParent();
##        if ( newParent == oldParent )
##        {
##            // nothing done
##            return false;
##        }

##        const bool oldEnabledState = IsEnabled();

##        // unlink this window from the existing parent.
##        if ( oldParent )
##        {
##            oldParent->RemoveChild(this);
##        }
##        else
##        {
##            wxTopLevelWindows.DeleteObject((wxWindow *)this);
##        }

##        // add it to the new one
##        if ( newParent )
##        {
##            newParent->AddChild(this);
##        }
##        else
##        {
##            wxTopLevelWindows.Append((wxWindow *)this);
##        }

##        // We need to notify window (and its subwindows) if by changing the parent
##        // we also change our enabled/disabled status.
##        const bool newEnabledState = IsEnabled();
##        if ( newEnabledState != oldEnabledState )
##        {
##            NotifyWindowOnEnableChange(newEnabledState);
##        }

##        return true;

    #-----------------------------------------------------------------------

    def ResetConstraints(self):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            constr.left.SetDone(False)
            constr.top.SetDone(False)
            constr.right.SetDone(False)
            constr.bottom.SetDone(False)
            constr.width.SetDone(False)
            constr.height.SetDone(False)
            constr.centreX.SetDone(False)
            constr.centreY.SetDone(False)

        for child in self.ts_Children:

            if (not (child.IsTopLevel())):
                child.ResetConstraints()

    #-----------------------------------------------------------------------

    def SafelyProcessEvent(self, event):
        '''
        See ProcessEvent() for more info about why you should not use
        this function and the reason for making this function protected
        in wxWindow.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'SafelyProcessEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SatisfyConstraints(self):
        '''
        '''
        constr = self.GetConstraints()
        if (constr & constr.AreSatisfied()) > 0:
            wasOk = True
        else:
            wasOk = False

        self.ResetConstraints()   # Mark all constraints as unevaluated

        noChanges = 1

        # if we're a top level panel (i.e. our parent is frame/dialog), our
        # own constraints will never be satisfied any more unless we do it
        # here
        if (wasOk):

            while (noChanges > 0):

                self.LayoutPhase1(noChanges)

        self.LayoutPhase2(noChanges)


    #-----------------------------------------------------------------------

    def ScreenToClient(self, pt):
        '''
        Converts from screen to client window coordinates.

        Parameters:
        pt      The screen position.
        '''
        msg = 'NotImplementedError: %s' % 'ScreenToClient in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ScreenToClientXY(self, x, y):
        '''
        Converts from screen to client window coordinates.
        '''
        msg = 'NotImplementedError: %s' % 'ScreenToClientXY in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ScrollLines(self, lines):
        '''
        If the platform and window class supports it, scrolls the window
        by the given number of lines down, if lines is positive, or up if
        lines is negative.
        '''
        msg = 'NotImplementedError: %s' % 'ScrollLines in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ScrollPages(self, pages):
        '''
        If the platform and window class supports it, scrolls the window
        by the given number of pages down, if pages is positive, or up
        if pages is negative.
        '''
        msg = 'NotImplementedError: %s' % 'ScrollPages in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def ScrollWindow(self, dx, dy, rect=None):
        '''
        Physically scrolls the pixels in the window and move child windows
        accordingly.
        '''
        msg = 'NotImplementedError: %s' % 'ScrollWindow in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SendDestroyEvent(self):
        '''
        Generate wxWindowDestroyEvent for this window.

        This is called by the window itself when it is being destroyed and
        usually there is no need to call it but see wxWindowDestroyEvent
        for explanations of when you might want to do it.
        '''
        if True:

            msg = 'NotImplementedError: %s' % 'SendDestroyEvent in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:

            if self.ts_IsBeingDeleted:

                return

            else:

                self.ts_IsBeingDeleted = True

##                wxWindowDestroyEvent = Event()
##                event = Event(wx.WindowDestroyEvent)
##                event.SetEventSource(self)
##                event.SetId(self.GetId())
##                self.GetEventHandler().ProcessEvent(event)

    #-----------------------------------------------------------------------

    def SendIdleEvents(self, event):
        '''
        Send idle event to window and all subwindows
        '''
        if True:

            msg = 'NotImplementedError: %s' % 'SendIdleEvents in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        needMore = False

##        self.OnInternalIdle()

##        # should we send idle event to this window?
##        if ((wxIdleEvent.GetMode() == wx.IDLE_PROCESS_ALL) or \
##            (self.HasExtraStyle(wx.WS_EX_PROCESS_IDLE))):

##            event.SetEventSource(self)
##            self.HandleWindowEvent(event)

##            if (event.MoreRequested()):
##                needMore = True

##        for child in self.ts_Children:

##            if (child.SendIdleEvents(event)):
##                needMore = True

##        return (needMore)

    #-----------------------------------------------------------------------

    def SendSizeEvent(self, flags=0):
        '''
        This function sends a dummy size event to the window allowing it
        to re-layout its children positions.

        It is sometimes useful to call this function after adding or
        deleting a children after the frame creation or if a child size
        changes. Note that if the frame is using either sizers or
        constraints for the children layout, it is enough to call
        wxWindow::Layout() directly and this function should not be
        used in this case.

        If flags includes wxSEND_EVENT_POST value, this function posts
        the event, i.e. schedules it for later processing, instead of
        dispatching it directly. You can also use PostSizeEvent() as
        a more readable equivalent of calling this function with
        this flag.

        Parameters:

        flags   May include wxSEND_EVENT_POST. Default value is 0.
        '''
        msg = 'NotImplementedError: %s' % 'SendSizeEvent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        wxSizeEvent event(GetSize(), GetId());
##        event.SetEventSource(this);
##        if ( flags & wxSEND_EVENT_POST )
##            wxPostEvent(GetEventHandler(), event);
##        else
##            HandleWindowEvent(event);


    #-----------------------------------------------------------------------

    def SendSizeEventToParent(self, flags=0):
        '''
        Safe wrapper for GetParent()->SendSizeEvent().

        This function simply checks that the window has a valid parent
        which is not in process of being deleted and calls SendSizeEvent()
        on it. It is used internally by windows such as toolbars changes
        to whose state should result in parent re-layout (e.g. when a
        toolbar is added to the top of the window, all the other windows
        must be shifted down).
        '''
        msg = 'NotImplementedError: %s' % 'SendSizeEventToParent in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetAcceleratorTable(self, accel):
        '''
        Sets the accelerator table for this window.
        '''
        assignedId = self.ts_AssignedId
        dbase = tsWxGTUI_DataBase
        try:
            dbase.AcceleratorTableByAssignedId[assignedId] = accel
        except Exception as keyError:

            msg = 'ProgramError: %s' % 'SetAcceleratorTable in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetAccessible(self, accessible):
        '''
        Sets the accessible for this window.

        Any existing accessible for this window will be deleted first,
        if not identical to accessible.
        '''
        msg = 'NotImplementedError: %s' % 'SetAccessible in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetAutoLayout(self, autoLayout):
        '''
        Determines whether the Layout function will be called automatically
        when the window is resized. Please note that this only happens for
        the windows usually used to contain children, namely wx.Panel and
        wx.TopLevelWindow (and the classes deriving from them).

        This method is called implicitly by SetSizer but if you use
        SetConstraints you should call it manually or otherwise the window
        layout will not be correctly updated when the window is resized.
        '''
        self.ts_AutoLayout = autoLayout

    #-----------------------------------------------------------------------

    def SetBackgroundColour(self, colour):
        '''
        Sets the background colour of the window.

        Please see InheritAttributes() for explanation of the
        difference between this method and SetOwnBackgroundColour().

        Parameters:
        colour  The colour to be used as the background colour; pass
        wxNullColour to reset to the default colour. Note that you
        may want to use wxSystemSettings::GetColour() to retrieve a
        suitable colour to use rather than setting an hard-coded one.

        Remarks:
        The background colour is usually painted by the default
        wxEraseEvent event handler function under Windows and
        automatically under GTK. Note that setting the background
        colour does not cause an immediate refresh, so you may wish
        to call wxWindow::ClearBackground or wxWindow::Refresh after
        calling this function. Using this function will disable
        attempts to use themes for this window, if the system
        supports them. Use with care since usually the themes
        represent the appearance chosen by the user to be used
        for all applications on the system.

        Returns:
        True if the colour was really changed, false if it was already set
        to this colour and nothing was done.
        '''
        color = colour.lower()
        validColor = (color in list(tsGTUI.xterm256ColorCodeFromName.keys()))
        if not validColor:
            msg = 'SetBackgroundColour "%s" Invalid in tsWxWindow' % color
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        changedColor = (color != self.ts_BackgroundColour)

        if changedColor:
            self.ts_BackgroundColour = color

        return (changedColor)

    #-----------------------------------------------------------------------

    def SetBackgroundStyle(self, style):
        '''
        Sets the background style of the window.

        The default background style is wxBG_STYLE_ERASE which
        indicates that the window background may be erased in
        EVT_ERASE_BACKGROUND handler. This is a safe, compatibility
        default; however you may want to change it to wxBG_STYLE_SYSTEM
        if you do not define any erase background event handlers
        at all, to avoid unnecessary generation of erase background
        events and always let system erase the background. And you
        should change the background style to wxBG_STYLE_PAINT if
        you define an EVT_PAINT handler which completely overwrites
        the window background as in this case erasing it previously,
        either in EVT_ERASE_BACKGROUND handler or in the system
        default handler, would result in flicker as the background
        pixels will be repainted twice every time the window is
        redrawn. Do ensure that the background is entirely erased
        by your EVT_PAINT handler in this case however as otherwise
        garbage may be left on screen.

        Notice that in previous versions of wxWidgets a common way
        to work around the above mentioned flickering problem was
        to define an empty EVT_ERASE_BACKGROUND handler. Setting
        background style to wxBG_STYLE_PAINT is a simpler and
        more efficient solution to the same problem.
        '''
        changed = (style == wx.BG_STYLE_SYSTEM or \
                   style == wx.BG_STYLE_COLOUR or \
                   style == wx.BG_STYLE_CUSTOM)
##        changed = (style == wx.BG_STYLE_SYSTEM or \
##                   style == wx.BG_STYLE_COLOUR or \
##                   style == wx.BG_STYLE_CUSTOM) and \
##                  (style != self.BackgroundStyle)

        if changed:
            self.ts_BackgroundStyle = style

        return (changed)

    #-----------------------------------------------------------------------

    def SetBestSize(self, *args, **kwargs):
        '''
        This function returns the best acceptable minimal size for the
        window, if applicable. For example, for a static text control,
        it will be the minimal size such that the control label is not
        truncated. For windows containing subwindows (such as wx.Panel),
        the size returned by this function will be the same as the size
        the window would have had after calling Fit.
        '''
        parent = args[0]
        size = kwargs['size']
        style = kwargs['style']
        name = kwargs['name']
        self.ts_BestSize = len(name)

        return (self.ts_BestSize)

    #-----------------------------------------------------------------------

    def SetBestVirtualSize(self, *args, **kwargs):
        '''
        This function returns the best acceptable minimal size for the
        window, if applicable. For example, for a static text control,
        it will be the minimal size such that the control label is not
        truncated. For windows containing subwindows (such as wx.Panel),
        the size returned by this function will be the same as the size
        the window would have had after calling Fit.
        '''
        parent = args[0]
        size = kwargs['size']
        style = kwargs['style']
        name = kwargs['name']
        self.BestVirtualSize = len(name) # TBD - Label

        return (self.ts_BestVirtualSize)

    #-----------------------------------------------------------------------

    def SetBorder(self, flags):
        '''
        '''
        self.ts_Border = flags

    #-----------------------------------------------------------------------

    def SetCanFocus(self, canFocus):
        '''
        his method is only implemented by ports which have support for
        native TAB traversal (such as GTK+ 2.0).
        '''
        msg = 'NotImplementedError: %s' % 'SetCanFocus in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetCaret(self, caret):
        '''
        Sets the caret() associated with the window.
        '''
        self.ts_Caret = caret

    #-----------------------------------------------------------------------

    def SetClientAreaOrigin(self, pos):
        '''
        '''
        if self.Parent is None:
            self.ts_ClientAreaOrigin = wxPoint(0, 0)
        else:
            newClientAreaOrigin = self.tsGetClassInstanceFromTuple(pos, wxPoint)
            self.ts_ClientRect.x = newClientAreaOrigin.x
            self.ts_ClientRect.y = newClientAreaOrigin.y
            self.ts_ClientAreaOrigin = newClientAreaOrigin

    #-----------------------------------------------------------------------

    def SetClientRect(self, rect):
        '''
        This sets the size of the window client area in pixels.
        '''
        self.ts_ClientRect = self.tsGetClassInstanceFromTuple(rect, wxRect)

    #-----------------------------------------------------------------------

    def SetClientSize(self, size):
        '''
        This sets the size of the window client area in pixels.

        Using this function to size a window tends to be more device-
        independent than SetSize(), since the application need not worry
        about what dimensions the border or title bar have when trying
        to fit the window around panel items, for example.
        '''
        newClientSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        self.ts_ClientRect.width = newClientSize.width
        self.ts_ClientRect.height = newClientSize.height
        self.ts_ClientSize = newClientSize

    #-----------------------------------------------------------------------

    def SetClientSizeWH(self, width, height):
        '''
        This sets the size of the window client area in pixels.

        Using this function to size a window tends to be more device-
        independent than SetSize(), since the application need not worry
        about what dimensions the border or title bar have when trying
        to fit the window around panel items, for example.
        '''
        self.SetClientSize(wxSize(width, height))

    #-----------------------------------------------------------------------

    def SetConstraints(self, constraints):
        '''
        Sets the window to have the given layout constraints.
        '''
##        msg = 'NotImplementedError: %s' % 'SetConstraints in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if (not (self.ts_Constraints is None) ):

            self.UnsetConstraints(self.ts_Constraints)
            del self.ts_Constraints

        self.ts_Constraints = constraints
        if (not (self.ts_Constraints is None) ):

            # Make sure other windows know they're part of a 'meaningful
            # relationship'
            if ( self.ts_Constraints.left.GetOtherWindow() and \
                 (self.ts_Constraints.left.GetOtherWindow() != self) ):

                self.ts_Constraints.left.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.top.GetOtherWindow() and \
                 (self.ts_Constraints.top.GetOtherWindow() != self) ):

                self.ts_Constraints.top.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.right.GetOtherWindow() and \
                 (self.ts_Constraints.right.GetOtherWindow() != self) ):

                self.ts_Constraints.right.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.bottom.GetOtherWindow() and \
                 (self.ts_Constraints.bottom.GetOtherWindow() != self) ) :

                self.ts_Constraints.bottom.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.width.GetOtherWindow() and \
                 (self.ts_Constraints.width.GetOtherWindow() != self) ):

                self.ts_Constraints.width.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.height.GetOtherWindow() and \
                 (self.ts_Constraints.height.GetOtherWindow() != self) ):

                self.ts_Constraints.height.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.centreX.GetOtherWindow() and \
                 (self.ts_Constraints.centreX.GetOtherWindow() != self) ):

                self.ts_Constraints.centreX.GetOtherWindow().AddConstraintReference(self)

            if ( self.ts_Constraints.centreY.GetOtherWindow() and \
                 (self.ts_Constraints.centreY.GetOtherWindow() != self) ):

                self.ts_Constraints.centreY.GetOtherWindow().AddConstraintReference(self)

    #-----------------------------------------------------------------------

    def SetConstraintSizes(self, Recurse=False):
        '''
        '''
        # Need to distinguish between setting the 'fake' size for windows
        # and sizers, and setting the real values.
        constr = self.GetConstraints()
        if (not (constr is None) and \
            constr.AreSatisfied()):

            x = constr.left.GetValue()
            y = constr.top.GetValue()
            w = constr.width.GetValue()
            h = constr.height.GetValue()

            if ((constr.width.GetRelationship() != wx.AsIs) or \
                (constr.height.GetRelationship() != wx.AsIs)):

                # We really shouldn't set negative sizes for the windows
                # so make them at least of 1*1 size
                if w > 0:
                    wtmp = w
                else:
                    wtmp = 1

                if h > 0:
                    htmp = h
                else:
                    htmp = 1
                self.Rect = wxRect(x, y, wtmp, htmp)

            else:

                # If we don't want to resize this window, just move it...
                self.Move(x, y)

        elif (not (constr is None)):

            self.logger.debug(
                'Constraints not satisfied for %s named "%s".',
                self.GetClassInfo().GetClassName(),
                self.GetName())

        if (Recurse):

            for win in self.ts_Children:

                if ((not (win.IsTopLevel())) and \
                    (win.GetConstraints())):

                    win.SetConstraintSizes()

    #-----------------------------------------------------------------------

    def SetContainingSizer(self, sizer):
        '''
        This normally does not need to be called by user code.

        It is called when a window is added to a sizer, and is used so
        the window can remove itself from the sizer when it is destroyed.
        '''
        # adding a window to a sizer twice is going to result in fatal and
        # hard to debug problems later because when deleting the second
        # associated wxSizerItem we're going to dereference a dangling
        # pointer; so try to detect this as early as possible
        if ((sizer is None) or (self.ts_ContainingSizer == sizer)):
            msg = 'Adding a window to the same sizer twice?'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        self.ts_ContainingSizer = sizer

    #-----------------------------------------------------------------------

    def SetCursor(self, cursor):
        '''
        Sets the window cursor.

        Notice that the window cursor also sets it for the children of
        the window implicitly.

        The cursor may be wxNullCursor in which case the window cursor
        will be reset back to default.

        Parameters:
        cursor  Specifies the cursor that the window should normally
        display.
        '''
        msg = 'NotImplementedError: %s' % 'SetCursor in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetDimensions(self, x, y, width, height, sizeFlags=wx.SIZE_AUTO):
        '''
        Sets the position and size of the window in pixels. The sizeFlags
        parameter indicates the interpretation of the other params if they
        are equal to -1.
        '''
        self.ts_Rect = self.tsGetClassInstanceFromTuple(
            (x, y, width, height), wxRect)

    #-----------------------------------------------------------------------

    def SetDoubleBuffered(self, on):
        '''
        Currently wxGTK2 only.
        '''
        self.ts_DoubledBuffered = on

    #-----------------------------------------------------------------------

    def SetDropTarget(self, dropTarget):
        '''
        Associates a drop target with this window.

        If the window already has a drop target, it is deleted.
        '''
        msg = 'NotImplementedError: %s' % 'SetDropTarget in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetEventHandler(self, handler):
        '''
        Sets the event handler for this window.

        Note that if you use this function you may want to use as the
        "next" handler of handler the window itself; in this way when
        handler does not process an event, the window itself will have
        a chance to do it.

        Parameters:
        handler         Specifies the handler to be set. Cannot be NULL.
        '''
        msg = 'NotImplementedError: %s' % 'SetEventHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetExtraStyle(self, exStyle):
        '''
        Sets the extra style bits for the window.

        The currently defined extra style bits are reported in the
        class description.
        '''
        msg = 'NotImplementedError: %s' % 'SetExtraStyle in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetFocus(self):
        '''
        This sets the window to receive keyboard input.
        '''
        pass
##        try:
##            topLevelSiblings = self.GetTopLevelSiblings()
##            for classId in topLevelSiblings:
##                theClass = wx.WindowsByAssignedId[classId]
##                if theClass is self:
##                    self.ts_HasFocus = True
##                else:
##                    self.ts_HasFocus = False
##        except Exception, e:
##            msg = 'SetFocus (in tsWxWindow): %s' % e
##            self.logger.error(msg)
##            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetFocusFromKbd(self):
        '''
        This function is called by wxWidgets keyboard navigation code when
        the user gives the focus to this window from keyboard.
        '''
        FocusFromKbd = self.ts_FocusFromKbd.ts_EarliestAncestor
        if FocusFromKbd is None:
            msg = 'NotImplementedError: %s' % 'SetFocusFromKbd in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        panelList = []
        foregroundList = []
        backgroundList = []
        outputDataBase = {}
        inputDataBase = tsWxGTUI_DataBase.CursesPanels
        for record in inputDataBase:
            if record == 'name':
                pass # outputDataBase['name'] = record
            else:
                assignedId = inputDataBase[record]['assignedId']
                earliestAncestor = inputDataBase[record]['earliestAncestor']
                handle = inputDataBase[record]['handle']
                label = inputDataBase[record]['label']
                name = inputDataBase[record]['name']
                panel = inputDataBase[record]['panel']
##                (prefix, suffix) = panel.split('-')
##                index = int(suffix) - 10000
                panelList += [panel]
                if earliestAncestor == FocusFromKbd:
                    foregroundList += [handle]
                else:
                    backgroundList += [handle]

        for i in range(0, len(backgroundList)):
            panelList[i].replace(backgroundList[i])

        for i in range(0, len(foregroundList)):
            panelList[i + len(backgroundList)].replace(foregroundList[i])

        self.tsCursesPanelUpdatePanels()
        self.tsCursesDoUpdate()

    #-----------------------------------------------------------------------

    def SetFont(self, font):
        '''
        Sets the font for this window.

        This function should not be called for the parent window if
        you do not want its font to be inherited by its children, use
        SetOwnFont() instead in this case and see InheritAttributes()
        for more explanations.

        Please notice that the given font is not automatically used
        for wxPaintDC objects associated with this window, you need
        to call wxDC::SetFont too. However this font is used by any
        standard controls for drawing their text as well as by
        GetTextExtent().

        Parameters:
        font    Font to associate with this window, pass wxNullFont
        to reset to the default font.

        Returns:
        True if the font was really changed, False if it was already
        set to this font and nothing was done.
        '''
        msg = 'NotImplementedError: %s' % 'SetFont in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetForegroundColour(self, colour):
        '''
        Sets the foreground colour of the window.

        Please see InheritAttributes() for explanation of the difference
        between this method and SetOwnForegroundColour().

        Parameters:
        colour  The colour to be used as the foreground colour; pass
        wxNullColour to reset to the default colour.

        Remarks:
        The meaning of foreground colour varies according to the window
        class; it may be the text colour or other colour, or it may not
        be used at all.

        Returns:
        true if the colour was really changed, false if it was already
        set to this colour and nothing was done.
        '''
        color = colour.lower()

        validColor = (color in list(tsGTUI.xterm256ColorCodeFromName.keys()))
        if not validColor:
            msg = 'SetForegroundColour "%s" Invalid in tsWxWindow' % color
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        changedColor = (color != self.ts_ForegroundColour)

        if changedColor:
            self.ts_ForegroundColour = color

        return (changedColor)

    #-----------------------------------------------------------------------

    def SetHelpText(self, helpText):
        '''
        Sets the help text to be used as context-sensitive help for this
        window.

        Note that the text is actually stored by the current wxHelpProvider
        implementation, and not in the window object itself.
        '''
        msg = 'NotImplementedError: %s' % 'SetHelpText in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetHelpTextForId(self, text):
        '''
        Associate this help text with all windows with the same id as this one.
        '''
        msg = 'NotImplementedError: %s' % 'SetHelpTextForId in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetId(self, winid):
        '''
        Sets the identifier of the window.

        Remarks:
        Each window has an integer identifier. If the application has not
        provided one, an identifier will be generated. Normally, the
        identifier should be provided on creation and should not be
        modified subsequently.
        '''
        self.ts_Id = winid

    #-----------------------------------------------------------------------

    def SetInitialBestSize(self, size=wx.DefaultSize):
        '''
        Sets the initial window size if none is given (i.e. at least one
        of the components of the size passed to ctor/Create() is
        wxDefaultCoord).

        Deprecated.
        '''
        msg = 'NotImplementedError: %s' % 'SetInitialBestSize in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetInitialSize(self, size=wx.DefaultSize):
        '''
        A "Smart" SetSize that will fill in default size components with the
        window best size values.

        Also sets the windows minsize to the value passed in for use with
        sizers. This means that if a full or partial size is passed to this
        function then the sizers will use that size instead of the results
        of GetBestSize() to determine the minimum needs of the window for
        layout.

        Most controls will use this to set their initial size, and their
        min size to the passed in value (if any.)
        '''
        # Set the min size to the size passed in.  This will usually either
        # be wxDefaultSize or the size passed to this window's ctor/Create
        # function.
        self.SetMinSize(size)

        # Merge the size with the best size if needed
        best = self.GetEffectiveMinSize()

        # If the current size doesn't match then change it
        if (self.GetSize() != best):
            self.SetSize(best)

    #-----------------------------------------------------------------------

    def SetLabel(self, label):
        '''
        Sets the windows label.

        Parameters:
        label   The window label.
        '''
        if DEBUG:
            self.logger.debug(
                'SetLabel: label="%s" (formerly="%s") for className=%s' % (
                    label, self.Label, self.ClassName))

        if self.ClassName == 'Frame' or \
           self.ClassName == 'Dialog':

            self.ts_Title = label

        elif self.ClassName == 'Button':

            self.ts_ButtonText = label

        elif self.ClassName == 'StaticText':

            self.ts_ButtonText = label

        else:

            self.ts_Label = label

    #-----------------------------------------------------------------------

    def SetLayoutDirection(self, dir):
        '''
        Set the layout direction (LTR or RTL) for this window.
        '''
        msg = 'NotImplementedError: %s' % 'SetLayoutDirection in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetMaxClientSize(self, size=wx.DefaultSize):
        '''
        Sets the maximum client size of the window, to indicate to the
        sizer layout mechanism that this is the maximum possible size
        of its client area.

        Note that this method is just a shortcut for:
        SetMaxSize(ClientToWindowSize(size))
        '''
        self.SetMaxSize(self.ClientToWindowSize(size))

    #-----------------------------------------------------------------------

    def SetMaxSize(self, maxSize):
        '''
        Sets the maximum size of the window, to indicate to the sizer
        layout mechanism that this is the maximum possible size.
        '''
        self.ts_MaxSize = self.tsGetClassInstanceFromTuple(maxSize, wxSize)

    #-----------------------------------------------------------------------

    def SetMinClientSize(self, size=wx.DefaultSize):
        '''
        Sets the minimum client size of the window, to indicate to the sizer
        layout mechanism that this is the minimum required size of windows
        client area.

        You may need to call this if you change the window size after
        construction and before adding to its parent sizer.

        Note, that just as with SetMinSize(), calling this method does not
        prevent the program from explicitly making the window smaller than
        the specified size.

        Note that this method is just a shortcut for:
        SetMinSize(ClientToWindowSize(size))
        '''
        self.SetMinSize(self.ClientToWindowSize(size))

    #-----------------------------------------------------------------------

    def SetMinSize(self, minSize):
        '''
        Sets the minimum size of the window, to indicate to the sizer layout
        mechanism that this is the minimum required size.

        You may need to call this if you change the window size after
        construction and before adding to its parent sizer.

        Notice that calling this method does not prevent the program from
        making the window explicitly smaller than the specified size by
        calling SetSize(), it just ensures that it will not become smaller
        than this size during the automatic layout.
        '''
        self.ts_MinSize = self.tsGetClassInstanceFromTuple(minSize, wxSize)

    #-----------------------------------------------------------------------

    def SetName(self, name):
        '''
        Sets the windows name.

        Parameters:
        name    A name to set for the window.
        '''
        self.ts_Name = name

    #-----------------------------------------------------------------------

    def SetNextHandler(self, handler):
        '''
        wxWindows cannot be used to form event handler chains; this
        function thus will assert when called.

        Note that instead you can use PushEventHandler() or
        SetEventHandler() to implement a stack of event handlers
        to override wxWindow own event handling mechanism.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'SetNextHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetOwnBackgroundColour(self, colour):
        '''
        Sets the background colour of the window but prevents it from
        being inherited by the children of this window.
        '''
        msg = 'NotImplementedError: %s' % \
            'SetOwnBackgroundColour in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetOwnFont(self, font):
        '''
        Sets the font of the window but prevents it from being inherited
        by the children of this window.
        '''
        msg = 'NotImplementedError: %s' % 'SetOwnFont in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetOwnForegroundColour(self, colour):
        '''
        Sets the foreground colour of the window but prevents it from
        being inherited by the children of this window.
        '''
        msg = 'NotImplementedError: %s' % \
            'SetOwnForegroundColour in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetPalette(self, pal):
        '''
        Deprecated:
        use wxDC::SetPalette instead.
        '''
        msg = 'NotImplementedError: %s' % 'SetPalette in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetParent(self, parent):
        '''
        Set the parent window of this window, or None if there is not one.
        '''
        self.ts_Parent = parent

    #-----------------------------------------------------------------------

    def SetPosition(self, pt, flags=wx.SIZE_USE_EXISTING):
        '''
        Moves the window to the given position.
        '''
##        SIZE_USE_EXISTING         = 0x0000
##        SIZE_AUTO_WIDTH           = 0x0001
##        SIZE_AUTO_HEIGHT          = 0x0002
##        SIZE_AUTO                 = (SIZE_AUTO_WIDTH | SIZE_AUTO_HEIGHT)
##        SIZE_ALLOW_MINUS_ONE      = 0x0004
##        SIZE_NO_ADJUSTMENTS       = 0x0008
##        SIZE_FORCE                = 0x0010

        if flags != wx.SIZE_USE_EXISTING:
            thePos = self.tsGetClassInstanceFromTuple(pt, wxPoint)

            self.ts_Rect.x = thePos.x
            self.ts_Rect.y = thePos.y

    #-----------------------------------------------------------------------

    def SetPreviousHandler(self, handler):
        '''
        wxWindows cannot be used to form event handler chains; this
        function thus will assert when called.

        Note that instead you can use PushEventHandler() or SetEventHandler()
        to implement a stack of event handlers to override wxWindows own
        event handling mechanism.

        Reimplemented from wxEvtHandler.
        '''
        msg = 'NotImplementedError: %s' % 'SetPreviousHandler in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetRect(self, rect, sizeFlags=wx.SIZE_AUTO):
        '''
        Sets the position and size of the window in pixels using a wx.Rect.
        '''
##        SIZE_USE_EXISTING         = 0x0000
##        SIZE_AUTO_WIDTH           = 0x0001
##        SIZE_AUTO_HEIGHT          = 0x0002
##        SIZE_AUTO                 = (SIZE_AUTO_WIDTH | SIZE_AUTO_HEIGHT)
##        SIZE_ALLOW_MINUS_ONE      = 0x0004
##        SIZE_NO_ADJUSTMENTS       = 0x0008
##        SIZE_FORCE                = 0x0010
        self.ts_Rect = self.tsGetClassInstanceFromTuple(rect, wxRect)

    #-----------------------------------------------------------------------

    def SetScrollPos(self,
                     orientation,
                     pos,
                     refresh=True):
        '''
        Sets the position of one of the built-in scrollbars.
        '''
        msg = 'NotImplementedError: %s' % 'SetScrollPos in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetScrollbar(self,
                     orientation,
                     position,
                     thumbSize,
                     range,
                     refresh=True):
        '''
        Sets the scrollbar properties of a built-in scrollbar.

        Parameters:


        orientation     Determines the scrollbar whose page size is to
                        be set. May be wxHORIZONTAL or wxVERTICAL.
        position        The position of the scrollbar in scroll units.

        thumbSize       The size of the thumb, or visible portion of the
                        scrollbar, in scroll units.

        range           The maximum position of the scrollbar.

        refresh         true to redraw the scrollbar, false otherwise.

        Remarks:

        Let us say you wish to display 50 lines of text, using the same
        font. The window is sized so that you can only see 16 lines at
        a time. You would use:

                    scrollbar->SetScrollbar(wxVERTICAL, 0, 16, 50);

        The page size is 1 less than the thumb size so that the last
        line of the previous page will be visible on the next page,
        to help orient the user. Note that with the window at this
        size, the thumb position can never go above 50 minus 16, or 34.
        You can determine how many lines are currently visible by
        dividing the current view size by the character height in
        pixels. When defining your own scrollbar behaviour, you will
        always need to recalculate the scrollbar settings when the
        window size changes. You could therefore put your scrollbar
        calculations and SetScrollbar() call into a function named
        AdjustScrollbars, which can be called initially and also
        from a wxSizeEvent event handler function.
        '''
        msg = 'NotImplementedError: %s' % 'SetScrollbar in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetSize(self, size):
        '''
        Sets the size of the window in pixels.

        The size is specified using a wxRect, wxSize or by a couple of
        int objects.

        Remarks:
        This form must be used with non-default width and height values.
        '''
        self.ts_Size = self.tsGetClassInstanceFromTuple(size, wxSize)

    #-----------------------------------------------------------------------

    def SetSizeConstraint(self, x, y, w, h):
        '''
        '''
        constr = self.GetConstraints()
        if (not (constr is None)):

            if (x != wx.DefaultCoord):

                constr.left.SetValue(x)
                constr.left.SetDone(True)

            if (y != wx.DefaultCoord):

                constr.top.SetValue(y)
                constr.top.SetDone(True)

            if (w != wx.DefaultCoord):

                constr.width.SetValue(w)
                constr.width.SetDone(True)

            if (h != wx.DefaultCoord):

                constr.height.SetValue(h)
                constr.height.SetDone(True)

    #-----------------------------------------------------------------------

    def SetSizeHints(self,
                     minSize,
                     maxSize=wx.DefaultSize,
                     incSize=wx.DefaultSize):
        '''
        Use of this function for windows which are not toplevel windows
        (such as wxDialog or wxFrame) is discouraged.

        Please use SetMinSize() and SetMaxSize() instead.
        '''
        msg = 'NotImplementedError: %s' % 'SetSizeHints in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetSizeWH(self, width, height):
        '''
        Sets the size of the window in pixels.
        '''
        self.ts_Rect.width = width
        self.ts_Rect.height = height

    #-----------------------------------------------------------------------

    def SetSizer(self, sizer, deleteOld=True):
        '''
        Sets the window to have the given layout sizer.

        The window will then own the object, and will take care of its
        deletion. If an existing layout constraints object is already
        owned by the window, it will be deleted if the deleteOld parameter
        is true.

        Note that this function will also call SetAutoLayout() implicitly
        with true parameter if the sizer is non-NULL and false otherwise
        so that the sizer will be effectively used to layout the window
        children whenever it is resized.

        Parameters:
        sizer   The sizer to set. Pass NULL to disassociate and
        conditionally delete the windows sizer. See below.

        deleteOld       If true (the default), this will delete any
        pre-existing sizer. Pass false if you wish to handle deleting
        the old sizer yourself but remember to do it yourself in this
        case to avoid memory leaks.

        Remarks:
        SetSizer enables and disables Layout automatically.
        '''
##        msg = 'NotImplementedError: %s' % 'SetSizer in tsWxWindow'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        self.logger.wxASSERT_MSG(
            (sizer is not None),
            'Window.SetSizer sizer cannot be %s.' % sizer)

        self.logger.wxASSERT_MSG(
            (not (isinstance(sizer, tuple))),
            'Window.SetSizer sizer instance cannot be %s.' % str(sizer))

        if deleteOld:

            if (not (self.ts_Sizer is None)):
                oldSizer = self.ts_Sizer
                del oldSizer

        self.ts_Sizer = sizer

    #-----------------------------------------------------------------------

    def SetSizerAndFit(self, sizer, deleteOld=True):
        '''
        This method calls SetSizer() and then wxSizer::SetSizeHints which
        sets the initial window size to the size needed to accommodate all
        sizer elements and sets the size hints which, if this window is a
        top level one, prevent the user from resizing it to be less than
        this minimal size.
        '''
        msg = 'NotImplementedError: %s' % 'SetSizerAndFit in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetStyle(self, style):
        '''
        Sets the style of the window.
        '''
        self.ts_Style = style

    #-----------------------------------------------------------------------

    def SetThemeEnabled(self, enableTheme):
        '''
        This function tells a window if it should use the systems "theme"
        code to draw the windows background instead of its own background
        drawing code.

        This does not always have any effect since the underlying platform
        obviously needs to support the notion of themes in user defined
        windows. One such platform is GTK+ where windows can have (very
        colourful) backgrounds defined by a users selected theme.

        Dialogs, notebook pages and the status bar have this flag set to
        true by default so that the default look and feel is simulated best.
        '''
        msg = 'NotImplementedError: %s' % 'SetThemeEnabled in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetToolTip(self, tip):
        '''
        Attach a tooltip to the window.

        wxToolTip pointer can be NULL in the overload taking the pointer,
        meaning to unset any existing tooltips; however UnsetToolTip()
        provides a more readable alternative to this operation.

        Notice that these methods are always available, even if wxWidgets
        was compiled with wxUSE_TOOLTIPS set to 0, but do not do anything
        in this case.
        '''
        msg = 'NotImplementedError: %s' % 'SetToolTip in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetToolTipString(self, tip):
        '''
        Attach a tooltip to the window.

        wxToolTip pointer can be NULL in the overload taking the pointer,
        meaning to unset any existing tooltips; however UnsetToolTip()
        provides a more readable alternative to this operation.

        Notice that these methods are always available, even if wxWidgets
        was compiled with wxUSE_TOOLTIPS set to 0, but do not do anything
        in this case.
        '''
        msg = 'NotImplementedError: %s' % 'SetToolTipString in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetTopLevelAncestor(self, candidate):
        '''
        Set top-level GUI object of our earliest ancestor.
        '''

        self.logger.notice(
            'Begin SetTopLevelAncestor: [%s].' % self.ts_EarliestAncestor)

        try:
            theLabel = candidate.ts_Label
        except AttributeError as e:
            self.logger.warning(
                '%s.SetTopLevelAncestor: Exception = %s' % (__title__, str(e)))
            theLabel = None

        try:
            theTitle = candidate.ts_Title
        except AttributeError as e:
            self.logger.warning(
                '%s.SetTopLevelAncestor: Exception = %s' % (__title__, str(e)))
            theTitle = None

        if candidate.theFirstCallerClassName in wx.TopLevelClasses:

            if candidate.ts_Parent is None:

                # Normal Top-Level Window having no parent
                self.ts_EarliestAncestor = candidate.ts_AssignedId

                fmt = 'SetTopLevelAncestor (accepted): ' + \
                    'assignedId="%d"; ' + \
                    'name="%s"; ' + \
                    'label="%s"; ' + \
                    'title="%s".'
                self.logger.debug(fmt % (candidate.ts_AssignedId,
                                         candidate.ts_Name,
                                         theLabel,
                                         theTitle))

                self.SetTopLevelSiblings(candidate)

            elif candidate.theFirstCallerClassName == 'Dialog':

                # Normal Top-Level Modal Window having a parent
                self.ts_EarliestAncestor = candidate.ts_AssignedId

                fmt = 'SetTopLevelAncestor (accepted): ' + \
                    'assignedId="%d"; ' + \
                    'name="%s"; ' + \
                    'label="%s"; ' + \
                    'title="%s"; ' + \
                    'parentAssignedId="%d"; ' + \
                    'parentName="%s; ' + \
                    'parentLabel="%s; ' + \
                    'parentTitle="%s"".'
                self.logger.debug(fmt % (candidate.ts_AssignedId,
                                         candidate.ts_Name,
                                         candidate.ts_Label,
                                         candidate.ts_Title,
                                         candidate.ts_Parent.ts_AssignedId,
                                         candidate.ts_Parent.ts_Name,
                                         candidate.ts_Parent.ts_Label,
                                         candidate.ts_Parent.ts_Title))

                self.SetTopLevelSiblings(candidate)

            else:

                # Abnormal Top-Level Window having a parent
                self.ts_EarliestAncestor = candidate.ts_Parent.ts_AssignedId

                fmt = 'SetTopLevelAncestor (has parent): ' + \
                    'assignedId="%d"; ' + \
                    'name="%s"; ' + \
                    'label="%s"; ' + \
                    'title="%s";' + \
                    'parentAssignedId="%d"; ' + \
                    'parentName="%s; ' + \
                    'parentLabel="%s; ' + \
                    'parentTitle="%s".'
                self.logger.warning(fmt % (candidate.ts_AssignedId,
                                           candidate.ts_Name,
                                           candidate.ts_Label,
                                           candidate.ts_Title,
                                           candidate.ts_Parent.ts_AssignedId,
                                           candidate.ts_Parent.ts_Name,
                                           candidate.ts_Parent.ts_Label,
                                           candidate.ts_Parent.ts_Title))

        else:

            if candidate.ts_Parent is None:

                # Abnormal non-Top-Level Window having a parent
                self.ts_EarliestAncestor = candidate.ts_Parent

                fmt = 'SetTopLevelAncestor (no parent, and not in %s): ' + \
                    'assignedId="%d"; name="%s".'
                self.logger.warning(fmt % (wx.TopLevelClasses,
                                           candidate.ts_AssignedId,
                                           candidate.ts_Name))

            elif candidate.ts_Parent.ts_EarliestAncestor is not None:

                # Normal non-Top-Level Window having an ancestor
                self.ts_EarliestAncestor = (
                    candidate.ts_Parent.ts_EarliestAncestor)

                fmt = 'SetTopLevelAncestor (child with ancestor in %s): ' + \
                    'assignedId="%d"; ' + \
                    'name="%s"; ' + \
                    'parentAssignedId="%d"; ' + \
                    'parentName="%s".'
                self.logger.debug(fmt % (wx.TopLevelClasses,
                                         candidate.ts_AssignedId,
                                         candidate.ts_Name,
                                         candidate.ts_Parent.ts_AssignedId,
                                         candidate.ts_Parent.ts_Name))

            else:

                # Abnormal non-Top-Level Window having a parent
                self.ts_EarliestAncestor = candidate.ts_Parent

                fmt = 'SetTopLevelAncestor (parent and not in %s): ' \
                    'assignedId="%d"; ' + \
                    'name="%s"; ' + \
                    'parentAssignedId="%d"; ' + \
                    'parentName="%s".'
                self.logger.warning(fmt % (wx.TopLevelClasses,
                                           candidate.ts_AssignedId,
                                           candidate.ts_Name,
                                           candidate.ts_Parent.ts_AssignedId,
                                           candidate.ts_Parent.ts_Name))

        tsWxGTUI_DataBase.WindowTopLevelAncestors[
            self] = self.ts_EarliestAncestor

        self.logger.notice(
            'End SetTopLevelAncestor: [%s].' % self.ts_EarliestAncestor)

    #-----------------------------------------------------------------------

    def SetTopLevelSiblings(self, candidate):
        '''
        '''

        topLevelSiblings = tsWxGTUI_DataBase.WindowsByShowOrder['OrderOfShow']

        self.logger.notice(
            'Begin SetTopLevelSiblings: %s.' % topLevelSiblings)

        try:
            theTitle = candidate.ts_Title
        except AttributeError as e:
            theTitle = None

        if candidate.theFirstCallerClassName in wx.TopLevelClasses:

            if candidate.ts_AssignedId in topLevelSiblings:

                fmt = 'SetTopLevelSiblings (duplicated): ' \
                    'assignedId="%d"; title="%s".'
                msg = fmt % (candidate.ts_AssignedId, theTitle)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            else:

                tsWxGTUI_DataBase.WindowsByShowOrder[
                    'OrderOfShow'] += [
                        candidate.ts_AssignedId]

                fmt = 'SetTopLevelSiblings (added): ' \
                    'assignedId="%d"; title="%s".'
                self.logger.debug(fmt % (candidate.ts_AssignedId,
                                         theTitle))

        else:

            fmt = 'SetTopLevelSiblings (rejected): ' \
                'assignedId="%d"; title="%s".'
            msg = fmt % (candidate.ts_AssignedId, theTitle)
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        topLevelSiblings = tsWxGTUI_DataBase.WindowsByShowOrder['OrderOfShow']
        self.logger.notice(
            'End SetTopLevelSiblings: %s.' % topLevelSiblings)

    #-----------------------------------------------------------------------

    def SetValidator(self, validator):
        '''
        Deletes the current validator (if any) and sets the window validator,
        having called wx.Validator.Clone to create a new validator of this
        type.
        '''
        if True:
            msg = 'NotImplementedError: %s' % 'SetValidator in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:
            self.ts_Validator = validator

    #-----------------------------------------------------------------------

    def SetVirtualSize(self, size):
        '''
        Sets the virtual size of the window in pixels.
        '''
        self.ts_VirtualSize = self.tsGetClassInstanceFromTuple(size, wxSize)

    #-----------------------------------------------------------------------

    def SetVirtualSizeHints(self, minW, minH, maxW=-1, maxH=-1):
        '''
        Allows specification of minimum and maximum virtual window sizes.
        If a pair of values is not set (or set to -1), the default values
        will be used. If this function is called, the user will not be able
        to size the virtual area of the window outside the given bounds.
        '''
        msg = 'NotImplementedError: %s' % 'SetVirtualSizeHints in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetVirtualSizeHintsSz(self, minSize, maxSize=wx.DefaultSize):
        '''
        Allows specification of minimum and maximum virtual window sizes.
        If a pair of values is not set (or set to -1), the default values
        will be used. If this function is called, the user will not be able
        to size the virtual area of the window outside the given bounds.
        '''
        msg = 'NotImplementedError: %s' % 'SetVirtualSizeHintsSz in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetVirtualSizeWH(self, w, h):
        '''
        Set the the virtual size of a window in pixels. For most windows
        this is just the client area of the window, but for some like
        scrolled windows it is more or less independent of the screen
        window size.
        '''
        msg = 'NotImplementedError: %s' % 'SetVirtualSizeWH in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetWindowStyle(self, style):
        '''
        See SetWindowStyleFlag() for more info.

        Reimplemented in wxTreeCtrl.
        '''
        msg = 'NotImplementedError: %s' % 'SetWindowStyle in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetWindowStyleFlag(self, style):
        '''
        Sets the style of the window.

        Please note that some styles cannot be changed after the window
        creation and that Refresh() might need to be called after changing
        the others for the change to take place immediately.

        See Window styles for more information about flags.

        See also:
        GetWindowStyleFlag()

        Reimplemented in wxAuiToolBar, and wxListCtrl.
        '''
        msg = 'NotImplementedError: %s' % 'SetWindowStyleFlag in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def SetWindowVariant(self, variant):
        '''
        This function can be called under all platforms but only does
        anything under Mac OS X 10.3+ currently.

        Under this system, each of the standard control can exist in
        several sizes which correspond to the elements of wxWindowVariant
        enum.

        By default the controls use the normal size, of course, but this
        function can be used to change this.

        Variant values are:

        wx.WINDOW_VARIANT_NORMAL        Normal size

        wx.WINDOW_VARIANT_SMALL         Smaller size (about 25 % smaller
                                        than normal)

        wx.WINDOW_VARIANT_MINI          Mini size (about 33 % smaller than
                                        normal)

        wx.WINDOW_VARIANT_LARGE         Large size (about 25 % larger than
                                        normal)
        '''
        if (self.ts_WindowVariant != variant):

            self.ts_WindowVariant = variant

            self.DoSetWindowVariant(variant)

    #-----------------------------------------------------------------------

    def ShouldInheritColours(self):
        '''
        Return true from here to allow the colours of this window to be
        changed by InheritAttributes().

        Returning false forbids inheriting them from the parent window.

        The base class version returns false, but this method is
        overridden in wxControl where it returns true.
        '''
        msg = 'NotImplementedError: %s' % 'ShouldInheritColours in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Show(self, show=True):
        '''
        Shows or hides the window. You may need to call Raise for a top
        level window if you want to bring it to top, although this is not
        needed if Show is called immediately after the frame creation.
        Returns True if the window has been shown or hidden or False if
        nothing was done because it already was in the requested state.
        '''
##        # TBD - Implement this only when we are tracking activity.
##        if (show != self.ts_IsShown):

##            self.ts_IsShown = show

##            return (True)

##        else:

##            return (False)

        if self.tsIsShowPermitted and show:

            self.ts_Shown = False

            if DEBUG:

                self.logger.debug(
                    '  Started Show: %d (%s)' % (self.ts_AssignedId,
                                                 self.ts_Name))
                self.logger.debug(
                    '\n\n Children Show: %d (%s) %s\n' % (self.ts_AssignedId,
                                                          self.ts_Name,
                                                          self.Children))

            if self.ts_Handle is None:

                self.logger.debug(
                    '  Started Show (Create Handle): %d (%s)' % (
                        self.ts_AssignedId,
                        self.ts_Name))

                try:

                    self.ts_Sizer.Layout()

                except Exception as errorCode:

                    if False: # DEBUG:

                        # TBD - Disable until recursion error resolved.
                        msg = 'Window.Show: %s' % str(errorCode)
                        print('DEBUG: %s.\n' % msg)
                        self.logger.debug(msg)

                    pass

                self.tsShow()

                self.logger.debug(
                    'Completed Show (Create Handle): %d (%s)' % (
                        self.ts_AssignedId,
                        self.ts_Name))

            # TBD - Should curses level calls be here?
            if (self.ts_Handle is not None) and \
               (not self.ts_Shown):

                window = self.ts_Handle

                try:

                    window.redrawwin()

                except Exception as errorCode:

                    msg = 'window.redrawwin: %d (%s); errorCode=%s' % (
                        self.ts_AssignedId,
                        self.ts_Name,
                        str(errorCode))
                    self.logger.error(msg)
                    raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

                window.noutrefresh()

                for child in self.Children:

                    child.Show()

                if self.Parent == None:

                    self.tsCursesDoUpdate()

                if DEBUG:

                    self.logger.debug(
                        'Completed Show: %d (%s)' % (self.ts_AssignedId,
                                                     self.ts_Name))

                self.ts_Shown = True

        else:

            self.ts_Shown = False

            if DEBUG:

                self.logger.debug(
                    '  Skipped Show (Hide): %d (%s)' % (
                        self.ts_AssignedId,
                        self.ts_Name))

    #-----------------------------------------------------------------------

    def Thaw(self):
        '''
        Re-enables window updating after a previous call to Freeze().

        To really thaw the control, it must be called exactly the same
        number of times as Freeze().

        If the window has any children, they are recursively thawed too.
        '''
##        wxASSERT_MSG( m_freezeCount, "Thaw() without matching Freeze()" );

##        if ( !--m_freezeCount )
##        {
##            // recursively thaw all children:
##            for ( wxWindowList::iterator i = GetChildren().begin();
##                  i != GetChildren().end(); ++i )
##            {
##                wxWindow *child = *i;
##                if ( child->IsTopLevel() )
##                    continue;

##                child->Thaw();
##            }

##            // physically thaw this window:
##            DoThaw();
##        }

        self.ts_Freeze = False

        for child in self.ts_Children:
            child.Thaw()

    #-----------------------------------------------------------------------

    def ToggleWindowStyle(self, flag):
        '''
        Turns the given flag on if it is currently turned off and vice versa.

        This function cannot be used if the value of the flag is 0 (which
        is often the case for default flags).

        Also, please notice that not all styles can be changed after the
        control creation.

        Returns:
        Returns true if the style was turned on by this function, false if
        it was switched off.
        '''
        self.logger.wxASSERT_MSG(
            flag,
            'Window.ToggleWindowStyle: flags with 0 value cannot be toggled')

        style = self.GetWindowStyleFlag()
        if (style & flag):

            style &= ~flag
            rc = False

        else: # currently off

            style |= flag
            rc = True

        self.SetWindowStyleFlag(style)

        return (rc)

    #-----------------------------------------------------------------------

    def TransferDataFromWindow(self):
        '''
        Transfers values from child controls to data areas specified by their
        validators.

        Returns false if a transfer failed. If the window has
        wx.WS_EX_VALIDATE_RECURSIVELY extra style flag set, the method will
        also call TransferDataFromWindow() of all child windows.
        '''
        if True:
            msg = 'NotImplementedError: %s' % \
                'TransferDataFromWindow in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:

            if wx.USE_VALIDATORS:
                recurse = (self.GetExtraStyle() & \
                           (wx.WS_EX_VALIDATE_RECURSIVELY != 0))

                for child in self.ts_Children:

                    validator = child.GetValidator()
                    if (validator and \
                        (not validator.TransferFromWindow())):

                        # nop warning here because the application is
                        # supposed to give one itself - we don't know
                        # here what might have gone wrongly

                        return (False)

                    if (recurse):

                        if (not(child.TransferDataFromWindow())):

                            # warning already given
                            return (False)

            return (True)

    #-----------------------------------------------------------------------

    def TransferDataToWindow(self):
        '''
        Transfers values to child controls from data areas specified by their
        validators.

        If the window has wx.WS_EX_VALIDATE_RECURSIVELY extra
        style flag set, the method will also call TransferDataToWindow() of
        all child windows.
        '''
        if True:
            msg = 'NotImplementedError: %s' % \
                'TransferDataToWindow in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)
        else:
            if wx.USE_VALIDATORS:
                recurse = (self.GetExtraStyle() & \
                           wx.WS_EX_VALIDATE_RECURSIVELY != 0)

                for child in self.ts_Children:
                    validator = child.GetValidator()
                    if (validator is not None) and \
                       (not validator.TransferToWindow()):

                        self.logger.warning(
                            'Could not transfer data to window')

                        return (False)

                    if (recurse):

                        if (not child.TransferDataToWindow()):

                            # warning already given
                            return (False)

            return (True)

    #-----------------------------------------------------------------------

    def SetTransparent(self, alpha):
        '''
        Set the transparency of the window.

        If the system supports transparent windows, returns true, otherwise
        returns false and the window remains fully opaque. See also
        CanSetTransparent().

        The parameter alpha is in the range 0..255 where 0 corresponds to
        a fully transparent window and 255 to the fully opaque one. The
        constants wxIMAGE_ALPHA_TRANSPARENT and wxIMAGE_ALPHA_OPAQUE can
        be used.

        Reimplemented in wxTopLevelWindow.
        '''
        return (False)

    #-----------------------------------------------------------------------

    def UnregisterHotKey(self, hotkeyId):
        '''
        Unregisters a system wide hotkey.

        Parameters:
        hotkeyId        Numeric identifier of the hotkey. Must be the
        same id that was passed to RegisterHotKey().

        Returns:
        true if the hotkey was unregistered successfully, false if the
        id was invalid.

        Remarks:
        This function is currently only implemented under MSW.
        '''
        msg = 'NotImplementedError: %s' % 'UnregisterHotKey in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    @staticmethod
    def UnreserveControlId(id, count=1):
        '''
        Unreserve an ID or range of IDs that was reserved by NewControlId().

        See Window IDs for more information.

        Parameters:
        id      The starting ID of the range of IDs to unreserve.

        count   The number of sequential IDs to unreserve.


        Remarks:
        The Ncurses-based tsWx implementation creates new control Ids via
        a non-static method (See Object.tsNewId()). It currently does not
        support the reference count feature.
        '''
        msg = 'NotImplementedError: %s' % 'UnreserveControlId in tsWxWindow'
        # self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def UnsetToolTip(self):
        '''
        Unset any existing tooltip.
        '''
        msg = 'NotImplementedError: %s' % 'UnsetToolTip in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Update(self):
        '''
        Calling this method immediately repaints the invalidated area of
        the window and all of its children recursively (this normally
        only happens when the flow of control returns to the event loop).

        Notice that this function does not invalidate any area of the
        window so nothing happens if nothing has been invalidated
        (i.e. marked as requiring a redraw). Use Refresh() first if
        you want to immediately redraw the window unconditionally.
        '''
        msg = 'NotImplementedError: %s' % 'Update in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def UpdateWindowUI(self, flags=wx.UPDATE_UI_NONE):
        '''
        This function sends EVT_UPDATE_UI events to the window.

        The particular implementation depends on the window; for example
        a wx.ToolBar will send an update UI event for each toolbar button,
        and a wx.Frame will send an update UI event for each menubar menu
        item.

        You can call this function from your application to ensure that
        your UI is up-to-date at a particular point in time (as far as
        your EVT_UPDATE_UI handlers are concerned). This may be necessary
        if you have called wx.UpdateUIEvent.SetMode or
        wx.UpdateUIEvent.SetUpdateInterval to limit the overhead that
        wxWindows incurs by sending update UI events in idle time.
        The flags should be a bitlist of one or more of the following
        values:

        wx.UPDATE_UI_NONE       No particular value
        wx.UPDATE_UI_RECURSE    Call the function for descendants
        wx.UPDATE_UI_FROMIDLE   Invoked from OnIdle

        If you are calling this function from an OnInternalIdle or OnIdle
        function, make sure you pass the wxUPDATE_UI_FROMIDLE flag, since
        this tells the window to only update the UI elements that need to
        be updated in idle time. Some windows update their elements only
        when necessary, for example when a menu is about to be shown.
        The following is an example of how to call UpdateWindowUI from an
        idle function.

        void MyWindow::OnInternalIdle()
        {
            if (wxUpdateUIEvent::CanUpdate(this))
                UpdateWindowUI(wxUPDATE_UI_FROMIDLE);
        }
        '''
        event = Event(self.GetId())
        event.SetEventSource(self)

        if ( self.GetEventHandler().ProcessEvent(event) ):

            self.DoUpdateWindowUI(event)


        if (flags & wx.UPDATE_UI_RECURSE):

            for child in self.ts_Children:

                child.UpdateWindowUI(flags)

    #-----------------------------------------------------------------------

    def UseBgCol(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'UseBgCol in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Validate(self):
        '''
        Validates the current values of the child controls using their
        validators.

        If the window has wx.WS_EX_VALIDATE_RECURSIVELY extra
        style flag set, the method will also call Validate() of all child
        windows.

        Returns:
        Returns false if any of the validations failed.
        '''
        msg = 'NotImplementedError: %s' % 'Validate in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def WarpPointer(self, x, y):
        '''
        Moves the pointer to the given position on the window.

        NOTE:
        Apple Human Interface Guidelines forbid moving the mouse cursor
        programmatically so you should avoid using this function in Mac
        applications (and probably avoid using it under the other platforms
        without good reason as well).

        Parameters:
        x       The new x position for the cursor.

        y       The new y position for the cursor.
        '''
        msg = 'NotImplementedError: %s' % 'WarpPointer in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def wxGetMetricOrDefault(self, what, win):
        '''
        helper of GetWindowBorderSize(): as many ports do not implement
        support for wxSYS_BORDER/EDGE_X/Y metrics in their wxSystemSettings,
        use hard coded fallbacks in this case
        '''
        rc = self.ts_SystemSettings.GetMetric(what, win)
        if ( rc == -1 ):

            if ((what == self.ts_SystemSettings.wxSYS_BORDER_X) or \
                (what == self.ts_SystemSettings.wxSYS_BORDER_Y)):

                # 2D border is by default 1 character width/height
                rc = 1

            elif ((what == self.ts_SystemSettings.wxSYS_EDGE_X) or \
                  (what == self.ts_SystemSettings.wxSYS_EDGE_Y)):

                # 3D borders are by default 1 character width/height
                rc = 1

            else:

                self.logger.wxFAIL_MSG(
                    'Unexpected wxGetMetricOrDefault() argument')
                rc = 0

        return (rc)

    #-----------------------------------------------------------------------

    def wxHasRealChildren(self, win):
        '''
        On Mac, host scrollbars are explicitly children.
        '''
        realChildCount = 0

        return (realChildCount > 0)

    #----------------------------------------------------------------------
    # Begin tsWx API Extensions

    def tsBuildCursesNewWindowGenealogy(self):
        '''
        Gather genealogy information about the creator of a new curses window.
        '''
        parentClass = self.Parent # self.theFirstCallerClassName.Parent
        if parentClass is None:
            if DEBUG:
                if self.theFirstCallerClassName in wx.TopLevelClasses:
                    msg = 'tsRegisterClassWindow: %s <- 1st %s in %s' % \
                        (self.ts_ClassName,
                         self.theFirstCallerClassName,
                         str(wx.TopLevelClasses))
                    self.logger.warning(msg)
                else:
                    msg = 'tsRegisterClassWindow: %s <- 1st %s NOT in %s' % \
                        (self.ts_ClassName,
                         self.theFirstCallerClassName,
                         str(wx.TopLevelClasses))
                    self.logger.error(msg)
                    raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            parentName = None
            parentLabel = None
            # Needed for mouse event lookups in tsWxPyApp
            parentWindowIndex = None
        else:
            parentName = parentClass.Name
            parentLabel = parentClass.GetLabel()
            # Needed for mouse event lookups in tsWxPyApp
            parentWindowIndex = parentClass.ts_WindowIndex

        if self.ts_ClassName != self.theFirstCallerClassName:
            # TBD - Restore the chronological registration caused by
            # delaying tsBeginClassRegistration until a class
            # (such as Frame) had initialized each of its
            # ancestorial base classes (ending with Object).

            if DEBUG:
                self.logger.debug(
                    '\n\ntsRegisterClassWindow ' + \
                    'restored theFirstCallerClassName ' + \
                    '(%s <- %s).\n' % \
                    (self.ts_ClassName, self.theFirstCallerClassName))

            self.ts_ClassName = self.theFirstCallerClassName

        handleSelf = self

        handleDict = {}

        try:
            handleDict['AcceleratorTable'] = handleSelf.ts_AcceleratorTable
        except AttributeError:
            pass
        except Exception as e:
            handleDict['AcceleratorTable'] = 'N/A because %s' % str(e)

        try:
            handleDict['AcceptFiles'] = handleSelf.ts_AcceptFiles
        except AttributeError:
            pass
        except Exception as e:
            handleDict['AcceptFiles'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['assignedId'] = handleSelf.ts_AssignedId
##            except Exception, e:
##                handleDict['assignedId'] = 'N/A because %s' % str(e)

        try:
            handleDict['AssignedId'] = handleSelf.ts_AssignedId
        except AttributeError:
            pass
        except Exception as e:
            handleDict['AssignedId'] = 'N/A because %s' % str(e)

        try:
            handleDict['AutoLayout'] = handleSelf.ts_AutoLayout
        except AttributeError:
            pass
        except Exception as e:
            handleDict['AutoLayout'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['backgroundColour'] = handleSelf.BackgroundColour
##            except Exception, e:
##                handleDict['backgroundColour'] = 'N/A because %s' % str(e)

        try:
            handleDict['BackgroundColour'] = handleSelf.ts_BackgroundColour
        except AttributeError:
            pass
        except Exception as e:
            handleDict['BackgroundColour'] = 'N/A because %s' % str(e)

        try:
            handleDict['BackgroundStyle'] = handleSelf.ts_BackgroundStyle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['BackgroundStyle'] = 'N/A because %s' % str(e)

        try:
            handleDict['BestSize'] = handleSelf.ts_BestSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['BestSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['BestVirtualSize'] = handleSelf.ts_BestVirtualSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['BestVirtualSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['Border'] = handleSelf.ts_Border
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Border'] = 'N/A because %s' % str(e)

        try:
            handleDict['ButtonText'] = handleSelf.ts_ButtonText
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ButtonText'] = 'N/A because %s' % str(e)

        try:
            handleDict['CacheBestSize'] = handleSelf.ts_CacheBestSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['CacheBestSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['CaptureMouse'] = handleSelf.ts_CaptureMouse
        except AttributeError:
            pass
        except Exception as e:
            handleDict['CaptureMouse'] = 'N/A because %s' % str(e)

        try:
            handleDict['Caret'] = handleSelf.ts_Caret
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Caret'] = 'N/A because %s' % str(e)

        try:
            handleDict['CharHeight'] = handleSelf.ts_CharHeight
        except AttributeError:
            pass
        except Exception as e:
            handleDict['CharHeight'] = 'N/A because %s' % str(e)

        try:
            handleDict['CharWidth'] = handleSelf.ts_CharWidth
        except AttributeError:
            pass
        except Exception as e:
            handleDict['CharWidth'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['children'] = handleSelf.ts_Children
##            except Exception, e:
##                handleDict['children'] = 'N/A because %s' % str(e)

        try:
            handleDict['Children'] = handleSelf.ts_Children
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Children'] = 'N/A because %s' % str(e)

        try:
            handleDict['class'] = handleSelf
        except AttributeError:
            pass
        except Exception as e:
            handleDict['class'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['className'] = handleSelf.ts_ClassName
##            except Exception, e:
##                handleDict['className'] = 'N/A because %s' % str(e)

        try:
            handleDict['ClassName'] = handleSelf.ts_ClassName
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ClassName'] = 'N/A because %s' % str(e)

        try:
            handleDict['ClientAreaOrigin'] = handleSelf.ts_ClientAreaOrigin
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ClientAreaOrigin'] = 'N/A because %s' % str(e)

        try:
            handleDict['ClientRect'] = handleSelf.ts_ClientRect
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ClientRect'] = 'N/A because %s' % str(e)

        try:
            handleDict['ClientSize'] = handleSelf.ts_ClientSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ClientSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['Constraints'] = handleSelf.ts_Constraints
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Constraints'] = 'N/A because %s' % str(e)

        try:
            handleDict['ContainingSizer'] = handleSelf.ts_ContainingSizer
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ContainingSizer'] = 'N/A because %s' % str(e)

        try:
            handleDict['Cursor'] = handleSelf.ts_Cursor
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Cursor'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'DefaultAttributes'] = handleSelf.ts_DefaultAttributes
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'DefaultAttributes'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'DescendantOrderOfShow'] = handleSelf.ts_DescendantOrderOfShow
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'DescendantOrderOfShow'] = 'N/A because %s' % str(e)

        try:
            handleDict['DoubledBuffered'] = handleSelf.ts_DoubledBuffered
        except AttributeError:
            pass
        except Exception as e:
            handleDict['DoubledBuffered'] = 'N/A because %s' % str(e)

        try:
            handleDict['DropTarget'] = handleSelf.ts_DropTarget
        except AttributeError:
            pass
        except Exception as e:
            handleDict['DropTarget'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['earliestAncestor'] = handleSelf.ts_EarliestAncestor
##            except Exception, e:
##                handleDict['earliestAncestor'] = 'N/A because %s' % str(e)

        try:
            handleDict['EarliestAncestor'] = handleSelf.ts_EarliestAncestor
        except AttributeError:
            pass
        except Exception as e:
            handleDict['EarliestAncestor'] = 'N/A because %s' % str(e)

        try:
            handleDict['EffectiveMinSize'] = handleSelf.ts_EffectiveMinSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['EffectiveMinSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['Enabled'] = handleSelf.ts_Enabled
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Enabled'] = 'N/A because %s' % str(e)

        try:
            handleDict['EventHandle'] = handleSelf.ts_EventHandle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['EventHandle'] = 'N/A because %s' % str(e)

        try:
            handleDict['ExtraStyle'] = handleSelf.ts_ExtraStyle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ExtraStyle'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['focusEnabled'] = handleSelf.ts_FocusEnabled
##            except Exception, e:
##                handleDict['focusEnabled'] = 'N/A because %s' % str(e)

        try:
            handleDict['FocusEnabled'] = handleSelf.ts_FocusEnabled
        except AttributeError:
            pass
        except Exception as e:
            handleDict['FocusEnabled'] = 'N/A because %s' % str(e)

        try:
            handleDict['FocusFromKbd'] = handleSelf.ts_FocusFromKbd
        except AttributeError:
            pass
        except Exception as e:
            handleDict['FocusFromKbd'] = 'N/A because %s' % str(e)

        try:
            handleDict['Font'] = handleSelf.ts_Font
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Font'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['foregroundColour'] = handleSelf.ForegroundColour
##            except Exception, e:
##                handleDict['foregroundColour'] = 'N/A because %s' % str(e)

        try:
            handleDict['ForegroundColour'] = handleSelf.ts_ForegroundColour
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ForegroundColour'] = 'N/A because %s' % str(e)

##            try:
##                handleDict[
##                    'FrameAcceleratorTable'] = \
##                    handleSelf.ts_FrameAcceleratorTable
##            except AttributeError:
##                pass
##            except Exception, e:
##                handleDict['FrameAcceleratorTable'] = 'N/A because %s' % str(e)

        try:
            handleDict['Freeze'] = handleSelf.ts_Freeze
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Freeze'] = 'N/A because %s' % str(e)

        try:
            handleDict['GrandParent'] = handleSelf.ts_Parent.ts_Parent
            if (handleSelf.ts_Parent.ts_Parent is None) and \
               (handleSelf.ts_Parent.ts_ClassName in wx.TopLevelClasses):
                handleDict['GrandParent'] = '%s (stdscr)' % \
                    handleSelf.ts_Parent.ts_Parent
        except AttributeError:
            pass
        except Exception as e:
            handleDict['GrandParent'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentAssignedId'] = \
                handleSelf.ts_Parent.ts_Parent.ts_AssignedId
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentAssignedId'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentHandle'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Handle
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentHandle'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentName'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Name
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentName'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentLabel'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Label
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentLabel'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentTitle'] = \
                handleSelf.ts_Parent.ts_Parent.ts_Title
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentTitle'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'GrandParentWindowIndex'] = \
                handleSelf.ts_Parent.ts_Parent.ts_WindowIndex
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'GrandParentWindowIndex'] = 'N/A because %s' % str(e)

        try:
            handleDict['GtkWidget'] = handleSelf.ts_GtkWidget
        except AttributeError:
            pass
        except Exception as e:
            handleDict['GtkWidget'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['handle'] = handleSelf.ts_Handle
##            except Exception, e:
##                handleDict['handle'] = 'N/A because %s' % str(e)

        try:
            handleDict['Handle'] = handleSelf.ts_Handle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Handle'] = 'N/A because %s' % str(e)

        try:
            handleDict['HasFocus'] = handleSelf.ts_HasFocus
        except AttributeError:
            pass
        except Exception as e:
            handleDict['HasFocus'] = 'N/A because %s' % str(e)

        try:
            handleDict['HelpText'] = handleSelf.ts_HelpText
        except AttributeError:
            pass
        except Exception as e:
            handleDict['HelpText'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['id'] = handleSelf.ts_Id
##            except Exception, e:
##                handleDict['id'] = 'N/A because %s' % str(e)

        try:
            handleDict['Id'] = handleSelf.ts_Id
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Id'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['label'] = handleSelf.GetLabel()
##            except Exception, e:
##                handleDict['label'] = 'N/A because %s' % str(e)

        try:
            handleDict['Label'] = handleSelf.ts_Label
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Label'] = 'N/A because %s' % str(e)

        try:
            handleDict['LayoutDirection'] = handleSelf.ts_LayoutDirection
        except AttributeError:
            pass
        except Exception as e:
            handleDict['LayoutDirection'] = 'N/A because %s' % str(e)

        try:
            handleDict['MaxHeight'] = handleSelf.ts_MaxHeight
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MaxHeight'] = 'N/A because %s' % str(e)

        try:
            handleDict['MaxSize'] = handleSelf.ts_MaxSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MaxSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['MaxWidth'] = handleSelf.ts_MaxWidth
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MaxWidth'] = 'N/A because %s' % str(e)

        try:
            handleDict['membershipFlag'] = handleSelf.ts_MembershipFlag
        except AttributeError:
            pass
        except Exception as e:
            handleDict['membershipFlag'] = 'N/A because %s' % str(e)

        try:
            handleDict['MinHeight'] = handleSelf.ts_MinHeight
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MinHeight'] = 'N/A because %s' % str(e)

        try:
            handleDict['MinSize'] = handleSelf.ts_MinSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MinSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['MinWidth'] = handleSelf.ts_MinWidth
        except AttributeError:
            pass
        except Exception as e:
            handleDict['MinWidth'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['name'] = handleSelf.ts_Name
##            except Exception, e:
##                handleDict['name'] = 'N/A because %s' % str(e)

        try:
            handleDict['name'] = handleSelf.ts_Name
        except AttributeError:
            pass
        except Exception as e:
            handleDict['name'] = 'N/A because %s' % str(e)

        try:
            handleDict['PanelLayer'] = handleSelf.ts_PanelLayer
        except AttributeError:
            pass
        except Exception as e:
            handleDict['PanelLayer'] = 'N/A because %s' % str(e)

        try:
            handleDict['Parent'] = handleSelf.ts_Parent
            if (handleSelf.ts_Parent is None) and \
               (handleSelf.ts_ClassName in wx.TopLevelClasses):
                handleDict['Parent'] = '%s (stdscr)' % handleSelf.ts_Parent
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Parent'] = 'N/A because %s' % str(e)

        try:
            handleDict['ParentAssignedId'] = \
                handleSelf.ts_Parent.ts_AssignedId
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ParentAssignedId'] = 'N/A because %s' % str(e)

        try:
            handleDict['parentClass'] = parentClass
        except AttributeError:
            pass
        except Exception as e:
            handleDict['parentClass'] = 'N/A because %s' % str(e)

        try:
            handleDict['ParentHandle'] = handleSelf.ts_Parent.ts_Handle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ParentHandle'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['parentName'] = parentName
##            except Exception, e:
##                handleDict['parentName'] = 'N/A because %s' % str(e)

        try:
            handleDict['ParentName'] = handleSelf.ts_Parent.ts_Name
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ParentName'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['parentLabel'] = parentLabel
##            except Exception, e:
##                handleDict['parentLabel'] = 'N/A because %s' % str(e)

        try:
            handleDict['ParentLabel'] = handleSelf.ts_Parent.ts_Label
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ParentLabel'] = 'N/A because %s' % str(e)

        try:
            handleDict['ParentTitle'] = handleSelf.ts_Parent.ts_Title
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ParentTitle'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['parentWindowIndex'] = parentWindowIndex
##            except Exception, e:
##                handleDict['parentWindowIndex'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'ParentWindowIndex'] = \
                handleSelf.ts_Parent.ts_WindowIndex
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'ParentWindowIndex'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['rect'] = handleSelf.Rect
##            except Exception, e:
##                handleDict['rect'] = 'N/A because %s' % str(e)

        try:
            handleDict['Rect'] = handleSelf.ts_Rect
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Rect'] = 'N/A because %s' % str(e)

        try:
            handleDict['RefreshWindowAndChildren'
                       ] = handleSelf.ts_RefreshWindowAndChildren
        except AttributeError:
            pass
        except Exception as e:
            handleDict['RefreshWindowAndChildren'
                       ] = 'N/A because %s' % str(e)

        try:
            handleDict['RefreshOnlyThisRect'
                       ] = handleSelf.ts_RefreshOnlyThisRect
        except AttributeError:
            pass
        except Exception as e:
            handleDict['RefreshOnlyThisRect'
                       ] = 'N/A because %s' % str(e)

        try:
            handleDict['RefreshEraseBackground'
                       ] = handleSelf.ts_RefreshEraseBackground
        except AttributeError:
            pass
        except Exception as e:
            handleDict['RefreshEraseBackground'
                       ] = 'N/A because %s' % str(e)

        try:
            handleDict['ScreenPosition'] = handleSelf.ts_ScreenPosition
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ScreenPosition'] = 'N/A because %s' % str(e)

        try:
            handleDict['Shown'] = handleSelf.ts_Shown
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Shown'] = 'N/A because %s' % str(e)

        try:
            handleDict['Size'] = handleSelf.ts_Size
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Size'] = 'N/A because %s' % str(e)

        try:
            handleDict['Sizer'] = handleSelf.ts_Sizer
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Sizer'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['style'] = handleSelf.ts_Style
##            except Exception, e:
##                handleDict['style'] = 'N/A because %s' % str(e)

        try:
            handleDict['Style'] = handleSelf.ts_Style
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Style'] = 'N/A because %s' % str(e)

        try:
            handleDict['SystemEventTable'] = handleSelf.ts_SystemEventTable
        except AttributeError:
            pass
        except Exception as e:
            handleDict['SystemEventTable'] = 'N/A because %s' % str(e)

        try:
            handleDict[
                'theFirstCallerClassName'] = \
                handleSelf.theFirstCallerClassName
        except AttributeError:
            pass
        except Exception as e:
            handleDict[
                'theFirstCallerClassName'] = 'N/A because %s' % str(e)

        try:
            handleDict['Text'] = handleSelf.ts_Text
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Text'] = 'N/A because %s' % str(e)

        try:
            handleDict['theEntry'] = handleSelf.ts_theEntry
        except AttributeError:
            pass
        except Exception as e:
            handleDict['theEntry'] = 'N/A because %s' % str(e)

        try:
            handleDict['ThemeEnabled'] = handleSelf.ts_ThemeEnablede
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ThemeEnabled'] = 'N/A because %s' % str(e)

        try:
            handleDict['thisown'] = handleSelf.thisown
        except AttributeError:
            pass
        except Exception as e:
            handleDict['thisown'] = 'N/A because %s' % str(e)

        try:
            handleDict['Title'] = handleSelf.ts_Title
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Title'] = 'N/A because %s' % str(e)

        try:
            handleDict['ToolTip'] = handleSelf.ts_ToolTip
        except AttributeError:
            pass
        except Exception as e:
            handleDict['ToolTip'] = 'N/A because %s' % str(e)

        try:
            handleDict['TopLevel'] = handleSelf.ts_TopLevel
        except AttributeError:
            pass
        except Exception as e:
            handleDict['TopLevel'] = 'N/A because %s' % str(e)

        try:
            handleDict['TopLevelParent'] = handleSelf.ts_TopLevelParent
        except AttributeError:
            pass
        except Exception as e:
            handleDict['TopLevelParent'] = 'N/A because %s' % str(e)

        try:
            handleDict['UpdateClientRect'] = handleSelf.ts_UpdateClientRect
        except AttributeError:
            pass
        except Exception as e:
            handleDict['UpdateClientRect'] = 'N/A because %s' % str(e)

        try:
            handleDict['UpdateRegion'] = handleSelf.ts_UpdateRegion
        except AttributeError:
            pass
        except Exception as e:
            handleDict['UpdateRegion'] = 'N/A because %s' % str(e)

        try:
            handleDict['UserEventTable'] = handleSelf.ts_UserEventTable
        except AttributeError:
            pass
        except Exception as e:
            handleDict['UserEventTable'] = 'N/A because %s' % str(e)

        try:
            handleDict['Validator'] = handleSelf.ts_Validator
        except AttributeError:
            pass
        except Exception as e:
            handleDict['Validator'] = 'N/A because %s' % str(e)

        try:
            handleDict['VirtualSize'] = handleSelf.ts_VirtualSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['VirtualSize'] = 'N/A because %s' % str(e)

        try:
            handleDict['VirtualSize'] = handleSelf.ts_VirtualSize
        except AttributeError:
            pass
        except Exception as e:
            handleDict['VirtualSize'] = 'N/A because %s' % str(e)

##            try:
##                handleDict['windowIndex'] = handleSelf.ts_WindowIndex
##            except Exception, e:
##                handleDict['windowIndex'] = 'N/A because %s' % str(e)

        try:
            handleDict['WindowIndex'] = handleSelf.ts_WindowIndex
        except AttributeError:
            pass
        except Exception as e:
            handleDict['WindowIndex'] = 'N/A because %s' % str(e)

        try:
            handleDict['WindowStyle'] = handleSelf.ts_WindowStyle
        except AttributeError:
            pass
        except Exception as e:
            handleDict['WindowStyle'] = 'N/A because %s' % str(e)

        try:
            handleDict['WindowStyleFlag'] = handleSelf.ts_WindowStyleFlag
        except AttributeError:
            pass
        except Exception as e:
            handleDict['WindowStyleFlag'] = 'N/A because %s' % str(e)

        try:
            handleDict['WindowVariant'] = handleSelf.ts_WindowVariant
        except AttributeError:
            pass
        except Exception as e:
            handleDict['WindowVariant'] = 'N/A because %s' % str(e)

##            # Cannot include theWindows
##            try:
##                handleDict['theWindows'] = str(handleSelf.ts_theWindows)
##            except Exception, e:
##                handleDict['theWindows'] = 'N/A because %s' % str(e)

        return (handleDict)

    #-----------------------------------------------------------------------

    def tsCreateBorder(self):
        '''
        Create the pixel pattern that fills the outermost horizontal,
        vertical and corner areas of the window.

        Note - Use distinctive patterns that are platform independent.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            if self.tsIsBorderStyle(style=self.ts_Style):

                if self.ts_Style & wx.BORDER_DOUBLE:
                    xx = ord('=')
                    self.tsCursesBorder(xx, xx, xx, xx, xx, xx, xx, xx)

                elif self.ts_Style & wx.BORDER_RAISED:
                    xx = ord('*') # curses.ACS_BLOCK
                    self.tsCursesBorder(xx, xx, xx, xx, xx, xx, xx, xx)

                elif self.ts_Style & wx.BORDER_SUNKEN:
                    xx = ord(' ') # ord('x') # curses.ACS_LANTERN
                    self.tsCursesBorder(xx, xx, xx, xx, xx, xx, xx, xx)

                elif self.ts_Style & wx.BORDER_THEME:
                    xx = ord('#') # curses.ACS_DIAMOND
                    self.tsCursesBorder(xx, xx, xx, xx, xx, xx, xx, xx)

                elif self.ts_Style & wx.BORDER_STATIC:
                    xx = ord('+') # curses.ACS_CKBOARD
                    self.tsCursesBorder(xx, xx, xx, xx, xx, xx, xx, xx)

                else:
                    self.tsCursesBox()

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateButton(self):
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
                    self.tsCreateButtonLine(text)
                else:
                    self.tsCreateButtonMultiLine(text)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateButtonLine(self, theLabel):
        '''
        Create single line button.
        '''
        self.logger.debug(
            'tsCreateButtonLine: theLabel="%s"; rect=%s' % (
                theLabel, str(self.Rect)))

        if theLabel == wx.EmptyString:
            pass

        else:
            characterCellAttribute = tsGTUI.DISPLAY_STANDOUT
            characterCellAccelerator = tsGTUI.DISPLAY_UNDERLINE
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

    #-----------------------------------------------------------------------

    def tsCreateButtonMultiLine(self, text):
        '''
        Create multi-line button.
        '''
        # TBD - Under Construction. Should surround text with border.
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

    def tsCreateLabel(self):
        '''
        Create single or multi-line label.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            text = self.GetLabel()
            if text != wx.EmptyString:
                if text.find('\n') == -1:
                    self.tsCreateLabelLine(text)
                else:
                    self.tsCreateLabelMultiLine(text)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateLabelLine(self, text):
        '''
        Create single line label.
        '''
        window = self.ts_Handle

        aLine = text
        borderThickness = self.tsIsBorderThickness(
            style=self.ts_Style, pixels=True)

        if text == wx.EmptyString:
            col = 0 + borderThickness.width // wx.pixelWidthPerCharacter
            row = 0 + borderThickness.height // wx.pixelHeightPerCharacter
        else:
            col = 1
            row = 0

        attr = curses.A_BOLD
        if aLine != wx.EmptyString:
            window.attron(attr)
            if self.tsIsBorderStyle(style=self.ts_Style):
                # Adjust for indent, border and space on left and right sides.
                maxCols = min(len(aLine) + len('  '),
                              (self.Rect.width - (
                                  4 * borderThickness.width) \
                               // wx.pixelWidthPerCharacter)) - col
                window.addstr(int(row), int(col), ' %s ' % aLine[0:maxCols])
##                self.ts_Handle.addstr(0, 1, ' %s ' % aLine[0:5])
            else:
                # Adjust for indent on left and right sides.
                maxCols = min(len(aLine),
                              (self.Rect.width - (
                                  2 * borderThickness.width) \
                               // wx.pixelWidthPerCharacter)) - col
                window.addstr(int(row), int(col), '%s' % aLine[0:maxCols])
            window.attroff(attr)

    #-----------------------------------------------------------------------

    def tsCreateLabelMultiLine(self, text):
        '''
        Create multi-line label.
        '''
        window = self.ts_Handle

        # TBD - Under Construction.
        expandTabs = True
        replaceWhitespace = True
        initialIndent = ''
        subsequentIndent = ''
        fixSentenceEndings = False
        breakLongWords = True

        if self.tsIsBorderStyle(style=self.ts_Style):
            maxCol = (self.Rect.width // wx.pixelWidthPerCharacter) - 1
            maxRow = (self.Rect.height // wx.pixelHeightPerCharacter) - 1
        else:
            maxCol = self.Rect.width // wx.pixelWidthPerCharacter
            maxRow = self.Rect.height // wx.pixelHeightPerCharacter

        theWrapper = TextWrapper(
            width = maxCol - len(subsequentIndent),
            expand_tabs = expandTabs,
            replace_whitespace = replaceWhitespace,
            initial_indent = initialIndent,
            subsequent_indent = subsequentIndent,
            fix_sentence_endings = fixSentenceEndings,
            break_long_words = breakLongWords)

        theLabel = text

        theLines = theWrapper.wrap(theLabel)

        if self.tsIsBorderStyle(style=self.ts_Style):
            if len(theLines) == 1:
                # Label is used as title
                col = self.tsIsBorderThickness(style=self.ts_Style,
                                               pixels=False)
                row = 0
            else:
                # Text is not used as a title
                col = self.tsIsBorderThickness(style=self.ts_Style,
                                               pixels=False)
                row = self.tsIsBorderThickness(style=self.ts_Style,
                                               pixels=False)
        else:
            # Text is not used as a title
            col = 0
            row = 0

        for aLine in theLines:
            if row < maxRow:
                # TBD - Verify the constraints against wxPython.
                if self.tsIsBorderStyle(style=self.ts_Style):
                    window.addstr(
                        int(row), int(col), ' %s ' % aLine[0:min(len(aLine),
                                                                 maxCol - 1)])
                else:
                    window.addstr(
                        int(row), int(col), '%s' % aLine[0:min(len(aLine),
                                                               maxCol - 1)])
            row += 1

    #-----------------------------------------------------------------------

    def tsCreateMenuBar(self):
        '''
        Create the pixel pattern that fills the outermost horizontal,
        vertical and corner areas of the window.

        Note - Use distinctive patterns that are platform independent.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:

##            self.tsCursesScrollOk(0)
##            self.tsCursesBkgd(' ', attr=None)

            if self.tsIsBorderStyle(style=self.ts_Style):
                # TBD - Should the format control be added to theme? No.
                if True:
                    # Use horizontal lines to separate menu
                    # from title and client areas.
                    ls = ord(' ')
                    rs = ls
                    ts = curses.ACS_HLINE
                    bs = ts
                    tl = ts
                    tr = ts
                    bl = bs
                    br = bs
                else:
                    # Use horizontal and vertical lines to separate menu
                    # from title and client areas.
                    ls = curses.ACS_VLINE
                    rs = ls
                    ts = curses.ACS_HLINE
                    bs = ts
                    tl = curses.ACS_ULCORNER
                    tr = curses.ACS_URCORNER
                    bl = curses.ACS_LLCORNER
                    br = curses.ACS_LRCORNER
                self.tsCursesBorder(ls, rs, ts, bs, tl, tr, bl, br)

            self.tsCreateLabel()

    #-----------------------------------------------------------------------

    def tsCreateScrollBarButton(self):
        '''
        Create single or multi-line buttons.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            text = self.GetLabel()
            if text != wx.EmptyString:
                if text.find('\n') == -1:
                    self.tsCreateScrollBarButtonLine(text)
                else:
                    self.tsCreateScrollBarButtonMultiLine(text)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateScrollBarButtonLine(self, theLabel):
        '''
        Create single line button.
        '''
        self.logger.debug(
            'tsCreateScrollBarButtonLine: theLabel=%s; rect=%s' % (
                str(theLabel), str(self.Rect)))

        if theLabel == wx.EmptyString:
            pass

        else:
            characterCellAttribute = tsGTUI.DISPLAY_STANDOUT
            characterCellAccelerator = tsGTUI.DISPLAY_UNDERLINE
            window = self.ts_Handle

            (prefix,
             character,
             suffix,
             flags) = self.tsParseAcceleratorTextLabel(theLabel)

            aLine = prefix + character + suffix

##            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
##                                                       pixels=True)

            if wx.ThemeToUse['ScrollBar']['ArrowBorder']:

                borderThickness = wxSize(1, 1)

            else:

                borderThickness = wxSize(0, 0)

            col = 0 + borderThickness.width
            row = 0 + borderThickness.height

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

    #-----------------------------------------------------------------------

    def tsCreateScrollBarButtonMultiLine(self, text):
        '''
        Create multi-line button.
        '''
        # TBD - Under Construction. Should surround text with border.
        msg = 'NotImplementedError: %s' % \
            'tsCreateScrollBarButtonMultiLine in tsWxWindow'
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

    def tsCreateStatusLabel(self):
        '''
        Create single or multi-line Status Label.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            text = self.GetLabel()
            if text != wx.EmptyString:
                if text.find('\n') == -1:
                    self.tsCreateStatusLabelLine(text)
                else:
                    self.tsCreateStatusLabelMultiLine(text)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsCreateStatusLabelLine(self, text):
        '''
        Create single line Status Label.
        '''
        theLabel = text
        theMargin = wx.tsGetClassInstanceFromTuple(
            wx.ThemeToUse['StatusBar']['Margin'], wxSize)

        col = theMargin.width // wx.pixelWidthPerCharacter
        row = theMargin.height // wx.pixelHeightPerCharacter
        spaceAvailable = (
            self.Rect.width // \
            wx.pixelWidthPerCharacter) - col - 1

        theLabelLength = min(len(theLabel), spaceAvailable)

        if wx.ThemeToUse['StatusBar']['Ellipses']:
            ellipses = '...'
            ellipsesLength = len(ellipses)
            if theLabelLength < spaceAvailable:
                fillLength = spaceAvailable - theLabelLength
                filledText = '%s%s' % (theLabel, ' ' * fillLength)
            else:
                filledText = '%s%s' % (
                    theLabel[0:spaceAvailable - ellipsesLength],
                    ellipses)
        else:
            filledText = theLabel[0:spaceAvailable]

        self.tsCursesAddStr(
            int(col), int(row), filledText, attr=None, pixels=False)

    #-----------------------------------------------------------------------

    def tsCreateStatusLabelMultiLine(self, text):
        '''
        Create multi-line Status Label.
        '''
        theLabel = text
        theMargin = wx.tsGetClassInstanceFromTuple(
            wx.ThemeToUse['StatusBar']['Margin'], wxSize)

        col = theMargin.width // wx.pixelWidthPerCharacter
        row = theMargin.height // wx.pixelHeightPerCharacter
        spaceAvailable = (
            self.Rect.width // \
            wx.pixelWidthPerCharacter) - col - 1

        # TBD - Under Construction.
        expandTabs = True
        replaceWhitespace = True
        initialIndent = ''
        subsequentIndent = ''
        fixSentenceEndings = False
        breakLongWords = True

        if self.tsIsBorderStyle(style=self.ts_Style):
            maxCol = (self.Rect.width // wx.pixelWidthPerCharacter) - 1
            maxRow = (self.Rect.height // wx.pixelHeightPerCharacter) - 1
        else:
            maxCol = self.Rect.width // wx.pixelWidthPerCharacter
            maxRow = self.Rect.height // wx.pixelHeightPerCharacter

        theWrapper = TextWrapper(
            width = maxCol - len(subsequentIndent),
            expand_tabs = expandTabs,
            replace_whitespace = replaceWhitespace,
            initial_indent = initialIndent,
            subsequent_indent = subsequentIndent,
            fix_sentence_endings = fixSentenceEndings,
            break_long_words = breakLongWords)

        theLines = theWrapper.wrap(text)

        for aLine in theLines:
            theLabel = aLine
            theLabelLength = min(len(theLabel), spaceAvailable)

            if wx.ThemeToUse['StatusBar']['Ellipses']:
                ellipses = '...'
                ellipsesLength = len(ellipses)
                if theLabelLength < spaceAvailable:
                    fillLength = spaceAvailable - theLabelLength
                    filledText = '%s%s' % (theLabel, ' ' * fillLength)
                else:
                    filledText = '%s%s' % (
                        theLabel[0:spaceAvailable - ellipsesLength],
                        ellipses)
            else:
                filledText = theLabel[0:spaceAvailable]

            if row < maxRow:

                self.tsCursesAddStr(
                    int(col), int(row), filledText, attr=None, pixels=False)

            row += 1

    #-----------------------------------------------------------------------

    def tsCreateTitleLine(self, text):
        '''
        Create single line Title.
        '''
        window = self.ts_Handle
        if window is None:
            status = False
        else:
            aLine = text
            borderThickness = self.tsIsBorderThickness(style=self.ts_Style,
                                                       pixels=True)
            col = 1
            row = 0

            attr = curses.A_BOLD
            if aLine != wx.EmptyString:
                window.attron(attr)
                if self.tsIsBorderStyle(style=self.ts_Style):
                    # Adjust for indent, border and space on left
                    # and right sides.
                    maxCols = min(len(aLine),
                                  (self.Rect.width - \
                                   4 * borderThickness.width // \
                                   wx.pixelWidthPerCharacter))
                    window.addstr(int(row),
                                  int(col), ' %s ' % aLine[0:maxCols])
                else:
                    # Adjust for indent on left and right sides.
                    maxCols = min(len(aLine),
                                  (self.Rect.width - \
                                   2 * borderThickness.width // \
                                   wx.pixelWidthPerCharacter))
                    window.addstr(int(row), int(col), '%s' % aLine[0:maxCols])
                window.attroff(attr)

            status = True

        return (status)

    #-----------------------------------------------------------------------

    def tsFindWindowByAssignedId(self, winid):
        '''
        Find a child of this window by window ID.
        '''
        try:
            win = tsWxGTUI_DataBase.WindowsByAssignedId[winid]
        except Exception as findError:
            win = None
            self.logger.debug(
                'tsFindWindowByAssignedId KeyError: %d' % winid)

        return (win)

    #-----------------------------------------------------------------------

    def tsGetCharacterRectangle(self,
                                pixelCols,
                                pixelRows,
                                pixelWidth,
                                pixelHeight):
        '''
        Convert pixel measurments (position and size) to their
        equivalent character ones.
        '''
        (characterX, characterY) = self.tsGetCharacterValues(
            pixelCols, pixelRows)

        (characterWidth, characterHeight) = self.tsGetCharacterValues(
            pixelWidth, pixelHeight)

        return (wxRect(characterX,
                       characterY,
                       characterWidth,
                       characterHeight))

    #-----------------------------------------------------------------------

    def tsGetCharacterSize(self, pixelCols, pixelRows):
        '''
        Convert from pixel to character dimensions.
        '''
        if pixelCols == wx.UseDefaultValue:
            characterCols = pixelCols
        else:
            # Round up to the next whole character
            characterCols = int(float(
                pixelCols + (wx.pixelWidthPerCharacter - 1)) / float(
                    wx.pixelWidthPerCharacter))

        if pixelRows == wx.UseDefaultValue:
            characterRows = pixelRows
        else:
            # Round up to the next whole character
            characterRows = int(float(
                pixelRows + (wx.pixelHeightPerCharacter - 1)) / float(
                    wx.pixelHeightPerCharacter))

        return (wxSize(characterCols, characterRows))

    #-----------------------------------------------------------------------

    def tsGetCharacterValues(self, pixelCols, pixelRows):
        '''
        Convert pixel measurments (size or position) to their
        equivalent character ones.
        '''
        if pixelRows == wx.UseDefaultValue:
            characterRows = pixelRows
        else:
            # Round up to the next whole character
            characterRows = int(float(
                pixelRows + (wx.pixelHeightPerCharacter - 1)) / float(
                    wx.pixelHeightPerCharacter))

        if pixelCols == wx.UseDefaultValue:
            characterCols = pixelCols
        else:
            # Round up to the next whole character
            characterCols = int(float(
                pixelCols + (wx.pixelWidthPerCharacter - 1)) / float(
                    wx.pixelWidthPerCharacter))

        return (characterCols, characterRows)

    #-----------------------------------------------------------------------

    def tsGetClassInstanceFromTuple(self, theTuple, theClass):
        '''
        Generate the specified class instance from the specified tuple.
        '''
        if isinstance(theTuple, tuple):
            args = []
            for item in theTuple:
                args.append(item)
            theInstance = theClass(*args)
        else:
            theInstance = theTuple

        return (theInstance)

    #-----------------------------------------------------------------------

    def tsGetParentCharacterRectangleData(self,
                                          pos=wx.DefaultPosition,
                                          size=wx.DefaultSize):
        '''
        '''
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        return (wxRect(thePosition.x,
                       thePosition.y,
                       theSize.width,
                       theSize.height))

    #-----------------------------------------------------------------------

    def tsGetParentPosition(self, parent):
        '''
        Get the beginning coordinates of the parent window.
        '''
        if self.Parent is None:
            theDisplay = self.display # wx.Display()
            theClientArea = theDisplay.ClientArea
        else:
            # TBD - Tailor for Frames
            theClientArea = self.Parent.Rect

##        try:
##            (begin_y_parent, begin_x_parent) = parent.Handle.getbegyx()
##        except AttributeError:
##            (begin_y_parent, begin_x_parent) = self.stdscr.stdscr.getbegyx()

        return (wxPoint(theClientArea.x, theClientArea.y))

    #-----------------------------------------------------------------------

    def tsGetParentSize(self, parent):
        '''
        Get the width and height dimensions of the parent window.
        '''
        if self.Parent is None:
            theDisplay = self.display # wx.Display()
            theClientArea = theDisplay.ClientArea
        else:
            # TBD - Tailor for Frames
            theClientArea = self.Parent.Rect


##        try:
##            (maxParentRows, maxParentCols) = parent.Handle.getmaxyx()
##        except AttributeError:
##            (maxParentRows, maxParentCols) = self.stdscr.stdscr.getmaxyx()

        return (wxSize(theClientArea.width, theClientArea.height))

    #-----------------------------------------------------------------------

    def tsGetPixelSize(self, characterCols, characterRows):
        '''
        Convert from character to pixel dimensions.
        '''
        if characterCols == wx.UseDefaultValue:
            pixelCols = characterCols
        else:
            pixelCols = int(characterCols * wx.pixelWidthPerCharacter)

        if characterRows == wx.UseDefaultValue:
            # Use default when a value is wx.UseDefaultValue.
            pixelRows = characterRows
        else:
            pixelRows = int(characterRows * wx.pixelHeightPerCharacter)

        return (wxSize(pixelCols, pixelRows))

    #-----------------------------------------------------------------------

    def tsGetPixelValues(self, characterCols, characterRows):
        '''
        Convert character measurments (size or position) to their
        equivalent pixel ones.
        '''
        if characterRows == wx.UseDefaultValue:
            pixelRows = characterRows
        else:
            pixelRows = int(characterRows * wx.pixelHeightPerCharacter)

        if characterCols == wx.UseDefaultValue:
            pixelCols = characterCols
        else:
            pixelCols = int(characterCols * wx.pixelWidthPerCharacter)

        return (pixelCols, pixelRows)

    #-----------------------------------------------------------------------

    def tsGetRectangle(self, pos=wx.DefaultPosition, size=wx.DefaultSize):
        '''
        Return wx.Rect object from wx.Point and wx.Size objects.
        '''
        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)

        return (wxRect(thePosition.x,
                       thePosition.y,
                       theSize.width,
                       theSize.height))

    #-----------------------------------------------------------------------

    def tsGetTheId(self):
        '''
        Return the ID associated with this class instance.
        '''
        return id(self)

    #-----------------------------------------------------------------------

    def tsInternalOnSize(self):
        '''
        '''
        msg = 'Window.tsInternalOnSize: EVT_SIZE not handled.'
        print('DEBUG: %s.\n' % msg)

    #-----------------------------------------------------------------------

    def tsIsBorderStyle(self, style=wx.BORDER_NONE):
        '''
        Return True if window has a border; else return False.
        '''
        # BORDER             = 0x02000000
        # BORDER_DOUBLE      = 0x10000000
        # BORDER_MASK        = 0x1F200000
        # BORDER_NONE        = 0x00200000
        # BORDER_RAISED      = 0x04000000
        # BORDER_SIMPLE      = 0x02000000
        # BORDER_STATIC      = 0x01000000
        # BORDER_SUNKEN      = 0x08000000
        # BORDER_THEME       = 0x10000000
        if (style & wx.BORDER_MASK) == 0:
            return (False)
        else:
            return (True)

    #-----------------------------------------------------------------------

    def tsIsBorderThickness(self, style=wx.BORDER_NONE, pixels=True):
        '''
        Return size of window border in pixel or character thickness units.
        '''
        if not self.tsIsBorderStyle(style=style):
            # No border required.
            thickness = wxSize(0, 0)

        elif pixels:
            # Standard border required in pixel units.
            thickness = wxSize(wx.pixelWidthPerCharacter,
                               wx.pixelHeightPerCharacter)
        else:
            # Standard border required in character units.
            thickness = wxSize(1, 1)

        return (thickness)

    #-----------------------------------------------------------------------

    def tsIsShowPermitted(self):
        '''
        Return False if the earliest ancestor of this window has been
        permanently CLOSED or temporarily ICONIZED. Else, return True.

        This facilitates the imposition of a permanent CLOSE or temporary
        ICONIZE override to the permission for showing of a window, ita
        children and its ancestors.
        '''
        theEarliestAncestor = self.tsFindWindowByAssignedId(
            self.ts_EarliestAncestor)

        if (theEarliestAncestor.Closed or \
            theEarliestAncestor.Iconized):

            isShowPermitted = False

        else:

            isShowPermitted = True

        return (isShowPermitted)

    #-----------------------------------------------------------------------

    def tsOnHelp(self, evt):
        '''
        '''
        objectCriteria = 'Window.tsOnHelp: EVT_HELP not handled.'
        objectId = self.ts_AssignedId

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxWindow.tsOnHelp: ' + \
            'objectId is None.')

        precedenceSequence = [True, False]
        for precedence in precedenceSequence:

            self.tsProcessSelectedEventTable(
                objectCriteria=evt.EventCriteria,
                objectId=evt.EventSource.ts_AssignedId,
                triggeringEvent=evt,
                triggeringObject=evt.EventSource,
                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

    def tsOnInitDialog(self, evt):
        '''
        '''
        objectCriteria = 'Window.tsOnInitDialog: EVT_INIT_DIALOG not handled.'
        objectId = self.ts_AssignedId

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxWindow.tsOnInitDialog: ' + \
            'objectId is None.')

        precedenceSequence = [True, False]
        for precedence in precedenceSequence:

            self.tsProcessSelectedEventTable(
                objectCriteria=evt.EventCriteria,
                objectId=evt.EventSource.ts_AssignedId,
                triggeringEvent=evt,
                triggeringObject=evt.EventSource,
                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

    def tsOnMiddleDown(self, evt):
        '''
        '''
        objectCriteria = 'Window.tsOnMiddleDown: EVT_MIDDLE_DOWN not handled.'
        objectId = self.ts_AssignedId

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxWindow.tsOnMiddleDown: ' + \
            'objectId is None.')

        precedenceSequence = [True, False]
        for precedence in precedenceSequence:

            self.tsProcessSelectedEventTable(
                objectCriteria=evt.EventCriteria,
                objectId=evt.EventSource.ts_AssignedId,
                triggeringEvent=evt,
                triggeringObject=evt.EventSource,
                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

    def tsOnSysColourChanged(self, evt):
        '''
        '''
        objectCriteria = 'Window.tsOnSysColourChanged: ' + \
            'EVT_SYS_COLOUR_CHANGED not handled.'
        objectId = self.ts_AssignedId

        self.logger.wxASSERT_MSG(
            (not (objectId is None)),
            msg='tsWxWindow.tsOnSysColourChanged: ' + \
            'objectId is None.')

        precedenceSequence = [True, False]
        for precedence in precedenceSequence:

            self.tsProcessSelectedEventTable(
                objectCriteria=evt.EventCriteria,
                objectId=evt.EventSource.ts_AssignedId,
                triggeringEvent=evt,
                triggeringObject=evt.EventSource,
                useSystemEventTable=precedence)

    #-----------------------------------------------------------------------

    def tsParseAcceleratorTextLabel(self, text):
        '''
        Parse label text for prefix string, hot key character, suffix and
        flag strings. Where "&"  precedes the Hot-key character and "\t"
        prefixes the "Alt-" / "Ctrl-" / "Shift-" accelerator markup.

        Example: text = "S&ample\tCtrl-a" should produce:
        prefix = "S"
        hot key character = "a"
        suffix = "mple"
        accelerator = "Ctrl-a"
        '''
        myParts = text.split('\t')
        offset = 0
        if len(myParts) == 1:
            prefix = text
            character = ''
            suffix = ''
            accelerator = ''
        else:
            labelParts = myParts[0].split('&')
            prefix = labelParts[0]
            character = labelParts[1][0:1]
            suffix = labelParts[1][1:len(labelParts[1]) - offset]
            accelerator = myParts[1]

        return (prefix, character, suffix, accelerator)

    #-----------------------------------------------------------------------

    def tsRegisterClassWindow(self):
        '''
        Capture window information needed for debugging.
        '''
        if self.ts_Name == wx.ScreenNameStr:

            expectedHandle = self.display.TheTerminalScreen

            self.logger.wxASSERT_MSG(
                (self.ts_Handle == expectedHandle),
                msg='tsWxWindow.tsRegisterClassWindow (Screen): ' + \
                'self.ts_Handle != %s.' % str(expectedHandle))

        else:

            expectedHandle = None

            self.logger.wxASSERT_MSG(
                (not (self.ts_Handle is expectedHandle)),
                msg='tsWxWindow.tsRegisterClassWindow: ' + \
                'self.ts_Handle != %s.' % str(expectedHandle))

        #-------------------------------------------------------------------

        try:

            earliestAncestor = tsWxGTUI_DataBase.WindowsByAssignedId[
                self.ts_EarliestAncestor]

            if (not (self.ts_AssignedId in \
                     earliestAncestor.ts_DescendantOrderOfShow)):

                earliestAncestor.ts_DescendantOrderOfShow.append(
                    self.ts_AssignedId)

            fmt1 = 'tsWxWindow.tsRegisterClassWindow: '
            fmt2 = 'self.ts_AssignedId=%s \n' % self.ts_AssignedId
            fmt3 = 'earliestAncestor=%s \n' % \
                earliestAncestor
            fmt4 = 'DescendantOrderOfShow=%s \n' % \
                str(earliestAncestor.ts_DescendantOrderOfShow)
            msg = fmt1 + fmt2 + fmt3 + fmt4
            print('DEBUG: %s' % msg)

##              tsWxGTUI_DataBase.WindowsByAssignedId[
##                  self.ts_EarliestAncestor.ts_AssignedId][
##                  'DescendantOrderOfShow'
##                  ] = self.ts_EarliestAncestor.ts_DescendantOrderOfShow

        except AttributeError:

            pass

        except Exception as errorCode:

            msg = 'tsWxWindow.tsRegisterClassWindow: ' + \
                'errorCode=%s' % str(errorCode)
            self.logger.warning(msg)
            # raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        #-------------------------------------------------------------------

        if self.ts_Name == wx.ScreenNameStr:

            if True:

                # Create a curses panel layer for curses "sdscr" so that
                # the panel mechanism will include new output during
                # panel type updates.
                self.ts_Handle = self.display.TheTerminalScreen
                self.ts_PanelLayer = self.TheTerminal.tsGetCursesNewPanel(
                    self.ts_Handle)

            else:

                # Do not create a curses panel layer for sdscr. 
                self.ts_PanelLayer = None

            msg = 'tsRegisterClassWindow: thePanel=%s' % self.ts_PanelLayer
            self.logger.debug(msg)

            dataBase = tsWxGTUI_DataBase

            if not (self.ts_PanelLayer is None):

                cursesPanels = dataBase.CursesPanels
                thePanelId = len(cursesPanels) - 1 + 10000
                cursesPanels[thePanelId] = {
                    'assignedId': self.ts_AssignedId,
                    'earliestAncestor': self.ts_EarliestAncestor,
                    'handle': self.ts_Handle,
                    'label': self.GetLabel(),
                    'name': 'panel-%d' % thePanelId,
                    'panel': self.ts_PanelLayer
                    }

                # Begin Register wxPython object by curses panel.
                tsWxGTUI_DataBase.WindowsByCursesPanel[
                    self.ts_PanelLayer] = {
                        'wxPythonWindowInstance': self,
                        'wxPythonWindowAssignedId': self.ts_AssignedId,
                        'wxPythonWindowName': self.ts_Name,
                        'name': 'panel-%d' % thePanelId
                        }
                # End Register wxPython object by curses panel.

                # Added 20150125
                # Begin Register wxPython object by curses panel layer.
##                self.ts_WindowAssignedIdByCursesPanelLayer[
##                    self.ts_PanelLayer] = self.ts_AssignedId
                tsWxGTUI_DataBase.WindowAssignedIdByCursesPanelLayer[
                    self.ts_PanelLayer] = self.ts_AssignedId
                # End Register wxPython object by curses panel layer.

        else:

            self.ts_PanelLayer = self.TheTerminal.tsGetCursesNewPanel(
                self.ts_Handle)

            msg = 'tsRegisterClassWindow: thePanel=%s' % self.ts_PanelLayer
            self.logger.debug(msg)

            dataBase = tsWxGTUI_DataBase

            cursesPanels = dataBase.CursesPanels
            thePanelId = len(cursesPanels) - 1 + 10000
            cursesPanels[thePanelId] = {
                'assignedId': self.ts_AssignedId,
                'earliestAncestor': self.ts_EarliestAncestor,
                'handle': self.ts_Handle,
                'label': self.GetLabel(),
                'name': 'panel-%d' % thePanelId,
                'panel': self.ts_PanelLayer
            }

            # Begin Register wxPython object by curses panel.
            tsWxGTUI_DataBase.WindowsByCursesPanel[
                self.ts_PanelLayer] = {
                    'wxPythonWindowInstance': self,
                    'wxPythonWindowAssignedId': self.ts_AssignedId,
                    'wxPythonWindowName': self.ts_Name,
                    'name': 'panel-%d' % thePanelId
                    }
                                       
            # End Register wxPython object by curses panel.

        tsWxGTUI_DataBase.WindowsByAssignedId[
            self.ts_AssignedId] = self

        tsWxGTUI_DataBase.WindowsByHandle[
            self.ts_Handle] = self

        tsWxGTUI_DataBase.WindowsById[
            self.caller_id] = self

        tsWxGTUI_DataBase.WindowsByName[
            self.caller_name] = self

        tsWxGTUI_DataBase.WindowHandles[
            self.ts_AssignedId] = self.ts_Handle

##        tsWxGTUI_DataBase.WindowsByPad[
##            self.ts_Pad] = self

        tsWxGTUI_DataBase.WindowsByPanelLayer[
            self.ts_PanelLayer] = self

        # Added 20150125
        # Begin Register wxPython object by curses panel layer.
##      self.ts_WindowAssignedIdByCursesPanelLayer[
##          self.ts_PanelLayer] = self.ts_AssignedId
        tsWxGTUI_DataBase.WindowAssignedIdByCursesPanelLayer[
            self.ts_PanelLayer] = self.ts_AssignedId
        # End Register wxPython object by curses panel layer.

        if DEBUG and VERBOSE:
            self.logger.debug(
                '\n\n WindowsByAssignedId: %s' % \
                str(tsWxGTUI_DataBase.WindowsByAssignedId))
            self.logger.debug(
                '\n\n         WindowsById: %s' % \
                str(tsWxGTUI_DataBase.WindowsById))
            self.logger.debug(
                '\n\n       WindowsByName: %s' % \
                str(tsWxGTUI_DataBase.WindowsByName))
            self.logger.debug(
                '\n\n WindowHandles: %s' % \
                str(tsWxGTUI_DataBase.WindowHandles))

        self.ts_WindowIndex = tsWxGTUI_DataBase.TheWindows[
            'windowIndex']

        self.ts_theWindows = tsWxGTUI_DataBase.TheWindows

        if self.ts_WindowIndex is None:
            self.ts_WindowIndex = 0
        else:
            self.ts_WindowIndex += 1
        tsWxGTUI_DataBase.TheWindows[
            'windowIndex'] = self.ts_WindowIndex

        xx = self.tsBuildCursesNewWindowGenealogy()

        if tsWxGTUI_DataBase.TheWindows is None:
            tsWxGTUI_DataBase.TheWindows = {}
        tsWxGTUI_DataBase.TheWindows[self.ts_WindowIndex] = xx

        if DEBUG and VERBOSE:
            self.logger.debug(
                '\n\n\t %s\n' % \
                tsWxGTUI_DataBase.TheWindows[
                    self.ts_WindowIndex])

        # TBD - Should user supplied IDs be checked for uniqueness?
##        self.windowID[id] = wx.TheWindows[self.ts_WindowIndex]

        if DEBUG and VERBOSE:
            self.logger.debug(
                '\n\nClassname: %s; MembershipFlag: %s.\n' % \
                (self.ClassName,  self.ts_MembershipFlag))

            self.logger.debug(
                '\n\nCursesDataBase: %s\n' % \
                tsWxGTUI_DataBase.CursesDataBase)

    #----------------------------------------------------------------------

    def tsRegisterKeyboardInputOrder(self):
        '''
        Register caller windows in KeyboardInput order list.
        '''

        if not (self in Window.TheKeyboardInputRecipients):

            Window.TheKeyboardInputRecipients.insert(0, self)

            self.logger.debug(
                'tsRegisterKeyboardInputOrder by %s; %s' % (
                    self,
                    str(Window.TheKeyboardInputRecipients)))

            tsWxGTUI_DataBase.KeyboardInputRecipients[
                'lifoList'] = Window.TheKeyboardInputRecipients

    #----------------------------------------------------------------------

    def tsRegisterShowOrder(self):
        '''
        Register caller windows in show order list.
        '''

        if self.ts_PanelLayer not in \
           tsWxGTUI_DataBase.WindowsByShowOrder[
               'PanelLayer']:

            tsWxGTUI_DataBase.WindowsByShowOrder[
                'PanelLayer'] += [self.ts_PanelLayer]

        if self.ts_PanelLayer not in \
           tsWxGTUI_DataBase.WindowsByShowOrder[
               'AssignedIdByPanelLayer']:

            tsWxGTUI_DataBase.WindowsByShowOrder[
                'AssignedIdByPanelLayer'][
                    self.ts_PanelLayer] = self.ts_AssignedId

        #------------------------------------------------------------------

        if self.ts_AssignedId not in \
           tsWxGTUI_DataBase.WindowsByShowOrder[
               'OrderOfShow']:

            tsWxGTUI_DataBase.WindowsByShowOrder[
                'OrderOfShow'] += [self.ts_AssignedId]

        if self.ts_AssignedId not in \
           tsWxGTUI_DataBase.WindowsByShowOrder[
               'OrderOfShowPanelStack']:

            tsWxGTUI_DataBase.WindowsByShowOrder[
                'OrderOfShowPanelStack'] += [self.ts_AssignedId]

        #------------------------------------------------------------------

        self.logger.debug(
            'tsRegisterShowOrder by %s; %s' % (
                self,
                str(tsWxGTUI_DataBase.WindowsByShowOrder)))

    #----------------------------------------------------------------------

    def tsResetShowOrder(self):
        '''
        Erase all previously registered windows from show order list.
        '''
        tsWxGTUI_DataBase.WindowsByShowOrder = {}

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'name'] = 'WindowsByShowOrder'

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'PanelStack'] = {}

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'PanelStack'][
                'name'] = 'PanelStack'

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'OrderOfShow'] = []

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'OrderOfShowPanelStack'] = []

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'PanelLayer'] = []

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'AssignedIdByPanelLayer'] = {}

        tsWxGTUI_DataBase.WindowsByShowOrder[
            'AssignedIdByPanelLayer'][
                'name'] = 'AssignedIdByPanelLayer'

        self.logger.debug('tsResetShowOrder by %s' % self)

    #-----------------------------------------------------------------------

##    def tsRoundHorizontal(self, value):
##        '''
##        Return the horizontal position aligned to the nearest text column.
##        '''
##        roundHorizontal = wx.pixelWidthPerCharacter // 2
##        remainder = value % roundHorizontal
##        if not (wx.ThemeToUse['CharacterCellAlignment']):

##            return (value)

##        elif remainder < roundHorizontal:

##            return (value - remainder)

##        else:

##            return (value - remainder + roundHorizontal)

    #-----------------------------------------------------------------------

    def tsRoundHorizontal(self, value, nSplits=1):
        '''
        Return the horizontal position aligned to the nearest text column.
        '''
        splitValue = value // nSplits
        roundHorizontal = wx.pixelWidthPerCharacter // 2
        remainder = splitValue % roundHorizontal
        if not (wx.ThemeToUse['CharacterCellAlignment']):

            return (splitValue)

        elif remainder < roundHorizontal:

            return (splitValue - remainder)

        else:

            return (splitValue - remainder + roundHorizontal)

    #-----------------------------------------------------------------------

##    def tsRoundVertical(self, value):
##        '''
##        Return the vertical position aligned to the nearest text row.
##        '''
##        roundVertical = wx.pixelHeightPerCharacter // 2
##        remainder = value % roundVertical
##        if  not (wx.ThemeToUse['CharacterCellAlignment']):

##            return  (value)

##        elif remainder < roundVertical:

##            return (value - remainder)

##        else:

##            return (value - remainder + roundVertical)

    #-----------------------------------------------------------------------

    def tsRoundVertical(self, value, nSplits=1):
        '''
        Return the vertical position aligned to the nearest text row.
        '''
        splitValue = value // nSplits
        roundVertical = wx.pixelHeightPerCharacter // 2
        remainder = value % roundVertical
        if  not (wx.ThemeToUse['CharacterCellAlignment']):

            return  (splitValue)

        elif remainder < roundVertical:

            return (splitValue - remainder)

        else:

            return (splitValue - remainder + roundVertical)

    #-----------------------------------------------------------------------

##    def tsRoundXY(self, xValue, yValue):
##        '''
##        Return the horizontal (x) and vertical (y) values aligned to the
##        nearest text column and row position.
##        '''
##        return (self.tsRoundHorizontal(xValue),
##                self.tsRoundVertical(yValue))

    #-----------------------------------------------------------------------

    def tsRoundXY(self, xValue, yValue, xSplits=1, ySplits=1):
        '''
        Return the horizontal (x) and vertical (y) values aligned to the
        nearest text column and row position.
        '''
        return (self.tsRoundHorizontal(xValue, xSplits),
                self.tsRoundVertical(yValue, ySplits))

    #-----------------------------------------------------------------------

    def tsSetCharHeight(self, pixels):
        '''
        Sets the (average) character size for the current font.
        '''
        self.ts_CharHeight = pixels

    #-----------------------------------------------------------------------

    def tsSetCharWidth(self, pixels):
        '''
        Sets the (average) character size for the current font.
        '''
        self.ts_CharWidth = pixels

    #-----------------------------------------------------------------------

    def tsShow(self):
        '''
        Create and update non-class specific native GUI.
        '''
        if self.tsIsShowPermitted:

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
            except Exception as e:
                msg = '%s; %s' % (__title__, e)
                self.logger.error(msg)
                raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

            self.tsUpdate()

    #-----------------------------------------------------------------------

    def tsStripAcceleratorTextLabel(self, text):
        '''
        '''
        (prefix,
         character,
         suffix,
         flags) = self.tsParseAcceleratorTextLabel(text)

        return (prefix + character + suffix)

    #-----------------------------------------------------------------------

    def tsTaskBarDumpPanelStack(self):
        '''
        '''
        panelStack = []
        panelStackBottom = curses.panel.bottom_panel()
        panelStackTop = curses.panel.top_panel()
        panelStackLayer = panelStackBottom

        fmt1 = 'tsWxWindow.tsTaskBarDumpPanelStack: '
        fmt2 = 'panelStackBottom=%s' % panelStackBottom
        fmt3 = 'panelStackTop=%s' % panelStackTop
        fmt4 = 'panelStackLayer=%s' % panelStackLayer
        msg = '\n%s \n\t%s \n\t%s \n\t%s' % (fmt1, fmt2, fmt3, fmt4)
        self.logger.debug(msg)
        print('\n\%s' % msg)

        done = False
        while not done:
            try:
                theWindow = tsWxGTUI_DataBase.WindowsByPanelLayer[
                    panelStackLayer]
                msg = 'tsWxWindow.tsTaskBarDumpPanelStack: ' + \
                    'panelStackLayer=%s; Id=%s; Label=%s' % (
                        panelStackLayer,
                        theWindow.Id,
                        theWindow.GetLabel())
                self.logger.debug(msg)
                print('\n\%s' % msg)
                panelStack.append(panelStackLayer)
                if panelStackLayer == panelStackTop:
                    done = True
                else:
                    panelStackLayer = panelStackLayer.panel.above()
            except Exception as dumpErrorCode:
                msg = 'tsWxWindow.tsTaskBarDumpPanelStack: ' + \
                    'dumpErrorCode=%s' % dumpErrorCode
                self.logger.debug(msg)
                print('\n\%s' % msg)
                done = True

    #-----------------------------------------------------------------------

    def tsTaskBarTopTask(self, earliestAncestor):
        '''
        Show that focus has been shifted to the earliest ancestor of
        designated top task and its associated descendants.

        Beginning with the earliest ancestor, move the associated overlay
        layer(s) to the top of the stack. Update the display whether or not
        there were any moves.
        '''
        try:

            msg = 'tsWxWindow.tsTaskBarTopTask (entry): ' + \
                'earliestAncestor (AssignedId)=%s; (Label)="%s"' % (
                    str(earliestAncestor.ts_AssignedId),
                    str(earliestAncestor.GetLabel()))
            self.logger.debug(msg)

            if DEBUG:

                print('DEBUG: %s\n' % msg)

            if wx.USE_CURSES_PANEL_STACK:

                self.tsTaskBarDumpPanelStack()

                if DEBUG:

                    countMax = len(earliestAncestor.ts_DescendantOrderOfShow)
                    count = 0

                for assignedId in earliestAncestor.ts_DescendantOrderOfShow:

                    if assignedId == 265:

                        ### TBD - Fix non-working PanelLayer operations
                        print('<<< Focussing assignedId=%d >>>' % assignedId)

                        theWindow = self.tsFindWindowByAssignedId(
                            assignedId)

                        panelLayer = theWindow.ts_PanelLayer
                        panelLayer.top()
                        panelLayer.hide()

                        curses.panel.update_panels()
                        curses.doupdate()
##                        self.tsCursesPanelUpdatePanels()
##                        self.tsCursesDoUpdate()

                    else:

                        print('<<< Skipping assignedId=%d >>>' % assignedId)
                        continue

                    theWindow = self.tsFindWindowByAssignedId(
                        assignedId)

                    panelLayer = theWindow.ts_PanelLayer

                    if DEBUG:

                        count += 1
                        if count == 1:
                            status = 'movedTopTask'
                        else:
                            status = 'movedTopChild'

                        fmt1 = 'tsWxWindow.tsTaskBarTopTask (PanelStack): '
                        fmt2 = 'status=%s; ' % status
                        fmt3 = 'assignedId=%d; ' % assignedId
                        fmt4 = 'Label="%s"; ' % theWindow.GetLabel()
                        fmt5 = 'panelLayer=%s' % str(panelLayer)
                        msg = fmt1 + fmt2 + fmt3 + fmt4 + fmt5
                        self.logger.debug(msg)
                        print('DEBUG: %s\n' % msg)

                    panelLayer.top()

                self.tsCursesPanelUpdatePanels()
                self.tsCursesDoUpdate()

            else:

                for child in earliestAncestor.ts_Children:

                    try:

                        if not (child.ts_PanelLayer is None):

                            if DEBUG:

                                msg = 'tsWxWindow.tsTaskBarTopTask ' + \
                                    '(Non-PanelStack): ' + \
                                    'child=%s; panelLayer=%s' % (
                                        str(child),
                                        str(child.ts_PanelLayer))
                                self.logger.debug(msg)
                                print('DEBUG: %s\n' % msg)

                            self.tsTaskBarTopChild(child, earliestAncestor)

                    except AttributeError as errorCode:

                        msg = 'tsWxWindow.tsTaskBarTopTask: ' + \
                            'earliestAncestor=%s; errorCode=%s' % (
                                str(child),
                                str(earliestAncestor))
                        self.logger.error(msg)
                        print('ERROR: %s\n' % msg)

                earliestAncestor.Show()

            msg = 'tsWxWindow.tsTaskBarTopTask (exit): ' + \
                'earliestAncestor (AssignedId)=%s; (Label)="%s"' % (
                    str(earliestAncestor.ts_AssignedId),
                    str(earliestAncestor.GetLabel()))
            self.logger.debug(msg)

        except KeyError as errorCode:

            msg = 'tsWxWindow.tsTaskBarTopTask: ' + \
                'earliestAncestor=%s; errorCode=%s' % (
                    str(earliestAncestor),
                    str(errorCode))
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)

        except AttributeError as errorCode:

            msg = 'tsWxWindow.tsTaskBarTopTask: ' + \
                'earliestAncestor=%s; errorCode=%s' % (
                    str(earliestAncestor),
                    str(errorCode))
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            #raise errorCode

    #-----------------------------------------------------------------------

    def tsTaskBarTopChild(self, child, earliestAncestor):
        '''
        Show that focus has been shifted to the earliest ancestor of
        designated child task and its associated descendants.

        Beginning with the earliest ancestor, move the associated overlay
        layer(s) to the top of the stack. Update the display whether or not
        there were any moves.
        '''
        try:

            msg = 'tsWxWindow.tsTaskBarTopChild (entry): ' + \
                'child (AssignedId)=%s; (Label)="%s"' % (
                    str(child.ts_AssignedId), str(child.GetLabel()))

            self.logger.debug(msg)

            if DEBUG:

                print('DEBUG: %s\n' % msg)

            for grandChild in child.ts_Children:

                try:

                    if not (grandChild.ts_PanelLayer is None):

                        msg = 'tsWxWindow.tsTaskBarTopChild (entry)' + \
                            'grandChild=%s; panelLayer=%s' % (
                                str(grandChild),
                                str(grandChild.ts_PanelLayer))
                        self.logger.debug(msg)

                        if DEBUG:

                            print('DEBUG: %s\n' % msg)

                        self.tsTaskBarTopChild(grandChild,
                                               earliestAncestor)

                        msg = 'tsWxWindow.tsTaskBarTopChild (exit)' + \
                            'grandChild=%s; panelLayer=%s' % (
                                str(grandChild),
                                str(grandChild.ts_PanelLayer))
                        self.logger.debug(msg)

                except AttributeError as errorCode:

                    msg = 'tsWxWindow.tsTaskBarTopChild: ' + \
                        'grandChild=%s; errorCode=%s' % (
                            str(grandChild),
                            str(earliestAncestor))
                    self.logger.error(msg)
                    print('ERROR: %s\n' % msg)

            child.Show()

            msg = 'tsWxWindow.tsTaskBarTopChild (exit): ' + \
                'child (AssignedId)=%s; (Label)="%s"' % (
                    str(child.ts_AssignedId), str(child.GetLabel()))

            self.logger.debug(msg)

        except KeyError as errorCode:

            msg = 'tsWxWindow.tsTaskBarTopChild: ' + \
                'earliestAncestor=%s; errorCode=%s' % (
                    str(earliestAncestor),
                    str(errorCode))
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)

        except AttributeError as errorCode:

            msg = 'tsWxWindow.tsTaskBarTopChild: ' + \
                'Child=%s; errorCode=%s' % (
                    str(child),
                    str(errorCode))
            self.logger.error(msg)
            print('ERROR: %s\n' % msg)
            # raise errorCode

    #-----------------------------------------------------------------------

    def tsTrapIfTooSmall(self, name, myRect):
        '''
        '''
        # TBD - Under Construction.
        if True:
            return
        else:
            msg = 'NotImplementedError: %s' % 'tsTrapIfTooSmall in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        minScreenDimensions = wx.ThemeToUse['MinScreenDimensions']
        minScreenWidth = minScreenDimensions['FrameWidth']
        minScreenHeight = minScreenDimensions['FrameHeight'] + \
            minScreenDimensions['MenuBarHeight'] + \
            minScreenDimensions['ToolBarHeight'] + \
            minScreenDimensions['StatusBarHeight'] + \
            minScreenDimensions['RedirectionHeight'] + \
            minScreenDimensions['TaskBarHeight']

        minClientHeight = minScreenDimensions['FrameHeight'] + \
            minScreenDimensions['MenuBarHeight'] + \
            minScreenDimensions['ToolBarHeight'] + \
            minScreenDimensions['StatusBarHeight']

        minWidth = minScreenWidth

        if name == wx.TaskBarNameStr:
            minHeight = minScreenDimensions['TaskBarHeight']

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

        actualScreen = self.display.GetGeometry(pixels=True)

        actualScreenWidth = actualScreen.width
        actualScreenHeight = actualScreen.height
        actualScreenSize = wxSize(actualScreenWidth, actualScreenHeight)

        if actualScreenSize.width < minScreenSize.width:

            fmt = '  Screen "%s" width (%d) is too small.' + \
                ' Please make screen at least (%d) columns'
            abortMsg = fmt % (self.display.Name,
                              actualScreenSize.width,
                              minScreenSize.width)

            self.logger.error('    tsTrapIfTooSmall: %s' % abortMsg)

            raise tse.UserInterfaceException(
                tse.GRAPHICAL_WINDOW_NOT_VALID, abortMsg)

        if actualScreenSize.height < minScreenSize.height:

            fmt = '  Screen "%s" height (%d) is too small.' + \
                ' Please make screen at least (%d) lines'
            abortMsg = fmt % (self.display.Name,
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

    #----------------------------------------------------------------------

    def tsUnRegisterKeyboardInputOrder(self):
        '''
        Remove registered caller window from KeyboardInput order list.
        '''
        activeCaller = Window.TheKeyboardInputRecipients[0]
        caller = self
        fmt1 = 'Window.tsUnRegisterKeyboardInputOrder: '
        fmt2 = 'caller="%s" ' % caller
        fmt3 = 'Not activeCaller="%s".' % activeCaller
        msg = fmt1 + fmt2 + fmt3
        self.logger.wxASSERT_MSG(
            (not (caller == activeCaller),
             msg))

        Window.TheKeyboardInputRecipients.remove(0)

        self.logger.debug(
            'tsRegisterKeyboardInputOrder removed %s; %s' % (
                self,
                str(Window.TheKeyboardInputRecipients)))

        tsWxGTUI_DataBase.KeyboardInputRecipients[
            'lifoList'] = Window.TheKeyboardInputRecipients

    #-----------------------------------------------------------------------

    def tsUpdate(self):
        '''
        Placeholder for class specific method.
        '''
        if self.tsIsShowPermitted and True:

            msg = 'NotImplementedWarning: %s' % 'tsUpdate in tsWxWindow'
            self.logger.warning(msg)

        else:

            msg = 'NotImplementedError: %s' % 'tsUpdate in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def tsWindowLayout(self, parent, pos, size, style, name):
        '''
        Calculate position and size of frame based upon arguments.
        '''
        try:

            if (not (self.ts_Handle is None)):

                # Inhibit operation once self.ts_Handle has been
                # assigned a curses window identifier.
                return (self.ts_Rect, self.ts_ClientRect)

        except AttributeError:

            # TBD - Resolve why some Controls do not initialize via
            #       self.ts_Handle = None. Thoght I did that for:
            #       Button, CheckBox, Gauge, RadioBox, RadioButton,
            #       StaticText, TaskBarButton and TextCtrl.
            self.ts_Handle = None

        except Exception as errorCode:

            msg = 'tsWxWindow.tsWindowLayout: errorCode=%s' % errorCode
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        thePosition = self.tsGetClassInstanceFromTuple(pos, wxPoint)
        theSize = self.tsGetClassInstanceFromTuple(size, wxSize)
        theBorder = self.tsIsBorderThickness(style, pixels=True)

        theDefaultPosition = self.tsGetClassInstanceFromTuple(
            wx.DefaultPosition, wxPoint)

        theDefaultSize = self.tsGetClassInstanceFromTuple(
            wx.DefaultSize, wxSize)

        if name == wx.TaskBarNameStr:

            # Top level window frame reserved for the session's taskbar
            # input and output.
            try:

                myRect = self.TheDisplay.tsGetTaskArea(pixels=True)

            except AttributeError as errorCode:

                myRect = None

        elif name == wx.StdioNameStr:

            # Top level window frame reserved for the session's redirected
            # error, normal and print message output.
            try:

                myRect = self.TheDisplay.tsGetRedirectedStdioArea(pixels=True)

            except AttributeError as errorCode:

                myRect = None

        elif parent is None:

            # Top level window frame or dialog reserved for the session's
            # task input and output.
            try:

                myRect = self.TheDisplay.GetClientArea(pixels=True)

            except AttributeError as errorCode:

                myRect = None

        else:

            # Lower level window panel reserved for the session's
            # task input and output.
            if thePosition == theDefaultPosition and \
               theSize == theDefaultSize:

                myRect = parent.GetClientArea(pixels=True)

            elif thePosition == theDefaultPosition:

                myRect = wxRect(parent.ClientArea.x,
                                parent.ClientArea.y,
                                theSize.width,
                                theSize.height)

            elif theSize == theDefaultSize:

                theParentSize = wxSize(
                    parent.ClientArea.width,
                    parent.ClientArea.height)

                myRect = wxRect(
                    thePosition.x,
                    thePosition.y,
                    theParentSize.width - thePosition.x,
                    theParentSize.height - thePosition.y)

            else:

                try:
                    theParentRect = parent.GetClientArea()
                except Exception as errorCode:
                    theParentRect = parent.ts_Rect

                myRect = wxRect(thePosition.x,
                                thePosition.y,
                                theSize.width,
                                theSize.height)

                if not theParentRect.InsideRect(myRect):
                    myRect = wxRect(
                        max(thePosition.x, theParentRect.x),
                        max(thePosition.y, theParentRect.y),
                        min(theSize.width, theParentRect.width),
                        min(theSize.height, theParentRect.height - 1))

                if not theParentRect.InsideRect(myRect):
                    myRect = theParentRect

        myClientRect = wxRect(myRect.x + theBorder.width,
                              myRect.y + theBorder.height,
                              myRect.width - 2 * theBorder.width,
                              myRect.height - 2 * theBorder.height)

        self.tsTrapIfTooSmall(name, myRect)
        msg = 'parent=%s; pos=%s; size=%s; name=%s; myRect=%s' % \
            (parent, pos, size, name, myRect)

        self.logger.debug('    tsWindowLayout: %s' % msg)

        return (myRect, myClientRect)

    #-----------------------------------------------------------------------

    def UnsetConstraints(self, c):
        '''
        This removes any dangling pointers to this window in other window
        constraintsInvolvedIn lists.
        '''
        if (not (c is None)):

            if ( c.left.GetOtherWindow() and \
                 (c.top.GetOtherWindow() != self ) ):
                c.left.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.top.GetOtherWindow() and \
                 (c.top.GetOtherWindow() != self) ):
                c.top.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.right.GetOtherWindow() and \
                 (c.right.GetOtherWindow() != self) ):
                c.right.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.bottom.GetOtherWindow() and \
                 (c.bottom.GetOtherWindow() != self) ):
                c.bottom.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.width.GetOtherWindow() and \
                 (c.width.GetOtherWindow() != self) ):
                c.width.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.height.GetOtherWindow() and \
                 (c.height.GetOtherWindow() != self) ):
                c.height.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.centreX.GetOtherWindow() and \
                 (c.centreX.GetOtherWindow() != self) ):
                c.centreX.GetOtherWindow().RemoveConstraintReference(self)

            if ( c.centreY.GetOtherWindow() and \
                 (c.centreY.GetOtherWindow() != self) ):
                c.centreY.GetOtherWindow().RemoveConstraintReference(self)

    #-----------------------------------------------------------------------

    def WindowToClientSize(self, size):
        '''
        Converts window size size to corresponding client area size In other
        words, the returned value is what would GetClientSize() return if
        this window had given window size.
        '''
        # const wxSize diff(GetSize() - GetClientSize());

        # return wxSize(size.x == -1 ? -1 : size.x - diff.x,
        #               size.y == -1 ? -1 : size.y - diff.y);

        diff = self.GetSize() - self.GetClientSize()
        result = wxSize(0, 0)

        if (size.x == -1):
            result.x = -1
        else:
            result.x =  size.x - diff.x

        if (size.y == -1):
            result.y = -1
        else:
            result.y =  size.y - diff.y

        return (result)

    #----------------------------------------------------------------------

    def OnClose(self, evt):
        '''
        '''
##        if (not (self.ts_PanelLayer is None)):

        self.ts_BackgroundColour = 'Black'
        self.ts_ForegroundColour = 'Red'
        self.tsUpdate()
        self.Show()
        return

        try:

            msg = 'tsWindow.OnClose: Panel Layer for %s' % str(self)
            print(msg)
            if (not (self.ts_PanelLayer is None)):

                # TBD - Children do NOT close.
                for child in self.ts_Children:
                    child.OnClose(evt)

                self.ts_BackgroundColour = 'Black'
                self.ts_ForegroundColour = 'Red'
                self.tsUpdate()
                self.Show()

##                self.ts_Handle.clear()
##                self.ts_Handle.refresh()

##                self.ts_PanelLayer.Hide()
##                self.tsUpdate()
##                self.Show()

            else:

                msg = 'tsWindow.OnClose: No Panel Layer for %s' % str(self)
                print(msg)

        except Exception as errorCode:

            fmt1 = 'NotImplementedError: %s' % 'OnClose in tsWxWindow'
            fmt2 = 'errorCode=%s' % errorCode
            msg = fmt1 + fmt1
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #----------------------------------------------------------------------

    def OnHelp(self, evt):
        '''
        Show help for this window.
        '''
        msg = 'NotImplementedError: %s' % 'OnHelp in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #----------------------------------------------------------------------

    def OnInitDialog(self, evt):
        '''
        The default action is to populate dialog with data when it is
        created, and nudge the UI into displaying itself correctly
        in case we havee turned the wxUpdateUIEvents frequency
        down low.
        '''
        if True:
            msg = 'NotImplementedError: %s' % 'OnInitDialog in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        else:
            self.TransferDataToWindow()

            # Update the UI at this point
            self.UpdateWindowUI(wx.UPDATE_UI_RECURSE)

    #----------------------------------------------------------------------

    def OnInternalIdle(self):
        '''
        This virtual function is normally only used internally, but
        sometimes an application may need it to implement functionality
        that should not be disabled by an application defining an OnIdle
        handler in a derived class.

        This function may be used to do delayed painting, for example,
        and most implementations call UpdateWindowUI() in order to send
        update events to the window in idle time.
        '''
        if True:
            msg = 'NotImplementedError: %s' % 'OnInternalIdle in tsWxWindow'
            self.logger.error(msg)
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

##        if ( wxUpdateUIEvent.CanUpdate(self) ):
##            UpdateWindowUI(wx.UPDATE_UI_FROMIDLE)

    #----------------------------------------------------------------------

    def OnMaximize(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'OnMaximize in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #----------------------------------------------------------------------

    def OnMinimize(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'OnMinimize in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #----------------------------------------------------------------------

    def OnRestoreDown(self, evt):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'OnRestoreDown in tsWxWindow'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    # End tsWx API Extensions
    #----------------------------------------------------------------------

    AcceleratorTable = property(GetAcceleratorTable, SetAcceleratorTable)
    AutoLayout = property(GetAutoLayout, SetAutoLayout)
    BackgroundColour = property(GetBackgroundColour, SetBackgroundColour)
    BackgroundStyle = property(GetBackgroundStyle, SetBackgroundStyle)
    BestSize = property(GetBestSize)
    BestVirtualSize = property(GetBestVirtualSize)
    Border = property(GetBorder)
    Caret = property(GetCaret, SetCaret)
    CharHeight = property(GetCharHeight)
    CharWidth = property(GetCharWidth)
    Children = property(GetChildren)
    ClientAreaOrigin = property(GetClientAreaOrigin)
    ClientRect = property(GetClientRect, SetClientRect)
    ClientSize = property(GetClientSize, SetClientSize)
    Constraints = property(GetConstraints, SetConstraints)
    ContainingSizer = property(GetContainingSizer, SetContainingSizer)
    Cursor = property(GetCursor, SetCursor)
    DefaultAttributes = property(GetDefaultAttributes)
    DropTarget = property(GetDropTarget, SetDropTarget)
    EffectiveMinSize = property(GetEffectiveMinSize)
    Enabled = property(IsEnabled, Enable)
    EventHandler = property(GetEventHandler, SetEventHandler)
    ExtraStyle = property(GetExtraStyle, SetExtraStyle)
    Font = property(GetFont, SetFont)
    ForegroundColour = property(GetForegroundColour, SetForegroundColour)
    GrandParent = property(GetGrandParent)
    GtkWidget = property(GetGtkWidget)
    Handle = property(GetHandle)
    HelpText = property(GetHelpText, SetHelpText)
    Id = property(GetId, SetId)
    Label = property(GetLabel, SetLabel)
    LayoutDirection = property(GetLayoutDirection, SetLayoutDirection)
    MaxHeight = property(GetMaxHeight)
    MaxSize = property(GetMaxSize, SetMaxSize)
    MaxWidth = property(GetMaxWidth)
    MinHeight = property(GetMinHeight)
    MinSize = property(GetMinSize, SetMinSize)
    MinWidth = property(GetMinWidth)
    Name = property(GetName, SetName)
    Parent = property(GetParent)
    Position = property(GetPosition, SetPosition)
    Rect = property(GetRect, SetRect)
    ScreenPosition = property(GetScreenPosition)
    ScreenRect = property(GetScreenRect)
    Shown = property(IsShown, Show)
    Size = property(GetSize, SetSize)
    Sizer = property(GetSizer, SetSizer)
    ThemeEnabled = property(GetThemeEnabled, SetThemeEnabled)
##    thisown: The membership flag)
    ToolTip = property(GetToolTip, SetToolTip)
    TopLevel = property(IsTopLevel)
    TopLevelParent = property(GetTopLevelParent)
    UpdateClientRect = property(GetUpdateClientRect)
    UpdateRegion = property(GetUpdateRegion)
    Validator = property(GetValidator, SetValidator)
    VirtualSize = property(GetVirtualSize, SetVirtualSize)
    WindowStyle = property(GetWindowStyle, SetWindowStyle)
    WindowStyleFlag = property(GetWindowStyleFlag, SetWindowStyleFlag)
    WindowVariant = property(GetWindowVariant, SetWindowVariant)
    tsTopLevelAncestor = property(GetTopLevelAncestor, SetTopLevelAncestor)
    tsTopLevelSiblings = property(GetTopLevelSiblings, SetTopLevelSiblings)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    def theMainApplication():
        print(__header__)

        myWindow = Window(None)

        print('tsGetCharacterValues (80, 40):', myWindow.tsGetCharacterValues(
            640, 480))
        print('tsGetCharacterValues (-1, -1):', myWindow.tsGetCharacterValues(
            -1, -1))
        print('tsGetPixelValues (8, 12):', myWindow.tsGetPixelValues(1, 1))
        print('tsGetPixelValues (-1, -1):', myWindow.tsGetPixelValues(-1, -1))
        print('getCharacterRectangle (2, 3, 80, 40):', myWindow.tsGetCharacterRectangle(16, 36, 640, 480))

        print('getCharacterRectangle (-1, -1, -1, -1):', myWindow.tsGetCharacterRectangle(-1, -1, -1, -1))

        myTuple = (16, 36, 640, 480)
        myClass = wxRect
        myRect = wx.tsGetClassInstanceFromTuple(myTuple, myClass)
        print('tsGetClassInstanceFromTuple %s: %s' % (type(myRect), myRect))

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:
        theApplication = TsApplication(
            header=__header__,
            main=theMainApplication,
            mainTitleVersionDate=mainTitleVersionDate,
            title=__title__,
            version=__version__,
            date=__date__,
            logs=['cliAPP', 'guiAPP'])

        theApplication.runMain()
    except Exception as theApplication:
        if isinstance(theApplication, tse.TsExceptions):
            msg = str(theApplication)
            tse.displayError(theApplication)
            exitStatus = theApplication.exitCode
        else:
            msg = None
            sys.stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

    if msg == tse.NO_ERROR:
        sys.stdout.write(msg)
    elif msg is not None:
        sys.stderr.write(msg.replace('"', ''))

    # Return (exitStatus)
    sys.exit(exitStatus)
