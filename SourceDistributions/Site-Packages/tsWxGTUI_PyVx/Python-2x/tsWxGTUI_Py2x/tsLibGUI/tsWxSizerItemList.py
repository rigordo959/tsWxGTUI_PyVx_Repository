#! /usr/bin/env python
# "Time-stamp: <04/09/2015  5:08:33 AM rsg>"
'''
tsWxSizerItemList.py - Class wraps a tsWxDoubleLinkedList class
(rather than a wxList-based class) and gives it a Python
sequence-like interface. Sequence operations supported are length,
first, last, next and index access and iteration.
'''
#################################################################
#
# File: tsWxSizerItemList.py
#
# Purpose:
#
#    Class wraps a tsWxDoubleLinkedList class (rather than a
#    wxList-based class) and gives it a Python sequence-like
#    interface. Sequence operations supported are length,
#    first, last, next and index.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSizerItemList import SizerItemList
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    2012/06/02 rsg Changed InsertBeginning to InsertAsHead. Changed
#                   InsertEnd to InsertAsTail.
#
#    2012/06/02 rsg Added support for optional LIFO (Last In First Out)
#                   "stack" mode or default FIFO (First In First Out)
#                   "queue" mode to DoubleLinkedList.
#
#    2012/06/02 rsg Updated test cases to replicate the lates ones
#                   used for base class tsWxDoubleLinkedList.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxSizerItemList'
__version__   = '1.1.0'
__date__      = '04/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'

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

from tsWxGTUI_Py2x.tsLibCLI import tsCxGlobals as cx

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI.tsWxDoubleLinkedList import DoubleLinkedList

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------
 
class SizerItemList(DoubleLinkedList):
    '''
    Class wraps a tsWxDoubleLinkedList class (rather than a wxList-based
    class) and gives it a Python sequence-like interface. Sequence
    operations supported are length, first, last, next and index.

    NOTE: This implementation uses the "object" based DoubleLinkedList
    Class. It eliminate the need to build an equivalent object based Class
    from scratch.
    '''
    def __init__(self, userData=None, lifoMode=False):
        '''
        '''
##        theClass = 'SizerItemList'

##        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

        DoubleLinkedList.__init__(self, userData=userData, lifoMode=lifoMode)

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

if __name__ == '__main__':

    #-----------------------------------------------------------------------

    def test_low_level_interface():
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
        print('\n***** Five Member Set [abcde] after ' + \
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

            print('\tPrevious="%s"; userData="%s"; Next="%s"' % (
                textPrevious, textCurrent, textNext))

            if node.nextNode is None:
                done = True
                print('\n')
            else:
                node = node.nextNode

        #-------------------------------------------------------------------

        node = firstNode
        done = False
        print('\n***** Five Member Set [abcde] after ' + \
              'low level forward access')
        while not done:
            print('\t"%s"' % node.userData)
            if node.nextNode is None:
                done = True
                print('\n')
            else:
                node = node.nextNode

        #-------------------------------------------------------------------

        node = lastNode
        done = False
        print('\n***** Five Member Set [edcba] after ' + \
              'low level backward access')
        while not done:
            print('\t"%s"' % node.userData)
            if node.previousNode is None:
                done = True
                print('\n')
            else:
                node = node.previousNode

        #-------------------------------------------------------------------

        myList.Remove(myList.tail)
        node = myList.head
        done = False
        print('\n***** Four Member Set [abcd] after ' + \
              'low level tail removal')
        while not done:
            print('\t"%s"' % node.userData)
            if node.nextNode is None:
                done = True
                print('\n')
            else:
                node = node.nextNode

        #-------------------------------------------------------------------

        myList.Remove(myList.head)
        node = myList.head
        done = False
        print('\n***** Three Member Set [bcd] after ' + \
              'low level head removal')
        while not done:
            print('\t"%s"' % node.userData)
            if node.nextNode is None:
                done = True
                print('\n')
            else:
                node = node.nextNode

        #-------------------------------------------------------------------

        myList.Remove(myList.head.nextNode)
        node = myList.head
        done = False
        print('\n***** Two Member Set (bd) after ' + \
              'low level internal removal')
        while not done:
            print('\t"%s"' % node.userData)
            if node.nextNode is None:
                done = True
                print('\n')
            else:
                node = node.nextNode

   #-----------------------------------------------------------------------

    def test_high_level_interface():
        '''
        '''

        #------------------------------------------------------------------

        myList = DoubleLinkedList("a")
        myList.Add("b")
        myList.Add("c")
        myList.Add("d")
        myList.Add("e")

        print('\n***** Five Member Set [abcde] with ' + \
                       'high level iterator access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)

        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member Set {??abcde??] with high level ' + \
              'forward index access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        for index in range(0 - 2, theCount + 2):

            node = myList.GetIndex(index)
            if node is None:
                theGetUserData = '?'
            else:
                theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))

        #------------------------------------------------------------------

        myList = DoubleLinkedList("a")
        myList.Add("b")
        myList.Add("c")
        myList.Add("d")
        myList.Add("e")

        print('\n***** Five Member Set {??edcba??] with high level ' + \
              'reverse index access')
        theCount = myList.GetCount()
        print('\t     theCount="%s"' % theCount)
        for index in range(theCount + 1, 0 - 3, -1):

            node = myList.GetIndex(index)
            if node is None:
                theGetUserData = '?'
            else:
                theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print(
            '\n***** Five Member Set [abcde] with high level InsertAsTail access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member Set [edcba] with high level ' + \
              'InsertAsHead access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member Set [edcba] with high level ' + \
              'InsertBefore access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member Set [adbec] with high level ' + \
              'InsertAfter access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member FIFO Set [abcde] with ' + \
                       'high level Push and Pop access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)

        index = 0
        node = myList.Pop()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
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

        print('\n***** Five Member LIFO Set [edcba] with ' + \
                       'high level Push and Pop access')
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)

        index = 0
        node = myList.Pop()
        while (not (node is None)):
            theGetUserData = node.GetUserData()
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            index += 1
            node = myList.Pop()

   #-----------------------------------------------------------------------

    print(__header__)

    test_low_level_interface()
    test_high_level_interface()
