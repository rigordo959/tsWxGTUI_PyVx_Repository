#!/bin/bash
#"Time-stamp: <08/25/2016  8:14:24 AM rsg>"
#
# create an archive file (e.g., tarball on Linux, Mac OS X
# and  Unix) containing your setup script setup.py, and
# your modules (tsPlatformQuery.py) or packages (tsLibCLI).
#
# tar -zcf /path/to/file.tar.gz /path/to/directory
#
# theDestination="dist"
theSource="tsWxGTUI_Py2x"
theVersion="0.0.6"
theExtension="tar.gz"

# rm -rf ../$theDestination
# mkdir ../$theDestination
tar -zcf ../$theSource-$theVersion.$theExtension ./$theSource

