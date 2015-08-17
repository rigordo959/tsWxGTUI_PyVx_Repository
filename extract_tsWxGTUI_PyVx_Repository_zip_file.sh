#!/bin/bash          
#"Time-stamp: <08/17/2015 12:56:14 PM rsg>"
#
# File:
#
#    extract_tsWxGTUI_PyVx_Repository_zip_file.sh
#
# Purpose:
#
#    Support a user who visted GitHub and clicked on the
#    "Download ZIP" rather than the "Clone in Desktop"
#    button.
#
#    This script must only be run after the download has
#    been retrieved from:
#
#       "https://github.com/rigordo959/tsWxGTUI_PyVx_Repository"
#
#    It extracts the contents of a compressed archive file
#    named:
#
#       "tsWxGTUI_PyVx_Repository-master.zip"
#
#    GitHub is a Web-based Git repository hosting service,
#    which offers all of the distributed revision control
#    and source code management (SCM) functionality of Git
#    as well as adding its own features.
#
# Toolkit Author's Currently Available Test Platforms:
#
#    -------------------------------------------------------------------
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
#    -------------------------------------------------------------------
#    # 32-/64-bit Operating System on Host Computer
#       macDesktop       (for 64-bit Mac OS X 10.10.4 on Apple Desktop Host)
#    
#          # 32-bit Virtual Machine Computer running as Guest OS on macDesktop
#          macDesktopUbuntu12VM   (for 32-bit Ubuntu 12.04 Linux Guest OS)
#          macDesktopWin7VM       (for 32-bit Windows 7 Guest OS)
#          macDesktopWin81VM      (for 32-bit Windows 8.1 Guest OS)
#    
#          # 64-bit Virtual Machine Computer running as Guest OS on macDesktop
#          macDesktopDebian8VM    (for 64-bit Debian 8 Linux Guest OS)
#          macDesktopFedora22VM   (for 64-bit Fedora 22 Linux Guest OS)
#          macDesktopOpenSuSE13VM (for 64-bit OpenSuSE 13 Linux Guest OS)
#          macDesktopPCBSD11VM    (for 64-bit PC-BSD 11 Unix Guest OS)
#          macDesktopUbuntu14VM   (for 64-bit Ubuntu 14.04 Linux Guest OS)
#          macDesktopUbuntu15VM   (for 64-bit Ubuntu 15.04 Linux Guest OS)
#          macDesktopWin10VM      (for 64-bit Windows 10 Guest OS)
#
# Capabilities:
#
#    1. Supported host os types with POSIX-comptible command line interfaces:
#
#       (a) cygwin
#
#           tested using the free, linux-like plug-in for
#           Microsoft Windows (XP, 7, 8, 8.1 and 10).
#
#       (b) linux
#
#           to be tested using the free, open source GNU
#           toolchain and Linux kernel (Debian 8, Fedora 22,
#           Ubuntu 15.04 etc.)
#
#       (c) mac os x
#
#           to be tested using Darwin & BSD Unix based
#           Mac OS X Lion (7.5) and Yosemite (10.10.4)
#
#       (c) unix
#
#           to be tested using Open Indiana 151a8 (OpenSolaris 11
#           based) and PC-BSD 11 (FreeBSD Unix based).
#
# Limitations:
#
#    1. Unsupported host os types:
#
#       (a) Microsoft Windows --- Support requires cygwin the free,
#                      linux-like plug-in from Ret Hat.
#
# Notes:
#
#    The extraction uses the capitalized variables which
#    must be customized by the user.
#
#    The customizations must reflect the user's computer
#    operating system, command line interface shell and
#    the folders/directories to be used for the download
#    and extraction.
#
#    The following example variables are specific for a
#    computer with:
#
#       Operating System:
#
#         "Microsoft Windows 7" with Cygwin, Red Hat's free
#         Linux-like environment and command-line interface
#         for Microsoft Windows. Cygwin provides native
#         integration of Windows-based applications, data,
#         and other system resources with applications,
#         software tools, and data of the Linux-like envi-
#         ronment.
#
#       Command Line Interface Application:
#
#         "Cygwin" bash shell
#
#       User Name:
#
#         "rsg"
#
#       Internet Web Browser Download Folder:
#
#         "/cygdrive/c/Users/rsg/Downloads"
#
#       Toolkit User Working Folder
#
#         "/cygdrive/c/Temp/WR/tsWxGTUI_PyVx_Repository"
#
# Modifications:
#
#    2015/08/15 rsg Added logic to set customized variable based
#                   on host os type (linux/mac os x/unix).
#
#    2015/08/17 rsg Added logic to set customized variable based
#                   on Windows user and host os type (cygwin).
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
