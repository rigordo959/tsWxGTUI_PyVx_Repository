#!/bin/bash
#"Time-stamp: <08/25/2016  8:30:06 AM rsg>"
#
function makeManPage() {
  pydoc $1.py > $1.man
}

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
