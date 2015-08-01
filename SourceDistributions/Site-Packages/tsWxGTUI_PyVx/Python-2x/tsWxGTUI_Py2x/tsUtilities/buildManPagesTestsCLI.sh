#! /usr/bin/env python
# "Time-stamp: <04/08/2014  8:27:36 AM rsg>"
# File: buildManPagesTestsCLI.sh

python test_tsApplication.py -h > ./tsManPagesTestsCLI/test_tsApplication.man

python test_tsCommandLineEnv.py -h > ./tsManPagesTestsCLI/test_tsCommandLineEnv.man

python test_tsDoubleLinkedList.py -h > ./tsManPagesTestsCLI/test_tsDoubleLinkedList.man

python test_tsOperatorSettingsParser.py -h > ./tsManPagesTestsCLI/test_tsOperatorSettingsParser.man

python test_tsPlatformRunTimeEnvironment.py -h > ./tsManPagesTestsCLI/test_tsPlatformRunTimeEnvironment.man

python test_tsSysCommand.py -h > ./tsManPagesTestsCLI/test_tsSysCommand.man
python tsCxGlobals.py -h > ./tsManPagesTestsCLI/tsCxGlobals.man

