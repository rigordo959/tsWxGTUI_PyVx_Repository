#-----------------------------------------------------------
#"Time-stamp: <07/07/2015  7:33:25 PM rsg>"
#-----------------------------------------------------------

=== Title Page for File: README7-Developer-Sandboxes.txt ===

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode 8-/16-color (xterm-family) & non-color
   (vt100-family) terminals and terminal emulators.

   You can find this and other plain-text files in the
   Toolkit subdirectory named:

       "./<Toolkit Recipient's Repository>/Documents".

       <Your Working Repository>
       (e.g. "tsWxGTUI_PyVx_Repository") 
         |
         |  Working repository containing directories and
         |  files to be packaged into downloadable "tarball"
         |  and/or "zip" files via the setup shell scripts
         |  at the bottom of this diagram.
         |
         +-- ["Documents"]
         |     |
         |     |  This directory contains a collection of files
         |     |  which provide the Toolkit recipient with an
         |     |  understanding of the purpose, goals & capabil-
         |     |  ities, non-goals & limitations, terms & condi-
         |     |  tions and procedures for installing, operating,
         |     |  modifying and redistributing the Toolkit. 
         |     |
         |     |  Deliverable Toolkit manual pages are a
         |     |  form of online software documentation
         |     |  usually found on a Unix or Unix-like oper-
         |     |  ating system.
         |     |
         |     +-- "README3-Documents.txt"
         |
         +-- ["ManPages"]
         |     |
         |     |  Deliverable Toolkit manual pages are a
         |     |  form of online software documentation
         |     |  usually found on a Unix or Unix-like oper-
         |     |  ating system.
         |     |
         |     +-- "README4-ManPages.txt"
         |
         +-- ["Notebooks"]
         |     |
         |     |  Contains a collection of commentaries that
         |     |  express opinions or offerings of explana-
         |     |  tions about events or situations that might
         |     |  be useful to Toolkit installers, developers,
         |     |  operators, troubleshooters and distributors.
         |     |  The documents may be in Application-specific
         |     |  formats (Adobe PDF, JPEG Bit-mapped image,
         |     |  Microsoft Office, Plain text etc.).
         |     |
         |     +-- "README5-Notebooks.txt"
         |
         +-- ["SourceDistributions"]
         |     |
         |     |  Contains a collection of computer program
         |     |  source code files that the Toolkit recip-
         |     |  ient will need to install, operate, modify
         |     |  and re-distribute the Toolkit.
         |     |
         |     +-- "README6-SourceDistributions.txt"
         |     |
         |     +-- ["Developer-Sandboxes"] (Pre-dates Site-Packages)
         |     |     |
         |     |     |  A sandbox is a testing environment that iso-
         |     |     |  lates untested code changes and outright experi-
         |     |     |  mentation from the production environment or
         |     |     |  repository.
         |     |     |
         |     |     +-- ["tsWxGTUI_PyVx"]
         |     |           |
         |     |           | Contains one or more Python language gener-
         |     |           | ation-specific releases each sharing the same
         |     |           | programmer (API) and user (CLI & GUI) inter-
         |     |           | faces, documents and manual pages.
         |     |           |
         |     |           +-- ["Documents"]
         |     |           |
         |     |           +-- ["ManPages"]
         |     |           |
         |     |           +-- ["Python-2x"]
         |     |           |     |
         |     |           |     | Second generation Python programming
         |     |           |     | language.
         |     |           |     |
         |     |           |     +-- ["tsWxGTUI_Py2x"]
         |     |           |           |
         |     |           |           +-- ["tsDemoArchive"]
         |     |           |           |     |
         |     |           |           |     +-- ["src"]
         |     |           |           |     |
         |     |           |           |     +-- "TermsAndConditions.txt"
         |     |           |           |
         |     |           |           +-- ["tsLibCLI"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsApplicationPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsCommandLineEnvPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsCommandLineInterfacePkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsCxGlobalsPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsDoubleLinkedListPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsExceptionPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsGistGetTerminalSizePkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsLoggerPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsOperatorSettingsParserPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsPlatformRunTimeEnvironmentPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsReportUtilityPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsSysCommandsPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |
         |     |           |           +-- ["tsLibGUI"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsWxPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |
         |     |           |           +-- ["tsToolsCLI"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsLinesOfCodeProjectMetricsPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsPlatformQueryPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsStripCommentsPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsStripLineNumbersPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsTreeCopyPkg"]
         |     |           |           |     |     |
         |     |           |           |     |     +-- ["src"]
         |     |           |           |     |     +-- ["test"]
         |     |           |           |     |
         |     |           |           |     +-- ["tsTreeTrimLinesPkg"]
         |     |           |           |           |
         |     |           |           |           +-- ["src"]
         |     |           |           |           +-- ["test"]
         |     |           |           |
         |     |           |           +-- ["tsToolsGUI"]
         |     |           |           |
         |     |           |           +-- ["tsUtilities"]
         |     |           |
         |     |           +-- ["Python-3x"] (Ported from Python-2x)
         |     |                 |
         |     |                 | Third generation Python programming
         |     |                 | language.
         |     |                 |
         |     |                 +-- ["tsWxGTUI_Py3x"]
         |     |
         |     +-- ["Site-Packages"]
         |           |
         |           |  A site-packages is the location where third-
         |           |  party packages are installed (i.e., those
         |           |  not part of the core Python distribution).
         |           |  NOTE: That with Linux, Mac OS X and Unix
         |           |  operating systems one must have root priv-
         |           |  iledges to write to that location.
         |           |
         |           +-- ["tsWxGTUI_PyVx"]
         |                 |
         |                 +-- ["Documents"]
         |                 |
         |                 +-- ["ManPages"]
         |                 |
         |                 +-- ["Python-2x"]
         |                 |     |
         |                 |     | Second generation Python programming
         |                 |     | language.
         |                 |     |
         |                 |     +-- ["tsWxGTUI_Py2x"]
         |                 |           |
         |                 |           +-- ["tsDemoArchive"]
         |                 |           |     |
         |                 |           |     +-- ["tsTestsLibCLI"]
         |                 |           |     +-- ["tsTestsLibGUI"]
         |                 |           |     +-- ["tsTestsToolsCLI"]
         |                 |           |     +-- ["tsTestsToolsGUI"]
         |                 |           |     +-- ["tsTestsToolsLibCLI"]
         |                 |           |     +-- ["tsTestsToolsLibGUI"]
         |                 |           |
         |                 |           +-- ["tsLibCLI"]
         |                 |           |
         |                 |           +-- ["tsLibGUI"]
         |                 |           |
         |                 |           +-- ["tsToolsCLI"]
         |                 |           |
         |                 |           +-- ["tsToolsGUI"]
         |                 |           |
         |                 |           +-- ["tsUtilities"]
         |                 |
         |                 +-- ["Python-3x"] (Ported from Python-2x)
         |                       |
         |                       | Third generation Python programming
         |                       | language.
         |                       |
         |                       +-- ["tsWxGTUI_Py3x"]
         |
         +-- "README.txt"

======================= End-Of-File ========================
