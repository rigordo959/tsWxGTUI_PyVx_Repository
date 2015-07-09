#-----------------------------------------------------------
#"Time-stamp: <05/12/2015 10:45:47 AM rsg>
#-----------------------------------------------------------

================ File: README-tsDocCLI.txt =================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find this and other plain-text files in the
   Toolkit subdirectory named
       "./tsWxGTUI_PyVx/Documents/tsDocCLI".

===================== TABLE OF CONTENTS ====================

1.Python Language Generation-Specific Versions

   1.1 "tsWxGTUI_Py3x" Release (CLI & GUI)
   1.2 "tsWxGTUI_Py2x" Release (CLI & GUI)
   1.3 "tsWxGTUI_Py1x" Release (CLI & GUI) (Not Planned)

2. Operator Documentation

   2.1 How to Prepare Platform to Get Started
   2.2 How to Install and Redistribute
   2.3 How to Use and Modify
   2.4 How to Learn "tsWxGTUI" Toolkit Software Development
   2.5 Terms & Conditions

======= PYTHON LANGUAGE GENERATION-SPECIFIC VERSIONS =======

1. Python Language Generation-Specific Versions

   The TeamSTARS "tsWxGTUI_PyVx" Toolkit is implemented
   and released in Python language generation specific
   versions (listed in reverse chronological order
   with newest generation first and oldest one last):

   1.1 "tsWxGTUI_Py3x" Release (CLI & GUI)

       This release supports application program develop-
       ment in the third generation Python language.
       It is a translation of the "tsWxGTUI_Py2x" Release
       produced by the standard Python 2to3 utility that
       is then debugged to resolve other porting issues
       such as byte decode/encode and file access mode.

       The Toolkit currently supports Python 3.0.0-3.4.2.

   1.2 "tsWxGTUI_Py2x" Release (CLI & GUI)

       This release supports application program develop-
       ment in the second generation Python language.

       The Toolkit currently supports Python 2.0.0-2.7.9.

   1.3 "tsWxGTUI_Py1x" Release (CLI & GUI) (Not Planned)

       This release would potentially support application
       program development in the now obsolete first gen-
       eration Python language.

       The Toolkit could potentially support Python 1.0.0-
       1.6.1.

       With considerable effort, it could be produced by
       back-porting source code for the "tsWxGTUI_Py2x"
       Release and associated components from the second
       generation Python language Global Module Index.

       However, back-porting is NOT recommended because:

       a. The Python Software Foundation provides limited
          means to download the Python 1.x distribution
          produced at CNRI (The Corporation for National
          Research Initiatives, based in Reston, Virginia).

       b. Python 1.x does NOT recognize the following
          Python 2.x syntax and semantics features:

          * import someModule as someAlias
            (try:
               import someModule
               someAlias = someModule
            )

          * from someModule import someClass as someAlias
            (try:
               from someModule import someClass
               someAlias = someClass
            )

          * print function
            (try:
               fmt = someFormatedString
                     (ex. 'number=%d; text=%s' % (number, text)))
               print fmt
            )

          * @staticmethod
            (try:
               #@staticmethod
               def someMethod(self, argList)
            )

       c. Python 1.x does NOT provide the following library
          modules:

          * optparse (try modifying a copy of optparse from
            Python 2.x or emulating with getopt)

          * platform (try emulating by using sys.argv)

          * subprocess (try emulating with TBD)

          * textwrap (try modifying a copy of textwrap from
            Python 2.x)

       d. Python 1.x does NOT recognize the Python 2.x syntax
          for the new type class statement:
          (try removing the (object) inheritance reference)

       e. Python 1.x does NOT recognize the Python 2.x syntax
          property statement:
          (try commenting out the property statement)

       f. Python 1.x does NOT recognize the following Python
          2.x assignment syntax:

          * something += increment
            (try something = something + increment)

          * something -= increment
            (try something = something - increment)

=================== OPERATOR DOCUMENTATION =================

