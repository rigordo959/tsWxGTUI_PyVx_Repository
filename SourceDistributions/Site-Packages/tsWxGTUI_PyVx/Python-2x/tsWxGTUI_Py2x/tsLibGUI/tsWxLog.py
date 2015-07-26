#! /usr/bin/env python
# "Time-stamp: <03/28/2015 12:34:48 PM rsg>"
'''
tsWxLog.py - Class defines the interface for the log targets
used by wxWidgets logging functions as explained in the wxLog
Classes Overview. This implementation uses the tsLogger class.
'''
#################################################################
#
# File: tsWxLog.py
#
# Purpose:
#
#    Class defines the interface for the log targets used by
#    wxWidgets logging functions as explained in the wxLog
#    Classes Overview. This implementation uses the tsLogger
#    class.
#
# Usage (example):
#
#    # Import
#
#    from tsWxLog import Log
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
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxLog'
__version__   = '0.0.0'
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

import time

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
from tsWxGTUI_Py2x.tsLibCLI import tsLogger

Logger = tsLogger.TsLogger

#---------------------------------------------------------------------------

from tsWxGTUI_Py2x.tsLibGUI import tsWxGlobals as wx

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

##wxLogOverview = """

##wxLog Classes Overview

##Classes: wxLog, wxLogStderr, wxLogStream, wxLogTextCtrl, wxLogWindow,
##wxLogGui, wxLogNull,wxLogBuffer, wxLogChain, wxLogInterposer,
##wxLogInterposerTemp, wxStreamToTextRedirector

##Table of contents:
##*       Introduction
##*       Log Messages Selection
##*       Log Targets
##*       Logging in Multi-Threaded Applications
##*       Logging Customization
##*       Using trace masks
##*       Timestamps

###---------------------------------------------------------------------------
 
##Introduction

##This is a general overview of logging classes provided by wxWidgets.
##The word logging here has a broad sense, including all of the program
##output, not only non-interactive messages. The logging facilities
##included in wxWidgets provide the base wxLog class which defines
##the standard interface for a log target as well as several standard
##implementations of it and a family of functions to use with them.

##First of all, no knowledge of wxLog classes is needed to use them. For
##this, you should only know aboutwxLogXXX() functions. All of them have
##the same syntax as printf() or vprintf() , i.e. they take the format
##string as the first argument and respectively a variable number of
##arguments or a variable argument list pointer. Here are all of them:

##*       wxLogFatalError() which is like wxLogError(), but also
##        terminates the program with the exit code 3 (using abort()
##        standard function). Unlike for all the other logging functions,
##        this function can't be overridden by a log target.

##*       wxLogError() is the function to use for error messages,
##        i.e. the messages that must be shown to the user. The default
##        processing is to pop up a message box to inform the user about
##        it.

##*       wxLogWarning() for warnings. They are also normally shown to
##        the user, but don't interrupt the program work.

##*       wxLogMessage() is for all normal, informational messages. They
##        also appear in a message box by default (but it can be changed,
##        see below).

##*       wxLogVerbose() is for verbose output. Normally, it is suppressed,
##        but might be activated if the user wishes to know more details
##        about the program progress (another, but possibly confusing name
##        for the same function is wxLogInfo).

##*       wxLogStatus() is for status messages. They will go into the
##        status bar of the active or specified (as the first argument)
##        wxFrame if it has one.

##*       wxLogSysError() is mostly used by wxWidgets itself, but might
##        be handy for logging errors after system call (API function)
##        failure. It logs the specified message text as well as the last
##        system error code (errno or Windows' GetLastError() depending
##        on the platform) and the corresponding error message. The second
##        form of this function takes the error code explicitly as the
##        first argument.

##*       wxLogDebug() is the right function for debug output. It only
##        does anything at all in the debug mode (when the preprocessor
##        symbol __WXDEBUG__ is defined) and expands to nothing in
##        release mode (otherwise). Note that under Windows, you must
##        either run the program under debugger or use a 3rd party
##        program such as DebugView (http://www.microsoft.com/technet/
##        sysinternals/Miscellaneous/DebugView.mspx) to actually see
##        the debug output.

##*       wxLogTrace() as wxLogDebug() only does something in debug build.
##        The reason for making it a separate function from it is that
##        usually there are a lot of trace messages, so it might make
##        sense to separate them from other debug messages which would be
##        flooded in them. Moreover, the second version of this function
##        takes a trace mask as the first argument which allows to further
##        restrict the amount of messages generated.

