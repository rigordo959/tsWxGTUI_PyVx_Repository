#"Time-stamp: <12/06/2014  9:31:33 AM rsg>"

============== File: $README-tsDemoArchive.txt =============

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "nCurses"-based
   +---------+         Graphical-Text User Interface (GUI)

   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode terminals and terminal emulators.

===================== TABLE OF CONTENTS ====================

   The directory "tsDemoArchive"  contains those files
   which demonstrate or verify the proper operation of
   the TeamSTARS "tsWxGTUI" Toolkit.

------------------------------------------------------------

__init__.py - The __init__.py files are required to make
    Python treat the directories as containing packages;
    this is done to prevent directories with a common name,
    such as string, from unintentionally hiding valid
    modules that occur later on the module search path.
    In the simplest case, __init__.py can just be an empty
    file, but it can also execute initialization code for
    the package or set the __all__ variable.

------------------------------------------------------------

test_tsApplication.py - Demonstration and design verifi-
    cation test of "tsApplication", the base class for
    launching the application specified by an operator.
    It initializes and configures the application using
    keyword value pairs and positional arguments:

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) Run the following test case to capture display out-
       put via stdout, with the "-h" or "--help" option:

       python test_tsApplication.py -h > displayStdout.log

       After the test has been executed, compare the contents
       of "./tsManPagesTestsCLI/test_tsApplication.man" with
       the contents of "displayStdout.log" The contents should
       be the same except for date and time.

    d) Run the following test case to capture display out-
       put via stdout, without any options and positional
       arguments:

       python test_tsApplication.py > displayStdout.log

       In "displayStdout.log" and on the display:

test_tsApplication, v1.11.0 (build 06/01/2013)

	rawArgsOptions=[]



	tsCommandLineEnv.prototype (parameter list): 
		args=['argparse'];
		kw={}

	tsCommandLineEnv.prototype (command line argv): 
		args=['argparse'];
		options (unsorted)={'debug': False, 'about': False, 'version': False, 'Verbose': False, 'module': 'argparse'}

	tsCommandLineEnv.prototype (command line argv): 
		args (positional) =['argparse']
		options (sorted)= {Verbose: "False", about: "False", debug: "False", module: "argparse", version: "False"}

    e) Run the following test case to capture display out-
       put via stderr, without any options and positional
       arguments:

       python test_tsApplication.py > displayStderr.log

       After the test has been executed, check the contents
       of the run time log files. There should be a single
       exception report:

       In the "exitTest" file:

           "DEBUG: ***** ExitTest Input Output Exception / 
            Oops! Invalid Name *****".

       In "displayStderr.log" and on the display:

Input Output Exception: Oops! Invalid Name; ExitTest. [ExitCode #255]

  Input Output Exception (1); Oops! Invalid Name (255); ExitCode (255).

    Details: ExitTest.

    Traceback (most recent call last):

        File "test_tsApplication.py", line 381, in <module>
          theApplication.runMainApplication()
        File "/cygdrive/d/WR/SoftwareGadgetry-PyPI/Python-2x/tsWxGTUI_Py2x/tsLibCLI/tsApplicationPkg/src/tsApplication.py", line 1739, in runMainApplication
          self.runTimeEntryPoint()
        File "test_tsApplication.py", line 340, in prototype
          exitTest()
        File "test_tsApplication.py", line 258, in exitTest
          raise tse.InputOutputException(errorName, message)
        File "/cygdrive/d/WR/SoftwareGadgetry-PyPI/Python-2x/tsWxGTUI_Py2x/tsLibCLI/tsExceptionPkg/src/tsExceptions.py", line 663, in __init__
          traceback.format_stack())
      
Input Output Exception: Oops! Invalid Name; ExitTest. [ExitCode #255]

------------------------------------------------------------

test_tsCommandLineEnv.py - Demonstration and design verifi-
    cation test of "tsCommandLineEnv" module, a derivative
    of "tsApplication" that can be used to launch only the
    Command Line Interface portion of an applications.
    It provides a wrapper that produces Unix-style exit
    codes and messages, upon application termination.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsCommandLineInterface.py - Demonstration and design
    verification test of "tsCommandLineInterface.py", a
    class that establishes methods that prompt or re-prompt
    the operator for input, validate that the operator has
    supplied the expected number of inputs and that each is
    of the expected type. 

------------------------------------------------------------

test_tsCxGlobals.py - Demonstration and design verification
    test of "tsCxGlobals.py", a module that establishes
    configuration constants and macro-type functions for the
    Command Line Interface mode of the "tsWxGTUI" Toolkit.

    a) Provides a centralized mechanism for modifying/restor-
       ing those configuration constants that can be intero-
       gated at runtime by those software components having
       a "need-to-know". The intent being to avoid subsequent
       searches to locate and modify or restore a constant
       appropriate to the current configuration.

    b) Provides a theme-based mechanism for modifying/restor-
       ing those configuration constants as appropriate for
       the users (System Operator, Software Engineer, System
       Administrator and Field Service) users and their
       activities:

       Supervisory Control and Data Acquisition (SCADA)
       Application ("tsWxGTUI" CLI/GUI) Development
       Toolkit ("tsWxGTUI") Development

