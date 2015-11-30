#! /usr/bin/env python
#"Time-stamp: <03/08/2015  3:04:20 AM rsg>"
'''
tsExceptions.py - Class to define and handle error exceptions.
Maps run time exception types into 8-bit exit codes and prints
associated diagnostic message and traceback info.
'''
#################################################################
#
# File: tsExceptions.py
#
# Purpose:
#
#     Class to define and handle error exceptions. Maps run time
#     exception types into 8-bit exit codes and prints associated
#     diagnostic message and traceback info.
#
# Limitations:
#
#     1. ExitCode shall be an 8-bit value:
#                0 - Non-Error Error (i.e., Success)
#            value - <2-Bit Excepton Code> <6-Bit Error Code>
#              255 - Invalid Error Code
#
#     2. Bit-field width trades inefficient space utilization
#        for independent localization of exceptions.
#
# Usage (examples):
#
#     # Import
#     import tsExceptions as tse
#
#     def readFile(filename, mode)
#         try:
#             command = file(%s, %s) % filename, mode
#             myFile = file(filename, mode)
#         except IOError, (errno, strerr):
#             msg = 'Command=%s; ERRNO=%d; STRERR=%s' % \
#                   (command, errno, strerr)
#             raise tse.ProgramException(tse.IO_ERROR, msg)
#
#     if __name__ == "__main__":
#
#         exitStatus = tse.NONERROR_ERROR_CODE
#         msg = 'No Errors'
#
#         try:
#             filename = 'ShouldNotExist.txt'
#             mode = 'r'
#             readFile(filename, mode)
#         except Exception, e:
#             if isinstance(e, tse.TsExceptions):
#                 msg = str(e)
#                 tse.displayError(e)
#                 exitStatus = e.exitCode
#             else:
#                 msg = None
#                 sys.stderr.write(traceback.format_exc())
#                 exitStatus = tse.INVALID_ERROR_CODE
#
#         if msg == tse.NO_ERROR:
#             sys.stdout.write('%s' % msg)
#         elif msg is not None:
#             sys.stderr.write(msg.replace('"', ''))
#
#         # Return (exitStatus)
#         sys.exit(exitStatus)
#
# Modifications:
#
#    2013/07/13 rsg Added GRAPHICAL_WINDOW_RESIZED.
#
#    2013/07/17 rsg Added diagnostic exception placeholder
#                   errors so that UNKNOWN error produces
#                   exit code of 255.
#
# Notes:
#
#     1. Should exceptions pass error names or error codes
#        with error message?
#            Codes can be determined from manually set constants
#            or by looking up value associated with error name.
#
#            Names can be determined from manually set constants
#            or by looking up value associated with error code.
#
#            User friendliness favors readability of name. The
#            advantage of a name constant is compile time error
#            rather than run time detection. Changing the name
#            always requires changing each and every reference.
#
# To Do:
#
#     1. Review and finalize the available exceptions and errors.
#
#################################################################

__title__     = 'tsExceptions.py'
__version__   = '1.3.0'
__date__      = '07/17/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s. All rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 - Frederick A. Kier. ' + \
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

#--------------------------------------------------------------------------

import math
import os.path
import sys
import traceback

#--------------------------------------------------------------------------

