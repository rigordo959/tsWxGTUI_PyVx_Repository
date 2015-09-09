#! /usr/bin/env python
# "Time-stamp: <04/08/2014  8:29:48 AM rsg>"
# File: buildManPagesToolsCLI.sh

python tsLinesOfCodeProjectMetrics.py -h > ./tsManPagesToolsCLI/tsLinesOfCodeProjectMetrics.man

python tsPlatformQuery.py -h > ./tsManPagesToolsCLI/tsPlatformQuery.man

python tsStripComments.py -h > ./tsManPagesToolsCLI/tsStripComments.man

python tsStripLineNumbers.py -h > ./tsManPagesToolsCLI/tsStripLineNumbers.man

python tsTreeCopy.py -h > ./tsManPagesToolsCLI/tsTreeCopy.man

python tsTreeTrimLines.py -h > ./tsManPagesToolsCLI/tsTreeTrimLines.man

