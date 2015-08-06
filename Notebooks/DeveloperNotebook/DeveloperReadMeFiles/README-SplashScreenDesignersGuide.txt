#-----------------------------------------------------------
#"Time-stamp: <06/01/2015  7:48:18 AM rsg>"
#-----------------------------------------------------------

======= File: $README-SplashScreenDesignersGuide.txt =======

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode 8-/16-color (xterm-family) & non-color
   (vt100-family) terminals and terminal emulators.

   You can find this and other files in the following
   Toolkit subdirectories:

   <Your Working Repository>
   (e.g. "Technical_Preview") 
     |
     +-- ["$Notebooks"]
     |     |
     |     +-- ["Engineering-Documents"]
     |           |
     |           +-- ["MS-Excel-Files"]
     |                 |
     |                 +-- "SplashScreenDesignerGuide.xls"
     |
     +-- "MANIFEST_TREE.txt"

===================== TABLE OF CONTENTS ====================

1. Sample Layout

2. Layout Procdure

======================= SAMPLE LAYOUT ======================

1. Sample Layout
 
     1.1 For "abundant" screen size (60+ column x 42+ row)
         displays:
 
         a. Trademark (60+ column x 10 row)
         b. Copyright (60+ column x 18 row)
         c. License   (60+ column x 14 row)
 
     1.2 For "usable" screen size  (60+ column x 32+ row)
         displays:
 
         a. Copyright (60+ column x 18 row)
         b. License   (60+ column x 14 row)
 
     1.3 For "minimal" screen size  (60+ column x 6 row)
         displays:
 
         a. Notice    (60+ column x 6 row)
 
     1.4 For" unusable" screen size  (59- column x 5- row)
         displays:
 
         a. Program error log file.(59- column x 4- row)
 
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789
   ========================= Trademark ========================
 
  0
  1   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
  2   | ts | Wx |     with Python-based
  3   +----+----+        Command Line Interface (CLI)
  4   | G T U I |     and "wxPython"-style, "nCurses"-based
  5   +---------+        Graphical-Text User Interface (GUI)
  6
  7   Get that cross-platform, pixel-mode "wxPython" feeling
  8   on character-mode terminals and terminal emulators.
  9
 
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789
   ========================= Copyright ========================
 
  0
  1      "tsWxGTUI_PyVx", v0.0.0 (pre-alpha build 11/28/2014)
  2
  3      Author(s): Richard S. Gordon
  4
  5      Copyright (c) 2010-2014 Richard S. Gordon,
  6                              a.k.a Software Gadgetry
  7                             (formerly TeamSTARS),
  8                    All rights reserved.
  9      GNU General Public License (GPL), Version 3,
 10                  29 June 2007
 11      GNU Free Documentation License (GFDL) 1.3,
 12                  3 November 2008
 13
 14      Each third-party component is subject to its
 15      copyright holder's designated copyright and
 16      license notices.
 17
 
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789
   ========================== License =========================
 
  0
  1   The "tsWxGTUI_PyVx" Toolkit and its third-party compo-
  2   nents are distributed as free and open source software.
  3   You may use, modify and redistribute it only under the
  4   terms and conditions set forth in the "COPYRIGHT.txt"
  5   and "LICENSE.txt" files located in direcory
  6   "./tsWxGTUI/tsDocCLI/UsageTermsAndConditions".
  7
  8   The "tsWxGTUI_PyVx" Toolkit and its third-party compo-
  9   nents are distributed in the hope that they will be
 10   useful, but WITHOUT ANY WARRANTY; WITHOUT EVEN THE
 11   IMPLIED WARRANTY OF MERCHANTABILITY OR FITNESS FOR
 12   A PARTICULAR PURPOSE.
 13
 
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789
   ========================== Notice ==========================
 
  0
  1   The Terms & Conditions which permit YOUR use, modifica-
  2   tion and redistribution of the "tsWxGTUI_PyVx" Toolkit
  3   may be found in the file "NOTICES.txt" located in the
  4   "./tsWxGTUI_PyVx/tsDocCLIUsageTermsAndConditions"
  5   directory.
  6

===================== LAYOUT PROCEDURE =====================

2. Layout Procdure

   2.1 For each developer-sandbox and site_package:

   2.2 Find file "tsCxGlobals" and Update to reflect recent
       changes to authors, credits, licenses, and notices
       associated with any enhancements and bug fixes.

       HINT:

           Locations should appear in "MANIFEST_TREE.txt"

   2.3 Find and run file "test_TermsAndConditions.py"

       HINT:

           Locations should appear in "MANIFEST_TREE.txt"

   2.4 Update file "test_TermsAndConditions.xls"

   2.5 Repeat steps 2.2-2.5 for next developer-sandbox and
       site_package until the required information is both
       aesthetically pleasing and fits the associated cate-
       gory of display screen size.

======================= End-Of-File ========================
