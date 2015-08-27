#!/bin/bash          
#"Time-stamp: <08/22/2015  3:29:41 AM rsg>"
#
# File:
#
#    extract_tsWxGTUI_PyVx_Repository_zip_file.sh
#
# Purpose:
#
#    This is a "bash" shell script to be used to extract
#    (to the recipient's computer Desktop) a collection of
#    directories, subdirectories and files from the Team-
#    STARS "tsWxGTUI_PyVx" Toolkit's compressed repository
#    archive "ZIP" file named:
#
#       "tsWxGTUI_PyVx_Repository-master.zip"
#
#    The Toolkit is released as open source software for
#    which the original source code is made freely avail-
#    able. Source code is the part of computer programs
#    that most users don't ever see; it's the part computer
#    programmers would manipulate to change how a computer
#    "program" or "application" works.
#
#    "GitHub" is a Web-based Git repository hosting service,
#    which offers all of the distributed revision control
#    and source code management (SCM) functionality of Git
#    as well as adding its own features.
#
#    The Toolkit author chose the "GitHub" service because
#    of its cost-free features that are popular with both
#    software authors and recipients.
#
#    This "bash" script supports a user who visted "GitHub"
#    and clicked on the "Download ZIP" rather than the
#    "Clone in Desktop" button because the recipient's
#    computer lacked automatic "zip" file extraction
#    capabilities.
#
#    This "bash" script must only be run after the download
#    has been retrieved from:
#
#       "https://github.com/rigordo959/
#                tsWxGTUI_PyVx_Repository"
#
# Preparation:
#
#    Firefox Example avoids extra steps:
#       select all text;
#       copy all text to clipboard
#       launching text editor;
#       pasting in the clipboard text in clipboard of
#       saving the editor text as a file on the Desktop
#       exiting editor
#
#    # Step #1 - Launch Web browser (such as Firefox, Internet Explorer etc.)
#    Click on Firefox
#
#    # Step #2 - Enter Search Address for GitHub Project
#    https://github.com/rigordo959/tsWxGTUI_PyVx_Repository
#
#    # Step #3 - Select Scriot File
#    Click on extract_tsWxGTUI_PyVx_Repository_zip_file.sh
#
#    # Step #4 - Open Script File to View
#    Click on RAW
#
#    # Step #5 - Select Save Page As Action
#    Click right mouse button on Save Page As
#
#    # Step #6 - Select Desktop for Save Page As Destination
#    Click left mouse button on users -> Your ID -> Desktop -> Save
#
# Usage:
#
#    # Step #1 - Alert recipients when "bash" not available
#    bash 
#
#    # Step #2 - Alert recipients when "Desktop" directory not available 
#    cd ~/Desktop
#
#    # Step #3 - Copy the "bash" script to the recipient's "Desktop"
#    cp -p ~/Downloads/extract_tsWxGTUI_PyVx_Repository_zip_file.sh .
#
#    # Step #4 - Change the "bash" script to enable execute mode access.
#    chmod 775 ./extract_tsWxGTUI_PyVx_Repository_zip_file.sh
#
#    # Step #5 - Launch the "bash" script
#    ./extract_tsWxGTUI_PyVx_Repository_zip_file.sh
#
# Capabilities:
#
#    1. Supported 32-/64-bit host computer OS types with POSIX-comptible
#       command line interfaces and Python 2x/Python 3x application
#       programs:
#
#       (a) Linux
#
#           tested using the free, open source GNU toolchain and
#           Linux kernel (Debian 8, Fedora 22, Ubuntu 15.04 etc.)
#
#       (b) Mac OS X
#
#           tested using Darwin & BSD Unix based Mac OS X
#           Lion (7.5) and Yosemite (10.10.5)
#
#       (c) Microsoft Windows
#
#           tested using Professional Editions of Windows (XP, 7,
#           8, 8.1 and 10)
#
#       (d) Unix
#
#           tested using OpenIndiana 151a8 (OpenSolaris 11) and
#           PC-BSD 11 (FreeBSD 11 server with Linux GUI Desktop).
#
#    2. Supported 32-/64-bit host computer OS types with Curses-
#       comptible Graphical User Interfaces, 8-color terminal
#       emulators (xterm & xterm-color) 16-color terminal emulators
#       (xterm-16color, xterm-88color & xterm-256color) non-color
#       (vt100 and vt220) terminal emulators and Python 2x/Python:
#
#       (a) Linux
#
#           tested using the free, open source GNU toolchain and
#           Linux kernel (Debian 8, Fedora 22, Ubuntu 15.04 etc.)
#
#       (b) Mac OS X
#
#           tested using Darwin & BSD Unix based Mac OS X
#           Lion (7.5) and Yosemite (10.10.5)
#
#       (c) Microsoft Windows
#
#           tested using the free, linux-like plug-in for Professional
#           Editions of Windows (XP, 7, 8, 8.1 and 10)
#
#       (d) Unix
#
#           tested using OpenIndiana 151a8 (OpenSolaris 11) and
#           PC-BSD 11 (FreeBSD 11 server with Linux GUI Desktop).
#
# Limitations:
#
#    1. Some 32-/64-bit host computer OS releases still use the
#       traditional "Curses" instead of the newer "nCurses"
#       terminal device interface.
#
#       As a result, they will:
#
#       (a) output the proper display but
#
#       (b) ignore mouse input from vt100 and vt220 terminal
#           device emulators
#
# Notes:
#
#    # Toolkit Author's Currently Available Test Platforms:
#
#    #-------------------------------------------------------------------
#
#    # 32-bit Operating System on Host Computer
#
#       macLaptop        (for 32-bit Mac OS X 10.7.5 on Apple Laptop Host)
#
#          # 32-bit Virtual Machine Computer running as Guest OS on macLaptop
#          # The availability of host-level anti-virus protection compensates,
#          # in part, for Microsoft having ended XP support on April 8, 2014.
#             macLaptopWinXPVM  (for 32-bit Windows XP Guest OS)
#
#       linuxLaptop      (for 32-bit Ubuntu 10.04 Linux on Dell Laptop Host)
#
#       # windowsLaptop    (for 32-bit Windows XP on Dell Dell Laptop Host)
#       # taken out of service when Microsoft ended support on April 8, 2014.
#       #
#       # An unsupported version of Windows will no longer receive software
#       # updates from Windows Update. These include security updates that
#       # can help protect your PC from harmful viruses, spyware, and other
#       # malicious software, which can steal your personal information.
#       # Windows Update also installs the latest software updates to improve
#       # the reliability of Windows?new drivers for your hardware and more.
#
#    #-------------------------------------------------------------------
#
#    # 32-/64-bit Operating System on Host Computer
#       macDesktop       (for 64-bit Mac OS X 10.10.4 on Apple Desktop Host)
#    
#          # 32-bit Virtual Machine Computer running as Parallels 11
#          # Guest OS on macDesktop
#          macDesktopLXLE14VM     (for 32-bit Ubuntu 14.04.2/Lubuntu 12.04.5
#                                  Linux Guest OS. Light on resources; Heavy on
#                                  functions. Always based on Ubuntu/Lubuntu.)
#          macDesktopUbuntu12VM   (for 32-bit Ubuntu 12.04 LTS Linux Guest OS)
#          macDesktopWin7VM       (for 32-bit Windows 7 Pro Guest OS)
#          macDesktopWin81VM      (for 32-bit Windows 8.1 Pro Guest OS)
#    
#          # 64-bit Virtual Machine Computer running as as Parallels 11
#          # Guest OS on macDesktop
#          macDesktopDebian8VM    (for 64-bit Debian 8 Linux Guest OS)
#          macDesktopFedora22VM   (for 64-bit Fedora 22 Linux Guest OS)
#          macDesktopOpenSuSE13VM (for 64-bit OpenSuSE 13.2 Linux Guest OS)
#          macDesktopSolaris11VM  (for 64-bit OpenIndiana 151a8 Unix-like
#                                  OpenSolaris 11 Guest OS)
#          macDesktopPCBSD11VM    (for 64-bit PC-BSD 11 Unix-like Guest OS
#                                  with FreeBSD server and Linux GUI Desktop)
#          macDesktopUbuntu14VM   (for 64-bit Ubuntu 14.04 LTS Linux Guest OS)
#          macDesktopUbuntu15VM   (for 64-bit Ubuntu 15.04 Linux Guest OS)
#          macDesktopWin10VM      (for 64-bit Windows 10 Pro Guest OS)
#
#    #-------------------------------------------------------------------
#
# Modifications:
#
#    2015/08/15 rsg Added logic to set customized variable based
#                   on host os type (linux/mac os x/unix).
#
#    2015/08/17 rsg Added logic to set customized variable based
#                   on Windows user and host os type (cygwin).
#
#    2015/08/21 rsg Added Usage section.
#
#    2015/08/22 rsg Updated the Capabilities, Limitations and
#                   Notes sections.
#
# To-Do:
#
#    None
#
# Example: Year-Month-Day = 2015-08-17
DATE=$(date +"%Y-%m-%d")
echo $DATE
#
# Example: Hour-Minute-Second = 23:06:59
TIME= $(date +"%R:%S")
echo $TIME
#
# Example: Year-Month-Day-at-Hour-Minute-Second = 2015-08-17-at-23:06:59
NOW=$(date +"%Y-%m-%d-at-%R:%S")
echo $NOW