------------------------------------------------------------

test_tsDoubleLinkedList.py - Demonstration and design
    verification test of "tsDoubleLinkedList.py", a
    class to establish a representation of a linked
    list with forward and backward pointers. It pro-
    vides a functional and interface capability for
    randomly or sequentially populating, accessing
    and de-populating a double-linked list of user
    defined objects.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsExceptions.py - Demonstration and design verifi-
    cation test of "tsExceptions.py", a class to define
    and handle error exceptions that maps run time
    exception types into 8-bit exit codes and prints
    associated diagnostic message and traceback info.

------------------------------------------------------------

test_tsLogger.py - Demonstration and design verifi-
    cation test of "tsLogger.py ", a class that
    emulates a subset of Python logging API. It defines
    and handles prioritized, time and date stamped
    event message formatting and output to files and
    devices. Files are organized in a date and time
    stamped directory named for the launched application.
    Unix-type devices include syslog, stderr, stdout and
    stdscr (the ncurses display screen). It also supports
    "wxPython"-style logging of assert and check case
    results.

------------------------------------------------------------

test_tsOperatorSettingsParser.py - Demonstration and design
    verification test of "tsOperatorSettingsParser.py", a
    class to parse the command line entered by the oper-
    ator of an application program. Parsing extracts the
    Keyword-Value pair Options and Positional Arguments
    that will configure and control the application
    during its execution. 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsPlatformRunTimeEnvironment.py - Demonstration and
    design verification test of "tsPlatformRunTimeEnvi-
    ronment", a class to capture current hardware,
    software and network information about the run time
    environment for the user process.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including
                             its title, version and date)
                             and exit
       -a, --about           show a summary of the terms &
                             conditions for users
                             of this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -o OUTPUT, --output=OUTPUT
                             log/display current hardware
                             and software
                             information about the run time
                             environment to this
                             output file (default =
                             "./test_tsPlatformRunTime-
                             Environment.txt")
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting.
                             (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) Host processor hardware support includes various
       releases of 32-bit/64-bit processors (including
       Pentium, PowerPC, SPARC etc.) from companies such
       as Advanced Microdevices, Advanced RISC Machines,
       International Business Machines, Motorola and
       Oracle/Sun Microsystems etc.

    d) Host operating system software support includes
       various releases of Cygwin, Linux ('Debian',
       Fedora, 'Mandriva', 'Red Hat', 'SuSE' and
       'Ubuntu'), Mac OS X (10.4-10.9), Microsoft Windows
       ('98', '2000', 'XP', 'Vista', '7', '8' and '8.1')
       and Unix ('FreeBSD', 'PC-BSD', 'OpenIndiana' and
       'Solaris').

    e) Host virtual machine software support includes
       various releases of Java and Python.

------------------------------------------------------------

test_tsReportUtilities.py - Demonstration and design verifi-
    cation test of "tsReportUtilities.py", a class defining
    methods used to format information: date and time
    (begin, end and elapsed), file size (with kilo-, mega-,
    giga-, tera-, peta-, exa-, zeta- and yotta-byte units)
    and nested Python dictionaries.

------------------------------------------------------------

