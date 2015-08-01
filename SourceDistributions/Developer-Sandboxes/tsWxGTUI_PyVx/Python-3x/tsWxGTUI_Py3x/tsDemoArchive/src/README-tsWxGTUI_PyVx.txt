#"Time-stamp: <05/09/2014  8:10:37 AM rsg>"

============== File: README-tsWxGTUI_PyVx.txt =============

   +----+----+  TeamSTARS "tsWxGTUI" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "nCurses"-based
   +---------+         Graphical-Text User Interface (GUI)

   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode terminals and terminal emulators.

===================== TABLE OF CONTENTS ====================

1. Release Distribution

2. Contents of Downloaded "tarball" or "zip" File

=================== Release Distribution ===================

1. Release Distribution

   Each Python version-specific "tsWxGTUI" Toolkit is down-
   loaded (as either a compressed, "tarball" or "zip"
   file) from the Python Package Index, a repository of
   software for the Python programming lanuage.

   The "tarball" or "zip" file name is composed of three
   components:

   <Release Name>_<Python Type>-<Major.Minor.BugFix Number>:

   a. Release Name:

      "tsWxGTUI"

   b. Python Type:

      "_Py2x" - Identifies second generation syntax associ-
                ated with Python 2.6.6-2.7.6.

      "_Py3x" - Identifies third generation syntax associ-
                ated with Python 3.2.0-3.2.5.

   c. Major-Minor-BugFix Number:

      "0.0.0" Identifies first major, pre-alpha, release

      "1.0.0" Identifies first major, production, release

      "3.2.1" Identifies first bug fix, for second func-
              tional enhancement for third major production
              release

   d. Release File Type:

      "tarball" Type such as:

          "tsWxGTUI_Py2-3.2.1.tar.gz"
          "tsWxGTUI_Py3-3.2.1.tar.gz"

      "zip" Type such as:

          "tsWxGTUI_Py2-3.2.1.zip"
          "tsWxGTUI_Py3-3.2.1.zip"

    --------------------------------------------------------
    NOTES:

    a. Directory names are displayed within square brackets
       and double quotation marks, as in ["tsDemoArchive"]. 

    b. File names are displayed within double quotation
       marks, as in "tsCxGlobals.py". 
    --------------------------------------------------------

====== Contents of Downloaded "tarball" or "zip" File ======

