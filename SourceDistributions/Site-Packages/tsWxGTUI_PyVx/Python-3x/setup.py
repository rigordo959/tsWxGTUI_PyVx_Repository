#! /usr/bin/env python
# "Time-stamp: <08/26/2016  9:22:03 AM rsg>"
'''
setup.py - The setup script uses features from both the basic
Python distutils and its setuptools (easy_install) enhancement.
It is the common script used by developers and installers of
the "tsWxGTUI_PyVx" Toolkit site-packages.
'''
#################################################################
#
# File: setup.py
#
# Purpose:
#
#    The setup script uses features from both the basic Python
#    distutils and its setuptools (easy_install) enhancement.
#    It is the common script used by both developers and install-
#    ers of the "tsWxGTUI_PyVx" Toolkit site-packages.
#
# Requirements:
#
#    See http://docs.python.org/2/distutils/introduction.html
#    See http://pythonhosted.org/setuptools/
#
# Capabilities:
#
#    1. The "sdist" command option is almost exclusively used by
#       module developers.
#
#       It will create an archive file (e.g., tarball on Linux, Mac
#       OS X and Unix). The command is equivalent to the following:
#
#       #############################################################
#       # tar -zcf /path/to/file.tar.gz /path/to/directory
#       tar -zcf /path/to/tsWxGTUI_PyVx.tar.gz /path/to/tsWxGTUI_PyVx
#       tar -zcf /path/to/tsWxGTUI_Py2x.tar.gz /path/to/tsWxGTUI_Py2x
#       tar -zcf /path/to/tsWxGTUI_Py3x.tar.gz /path/to/tsWxGTUI_Py3x
#       #############################################################
#
#       It will create an archive file (e.g., ZIP file on Micro-
#       soft Windows). The command is equivalent to the following:
#
#       #############################################################
#       # zip options archive inpath inpath ...
#       zip -r /path/to/tsWxGTUI_PyVx.zip /path/to/tsWxGTUI_PyVx
#       zip -r /path/to/tsWxGTUI_Py2x.zip /path/to/tsWxGTUI_Py2x
#       zip -r /path/to/tsWxGTUI_Py3x.zip /path/to/tsWxGTUI_Py3x
#       #############################################################
#
#       Each archive file will contain the following:
#
#       a. setup script (setup.py)
#       b. modules (e.g., tsPlatformQuery.py)
#       c. packages (e.g., tsLibCLI).
#
#       The archive file is named tsWxGTUI_PyVx-<version>.tar.gz
#       (or .zip), and will unpack into a directory named
#       tsWxGTUI_PyVx-<version>.
#
#          For use with Python 2.0.0-2.7.11, Py2x will replace PyVx.
#
#          For use with Python 3.0.0-3.5.1, Py3x will replace PyVx.
#
#    2. The "build" command option creates a Python version-specific
#       installable "image" of the "tsWxGTUI" Toolkit from its
#       distribution download.
#
#    3. The "install" command option copies the installable "image"
#       into the site-package of whichever Python interpretter
#       launched the setup.py script.
#
#       The installed "image" supports the running (execution) of
#       those Python application programs whose Command Line
#       Interface or Graphical-style User Interface requires the
#       services of the "tsWxGTUI" Toolkit.
#
#    4. The "upload" command option copies the installable "image"
#       into the Python Package Index (PyPi) site-package of whichever
#       Python interpretter launched the setup.py script.
#
# Limitations:
#
#    CLI-mode ("argparse", "optparse", "getopt")
#
#       The setup.py file for building source code distributions
#       has had  use/testing on Linux, Mac OS X, Microsoft Windows
#       and Unix with their built-in or add-on Python:
#
#       Python 2.x (2.0.1, 2.4.6, 2.5.6, 2.6.4, 2.6.6, 2.6.8,
#                   2.6.9, 2.7.1, 2.7.3, 2.7.5, 2.7.6, 2.7.9,
#                   2.7.10, 2.7.11)
#
#       and
#
#       Python 3.x (3.0.1, 3.1.5, 3.2.3, 3.2.3, 3.2.5, 3.3.0,
#                   3.3.1, 3.3.4, 3.4.0, 3.4.1, 3.4.2, 3.4.3,
#                   3.5.0, 3.5.1).
#
#    GUI-mode ("wxPython" API Subset Emulation)
#
#       The setup.py file for building source code distributions
#       has had use/testing on Linux, Mac OS X, Microsoft Windows
#       and Unix with their built-in or add-on Python:
#
#       Python 2.x (2.6.4, 2.6.6, 2.6.8, 2.6.9, 2.7.1, 2.7.3,
#                   2.7.5, 2.7.6, 2.7.9, 2.7.10, 2.7.11)
#
#       and
#
#       Python 3.x (3.2.3, 3.2.3, 3.2.5, 3.3.0, 3.3.1, 3.3.4,
#                   3.4.0, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1).
#
#    The installed site-package must be removed (manuallly) from
#    hosts being used to fix, enhance and debug the "tsWxGTUI_PyVx"
#    Toolkit. Removal ensures that only the un-installed, modi-
#    fied Toolkit will be run. 
#
# Usage:
#
#    cd ./tsWxGTUI_PyVx_Repository/SourceDistributions/Site-Packages
#
#    # if Python 3.0.0 <= version < 4.0.0:
#
#          pushd ./tsWxGTUI_PyVx/Python-3x
#
#          # If using specific Python 3.x (example for 3.4.3)
#          python3.4.3 setup.py sdist
#          python3.4.3 setup.py build
#          python3.4.3 setup.py install
#          python3.4.3 setup.py upload
#
#          # If using default Python 3.x
#          python setup.py sdist
#          python setup.py build
#          python setup.py install
#          python setup.py upload
#
#    # else Python 2.0.0 <= version < 3.0.0:
#
#          pushd ./tsWxGTUI_PyVx/Python-2x
#
#          # If using specific Python 2.x (example for 2.7.11)
#          python2.7.11 setup.py sdist
#          python2.7.11 setup.py build
#          python2.7.11 setup.py install
#          python2.7.11 setup.py upload
#
#          # If using default Python 2.x
#          python setup.py sdist
#          python setup.py build
#          python setup.py install
#          python setup.py upload
#
# Notes:
#
#    From: "https://docs.python.org/2/distutils/sourcedist.html":
#
#    "As shown in section A Simple Example, you use the sdist command to
#    create a source distribution. In the simplest case,
#
#    python setup.py sdist
#
#    (assuming you haven't specified any sdist options in the setup script
#    or config file), sdist creates the archive of the default format for
#    the current platform. The default format is a gzip'ed tar file
#    (.tar.gz) on Unix, and ZIP file on Windows.
#
#    You can specify as many formats as you like using the --formats option,
#    for example:
#
#          python setup.py sdist --formats=gztar,zip"
#
#    From: "http://pythonhosted.org/an_example_pypi_project/setuptools.html":
#
#    "Standard commands:
#      build             build everything needed to install
#      build_py          "build" pure Python modules (copy to build directory)
#      build_ext         build C/C++ extensions (compile/link to build directory)
#      build_clib        build C/C++ libraries used by Python extensions
#      build_scripts     "build" scripts (copy and fixup #! line)
#      clean             clean up temporary files from 'build' command
#      install           install everything from build directory
#      install_lib       install all Python modules (extensions and pure Python)
#      install_headers   install C/C++ header files
#      install_scripts   install scripts (Python or otherwise)
#      install_data      install data files
#      sdist             create a source distribution (tarball, zip file, etc.)
#      register          register the distribution with the Python package index
#      bdist             create a built (binary) distribution
#      bdist_dumb        create a "dumb" built distribution
#      bdist_rpm         create an RPM distribution
#      bdist_wininst     create an executable installer for MS Windows
#      upload            upload binary package to PyPI
#    
#    Extra commands:
#      rotate            delete older distributions, keeping N newest files
#      develop           install package in 'development mode'
#      setopt            set an option in setup.cfg or another config file
#      saveopts          save supplied options to setup.cfg or other config file
#      egg_info          create a distribution's .egg-info directory
#      upload_sphinx     Upload Sphinx documentation to PyPI
#      install_egg_info  Install an .egg-info directory for the package
#      alias             define a shortcut to invoke one or more commands
#      easy_install      Find/get/install Python packages
#      bdist_egg         create an "egg" distribution
#      test              run unit tests after in-place build
#      build_sphinx      Build Sphinx documentation
#    
#    usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
#       or: setup.py --help [cmd1 cmd2 ...]
#       or: setup.py --help-commands
#       or: setup.py cmd --help"
#
#    From Wikipedia, the free encyclopedia:
#
#       "GitHub is a Web-based Git repository hosting service. It offers
#        all of the distributed revision control and source code manage-
#        ment (SCM) functionality of Git as well as adding its own fea-
#        tures. Unlike Git, which is strictly a command-line tool,
#        GitHub provides a Web-based graphical interface and desktop as
#        well as mobile integration. It also provides access control and
#        several collaboration features such as bug tracking, feature
#        requests, task management, and wikis for every project.
#
#        GitHub offers both plans for private repositories and free
#        accounts, which are usually used to host open-source software
#        projects. As of 2015, GitHub reports having over 11 million
#        users and over 29.4 million repositories, making it the
#        largest host of source code in the world."
#
#    Though you do not need to become a "GitHub" web hosting service
#    member, you may view or obtain a clone or copy of the Toolkit
#    author's work via the following internet web address:
#
#        https://github.com/rigordo959/tsWxGTUI_PyVX_Repository

