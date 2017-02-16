#-----------------------------------------------------------
#"Time-stamp: <12/18/2016  2:53:03 PM rsg>"
#-----------------------------------------------------------

======== File: README-SplashScreenDesignersGuide.txt =======

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling on
   platforms with:

   * 64-bit processors, nCurses 6.x, 64-bit Python 3.6.x or
     later GUI applications and character-mode 256-/16-/8-
     color (xterm-family) and non-color (vt100-family)
     terminals and terminal emulators.

   * 32-bit processors, nCurses 6.x/5.x, 32-bit Python 3.5.2
     or earlier GUI applications and character-mode 16-/8-
     color (xterm-family) and non-color (vt100-family)
     terminals and terminal emulators.

   <Your Working Repository>
   (e.g. "tsWxGTUI_PyVx_Repository") 
     |
     +-- ["Documents"]
     |
     +-- ["ManPages"]
     |
     +-- ["Notebooks"]
     |     |
     |     +-- ["DeveloperNotebook"]
     |     |
     |     +-- ["EngineeringNotebook"]
     |     |     |
     |     |     +-- ["MS-Excel-Files"]
     |     |           |
     |     |           +-- "SplashScreenDesignerGuide.xls"
     |     |
     |     +-- ["ProjectNotebook"]
     |     |     |
     |     |     +-- "PROJECT-01-Title_Page.txt"
     |     |     +-- "PROJECT-02-Table_Of_Contents.txt"
     |     |     +-- "PROJECT-03-Purpose.txt"
     |     |     +-- "PROJECT-04-Goals.txt"
     |     |     +-- "PROJECT-05-Non-Goals.txt"
     |     |     +-- "PROJECT-06-Design_Strategy.txt"
     |     |     +-- "PROJECT-07-Design_Architecture.txt"
     |     |     +-- "PROJECT-08-Release_Strategy.txt"
     |     |     +-- "PROJECT-09-Software_Configuration_Management.txt"
     |     |     +-- "PROJECT-10-Software_Repository.txt"
     |     |     +-- "PROJECT-11-Features.txt"
     |     |     +-- "PROJECT-12-Capabilities.txt"
     |     |     +-- "PROJECT-13-Limitations.txt"
     |     |     +-- "PROJECT-14-Reference_Documents.txt"
     |     |     +-- "PROJECT-15-Built-in_Documentation_Symbols.txt"
     |     |     +-- "PROJECT-16-Applicaion_Launch_Modules.txt"
     |     |     +-- "PROJECT-17-Directory_and_Import_Guide.txt"
     |     |     +-- "PROJECT-18-Site-Package_Install_Guide.txt"
     |     |     +-- "PROJECT-19-Developer-Sandbox_Install_Guide.txt"
     |     |     +-- "PROJECT-20-Splash_Screen_Guide.txt"
     |     |     |
     |     |     +-- "README5-ProjectNotebook.txt"
     |     |
     |     +-- "README5-Notebooks.txt"
     |
     +-- ["SourceDistributions"]
     |
     +-- "README.txt"

===================== TABLE OF CONTENTS ====================

1. Jargon

2. Sample Layout

3. Layout Procdure

=========================== JARGON =========================

1. Jargon

   * Splash Screen --- a graphical control element consist-
     ing of window containing an image, a logo and the cur-
     rent version of the software. A splash screen usually
     appears while a program is launching. Splash screens
     may cover the entire screen, or simply a rectangle
     near the center of the screen.

     The Splash Screen enabling or disabling is an option
     within ./tsLibGUI/tsWxGlobals.py.

     The Splash Screen is constructed and displayed by
     ./tsLibGUI/tsWxGraphicalTextUserInterface.py.

   * Masthead --- a statement printed in all issues of a
     newspaper, magazine, or the like, usually on the
     editorial page, giving the publication's name, the
     names of the owner and staff, etc. The contents
     are defined within ./tsLibCLI/tsCxGlobals.py.

   * Trademark --- a proprietary term that is usually reg-
     istered with the Patent and Trademark Office to assure
     its exclusive use by its owner. It is a distinctive
     mark or feature particularly characteristic of or
     identified with a person or thing. A Masthead could be
     Trademarked. The contents are defined within
     ./tsLibCLI/tsCxGlobals.py.

   * Copyright --- a form of protection provided by the laws
     of the United States for "original works of authorship",
     including literary, dramatic, musical, architectural,
     cartographic, choreographic, pantomimic, pictorial,
     graphic, sculptural, and audiovisual creations.
     "Copyright" literally means the right to copy but has
     come to mean that body of exclusive rights granted by
     law to copyright owners for protection of their work.
     Copyright protection does not extend to any idea,
     procedure, process, system, title, principle, or dis-
     covery. Similarly, names, titles, short phrases,
     slogans, familiar symbols, mere variations of typo-
     graphic ornamentation, lettering, coloring, and list-
     ings of contents or ingredients are not subject to
     copyright. The contents are defined within
     ./tsLibCLI/tsCxGlobals.py.

   * Copyright Notice --- consists of three elements. They
     are the "c" in a circle (©), the year of first publi-
     cation, and the name of the owner of copyright. A
     copyright notice is no longer legally required to
     secure copyright on works first published on or after
     March 1, 1989, but it does provide legal benefits. The
     contents are defined within ./tsLibCLI/tsCxGlobals.py.

   * License --- allows an intellectual property rights
     holder (the licensor) to make money from a creative
     work by charging a user (the licensee) for product
     use. Licenses protect proprietary rights in things
     such as software and other computer products. The
     contents are defined within ./tsLibCLI/tsCxGlobals.py.

   * Notice --- the legal concept describing a requirement
     that a party be aware of legal process affecting their
     rights, obligations or duties. The contents
     are defined within ./tsLibCLI/tsCxGlobals.py.

======================= SAMPLE LAYOUT ======================

2. Sample Layout

     A splash screen is a window with a thin border. It dis-
     plays a "bitmap" (text) describing your application.
     The splash screen is shown during application initial-
     ization. The application then either explicitly de-
     stroys it or lets it time-out.
 
     2.1 For "abundant" screen size (60+ column x 42+ row)
         displays:
 
         a. Trademark (60+ column x 10 row)
         b. Copyright (60+ column x 18 row)
         c. License   (60+ column x 14 row)
 
     2.2 For "usable" screen size  (60+ column x 32+ row)
         displays:
 
         a. Copyright (60+ column x 18 row)
         b. License   (60+ column x 14 row)
 
     2.3 For "minimal" screen size  (60+ column x 6 row)
         displays:
 
         a. Notice    (60+ column x 6 row)
 
     2.4 For" unusable" screen size  (59- column x 5- row)
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

3. Layout Procdure

   3.1 For each developer-sandbox and site_package:

   3.2 Find file "tsCxGlobals" and Update to reflect recent
       changes to authors, credits, licenses, and notices
       associated with any enhancements and bug fixes.

       HINT:

           Locations should appear in "MANIFEST_TREE.txt"

   3.3 Find and run file "test_TermsAndConditions.py"

       HINT:

           Locations should appear in "MANIFEST_TREE.txt"

   3.4 Update file "test_TermsAndConditions.xls"

   3.5 Repeat steps 2.2-2.5 for next developer-sandbox and
       site_package until the required information is both
       aesthetically pleasing and fits the associated cate-
       gory of display screen size.

======================= End-Of-File ========================
