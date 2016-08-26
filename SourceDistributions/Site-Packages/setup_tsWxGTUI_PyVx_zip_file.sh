#!/bin/bash
#"Time-stamp: <08/25/2016  8:23:50 AM rsg>"
#
# create an archive file (e.g., ZIP file onWindows) containing
# your setup script setup.py, and your module (tsPlatformQuery.py)
# or package (tsLibCLI).
#
# zip options archive inpath inpath .
# zip -r /path/to/tsWxGTUI_PyVx-0.0.6.zip /path/to/tsWxGTUI_PyVx
#
# theDestination="dist"
theSource="tsWxGTUI_PyVx"
theVersion="0.0.6-Site-Package"
theExtension="zip"

# rm -rf ../$theDestination
# mkdir ./$theDestination
zip -r ./$theSource-$theVersion.$theExtension ./$theSource
