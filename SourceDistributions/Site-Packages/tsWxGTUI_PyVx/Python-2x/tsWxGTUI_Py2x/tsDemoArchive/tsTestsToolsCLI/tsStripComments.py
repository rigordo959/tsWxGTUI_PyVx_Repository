#! /usr/bin/env python
#"Time-stamp: <03/10/2015  4:13:15 AM rsg>"
'''
tsStripCommentsts.py - Python application program to transform an
annotated, development version of a directory of sub-directories
and Python source files into an unannotated copy. The copy is
intended to conserve storage space when installed in an embedded
system. The transformation involves stripping comments and doc
strings by de-tokenizing a tokenized version of each Python
source file. Non-Python files are trimmed of trailing whitespace.
'''
#################################################################
#
# File: tsStripComments.py
#
# Purpose:
#
#     Python application program to transform an annotated,
#     development version of a directory of sub-directories
#     and Python source files into an unannotated copy. The
#     copy is intended to conserve storage space when installed
#     in an embedded system. The transformation involves strip-
#     ping comments and doc strings by de-tokenizing a tokenized
#     version of each Python source file. Non-Python files are
#     trimmed of trailing whitespace.
#
# Limitations:
#
#     1. Transforms only files who's name ends with '.py'. Copies
#        all other file objects (symlinks, directories, shell
#        scripts, configuration files, text files etc.).
#
#     2. Directory INPUT must currently exist.
#
#     3. Directory OUTPUT must NOT currently exist.
#
#     4. There must be no mixture of tab and blank space characters
#        in order for the stripped OUTPUT file to be executable
#        without "IndentationError". This can be accomplished by:
#
#        a) using Xemacs to edit each INPUT file
#        b) using the Edit menu to "Select All"
#        c) using the Cmds menu to "Execute Name Command" "untabify".
#        d) using the Save tool.
#
#
# Usage (examples):
#
#     python tsStripComments.py -i INPUT -o OUTPUT
#
# Notes:
#
#     The tsStripComents module originally used the static methods/
#     functions associated with the standard Python shutil module,
#     including an enhanced version of copyfile.
#
#     Modified versions of those static methods/functions are now
#     incorporated as instance methods/functions associated with
#     the TsShutil class. This encapsulation enables inheritance.
#     Inheritance facilitates access to an application-wide event
#     logger (tsLogger). Logging not only captured, time-stamped
#     and categorized error, warning and debug messages, but it
#     eliminated the need for conditionalized print statements.
#
# Methods:
#
#     Error - EnvironmentError Stub
#
#     TsShutil - Utility functions for copying and archiving files
#           and directory trees.
#
#     TsShutil.__init__ - Class constructor
#
#     TsShutil._basename - A basename() variant which first strips
#           the trailing slash, if present.
#
#     TsShutil._destinsrc - Function, used only by move, It detects
#           inappropriate move of a directory into itself.
#
#     TsShutil._ignore_patterns - Function that can be used as
#           copytree() ignore parameter.
#
#     TsShutil._samefile - Function to check if src and dst are one
#           and the same.
#
#     TsShutil.copy - Copy data and mode bits ("cp src dst").
#
#     TsShutil.copy2 - Copy data and all stat info ("cp -p src dst").
#
#     TsShutil.copyfile - Copy data from src to dst
#
#     TsShutil.copyfileobj - Copy data from file-like object fsrc
#           to file-like object fdst.
#
#     TsShutil.copymode - Copy mode bits from src to dst.
#
#     TsShutil.copystat - Copy all stat info (mode bits, atime,
#           mtime, flags) from src to dst.
#
#     TsShutil.copytree - Recursively copy a directory tree using copy2().
#
#     TsShutil.move - Recursively move a file or directory to another
#           location. This is similar to the Unix "mv" command.
#
#     TsShutil.onerror - Handler if ignore_errors
#
#     TsShutil.onerror - Handler if onerror is None
#
#     TsShutil.remove_comments_and_docstrings - Returns "source" minus
#           comments and docstrings.
#
#     TsShutil.replaceComments - Create a filtered copy of the designated
#           input file to the designated output file such that there will
#           be no comments or doc strings.
#
#     TsShutil.replaceLine - Create a filtered copy of the designated
#           input file to the designated output file such that there
#           will be no lines having superfluous trailing white space.
#
#     TsShutil.rmtree - Recursively delete a directory tree.
#
#     TsShutil.strip_documentation - Remove blank lines before updating
#           destination.
#
#     TsShutil.trimWhiteSpace - Identify and remove superfluous white
#           space from end of the given string.
#
#     TsStripComments - Class to transform an annotated, development
#           version of a directory of sub-directories and Python source
#           files into an unannotated copy.
#
#     TsStripComments.EntryPoint -
#
#     TsStripComments.__init__ - Class constructor.
#
#     TsStripComments.exitTest - Terminate application with appropriate
#           normal or eror exit code and messange.
#
#     TsStripComments.getSettings - Parse command line and extract any
#           keyword-value pair options and positional arguments.
#
# Modifications:
#
#     2013/07/29 rsg Derived directory tree copying code from
#                    tsTreeTrimLinesPkg.
#
#     2013/07/30 rsg Created TsShutil class to encapsulate
#                    instance methods/function based on
#                    associated static ones of the standard
#                    Python shutil module.
#
#     2013/08/20 rsg Added Limitation #4 regarding avoidance of
#                    "IndentationError" during execution.
#
#     2013/08/22 rsg Added logic to strip_documentation that
#                    exempts first of multiple blank lines
#                    from deletion. This is intended to improve
#                    readability and fix problem with doc string
#                    style quotes referenced by
#                    tsOperatorSettingsParser-type modules.
#
#     2013/08/22 rsg Determined why logic to strip_documentation
#                    that exempts first of multiple blank lines
#                    not fix run time trap by test applications.
#                    However, since unstripped version of test
#                    applications do NOT trap, this implies that
#                    stripped building block modules are OK and
#                    that the problem is associated with the
#                    deletion of those doc strings in the
#                    launched module that are required by the
#                    tsOperatorSettingsParser-type module in
#                    order to build run time help.
#
# ToDo:
#
#
#################################################################

