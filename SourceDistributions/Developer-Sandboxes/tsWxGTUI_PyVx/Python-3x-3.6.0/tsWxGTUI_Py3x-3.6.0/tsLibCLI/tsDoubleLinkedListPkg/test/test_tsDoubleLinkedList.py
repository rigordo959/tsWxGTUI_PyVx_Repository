#! /usr/bin/env python
#"Time-stamp: <02/23/2015  5:21:46 AM rsg>"
'''
test_tsDoubleLinkedList.py - Application program to validate and
demonstrate the features of the tsDoubleLinkedList.
'''
#################################################################
#
# File: test_tsDoubleLinkedList.py
#
# Purpose:
#
#    Application program to validate and
#    demonstrate the features of the tsDoubleLinkedList.
#
# Usage (example):
#
#     python test_tsDoubleLinkedList.py
#
# Methods:
#
# Modifications:
#
#    2014/02/09 rsg Added Python 3.x conversion of Python 2.x
#                   version.
#
# ToDo:
#
#   None
#
#################################################################

__title__     = 'test_tsDoubleLinkedList'
__version__   = '1.1.0'
__date__      = '02/09/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013-2014 ' + \
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

#--------------------------------------------------------------------------

import os.path
import platform
import sys
import time

#--------------------------------------------------------------------------

try:

    import tsLibCLI

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

try:

    import tsExceptions as tse
    import tsLogger as Logger

    import tsOperatorSettingsParser

    from tsCommandLineEnv import CommandLineEnv
    from tsDoubleLinkedList import DoubleLinkedList

except ImportError as importCode:

    print('%s: ImportError (tsLibCLI); ' % __title__ + \
          'importCode=%s' % str(importCode))

#--------------------------------------------------------------------------

__help__ = '''
This program validates and demonstrates the tsDoubleLinkedList module.

'''

DEBUG = False

DebugKeyValueUndefined     = False
DebugSimulatedErrorTrap = False
EnableOptionsGNU = True

theAssignedLogger = None

runTimeTitleEnabled = True
tracebackEnabled = False

#-----------------------------------------------------------------------

def test_low_level_interface(myLogger):
    '''
    '''

    #-------------------------------------------------------------------

    myList = DoubleLinkedList("a")
    myList.Add("b")
    myList.Add("c")
    myList.Add("d")
    myList.Add("e")
    firstNode = myList.GetFirst()
    lastNode = myList.GetLast()

    #-------------------------------------------------------------------

    node = firstNode
    done = False
    myLogger.debug('\n***** Five Member Set [abcde] after ' + \
          'low level next/previous access')
    while not done:
        if node.previousNode is None:
            textPrevious = None
        else:
            textPrevious = node.previousNode.userData

        textCurrent = node.userData

        if node.nextNode is None:
            textNext = None
        else:
            textNext = node.nextNode.userData

        myLogger.debug(
            '\tPrevious="%s"; userData="%s"; Next="%s"' % (
            textPrevious, textCurrent, textNext))

        if node.nextNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.nextNode

    #-------------------------------------------------------------------

    node = firstNode
    done = False
    myLogger.debug(
        '\n***** Five Member Set [abcde] after ' + \
        'low level forward access')
    while not done:
        myLogger.debug('\t"%s"' % node.userData)
        if node.nextNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.nextNode

    #-------------------------------------------------------------------

    node = lastNode
    done = False
    myLogger.debug(
        '\n***** Five Member Set [edcba] after ' + \
        'low level backward access')
    while not done:
        myLogger.debug('\t"%s"' % node.userData)
        if node.previousNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.previousNode

    #-------------------------------------------------------------------

    myList.Remove(myList.tail)
    node = myList.head
    done = False
    myLogger.debug(
        '\n***** Four Member Set [abcd] after ' + \
        'low level tail removal')
    while not done:
        myLogger.debug('\t"%s"' % node.userData)
        if node.nextNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.nextNode

    #-------------------------------------------------------------------

    myList.Remove(myList.head)
    node = myList.head
    done = False
    myLogger.debug(
        '\n***** Three Member Set [bcd] after ' + \
        'low level head removal')
    while not done:
        myLogger.debug('\t"%s"' % node.userData)
        if node.nextNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.nextNode

    #-------------------------------------------------------------------

    myList.Remove(myList.head.nextNode)
    node = myList.head
    done = False
    myLogger.debug(
        '\n***** Two Member Set (bd) after ' + \
        'low level internal removal')
    while not done:
        myLogger.debug('\t"%s"' % node.userData)
        if node.nextNode is None:
            done = True
            myLogger.debug('\n')
        else:
            node = node.nextNode

