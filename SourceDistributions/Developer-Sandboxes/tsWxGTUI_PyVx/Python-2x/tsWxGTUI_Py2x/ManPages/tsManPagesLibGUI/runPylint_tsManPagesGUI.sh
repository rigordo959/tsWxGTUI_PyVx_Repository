#!/bin/bash
#"Time-stamp: <08/25/2016  8:15:09 AM rsg>"
# lookForErrors="E:"
# lookForWarnings="W:"
# lookFor=lookForErrors
rm -rf ../pylint
mkdir  ../pylint
mkdir  ../pylint/Errors
mkdir  ../pylint/Warnings

function makePyLint() {
  pylint $1.py | grep "E:" > ../pylint/Errors/$1.lst
  pylint $1.py | grep "W:" > ../pylint/Warnings/$1.lst
}
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
makePyLint ./tsWxCliLinesOfCode
makePyLint ./tsWxColor
makePyLint ./tsWxColorDatabase
makePyLint ./tsWxCommandLineEnv
makePyLint ./tsWxControl
makePyLint ./tsWxControlWithItems
makePyLint ./tsWxCursor
makePyLint ./tsWxDebugHandlers
makePyLint ./tsWxDialog
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
makePyLint ./tsWxGauge
makePyLint ./tsWxGlobals
makePyLint ./tsWxGraphicalTextUserInterface
makePyLint ./tsWxGridBagSizer
makePyLint ./tsWxGridSizer
makePyLint ./tsWxItemContainer
makePyLint ./tsWxKeyboardState
makePyLint ./tsWxKeyEvent
makePyLint ./tsWxLayout_h
makePyLint ./tsWxLayoutAlgorithm
makePyLint ./tsWxLayoutGTUI
makePyLint ./tsWxLinesOfCode
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
makePyLint ./tsWxReVersion
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
