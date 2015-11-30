#! /usr/bin/env python
#"Time-stamp: <05/06/2015  6:11:35 AM rsg>"
'''
test_tab.py - Module for demonstrating the Python indentation check.
'''
##12345678901234567890
##        first
##                second
print('Valid Indentation (with spaces): 0.')
try:
    print('Valid Indentation (with spaces): 4.')
    print('Valid Indentation (with spaces): 4.')
    print('Valid Indentation (with spaces): 4.')
except Exception, myError:
    print('Valid Indentation (with spaces) Exception: %s' % str(myError))

print('Valid Indentation (with tabs): 0.')
try:
    print('Valid Indentation (with tabs): 1.')
    print('Valid Indentation (with tabs): 1.')
    print('Valid Indentation (with tabs): 1.')
except Exception, myError:
    print('Valid Indentation (with spaces) Exception: %s' % str(myError))

##print('Indentation (with spaces): 0.')
##try:
##    print('Indentation (with spaces): 4.')
##        print('Indentation (with spaces): 8.')
##            print('Indentation (with spaces): 12.')
##except Exception, myError:
##    print('Indentation (with spaces) Exception: %s' % str(myError))

##print('Indentation (with tabs): 0.')
##try:
##    print('Indentation (with tabs): 4.')
##	print('Indentation (with tabs): 8.')
##	    print('Indentation (with tabs): 12.')
##except Exception, myError:
##    print('Indentation (with tabs) Exception: %s' % str(myError))

    
