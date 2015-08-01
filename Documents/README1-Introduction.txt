#-----------------------------------------------------------
#"Time-stamp: <07/07/2015  8:17:02 PM rsg>
#-----------------------------------------------------------

============== File: README1-Introduction.txt ==============

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
         +-- ["Documents"]
         |     |
         |     |  This directory contains a collection of files
         |     |  which provide the Toolkit recipient with an
         |     |  understanding of the purpose, goals & capabil-
         |     |  ities, non-goals & limitations, terms & condi-
         |     |  tions and procedures for installing, operating,
         |     |  modifying and redistributing the Toolkit. 
         |     :
         |     :
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
         |     :
         |     :
         |     +-- "TROUBLESHOOT.txt"
         |
         +-- "README.txt"

===================== TABLE OF CONTENTS ====================

1. What is it?

   1.1 In a Nutshell
   1.2 The Gory Details

2. How is it implemented?

   2.1 Python Programming Language
   2.2 Python-based Command Line Interface (CLI)
   2.3 "wxPython"-style Graphical-Text User Interface (GUI)

3. What are the System Requirements?

   3.1 Hardware
   3.2 Software

4. The Latest Versions

   4.1 "tsWxGTUI_Py2x-0.0.0" for Python 2.4.1 - 2.7.9
   4.2 "tsWxGTUI_Py3x-0.0.0" for Python 3.0.0 - 3.4.3

5. Deliverables

   5.1 Documentation
   5.2 Source Code

6. Installation

7. Licensing

8. Contacts

9. Acknowledgments

======================== WHAT IS IT? =======================

