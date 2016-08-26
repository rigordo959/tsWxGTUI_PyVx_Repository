#!/usr/bin/bash
#"Time-stamp: <04/20/2015  6:24:58 AM rsg>"
#
function makeManPage() {
  pydoc $1.py > $1.man
}

makeManPage ./tsApplication
makeManPage ./tsCommandLineEnv
makeManPage ./tsCommandLineInterface
makeManPage ./tsCxGlobals
makeManPage ./tsDoubleLinkedList
makeManPage ./tsExceptions
makeManPage ./tsGistGetTerminalSize
makeManPage ./tsLogger
makeManPage ./tsOperatorSettingsParser
makeManPage ./tsPlatformRunTimeEnvironment
makeManPage ./tsReportUtilities
makeManPage ./tsSysCommands