__all__ = ['ABORT_BY_OPERATOR',
           'APPLICATION_TRAP',
           'ARGUMENT_KEY_NOT_VALID',
           'ARGUMENT_TYPE_NOT_VALID',
           'ARGUMENT_VALUE_NOT_VALID',
           'ARITHMETIC_ERROR',
           'CHARACTER_GRAPHICS_NOT_AVAILABLE',
           'COMMAND_LINE_ARGUMENT_DOES_NOT_EXIST',
           'COMMAND_LINE_ARGUMENT_NOT_UNIQUE',
           'COMMAND_LINE_ARGUMENT_NOT_VALID',
           'COMMAND_LINE_OPERATION_DOES_NOT_EXIST',
           'COMMAND_LINE_OPERATION_NOT_VALID',
           'COMMAND_LINE_OPTION_DOES_NOT_EXIST',
           'COMMAND_LINE_OPTION_NOT_VALID',
           'COMMAND_LINE_SWITCH_DOES_NOT_EXIST',
           'COMMAND_LINE_SWITCH_NOT_VALID',
           'COMMAND_LINE_SYNTAX_NOT_VALID',
           'DIAGNOSTIC_EXCEPTION',
           'DiagnosticException',
           'EXECUTABLE_IMAGE_DOES_NOT_EXIST',
           'EXECUTABLE_IMAGE_NOT_VALID',
           'EXECUTABLE_INSTRUCTION_NOT_VALID',
           'FILE_CREATE_ACCESS_NOT_PERMITTED',
           'FILE_DELETE_ACCESS_NOT_PERMITTED',
           'FILE_DIRECTORY_NOT_FOUND',
           'FILE_EXECUTE_ACCESS_NOT_PERMITTED',
           'FILE_NOT_FOUND',
           'FILE_READ_ACCESS_NOT_PERMITTED',
           'FILE_STORAGE_MEDIA_FULL',
           'FILE_WRITE_ACCESS_NOT_PERMITTED',
           'FORMAT_ERROR',
           'GRAPHICAL_BUTTON_NOT_VALID',
           'GRAPHICAL_DIALOG_NOT_VALID',
           'GRAPHICAL_MENU_NOT_VALID',
           'GRAPHICAL_WINDOW_RESIZED',
           'GRAPHICAL_WINDOW_DOES_NOT_EXIST',
           'GRAPHICAL_WINDOW_NOT_VALID',
           'INPUT_OUTPUT_EXCEPTION',
           'INTERRUPT_ALREADY_IN_USE',
           'INTERRUPT_DOES_NOT_EXIST',
           'INTERRUPT_RECEIVER_NOT_READY',
           'INTERRUPT_TRANSMITTER_NOT_READY',
           'INVALID_ERROR_CODE',
           'IO_ERROR',
           'InputOutputException',
           'LOGIC_ERROR',
           'NO_ERROR',
           'OS_ERROR',
           'PROGRAM_EXCEPTION',
           'ProgramException',
           'SIGNAL_ALREADY_IN_USE',
           'SIGNAL_DOES_NOT_EXIST',
           'SIGNAL_RECEIVER_NOT_READY',
           'SIGNAL_TRANSMITTER_NOT_READY',
           'SPURIOUS_INTERRUPT_RECEIVED',
           'SPURIOUS_SIGNAL_RECEIVED',
           'SYNTAX_ERROR',
           'TIMEOUT_ERROR',
           'TsExceptions',
           'UNKNOWN_ERROR',
           'USER_INTERFACE_EXCEPTION',
           'UserInterfaceException']

#--------------------------------------------------------------------------

NONERROR_ERROR_CODE = 0
INVALID_ERROR_CODE = 255

# Key/Value Constants that identify and describe the exceptions:
DIAGNOSTIC_EXCEPTION = 'Diagnostic Exception'
INPUT_OUTPUT_EXCEPTION = 'Input Output Exception'
PROGRAM_EXCEPTION = 'Program Exception'
USER_INTERFACE_EXCEPTION = 'User Interface Exception'

# Key/Value Constants that identify and describe the diagnostic exception
# errors:
UNKNOWN_ERROR = 'Unknown Error'

#--------------------------------------------------------------------------

