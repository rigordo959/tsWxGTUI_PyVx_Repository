#! /usr/bin/env python
# "Time-stamp: <04/08/2015  9:22:09 AM rsg>"
'''
tsWxStaticBoxSizer.py - Class to establish a sizer derived from
wxBoxSizer but adds a static box around the sizer.
'''
#################################################################
#
# File: tsWxStaticBoxSizer.py
#
# Purpose:
#
#    Class to establish a sizer derived from wxBoxSizer but
#    adds a static box around the sizer.
#
# Usage (example):
#
#    # Import
#    try:
#        import ts
#    except:
#        pass
#
#    from tsWxStaticBoxSizer import StaticBoxSizer
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
#    2011/12/11 rsg Use "//" instead of "/", in CalcMin, so as
#               to adjust for multiple of standard character size.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxStaticBoxSizer'
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

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py2x.tsLibGUI.tsWxBoxSizer import BoxSizer
from tsWxGTUI_Py2x.tsLibGUI.tsWxPoint import Point as wxPoint
from tsWxGTUI_Py2x.tsLibGUI.tsWxRect import Rect as wxRect
from tsWxGTUI_Py2x.tsLibGUI.tsWxSize import Size as wxSize
from tsWxGTUI_Py2x.tsLibGUI.tsWxSizerItem import SizerItem as wxSizerItem
from tsWxGTUI_Py2x.tsLibGUI.tsWxStaticBox import StaticBox

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

DEFAULT_POS = wxPoint(wx.DefaultPosition)
DEFAULT_SIZE = wxSize(wx.DefaultSize)

#---------------------------------------------------------------------------
 