test_tsSysCommand.py - Demonstration and design verifi-
    cation test of "tsSysCommands.py, a class definition
    and methods for issuing shell commands to and receiving
    responses from the host operating system. 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -c COMMAND, --command=COMMAND
                             command [default = None]
       -v, --verbose         print status messages to
                             stdout [default = False]

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsWxBoxSizer.py - Demonstration and design verifi-
    cation test of the "tsWxBoxSizer" class and associated
    building block components of tsLibCLI and tsLibGUI. It
    features:

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A splash screen displaying Trademark, Copyright,
       License and Warranty disclaimer.

    d) A wxPython-style White on Blue Frame displaying:

       - Sample Frame Title

       - Sample Event triggering Blue on White Frame Control
         buttons (tokenize/minimize, maximize/restore and
         close)

       - Sample White on Blue Menu Bar

       - Sample wx.Panels:

         White on Blue Frame client sizer containing

             White on Magenta Horizontal sizer with

                 White on Cyan Vertical sizer,
                 White on Green Vertical sizer and
                 White on Yellow on Cyan Vertical sizer

             White on Red Horizontal sizer 

    e) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    f) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxCheckBox.py - Demonstration and design verifi-
    cation test of the tsWxCheckBox class and associated
    building block components of tsLibCLI and tsLibGUI. It
    features:

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application program
                             progress and
                             diagnostic messages useful in
                             debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments,
                             an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse", while
                             a Positional
                             Argument is used to override it
                             with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A splash screen displaying Trademark, Copyright,
       License and Warranty disclaimer.

    d) A wxPython-style White on Blue Frame displaying:

       - Sample Frame Title

       - Sample Event triggering Blue on White Frame Control
         buttons (tokenize/minimize, maximize/restore and
         close)

       - Sample White on Blue Menu Bar

       - Sample wx.Panels:

         White on Blue Frame client sizer containing

             Black on Cyan Horizontal sizer with

                 Left Aligned Two-State Checkboxes,
                 Underlined Hot-Key Character (for Future Event)

             Black on Green Horizontal sizer with

                 Right Aligned Two-/Three-State Checkboxes,
                 Underlined Hot-Key Character (for Future Event)

    e) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    f) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxDisplay.py - Demonstration and design verifi-
    cation test of 

------------------------------------------------------------

test_tsWxDoubleLinkedList.py - Demonstration and design verifi-
    cation test of 

------------------------------------------------------------

test_tsWxGlobals.py - Demonstration and design verifi-
    cation test of 

------------------------------------------------------------

test_tsWxGraphicalTextUserInterface.py - Demonstration and
    design verification test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsWxGridSizer.py - Demonstration and design verifi-
    cation test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsWxMultiFrameEnv.py - Demonstration and design verifi-
    cation test of "tsWxMultiFrameEnv" module, a derivative
    of "tsCommand LineEnv" that can be used to launch both
    the Command Line Interface and Graphical-style User
    Interface portions of an applications. It provides a
    wrapper that produces Unix-style exit codes and mes-
    sages, upon application termination. 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    d) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxRSM.py - Mock (static) Supervisory Control and
    Data Acquisition (SCADA) application demonstration of
    the character-mode, wxPython emulation. It features:

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A splash screen displaying Trademark, Copyright,
       License and Warranty disclaimer.

    d) A White on Blue SCADA frame displaying:

       - operating mode and status
       - operator setpoints
       - equipment operating capabilities and constraints
       - available analog and digital sensor signal values

    e) A Blue on White SCADA dialog displaying:

       - exit on-line diagnostic and maintenance command
       - pause on-line display update command
       - start/stop diagnostic report logging commands
       - start/stop input/output signal setup/calibration
         commands

    f) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    g) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxScrolledWindow.py - Demonstration and design verifi-
    cation test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages.

    d) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxScrolledWindowDual.py - Demonstration and design verifi-
    cation test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    d) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

test_tsWxSplashScreen.py - Demonstration and design verifi-
    cation test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

test_tsWxWidgets.py - Demonstration and design verifi-
    cation test of 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsOperatorSettingsParserPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -d, --debug           log/display application
                             program progress and
                             diagnostic messages useful
                             in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose trouble-
                             shooting details for
                             application program activity
                             tracking diagnostic
                             messages (default = False)
       -m {argparse}, --module {argparse}
                             sets default for standard
                             Python parser module. (To
                             demonstrate the similarity
                             and differences between
                             Optional and Positional
                             Arguments, an Optional
                             Argument is used to set the
                             latest Python
                             recommendation, "argparse",
                             while a Positional
                             Argument is used to override
                             it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) A White on Black Redirected output frame displaying
       date and time-stamped event notification messages
       with color markup to highlight event severity.

    d) A White on Black Task Bar frame displaying buttons
       to shift focus and bring a frame/dialog from partial-
       ly overlapped background to non-overlapped foreground
       (a Future Feature). Displays application run time
       name, a rotating baton to temporarily indicate lapses
       in activity and the date and time to indicate current
       activity.

------------------------------------------------------------

tsCxGlobals.py - Demonstration and design verifi-
    cation test of 

------------------------------------------------------------

