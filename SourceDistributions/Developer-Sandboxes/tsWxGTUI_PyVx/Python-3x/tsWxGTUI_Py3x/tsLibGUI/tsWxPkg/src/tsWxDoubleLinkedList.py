#! /usr/bin/env python
# "Time-stamp: <10/25/2013  7:23:15 AM rsg>"
'''
tsWxDoubleLinkedList.py - Class to establish a representation
of a linked list with forward and backward pointers.
'''
#################################################################
#
# File: tsWxDoubleLinkedList.py
#
# Purpose:
#
#    Class to establish a representation of a linked list with
#    forward and backward pointers.
#
# Usage (example):
#
#    # Import
#
#    from tsWxDoubleLinkedList import DoubleLinkedList
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    Provide a functional and interface capability for randomly
#    or sequentially populating, accessing and de-populating a
#    double-linked list of user defined objects.
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
#    2010/11/12 rsg Substituted node objects for integers in
#                   next/previous and head/tail links.
#
#    2011/09/11 rsg Added the GetUserData and SetUserData methods
#                   to the DoubleLinkedListNode Class in order to
#                   support higher level application access.
#
#    2011/09/11 rsg Added iterationCount, currentNode, previousNode,
#                   and nextNode attributes to DoubleLinkedList
#                   Class to support higher level application access.
#
#    2011/09/11 rsg Renamed methods GetNext to getNext and GetPrevious
#                   to getPrevious in DoubleLinkedList Class inorder to
#                   distinguish old lower level application access
#                   from new higher level ones.
#
#    2011/09/11 rsg Added GetCount, GetFirst, GetIndex, GetLast,
#                   GetNext methods to DoubleLinkedList Class inorder
#                   to support higher level application access.
#
#    2011/09/11 rsg Modified and expanded built-in, stand-alone,
#                   (if __name__ == '__main__ test cases to support
#                   lower level and higher level application access.
#
#    2011/09/12 rsg Added Insert methods (with after, before, beginning
#                   and end variants) to DoubleLinkedList Class inorder
#                   to support additional higher level application access.
#
#    2012/06/02 rsg Changed InsertBeginning to InsertAsHead. Changed
#                   InsertEnd to InsertAsTail.
#
#    2012/06/02 rsg Added support for optional LIFO (Last In First Out)
#                   "stack" mode or default FIFO (First In First Out)
#                   "queue" mode to DoubleLinkedList.
#
#    2012/10/07 rsg Added statement of requirements.
#
#    2012/11/24 rsg Modified DoubleLinkedListNode class.
#                   Added "Node" suffix to next and previous to
#                   facilitate porting from 2.x to 3.x..
#
# ToDo:
#
#    2011/09/12 rsg Expand the set of built-in, stand-alone tests
#                   to become a full unit-test suite. Currently,
#                   the tests only exercise a subset the possible
#                   usage variations. The expanded suite ought to
#                   me moved into to a separate test module.
#
#################################################################

__title__     = 'tsWxDoubleLinkedList'
__version__   = '1.4.0'
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

##import tsWxGlobals as wx # Invalid import because of circular dependency.
import tsCxGlobals as cx

#---------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

#---------------------------------------------------------------------------

class DoubleLinkedListNode(object):
    '''
    Class to establish a representation of a linked list node with forward
    and backward pointers.
    '''
    def __init__(self, userData=None):
        '''
        '''
##        theClass = 'DoubleLinkedListNode'

##        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

        self.userData = userData
        self.previousNode = None
        self.nextNode = None

##        print('\tDoubleLinkedListNode: userData=%s; previous=%s; next=%s' % (
##            self.userData, self.previousNode, self.nextNode))

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def GetUserData(self):
        '''
        Returns the user data associated with this node.
        '''
        if self.userData is None:

            # Oops, no userData.
            userData = None

        else:

            # Already reached end of iteration.
            userData = self.userData

        return (userData)

    #-----------------------------------------------------------------------

    def SetUserData(self, userData=None):
        '''
        Sets the user data associated with this node.
        '''
        try:

            self.userData = userData
            status = True

        except AttributeError:

            status = False

        return (status)

