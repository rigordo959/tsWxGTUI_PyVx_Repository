#!/usr/bin/bash
#"Time-stamp: <05/05/2015  1:43:44 PM rsg>"
#
# create an archive file (e.g., tarball on Linux, Mac OS X
# and  Unix) containing your setup script setup.py, and
# your modules (tsPlatformQuery.py) or packages (tsLibCLI).
#
# tar -zcf /path/to/file.tar.gz /path/to/directory
#
mkdir ./dist
tar -zcf ./dist/tsWxGTUI_Py3x-0.0.0.tar.gz ./tsWxGTUI_Py3x

