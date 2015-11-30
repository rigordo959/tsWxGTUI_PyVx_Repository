#! /usr/bin/env python
# "Time-stamp: <05/05/2015  6:07:54 AM rsg>"
'''

   ===================================================
   T e c h n i c a l    P r e v i e w    E d i t i o n
   ===================================================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./tsWxGTUI_PyVx/Documents".

'''
#################################################################
#
# File: say_hello.py
#
# Purpose:
#
#    The common script used by both developers and installers
#    of the TeamSTARS "tsWxGTUI_PyVx" Toolkit. It identifies:
#
#    1. TeamSTARS "tsWxGTUI_PyVx" Toolkit masthead, the name
#       of a publication (as a newspaper) displayed on the
#       top of the first page.
#    2. supported TeamSTARS "tsWxGTUI_PyVx" Toolkit software
#       distribution
#    3. current working directory
#    4. python version
#    5. copyright holder
#    6. recipient's terms and conditions of TeamSTARS "tsWxGTUI"
#       Toolkit software use, modifiction and redistribution
#    7. TeamSTARS "tsWxGTUI_PyVx" Toolkit warranty disclaimer
#
# Usage (examples):
#
#    python say_hello.py
#
# Methods:
#
#    None
#
# Classes:
#
#    None
#
# Modifications:
#
#    2014/11/14 rsg Added description of file's purpose and then
#                   re-organized output to reflect the purpose.
#
#    2015/02/15 rsg Update Toolkit masthead
#
#    2015/05/05 rsg Update Toolkit masthead
#
# ToDo:
#
#    None
#
#################################################################

#--------------------------------------------------------------------------

import os
import sys

cwd = os.getcwd()
tsPythonVersion = sys.version[0:5]

if (cwd.lower().find('python-1x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py1x'

elif (cwd.lower().find('python-2x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py2x'

elif (cwd.lower().find('python-3x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py3x'

elif (cwd.lower().find('python-4x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py4x'

elif (tsPythonVersion >= '1') and (tsPythonVersion < '2'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py1x'

elif (tsPythonVersion >= '2') and (tsPythonVersion < '3'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py2x'

elif (tsPythonVersion >= '3') and (tsPythonVersion < '4'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py3x'

else:

      # Presume default prefix
      prefix = 'tsWxGTUI_PyVx'

tsWxGTUI_PyVx = prefix

__title__     = '"%s" Toolkit' % prefix
__version__   = '0.0.0 (pre-alpha)'
__date__      = '05/05/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2010-2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License (GPL), ' + \
                'Version 3, 29 June 2007' + \
                '\n  GNU Free Documentation License (GFDL) 1.3, ' + \
                '3 November 2008'
__credits__   = ''
__disclaimer__ = '''
The "%s" Toolkit and its third-party components
are distributed as free and open source software. You may
use, modify and redistribute it only under the terms and
conditions set forth in the "COPYRIGHT.txt", "CREDITS.txt"
and "LICENSE.txt" files located in the directory
"./%s/Documents".

The "%s" Toolkit and its third-party components
are distributed in the hope that they will be useful, but
WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY
OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL THE ABOVE COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
''' % (tsWxGTUI_PyVx, 'tsWxGTUI_PyVx', tsWxGTUI_PyVx)

__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if len( __credits__) == 0:
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__line5__ = __disclaimer__

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n  %s\n' % (
    __line1__,
    __line2__,
    __line3__,
    __line4__,
    __line5__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

print(__doc__)
if (prefix == 'tsWxGTUI_Py2x') or (prefix == 'tsWxGTUI_Py3x'):
    print('   Supported Source Code Distribution:\n\t%s' % prefix)
else:
    print('   Unsupported Source Code Distribution:\n\t%s' % prefix)
print('   Current Working Directory:\n\t%s' % cwd)
print('   Python Version (Setup):\n\t%s' % tsPythonVersion)
print(__header__)
