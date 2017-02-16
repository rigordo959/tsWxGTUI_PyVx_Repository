#-----------------------------------------------------------
#"Time-stamp: <12/18/2016  2:51:17 PM rsg>"
#-----------------------------------------------------------

================= File: README_Manifest.txt ================

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

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./tsWxGTUI_PyVx/Documents".

========================= MANIFEST =========================

Each release of the TeamSTARS "tsWxGUI_PyVx" Toolkit has
a release number suffix (such as "-0.0.0").

1. Toolkit Subdirectories

   The downloaded release file is a container of one or more
   Toolkit subdirectories.

   Excerpt From:

      http://wiki.python.org/moin/Python2orPython3

   "Should I use Python 2 or Python 3 for my development
   activity?

   What are the differences?

   Short version: Python 2.x is legacy, Python 3.x is the
   present and future of the language.

   Python 3.0 was released in 2008. The final 2.x version
   2.7 release came out in mid-2010, with a statement of
   extended support for this end-of-life release. The 2.x
   branch will see no new major releases after that. 3.x
   is under active development and has already seen over
   five years of stable releases, including version 3.3
   in 2012 and 3.4 in 2014. This means that all recent
   standard library improvements, for example, are only
   available by default in Python 3.x.

   Guido van Rossum (the original creator of the Python
   language) decided to clean up Python 2.x properly,
   with less regard for backwards compatibility than is
   the case for new releases in the 2.x range. The most
   drastic improvement is the better Unicode support (with
   all text strings being Unicode by default) as well as
   saner bytes/Unicode separation.

   Besides, several aspects of the core language (such as
   print and exec being statements, integers using floor
   division) have been adjusted to be easier for newcomers
   to learn and to be more consistent with the rest of the
   language, and old cruft has been removed (for example,
   all classes are now new-style, "range()" returns a memory
   efficient iterable, not a list as in 2.x)."

   1.1 Subdirectory ["tsWxGUI_Py2x"]

       Contains source code implemented in the second
       generation Python programming language.

       Each supports Python 2.4.1 - 2.7.9. It is possible
       to backport to older Python versions with loss of
       some functionality and convenience.

       The popularity and wide availability of Python 2.x
       and its standard Python 2to3 utility makes this the
       natural baseline source code version.

   1.2 Subdirectories ["tsWxGUI_Py3x"]

       Contains source code implemented in the third
       generation Python programming language.

       Each supports Python 3.0.0 - 3.4.3. It is possible
       to port to newer Python versions with gain of
       some functionality and convenience.

       The growing popularity and limited availability of
       Python 3x, and the absence of a 3to2 utility, made
       this the logical "port" of the baseline Python 2x
       source code version.

