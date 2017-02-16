#-----------------------------------------------------------
#"Time-stamp: <01/18/2017  8:07:55 AM rsg>
#-----------------------------------------------------------

===================== File: README.txt =====================

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

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit's cross-platform
   Virtual Machine design and implementation supports a broad
   assortment of open and proprietary hardware and software
   platforms.

   You can find this and other plain-text files in the Toolkit
   subdirectory named:

       "./<Toolkit Recipient's Repository>/Documents".

       <Your Working Repository>
       (e.g. "tsWxGTUI_PyVx_Repository") 
         |
         |
         +-- ["Documents"]

===================== TABLE OF CONTENTS ====================

Preface

   A. Software Interface Generator (SWIG)

   B. "nCurses" Library (Enhanced terminal control for
      Unix-like systems, enabling the construction of
      Graphical-style Text User Interface applications)

   C. Python Standard "Curses" Library (Basic Unix
      Capabilities)

   D. Python SWIG "Curses" Library (Enhanced Unix
      Capabilities)

   E. Python SWIG "PDCurses" Library (Emulated-Unix
      Platforms)

1. Introduction

   1.1 Application Programs
   1.2 Embedded Systems
   1.3 Toolkit Components
   1.4 Multi-Project Release
   1.5 What should you do to get started?

2. Release Distribution Identification

   2.1 <Release Name>:
   2.2 <Python Version>:
   2.3 <Major.Minor.BugFix Number>:

3. Release Distribution File Type

   3.1 "Git" Repository Clone "Zip" File
   3.2 "Zip" File for Microsoft Windows
   3.3 "Tar" File for Cygwin, GNU/Linux and Unix

4. Source Distribution Type

   4.1 Installable Site-Packages

   4.2 Experimental Developer-Sandboxes

5. Sdist, Build & Install Contents & Organization

============================= Preface ===========================

Preface

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit is an evolutionary
   upgrade from it predecessor, the TeamSTARS "tsWxGTUI_PyVx"
   Toolkit. It uses the Software Interface Generator (SWIG), a
   software development tool, to introduce new features and
   capabilities.

A. Software Interface Generator (SWIG)

   SWIG is a software development tool that connects software
   libraries written in C and C++ with applications written in a
   variety of high-level programming languages. It is used with
   different types of target languages including common scripting
   languages such as Javascript, Perl, PHP, Python, Tcl and Ruby.
   It is used to create high-level interpreted or compiled
   programming environments, user interfaces, and as a tool for
   testing and prototyping C/C++ software. SWIG is used to parse
   C/C++ interfaces and generate the 'glue code' required for the
   above target languages to call into the C/C++ code.

B. "nCurses" Library (Enhanced terminal control for Unix-like
   systems, enabling the construction of Graphical-style Text
   User Interface applications)

   For many years, the Python Software Foundation supported only
   the Free Software Foundation GNU Project's "ncurses" (new
   curses) library. The library being a free software emulation
   of curses in AT&T Unix System V Release 4.0 (SVr4), and more.
   It uses terminfo format, supports pads and color and multiple
   highlights and forms characters and function-key mapping, and
   has all the other SVr4-curses enhancements over BSD Unix
   curses. SVr4 curses is better known today as X/Open Curses.

   The most recent release introduced support for multi-byte
   unicode and for 64-bit processors (with associated support for
   at least 256 colors).   

C. Python Standard "Curses" Library (Basic Unix Capabilities)

   The Python Standard "Curses" Library module never supported
   all of the available "nCurses" Library Application Programming
   Interface (API) functions. Its API subset only included those
   functions traditionally found in the AT&T Unix System V
   Release 4.0 "Curses" library.

D. Python SWIG "Curses" Library (Enhanced Unix Capabilities)

   SWIG has made it practical to optionally provide the full
   "nCurses" API to users of the "TeamSTARS "tsWxGTUI_PyVx"
   Toolkit.

