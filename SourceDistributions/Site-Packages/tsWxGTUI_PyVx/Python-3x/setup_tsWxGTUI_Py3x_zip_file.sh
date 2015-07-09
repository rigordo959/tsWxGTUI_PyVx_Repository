#!/usr/bin/bash
#"Time-stamp: <05/05/2015  1:44:01 PM rsg>"
#
# create an archive file (e.g., ZIP file onWindows) containing
# your setup script setup.py, and your module (tsPlatformQuery.py)
# or package (tsLibCLI).
#
# zip options archive inpath inpath .
# zip -r /path/to/tsWxGTUI_Py3x-0.0.0.zip /path/to/tsWxGTUI_Py3x
#
mkdir ./dist
zip -r ./dist/tsWxGTUI_Py3x-0.0.0.zip ./tsWxGTUI_Py3x
