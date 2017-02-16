#! /usr/bin/env python
#"Time-stamp: <05/12/2014  6:27:13 AM rsg>"
#
'''
tsCommandLineParserBuilder.py - Class for parsing command-line options. It
uses a declarative style of command-line parsing: you create
an instance of tsCommandLineParserBuilder, populate it with options, and parse
the command line. It allows users to specify options in the
conventional GNU/POSIX syntax, and additionally generates usage
and help messages for you.
'''
#################################################################
#
# File: tsCommandLineParserBuilder.py
#
# Purpose:
#
#    Class for parsing command-line options. It uses a declarative
#    style of command-line parsing: you create an instance of
#    tsCommandLineParserBuilder, populate it with options, and parse the
#    command line. It allows users to specify options in the
#    conventional GNU/POSIX syntax, and additionally generates usage
#    and help messages for you.
#
# Limitations:
#
#
# Notes:
#
#    None.
#
# Usage (example):
#
#     ## Import Module
#     import tsCommandLineParserBuilder
#
# Methods:
#
# Modifications:
#
# ToDo:
#
#################################################################

__title__     = 'tsCommandLineParserBuilder'
__version__   = '1.6.0'
__date__      = '04/19/2013'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
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

from optparse import OptionParser, Option
import sys
import traceback

try:

    import tsExceptions as tse
    import tsApplication as tsAPP

except ImportError, importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

