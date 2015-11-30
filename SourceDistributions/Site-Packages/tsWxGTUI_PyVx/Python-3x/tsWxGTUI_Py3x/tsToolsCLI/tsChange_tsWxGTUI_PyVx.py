#! /usr/bin/env python
#"Time-stamp: <05/06/2015  6:08:11 AM rsg>"
'''
tsChange_tsWxGTUI_PyVx.py - Tool to generate a directory of
installable source files. It transforms the tsWxGTUI_PyVx
import identifier created by merging tsWxGTUI_Py2x changes
into a previous tsWxGTUI_Py3x.
'''
#################################################################
#
# File: tsChange_tsWxGTUI_PyVx.py.py
#
# Purpose:
#
#     Tool to generate a directory of installable source files.
#     It transforms the tsWxGTUI_PyVx import identifier created
#     by merging tsWxGTUI_Py2x changes into a previous
#     tsWxGTUI_Py3x.
#
# Limitations:
#
# Usage (example):
#
#    python tsChange_tsWxGTUI_PyVx.py -s -i source -o destination
#
# Modifications:
#
#   2015/04/24 rsg Original version derived from tsTreeTrimLines..
#
# ToDo:
#
#   1. TBD.
#
#################################################################

__title__     = 'tsChange_tsWxGTUI_PyVx.py.py'
__version__   = '1.0.0'
__date__      = '04/24/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier. ' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Logging Module API Features: ' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0'

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

import fnmatch
import os
import os.path
import stat
import sys
from optparse import OptionParser
from os.path import abspath

#--------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py3x.tsLibCLI import tsLogger as Logger
from tsWxGTUI_Py3x.tsLibCLI import tsCommandLineEnv

CommandLineEnv = tsCommandLineEnv.CommandLineEnv

#--------------------------------------------------------------------------

# Installable toolkit version to search for
# and version to be substituted

oldVersion = 'from tsWxGTUI_Py2x.'
newVersion = 'from tsWxGTUI_Py3x.' 

#--------------------------------------------------------------------------

def getOptions():
    '''
    Parse the command line and return a list of positional arguments
    and a dictionanary of keyword options.
    '''
    parser = OptionParser(usage='''\
    %prog [options]... source destination

    Copies a directory tree from the specified source to destination.
    ''')

    parser.add_option("-i", "--input",
                        action="store",
                        dest="input",
                        default="./",
                        type="string",
                        help="topLevel directory [default = ./]")

    parser.add_option("-o", "--output",
                        action="store",
                        dest="output",
                        default="../published",
                        type="string",
                        help="output directory [default = ../published]")

    parser.add_option("-n", "--notices",
                        action="store",
                        dest="noticeDirectory",
                        default="/tmp/notices",
                        type="string",
                        help="notice directory [default = ../notices]")

    parser.add_option("-s", "--symlinks",
                      action="store_true",
                      dest="symlinks",
                      default=False,
                      help="Copy symbolic links, if True, " + \
                      "or contents of linked files, if False " + \
                      "[default = False].")

    parser.add_option("-v", "--verbose",
                        action="store_true",
                        dest="verbose",
                        default=False,
                        help="print status messages to stdout [default = False]")

    (options, args) = parser.parse_args()
    print('getOptions: args=%s' % str(args))
    print('getOptions: options=%s' % str(options))
    if len(args) != 0:
        parser.print_help()
        sys.exit(1)

    return (args, options)

#--------------------------------------------------------------------------

def replaceMacros(inputName, outputName, noticeDirectory):
    '''
    It transforms the tsWxGTUI_PyVx import identifier created by
    merging tsWxGTUI_Py2x changes into a previous tsWxGTUI_Py3x.
    '''
    try:
        inputFile = open(inputName, 'r')
        outputFile = open(outputName, 'w')
    except:
        if os.path.islink(inputName):
            # Report Broken Symbolic Link to Named File.
            link = os.readlink(inputName)
            print(
                '  *** WARNING: Broken Link Issue with\n    %s->%s\n' \
                % (inputName, link))
        else:
            # Report Unknown Access Issue to Named File.
            print(
                '  *** WARNING: Unknown Access Issue with\n    %s\n' \
                % inputName)

    changed = False
    try:
        for line in inputFile:
        ##    print line
            if str(line).find(oldVersion) > -1:
                changed = True
                outputFile.write('%s' % line.replace(oldVersion,
                                                     newVersion))
            else:
                outputFile.write('%s' % line)
    except:
        if os.path.islink(inputName):
            # Report Broken Symbolic Link to Named File.
            link = os.readlink(inputName)
            print(
                '  *** WARNING: Broken Link Issue with\n    %s->%s\n' \
                % (inputName, link))
        else:
            # Report Unknown Access Issue to Named File.
            print(
                '  *** WARNING: Unknown Access Issue with\n    %s\n' \
                % inputName)

    return changed

