#! /usr/bin/bash
function quit {
    exit
}
function capture_help {
    python $1.py -h > $1.help
}
function capture_about {
    python $1.py -a > $1.about
}
function capture_version {
    python $1.py -v > $1.version
}
function capture_OperatorSettingsParser_Output {
    python $1.py -h > $1.help
    python $1.py -a > $1.about
    python $1.py -v > $1.version
    python $1.py > $1.stdout
    python $1.py 2> $1.stderr
}
capture_OperatorSettingsParser_Output test_tsApplication
capture_OperatorSettingsParser_Output test_tsCommandLineEnv
capture_OperatorSettingsParser_Output test_tsDoubleLinkedList
capture_OperatorSettingsParser_Output test_tsOperatorSettingsParser
capture_OperatorSettingsParser_Output test_tsPlatformRunTimeEnvironment
capture_OperatorSettingsParser_Output test_tsReportUtilities
capture_OperatorSettingsParser_Output test_tsSysCommand
capture_OperatorSettingsParser_Output tsLinesOfCodeProjectMetrics

# capture_help __init__
# capture_help run_tutorial
# capture_help test_tsCommandLineInterface
# capture_help test_tsCxGlobals
# capture_help test_tsExceptions
# capture_help test_tsLogger

# capture_help test_tsWxBoxSizer
# capture_help test_tsWxCheckBox
# capture_help test_tsWxDoubleLinkedList
# capture_help test_tsWxGlobals
# capture_help test_tsWxGraphicalTextUserInterface
# capture_help test_tsWxGridSizer
# capture_help test_tsWxMultiFrameEnv
# capture_help test_tsWxRSM
# capture_help test_tsWxScrolledWindow
# capture_help test_tsWxScrolledWindowDual
# capture_help test_tsWxSplashScreen
# capture_help test_tsWxWidgets
# capture_help tsCxGlobals
# capture_help tsLinesOfCodeProjectMetrics
# capture_help tsPlatformQuery
# capture_help tsStripComments
# capture_help tsStripLineNumbers
# capture_help tsTreeCopy
# capture_help tsTreeTrimLines
# capture_help Tutorial_CLI_0_hello_world_print_statement
# capture_help Tutorial_CLI_1_hello_world_print_function
# capture_help Tutorial_CLI_2_hello_world_script_environment
# capture_help Tutorial_CLI_3_hello_world_main_module_application
# capture_help Tutorial_CLI_4_Command_Line_PlatformQuery_Application
# capture_help Tutorial_GUI_0_Curses_LowLevel_WidgetApi_application
# capture_help Tutorial_GUI_1_wxPython_HighLevel_WidgetApi_application
# capture_help Tutorial_GUI_2_tsWxGTUI_HighLevel_BoxSizerApi_application
quit
