#!/usr/bin/env python
# "Time-stamp: <06/09/2015  6:41:10 AM rsg>"
#################################################################
#
# File:
#
# Purpose:
#
#    Demonstrates wxPython High Level API using source code for
#    Python 2.7.0-2.7.6 or Python 3.0.0-3.2.3.
#
# Limitations:
#
#    Pre-requisites include:
#
#    1. Host computer is a 32-bit/64-bit processor.
#
#    2. Host computer operating system is Linux,
#       Mac OS X, Microsoft Windows (without Cygwin add-on)
#       or Unix
#
#    3. Host computer has Python 2.7.x or 3.2.x installed
#
# Usage (example):
#
#    Execute:
#
#    d:\WR\SoftwareGadgetry-PyPI\Python-2x\tsWxGTUI_Py2x>
#       c:\Python27\python.exe
#          Tutorial_GUI_1_wxPython_HighLevel_WidgetApi_application.py
#
#    d:\WR\SoftwareGadgetry-PyPI\Python-3x\tsWxGTUI_Py3x>
#       c:\Python32\python.exe
#          Tutorial_GUI_1_wxPython_HighLevel_WidgetApi_application.py
#
#################################################################

try:

    # Use the "wxPython" Toolkit if Available
    import wx

    app = wx.App(True)  # Create a new app,
                        # Redirect stdout/stderr to a window.
    frame = wx.Frame(   # A Frame is a top-level window.
        None,
        wx.ID_ANY,
        "Hello World via tsWxGTUI")

    frame.Show(True)    # Show the frame.

    app.MainLoop()

except Exception as errorCode:

    # Rrport nature of import exception.
    print("\n\t%s:\n\t\t'wxPython' Error:\n\t\t\t'%s'" % (
        "Tutorial_GUI_5_wxPython_HighLevel_WidgetApi_application",
        str(errorCode)))
