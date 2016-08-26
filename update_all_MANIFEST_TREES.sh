#!/usr/bin/bash
#"Time-stamp: <01/29/2016  9:22:50 AM rsg>"
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
pushd ./SourceDistributions
echo "# pushd to ./SourceDistributions"
    pushd ./Developer-Sandboxes
    echo "    # pushd to ./Developer-Sandboxes"
        pushd ./tsWxGTUI_PyVx
        echo "        # pushd to ./tsWxGTUI_PyVx"
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
        popd
        echo "        # popd from ./tsWxGTUI_PyVx"
    ./MANIFEST_TREE.sh
    popd
    echo "    # popd from ./Developer-Sandboxes"
    pushd ./Site-Packages
    echo "    # pushd to ./Site-Packages"
        pushd ./tsWxGTUI_PyVx
        echo "        # pushd to ./tsWxGTUI_PyVx"
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
        popd
        echo "        # popd from ./tsWxGTUI_PyVx"
    ./MANIFEST_TREE.sh
    popd
    echo "    #popd from ./Site-Packages"
popd
echo "# popd from ./SourceDistributions"
./MANIFEST_TREE.sh