2. Contents of Downloaded "tarball" or "zip" File

   a. The "tsWxGTUI" Toolkit author(s) recommend use of a
      single download directory that separates the source
      code for the two supported Python language versions:
 
      ["/WR/SoftwareGadgetry-PyPI-Download"]
           |
           |    Working repository containing extracted
           |    files from zip and/or tarball download(s).
           |
           +-- ["Python-2x"]
           |     |
           |     +-- ["dist"]
           |           |
           |           +-- ["tsWxGTUI_Py2x-3.2.1.zip"]
           |                 |
           |                 +-- ["tsWxGTUI_Py2x-3.2.1"]
           |                       |
           |                       +-- ["tsWxGTUI_Py2x"]
           |                       +-- ["tsWxGTUI_Py2x.egg-info"]
           |                       |
           |                       +-- "__init__.py"
           |                       +-- "MANIFEST.in"
           |                       +-- "MANIFEST_TREE.html"
           |                       +-- "MANIFEST_TREE.sh"
           |                       +-- "MANIFEST_TREE.txt"
           |                       +-- "README-setup.txt"
           |                       +-- "say_hello.py"
           |                       +-- "setup.cfg"
           |                       +-- "setup.py"
           |
           +-- ["Python-3x"]
                 |
                 +-- ["dist"]
                       |
                       +-- ["tsWxGTUI_Py3x-3.2.1.tar.gz"]
                             |
                             +-- ["dist"]
                                   |
                                   +-- ["tsWxGTUI_Py3x-3.2.1.tar"]
                                         |
                                         +-- ["tsWxGTUI_Py3x"]
                                         +-- ["tsWxGTUI_Py3x.egg-info"]
                                         |
                                         +-- "__init__.py"
                                         +-- "MANIFEST.in"
                                         +-- "MANIFEST_TREE.html"
                                         +-- "MANIFEST_TREE.sh"
                                         +-- "MANIFEST_TREE.txt"
                                         +-- "README-setup.txt"
                                         +-- "say_hello.py"
                                         +-- "setup.cfg"
                                         +-- "setup.py"


   b. Source directories and files can only be used, by Soft-
      ware Engineers and System Operators, after they have
      been extracted from the download. The extraction and
      subsequent site-package installation creates the
      following components:

         ["tsWxGTUI_PyVx"]
           |
           +-- ["tsDemoArchive"]
           |
           |    Contains those application programs which
           |    demonstrate or verify the proper operation
           |    of the TeamSTARS "tsWxGTUI" Toolkit.
           |
           +-- ["tsDocCLI"]
           |
           |    Contains documents in a plain text format
           |    suitable for use on software development
           |    and embedded systems having limited
           |    capabilities and resources.
           |
           |    Topics include:
           |
           |        How to Prepare Platform to Get Started
           |
           |        How to Install and Redistribute
           |
           |        How to Use and Modify
           |
           |        How to Learn "tsWxGTUI" Toolkit
           |        Software Development
           |
           |        Terms & Conditions
           |
           +-- ["tsDocGUI"]
           |
           |    Contains documents in a multi-font format
           |    with tables and graphical images suitable
           |    for use on software development, word pro-
           |    cessing and desktop publishing systems
           |    having enhanced capabilities and resources.
           |
           |    Topics include:
           |
           |        Announcement
           |        Brochure
           |        Introduction
           |        Usage Terms & Conditions
           |        Development Plan
           |        Requirement Specifications
           |        Release Notes
           |        Software User's Manual
           |
           +-- ["tsLibCLI"]
           |
           |    Contains general-purpose, re-usable
           |    building blocks supporting Command
           |    Line Interface.
           |
           +-- ["tsLibGUI"]
           |
           |    Contains general-purpose, re-usable
           |    building blocks supporting character-mode,
           |    "wxPython"-style Graphical-style User
           |    Interface.
           |
           |    Also contains Theme-based configuration
           |    settings for customizing Graphical-style
           |    User Interface.
           |
           +-- ["tsManPagesLibCLI"]
           |
           |    Contains Application Programming
           |    Interface documents produced via PyDoc
           |    from source code in "tsLibCLI".
           |
           +-- ["tsManPagesLibGUI"]
           |
           |    Contains Application Programming
           |    Interface documents produced via PyDoc
           |    from source code in "tsLibGUI".
           |
           +-- ["tsManPagesTestsCLI"]
           |
           |    Contains System Operator help
           |    documents produced via "--help"
           |    option when launching the CLI test
           |    applications in ["tsDemoArchive"].
           |
           +-- ["tsManPagesTestsGUI"]
           |
           |    Contains System Operator help
           |    documents produced via "--help"
           |    option when launching the GUI test
           |    applications in ["tsDemoArchive"].
           |
           +-- ["tsManPagesToolsCLI"]
           |
           |    Contains Application Programming
           |    Interface document produced via "--help"
           |    option when launching the CLI tool
           |    applications in ["tsDemoArchive"].
           |
           +-- ["tsManPagesToolsGUI"]
           |
           |    Currently has no content.
           |
           |    Contains Application Programming
           |    Interface document produced via "--help"
           |    option when launching the GUI tool
           |    applications in ["tsDemoArchive"].
           |
           +-- ["tsToolsCLI"]
           |
           |    Contains software development CLI tools
           |    to monitor and improve productivity.
           |
           +-- ["tsToolsGUI"]
           |
           |    Currently has no content.
           |
           |    Contains software development GUI tools
           |    to monitor and improve productivity.
           |
           +-- ["tsUtilities"]
           |
           |    Contains CLI shell and Python scripts to
           |    monitor and modify hardware and software
           |    features.
           |
           +-- "tsCxGlobals.py"
           |
           |    Contains Theme-based configuration
           |    settings for customizing Command Line
           |    Interface.
           |
           +-- Demo file collection of Tests and Tools
               copied from ["tsDemoArchive"]  

======================= End-Of-File ========================

