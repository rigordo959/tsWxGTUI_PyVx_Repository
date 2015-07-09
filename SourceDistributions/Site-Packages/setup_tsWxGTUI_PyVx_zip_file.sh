#!/usr/bin/bash
#"Time-stamp: <07/07/2015  7:21:12 PM rsg>"
#
# create an archive file (e.g., ZIP file onWindows) containing
# your setup script setup.py, and your module (tsPlatformQuery.py)
# or package (tsLibCLI).
#
# zip options archive inpath inpath .
# zip -r /path/to/tsWxGTUI_PyVx-0.0.0.zip /path/to/tsWxGTUI_PyVx
#
theDestination="dist"
theSource="tsWxGTUI_PyVx"
theVersion="0.0.0-Site-Package"
theExtension="zip"

rm -rf ../$theDestination
mkdir ./$theDestination
zip -r ./$theDestination/$theSource-$theVersion.$theExtension ./$theSource