#--------------------------------------------------------------------------

def getDirectoryData(inputDirectory, outputDirectory, noticeDirectory):
    '''
    Scan directory for files to be published.
    '''
    try:
        os.mkdir(outputDirectory)
    except OSError:
        pass

    sourceCodeExtension = '.py'
    for dirpath, dirnames, filenames in os.walk(inputDirectory):
        if dirnames is None:
            pass
        indent = dirpath.count(os.sep)
        header = 'Directory: %s' % dirpath
        print('\n%s%s' % ('    ' * indent, header))
        print('%s%s\n' % ('    ' * indent, '-' * len(header)))
        for name in filenames:
            if name.lower().endswith(sourceCodeExtension.lower()):
                inputName = os.path.join(dirpath, name)
                outputName = os.path.join(dirpath, outputDirectory, name)
                changed = replaceMacros(inputName,
                                        outputName,
                                        noticeDirectory)
                if changed:
                    print(' CHANGED', name)
                else:
                    print('        ', name)

#----------------------------------------------------------------------

def theMainApplication():
    '''
    Display program name, version and date. Receive and validate command
    line options and arguments. Display help, error and status
    information. Initiate the file directory copy.
    '''
    print(__header__)

    (myArgs, myOptions) = getOptions()
    print('theMainApplication: myArgs=%s' % str(myArgs))
    print('theMainApplication: myOptions=%s' % str(myOptions))

    mySource = myOptions.input
    myDestination = myOptions.output

    symlinks = myOptions.symlinks

    exitStatus = 0
    exitMsg = 'No Errors'

    if mySource == '':
        exitMsg = 'COMMAND LINE ERROR: ' \
                  'No Source specified.'
        exitStatus = tse.INVALID_ERROR_CODE

    elif myDestination == '':
        exitMsg = 'COMMAND LINE ERROR: ' \
                  'No Destination specified.'
        exitStatus = tse.INVALID_ERROR_CODE

    elif myDestination == mySource:
        exitMsg = 'COMMAND LINE ERROR: ' \
                  'Cannot use Source "%s" also for Destination.' % \
                  mySource
        exitStatus = tse.INVALID_ERROR_CODE

    if exitStatus == 0:
        copytree(os.path.abspath(mySource),
                 os.path.abspath(myDestination),
                 symlinks)
        print('\n  Completed. See "%s" for results.' % myDestination)

    else:
        print('\n  Aborted. See "%s" for results.' % myDestination)

        sys.stderr.write(exitMsg.replace("'", ""))
        sys.exit(exitStatus)

#--------------------------------------------------------------------------

__all__ = ["copyfileobj","copyfile","copymode","copystat","copy","copy2",
           "copytree","move","rmtree","Error"]

DEBUG = False

sourceCodeExtensions = [
    '.ada',
    '.asm',
    '.bash',
    '.bas',
    '.bat',
    '.c',
    '.c++',
    '.cpp',
    '.csh',
    '.dat',
    '.f',
    '.f77',
    '.for',
    '.ftn',
    '.g77',
    '.h',
    '.inc',
    '.ksh',
    '.pas',
    '.plm',
    '.py',
    '.pyx',
    '.sh',
    '.src',
    '.txt']

#--------------------------------------------------------------------------

class Error(EnvironmentError):
    pass

try:
    WindowsError
except NameError:
    WindowsError = None

#--------------------------------------------------------------------------

def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

#--------------------------------------------------------------------------

