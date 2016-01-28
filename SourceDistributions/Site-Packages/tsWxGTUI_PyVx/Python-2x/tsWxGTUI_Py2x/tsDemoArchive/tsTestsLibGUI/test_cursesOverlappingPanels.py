#! /usr/bin/env python
# "Time-stamp: <01/23/2015  3:44:53 AM rsg>"
#
# From:
#    http://stackoverflow.com/questions/21172087
#      /i-need-an-example-of-overlapping-curses-windows-using-panels-in-python
#
# Asked Jan 16 '14 at 20:22
#
#    By Mark Lakata
#
from time import sleep
import curses, curses.panel

def make_panel(h,l, y,x, str):
    win = curses.newwin(h,l, y,x)
    win.erase()
    win.box()
    win.addstr(2, 2, str)

    panel = curses.panel.new_panel(win)
    return win, panel

def test(stdscr):
    try:
        curses.curs_set(0)
    except:
        pass
    stdscr.box()
    stdscr.addstr(2, 2, "panels everywhere")
    win1, panel1 = make_panel(10,12, 5,5, "Panel 1")
    win2, panel2 = make_panel(10,12, 8,8, "Panel 2")
    curses.panel.update_panels(); stdscr.refresh()
    sleep(1)

    panel1.top(); curses.panel.update_panels(); stdscr.refresh()
    sleep(1)

    for i in range(20):
        panel2.move(8, 8+i)
        curses.panel.update_panels(); stdscr.refresh()
        sleep(0.1)

    sleep(1)

if __name__ == '__main__':
    curses.wrapper(test)