1. What is it?

   The "tsWxGTUI" Toolkit provides a collection of building-
   block components, tools, utilities, and tests.

   The Toolkit facilitates the effort of software developers
   creating enhanceing, troubleshooting, maintaining and sup-
   porting application programs with character-mode Command
   Line and Graphical-style User Interfaces that are suitable
   for the local and remote monitoring and control of computer
   systems that are embedded in mission-critical equipment.

   1.1 In a Nutshell

       The TeamSTARS "tsWxGTUI_PyVx" Toolkit software is
       engineered to facilitate the development and use of
       application programs with the following features:

       1.1.1 User-friendly Interfaces:

             a. Command Line Interface (CLI)

                Output to the user of a chronological se-
                quence of lines of text via a scrolling
                computer terminal display with input from
                the user via a computer terminal keyboard.

             b. Graphical-style User Interface (GUI)

                Output to the user of character strings to
                application-specified column and row (line)
                fields of a computer terminal display with
                input from the user via a computer terminal
                keyboard and pointing device (such as mouse,
                trackball, touchpad or touchscreen).

       1.1.2 General-purpose, portability, maintainability,
             re-usability, scalablility, deployability:

             a. Toolkit Applications

                Software development and installation tool-
                kit for automation, communication, control,
                diagnostic, instrumentation and simulation
                applications.

             b. Usage Applications

                Computerized mainframe, workstation, desk-
                top, laptop, tablet and embedded systems
                with 32-bit/64-bit processors from various
                manufacturers and popular operating systems
                including GNU/Linux, Mac OS X, Microsoft
                Windows and Unix.

   1.2 The Gory Details

       Software development systems typically have suffi-
       cient and upgradable resources including 32-bit/
       64-bit processors, random access memory, non-volatile
       memory (such as electro-mechanical hard drives and
       electronic flash memory), network interface devices
       and operator control consoles with keyboard, mouse
       and large high-cost pixel-mode/graphics-mode displays
       that can also operate in character-mode/text-mode.

       Embedded systems typically are optimized for specific
       commercial, industrial, medical and military applica-
       tions. The more capable systems have 32-bit/64-bit
       processors, random access memory, non-volatile mem-
       ory, network interface devices and operator control
       consoles with keyboard, mouse and small low-cost
       character-mode/text-mode displays.

       The Toolkit provides utilities, tools and a library
       of building blocks for you to create application
       programs that can raise the productivity and reduce
       the applied time of software developers and main-
       tainers by its use of the high-level Python program-
       ming language.

       It can also raise the productivity of system admin-
       istrators, software developers, equipment operators
       and field service personnel by providing a suitable
       user-friendly interface:

       1.2.1 A Command Line Interface (CLI)

             Please see encyclopedia-based information at:

                    http://en.wikipedia.org/wiki/
                           Command-line_interface

       1.2.2 A Text-based User Interface (TUI)

             The Text-based User Interface (TUI) emulates a sub-
             set of the Application Programming Interface (API)
             for wxPython, a popular cross-platform Graphical
             User Interface (GUI). The baseline API for the TUI
             os that of wxPython 2.8.9.2. Once development has
             been completed, the API can be updated to track
             the latest wxPython version.

             Please see encyclopedia-based information at:

                http://en.wikipedia.org/wiki
                       /Text-based_user_interface

                http://en.wikipedia.org/wiki
                       /Graphical_user_interface

             It can raise overall productivity through its abil-
             ity to monitor remote computer systems and associ-
             ated equipment from the convenience of a local
             centralized computer system.

             The network communication speed of character data
             will be faster than that of pixel data because:

             1. There would be more pixels than character cells
                involved in programmatic change. For example, on
                a 307,200 (640x480) pixel display, there are
                only 3,200 (80 cols x 40 rows) character cells
                when using a 96 (8x12) pixel font.

             2. There would only be 1 byte involved in the fol-
                lowing programmatic character cell changes:

                a) Which of the 256 text characters, and pre-
                   assigned 96 (8x12) pixel combinaions, to
                   apply to individual character cells.

                b) Which of the 256 (16x16) color pairs, and
                   pre-assigned 256x256x256 red-green-blue
                   foreground color intensity levels, and
                   256x256x256 red-green-blue background
                   color intensity levels to apply to indi-
                   vidual strings of one or more character
                   cells.

                c) Which of the 8 text character attribute
                   combinations (alternate character set,
                   blink mode, bold mode, dim mode, normal
                   attribute, reverse background and fore-
                   ground colors, standout mode and underline
                   mode) to apply to individual strings of one
                   or more character cells.

             3. Alterative Solutions

                a) The Java programming language user community
                   has access to a small footprint console in-
                   terface.

                   See "http://www.codeproject.com/Articles/328417/
                              Java-Console-apps-made-easy"

                   In the absence of any statement about char-
                   acter-mode, it is presumed that the Java
                   console operates only in pixel-mode.

                b) The wxWidgets 3.0 C++ programming language
                   user community has access to a set of console
                   interface classes that were not in wxWidgets
                   2.8 or 2.9.

                   See "http://docs.wxwidgets.org/trunk/
                               classwx_app_console.html"

                   In the absence of any statement about char-
                   acter-mode, it is presumed that the set of
                   "wxWidgets 3.0" console interface classes
                   operate only in standard pixel-mode.

                c) "Urwid"

                   Excerpt from "http://urwid.org/manual/
                                        overview.html"

                   "Urwid is a console user interface library for
                   Python. Urwid offers an alternative to using
                   Python's curses module directly and handles
                   many of the difficult and tedious tasks for you.

                   ../_images/introduction.png

                   Each Urwid component is loosely coupled and
                   designed to be extended by the user.

                   Display modules are responsible for accepting
                   user input and converting escape sequences to
                   lists of keystrokes and mouse events. They
                   also draw the screen contents and convert
                   attributes used in the canvases rendered to
                   the actual colors that appear on screen.

                   The included widgets are simple building blocks
                   and examples that try not to impose a particular
                   style of interface. It may be helpful to think
                   of Urwid as a console widget construction set
                   rather than a finished UI library like GTK or
                   Qt. The Widget base class describes the widget
                   interface and widget layout describes how widgets
                   are nested and arranged on the screen.

                   Text is the bulk of what will be displayed in
                   any console user interface. Urwid supports a
                   number of text encodings and Urwid comes with
                   a configurable text layout that handles the
                   most of the common alignment and wrapping modes.
                   If you need more flexibility you can also write
                   your own text layout classes.

                   Urwid supports a range of common display attri-
                   butes, including 256-color foreground and back-
                   ground settings, bold, underline and standount
                   settings for displaying text. Not all of these
                   are supported by all terminals, so Urwid helps
                   you write applications that support different
                   color modes depending on what the user's term-
                   inal supports and what they choose to enable."

                   <additional info not reproduced>

                d) "npyscreen"

                   Excerpts from "https://code.google.com/p/npyscreen/"

                   "Npyscreen is a python widget library and appli-
                   cation framework for programming terminal or
                   console applications. It is built on top of
                   ncurses, which is part of the standard library."

                   <additional info not reproduced>

                   "Strengths

                   This framework should be powerful enough to create
                   everything from quick, simple programs to complex,
                   multi-screen applications. It is designed to make
                   doing the simple tasks very quick and to take much
                   of the pain out of writing larger applications.

                   There is a very wide variety of default widgets - 
                   everything from simple text fields to more complex
                   tree and grid views.

                   The framework is easy to extend. That said, if
                   you have a requirement for a widget that is not
                   currently included you can try emailing me and
                   I'll see whether I have time to help - no
                   promises!"

