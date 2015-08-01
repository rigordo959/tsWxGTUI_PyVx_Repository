#-----------------------------------------------------------
#"Time-stamp: <06/09/2015  1:43:32 PM rsg>"
#-----------------------------------------------------------

============== File: README-tsWxGTUI_PyVx.txt =============

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode 8-/16-color (xterm-family) & non-color
   (vt100-family) terminals and terminal emulators.

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./tsWxGTUI_PyVx/Documents".

===================== TABLE OF CONTENTS ====================

1. Release Distribution Nominclature

2. Engineering Contents and Organization Overview

3. Sdist, Build & Install Contents & Organization Overview

============= RELEASE DISTRIBUTION NOMINCLATURE ============

1. Release Distribution Nominclature

   Each Python version-specific TeamSTARS "tsWxGTUI_PyVx"
   Toolkit is downloaded (as either a compressed, "tarball"
   or "zip" file) from the Python Package Index, a reposi-
   tory of software for the Python programming lanuage.

   The "tarball" or "zip" file name is composed of three
   components:

   <Release Name>_<Python Type>-<Major.Minor.BugFix Number>:

   1.1 Release Name:

       "tsWxGTUI"

   1.2 Python Type:

       1.2.1 "_Py3x" - Identifies third generation Python language
                       syntax associated with Python 3.2.0-3.5.x.

                       Current stable release is Python 3.4.2
                       as of 13 Oct. 2014.

                       Latest release candidate is Python 3.4.3rc1
                       as of 8 Feb. 2015.

                       Latest alpha release is Python 3.5.0a1
                       as of 8 Feb. 2015.

                       NOTE: The Python Software Foundation has
                             designated Python 3.x to be under
                             active development.

                             There will be ongoing feature enhance-
                             ment upgrades.

                             There will be a limited number of
                             bug fix updates to earlier Python
                             3.x releases.

       1.2.2 "_Py2x" - Identifies second generation Python language
                       syntax associated with Python 2.6.6-2.7.x.

                       Current stable release is Python 2.7.9
                       as of 10 Dec. 2014.

                       NOTE: The Python Software Foundation has
                             designated Python 2.x to be in its
                             End-Of-Life stage.

                             There will be no more feature
                             enhancement upgrades (back-ported
                             from Python 3x).

                             There will a limited number of
                             bug fix updates to Python 2.7.

       1.2.3 "_Py1x" - Identifies first generation Python language
                       syntax associated with Python 1.0.0-1.6.x.

                       Final stable release is Python 1.6.1
                       as of 25 Feb. 2001.

                       NOTE: The Python Software Foundation has
                             designated Python 1.x to be in its
                             End-Of-Life stage.

                             There will be no more feature
                             enhancement upgrades (back-ported
                             from Python 2x).

                             There will be no more bug fix
                             updates to Python 1.6.

                       It is NOT recommended for use (unless one abso-
                       lutely must support a computer platform whose
                       Python 1x interpreter and operating system
                       software cannot be upgraded) because:

                       a) It "seems" to support only modules imported
                          from a single level (monolithic) directory
                          structure. Relevant documentation for this
                          long obsolete Python generation is scarce.

                          Limited functionality was achieved during
                          experimentation by the replacement of the
                          multi-level (hierarchical) 2x-style file
                          system by a single level (monolithic) one,
                          in order to workaround countless module
                          import issues. The workaround involved
                          eliminating the importing (implicit on
                          package directory access) of and reference
                          to numerous nested "__init__.py" files in
                          the original multi-level directory struc-
                          ture.

                       b) To support the Command Line Interface,
                          will require back-porting of several
                          Global Module Index components (optparse,
                          platform and textwrap) from Python 2x.

                       c) It does NOT support the Graphical-style
                          User Interface because it would require
                          extensive effort to back-port additional
                          Global Module Index components.

                          It is unlikely that the 1x "Curses" module
                          supports recent terminal emulators in its
                          TermCap (Curses) or TermInfo (nCurses/
                          _curses) database (such as xterm-16color
                          and xterm-256color).

                          The 1x "Curses" module does not support the
                          "_curses" module which supplies mouse posi-
                          tion and button definitions.

   1.3 Major-Minor-BugFix Number:

       1.3.1 "0.0.0" Identifies first major, pre-alpha stage, release

       1.3.2 "1.0.0" Identifies first major, production stage, release

       1.3.3 "3.2.1" Identifies first bug fix, for second func-
                     tional enhancement for third major production
                     release

   1.4 Release File Type:

       The files and directories/folders associated with the
       TeamSTARS "tsWxGTUI_PyVx" Toolkit may be released in
       any of several archive file formats, with or without
       data compression. The actual format depends on the type
       of computer platform operating system used to package
       the release:

       1.4.1 Microsoft Windows platforms (such as Windows XP, Vista,
             7, 8, 8.1 and 10) support a "zip" archive file format
             such as:

             Multi-generation Python programming language release
             sdist-stage source code and documentation products:

                "tsWxGTUI_PyVx-3.2.1.zip"    (106,632,641 bytes)

             Single-generation Python programming language release
             sdist-stage source code products:

                "tsWxGTUI_Py3x-3.2.1.zip"
                "tsWxGTUI_Py2x-3.2.1.zip"    (  2,251,821 bytes)
                "tsWxGTUI_Py1x-3.2.1.zip"

       1.4.2 POSIX-compatible platforms (such as Linux, Unix and
             Cygwin, the free, Linux-like plug-in for Microsoft
             Windows) support a "tar" archive file format and
             optional "gz" compression such as:

             Multi-generation Python programming language release
             sdist-stage source code and documentation products:

                "tsWxGTUI_PyVx-3.2.1.tar"    (292,465,280 bytes)
                "tsWxGTUI_PyVx-3.2.1.tar.gz" (104,901,314 bytes)
                "tsWxGTUI_PyVx-3.2.1.tgz"    (104,901,314 bytes)

             Single-generation Python programming language release
             sdist-stage source code products:

                "tsWxGTUI_Py3x-3.2.1.tar.gz"
                "tsWxGTUI_Py2x-3.2.1.tar.gz" (  1,769,671 bytes)
                "tsWxGTUI_Py1x-3.2.1.tar.gz"

             Single-generation Python programming language release
             build-stage products:

                "tsWxGTUI_Py2x build"        ( 10,992,421 bytes)
                "tsWxGTUI_Py2x.egg-info"     (     75,456 bytes)

             Single-generation Python programming language release
             install-stage products:

                "tsWxGTUI_Py2x build"        ( 10,992,421 bytes)
                "tsWxGTUI_Py2x.egg-info"     (     75,456 bytes)

                "tsWxGTUI_Py2x dist"         (  4,036,623 bytes)
                "tsWxGTUI_Py2x-0.0.0-py2.7.egg"
                                             ( 16,266,200 bytes)

