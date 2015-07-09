#!/usr/bin/bash
#"Time-stamp: <02/13/2014  6:43:29 AM rsg>"
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

makePyLint ./tsApplication
makePyLint ./tsCommandLineEnv
makePyLint ./tsCommandLineInterface
makePyLint ./tsCxGlobals
makePyLint ./tsDoubleLinkedList
makePyLint ./tsExceptions
makePyLint ./tsGistGetTerminalSize
makePyLint ./tsLogger
makePyLint ./tsOperatorSettingsParser
makePyLint ./tsPlatformRunTimeEnvironment
makePyLint ./tsReportUtilities
makePyLint ./tsSysCommands

