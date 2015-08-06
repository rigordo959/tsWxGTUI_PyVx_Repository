#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:33:54 AM rsg>"
'''
tsWxFlexGridSizer.py - Class to emulate the wxPython API for non-graphical,
curses-based platforms.
'''
#################################################################
#
# File: tsWxFlexGridSizer.py
#
# Purpose:
#
#    Class to emulate the wxPython API for non-graphical,
#    curses-based platforms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxFlexGridSizer import FlexGridSizer
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.)
#
#################################################################

__title__     = 'tsWxFlexGridSizer'
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

import tsWxGlobals as wx
from tsWxGridSizer import GridSizer
from tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------
 
class FlexGridSizer(GridSizer):
    '''
    A flex grid sizer is a sizer which lays out its children in a
    two-dimensional table with all table cells in one row having the same
    height and all cells in one column having the same width, but all rows
    or all columns are not necessarily the same height or width as in the
    wx.GridSizer.

    wx.FlexGridSizer can also size items equally in one direction but
    unequally ("flexibly") in the other. If the sizer is only flexible in
    one direction (this can be changed using SetFlexibleDirection), it needs
    to be decided how the sizer should grow in the other ("non flexible")
    direction in order to fill the available space. The SetNonFlexibleGrowMode
    method serves this purpose.
    '''
    def __init__(self, rows=1, cols=0, vgap=0, hgap=0):
        '''
        '''
        theClass = 'FlexGridSizer'

        wx.RegisterFirstCallerClassName(self, theClass)

        GridSizer.__init__(self, rows, cols, vgap, hgap)

        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, id)

        self.ts_ColWidths = cols
        self.ts_FlexibleDirection = wx.BOTH
        self.ts_GrowMode = wx.FLEX_GROWMODE_SPECIFIED
        self.ts_NonFlexibleGrowMode = rows
        self.ts_RowHeights = vgap

        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    // helper of AdjustForGrowables() which is called for rows/columns separately
##    //
##    // parameters:
##    //      delta: the extra space, we do nothing unless it's positive
##    //      growable: indices or growable rows/cols in sizes array
##    //      sizes: the height/widths of rows/cols to adjust
##    //      proportions: proportions of the growable rows/cols or NULL if they all
##    //                   should be assumed to have proportion of 1
##    static void
##    DoAdjustForGrowables(int delta,
##                         const wxArrayInt& growable,
##                         wxArrayInt& sizes,
##                         const wxArrayInt *proportions)
##    {
##        if ( delta <= 0 )
##            return;

##        // total sum of proportions of all non-hidden rows
##        int sum_proportions = 0;

##        // number of currently shown growable rows
##        int num = 0;

##        const int max_idx = sizes.size();

##        const size_t count = growable.size();
##        size_t idx;
##        for ( idx = 0; idx < count; idx++ )
##        {
##            // Since the number of rows/columns can change as items are
##            // inserted/deleted, we need to verify at runtime that the
##            // requested growable rows/columns are still valid.
##            if ( growable[idx] >= max_idx )
##                continue;

##            // If all items in a row/column are hidden, that row/column will
##            // have a dimension of -1.  This causes the row/column to be
##            // hidden completely.
##            if ( sizes[growable[idx]] == -1 )
##                continue;

##            if ( proportions )
##                sum_proportions += (*proportions)[idx];

##            num++;
##        }

##        if ( !num )
##            return;

##        // the remaining extra free space, adjusted during each iteration
##        for ( idx = 0; idx < count; idx++ )
##        {
##            if ( growable[idx] >= max_idx )
##                continue;

##            if ( sizes[ growable[idx] ] == -1 )
##                continue;

##            int cur_delta;
##            if ( sum_proportions == 0 )
##            {
##                // no growable rows -- divide extra space evenly among all
##                cur_delta = delta/num;
##                num--;
##            }
##            else // allocate extra space proportionally
##            {
##                const int cur_prop = (*proportions)[idx];
##                cur_delta = (delta*cur_prop)/sum_proportions;
##                sum_proportions -= cur_prop;
##            }

##            sizes[growable[idx]] += cur_delta;
##            delta -= cur_delta;
##        }
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::AdjustForGrowables(const wxSize& sz)
##    {
##    #if wxDEBUG_LEVEL
##        // by the time this function is called, the sizer should be already fully
##        // initialized and hence the number of its columns and rows is known and we
##        // can check that all indices in m_growableCols/Rows are valid (see also
##        // comments in AddGrowableCol/Row())
##        if ( !m_rows || !m_cols )
##        {
##            if ( !m_rows )
##            {
##                int nrows = CalcRows();