================== HOW IS IT IMPLEMENTED? ==================

2. How is it implemented?

   2.1 Python Programming Language

       From https://docs.python.org/3/faq/general.html
       From https://docs.python.org/2/faq/general.html

       "What is Python:

          Python is an interpreted, interactive, object-
          oriented programming language. It incorporates
          modules, exceptions, dynamic typing, very high
          level dynamic data types, and classes. Python
          combines remarkable power with very clear syntax.
          It has interfaces to many system calls and librar-
          ies, as well as to various window systems, and is
          extensible in C or C++. It is also usable as an
          extension language for applications that need a
          programmable interface. Finally, Python is port-
          able: it runs on many Unix variants, on the Mac,
          and on PCs ..."

          Python 3x and 2x for 32-bit and 64-bit processors:

            "... on Windows 2000 and later."

          Python 2x for 16-bit and 32-bit processors:

            "... under MS-DOS, Windows, Windows NT, and OS/2."

          Python 1x for 16-bit and 32-bit processors

            System requirements are no longer available.

       From http://ftp.python.org/download/releases/1.6.1/

           "Python 1.6 was the last of the versions developed
           at [the Corporation for National Research Initiatives]
           CNRI and the only version issued by CNRI with an
           open source license. Following the release of Python
           1.6, and after Guido van Rossum left CNRI to work
           with commercial software developers, it became clear
           that the ability to use Python with software available
           under the GNU General Public License (GPL) was very
           desirable. CNRI and the Free Software Foundation (FSF)
           interacted to develop enabling wording changes to the
           Python license. Python 1.6.1 is essentially the same
           as Python 1.6, with a few minor bug fixes, and with a
           GPL-compatible license."

       2.1.1 The high-level Python programming language is
             used to implement the TeamSTARS "tsWxGTUI_PyVx"
             Toolkit.

             The TeamSTARS "tsWxGTUI_PyVx" Toolkit's building
             block and tool components import and use run
             time library components from the Python Global
             Module Index and from Python user-installed
             site-packages.

             Python is a popular, field proven, portable,
             cross-platform programming language.

             Please see encyclopedia-based Python information at:

               http://en.wikipedia.org/wiki
                      /Python_(programming_language)

   2.2 Python-based Command Line Interface (CLI)

       2.2.1 The TeamSTARS "tsWxGTUI_PyVx" Toolkit's Command
             Line Interface building block components import
             and use the Keyword-Value Pair and Positional
             argument parsers:

             Please see Python Global Module Index-based
             information at:

               http://docs.python.org/3/library
                      /argparse.html

               http://docs.python.org/2/library
                      /optparse.html

               http://docs.python.org/2/library
                      /getopt.html

             Availablility:

             a) "argparse"

                Introduced in Python 2.7 and Python 3.2.

             b) "optparse"

                Introduced in Python 2.3 (deprecated in
                Python 2.7) and Python 3.0 (deprecated
                in Python 3.2).

             c) "getopt"

                Available in Python 1.6, 2.0 and Python 3.0.

   2.3 "wxPython"-style Graphical-Text User Interface (GUI)

       1.3.1 The TeamSTARS "tsWxGTUI_PyVx" Toolkit's Text-
             based User Interface components import and use
             the Terminal handler ("curses") for character-
             cell displays available in Python's Global
             Module Index.

             It uses "curses" to emulate a subset of the
             Application Programming Interface (API) of
             "wxPython", a wrapper to the popular
             "wxWidgets" pixel-mode, cross-platform
             Graphical User Interface Toolkit which is
             implemented in the C++ programming language.

             The "wxPython" emulation retains the pixel-
             mode parameters of the "wxPython" API and
             mimics the look and feel of Microsoft
             "Windows XP" Displays which are similar to
             those of Linux "GTK+" Displays:

             a) GUI container features such as frames,
                dialogs and panels and buttons to close,
                iconize and maximize/restore the container.

             b) GUI control features such as buttons,
                checkboxes, radio buttons, scroll bars,
                scroll lists and status bars.

             c) GUI layout features such as box sizer
                and grid sizer.

             d) GUI operator notification features such
                as a scrolling log of date and time stamped
                event notification messages.

             e) GUI desktop features such as task bar
                buttons to control GUI container focus.

             Please see encyclopedia-based information at:

                http://en.wikipedia.org/wiki/WxPython

                http://en.wikipedia.org/wiki/WxWidgets

                http://en.wikipedia.org/wiki/GTK%2B

             Please see Python Global Module Index-based
             information at:

                http://docs.python.org/2/library
                       /curses.html

                http://docs.python.org/3/library
                       /curses.html