tsLinesOfCodeProjectMetrics.py - Python application program,
    with a Command Line Interface (CLI), that generates
    reports of software project progress and the estimated
    cost (or contributed value) of the project when it is
    finally completed.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the "tsOperatorSettingsParser.py"
       module from the "tsLinesOfCodeProjectMetricsPkg" to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this
                             software (including its
                             title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users of
                             this software (including the
                             applicable product
                             identification, authors,
                             contributors, copyrights,
                             licenses and purpose) and exit
       -i INPUT, --input INPUT
                             gather software source file
                             metrics (source type, code
                             lines, comment lines, total
                             lines, words, characters)
                             for each invidual file and
                             for collection of files in
                             this input directory (default = "./").
       -o OUTPUT, --output OUTPUT
                             log/display source file metrics
                             (source type, code
                             lines, comment lines, total lines,
                             words, characters)
                             for each invidual file and for
                             collection of files to
                             this output file (default =
                             "./tsLinesOfCodeProjectMetrics.pyStatistics.txt")
       -d, --debug           log/display application program progress and
                             diagnostic messages useful in debugging and
                             troubleshooting. (default = False).
       -s, --scan            enable log/display software source file parsing
                             activity details source file type (file name
                             extension) and individual line type
                             (code, comment,
                             directive) (default = False)
       -V, --Verbose         log/display verbose troubleshooting details for
                             application program activity tracking diagnostic
                             messages (default = False)
       -p {0,1,2}, --project {0,1,2}
                             log/display software development
                             project metrics in
                             accordance with COCOMO Model, first published, in
                             1981, by Dr. Barry W. Boehm. Key choice: {"0"
                             (default) | "1" | "2"} where: "0"
                             selects "organic"
                             model "small" teams with "good" experience working
                             with "less than rigid" requirements; "1" selects
                             "semi-detatched" model "medium" teams with mixed
                             experience working with a mix of "rigid" and "less
                             than rigid" requirements; "2" selects
                             "embedded" model
                             developed within a set of "tight"
                             constraints. It is
                             also combination of "organic" and "semi-detached"
                             projects. (hardware, software, operational, ...)
       -m {argparse}, --module {argparse}
                             sets default for standard Python
                             parser module. (To
                             demonstrate the similarity and
                             differences between
                             Optional and Positional Arguments, an Optional
                             Argument is used to set the latest Python
                             recommendation, "argparse", while a Positional
                             Argument is used to override it with a now Python
                             deprecated "optparse" or "getopt")

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) It scans an operator designated file directory tree
       containing the source files, in one or more program-
       ming language specific formats (such as Ada, Assem-
       bler, C/C++, Cobol, Fortran, PL/M, Python, Text, and
       various command line shells).

       * For each file, it accumulates and reports the total
         number of code lines, blank/comment lines, words
         and characters.

       * For each programming language format, it accumulates
         and reports a summary of details of the associated
         source files.

       * For the entire set of source files, it accumulates
         and reports a summary of details.

    d) It uses the summary of the entire set of source files
       to derive, analyze, estimate and report metrics for
       the software development project (such as labor, cost,
       schedule and lines of code per day productivity). 

------------------------------------------------------------

tsPlatformQuery.py - Python application program, with a
    Command Line Interface (CLI), to capture current hard-
    ware, software and network information about the run
    time environment for the user process.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -v, --version         show the build version of this software (including
                             its title, version and date) and exit
       -a, --about           show a summary of the terms &
                             conditions for users
                             of this software (including the applicable product
                             identification, authors, contributors, copyrights,
                             licenses and purpose) and exit
       -o OUTPUT, --output=OUTPUT
                             log/display current hardware and software
                             information about the run time environment to this
                             output file (default = "./tsPlatformQuery.txt")
       -d, --debug           log/display application program progress and
                             diagnostic messages useful in debugging and
                             troubleshooting. (default = False).
       -V, --Verbose         log/display verbose troubleshooting details for
                             application program activity tracking diagnostic
                             messages (default = False)

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) Host processor hardware support includes various
       releases of 32-bit/64-bit processors (including
       Pentium, PowerPC, SPARC etc.) from companies such
       as Advanced Microdevices, Advanced RISC Machines,
       International Business Machines, Motorola and
       Oracle/Sun Microsystems etc.

    d) Host operating system software support includes
       various releases of Cygwin, Linux ('Debian',
       Fedora, 'Mandriva', 'Red Hat', 'SuSE' and
       'Ubuntu'), Mac OS X (10.4-10.9), Microsoft Windows
       ('98', '2000', 'XP', 'Vista', '7', '8' and '8.1')
       and Unix ('FreeBSD', 'PC-BSD', 'OpenIndiana' and
       'Solaris').

    e) Host virtual machine software support includes
       various releases of Java and Python.

