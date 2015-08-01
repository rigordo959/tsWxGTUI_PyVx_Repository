#! /usr/bin/env python
# "Time-stamp: <03/28/2015  2:09:08 AM rsg>"
'''
test_TermsAndConditions.py - Capture and display the contents
of the Masthead, Copyright, License and Notice entries in the
configuration file "tsWxGlobals" to facilitate validation.
'''
#################################################################
#
# File: test_TermsAndConditions.py
#
# Purpose:
#
#     Capture and display the contents of the Masthead, Copy-
#     right, License and Notice entries in the configuration
#     file "tsWxGlobals" to facilitate validation.
#
# Usage (example):
#
#     python test_TermsAndConditions.py
#
# Requirements:
#
#
# Capabilities:
#
#
# Limitations:
#
#
# Notes:
#
# Classes:
#
#
# Methods:
#
#
# Modifications:
#
#    2015/01/14 rsg Initial version.
#
# ToDo:
#
#
##############################################################

__title__     = 'test_TermsAndConditions'
__version__   = '1.0.0'
__date__      = '01/14/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = ''

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

import math
import os
import signal
import sys
import time
import types
import platform

#--------------------------------------------------------------------------

tsPythonVersion = sys.version[0:5]
if (tsPythonVersion >= '1') and (tsPythonVersion < '2'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py1x'

elif (tsPythonVersion >= '2') and (tsPythonVersion < '3'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py2x'

elif (tsPythonVersion >= '3') and (tsPythonVersion < '4'):

    # Presume tsWxGTUI_PyVx reflects Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_Py3x'

else:

    # Presume tsWxGTUI_PyVx reflects default Python version
    tsWxGTUI_PyVx = 'tsWxGTUI_PyVx'

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsCxGlobals as cx
from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

#--------------------------------------------------------------------------

##DEBUG = True # Avoids tsWx import because of circular dependency.
DEBUG = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Launch'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Progress'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Termination'] | \
        cx.ThemeToUse['Troubleshooting']['Debug_GUI_Exceptions']

##VERBOSE = True # Avoids tsWx import because of circular dependency.
VERBOSE = cx.ThemeToUse['Troubleshooting']['Debug_GUI_Configuration']

###--------------------------------------------------------------------------

##try:

##    import tsLibGUI

##except ImportError, importCode:

##    print('%s: ImportError (tsLibGUI); ' % __title__ + \
##          'importCode=%s' % str(importCode))

###--------------------------------------------------------------------------

##try:

##    from tsWxGlobals import ThemeToUse as wxThemeToUse

##except ImportError, importCode:

##    print('%s: ImportError (tsLibGUI); ' % __title__ + \
##          'importCode=%s' % str(importCode))

#---------------------------------------------------------------------------

hostOS = platform.system().upper()
pythonVersion = 'Python-%s' % str(platform.python_version())

#---------------------------------------------------------------------------

class TermsAndConditions(object):
    '''
    '''

    #-----------------------------------------------------------------------

    def __init__(self):
        '''
        '''
        print('\nBegin "__init__".')
        self.logger = tsLogger.TsLogger(
            threshold=tsLogger.DEBUG,
            start=time.time(),
            name=tsLogger.StandardOutputFile)

        try:

##            print('\n\tBegin "splashScreenConfig".')

            ##     'SplashScreen': {
            ##   'name': 'SplashScreen', 
            ##   'Copyright': {
            ##       'name': 'Copyright',
            ##       'text': theCopyright,
            ##       'BackgroundColour': COLOR_BLACK,
            ##       'ForegroundColour': COLOR_WHITE
            ##       },
            ##   'Enabled': True,
            ##   'Image': {
            ##       'name': 'Image',
            ##       'MakeReusable': True,
            ##       'Path': './bmp/',
            ##       'FileName': 'SplashScreen.bmp'
            ##       },
            ##   'License': {
            ##       'name': 'License',
            ##       'text': theLicense,
            ##       'BackgroundColour': COLOR_BLACK,
            ##       'ForegroundColour': COLOR_WHITE
            ##       },
            ##   'Notices': {
            ##       'name': 'Notices',
            ##       'text': theNotices,
            ##       'BackgroundColour': COLOR_BLACK,
            ##       'ForegroundColour': COLOR_WHITE
            ##       },
            ##   'ShowSeconds': 15,
            ##   'Masthead': {
            ##       'name': 'Masthead',
            ##       'text': theMasthead,
            ##       'BackgroundColour': COLOR_BLACK,
            ##       'ForegroundColour': COLOR_WHITE
            ##       }
            ##   },

            self.theSplashScreen = {} # wxThemeToUse['SplashScreen']
            self.theSplashScreen['Copyright'] = cx.theCopyright
            self.theSplashScreen['License'] = cx.theLicense
            self.theSplashScreen['Notices'] = cx.theNotices
            self.theSplashScreen['Masthead'] = cx.theMasthead

            self.theSplashScreen['FileName'] = 'TermsAndConditions.txt'

            self.theSplashScreen['Path'] = './logs'

            self.mkdirsHead = self.theSplashScreen['Path']

            self.mkdirsMode = 0777

            readme_file = os.path.join(
                self.mkdirsHead,
                self.theSplashScreen['FileName'])

            try:
                print('\n\t\tBegin "makedirs".')
                # os.makedirs(self.mkdirsHead, self.mkdirsMode)
                readme_mode = 'w'
                readme_buffering = 0
                sys.stderr.write(
                    'INFO: readme_file=%s\n' % str(readme_file))
                print('\n\t\tEnd "makedirs".')

            except Exception, e:
                sys.stderr.write('EXCEPTION: <%s>' % str(e))
                print('\n\t\tException "makedirs".')

            try:
                print('\n\t\tBegin "open".')
                self.readme_fileID = open(readme_file,
                                          readme_mode,
                                          readme_buffering)
                print('\n\t\tEnd "open".')
            except IOError, e:
                sys.stderr.write('WARNING: <%s>' % str(e))
                print('\n\t\tExceptopn "open".')

            print('\n\tBegin "splashScreenConfig".')

        except Exception, errorCode:

            print('%s: Configuration Error (wx.ThemeToUse); ' % __title__ + \
                  'importCode=%s' % str(errorCode))
            print('Exception "__init__".')

        print('End "__init__".')

    #-----------------------------------------------------------------------

    def tsGetSplashScreenMetrics(self):
        '''
        Build the SplashScreen to fit available screen.
        '''
        splashScreenMasthead = []
        linesMasthead = self.theSplashScreen['Masthead'].split('\n')
        maxMastheadWidth = 0
        maxMastheadHeight = 0
        separator = '%s' % '-' * 58

        print(separator)
##        self.readme_fileID.write('+-%-58s-+\n' % str(separator))
        for aLine in linesMasthead:
            maxMastheadWidth = max(
                maxMastheadWidth, len(aLine))
            maxMastheadHeight += 1
            splashScreenMasthead += [aLine]
            print('(row %2d, col %2d):"%s"' % (
                maxMastheadHeight, maxMastheadWidth, str(aLine)))
##            self.readme_fileID.write('| %-58s |\n' % str(aLine))
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxMastheadWidth=%d; maxMastheadHeight=%d' % (
                maxMastheadWidth, maxMastheadHeight))

        splashScreenCopyright = []
        linesCopyright = self.theSplashScreen['Copyright'].split('\n')
        maxCopyrightWidth = 0
        maxCopyrightHeight = 0

        print(separator)
        for aLine in linesCopyright:
            maxCopyrightWidth = max(
                maxCopyrightWidth, len(aLine))
            maxCopyrightHeight += 1
            splashScreenCopyright += [aLine]
            print('(row %2d, col %2d):[%s]' % (
                maxCopyrightHeight, maxCopyrightWidth, str(aLine)))
