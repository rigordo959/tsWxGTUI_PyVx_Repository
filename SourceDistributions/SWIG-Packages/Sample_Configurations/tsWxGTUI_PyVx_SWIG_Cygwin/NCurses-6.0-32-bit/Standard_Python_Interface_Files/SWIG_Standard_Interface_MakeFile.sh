#!/usr/bin/bash
#"Time-stamp: <01/28/2017 10:25:46 AM rsg>"
#
# touch curses.i
# touch form.i
# touch menu.i
# touch ncurses_dll.i
# touch panel.i
# touch wrapper.i
#
swig -c++ -python curses.i
swig -c++ -python form.i
swig -c++ -python menu.i
# swig -c++ -python ncurses_dll.i
swig -c++ -python panel.i
# $ swig -c++ -python wrapper.i
