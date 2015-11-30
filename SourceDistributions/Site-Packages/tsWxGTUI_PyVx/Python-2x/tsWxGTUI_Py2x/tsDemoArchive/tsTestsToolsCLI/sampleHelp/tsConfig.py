#-----------------------------------------------------------
#
# tsConfig.py
#
# TeamSTARS Config Class
#
# Copyright (C) 2007 TeamSTARS, Dick Gordon and Rick Kier
# E-mail: TeamSTARS AT TeamSTARS DOT net
#
#-----------------------------------------------------------
'''
Wrapper for Config Object

See documentation for Config Object
http://www.voidspace.org.uk/python/configobj.html
'''

import configobj as co

class TsConfig(co.ConfigObj):

    def __init__(self, infile=None, options=None, **kwargs):
        co.ConfigObj.__init__(self, infile, options, **kwargs)
 
