#! /usr/bin/env python
#"Time-stamp: <06/01/2013  7:19:17 AM rsg>"
'''
tsCommandLineInterface.py - Class establishes methods that
prompt or re-prompt the operator for input, validate that the
operator has supplied the expected number of inputs and that
each is of the expected type.

'''
#################################################################
#
# File: tsCommandLineInterface.py
#
# Purpose:
#
#     Class establishes methods that prompt or re-prompt the
#     operator for input, validate that the operator has supplied
#     the expected number of inputs and that each is of the
#     expected type.
#
# Limitations:
#
#    1. Input Interface
#
#       Required: Computer Keyboard (industry standard mult-button).
#
#           (stdin used to read a line of text)
#
#    2. Output Interface
#
#       Required: Computer Monitor (industry standard Monochrome or
#       Color).
#
#           (stdout used for consoleLoggingThreshold < Logger.WARNING
#            stderr used for consoleLoggingThreshold >= Logger.WARNING)
#
# Usage (example):
#
#     ## Import Module
#     import tsCommandLineInterface as tsCLI
#
#     ## Instantiate Module
#     myUserInterface = tsCLI.CommandLineInterface()
#
#     ## Reference Module Methods
#     myUserInterface.startup()
#     reply = myUserInterface.keyboard(prompt)
#     myUserInterface.display(reply)
#     myUserInterface.display('INFO: %s' % reply, stderr=False)
#     myUserInterface.display('ERROR: %s' % reply, stderr=True)
#     myUserInterface.shutdown(msg, stderr=False)
#
# Methods:
#
# ToDo:
#   1. TBD.
#
# Modifications:
#
#################################################################

__title__     = 'tsCommandLineInterface'
__version__   = '1.2.2'
__date__      = '06/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if ((len(__credits__) == 0)):
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#---------------------------------------------------------------------------

import sys

#---------------------------------------------------------------------------

class CommandLineInterface(object):
    '''
    Class establishes methods that prompt or re-prompt the operator
    for input, validate that the operator has supplied the expected
    number of inputs and that each is of the expected type.
    '''
    def __init__(self):
        '''
        Instantiate class variables.
        '''
        # Register standard console devices
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    #-----------------------------------------------------------------------

    def keyboard(self, thePrompt, indent=0):
        '''
        Display a prompt and input text from the console keyboard.
        '''
        self.infoDisplay('%s ' % thePrompt, indent=indent)
        theReply = self.stdin.readline().strip('\n')

        return (theReply, thePrompt)

    #-----------------------------------------------------------------------

    def infoDisplay(self, theInfo, indent=0):
        '''
        Output message to the standard output console.
        '''
        if indent > 0:
            self.stdout.write('\n%s%s' % (' ' * indent, theInfo))
        else:
            self.stdout.write('\n%s' % theInfo)

    #-----------------------------------------------------------------------

    def errorDisplay(self, theError, indent=0):
        '''
        Output message to the standard error console.
        '''
        if indent > 0:
            self.stderr.write('\n%s%s' % (' ' * indent, theError))
        else:
            self.stderr.write('\n%s' % theError)

    #-----------------------------------------------------------------------

    def multiFieldInput(self,
                        prompt,
                        fmt='%s',
                        delimeter=',',
                        container=None,
                        indent=0,
                        debug=False):
        '''
        Display a prompt and input multiple entries from the console keyboard.
        '''

        fmtTypes = fmt.split(',')
        if debug:
            print('  fmtTypes  = "%s"' % str(fmtTypes))
            print('  delimeter = "%s"' % delimeter)
            print('  container = "%s"' % container)
        values = []
        done = False
        while not done:
            try:
                text = input('%s%s' % (' ' * indent, prompt))

                args = text.split(delimeter)
                argc = len(fmtTypes)

                if debug:
                    print('  text="%s"' % text)
                    print('  args=%s' % str(args))
                    print('  argc=%d' % argc)

                for i in range(0, argc):

                    if fmtTypes[i].strip() == '%d':
                        values += [int(args[i])]
                    elif fmtTypes[i].strip() == '%f':
                        values += [float(args[i])]
                    else:
                        values += [args[i]]

                done = True

            except Exception as e:
                print('  EXCEPTION: e=%s' % e)

        if debug:
            print('  values=%s' % str(values))

        if container is None and \
           len(values) == 1:

            # single string, integer or float
            return values[0]

        elif container is tuple:

            # tuple of string(s), integer(s) and/or float(s)
            return tuple(values)

        else:

            # list of string(s), integer(s) and/or float(s)
            return values

#---------------------------------------------------------------------------

if __name__ == "__main__":

    print(__header__)

    myCLI = CommandLineInterface()

    answer = myCLI.multiFieldInput(
        'single field; default format? ', indent=4, debug=True)
    print('  answer type = %s; answer= "%s"' % (type(answer), answer))
    print('\n\n')

    fmt = '%s,%f,%d'
    answer = myCLI.multiFieldInput(
        'three fields; format=%s? ' % fmt, fmt, indent=4, debug=True)
    print('  answer type = %s; answer= "%s"' % (type(answer), answer))
    print('\n\n')