#    Additional reference:
#
#        http://guide.python-distribute.org/quickstart.html
#
#    Setup.py installs "tsWxGTUI" items in the following
#    platform host (Cygwin, Linux, Mac OS X, Microsoft
#    Windows, Unix) and Python version (XY or X.Y) specific
#    locations:
#
#    Cygwin (a free Linux-like Command Line Interface and GNU
#    toolkit add-on to Microsoft Windows from Red Hat)
#
#        Built-in <Path>:
#            /cygwin/lib
#
#        User Add-on <Path>:
#            /cygwin/lib
#
#        <Path>/site-packages/tsWxGTUI_PyVx
#        <Path>/site-packages/tsWxGTUI_PyVx.egg-info
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsUtilities
#
#    GNU/Linux
#
#        Built-in <Path>:
#            /Library/Python/X.Y
#
#        User Add-on <Path>:
#            /opt/local/lib/pythonX.Y
#
#        <Path>/dist-packages/tsWxGTUI_PyVx
#        <Path>/dist-packages/tsWxGTUI_PyVx.egg-info
#        <Path>/dist-packages/tsWxGTUI_PyVx/tsLibCLI
#        <Path>/dist-packages/tsWxGTUI_PyVx/tsLibGUI
#        <Path>/dist-packages/tsWxGTUI_PyVx/tsToolsCLI
#        <Path>/dist-packages/tsWxGTUI_PyVx/tsToolsGUI
#        <Path>/dist-packages/tsWxGTUI_PyVx/tsUtilities
#
#    Mac OS X
#
#        Built-in <Path>:
#            /Library/Python/X.Y
#
#        User Add-on <Path>:
#            /opt/local/lib/pythonX.Y
#
#        <Path>/site-packages/tsWxGTUI_PyVx
#        <Path>/site-packages/tsWxGTUI_PyVx.egg-info
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsUtilities
#
#    Microsoft Windows
#
#        Built-in <Path>:
#            /PythonXY
#
#        User Add-on <Path>:
#            /PythonXY
#
#        <Path>/site-packages/tsWxGTUI_PyVx
#        <Path>/site-packages/tsWxGTUI_PyVx.egg-info
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsUtilities
#        ##
#        ## The following are installed but are not usable
#        ## without a usable Curses library for Windows.
#        ## The GnuWin32 Project provides a POSIX-compliant
#        ## Command Line Interface that works with Windows
#        ## Command Prompt and Windows PoserShell.GNU Toolkit
#        ##
#        ## Unfortunately, the contributed PDCurses 2.6 does
#        ## not resolve Python's Curses mouse button references.
#        ##
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsGUI
#
#    Unix
#
#        Built-in <Path>:
#            /Library/Python/X.Y
#
#        User Add-on <Path>:
#            /opt/local/lib/pythonX.Y
#
#        <Path>/site-packages/tsWxGTUI_PyVx
#        <Path>/site-packages/tsWxGTUI_PyVx.egg-info
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsLibGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsCLI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsToolsGUI
#        <Path>/site-packages/tsWxGTUI_PyVx/tsUtilities
#
#    Debugging the setup script
#
#        Sometimes things go wrong, and the setup script doesn't
#        do what the developer wants.
#
#        Distutils catches any exceptions when running the setup
#        script, and print a simple error message before the script
#        is terminated. The motivation for this behaviour is to not
#        confuse administrators who don't know much about Python
#        and are trying to install a package. If they get a big
#        long traceback from deep inside the guts of Distutils,
#        they may think the package or the Python installation is
#        broken because they don't read all the way down to the
#        bottom and see that it's a permission problem.
#
#        On the other hand, this doesn't help the developer to
#        find the cause of the failure. For this purpose, the
#        DISTUTILS_DEBUG environment variable can be set to
#        anything except an empty string, and distutils will
#        now print detailed information what it is doing, and
#        prints the full traceback in case an exception occurs.
#
# Methods:
#
#    read - Return the contents of the designated "README" file
#        after it has been opened for read access.
#
#    is_package - Return True if and only if there is a file
#        named "__init__.py" in the designated path.
#        If True, this would denote that the path contains a
#        package type collection of Python source code files.
#
# Classes:
#
#    None
#
# Modifications:
#
#    2013/05/05 rsg Added ".tsLibCLI.tsCommandLineParserPkg"
#
#    2013/05/06 rsg Removed ".Python-2.x.tsApplications"
#                   which contained Previous "tsUnitTestApps".
#
#    2013/09/13 rsg Updated to reflect deliverable changes.
#
#    2013/10/08 rsg Added "tsUtilities".
#
#    2013/10/08 rsg Added commented definitions for egg-info file
#                   to include documents associated with the
#                   README file.
#
#    2013/10/26 rsg Added content to Capabilities, Limitations
#                   and Notes.
#
#    2013/12/16 rsg Updated installation description.
#
#    2013/12/24 rsg Removed non-essential tsLibCLI
#                   preview references to:
#                     tsConfifObjPkg
#                     tsDataBasePkg
#                     tsDecoratorsPkg
#                     tsLoggingPkg
#                     tsMultiLevelOptionParserPkg
#                     tsThreadPoolPkg
#
#    2013/12/24 rsg Removed non-essential tsToolsCLI
#                   preview references to:
#                     tsLibraryImportPkg
#                     tsPublishPkg
#                     tsReAuthorPkg
#                     tsReImportPkg
#                     tsReVersionPkg
#
#    2014/02/15 rsg Revised platform requirements after
#                   discovering incompatibility issue with
#                   Python 3.3 and 3.4.
#
#    2014/03/05 rsg Created version with '%s-%s' % (
#                   tsPythonVersion, tsToolkitVersion)
#                   to register Python version dependancies.
#                   Examples:
#                     2.7.3 code runs on 2.6.8 but 2.5.0 traps.
#                     3.2.3 code runs on 3.2.3 but 3.3.3 traps.
#
#    2014/03/11 rsg Added support for MANIFEST.in.
#
#    2014/04/06 rsg Changed prefix to "tsWxGTUI_PyVx"
#                   or "tsWxGTUI_Py3x" from "tsWxGTUI"
#                   in order to distinguish "legacy"
#                   and "currect" from next generation
#                   "current" and future" Python version.
#
#    2014/04/16 rsg Added and explained use, substitution and
#                   reference to PyVx for Python 2.x and 3.x.
#                   Also, corrected name associated with
#                   tsWxGTUI_PyVx.egg-info file.
#
#    2014/05/29 rsg Added support for Python 1.x, in unlikely
#                   event that someone wants this capability.
#                   This is unlikely to be used because python
#                   1.x is nolonger available via:
#                   https://www.python.org/download/releases/.
#
#    2014/07/06 rsg Updated classifiers to identify platforms
#                   used for development and testing.
#
#    2014/11/04 rsg Updated classifiers to identify additional
#                   platforms used for development and testing.
#
#    2014/11/05 rsg Added Python Version identification logic
#                   from say_hello.py.
#
#    2014/11/14 rsg Added list of methods. Update classifiers.
#
#    2015/01/05 rsg Added support for Windows 10.
#
#    2015/05/02 rsg Clarified setup application for Linux,
#                   Mac OS X, Microsoft Windows and Unix.
#
#    2016/01/26 rsg General revisions to documentation to show
#                   support for Python 2.7.10, 2.7.11, 3.5.0
#                   and 3.5.1.
#
#                   Updated supported host operating system.
#
#    2016/03/26 rsg Updated to support "python setup.py upload"
#                   to pypi and testpypi.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = 'setup'
__version__   = '0.0.7'
__date__      = '08/26/2016'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2016 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License (GPL), ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  Python Disutils and API Features: ' + \
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