##The usage of these functions should be fairly straightforward, however
##it may be asked why not use the other logging facilities, such as C
##standard stdio functions or C++ streams. The short answer is that
##they're all very good generic mechanisms, but are not really adapted
##for wxWidgets, while the log classes are. Some of advantages in using
##wxWidgets log functions are:

##*       Portability: It is a common practice to use printf() statements
##        or cout/cerr C++ streams for writing out some (debug or
##        otherwise) information. Although it works just fine under Unix,
##        these messages go strictly nowhere under Windows where the
##        stdout of GUI programs is not assigned to anything. Thus, you
##        might view wxLogMessage() as a simple substitute for printf().
##        You can also redirect thewxLogXXX calls to cout by just writing:

##*           wxLog* logger = new wxLogStream(&cout);

##*           wxLog::SetActiveTarget(logger);

##Finally, there is also a possibility to redirect the output sent to cout
##to a wxTextCtrl by using thewxStreamToTextRedirector class.

##*       Flexibility: The output of wxLog functions can be redirected
##        or suppressed entirely based on their importance, which is
##        either impossible or difficult to do with traditional methods.
##        For example, only error messages, or only error messages and
##        warnings might be logged, filtering out all informational
##        messages.

##*       Completeness: Usually, an error message should be presented
##        to the user when some operation fails. Let's take a quite
##        simple but common case of a file error: suppose that you're
##        writing your data file on disk and there is not enough space.
##        The actual error might have been detected inside wxWidgets
##        code (say, in wxFile::Write), so the calling function doesn't
##        really know the exact reason of the failure, it only knows
##        that the data file couldn't be written to the disk. However,
##        as wxWidgets useswxLogError() in this situation, the exact
##        error code (and the corresponding error message) will be
##        given to the user together with 'high level' message about
##        data file writing error.

###---------------------------------------------------------------------------

##Log Messages Selection

##By default, most log messages are enabled. In particular, this means
##that errors logged by wxWidgets code itself (e.g. when it fails to
##perform some operation, for instance wxFile::Open() logs an error
##when it fails to open a file) will be processed and shown to the user.

##To disable the logging entirely you can usewxLog::EnableLogging()
##method or, more usually, wxLogNull class which temporarily disables
##logging and restores it back to the original setting when it is
##destroyed.

##To limit logging to important messages only, you may use
##wxLog::SetLogLevel() with e.g. wxLOG_Warning value -- this will
##completely disable all logging messages with the severity less
##than warnings, sowxLogMessage() output won't be shown to the user
##any more.

##Moreover, the log level can be set separately for different log
##components. Before showing how this can be useful, let us explain
##what log components are: they are simply arbitrary strings identifying
##the component, or module, which generated the message. They are
##hierarchical in the sense that 'foo/bar/baz' component is supposed
##to be a child of 'foo'. And all components are children of the
##unnamed root component.

##By default, all messages logged by wxWidgets originate from 'wx'
##component or one of its subcomponents such as 'wx/net/ftp',
##while the messages logged by your own code are assigned empty log
##component. To change this, you need to define wxLOG_COMPONENT to a
##string uniquely identifying each component, e.g. you could give it
##the value 'MyProgram' by default and re-define it as 'MyProgram/DB'
##in the module working with the database and 'MyProgram/DB/Trans' in
##its part managing the transactions. Then you could use
##wxLog::SetComponentLevel() in the following ways:

##        // disable all database error messages, everybody knows
##        // databases never fail anyhow
##        wxLog::SetComponentLevel('MyProgram/DB', wxLOG_FatalError);

##        // but enable tracing for the transactions as somehow our
##        // changes don't get committed sometimes
##        wxLog::SetComponentLevel('MyProgram/DB/Trans', wxLOG_Trace);

##        // also enable tracing messages from wxWidgets dynamic module
##        // loading mechanism
##        wxLog::SetComponentLevel('wx/base/module', wxLOG_Trace);

##Notice that the log level set explicitly for the transactions code
##overrides the log level of the parent component but that all other
##database code subcomponents inherit its setting by default and so
##won't generate any log messages at all.

###---------------------------------------------------------------------------

##Log Targets

##After having enumerated all the functions which are normally used to
##log the messages, and why would you want to use them, we now describe
##how all this works.

##wxWidgets has the notion of a log target: it is just a class deriving
##from wxLog. As such, it implements the virtual functions of the base
##class which are called when a message is logged. Only one log target
##is active at any moment, this is the one used by wxLogXXX() functions.
##The normal usage of a log object (i.e. object of a class derived
##from wxLog) is to install it as the active target with a call to
##SetActiveTarget() and it will be used automatically by all subsequent
##calls to wxLogXXX() functions.