2. Operator Documentation
 
   User documentation for each TeamSTARS "tsWxGTUI_PyVx"
   Toolkit distribution is contained, in plain text format,
   in the subdirectory named "./tsWxGTUI_PyVx/tsDocCLI".
   The subdirectory is organized, by topic, to contain the
   following:

   2.1 How to Prepare Platform to Get Started

      The "./GettingStartedFiles" subdirectory contains
      the following file(s):

      "README-GettingStarted.txt" -

   2.2 How to Install and Redistribute

      The "./DistributionReadMeFiles" subdirectory contains
      the following file(s):

      "AUTHORS.txt"  - List of the principal "tsWxGTUI"
                       Toolkit author(s) and authors
                       credited for work covered by a prior
                       copyright and license.

      "BUGS.txt"     - List of Known Problems / Issues.

      "CHANGE_
       LOG.txt"      - List of Additions, Modification and
                       Deletions.

      "CONFIG-
       URE.txt"      - Instructions for applying factory and
                       site-specific configurations.

      "COPYING.txt"  - Instructions for copying all or a
                       portion of the distribution.

      "FAQ.txt"      - Answers to Frequently Asked
                       Questions.

      "INSTALL.txt"  - Describes steps to download, extract
                       install and configure the "tsWxGUI"
                       Toolkit.

      "LICENSE.txt"  - General and special arrangements,
                       provisions, rules, specifications and
                       standards that form an integral part
                       of the agreement or contract between
                       the creator and recipient of Copy-
                       righted and Licensed Work.

      "MANIFEST.txt" - Tally List for deliverable items.

      "NEWS.txt"     - Announcements of new releases.

      "NOTICES.txt"  - Details the copyright(s) and li-
                       cense(s).

      "OPERATE.txt"  - Describes steps to use the "tsWxGUI"
                       Toolkit.

      "README.txt"   - Introduces new recipients to the
                       purpose, goals, non-goals, design
                       and features of the computer
                       software product.

      "THANKS.txt"   - Acknowledgments to those otherwise
                       unsung heros who contributed time
                       and effort to supporting the authors
                       as planners, editors, designers,
                       coders and testers.

      "TO-DO.txt"    - A To-Do-List provides a roadmap for
                       development and troubleshooting work.

      "TROUBLE-
       SHOOT.txt"    - Provides a list of available refer-
                       ence resources and a guide for plan-
                       ning, developing and troubleshooting
                       a cross-platform system of hundreds
                       of files each containing a few, tens
                       or hundred of class, data and method
                       definitions. Its complexity becomes
                       apparent in the recent software
                       Lines-Of-Code metrics.
 
   2.3 How to Use and Modify

      The "./DeveloperReadMeFiles" subdirectory contains
      the following file(s):

      "README.txt"
      "README_1st.txt"
      "README_1st-PyPI-Dev-tsWxGTUI.txt"
      "README-01-Title_Page.txt"
      "README-02-Table_Of_Contents.txt"
      "README-03-Purpose.txt"
      "README-04-Goals.txt"
      "README-05-Non-Goals.txt"
      "README-06-Design_Strategy.txt"
      "README-07-Design_Architecture.txt"
      "README-08-Software_Configuration_Management.txt"
      "README-09-tsWxGTUI_Directories.txt"
      "README-10-tsToolkitCLI_Directories.txt"
      "README-11-tsToolkitGUI_Directories.txt"
      "README-12-Features.txt"
      "README-13-Current_Capabilities.txt"
      "README-14-Current_Limitations.txt"
      "README-15-Reference_Documents.txt"

   2.4 How to Learn "tsWxGTUI" Toolkit Software Development

      The "./DeveloperTutorialFiles" subdirectory contains
      the following file(s):

      "CLI_0_hello_world_print_statement.py"
      "CLI_1_hello_world_print_function.py"
      "CLI_2_hello_world_script_environment.py"
      "CLI_3_hello_world_main_module_application.py"
      "GUI_4_Curses_LowLevel_WidgetApi_application.py"
      "GUI_5_tsWxGTUI_HighLevel_WidgetApi_application.py"
      "GUI_6_tsWxGTUI_HighLevel_BoxSizerApi_application.py"
      "ReadMe_Developer_Tutorial_Files.txt"
      "test_tsCxGlobals.py"
      "test_tsWxGlobals.py"
      "tsCxGlobals.py"

   2.5 Terms & Conditions

      The "./UsageTermsAndConditions" subdirectory contains
      the following file(s):

      "COPYRIGHT.txt"
      "LICENSE.txt"
      "NOTICES.txt"
      "SplashScreenDesignersGuide.txt"

======================= End-Of-File ========================