HOST=$(hostname)

if [ "$OSTYPE" == "cygwin" ]

then

    # $OSTYPE == "cygwin", the linux-like plug-in for "windows"
    # User may optionally customize the following statement.
    DOWNLOADS_DIRECTORY=/cygdrive/c/Users/$USER/Downloads

    # User may optionally customize the following statement.
    TARGET_PATH=/cygdrive/c/Users/$USER/Desktop/myWR-$NOW

else

    # $OSTYPE == "linux", "mac os x" or "unix"
    # User may optionally customize the following statement.
    DOWNLOADS_DIRECTORY=~/Downloads

    # User may optionally the following statement.
    TARGET_PATH=~/Desktop/myWR-$NOW

fi

#
# User may optionally customiz the following repository name statement.
# Example: REPOSITORY_NAME=tsWxGTUI_PyVx_Repository
REPOSITORY_NAME=tsWxGTUI_PyVx_Repository
#
# User may optionally customiz the following repository branch statement.
# Example: REPOSITORY_BRANCH=-master
REPOSITORY_BRANCH=-master
#
# Standard GitHub repository download extension type.
REPOSITORY_EXTENSION=.zip
#
DOWNLOADS_FILE=$REPOSITORY_NAME$REPOSITORY_BRANCH$REPOSITORY_EXTENSION
DOWNLOADS_PATH=$DOWNLOADS_DIRECTORY/$DOWNLOADS_FILE
echo $DOWNLOADS_PATH
file $DOWNLOADS_PATH
#
TARGET_DIRECTORY=tsWxGTUI_PyVx_Repository
#
rm -rf $TARGET_PATH
mkdir $TARGET_PATH
cp -p $DOWNLOADS_PATH $TARGET_PATH
#
SOURCE_PATH=$TARGET_PATH/$DOWNLOADS_FILE
SOURCE_DIRECTORY=$REPOSITORY_NAME$REPOSITORY_BRANCH
#
cd $TARGET_PATH
unzip $DOWNLOADS_FILE
#
# Rename folder/directory to remove "-master" branch suffix
# from repository name
mv $SOURCE_DIRECTORY $TARGET_DIRECTORY