##            self.readme_fileID.write('| %-58s |\n' % str(aLine))
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxCopyrightWidth=%d; maxCopyrightHeight=%d' % (
                maxCopyrightWidth, maxCopyrightHeight))

        splashScreenLicense = []
        linesLicense = self.theSplashScreen['License'].split('\n')
        maxLicenseWidth = 0
        maxLicenseHeight = 0

        print(separator)
        for aLine in linesLicense:
            maxLicenseWidth = max(
                maxLicenseWidth, len(aLine))
            maxLicenseHeight += 1
            splashScreenLicense += [aLine]
            print('(row %2d, col %2d):[%s]' % (
                maxLicenseHeight, maxLicenseWidth, str(aLine)))
##            self.readme_fileID.write('| %-58s |\n' % str(aLine))
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxLicenseWidth=%d; maxLicenseHeight=%d' % (
                maxLicenseWidth, maxLicenseHeight))

        splashScreenNotices = []
        linesNotices = self.theSplashScreen['Notices'].split('\n')
        maxNoticesWidth = 0
        maxNoticesHeight = 0

        print(separator)
        for aLine in linesNotices:
            maxNoticesWidth = max(
                maxNoticesWidth, len(aLine))
            maxNoticesHeight += 1
            splashScreenNotices += [aLine]
            print('(row %2d, col %2d):[%s]' % (
                maxNoticesHeight, maxNoticesWidth, str(aLine)))
