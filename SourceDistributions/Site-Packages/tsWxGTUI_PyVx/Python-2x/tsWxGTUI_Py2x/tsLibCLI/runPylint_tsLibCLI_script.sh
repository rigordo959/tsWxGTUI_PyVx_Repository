#!/bin/bash
#"Time-stamp: <08/25/2016  8:27:00 AM rsg>"
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
makePyLint __init__.py
makePyLint tsApplication.py
makePyLint tsCommandLineEnv.py
makePyLint tsCommandLineInterface.py
makePyLint tsCxGlobals.py
makePyLint tsDoubleLinkedList.py
makePyLint tsExceptions.py
makePyLint tsGistGetTerminalSize.py
makePyLint tsLogger.py
makePyLint tsOperatorSettingsParser.py
makePyLint tsPlatformRunTimeEnvironment.py
makePyLint tsReportUtilities.py
makePyLint tsSysCommands.py