2. Toolkit Working Repository

   Presuming that Toolkit release recipients will develop
   Toolkit application programs for subsequent release, it
   is suggested that recipients emulate the Toolkit Author's
   working software repository.

   This tactic minimizes duplication of files, directories
   and effort. It facilitates use of file comparison and
   merge tools such as GNU's "Diffutils" and Deltopia's
   "DeltaWalker" to merge updates from the Python 2.x baseline
   source code into older, previously debugged Python 3.x
   source code thereby avoiding a translation with Python's
   "2to3" utility and manual debugging of the previously
   fixed translation issues.

   The following organization charts depicts both standard
   and optional features.

      --------------------------------------------------------
      Key:

         [] -- Denotes a Directory containing one or more
               Directories and/or Files.

         "" -- Denotes Name of a Directory or File.

         +  -- Denotes an organizational branch relationship.

         |  -- Denotes a organizational hierarchy relationship.

         :  -- Denotes an optional or temporary organizational
               relationship.
      --------------------------------------------------------

   2.1 Toolkit Genealogy

       The following chart depicts the lines of descent or
       development for multiple Python programming lanuage
       generations.
 

       <Your Working Repository>
       (e.g. "Technical_Preview") 
         |
         |  Working repository containing directories and
         |  files to be packaged into downloadable "tarball"
         |  and/or "zip" files via the commands:
         |
         |  a) "setup_Technical_Preview_tar_file.sh";
         |
         |  b) "setup_Technical_Preview_zip_file.sh";
         |
         |  c) "python setup.py sdist" (under development).
         |
         +-- ["tsWxGTUI_PyVx"]
         |     |
         |     |  The TeamSTARS "tsWxGTUI_PyVx" Toolkit
         |     |  documentation and source code for the
         |     |  multi-generation Python programming
         |     |  language release distribution.
         |     |
         |     +-- ["Documents"]
         |     |     |
         |     |     |  Deliverable Toolkit software documentation
         |     |     |  is written text that accompanies computer
         |     |     |  software. It either explains how it operates
         |     |     |  or how to use it, and may mean different
         |     |     |  things to people in different roles.
         |     |     |
         |     |     |  Types of software documentation include:
         |     |     |
         |     |     |  a) Requirements - Statements that identify
         |     |     |     attributes, capabilities, characteristics,
         |     |     |     or qualities of a system. This is the
         |     |     |     foundation for what shall be or has been
         |     |     |     implemented.
         |     |     |
         |     |     |  b) Architecture/Design - Overview of software.
         |     |     |     Includes relations to an environment and
         |     |     |     construction principles to be used in design
         |     |     |     of software components.
         |     |     |
         |     |     |  c) Technical - Documentation of code, algorithms,
         |     |     |     interfaces, and APIs.
         |     |     |
         |     |     |  d) End user - Manuals for the end-user, system
         |     |     |     administrators and support staff.
         |     |     |
         |     |     +-- ["ManPages"]
         |     |     |     |
         |     |     |     |  Deliverable Toolkit manual pages are a form
         |     |     |     |  of online software documentation usually found
         |     |     |     |  on a Unix or Unix-like operating system. Topics
         |     |     |     |  covered include computer programs (including
         |     |     |     |  library and system calls), formal standards
         |     |     |     |  and conventions, and even abstract concepts.
         |     |     |     |  A user may NOT invoke a man page by issuing the
         |     |     |     |  man command.
         |     |     |     |
         |     |     |     |  A user may display a man page by issuing the
         |     |     |     |  less <man document file> command.
         |     |     |     |
         |     |     |     +--["tsManPagesLibCLI"]
         |     |     |     +--["tsManPagesLibGUI"]
         |     |     |     +--["tsManPagesTestsLibCLI"]
         |     |     |     +--["tsManPagesTestsLibGUI"]
         |     |     |     +--["tsManPagesToolsCLI"]
         |     |     |     +--["tsManPagesToolsGUI"]    (Future)
         |     |     |     +--["tsManPagesToolsLibCLI"]
         |     |     |     +--["tsManPagesToolsLibGUI"] (Future)
         |     |     |     +--["tsManPagesUtilities"]   (Future)
         |     |     |
         |     |     +-- ["wxPython-2.8.9.2-docs"]
         |     |     |
         |     |     |     The TeamSTARS "tsWxGTUI_PyVx" Toolkit emulates a
         |     |     |     character-mode compatible subset of the pixel-mode
         |     |     |     "wxPython" 2.8.9.2 API.
         |     |     |
         |     |     |     Archive copies of documentation files and direc-
         |     |     |     tories, in HTML format, for version 2.8.9.2 of
         |     |     |     "wxPython" and "wxWidgets" published by Julian
         |     |     |     Smart, Robert Roebling et al. The documentation
         |     |     |     is now obsolete and only version 2.8.12 is avail-
         |     |     |     able on-line.
         |     |     |
         |     |     +-- ["wxPython-3.0.2.0-docs"]
         |     |     |
         |     |     |     The TeamSTARS "tsWxGTUI_PyVx" Toolkit emulates a
         |     |     |     character-mode compatible subset of the pixel-mode
         |     |     |     "wxPython" 2.8.9.2 API.
         |     |     |
         |     |     |     For those interested in upgrading it to emulate
         |     |     |     the latest version:
         |     |     |
         |     |     |     Archive copies of documentation files and direc-
         |     |     |     tories, in HTML format, for version 3.0.2.0 of
         |     |     |     "wxPython" and "wxWidgets" published by Julian
         |     |     |     Smart, Robert Roebling et al. The documentation
         |     |     |     is available on-line.
         |     |
         |     +-- ["Python-2x"]
         |     |     |
         |     |     +-- Deliverable Release for 2nd generation
         |     |         Python with single-level packages and
         |     |         import via manual static path generation.
         |     | 
         |     |         Release for subsequent upgrades to 2nd
         |     |         generation Python (beginning end-of-life
         |     |         with only new bug-fix updates but no more
         |     |         new feature enhancement upgrades).
         |     | 
         |     |         Release of "tsWxGTUI_Py2x" as one of the
         |     |         installed site-packages occurs via the
         |     |         command "python2 setup.py install".
         |     |
         |     +-- ["Python-3x"]
         |           |
         |           +-- Deliverable Release for 3rd generation
         |               Python with single-level packages and
         |               import via manual static path generation.
         |
         |               Release created via port from 2nd to 3rd
         |               generation Python.
         |
         |               Release for subsequent upgrades to 3rd
         |               generation Python (feature enhancement
         |               upgrades and bug-fix updates).
         | 
         |               Release of "tsWxGTUI_Py3x" as one of the
         |               installed site-packages occurs via the
         |               command "python3 setup.py install".
         |
         +-- "MANIFEST.in"
         |
         |    Deliverable File inclusion criteria list.
         |
         +-- "MANIFEST_template.in"
         |
         |    Deliverable Generic file inclusion criteria list
         |    template for any Python version-specific TeamSTARS
         |    "tsWxGTUI_PyVx" Toolkit.
         |
         +-- "MANIFEST_TREE.html"
         |
         |    Non-Deliverable Diagram (Multi-Level Org Chart)
         |    depicting the hierarchical relationship between files
         |    in the release, in Hypertext Markup Language format.
         |
         |    Diagram created via Command "./MANIFEST_TREE.sh".
         |
         +-- "MANIFEST_TREE.sh"
         |
         |    Deliverable POSIX-style Command Line Interface shell
         |    script to generate diagrams depicting the hierarchical
         |    relationship between files in the release
         |    ("MANIFEST_TREE.html" and "MANIFEST_TREE.txt").
         |
         +-- "MANIFEST_TREE.txt"
 
              Non-Deliverable Diagram (Multi-Level Org Chart)
              depicting the hierarchical relationship between
              files in the release, in Plain Text format.

              Diagram created via Command "./MANIFEST_TREE.sh".

   2.2 Individual Sub-Project Python Working Repository

       The following chart depicts the lines of descent or
       development for a single Python programming lanuage
       generation.

       ["tsWxGUI_Py2x"] or ["tsWxGUI_Py3x"]
         |
         +-- ["Documents"]
         |     |
         |     +-- ["ManPages"]
         |     |     |
         |     |     |  Deliverable Toolkit manual pages are a form
         |     |     |  of online software documentation usually found
         |     |     |  on a Unix or Unix-like operating system. Topics
         |     |     |  covered include computer programs (including
         |     |     |  library and system calls), formal standards
         |     |     |  and conventions, and even abstract concepts.
         |     |     |  A user may NOT invoke a man page by issuing the
         |     |     |  man command.
         |     |     |
         |     |     |  A user may display a man page by issuing the
         |     |     |  less <man document file> command.
         |     |     |
         |     |     +--["tsManPagesLibCLI"]
         |     |     +--["tsManPagesLibGUI"]
         |     |     +--["tsManPagesTestsLibCLI"]
         |     |     +--["tsManPagesTestsLibGUI"]
         |     |     +--["tsManPagesToolsCLI"]
         |     |     +--["tsManPagesToolsGUI"]    (Reserved for Future Use)
         |     |     +--["tsManPagesToolsLibCLI"]
         |     |     +--["tsManPagesToolsLibGUI"] (Reserved for Future Use)
         |     |     +--["tsManPagesUtilities"]   (Reserved for Future Use)
         |
         +--["tsDemoArchive"]
         |     :
         |     :   Deliverable known Working backup copies of Demo, Test
         |     :   & Tool Applications
         |
         +--["tsLibCLI"]
         |     :
         |     :   Deliverable known Working library of Toolkit Building
         |     :   Block components for Command Line Interface.
         |
         +--["tsLibGUI"]
         |     :
         |     :   Deliverable known Working library of Toolkit Building
         |     :   Block components for wxPython-style, character-mode
         |     :   Graphical User Interface.
         |
         +--["tsTestsLibCLI"]
         |     :
         |     :   Deliverable known Working application program tests
         |     :   for library of those Toolkit Building Block components
         |     :   associated with Command Line Interface.
         |
         +--["tsTestsLibGUI"]
         |     :
         |     :   Deliverable known Working application program tests
         |     :   for library of those Toolkit Building Block components
         |     :   associated with wxPython-style, character-mode
         |     :   Graphical User Interface.
         |
         +--["tsTestsToolsLibCLI"]
         |     :
         |     :   Deliverable known Working application program tests
         |     :   for library of those Tool Building Block components
         |     :   associated with Command Line Interface.
         |
         +--["tsTestsToolsLibGUI"]
         |     :
         |     :   Deliverable known Working application program tests
         |     :   for library of those Tool Building Block components
         |     :   associated with wxPython-style, character-mode
         |     :   Graphical User Interface.
         |
         +--["tsToolsCLI"]
         |     :
         |     :   Deliverable known Working application Tool programs
         |     :   associated with Command Line Interface.
         |
         +--["tsToolsGUI"]
         |     :
         |     :   Deliverable known Working application Tool programs
         |     :   associated with wxPython-style, character-mode
         |     :   Graphical User Interface. (Future)
         |
         +--["tsUtilities"]
         |     :
         |     :   Deliverable known Working computer administration
         |     :   utilities associated with Command Line Interface.
         |     :   (Future)
         |
         :
         +--["logs"]
         :     :
         :     :   Non-Deliverable Diagnostic Run Time Directories
         :     :   & Files generated during execution of Toolkit
         :     :   application programs.
         :     :
         :     +--["2014-12-28-at-16-19-31"]
         :     :      |
         :     :      +-- "PlatformRunTimeEnvironment.log"
         :     :      +-- "test_tsCxGlobals.log"
         :     :
         :     +--["2014-12-29-at-05-33-35"]
         :     :      |
         :     :      +-- "debug_via_tsru.log"
         :     :      +-- "DisplayConfiguration.log"
         :     :      +-- "PlatformRunTimeEnvironment.log"
         :     :      +-- "Redirected-stdout.log"
         :     :      +-- "TerminalRunTimeEnvironment.log"
         :     :      +-- "test_tsWxBoxSizer.log"
         :     :
         :     +--["bmp"]
         :            |
         :            +--["README_BMP.txt"]
         :            +--["SplashScreen-[80x50_VT100]-cygwin_nt-6.1.bmp"]
         :            +--["SplashScreen-[80x50_XTERM]-cygwin_nt-6.1.bmp"]
         |
         +-- "__init__.py"
         :
         :   Non-deliverable, user-installed Demo, Test & Tool Applications

3. Toolkit "as-published" Manifest

   Toolkit release recipients will find the "as-published"
   "MANIFEST.txt" file in the "SoftwareGadgetry_PyPI"
   directory as depicted above.

   The "MANIFEST.in" file identifies which directories and
   file types are to be packaged by the "setup.py sdist"
   command.

4. Toolkit "with recipient changes" Manifest

   The "MANIFEST.in" can be modified and the "MANIFEST.sh"
   shell script can be run to update the "MANIFEST.txt" file
   to release "with recipient changes".

======================= End-Of-File ========================