##To create a new log target class you only need to derive it from wxLog
##and override one or several ofwxLog::DoLogRecord(), wxLog::
##DoLogTextAtLevel() and wxLog::DoLogText() in it. The first one is the
##most flexible and allows you to change the formatting of the messages,
##dynamically filter and redirect them and so on -- all log messages,
##except for those generated by wxLogFatalError(), pass by this function.
##wxLog::DoLogTextAtLevel() should be overridden if you simply want to
##redirect the log messages somewhere else, without changing their
##formatting. Finally, it is enough to override wxLog::DoLogText() if
##you only want to redirect the log messages and the destination doesn't
##depend on the message log level.

##There are some predefined classes deriving from wxLog and which might
##be helpful to see how you can create a new log target class and, of
##course, may also be used without any change. There are:

##*       wxLogStderr: This class logs messages to a FILE *, using stderr
##        by default as its name suggests.

##*       wxLogStream: This class has the same functionality as wxLogStderr,
##        but uses ostream and cerr instead of FILE * and stderr.

##*       wxLogGui: This is the standard log target for wxWidgets
##        applications (it is used by default if you don't do anything)
##        and provides the most reasonable handling of all types of
##        messages for given platform.

##*       wxLogWindow: This log target provides a 'log console' which
##        collects all messages generated by the application and also
##        passes them to the previous active log target. The log window
##        frame has a menu allowing user to clear the log, close it
##        completely or save all messages to file.

##*       wxLogBuffer: This target collects all the logged messages
##        in an internal buffer allowing to show them later to the
##        user all at once.

##*       wxLogNull: The last log class is quite particular: it doesn't
##        do anything. The objects of this class may be instantiated to
##        (temporarily) suppress output of wxLogXXX() functions. As an
##        example, trying to open a non-existing file will usually
##        provoke an error message, but if for some reasons it is
##        unwanted, just use this construction:

##*           wxFile file;
##*
##*           // wxFile.Open() normally complains if file can't be
##*           // opened, we don't want it
##*           {
##*               wxLogNull logNo;
##*               if ( !file.Open('bar') )
##*               {
##*                   // ... process error ourselves ...
##*               }
##*           } // ~wxLogNull called, old log sink restored
##*
##*           wxLogMessage('...'); // ok

##The log targets can also be combined: for example you may wish to
##redirect the messages somewhere else (for example, to a log file) but
##also process them as normally. For this the wxLogChain, wxLogInterposer,
##and wxLogInterposerTemp can be used.

###---------------------------------------------------------------------------

##Logging in Multi-Threaded Applications

##Starting with wxWidgets 2.9.1, logging functions can be safely called
##from any thread. Messages logged from threads other than the main one
##will be buffered until wxLog::Flush() is called in the main thread
##(which usually happens during idle time, i.e. after processing all
##pending events) and will be really output only then. Notice that the
##default GUI logger already only output the messages when it is flushed,
##so by default messages from the other threads will be shown more or
##less at the same moment as usual. However if you define a custom log
##target, messages may be logged out of order, e.g. messages from the
##main thread with later timestamp may appear before messages with earlier
##timestamp logged from other threads. wxLog does however guarantee that
##messages logged by each thread will appear in order in which they were
##logged.

##Also notice that wxLog::EnableLogging() and wxLogNull class which uses
##it only affect the current thread, i.e. logging messages may still be
##generated by the other threads after a call to EnableLogging(false).

###---------------------------------------------------------------------------

##Logging Customization

##To completely change the logging behaviour you may define a custom log
##target. For example, you could define a class inheriting from wxLog which
##shows all the log messages in some part of your main application window
##reserved for the message output without interrupting the user work flow
##with modal message boxes.

##To use your custom log target you may either call wxLog::SetActiveTarget()
##with your custom log object or create a wxAppTraits-derived class and
##override wxAppTraits::CreateLogTarget() virtual method in it and also
##override wxApp::CreateTraits() to return an instance of your custom
##traits object. Notice that in the latter case you should be prepared
##for logging messages early during the program startup and also during
##program shutdown so you shouldn't rely on existence of the main
##application window, for example. You can however safely assume that
##GUI is (already/still) available when your log target as used as
##wxWidgets automatically switches to using wxLogStderr if it isn't.

##There are several methods which may be overridden in the derived class
##to customize log messages handling:wxLog::DoLogRecord(),
##wxLog::DoLogTextAtLevel() and wxLog::DoLogText().