import os
import sys

##import tsWxGTUI as mypackage

# print('setup.py: __file__ = %s' % __file__)

#--------------------------------------------------------------------------

tsPythonVersion = sys.version[0:5]

# Debugging the setup script

SETUP_DEBUG = True

if SETUP_DEBUG:
    DISTUTILS_DEBUG = 'Debugging the setup script.'
else:
    DISTUTILS_DEBUG = ''

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if tsPythonVersion < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from setuptools import setup, find_packages

#--------------------------------------------------------------------------

cwd = os.getcwd()

if (cwd.lower().find('python-1x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py1x'

elif (cwd.lower().find('python-2x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py2x'

elif (cwd.lower().find('python-3x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py3x'

elif (cwd.lower().find('python-4x') != -1):

      # Presume prefix reflects directory name
      prefix = 'tsWxGTUI_Py4x'

elif (tsPythonVersion >= '1') and (tsPythonVersion < '2'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py1x'

elif (tsPythonVersion >= '2') and (tsPythonVersion < '3'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py2x'

elif (tsPythonVersion >= '3') and (tsPythonVersion < '4'):

      # Presume prefix reflects Python version
      prefix = 'tsWxGTUI_Py3x'

else:

      # Presume default prefix
      prefix = 'tsWxGTUI_PyVx'

package_dir = {'src': 'src'}
test_dir = {'test': 'test'}

#--------------------------------------------------------------------------

# Utility function to read the "README" file.
# Used for the long_description.
# It's nice, because now:
#
#   1) we have a top level "README" file and
#
#   2) it's easier to type in the "README" file than to put a raw
#      string in below ...
#
#   3) Generation of the "README.txt" file may be facil-
#      itated by:
#
#      a) saving the Microsoft Word version of the TeamSTARS
#         "tsWGTUI" Toolkit Brochure file as a WEB page
#         (.htm) file
#
#      b) using the "lynx" utility, a text-based web browser
#         for use on cursor-addressable character cell terminals
#         with its command to dump the (.htm) file into a text
#         file, "README.txt", via the following command line:
#
#         $ lynx -dump
#            ./tsWxGTUI_Vol.__1_SDIST_Brochure.htm > 
#                README.txt
#
#      c) re-formatting and editing the text file, "README.txt",
#         into a more readable style suited to a small display.
#
def read(fname):
    '''
    Return the contents of the designated "README" file
    after it has been opened for read access.
    '''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#--------------------------------------------------------------------------

# Utility function to report whether or not the designated path
# contains the "__init__.py" file associated with a collection
# (package) of Python source code files.
def is_package(path):
    '''
    Return True if and only if there is a file named
    "__init__.py" in the designated path. If True, this
    would denote that the path contains a package
    type collection of Python source code files.
    '''
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )

#--------------------------------------------------------------------------

##def find_packages(path=__path__, prefix=""):
##    """ Find all packages in path """
##    yield prefix
##    prefix = prefix + "."
##    for _, name, ispkg in walk_packages(path, prefix):
##        if ispkg:
##            yield name

#--------------------------------------------------------------------------

#
tsToolkitVersion = '0.0.7'

setup(
    name = prefix,
    version = tsToolkitVersion,
    packages = find_packages(exclude=[
        "ez_setup", "tests", "tests.*"]),
    scripts = ["say_hello.py"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ["docutils>=0.3"],

##    package_data = {
##        # If any package contains *.txt or *.rst files, include them:
##        "": ["*.txt", "*.rst"],
##        # And include any *.msg files found in the "hello" package, too:
##        "hello": ["*.msg"],
##      },

    include_package_data=True,

    # metadata for upload to PyPI
    author = "Richard S. Gordo, a.k.a. Software Gadgetry",
    author_email = "SoftwareGadgetry@comcast.net",
    maintainer = "Richard S. Gordon",
    maintainer_email = "SoftwareGadgetry@comcast.net",
##    package_index_owner = "rigordo959",
##    url = "https://pypi.python.org/pypi ",

##    download_url = "https://pypi.python.org/pypi/tsWxGTUI_PyVx ",
##    home_page = "https://github.com/rigordo959/tsWxGTUI_PyVx_Repository",
##    download_url = "https://github.com/rigordo959/tsWxGTUI_PyVx_Repository/archive/master.zip",
    # To download the toolkit as a compressed zip file, click on the <Download ZIP button>.
    # Extract the dirctories and files via the CLI command <unzip tsWxGTUI_PyVx_Repository-master.zip>.

    description = (
        "Cross-platform toolkit for developing Python CLI and TUI applications for POSIX-compatible 32-bit/64-bit platforms. Text-mode emulation of pixel-mode wxPython GUI is launced by CLI."),

    long_description = read("README.txt"),
    license = "GNU GENERAL PUBLIC LICENSE (GPL) Version 3, 29 June 2007 ",
    keywords = ["CLI",
                "Cross-platform",
                "Curses",
                "GUI",
                "Ncurses",
                "POSIX",
                "TUI",
                "wxPython"],
##    platform_requirements = [
##        "HOST CPU with 32-bit/64-bit processor ",
##        "Host  OS with Multi-User, Multi-Process and Multi-Threaded features ",
##        "Command Line Interface shells (POSIX-type "bash", "sh") ",
##        "Command Line Interface shells (Microsoft-type "command prompt") ",
##        "Graphical User Interface (wxPython-style "text user interface") ",
##        "Remote Command Line Interface shells ("ssh", "rsh", "sftp", "ftp") ",
##        "Python Virtual Machine with Python Run Time Library modules ",
##        "Curses/nCurses Terminal Control Library for POSIX-like systems ",
##        "Non-Color Console/Terminal/Emulator (mouse with vt100/vt220) ",
##        "8-Color   Console/Terminal/Emulator (mouse with cygwin mintty) ",
##        "8-Color   Console/Terminal/Emulator (mouse with xterm/xterm-color) ",
##        "16-Color  Console/Terminal/Emulator (mouse with xterm-16color) ",
##        "16-Color  Console/Terminal/Emulator (mouse with xterm-88color) ",
##        "16-Color  Console/Terminal/Emulator (mouse with xterm-256color)"
##        ],
##
    classifiers = [
##
        "Development Status :: 2 - Pre-Alpha ",
        "Environment :: Console ",
        "Environment :: Console :: Curses ",
        "Environment :: MacOS X ",
        "Environment :: Win32 (MS Windows CLI-mode only) ",
        "Environment :: Win32 (MS Windows+Cygwin) ",
        "Environment :: Win64 (MS Windows CLI-mode only) ",
        "Environment :: Win64 (MS Windows+Cygwin) ",
        "Environment :: X11 Applications ",
        "Environment :: X11 Applications :: GNOME ",
        "Environment :: X11 Applications :: GTK ",
        "Environment :: X11 Applications :: KDE ",
##
##        "Intended Audience :: Customer Service ",
        "Intended Audience :: Developers ",
        "Intended Audience :: Education ",
##        "Intended Audience :: End Users/Desktop ",
##        "Intended Audience :: Information Technology ",
##        "Intended Audience :: Manufacturing ",
##        "Intended Audience :: Science/Research ",
##        "Intended Audience :: System Administrators ",
##
        "License :: Creative Commons Attribution-ShareAlike 2.5 ",
        "License :: Creative Commons Attribution-ShareAlike 3.0 ",
        "License :: GNU Free Documentation License v1.3 (GFDLv1.3) ",
        "License :: OSI Approved ",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3) ",
##
        "Natural Language :: English ",
##
        "Operating System :: MacOS ",
##        "Operating System :: MacOS :: MacOS X :: 10.3  (Panther) ",
##        "Operating System :: MacOS :: MacOS X :: 10.4  (Tiger) ",
##        "Operating System :: MacOS :: MacOS X :: 10.5  (Leopard) ",
##        "Operating System :: MacOS :: MacOS X :: 10.6  (Snow Leopard) ",
        "Operating System :: MacOS :: MacOS X :: 10.7  (Lion) ",
        "Operating System :: MacOS :: MacOS X :: 10.8  (Mountain Lion) ",
        "Operating System :: MacOS :: MacOS X :: 10.9  (Mavericks) ",
        "Operating System :: MacOS :: MacOS X :: 10.10 (Yosemite) ",
        "Operating System :: MacOS :: MacOS X :: 10.11 (El Capitan) ",
##
##### CAUTION ##########################################################
##
##    From http://windows.microsoft.com/en-us/windows/end-support-help
##
##       "As of April 8, 2014, support and updates for Windows XP are
##        no longer available. Don"t let your PC go unprotected."
##
##       "How do I stay protected?
##        To stay protected now that support has ended, you have two
##        options:
##
##        Upgrade your current PC
##        Very few older computers are able to run Windows 10, which
##        is the latest version of Windows. We recommend that you check
##        out the Windows 10 specifications page to find out if your PC
##        meets the system requirements for Windows 10. For more detail-
##        ed information, read the FAQ.
##
##        Get a new PC
##        If your current PC can"t run Windows 10, it might be time to
##        consider shopping for a new one. Be sure to explore our great
##        selection of new PCs. They"re more powerful, lightweight, and
##        stylish than ever before -- and with an average price that"s
##        considerably less expensive than the average PC was 12 years
##        ago."
##
########################################################################
##
        "Operating System :: Microsoft ",
        "Operating System :: Microsoft :: Windows ",
        "Operating System :: Microsoft :: Windows :: Windows XP  (CLI mode only) ",
        "Operating System :: Microsoft :: Windows :: Windows 7   (CLI mode only) ",
        "Operating System :: Microsoft :: Windows :: Windows 8   (CLI mode only) ",
        "Operating System :: Microsoft :: Windows :: Windows 10  (CLI mode only) ",
##
        "Operating System :: POSIX ",
        "Operating System :: POSIX :: AIX (NOT tested) ",
        "Operating System :: POSIX :: BSD (NOT tested) ",
        "Operating System :: POSIX :: BSD :: BSD/OS (NOT tested) ",
        "Operating System :: POSIX :: BSD :: FreeBSD (NOT tested) ",
        "Operating System :: POSIX :: BSD :: NetBSD (NOT tested) ",
        "Operating System :: POSIX :: BSD :: OpenBSD (NOT tested) ",
        "Operating System :: POSIX :: CYGWIN ",
        "Operating System :: POSIX :: CYGWIN :: Windows XP ",
        "Operating System :: POSIX :: CYGWIN :: Windows 7 ",
        "Operating System :: POSIX :: CYGWIN :: Windows 8 ",
        "Operating System :: POSIX :: CYGWIN :: Windows 10 ",
        "Operating System :: POSIX :: GNU Hurd (NOT tested) ",
        "Operating System :: POSIX :: HP-UX (NOT tested) ",
        "Operating System :: POSIX :: IRIX (NOT tested) ",
        "Operating System :: POSIX :: Linux ",
        "Operating System :: POSIX :: Linux :: CentOS 7 (Red Hat) ",
        "Operating System :: POSIX :: Linux :: Debian 8 ",
        "Operating System :: POSIX :: Linux :: Fedora 23 (Red Hat) ",
        "Operating System :: POSIX :: Linux :: OpenSUSE 13 ",
        "Operating System :: POSIX :: Linux :: Scientific 7 (Red Hat) ",
        "Operating System :: POSIX :: Linux :: Ubuntu 12.04 LTS ",
        "Operating System :: POSIX :: Linux :: Ubuntu 14.04 LTS ",
        "Operating System :: POSIX :: Linux :: Ubuntu 15.10 ",
        "Operating System :: POSIX :: Unix ",
        "Operating System :: POSIX :: Unix :: BSD :: BSD/OS (NOT tested) ",
        "Operating System :: POSIX :: Unix :: BSD :: FreeBSD 11.0  (CLI mode only) ",
        "Operating System :: POSIX :: Unix :: BSD :: PC-BSD 11.0 ",
        "Operating System :: POSIX :: Unix :: Solaris (NOT tested) ",
        "Operating System :: POSIX :: Unix :: Solaris :: OpenIndiana 151.a8 ",
        "Operating System :: POSIX :: Unix :: Solaris :: OpenSolaris 11 ",
        "Operating System :: POSIX :: Unix :: SunOS (NOT tested) ",
##
##        "Operating System :: Microsoft :: Windows :: XP  (CLI mode only) ",
##        "Operating System :: POSIX :: CYGWIN :: Windows XP ",
##        "Operating System :: BeOS ",
##        "Operating System :: MacOS ",
##        "Operating System :: MacOS :: MacOS 9 ",
##        "Operating System :: Microsoft ",
##        "Operating System :: Microsoft :: MS-DOS ",
##        "Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier ",
##        "Operating System :: Microsoft :: Windows :: Windows 95/98/2000 ",
##        "Operating System :: Microsoft :: Windows :: Windows CE ",
##        "Operating System :: Microsoft :: Windows :: Windows NT/2000 ",
##        "Operating System :: Microsoft :: Windows :: Windows Server 2003 ",
##        "Operating System :: Microsoft :: Windows :: Windows Server 2008 ",
##        "Operating System :: Microsoft :: Windows :: Windows Vista ",
##        "Operating System :: Microsoft :: Windows ",
##        "Operating System :: OS Independent ",
##        "Operating System :: OS/2 ",
##        "Operating System :: Other OS ",
##        "Operating System :: PalmOS ",
##        "Operating System :: PDA Systems ",
##        "Operating System :: POSIX :: AIX ",
##        "Operating System :: POSIX :: BSD ",
##        "Operating System :: POSIX :: BSD :: BSD/OS ",
##        "Operating System :: POSIX :: BSD :: FreeBSD ",
##        "Operating System :: POSIX :: BSD :: NetBSD ",
##        "Operating System :: POSIX :: BSD :: OpenBSD ",
##        "Operating System :: POSIX :: GNU Hurd ",
##        "Operating System :: POSIX :: HP-UX ",
##        "Operating System :: POSIX :: IRIX ",
##        "Operating System :: POSIX :: Other ",
##        "Operating System :: POSIX :: SCO ",
##        "Operating System :: POSIX :: Solaris ",
##        "Operating System :: POSIX :: SunOS ",
##
        "Programming Language :: Python ",
        "Programming Language :: Python :: 2 ",
        "Programming Language :: Python :: 2.0 (CLI mode only) ",
        "Programming Language :: Python :: 2.1 (CLI mode only) ",
        "Programming Language :: Python :: 2.2 (CLI mode only) ",
        "Programming Language :: Python :: 2.3 (CLI mode only) ",
        "Programming Language :: Python :: 2.4 (CLI mode only) ",
        "Programming Language :: Python :: 2.5 (CLI mode only) ",
        "Programming Language :: Python :: 2.6 ",
        "Programming Language :: Python :: 2.7 ",
        "Programming Language :: Python :: 3 ",
        "Programming Language :: Python :: 3.0 ",
        "Programming Language :: Python :: 3.0 (CLI mode only) ",
        "Programming Language :: Python :: 3.1 ",
        "Programming Language :: Python :: 3.2 ",
        "Programming Language :: Python :: 3.3 ",
        "Programming Language :: Python :: 3.4 ",
        "Programming Language :: Python :: 3.5 ",
##
        "Topic :: Education ",
        "Topic :: Education :: Software Engineering ",
        "Topic :: Education :: System Engineering ",
        "Topic :: Software Development ",
        "Topic :: Software Development :: Embedded Systems ",
        "Topic :: Software Development :: Libraries :: Python Modules ",
        "Topic :: Software Development :: Widget Sets ",
        "Topic :: System :: Distributed Computing ",
        "Topic :: Documentation ",
        "Topic :: Education ",
        "Topic :: Education :: Software Engineering ",
        "Topic :: Education :: System Engineering ",
        "Topic :: Software Development :: User Interfaces ",
        "Topic :: Software Development :: Widget Sets ",
        "Topic :: System :: Distributed Computing ",
        "Topic :: Utilities "
        ],

##
    platforms = [
        "Mobile Phone",
        "Tablet Computer",
        "Laptop Computer",
        "Desktop Computer",
        "Super Computer",
        "Embedded System",
        "HOST CPU with 32-bit/64-bit processor ",
        "Host  OS with Multi-User, Multi-Process and Multi-Threaded features ",
        "Command Line Interface shells (POSIX-type `bash`, `sh`) ",
        "Command Line Interface shells (Microsoft-type `command prompt`) ",
        "Graphical User Interface (wxPython-style `text user interface`) ",
        "Remote Command Line Interface shells (`ssh`, `rsh`, `sftp`, `ftp`) ",
        "Python Virtual Machine with Python Run Time Library modules ",
        "Curses/nCurses Terminal Control Library for POSIX-like systems ",
        "Non-Color Console/Terminal/Emulator (mouse with vt100/vt220) ",
        "8-Color   Console/Terminal/Emulator (mouse with cygwin mintty) ",
        "8-Color   Console/Terminal/Emulator (mouse with xterm/xterm-color) ",
        "16-Color  Console/Terminal/Emulator (mouse with xterm-16color) ",
        "16-Color  Console/Terminal/Emulator (mouse with xterm-88color) ",
        "16-Color  Console/Terminal/Emulator (mouse with xterm-256color)"
        ],
##

##    # packages=find_packages(),
##    packages = list(find_packages(mypackage.__path__,
##                                mypackage.__name__)),
##    include_package_data = True,
##    zip_safe = False,

##    package_data={"tsWxGTUI": ["license.txt"]},
##    package_data={"Usage_Terms_and_Conditions": [
##        "Usage_Terms_and_Conditions/COPYRIGHT.txt ",
##        "Usage_Terms_and_Conditions/LICENSE.txt ",
##        "Usage_Terms_and_Conditions/NOTICES.txt "]
##                  },
##    include_package_data=True,

)
