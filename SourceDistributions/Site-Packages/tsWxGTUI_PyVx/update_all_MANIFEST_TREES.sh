#!/usr/bin/bash
#"Time-stamp: <03/25/2016  5:43:44 AM rsg>"
#
############################################################
#
# Traverse all repository subdirectories and create a top-
# level and lower-level directory listings that contain a
# depth indented listing of component files.
#
# Each directory listing provides a transport document (man-
# ifest} that serves as a tally-sheet and record with the
# name and identifying attributes of each directory and file
# published in the Toolkit software release.
#
############################################################
#
pushd ./Python-2x
echo "            # pushd to ./Python-2x"
./MANIFEST_TREE.sh
popd
echo "            # popd from ./Python-2x"
pushd ./Python-3x
echo "            # pushd to ./Python-3x"
./MANIFEST_TREE.sh
popd
echo "            # popd from ./Python-3x"
./MANIFEST_TREE.sh