#-----------------------------------------------------------------------

def test_high_level_interface(myLogger):
    '''
    '''

    #------------------------------------------------------------------

    myList = DoubleLinkedList("a")
    myList.Add("b")
    myList.Add("c")
    myList.Add("d")
    myList.Add("e")

    myLogger.debug(
        '\n***** Five Member Set [abcde] with ' + \
        'high level iterator access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)

    index = 0
    node = myList.GetFirst()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.GetNext()

    #------------------------------------------------------------------

    myList = DoubleLinkedList("a")
    myList.Add("b")
    myList.Add("c")
    myList.Add("d")
    myList.Add("e")

    myLogger.debug(
        '\n***** Five Member Set {??abcde??] with high level ' + \
        'forward index access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)
    for index in range(0 - 2, theCount + 2):

        node = myList.GetIndex(index)
        if node is None:
            theGetUserData = '?'
        else:
            theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))

    #------------------------------------------------------------------

    myList = DoubleLinkedList("a")
    myList.Add("b")
    myList.Add("c")
    myList.Add("d")
    myList.Add("e")

    myLogger.debug(
        '\n***** Five Member Set {??edcba??] with high level ' + \
        'reverse index access')
    theCount = myList.GetCount()
    myLogger.debug('\t     theCount="%s"' % theCount)
    for index in range(theCount + 1, 0 - 3, -1):

        node = myList.GetIndex(index)
        if node is None:
            theGetUserData = '?'
        else:
            theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))

    #------------------------------------------------------------------

    myList = DoubleLinkedList()
    myList.InsertAsTail("a")
    myList.InsertAsTail("b")
    myList.InsertAsTail("c")
    myList.InsertAsTail("d")
    myList.InsertAsTail("e")

    myLogger.debug(
        '\n***** Five Member Set [abcde] with high level InsertAsTail access')
    theCount = myList.GetCount()
    myLogger.debug(
        '\ttheCount="%s"' % theCount)
    index = 0
    node = myList.GetFirst()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.GetNext()

    #------------------------------------------------------------------

    myList = DoubleLinkedList()
    myList.InsertAsHead("a")
    myList.InsertAsHead("b")
    myList.InsertAsHead("c")
    myList.InsertAsHead("d")
    myList.InsertAsHead("e")

    myLogger.debug(
        '\n***** Five Member Set [edcba] with high level ' + \
        'InsertAsHead access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)
    index = 0
    node = myList.GetFirst()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.GetNext()

    #------------------------------------------------------------------

    myList = DoubleLinkedList()
    myList.InsertAsHead("a")
    myList.InsertBefore(0, "b")
    myList.InsertBefore(0, "c")
    myList.InsertBefore(0, "d")
    myList.InsertBefore(0, "e")

    myLogger.debug(
        '\n***** Five Member Set [edcba] with high level ' + \
        'InsertBefore access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)
    index = 0
    node = myList.GetFirst()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.GetNext()

    #------------------------------------------------------------------

    myList = DoubleLinkedList()
    myList.InsertAsHead("a")
    myList.InsertAfter(0, "b")
    myList.InsertAfter(1, "c")
    myList.InsertAfter(0, "d")
    myList.InsertAfter(2, "e")

    myLogger.debug(
        '\n***** Five Member Set [adbec] with high level ' + \
        'InsertAfter access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)
    index = 0
    node = myList.GetFirst()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.GetNext()

    #------------------------------------------------------------------

    myList = DoubleLinkedList(lifoMode=False)
    myList.Push("a")
    myList.Push("b")
    myList.Push("c")
    myList.Push("d")
    myList.Push("e")

    myLogger.debug(
        '\n***** Five Member FIFO Set [abcde] with ' + \
        'high level Push and Pop access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)

    index = 0
    node = myList.Pop()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.Pop()

    #------------------------------------------------------------------

    myList = DoubleLinkedList(lifoMode=True)
    myList.Push("a")
    myList.Push("b")
    myList.Push("c")
    myList.Push("d")
    myList.Push("e")

    myLogger.debug(
        '\n***** Five Member LIFO Set [edcba] with ' + \
        'high level Push and Pop access')
    theCount = myList.GetCount()
    myLogger.debug('\ttheCount="%s"' % theCount)

    index = 0
    node = myList.Pop()
    while (not (node is None)):
        theGetUserData = node.GetUserData()
        myLogger.debug(
            '\tnode=[%d]; userData="%s"; theCount=%d' % (
            index,
            theGetUserData,
            myList.GetCount()))
        index += 1
        node = myList.Pop()

#--------------------------------------------------------------------------

if __name__ == "__main__":

    #----------------------------------------------------------------------

    def exitTest():
        '''
        Simulated Input / Output Exception to induce termination
        with an exit code and message.
        '''

        if DebugSimulatedErrorTrap:

            exceptionName = tse.INPUT_OUTPUT_EXCEPTION
            errorName = 'Oops! Invalid Name'

            myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                       name='exitTest')

            message = 'ExitTest'

            myLogger.debug('***** ExitTest %s / %s *****' % (
                exceptionName, errorName))
            raise tse.InputOutputException(errorName, message)

        else:

            return

    #----------------------------------------------------------------------

    def getRunTimeTitle():
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        # Capture Command Line Arguments.
        argv = sys.argv

        # Separate File Path from its associated File Name and Extension
        (filePath, fileNameExt) = os.path.split(argv[0])

        # Separate File Name from its associated Extension
        (fileName, fileExt) = os.path.splitext(fileNameExt)

        return (fileName)

    #----------------------------------------------------------------------

    def getRunTimeTitleVersionDate():
        '''
        Return Run Time Title, or Build Title, whichever was actually
        used in command line, stripping it of any file path.
        '''
        runTimeTitle = getRunTimeTitle()
        if runTimeTitle == __title__:

            runTimeTitleVersionDate = mainTitleVersionDate

        else:

            runTimeTitleVersionDate = '%s, v%s (build %s)' % (
                runTimeTitle, __version__, __date__)

        return (runTimeTitleVersionDate)

    #----------------------------------------------------------------------

    def prototype(*args, **kw):
        '''
        Simulated main program entry point with simulated exception
        inducing exit test.
        '''
        print('\n%s\n' % getRunTimeTitleVersionDate())

        rawArgsOptions = sys.argv[1:]
        print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        theModule = tsOperatorSettingsParser
        theClass = theModule.TsOperatorSettingsParser()
        (args, options) = theClass.parseCommandLineDispatch()

        if True or DEBUG:

            print('\n\ttsCommandLineEnv.prototype (parameter list): ' + \
                  '\n\t\targs=%s;\n\t\tkw=%s' % (str(args),
                                                 str(kw)))

            print('\n\ttsCommandLineEnv.prototype (command line argv): ' + \
                  '\n\t\targs=%s;\n\t\toptions (unsorted)=%s' % (
                      str(args),
                      str(options)))

            fmt1 = '\n\ttsCommandLineEnv.prototype (command line argv): '
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                value = '"%s"' % options[key]
                if text == '':
                    text = '{%s: %s' % (str(key), str(value))
                else:
                    text += ', %s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   start=time.time(),
                                   name='') # './myDoubleLinkedList.log')
        test_low_level_interface(myLogger)
        test_high_level_interface(myLogger)

        exitTest()

    #----------------------------------------------------------------------

    myApp = CommandLineEnv(

        buildTitle=__title__,
        buildVersion=__version__,
        buildDate=__date__,
        buildAuthors=__authors__,
        buildCopyright=__copyright__,
        buildLicense=__license__,
        buildCredits=__credits__,
        buildTitleVersionDate=mainTitleVersionDate,
        buildHeader=__header__,
        buildPurpose=__doc__,

        enableDefaultCommandLineParser=False,

##      guiMessageFilename=None,
##      guiMessageRedirect=False,
##      guiRedirects=False,
##      guiRequired=False,
##      guiTopLevelObject=None,
##      guiTopLevelObjectId=None,
##      guiTopLevelObjectName=None,
##      guiTopLevelObjectParent=None,
##      guiTopLevelObjectTitle=None,

        logs=[],

        runTimeEntryPoint=prototype)

    myApp.Wrapper()