======== ENGINEERING CONTENTS AND ORGANIZATION OVERVIEW ========

2. Engineering Contents and Organization Overview

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit has been engineered,
   developed and tested for use with the second generation
   Python programming language (Python 2x), the most popular
   and widely available generation.

   In recognition of the growing popularity and availability
   of the third generation Python programming language (Python
   3x), and as a convenience to Toolkit users, a Python 3x port
   of the Python 2x Toolkit has also been developed and tested.

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit author(s) recommend
   keeping the engineering documentation and source code for
   the multi-generation Python Toolkits together only on
   those computer systems used for Toolkit development and
   maintenance. This minimizes file editing and duplication.
   It also minimizes debugging and troubleshooting. This
   ultimately maximizes productivity.

   Source code for the multi-generation Python Toolkit dis-
   tribution is created in a working repository directory
   named:

      "/WR/SoftwareGadgetry-PyPI/tsWxGTUI_PyVx"

   It is released on a POSIX-compatible system (such as
   Linux, Unix or Cygwin, the free Linux-like Plug-in for
   Microsoft Windows), as a single compressed "tarball"
   file.

   For the initial (pre-alpha) release (0.0.0), the "tar-
   ball" file is named:

      "tsWxGTUI_PyVx-0.0.0.tar.gx".

   The Engineering Contents and Organization is depicted
   (details include access permissions, file size and modi-
   fication date and time) in the following toolkit working
   repository files:

      "./tsWxGTUI_PyVx/MANIFEST_TREE.txt"
      "./tsWxGTUI_PyVx/MANIFEST_TREE.html"

   An overview, annotated with design guidelines, is depicted
   in the following organization chart:

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
 
      ["/WR/SoftwareGadgetry-PyPI"]
           |
           |  Working repository containing directories and
           |  files to be packaged into downloadable "tarball"
           |  and/or "zip" files.
           |
           +-- ["tsWxGTUI_PyVx"]
           |     |
           |     |  The TeamSTARS "tsWxGTUI_PyVx" Toolkit docu-
           |     |  mentation and source code for the multi-
           |     |  generation Python programming language
           |     |  release distribution.
           |     |
           |     +-- ["Documents"]
           |     |     |
           |     |     |  Toolkit documents replicated and organized
           |     |     |  for use by trainees, software developers,
           |     |     |  system operators, software distributors,
           |     |     |  system engineers and system troubleshooters.
           |     |     |
           |     |     +-- ["tsDevelopers"]
           |     |     |     |
           |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- "$GETTING_STARTED.txt"
           |     |     |     +-- "$README.txt"
           |     |     |     +-- "$README-DeveloperReadMeFiles.txt"
           |     |     |     +-- "$README-DeveloperTutorialFiles.txt"
           |     |     |     +-- "$README-HowToUseAndModify.txt"
           |     |     |     +-- "$README-InstallAndRedistribute.txt"
           |     |     |     +-- "$README-tsDemoArchive.txt"
           |     |     |     +-- "$README-tsLibCLI.txt"
           |     |     |     +-- "$README-tsLibGUI.txt"
           |     |     |     +-- "$README-tsToolsCLI.txt"
           |     |     |     +-- "$README-tsToolsGUI.txt"
           |     |     |     +-- "$README-tsUtilities.txt"
           |     |     |     +-- "$README-tsWxGTUI_PyVx.txt"
           |     |     |     |
           |     |     |     +-- "__init__.py"
           |     |     |     |
           |     |     |     +-- "BUGS.txt"
           |     |     |     +-- "CHANGE_LOG.txt"
           |     |     |     +-- "CONFIGURE.txt"
           |     |     |     +-- "DEMO.txt"
           |     |     |     +-- "FAQ.txt"
           |     |     |     +-- "INSTALL.txt"
           |     |     |     +-- "OPERATE.txt"
           |     |     |     +-- "THANKS.txt"
           |     |     |     +-- "TO-DO.txt"
           |     |     |     +-- "TROUBLESHOOT.txt
           |     |     |
           |     |     +-- ["tsDistributors"]
           |     |     |     |
           |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- "$GETTING_STARTED.txt"
           |     |     |     +-- "$README.txt"
           |     |     |     |
           |     |     |     +-- "__init__.py"
           |     |     |     |
           |     |     |     +-- "AUTHORS.txt"
           |     |     |     +-- "BUGS.txt"
           |     |     |     +-- "CHANGE_LOG.txt"
           |     |     |     +-- "CONFIGURE.txt"
           |     |     |     +-- "COPYING.txt"
           |     |     |     +-- "COPYRIGHT.txt"
           |     |     |     +-- "CREDITS.txt"
           |     |     |     +-- "DEMO.txt"
           |     |     |     +-- "FAQ.txt"
           |     |     |     +-- "INSTALL.txt"
           |     |     |     +-- "LICENSE.txt"
           |     |     |     +-- "MANIFEST_README.txt"
           |     |     |     +-- "NEWS.txt"
           |     |     |     +-- "NOTICES.txt"
           |     |     |     +-- "OPERATE.txt"
           |     |     |     +-- "THANKS.txt"
           |     |     |     +-- "TO-DO.txt"
           |     |     |     +-- "TROUBLESHOOT.txt
           |     |     |
           |     |     +-- ["tsOperators"]
           |     |     |     |
           |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     |  Contains Application Programming
           |     |     |     |  Interface documents produced via PyDoc
           |     |     |     |  from source code.
           |     |     |     |
           |     |     |     |  ManPages can be built for new or updated
           |     |     |     |  source code by running the appropriate
           |     |     |     |  "buildManPage" script in the directory
           |     |     |     |  ["tsUtilities"].
           |     |     |     |
           |     |     |     +-- ["tsManPagesLibCLI"]
           |     |     |     |
           |     |     |     |  Contains Application Programming
           |     |     |     |  Interface documents produced via PyDoc
           |     |     |     |  from source code in "tsLibCLI".
           |     |     |     |
           |     |     |     +-- ["tsManPagesLibGUI"]
           |     |     |     |
           |     |     |     |  Contains Application Programming
           |     |     |     |  Interface documents produced via PyDoc
           |     |     |     |  from source code in "tsLibGUI".
           |     |     |     |
           |     |     |     +-- ["tsManPagesTestsCLI"]
           |     |     |     |
           |     |     |     |  Contains System Operator help
           |     |     |     |  documents produced via "--help"
           |     |     |     |  option when launching the CLI test
           |     |     |     |  applications in ["tsDemoArchive"].
           |     |     |     |
           |     |     |     +-- ["tsManPagesTestsGUI"]
           |     |     |     |
           |     |     |     |  Contains System Operator help
           |     |     |     |  documents produced via "--help"
           |     |     |     |  option when launching the GUI test
           |     |     |     |  applications in ["tsDemoArchive"].
           |     |     |     |
           |     |     |     +-- ["tsManPagesToolsCLI"]
           |     |     |     |
           |     |     |     |  Contains Application Programming
           |     |     |     |  Interface document produced via "--help"
           |     |     |     |  option when launching the CLI tool
           |     |     |     |  applications in ["tsDemoArchive"].
           |     |     |     |
           |     |     |     +-- ["tsManPagesToolsGUI"]
           |     |     |     |
           |     |     |     |  Currently has no content.
           |     |     |     |
           |     |     |     |  Contains Application Programming
           |     |     |     |  Interface document produced via "--help"
           |     |     |     |  option when launching the GUI tool
           |     |     |     |  applications in ["tsDemoArchive"].
           |     |     |     |
           |     |     |     +-- "$GETTING_STARTED.txt"
           |     |     |     +-- "$README.txt"
           |     |     |     |
           |     |     |     +-- "__init__.py"
           |     |     |     |
           |     |     |     +-- "BUGS.txt"
           |     |     |     +-- "CHANGE_LOG.txt"
           |     |     |     +-- "DEMO.txt"
           |     |     |     +-- "FAQ.txt"
           |     |     |     +-- "OPERATE.txt"
           |     |     |
           |     |     +-- ["tsTroubleshooters"]
           |     |     |     |
           |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- "$GETTING_STARTED.txt"
           |     |     |     +-- "$README.txt"
           |     |     |     +-- "__init__.py"
           |     |     |     +-- "AUTHORS.txt"
           |     |     |     +-- "BUGS.txt"
           |     |     |     +-- "CHANGE_LOG.txt"
           |     |     |     +-- "CONFIGURE.txt"
           |     |     |     +-- "COPYING.txt"
           |     |     |     +-- "COPYRIGHT.txt"
           |     |     |     +-- "CREDITS.txt"
           |     |     |     +-- "DEMO.txt"
           |     |     |     +-- "FAQ.txt"
           |     |     |     +-- "INSTALL.txt"
           |     |     |     +-- "LICENSE.txt"
           |     |     |     +-- "MANIFEST_README.txt"
           |     |     |     +-- "NEWS.txt"
           |     |     |     +-- "NOTICES.txt"
           |     |     |     +-- "OPERATE.txt"
           |     |     |     +-- "THANKS.txt"
           |     |     |     +-- "TO-DO.txt"
           |     |     |     +-- "TROUBLESHOOT.txt
           |     |     |
           |     |     +-- ["tsEngineering"]
           |     |     |     |
           |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- ["Adobe-PDF-Files"]
           |     |     |     |     |
           |     |     |     |     +-- ["How to Configure Remote Access"]
           |     |     |     |     +-- ["How to Engineer tsWxGTUI_PyVx"]
           |     |     |     |     +-- ["How to Implement with Python"]
           |     |     |     |
           |     |     |     +-- ["ASCII-Text-Files"]
           |     |     |     |     |
           |     |     |     |     +-- ["README_BMP.txt"]
           |     |     |     |
           |     |     |     +-- ["JPEG-Image-Files"]
           |     |     |     |     |
           |     |     |     |     +-- ["tsScreenShots"]
           |     |     |     |     |
           |     |     |     |     +-- selected block diagram images
           |     |     |     |
           |     |     |     +-- ["MS-Access-Files"]
           |     |     |     |     |
           |     |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- ["MS-Excel-Files"]
           |     |     |     |     |
           |     |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- ["MS-PowerPoint-Files"]
           |     |     |     |     |
           |     |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- ["MS-Visio-Files"]
           |     |     |     |     |
           |     |     |     |     +-- [To-Be-Determined]
           |     |     |     |
           |     |     |     +-- ["MS-Word-Files"]
           |     |     |     |     |
           |     |     |     |     +-- ["MIL-STD-498 Templates"]
           |     |     |     |     +-- ["Words to Engineer tsWxGTUI_PyVx"]
           |     |     |     |           |
           |     |     |     |           |   Files generated with AuthorIT 5
           |     |     |     |           |   Reusable Content Manager
           |     |     |     |           |
           |     |     |     |           +-- Editable source for Adobe PDF
           |     |     |     |
           |     |     |     +-- "$GETTING_STARTED.txt"
           |     |     |     +-- "$README-tsEngineering.txt"
           |     |     |
           |     |     +-- "$README.txt"
           |     |     +-- "$README-tsWxGTUI_PyVx.txt"
           |     |     +-- "$GETTING_STARTED.txt"
           |     |     +-- "$TermsAndConditions.txt"
           |     |
           |     +-- ["Python"]
           |     |     |
           |     |     |  Placeholder for Toolkit experimenting.
           |     |     |
           |     |     +-- ["tsWxGTUI_PyPx"]
           |     |     |
           |     |     +-- "$README.txt"
           |     |     +-- "MANIFEST.in"
           |     |     +-- "MANIFEST_TREE.html"
           |     |     +-- "MANIFEST_TREE.sh"
           |     |     +-- "MANIFEST_TREE.txt"
           |     |     +-- "__init__.py"
           |     |     +-- "say_hello.py"
           |     |     +-- "setup.py"
           |     |
           |     +-- ["Python-1x"]
           |     |     |
           |     |     |  Placeholder for future back-port from 2nd
           |     |     |  to 1st (beyond end-of-life with neither new
           |     |     |  feature enhancement upgrades or new bug-fix
           |     |     |  updates) generation Python.
           |     |     |
           |     |     +-- ["tsWxGTUI_Py1x"]
           |     |     |
           |     |     +-- "$README.txt"
           |     |     +-- "MANIFEST.in"
           |     |     +-- "MANIFEST_TREE.html"
           |     |     +-- "MANIFEST_TREE.sh"
           |     |     +-- "MANIFEST_TREE.txt"
           |     |     +-- "__init__.py"
           |     |     +-- "say_hello.py"
           |     |     +-- "setup.py"
           |     |
           |     +-- ["Python-2x"]
           |     |     |
           |     |     |  Release for 2nd generation Python.
           |     |     |
           |     |     |  Release for subsequent upgrades to 2nd
           |     |     |  (beginning end-of-life with only new bug-fix
           |     |     |  updates but no more new feature enhancement
           |     |     |  upgrades) generation Python.
           |     |     |
           |     |     +-- ["tsWxGTUI_Py2x"]
           |     |     |     |
           |     |     |     +-- ["tsDemoArchive"]
           |     |     |     |
           |     |     |     |  Contains those application programs which
           |     |     |     |  demonstrate or verify the proper operation
           |     |     |     |  of the TeamSTARS "tsWxGTUI" Toolkit.
           |     |     |     |
           |     |     |     +-- ["tsLibCLI"]
           |     |     |     |
           |     |     |     |  Contains general-purpose, re-usable
           |     |     |     |  building blocks supporting Command
           |     |     |     |  Line Interface.
           |     |     |     |
           |     |     |     |  Also contains Theme-based configuration
           |     |     |     |  settings for customizing Command Line
           |     |     |     |  Interface.
           |     |     |     |
           |     |     |     +-- ["tsLibGUI"]
           |     |     |     |
           |     |     |     |  Contains general-purpose, re-usable
           |     |     |     |  building blocks supporting character-mode,
           |     |     |     |  "wxPython"-style Graphical-style User
           |     |     |     |  Interface.
           |     |     |     |
           |     |     |     |  Also contains Theme-based configuration
           |     |     |     |  settings for customizing Graphical-style
           |     |     |     |  User Interface.
           |     |     |     |
           |     |     |     +-- ["tsToolsCLI"]
           |     |     |     |
           |     |     |     |  Contains software development CLI tools
           |     |     |     |  to monitor and improve productivity.
           |     |     |     |
           |     |     |     +-- ["tsToolsGUI"]
           |     |     |     |
           |     |     |     |  Currently has no content.
           |     |     |     |
           |     |     |     |  Contains software development GUI tools
           |     |     |     |  to monitor and improve productivity.
           |     |     |     |
           |     |     |     +-- ["tsUtilities"]
           |     |     |     |
           |     |     |     |  Contains CLI shell and Python scripts to
           |     |     |     |  monitor and modify hardware and software
           |     |     |     |  features.
           |     |     |     |
           |     |     |     +-- selected files from ["tsDemoArchive"]
           |     |     |
           |     |     +-- "$README.txt"
           |     |     +-- "MANIFEST.in"
           |     |     +-- "MANIFEST_TREE.html"
           |     |     +-- "MANIFEST_TREE.sh"
           |     |     +-- "MANIFEST_TREE.txt"
           |     |     +-- "__init__.py"
           |     |     +-- "say_hello.py"
           |     |     +-- "setup.py"
           |     |
           |     +-- ["Python-3x"]
           |     |     |
           |     |     |  Release for port from 2nd to 3rd
           |     |     |  generation Python.
           |     |     |
           |     |     |  Release for subsequent upgrades
           |     |     |  (feature enhancements) and updates
           |     |     |  (bug-fixes) to 3rd generation Python.
           |     |     |
           |     |     +-- ["tsWxGTUI_Py3x"]
           |     |     |     |
           |     |     |     +-- ["tsDemoArchive"]
           |     |     |     |
           |     |     |     |  Contains those application programs which
           |     |     |     |  demonstrate or verify the proper operation
           |     |     |     |  of the TeamSTARS "tsWxGTUI" Toolkit.
           |     |     |     |
           |     |     |     +-- ["tsLibCLI"]
           |     |     |     |
           |     |     |     |  Contains general-purpose, re-usable
           |     |     |     |  building blocks supporting Command
           |     |     |     |  Line Interface.
           |     |     |     |
           |     |     |     |  Also contains Theme-based configuration
           |     |     |     |  settings for customizing Command Line
           |     |     |     |  Interface.
           |     |     |     |
           |     |     |     +-- ["tsLibGUI"]
           |     |     |     |
           |     |     |     |  Contains general-purpose, re-usable
           |     |     |     |  building blocks supporting character-mode,
           |     |     |     |  "wxPython"-style Graphical-style User
           |     |     |     |  Interface.
           |     |     |     |
           |     |     |     |  Also contains Theme-based configuration
           |     |     |     |  settings for customizing Graphical-style
           |     |     |     |  User Interface.
           |     |     |     |
           |     |     |     +-- ["tsToolsCLI"]
           |     |     |     |
           |     |     |     |  Contains software development CLI tools
           |     |     |     |  to monitor and improve productivity.
           |     |     |     |
           |     |     |     +-- ["tsToolsGUI"]
           |     |     |     |
           |     |     |     |  Currently has no content.
           |     |     |     |
           |     |     |     |  Contains software development GUI tools
           |     |     |     |  to monitor and improve productivity.
           |     |     |     |
           |     |     |     +-- ["tsUtilities"]
           |     |     |     |
           |     |     |     |  Contains CLI shell and Python scripts to
           |     |     |     |  monitor and modify hardware and software
           |     |     |     |  features.
           |     |     |     |
           |     |     |     +-- selected files from ["tsDemoArchive"]
           |     |     |
           |     |     +-- "$README.txt"
           |     |     +-- "MANIFEST.in"
           |     |     +-- "MANIFEST_TREE.html"
           |     |     +-- "MANIFEST_TREE.sh"
           |     |     +-- "MANIFEST_TREE.txt"
           |     |     +-- "__init__.py"
           |     |     +-- "say_hello.py"
           |     |     +-- "setup.py"
           |     |
           |     +-- ["Python-4x"]
           |           |
           |           |  Placeholder for future port from 3rd
           |           |  to 4th generation Python.
           |           |
           |           +-- ["tsWxGTUI_Py4x"]
           |           |
           |           +-- "$README.txt"
           |           +-- "MANIFEST.in"
           |           +-- "MANIFEST_TREE.html"
           |           +-- "MANIFEST_TREE.sh"
           |           +-- "MANIFEST_TREE.txt"
           |           +-- "__init__.py"
           |           +-- "say_hello.py"
           |           +-- "setup.py"
           |
           +-- "MANIFEST.in"
           |
           |    File inclusion criteria list.
           |
           +-- "MANIFEST_template.in"
           |
           |    Generic file inclusion criteria list template
           |    for any Python version-specific TeamSTARS
           |    "tsWxGTUI_PyVx" Toolkit.
           |
           +-- "MANIFEST_TREE.html"
           |
           |    Diagram (Multi-Level Org Chart) depicting the
           |    hierarchical relationship between files in the
           |    release, in Hypertext Markup Language format.
           |
           +-- "MANIFEST_TREE.sh"
           |
           |    POSIX-style Command Line Interface shell script to
           |    generate diagrams depicting the hierarchical relation-
           |    ship between files in the release ("MANIFEST_TREE.html"
           |    and "MANIFEST_TREE.txt").
           |
           +-- "MANIFEST_TREE.txt"
 
                Diagram (Multi-Level Org Chart) depicting the
                hierarchical relationship between files in the
                release, in Plain Text format.