============= WHAT ARE THE SYSTEM REQUIREMENTS? ============

3. What are the System Requirements?

   The design of the TeamSTARS "tsWxGTUI_PyVx" Toolkit sup-
   ports a wide range of possible system configurations.

   Cross-platform Python virtual machine technology is often
   available for Intel and non-Intel 32-bit and 64-bit pro-
   cessor based systems running proprietary and non-proprie-
   tary operating systems.

   For example, Toolkit development and testing has involved
   the following system configurations:

   3.1 Hardware

       The TeamSTARS "tsWxGTUI_PyVx" Toolkit development and
       testing platforms have involved three classes of
       equipment represented by the following:

       a. Minimal Usability and Performance

          1998-model year, 366 MHz Intel Pentium II-based
          Dell Inspiron 7000 laptop with 384 MB RAM, 640x480/
          1024x768 pixel resolution display and dual PCMIA
          Card expansion capabilities for network and periph-
          eral device interfaces (with marginal resources and
          performance) sufficient enough to serve as the low-
          end, single user baseline development and operator
          platform.

          Its interchangeabble 32 GB (4200 RPM) ATA hard
          drives were used to run either:

          * Microsoft Windows Desktop with Cygwin, the free
            GNU/Linux-like Plug-in from Red Hat (XP Pro); or

          * Ubuntu GNU/Linux Desktop (12.04)

          The platform's limited memory and available PCMCIA
          network adapters were incompatible with later ver-
          sions of Windows or with other Linux distributions.
          (Windows XP recongnized Xircom Ethernet and 3Com
          Wireless adapters; Ubuntu Linux 12.04 recognized
          only Linksys Wireless adapter.

       b. Moderate Usability and Performance

          2007-model year, 2.33 GHz Intel Core 2 Duo
          processor-based Apple 17" MacBook Pro laptop with
          4 GB RAM, 1920x1200 pixel resolution display and
          sufficient performance, resources and expansion
          capabilities to serve as the mid-range, single
          user baseline development and operator platform.

          Its 160 GB (5400 RPM) SATA 1.5 Gb/s internal
          hard drive was used to run Apple's Mac OS X 10.7
          and the hypervisor virtualization applications
          (Parallels Desktop 8 and VMware Fusion 5) that
          supported various guest operating systems.

          Its 1.5 TB (7200 RPM) SATA 3 Gb/s external hard
          drive was used to store and concurrently run an
          assortment of up to two configured versions se-
          lected (for normal use rather than for stress-
          testing) from the following guest operating
          systems:

          * Fedora GNU/Linux Desktop (17)

          * Ubuntu GNU/Linux Desktop (12.04)

          * Microsoft Windows Desktop with Cygwin, the free
            GNU/Linux-like Plug-in from Red Hat
            (XP Pro, 7 Pro, 8 Pro and 8.1 Pro)

          * OpenIndianna (OpenSolaris 11-based) Unix Desktop
            (151a6)

          NOTEs:

          1) A Seagate ST31500341AS 1.5TB SATA 7200 RPM was
             used as the external hard drive. The wear and
             tear from using a consumer product (over 8-10
             hours a day, 7 days each week for 7 years) for
             the Guest Operating System swapfile and data
             storage ultimately wore it out (unrecoverable
             disk head crash).

          2) Subsequent research indicated that a more
             appropriate hard drive would have been be an
             Hitachi Ultrastar 7K3000 HUA723020ALA641 2TB
             7200RPM 64MB Cache SATA 6.0Gb/s 3.5" Enterprise
             Hard Drive -OEM.

       c. High Usability and Performance

          2013-model year, 3.5 GHz Intel Quad Core i7 proces-
          sor-based Apple 27" iMac desktop with 16 GB RAM,
          2560x1440 pixel resolution display and sufficient
          performance, resources and expansion capabilities
          to serve as the high-end, multi-user baseline de-
          velopment and operator platform.

          Its 3 TB (7200 RPM) SATA 6 Gb/s internal hard drive
          had 128 GB Solid State Flash memory and was used to
          run Apple's Mac OS X 10.9-10.10 and the hypervisor
          virtualization applications (Parallels Desktop 9-10
          and VMware Fusion 5 an 7) that supported various guest
          operating systems.

          Its 3 TB (7200 RPM) SATA 6 Gb/s internal hard drive
          was normally used to store and concurrently run an
          assortment of up to four configured versions selected
          (for normal use rather than for stress-testing) from
          the following guest operating systems:

          * CentOS GNU/Linux Desktop (7.0)

          * Debian GNU/Linux Server (13.0)
            Configures with Apache, Bugzilla and MySQL.

          * Fedora GNU/Linux Desktop (20-22)

          * OpenSuSE GNU/Linux Desktop (13.1)

          * Scientific GNU/Linux Desktop (6.5 & 7.0)

          * Ubuntu GNU/Linux Desktop (12.04 & 14.04)

          * Microsoft Windows Desktop with Cygwin, the free
            GNU/Linux-like Plug-in from Red Hat
            (XP Pro, 7 Pro, 8 Pro, 8.1 Pro and
            10 Technical Preview)

          * PC-BSD (FreeBSD-based) Unix Desktop (9.2 & 10.0)

          * OpenIndianna (OpenSolaris 11-based) Unix Desktop (151a8)

   3.2 Software

       The TeamSTARS "tsWxGTUI_PyVx" Toolkit development and
       testing platforms have involved an assortment of single
       and multi-user, mult-process and multi-threaded POSIX-
       compatible operating system releases.

       The following operating system information consists of
       annotated excerpts From Wikipedia, the free encyclope-
       dia, in order to preserve a snapshot of relevant con-
       tent that might otherwise be subject to change and
       lose relevance:

       a. GNU/Linux

          GNU is a Unix-like computer operating system devel-
          oped by the GNU Project, ultimately aiming to be a
          "complete Unix-compatible software system" composed
          wholly of free software.

          Linux is a Unix-like and mostly POSIX-compliant com-
          puter operating system assembled under the model of
          free and open-source software development and dis-
          tribution. The defining component of Linux is the
          Linux kernel, an operating system kernel first re-
          leased on 5 October 1991 by Linus Torvalds. The Free
          Software Foundation uses the name GNU/Linux to
          describe the operating system, which has led to some
          controversy.

          Many computer users run a modified version of the
          GNU system every day, without realizing it. Through
          a peculiar turn of events, the version of GNU which
          is widely used today is often called "Linux", and
          many of its users are not aware that it is basically
          the GNU system, developed by the GNU Project.

          Please see encyclopedia-based information at:

             http://en.wikipedia.org/wiki/GNU
             http://en.wikipedia.org/wiki/Linux
             http://en.wikipedia.org/wiki/Linux_kernel

          * CentOS, a distribution derived from the same
            sources used by Red Hat, maintained by a dedi-
            cated volunteer community of developers with
            both 100% Red Hat-compatible versions and an
            upgraded version that is not always 100%
            upstream compatible. (7.0)

          * Debian, a non-commercial distribution and one of
            the earliest, maintained by a volunteer developer
            community with a strong commitment to free soft-
            ware principles and democratic project management

          * Fedora, a community distribution sponsored by
            American company Red Hat. (17-22)

          * OpenSuSE, a community distribution mainly spon-
            sored by German company SuSE. (13.1)

          * SuSE Linux Enterprise, derived from openSuSE, is
            maintained and commercially supported by SuSE.

          * Red Hat Enterprise Linux, a derivative of Fedora,
            maintained and commercially supported by Red Hat

          * Scientific, a Linux distribution produced by
            Fermi National Accelerator Laboratory. It is a
            free and open source operating system based on
            Red Hat Enterprise Linux and aims to be "as
            close to the commercial enterprise distribution
            as we can get it.". (6.5 and 7.0)

            This product is derived from the free and open
            source software made available by Red Hat, Inc.,
            but is not produced, maintained or supported by
            Red Hat. Specifically, this product is built from
            the source code for Red Hat Enterprise Linux
            versions, under the terms and conditions of Red
            Hat Enterprise Linux's EULA and the GNU General
            Public License.

          * Ubuntu, a popular desktop and server distribution
            derived from Debian, maintained by British company
            Canonical Ltd. (12.04 LTS and 14.04 LTS)

       b. Microsoft Windows, a metafamily of graphical operat-
          ing systems developed, marketed, and sold by Micro-
          soft. It consists of several families of operating
          systems, each of which cater to a certain sector of
          the computing industry. Active Windows families in-
          clude Windows NT, Windows Embedded and Windows
          Phone; these may encompass subfamilies, e.g. Windows
          Embedded Compact (Windows CE) or Windows Server.
          Defunct Windows families include Windows 9x and
          Windows Mobile.

          Microsoft Windows will only require "Cygwin", the
          free Linux-like plug-in from Red Hat for users of
          the "wxPython"-style, "Curses"-based Graphical-Text
          User Interface. (Home or Professional editions of
          Windows XP, 7, 8, 8.1, 10 Technical Preview)

          Microsoft introduced an operating environment named
          Windows on November 20, 1985 as a graphical operat-
          ing system shell for MS-DOS in response to the grow-
          ing interest in graphical user interfaces (GUIs).
          Microsoft Windows came to dominate the world's per-
          sonal computer market with over 90% market share,
          overtaking Mac OS, which had been introduced in
          1984. However, it is outsold by Android on smart-
          phones and tablets.

       c. OS X (formerly known as Mac OS X), a series of Unix-
          based graphical interface operating systems develop-
          ed and marketed by Apple Inc. It is designed to run
          on Mac computers. (10.4 "Tiger"-10.10 "Yosemite")

          NOTES: From http://en.wikipedia.org/wiki/OS_X

               "The first releases of Mac OS X from 1999 to
               2006 can run only on the PowerPC based Macs of
               the period. After Apple announced it would
               shift to using Intel x86 CPUs from 2006 onwards,
               Tiger and Leopard were released in versions for
               Intel and PowerPC processors. Snow Leopard is
               the first version released only for Intel Macs.
               Since the release of Mac OS X 10.7 "Lion", OS X
               has dropped support for 32-bit Intel processors
               as well. It now runs exclusively on 64-bit Intel
               CPUs."

               Mac OS X Version       PowerPC Platform
                                     (NOT tested with Toolkit)
               ---------------------  --------------------------
               10.0: "Cheetah"        (32-bit PowerPC)
               10.1: "Puma"           (32-bit PowerPC)
               10.2: "Jaguar"         (32-bit PowerPC)
               10.3: "Panther"        (32-bit PowerPC)
               10.4: "Tiger"          (32-bit PowerPC and Intel)
               10.5: "Leopard"        (32-bit PowerPC and Intel)
               
               Mac OS X Version       Intel Platforms
                                     (tested with Toolkit)
               ---------------------  --------------------------
               10.4: "Tiger"          (32-bit PowerPC and Intel)
               10.5: "Leopard"        (32-bit PowerPC and Intel)
               10.6: "Snow Leopard"   (32-bit Intel)
               10.7: "Lion"           (32-bit Intel)
               10.8: "Mountain Lion"  (64-bit Intel)
               10.9: "Mavericks"      (64-bit Intel)
               10.10: "Yosemite"      (64-bit Intel)

          Versions 10.5 "Leopard" running on Intel proces-
          sors, 10.6 "Snow Leopard", 10.7 "Lion", 10.8 "Moun-
          tain Lion", 10.9 "Mavericks", and 10.10 "Yosemite"
          have obtained UNIX 03 certification.

          iOS, which runs on the iPhone, iPod Touch, iPad, and
          the 2nd and 3rd generation Apple TV, shares the
          Darwin core and many frameworks with OS X.

       d. Unix, a multitasking, multiuser computer operating
          system that exists in many variants. The original
          Unix was developed at AT&T's Bell Labs research
          center by Ken Thompson, Dennis Ritchie, and others.
          From the power user's or programmer's perspective,
          Unix systems are characterized by a modular design
          that is sometimes called the "Unix philosophy,"
          meaning the OS provides a set of simple tools that
          each perform a limited, well-defined function,
          with a unified filesystem as the main means of com-
          munication and a shell scripting and command lan-
          guage to combine the tools to perform complex work-
          flows.

          * FreeBSD, a free Unix-like operating system de-
            scended from Research Unix via the Berkeley Soft-
            ware Distribution (BSD). Although for legal rea-
            sons FreeBSD cannot use the Unix trademark, it is
            a direct descendant of BSD, which was historically
            also called "BSD Unix" or "Berkeley Unix." (10.0)

          * OpenIndiana, a free and open-source, Unix operat-
            ing system derived from OpenSolaris. Developers
            forked OpenSolaris after Oracle Corporation dis-
            continued it, in order to continue development
            and distribution of the source code. The Open-
            Indiana project is stewarded by the illumos
            Foundation, which also stewards the illumos
            operating system. OpenIndiana's developers
            strive to make it "the defacto OpenSolaris
            distribution installed on production servers
            where security and bug fixes are required
            free of charge". (151a8)

          * OpenSolaris, a descendant of the UNIX System V
            Release 4 (SVR4) code base developed by Sun and
            AT&T in the late 1980s. It is the only version
            of the System V variant of UNIX available as
            open source.

          * PC-BSD, or PCBSD, a Unix-like, desktop-oriented
            operating system built upon the most recent re-
            leases of FreeBSD. It aims to be easy to install
            by using a graphical installation program, and
            easy and ready-to-use immediately by providing
            KDE SC, LXDE, Xfce, and MATE as the graphical
            user interface. (10.0)