E. Python SWIG "PDCurses" Library (Emulated-Unix Platforms)
                                   
   For those applications that require it, the "TeamSTARS
   "tsWxGTUI_PyVx" Toolkit can optionally produce the
   'glue code' by which Public Domain Curses ("PDCurses") can
   interface to:

   1. Unix-like systems offering only the AT&T Unix System V
      Release 4.0 Curses API.

   2. Non-Unix systems (such as  DOS, OS/2, Windows, X11 and SDL).
      PDCurses offers Microsoft Windows several API options:

      Requires use of one of the following PDCurses API ports:

      a. SDL (Simple DirectMedia Layer) API

          Simple DirectMedia Layer (SDL) is a cross-platform,
          free and open source multimedia library written in C
          that presents a simple interface to various platforms'
          graphics, sound, and input devices. It is widely used
          due to its simplicity. Over 700 games, 180 applications,
          and 120 demos have been posted on its website.

          SDL has the word "layer" in its title because it is
          actually a wrapper around operating-system-specific
          functions. The main purpose of SDL is to provide a
          common framework for accessing these functions. For
          further functionality beyond this goal, many libraries
          have been created to work on top of SDL. Software
          developers use it to write computer games and other
          multimedia applications that can run on many operating
          systems: Android, iOS, Linux, Mac OS X, Windows and
          other platforms. It manages video, events, digital
          audio, CD-ROM, threads, shared object loading,
          networking and timers.

      b. Win32 API

         An application programming interface designed to use a
         character-mode console. It uses only mono-spaced fonts
         and a limited set of font attributes. Its text rendition
         approximates that of an xterm. 

         It is common to all Microsoft's 32-bit Windows operating
         systems. These currently include: Windows 95, Windows 98,
         Windows NT, Windows CE, Windows 2000, Windows XP,
         Windows 7, Windows 8 and Windows 10.

      c. Win32a API

         An application programming interface designed to use a
         graphical-mode console. It uses Windows GDI instead of
         the console. This lets PDCurses escape the limitations
         of the console, so that it can implement essentially
         everything specified in Curses. (Some of these improve-
         ments have also been applied to PDCurses for X11, SDL,
         etc.)

         It is common to all Microsoft's 32-bit Windows operating
         systems. These currently include: Windows 95, Windows 98,
         Windows NT, Windows CE, Windows 2000, Windows XP,
         Windows 7, Windows 8 and Windows 10.

         The screen shot (at http://www.projectpluto.com/win32a.htm)
         shows some of the things this flavor of PDCurses can do,
         such as display of bold, italic, underlined, overlined,
         dimmed, 'strikeout', blinking text, full RGB colors,
         display of the full range of Unicode, a range of blinking
         cursor styles and blinking text, and fullwidth and combined
         characters. All of this is backward-compatible to the
         original PDCurses specification.

      d. X11 API

         This is a port of PDCurses for X11, aka XCurses. It is
         designed to allow existing curses programs to be re-compiled
         with PDCurses, resulting in native X11 programs.

   SWIG is free software and the code that SWIG generates is
   compatible with commercial and non-commercial projects.

========================== Introduction =========================

1. Introduction

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit is released as Free
   and Open Source Software. You can get all of the source
   code and associated building-blocks, tools, tests, util-
   ities, examples and documentation via the "GitHub" Web-
   based repository hosting service.

   Implemented in both the mature Python 2x and evolving Py-
   thon 3x programming languages, its source code is that
   part of computer software which most users don't ever
   see; it's the part computer programmers manipulate to
   change how a computer "program" or "application" works.

   It has been designed to facilitate the creation, enhance-
   ment, troubleshooting, maintenance, porting and support
   of application programs that are suitable for the moni-
   toring and control of equipment with embedded computer
   systems.

   1.1 Application Programs

       Automation, communication, control, diagnostic, in-
       strumentation and simulation application programs
       typically require an "operator-friendly" Command Line
       Interface (CLI) or a Graphical-style User Interface
       (GUI) that can be monitored and controlled locally or
       remotely.

   1.2 Embedded Systems

        Mission-critical systems for commercial, industrial,
        medical and military applications are typically cus-
        tomized and optimized for a specific use. Unlike
        their general purpose desktop, laptop and workstation
        counterparts, embedded systems typically have limit-
        ed, application-specific processing, memory, commu-
        nication, input/output and file storage resources.
        Some may have character-mode hardware only suitable
        for their operating system's command line console.

   1.3 Toolkit Components

       The component of the Toolkit source code serve two
       distinct roles:

       1.3.1 "Site-Packages"

             The TeamSTARS "tsWxGTUI_PyVx" Toolkit repository
             contains separately installable Python 2x and Python
             3x "site-packages". Each contains on-line documen-
             tation and the appropriate Python version-specific
             source code.

             Local or remote applications that have imported the
             appropriate Python 2x or Python 3x "site-package"
             can be launched from any convenient directory on the
             associated local or remote computer system.

       1.3.2 "Developer-Sandboxes"

             The TeamSTARS "tsWxGTUI_PyVx" Toolkit repository
             contains separate non-installable Python 2x and
             Python 3x "developer-sandboxes" which facilitate:

             a. experimentation, development and troubleshooting
                of Toolkit enhancements and customizations.

             b. porting to other hardware and software platforms.

             Local or remote Python 2x applications can only be
             launched from the associated "tsWxGTUI_Py2x"
             "developer-sandbox" directory.

             Local or remote Python 3x applications can only be
             launched from the associated "tsWxGTUI_Py3x"
             "developer-sandbox" directory.

   1.4 Multi-Project Release

       The two "site-packages" and two "developer-sandboxes" are
       released together so that (despite their Python 2x and
       Python 3x implementation differences) they retain the
       identical Application Programming Interface (API) and
       User Interface (UI) look and feel:

       a. Comand Line User Interface (CLI)

       b. Graphical User Interface (GUI)

   1.5 What should you do to get started?

       Browse through the following information located in
       the directory "./tsWxGTUI_PyVx/Documents". It provid-
       es an overview of the Toolkit distribution and its
       contents:

       1.5.1 What is the TeamSTARS "tsWxGTUI_PyVx" Toolkit?

             a) "README1-Introduction.txt"
             b) "README2-Repository.txt"
             c) "README3-Documents.txt"
             d) "README4-ManPages.txt"
             e) "README5-Notebooks.txt"
             f) "README6-SourceDistribution.txt"
             g) "README7-DeveloperSandboxes.txt"
             h) "README8-SitePackages.txt"
             i) "README9-KeyboardMouseInput.txt"

       1.5.2 How to prepare your computer(s) for use with the
             Toolkit? 

             a) "GETTING_STARTED.txt"

                References citations and commentaries on
                computer jargon and topics associated with:

                "User Interfaces"
                "Operating Systems"
                "Toolkit Development Resources"
                "Python Download Gotchas"
                "wxPython/wxWidgets Development Resources"

       1.5.3 How can you become familiar with the features,
             look and feel of the Toolkit? 

             a) "INSTALL.txt" (includes a concise "Quick Test
                Drive" commentary)

             b) "DEMO.txt" (includes a verbose "Narrated,
                Scripted Demo Test Drive" commentary)

             c) "TROUBLESHOOT.txt" (includes a verbose
                "Insight of the "tsWxGTUI" Toolkit
                Developer(s)" commentary)

       1.5.4 What are the currently known Toolkit limitations,
             bugs and update roadmap? 

             a) "BUGS.txt"
             b) "TO-DO.txt"

       1.5.5 Experience the features, look and feel of the Toolkit

             Running through the scenarios presented in the
             following documents:

             a) "INSTALL.txt" (includes a concise "Quick Test
                Drive" commentary)

             b) "DEMO.txt" (includes a verbose "Narrated,
                Scripted Demo Test Drive" commentary)

             c) "TROUBLESHOOT.txt" (includes a verbose
                "Insight of the "tsWxGTUI" Toolkit
                Developer(s)" commentary)

             d) Python source code for the associated application
                programs and building blocks.


                                           Richard S. Gordon
                                SoftwareGadgetry@comcast.net