##The last method is the simplest one: you should override it if you
##simply want to redirect the log output elsewhere, without taking into
##account the level of the message. If you do want to handle messages of
##different levels differently, then you should override wxLog::
##DoLogTextAtLevel().

##Finally, if more control over the output format is needed, then the
##first function must be overridden as it allows to construct custom
##messages depending on the log level or even do completely different
##things depending on the message severity (for example, throw away all
##messages except warnings and errors, show warnings on the screen
##and forward the error messages to the user's (or programmer's)
##cell phone -- maybe depending on whether the timestamp tells us
##if it is day or night in the current time zone).

##The dialog sample illustrates this approach by defining a custom
##log target customizing the dialog used bywxLogGui for the single
##messages.

###---------------------------------------------------------------------------

##Using trace masks

##Notice that the use of log trace masks is hardly necessary any
##longer in current wxWidgets version as the same effect can be
##achieved by using different log components for different log
##statements of any level. Please see Log Messages Selection for
##more information about the log components.

##The functions below allow some limited customization of wxLog
##behaviour without writing a new log target class (which, aside
##from being a matter of several minutes, allows you to do anything
##you want). The verbose messages are the trace messages which are
##not disabled in the release mode and are generated bywxLogVerbose().
##They are not normally shown to the user because they present
##little interest, but may be activated, for example, in order
##to help the user find some program problem.

##As for the (real) trace messages, their handling depends on the
##currently enabled trace masks:
 
##if wxLog::AddTraceMask() was called for the mask of the given
##message, it will be logged, otherwise nothing happens.

##For example,

##wxLogTrace( wxTRACE_OleCalls, 'IFoo::Bar() called' );

##will log the message if it was preceded by:

##wxLog::AddTraceMask( wxTRACE_OleCalls );

##The standard trace masks are given in wxLogTrace() documentation.

###---------------------------------------------------------------------------

##Timestamps

##The wxLog::LogRecord() function automatically prepends a time stamp
##to all the messages. The format of the time stamp may be changed: it
##can be any string with % specifications fully described in the
##documentation of the standard strftime() function. For example,
##the default format is '[%d/%b/%y %H:%M:%S] ' which gives something
##like '[17/Sep/98 22:10:16] ' (without quotes) for the current date.

##Setting an empty string as the time format or calling the shortcut
##wxLog::DisableTimestamp(), disables timestamping of the messages
##completely.

##Note:

##Timestamping is disabled for Visual C++ users in debug builds by
##default because otherwise it would be impossible to directly go
##to the line from which the log message was generated by simply
##clicking in the debugger window on the corresponding error message.
##If you wish to enable it, please use SetTimestamp() explicitly.

##"""

#---------------------------------------------------------------------------

class Log(Logger):
    '''
    wxLog class defines the interface for the log targets used by
    wxWidgets logging functions as explained in the wxLog overview.

    The only situations when you need to directly use this class
    is when you want to derive your own log target because the
    existing ones does not satisfy your needs.

    Another case is if you wish to customize the behaviour of the
    standard logging classes (all of which respect the wxLog
    settings): for example, set which trace messages are logged
    and which are not or change (or even remove completely) the
    timestamp on the messages.

    Otherwise, it is completely hidden behind the wxLogXXX()
    functions and you may not even know about its existence.

    See log overview for the descriptions of wxWidgets logging
    facilities.
    '''
    def __init__(self):
        '''
        '''
##        theClass = 'Log'

##        wx.RegisterFirstCallerClassName(self, theClass)

##        Logger.__init__(self,  *kw)

        Logger.__init__(
            self,
            threshold=wx.DEBUG,
            start=time.time(),
            name='sample.log')

##        self_ts_Logger = []
##        self.ts_Threshold = Logger.INFO
##        self.ts_StartTime = time.time()
##        self.ts_Device = None
##        self.ts_Logger = Logger.DummyLogger

    #-----------------------------------------------------------------------

    def __del__(self):
        '''
        '''
        pass