#---------------------------------------------------------------------------

class DoubleLinkedList(object):
    '''
    Class to establish a representation of a linked list with forward
    and backward pointers.
    '''
    def __init__(self, userData=None, lifoMode=False):
        '''
        '''
##        theClass = 'DoubleLinkedList'

##        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)

        self.lifoMode = lifoMode # Set True for Stack or False for Queue

        if userData is None:

            # Create empty index accessible list of nodes.
            self.indexedNodeList = []

            # Create empty doubly linked list of nodes.
            self.count = 0
            self.head = None
            self.tail = None

        else:

            # Create first node.
            newNode = DoubleLinkedListNode(userData)

            # Create first node in index accessible list of nodes.
            self.indexedNodeList = [newNode]

            # Create first node in doubly linked list of nodes.
            self.count = 1
            self.head = newNode
            self.tail = self.head

##        print('DoubleLinkedList: count=%d; head=%s; tail=%s\n\n' % (
##            self.count, self.head, self.tail, self))

##        print('DoubleLinkedList: indexedNodeList=%s\n\n' % \
##            self.indexedNodeList)

        # Initialize iterative access controls
        self.iterationCount = 0
        self.currentNode = None
        self.previousNode = self.currentNode
        self.nextNode = self.currentNode

        self.lastHead = self.head
        self.lastTail = self.tail

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        del self

    #-----------------------------------------------------------------------

    def Add(self, userData):
        '''
        Add a node to the list tail and appropriately adjust the forward
        and backward links.
        '''
        self.InsertAsTail(userData)

