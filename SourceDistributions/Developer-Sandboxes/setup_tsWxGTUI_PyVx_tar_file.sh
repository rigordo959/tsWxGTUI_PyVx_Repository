#!/usr/bin/bash
#"Time-stamp: <07/07/2015  7:21:42 PM rsg>"
#
# create an archive file (e.g., tarball on Linux, Mac OS X
# and  Unix) containing your setup script setup.py, and
# your modules (tsPlatformQuery.py) or packages (tsLibCLI).
#
# tar -zcf /path/to/file.tar.gz /path/to/directory
#
theDestination="dist"
theSource="tsWxGTUI_PyVx"
theVersion="0.0.0-Dev-Sandbox"
theExtension="tar.gz"

rm -rf ../$theDestination
mkdir ./$theDestination
tar -zcf ./$theDestination/$theSource-$theVersion.$theExtension ./$theSource

