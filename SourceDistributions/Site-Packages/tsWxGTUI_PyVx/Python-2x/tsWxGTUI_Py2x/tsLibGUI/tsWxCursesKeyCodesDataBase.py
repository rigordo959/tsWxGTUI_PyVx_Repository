#! /usr/bin/env python
# "Time-stamp: <03/18/2015  4:58:03 AM rsg>"
'''
tsWxCursesKeyCodesDataBase.py - Dictionary of Python Curses Key
Codes to be associared with the terminal console keyboard.
'''
#################################################################
#
# File: tsWxCursesKeyCodesDataBase.py
#
# Purpose:
#
#     Dictionary of Python Curses Key Codes to be associared with
#     the terminal console keyboard.
#
# Usage (example):
#
#     ## Import Module
#     import tsWxCursesKeyCodesDataBase
#
# Requirements:
#
#    1. Input Interface
#
#       Computer Keyboard (industry standard mult-button).
#
#    2. Output Interface
#
#       Required: Computer Monitor (industry standard 256-color,
#       8-color recommended minimum or monochrome) able to display
#       text characters (80-column by 25-row is recommended minimum
#       format).
#
#       Optional: Font type, font size, screen columns and screen
#       rows are established by manual user actions.
#
# Capabilities:
#
#    1. Defines the key codes to be associated with the terminal
#       console keyboard.
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Classes:
#
#    None
#
# Methods:
#
#    None
#
# Modifications:
#
#    2015/03/17 rsg Extracted this code from the module named
#                   tsWxGraphicalTextUserInterface.py so as
#                   to facilitate the editing and maintenance
#                   of both files.
#
# ToDo:
#
#    None
#
##############################################################

__title__     = 'tsWxCursesKeyCodesDataBase'
__version__   = '2.42.1'
__date__      = '03/17/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibGUI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Curses Module API & ' + \
                'Run Time Library Features:' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  wxWidgets (formerly wxWindows) & ' + \
                'wxPython API Features:' + \
                '\n\t  Copyright (c) 1992-2008 Julian Smart, ' + \
                'Robert Roebling,' + \
                '\n\t\t\tVadim Zeitlin and other members of the ' + \
                '\n\t\t\twxWidgets team.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  wxWindows Library License' + \
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t\t\tfor Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 Free Software ' + \
                '\n\t\t\tFoundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  nCurses README,v 1.23 2006/04/22' + \
                '\n\n\t  RGB to Color Name Mapping (Triplet and Hex)' + \
                '\n\t  Copyright (c) 2010 Kevin J. Walsh' + \
                '\n\t\t\tAll rights reserved.'

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

#---------------------------------------------------------------------------

import curses
import curses.ascii

#---------------------------------------------------------------------------

# Set of key codes that curses guarantees to recognize