##                for ( size_t n = 0; n < m_growableRows.size(); n++ )
##                {
##                    wxASSERT_MSG( m_growableRows[n] < nrows,
##                                  "invalid growable row index" );
##                }
##            }

##            if ( !m_cols )
##            {
##                int ncols = CalcCols();

##                for ( size_t n = 0; n < m_growableCols.size(); n++ )
##                {
##                    wxASSERT_MSG( m_growableCols[n] < ncols,
##                                  "invalid growable column index" );
##                }
##            }
##        }
##    #endif // wxDEBUG_LEVEL


##        if ( (m_flexDirection & wxHORIZONTAL) || (m_growMode != wx.FLEX_GROWMODE_NONE) )
##        {
##            DoAdjustForGrowables
##            (
##                sz.x - m_calculatedMinSize.x,
##                m_growableCols,
##                m_colWidths,
##                m_growMode == wx.FLEX_GROWMODE_SPECIFIED ? &m_growableColsProportions
##                                                        : NULL
##            );

##            // This gives nested objects that benefit from knowing one size
##            // component in advance the chance to use that.
##            bool didAdjustMinSize = false;

##            // Iterate over all items and inform about column width
##            const int ncols = GetEffectiveColsCount();
##            int col = 0;
##            for ( wxSizerItemList::iterator i = m_children.begin();
##                  i != m_children.end();
##                  ++i )
##            {
##                didAdjustMinSize |= (*i)->InformFirstDirection(wxHORIZONTAL, m_colWidths[col], sz.y - m_calculatedMinSize.y);
##                if ( ++col == ncols )
##                    col = 0;
##            }

##            // Only redo if info was actually used
##            if( didAdjustMinSize )
##            {
##                DoAdjustForGrowables
##                (
##                    sz.x - m_calculatedMinSize.x,
##                    m_growableCols,
##                    m_colWidths,
##                    m_growMode == wx.FLEX_GROWMODE_SPECIFIED ? &m_growableColsProportions
##                                                            : NULL
##                );
##            }
##        }

##        if ( (m_flexDirection & wxVERTICAL) || (m_growMode != wx.FLEX_GROWMODE_NONE) )
##        {
##            // pass NULL instead of proportions if the grow mode is ALL as we
##            // should treat all rows as having proportion of 1 then
##            DoAdjustForGrowables
##            (
##                sz.y - m_calculatedMinSize.y,
##                m_growableRows,
##                m_rowHeights,
##                m_growMode == wx.FLEX_GROWMODE_SPECIFIED ? &m_growableRowsProportions
##                                                        : NULL
##            );
##        }
##    }

    #-----------------------------------------------------------------------

##    bool wxFlexGridSizer::IsRowGrowable( size_t idx )
##    {
##        return m_growableRows.Index( idx ) != wxNOT_FOUND;
##    }

    #-----------------------------------------------------------------------

##    bool wxFlexGridSizer::IsColGrowable( size_t idx )
##    {
##        return m_growableCols.Index( idx ) != wxNOT_FOUND;
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::AddGrowableRow( size_t idx, int proportion )
##    {
##        wxASSERT_MSG( !IsRowGrowable( idx ),
##                      "AddGrowableRow() called for growable row" );

##        // notice that we intentionally don't check the index validity here in (the
##        // common) case when the number of rows was not specified in the ctor -- in
##        // this case it will be computed only later, when all items are added to
##        // the sizer, and the check will be done in AdjustForGrowables()
##        wxCHECK_RET( !m_rows || idx < (size_t)m_rows, "invalid row index" );

##        m_growableRows.Add( idx );
##        m_growableRowsProportions.Add( proportion );
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::AddGrowableCol( size_t idx, int proportion )
##    {
##        wxASSERT_MSG( !IsColGrowable( idx ),
##                      "AddGrowableCol() called for growable column" );

##        // see comment in AddGrowableRow(): although it's less common to omit the
##        // specification of the number of columns, it still can also happen
##        wxCHECK_RET( !m_cols || idx < (size_t)m_cols, "invalid column index" );

##        m_growableCols.Add( idx );
##        m_growableColsProportions.Add( proportion );
##    }

    #-----------------------------------------------------------------------

##    // helper function for RemoveGrowableCol/Row()
##    static void
##    DoRemoveFromArrays(size_t idx, wxArrayInt& items, wxArrayInt& proportions)
##    {
##        const size_t count = items.size();
##        for ( size_t n = 0; n < count; n++ )
##        {
##            if ( (size_t)items[n] == idx )
##            {
##                items.RemoveAt(n);
##                proportions.RemoveAt(n);
##                return;
##            }
##        }

