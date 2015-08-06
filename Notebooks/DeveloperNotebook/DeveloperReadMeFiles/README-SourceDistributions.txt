#-----------------------------------------------------------
#"Time-stamp: <05/20/2015  8:15:07 PM rsg>"
#-----------------------------------------------------------

=========== File: $README-SourceDistributions.txt ==========

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find other plain-text files in the Toolkit
   subdirectory named ["$Documents"].

       <Your Working Repository>
       (e.g. "Technical_Preview") 
         |
         |  Working repository containing directories and
         |  files to be packaged into downloadable "tarball"
         |  and/or "zip" files via the commands:
         |
         +-- ["$Documents"]
         |
         +-- ["$ManPages"]
         |
         +-- ["$Notebooks"]
         |
         +-- ["$SourceDistributions"]
               |
               +-- ["$Developer-Sandbox"]
               |     |
               |     +-- ["tsWxGTUI_PyVx"]
               |     |     |
               |     |     +-- ["Python-2x"]
               |     |     |     |
               |     |     |     +-- ["tsWxGTUI_Py2x"]
               |     |     |     |     |
               |     |     |     |     +-- "$README-tsWxGTUI_Py2x-Developer-Sandbox"
               |     |     |     |
               |     |     |     +-- "$README-Python-2x-Developer-Sandbox"
               |     |     |
               |     |     +-- ["Python3x"]
               |     |     |     |
               |     |     |     +-- ["tsWxGTUI_Py3x"]
               |     |     |     |     |
               |     |     |     |     +-- "$README-tsWxGTUI_Py3x-Developer-Sandbox"
               |     |     |     |
               |     |     |     +-- "$README-Python-3x-Developer-Sandbox"
               |     |     |
               |     |     +-- "$README-tsWxGTUI_PyVx-Developer-Sandbox"
               |     |
               |     +-- "$README-Developer-Sandbox"
               |
               +-- ["$Site-Package"]
               |     |
               |     +-- ["tsWxGTUI_PyVx"]
               |     |     |
               |     |     +-- ["Python-2x"]
               |     |     |     |
               |     |     |     +-- ["tsWxGTUI_Py2x"]
               |     |     |     |     |
               |     |     |     |     +-- "$README-tsWxGTUI_Py2x-Site-Package"
               |     |     |     |
               |     |     |     +-- "$README-Python-2x-Site-Package"
               |     |     |
               |     |     +-- ["Python3x"]
               |     |     |     |
               |     |     |     +-- ["tsWxGTUI_Py3x"]
               |     |     |     |     |
               |     |     |     |     +-- "$README-tsWxGTUI_Py3x-Site-Package"
               |     |     |     |
               |     |     |     +-- "$README-Python-3x-Site-Package"
               |     |     |
               |     |     +-- "$README-tsWxGTUI_PyVx-Site-Package"
               |     |
               |     +-- "$README-Site-Package"
               |
               +-- "$README-SourceDistributions.txt"

===================== TABLE OF CONTENTS ====================

1. Source Code

2. Developer-Sandbox

3. Site-Package

===================== SourceDistribution ====================

1. Source Code

   Excerpt From Wikipedia, the free encyclopedia:

   "In computing, source code is any collection of computer
   instructions (possibly with comments) written using some
   human-readable computer language, usually as text. The
   source code of a program is specially designed to facili-
   tate the work of computer programmers, who specify the
   actions to be performed by a computer mostly by writing
   source code. The source code is often transformed by a
   compiler program into low-level machine code understood
   by the computer. The machine code might then be stored
   for execution at a later time. Alternatively, an inter-
   preter can be used to analyze and perform the outcomes
   of the source code program directly on the fly.

   Most computer applications are distributed in a form that
   includes executable files, but not their source code. If
   the source code were included, it would be useful to a
   user, programmer, or system administrator, who may wish
   to modify the program or to understand how it works.

   Aside from its machine-readable forms, source code also
   appears in books and other media; often in the form of
   small code snippets, but occasionally complete code
   bases; a well-known case is the source code of PGP."

===================== DEVELOPER-SANDBOX ====================

2. Developer-Sandbox

   Excerpt From Wikipedia, the free encyclopedia:

   "A sandbox is a testing environment that isolates untest-
   ed code changes and outright experimentation from the
   production environment or repository, in the context of
   software development including Web development and revis-
   ion control. Sandboxing protects "live" servers and their
   data, vetted source code distributions, and other collec-
   tions of code, data and/or content, proprietary or pub-
   lic, from changes that could be damaging (regardless of
   the intent of the author of those changes) to a mission-
   critical system or which could simply be difficult to
   revert. Sandboxes replicate at least the minimal func-
   tionality needed to accurately test the programs or
   other code under development (e.g. usage of the same
   environment variables as, or access to an identical
   database to that used by, the stable prior implementa-
   tion intended to be modified; there are many other
   possibilities, as the specific functionality needs vary
   widely with the nature of the code and the application[s]
   for which it is intended.)

   The concept of the sandbox (sometimes also called a work-
   ing directory, a test server or development server) is
   typically built into revision control software such as
   CVS and Subversion (SVN), in which developers "check out"
   a copy of the source code tree, or a branch thereof, to
   examine and work on. Only after the developer has (hope-
   fully) fully tested the code changes in their own sandbox
   should the changes be checked back into and merged with
   the repository and thereby made available to other devel-
   opers or end users of the software.[1]

   By further analogy, the term "sandbox" can also be ap-
   plied in computing and networking to other temporary or
   indefinite isolation areas, such as security sandboxes
   and search engine sandboxes (both of which have highly
   specific meanings), that prevent incoming data from
   affecting a "live" system (or aspects thereof) unless/
   until defined requirements or criteria have been met."

   Unlike the contents of the installable site-package,
   this sandbox uses a multi-level tree of subdirecories and
   associated files whose topology is defined by a set of
   package "__init__.py" files which collaborate in perform-
   ing dynamic path generation and importing of modules and
   subpackages. Applications import individual packages and
   individual modules simply by name (if module name is
   unique) or by package.module name (if module name is not
   unique).

======================= SITE-PACKAGE =======================

3. Site-Package

   Site-packages is the location where third-party packages
   are installed (i.e., those not part of the core Python
   distribution). NOTE: That with Linux, Mac OS X and Unix
   operating systems one must have root priviledges to write
   to that location.

   Unlike the contents of the Developer-Sandbox, the third-
   party site-package and it users must explicitly import
   via the site-package.package.module path identifier.

======================= End-Of-File ========================