# Key/Value Constants that identify and describe the input/output exception
# errors:
FILE_CREATE_ACCESS_NOT_PERMITTED = 'File Create Access Not Permitted'
FILE_DELETE_ACCESS_NOT_PERMITTED = 'File Delete Access Not Permitted'
FILE_DIRECTORY_NOT_FOUND = 'File Directory Not Found'
FILE_EXECUTE_ACCESS_NOT_PERMITTED = 'File Execute Access Not Permitted'
FILE_NOT_FOUND = 'File Not Found'
FILE_READ_ACCESS_NOT_PERMITTED = 'File Read Access Not Permitted'
FILE_STORAGE_MEDIA_FULL = 'File Storage Media Full'
FILE_WRITE_ACCESS_NOT_PERMITTED = 'File Write Access Not Permitted'
INTERRUPT_ALREADY_IN_USE = 'Interrupt Already In Use'
INTERRUPT_DOES_NOT_EXIST = 'Interrupt Does Not Exist'
INTERRUPT_RECEIVER_NOT_READY = 'Interrupt Receiver Not Ready'
INTERRUPT_TRANSMITTER_NOT_READY = 'Interrupt Transmitter Not Ready'
IO_ERROR = 'IO Error'
SIGNAL_ALREADY_IN_USE = 'Signal Already In Use'
SIGNAL_DOES_NOT_EXIST = 'Signal Does Not Exist'
SIGNAL_RECEIVER_NOT_READY = 'Signal Receiver Not Ready'
SIGNAL_TRANSMITTER_NOT_READY = 'Signal Transmitter Not Ready'
SPURIOUS_INTERRUPT_RECEIVED = 'Spurious Interrupt Received'
SPURIOUS_SIGNAL_RECEIVED = 'Spurious Signal Received'

#--------------------------------------------------------------------------

# Key/Value Constants that identify and describe the program exception errors:
NO_ERROR = 'No Error'
ABORT_BY_OPERATOR = 'Abort By Operator'
APPLICATION_TRAP = 'Application Trap'
ARGUMENT_KEY_NOT_VALID = 'Argument Key Not Valid'
ARGUMENT_TYPE_NOT_VALID = 'Argument Type Not Valid'
ARGUMENT_VALUE_NOT_VALID = 'Argument Value Not Valid'
ARITHMETIC_ERROR = 'Arithmetic Error'
EXECUTABLE_IMAGE_DOES_NOT_EXIST = 'Executable Image Does Not Exist'
EXECUTABLE_IMAGE_NOT_VALID = 'Executable Image Not Valid'
EXECUTABLE_INSTRUCTION_NOT_VALID = 'Executable Instruction Not Valid'
FORMAT_ERROR = 'Format Error'
LOGIC_ERROR = 'Logic Error'
OS_ERROR = 'OS Error'
SYNTAX_ERROR = 'Syntax Error'
TIMEOUT_ERROR = 'Timeout Error'

#--------------------------------------------------------------------------

# Key/Value Constants that identify and describe the user interface exception
# errors:
CHARACTER_GRAPHICS_NOT_AVAILABLE = 'Character Graphics Not Available'
COMMAND_LINE_ARGUMENT_DOES_NOT_EXIST = 'Command Line Argument Does Not Exist'
COMMAND_LINE_ARGUMENT_NOT_UNIQUE = 'Command Line Argument Not Unique'
COMMAND_LINE_ARGUMENT_NOT_VALID = 'Command Line Argument Not Valid'
COMMAND_LINE_OPERATION_DOES_NOT_EXIST = 'Command Line Operation Does Not Exist'
COMMAND_LINE_OPERATION_NOT_VALID = 'Command Line Operation Not Valid'
COMMAND_LINE_OPTION_DOES_NOT_EXIST = 'Command Line Option Does Not Exist'
COMMAND_LINE_OPTION_NOT_VALID = 'Command Line Option Not Valid'
COMMAND_LINE_SWITCH_DOES_NOT_EXIST = 'Command Line Switch Does Not Exist'
COMMAND_LINE_SWITCH_NOT_VALID = 'Command Line Switch Not Valid'
COMMAND_LINE_SYNTAX_NOT_VALID = 'Command Line Syntax Not Valid'
GRAPHICAL_BUTTON_NOT_VALID = 'Graphical Button Not Valid'
GRAPHICAL_DIALOG_NOT_VALID = 'Graphical Dialog Not Valid'
GRAPHICAL_MENU_NOT_VALID = 'Graphical Menu Not Valid'
GRAPHICAL_WINDOW_RESIZED = 'Graphical Window Resized'
GRAPHICAL_WINDOW_DOES_NOT_EXIST = 'Graphical Window Does Not Exist'
GRAPHICAL_WINDOW_NOT_VALID = 'Graphical Window Not Valid'

