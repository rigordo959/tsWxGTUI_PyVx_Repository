#!/bin/bash
#"Time-stamp: <08/25/2016  8:19:45 AM rsg>"
#
function makeManPage() {
  pydoc $1.py > $1.man
}

# makeManPage ./PyDbLite
# makeManPage ./RobinDunnExample
# makeManPage ./SimpleAsyncHTTPServer
# makeManPage ./baseline_test_tsWxMultiFrameEnv
# makeManPage ./baseline_tsWxMultiFrameEnv
# makeManPage ./breadboard_tsLogger_tsLogging
# makeManPage ./buzhug
# makeManPage ./buzhug_algos
# makeManPage ./buzhug_client
# makeManPage ./buzhug_files
# makeManPage ./buzhug_server
# makeManPage ./buzhug_test
# makeManPage ./create_pylint_script
# makeManPage ./curses_keycode
# makeManPage ./draft_test_tsWxFrameEmulation
# makeManPage ./draft_test_tsWxMultiFrameEnv
# makeManPage ./draft_test_tsWxWidgets
# makeManPage ./draft_tsLinesOfCodeProjectMetrics
# makeManPage ./draft_tsStripComments
# makeManPage ./draft_tsWxMultiFrameEnv
# makeManPage ./draft_tsWxWidgets
# makeManPage ./getStripCommentsArgParseOptions
# makeManPage ./getStripCommentsOptParseOptions
# makeManPage ./hello_world
# makeManPage ./ipv4socketclient
# makeManPage ./ipv4socketserver
# makeManPage ./ipv6socketclient
# makeManPage ./ipv6socketserver
# makeManPage ./junkcolor
# makeManPage ./junktab
# makeManPage ./life
# makeManPage ./ncurses
# makeManPage ./new_test_tsWxRSM
# makeManPage ./process_tsWxLinesOfCode
# makeManPage ./rain
# makeManPage ./repeat
# makeManPage ./rick_tsWxGUI
# makeManPage ./rsg_aui_demo
# makeManPage ./sample_delwin
# makeManPage ./sample_textCtrlCursor
# makeManPage ./scratchpad
# makeManPage ./setup
# makeManPage ./stripCommentsAndDocStrings
# makeManPage ./stripLineNumbers
# makeManPage ./tclock
# makeManPage ./test_BoxSizer
# makeManPage ./test_GetArgs
# makeManPage ./test_GetOptions
# makeManPage ./test_GridSizer
# makeManPage ./test_Partitioning
# makeManPage ./test_assert_valid_sizer_flags
# makeManPage ./test_bitshift
# makeManPage ./test_colorRGBList
# makeManPage ./test_colors
# makeManPage ./test_copyright
# makeManPage ./test_dictkey
# makeManPage ./test_disclaimer
# makeManPage ./test_license
# makeManPage ./test_multi_author_copyright
# makeManPage ./test_ncurses
# makeManPage ./test_print
# makeManPage ./test_pythonCurses
# makeManPage ./test_tabs
# makeManPage ./test_thread_tsWxLinesOfCode
# makeManPage ./test_topLevel
# makeManPage ./test_tsApplication
# makeManPage ./test_tsCommandLineEnv
# makeManPage ./test_tsCommandLineInterface
# makeManPage ./test_tsCommandLineParser
# makeManPage ./test_tsCurses
# makeManPage ./test_tsDecorators
# makeManPage ./test_tsDiagnosticCurses
# makeManPage ./test_tsExceptions
# makeManPage ./test_tsLibraries
# makeManPage ./test_tsLinesOfCode
# makeManPage ./test_tsLogger
# makeManPage ./test_tsOperatorSettingsParser
# makeManPage ./test_tsParseAcceleratorTextLabel
# makeManPage ./test_tsPlatformRunTimeEnvironment
# makeManPage ./test_tsReportUtilities
# makeManPage ./test_tsStripComments
# makeManPage ./test_tsStripSettingsParser
# makeManPage ./test_tsSysCommand
# makeManPage ./test_tsThreadPool
# makeManPage ./test_tsWxAUI
# makeManPage ./test_tsWxAcceleratorEntry
# makeManPage ./test_tsWxBoxLogo
# makeManPage ./test_tsWxBoxSizer
# makeManPage ./test_tsWxCheckBox
# makeManPage ./test_tsWxCheckBoxEvent
# makeManPage ./test_tsWxCliLinesOfCode
# makeManPage ./test_tsWxCurses
# makeManPage ./test_tsWxDiagnostic
# makeManPage ./test_tsWxDialogDemo
# makeManPage ./test_tsWxDisplay
# makeManPage ./test_tsWxEvents
# makeManPage ./test_tsWxFieldMarkup
# makeManPage ./test_tsWxFileCommander
# makeManPage ./test_tsWxFrame
# makeManPage ./test_tsWxFrameEmulation
# makeManPage ./test_tsWxGauge
# makeManPage ./test_tsWxGraphicalTextUserInterface
# makeManPage ./test_tsWxGridSizer
# makeManPage ./test_tsWxKeyEvents
# makeManPage ./test_tsWxLinesOfCode
# makeManPage ./test_tsWxLogo
# makeManPage ./test_tsWxMarkupDiagnostic
# makeManPage ./test_tsWxMetrics
# makeManPage ./test_tsWxMidiWindow
# makeManPage ./test_tsWxMouseEvent
# makeManPage ./test_tsWxMultiFrameEnv
# makeManPage ./test_tsWxOverlays
# makeManPage ./test_tsWxPasswordEntryDialog
# makeManPage ./test_tsWxPySimpleApp
# makeManPage ./test_tsWxRSM
# makeManPage ./test_tsWxRadioBox
# makeManPage ./test_tsWxRadioBoxEvent
# makeManPage ./test_tsWxScrollBar
# makeManPage ./test_tsWxScrolled
# makeManPage ./test_tsWxScrolled3Boxes
# makeManPage ./test_tsWxScrolledWindow
# makeManPage ./test_tsWxScrolledWindowDual
# makeManPage ./test_tsWxSplashScreen
# makeManPage ./test_tsWxStaticBoxSizer
# makeManPage ./test_tsWxStaticLine
# makeManPage ./test_tsWxStaticText
# makeManPage ./test_tsWxStatusBar
# makeManPage ./test_tsWxSystemSettings
# makeManPage ./test_tsWxTaskBar
# makeManPage ./test_tsWxTemplate
# makeManPage ./test_tsWxTextCtrl
# makeManPage ./test_tsWxTextEntryDialog
# makeManPage ./test_tsWxVt100Widgets
# makeManPage ./test_tsWxWidgets
# makeManPage ./test_tsWxWidgetsMarkup
# makeManPage ./test_version_comparison
# makeManPage ./test_wxAUI
# makeManPage ./test_wxAUI_rsg_01
# makeManPage ./test_wxAUI_rsg_02
# makeManPage ./test_wxBoxSizer
# makeManPage ./test_wxFrame
# makeManPage ./test_wxGridBagSizer
# makeManPage ./test_wxGridSizer
# makeManPage ./test_wxPySimpleApp
# makeManPage ./test_wxPython
# makeManPage ./test_wxPythonColors
# makeManPage ./test_wxSizerItemList
# makeManPage ./test_wxWidgets
# makeManPage ./test_wx_dir
# makeManPage ./thread_tsWxLinesOfCode
# makeManPage ./threadpool
# makeManPage ./tsLogger_test
# makeManPage ./wxPython_colors
# makeManPage ./wxPython_keycode
# makeManPage ./wxcursors
# makeManPage ./xmas