class StaticBoxSizer(BoxSizer):
    '''
    Class to establish a sizer derived from wxBoxSizer but adds a static
    box around the sizer.

    The static box may be either created independently or the sizer may
    create it itself as a convenience. In any case, the sizer owns the
    wxStaticBox control and will delete it in the wxStaticBoxSizer
    destructor.

    Note that since wxWidgets 2.9.1 you are encouraged to create the
    windows which are added to wxStaticBoxSizer as children of wxStaticBox
    itself, see this class documentation for more details.

    Example of use of this class:

    void MyFrame::CreateControls()
    {
        wxPanel *panel = new wxPanel(this);
        ...
        wxStaticBoxSizer *sz = new wxStaticBoxSizer(
        wxVERTICAL, panel, "Box");

        sz->Add(new wxStaticText(
        sz->GetStaticBox(),
        wxID_ANY,
        "This window is a child of the staticbox"));
        ...
    }
    '''
    def __init__(self, box, orient=wx.HORIZONTAL):
        '''
        Constructor.

        Note: This implementation does not handle the alternate form.

        wxStaticBoxSizer::wxStaticBoxSizer( wxStaticBox *box, int orient )
            : wxBoxSizer( orient ),
              m_staticBox( box )
        {
            wxASSERT_MSG( box, wxT("wxStaticBoxSizer needs a static box") );

            // do this so that our Detach() is called if the static box
            // is destroyed before we are
            m_staticBox->SetContainingSizer(this);
        }

        wxStaticBoxSizer::wxStaticBoxSizer(int orient, wxWindow *win,
                                           const wxString& s)
                        : wxBoxSizer(orient),
                          m_staticBox(new wxStaticBox(win, wxID_ANY, s))
        {
            // same as above
            m_staticBox->SetContainingSizer(this);

        '''
        theClass = 'StaticBoxSizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        BoxSizer.__init__(self, orient)

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)

        self.logger.wxASSERT_MSG(isinstance(box, StaticBox),
                                 'wxStaticBoxSizer needs a static box')

        # TBD - Placeholders for missing instance variables
        self.ts_Position = wx.DefaultPosition
        self.ts_Size = wx.DefaultSize

        if not isinstance(box, StaticBox):
            parent = self
            box = StaticBox(
                parent,
                id=wx.ID_ANY,
                label=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                validator=wx.DefaultValidator,
                name=wx.StaticBoxNameStr)

        # Do this so that our Detach() is called if the static box is
        # destroyed before we are
        self.ts_StaticBox = box
        # TBD - What to do?
        # self.ts_StaticBox.SetContainingSizer(self)
        self.ts_ContainingSizer = box

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

    def Add(self, item, proportion=0, flag=0, border=0, userData=None):
        '''
        Appends a child to the sizer.

        wxSizer itself is an abstract class, but the parameters are
        equivalent in the derived classes that you will instantiate to
        use it so they are described here:

        Parameters:
        window  The window to be added to the sizer. Its initial size
        (either set explicitly by the user or calculated internally when
        using wxDefaultSize) is interpreted as the minimal and in many
        cases also the initial size.

        proportion      Although the meaning of this parameter is
        undefined in wxSizer, it is used in wxBoxSizer to indicate if a
        child of a sizer can change its size in the main orientation of
        the wxBoxSizer - where 0 stands for not changeable and a value
        of more than zero is interpreted relative to the value of other
        children of the same wxBoxSizer. For example, you might have a
        horizontal wxBoxSizer with three children, two of which are
        supposed to change their size with the sizer. Then the two
        stretchable windows would get a value of 1 each to make them
        grow and shrink equally with the sizers horizontal dimension.

        flag OR-combination of flags affecting sizers behaviour.
        See wxSizer flags list for details.

        border Determines the border width, if the flag parameter is
        set to include any border flag.

        userData Allows an extra object to be attached to the
        sizer item, for use in derived classes when sizing information
        is more complex than the proportion and flag will allow for.
        '''
        # Create new SizerItem with default addributes
        child = wxSizerItem()

        if isinstance(item, tuple) or \
           isinstance(item, wxSize):

            # Overload the child's wxSizerSpacer attribute
            child.ts_Size = wx.tsGetClassInstanceFromTuple(item, wxSize)
            child.ts_Kind = wx.Item_Spacer
            self.ts_Size = child.ts_Size
            self.logger.debug(
                'StaticBoxSizer.Add: Tuple=%s' % str(self.ts_Size))

        elif isinstance(item, StaticBoxSizer):
 
            # Overload the child's wxSizer attribute
            child.Sizer = item
            child.ts_Kind = wx.Item_Sizer
            self.ts_Size = None
            self.logger.debug(
                'StaticBoxSizer.Add: Sizer=%s' % str(self.ts_Size))

        else:

            # Overload the child's window attribute
            # Supports Top Level Windows (i.e., Dialogs and Frames)
            # Supports Lower Level Windows (i.e., Buttons, Check Boxes,
            # Gauges, Panels, Radio Boxes, Radio Buttons etc.).
            child.Window = item
            child.ts_Kind = wx.Item_Window
            try:
                self.ts_Size = item.ts_Size
            except AttributeError:
                self.ts_Size = DEFAULT_SIZE
            self.logger.debug(
                'StaticBoxSizer.Add: Window=%s' % str(self.ts_Size))

        # Overload the child's other attributes
        child.Proportion = proportion
        child.Flag = flag
        child.Border = border
        child.UserData = userData

        # Register the child in the wxSizerItemList
        self.ts_Children.Add(child)
 
        return (child)

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        Calculate the total minimum width and height needed by all items
        in the sizer according to this sizer layout algorithm.
        '''
        # The minimal size for the sizer should be big enough to allocate
        # its element at least its minimal size but also, and this is the
        # non-trivial part, to respect the children proportion. To satisfy
        # the latter condition we must find the greatest min-size-to-
        # proportion ratio for all elements with non-zero proportion.

        # This sizer instance only manages a single parent's client area.
        # Unlike wxWidgets, a parent's client area depends on size of
        # Top Level Window (Frame or Dialog) that depends on initial size
        # of Display Screen which was manually set by a System Operator.

        sizerClientArea = self.FindSizerClientArea()
        self.logger.debug(
            'StaticBoxSizer.CalcMin: sizerClientArea=%s' % str(
                sizerClientArea))

        self.ts_CalcMinArea = []
        self.ts_CalcMinAreaProportion = []
        self.ts_CalcMinKind = []
        self.ts_CalcMinWindow = []
        self.ts_ClientArea = []
        self.ts_ContainingWindow = None
        self.ts_MinSize = wxSize(0, 0)
        self.ts_SizeMinThis = []
        self.ts_TotalFixedSize = wxSize(0, 0)
        self.ts_TotalProportion = 0

        for i in range(0, self.ts_Children.GetCount()):
            node = self.ts_Children.GetIndex(i)

            item =  node.GetUserData()
            msg = 'StaticBoxSizer.CalcMin: item[%d]=%s' % (i, str(item))
##            print(msg)
            self.logger.debug(msg)

            if (True or item.IsShown()):

                # sizeMinThis = item.CalcMin()
                # TBD - Not sure if the following is equivalent.

                if (item.ts_Kind == wx.Item_None):

                    msg = 'Kind: %s' % 'Item_None'
                    sizeMinThis = wxSize(0, 0)
                    self.ts_CalcMinWindow += [None]

                elif (item.ts_Kind == wx.Item_Sizer):

                    msg = 'Kind: %s' % 'Item_Sizer'
                    self.ts_Sizer.Layout()
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = item.ts_Sizer.Size

                elif (item.ts_Kind == wx.Item_Spacer):

                    msg = 'Kind: %s' % 'Item_Spacer'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = item.ts_Spacer.Size

                elif (item.ts_Kind == wx.Item_Window):

                    msg = 'Kind: %s' % 'Item_Window'
                    self.ts_CalcMinWindow += [item.ts_Window]
                    parent = item.ts_Window.ts_Parent
                    clientArea = parent.ClientArea

                    if (clientArea == sizerClientArea):

                        theRect = parent.Rect
                        theClientArea = parent.ClientArea
                        print('StaticBoxSizer.CalcMin: ' + \
                              'Rect=%s; ClientArea=%s' % (
                                  str(theRect),
                                  str(theClientArea)))

                    else:

                        theRect = parent.Rect
                        theClientArea = parent.ClientArea
                        print(
                            'StaticBoxSizer.CalcMin: ' + \
                            'Rect=%s; ClientArea=%s' % (
                                str(theRect),
                                str(theClientArea)))
                        self.logger.error(
                            'StaticBoxSizer.CalcMin: ' + \
                            'Rect=%s; ClientArea=%s' % (
                                str(theRect),
                                str(theClientArea)))

                    msg = '%s; Parent.clientArea=%s' % (msg, str(clientArea))
                    sizeMinThis = wxSize(clientArea.width, clientArea.height)

                    if (self.ts_ContainingWindow is None):

                        self.ts_ContainingWindow = parent
                        self.ts_ClientArea = clientArea

                    elif (self.ts_ContainingWindow == parent):

                        pass

                    else:

                        fmt1 = 'StaticBoxSizer.CalcMin: '
                        fmt2 = 'Rejected Parent=%s' % str(parent)
                        fmt3 = 'Previous Parent=%s' % str(
                            self.ts_ContainingWindow)
                        msgError = fmt1 + fmt2 + fmt3
                        print(msgError)
                        self.logger.error(msgError)

                elif (item.ts_Kind == wx.Item_Max):

                    msg = 'Kind: %s' % 'Item_Max'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = wxSize(0, 0)

                else:

                    msg = 'Kind: %s' % 'Item_Unknown'
                    self.ts_CalcMinWindow += [None]
                    sizeMinThis = wxSize(0, 0)

                self.logger.debug(msg)

                propThis = item.GetProportion()

                self.ts_CalcMinArea += [sizeMinThis]
                self.ts_CalcMinAreaProportion += [propThis]
                self.ts_CalcMinKind += [item.ts_Kind]
                self.ts_SizeMinThis += [sizeMinThis]

                if (propThis != 0):

                    # Adjustable size item

                    self.ts_TotalProportion += propThis

                    msg = 'StaticBoxSizer.CalcMin: ' + \
                          'item[%d]=%s; totalProp= %s' % (
                              i, str(item), str(self.ts_TotalProportion))
                    self.logger.debug(msg)

                else:

                    # Fixed size item

                    self.ts_TotalFixedSize += sizeMinThis

                    msg = 'StaticBoxSizer.CalcMin: ' + \
                          'item[%d]=%s; totalFixed= %s' % (
                              i, str(item), str(self.ts_TotalFixedSize))
                    self.logger.debug(msg)

        for i in range(0, self.ts_Children.GetCount()):

            if (self.ts_Orientation == wx.HORIZONTAL):

                orientation = 'HORIZONTAL'
                self.ts_CalcMinArea[i].height = self.ts_ClientArea.height

                if (self.ts_CalcMinAreaProportion[i] == 0):

                    self.ts_CalcMinArea[
                        i].width = self.ts_SizeMinThis[i].width

                else:

                    scalableWidth = self.ts_ClientArea.width - \
                                    self.ts_TotalFixedSize.width

                    self.ts_CalcMinArea[i].width = int(0.5 + (
                        scalableWidth * (
                            float(self.ts_CalcMinAreaProportion[i]) /
                            float(self.ts_TotalProportion))))

            else:

                orientation = '  VERTICAL'
                self.ts_CalcMinArea[i].width = self.ts_ClientArea.width

                if (self.ts_CalcMinAreaProportion[i] == 0):

                    self.ts_CalcMinArea[
                        i].height = self.ts_SizeMinThis[i].height

                else:

                    scalableHeight = self.ts_ClientArea.height - \
                                     self.ts_TotalFixedSize.height

                    self.ts_CalcMinArea[i].height = int(0.5 + (
                        scalableHeight * (
                            float(self.ts_CalcMinAreaProportion[i]) /
                            float(self.ts_TotalProportion))))

                if True:

                    # Adjust to be multiple of standard character size
                    self.ts_CalcMinArea[i].width = (
                        (self.ts_CalcMinArea[i].width // \
                         wx.pixelWidthPerCharacter) * \
                        wx.pixelWidthPerCharacter)

                    self.ts_CalcMinArea[i].height = (
                        (self.ts_CalcMinArea[i].height // \
                         wx.pixelHeightPerCharacter) * \
                        wx.pixelHeightPerCharacter)

            fmt1 = '%s CalcMinArea[%d]: width=%3d; height=%3d; ' % (
                orientation,
                i,
                int(self.ts_CalcMinArea[i].width),
                int(self.ts_CalcMinArea[i].height))

            fmt2 = 'totalProportion=%3d' % int(self.ts_TotalProportion)

            self.logger.debug(fmt1 + fmt2)

        theCalcMinSize = self.GetSizeInMajorDir(self.ts_ClientArea)
        self.logger.debug('theCalcMinSize=%d' % theCalcMinSize)
        return (theCalcMinSize)

    #-----------------------------------------------------------------------

##    def CalcMinDisable(self):
##        '''
##        This method is where the sizer will do the actual calculation of its
##        childrens minimal sizes. You should not need to call this directly
##        as it is called by Layout