------------------------------------------------------------

tsStripComments.py - Python application program, with a
    Command Line Interface (CLI), to transform an annotated,
    development version of a directory of subdirectories and
    Python source files into an unannotated copy. The copy
    is intended to conserve storage space when installed in
    an embedded system. The transformation involves strip-
    ping comments and docstrings by de-tokenizing a token-
    ized version of each Python source file. Non-Python
    files are trimmed of trailing whitespace.   

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

      -h, --help            show this help message and exit
      -v, --version         show the build version of this
                            software (including its
                            title, version and date) and exit
      -a, --about           show a summary of the terms &
                            conditions for users of
                            this software (including the applicable product
                            identification, authors, contributors, copyrights,
                            licenses and purpose) and exit.
      -i INPUT, --input INPUT
                            sets input directory containing annotated Python
                            source code files and sub-directories of additional
                            files which are to be copied without their comments
                            and document strings. (default = "./").
      -o OUTPUT, --output OUTPUT
                            sets output directory containing
                            un-annotated Python
                            source code files and sub-directories of additional
                            files which have been stripped of
                            their comments and
                            document strings. (default = "./WithoutComments").
      -d, --debug           log/display application program progress and
                            diagnostic messages useful in debugging and
                            troubleshooting. (default = False).
      -s, --scan            enable log/display software source file parsing
                            activity details source file type (file name
                            extension) and individual line
                            type (code, comment,
                            directive) (default = False)
      -V, --Verbose         log/display verbose troubleshooting details for
                            application program activity tracking diagnostic
                            messages (default = False)
      -m {argparse}, --module {argparse}
                            sets default for standard Python parser module that
                            will be used to extract operator settings (keyword-
                            value pairs and positional arguments)
                            from the command
                            line used to launch the tsStripComments
                            application.
                            (NOTE: To demonstrate the similarity
                            and differences
                            between Optional and Positional
                            Arguments, an Optional
                            Argument is used to set the latest Python
                            recommendation, "argparse", while a Positional
                            Argument is used to override it with a now Python
                            deprecated "optparse" or "getopt".)

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

tsStripLineNumbers.py - Python application program, with a
    Command Line Interface (CLI), to strip line numbers from
    source code that do NOT reference line numbers for
    conditional branching.

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -i INPUT, --input=INPUT
                             topLevel directory [default = ./]
       -o OUTPUT, --output=OUTPUT
                             output directory ' +
                             '[default = ../published]

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

    c) Output from source files in the BASIC programming
       language format is NOT stripped of line numbers
       because line numbers are used for conditional
       branching.

    d) Output from fixed format Fortran (F77) code is NOT
       corrected to ensure that each statement first char-
       acter begins in column 7 and that each ampersand
       ("&") continuation character is in column 6.

------------------------------------------------------------

tsTreeCopy.py - Python application program, with a
    Command Line Interface (CLI), to copy the contents of
    a source directory to a target directory.   

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -i INPUT, --input=INPUT
                             topLevel directory [default = ./]
       -o OUTPUT, --output=OUTPUT
                             output directory [default = ../published]
       -s, --symlinks        Copy symbolic links, if True, ' +
                             'or contents of linked files, if False ' +
                             '[default = False].

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

------------------------------------------------------------

tsTreeTrimLines.py - Python application program, with a
    Command Line Interface (CLI), to copy the contents of
    a source directory to a target directory after strip-
    ping superfuous white space (blanks) from the end of
    each line. 

    a) Input provided on the command line by an operator.
       The command line uses a Unix-style, free-format to
       promote future enhancement and on-going maintenance.
       Imports and uses the Python "argparse" module to:

       -h, --help            show this help message and exit
       -i INPUT, --input=INPUT
                             topLevel directory [default = ./]
       -o OUTPUT, --output=OUTPUT
                             output directory [default = ../published]
       -n NOTICEDIRECTORY, --notices=NOTICEDIRECTORY
                             notice directory [default = ../notices]
       -s, --symlinks        Copy symbolic links, if True,
                             or contents of linked
                             files, if False [default = False].
       -v, --verbose         print status messages to stdout
                             [default = False]

    b) Input provided in the parameter list of the applica-
       tion's invocation of the class instantiation. The par-
       ameter list uses a Python-style free-format to promote
       future enhancement and on-going maintenance.

======================= End-Of-File ========================