##        wxFAIL_MSG( wxT("column/row is already not growable") );
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::RemoveGrowableCol( size_t idx )
##    {
##        DoRemoveFromArrays(idx, m_growableCols, m_growableColsProportions);
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::RemoveGrowableRow( size_t idx )
##    {
##        DoRemoveFromArrays(idx, m_growableRows, m_growableRowsProportions);
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::AdjustForFlexDirection()
##    {
##        // the logic in CalcMin works when we resize flexibly in both directions
##        // but maybe this is not the case
##        if ( m_flexDirection != wxBOTH )
##        {
##            // select the array corresponding to the direction in which we do *not*
##            // resize flexibly
##            wxArrayInt& array = m_flexDirection == wxVERTICAL ? m_colWidths
##                                                              : m_rowHeights;

##            const size_t count = array.GetCount();

##            // find the largest value in this array
##            size_t n;
##            int largest = 0;

##            for ( n = 0; n < count; ++n )
##            {
##                if ( array[n] > largest )
##                    largest = array[n];
##            }

##            // and now fill it with the largest value
##            for ( n = 0; n < count; ++n )
##            {
##                // don't touch hidden rows
##                if ( array[n] != -1 )
##                    array[n] = largest;
##            }
##        }
##    }

    #-----------------------------------------------------------------------

    def AddGrowableCol(self, idx, proportion):
        '''
        Specifies that column idx (starting from zero) should be grown if
        there is extra space available to the sizer.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def AddGrowableRow(self, idx, proportion):
        '''
        Specifies that row idx (starting from zero) should be grown if there
        is extra space available to the sizer.
        '''
        pass

    #-----------------------------------------------------------------------

    def CalcMin(self):
        '''
        This method is where the sizer will do the actual calculation of its
        childrens minimal sizes. You should not need to call this directly
        as it is called by Layout

        Modeled after TBD in sizer.cpp file of wxWidgets.
        '''
        width = 0
        height = 0
        for item in self.GetChildren():
            # calculate the total minimum width and height needed
            # by all items in the sizer according to this sizer's
            # layout algorithm.
            minSize = item.MinSize
            width += minSize.width
            height += minSize.height

        size = wxSize(width, height)
        self.logger.debug('CalcMin: size=%s' % size)

        return (size)

    #-----------------------------------------------------------------------

##    wxSize wxFlexGridSizer::CalcMin()
##    {
##        int nrows,
##            ncols;

##        // Number of rows/columns can change as items are added or removed.
##        if ( !CalcRowsCols(nrows, ncols) )
##            return wxSize();


##        // We have to recalculate the sizes in case the item minimum size has
##        // changed since the previous layout, or the item has been hidden using
##        // wxSizer::Show(). If all the items in a row/column are hidden, the final
##        // dimension of the row/column will be -1, indicating that the column
##        // itself is hidden.
##        m_rowHeights.assign(nrows, -1);
##        m_colWidths.assign(ncols, -1);

##        for ( wxSizerItemList::iterator i = m_children.begin();
##              i != m_children.end();
##              ++i)
##        {
##            wxSizerItem * const item = *i;
##            if ( item->IsShown() )
##            {
##                item->CalcMin();
##            }
##        }

##        // The stage of looking for max values in each row/column has been
##        // made a separate function, since it's reused in AdjustForGrowables.
##        FindWidthsAndHeights(nrows,ncols);

##        return m_calculatedMinSize;
##    }

    #-----------------------------------------------------------------------

##    void wxFlexGridSizer::FindWidthsAndHeights(int nrows, int ncols)
##    {
##        // We have to recalculate the sizes in case the item minimum size has
##        // changed since the previous layout, or the item has been hidden using
##        // wxSizer::Show(). If all the items in a row/column are hidden, the final
##        // dimension of the row/column will be -1, indicating that the column
##        // itself is hidden.
##        m_rowHeights.assign(nrows, -1);
##        m_colWidths.assign(ncols, -1);

##        // n is the index of the item in left-to-right top-to-bottom order
##        size_t n = 0;
##        for ( wxSizerItemList::iterator i = m_children.begin();
##              i != m_children.end();
##              ++i, ++n )
##        {
##            wxSizerItem * const item = *i;
##            if ( item->IsShown() )
##            {
##                // NOTE: Not doing the calculation here, this is just
##                // for finding max values.
##                const wxSize sz(item->GetMinSizeWithBorder());

##                const int row = n / ncols;
##                const int col = n % ncols;

##                if ( sz.y > m_rowHeights[row] )
##                    m_rowHeights[row] = sz.y;
##                if ( sz.x > m_colWidths[col] )
##                    m_colWidths[col] = sz.x;
##            }
##        }

##        AdjustForFlexDirection();

##        m_calculatedMinSize = wxSize(SumArraySizes(m_colWidths, m_hgap),
##                                     SumArraySizes(m_rowHeights, m_vgap));
##    }

    #-----------------------------------------------------------------------
 
    def GetColWidths(self):
        '''
        Returns a list of integers representing the widths of each of the
        columns in the sizer.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def GetFlexibleDirection(self):
        '''
        Returns a value that specifies whether the sizer flexibly resizes
        its columns, rows, or both (default).
        '''
        pass

    #-----------------------------------------------------------------------
 
    def GetNonFlexibleGrowMode(self):
        '''
        Returns the value that specifies how the sizer grows in the
        non-flexible direction if there is one.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def GetRowHeights(self):
        '''
        Returns a list of integers representing the heights of each of the
        rows in the sizer.
        '''
        pass

    #-----------------------------------------------------------------------

    def RecalcSizes(self):
        '''
        '''
        pass
##    {
##        int nrows, ncols;
##        if ( !CalcRowsCols(nrows, ncols) )
##            return;

##        const wxPoint pt(GetPosition());
##        const wxSize sz(GetSize());

##        AdjustForGrowables(sz);

##        wxSizerItemList::const_iterator i = m_children.begin();
##        const wxSizerItemList::const_iterator end = m_children.end();

##        int y = 0;
##        for ( int r = 0; r < nrows; r++ )
##        {
##            if ( m_rowHeights[r] == -1 )
##            {
##                // this row is entirely hidden, skip it
##                for ( int c = 0; c < ncols; c++ )
##                {
##                    if ( i == end )
##                        return;

##                    ++i;
##                }

##                continue;
##            }

##            const int hrow = m_rowHeights[r];
##            int h = sz.y - y; // max remaining height, don't overflow it
##            if ( hrow < h )
##                h = hrow;

##            int x = 0;
##            for ( int c = 0; c < ncols && i != end; c++, ++i )
##            {
##                const int wcol = m_colWidths[c];

##                if ( wcol == -1 )
##                    continue;

##                int w = sz.x - x; // max possible value, ensure we don't overflow
##                if ( wcol < w )
##                    w = wcol;

##                SetItemBounds(*i, pt.x + x, pt.y + y, w, h);

##                x += wcol + m_hgap;
##            }

##            if ( i == end )
##                return;

##            y += hrow + m_vgap;
##        }
##    }

    #-----------------------------------------------------------------------

    def RemoveGrowableCol(self, idx):
        '''
        Specifies that column idx is no longer growable.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def RemoveGrowableRow(self, idx):
        '''
        Specifies that row idx is no longer growable.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def SetFlexibleDirection(self, direction):
        '''
        Specifies whether the sizer should flexibly resize its columns,
        rows, or both.
        '''
        pass

    #-----------------------------------------------------------------------
 
    def SetNonFlexibleGrowMode(self, mode):
        '''
        Specifies how the sizer should grow in the non-flexible direction
        if there is one (so SetFlexibleDirection must have been called
        previously)
        '''
        pass

    #-----------------------------------------------------------------------
 
    def SumArraySizes(self, mode):
        '''
        Specifies how the sizer should grow in the non-flexible direction
        if there is one (so SetFlexibleDirection must have been called
        previously)
        '''
        pass

##    // helper function used in CalcMin() to sum up the sizes of non-hidden items
##    static int SumArraySizes(const wxArrayInt& sizes, int gap)
##    {
##        // Sum total minimum size, including gaps between rows/columns.
##        // -1 is used as a magic number meaning empty row/column.
##        int total = 0;

##        const size_t count = sizes.size();
##        for ( size_t n = 0; n < count; n++ )
##        {
##            if ( sizes[n] != -1 )
##            {
##                if ( total )
##                    total += gap; // separate from the previous column

##                total += sizes[n];
##            }
##        }

##        return total;
##    }

    #-----------------------------------------------------------------------

    ColWidths = property(GetColWidths)
    FlexibleDirection = property(GetFlexibleDirection, SetFlexibleDirection)
    NonFlexibleGrowMode = property(GetNonFlexibleGrowMode,
                                   SetNonFlexibleGrowMode)
    RowHeights = property(GetRowHeights)

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