##KEY_BREAK            = 0x00000101
##KEY_DOWN             = 0x00000102
##KEY_UP               = 0x00000103
##KEY_LEFT             = 0x00000104
##KEY_RIGHT            = 0x00000105
##KEY_HOME             = 0x00000106
##KEY_BACKSPACE        = 0x00000107
##KEY_F0               = 0x00000108
##KEY_F1               = 0x00000109
##KEY_F2               = 0x0000010A
##KEY_F3               = 0x0000010B
##KEY_F4               = 0x0000010C
##KEY_F5               = 0x0000010D
##KEY_F6               = 0x0000010E
##KEY_F7               = 0x0000010F
##KEY_F8               = 0x00000110
##KEY_F9               = 0x00000111
##KEY_F10              = 0x00000112
##KEY_F11              = 0x00000113
##KEY_F12              = 0x00000114
##KEY_DL               = 0x00000148
##KEY_IL               = 0x00000149
##KEY_DC               = 0x0000014A
##KEY_IC               = 0x0000014B
##KEY_EIC              = 0x0000014C
##KEY_CLEAR            = 0x0000014D
##KEY_EOS              = 0x0000014E
##KEY_EOL              = 0x0000014F
##KEY_SF               = 0x00000150
##KEY_SR               = 0x00000151
##KEY_NPAGE            = 0x00000152
##KEY_PPAGE            = 0x00000153
##KEY_STAB             = 0x00000154
##KEY_CTAB             = 0x00000155
##KEY_CATAB            = 0x00000156
##KEY_ENTER            = 0x00000157
##KEY_SRESET           = 0x00000158
##KEY_RESET            = 0x00000159
##KEY_PRINT            = 0x0000015A
##KEY_LL               = 0x0000015B
##KEY_A1               = 0x0000015C
##KEY_A3               = 0x0000015D
##KEY_B2               = 0x0000015E
##KEY_C1               = 0x0000015F
##KEY_C3               = 0x00000160
##KEY_BTAB             = 0x00000161
##KEY_BEG              = 0x00000162
##KEY_CANCEL           = 0x00000163
##KEY_CLOSE            = 0x00000164
##KEY_COMMAND          = 0x00000165
##KEY_COPY             = 0x00000166
##KEY_CREATE           = 0x00000167
##KEY_END              = 0x00000168
##KEY_EXIT             = 0x00000169
##KEY_FIND             = 0x0000016A
##KEY_HELP             = 0x0000016B
##KEY_MARK             = 0x0000016C
##KEY_MESSAGE          = 0x0000016D
##KEY_MOVE             = 0x0000016E
##KEY_NEXT             = 0x0000016F
##KEY_OPEN             = 0x00000170
##KEY_OPTIONS          = 0x00000171
##KEY_PREVIOUS         = 0x00000172
##KEY_REDO             = 0x00000173
##KEY_REFERENCE        = 0x00000174
##KEY_REFRESH          = 0x00000175
##KEY_REPLACE          = 0x00000176
##KEY_RESTART          = 0x00000177
##KEY_RESUME           = 0x00000178
##KEY_SAVE             = 0x00000179
##KEY_SBEG             = 0x0000017A
##KEY_SCANCEL          = 0x0000017B
##KEY_SCOMMAND         = 0x0000017C
##KEY_SCOPY            = 0x0000017D
##KEY_SCREATE          = 0x0000017E
##KEY_SDC              = 0x0000017F
##KEY_SDL              = 0x00000180
##KEY_SELECT           = 0x00000181
##KEY_SEND             = 0x00000182
##KEY_SEOL             = 0x00000183
##KEY_SEXIT            = 0x00000184
##KEY_SFIND            = 0x00000185
##KEY_SHELP            = 0x00000186
##KEY_SHOME            = 0x00000187
##KEY_SIC              = 0x00000188
##KEY_SLEFT            = 0x00000189
##KEY_SMESSAGE         = 0x0000018A
##KEY_SMOVE            = 0x0000018B
##KEY_SNEXT            = 0x0000018C
##KEY_SOPTIONS         = 0x0000018D
##KEY_SPREVIOUS        = 0x0000018E
##KEY_SPRINT           = 0x0000018F
##KEY_SREDO            = 0x00000190
##KEY_SREPLACE         = 0x00000191
##KEY_SRIGHT           = 0x00000192
##KEY_SRSUME           = 0x00000193
##KEY_SSAVE            = 0x00000194
##KEY_SSUSPEND         = 0x00000195
##KEY_SUNDO            = 0x00000196
##KEY_SUSPEND          = 0x00000197
##KEY_UNDO             = 0x00000198
##KEY_MOUSE            = 0x00000199
##KEY_RESIZE           = 0x0000019A
##KEY_MAX              = 0x000001FF

