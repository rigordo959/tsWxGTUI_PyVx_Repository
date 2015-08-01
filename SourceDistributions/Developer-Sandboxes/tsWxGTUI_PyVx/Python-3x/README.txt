#-----------------------------------------------------------
#"Time-stamp: <07/23/2015  7:43:05 AM rsg>
#-----------------------------------------------------------

===================== File: README.txt =====================

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
         |
         +-- ["Documents"]

===================== TABLE OF CONTENTS ====================

1. Welcome

   1.1 Application Programs
   1.2 Development Systems
   1.3 Embedded Systems
   1.4 What should you do to get started?

2. Release Distribution Identification

   2.1 <Release Name>:
   2.2 <Python Version>:
   2.3 <Major.Minor.BugFix Number>:

3. Release Distribution File Type

   3.1 "Zip" File for Microsoft Windows
   3.2 "Tar" File for Cygwin, GNU/Linux and Unix

4. Source Distribution Type

   4.1 Installable Site-Packages

   4.2 Experimental Developer-Sandboxes

5. Sdist, Build & Install Contents & Organization

========================== WELCOME =========================

1. The TeamSTARS "tsWxGTUI_PyVx" Toolkit provides a collec-
   tion of building-block components, tools, utilities, and
   tests. It has been designed to facilitate the creation,
   enhancement, troubleshooting, maintenance and support of
   application programs that are suitable for embedded sys-
   tems.

   1.1 Application Programs

       Automation, communication, control, diagnostic, in-
       strumentation and simulation application programs
       typically require an "operator-friendly" Command Line
       Interface (CLI) or a Graphical-style User Interface
       (GUI) that can be monitored and controlled locally or
       remotely.

   1.2 Development Systems

        General-purpose systems used for development of:

        a. software (source code for libraries of scripts,
           building blocks, tools and applications)

        b. documentation (presentations, training material,
           programmer reference manuals etc.)

        Such general-purpose desktop, laptop and workstation
        computer systems typically have upgradable or at least
        sufficient processing, memory, communication, input/
        output and file storage resources. They typically have
        computer terminal interface hardware suitable for a
        pixel-mode display that also supports character-mode. 

   1.3 Embedded Systems

        Mission-critical systems used to monitor and control:

        a. operating mode (setup, diagnostic/test, monitor
           only, manual, automatic etc.)

        b. setpoints (startup/shutdown sequences, tempera-
           tures, pressures, motion speed, fluid/gas flows,
           lighting brightness/contrast, sound loudness/tonal
           balance, detector sensitivity etc.)

        c. commercial, industrial, manufacturing, medical or
           military equipment.

        Such application-specific computer systems typically have
        upgradable but limited processing, memory, communication,
        input/output and file storage resources. Some may have
        character-mode hardware only suitable for their operating
        system's command line console.

   1.4 What should you do to get started?

       Browse through the following information located in
       the directory "./tsWxGTUI_PyVx/Documents". It provid-
       es an overview of the Toolkit distribution and its
       contents:

       1.4.1 What is the TeamSTARS "tsWxGTUI_PyVx" Toolkit?

             a) "README1-Introduction.txt"
             b) "README2-Repository.txt"
             c) "README3-Documents.txt"
             d) "README4-ManPages.txt"
             e) "README5-Notebooks.txt"
             f) "README6-SourceDistribution.txt"
             g) "README7-DeveloperSandboxes.txt"
             h) "README8-SitePackages.txt"
             i) "README9-KeyboardMouseInput.txt"

       1.4.2 How to prepare your computer(s) for use with the
             Toolkit? 

             a) "GETTING_STARTED.txt"

       1.4.3 How can you become familiar with the features,
             look and feel of the Toolkit? 

             a) "DEMO.txt"
             b) "TROUBLESHOOT.txt"

       1.4.4 What are the currently known Toolkit limitations,
             bugs and update roadmap? 

             a) "BUGS.txt"
             b) "TO-DO.txt"

       1.4.5 Experience the features, look and feel of the
             Toolkit by running through the scenarios pre-
             sented in DEMO.txt file and browsing through
             the Python source code for the associated
             application programs and building blocks.


                                           Richard S. Gordon
                                SoftwareGadgetry@comcast.net