##        msg = 'NotImplementedError: %s' % '__del__ in tsWxLog'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def AddTraceMask(self, mask):
        '''
        Add the mask to the list of allowed masks for wxLogTrace.

        See also: RemoveTraceMask(), GetTraceMasks()
        '''
        msg = 'NotImplementedError: %s' % 'AddTraceMask in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def ClearTraceMasks(self):
        '''
        Removes all trace masks previously set with AddTraceMask.

        See also: RemoveTraceMask()
        '''
        msg = 'NotImplementedError: %s' % 'ClearTraceMasks in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Destroy(self):
        '''
        '''
        msg = 'NotImplementedError: %s' % 'Destroy in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def DisableTimestam(self):
        '''
        Disables time stamping of the log messages.
        '''
        msg = 'NotImplementedError: %s' % 'DisableTimestam in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def DoLogRecord(self, level, msg, info):
        '''
        Called to log a new record.

        Any log message created by wxLogXXX() functions is passed to this
        method of the active log target. The default implementation
        prepends the timestamp and, for some log levels (e.g. error
        and warning), the corresponding prefix to msg and passes it to
        DoLogTextAtLevel().

        You may override this method to implement custom formatting of
        the log messages or to implement custom filtering of log messages
        (e.g. you could discard all log messages coming from the given
        source file).
        '''
        msg = 'NotImplementedError: %s' % 'DoLogRecord in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def DoLogText(self, msg):
        '''
        Called to log the specified string.

        A simple implementation might just send the string to stdout
        or stderr or save it in a file (of course, the already existing
        wxLogStderr can be used for this).

        The base class version of this function asserts so it must be
        overridden if you do not override DoLogRecord() or
        DoLogTextAtLevel().
        '''
        msg = 'NotImplementedError: %s' % 'DoLogText in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def DoLogTextAtLevel(self, level, msg):
        '''
        Called to log the specified string at given level.

        The base class versions logs debug and trace messages on the
        system default debug output channel and passes all the other
        messages to DoLogText().
        '''
        msg = 'NotImplementedError: %s' % 'DoLogTextAtLevel in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def DontCreateOnDemand(self):
        '''
        Instructs wxLog to not create new log targets on the fly if there
        is none currently. (Almost) for internal use only: it is supposed
        to be called by the application shutdown code.

        Note that this function also calls ClearTraceMasks.
        '''
        msg = 'NotImplementedError: %s' % 'DontCreateOnDemand in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def EnableLogging(self, enable=True):
        '''
        Globally enable or disable logging.

        Calling this function with false argument disables all log
        messages for the current thread.

        See also: wxLogNull, IsEnabled()

        Returns: The old state, i.e. true if logging was previously
        enabled and false if it was disabled.
        '''