== SDIST, BUILD & INSTALL CONTENTS & ORGANIZATION OVERVIEW =

3. Sdist, Build & Install Contents & Organization Overvie

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit has been engineered
   to support the legacy version of the Python "Distutils".

      --------------------------------------------------------
      NOTES:

      a) For an introduction to the legacy version of the
         Python "Distutils", please see:

            https://docs.python.org/3.5/distutils/index.html

      b) The Toolkit includes application-specific versions
         of the Python 2x & 3x "Distutils" script named
         "setup.py".
 
      c) The command "python setup.py sdist" can be used to
         create an application-specific source code distri-
         bution.

      d) The command "python setup.py build" can be used to
         create an application-specific "tarball" or "zip"
         File and an associated Python "egg" file.

         Python "egg" files are a way of bundling additional
         information with a Python project, that allows the
         project's dependencies to be checked and satisfied
         at runtime, as well as allowing projects to provide
         plugins for other projects. There are several bin-
         ary formats that embody eggs, but the most common
         is '.egg' zipfile format, because it's a convenient
         one for distributing projects. All of the formats
         support including package-specific data, project-
         wide metadata, C extensions, and Python code.

      e) The command "python setup.py install" can be used to
         install an application-specific Toolkit with other
         site-packages associated with the Python interpreter.

         CAUTION: Since this may interfere with further
                  Toolkit debugging, an install should only
                  occur after the Toolkit has been formally
                  qualified for use by system operators.
      --------------------------------------------------------
 
   3.1 The command "python setup.py sdist" can be used to
       create a Python generation (Px denoting 2x or 3x)
       specific and release specific (0.0.0) source code
       distribution, when executed in the directory
       ["Python-Px"], in a subdirectory named "dist" which
       contains:

       a) A "tarball" file named "tsWxGTUI_PyPx-0.0.0.tar.gz"

          or

       b) A "zip" file named "tsWxGTUI_PyPx-0.0.0.zip".

       The "tarball" and "zip" files contain a directory
       named ["tsWxGTUI_PyPx-0.0.0"]. It contains the
       following:

       ["tsWxGTUI_PyPx-0.0.0"]
         |
         +-- ["tsWxGTUI_PyPx"]
         |     |
         |     +-- ["tsDemoArchive"]
         |     +-- ["tsLibCLI"]
         |     +-- ["tsLibGUI"]
         |     +-- ["tsToolsCLI"]
         |     +-- ["tsToolsGUI"]
         |     +-- ["tsUtilities"]
         |     |
         |     +-- selected files from ["tsDemoArchive"]
         |
         +-- ["tsWxGTUI_PyPx.egg-info"]
         |     |
         |     +-- "PKG-INFO"
         |     +-- "SOURCES.txt"
         |     +-- "dependency_links.txt"
         |     +-- "requires.txt"
         |     +-- "top_level.txt"
         |
         +-- "$README.txt"
         +-- "MANIFEST.in"
         +-- "MANIFEST_TREE.html"
         +-- "MANIFEST_TREE.sh"
         +-- "MANIFEST_TREE.txt"
         +-- "__init__.py"
         +-- "say_hello.py"
         +-- "setup.cfg"
         +-- "setup.py"

   3.2 The command "python setup.py build", when executed in
       the directory named ["Python-Px"] (where Px denotes
       2x or 3x), can be used to prepare the following:

       ["Python-Px"]
         |
         +-- ["build"]
         |     |
         |     +-- ["lib"]
         |     |     |
         |     |     +-- ["tsWxGTUI_PyPx"]
         |     |
         |     +-- ["scripts-P.x"]
         |           |
         |           +-- "say_hello.py"
         |
         +-- ["tsWxGTUI_PyPx.egg-info"]

   3.3 The command "python setup.py install", when executed in
       the directory named ["Python-Px"] (where Px denotes
       2x or 3x), can be used to install the Toolkit with
       other site-packages associated with the Python inter-
       preter.

       Setup.py installs the Toolkit in the following platform
       host (Cygwin, Linux, Mac OS X, Microsoft Windows, Unix)
       and Python version (XY or X.Y) specific locations:
 
       3.3.1 Cygwin (a free Linux-like Command Line Interface
             and GNU toolkit add-on to Microsoft Windows from
             Red Hat)
 
             Built-in <Path>:
                /cygwin/lib
 
             User Add-on <Path>:
                /cygwin/lib

             The following diagram depicts the Cygwin instal-
             lation for Python 2.7:

             ["/cygwin/lib"]
               |
               +-- ["python2.7"]
                     |
                     +-- ["site-packages"]
                           |
                           +-- ["tsWxGTUI_Py2x-0.0.0-py2.7.egg"]
                                 |
                                 +-- ["EGG-INFO"]
                                 |     |
                                 |     +-- ["scripts"]
                                 |     |
                                 |     +-- "dependency_links.txt"
                                 |     +-- "not-zip-safe"
                                 |     +-- "PKG-INFO"
                                 |     +-- "requires.txt"
                                 |     +-- "SOURCES.txt"
                                 |     +-- "top_level.txt"
                                 |
                                 +-- ["tsWxGTUI_Py2x"]

             The following diagram depicts the Cygwin instal-
             lation for Python 3.2:

             ["/cygwin/lib"]
               |
               +-- ["python3.2"]
                     |
                     +-- ["site-packages"]
                           |
                           +-- ["tsWxGTUI_Py3x-0.0.0-py3.2.egg"]
                                 |
                                 +-- ["EGG-INFO"]
                                 |     |
                                 |     +-- ["scripts"]
                                 |     |
                                 |     +-- "dependency_links.txt"
                                 |     +-- "not-zip-safe"
                                 |     +-- "PKG-INFO"
                                 |     +-- "requires.txt"
                                 |     +-- "SOURCES.txt"
                                 |     +-- "top_level.txt"
                                 |
                                 +-- ["tsWxGTUI_Py3x"]
 
       3.3.2 GNU/Linux(CentOS, OpenSuSE, Scientific and Ubuntu)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y
 
       3.3.3 Mac OS X (10.3 Panther - 10.10 Yosemite)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y
 
       3.3.4 Microsoft Windows (XP, Vista, 7, 8, 8.1, 10)
 
             Built-in <Path>:
                /PythonXY
 
             User Add-on <Path>:
                /PythonXY
 
       3.3.5 Unix (FreeBSD/PC-BSD and OpenIndiana/OpenSolaris)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y

======================= End-Of-File ========================