def _samefile(src, dst):
    # Macintosh, Unix.
    if hasattr(os.path,'samefile'):
        try:
            return os.path.samefile(src, dst)
        except OSError:
            return False

    # All other platforms: check for same pathname.
    return (os.path.normcase(os.path.abspath(src)) ==
            os.path.normcase(os.path.abspath(dst)))

#--------------------------------------------------------------------------

def copyfile(src, dst):
    """Copy data from src to dst"""
    if _samefile(src, dst):
        raise Error("`%s` and `%s` are the same file" % (src, dst))

    strippedCopy = False
    if not os.path.islink(src) and \
       not os.path.isdir(src):
 
        noticeDirectory = '/tmp/notices'
        for sourceCodeExtension in sourceCodeExtensions:
            if src.lower().endswith(sourceCodeExtension.lower()):
                strippedCopy = True

                # print('Propose stripping file = "%s"' % src)
                (changed,
                 totalCharacters,
                 totalLines) = replaceLine(src,
                                           dst,
                                           noticeDirectory)
                if DEBUG:
                    if changed:
                        print(
                            ' CHANGED %d-chars %d-lines %s' % (totalCharacters,
                                                               totalLines,
                                                               src))
                    else:
                        print(
                            '         %d-chars %d-lines %s' % (totalCharacters,
                                                               totalLines,
                                                               src))

                else:
                    if changed:
                        print(' CHANGED %s' % src)
                    else:
                        print('         %s' % src)

    if not strippedCopy:

        fsrc = None
        fdst = None
        try:
            fsrc = open(src, 'rb')
            fdst = open(dst, 'wb')
            copyfileobj(fsrc, fdst)
        finally:
            if fdst:
                fdst.close()
            if fsrc:
                fsrc.close()

        print('  cloned %s' % src)

#--------------------------------------------------------------------------

def copymode(src, dst):
    """Copy mode bits from src to dst"""
    if hasattr(os, 'chmod'):
        st = os.stat(src)
        mode = stat.S_IMODE(st.st_mode)
        os.chmod(dst, mode)

#--------------------------------------------------------------------------

def copystat(src, dst):
    """Copy all stat info (mode bits, atime, mtime, flags) from src to dst"""
    st = os.stat(src)
    mode = stat.S_IMODE(st.st_mode)
    if hasattr(os, 'utime'):
        os.utime(dst, (st.st_atime, st.st_mtime))
    if hasattr(os, 'chmod'):
        os.chmod(dst, mode)
    if hasattr(os, 'chflags') and hasattr(st, 'st_flags'):
        os.chflags(dst, st.st_flags)

#--------------------------------------------------------------------------

def copy(src, dst):
    """Copy data and mode bits ("cp src dst").

    The destination may be a directory.

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst)
    copymode(src, dst)

#--------------------------------------------------------------------------

def copy2(src, dst):
    """Copy data and all stat info ("cp -p src dst").

    The destination may be a directory.

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst)
    copystat(src, dst)

#--------------------------------------------------------------------------

def ignore_patterns(*patterns):
    """Function that can be used as copytree() ignore parameter.

    Patterns is a sequence of glob-style patterns
    that are used to exclude files"""
    def _ignore_patterns(path, names):
        ignored_names = []
        for pattern in patterns:
            ignored_names.extend(fnmatch.filter(names, pattern))
        return set(ignored_names)
    return _ignore_patterns

#--------------------------------------------------------------------------

def copytree(src, dst, symlinks=False, ignore=None):
    """Recursively copy a directory tree using copy2().

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

    """
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
                copytree(srcname, dstname, symlinks, ignore)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            print(
                'ERROR: name="%s"; err="%s"' %(name, str(err.args[0])))
            errors.extend(err.args[0])
            exit(0)
    try:
        copystat(src, dst)
    except OSError as why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

#--------------------------------------------------------------------------