##        Modeled after TBD in sizer.cpp file of wxWidgets.
##        '''
##        (top_border, other_border) = self.ts_StaticBox.GetBordersForSizer()

##        ret = (BoxSizer.CalcMin())
##        ret.x += 2 * other_border

##        # ensure that we're wide enough to show the static box label
##        # (there is no need to check for the static box best size in
##        # vertical direction though)
##        boxWidth = self.GetBestSize().x # self.ts_StaticBox.GetBestSize().x
##        if ( ret.x < boxWidth ):
##            ret.x = boxWidth

##        ret.y += other_border + top_border

##        return (ret)

    #-----------------------------------------------------------------------

    def GetStaticBox(self):
        '''
        Returns the static box associated with this sizer.
        '''
        return (self.ts_StaticBox)

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        Recalculate (if necessary) the position and size of each item and
        then call item.SetDimension to do the actual positioning and sizing
        of the items within the space alloted to this sizer.
        '''
        self.ts_RecalcArea = []

        for i in range(0, self.ts_Children.GetCount()):

            if (self.ts_Orientation == wx.HORIZONTAL):

                # Horizontal Layout
                orientation = 'HORIZONTAL'
                if (i == 0):

                    self.ts_RecalcArea += [wxRect(
                        self.ts_ClientArea.x,
                        self.ts_ClientArea.y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

                else:

                    self.ts_RecalcArea += [wxRect(
                        (self.ts_RecalcArea[i - 1].x + \
                         self.ts_RecalcArea[i - 1].width),
                        self.ts_RecalcArea[i - 1].y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

            else:

                # Vertical Layout
                orientation = '  VERTICAL'

                if (i == 0):

                    self.ts_RecalcArea += [wxRect(
                        self.ts_ClientArea.x,
                        self.ts_ClientArea.y,
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

                else:

                    self.ts_RecalcArea += [wxRect(
                        self.ts_RecalcArea[i - 1].x,
                        (self.ts_RecalcArea[i - 1].y + \
                         self.ts_RecalcArea[i - 1].height),
                        self.ts_CalcMinArea[i].width,
                        self.ts_CalcMinArea[i].height)]

            msg = '%s RecalcSizes[%d]: Rect=%s; ' % (
                orientation,
                i,
                self.ts_RecalcArea[i])

            print(msg)

            self.ts_CalcMinWindow[i].ts_Rect = self.ts_RecalcArea[i]

##        self.RecalcSizes_Orig()

    #-----------------------------------------------------------------------

##    def RecalcSizesDisable(self):
##        '''
##        '''
##        (top_border, other_border) = self.ts_StaticBox.GetBordersForSizer()

