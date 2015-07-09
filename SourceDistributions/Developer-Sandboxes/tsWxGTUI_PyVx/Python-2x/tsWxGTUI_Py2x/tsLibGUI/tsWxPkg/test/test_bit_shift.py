#! /usr/bin/env python
# "Time-stamp: <03/27/2014  7:51:43 AM rsg>"
'''
test_bit_shift.py - Module to establish the number of bits
needed to represent the foreground and background color
palette associated with a specific terminal emulator.
'''

import math

__title__     = 'test_bit_shift'
__version__   = '1.0.0'
__date__      = '03/27/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2014 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'

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

print('%s' % __header__)
print('%s' % __doc__)

print('%18s  %11s  %16s' % ('TERMINAL EMULATOR',
                            'COLOR_COUNT',
                            'BIT_SHIFT_TO_USE'))

print('%18s  %11s  %16s' % ('-' * 18,
                            '-' * 11,
                            '-' * 16))

set_to_use_count = [8, 16, 32, 64, 70, 88, 128, 141, 256]
last_bit_shift = 0
for color_count in set_to_use_count:
    if color_count <= 8:
        emulator = 'xterm'
    elif color_count <= 16:
        emulator = 'xterm-16color'
    elif color_count <= 88:
        emulator = 'xterm-88color'
    elif color_count <= 256:
        emulator = 'xterm-256color'
    bit_shift_to_use = int(math.log(color_count, 2))
    if bit_shift_to_use != last_bit_shift:
        last_bit_shift = bit_shift_to_use
        print('')
    print('%18s  %11s  %16s' % (
        str(emulator), str(color_count),str(bit_shift_to_use)))