##            self.readme_fileID.write('| %-58s |\n' % str(aLine))
        self.logger.debug(
            'tsBuildSplashScreen: ' + \
            'maxNoticesWidth=%d; maxNoticesHeight=%d' % (
                maxNoticesWidth, maxNoticesHeight))

##        self.readme_fileID.write('+-%-58s-+\n' % str(separator))

##        self.readme_fileID.flush()
##        self.readme_fileID.close()
        print(separator)

    #-----------------------------------------------------------------------

    def tsBuildTermsAndConditions(self):
        '''
        Build the Terms and Conditions file.
        '''
        theWidth = self.tsGetTermsAndConditionsMaxWidth()
        self.tsOutputTermsAndConditions(maxWidth=theWidth)

    #-----------------------------------------------------------------------

    def tsGetTermsAndConditionsMaxWidth(self):
        '''
        Return the maximum width required to display the contents of
        all Masthead, Copyright, License and Notices lines-of-text.
        '''
        linesMasthead = self.theSplashScreen['Masthead'].split('\n')
        maxMastheadWidth = 0

        for aLine in linesMasthead:
            maxMastheadWidth = max(
                maxMastheadWidth, len(aLine))

        linesCopyright = self.theSplashScreen['Copyright'].split('\n')
        maxCopyrightWidth = 0

        for aLine in linesCopyright:
            maxCopyrightWidth = max(
                maxCopyrightWidth, len(aLine))

        linesLicense = self.theSplashScreen['License'].split('\n')
        maxLicenseWidth = 0

        for aLine in linesLicense:
            maxLicenseWidth = max(
                maxLicenseWidth, len(aLine))

        linesNotices = self.theSplashScreen['Notices'].split('\n')
        maxNoticesWidth = 0

        for aLine in linesNotices:
            maxNoticesWidth = max(
                maxNoticesWidth, len(aLine))

            return (max(maxMastheadWidth,
                        maxCopyrightWidth,
                        maxLicenseWidth,
                        maxNoticesWidth))

    #-----------------------------------------------------------------------

    def tsOutputTermsAndConditions(self, maxWidth):
        '''
        Output the Terms and Conditions to the Log directory..
        '''
        splashScreenMasthead = []
        linesMasthead = self.theSplashScreen['Masthead'].split('\n')
        maxMastheadWidth = 0
        maxMastheadHeight = 0
        separator = '%s' % '-' * maxWidth
        horizontal_border = '+-%s-+' % separator

        self.readme_fileID.write('%s\n' % str(horizontal_border))
        for aLine in linesMasthead:
            padding = ' '* (maxWidth - len(aLine))
            self.readme_fileID.write('| %s%s |\n' % (str(aLine), str(padding)))

        splashScreenCopyright = []
        linesCopyright = self.theSplashScreen['Copyright'].split('\n')
        maxCopyrightWidth = 0
        maxCopyrightHeight = 0

        for aLine in linesCopyright:
            padding = ' '* (maxWidth - len(aLine))
            self.readme_fileID.write('| %s%s |\n' % (str(aLine), str(padding)))

        splashScreenLicense = []
        linesLicense = self.theSplashScreen['License'].split('\n')
        maxLicenseWidth = 0
        maxLicenseHeight = 0

        for aLine in linesLicense:
            padding = ' '* (maxWidth - len(aLine))
            self.readme_fileID.write('| %s%s |\n' % (str(aLine), str(padding)))

        splashScreenNotices = []
        linesNotices = self.theSplashScreen['Notices'].split('\n')
        maxNoticesWidth = 0
        maxNoticesHeight = 0

        for aLine in linesNotices:
            padding = ' '* (maxWidth - len(aLine))
            self.readme_fileID.write('| %s%s |\n' % (str(aLine), str(padding)))

        self.readme_fileID.write('%s\n' % str(horizontal_border))

        self.readme_fileID.flush()
        self.readme_fileID.close()

#---------------------------------------------------------------------------

if __name__ == '__main__':
 
    print(__header__)

    myResults = TermsAndConditions()
    myResults.tsGetSplashScreenMetrics()
    myResults.tsBuildTermsAndConditions()