##        self.ts_Threshold = Logger.INFO
##        self.ts_StartTime = time.time()
##        self.ts_Device = None
##        self.ts_Logger = Logger.TsLogger(threshold=self.ts_Threshold,
##                                         start=self.ts_StartTime,
##                                         name=self.ts_Device)
        msg = 'NotImplementedError: %s' % 'EnableLogging in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def Flush(self):
        '''
        Some of wxLog implementations, most notably the standard wxLogGui
        class, buffer the messages (for example, to avoid showing the
        user a zillion of modal message boxes one after another -- which
        would be really annoying).

        This function shows them all and clears the buffer contents. If
        the buffer is already empty, nothing happens.

        If you override this method in a derived class, call the base
        class version first, before doing anything else.

        Reimplemented in wxLogGui, and wxLogBuffer.
        '''
        msg = 'NotImplementedError: %s' % 'Flush in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def FlushActive(self):
        '''
        Flushes the current log target if any, does nothing if
        there is none.

        When this method is called from the main thread context, it also
        flushes any previously buffered messages logged by the other
        threads. When it is called from the other threads it simply calls
        Flush() on the currently active log target, so it mostly makes
        sense to do this if a thread has its own logger set with
        SetThreadActiveTarget().
        '''
        msg = 'NotImplementedError: %s' % 'FlushActive in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetActiveTarget(self):
        '''
        Returns the pointer to the active log target (may be NULL).

        Notice that if SetActiveTarget() had not been previously explicitly
        called, this function will by default try to create a log target
        by calling wxAppTraits::CreateLogTarget() which may be overridden
        in a user-defined traits class to change the default behaviour.
        You may also call DontCreateOnDemand() to disable this behaviour.

        When this function is called from threads other than main one,
        auto-creation does not happen. But if the thread has a thread-
        specific log target previously set by SetThreadActiveTarget(),
        it is returned instead of the global one. Otherwise, the global
        log target is returned.
        '''
        msg = 'NotImplementedError: %s' % 'GetActiveTarget in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetLogLevel(self):
        '''
        Returns the current log level limit.

        All messages at levels strictly greater (i.e., tsLogger severity
        levels lower) than the value returned by this function are not
        logged at all.

        See also: SetLogLevel(), IsLevelEnabled()
        '''
        msg = 'NotImplementedError: %s' % 'GetLogLevel in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetRepetitionCounting(self):
        '''
        Returns whether the repetition counting mode is enabled.
        '''
        msg = 'NotImplementedError: %s' % 'GetRepetitionCounting ' + \
              'in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetTimestamp(self):
        '''
        Returns the current timestamp format string.
        '''
        msg = 'NotImplementedError: %s' % 'GetTimestamp in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetTraceMasks(self):
        '''
        Returns the currently allowed list of string trace masks.
        '''
        msg = 'NotImplementedError: %s' % 'GetTraceMasks in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def GetVerbose(self):
        '''
        Returns whether the verbose mode is currently active.
        '''
        msg = 'NotImplementedError: %s' % 'GetVerbose in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def IsAllowedTraceMask(self, mask):
        '''
        Returns true if the mask is one of allowed masks for wxLogTrace().
        '''
        msg = 'NotImplementedError: %s' % 'IsAllowedTraceMask in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def IsEnabled(self):
        '''
        Returns true if logging is enabled at all now.

        See also: IsLevelEnabled(), EnableLogging()
        '''
        msg = 'NotImplementedError: %s' % 'IsEnabled in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def IsLevelEnabled(self, level, component):
        '''
        Returns true if logging at this level is enabled for the current
        thread.

        This function only returns true if logging is globally enabled
        and if level is less than or equal to the maximal log level
        enabled for the given component.

        See also: IsEnabled(), SetLogLevel(), GetLogLevel(),
        SetComponentLevel()
        '''
        msg = 'NotImplementedError: %s' % 'IsLevelEnabled in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    def LogRecord(self, level, msg, info):
        '''
        Log the given record.

        This function should only be called from the DoLog()
        implementations in the derived classes if they need to call
        DoLogRecord() on another log object (they can, of course,
        just use wxLog::DoLogRecord() call syntax to call it on the
        object itself). It should not be used for logging new messages
        which can be only sent to the currently active logger using
        OnLog() which also checks if the logging (for this level) is
        enabled while this method just directly calls DoLog().

        Example of use of this class from wxLogChain:

        void wxLogChain::DoLogRecord(wxLogLevel level,
                                     const wxString& msg,
                                     const wxLogRecordInfo& info)
        {
            // let the previous logger show it
            if ( m_logOld && IsPassingMessages() )
                m_logOld->LogRecord(level, msg, info);

            // and also send it to the new one
            if ( m_logNew && m_logNew != this )
                m_logNew->LogRecord(level, msg, info);
        }
        '''
        msg = 'NotImplementedError: %s' % 'LogRecord in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def OnLog(self, level, szString, t):
        '''
        Forwards the message at specified level to the DoLog() function of
        the active log target if there is any, does nothing otherwise.
        '''
        msg = 'NotImplementedError: %s' % 'OnLog in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def RemoveTraceMask(self, mask):
        '''
        Remove the mask from the list of allowed masks for wxLogTrace.

        See also: AddTraceMask
        '''
        msg = 'NotImplementedError: %s' % 'RemoveTraceMask in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def Resume(self):
        '''
        Resumes logging previously suspended by a call to Suspend.

        All messages logged in the meanwhile will be flushed soon.
        '''
        msg = 'NotImplementedError: %s' % 'Resume in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetActiveTarget(self, logtarget):
        '''
        Sets the specified log target as the active one. Returns the
        pointer to the previous active log target (may be NULL). To
        suppress logging use a new instance of wxLogNull not NULL.
        If the active log target is set to NULL a new default log
        target will be created when logging occurs.
        '''
        self.logger = Logger(
            threshold=wx.DEBUG,
            start=time.time(),
            name=logtarget)