============= RELEASE DISTRIBUTION NOMINCLATURE ============

2. Release Distribution Nominclature

   Multiplr Python version-specific TeamSTARS "tsWxGTUI_PyVx"
   Toolkits are downloaded (as either a compressed, "tarball"
   or "zip" file) from the Python Package Index, a reposi-
   tory of software for the Python programming lanuage.

   The "tarball" or "zip" file name is composed of three
   components:

   2.1 <Release Name>:

       "tsWxGTUI_PyVx"   - Designates the entire collection of
                           source code and tools that may be
                           downloaded.

       "tsWxGTUI_Py3x"   - Designates a collection of third
                           generation Python language source
                           code and tools for use with evolv-
                           ing hardware and software technology
                           that is growing in popularity and
                           availability.

       "tsWxGTUI_Py2x"   - Designates a collection of second
                           generation Python language source
                           code and tools for use with mature
                           hardware and software technology
                           that is popular and readily avail-
                           able.

       "tsWxGTUI_Py1x"   - Designates a collection of first
                           generation Python language source
                           code and tools for use with out-
                           dated hardware and software tech-
                           nology that is no longer popular
                           and/or readily available.

   2.2 <Python Version>:

       2.2.1 "Python-3x" - Identifies third generation Python
                           language. Syntax is associated with
                           Python 3.0.0-3.5.x.

                       Current stable release is Python 3.4.3
                       as of 25 Feb. 2015.

                       Latest (beta) release is Python 3.5.0b2
                       as of 1 June 2015.

                       NOTE: The Python Software Foundation has
                             designated Python 3.x to be under
                             active development.

                             There will be ongoing feature enhance-
                             ment upgrades.

                             There will be a limited number of
                             bug fix updates to earlier Python
                             3.x releases.

       2.2.2 "Python-2x" - Identifies second generation Python
                           language. Syntax is associated with
                           Python 2.0.0-2.7.x.

                       Current stable release is Python 2.7.10
                       as of 23 May 2015.

                       NOTE: The Python Software Foundation has
                             designated Python 2.x to be in its
                             End-Of-Life stage.

                             There will be no more feature
                             enhancement upgrades (back-ported
                             from Python 3x).

                             There will a limited number of
                             bug fix updates to Python 2.7.x.

       2.2.3 "Python-1x" - Reserved for Future use.
                           Identifies first generation Python
                           language. Syntax is associated with
                           Python 1.0.0-1.6.x.

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
                          may require back-porting of several
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

   2.3 <Major.Minor.BugFix Number>:

       2.3.1 "0.0.0" Identifies first major, pre-alpha stage release.

       2.3.2 "0.0.1" Identifies first major, pre-alpha stage release
                     with its first bug fix. 

       2.3.3 "0.1.0" Identifies first major, pre-alpha stage release
                     with its first functional enhancement.

       2.3.4 "1.0.0" Identifies first major, production stage release.

       2.4.5 "3.2.1" Identifies third major production release includ-
                     ing its second functional enhancement with its
                     first bug fix. 