============= Release Distribution Nominclature ============

2. Release Distribution Nominclature

   Multiple Python version-specific TeamSTARS "tsWxGTUI_PyVx"
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
                           Python 3.0.0-3.6.x.

                       Current stable release is Python 3.6.0 as
                       of 23 Dec. 2016. See the new features in
                       Python 3.6 compared to Python 3.5 in:

                           "https://docs.python.org/3/whatsnew/
                                    3.6.html"

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

                       Current stable release is Python 2.7.13
                       as of 17 Dec. 2016.

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

============== Release Distribution File Type ==============

3. Release Distribution File Type

   The files and directories/folders associated with the
   TeamSTARS "tsWxGTUI_PyVx" Toolkit may be released in
   any of several archive file formats, with or without
   data compression. The actual format depends on the type
   of computer platform operating system used to package
   the release:

   3.1 "Git" Repository Clone "Zip" File

       Excerpted from From Wikipedia, the free encyclopedia

          "Git is a distributed revision control system with an
          emphasis on speed, data integrity, and support for
          distributed, non-linear workflows. Git was initially
          designed and developed by Linus Torvalds for Linux
          kernel development in 2005, and has since become one
          of the most widely adopted version control systems for
          software development.

          As with most other distributed version control sys-
          tems, and unlike most client-server systems, every
          Git working directory is a full-fledged repository
          with complete history and full version-tracking cap-
          abilities, independent of network access or a central
          server. Like the Linux kernel, Git is free software
          distributed under the terms of the GNU General Public
          License version 2."

          "GitHub" offers all of the distributed revision control
          and source code management (SCM) functionality of Git
          as well as adding its own features.

       The Toolkit author chose the "GitHub" service because
       its cost-free features are popular with both software
       authors and recipients.
   
       You must use a web browser to download the TeamSTARS
       "tsWxGTUI_PyVx" Toolkit to your computer's desktop or
       to another convenient location.

       Though you do not need to become a "GitHub" member, you
       must use the following internet web address to view or
       obtain a copy of the toolkit repository:

          https://github.com/rigordo959/tsWxGTUI_PyVX_Repository

       The cloning process downloads a compressed "zip" file and
       then extracts the contents into a Git repository on your
       computer's desktop or to another convenient location.

   3.2 "Zip" File for Microsoft Windows

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

   3.3 "Tar" File for Cygwin, GNU/Linux and Unix

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

================= Source Distribution Type =================

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

====== Sdist, Build & Install Contents & Organization ======

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
 
       5.3.3 Mac OS X (10.3 Panther - 10.11 El Capitan)
 
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