KeyCodes = {
    'name':                     'Curses Key Codes',
    curses.ascii.NUL:           'NULL CHAR',
    curses.ascii.SOH:           'START OF HEADING',
    curses.ascii.STX:           'START OF TEXT',
    curses.ascii.ETX:           'END OF TEXT',
    curses.ascii.EOT:           'END OF TRANSMISSION',
    curses.ascii.ENQ:           'ENQUIRY',
    curses.ascii.ACK:           'ACKNOWLEDGEMENT',
    curses.ascii.BEL:           'BELL',
    curses.ascii.BS:            'BACK SPACE',
    curses.ascii.TAB:           'HORIZONTAL TAB',
    curses.ascii.LF:            'LINE FEED',
    curses.ascii.VT:            'VERTICAL TAB',
    curses.ascii.FF:            'FORM FEED',
    curses.ascii.CR:            'CARRIAGE RETURN',
    curses.ascii.SO:            'SHIFT OUT / X-ON',
    curses.ascii.SI:            'SHIFT IN / X-OFF',
    curses.ascii.DLE:           'DATA LINE ESCAPE',
    curses.ascii.DC1:           'DEVICE CONTROL 1 (oft. XON)',
    curses.ascii.DC2:           'DEVICE CONTROL 2',
    curses.ascii.DC3:           'DEVICE CONTROL 3 (oft. XOFF)',
    curses.ascii.DC4:           'DEVICE CONTROL 4',
    curses.ascii.NAK:           'NEGATIVE ACKNOWLEDGEMENT',
    curses.ascii.SYN:           'SYNCHRONOUS IDLE',
    curses.ascii.ETB:           'END OF TRANSMIT BLOCK',
    curses.ascii.CAN:           'CANCEL',
    curses.ascii.EM:            'END OF MEDIUM',
    curses.ascii.SUB:           'SUBSTITUTE',
    curses.ascii.ESC:           'ESCAPE',
    curses.ascii.FS:            'FILE SEPARATOR',
    curses.ascii.GS:            'GROUP SEPARATOR',
    curses.ascii.RS:            'RECORD SEPARATOR',
    curses.ascii.US:            'UNIT SEPARATOR',
    curses.ascii.SP:            'SPACE',
    curses.ascii.DEL:           'DELETE',
    curses.KEY_MIN:             'KEY_MIN',
    curses.KEY_BREAK:           'KEY_BREAK',
    curses.KEY_DOWN:            'KEY_DOWN',
    curses.KEY_UP:              'KEY_UP',
    curses.KEY_LEFT:            'KEY_LEFT',
    curses.KEY_RIGHT:           'KEY_RIGHT',
    curses.KEY_HOME:            'KEY_HOME',
    curses.KEY_BACKSPACE:       'KEY_BACKSPACE',
    curses.KEY_F0:              'KEY_F0',
    curses.KEY_F1:              'KEY_F1',
    curses.KEY_F2:              'KEY_F2',
    curses.KEY_F3:              'KEY_F3',
    curses.KEY_F4:              'KEY_F4',
    curses.KEY_F5:              'KEY_F5',
    curses.KEY_F6:              'KEY_F6',
    curses.KEY_F7:              'KEY_F7',
    curses.KEY_F8:              'KEY_F8',
    curses.KEY_F9:              'KEY_F9',
    curses.KEY_F10:             'KEY_F10',
    curses.KEY_F11:             'KEY_F11',
    curses.KEY_F12:             'KEY_F12',
    curses.KEY_DL:              'KEY_DL',
    curses.KEY_IL:              'KEY_IL',
    curses.KEY_DC:              'KEY_DC',
    curses.KEY_IC:              'KEY_IC',
    curses.KEY_EIC:             'KEY_EIC',
    curses.KEY_CLEAR:           'KEY_CLEAR',
    curses.KEY_EOS:             'KEY_EOS',
    curses.KEY_EOL:             'KEY_EOL',
    curses.KEY_SF:              'KEY_SF',
    curses.KEY_SR:              'KEY_SR',
    curses.KEY_NPAGE:           'KEY_NPAGE',
    curses.KEY_PPAGE:           'KEY_PPAGE',
    curses.KEY_STAB:            'KEY_STAB',
    curses.KEY_CTAB:            'KEY_CTAB',
    curses.KEY_CATAB:           'KEY_CATAB',
    curses.KEY_ENTER:           'KEY_ENTER',
    curses.KEY_SRESET:          'KEY_SRESET',
    curses.KEY_RESET:           'KEY_RESET',
    curses.KEY_PRINT:           'KEY_PRINT',
    curses.KEY_LL:              'KEY_LL',
    curses.KEY_A1:              'KEY_A1',
    curses.KEY_A3:              'KEY_A3',
    curses.KEY_B2:              'KEY_B2',
    curses.KEY_C1:              'KEY_C1',
    curses.KEY_C3:              'KEY_C3',
    curses.KEY_BTAB:            'KEY_BTAB',
    curses.KEY_BEG:             'KEY_BEG',
    curses.KEY_CANCEL:          'KEY_CANCEL',
    curses.KEY_CLOSE:           'KEY_CLOSE',
    curses.KEY_COMMAND:         'KEY_COMMAND',
    curses.KEY_COPY:            'KEY_COPY',
    curses.KEY_CREATE:          'KEY_CREATE',
    curses.KEY_END:             'KEY_END',
    curses.KEY_EXIT:            'KEY_EXIT',
    curses.KEY_FIND:            'KEY_FIND',
    curses.KEY_HELP:            'KEY_HELP',
    curses.KEY_MARK:            'KEY_MARK',
    curses.KEY_MESSAGE:         'KEY_MESSAGE',
    curses.KEY_MOVE:            'KEY_MOVE',
    curses.KEY_NEXT:            'KEY_NEXT',
    curses.KEY_OPEN:            'KEY_OPEN',
    curses.KEY_OPTIONS:         'KEY_OPTIONS',
    curses.KEY_PREVIOUS:        'KEY_PREVIOUS',
    curses.KEY_REDO:            'KEY_REDO',
    curses.KEY_REFERENCE:       'KEY_REFERENCE',
    curses.KEY_REFRESH:         'KEY_REFRESH',
    curses.KEY_REPLACE:         'KEY_REPLACE',
    curses.KEY_RESTART:         'KEY_RESTART',
    curses.KEY_RESUME:          'KEY_RESUME',
    curses.KEY_SAVE:            'KEY_SAVE',
    curses.KEY_SBEG:            'KEY_SBEG',
    curses.KEY_SCANCEL:         'KEY_SCANCEL',
    curses.KEY_SCOMMAND:        'KEY_SCOMMAND',
    curses.KEY_SCOPY:           'KEY_SCOPY',
    curses.KEY_SCREATE:         'KEY_SCREATE',
    curses.KEY_SDC:             'KEY_SDC',
    curses.KEY_SDL:             'KEY_SDL',
    curses.KEY_SELECT:          'KEY_SELECT',
    curses.KEY_SEND:            'KEY_SEND',
    curses.KEY_SEOL:            'KEY_SEOL',
    curses.KEY_SEXIT:           'KEY_SEXIT',
    curses.KEY_SFIND:           'KEY_SFIND',
    curses.KEY_SHELP:           'KEY_SHELP',
    curses.KEY_SHOME:           'KEY_SHOME',
    curses.KEY_SIC:             'KEY_SIC',
    curses.KEY_SLEFT:           'KEY_SLEFT',
    curses.KEY_SMESSAGE:        'KEY_SMESSAGE',
    curses.KEY_SMOVE:           'KEY_SMOVE',
    curses.KEY_SNEXT:           'KEY_SNEXT',
    curses.KEY_SOPTIONS:        'KEY_SOPTIONS',
    curses.KEY_SPREVIOUS:       'KEY_SPREVIOUS',
    curses.KEY_SPRINT:          'KEY_SPRINT',
    curses.KEY_SREDO:           'KEY_SREDO',
    curses.KEY_SREPLACE:        'KEY_SREPLACE',
    curses.KEY_SRIGHT:          'KEY_SRIGHT',
    curses.KEY_SRSUME:          'KEY_SRSUME',
    curses.KEY_SSAVE:           'KEY_SSAVE',
    curses.KEY_SSUSPEND:        'KEY_SSUSPEND',
    curses.KEY_SUNDO:           'KEY_SUNDO',
    curses.KEY_SUSPEND:         'KEY_SUSPEND',
    curses.KEY_UNDO:            'KEY_UNDO',
    curses.KEY_MOUSE:           'KEY_MOUSE',
    curses.KEY_RESIZE:          'KEY_RESIZE',
    curses.KEY_MAX:             'KEY_MAX'
    }

#---------------------------------------------------------------------------

if __name__ == '__main__':
 
    print(__header__)
