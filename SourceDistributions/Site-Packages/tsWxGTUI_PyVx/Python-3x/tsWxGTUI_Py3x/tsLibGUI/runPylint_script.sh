#!/bin/bash
#"Time-stamp: <08/25/2016  8:31:41 AM rsg>"
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
tsWx.py
tsWxAboutDialogInfo.py_draft
tsWxAcceleratorEntry.py
tsWxAcceleratorTable.py
tsWxActivateEvent.py_draft
tsWxApp.py
tsWxAppConsole.py_draft
tsWxBoxSizer.py
tsWxButton.py
tsWxCallLater.py
tsWxCaret.py
tsWxCheckBox.py
tsWxChildFocusEvent.py_draft
tsWxChoice.py
tsWxClipboard.py_draft
tsWxClipboardLocker.py_draft
tsWxClipboardTextEvent.py_draft
tsWxCloseEvent.py_draft
tsWxColor.py
tsWxColorDatabase.py
tsWxColour.py_draft
tsWxColourData.py_draft
tsWxControl.py
tsWxControlWithItems.py
tsWxCursesKeyCodesDataBase.py
tsWxCursesMouseButtonCodesDataBase.py
tsWxCursesServices.py
tsWxCursor.py
tsWxDebugHandlers.py
tsWxDialog.py
tsWxDialogButton.py
tsWxDisplay.py
tsWxDoubleLinkedList.py
tsWxEraseEvent.py
tsWxEvent.py
tsWxEventDaemon.py
tsWxEventLoop.py
tsWxEventLoopActivator.py
tsWxEventQueueEntry.py
tsWxEventTableEntry.py
tsWxEvtHandler.py
tsWxFlexGridSizer.py
tsWxFocusEvent.py
tsWxFrame.py
tsWxFrameButton.py
tsWxGauge.py
tsWxGlobals.py
tsWxGraphicalTextUserInterface.py
tsWxGridBagSizer.py
tsWxGridSizer.py
tsWxItemContainer.py
tsWxKeyboardState.py
tsWxKeyEvent.py
tsWxListBox.py
tsWxLog.py
tsWxMenu.py
tsWxMenuBar.py
tsWxMouseEvent.py
tsWxMouseState.py
tsWxMultiFrameEnv.py
tsWxNonLinkedList.py
tsWxObject.py
tsWxPanel.py
tsWxPasswordEntryDialog.py
tsWxPoint.py
tsWxPyApp.py
tsWxPyEventBinder.py
tsWxPyOnDemandOutputWindow.py
tsWxPySimpleApp.py
tsWxPySizer.py
tsWxPythonColor16DataBase.py
tsWxPythonColor16SubstitutionMap.py
tsWxPythonColor256DataBase.py
tsWxPythonColor88DataBase.py
tsWxPythonColor8DataBase.py
tsWxPythonColor8SubstitutionMap.py
tsWxPythonColorDataBaseRGB.py
tsWxPythonColorNames.py
tsWxPythonColorRGBNames.py
tsWxPythonColorRGBValues.py
tsWxPythonMonochromeDataBase.py
tsWxPythonPrivateLogger.py
tsWxRadioBox.py
tsWxRadioButton.py
tsWxRect.py
tsWxScreen.py
tsWxScrollBar.py
tsWxScrollBarButton.py
tsWxScrollBarGauge.py
tsWxScrolled.py
tsWxScrolledText.py
tsWxScrolledWindow.py
tsWxShowEvent.py
tsWxSize.py
tsWxSizer.py
tsWxSizerFlags.py
tsWxSizerItem.py
tsWxSizerItemList.py
tsWxSizerSpacer.py
tsWxSlider.py
tsWxSplashScreen.py
tsWxStaticBox.py
tsWxStaticBoxSizer.py
tsWxStaticLine.py
tsWxStaticText.py
tsWxStatusBar.py
tsWxSystemSettings.py
tsWxTaskBar.py
tsWxTextCtrl.py
tsWxTextEditBox.py
tsWxTextEntry.py
tsWxTextEntryDialog.py
tsWxTimer.py
tsWxToggleButton.py
tsWxTopLevelWindow.py
tsWxValidator.py
tsWxWindow.py
tsWxWindowCurses.py