3. Release Distribution File Type

   The files and directories/folders associated with the
   TeamSTARS "tsWxGTUI_PyVx" Toolkit may be released in
   any of several archive file formats, with or without
   data compression. The actual format depends on the type
   of computer platform operating system used to package
   the release:

   3.1 "Zip" File for Microsoft Windows

       Microsoft Windows platforms (such as Windows XP, Vista,
       7, 8, 8.1 and 10 Technical Preview) support a "zip"
       archive file format such as:

       Multi-generation Python programming language release
       sdist-stage source code and documentation products:

           "tsWxGTUI_PyVx-3.2.1.zip"    (106,632,641 bytes)

       Single-generation Python programming language release
       sdist-stage source code products:

           "tsWxGTUI_Py3x-3.2.1.zip"
           "tsWxGTUI_Py2x-3.2.1.zip"    (  2,251,821 bytes)
           "tsWxGTUI_Py1x-3.2.1.zip"

   3.2 "Tar" File for Cygwin, GNU/Linux and Unix

       POSIX-compatible platforms (such as Linux, Unix and
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

4. Source Distribution Type

   4.1 Installable Site-Packages

       A "site-package" designates an author-qualified collec-
       tion of source code and tools that is usable (in the
       manner of packages built-into Python's Global Module Index)
       only after its installation via a python version-specific
       "python setup.py install" commanand.  

       Each site-package consists of a single layer of one or
       more building-block library packages with an empty
       package "__init__.py" file.

       From "http://stackoverflow.com/questions/448271/
                    what-is-init-py-for":

           "The __init__.py files are required to make Python
           treat the directories as containing packages; this
           is done to prevent directories with a common name,
           such as string, from unintentionally hiding valid
           modules that occur later on the module search path.
           In the simplest case, __init__.py can just be an
           empty file, but it can also execute initialization
           code for the package or set the __all__ variable,
           described later." 

   4.2 Experimental Developer-Sandboxes

       A "developer-sandbox" designates a debuggable collection
       of prototype source code and tools. Once debugged, tested
       and pre-qualified, a copy of the sandbox can be "readily"
       re-organized (via creating directories and moving files)
       and transformed (via editing import statements) into an
       installable site-package.

       NOTICE: To retain recent Site-Package feature enhance-
               ments and bug fixes, developers should ensure
               that they have been or will be back-ported into
               the Sandbox before it is used to prototype any
               new features of significant complexity.

       Each developer-sandbox consists of a multi-level hier-
       archy of building-block library packages with individual
       "__init__.py" files that automatically generate the full
       import path based upon package topology and import depen-
       dancy relationships.

============= RELEASE CONTENTS AND ORGANIZATION ============

3. Release Contents and Organization

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
   maintenance. This minimizes file editing and copying.
   It also minimizes debugging and troubleshooting. This
   ultimately maximizes productivity.

   Source code for the multi-generation Python Toolkit dis-
   tribution is created in a working repository directory
   named:

      "/WR/tsWxGTUI_PyVx_Repository/tsWxGTUI_PyVx"

   It is released on a POSIX-compatible system, as a single
   compressed "tarball" file suitable for installation and use
   on Linux, Unix or Microsoft Windows (with Cygwin, the free
   Linux-like Plug-in from Red Hat).

   For the initial (pre-alpha) release (0.0.0), the "tar-
   ball" file is named:

      "tsWxGTUI_PyVx-0.0.0.tar.gx".

   The Release Contents and Organization is depicted
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
               hierarchy relationship.

        CLI -- Denotes those Toolkit components associated
               with the text-mode, Command Line-style User
               Interface. A user may then enter a command
               as a line of text, via a keyboard. In response,
               the Toolkit outputs a scrolling sequence of
               text lines to the display terminal.

               This low-level interface, though somewhat user-
               friendly, is relatively difficult to use. It is
               typically used during computer hardware and soft-
               ware installation, configuration and trouble-
               shooting.

               It requires accurate typing/reading skills and
               mastery of a complex vocabulary and syntax fea-
               turing both required and optional parameters.

        GUI -- Denotes those Toolkit components associated
               with the Graphical-style User Interface. The
               Toolkit outputs text characters to various row
               and column positions on a display terminal.
               This organizes side-by-side and/or overlapping
               areas for user input (via keyboard and/or mouse)
               and for output (via as color or non-color dis-
               play terminal).

               This high-level, user-friendly interface is
               relatively easy to use. It is typically used
               during operation of a computerized Supervisory
               Control and Data Acquisition (SCADA) system.

               It requires basic typing/reading skills and
               familiarity with proper SCADA system operation.
      --------------------------------------------------------

       <Your Working Repository>
       (e.g. "tsWxGTUI_PyVx_Repository") 
         |
         |  Working repository containing directories and
         |  files to be packaged into downloadable "tarball"
         |  and/or "zip" files via the setup shell scripts
         |  at the bottom of this diagram.
         |
         +-- ["Documents"] (Original)
         |     |
         |     |  This directory contains a collection of files
         |     |  which provide the Toolkit recipient with an
         |     |  understanding of the purpose, goals & capabil-
         |     |  ities, non-goals & limitations, terms & condi-
         |     |  tions and procedures for installing, operating,
         |     |  modifying and redistributing the Toolkit. 
         |     |
         |     +-- "README.txt"
         |     +-- "README1-Introduction.txt"
         |     +-- "README2-Repository.txt"
         |     +-- "README3-Documents.txt"
         |     +-- "README4-ManPages.txt"
         |     +-- "README5-Notebooks.txt"
         |     +-- "README6-SourceDistributions.txt"
         |     +-- "README7-DeveloperSandboxes.txt"
         |     +-- "README8-SitePackages.txt"
         |     +-- "README9-KeyboardMouseInput.txt"
         |     +-- "GETTING_STARTED.txt"
         |     +-- "DEMO.txt"
         |
         +-- ["ManPages"] (Original)
         |     |
         |     |  Deliverable Toolkit manual pages are a
         |     |  form of online software documentation
         |     |  usually found on a Unix or Unix-like
         |     |  operating system.
         |     |
         |     |  Topics covered include computer programs
         |     |  (including library and system calls),
         |     |  formal standards and conventions, and even
         |     |  abstract concepts.
         |     |
         |     |  Unlike their Unix or Unix-like counterparts,
         |     |  a Toolkit user may NOT invoke a man page by
         |     |  issuing the "man command". Instead, a user
         |     |  mmust display a man page by issuing the
         |     |  "less <man document file>" command.
         |     |
         |     +-- ["tsManPagesLibCLI"]
         |     +-- ["tsManPagesLibGUI"]
         |     +-- ["tsManPagesTestsLibCLI"]
         |     +-- ["tsManPagesTestsLibGUI"]
         |     +-- ["tsManPagesToolsCLI"]
         |     +-- ["tsManPagesToolsGUI"]     (Future)
         |     +-- ["tsManPagesToolsLibCLI"]
         |     +-- ["tsManPagesToolsLibGUI"]  (Future)
         |     +-- ["tsManPagesUtilitiesCLI"] (Future)
         |     |
         |     +-- "README4-ManPages.txt"
         |
         +-- ["Notebooks"] (Pre-dates Documents)
         |     |
         |     |  Contains a collection of commentaries that
         |     |  express opinions or offerings of explana-
         |     |  tions about events or situations that might
         |     |  be useful to Toolkit installers, developers,
         |     |  operators, troubleshooters and distributors.
         |     |  The documents may be in Application-specific
         |     |  formats (such as Adobe PDF, JPEG Bit-mapped
         |     |  image, LibreOffice, Microsoft Office, plain
         |     |  text).
         |     |
         |     +-- ["DeveloperNotebook"] (Future Original
         |     |     |                    Developer-Sandbox)
         |     |     |
         |     |     |  Contains a collection of:
         |     |     |     API-References-Pixel-Mode-wxPython
         |     |     |     and Developer-ReadMe-Files
         |     |
         |     +-- ["EngineeringNotebook"] (Original Site-Package)
         |     |     |
         |     |     |  Contains a Toolkit User oriented collection of
         |     |     |     ["EngineeringNotebook"] abstracts:
         |     |     |
         |     |     |     Project (purpose,
         |     |     |              goals,
         |     |     |              non-goals,
         |     |     |              features,
         |     |     |              capabilities,
         |     |     |              limitations),
         |     |
         |     +-- ["EngineeringNotebook"] (Future Original
         |     |     |                      Developer-Sandbox)
         |     |     |
         |     |     |  Contains a Toolkit User oriented collection of
         |     |     |     ["EngineeringNotebook"] abstracts:
         |     |     |
         |     |     |     Project (purpose,
         |     |     |              goals,
         |     |     |              non-goals,
         |     |     |              features,
         |     |     |              capabilities,
         |     |     |              limitations),
         |     |     |
         |     |     |  Contains a Toolkit Developer oriented collection of:
         |     |     |
         |     |     |     Project (purpose,
         |     |     |              goals,
         |     |     |              non-goals,
         |     |     |              features,
         |     |     |              capabilities,
         |     |     |              limitations),
         |     |     |
         |     |     |     Plan (software life-cycle),
         |     |     |
         |     |     |     Requirements (purpose,
         |     |     |                   goals,
         |     |     |                   non-goals,
         |     |     |                   features,
         |     |     |                   capabilities,
         |     |     |                   limitations,
         |     |     |                   file system configuration,
         |     |     |                   hardware & software interface,
         |     |     |                   software,
         |     |     |                   system,
         |     |     |                   user configuration options),
         |     |     |
         |     |     |     Design (API emulation strategy, architecture),
         |     |     |
         |     |     |     Implementation (developer-sandbox, site-package),
         |     |     |
         |     |     |     Test (unit, integration, system, acceptance),
         |     |     |
         |     |     |     Marketing (announcement, brochure),
         |     |     |
         |     |     |     Release (introduction,
         |     |     |              release notes,
         |     |     |              software user's manual,
         |     |     |              terms & conditions,
         |     |     |              dictionary),
         |     |     |
         |     |     |     Third-party Resources
         |     |
         |     +-- "README5-Notebooks.txt"
         |
         +-- ["SourceDistributions"] (Original)
         |     |
         |     |  Contains a collection of computer program
         |     |  source code files that the Toolkit recip-
         |     |  ient will need to install, operate, modify
         |     |  and re-distribute the Toolkit.
         |     |
         |     +-- "README6-SourceDistributions.txt"
         |     |
         |     +-- ["Developer-Sandboxes"] (Future Original
         |     |     |                      Pre-dates Site-Packages)
         |     |     |
         |     |     |  A sandbox is a testing environment that iso-
         |     |     |  lates untested code changes and outright
         |     |     |  experimentation from the production environ-
         |     |     |  ment or repository.
         |     |     |
         |     |     +-- ["tsWxGTUI_PyVx"] (Developer-Sandbox)
         |     |           |
         |     |           +-- ["Documents"] (Copy)
         |     |           |
         |     |           +-- ["ManPages"] (Copy)
         |     |           |
         |     |           +-- ["Python-2x"] (Developer-Sandbox)
         |     |           |     |
         |     |           |     +-- ["tsWxGTUI_Py2x"]
         |     |           |
         |     |           +-- ["Python-3x"]  (Developer-Sandbox,
         |     |                 |             Ported from Python-2x)
         |     |                 |
         |     |                 +-- ["tsWxGTUI_Py3x"]
         |     |
         |     +-- ["Site-Packages"] (Original)
         |           |
         |           |  A site-package is the location where third-
         |           |  party packages are installed (i.e., those
         |           |  not part of the core Python distribution).
         |           |  NOTE: That with Linux, Mac OS X and Unix
         |           |  operating systems one must have root priv-
         |           |  ileges to write to that location.
         |           |
         |           +-- ["tsWxGTUI_PyVx"] (Site-Package)
         |                 |
         |                 +-- ["Documents"] (Copy)
         |                 |
         |                 +-- ["ManPages"] (Copy)
         |                 |
         |                 +-- ["Python-2x"] (Site-Package)
         |                 |     |
         |                 |     +-- ["tsWxGTUI_Py2x"]
         |                 |
         |                 +-- ["Python-3x"] (Site-Package,
         |                       |            Ported from Python-2x)
         |                       |
         |                       +-- ["tsWxGTUI_Py3x"]
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
         |
         |    Non-Deliverable Diagram (Multi-Level Org Chart)
         |    depicting the hierarchical relationship between
         |    files in the release, in Plain Text format.
         |
         |    Diagram created via Command "./MANIFEST_TREE.sh".
         |
         +-- "setup_tsWxGTUI_PyVx_Repository_tar_file.sh"
         |
         |    Deliverable POSIX-style Command Line Interface shell
         |    script to generate downloadable "tarball" file.
         |
         +-- "setup_tsWxGTUI_PyVx_Repository_zip_file.sh"
         |
         |    Deliverable POSIX-style Command Line Interface shell
         |    script to generate downloadable "zip" file.
         |
         +-- "README.txt"

====== SDIST, BUILD & INSTALL CONTENTS & ORGANIZATION ======

5. Sdist, Build & Install Contents & Organization

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit has been engineered
   to support the legacy version of the Python "Distutils".

      ------------------------------------------------------
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
      ------------------------------------------------------
 
   5.1 The command "python setup.py sdist" can be used to
       create a Python generation (Vx denoting 2x or 3x)
       specific and release specific (0.0.0) source code
       distribution, when executed in the directory
       ["Python-Vx"], in a subdirectory named "dist" which
       contains:

       a) A "tarball" file named "tsWxGTUI_PyVx-0.0.0.tar.gz"

          or

       b) A "zip" file named "tsWxGTUI_PyVx-0.0.0.zip".

       The "tarball" and "zip" files contain a directory
       named ["tsWxGTUI_PyVx-0.0.0"]. It contains the
       following:

       ["tsWxGTUI_PyVx_Repository-0.0.0"]
         |
         +-- ["tsWxGTUI_PyVx"]
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
         +-- ["tsWxGTUI_PyVx.egg-info"]
         |     |
         |     +-- "PKG-INFO"
         |     +-- "SOURCES.txt"
         |     +-- "dependency_links.txt"
         |     +-- "requires.txt"
         |     +-- "top_level.txt"
         |
         +-- "README.txt"
         +-- "MANIFEST.in"
         +-- "MANIFEST_TREE.html"
         +-- "MANIFEST_TREE.sh"
         +-- "MANIFEST_TREE.txt"
         +-- "__init__.py"
         +-- "say_hello.py"
         +-- "setup.cfg"
         +-- "setup.py"

   5.2 The command "python setup.py build", when executed in
       the directory named ["Python-Vx"] (where Vx denotes
       2x or 3x), can be used to prepare the following:

       ["Python-Vx"]
         |
         +-- ["build"]
         |     |
         |     +-- ["lib"]
         |     |     |
         |     |     +-- ["tsWxGTUI_PyVx"]
         |     |
         |     +-- ["scripts-P.x"]
         |           |
         |           +-- "say_hello.py"
         |
         +-- ["tsWxGTUI_PyVx.egg-info"]

   5.3 The command "python setup.py install", when executed in
       the directory named ["Python-Vx"] (where Vx denotes
       2x or 3x), can be used to install the Toolkit with
       other site-packages associated with the Python inter-
       preter.

       Setup.py installs the Toolkit in the following platform
       host (Cygwin, Linux, Mac OS X, Microsoft Windows, Unix)
       and Python version (XY or X.Y) specific locations:
 
       5.3.1 Cygwin (a free Linux-like Command Line Interface
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
 
       5.3.2 GNU/Linux(CentOS, OpenSuSE, Scientific and Ubuntu)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y
 
       5.3.3 Mac OS X (10.3 Panther - 10.10 Yosemite)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y
 
       5.3.4 Microsoft Windows (XP, Vista, 7, 8, 8.1, 10)
 
             Built-in <Path>:
                /PythonXY
 
             User Add-on <Path>:
                /PythonXY
 
       5.3.5 Unix (FreeBSD/PC-BSD 7, OpenIndiana 151a8
             and OpenSolaris 11)
 
             Built-in <Path>:
                /Library/Python/X.Y
 
             User Add-on <Path>:
                /opt/local/lib/pythonX.Y

======================= End-Of-File ========================

