#"Time-stamp: <06/16/2015  4:24:50 PM rsg>"

================ File: $README-tsLibCLI.txt ================

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

===================== TABLE OF CONTENTS ====================

1. Library Organization
2. tsApplication.py
3. tsCommandLineEnv.py
4. tsCommandLineInterface.py
5. tsCxGlobals.py
6. tsDoubleLinkedList.py
7. tsException.py
8. tsGistGetTerminalSize.py
9. tsLogger.py
10. tsOperatorSettingsParser.py
11. tsPlatformRunTimeEnvironment.py
12. tsReportUtility.py
13. tsSysCommands.py

=================== LIBRARY ORGANIZATION ===================

1. Library Organization

   The library of building blocks is organized, by the
   functional scope of each component, into a collection of
   "modules". When appropriate, any module may import and
   use the services of any other tsLibCLI module.

===================== tsApplication.py =====================

2. tsApplication.py

   It enables the application program launched by an oper-
   ator via a Command Line Interface (CLI) to also initial-
   ize, configure and use the same character-mode terminal
   with a Graphical-style User Interface (GUI).

   It registers and validates:

   a. operator application settings inputs from command
      line keyword-value pairs and positional arguments.

   b. instantiation settings input from applications
      via caller parameter list.

   It is the base class, for tsCommandLineEnv which itself
   is the base class for tsWxMultiFrameEnv.

==================== tsCommandLineEnv.py ===================

3. tsCommandLineEnv.py

   Class to initialize and configure the application program
   launched by an operator. It delivers those keyword-value
   pair options and positional arguments specified by the
   application, in its invocation parameter list. It wraps
   the Command Line Interface application with exception
   handlers to control exit codes and messages that may be
   used to co-ordinate other application programs. 

================= tsCommandLineInterface.py ================

4. tsCommandLineInterface.py

   Class establishes methods that prompt or re-prompt
   the operator for input, validate that the operator
   has supplied the expected number of inputs and that
   each is of the expected type.

======================= tsCxGlobals.py =====================

5. tsCxGlobals.py

   Module to establish configuration constants and
   macro-type functions for the Command Line Interface
   mode of the "tsWxGTUI" Toolkit.

   It provides a theme-based mechanism for modifying/
   restoring configuration constants as appropriate for
   various users and their activities.

=================== tsDoubleLinkedList.py ==================

6. tsDoubleLinkedList.py

   Class to establish a representation of a linked list
   with forward and backward pointers.

====================== tsException.py ======================

7. tsException.py

   Class to define and handle error exceptions. Maps run
   time exception types into 8-bit exit codes and prints
   associated diagnostic message and traceback info. 

================= tsGistGetTerminalSize.py =================

8. tsGistGetTerminalSize.py

   Third-Party Module, derived from "terminalsize.py" by
   Justin T. Riley, for acquiring the character size of the
   Python console window as tuple (width, height) on host
   operating systems (such as Linux, Mac OS X, Microsoft
   Windows and Unix). 

======================== tsLogger.py =======================

9. tsLogger.py

   Class that emulates a subset of Python logging API. It
   defines and handles prioritized, time and date stamped
   event message formatting and output to files and devices.
   Files are organized in a date and time stamped directory
   named for the launched application. Unix-type devices
   include syslog, stderr, stdout and stdscr (the ncurses
   display screen). It also supports "wxPython"-style log-
   ging of assert and check case results.

================ tsOperatorSettingsParser.py ===============