#---------------------------------------------------------------------------

def _buildMaps(names):
    '''
    Create listing of error names associated with each error code.
    '''
    itemNameFromCodeMap = {}
    itemCodeFromNameMap = {}
    itemCount = len(names)

    for i in range(itemCount):
##        # Create tabulation  of key/value constants
##        constant = names[i].upper().replace(' ', '_')
##        variable = names[i]
##        print "%s = '%s'" % (constant, variable)
        itemNameFromCodeMap[i] = names[i]
        itemCodeFromNameMap[names[i]] = i

    return (itemCount, itemCodeFromNameMap, itemNameFromCodeMap)

#--------------------------------------------------------------------------

def displayError(theException):
    '''
    Output the information that characterizes an exception.
    '''
    sys.stderr.write('\n%s\n' % theException.fullString)
    sys.stderr.write('\n  %s (%d); %s (%d);' % (
        theException.exceptionName,
        theException.exceptionCode,
        theException.errorName,
        theException.errorCode))
    sys.stderr.write(' ExitCode (%d).\n' % theException.exitCode)
    if theException.errorMessage == '':
        sys.stderr.write('\n    Details: %s.\n' % None)
    else:
        sys.stderr.write('\n    Details: %s.\n' % theException.errorMessage)
    sys.stderr.write('\n    Traceback (most recent call last):\n\n')
    tracebackLines = theException.tracebackString.split('\n')
    for line in tracebackLines:
        sys.stderr.write('      %s\n' % line)

#---------------------------------------------------------------------------

class TsExceptions(Exception):
    '''
    Base class for exceptions in this module.

    Class to define and handle error exceptions. Maps run time exception
    types into 8-bit exit codes and prints associated diagnostic message
    and traceback info.

    Attributes:
        theExceptionName - string indicating exception class
        theExceptionCode - code indicating exception class
        theErrorName     - string indicating error type
        theErrorCode     - code indicating error type
        theErrorMessage  - string describing cause of error
        tracebackList    - stack traceback as a list of strings
    '''
    exceptionNames = [PROGRAM_EXCEPTION,
                      INPUT_OUTPUT_EXCEPTION,
                      USER_INTERFACE_EXCEPTION,
                      DIAGNOSTIC_EXCEPTION]

    (exceptionCount,
     exceptionCodeFromNameMap,
     exceptionNameFromCodeMap) = _buildMaps(exceptionNames)

    #----------------------------------------------------------------------

    def __init__(self,
                 theExceptionName,
                 theExceptionCode,
                 theErrorName,
                 theErrorCode,
                 theErrorMessage,
                 tracebackList):
        '''
        Initialize base class.
        '''
        Exception.__init__(self)

        self.exceptionName = theExceptionName
        self.exceptionCode = theExceptionCode

        self.errorName = theErrorName
        self.errorCode = theErrorCode
 
        self.errorMessage = theErrorMessage

        self.exitCode = self.buildExitCode(theExceptionCode,
                                           theErrorCode)

        self.exitName = 'ExitCode #%d' % self.exitCode

        self.tracebackString = ''
        for item in tracebackList:
            self.tracebackString += item

        # Style: <Class Name>: '<Error Name>'
        if theErrorMessage is None or \
           theErrorMessage == '':
            self.fullString = '%s: %s. [%s]' % (
                self.exceptionName,
                self.errorName,
                self.exitName)
        else:
            self.fullString = '%s: %s; %s. [%s]' % (
                self.exceptionName,
                self.errorName,
                self.errorMessage,
                self.exitName)

    #----------------------------------------------------------------------

    def __str__(self):
        '''
        Called by the repr() built-in function and by string conversions
        (reverse quotes) to compute the ``official'' string representation
        of an object. If at all possible, this should look like a valid
        Python expression that could be used to recreate an object with
        the same value (given an appropriate environment). If this is not
        possible, a string of the form "<...some useful description...>"
        should be returned. The return value must be a string object. If
        a class defines __repr__() but not __str__(), then __repr__() is
        also used when an ``informal'' string representation of instances
        of that class is required.

        This is typically used for debugging, so it is important that the
        representation is information-rich and unambiguous.
        '''
        return repr(self.fullString)

    #----------------------------------------------------------------------

    def buildExitCode(self, exceptionCode, errorCode):
        '''
        Encode an exception ID into the upper bits and an error ID into
        the lower bits so that an 8-bit value is available for use upon
        process exit.
        '''
        # Calculate the return code
        #   The size is 8 bits
        #   Maximum error code is 255 decimal
        # Format:
        #   <3-Bit ExceptionCode><5-Bit ErrorCode> in hex
        #   0xff when either of them are too big
        bitsPerUpperField = int(math.log(self.exceptionCount)+ 1)
        bitsPerLowerField = 8 - bitsPerUpperField
        maximumNumberInUpperField = (2**bitsPerUpperField) - 1
        maximumNumberInLowerField = (2**bitsPerLowerField) - 1