__title__     = 'tsStripComents.py'
__version__   = '1.2.1'
__date__      = '08/27/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
    '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
    'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  Python Logging and Shutil Modules API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  Remove Comments and Docstrings Method: ' + \
                '\n\t  Copyright (c) 2009 Dan McDougall ' + \
                'on StackOverflow.com.' + \
                '\n\t\t\tAll rights reserved.'

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

#--------------------------------------------------------------------------

## import thread
## import time
## import traceback
import cStringIO
import collections
import errno
import fnmatch
import math
import os
import os.path
import platform
import stat
import sys
import tokenize
# from os.path import abspath

try:
    from pwd import getpwnam
except ImportError:
    getpwnam = None

try:
    from grp import getgrnam
except ImportError:
    getgrnam = None

##__all__ = ["copyfileobj", "copyfile", "copymode", "copystat", "copy", "copy2",
##           "copytree", "move", "rmtree", "Error", "SpecialFileError",
##           "ExecError", "make_archive", "get_archive_formats",
##           "register_archive_format", "unregister_archive_format",
##           "ignore_patterns"]

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py2x.tsLibCLI import tsCommandLineEnv

CommandLineEnv = tsCommandLineEnv.CommandLineEnv

#--------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsToolsLibCLI import tsStripSettingsParser

#--------------------------------------------------------------------------

__all__ = ['copyfileobj','copyfile','copymode','copystat','copy','copy2',
           'copytree','move','rmtree','Error']

#--------------------------------------------------------------------------

DEBUG    = False  # Enables log with debugging details
SCAN_LOG = False  # Enables log with line by line scan parsing details
VERBOSE  = False  # Enables log with redirected output details

myOptions = None
argParseCreated = '2.7.0'
optParseCreated = '2.3.0'
optParseDeprecated = argParseCreated
platformVersion = str(platform.python_version())