class TsOptionParser(OptionParser):

    rangeKey = 'range'
    minimumArgumentRange = 0
    maximumArgumentRange = 1

    def __init__(self,
                 usage=None,
                 option_list=None,
                 option_class=Option,
                 version=None,
                 conflict_handler="error",
                 description=None,
                 formatter=None,
                 add_help_option=True,
                 prog=None,
                 epilog=None,
                 argsDefinitions=None):
        """
        Instance attributes:
          usage : string
            a usage string for your program.  Before it is displayed
            to the user, "%prog" will be expanded to the name of
            your program (self.prog or os.path.basename(sys.argv[0])).
          prog : string
            the name of the current program (to override
            os.path.basename(sys.argv[0])).
          epilog : string
            paragraph of help text to print after option help

          option_groups : [OptionGroup]
            list of option groups in this parser (option groups are
            irrelevant for parsing the command-line, but very useful
            for generating help)

          allow_interspersed_args : bool = true
            if true, positional arguments may be interspersed with options.
            Assuming -a and -b each take a single argument, the command-line
              -ablah foo bar -bboo baz
            will be interpreted the same as
              -ablah -bboo -- foo bar baz
            If this flag were false, that command line would be interpreted as
              -ablah -- foo bar -bboo baz
            -- ie. we stop processing options as soon as we see the first
            non-option argument.  (This is the tradition followed by
            Python's getopt module, Perl's Getopt::Std, and other argument-
            parsing libraries, but it is generally annoying to users.)

          process_default_values : bool = true
            if true, option default values are processed similarly to option
            values from the command line: that is, they are passed to the
            type-checking function for the option's type (as long as the
            default value is a string).  (This really only matters if you
            have defined custom types; see SF bug #955889.)  Set it to false
            to restore the behaviour of Optik 1.4.1 and earlier.

          rargs : [string]
            the argument list currently being parsed.  Only set when
            parse_args() is active, and continually trimmed down as
            we consume arguments.  Mainly there for the benefit of
            callback options.
          largs : [string]
            the list of leftover arguments that we have skipped while
            parsing options.  If allow_interspersed_args is false, this
            list is always empty.
          values : Values
            the set of option values currently being accumulated.  Only
            set when parse_args() is active.  Also mainly for callbacks.
 
        """
        OptionParser.__init__(self,
                              usage=usage,
                              option_list=option_list,
                              option_class=option_class,
                              version=version,
                              conflict_handler=conflict_handler,
                              description=description,
                              formatter=formatter,
                              add_help_option=add_help_option,
                              prog=prog,
                              epilog=epilog)
 
        self.ts_argsDefinitions = argsDefinitions
 
    def check_values(self, values, args):
        """

        argDefinitions is a dictionary.  It contains the minimum
        and maximum number of arguments.  There is a key for each
        argument number which indicates the type.  The values for
        type keys are the python types (Note: not a string)
        Types allowed are:
          None : do not check
          int  : argument string must convert to an integer
          long : argument string must convert to a long
          float: argument string must convert to float
          str  : argument string must convert to string
 
        range : tuple with minimum and maximum arguments
            1 : type of argument number 1
 
        check_values(values : Values, args : [string])
        -> (values : Values, args : [string])

        Check that the supplied option values and leftover arguments are
        valid.  Returns the option values and leftover arguments
        (possibly adjusted, possibly completely new -- whatever you
        like).  Default implementation just returns the passed-in
        values; subclasses may override as desired.
        """

        # Should we check the arguments?
        if self.ts_argsDefinitions is not None:
            # Yes, number range first
            numberOfArgs = len(args)
            try:
                minimumAguments = self.ts_argsDefinitions[self.rangeKey][self.minimumArgumentRange]
                maximumArguments = self.ts_argsDefinitions[self.rangeKey][self.maximumArgumentRange]
            except KeyError, e:
                raise tse.ProgramException(tse.LOGIC_ERROR, 'Invalid argument definitions: %s key not found' % self.rangeKey)
            # number range check
            if numberOfArgs < minimumAguments or numberOfArgs > maximumArguments:
                if minimumAguments == maximumArguments:
                    expected = '%d' % minimumAguments
                else:
                    expected = '%d to %d' % (minimumAguments, maximumArguments)
 
                self.print_help()
                self.error('Invalid number of arguments: %d, expected: %s' % (numberOfArgs, expected))
 
            # Check the argument types
            for argumentNumber in xrange(numberOfArgs):
                try:
                    argumentType = self.ts_argsDefinitions[argumentNumber + 1]
                except KeyError:
                    continue
                if argumentType is None:
                    continue
                try:
                    argumentType(args[argumentNumber])
                except ValueError, e:
                    self.print_help()
                    self.error('Invalid argument %d, expected %s, received: %s' % (argumentNumber + 1, argumentType, args[argumentNumber]))
 
        return (values, args)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def getOptions():
        '''
        Parse the command line and return a list of positional arguments
        and a dictionanary of keyword options.

        NOTE: Requirement is an inappropriate, oversimplification.
              Invoking argparse or optparse (deprecated with Python 2.7.0)
              do not produce equivalent output without substantial post
              processing that has not yet been created. This may explain
              inability to migrate use of tsApplication to tsCommandLineEnv
              or to tsWxMultiFrameEnv.
        '''
        parser = OptionParser(usage='''\
        %prog [options]...

        Capture current hardware and software information
        about the run time environment for the user process.
        ''')

        (options, args) = parser.parse_args()
        if len(args) != 0:
            parser.print_help()
            sys.exit(1)

        return (args, options)

    #----------------------------------------------------------------------

    def mainTest(*args, **kw):
        print(__header__)
        print('tsCommandLineParserBuilder.mainTest: ' + \
              'args=%s; kw=%s' % (str(args), str(kw)))

    #----------------------------------------------------------------------

    exitStatus = tse.NONERROR_ERROR_CODE
    msg = tse.NO_ERROR

    try:

        theApplication = tsAPP.TsApplication(
                buildTitle=__title__,
                buildVersion=__version__,
                buildDate=__date__,
                buildAuthors=__authors__,
                buildCopyright=__copyright__,
                buildLicense=__license__,
                buildCredits=__credits__,
                buildTitleVersionDate=mainTitleVersionDate,
                buildHeader=__header__,
                getOptions=getOptions,
                runTimeTitle='main',
                logs=[],
                runTimeEntryPoint=mainTest)

        theApplication.runMainApplication()

    except Exception, e:
        if isinstance(e, tse.TsExceptions):
            msg = str(e).replace("'", "")
            tse.displayError(e)
            exitStatus = e.exitCode
        else:
            msg = None
            sys.stderr.write(traceback.format_exc())
            exitStatus = tse.INVALID_ERROR_CODE

    if msg == tse.NO_ERROR:
        sys.stdout.write('\n' + msg + '\n')
    elif msg is not None:
        sys.stderr.write(msg + '\n')

    # Return (exitStatus)
    sys.exit(exitStatus)
