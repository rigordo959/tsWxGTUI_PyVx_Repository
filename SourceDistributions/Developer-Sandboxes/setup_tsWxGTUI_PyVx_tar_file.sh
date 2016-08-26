#!/bin/bash
#"Time-stamp: <08/25/2016  8:13:44 AM rsg>"
#
# create an archive file (e.g., tarball on Linux, Mac OS X
# and  Unix) containing your setup script setup.py, and
# your modules (tsPlatformQuery.py) or packages (tsLibCLI).
#
# tar -zcf /path/to/file.tar.gz /path/to/directory
#
# theDestination="dist"
theSource="tsWxGTUI_PyVx"
theVersion="0.0.6-Dev-Sandbox"
theExtension="tar.gz"

# rm -rf ../$theDestination
# mkdir ./$theDestination
tar -zcf ./$theSource-$theVersion.$theExtension ./$theSource

