#!/bin/bash
#"Time-stamp: <08/25/2016  8:20:03 AM rsg>"
# lookForErrors="E:"
# lookForWarnings="W:"
# lookFor=lookForErrors
rm -rf ../pylint
mkdir  ../pylint
mkdir  ../pylint/Report
mkdir  ../pylint/Convention
mkdir  ../pylint/Error
mkdir  ../pylint/Fatal
mkdir  ../pylint/Refactor
mkdir  ../pylint/Warning

function makePyLint() {
  echo "makePyLint(" $1 ")"
  echo "    Report(" $1 ")"
  pylint $1.py > ../pylint/Report/$1.lst
  echo "    Convention(" $1 ")"
  # pylint $1.py | grep "C:" > ../pylint/Convention/$1.lst
  cat ../pylint/Report/$1.lst | grep "C:" > ../pylint/Convention/$1.lst
  echo "    Error(" $1 ")"
  # pylint $1.py | grep "E:" > ../pylint/Error/$1.lst
  cat ../pylint/Report/$1.lst | grep "E:" > ../pylint/Error/$1.lst
  echo "    Fatal(" $1 ")"
  # pylint $1.py | grep "F:" > ../pylint/Fatal/$1.lst
  cat ../pylint/Report/$1.lst | grep "F:" > ../pylint/Fatal/$1.ls
  echo "    Refactor(" $1 ")"t
  # pylint $1.py | grep "R:" > ../pylint/Refactor/$1.lst
  cat ../pylint/Report/$1.lst | grep "R:" > ../pylint/Refactor/$1.lst
  echo "    Warning(" $1 ")"
  # pylint $1.py | grep "W:" > ../pylint/Warning/$1.lst
  cat ../pylint/Report/$1.lst | grep "W:" > ../pylint/Warning/$1.lst

}

# makePyLint ./__init__
makePyLint ./__init__
makePyLint ./test_tsApplication
makePyLint ./test_tsCommandLineEnv
makePyLint ./test_tsCommandLineInterface
makePyLint ./test_tsCxGlobals
makePyLint ./test_tsDoubleLinkedList
makePyLint ./test_tsExceptions
makePyLint ./test_tsLogger
makePyLint ./test_tsOperatorSettingsParser
makePyLint ./test_tsPlatformRunTimeEnvironment
makePyLint ./test_tsReportUtilities
makePyLint ./test_tsSysCommand
makePyLint ./test_tsWxBoxSizer
makePyLint ./test_tsWxGlobals
makePyLint ./test_tsWxGraphicalTextUserInterface
makePyLint ./test_tsWxGridSizer
makePyLint ./test_tsWxMultiFrameEnv
makePyLint ./test_tsWxScrolledWindow
makePyLint ./test_tsWxScrolledWindowDual
makePyLint ./test_tsWxWidgets
makePyLint ./tsApplication
makePyLint ./tsCommandLineEnv
makePyLint ./tsCommandLineInterface
makePyLint ./tsCxGlobals
makePyLint ./tsDoubleLinkedList
makePyLint ./tsExceptions
makePyLint ./tsGistGetTerminalSize
makePyLint ./tsLogger
makePyLint ./tsOperatorSettingsParser
makePyLint ./tsOperatorSettingsParserBuilder
makePyLint ./tsPlatformQuery
makePyLint ./tsPlatformRunTimeEnvironment
makePyLint ./tsReportUtilities
makePyLint ./tsSysCommands
makePyLint ./tsWx
makePyLint ./tsWxAcceleratorEntry
makePyLint ./tsWxAcceleratorTable
makePyLint ./tsWxApp
makePyLint ./tsWxBoxSizer
makePyLint ./tsWxButton
makePyLint ./tsWxCallLater
makePyLint ./tsWxCaret
makePyLint ./tsWxCheckBox
makePyLint ./tsWxChoice
makePyLint ./tsWxColor
makePyLint ./tsWxColorDatabase
makePyLint ./tsWxControl
makePyLint ./tsWxControlWithItems
makePyLint ./tsWxCursor
makePyLint ./tsWxDebugHandlers
makePyLint ./tsWxDialog
makePyLint ./tsWxDialogButton
makePyLint ./tsWxDisplay
makePyLint ./tsWxDoubleLinkedList
makePyLint ./tsWxEraseEvent
makePyLint ./tsWxEvent
makePyLint ./tsWxEventDaemon
makePyLint ./tsWxEventLoop
makePyLint ./tsWxEventLoopActivator
makePyLint ./tsWxEventQueueEntry
makePyLint ./tsWxEventTableEntry
makePyLint ./tsWxEvtHandler
makePyLint ./tsWxFlexGridSizer
makePyLint ./tsWxFocusEvent
makePyLint ./tsWxFrame
makePyLint ./tsWxFrameButton
makePyLint ./tsWxGauge
makePyLint ./tsWxGlobals
makePyLint ./tsWxGraphicalTextUserInterface
makePyLint ./tsWxGridBagSizer
makePyLint ./tsWxGridSizer
makePyLint ./tsWxItemContainer
makePyLint ./tsWxKeyboardState
makePyLint ./tsWxKeyEvent
makePyLint ./tsWxListBox
makePyLint ./tsWxLog
makePyLint ./tsWxMenu
makePyLint ./tsWxMenuBar
makePyLint ./tsWxMouseEvent
makePyLint ./tsWxMouseState
makePyLint ./tsWxMultiFrameEnv
makePyLint ./tsWxNonLinkedList
makePyLint ./tsWxObject
makePyLint ./tsWxPanel
makePyLint ./tsWxPasswordEntryDialog
makePyLint ./tsWxPoint
makePyLint ./tsWxPyApp
makePyLint ./tsWxPyEventBinder
makePyLint ./tsWxPyOnDemandOutputWindow
makePyLint ./tsWxPySimpleApp
makePyLint ./tsWxPySizer
makePyLint ./tsWxRadioBox
makePyLint ./tsWxRadioButton
makePyLint ./tsWxRect
makePyLint ./tsWxScreen
makePyLint ./tsWxScrollBar
makePyLint ./tsWxScrollBarButton
makePyLint ./tsWxScrollBarGauge
makePyLint ./tsWxScrolled
makePyLint ./tsWxScrolledText
makePyLint ./tsWxScrolledWindow
makePyLint ./tsWxShowEvent
makePyLint ./tsWxSize
makePyLint ./tsWxSizer
makePyLint ./tsWxSizerFlags
makePyLint ./tsWxSizerItem
makePyLint ./tsWxSizerItemList
makePyLint ./tsWxSizerSpacer
makePyLint ./tsWxSlider
makePyLint ./tsWxSplashScreen
makePyLint ./tsWxStaticBox
makePyLint ./tsWxStaticBoxSizer
makePyLint ./tsWxStaticLine
makePyLint ./tsWxStaticText
makePyLint ./tsWxStatusBar
makePyLint ./tsWxSystemSettings
makePyLint ./tsWxTaskBar
makePyLint ./tsWxTextCtrl
makePyLint ./tsWxTextEditBox
makePyLint ./tsWxTextEntry
makePyLint ./tsWxTextEntryDialog
makePyLint ./tsWxTimer
makePyLint ./tsWxToggleButton
makePyLint ./tsWxTopLevelWindow
makePyLint ./tsWxValidator
makePyLint ./tsWxWindow
makePyLint ./wingdbstub
