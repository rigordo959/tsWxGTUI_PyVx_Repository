#! /usr/bin/env python
#"Time-stamp: <04/22/2015  7:29:01 AM rsg>"
'''
tsProjectMetrics.py - Class, used by the
tsLinesOfCodeProjectMetrics.py tool, to derive software
development project labor, cost, schedule and productivity
metrics from the software lines of code metrics.
'''
#################################################################
#
# File: tsProjectMetrics.py
#
# Purpose:
#
#    Class to derive software development project labor, cost,
#    schedule and productivity metrics from the software lines
#    of code metrics.
#
# Limitations:
#
#    From Wikipedia, the free encyclopedia
#
#    The Constructive Cost Model (COCOMO) is an algorithmic
#    software cost estimation model developed by Barry W.
#    Boehm. The model uses a basic regression formula with
#    parameters that are derived from historical project
#    data and current as well as future project characteristics.
#
#    COCOMO was first published in Boehm's 1981 book Software
#    Engineering Economics[1] as a model for estimating effort,
#    cost, and schedule for software projects. It drew on a
#    study of 63 projects at TRW Aerospace where Boehm was
#    Director of Software Research and Technology. The study
#    examined projects ranging in size from 2,000 to 100,000
#    lines of code, and programming languages ranging from
#    assembly to PL/I. These projects were based on the
#    waterfall model of software development which was the
#    prevalent software development process in 1981.
#
#    References to this model typically call it COCOMO 81. In
#    1995 COCOMO II was developed and finally published in
#    2000 in the book Software Cost Estimation with COCOMO II.
#    [2] COCOMO II is the successor of COCOMO 81 and is better
#    suited for estimating modern software development projects.
#    It provides more support for modern software development
#    processes and an updated project database. The need for
#    the new model came as software development technology
#    moved from mainframe and overnight batch processing to
#    desktop development, code reusability and the use of
#    off-the-shelf software components. This article refers
#    to COCOMO 81.
#
#    COCOMO consists of a hierarchy of three increasingly
#    detailed and accurate forms. The first level, Basic
#    COCOMO is good for quick, early, rough order of
#    magnitude estimates of software costs, but its accuracy
#    is limited due to its lack of factors to account for
#    difference in project attributes (Cost Drivers).
#    Intermediate COCOMO takes these Cost Drivers into
#    account and Detailed COCOMO additionally accounts
#    for the influence of individual project phases.
#
# Notes:
#
#    Algorithm requirements (for estimating software project
#    development effort, staffing and scheduling) is based
#    on COCOMO(R) 81 publication by Dr, Barry Boehm.
#
# Usage (example):
#
#   python tsProjectMetrics.py
#
# Methods:
#
#   ProjectMetrics
#   ProjectMetrics.__init__
#   ProjectMetrics.writeEstimatedDevelopmentEffort
#   ProjectMetrics.writeResults
#
# Modifications:
#
#   2013/02/10 rsg Added writeEstimatedDevelopmentEffort method.
#
# ToDo:
#
#################################################################

__title__     = 'tsProjectMetrics'
__version__   = '2.2.0'
__date__      = '05/24/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Algorithm Features of COCOMO(R) 81: ' + \
                '\n\t  Copyright (c) 1981 Dr. Barry W. Boehm. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if ((len(__credits__) == 0)):
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

import os.path

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger

#--------------------------------------------------------------------------

# COCOMO Model Types,
# From Wikipedia, the free encyclopedia

ORGANIC        = 0 # "small" teams with "good" experience working
                   # with "less than rigid" requirements

SEMI_DETATCHED = 1 # "medium" teams with mixed experience working
                   # with a mix of rigid and less than rigid requirements

EMBEDDED       = 2 # developed within a set of "tight" constraints.
                   # It is also combination of organic and semi-detached
                   # projects.(hardware, software, operational, ...)

Software_Project = ORGANIC

#########################################################################
# Begin Test Control Switches

# End Test Control Switches
#########################################################################

#--------------------------------------------------------------------------

