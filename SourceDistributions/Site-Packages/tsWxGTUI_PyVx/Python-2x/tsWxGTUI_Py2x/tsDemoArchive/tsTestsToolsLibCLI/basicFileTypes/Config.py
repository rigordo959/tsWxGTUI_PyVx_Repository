#-----------------------------------------------------------
#
# File: Config.py
#
#-----------------------------------------------------------
'''
Wrapper for Config Object

See documentation for Config Object
http://www.voidspace.org.uk/python/configobj.html
'''

import configobj as co

class Config(co.ConfigObj):

    def __init__(self, infile=None, options=None, **kwargs):
        co.ConfigObj.__init__(self, infile, options, **kwargs)
 
