#! /usr/bin/env python
# "Time-stamp: <12/28/2014 11:16:54 AM rsg>"
#
__doc__ = '''
test_Toolkit_Import_Sequence.py - Test and demonstrate the
        import sequence of the for building of the TeamSTARS
        "tsWxGTUI_PyVx" Toolkit block components.

    1st stage (required) --- Command Line Interface (CLI) Library

    2nd stage  (optioal) --- Graphical-style User Interface (GUI)
                             Library

    3rd stage (launcher) --- tsCommandLineEnv or tsWxMultiFrameEnv
'''
#################################################################
#
# File: test_Toolkit_Import_Sequence.py
#
# Purpose:
#
#     test_Toolkit_Import_Sequence.py - Test and demonstrate the
#     import sequence of the for building of the TeamSTARS
#     "tsWxGTUI_PyVx" Toolkit block components.
#
#    1st stage (required) --- Command Line Interface (CLI) Library
#
#    2nd stage  (optioal) --- Graphical-style User Interface (GUI)
#                             Library
#
#    3rd stage (launcher) --- tsCommandLineEnv or tsWxMultiFrameEnv
#
# Usage (example):
#
#    # Execute
#
#    python test_Toolkit_Import_Sequence.py
#
# Capabilities:
#
#    TBD.
#
# Limitations:
#
#    TBD.
#
# Notes:
#
#    TBD.
#
# Methods:
#
#    TBD.
#
# Classes:
#
#    TBD.
#
# Modifications:
#
#    2014/12/28 rsg Initial version.
#
# ToDo:
#
#    TBD.
#
#################################################################

__title__     = 'test_Toolkit_Import_Sequence'
__version__   = '1.0.0'
__date__      = '12/28/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2014 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = ''

__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if len( __credits__) == 0:
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

separator = '''
-------------------------------------------------------------------------
'''

import sys

Launch_Name = sys.argv[0]

print('%s' % __header__)

print('%s' % separator)

print('\n\nLaunch_Name=%s' % Launch_Name)
print('\n\n__doc__=%s' % __doc__)

# Python-based CLI Mode
try:

    print('%s' % separator)

    CLImode = True
    print('\n\nCLImode=%s' % CLImode)

    import tsLibCLI
    print('\n\ntsLibCLI: %s' % dir(tsLibCLI))

    print('%s' % separator)

    import tsExceptions as tse
    print('\n\ntse: %s' % dir(tse))

    print('%s' % separator)

    import tsLogger as Logger
    print('\n\nLogger: %s' % dir(Logger))

    print('%s' % separator)

    import tsOperatorSettingsParser
    print('\n\ntsOperatorSettingsParser: %s' % dir(tsOperatorSettingsParser))

    print('%s' % separator)

    from tsDoubleLinkedList \
         import DoubleLinkedList
    print('\n\nDoubleLinkedList: %s' % dir(DoubleLinkedList))

    print('%s' % separator)

    if CLImode:

        from tsCommandLineEnv \
             import CommandLineEnv

        print('\n\nCommandLineEnv: %s' % dir(CommandLineEnv))

except ImportError, importCode:

    CLImode = False
    print('\n\nCLImode=%s' % CLImode)

    fmt1 = '%s: ImportError ' % str(__title__)
    fmt2 = '(tsLibCLI); '
    fmt3 = 'importCode=%s' % str(importCode)
    msg = fmt1 + fmt2 + fmt3

    print(msg)

##    raise tse.PROGRAM_EXCEPTION(
##      tse.APPLICATION_TRAP,
##      msg)

if CLImode:

    # wxPython-style, nCurses-based GUI Mode
    try:

	print('%s' % separator)

        GUImode = True
        print('\n\nGUImode=%s' % GUImode)

        import tsLibGUI
        print('\n\ntsLibGUI: %s' % dir(tsLibGUI))

	print('%s' % separator)

        import tsWx as wx
        print('\n\nwx: %s' % dir(wx))

	print('%s' % separator)

        from tsWxMultiFrameEnv import MultiFrameEnv
        print('\n\nMultiFrameEnv: %s' % dir(MultiFrameEnv))

    except ImportError, importCode:

        GUImode = False
        print('\n\nGUImode=%s' % GUImode)

        fmt1 = '%s: ImportError ' % __title__
        fmt2 = '(tsLibGUI); '
        fmt3 = 'importCode=%s' % str(importCode)
        msg = fmt1 + fmt2 + fmt3

        print(msg)

##        raise tse.UserInterfaceException(
##            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE,
##            msg)

print('%s' % separator)