##if DEBUG:
##    # Import wingdbstub only if cygwin platform.
##    hostOS = platform.system().lower()
##    if (hostOS.find('cygwin') != -1):
##        try:
##            import wingdbstub
##        except ImportError:
##            pass

sourceCodeExtensions = ['.py']

#--------------------------------------------------------------------------

class Error(EnvironmentError):
    pass

try:
    WindowsError
except NameError:
    WindowsError = None

#--------------------------------------------------------------------------

class TsShutil(object):
    '''
    Utility functions for copying and archiving files and directory
    trees. Class instance methods/function are based on associated
    static ones of the standard Python shutil module.

    NOTE: The functions here do not copy the resource fork or other
    metadata on Mac.
    '''

    #----------------------------------------------------------------------

    def __init__(self):
        '''
        Constructor.
        '''
        pass

    #----------------------------------------------------------------------

    def _basename(self, path):
        '''
        A basename() variant which first strips the trailing slash,
        if present.

        Thus we always get the last component of the path, even for
        directories.
        '''
        return os.path.basename(path.rstrip(os.path.sep))

    #----------------------------------------------------------------------

    def _destinsrc(self, src, dst):
        '''
        Function, used only by move, It detects inappropriate move of
        a directory into itself.
        '''
        src = abspath(src)
        dst = abspath(dst)
        if not src.endswith(os.path.sep):
            src += os.path.sep
        if not dst.endswith(os.path.sep):
            dst += os.path.sep
        return dst.startswith(src)

    #----------------------------------------------------------------------

    def _ignore_patterns(self, *patterns):
        '''
        Function that can be used as copytree() ignore parameter.

        Patterns is a sequence of glob-style patterns
        that are used to exclude files
        '''
        def _ignore_patterns(path, names):
            ignored_names = []
            for pattern in patterns:
                ignored_names.extend(fnmatch.filter(names, pattern))
            return set(ignored_names)
        return _ignore_patterns

    #----------------------------------------------------------------------

    def _samefile(self, src, dst):
        '''
        Function to check if src and dst are one and the same.
        '''
        # Macintosh, Unix.
        if hasattr(os.path,'samefile'):
            try:
                return os.path.samefile(src, dst)
            except OSError:
                return False

        # All other platforms: check for same pathname.
        return (os.path.normcase(os.path.abspath(src)) ==
                os.path.normcase(os.path.abspath(dst)))

    #----------------------------------------------------------------------

    def copy(self, src, dst):
        '''
        Copy data and mode bits ("cp src dst").

        The destination may be a directory.
        '''
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        self.copyfile(src, dst)
        self.copymode(src, dst)

    #----------------------------------------------------------------------

    def copy2(self, src, dst):
        '''
        Copy data and all stat info ("cp -p src dst").

        The destination may be a directory.
        '''
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        self.copyfile(src, dst)
        self.copystat(src, dst)

    #----------------------------------------------------------------------

    def copyfile(self, src, dst):
        '''
        Copy data from src to dst
        '''
        if self._samefile(src, dst):
            raise Error, "`%s` and `%s` are the same file" % (src, dst)

        strippedCopy = False
        if not os.path.islink(src) and \
           not os.path.isdir(src):

            noticeDirectory = '/tmp/notices'
            for sourceCodeExtension in sourceCodeExtensions:
                if src.lower().endswith(sourceCodeExtension.lower()):

                    strippedCopy = True

                    if src.lower().endswith('.py'):

                        service = 'StripComments'

                        self.logger.debug(
                        'copyfile:Propose service "%s" on file = "%s"' % (
                            service, src))

                        (changed,
                         totalCharacters,
                         totalLines) = self.replaceComments(
                             src,
                             dst,
                             noticeDirectory)

                    if DEBUG:
                        if changed:
                            print(
                                ' CHANGED %d-chars %d-lines %s' % (
                                    totalCharacters,
                                    totalLines,
                                    src))
                            self.logger.debug(
                                'copyfile: CHANGED %d-chars %d-lines %s' % (
                                    totalCharacters,
                                    totalLines,
                                    src))
                        else:
                            print(
                                '         %d-chars %d-lines %s' % (
                                    totalCharacters,
                                    totalLines,
                                    src))
                            self.logger.debug(
                                'copyfile:         %d-chars %d-lines %s' % (
                                    totalCharacters,
                                    totalLines,
                                    src))

                    else:
                        if changed:
                            print(' CHANGED %s' % src)
                            self.logger.debug(
                            'copyfile: CHANGED %s' % src)
                        else:
                            print('         %s' % src)
                            self.logger.debug(
                            'copyfile:         %s' % src)

        if not strippedCopy:

            fsrc = None
            fdst = None
            try:
                fsrc = open(src, 'rb')
                fdst = open(dst, 'wb')
                self.copyfileobj(fsrc, fdst)
            finally:
                if fdst:
                    fdst.close()
                if fsrc:
                    fsrc.close()

            print('  cloned %s' % src)
            self.logger.debug('copyfile:  cloned %s' % src)

    #----------------------------------------------------------------------

    def copyfileobj(self, fsrc, fdst, length=16*1024):
        '''
        Copy data from file-like object fsrc to file-like object fdst.
        '''
        while True:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)

    #----------------------------------------------------------------------

    def copymode(self, src, dst):
        '''
        Copy mode bits from src to dst.
        '''
        if hasattr(os, 'chmod'):
            st = os.stat(src)
            mode = stat.S_IMODE(st.st_mode)
            os.chmod(dst, mode)

    #----------------------------------------------------------------------

    def copystat(self, src, dst):
        '''
        Copy all stat info (mode bits, atime, mtime, flags) from src to dst.
        '''
        st = os.stat(src)
        mode = stat.S_IMODE(st.st_mode)
        if hasattr(os, 'utime'):
            os.utime(dst, (st.st_atime, st.st_mtime))
        if hasattr(os, 'chmod'):
            os.chmod(dst, mode)
        if hasattr(os, 'chflags') and hasattr(st, 'st_flags'):
            os.chflags(dst, st.st_flags)

    #----------------------------------------------------------------------

    def copytree(self, src, dst, symlinks=False, ignore=None):
        '''
        Recursively copy a directory tree using copy2().

        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.

        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied.

        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():

            callable(src, names) -> ignored_names

        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.

        XXX Consider this example code rather than the ultimate tool.
        '''
        names = os.listdir(src)
        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()

        os.makedirs(dst)
        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    self.copytree(srcname, dstname, symlinks, ignore)
                else:
                    self.copy2(srcname, dstname)
                # XXX What about devices, sockets etc.?
            except (IOError, os.error), why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Error, err:
                print(
                    'ERROR: name="%s"; err="%s"' %(name, str(err.args[0])))
                self.logger.error(
                    'copytree: name="%s"; err="%s"' %(name, str(err.args[0])))
                errors.extend(err.args[0])
                exit(0)
        try:
            self.copystat(src, dst)
        except OSError, why:
            if WindowsError is not None and isinstance(why, WindowsError):
                # Copying file access times may fail on Windows
                pass
            else:
                errors.extend((src, dst, str(why)))
        if errors:
            raise Error, errors

    #----------------------------------------------------------------------

    def move(self, src, dst):
        '''
        Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command.

        If the destination is a directory or a symlink to a directory, the
        source is moved inside the directory. The destination path must not
        already exist.

        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.

        If the destination is on our current filesystem, then rename() is
        used. Otherwise, src is copied to the destination and then removed.
        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.
        '''
        real_dst = dst
        if os.path.isdir(dst):
            real_dst = os.path.join(dst, _basename(src))
            if os.path.exists(real_dst):
                raise Error, \
                      "Destination path '%s' already exists" % real_dst
        try:
            os.rename(src, real_dst)
        except OSError:
            if os.path.isdir(src):
                if self._destinsrc(src, dst):
                    raise Error, \
                          "Cannot move a directory " + \
                          "'%s' into itself '%s'." % (src, dst)
                self.copytree(src, real_dst, symlinks=True)
                self.rmtree(src)
            else:
                self.copy2(src, real_dst)
                os.unlink(src)

    #----------------------------------------------------------------------

    def remove_comments_and_docstrings(self, source):
        '''
        From: http://stackoverflow.com/questions/1769332/
                     script-to-remove-python-comments-docstrings

        Returns "source" minus comments and docstrings.

        I am leaving stub comments in the place of docstrings and comments
        since it simplifies the code. If you remove them completely, you
        also have to get rid of indentation before them.
        '''
        io_obj = cStringIO.StringIO(source)
        out = ""
        prev_toktype = tokenize.INDENT
        last_lineno = -1
        last_col = 0
        for tok in tokenize.generate_tokens(io_obj.readline):
            token_type = tok[0]
            token_string = tok[1]
            start_line, start_col = tok[2]
            end_line, end_col = tok[3]
            ltext = tok[4]
            # The following two conditionals preserve indentation.
            # This is necessary because we're not using tokenize.untokenize()
            # (because it spits out code with copious amounts of oddly-placed
            # whitespace).
            if start_line > last_lineno:
                last_col = 0
            if start_col > last_col:
                out += (" " * (start_col - last_col))
            # Remove comments:
            if token_type == tokenize.COMMENT:
                pass
            # This series of conditionals removes docstrings:
            elif token_type == tokenize.STRING:
                if prev_toktype != tokenize.INDENT:
                    # This is likely a docstring; double-check we're not
                    # inside an operator:
                    if prev_toktype != tokenize.NEWLINE:
                        # Note regarding NEWLINE vs NL: The tokenize module
                        # differentiates between newlines that start a new
                        # statement
                        #
                        # and newlines inside of operators such as parens,
                        # brackes, and curly braces.  Newlines inside of
                        # operators are NEWLINE and newlines that start
                        # new code are NL.
                        #
                        # Catch whole-module docstrings:
                        if start_col > 0:
                            # Unlabelled indentation means we're inside
                            # an operator
                            out += token_string
                        # Note regarding the INDENT token: The tokenize
                        # module does not label indentation inside of
                        # an operator (parens, brackets, and curly braces)
                        # as actual indentation.
                        #
                        # For example:
                        #
                        # def foo():
                        #     "The spaces before this docstring are
                        #     tokenize.INDENT"
                        #     test = [
                        #         "The spaces before this string do not get a
                        #         token"
                        #     ]
            else:
                out += token_string
            prev_toktype = token_type
            last_col = end_col
            last_lineno = end_line
        return (out)

    #----------------------------------------------------------------------

    def replaceComments(self, inputName, outputName, noticeDirectory):
        '''
        Create a filtered copy of the designated input file to the designated
        output file such that there will be no comments or doc strings.
        '''
        try:

            inputFile = open(inputName, 'r')

        except Exception, e:

            print('replaceComments: Exception, e=%s' % e)
            self.logger.error('replaceComments: Exception, e=%s' % e)
            if os.path.islink(inputName):

                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
                self.logger.warning(
                    'replaceComments: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))

            else:

                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    inputName)
                self.logger.warning(
                    'replaceComments: Unknown Access Issue with\n    %s\n' % \
                    inputName)

        try:

            totalInputCharacters = 0
            totalInputLines = 0
            for line in inputFile:

                totalInputCharacters += len(line)
                totalInputLines += 1

        except:

            if os.path.islink(inputName):

                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
                self.logger.warningg(
                    'replaceComments: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))

            else:

                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    inputName)
                self.logger.warning(
                    'replaceComments: Unknown Access Issue with\n    %s\n' % \
                    inputName)

        self.strip_documentation(
            inputName,
            outputName)

        changed = False

        try:

            outputFile = open(outputName, 'r')

        except Exception, e:

            self.logger.debug('Exception: e=%s' % e)
            if os.path.islink(outputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (outputName, link))
                self.logger.warning(
                    'replaceComments: Broken Link Issue with\n    %s->%s\n' % \
                    (outputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    outputName)
                self.logger.warning(
                    'replaceComments: Unknown Access Issue with\n    %s\n' % \
                    outputName)

        try:

            totalOutputCharacters = 0
            totalOutputLines = 0
            for line in outputFile:

                totalOutputCharacters += len(line)
                totalOutputLines += 1

        except:

            if os.path.islink(inputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
                self.logger.warning(
                    'replaceComments: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    inputName)
                self.logger.warning(
                    'replaceComments: Unknown Access Issue with\n    %s\n' % \
                    inputName)

        if totalInputCharacters != totalOutputCharacters:

            changed = True

        return (changed, totalOutputCharacters, totalOutputLines)

    #----------------------------------------------------------------------

    def replaceLine(self, inputName, outputName, noticeDirectory):
        '''
        Create a filtered copy of the designated input file to the designated
        output file such that there will be no lines having superfluous
        trailing white space.
        '''
        try:
            inputFile = open(inputName, 'r')
        except Exception, e:
            print('Exception: e=%s' % e)
            self.logger.error('replaceLine: Exception: e=%s' % e)
            if os.path.islink(inputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
                self.logger.warning(
                    'replaceLine: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    inputName)
                self.logger.warning(
                    'replaceLine: Unknown Access Issue with\n    %s\n' % \
                    inputName)

        try:
            outputFile = open(outputName, 'w')
        except Exception, e:
            self.logger.debug('Exception: e=%s' % e)
            if os.path.islink(outputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (outputName, link))
                self.logger.warning(
                    'replaceLine: Broken Link Issue with\n    %s->%s\n' % \
                    (outputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    outputName)
                self.logger.warning(
                    'replaceLine: Unknown Access Issue with\n    %s\n' % \
                    outputName)

        changed = False

    ##    percentChangedLines = 0.0

    ##    percentChangedCharacters = 0.0

        try:
    ##        changedCharacters = 0
            totalCharacters = 0
    ##        changedLines = 0
            totalLines = 0
            for line in inputFile:
                totalCharacters += len(line)
                totalLines += 1
                trimmedText = '%s\n' % trimWhiteSpace(line)
                outputFile.write(trimmedText)

                if trimmedText != line:
    ##                changedLines += 1
    ##                changedCharacters += len(line) - len(trimmedText)
                    changed = True

    ##        percentChangedLines = 100.0 * float(changedLines) / float(totalLines)

    ##        percentChangedCharacters = 100.0 * float(changedCharacters) / \
    ##                                   float(totalCharacters)

        except:
            if os.path.islink(inputName):
                # Report Broken Symbolic Link to Named File.
                link = os.readlink(inputName)
                print(
                    '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
                self.logger.warning(
                    'replaceLine: Broken Link Issue with\n    %s->%s\n' % \
                    (inputName, link))
            else:
                # Report Unknown Access Issue to Named File.
                print(
                    '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                    inputName)
                self.logger.warning(
                    'replaceLine: Unknown Access Issue with\n    %s\n' % \
                    inputName)

        return (changed, totalCharacters, totalLines)

    #----------------------------------------------------------------------

    def rmtree(self, path, ignore_errors=False, onerror=None):
        '''
        Recursively delete a directory tree.

        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.
        '''
        if ignore_errors:

            def onerror(*args):
                '''
                ignore_errors
                '''
                pass

        elif onerror is None:

            def onerror(*args):
                '''
                onerror is None
                '''
                raise
        try:

            if os.path.islink(path):
                # symlinks to directories are forbidden, see bug #1669
                raise OSError("Cannot call rmtree on a symbolic link")

        except OSError:

            onerror(os.path.islink, path, sys.exc_info())
            # can't continue even if onerror hook returns
            return

        names = []
        try:

            names = os.listdir(path)

        except os.error, err:

            onerror(os.listdir, path, sys.exc_info())

        for name in names:

            fullname = os.path.join(path, name)

            try:
                mode = os.lstat(fullname).st_mode
            except os.error:
                mode = 0

            if stat.S_ISDIR(mode):

                self.rmtree(fullname, ignore_errors, onerror)

            else:

                try:
                    os.remove(fullname)
                except os.error, err:
                    onerror(os.remove, fullname, sys.exc_info())

        try:
            os.rmdir(path)
        except os.error:
            onerror(os.rmdir, path, sys.exc_info())

    #-----------------------------------------------------------------------

    def strip_documentation(self, source, target):
        '''
        Remove blank lines before updating destination.
        '''
        try:
            targetID = open(target, 'w')
        except Exception, errorCode:
            msg = str(errorCode)
            errorName = tse.USER_INTERFACE_EXCEPTION
            raise tse.ProgramException(errorName, msg)
        sourceID = open(source, 'r')
        buffer1 = ''
        for line in sourceID:
            buffer1 += line
        sourceID.close()
        buffer2 = self.remove_comments_and_docstrings(buffer1)
        buffer3 = buffer2.split('\n')
        buffer4 = ''
        for line in buffer3:
            buffer4 += line.rstrip() + '\n'

        buffer5 = buffer4.split('\n')
        buffer6 = ''
        for line in buffer5:
            newLine = line.rstrip()
            if len(newLine) > 0:
                buffer6 += newLine + '\n'
            else:
                buffer6 += '\n'

        buffer7 = buffer6.split('\n')
        savedFirstBlankLine = False
        for line in buffer7:
            if len(line.rstrip()) > 0:
                # register non-blank line
                savedFirstBlankLine = False
                targetID.write(line.rstrip() + '\n')
            elif savedFirstBlankLine:
                # Ignore consecutive blank lines.
                pass
            else:
                # register first blank line
                savedFirstBlankLine = True
                targetID.write('\n')

        targetID.close()
        self.copymode(source, target)

    #----------------------------------------------------------------------

    def trimWhiteSpace(self, string):
        '''
        Identify and remove superfluous white space from end of the given
        string. White space consists of the following characters:
        space [" "] and new line ["\n"].
        '''
        try:

            text = string.replace('\n', '')
            textLength = len(text)

            if textLength == 0:

                return text

            else:

                for i in range(0, textLength):

                    lastChar = textLength - i
                    nextChar = lastChar - 1
                    firstChar = 0

                    if nextChar == 0 or text[nextChar:lastChar] != ' ':

                        return text[firstChar:lastChar]

        except Exception, e:

            print('Exception: e=%s' % e)
            self.logger.error('trimWhiteSpace: Exception: e=%s' % e)

#--------------------------------------------------------------------------

class TsStripComments(tsStripSettingsParser.TsStripSettingsParser,
                      TsShutil):
    '''
    Class to transform an annotated, development version of a directory
    of sub-directories and Python source files into an unannotated copy.
    The copy is intended to conserve storage space when installed in an
    embedded system. The transformation involves stripping comments and
    doc strings by de-tokenizing a tokenized version of each Python
    source file. Non-Python files are trimmed of trailing whitespace.
    '''

    #----------------------------------------------------------------------

    def __init__(self):
        '''
        Display program name, version and date. Receive and validate
        command line options and arguments. Display help, error and
        status information. Initiate the transformation.
        '''
        tsStripSettingsParser.TsStripSettingsParser.__init__(self)
        TsShutil.__init__(self)

#--------------------------------------------------------------------------

if __name__ == '__main__':

    #----------------------------------------------------------------------

    def exitTest():
        '''
        Terminate application with appropriate normal or eror exit code
        and messange.
        '''
        exceptionName = tse.INPUT_OUTPUT_EXCEPTION
        errorName = 'Oops! Invalid Name'

        myLogger = Logger.TsLogger(threshold=Logger.DEBUG,
                                   name='exitTest')

        message = 'Exit Test'

        myLogger.debug('***** Exit Test %s / %s *****' % (
            exceptionName, errorName))
        raise tse.InputOutputException(errorName, message)

    #----------------------------------------------------------------------

    def getSettings(*args, **kw):
        '''
        Parse command line and extract any keyword-value pair options and
        positional arguments.
        '''
        myParser =  tsStripSettingsParser.TsStripSettingsParser()
        print('\n%s\n' % myParser.getRunTimeTitleVersionDate())

        rawArgsOptions = sys.argv[1:]
        print('\trawArgsOptions=%s' % str(rawArgsOptions))
        maxArgs = len(rawArgsOptions)

        (args, options) = myParser.parseCommandLineDispatch()

        print('type(args=%s)=%s' % (str(args), type(args)))
        print('type(options=%s)=%s' % (str(options), type(options)))

        if True or DEBUG:
            label = myParser.getRunTimeTitle()

            fmt1 = '%s.getSettings (parameter list): ' % label
            fmt2 = 'args=%s;\n\t\tkw=%s' % (str(args), str(kw))
            print('\n\t%s\n\t\t%s' % (fmt1, fmt2))

            fmt1 = '%s.getSettings (command line argv): ' % label
            fmt2 = 'args=%s' % str(args)
            fmt3 = 'options (unsorted)=%s' % str(options)
            print('\n\t%s\n\t\t%s;\n\t\t%s' % (fmt1, fmt2, fmt3))

            fmt1 = '\n\t%s.getSettings (command line argv): ' % label
            fmt2 = '\n\t\targs (positional) =%s' % str(args)
            keys = sorted(options.keys())
            text = ''
            for key in keys:
                try:
                    value = '"%s"' % options[key]
                except Exception, errorCode:
                    value = ''
                if text == '':
                    text = '{\n\t\t\t%s: %s' % (str(key), str(value))
                else:
                    text += ', \n\t\t\t%s: %s' % (str(key), str(value))
            text += '}'
            fmt3 = '\n\t\toptions (sorted)= %s' % text
            msg = fmt1 + fmt2 + fmt3
            print(msg)

        return (args, options)

    #----------------------------------------------------------------------

    def EntryPoint(*args, **kw):
        '''
        Run-time entry point for the Python application.
        '''

        print('\n\n\tEntryPoint (parameters:\n\t\tArgs=%s;\n\t\tOptions=%s' % (
            str(args), str(kw)))

        print(__header__)

        # Must get command line positional and keyword arguments
        # before redirection of stdout and stderr to GUI display.
        (args, options) = getSettings()

        if DEBUG and VERBOSE:
            state = dir(self)
            for item in state:
                if item == 'options':
                    print('\t\t%s=%s' % (item, str(self.options)))
                elif item == 'args':
                    print('\t\t%s=%s' % (item, str(self.args)))
                else:
                    print('\t\t%s' % item)

        try:

            debug_log    = options['debug']
            input = options['input']
            output = options['output']
            scan_log = options['scan']
            verbose_log  = options['Verbose']

            if DEBUG and VERBOSE:
                print('\tdebug_log = "%s"' % str(debug_log))
                print('\tinput = "%s"' % str(input))
                print('\toutput = "%s"' % str(output))
                print('\tscan_log = "%s"' % str(scan_log))
                print('\tverbose_log = "%s"' % str(verbose_log))

        except Exception, errorCode:

            print('\tErrorCode (args, options) = "%s"' % str(errorCode))
            print('\t\targs = "%s"' % str(args))
            print('\t\toptions = "%s"' % str(options))
            sys.exit(2)

        symlinks = False
        myTransformer = TsStripComments()
        myTransformer.copytree(os.path.abspath(input),
                               os.path.abspath(output),
                               symlinks)

    #----------------------------------------------------------------------

    myApp = CommandLineEnv(
        buildTitle=__title__,
        buildVersion=__version__,
        buildDate=__date__,
        buildAuthors=__authors__,
        buildCopyright=__copyright__,
        buildLicense=__license__,
        buildCredits=__credits__,
        buildTitleVersionDate=mainTitleVersionDate,
        buildHeader=__header__,
        buildPurpose=__doc__,
        logs=[Logger.StandardOutputFile],
        enableDefaultCommandLineParser=True,
        runTimeEntryPoint=EntryPoint)

    myApp.Wrapper()