makeManPage ./configobj
makeManPage ./decorator
makeManPage ./tsApplication
makeManPage ./tsCommandLineEnv
makeManPage ./tsCommandLineInterface
makeManPage ./tsCommandLineParser
makeManPage ./tsCommandLineParserBuilder
makeManPage ./tsConfig
makeManPage ./tsDecorators
makeManPage ./tsExceptions
makeManPage ./tsGraphicalTextUserInterface
makeManPage ./tsLibraryImport
makeManPage ./tsLinesOfCode
makeManPage ./tsLinesOfCodeProjectMetrics
makeManPage ./tsLogger
makeManPage ./tsLoggerMinimized
makeManPage ./tsOperatorSettingsParser
makeManPage ./tsOperatorSettingsParserBuilder
makeManPage ./tsOptionParser
makeManPage ./tsPlatformQuery
makeManPage ./tsPlatformRunTimeEnvironment
makeManPage ./tsProjectMetrics
makeManPage ./tsPublish
makeManPage ./tsReAuthor
makeManPage ./tsReImport
makeManPage ./tsReVersion
makeManPage ./tsReportUtilities
makeManPage ./tsSoftwareMetrics
makeManPage ./tsSoftwareParser
makeManPage ./tsStripComments
makeManPage ./tsStripLineNumbers
makeManPage ./tsStripSettingsParser
makeManPage ./tsSysCommands
makeManPage ./tsThreadPool
makeManPage ./tsTreeCopy
makeManPage ./tsTreeTrimLines
makeManPage ./tsTreeTrimShutil
makeManPage ./tsWx
makeManPage ./tsWxAcceleratorEntry
makeManPage ./tsWxAcceleratorTable
makeManPage ./tsWxApp
makeManPage ./tsWxBasicGridSizer
makeManPage ./tsWxBoxSizer
makeManPage ./tsWxButton
makeManPage ./tsWxCallLater
makeManPage ./tsWxCaret
makeManPage ./tsWxCheckBox
makeManPage ./tsWxChoice
makeManPage ./tsWxColor
makeManPage ./tsWxColorDatabase
makeManPage ./tsWxCommandLineEnv
makeManPage ./tsWxControl
makeManPage ./tsWxControlWithItems
makeManPage ./tsWxCursor
makeManPage ./tsWxDebugHandlers
makeManPage ./tsWxDialog
makeManPage ./tsWxDialogButton
makeManPage ./tsWxDisplay
makeManPage ./tsWxDoubleLinkedList
makeManPage ./tsWxEraseEvent
makeManPage ./tsWxEvent
makeManPage ./tsWxEventDaemon
makeManPage ./tsWxEventLoop
makeManPage ./tsWxEventLoopActivator
makeManPage ./tsWxEventQueueEntry
makeManPage ./tsWxEventTableEntry
makeManPage ./tsWxEvtHandler
makeManPage ./tsWxFlexGridSizer
makeManPage ./tsWxFocusEvent
makeManPage ./tsWxFrame
makeManPage ./tsWxFrameButton
makeManPage ./tsWxGauge
makeManPage ./tsWxGlobals
makeManPage ./tsWxGraphicalTextUserInterface
makeManPage ./tsWxGridBagSizer
makeManPage ./tsWxGridSizer
makeManPage ./tsWxItemContainer
makeManPage ./tsWxKeyEvent
makeManPage ./tsWxKeyboardState
makeManPage ./tsWxLayoutAlgorithm
makeManPage ./tsWxLayout_h
makeManPage ./tsWxLinesOfCode
makeManPage ./tsWxListBox
makeManPage ./tsWxLog
makeManPage ./tsWxMenu
makeManPage ./tsWxMenuBar
makeManPage ./tsWxMouseEvent
makeManPage ./tsWxMouseState
makeManPage ./tsWxMultiFrameEnv
makeManPage ./tsWxMultiFrameEnv_new
makeManPage ./tsWxNonLinkedList
makeManPage ./tsWxObject
makeManPage ./tsWxPanel
makeManPage ./tsWxPasswordEntryDialog
makeManPage ./tsWxPoint
makeManPage ./tsWxPyApp
makeManPage ./tsWxPyEventBinder
makeManPage ./tsWxPyOnDemandOutputWindow
makeManPage ./tsWxPySimpleApp
makeManPage ./tsWxPySizer
makeManPage ./tsWxRadioBox
makeManPage ./tsWxRadioButton
makeManPage ./tsWxReVersion
makeManPage ./tsWxRect
makeManPage ./tsWxRobinDunnExample
makeManPage ./tsWxScreen
makeManPage ./tsWxScrollBar
makeManPage ./tsWxScrollBarButton
makeManPage ./tsWxScrollBarGauge
makeManPage ./tsWxScrolled
makeManPage ./tsWxScrolledText
makeManPage ./tsWxScrolledWindow
makeManPage ./tsWxShowEvent
makeManPage ./tsWxSize
makeManPage ./tsWxSizer
makeManPage ./tsWxSizerFlags
makeManPage ./tsWxSizerItem
makeManPage ./tsWxSizerItemList
makeManPage ./tsWxSizerSpacer
makeManPage ./tsWxSlider
makeManPage ./tsWxSplashScreen
makeManPage ./tsWxStaticBox
makeManPage ./tsWxStaticBoxSizer
makeManPage ./tsWxStaticLine
makeManPage ./tsWxStaticText
makeManPage ./tsWxStatusBar
makeManPage ./tsWxSystemSettings
makeManPage ./tsWxTaskBar
makeManPage ./tsWxTextCtrl
makeManPage ./tsWxTextEditBox
makeManPage ./tsWxTextEntry
makeManPage ./tsWxTextEntryDialog
makeManPage ./tsWxTimer
makeManPage ./tsWxToggleButton
makeManPage ./tsWxTopLevelWindow
makeManPage ./tsWxValidator
makeManPage ./tsWxWindow
makeManPage ./validate
