#!/bin/bash
# "Time-stamp: <08/25/2016  8:27:07 AM rsg>"
#
# file: run_2to3_script.sh
#
# purpose:
#
#    convert operator specified file(s) from Python2.x to Python3.x style.
#    Apply all conversions except those invoked with "-x":
#
#        print - Assuming that files already use Python2.7 print method
#                instead of command line print statement, this option
#                prevents addition of superflous parantheses.
#
#        import - Assuming that files already use hierarchical file
#                 definitions, this option prevents addition of superflous
#                 superflous and inappropriate "dot notation".
#
# example usage:
#
#    cd /WR/SoftwareGadgetry-Dev/Python-2.x/tsLibraries/tsWxPkg/src
#    ./run_2to3_script.sh
#
# 2to3 -w -x print ./*.py
2to3 -w -x print -x import ./*.py
