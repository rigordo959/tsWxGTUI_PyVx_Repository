
#--------------------------------------------------------------------------

##class Antibody():
##    '''
##    From: http://stackoverflow.com/
##    questions/5340042/display-an-objects-attributes-in-python

##    I would like to display the attributes of a give object and was
##    wondering if there was a python function for it. For example if I
##    had an object from the following class:

##    Class Antibody():

##      self.raw = toSend
##              self.pdbcode = ''
##              self.year = ''

##    Usage:
##      a = Antibody(0)
##      print a.get_fields()
##    '''
##    def get_fields(self):
##        ret = []
##        for nm in dir(self):
##           if not nm.startswith('__') and not callable(getattr(self, nm)):
##              ret.append('self.' + nm)
##        return ret

#--------------------------------------------------------------------------

##class Antibody:
##    '''
##    From: http://stackoverflow.com/
##    questions/5340042/display-an-objects-attributes-in-python

##    Usage:
##    '''
##    def __init__(self,toSend):
##        self.raw = toSend
##        self.pdbcode = ''
##        self.year = ''
##    def attributes( self ):
##        return [ 'self.'+name for name in self.__dict__ ]