####        self.ts_StaticBox.SetSize(self.ts_Position.x,
####                                  self.ts_Position.y,
####                                  self.ts_Size.x,
####                                  self.ts_Size.y )
##        self.SetSize(self.ts_Position.x,
##                     self.ts_Position.y,
##                     self.ts_Size.x,
##                     self.ts_Size.y )

##        old_size = self.ts_Size
##        self.ts_Size.x -= 2 * other_border * wx.pixelWidthPerCharacter
##        self.ts_Size.y -= (top_border + other_border) * \
##                          wx.pixelHeightPerCharacter

##        old_pos = self.ts_Position
##        if (self.ts_StaticBox.GetChildren().GetCount() > 0):

##            # if the wxStaticBox has childrens, then these windows must
##            # be placed by the wxBoxSizer::RecalcSizes() call below
##            # using coordinates relative to the top-left corner of the
##            # staticbox (but unlike wxGTK, we need
##            # to keep in count the static borders here!):
##            self.ts_Position.x = other_border
##            self.ts_Position.y = top_border

##        else:

##            # the windows contained in the staticbox have been created
##            # as siblings of the staticbox (this is the "old" way of
##            # staticbox contents creation); in this case we need to
##            # position them with coordinates relative to our common parent
##            self.ts_Position.x += other_border
##            self.ts_Position.y += top_border

##        BoxSizer.RecalcSizes()

##        self.ts_Position = old_pos
##        self.ts_Size = old_size

    #-----------------------------------------------------------------------

    def SetStaticBox(self, box):
        '''
        Set the static box associated with this sizer.
        '''
        self.ts_StaticBox = box

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions
 
    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    StaticBox = property(GetStaticBox)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
