#! /usr/bin/env python
#"Time-stamp: <09/20/2013  4:38:35 AM rsg>"
'''
test_tsWxDialogDemo.py - Application program to mimic some features of
the Graphical Text User Interface.
'''
#################################################################
#
# File: test_tsWxDialogDemo.py
#
# Purpose:
#
#    Application program to mimic some features of the
#    Graphical Text User Interface.
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Usage (example):
#
#     python test_tsWxDialogDemo.py
#
# Methods:
#
#   None
#
# ToDo:
#
#   None
#
# Modifications:
#
#   None
#
#################################################################

__title__     = 'test_tsWxDialogDemo'
__version__   = '1.0.0'
__date__      = '06/25/2012'
__authors__   = 'Richard S. Gordon, a.k.a. Software Gadgetry'
__copyright__ = 'Copyright (c) 2012 Software Gadgetry. All rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Authors: %s' % __authors__
__line3__ = '%s' % __copyright__
__header__ = '\n\n%s\n\n  %s\n  %s\n' % (__line1__, __line2__, __line3__)

mainTitleVersionDate = __line1__

import os.path
import sys
import time
import traceback
from optparse import OptionParser

DEBUG = True

if False and DEBUG:
    # Import wingdbstub only if cygwin platform.
    import platform
    hostOS = platform.system().lower()
    if hostOS.find('cygwin') != -1:
        try:
            import wingdbstub
        except ImportError:
            pass

try:
    import tsLibraries
except ImportError:
    pass

import tsApplication as tsAPP
import tsExceptions as tse
##import tsLogger as Logger

#########################################################################
# Begin Test Control Switches
DEBUG = True
VERBOSE = False

redirectEnabled = DEBUG
if redirectEnabled:
    if VERBOSE:
        redirectedFileName = 'redirectedFile.log'
    else:
        redirectedFileName = None
else:
    redirectedFileName = None

runTimeTitleEnabled = False
exceptionHandlingEnabled = True
frameSizingEnabled = True
splashScreenSeconds = 0

centerOnScreenEnabled = False
tracebackEnabled = False

lastWindowId = None

def nextWindowId():
    global lastWindowId
    if lastWindowId is None:
        lastWindowId = 1 # wx.ID_ANY
    else:
        lastWindowId += 1
    return (lastWindowId)

# End Test Control Switches
#########################################################################

theStatusBar = None

__help__ = '''
This program demonstrates currently supported features.

'''

#--------------------------------------------------------------------------

if not exceptionHandlingEnabled:

    try:
        import wx
    except ImportError as wxImportError:
        import tsWx as wx

