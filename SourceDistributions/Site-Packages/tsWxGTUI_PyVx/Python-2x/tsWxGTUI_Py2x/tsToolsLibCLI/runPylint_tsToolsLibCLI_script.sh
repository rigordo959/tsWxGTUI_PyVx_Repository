#!/usr/bin/bash
#"Time-stamp: <05/07/2015  9:30:15 AM rsg>"
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
  echo "    Refactor(" $1 ")"
  # pylint $1.py | grep "R:" > ../pylint/Refactor/$1.lst
  cat ../pylint/Report/$1.lst | grep "R:" > ../pylint/Refactor/$1.lst
  echo "    Warning(" $1 ")"
  # pylint $1.py | grep "W:" > ../pylint/Warning/$1.lst
  cat ../pylint/Report/$1.lst | grep "W:" > ../pylint/Warning/$1.lst

}

# makePyLint ./__init__
makePyLint ./__init__
makePyLint ./tsLinesOfCode.py
makePyLint ./tsLOCPMOperatorSettingsParser.py
makePyLint ./tsProjectMetrics.py
makePyLint ./tsPRTEOperatorSettingsParser.py
makePyLint ./tsSoftwareMetrics.py
makePyLint ./tsSoftwareParser.py
makePyLint ./tsStripSettingsParser.py
makePyLint ./tsTreeTrimShutil.py

