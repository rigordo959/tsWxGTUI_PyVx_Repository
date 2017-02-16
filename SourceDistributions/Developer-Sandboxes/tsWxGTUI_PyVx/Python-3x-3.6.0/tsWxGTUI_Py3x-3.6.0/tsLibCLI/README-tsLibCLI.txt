#"Time-stamp: <03/15/2015  2:12:19 AM rsg>"

================ File: $README-tsLibCLI.txt ================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./Documents/tsDevelopers".

===================== TABLE OF CONTENTS ====================

1. Package Organization
2. tsApplicationPkg
3. tsCommandLineEnvPkg
4. tsCommandLineInterfacePkg
5. tsCxGlobalsPkg
6. tsDoubleLinkedListPkg
7. tsExceptionPkg
8. tsLoggerPkg
9. tsOperatorSettingsParserPkg
10. tsPlatformRunTimeEnvironmentPkg
11. tsReportUtilityPkg
12. tsSysCommandsPkg
13. Bug List
14. To-Do List


=================== PACKAGE ORGANIZATION ===================

1. Package Organization

  The library of building blocks is organized, by the
  functional scope of each component, into a collection of
  "packages". When appropriate, any package may import and
  use the services of any other tsLibCLI package.
  
  Source code is contained in the associated ["src"] sub-
  directory. Depending on its complexity, the source code
  of a package may also be sub-divided and organized into
  a set of one or more source files.
  
  Unit/Integration Test code is contained in the associated
  ["test"] sub-directory. Depending on its complexity, the
  test code of a package may also be sub-divided and organ-
  ized into a set of one or more test files.

===================== tsApplicationPkg =====================

2. tsApplicationPkg
  
   2.1 tsApplication.py

       Base class to initialize and configure the applica-
       tion program launched by an operator. It enables an
       application launched via a Command Line Interface (CLI)
       to initialize, configure and use the same character-
       mode terminal with a Graphical-style User Interface
       (GUI).

       Registers and validates instantiation settings input
       from applications via caller parameter list.

       It also registers and validates operator application
       settings inputs from command line keyword-value pairs
       and positional arguments.

==================== tsCommandLineEnvPkg ===================

3. tsCommandLineEnvPkg
  
   3.1 tsCommandLineEnv.py

       Class to initialize and configure the application
       program launched by an operator. It delivers those
       keyword-value pair options and positional arguments
       specified by the application, in its invocation
       parameter list. It wraps the Command Line Interface
       application with exception handlers to control exit
       codes and messages that may be used to coordinate
       other application programs.

       Establishes the command line environment for the ap-
       plication. Its services include platform configura-
       tion, initialization, input/output supervision and
       the application launcher.

================= tsCommandLineInterfacePkg ================

4. tsCommandLineInterfacePkg

   4.1 tsCommandLineInterface.py

       Class establishes methods that prompt or re-prompt
       the operator for input, validate that the operator
       has supplied the expected number of inputs and that
       each is of the expected type.

======================= tsCxGlobalsPkg =====================

5. tsCxGlobalsPkg

   5.1 tsCxGlobals.py

       Module to establish configuration constants and
       macro-type functions for the Command Line Interface
       mode of the "tsWxGTUI" Toolkit.

       It provides a centralized mechanism for modifying/
       restoring those configuration constants that can be
       interogated at runtime by those software components
       having a "need-to-know". The intent being to avoid
       subsequent searches to locate and modify or restore
       a constant appropriate to the current configuration.

       It also provides a theme-based mechanism for modify-
       ing/restoring those configuration constants as appro-
       priate for various users and their activities.

=================== tsDoubleLinkedListPkg ==================

6. tsDoubleLinkedListPkg

   6.1 tsDoubleLinkedList.py

       Class to establish a representation of a linked list
       with forward and backward pointers.

====================== tsExceptionPkg ======================

7. tsExceptionPkg

   7.1 tsException.py

       Class to define, categorize and handle error excep-
       tions.

       It wraps standard and application-specific error
       exception handlers to facilitate co-ordination of
       multiple application processes.

       It maps run time exception types into 8-bit exit
       codes and prints associated diagnostic messages and
       traceback info. 

======================== tsLoggerPkg =======================

8. tsLoggerPkg

   8.1 tsLogger.py

       Class that emulates a subset of Python logging API.

       It defines and handles prioritized, time and date
       stamped event message formatting and output to files
       and devices.

       Files are organized in a date and time stamped direc-
       tory named for the launched application. 

       Unix-type devices include syslog, stderr, stdout and
       stdscr (the curses display screen).

       It also supports "wxPython"-style logging of assert and
       check case results.

================ tsOperatorSettingsParserPkg ===============

9. tsOperatorSettingsParserPkg

   9.1 tsOperatorSettingsParser.py

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

      However, when one seeks to backport applications to
      Python 1.0-1.6 or to Python 2.0-2.6 or Python 3.0-3.1,
      the "tsOperatorSettings.py" module must be stripped of
      unsupported Python version specific parser modules in
      order to prevent a program trap which will block the
      application from running.

============== tsPlatformRunTimeEnvironmentPkg =============

10. tsPlatformRunTimeEnvironmentPkg

    10.1 tsPlatformRunTimeEnvironment.py

         Class to capture current hardware, software and
         network information about the run time environment
         for the user process.

         This package tries to retrieve as much platform-
         identifying data as available. Its goal is to
         capture current hardware, software and network
         information about the run time environment for a
         user process. It makes this information available
         via a file (default is "./PlatformRunTimeEnviron-
         ment.txt").

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

    10.2 tsGistGetTerminalSize.py

         Module for acquiring the character size of the
         Python console window as tuple (width, height) on
         host operating systems (such as Linux, Mac OS X,
         Microsoft Windows and Unix).

         Derived from: "https://gist.github.com/jtriley/
         1108174" by Justin T. Riley, created "terminal-
         size.py" for gist 2011-07-26T14:59:00-07:00. 

==================== tsReportUtilityPkg ====================

11. tsReportUtilityPkg

    11.1 tsReportUtility.py

         Class defining methods used to format information:
         date and time (begin, end and elapsed), file size
         (with kilo-, mega-, giga-, tera-, peta-, exa-,
         zeta- and yotta-byte units) and nested Python dic-
         tionaries for display to an opeator. It includes
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

====================== tsSysCommandsPkg =====================

12. tsSysCommandsPkg

    12.1 tsSysCommands.py

         Class definition and methods for issuing shell
         commands to and receiving responses from the
         host operating system.

         It wraps and uses appropriate Python subprocess
         module methods.

======================= End-Of-File ========================
