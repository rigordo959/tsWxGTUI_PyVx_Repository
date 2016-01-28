#-----------------------------------------------------------
#"Time-stamp: <05/20/2015  6:24:21 AM rsg>"
#-----------------------------------------------------------

================ File: $README-ManPages.txt ================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find this and other files in the following
   Toolkit subdirectories:

       <Your Working Repository>
       (e.g. "Technical_Preview") 
         |
         +-- ["$Documents"]
         |
         +-- ["$ManPages"]
         |     |
         |     |  Deliverable Toolkit manual pages are a
         |     |  form of online software documentation
         |     |  usually found on a Unix or Unix-like oper-
         |     |  ating system.
         |     |
         |     |  Topics covered include computer programs
         |     |  (including library and system calls),
         |     |  formal standards and conventions, and even
         |     |  abstract concepts.
         |     |
         |     |  A user may NOT invoke a man page by issu-
         |     |  ing the man command. Instead, a user may
         |     |  display a man page by issuing the
         |     |  less <man document file> command.
         |     |
         |     +-- ["tsManPagesLibCLI"]
         |     +-- ["tsManPagesLibGUI"]
         |     +-- ["tsManPagesTestsLibCLI"]
         |     +-- ["tsManPagesTestsLibGUI"]
         |     +-- ["tsManPagesTestsToolsLibCLI"]
         |     +-- ["tsManPagesTestsToolsLibGUI"] (Future)
         |     +-- ["tsManPagesToolsCLI"]
         |     +-- ["tsManPagesToolsGUI"]         (Future)
         |     +-- ["tsManPagesUtilities"]        (Future)
         |
         +-- ["$Notebooks"]
         |
         +-- ["$SourceDistributions"]

===================== TABLE OF CONTENTS ====================

1. ["$ManPages"]

2. How to create and install a manpage (Future)

====================== ["$ManPages"] ======================

1. ["$ManPages"]

   The following defines the purpose and use of a set of
   on-line reference documents. This Toolkit provides
   utility scripts that:

   a) create rudimentary ManPages from source code;

   b) do NOT yet merge Toolkit ManPages with ManPages
      installed by the host computer operating system or
      with the installation of other third-pary add-ons.

   Excerpt From Wikipedia, the free encyclopedia:

   "A man page (short for manual page) is a form of online
   software documentation usually found on a Unix or Unix-
   like operating system. Topics covered include computer
   programs (including library and system calls), formal
   standards and conventions, and even abstract concepts.
   A user may invoke a man page by issuing the man command.

   By default, man typically uses a terminal pager program
   such as more or less to display its output.

   Usage

   To read a manual page for a Unix command, type:

      man <command_name>

   Pages are traditionally referred to using the notation
   "name(section)": for example, ftp(1). The same page name
   may appear in more than one section of the manual, such
   as when the names of system calls, user commands, or
   macro packages coincide. Examples are man(1) and man(7),
   or exit(2) and exit(3).

   The syntax for accessing the non-default manual section
   varies between different man implementations. On Solaris,
   for example, the syntax for reading printf(3C) is:

      man -s 3c printf

   On Linux and BSD derivatives the same invocation would
   be:

      man 3 printf

   which searches for printf in section 3 of the man pages."

========== "How to create and install a manpage" ===========

2. How to create and install a manpage (Future)

   The following may be useful for a future Toolkit enhance-
   ment.

   Excerpts from Googe Search:

   "HowTo: Linux / UNIX Create a Manpage - nixCraft
   www.cyberciti.biz/faq/linux-unix-creating-a-manpage/
   May 6, 2010 - How do I create a man page for my shell
    or python script under Linux / UNIX ... 
    install -g 0 -o 0 -m 0644 nuseradd.1 /usr/local/man/man8/ gzip ...

   How to create a manpage? - Ask Ubuntu
   askubuntu.com/questions/42923/how-to-create-a-manpage
   Ask Ubuntu
   May 15, 2011 - With the help of Gmanedit · Install
   gmanedit you are able to create manpages with a
   graphical GUI. Gtk+ Manpages Editor is an editor for man ...

   Linux Man Page Howto - Who is Jens Schweikhardt?
   www.schweikhardt.net/man_page_howto.html
   The next decision is the directory in which it will
   finally be installed (say, when the user runs ` make
   install ' for your package.) On Linux, all man pages
   are below ...

   Linux Howtos: System -> Creating Your Own MAN Page
   www.linuxhowtos.org/system/creatingman.htm
   We will be using groff macros to create our manual page.
   These macros always ... Normally you put the version
   number of your program here. [center header]

   How can I add man page entries for my own power tools?
   unix.stackexchange.com/.../how-can-i-add-man-page-ent...
   Stack Exchange
   Feb 4, 2011 - I have no idea about how I can make my
   home-grown specialist scripts ... and you can create
   a man page from the POD file with the pod2man ... You
   can then optionally (b|g)zip it and put it in the
   appropriate man directory.

   How to add entry in Linux man page database - Stack ...
   stackoverflow.com/.../how-to-add-entry-in-linux-
   man-page-database
   Dec 25, 2012 - I have a manual page for mongoose web
   server named as mongoose.1 as a result of doing make
   and make install command to install ...

   How should a formatted man page look?
   www.tldp.org/HOWTO/Man-Page/q3.html
   Linux Documentation Project
   Here comes the man page for the (hypothetical)
   foo program. ... However, if you install using
   'make prefix=/opt/gnu' the references in the man
   page change to ..."

======================= End-Of-File ========================