##        msg = 'NotImplementedError: %s' % 'SetActiveTarget in tsWxLog'
##        self.logger.error(msg)
##        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetComponentLevel(self, pLogger):
        '''
        Sets the log level for the given component.

        For example, to disable all but error messages from wxWidgets
        network classes you may use

        \\ wxLog::SetComponentLevel("wx/net", wxLOG_Error);

        SetLogLevel() may be used to set the global log level.

        Parameters:
        component       Non-empty component name, possibly using slashes
        (/) to separate it into several parts.

        level   Maximal level of log messages from this component which
        will be handled instead of being simply discarded.
        '''
        msg = 'NotImplementedError: %s' % 'SetComponentLevel in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetLogLevel(self, logLevel):
        '''
        Specifies that log messages with level > logLevel should be
        ignored and not sent to the active log target.

        See also: SetComponentLevel()
        '''
        msg = 'NotImplementedError: %s' % 'SetLogLevel in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetRepetitionCounting(self, bRepetCounting):
        '''
        Enables logging mode in which a log message is logged once, and in
        case exactly the same message successively repeats one or more
        times, only the number of repetitions is logged.
        '''
        msg = 'NotImplementedError: %s' % 'SetRepetitionCounting ' + \
              'in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetThreadActiveTarget(self, ts):
        '''
        Sets a thread-specific log target.

        The log target passed to this function will be used for all
        messages logged by the current thread using the usual wxLog
        functions. This should not be called from the main thread
        which never uses a thread-specific log target but can be used
        for the other threads to handle thread logging completely
        separately; instead of buffering thread log messages in the
        main thread logger.

        Notice that unlike for SetActiveTarget(), wxWidgets does not
        destroy the thread-specific log targets when the thread
        terminates so doing this is your responsibility.

        This method is only available if wxUSE_THREADS is 1, i.e.
        wxWidgets was compiled with threads support.

        Parameters:
        logger  The new thread-specific log target, possibly NULL.

        Returns:
        The previous thread-specific log target, initially NULL.
        '''
        msg = 'NotImplementedError: %s' % 'SetThreadActiveTarget in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetTimestamp(self, ts):
        '''
        Sets the timestamp format prepended by the default log targets to
        all messages.

        The string may contain any normal characters as well
        as % prefixed format specificators, see strftime() manual for
        details. Passing an empty string to this function disables
        message timestamping.
        '''
        msg = 'NotImplementedError: %s' % 'SetTimestamp in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetTraceMask(self, ulMask):
        '''
        Sets the trace mask, see Customization section for details.
        '''
        msg = 'NotImplementedError: %s' % 'SetTraceMask in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def SetVerbose(self, verbose=True):
        '''
        Activates or deactivates verbose mode in which the verbose messages
        are logged as the normal ones instead of being silently dropped.

        The verbose messages are the trace messages which are not disabled
        in the release mode and are generated by wxLogVerbose().

        See also: wxLog Classes Overview
        '''
        msg = 'NotImplementedError: %s' % 'SetVerbose in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def Suspend(self):
        '''
        Suspends the logging until Resume is called. Note that the latter
        must be called the same number of times as the former to undo it,
        i.e. if you call Suspend() twice you must call Resume() twice as
        well.

        Note that suspending the logging means that the log sink will not
        be flushed periodically, it does not have any effect if the
        current log target does the logging immediately without waiting
        for Flush to be called (the standard GUI log target only shows
        the log dialog when it is flushed, so Suspend() works as expected
        with it).

        See also: Resume(), wxLogNull
        '''
        msg = 'NotImplementedError: %s' % 'Suspend in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------

    # @staticmethod
    def TimeStamp(self):
        '''
        The wxLog::DoLog() function automatically prepends a time stamp to
        all the messages. The format of the time stamp may be changed: it
        can be any string with % specifications fully described in the
        documentation of the standard strftime() function. For example,
        the default format is "[%d/%b/%y %H:%M:%S] " which gives something
        like "[17/Sep/98 22:10:16] " (without quotes) for the current date.
        Setting an empty string as the time format disables timestamping
        of the messages completely.
        '''
        msg = 'NotImplementedError: %s' % 'TimeStamp in tsWxLog'
        self.logger.error(msg)
        raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------

class LogBuffer(Log):
    '''
    wxLogBuffer is a very simple implementation of log sink which simply
    collects all the logged messages in a string (except the debug
    messages which are output in the usual way immediately as we are
    presumably not interested in collecting them for later).

    The messages from different log function calls are separated by the
    new lines.

    All the messages collected so far can be shown to the user (and the
    current buffer cleared) by calling the overloaded wxLogBuffer::Flush
    method.
    '''
    pass

#---------------------------------------------------------------------------

class LogChain(Log):
    '''
    This simple class allows you to chain log sinks, that is to install
    a new sink but keep passing log messages to the old one instead of
    replacing it completely as wxLog::SetActiveTarget does.

    It is especially useful when you want to divert the logs somewhere
    (for example to a file or a log window) but also keep showing the
    error messages using the standard dialogs as wxLogGui does by default.

    Example of usage:

    wxLogChain *logChain = new wxLogChain(new wxLogStderr);

    // all the log messages are sent to stderr and also processed as
    usually
    ...

    // do not delete logChain directly as this would leave a dangling
    // pointer as active log target, use SetActiveTarget() instead
    delete wxLog::SetActiveTarget(...something else or NULL...);
    '''
    pass

#---------------------------------------------------------------------------