==================== THE LATEST VERSIONS ===================

4. The Latest Versions

   The latest TeamSTARS "tsWxGTUI_PyVx" Toolkit version is a
   pre-alpha stage, pre-production release identitified as:

   4.1 "tsWxGTUI_Py2x-0.0.0" for Python 2.4.1 - 2.7.9
   4.2 "tsWxGTUI_Py3x-0.0.0" for Python 3.0.0 - 3.4.3

======================= DELIVERABLES =======================

5. Deliverables

   Deliverables for the TeamSTARS "tsWxGTUI_PyVx" Toolkit
   include the following:

   5.1 Documentation

       5.1.1 Documentation in Plain Text Format

             The TeamSTARS "tsWxGTUI_PyVx" Toolkit documen-
             tation is included, in plain text format,
             in the directory named:

               ./tsWxGTUI_PyVx_Reposiotry/Documents

       5.1.2 Documentation in HTML Format

             Since the TeamSTARS "tsWxGTUI_PyVx" Toolkit
             emulates a character-mode compatible subset of
             the wxPython and wxWidgets pixel-mode GUI Ap-
             plication Programming Interface (API), the
             documentation includes archive copies of pixel-
             mode API in its Hypertext Markup Language
             format.

             The archive copies are provided because the
             original On-Line versions are no longer avail-
             able on the wxWidgets and wxPython web sites.

   5.2 Source Code

       Excerpt From Wikipedia, the free encyclopedia:

       "Python is an open source programming language that
       was made to both look good and be easy to read. It
       was created by a programmer named Guido van Rossum
       in 1991. The language is named after the television
       show Monty Python's Flying Circus and many examples
       and tutorials include jokes from the show.

       Python is an interpreted language. An interpreted
       language allows the programmer to give the source
       code to the computer and the computer runs the code
       right away. This means if the programmer needs to
       change the code they can quickly see the results.
       This makes Python a good programming language for
       beginners and for making programs rapidly because
       you do not have to compile the code to make it run,
       and compiling takes a lot of time. But because the
       computer has to figure out what the code does every
       time the code runs, Python is a very slow language.
       Sometimes, it can be 200 times slower than C [pro-
       gramming language].

       Python is also a high-level programming language. A
       high-level language has advanced features which let
       the programmer to tell the computer what to do with-
       out having to worry about how the computer is going
       to do that as much as low-level programming languag-
       es. This makes writing programs easier and faster.
       Some of the rules of how you write code in Python are
       taken from C, and Python can run some C code."

       Since Python is not a conventional compiled language,
       its language syntax does not include compiler direc-
       tiives to conditionally compile language version spe-
       cific features. Consequently there must be separate
       source code directories and files for Python 2x and
       Python 3x.

       While many language features are common to Python 2x
       and Python 3x:

       a) obsolscent ones may be deprecated, available
          for a limited time (like the print statements and
          old-style classes introduced in Python 1x that
          were retained only in Python 2x) but not recom-
          mended;

       b) obsolete ones ultimately disappear(like the print
          statements and old-style classes syntax no longer
          in Python 3.x); and

       c) enhanced ones may be introduced (like the
          print function syntax introduced in Python 2x
          and the new except statement syntax introduced
          in Python 3.x).

       That being said, cross-platform regression testing on
       various Linux, Mac OS X, Microsoft Windows (with and
       without the free, Linux-like Cygwin plug-in) and Unix
       has established the set of Python 2x and Python 3x
       versions which fully support the Toolkit's Command
       Line Interface and Graphical User Interface.

       Release of the source code enables Toolkit users to
       customize the source code so as to support older or
       newer Python versions and platforms.

======================= INSTALLATION =======================

6. Installation

  Please see the file named:

     ./Documents/INSTALL.txt.

========================= LICENSING ========================

7. Licensing

  Please see the file named:

     ./Documents/LICENSE.txt.

========================= CONTACTS =========================

8. Contacts

  Technical Support Requests should be directed via email
  sent to:

        SoftwareGadgetry@comcast.net

====================== ACKNOWLEDGMENTS =====================

9. Acknowledgments

   Please see files with the following names:

     ./Documents/AUTHORS.txt.

     ./Documents/COPYRIGHT.txt.

     ./Documents/CREDITS.txt.

     ./Documents/THANKS.txt.

======================= End-Of-File ========================

