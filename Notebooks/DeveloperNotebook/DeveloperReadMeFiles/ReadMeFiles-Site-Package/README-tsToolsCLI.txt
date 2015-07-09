#"Time-stamp: <12/06/2014  9:22:07 AM rsg>"

=============== File: README-tsToolsCLI.txt ================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "nCurses"-based
   +---------+         Graphical-Text User Interface (GUI)

   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode terminals and terminal emulators.

===================== TABLE OF CONTENTS ====================

1. Package Organization
2. tsLinesOfCodeProjectMetricsPkg
3. tsPlatformQueryPkg
4. tsStripCommentsPkg
5. tsStripLineNumbersPkg
6. tsTreeCopyPkg
7. tsTreeTrimLinesPkg

=================== PACKAGE ORGANIZATION ===================

1. Package Organization

  The collection of application programs for improving and
  tracking the productivity of software developers is
  organized, by the functional scope of each tool, into
  "packages". When appropriate, any package may import
  and use the services of any tsLibCLI package.
  
  Source code is contained in the associated ["src"] sub-
  directory. Depending on its complexity, the source code
  of a package may also be sub-divided and organized into
  a set of one or more source files.
  
  Unit/Integration Test code is contained in the associated
  ["test"] sub-directory. Depending on its complexity, the
  test code of a package may also be sub-divided and organ-
  ized into a set of one or more test files.

============== tsLinesOfCodeProjectMetricsPkg ==============

2. tsLinesOfCodeProjectMetricsPkg

  tsLinesOfCodeProjectMetricsPkg - Python application pro-
  gram, with a Command Line Interface (CLI), that generates
  reports of software project progress and the estimated
  cost (or contributed value) of the project when it is
  finally completed.

  It scans an operator designated file directory tree con-
  taining the source files, in one or more programming lan-
  guage specific formats (such as Ada, Assembler, C/C++,
  Cobol, Fortran, PL/M, Python, Text, and various command
  line shells).

  * For each file, it accumulates and reports the total
    number of code lines, blank/comment lines, words and
    characters.

  * For each programming language format, it accumulates
    and reports a summary of details of the associated
    source files.

  * For the entire set of source files, it accumulates
    and reports a summary of details.

  It uses the summary of the entire set of source files
  to derive, analyze, estimate and report metrics for the
  software development project (such as labor, cost,
  schedule and lines of code per day productivity). 

==================== tsPlatformQueryPkg ====================

3. tsPlatformQueryPkg

  tsPlatformQueryPkg - Python application program, with
  a Command Line Interface (CLI), that uses tsPlatform-
  RunTimeEnvironmentPkg to capture current hardware and
  software information about the run time environment
  available to computer programs.

==================== tsStripCommentsPkg ====================

4. tsStripCommentsPkg

  tsStripCommentsPkg - Python application program, with
  a Command Line Interface (CLI), to transform an annotated,
  development version of a directory of sub-directories
  and Python source files into an un-annotated copy. The
  copy is intended to conserve storage space when installed
  in an embedded system. The transformation involves
  stripping comments and docstrings by de-tokenizing a
  tokenized version of each Python source file. Non-Python
  files are trimmed of trailing whitespace.

=================== tsStripLineNumbersPkg ==================

5. tsStripLineNumbersPkg

  tsStripLineNumbersPkg - Python application program, with
  a Command Line Interface (CLI), to strip line numbers
  from source code (such as annotated listings) that do
  not reference line numbers for conditional branching.

======================= tsTreeCopyPkg ======================

6. tsTreeCopyPkg

  tsTreeCopyPkg - Python application program, with
  a Command Line Interface (CLI), to copy the files
  and directories contained in a source directory
  to a target directory.

=================== tsTreeTrimLinesPkg ==================

7. tsTreeTrimLinesPkg

  tsTreeTrimLinesPkg - Python application program, with
  a Command Line Interface (CLI), to copy the files and
  directories contained in a source directory to a target
  directory after stripping superfluous white space
  (blanks) from end of each line.

======================= End-Of-File ========================
