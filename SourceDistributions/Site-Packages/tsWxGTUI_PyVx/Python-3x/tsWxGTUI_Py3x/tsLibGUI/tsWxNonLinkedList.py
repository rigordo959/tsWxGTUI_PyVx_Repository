#! /usr/bin/env python
# "Time-stamp: <03/28/2015 12:49:05 PM rsg>"
'''
tsWxNonLinkedList.py - Class to establish a representation of a
nonlinked list with forward and backward indexes.
'''
#################################################################
#
# File: tsWxNonLinkedList.py
#
# Purpose:
#
#    Class to establish a representation of a nonlinked list
#    with forward and backward indexes.
#
# Usage (example):
#
#    # Import
#
#    from tsWxNonLinkedList import NonLinkedList
#
# Requirements:
#
#    Provide a tsWxDoubleLinkedList-style functional and interface
#    capability for randomly or sequentially populating, accessing
#    and de-populating a simple, non-linked list of user defined
#    objects.
#
# Capabilities:
#
#    None
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Methods:
#
#    Add
#    GetCount
#    GetFirst
#    GetIndex
#    GetLast
#    GetNext
#    GetPrevious
#    InsertAfter
#    InsertAsHead
#    InsertAsTail
#    InsertBefore
#    Remove
#    __init__
#
# Classes:
#
#    NonLinkedList
#
# Modifications:
#
#    None
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'tsWxNonLinkedList'
__version__   = '1.0.0'
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

from tsWxGTUI_Py3x.tsLibCLI import tsCxGlobals as cx

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