class LogGui(Log):
    '''
    This is the default log target for the GUI wxWidgets applications.

    Please see Logging Customization for explanation of how to change
    the default log target.

    An object of this class is used by default to show the log messages
    created by using wxLogMessage(), wxLogError() and other logging
    functions. It does not display the messages logged by them
    immediately however but accumulates all messages logged during an
    event handler execution and then shows them all at once when its
    Flush() method is called during the idle time processing. This has
    the important advantage of showing only a single dialog to the user
    even if several messages were logged because of a single error as
    it often happens (e.g. a low level function could log a message
    because it failed to open a file resulting in its caller logging
    another message due to the failure of higher level operation
    requiring the use of this file). If you need to force the display
    of all previously logged messages immediately you can use
    wxLog::FlushActive() to force the dialog display.

    Also notice that if an error message is logged when several
    informative messages had been already logged before, the informative
    messages are discarded on the assumption that they are not useful
    -- and may be confusing and hence harmful -- any more after the error.
    The warning and error messages are never discarded however and any
    informational messages logged after the first error one are also
    kept (as they may contain information about the error recovery).
    You may override DoLog() method to change this behaviour.

    At any rate, it is possible that that several messages were
    accumulated before this class Flush() method is called. If this
    is the case, Flush() uses a custom dialog which shows the last
    message directly and allows the user to view the previously logged
    ones by expanding the "Details" wxCollapsiblePane inside it. This
    custom dialog also provides the buttons for copying the log
    messages to the clipboard and saving them to a file.

    However if only a single message is present when Flush() is called,
    just a wxMessageBox() is used to show it. This has the advantage of
    being closer to the native behaviour but it does not give the user
    any possibility to copy or save the message (except for the recent
    Windows versions where Ctrl-C may be pressed in the message box to
    copy its contents to the clipboard) so you may want to override
    DoShowSingleMessage() to customize wxLogGui -- the dialogs sample
    shows how to do this.
    '''
    pass

#---------------------------------------------------------------------------

class LogNull(Log):
    '''
    This class allows you to temporarily suspend logging.

    All calls to the log functions during the life time of an object
    of this class are just ignored.

    In particular, it can be used to suppress the log messages given
    by wxWidgets itself but it should be noted that it is rarely the
    best way to cope with this problem as all log messages are
    suppressed, even if they indicate a completely different error
    than the one the programmer wanted to suppress.

    For instance, the example of the overview:

          wxFile file;

          // wxFile.Open() normally complains if file cannot be
          opened, we do not want it
          {
            wxLogNull logNo;
            if ( !file.Open("bar") )
              ... process error ourselves ...
          } // ~wxLogNull called, old log sink restored

          wxLogMessage("..."); // ok

    would be better written as:

          wxFile file;

          // do not try to open file if it does not exist, we are
          // prepared to deal with this ourselves - but all other
          // errors are not expected
          if ( wxFile::Exists("bar") )
          {
              // gives an error message if the file could not be opened
              file.Open("bar");
          }
          else
          {
              ...
          }
    '''
    pass

#---------------------------------------------------------------------------

class LogRecordInfo(Log):
    '''
    Information about a log record (unit of the log output).
    '''
    pass

#---------------------------------------------------------------------------

class LogStderr(Log):
    '''
    This class can be used to redirect the log messages to a C file
    stream (not to be confused with C++ streams).

    It is the default log target for the non-GUI wxWidgets applications
    which send all the output to stderr.
    '''
    pass

#---------------------------------------------------------------------------

class LogStream(Log):
    '''
    This class can be used to redirect the log messages to a C++ stream.

    Please note that this class is only available if wxWidgets was
    compiled with the standard iostream library support
    (wxUSE_STD_IOSTREAM must be on).
    '''
    pass

#---------------------------------------------------------------------------

class LogTextCtrl(Log):
    '''
    Using these target all the log messages can be redirected to a text
    control.

    The text control must have been created with wxTE_MULTILINE style
    by the caller previously.
    '''
    pass

#---------------------------------------------------------------------------

class LogWindow(Log):
    '''
    This class represents a background log window: to be precise, it
    collects all log messages in the log frame which it manages but
    also passes them on to the log target which was active at the
    moment of its creation.

    This allows you, for example, to show all the log messages in a
    frame but still continue to process them normally by showing the
    standard log dialog.
    '''
    pass

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    myLogger = Log()
    myLogger.debug('Hello!')
    myLogger.error('Hello!')
    myLogger.SetActiveTarget('another.log')
    myLogger.debug('Goodbye!')
    myLogger.error('Goodbye!')
