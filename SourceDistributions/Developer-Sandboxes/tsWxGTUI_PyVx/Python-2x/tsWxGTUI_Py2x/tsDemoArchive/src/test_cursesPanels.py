#! /usr/bin/env python
# "Time-stamp: <02/23/2015  5:20:15 AM rsg>"
#
# From:
#    http://stackoverflow.com/questions/22731034/strange-behaviour-with-curses-panels
#
# Asked Mar 29 '14 at 12:21 By:
#
#    Bede Kelly
#
import curses
import curses.panel

def main(stdscr):
    # Setup screen object
    curses.cbreak()  # No need for [Return]
    curses.noecho()  # Stop keys being printed
    curses.curs_set(0)  # Invisible cursor
    stdscr.keypad(True)
    stdscr.clear()
#               format: (lines, cols, y, x)
    window_one = curses.newwin(10, 20, 1, 1)
    window_two = curses.newwin(5, 20, 5, 40)

    # Make windows clearly visible
    window_one.addstr(2, 2, "Window One")
    window_one.border(0)

    window_two.addstr(2, 2, "Window Two")
    window_two.border(0)

    # Create panels
    panel_one = curses.panel.new_panel(window_one)
    panel_two = curses.panel.new_panel(window_two)

    # Both hidden by default
    display_one = False
    display_two = False

    while True:
        if display_one:
            window_one.refresh()
            panel_one.show()
        else:
            panel_one.hide()
        if display_two:
            window_two.refresh()
            panel_two.show()
        else:
            panel_two.hide()
        curses.panel.update_panels()

        stdscr.refresh()
        key = stdscr.getkey()
        if key == '1':
            display_one = not display_one
        elif key == '2':
            display_two = not display_two
        elif key == 'q':
            return

if __name__ == "__main__":
    curses.wrapper(main)