else:

    try:

        import tsWx as wx

    except Exception as theTsWxImportError:

        _stdout = sys.stdout
        _stderr = sys.stderr

        _stderr.write('%s' % __header__)

        exitStatus = tse.NONERROR_ERROR_CODE
        msg = tse.NO_ERROR

        if isinstance(theTsWxImportError, tse.TsExceptions):

            exitStatus = theTsWxImportError.exitCode
            msg = '%s. [ExitCode #%d]' % (
                str(theTsWxImportError).replace("'", ""), exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                tse.displayError(theTsWxImportError)

        elif isinstance(theTsWxImportError, ImportError):

            exitStatus = 128 # TBD - tse.INVALID_ERROR_CODE
            msg = '%s. %s. %s. [ExitCode #%d]' % (
                tse.USER_INTERFACE_EXCEPTION,
                tse.CHARACTER_GRAPHICS_NOT_AVAILABLE,
                theTsWxImportError,
                exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        else:

            exitStatus = tse.INVALID_ERROR_CODE
            msg = "Unexpected error: %s [ExitCode #%d]" % (
                sys.exc_info()[0], exitStatus)
            if tracebackEnabled:
                _stderr.write('\n%s\n\n' % msg)
                _stderr.write(traceback.format_exc())

        _stderr.write('\n%s\n' % msg)

        # Return (exitStatus)
        sys.exit(exitStatus)

#--------------------------------------------------------------------------

##import  wx

#---------------------------------------------------------------------------
# Create and set a help provider.  Normally you would do this in
# the app's OnInit as it must be done before any SetHelpText calls.
##provider = wx.SimpleHelpProvider()
##wx.HelpProvider.Set(provider)

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):

    def __init__(self, parent, log=None):

        self.log = log
        wx.Panel.__init__(self,
                          parent,
                          -1,
                          pos=(10 * wx.pixelWidthPerCharacter,
                               10 * wx.pixelHeightPerCharacter), #wx.DefaultPosition,
                          size=(15 * wx.pixelWidthPerCharacter,
                                15 * wx.pixelHeightPerCharacter) #wx.DefaultSize
)

        b = wx.Button(self, -1, "Create and Show a custom Dialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)

        b = wx.Button(self, -1, "Show dialog with ShowWindowModal", (50, 140))
        self.Bind(wx.EVT_BUTTON, self.OnShowWindowModal, b)
        self.Bind(wx.EVT_WINDOW_MODAL_DIALOG_CLOSED,
                  self.OnWindowModalDialogClosed)

    #-----------------------------------------------------------------------

    def OnButton(self, evt):

        dlg = TestDialog(self, -1, "Sample Dialog", size=(350, 200),
                         style=wx.DEFAULT_DIALOG_STYLE,
                         )
        dlg.CenterOnScreen()

        # this does not return until the dialog is closed.
        val = dlg.ShowModal()
 
        if val == wx.ID_OK:
            self.log.WriteText("You pressed OK\n")
        else:
            self.log.WriteText("You pressed Cancel\n")

        dlg.Destroy()

    #-----------------------------------------------------------------------

    def OnShowWindowModal(self, evt):
        dlg = TestDialog(self, -1, "Sample Dialog", size=(350, 200),
                         style=wx.DEFAULT_DIALOG_STYLE)
        dlg.ShowWindowModal()

    #-----------------------------------------------------------------------

    def OnWindowModalDialogClosed(self, evt):
        dialog = evt.GetDialog()
        val = evt.GetReturnCode()
        try:
            btnTxt = { wx.ID_OK : "OK",
                       wx.ID_CANCEL: "Cancel" }[val]
        except KeyError:
            btnTxt = '<unknown>'
 
        # wx.MessageBox(
        print(
            "You closed the window-modal dialog with the %s button" % btnTxt)

        dialog.Destroy()

#---------------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#---------------------------------------------------------------------------


overview = """\
wxPython offers quite a few general purpose dialogs for useful data input from
the user; they are all based on the wx.Dialog class, which you can also
subclass to create custom dialogs to suit your needs.

The Dialog class, in addition to dialog-like behaviors, also supports the full
wxWindows layout featureset, which means that you can incorporate sizers or
layout constraints as needed to achieve the look and feel desired. It even
supports context-sensitive help, which is illustrated in this example.

The example is very simple; in real world situations, a dialog that had input
fields such as this would no doubt be required to deliver those values back to
the calling function. The Dialog class supports data retrieval in this manner.
<b>However, the data must be retrieved prior to the dialog being destroyed.</b>
The example shown here is <i>modal</i>; non-modal dialogs are possible as well.

See the documentation for the <code>Dialog</code> class for more details.

"""

#--------------------------------------------------------------------------

##if __name__ == '__main__':
##    import sys,os
##    import run
##    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

#--------------------------------------------------------------------------

##class TestDialog(wx.Dialog):

class _Prototype(wx.Dialog):
    '''
    Class to establish the dialog that contains the application specific
    graphical components.
    '''
    def tsGetTheId(self):
        '''
        Return the ID associated with this class instance.
        '''
        return id(self)

    #-----------------------------------------------------------------------

    def __init__(self,
                 parent,
                 id,
                 title,
                 size=(35 * wx.pixelWidthPerCharacter,
                       35 * wx.pixelHeightPerCharacter), #wx.DefaultSize,
                 pos=(10 * wx.pixelWidthPerCharacter,
                      10 * wx.pixelHeightPerCharacter), #wx.DefaultPosition,
                 style=wx.DEFAULT_DIALOG_STYLE,
                 name=wx.DialogNameStr):

        # Instead of calling wx.Dialog.__init__ we precreate the dialog
        # so we can set an extra style that must be set before
        # creation, and then we create the GUI object using the Create
        # method.
##        pre = wx.PreDialog()
##        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
##        pre.Create(parent, ID, title, pos, size, style)
        wx.Frame.__init__(self,
                          parent,
                          id=nextWindowId(),
                          title=title,
                          pos=pos,
                          size=pos,
                          style=style,
                          name=name)

        # This next step is the most important, it turns this Python
        # object into the real wrapper of the dialog (instead of pre)
        # as far as the wxPython extension is concerned.
##        self.PostCreate(pre)

        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "This is a wx.Dialog")
##        label.SetHelpText("This is the help text for the label")
        sizer.Add(label, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Field #1:")
##        label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(80,-1))
##        text.SetHelpText("Here's some help text for field #1")
        box.Add(text, 1, wx.ALIGN_CENTER|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Field #2:")
##        label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(80,-1))
##        text.SetHelpText("Here's some help text for field #2")
        box.Add(text, 1, wx.ALIGN_CENTER|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

##        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
##        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

##        btnsizer = wx.StdDialogButtonSizer()
 
##        if wx.Platform != "__WXMSW__":
##            btn = wx.ContextHelpButton(self)
##            btnsizer.AddButton(btn)
 
##        btn = wx.Button(self, wx.ID_OK)
##        btn.SetHelpText("The OK button completes the dialog")
##        btn.SetDefault()
##        btnsizer.AddButton(btn)

##        btn = wx.Button(self, wx.ID_CANCEL)
##        btn.SetHelpText("The Cancel button cancels the dialog. (Cool, huh?)")
##        btnsizer.AddButton(btn)
##        btnsizer.Realize()

##        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

        #-------------------------------------------------------------------
        # Begin Dialog Relocation
        #-------------------------------------------------------------------

        # TBD - Menu Bar Client Area Change in Frame did not
        # reduce height of panel.
        theDialog = self
##        menubar = wx.MenuBar(theFrame)
##        fileMenu = wx.Menu()
##        menubar.Append(fileMenu, '&File')
##        self.SetMenuBar(menubar)

##        self.Centre()
        self.Show()

        theRect = theDialog.Rect
        theClientArea = theDialog.ClientArea
        print('Dialog: Rect=%s; ClientArea=%s' % (str(theRect),
                                                  str(theClientArea)))

        #-------------------------------------------------------------------
        # End Dialog Relocation
        #-------------------------------------------------------------------

#--------------------------------------------------------------------------

if __name__ == '__main__':

    # Build Information (Top Level Executable Module)
    buildTitle     = __title__
    buildVersion   = __version__
    buildDate      = __date__
    buildAuthors   = __authors__
    buildCopyright = __copyright__

    # User Information (Command Line Interface)
    # TBD - May need to derive class from tsWxMultiFrameEnv
    # inorder to override cliAPP.getOptions.
    cliOptions = None # _Prototype.getOptions

    # Application Program Information (Graphical User Interface)
    guiTopLevelObjectId = wx.ID_ANY
    guiMessageRedirect = True
    guiMessageFilename = None
    guiTopLevelObject = _Prototype
    guiTopLevelObjectName = 'Prototype'
    guiTopLevelObjectTitle = 'Prototype_Feature'
 
    Instance =  wx.MultiFrameEnv(
        cliOptions=cliOptions,
        sourceTitle=buildTitle,
        sourceVersion=buildVersion,
        sourceDate=buildDate,
        sourceAuthors=buildAuthors,
        sourceCopyright=buildCopyright,
        # wrapperHeader=__header__,
        wrapperRedirect=guiMessageRedirect,
        wrapperFilename=guiMessageFilename,
        wrapperTopLevelObject=guiTopLevelObject,
        wrapperId=guiTopLevelObjectId,
        # wrapperMainTitleVersionDate=mainTitleVersionDate,
        wrapperName=guiTopLevelObjectName,
        wrapperTitle=guiTopLevelObjectTitle
        )
    Instance.Wrapper()

