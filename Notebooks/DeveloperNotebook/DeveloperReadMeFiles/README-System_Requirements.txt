#-----------------------------------------------------------
#"Time-stamp: <12/18/2016  2:53:12 PM rsg>"
#-----------------------------------------------------------

========== File: README-System_Requirements.txt ============

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

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./DeveloperReadMeFiles".

===================== TABLE OF CONTENTS ====================

1. System Requirements

   1.1 Hardware

       1.1.1 Central Processing Unit
       1.1.2 Random Access Memory
       1.1.3 Non-Volatile Storage
       1.1.4 Network Interface Device
       1.1.5 Keyboard Device
       1.1.6 Pointing Device
       1.1.7 Display Device
       1.1.8 Printer Device

   1.2 Software

       1.2.1 Operating System
       1.2.2 Command Line Interface Shell
       1.2.3 Graphical-style User Interface Shell
       1.2.4 Terminal Interface Libraries
       1.2.5 Terminal Emulators
       1.2.6 Development Tools
       1.2.7 Python Virtual Machines
       1.2.8 Python Integrated Development Environments
       1.2.9 TeamSTARS "tsWxGTUI" Toolkit

   1.3 Baseline Developmment and Test Platforms

       1.3.1 Low-Range Development & Operator Platform
       1.3.2 Mid-Range Development & Operator Platform
       1.3.3 High-Range Development & Operator Platform

   1.4 Command Line Interface
   1.5 Graphical User Interface
   1.6 Terminal Control Library Interface
   1.7 Terminal Emulators

2. Python Programming Resources

   2.1 Distributions

       2.1.1 Python Software Foundation Website
       2.2.2 ActiveState Website
       2.2.3 Download Python

   2.2 Training

       2.2.1 Dive Into Python
       2.2.2 Learn Python
       2.2.3 Python Community
       2.2.4 Python Cookbook

3. Release Process

   3.1 Release Nomenclature
   3.2 Python Distribution Utilities

4. Directories for Toolkit Development

   4.1 "tsWxGTUI_Py2x" - Identifies second generation syntax
       associated with Python 2.0.0-2.7.8.

   4.2 "tsWxGTUI_Py3x" - Identifies third generation syntax
       associated with Python 3.0.0-3.4.2.

   4.3 Toolkit Working Directory Nominclature

   4.4 Toolkit Working Repository Structure

   4.5 "tsWxGTUI_PyVx" Directory Structure

5. User Documentation

   5.1 Equipment Operator Documents
   5.2 Software Engineer and Developer Documents

==================== System Requirements ===================

