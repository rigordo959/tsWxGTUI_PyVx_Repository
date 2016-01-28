#!/usr/bin/env python

## python test_PythonReturnTypes.py

## value=12345 <type 'int'>
##	 result=12345 <type 'int'>
##	 result=12345 <type 'int'>
##	 result=[12345] <type 'list'>

## value=(123, 456) <type 'tuple'>
##	 result=(123, 456) <type 'tuple'>
##	 result=(123, 456) <type 'tuple'>
##	 result=[(123, 456)] <type 'list'>

## value=[123, 456] <type 'list'>
##	 result=[123, 456] <type 'list'>
##	 result=[123, 456] <type 'list'>
##	 result=[[123, 456]] <type 'list'>

myInt = 12345
myTuple = (123, 456)
myList = [123, 456]

def myIntReturn(value):
    '''
    Return copy of input argument.
    '''
    return value

def myTupleReturn(value):
    '''
    Return copy of input argument, perhaps within tuple.
    '''
    return (value)

def myListReturn(value):
    '''
    Return copy of input argument as list, perhaps within tuple.
    '''
    return ([value])

for item in [myInt, myTuple, myList]:
    print('\n value=%s %s' % (str(item), type(item)))
    for function in [myIntReturn, myTupleReturn, myListReturn]:
	result = function(item)
	print('\t result=%s %s' % (str(result), type(result)))