class NonLinkedList(object):
    '''
    Class to establish a representation of a nonlinked list with forward
    and backward indexes.
    '''
    def __init__(self, userData=None):
        '''
        Class constructor.
        '''

        if userData is None:

            # Create empty index accessible list of nodes for
            # character-type user data.
            self.ts_TextCharacterBuffer = []

            # Register empty list of nodes.
            self.count = len(self.ts_TextCharacterBuffer)

        else:

            # Create non-empty index accessible list of nodes for
            # character-type user data.
            self.ts_TextCharacterBuffer = [userData]

            # Register first node in list of nodes.
            self.count = len(self.ts_TextCharacterBuffer)

        self.iterationCount = 0

    #-----------------------------------------------------------------------

    def Add(self, userData):
        '''
        Add a node to the list tail.
        '''
        self.InsertAsTail(userData)

    #-----------------------------------------------------------------------

    def GetCount(self):
        '''
        Returns the number of objects in a list-type object.
        '''
        return (self.count)

    #-----------------------------------------------------------------------

    def GetFirst(self):
        '''
        Returns the first object in a list-type object.
        '''
        theCount = self.GetCount()

        self.iterationCount = 0

        if theCount == 0:

            userData = None

        else:

            userData = self.ts_TextCharacterBuffer[self.iterationCount]

        return (userData)

    #-----------------------------------------------------------------------

    def GetIndex(self, index):
        '''
        Returns the index specified member of the list.
        '''
        theCount = self.GetCount()

        if not ((0 <= index) and \
                (index < theCount)):

            userData = None

        else:

            userData = self.ts_TextCharacterBuffer[index]

        return (userData)

    #-----------------------------------------------------------------------

    def GetLast(self):
        '''
        Returns the last of the objects in a list-type object.
        '''
        theCount = self.GetCount()

        if theCount == 0:

            userData = None

        else:

            self.iterationCount = theCount - 1

            userData = self.ts_TextCharacterBuffer[self.iterationCount]

        return (userData)

    #-----------------------------------------------------------------------

    def GetNext(self):
        '''
        Returns the next of the objects in a list-type object.
        '''
        theCount = self.GetCount()

        if ((self.iterationCount + 1) < theCount):

            # Iteration can proceed.
            self.iterationCount += 1
            userData = self.ts_TextCharacterBuffer[self.iterationCount]

        else:

            # Already reached end of iteration.
            userData = None

        return (userData)

    #-----------------------------------------------------------------------

    def GetPrevious(self):
        '''
        Returns the previous object in a list-type object.
        '''
        if self.iterationCount > 1:

            # Iteration can proceed.
            self.iterationCount -= 1
            userData = self.ts_TextCharacterBuffer[self.iterationCount]

        else:

            # Already reached end of iteration.
            userData = self.GetFirst()

        return (userData)

    #-----------------------------------------------------------------------

    def InsertAfter(self, afterIndex, userData):
        '''
        Insert a node to the list after the specified node index.
        '''
        self.count += 1
        self.ts_TextCharacterBuffer.insert(afterIndex + 1, userData)

    #-----------------------------------------------------------------------

    def InsertAsHead(self, userData):
        '''
        Insert a node to the list before the specified node index.
        '''
        self.count += 1
        self.ts_TextCharacterBuffer.insert(0, userData)

    #-----------------------------------------------------------------------

    def InsertAsTail(self, userData):
        '''
        Insert a node at the end of the list.
        '''
        self.count += 1
        self.ts_TextCharacterBuffer.insert(self.count + 1, userData)

    #-----------------------------------------------------------------------

    def InsertBefore(self, beforeIndex, userData):
        '''
        Insert a node to the list before the specified node index.
        '''
        self.count += 1
        self.ts_TextCharacterBuffer.insert(beforeIndex, userData)

    #-----------------------------------------------------------------------

    def Remove(self, nodeIndex):
        '''
        Remove an indexed node from the list of nodes.
        '''
        if (0 <= nodeIndex) and (nodeIndex < self.count):

            del self.ts_TextCharacterBuffer[nodeIndex]
            self.count -= 1

    #----------------------------------------------------------------------

    Next = property(GetNext)
    Previous = property(GetPrevious)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    #-----------------------------------------------------------------------

    def test_high_level_interface():
        '''
        Unit level test of functional and interface cpabilities.
        '''

        #------------------------------------------------------------------

        myList = NonLinkedList("a")
        myList.Add("b")
        myList.Add("c")
        myList.Add("d")
        myList.Add("e")

        print('\n***** Five Member Set [abcde] with ' + \
              'high level iterator access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                           myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)

        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            node = myList.GetNext()
            index += 1

        #------------------------------------------------------------------

        myList = NonLinkedList("a")
        myList.Add("b")
        myList.Add("c")
        myList.Add("d")
        myList.Add("e")

        print('\n***** Five Member Set {??abcde??] with high level ' + \
              'forward index access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                  myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        for index in range(0 - 2, theCount + 2):

            node = myList.GetIndex(index)
            if node is None:
                theGetUserData = '?'
            else:
                theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))

        #------------------------------------------------------------------

        myList = NonLinkedList("a")
        myList.Add("b")
        myList.Add("c")
        myList.Add("d")
        myList.Add("e")

        print('\n***** Five Member Set {??edcba??] with high level ' + \
              'reverse index access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                  myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        for index in range(theCount + 1, 0 - 3, -1):

            node = myList.GetIndex(index)
            if node is None:
                theGetUserData = '?'
            else:
                theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))

        #------------------------------------------------------------------

        myList = NonLinkedList()
        myList.InsertAsTail("a")
        myList.InsertAsTail("b")
        myList.InsertAsTail("c")
        myList.InsertAsTail("d")
        myList.InsertAsTail("e")

        print(
            '\n***** Five Member Set [abcde] with high level ' + \
            'InsertAsTail access:' + \
            '\n\t\tTextCharacterBuffer=%s' % str(
                myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            index += 1
            node = myList.GetNext()

        #------------------------------------------------------------------

        myList = NonLinkedList()
        myList.InsertAsHead("a")
        myList.InsertAsHead("b")
        myList.InsertAsHead("c")
        myList.InsertAsHead("d")
        myList.InsertAsHead("e")

        print('\n***** Five Member Set [edcba] with high level ' + \
              'InsertAsHead access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                  myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            index += 1
            node = myList.GetNext()

        #------------------------------------------------------------------

        myList = NonLinkedList()
        myList.InsertAsHead("a")
        myList.InsertBefore(0, "b")
        myList.InsertBefore(0, "c")
        myList.InsertBefore(0, "d")
        myList.InsertBefore(0, "e")

        print('\n***** Five Member Set [edcba] with high level ' + \
              'InsertBefore access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                  myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            index += 1
            node = myList.GetNext()

        #------------------------------------------------------------------

        myList = NonLinkedList()
        myList.InsertAsHead("a")
        myList.InsertAfter(0, "b")
        myList.InsertAfter(1, "c")
        myList.InsertAfter(0, "d")
        myList.InsertAfter(2, "e")

        print('\n***** Five Member Set [adbec] with high level ' + \
              'InsertAfter access:' + \
              '\n\t\tTextCharacterBuffer=%s' % str(
                  myList.ts_TextCharacterBuffer))
        theCount = myList.GetCount()
        print('\ttheCount="%s"' % theCount)
        index = 0
        node = myList.GetFirst()
        while (not (node is None)):
            theGetUserData = node
            print('\tnode=[%d]; userData="%s"; theCount=%d' % (
                index,
                theGetUserData,
                myList.GetCount()))
            index += 1
            node = myList.GetNext()

   #-----------------------------------------------------------------------

    print(__header__)

    test_high_level_interface()