1. System Requirements

   1.1 Hardware

       Hardware components must include application-specific
       versions of the following:

       1.1.1 Central Processing Unit

             A required electronic device that loads and
             executes machine-readable instructions.

             It performs arithmetic and logic. It loads,
             modifies and stores machine-readable data.
             The processor may be any of the popular
             32-/64-bit single or multi-core devices.

       1.1.2 Random Access Memory

             A required electronic device that temporarily
             receives, stores and returns machine-readable
             machine instructions and data that will be
             available until the next power interruption.

       1.1.3 Non-Volatile Storage

             A required internal and optional external
             electronic device (Flash Memory) or elecro-
             mechanical device (Hard Drive) whose non-
             volatile memory receives, stores and can then
             return source and machine-readable data after
             electrical power interruptions. The optional
             external device may be local or remote. When
             remote, the system must include a Network
             Interface Device.

       1.1.4 Network Interface Device

             An optional electronic device (Modem) that
             inputs and outputs data over an optional wired
             or wireless telecommunications circuit.

       1.1.5 Keyboard Device

             A required hand-operated electronic or electro-
             mechanical device to input alpha-numeric and
             control data via an assembly of typewriter-style
             push buttons.

       1.1.6 Pointing Device

             An optional or required hand-operated electronic
             or electro-mechanical Mouse, Trackball, Touchpad
             or Touchscreen device that controls the coordi-
             nates of a cursor on the computer screen as you
             move the positioning control (hand, finger or
             stylus) around.

       1.1.7 Display Device

             A required electronic device that outputs alpha-
             numeric, graphic (or graphic-style) and control
             data to the computer screen.

       1.1.8 Printer Device

             An optional electro-mechanical device that out-
             puts alpha-numeric, graphic and control data to
             individual sheets of paper.

   1.2 Software

       Software components must include application-specific
       versions of the following:

       1.2.1 Operating System

             Platform-specific, multi-user (enables a user to
             login locally and the same or another user to login
             remotely), multi-process (enables a user to launch
             multiple applications and/or multiple instances of
             the same application), multi-threaded (enables each
             application to concurrently execute multiple tasks
             which may independently block while waiting for a
             triggering event notification) Operating Systems
             for 32-bit/64-bit processors:

             GNU/Linux (such as CentOS, Debian GNU, Fedora, Gentoo,
             Hard Hat, Mandriva, OpenSuSE, Red Hat, Scientific,
             Ubuntu, Yellow Dog etc.). In a GNU/Linux system, Linux
             is the kernel component. The rest of the system consists
             of other programs, many of which were written by or for
             the "GNU Project". Because the Linux kernel alone does
             not form a working operating system, we prefer to use
             the term "GNU/Linux" to refer to systems that many
             people casually refer to as "Linux".

             Mac OS X (such as Unix-like Darwin and BSD based
             10.4/Tiger - 10.10/Yosemite etc.)

             Microsoft Windows (such as Professional or Home
             editions of 8.1, 8, 7, Vista or XP) when augmented
             with Cygwin, the free, Linux-like Command Line
             Interface and GNU toolkit from Red Hat.

             Unix (such as FreeBSD/PC-BSD, HP-UX, IBM-AIX, IRIX,
             OpenIndiana, SCO, Solaris/SunOS etc.).

       1.2.2 Command Line Interface Shell

             Host Computer Operating System Command Line Interface
             Shell.

             Linux "Terminal".

             Mac OS X "iTerm", "iTerm2" or "Terminal".

             Microsoft Windows Command Prompt "cmd.exe" or
             "PowerShell.exe".

             Unix "Terminal".

       1.2.3 Graphical-style User Interface Shell

             Host Computer Operating System Graphical-style User
             Interface Shell.

             Linux "GNOME", "KDE", "X11" Desktop Window Manager.

             Mac OS X Desktop Window Manager.

             Microsoft Windows Desktop Window Manager.

             Unix "GNOME", "KDE", "X11" Desktop Window Manager.

       1.2.4 Terminal Interface Libraries

             Host Computer Terminal Interface Libraries.

             Linux "Curses"/"nCurses" Terminal Interface Library.

             Mac OS X "Curses"/"nCurses" Terminal Interface
             Library.

             Microsoft Windows "Curses"/"nCurses" Terminal Inter-
             face Library provided by Cygwin, the free, Linux-like
             Command Line Interface and GNU toolkit from Red Hat.

             Unix "Curses"/"nCurses" Terminal Interface Library.

       1.2.5 Terminal Emulators

             Host Computer Terminal Emulators.

             Linux vt100, vt220, xterm, xterm-color, xterm-16color,
             xterm-88color and xterm-256color.

             Mac OS X vt100, vt220, xterm, xterm-color, xterm-16color,
             xterm-88color and xterm-256color.

             Microsoft Windows vt100, vt220, mintty, xterm,
             xterm-color, xterm-16color, xterm-88color and
             xterm-256color provided by Cygwin, the free,
             Linux-like Command Line Interface and GNU
             toolkit from Red Hat.

             Unix vt100, vt220, xterm, xterm-color, xterm-16color,
             xterm-88color and xterm-256color.

       1.2.6 Development Tools

             Host Computer Development Tools:

             File Manager (such as "Midnight Commander" on Linux
             and Unix; "Finder" and "PathFinder" on Mac OS X;
             "File Explorer" and "Total Commander" on Microsoft
             Windows etc.).

             Text (source code) editor (such as "vi", "xemacs"
             etc.).

             Optional Word Processor (source code) editor (such
             as "Microsoft Word", "AuthorIt", "LibreOffice Text
             Document" etc.).

             Optional Block Diagram and Flowchart editor (such as
             "Microsoft Visio", "LibreOffice Presentation",
             "LibreOffice Drawing" etc.).

             Optional Database (such as "Microsoft Access",
             "MySQL", "PostgreSQL", "SQLite", "LibreOffice
             Database" etc.).

             Optional Spreadsheet (such as "Microsoft Excel",
             "LibreOffice Spreadsheet" etc.).

             Optional Programm debugger (such as "gdb").

       1.2.7 Python Virtual Machines

             Python Virtual Machine and its associated Python
             source code compiler and byte code interpreter.

       1.2.8 Python Integrated Development Environments

             Python Integrated Development Environments (such as
             "Python Idle", WingWare's "WingIDE" etc.)

       1.2.9 TeamSTARS "tsWxGTUI" Toolkit

             The "tsWxGTUI" Toolkit and its associated library
             of general purpose, re-usable buildig block modules,
             developmnt tools and utilities.

   1.3 Baseline Developmment and Test Platforms

       The following Developmment and Test Platforms represent
       a broad spectrum of Intel microprocessor based systems
       that are known to support the TeamSTARS "tsWxGTUI"
       Toolkit.

       NOTE: Since cross-platform operating system and Python
             virtual machine technology is also available for
             non-Intel based systems, it is likely that the
             TeamSTARS "tsWxGTUI" toolkit will also work on
             those systems which use the equivalent operating
             systems and Python virtual machines with 32-bit
             and 64-bit microprocessors from other manufactur-
             ers including:

                 AMD
                 ARM Holdings
                 Cyrix
                 Freescale
                 Intel
                 IBM
                 Marvell
                 NexGen
                 Nvidia Tegra
                 Oracle (previously Sun)
                 OWC
                 Qualcomm
                 Rise Technology
                 Samsung
                 SigmaTel
                 Texas Instruments
                 Transmeta
                 tilera
                 Via (Centaur Technology division)
                 winchip

       1.3.1 Low-Range Development & Operator Platform

             1998-model year, 366 MHz Intel Pentium II-based
             laptop with 384 MB RAM, 640x480/1024x768 pixel
             resolution display and expansion capabilities
             (marginal resources and performance) sufficient
             enough to serve as the low-level baseline
             development and operator platform.

             Its interchangeabble 32 GB (4200 RPM) ATA hard
             drives were used to run Windows XP Pro or
             the Linux operating system kernel with
             GNU toolchain (Ubuntu 12.04).

             Its limited memory and available PCMCIA
             network adapters were incompatible with later
             versions of Windows or with other Linux
             distributions.

       1.3.2 Mid-Range Development & Operator Platform

             2007-model year, 2.33 GHz Intel Core 2 Duo
             processor-based laptop with 4 GB RAM, 1920x1200
             pixel resolution display and sufficient perform-
             ance, resources and expansion capabilities to
             serve as the moderate-level baseline development
             and operator platform.

             Its 160 GB (5400 RPM) SATA 1.5 Gb/s internal hard
             drive was used to run Apple's Mac OS X 10-3-10.7
             and the hypervisor virtualization applications
             (Parallels Desktop 3-8 and VMware Fusion 4-5)
             that supported various guest operating systems.

             Its 1.5 TB (7200 RPM) SATA 3 Gb/s external hard
             drive was used to store and run configured versions
             of the following guest operating systems:

             Linux operating system kernel with GNU
             toolchain (Ubuntu 12.04).

             Microsoft Windows (8 Pro, 7 Pro and XP Pro).

             Unix (OpenSolaris 11/OpenIndianna 151a5).

       1.3.3 High-Range Development & Operator Platform

             2013-model year, 3.5 GHz Intel Quad Core i7
             processor-based desktop with 16 GB RAM,
             2560x1440 pixel resolution display and suf-
             ficient performance, resources and expansion
             capabilities to serve as the high-level base-
             line development and operator platform. Its
             3 TB (7200 RPM) SATA 6 Gb/s internal hard drive had
             128 GB Solid State Flash memory and was used
             to run Apple's Mac OS X 10.9-10.10 and the
             hypervisor virtualization applications
             (Parallels Desktop 9-10 and VMware Fusion 5)
             that supported various guest operating systems.
             Its 3 TB (7200 RPM) SATA 6 Gb/s internal hard
             drive was also used to store and run configured
             versions of the following guest operating systems:

             Linux operating system kernel with GNU tool-
             chain (CentOS 7.0, Fedora 20, OpenSuSE 13.1,
             Scientific 6.5 and Ubuntu 12.04 & 14.04);

             Microsoft Windows operating system (8.1 Pro,
             8 Pro, 7 Pro and XP Pro.

                NOTE:

                  CLI features are available with Windows
                  Command Prompt, Wndows PowerShell or
                  various third party shells.

                  GUI features become available to Windows
                  users only after the users install Cygwin,
                  the free and open source Linux-based
                  add-on from Red Hat. Cygwin provides
                  Windows users with POSIX-compatible
                  command line shells, terminal control
                  libraries, terminal emulators and the
                  GNU toolchain).

             Unix operating system (FreeBSD 9.2-10.0,
             OpenIndianna 151a8 PC-BSD 9.2-10.0).

   1.4 Command Line Interface

       User-friendly character-mode, cross-platform,
       Linux-/Unix-style processing of keyword-value pair
       options and positional arguments.

       Each platform must provide at least one of the fol-
       lowing building blocks in the Python version-specific
       Global Module Index:

       "argparse" (introduced with Python 2.7.0 and 3.2.0)
       "optparse" (introduced with Python 2.3.0 and 3.0.0;
                   subsequently deprecated by argparse)
       "getopt"   (introduced with Python 1.6.0 and 3.0.0)

   1.5 Graphical User Interface

       User-friendly character-mode, cross-platform, emula-
       tion of the pixel-mode "wxPython" GUI Toolkit.

       Each platform must provide the following "wxPython"-
       style GUI-objects: frames, dialogs, menu bars, scroll
       bars, status bars, text bar, buttons, checkboxes,
       radio boxes/buttons, scrollable text and mouse cursor
       and buttons.

       It must provide the following "wxPython"-style
       68-color palette:

       a) No colors may appear in output for vt100 and
          vt200 displays;

       b) Only the standard 8-colors may appear in output
          for cygwin mintty, xterm and xterm-color
          displays based on color substitution mappings
          from the 68-color palette;

       c) Only the standard 16-colors may appear in output
          for xterm-16color displays based on color
          substitution mappings from a 71-color palette;

       d) If the configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to True, then
          only the standard 16-colors may appear in output
          for xterm-88color displays, based on color
          substitution mappings from a 71-color palette;

          If the configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to False, then
          the experimental 71-color palette may be applied
          without need for any mapping;

       e) If the configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to True, then
          only the standard 16-colors may appear in output
          for xterm-256color displays, based on color
          substitution mappings from a 71-color palette;

          If the configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to False, then
          the experimental 140-color palette may be applied
          without need for any mapping.

   1.6 Terminal Control Library Interface

       Each platform must provide a Terminal-independent
       Application Programming Interface (API).

       a) Termcap-based curses on BSD UNIX

       b) Terminfo-based curses on AT&T UNIX

       c) Terminfo-based nCurses on Linux and on Cygwin
          for Microsoft Windows

   1.7 Terminal Emulators

       Each platform must provide a program that emulates
       a video terminal within some other display archi-
       tecture. Though typically synonymous with a shell
       or text terminal, the term terminal covers all
       remote terminals, including graphical interfaces.
       A terminal emulator inside a graphical user inter-
       face is often called a terminal window.

       a) Traditional mouseless, non-color (black and single
          shade of white, orange or green) for vt100 and
          vt220 displays with the following host application
          programs Cygwin Console, Linux Terminal, Mac OS X
          Terminal/iterm/iterm2 and Unix Terminal.

          Synthesized (xterm-style), mouse-supported, non-
          color (black and single shade of white, orange or
          green) for vt100 and vt220 displays with the fol-
          lowing host application programs Cygwin Mintty and
          Linux Xterm/UDxterm. It spends a noticeable period
          looping to collect twelve mouse input character se-
          quences and converting the input into a single
          xterm-style one used to establish which foreground
          GUI object the mouse was over when the mouse button
          was clicked. It recognizes only the mouse button
          press/release event but not the quick double and
          triple clicks.

       b) Mouse-supported 8-color (with support of 64
          color pairs) for cygwin mintty, xterm and
          xterm-color displays;

       c) Mouse-supported 16-colors (with support of 256
          color pairs) for xterm-16color displays;

       d) Mouse-supported 16-colors (with support of 256
          color pairs) for xterm-88color displays, if the
          configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to True;
          else Mouse-supported experimental 71-colors
          (with support of 5041 color pairs) for
          xterm-88color displays, if the configuration
          control parameter USE_256_COLOR_PAIR_LIMIT is
          set to False and the experimental 71-color
          palette will be applied without need for any
          mapping;

       e) Mouse-supported 16-colors (with support of 256
          color pairs) for xterm-256color displays, if the
          configuration control parameter
          USE_256_COLOR_PAIR_LIMIT is set to True;
          else Mouse-supported experimental 140-colors
          (with support of 19600 color pairs) for
          xterm-256color displays, if the configuration
          control parameter USE_256_COLOR_PAIR_LIMIT is
          set to False and the experimental 140-color
          palette will be applied without need for any
          mapping.

======================== End-Of-File =======================