def rmtree(path, ignore_errors=False, onerror=None):
    """Recursively delete a directory tree.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is false and onerror is None, an exception is raised.

    """
    if ignore_errors:
        def onerror(*args):
            pass
    elif onerror is None:
        def onerror(*args):
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
    except os.error as err:
        onerror(os.listdir, path, sys.exc_info())
    for name in names:
        fullname = os.path.join(path, name)
        try:
            mode = os.lstat(fullname).st_mode
        except os.error:
            mode = 0
        if stat.S_ISDIR(mode):
            rmtree(fullname, ignore_errors, onerror)
        else:
            try:
                os.remove(fullname)
            except os.error as err:
                onerror(os.remove, fullname, sys.exc_info())
    try:
        os.rmdir(path)
    except os.error:
        onerror(os.rmdir, path, sys.exc_info())

#--------------------------------------------------------------------------

def _basename(path):
    # A basename() variant which first strips the trailing slash, if present.
    # Thus we always get the last component of the path, even for directories.
    return os.path.basename(path.rstrip(os.path.sep))

#--------------------------------------------------------------------------

def move(src, dst):
    """Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command.

    If the destination is a directory or a symlink to a directory, the source
    is moved inside the directory. The destination path must not already
    exist.

    If the destination already exists but is not a directory, it may be
    overwritten depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed.
    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    """
    real_dst = dst
    if os.path.isdir(dst):
        real_dst = os.path.join(dst, _basename(src))
        if os.path.exists(real_dst):
            raise Error("Destination path '%s' already exists" % real_dst)
    try:
        os.rename(src, real_dst)
    except OSError:
        if os.path.isdir(src):
            if destinsrc(src, dst):
                raise Error("Cannot move a directory '%s' into itself '%s'." % (src, dst))
            copytree(src, real_dst, symlinks=True)
            rmtree(src)
        else:
            copy2(src, real_dst)
            os.unlink(src)

#--------------------------------------------------------------------------

def destinsrc(src, dst):
    src = abspath(src)
    dst = abspath(dst)
    if not src.endswith(os.path.sep):
        src += os.path.sep
    if not dst.endswith(os.path.sep):
        dst += os.path.sep
    return dst.startswith(src)

#---------------------------------------------------------------------------

def trimWhiteSpace(string):
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
    except Exception as e:
        print('Exception: e=%s' % e)

#---------------------------------------------------------------------------

def replaceLine(inputName, outputName, noticeDirectory):
    '''
    Create a filtered copy of the designated input file to the designated
    output file such that there will be no lines having superfluous
    trailing white space.
    '''
    try:
        inputFile = open(inputName, 'r')
    except Exception as e:
        print('Exception: e=%s' % e)
        if os.path.islink(inputName):
            # Report Broken Symbolic Link to Named File.
            link = os.readlink(inputName)
            print('  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                  (inputName, link))
        else:
            # Report Unknown Access Issue to Named File.
            print('  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                  inputName)

    try:
        outputFile = open(outputName, 'w')
    except Exception as e:
        print('Exception: e=%s' % e)
        if os.path.islink(outputName):
            # Report Broken Symbolic Link to Named File.
            link = os.readlink(inputName)
            print(
                '  *** WARNING: Broken Link Issue with\n    %s->%s\n' % \
                (outputName, link))
        else:
            # Report Unknown Access Issue to Named File.
            print(
                '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
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

            if str(line).find(oldVersion) > -1:

                changed = True
                changedLine = line.replace(oldVersion, newVersion)

                totalCharacters += len(changedLine)
                totalLines += 1
                trimmedText = '%s\n' % trimWhiteSpace(changedLine)
                outputFile.write(trimmedText)

##              outputFile.write('%s' % line.replace(oldVersion,
##                                                   newVersion))
            else:

                totalCharacters += len(line)
                totalLines += 1
                trimmedText = '%s\n' % trimWhiteSpace(line)
                outputFile.write(trimmedText)

##              outputFile.write('%s' % line)


##            totalCharacters += len(line)
##            totalLines += 1
##            trimmedText = '%s\n' % trimWhiteSpace(line)
##            outputFile.write(trimmedText)

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
        else:
            # Report Unknown Access Issue to Named File.
            print(
                '  *** WARNING: Unknown Access Issue with\n    %s\n' % \
                inputName)

    return (changed, totalCharacters, totalLines)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    prototype = theMainApplication
    myApp = tsCommandLineEnv.CommandLineEnv(

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

        enableDefaultCommandLineParser=False,

        logs=[],

        runTimeEntryPoint=prototype)

    myApp.Wrapper()