##        print 'Exceptions: %d (%d-bits); Errors: %d (%d-bits)' % \
##              (maximumNumberInUpperField + 1, bitsPerUpperField,
##               maximumNumberInLowerField + 1, bitsPerLowerField)

        # Do they both fit?
        if exceptionCode <= maximumNumberInUpperField and \
           errorCode <= maximumNumberInLowerField:
            # Yes, put them together
            exitCode = (exceptionCode << \
                        bitsPerLowerField) + errorCode
        else:
            # No, force a 255
            exitCode = INVALID_ERROR_CODE

        return exitCode

#---------------------------------------------------------------------------
 
class DiagnosticException(TsExceptions):
    '''
    Exception raised for diagnostic errors.

    Attributes:
        theErrorName    - string indicating error type
        theErrorMessage - string describing cause of error
    '''
    errorNames = [
        'UNUSED_00',
        'UNUSED_01',
        'UNUSED_02',
        'UNUSED_03',
        'UNUSED_04',
        'UNUSED_05',
        'UNUSED_06',
        'UNUSED_07',
        'UNUSED_08',
        'UNUSED_09',
        'UNUSED_10',
        'UNUSED_11',
        'UNUSED_12',
        'UNUSED_13',
        'UNUSED_14',
        'UNUSED_15',
        'UNUSED_16',
        'UNUSED_17',
        'UNUSED_18',
        'UNUSED_19',
        'UNUSED_20',
        'UNUSED_21',
        'UNUSED_22',
        'UNUSED_23',
        'UNUSED_24',
        'UNUSED_25',
        'UNUSED_26',
        'UNUSED_27',
        'UNUSED_28',
        'UNUSED_29',
        'UNUSED_30',
        'UNUSED_31',
        'UNUSED_32',
        'UNUSED_33',
        'UNUSED_34',
        'UNUSED_35',
        'UNUSED_36',
        'UNUSED_37',
        'UNUSED_38',
        'UNUSED_39',
        'UNUSED_40',
        'UNUSED_41',
        'UNUSED_42',
        'UNUSED_43',
        'UNUSED_44',
        'UNUSED_45',
        'UNUSED_46',
        'UNUSED_47',
        'UNUSED_48',
        'UNUSED_49',
        'UNUSED_50',
        'UNUSED_51',
        'UNUSED_52',
        'UNUSED_53',
        'UNUSED_54',
        'UNUSED_55',
        'UNUSED_56',
        'UNUSED_57',
        'UNUSED_58',
        'UNUSED_59',
        'UNUSED_60',
        'UNUSED_61',
        'UNUSED_62',
        UNKNOWN_ERROR]

    (errorCount,
     errorCodeFromNameMap,
     errorNameFromCodeMap) = _buildMaps(errorNames)

    #----------------------------------------------------------------------

    def __init__(self, theErrorName, theErrorMessage):
        '''
        Handle exception.
        '''
        theExceptionName = DIAGNOSTIC_EXCEPTION
        try:
            theExceptionCode = self.exceptionCodeFromNameMap[theExceptionName]
        except KeyError:
            theExceptionCode = INVALID_ERROR_CODE
        try:
            theErrorCode = self.errorCodeFromNameMap[theErrorName]
        except KeyError:
            theErrorCode = INVALID_ERROR_CODE
        TsExceptions.__init__(self,
                              theExceptionName,
                              theExceptionCode,
                              theErrorName,
                              theErrorCode,
                              theErrorMessage,
                              traceback.format_stack())