10. tsOperatorSettingsParser.py

    Class to parse the command line entered by the oper-
    ator of an application program.

    Parsing extracts the Keyword-Value pair Options and
    Positional Arguments that will configure and control
    the application during its execution.

    Typical syntax:

        python myApplication.py \
           [OPTION]...          \
           [ARGUMENT]...

    Typical examples:

        ./myApplication.py
        python myApplication.py
        python myApplication.py -h
        python myApplication.py --help
        python myFileCopier.py source.py target.py

    The standard Python library module ("argparse", "opt-
    parse" or "getopt"), appropriate for the active Python
    version provides the basic parsing algorithm, unless
    the operator includes one of the following library
    module names ("optparse" or "getopt") as the last
    positional argument.

    An application-specific configuration method provides
    the algorithm-specific definition of valid keyword-
    value pair options and/or positional arguments.

    Upon input of an operator help request, the algorithm
    displays the expected GNU/POSIX command line syntax
    and usage help. Upon detecting an operator input
    syntax error, the algorithm displays an error message
    and usage help.

    When used with Python 2.7 or Python 3.2, the "tsOper-
    ator-Settings.py" module (a "tsLibCLI" component of
    the "tsWXGTUI" Toolkit) supports the current and
    legacy Python version specific parser module(s) as
    an experimental and educational opportunity.

============== tsPlatformRunTimeEnvironment.py =============

11. tsPlatformRunTimeEnvironment.py

    Class to capture current hardware, software and
    network information about the run time environment
    for the user process. It makes this information
    available via a file (default is "./PlatformRun
    TimeEnvironment.txt").

    Host processor hardware support includes various
    releases of Arm, x86, PowerPC, SPARC and others.

    Host operating system software support includes
    various releases of Cygwin, Linux ('Debian',
    'OpenSUSE', 'RedHat', and Ubuntu), Mac OS X, Unix
    ('FreeBSD', 'OpenSolaris', 'PC-BSD'), Windows
    ('8.1', '8', '7', 'XP') and others.

    Host virtual machine software support includes
    various releases of Java and Python.

    Network identification support includes host name,
    aliases and ip-address list.

    Environment Variable support includes user, ses-
    sion, shell, path and time zone.

==================== tsReportUtility.py ====================

11. tsReportUtility.py

    Class defining methods used to format information:
    date and time (begin, end and elapsed), file size
    (with kilo-, mega-, giga-, tera-, peta-, exa-,
    zeta- and yotta-byte units) and nested Python dic-
    tionaries for display to an operator. It includes
    the following methods:

    displayDictionary - Recursive method to display
    nested entries in configuration dictionary.

    getByteCountStrings - Return a tupple with the text
    representations of a value.

    getDateAndTimeString - Construct timestamp string
    (in "Date at Time" format).

    getDateTimeString - Construct timestamp string
    suitable for use as label or alternatively for use
    as filename.

    getDayHourMinuteSecondString - Convert time from
    seconds to string format.

    getDictionaryKeyTypeList - Return a sorted list
    containing the key type in the specified diction-
    ary.

    getElapsedTimeString - Construct elapsed time in
    days, hours, minutes, seconds between supplied
    startup and current time inputs in seconds since
    the UNIX epoch.

    getHourMinuteSecondString - Construct elapsed time
    in days, hours, minutes, seconds between supplied
    startup and current time inputs in seconds since
    the UNIX epoch.

    getIndentString - Construct a string of white space
    appropriate for indenting level.

    getNextPathName - Construct the path to the next
    log file.

    getSecondsTimeFromHoursMinutesSecondsString - Con-
    vert time from string to seconds format.

    getSelectedDictionaryEntries - Return a dictioanry
    containing the specified type of entries from the
    specified dictionary.

    getSeparatorString - Construct a string of title
    and white space to separate one section of text
    from another.

    getStatisticsList - Create test summary after
    elapesed time and statistics details on the number
    of test runs, number of passing test runs, number
    of failing test runs, startup timestamp, shutdown
    timestamp and elapsed timestamp.

    getTimeStatisticsList - Generate Startup, Current
    (or Shutdown) and Elapsed Time strings.

    getYearMonthDayString - Construct date string (in
    "Year-Month-Day" format) from time in seconds since
    UNIX epoch.

====================== tsSysCommands.py =====================

12. tsSysCommands.py

    Class definition and methods for issuing shell
    commands to and receiving responses from the
    host operating system.

    It wraps and uses appropriate Python subprocess
    module methods.

======================= End-Of-File ========================