##        print('DoubleLinkedList.Add: count=%d; head=%s; tail=%s\n\n' % (
##            self.count, self.head, self.tail))

    #-----------------------------------------------------------------------

    def FindIndexByNode(self, node):
        '''
        Return the index associated with the specified node. Return None
        if node not found.
        '''
        for index in range(0, self.GetCount()):
            if (self.indexedNodeList[index] == node):
                return (index)

        return (None)

    #-----------------------------------------------------------------------

    def GetCount(self):
        '''
        Returns the number of children objects managed by the sizer in a
        list-type object.

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        return (self.count)

    #-----------------------------------------------------------------------

    def GetFirst(self):
        '''
        Returns the first of the children objects managed by the sizer
        in a list-type object.

        Modeled after wxSizerItemList::compatibility_iterator in
        sizer.cpp file of wxWidgets.
        '''
        theCount = self.GetCount()

        if theCount == 0:

            self.iterationCount = 0

            self.head = None
            self.tail = self.head
            self.currentNode = self.head
            self.previousNode = self.head
            self.nextNode = self.head

        else:

            self.iterationCount = 1

            self.currentNode = self.head
            self.previousNode = self.currentNode.previousNode
            self.nextNode = self.currentNode.nextNode

        return (self.head)

    #-----------------------------------------------------------------------

    def GetIndex(self, index):
        '''
        Returns the index specified member of the list.
        '''
        theCount = self.GetCount()

        if not ((0 <= index) and \
                (index < theCount)):

            node = None

        else:

            node = self.indexedNodeList[index]

        return (node)

    #-----------------------------------------------------------------------

    def GetLast(self):
        '''
        Returns the last of the children objects managed by the sizer
        in a list-type object.
        sizer.cpp file of wxWidgets.
        '''
        theCount = self.GetCount()

        if theCount == 0:

            self.iterationCount = 0

            self.head = None
            self.tail = self.head
            self.currentNode = self.head
            self.previousNode = self.head
            self.nextNode = self.head

        else:

            self.iterationCount = theCount

            self.currentNode = self.tail
            self.previousNode = self.currentNode.previousNode
            self.nextNode = self.currentNode.nextNode

        return (self.tail)

    #-----------------------------------------------------------------------

    def getNext(self, node):
        '''
        '''
        if node.tail is None:
            return (None)
        else:
            return (node.tail.userData)

    #-----------------------------------------------------------------------

    def GetNext(self):
        '''
        Returns the next of the children objects managed by the sizer
        in a list-type object.

        Modeled after wxSizerItemList::compatibility_iterator in
        sizer.cpp file of wxWidgets.
        '''
        theCount = self.GetCount()
        if theCount == 0:

            # Oops, nothing to iterate.
            return (None)

        elif theCount == 1:

            # Oops, someone forgot to begin iterations with GetFirst.
            return(self.GetFirst())

        elif self.iterationCount < theCount:

            # Iteration can proceed.
            self.iterationCount += 1

            self.previousNode = self.currentNode
            self.currentNode = self.previousNode.nextNode
            self.nextNode = self.currentNode.nextNode

            return (self.currentNode)

        else:

            # Already reached end of iteration.
            return (None)

    #-----------------------------------------------------------------------

    def getPrevious(self, node):
        '''
        '''
        if node.head is None:
            return (None)
        else:
            return (node.head.userData)

    #-----------------------------------------------------------------------

    def InsertAfter(self, afterIndex, userData):
        '''
        Insert a node to the list after the specified nodetail and
        appropriately adjust the forward and backward links.

        function insertAfter(List list, Node node, Node newNode)
             newNode.prev := node
             newNode.nextNode := node.next
             if node.next == null
                 list.lastNode := newNode
             else
                 node.next.prev := newNode
             node.next := newNode
        '''
        afterNode = self.indexedNodeList[afterIndex]

        newNode = DoubleLinkedListNode(userData)
        self.indexedNodeList.insert(afterIndex + 1, newNode)

        self.count += 1

        if (self.count == 1):

            self.head = newNode
            self.tail = self.head

        else:

            newNode.previousNode = afterNode
            newNode.nextNode = afterNode.nextNode
            if (newNode.nextNode is None):
                self.tail = newNode

            afterNode.nextNode = newNode

##        print('DoubleLinkedList.InsertAfter: count=%d; head=%s; ' + \
##              'tail=%s\n\n' % (self.count, self.head, self.tail))

    #-----------------------------------------------------------------------

    def InsertAsHead(self, userData):
        '''
        Insert a node to the list before the specified nodetail and
        appropriately adjust the forward and backward links.

        function insertBeginning(List list, Node newNode)
             if list.firstNode == null
                 list.firstNode := newNode
                 list.lastNode  := newNode
                 newNode.prev := null
                 newNode.nextNode := null
             else
                 insertBefore(list, list.firstNode, newNode)
        '''
        newNode = DoubleLinkedListNode(userData)
        self.indexedNodeList.insert(0, newNode)

        self.count += 1

        if (self.count == 1):

            self.head = newNode
            self.tail = self.head

        else:

            firstNode = self.head
            firstNode.previousNode = newNode
            newNode.previousNode = None # Previously set during instantiation
            newNode.nextNode = firstNode
            self.head = newNode

##        print('DoubleLinkedList.Add: count=%d; head=%s; tail=%s\n\n' % \
##              (self.count, self.head, self.tail))

    #-----------------------------------------------------------------------

    def InsertAsTail(self, userData):
        '''
        Insert a node at the end of the list and appropriately adjust
        the forward and backward links.

        function insertEnd(List list, Node newNode)
             if list.lastNode == null
                 insertBeginning(list, newNode)
             else
                 insertAfter(list, list.lastNode, newNode)
        '''
        newNode = DoubleLinkedListNode(userData)
        self.indexedNodeList.insert(self.count + 1, newNode)

        self.count += 1

        if (self.count == 1):

            self.head = newNode
            self.tail = self.head

        else:

            lastNode = self.tail
            lastNode.nextNode = newNode
            newNode.previousNode = lastNode
            newNode.nextNode = None # Previously set during instantiation
            self.tail = newNode

##        print(
##            'DoubleLinkedList.InsertAsTail: count=%d; head=%s; tail=%s\n\n' % (
##                self.count, self.head, self.tail))

    #-----------------------------------------------------------------------

    def InsertBefore(self, beforeIndex, userData):
        '''
        Insert a node to the list before the specified nodetail and
        appropriately adjust the forward and backward links.

        function insertBefore(List list, Node node, Node newNode)
             newNode.prev := node.prev
             newNode.nextNode := node
             if node.prev == null
                 list.firstNode := newNode
             else
                 node.prev.next := newNode
             node.prev    := newNode
        '''
        beforeNode = self.indexedNodeList[beforeIndex]

        newNode = DoubleLinkedListNode(userData)
        self.indexedNodeList.insert(beforeIndex, newNode)

        self.count += 1

        if (self.count == 1):

            self.head = newNode
            self.tail = self.head

        else:

            newNode.previousNode = beforeNode.previousNode
            if (newNode.previousNode is None):
                self.head = newNode
 
            newNode.nextNode = beforeNode
            beforeNode.previousNode = newNode

##        print('DoubleLinkedList.InsertBefore: count=%d; head=%s; ' + \
##              'tail=%s\n\n' % (
##            self.count, self.head, self.tail))

    #-----------------------------------------------------------------------

    def IsFIFO(self):
        '''
        Returns True if FIFO (not Lifo) mode.
        '''
        return (not self.lifoMode)

    #-----------------------------------------------------------------------

    def IsLIFO(self):
        '''
        Returns True if LIFO mode.
        '''
        return (self.lifoMode)

    #-----------------------------------------------------------------------

    def Pop(self):
        '''
        Remove and return node from position appropriate for FIFO (stack)
        or LIFO (queue).
        '''
        node = self.GetFirst()
        self.Remove(node)
        return (node)

    #-----------------------------------------------------------------------

    def Push(self, userData):
        '''
        Insert node in position appropriate for FIFO (stack) or LIFO (queue).
        '''
        if self.lifoMode:

            # Appends node to head of stack if LIFO mode so that
            # it will become the first off.
            self.InsertAsHead(userData)

        else:

            # Appends node to tail of queue, if FIFO mode so that
            # it will become the last off.
            self.InsertAsTail(userData)

    #-----------------------------------------------------------------------

    def Remove(self, node):
        '''
        Remove a node from the list and appropriately adjust the forward
        and backward links.

        function remove(List list, Node node)
           if node.prev == null
               list.firstNode := node.next
           else
               node.prev.next := node.next
           if node.next == null
               list.lastNode := node.prev
           else
               node.next.prev := node.prev
           destroy node
        '''
        self.lastHead = self.head
        self.lastTail = self.tail

        if (self.count == 0):

            # Cannot have anything to remove
            pass

        elif (self.count == 1):

            if (self.lastHead == node):

                self.count = 0
                self.head = None
                self.tail = None
                del node

            else:

                # Nothing that can be removed
                pass

        else:

            if (self.lastHead == node):

                self.count -= 1
                nextNode = node.nextNode
                nextNode.previousNode = node.previousNode
                self.head = nextNode
                del node

            elif (self.lastTail == node):

                self.count -= 1
                previousNode = node.previousNode
                previousNode.nextNode = node.nextNode
                self.tail = previousNode
                del node

            else:

                self.count -= 1
                previousNode = node.previousNode
                previousNode.nextNode = node.nextNode
                nextNode = node.nextNode
                nextNode.previousNode = previousNode
                del node

    #-----------------------------------------------------------------------

    Next = property(getNext)
    Previous = property(getPrevious)

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