class TsProjectMetrics(object):
    '''
    Class to derive software development project labor, cost, schedule
    and productivity metrics from the software lines of code metrics.
    '''

    #-----------------------------------------------------------------------

    def __init__(self,
                 logger,
                 debug_log,
                 input_dir,
                 output_file,
                 scan_log,
                 verbose_log,
                 fileID):
        '''
        Initialize the class and its variables.
        '''
        self.logger = logger
        self.debug_log = debug_log
        self.input_dir = input_dir
        self.output_file = output_file
        self.scan_log = scan_log
        self.verbose_log = verbose_log
        self.fileID = fileID

    #-----------------------------------------------------------------------

    def tsLocPMReportResults(self, lines):
        '''
        Write Estimated Development Effort.

        Basic COCOMO computes software development effort (and cost)
        as a function of program size. Program size is expressed in
        estimated thousands of source lines of code (SLOC)
 
        COCOMO applies to three classes of software projects:
 
        Organic projects - "small" teams with "good" experience
        working with "less than rigid" requirements
 
        Semi-detached projects - "medium" teams with mixed experience
        working with a mix of rigid and less than rigid requirements
 
        Embedded projects - developed within a set of "tight"
        constraints. It is also combination of organic and semi-
        detached projects.(hardware, software, operational, ...)
 
        The basic COCOMO equations take the form
 
        Effort Applied (E) = ab(KLOC)bb [ man-months ]
 
        Development Time (D) = cb(Effort Applied)db [months]
 
        People required (P) = Effort Applied / Development Time [count]
 
        where, KLOC is the estimated number of delivered lines
        (expressed in thousands ) of code for project. The
        coefficients ab, bb, cb and db are given in the following table:
 
               Software project        ab      bb      cb      db
               Organic                 2.4     1.05    2.5     0.38
               Semi-detached           3.0     1.12    2.5     0.35
               Embedded                3.6     1.20    2.5     0.32
 
        Basic COCOMO is good for quick estimate of software costs.
        However it does not account for differences in hardware
        constraints, personnel quality and experience, use of modern
        tools and techniques, and so on.
        '''
        estimatedLines = float(lines)
        estimatedKiloLines = estimatedLines / 1000.0

        if Software_Project == ORGANIC:

            projectClass = 'Organic'
            ab = 2.4
            bb = 1.05
            cb = 2.5
            db = 0.38

        elif Software_Project == SEMI_DETATCHED:

            projectClass = 'Semi-Detatched'
            ab = 3.0
            bb = 1.12
            cb = 2.5
            db = 0.35

        else:
            # EMBEDDED
            projectClass = 'Embedded'
            ab = 3.6
            bb = 1.2
            cb = 2.5
            db = 0.32

        effortApplied = ab * (estimatedKiloLines**bb)
        developmentTime = cb * (effortApplied**db)
        peopleRequired = effortApplied / developmentTime

        project = '\t\t"%s" Software Project Estimate' % projectClass
        model = '\n\t\tConstructive Cost Model (COCOMO(R) 81)'
        fmt0 = '%s%s' % (project, model)
 
        self.tsPMWriteResults(fmt0)

        fmt1 = '\nTotal Physical Source Lines of Code (KSLOC) ' + \
               '\t\t\t= %d (%3.2f)' % (estimatedLines, estimatedKiloLines)
        self.tsPMWriteResults(fmt1)
        fmt2 = '\n' + \
               'Estimated Development Effort in ' + \
               'Person-Years (Person-Months) ' + \
               '\t= %4.2f (%4.2f)' % (effortApplied / 12.0, effortApplied) + \
               '\n (Basic COCOMO model, Person-Months ' + \
               '= %4.2f * (KSLOC**%4.2f))' % (ab, bb)
        self.tsPMWriteResults(fmt2)

        fmt3 = '\n' + \
               'Estimated Schedule in Years (Months) ' + \
               '\t\t\t\t= %4.2f (%4.2f)' % (developmentTime / 12.0,
                                            developmentTime) + \
               '\n (Basic COCOMO model, ' + \
               'Months = %4.2f * (person-months**%4.2f))' % (cb, db)
        self.tsPMWriteResults(fmt3)

        fmt4 = '\n' + \
               'Estimated Average Number of Developers  ' + \
               '\t\t\t= %4.2f' % peopleRequired + \
               '\n (Effort/Schedule)'
        self.tsPMWriteResults(fmt4)

        assumedAverageSalary = 56286.0
        assumedOverhead = 2.4
        estimatedTotalCost = int(0.5 + (effortApplied / 12.0) * (
             assumedAverageSalary * assumedOverhead))
        fmt5 = '\n' + \
               'Total Estimated Cost to Develop ' + \
               '\t\t\t\t= $ %d' %  estimatedTotalCost + \
               '\n (Average Salary = $ %4.2f/year, Overhead = %4.2f).' % (
                   assumedAverageSalary, assumedOverhead)
        self.tsPMWriteResults(fmt5)

        assumedWorkWeeksPerYear = 50.0
        assumedHoursPerWorkDay = 8.0
        assumedDaysPerWorkWeek = 5.0
        assumedHoursPerWorkWeek = (
            assumedHoursPerWorkDay * assumedDaysPerWorkWeek)
        assumedHoursPerWorkYear = (
            assumedWorkWeeksPerYear * assumedHoursPerWorkWeek)
        appliedPeople = peopleRequired
        appliedYears = (effortApplied / 12.0)
        estimatedLinesOfCodePerHour = estimatedLines / (
            appliedPeople * appliedYears * assumedHoursPerWorkYear)
        fmt6 = '\n' + \
               'Estimated Productivity in Source Lines of Code per Day ' + \
               '\t\t= %2.2g' % (
                   estimatedLinesOfCodePerHour * assumedHoursPerWorkDay)
        self.tsPMWriteResults(fmt6)

        hline = '-' * 78
        self.tsPMWriteResults('\n%s' % hline)

    #-----------------------------------------------------------------------

    def tsPMWriteResults(self, resultsBuffer):
        '''
        '''
        self.fileID.write('%s\n' % resultsBuffer)
        print(resultsBuffer)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    pass