#---------------------------------------------------------------------------
 
class InputOutputException(TsExceptions):
    '''
    Exception raised for Input/Output errors.

    Attributes:
        theErrorName    - string indicating error type
        theErrorMessage - string describing cause of error
    '''
    errorNames = [
        FILE_CREATE_ACCESS_NOT_PERMITTED,
        FILE_DELETE_ACCESS_NOT_PERMITTED,
        FILE_DIRECTORY_NOT_FOUND,
        FILE_EXECUTE_ACCESS_NOT_PERMITTED,
        FILE_NOT_FOUND,
        FILE_READ_ACCESS_NOT_PERMITTED,
        FILE_STORAGE_MEDIA_FULL,
        FILE_WRITE_ACCESS_NOT_PERMITTED,
        INTERRUPT_ALREADY_IN_USE,
        INTERRUPT_DOES_NOT_EXIST,
        INTERRUPT_RECEIVER_NOT_READY,
        INTERRUPT_TRANSMITTER_NOT_READY,
        IO_ERROR,
        SIGNAL_ALREADY_IN_USE,
        SIGNAL_DOES_NOT_EXIST,
        SIGNAL_RECEIVER_NOT_READY,
        SIGNAL_TRANSMITTER_NOT_READY,
        SPURIOUS_INTERRUPT_RECEIVED,
        SPURIOUS_SIGNAL_RECEIVED,
        'UNUSED_19',
        'UNUSED_20',
        'UNUSED_21',
        'UNUSED_22',
        'UNUSED_23',
        'UNUSED_24',
        'UNUSED_25',
        'UNUSED_26',
        'UNUSED_27',
        'UNUSED_28',
        'UNUSED_29',
        'UNUSED_30',
        'UNUSED_31',
        'UNUSED_32',
        'UNUSED_33',
        'UNUSED_34',
        'UNUSED_35',
        'UNUSED_36',
        'UNUSED_37',
        'UNUSED_38',
        'UNUSED_39',
        'UNUSED_40',
        'UNUSED_41',
        'UNUSED_42',
        'UNUSED_43',
        'UNUSED_44',
        'UNUSED_45',
        'UNUSED_46',
        'UNUSED_47',
        'UNUSED_48',
        'UNUSED_49',
        'UNUSED_50',
        'UNUSED_51',
        'UNUSED_52',
        'UNUSED_53',
        'UNUSED_54',
        'UNUSED_55',
        'UNUSED_56',
        'UNUSED_57',
        'UNUSED_58',
        'UNUSED_59',
        'UNUSED_60',
        'UNUSED_61',
        'UNUSED_62',
        'UNUSED_63'
        ]

    (errorCount,
     errorCodeFromNameMap,
     errorNameFromCodeMap) = _buildMaps(errorNames)

    #----------------------------------------------------------------------

    def __init__(self, theErrorName, theErrorMessage):
        '''
        Handle exception.
        '''
        theExceptionName = INPUT_OUTPUT_EXCEPTION
        try:
            theExceptionCode = self.exceptionCodeFromNameMap[theExceptionName]
        except KeyError:
            theExceptionCode = INVALID_ERROR_CODE
        try:
            theErrorCode = self.errorCodeFromNameMap[theErrorName]
        except KeyError:
            theErrorCode = INVALID_ERROR_CODE
        TsExceptions.__init__(self,
                              theExceptionName,
                              theExceptionCode,
                              theErrorName,
                              theErrorCode,
                              theErrorMessage,
                              traceback.format_stack())

