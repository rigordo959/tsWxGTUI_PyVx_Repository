#!/bin/bash
#"Time-stamp: <08/25/2016  8:28:41 AM rsg>"
#
# PURPOSE
#
#    The announcement of the TeamSTARS "tsWxGTUI_PyVX" Toolkit
#    release is unusual in that the "GitHub" Repository contains
#    four related projects instead of the typical single project.
#
#    A Microsoft Word-based section and list numbering tool,
#    instead of a simple text editor is used to facilitate the
#    preparation of the announcement by re-using material from
#    other Word-based documents.
#
#    The announcement is then published, for the convenience of
#    its recipients, in the following portable document formats:
#
#       # Compatible with single-font, text-mode terminals
#       Plain Text
#
#       # Compatible with multi-font, graphics-mode terminals
#       Adobe PDF
#       Web Page HTML
#       Microsoft RTF
#
#    To avoid additional editing, the Plain Text is created by
#    dumping the Web Page HTML file using Lynx, a character-mode
#    Web Browser.
#
# USAGE
#
#    runLynx_Dump_Announcement.sh
#
#
## whichRepository="" # "./tsWxGTUI_PyVx_Repository"
## echo $whichRepository

whichDocuments="./Documents/Announcement"
## echo $whichDocuments

whichFile="Announcement"
## echo $whichFile

whichFileExtension="htm"
## echo $whichFileExtension

whichSource=$whichDocuments/$whichFile.$whichFileExtension
## echo $whichSource

whichTarget=$whichDocuments/$whichFile.txt
## echo $whichTarget

lynx -dump $whichSource > $whichTarget