#---------------------------------------------------------------------------

class ProgramException(TsExceptions):
    '''
    Exception raised for program errors.

    Attributes:
        theErrorName    - string indicating error type
        theErrorMessage - string describing cause of error
    '''
    errorNames = [
        NO_ERROR,
        ABORT_BY_OPERATOR,
        APPLICATION_TRAP,
        ARGUMENT_KEY_NOT_VALID,
        ARGUMENT_TYPE_NOT_VALID,
        ARGUMENT_VALUE_NOT_VALID,
        ARITHMETIC_ERROR,
        EXECUTABLE_IMAGE_DOES_NOT_EXIST,
        EXECUTABLE_IMAGE_NOT_VALID,
        EXECUTABLE_INSTRUCTION_NOT_VALID,
        FORMAT_ERROR,
        LOGIC_ERROR,
        OS_ERROR,
        SYNTAX_ERROR,
        TIMEOUT_ERROR,
        'UNUSED_15',
        'UNUSED_16',
        'UNUSED_17',
        'UNUSED_18',
        'UNUSED_19',
        'UNUSED_20',
        'UNUSED_21',
        'UNUSED_22',
        'UNUSED_23',
        'UNUSED_24',
        'UNUSED_25',
        'UNUSED_26',
        'UNUSED_27',
        'UNUSED_28',
        'UNUSED_29',
        'UNUSED_30',
        'UNUSED_31',
        'UNUSED_32',
        'UNUSED_33',
        'UNUSED_34',
        'UNUSED_35',
        'UNUSED_36',
        'UNUSED_37',
        'UNUSED_38',
        'UNUSED_39',
        'UNUSED_40',
        'UNUSED_41',
        'UNUSED_42',
        'UNUSED_43',
        'UNUSED_44',
        'UNUSED_45',
        'UNUSED_46',
        'UNUSED_47',
        'UNUSED_48',
        'UNUSED_49',
        'UNUSED_50',
        'UNUSED_51',
        'UNUSED_52',
        'UNUSED_53',
        'UNUSED_54',
        'UNUSED_55',
        'UNUSED_56',
        'UNUSED_57',
        'UNUSED_58',
        'UNUSED_59',
        'UNUSED_60',
        'UNUSED_61',
        'UNUSED_62',
        'UNUSED_63'
        ]

    (errorCount,
     errorCodeFromNameMap,
     errorNameFromCodeMap) = _buildMaps(errorNames)

    #----------------------------------------------------------------------

    def __init__(self, theErrorName, theErrorMessage):
        '''
        Handle exception.
        '''
        theExceptionName = PROGRAM_EXCEPTION
        try:
            theExceptionCode = self.exceptionCodeFromNameMap[theExceptionName]
        except KeyError:
            theExceptionCode = INVALID_ERROR_CODE
        try:
            theErrorCode = self.errorCodeFromNameMap[theErrorName]
        except KeyError:
            theErrorCode = INVALID_ERROR_CODE
        TsExceptions.__init__(self,
                              theExceptionName,
                              theExceptionCode,
                              theErrorName,
                              theErrorCode,
                              theErrorMessage,
                              traceback.format_stack())

#---------------------------------------------------------------------------

class UserInterfaceException(TsExceptions):
    '''
    Exception raised for program errors.

    Attributes:
        theErrorName    - string indicating error type
        theErrorMessage - string describing cause of error
    '''
    errorNames = [
        CHARACTER_GRAPHICS_NOT_AVAILABLE,
        COMMAND_LINE_ARGUMENT_DOES_NOT_EXIST,
        COMMAND_LINE_ARGUMENT_NOT_UNIQUE,
        COMMAND_LINE_ARGUMENT_NOT_VALID,
        COMMAND_LINE_OPERATION_DOES_NOT_EXIST,
        COMMAND_LINE_OPERATION_NOT_VALID,
        COMMAND_LINE_OPTION_DOES_NOT_EXIST,
        COMMAND_LINE_OPTION_NOT_VALID,
        COMMAND_LINE_SWITCH_DOES_NOT_EXIST,
        COMMAND_LINE_SWITCH_NOT_VALID,
        COMMAND_LINE_SYNTAX_NOT_VALID,
        GRAPHICAL_BUTTON_NOT_VALID,
        GRAPHICAL_DIALOG_NOT_VALID,
        GRAPHICAL_MENU_NOT_VALID,
        GRAPHICAL_WINDOW_RESIZED,
        GRAPHICAL_WINDOW_DOES_NOT_EXIST,
        GRAPHICAL_WINDOW_NOT_VALID,
        'UNUSED_17',
        'UNUSED_18',
        'UNUSED_19',
        'UNUSED_20',
        'UNUSED_21',
        'UNUSED_22',
        'UNUSED_23',
        'UNUSED_24',
        'UNUSED_25',
        'UNUSED_26',
        'UNUSED_27',
        'UNUSED_28',
        'UNUSED_29',
        'UNUSED_30',
        'UNUSED_31',
        'UNUSED_32',
        'UNUSED_33',
        'UNUSED_34',
        'UNUSED_35',
        'UNUSED_36',
        'UNUSED_37',
        'UNUSED_38',
        'UNUSED_39',
        'UNUSED_40',
        'UNUSED_41',
        'UNUSED_42',
        'UNUSED_43',
        'UNUSED_44',
        'UNUSED_45',
        'UNUSED_46',
        'UNUSED_47',
        'UNUSED_48',
        'UNUSED_49',
        'UNUSED_50',
        'UNUSED_51',
        'UNUSED_52',
        'UNUSED_53',
        'UNUSED_54',
        'UNUSED_55',
        'UNUSED_56',
        'UNUSED_57',
        'UNUSED_58',
        'UNUSED_59',
        'UNUSED_60',
        'UNUSED_61',
        'UNUSED_62',
        'UNUSED_63'
        ]

    (errorCount,
     errorCodeFromNameMap,
     errorNameFromCodeMap) = _buildMaps(errorNames)

    #----------------------------------------------------------------------

    def __init__(self, theErrorName, theErrorMessage):
        '''
        Handle exception.
        '''
        theExceptionName = USER_INTERFACE_EXCEPTION
        try:
            theExceptionCode = self.exceptionCodeFromNameMap[theExceptionName]
        except KeyError:
            theExceptionCode = INVALID_ERROR_CODE
        try:
            theErrorCode = self.errorCodeFromNameMap[theErrorName]
        except KeyError:
            theErrorCode = INVALID_ERROR_CODE
        TsExceptions.__init__(self,
                              theExceptionName,
                              theExceptionCode,
                              theErrorName,
                              theErrorCode,
                              theErrorMessage,
                              traceback.format_stack())

#--------------------------------------------------------------------------
 
if __name__ == "__main__":

    print(__header__)
